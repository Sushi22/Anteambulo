issue_type = "5xx"
start_time = '18-04-2024 10:00:00'
end_time = '18-04-2024 15:00:00'
selected_options = ["Container Restarts", "CPU throttling", "Thread Waiting Queue Size Exceeded", "Manage Resources for fix"]
service_name = "Flock"

report_template = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
</head>
<body>
    <h1>{issue_type}</h1>
    <h2>Service name : </h2><span><h2>{service_name}</h2>
    <h3>{start_time}</h3>
    <h3>{end_time}</h3>
    <h2>Steps used to debug<h2>
    <div>
    <p>{selected_options[0]}</p>
    <p>{selected_options[1]}</p>
    <p>{selected_options[2]}</p>
    <p>{selected_options[3]}</p>
    </div>

</body>
</html>
"""

filled_template = report_template.format(
    issue_type=issue_type,
    start_time=start_time,
    end_time=end_time,
    selected_options=selected_options,
    service_name=service_name
)