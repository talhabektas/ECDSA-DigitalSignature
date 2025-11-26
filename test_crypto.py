
import crypto_utils
import os

def test_workflow():
    print("Testing ECDSA Workflow...")
    
    # 1. Generate Keys
    print("1. Generating Keys (P-256)...")
    private_pem, public_pem = crypto_utils.generate_key_pair("P-256")
    assert private_pem is not None
    assert public_pem is not None
    print("   Keys generated successfully.")
    
    # 2. Sign File
    print("2. Signing Data...")
    data = b"Hello, World!"
    signature = crypto_utils.sign_file(private_pem, data)
    assert signature is not None
    print("   Data signed successfully.")
    
    # 3. Verify Signature
    print("3. Verifying Signature...")
    is_valid = crypto_utils.verify_signature(public_key_pem=public_pem, data=data, signature=signature)
    assert is_valid is True
    print("   Signature verified successfully (Valid Case).")
    
    # 4. Verify Invalid Signature
    print("4. Verifying Invalid Signature...")
    is_valid_invalid = crypto_utils.verify_signature(public_key_pem=public_pem, data=b"Wrong Data", signature=signature)
    assert is_valid_invalid is False
    print("   Signature verified successfully (Invalid Case).")
    
    print("\nAll tests passed!")

if __name__ == "__main__":
    test_workflow()
