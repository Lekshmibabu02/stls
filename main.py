from traffic_system import get_signal_action

def run_tests():
    test_cases = [
        # (currentSignal, isEmergencyVehicleApproaching, expectedOutput)
        ("RED", True, "IMMEDIATE GREEN"),
        ("YELLOW", True, "IMMEDIATE GREEN"),
        ("GREEN", True, "IMMEDIATE GREEN"),
        ("RED", False, "STOP"),
        ("YELLOW", False, "PREPARE TO STOP"),
        ("GREEN", False, "GO"),
        ("BLUE", False, "INVALID SIGNAL"),
        ("red", False, "STOP"), # Testing case insensitivity
    ]

    print(f"{'Input Signal':<15} | {'Emergency':<10} | {'Expected':<18} | {'Actual':<18} | {'Result'}")
    print("-" * 80)

    for sig, em, expected in test_cases:
        actual = get_signal_action(sig, em)
        result = "PASS" if actual == expected else "FAIL"
        print(f"{sig:<15} | {str(em):<10} | {expected:<18} | {actual:<18} | {result}")

if __name__ == "__main__":
    run_tests()
