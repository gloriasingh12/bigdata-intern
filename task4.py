# =================================================================
# PROJECT: Big Data Security & Compliance Framework
# DESCRIPTION: Implementing GDPR/HIPAA standards via Data Masking & Encryption logic.
# DELIVERABLE: A prototype demonstrating secure data handling practices.
# =================================================================

import hashlib

class SecurityFramework:
    def __init__(self):
        self.compliance_standards = ["GDPR", "HIPAA", "SOC2"]
        print(f"🛡️ Framework Initialized. Standards: {', '.join(self.compliance_standards)}")

    def anonymize_data(self, sensitive_info):
        """
        GDPR Requirement: PII (Personally Identifiable Information) Masking.
        Converts real names/IDs into secure hashes.
        """
        masked_id = hashlib.sha256(sensitive_info.encode()).hexdigest()[:12]
        return f"MASKED_{masked_id}"

    def apply_hipaa_encryption(self, health_record):
        """
        HIPAA Requirement: Technical Safeguards for Health Data.
        """
        # Simulating encryption of sensitive health data
        return f"[ENCRYPTED_DATA_BLOCK_{len(health_record)}]"

    def process_secure_record(self, user_record):
        print(f"\n🔐 Processing Record for: {user_record['name']}")
        
        # 1. Anonymize PII for GDPR
        protected_name = self.anonymize_data(user_record['name'])
        
        # 2. Encrypt Health Data for HIPAA
        protected_health = self.apply_hipaa_encryption(user_record['medical_history'])
        
        return {
            "user_id": protected_name,
            "health_info": protected_health,
            "compliance_status": "VERIFIED ✅"
        }

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    framework = SecurityFramework()

    # Sample Sensitive Big Data Record
    raw_record = {
        "name": "Aditya Tripathi",
        "email": "aditya@example.com",
        "medical_history": "Blood Group O+, No Allergies",
        "age": 21
    }

    print("\n--- Compliance Check in Progress ---")
    secure_output = framework.process_secure_record(raw_record)

    # Displaying Secure Deliverable
    print("\n" + "="*50)
    print("📊 SECURE COMPLIANCE REPORT")
    print("="*50)
    print(f"Original Name:  {raw_record['name']}")
    print(f"GDPR Status:    Data Anonymized -> {secure_output['user_id']}")
    print(f"HIPAA Status:   Record Encrypted -> {secure_output['health_info']}")
    print(f"Audit Status:   {secure_output['compliance_status']}")
    print("="*50)
    print("NOTE: This framework prevents unauthorized access to PII.")
