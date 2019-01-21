function createChart1(ctx, type, questionData, answersData, options = {}) {
    new Chart(ctx, {
        "type": type,
        "data": {
            "labels": questionData.labels,
            "datasets": [getChartData(questionData, answersData)]
        },
        "options": options
    });
}

function getChartData(questionData, answersData) {
    return {
        "label": questionData.question,
        "data": answersData,
        "fill": false,
        "backgroundColor": ["rgba(255, 99, 132, 0.2)", "rgba(255, 159, 64, 0.2)", "rgba(255, 205, 86, 0.2)", "rgba(75, 192, 192, 0.2)", "rgba(54, 162, 235, 0.2)", "rgba(153, 102, 255, 0.2)", "rgba(201, 203, 207, 0.2)"],
        "borderColor": ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)", "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)", "rgb(201, 203, 207)"],
        "borderWidth": 1
    }
}

function createChart(ctx, questionData) {
    if (questionData.type === "Single Choice") {
        const options = {
            "legend": {
                "position": "right"
            },
            "tooltips": {
                "callbacks": {
                    "label": function (tooltipItem, data) {
                        const dataset = data.datasets[tooltipItem.datasetIndex];
                        const total = dataset.data.reduce((previousValue, currentValue) => previousValue + currentValue);
                        const currentValue = dataset.data[tooltipItem.index];
                        const percentage = Math.floor(((currentValue / total) * 100) + 0.5);
                        return currentValue + " (" + percentage + "%)";
                    }
                }
            }
        };
        const answersData = Object.values(questionData.answers);
        createChart1(ctx, "pie", questionData, answersData, options);
    }
    else if (questionData.type === "Linear Scale") {
        const answersData = questionData.labels.map(label => {
            if (label in questionData.answers)
                return {x: label, y: questionData.answers[label]};
            else
                return {x: label, y: 0}
        });

        console.log(answersData);

        const options = {
            "legend": {
                "display": false
            },
            "scales": {
                "xAxes": [
                    {
                        "gridLines": {
                            "display": false
                        },
                    }
                ],
                "yAxes": [
                    {
                        "ticks": {
                            "beginAtZero": true,
                            "stepSize": 1,
                            "suggestedMax": 2
                        }
                    }
                ]
            }
        };

        createChart1(ctx, "bar", questionData, answersData, options);
    }
}