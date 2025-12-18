
import streamlit as st
import crypto_utils
import base64

st.set_page_config(page_title="ECDSA Tool", layout="wide")

st.title("ECDSA Digital Signature Tool")

menu = ["Key Generation", "Sign File", "Verify Signature"]
choice = st.sidebar.selectbox("Select Activity", menu)

if choice == "Key Generation":
    st.header("Generate ECDSA Key Pair")
    curve_name = st.selectbox("Select Curve", ["P-256", "P-384", "secp256k1"])
    
    if st.button("Generate Keys"):
        try:
            private_pem, public_pem = crypto_utils.generate_key_pair(curve_name)
            st.session_state['private_pem'] = private_pem
            st.session_state['public_pem'] = public_pem
            st.success("Keys Generated Successfully!")
        except Exception as e:
            st.error(f"Error generating keys: {e}")

    if 'private_pem' in st.session_state and 'public_pem' in st.session_state:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Private Key")
            st.code(st.session_state['private_pem'].decode(), language='text')
            st.download_button(
                label="Download Private Key",
                data=st.session_state['private_pem'],
                file_name="private_key.pem",
                mime="application/x-pem-file"
            )
        
        with c2:
            st.subheader("Public Key")
            st.code(st.session_state['public_pem'].decode(), language='text')
            st.download_button(
                label="Download Public Key",
                data=st.session_state['public_pem'],
                file_name="public_key.pem",
                mime="application/x-pem-file"
            )

elif choice == "Sign File":
    st.header("Sign File")
    
    uploaded_file = st.file_uploader("Upload File to Sign", type=None)
    private_key_file = st.file_uploader("Upload Private Key (PEM)", type=['pem'])
    
    if uploaded_file and private_key_file:
        file_bytes = uploaded_file.read()
        private_key_pem = private_key_file.read()
        
        if st.button("Sign File"):
            try:
                signature = crypto_utils.sign_file(private_key_pem, file_bytes)
                st.success("File Signed Successfully!")
                
                st.subheader("Signature (Hex)")
                st.code(signature.hex(), language='text')
                
                st.download_button(
                    label="Download Signature",
                    data=signature,
                    file_name=f"{uploaded_file.name}.sig",
                    mime="application/octet-stream"
                )
            except Exception as e:
                st.error(f"Error signing file: {e}")

elif choice == "Verify Signature":
    st.header("Verify Signature")
    
    uploaded_file = st.file_uploader("Upload Original File", type=None)
    public_key_file = st.file_uploader("Upload Public Key (PEM)", type=['pem'])
    signature_file = st.file_uploader("Upload Signature File (.sig)", type=['sig'])
    
    if uploaded_file and public_key_file and signature_file:
        file_bytes = uploaded_file.read()
        public_key_pem = public_key_file.read()
        signature = signature_file.read()
        
        if st.button("Verify Signature"):
            is_valid = crypto_utils.verify_signature(public_key_pem, file_bytes, signature)
            
            if is_valid:
                st.success("Signature is VALID! ✅")
            else:
                st.error("Signature is INVALID! ❌")
