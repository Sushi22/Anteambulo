def create_template(issue_type, selected_options):
    issue_type = issue_type
    selected_options = selected_options
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
        selected_options=selected_options,
    
    )

    return filled_template