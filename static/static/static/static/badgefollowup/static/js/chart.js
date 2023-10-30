google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['Cohort A',     11],
        ['Cohort B',      2],
        ['Cohort C',  2],
        ['Cohort D', 2],
        ['Cohort E',    7]
    ]);

    var options = {
        title: ''
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);
}