def get_signal_action(current_signal: str, is_emergency_vehicle_approaching: bool) -> str:
    """
    Determines the traffic signal action based on current signal and emergency status.
    
    Args:
        current_signal (str): The current color of the signal ("RED", "YELLOW", "GREEN").
        is_emergency_vehicle_approaching (bool): True if an emergency vehicle is near.
        
    Returns:
        str: The required action.
    """
    # Rule 1 — Emergency Check (highest priority)
    # The emergency check runs first — it overrides the switch entirely
    if is_emergency_vehicle_approaching:
        return "IMMEDIATE GREEN"

    # Rule 2 — Switch Statement (when no emergency)
    # Normalize input to handle case-sensitivity if needed, though prompt implies specific strings.
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

if __name__ == "__main__":
    # Example usage
    print(f"Emergency Approaching: {get_signal_action('RED', True)}")
    print(f"Red Signal: {get_signal_action('RED', False)}")
    print(f"Invalid Signal: {get_signal_action('PURPLE', False)}")
