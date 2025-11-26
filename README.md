# ECDSA Digital Signature Tool

A secure and user-friendly tool for generating ECDSA key pairs, signing files, and verifying digital signatures. Built with Python and Streamlit.

## Features

-   **Key Pair Generation**: Generate secure ECDSA key pairs using industry-standard curves:
    -   `P-256` (NIST P-256)
    -   `P-384` (NIST P-384)
    -   `secp256k1` (Bitcoin curve)
-   **File Signing**: Digitally sign any file format using your private key.
-   **Signature Verification**: Verify the authenticity and integrity of files using the corresponding public key.
-   **User-Friendly Interface**: Simple and intuitive web-based GUI powered by Streamlit.
-   **Secure**: Built on top of the robust `cryptography` Python library.

## Installation

1.  **Clone the repository** (or download the source code):
    ```bash
    git clone <https://github.com/talhabektas/ECDSA-DigitalSignature.git>
    cd <cryptology>
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install streamlit cryptography
    ```


## Usage

1.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

2.  **Navigate the Tool**:
    -   **Key Generation**: Select a curve and generate a new public/private key pair. Download the keys as PEM files.
    -   **Sign File**: Upload a file and your private key to generate a digital signature.
    -   **Verify Signature**: Upload the original file, the public key, and the signature to verify if the file has been tampered with.

## Technologies Used

-   **Python 3.x**
-   **Streamlit**: For the frontend interface.
-   **Cryptography**: For ECDSA implementation and secure key management.

## License

This project is open-source and available under the MIT License.
