import json

json_file = "src/web-test/reports/report.json"  
html_file = "src/web-test/reports/report.html"

with open(json_file, "r") as f:
    data = json.load(f)

html_content = """
<html>
<head>
    <title>Reporte de Pruebas</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #007BFF; }
        .scenario { border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; }
        .step { margin-left: 20px; }
        .passed { color: green; }
        .failed { color: red; }
    </style>
</head>
<body>
    <h1>Reporte de Automatización de Web</h1>
"""

for feature in data:
    html_content += f"<h2>Feature: {feature['name']}</h2>"

    for scenario in feature["elements"]:
        html_content += f"""
        <div class="scenario">
            <h3>{scenario['keyword']}: {scenario['name']}</h3>
            <p><b>Ubicación:</b> {scenario['location']}</p>
            <p><b>Estado:</b> <span class="{scenario['status']}">{scenario['status']}</span></p>
        """

        for step in scenario["steps"]:
            html_content += f"""
            <div class="step">
                <p><b>{step['keyword']}:</b> {step['name']}</p>
                <p>Estado: <span class="{step['result']['status']}">{step['result']['status']}</span></p>
                <p>Duración: {step['result']['duration']} segundos</p>
            </div>
            """

        html_content += "</div>"

html_content += "</body></html>"

with open(html_file, "w") as f:
    f.write(html_content)

print(f"Reporte generado exitosamente: {html_file}")