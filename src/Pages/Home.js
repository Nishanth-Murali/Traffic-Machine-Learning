import React, { Component } from 'react';
import {  Pie, Radar, Doughnut, Bubble, Scatter, Area  } from 'react-chartjs-2';
import './BarChart.css';
import data from './vol241.json';

class Home extends Component{

    constructor(props){
        super(props);
        this.state = {
            chartData :{
                // labels: data.map(item => {
                //     let date = new Date(item.Datetime * 1000);
                //     var hours = date.toUTCString();
                //     return   hours.slice(-12, -4);
                // }), // ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford'],
                labels : ['Light'],
                datasets: [
                    {
                        label:'Light',
                        data: data.map(item => item.Light),//[617594, 181045, 453060, 106519, 235162, 595072],
                        backgroundColor : 'rgba(255,206,86,0.6)'
                    },
                    {
                        label:'Bus',
                        data: data.map(item => item.Bus),
                        backgroundColor : 'rgba(153,102,192,0.6)'
                    },
                    {
                        label:'Single Unit Truck',
                        data: data.map(item => item["Single Unit Truck"]),
                        backgroundColor : 'rgba(48,159,255,0.6)'
                    },
                    {
                        label:'Articulated Truck',
                        data: data.map(item => item["Articulated Truck"]),
                        backgroundColor : 'rgba(54,162,22,0.6)'
                    },
                    {
                        label:'Motorized Vehicle',
                        data: data.map(item => item["Motorized Vehicle"]),
                        backgroundColor : 'rgba(230,100,100,0.6)'
                    },
                    {
                        label:'Bicycle',
                        data: data.map(item => item.Bicycle),
                        backgroundColor : 'rgba(54,62,221,0.6)'
                    }
                ],
            }
        };
    }

    render(){
        return(
            <div className="chart">
                <Doughnut 
                    data={this.state.chartData}
                    options={{ title:{
                        display:true,
                        text:'Vehicle count Data for 24 hours',
                        fontSize:25
                        },
                        legend:{display:true, position:'right'} 
                    }}
                />
            </div>
        );
    }
}

export default Home;