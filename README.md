# Secure Authentication Methods in AWS

This project explores and compares three secure authentication methods in Amazon Web Services (AWS): IAM-based authentication, X.509 certificate-based authentication, and custom JWT token-based authentication.

📄 **Lab Report:** [View Full Report (PDF)](https://drive.google.com/file/d/1KORBOyd1nCVQ2Mc6WQEyNP7lz-IlQO5W/view?usp=sharing)

📎 **Course:** Cyber Security Labs I  
🎓 **University:** Eötvös Loránd University  
👨‍🏫 **Supervisor:** Dr. Mohammed Alshawki  
🧑‍🎓 **Author:** Fuad Suleymanov

---

## 🔍 Project Overview

This lab focuses on implementing and evaluating secure authentication mechanisms in AWS by simulating real-world device-to-cloud communication using AWS IoT Core and Lambda.

The main goals are to:

- Implement three types of AWS-native authentication
- Compare security properties (e.g., resistance to replay attacks, impersonation)
- Measure average authentication latency and resource usage
- Recommend the most suitable method for different use cases

---

## 🔐 Authentication Methods Implemented

### 1. IAM-Based Authentication (STS)
- Uses IAM roles and AWS STS to grant temporary credentials
- Ideal for internal AWS services and trusted devices

### 2. X.509 Certificate-Based Authentication
- Uses device certificates for mutual TLS (mTLS)
- Suitable for device-to-cloud secure connections

### 3. Custom Token-Based Authentication (JWT)
- Generates JWTs and validates them via a Lambda authorizer
- Flexible, lightweight method for API-based access

---

## 📊 Performance & Security Comparison

| Criteria                  | IAM-Based       | X.509 Cert-Based | JWT-Based        |
|--------------------------|------------------|------------------|------------------|
| Avg. Latency             | 0.8–1.0s         | 1.5–2.0s         | 0.5–0.8s         |
| Credential Lifespan      | Short (STS)      | Long (revocable) | Short (configurable) |
| Complexity               | Moderate         | High             | Low to Moderate  |
| Replay Protection        | High             | High             | Medium           |

---

## ⚙️ Tools & Technologies

- **AWS Services:** IAM, IoT Core, STS, Lambda, API Gateway
- **Languages:** Python (Boto3, PyJWT)
- **Testing Tools:** MQTT.fx, Postman, requests

## 📫 Contact

If you have questions or feedback, feel free to reach out via LinkedIn or open an issue.

---

⭐️ If you find this project helpful or interesting, feel free to star the repo!
