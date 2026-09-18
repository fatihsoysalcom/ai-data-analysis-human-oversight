import statistics

def analyze_data(data_points: list) -> dict:
    """
    Simulates an AI system accessing and analyzing 'evidence' (data points).
    Identifies a simple trend or anomaly.
    """
    if not data_points:
        return {"status": "error", "message": "No data points to analyze."}

    # AI's access to evidence: Process the raw data (as discussed in the article)
    avg = statistics.mean(data_points)
    last_value = data_points[-1]
    
    # Simple anomaly detection: Is the last value significantly different from the average?
    deviation_threshold = avg * 0.10 # 10% deviation
    
    if abs(last_value - avg) > deviation_threshold:
        trend_message = f"Significant deviation detected! Last value ({last_value:.2f}) is far from average ({avg:.2f})."
        is_significant = True
    else:
        trend_message = f"Data stable. Last value ({last_value:.2f}) is close to average ({avg:.2f})."
        is_significant = False

    return {
        "status": "success",
        "average": avg,
        "last_value": last_value,
        "is_significant": is_significant,
        "analysis_message": trend_message
    }

def human_review_and_publish(ai_analysis: dict, human_override: bool = False) -> None:
    """
    Simulates human oversight and publishing authority.
    Decides whether to 'publish' (act on) the AI's findings.
    """
    print("\n--- Human Review Process ---")
    print("AI Analysis Report:")
    for key, value in ai_analysis.items():
        print(f"  {key.replace('_', ' ').capitalize()}: {value}")

    # Human decision logic based on AI's findings (illustrates 'Yayın Yetkisi' - Publishing Authority)
    if ai_analysis.get("is_significant"):
        print("\nAI suggests a significant event. Human review required for publication.")
        if human_override:
            print("Human override: Publishing the alert despite AI's internal rules.")
            print(f"ACTION: Publishing Alert - {ai_analysis['analysis_message']}")
        else:
            # This is where human judgment comes in. A stricter human rule for actual publication.
            if ai_analysis['last_value'] > ai_analysis['average'] * 1.2: # More strict condition (20% deviation) for publishing
                print("Human confirms: Deviation is critical. Publishing alert.")
                print(f"ACTION: Publishing Critical Alert - {ai_analysis['analysis_message']}")
            else:
                print("Human review: Deviation noted, but not critical enough for immediate publication. Monitoring.")
                print("ACTION: No immediate publication.")
    else:
        print("\nAI indicates stable data. No immediate action required.")
        print("ACTION: No publication needed.")

# --- Main execution ---
if __name__ == "__main__":
    # Example 1: Stable data
    print("--- Scenario 1: Stable Data ---")
    sensor_data_stable = [10.1, 10.2, 9.9, 10.3, 10.0, 10.1]
    print(f"Raw Data (Evidence): {sensor_data_stable}")
    
    # AI accesses evidence and performs analysis
    ai_result_stable = analyze_data(sensor_data_stable)
    
    # Human reviews AI's analysis and decides on publishing
    human_review_and_publish(ai_result_stable)

    print("\n" + "="*50 + "\n")

    # Example 2: Data with a significant deviation
    print("--- Scenario 2: Significant Deviation ---")
    sensor_data_deviation = [10.1, 10.2, 9.9, 10.3, 10.0, 15.5] # Last value is high
    print(f"Raw Data (Evidence): {sensor_data_deviation}")

    # AI accesses evidence and performs analysis
    ai_result_deviation = analyze_data(sensor_data_deviation)

    # Human reviews AI's analysis and decides on publishing
    human_review_and_publish(ai_result_deviation)

    print("\n" + "="*50 + "\n")

    # Example 3: Data with a deviation, but human decides not to publish (simulated discretion)
    print("--- Scenario 3: Deviation with Human Discretion (No Publish) ---")
    sensor_data_mild_deviation = [10.1, 10.2, 9.9, 10.3, 10.0, 11.5] # Mild deviation
    print(f"Raw Data (Evidence): {sensor_data_mild_deviation}")

    # AI accesses evidence and performs analysis
    ai_result_mild_deviation = analyze_data(sensor_data_mild_deviation)

    # Human reviews AI's analysis and decides on publishing
    # In this scenario, the AI flags it as significant (10% deviation),
    # but the human's stricter rule (20% deviation) prevents automatic publication.
    human_review_and_publish(ai_result_mild_deviation)

    print("\n" + "="*50 + "\n")
    
    # Example 4: Data with a deviation, human overrides to publish
    print("--- Scenario 4: Deviation with Human Override to Publish ---")
    sensor_data_override = [10.1, 10.2, 9.9, 10.3, 10.0, 11.5] # Mild deviation
    print(f"Raw Data (Evidence): {sensor_data_override}")

    # AI accesses evidence and performs analysis
    ai_result_override = analyze_data(sensor_data_override)

    # Human reviews AI's analysis and decides on publishing, with an explicit override
    # This simulates a human making a judgment call even if their internal rules
    # might not trigger an automatic publish, emphasizing human authority.
    human_review_and_publish(ai_result_override, human_override=True)