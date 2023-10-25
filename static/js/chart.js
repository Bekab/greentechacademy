google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['AWS Male',     11],
        ['AWS Female',      2],
        ['Cheeta',  2],
        ['Azure', 2],
        ['Fast Track',    7]
    ]);

    var options = {
        title: ''
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart'));

    chart.draw(data, options);
}