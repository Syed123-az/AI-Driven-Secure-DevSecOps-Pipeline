from flask import Blueprint, request, jsonify
from model_loader import load_model
from feature_extractor import extract_features

main = Blueprint("main", __name__)

model = load_model()


@main.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "service": "AI DevSecOps Pipeline"
    })


@main.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()

    if not data or "payload" not in data:
        return jsonify({"error": "Payload required"}), 400

    payload = data["payload"]

    features = extract_features(payload)

    threat_score = float(model.predict_proba(features)[0][1])

    decision = "BLOCKED" if threat_score > 0.7 else "ALLOWED"

    return jsonify({
        "payload": payload,
        "threat_score": round(threat_score, 3),
        "decision": decision
    })