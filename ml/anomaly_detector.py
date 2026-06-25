import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SentinelAI")

class NetworkAnomalyDetector:
    def __init__(self):
        # Unsupervised Isolation Forest model
        # contamination=0.1 assumes 10% of baseline traffic might be anomalous
        self.model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
        self.is_trained = False

    def train_baseline(self, normal_traffic_data):
        """
        Train the model on 'normal' network traffic features.
        Features expected: [packet_size, duration_ms, protocol_flag, packet_count]
        """
        logger.info("Training Isolation Forest on baseline network traffic...")
        self.model.fit(normal_traffic_data)
        self.is_trained = True
        logger.info("Training complete. Model ready for zero-day anomaly detection.")

    def analyze_traffic(self, traffic_features):
        """
        Analyze incoming network flow. 
        Returns True if anomaly (attack) detected, False if normal.
        """
        if not self.is_trained:
            raise RuntimeError("Model must be trained before analyzing traffic.")
        
        # Predict: 1 for normal, -1 for anomaly
        prediction = self.model.predict([traffic_features])
        is_anomaly = (prediction[0] == -1)
        
        if is_anomaly:
            logger.warning(f"[ALERT] Network Anomaly Detected! Features: {traffic_features}")
        return is_anomaly

# --- Demo / Execution Block ---
if __name__ == "__main__":
    detector = NetworkAnomalyDetector()
    
    # 1. Generate mock "normal" baseline traffic (e.g., standard HTTP browsing)
    # Features: [packet_size, duration_ms, protocol_flag, packet_count]
    normal_traffic = np.random.normal(loc=[500, 100, 1, 10], scale=[100, 20, 0.5, 2], size=(200, 4))
    
    # 2. Train the AI
    detector.train_baseline(normal_traffic)
    
    # 3. Test with normal traffic
    normal_test = [510, 105, 1, 12] 
    print(f"Normal traffic test -> Anomaly? {detector.analyze_traffic(normal_test)}")
    
    # 4. Test with anomalous traffic (e.g., DDoS spike or Port Scan)
    attack_test = [5000, 5, 6, 5000] # Massive size, tiny duration, weird protocol, huge count
    print(f"Attack traffic test -> Anomaly? {detector.analyze_traffic(attack_test)}")