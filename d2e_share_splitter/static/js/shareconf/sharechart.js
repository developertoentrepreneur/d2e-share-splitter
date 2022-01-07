google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data = google.visualization.arrayToDataTable(users_data);

  // googledata.push(users_data);

  var options = {
    title: "ShareDistribution Chart division",
  };

  var chart = new google.visualization.ShareDistributionChart(
    document.getElementById("sharechart")
  );

  chart.draw(data, options);
}
