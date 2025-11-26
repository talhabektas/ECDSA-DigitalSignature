
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

def generate_key_pair(curve_name):
    """
    Generates an ECDSA key pair for the specified curve.
    Supported curves: 'P-256', 'P-384', 'secp256k1'
    """
    if curve_name == 'P-256':
        curve = ec.SECP256R1()
    elif curve_name == 'P-384':
        curve = ec.SECP384R1()
    elif curve_name == 'secp256k1':
        curve = ec.SECP256K1()
    else:
        raise ValueError("Unsupported curve")

    private_key = ec.generate_private_key(curve)
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem

def sign_file(private_key_pem, data):
    """
    Signs data using the provided private key PEM.
    Returns the signature.
    """
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=None
    )

    signature = private_key.sign(
        data,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key_pem, data, signature):
    """
    Verifies the signature of the data using the public key PEM.
    Returns True if valid, False otherwise.
    """
    try:
        public_key = serialization.load_pem_public_key(public_key_pem)
        public_key.verify(
            signature,
            data,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False
    except Exception as e:
        print(f"Verification error: {e}")
        return False
