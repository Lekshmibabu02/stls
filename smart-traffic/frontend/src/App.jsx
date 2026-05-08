import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { ShieldAlert, Info, Activity } from 'lucide-react';

const API_URL = 'http://localhost:8000/api/traffic/calculate-action/';

function App() {
  const [currentSignal, setCurrentSignal] = useState('RED');
  const [isEmergency, setIsEmergency] = useState(false);
  const [action, setAction] = useState('STOP');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchAction();
  }, [currentSignal, isEmergency]);

  const fetchAction = async () => {
    setLoading(true);
    try {
      const response = await axios.post(API_URL, {
        currentSignal: currentSignal,
        isEmergencyVehicleApproaching: isEmergency
      });
      setAction(response.data.action);
    } catch (error) {
      console.error('Error fetching action:', error);
      setAction('ERROR');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Smart Traffic</h1>
      <p className="subtitle">Real-time signal management system</p>

      <div className={`traffic-light-container ${isEmergency ? 'emergency-pulse' : ''}`}>
        <div 
          className={`light red ${currentSignal === 'RED' ? 'active' : ''}`}
          onClick={() => setCurrentSignal('RED')}
        ></div>
        <div 
          className={`light yellow ${currentSignal === 'YELLOW' ? 'active' : ''}`}
          onClick={() => setCurrentSignal('YELLOW')}
        ></div>
        <div 
          className={`light green ${currentSignal === 'GREEN' ? 'active' : ''}`}
          onClick={() => setCurrentSignal('GREEN')}
        ></div>
      </div>

      <div className="controls">
        <div className="toggle-container">
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <ShieldAlert size={20} color={isEmergency ? "#ef4444" : "#94a3b8"} />
            <div>
              <div style={{ fontWeight: 600 }}>Emergency Vehicle</div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Overrides all logic</div>
            </div>
          </div>
          <div 
            className={`toggle ${isEmergency ? 'active' : ''}`}
            onClick={() => setIsEmergency(!isEmergency)}
          >
            <div className="toggle-circle"></div>
          </div>
        </div>

        <div className="result-card">
          <span className="result-label">Recommended Action</span>
          <div className="result-value">
            {loading ? 'Calculating...' : action}
          </div>
        </div>
      </div>

      <div style={{ marginTop: '2rem', display: 'flex', gap: '0.5rem', color: '#94a3b8', fontSize: '0.8rem', justifyContent: 'center', alignItems: 'center' }}>
        <Info size={14} />
        Click signal lights to change manual state
      </div>
    </div>
  );
}

export default App;
