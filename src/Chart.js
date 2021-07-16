import React, { Component } from 'react';
import { Bar, Line, Pie } from 'react-chartjs-2';
import './Chart.css';

class Chart extends Component{

    constructor(props){
        super(props);
        this.state = {
            chartData :{
                labels: ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford'],
                datasets: [{
                    label:'Population',
                    data: [617594, 181045, 453060, 106519, 235162, 595072],
                    backgroundColor: [
                        'rgba(255,99,132,0.6)',
                        'rgba(54,162,235,0.6)',
                        'rgba(255,206,86,0.6)',
                        'rgba(153,102,192,0.6)',
                        'rgba(48,159,255,0.6)',
                        'rgba(135,99,64,0.6)'
                    ]
                }],
            }
        };
    }

    render(){
        return(
            <div className="chart">
                Chart !
                <Bar
                    data={this.state.chartData}
                    options={{ title:{
                        display:true,
                        text:'Largest Cities in Massachusetts',
                        fontSize:25
                        },
                        legend:{display:true, position:'right'} 
                    }}
                />
            </div>
        );
    }
}

export default Chart;