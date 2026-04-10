import requests

API_URL = "http://127.0.0.1:5000/scan"

def run_pipeline(payload):
    print("\n🚀 Starting CI/CD Pipeline...")
    print(f"📦 Input Payload: {payload}")

    try:
        response = requests.post(API_URL, json={"payload": payload})

        if response.status_code != 200:
            print("❌ API Error:", response.text)
            return

        result = response.json()

        threat_score = result["threat_score"]
        decision = result["decision"]

        print(f"🔍 Threat Score: {threat_score}")
        print(f"⚖️ Decision: {decision}")

        if decision == "BLOCKED":
            print("🚫 Deployment BLOCKED due to security risk!")
        else:
            print("✅ Deployment ALLOWED. Proceeding...")

    except Exception as e:
        print("❌ Pipeline failed:", str(e))


# ----------- RUN -----------

if __name__ == "__main__":
    run_pipeline("User login successful")
    run_pipeline("' OR 1=1 --")