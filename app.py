from flask import Flask, render_template_string
import platform
import socket
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technical Hub Portal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { background-color: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', sans-serif; }
        .navbar-brand { font-weight: 800; font-size: 1.6rem; background: linear-gradient(135deg, #22c55e, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .card-custom { background: #161b22; border: 1px solid #30363d; border-radius: 12px; transition: all 0.25s ease; }
        .card-custom:hover { transform: translateY(-5px); border-color: #22c55e; }
        .status-badge { padding: 6px 16px; border-radius: 20px; background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid #22c55e; }
        .hero-title { font-size: 2.8rem; font-weight: 800; background: linear-gradient(135deg, #4ade80, #38bdf8, #a78bfa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg border-bottom border-secondary mb-4 py-3">
        <div class="container">
            <a class="navbar-brand" href="#"><i class="fa-solid fa-code-branch text-success"></i> TECHNICAL HUB</a>
            <span class="status-badge"><i class="fa-solid fa-circle-check"></i> Live Production Build</span>
        </div>
    </nav>
    <div class="container pb-5">
        <div class="text-center mb-5">
            <h1 class="hero-title">Welcome to Technical Hub Portal</h1>
            <p class="text-secondary fs-5">Enterprise DevOps & Cloud Engineering Innovation Center</p>
        </div>
        <div class="row g-4 mb-5">
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="fs-2 text-info mb-2"><i class="fa-solid fa-microchip"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Technical Environment</h5>
                    <h4 class="fw-bold text-light">{{ info.os }}</h4>
                    <p class="mb-0 text-muted fs-7">Host: {{ info.hostname }}</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="fs-2 text-success mb-2"><i class="fa-solid fa-network-wired"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Pod Network IP</h5>
                    <h4 class="fw-bold text-light">{{ info.ip }}</h4>
                    <p class="mb-0 text-muted fs-7">Kubernetes Cluster Node</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card-custom p-4">
                    <div class="fs-2 text-warning mb-2"><i class="fa-solid fa-bolt"></i></div>
                    <h5 class="text-secondary fs-6 text-uppercase">Live Engine Time</h5>
                    <h4 class="fw-bold text-light">{{ info.time }} UTC</h4>
                    <p class="mb-0 text-muted fs-7">Container Runtime Active</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def technical_hub():
    sys_info = {
        'os': f"{platform.system()} {platform.release()}",
        'hostname': socket.gethostname(),
        'ip': socket.gethostbyname(socket.gethostname()),
        'time': datetime.datetime.now().strftime("%H:%M:%S")
    }
    return render_template_string(HTML_TEMPLATE, info=sys_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
