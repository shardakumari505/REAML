import React, { useEffect, useState } from 'react';
import Plot from 'react-plotly.js';
import axios from 'axios';
import './dashboard.styles.scss'

const Dashboard = () => {
    const [plotData, setPlotData] = useState(null);

    useEffect(() => {
        // Fetch plot data from the Flask API endpoint
        axios.get('http://127.0.0.1:5000/api/get_plot_data')
            .then(response => setPlotData(JSON.parse(response.data)))  // Parse the JSON string
            .catch(error => console.error(error));
    }, []);

    return (
        <div className='dashboard-container'>
            <div className='dashboard-top'>
                {plotData && <Plot data={plotData.data} layout={plotData.layout} />}  {/* Use data and layout properties */}
            </div>
        </div>
    );
};

export default Dashboard;
