from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TrafficSignalActionView(APIView):
    """
    API endpoint that takes currentSignal and isEmergencyVehicleApproaching
    and returns the appropriate traffic action.
    """
    def post(self, request):
        current_signal = request.data.get('currentSignal')
        is_emergency = request.data.get('isEmergencyVehicleApproaching')

        if current_signal is None or is_emergency is None:
            return Response(
                {"error": "Both 'currentSignal' and 'isEmergencyVehicleApproaching' are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Implementation of the core logic
        if is_emergency:
            action = "IMMEDIATE GREEN"
        else:
            match current_signal.upper():
                case "RED":
                    action = "STOP"
                case "YELLOW":
                    action = "PREPARE TO STOP"
                case "GREEN":
                    action = "GO"
                case _:
                    action = "INVALID SIGNAL"

        return Response({"action": action}, status=status.HTTP_200_OK)
