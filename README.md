# Task 3 – Secure File Upload/Download Portal with AES Encryption

##  Overview
This project was completed as part of my **Cybersecurity Internship with Future Interns**.  
The goal was to build a **secure file sharing web application** where files are **encrypted at rest and decrypted upon download** using the AES algorithm.

This simulates real-world systems where data confidentiality is critical, such as in healthcare, legal, and corporate environments.

---

##  Objectives
- Develop a Flask-based web portal for file uploads and downloads
- Encrypt uploaded files using **AES (CBC mode)** before saving
- Decrypt files on download to restore the original
- Implement basic key management
- Document security architecture and testing

---

##  Tools & Technologies
- **Backend Framework:** Python Flask
- **Encryption Library:** PyCryptodome (AES)
- **Frontend:** HTML forms (Upload/Download UI)
- **Version Control:** Git & GitHub

---

##  Security Architecture
| Component           | Implementation Details                                                                 |
|---------------------|----------------------------------------------------------------------------------------|
| **Encryption**      | AES-128 CBC mode with PKCS7 padding                                                    |
| **Key Handling**    | Session-based key generation using `get_random_bytes(16)` (demo setup)                 |
| **IV Handling**     | Random IV generated per encryption and stored with ciphertext                          |
| **Storage**         | Encrypted files stored in `/encrypted` directory with `.enc` extension                 |
| **Transport**       | HTTPS support possible via Flask SSL or reverse proxy                                  |
| **File Validation** | Basic filename checks; recommend adding type/size validation in production             |

---

## Deliverables
- **`app.py`** – Flask server with upload/download AES encryption logic
- **`uploads/`** – Folder for decrypted files
- **`encrypted/`** – Folder for encrypted files
- **`templates/`** – HTML upload/download interface
- **`README.md`** – Documentation
- **`security_overview.pdf`** – Security design summary
- **Screenshots** – Web UI and encryption flow examples

---

## How to Run the Project
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/task3-secure-file-portal.git
   cd task3-secure-file-portal
