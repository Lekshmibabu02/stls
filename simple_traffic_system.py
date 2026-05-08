def get_traffic_action(current_signal, is_emergency):
    """
    Core Logic for Smart Traffic System.
    Returns the action based on signal color and emergency status.
    """
    # 1. High Priority Check: Emergency Vehicle always gets IMMEDIATE GREEN
    if is_emergency:
        return "IMMEDIATE GREEN"

    # 2. Normal Logic: Use a mapping (like a switch statement) for signal states
    # Note: .upper() makes the check case-insensitive (e.g., "red" or "RED" both work)
    match current_signal.upper():
        case "RED":
            return "STOP"
        case "YELLOW":
            return "PREPARE TO STOP"
        case "GREEN":
            return "GO"
        case _:
            # Default case for unrecognized signals
            return "INVALID SIGNAL"

# --- Demonstration / Testing ---
if __name__ == "__main__":
    print("--- Smart Traffic System Output ---")
    
    # Test Scenario 1: Emergency Vehicle Approaching (Priority 1)
    print(f"Emergency at Red:    {get_traffic_action('RED', True)}")
    
    # Test Scenario 2: Normal Traffic (Priority 2)
    print(f"Normal Red Signal:   {get_traffic_action('RED', False)}")
    print(f"Normal Yellow:       {get_traffic_action('YELLOW', False)}")
    print(f"Normal Green:        {get_traffic_action('GREEN', False)}")
    
    # Test Scenario 3: Invalid Input (Default Case)
    print(f"Unknown Signal:      {get_traffic_action('BLUE', False)}")
