
issue_type = "5xx"
selected_options = ["Container Restarts", "CPU throttling", "", ""]

report_template = 
 """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
</head>
<body>
    <h1></h1>
    
    <div class="error-section">
        <h2>Error Details</h2>
        <p><strong>Error Type:</strong> {error_type}</p>
        <p><strong>Error Message:</strong> {error_message}</p>
        <p><strong>Error Traceback:</strong></p>
        <pre>{error_traceback}</pre>
    </div>

    <div class="code-section">
        <h2>Code Snippet</h2>
        <pre>{code_snippet}</pre>
    </div>
</body>
</html>
"""
