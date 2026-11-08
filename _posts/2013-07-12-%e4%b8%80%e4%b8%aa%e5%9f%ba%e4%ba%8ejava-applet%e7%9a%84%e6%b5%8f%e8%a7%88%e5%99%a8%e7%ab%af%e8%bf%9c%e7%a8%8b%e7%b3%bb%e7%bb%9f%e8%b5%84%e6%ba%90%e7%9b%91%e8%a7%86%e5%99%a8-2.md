---
title: "Real-Time System Resource Monitoring with WebSockets"
date: 2013-07-12 16:47:43 +0000
author: "Eric Ma"
layout: post
categories: [web-development]
permalink: /%e4%b8%80%e4%b8%aa%e5%9f%ba%e4%ba%8ejava-applet%e7%9a%84%e6%b5%8f%e8%a7%88%e5%99%a8%e7%ab%af%e8%bf%9c%e7%a8%8b%e7%b3%bb%e7%bb%9f%e8%b5%84%e6%ba%90%e7%9b%91%e8%a7%86%e5%99%a8-2/
canonical: /%e4%b8%80%e4%b8%aa%e5%9f%ba%e4%ba%8ejava-applet%e7%9a%84%e6%b5%8f%e8%a7%88%e5%99%a8%e7%ab%af%e8%bf%9c%e7%a8%8b%e7%b3%bb%e7%bb%9f%e8%b5%84%e6%ba%90%e7%9b%91%e8%a7%86%e5%99%a8-2/
---

Java Applets were obsolete by 2016 and removed from Java 9+. If you need a browser-based system monitoring dashboard, use WebSockets or Server-Sent Events paired with modern JavaScript charting libraries.

## WebSocket + Python Backend Architecture

The most practical setup streams metrics from a Python backend to connected clients using WebSockets. Clients render real-time charts without server-side templating.

### Backend Metrics Collector

``` python
#!/usr/bin/env python3
import psutil
import json
import asyncio
import os
from websockets.server import serve
from datetime import datetime

async def broadcast_metrics(websocket, path):
    try:
        while True:
            metrics = {
                'cpu': psutil.cpu_percent(interval=1),
                'memory': psutil.virtual_memory().percent,
                'disk': psutil.disk_usage('/').percent,
                'load_avg': list(os.getloadavg()),
                'timestamp': datetime.utcnow().isoformat()
            }
            await websocket.send(json.dumps(metrics))
            await asyncio.sleep(2)
    except asyncio.CancelledError:
        pass

async def main():
    async with serve(broadcast_metrics, '0.0.0.0', 8080):
        print("Metrics server running on ws://0.0.0.0:8080")
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
```

For production, wrap with TLS and add authentication:

``` python
import ssl
from functools import wraps

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('cert.pem', 'key.pem')

async def authenticate(websocket, path):
    token = websocket.request_headers.get('Authorization', '').replace('Bearer ', '')
    if not validate_token(token):
        await websocket.close(code=1008, reason='Unauthorized')
        return
    await broadcast_metrics(websocket, path)

async def main():
    async with serve(authenticate, '0.0.0.0', 8080, ssl=ssl_context):
        print("Secure metrics server running on wss://0.0.0.0:8080")
        await asyncio.Future()
```

### Frontend Client

``` html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Monitor</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
        .container { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; padding: 20px; }
        .card { border: 1px solid #ddd; border-radius: 8px; padding: 15px; }
        canvas { max-height: 300px; }
        .status { padding: 10px; border-radius: 4px; font-size: 14px; }
        .status.connected { background: #d4edda; color: #155724; }
        .status.disconnected { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <div class="status disconnected" id="status">Disconnected</div>
    <div class="container">
        <div class="card"><canvas id="cpuChart"></canvas></div>
        <div class="card"><canvas id="memoryChart"></canvas></div>
        <div class="card"><canvas id="diskChart"></canvas></div>
        <div class="card"><canvas id="loadChart"></canvas></div>
    </div>

    <script>
        const maxDataPoints = 60;
        const metrics = { 
            labels: [], 
            cpu: [], 
            memory: [], 
            disk: [],
            load_avg: []
        };

        const chartConfigs = {
            cpu: {
                label: 'CPU %',
                color: 'rgb(255, 99, 132)',
                bgColor: 'rgba(255, 99, 132, 0.1)'
            },
            memory: {
                label: 'Memory %',
                color: 'rgb(75, 192, 192)',
                bgColor: 'rgba(75, 192, 192, 0.1)'
            },
            disk: {
                label: 'Disk %',
                color: 'rgb(255, 193, 7)',
                bgColor: 'rgba(255, 193, 7, 0.1)'
            },
            load_avg: {
                label: 'Load Average',
                color: 'rgb(153, 102, 255)',
                bgColor: 'rgba(153, 102, 255, 0.1)'
            }
        };

        function createChart(canvasId, metric) {
            return new Chart(document.getElementById(canvasId), {
                type: 'line',
                data: {
                    labels: metrics.labels,
                    datasets: [{
                        label: chartConfigs[metric].label,
                        data: metrics[metric],
                        borderColor: chartConfigs[metric].color,
                        backgroundColor: chartConfigs[metric].bgColor,
                        tension: 0.3,
                        fill: true,
                        pointRadius: 0
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    scales: {
                        y: { 
                            max: 100, 
                            min: 0,
                            ticks: { callback: v => v + '%' }
                        }
                    },
                    plugins: {
                        legend: { display: true }
                    }
                }
            });
        }

        const charts = {
            cpu: createChart('cpuChart', 'cpu'),
            memory: createChart('memoryChart', 'memory'),
            disk: createChart('diskChart', 'disk'),
            load_avg: createChart('loadChart', 'load_avg')
        };

        function connectWebSocket() {
            const token = localStorage.getItem('auth_token');
            const socket = new WebSocket('wss://monitoring-server:8080');
            let reconnectAttempts = 0;
            const maxAttempts = 10;

            socket.onopen = () => {
                if (token) {
                    socket.send(JSON.stringify({ type: 'auth', token }));
                }
                updateStatus(true);
                reconnectAttempts = 0;
            };

            socket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                const time = new Date(data.timestamp).toLocaleTimeString();

                metrics.labels.push(time);
                metrics.cpu.push(data.cpu);
                metrics.memory.push(data.memory);
                metrics.disk.push(data.disk);
                metrics.load_avg.push(data.load_avg[0]); // 1-minute load average

                if (metrics.labels.length > maxDataPoints) {
                    metrics.labels.shift();
                    metrics.cpu.shift();
                    metrics.memory.shift();
                    metrics.disk.shift();
                    metrics.load_avg.shift();
                }

                Object.values(charts).forEach(chart => chart.update('none'));
            };

            socket.onerror = () => {
                console.error('WebSocket error');
                updateStatus(false);
            };

            socket.onclose = () => {
                updateStatus(false);
                if (reconnectAttempts < maxAttempts) {
                    const delay = Math.pow(2, reconnectAttempts) * 1000;
                    reconnectAttempts++;
                    console.log(`Reconnecting in ${delay}ms`);
                    setTimeout(connectWebSocket, delay);
                }
            };

            return socket;
        }

        function updateStatus(connected) {
            const el = document.getElementById('status');
            el.textContent = connected ? 'Connected' : 'Disconnected';
            el.className = 'status ' + (connected ? 'connected' : 'disconnected');
        }

        connectWebSocket();
    </script>
</body>
</html>
```

## WebSockets vs Server-Sent Events

WebSockets provide bidirectional communication—useful when clients request specific metrics or adjust collection intervals. Server-Sent Events (SSE) work for unidirectional streams and use simpler HTTP, with better load-balancer compatibility.

Use SSE if you only need one-way data flow:

``` python
from aiohttp import web

async def metrics_stream(request):
    response = web.StreamResponse()
    response.headers['Content-Type'] = 'text/event-stream'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Connection'] = 'keep-alive'
    await response.prepare(request)

    try:
        while True:
            metrics = {
                'cpu': psutil.cpu_percent(interval=1),
                'memory': psutil.virtual_memory().percent,
                'timestamp': datetime.utcnow().isoformat()
            }
            await response.write(f"data: {json.dumps(metrics)}\n\n".encode())
            await asyncio.sleep(2)
    except asyncio.CancelledError:
        pass

    return response
```

Client-side SSE:

``` javascript
const eventSource = new EventSource('https://monitoring-server/metrics');

eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    updateCharts(data);
};

eventSource.onerror = () => {
    console.error('SSE connection lost');
    eventSource.close();
    setTimeout(() => location.reload(), 5000);
};
```

## Security Requirements

- Always use **WSS** (WebSocket Secure) or **HTTPS** for SSE in production
- Implement token-based authentication (JWT or OAuth2); never expose metrics unauthenticated
- Restrict collection intervals server-side to prevent DoS attacks
- Validate all incoming requests and reject unknown message types
- Set Content Security Policy headers to prevent XSS: `Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' cdn.jsdelivr.net`
- Rate-limit metric requests per client to prevent resource exhaustion
- Audit who accesses metrics—they reveal infrastructure topology and capacity

## Collection Intervals and Performance

- **CPU metrics**: 1-2 second intervals; more frequent polling wastes CPU
- **Disk/Network I/O**: 5-10 second intervals on busy systems
- **Load average/Memory**: 2-5 second intervals
- Keep only 1-2 hours of client-side data; archive to persistent storage
- Sample bursty metrics (network packets, syscalls) instead of capturing every event
- Add exponential backoff on reconnection to avoid thundering herd under load

## Handling Disconnections and Reconnection

``` javascript
function connectWebSocket() {
    const socket = new WebSocket('wss://monitoring-server:8080');
    let reconnectAttempts = 0;
    const maxAttempts = 10;

    socket.onopen = () => {
        console.log('Connected');
        reconnectAttempts = 0;
    };

    socket.onclose = () => {
        if (reconnectAttempts < maxAttempts) {
            const delay = Math.pow(2, reconnectAttempts) * 1000;
            console.log(`Reconnecting in ${delay}ms (attempt ${reconnectAttempts + 1})`);
            reconnectAttempts++;
            setTimeout(connectWebSocket, delay);
        } else {
            console.error('Max reconnection attempts reached');
        }
    };

    socket.onerror = (error) => {
        console.error('WebSocket error:', error);
    };

    return socket;
}
```

## Production Deployments

For anything beyond testing:

**Prometheus + Grafana**: Install the Prometheus node exporter on target systems, scrape metrics into Prometheus time-series database, visualize in Grafana. Excellent for multi-host monitoring with built-in alerting.

**Telegraf + InfluxDB**: High-performance metrics pipeline. Telegraf collects from diverse sources (HTTP, databases, system), InfluxDB stores, Grafana visualizes. Better for large cardinality datasets.

**Zabbix**: Open-source with distributed agents, trend analysis, sophisticated alerting, and compliance reporting. Suitable for enterprise deployments needing SNMP integration and custom triggers.

**Managed SaaS**: Datadog, New Relic, Honeycomb, or Elastic Cloud. Pay per host/metric volume; offloads infrastructure concerns.

## Monitoring Your Monitoring

Track these metrics on your monitoring system:

- WebSocket connection count over time
- Metric payload sizes and message throughput
- Client reconnection frequency
- Backend CPU/memory usage per connected client
- Message queue depth if buffering metrics

Set alerts on unexpected disconnects or high reconnection rates—they indicate network issues or backend problems.

## Advantages Over Legacy Approaches

Java Applets required browser plugins, failed silently on permission denial, incurred JVM startup overhead, and introduced attack surface through outdated security models. Modern web stacks run natively in browsers, deploy instantly without installation, use standardized TLS security and CORS headers, and scale to hundreds of concurrent clients efficiently. Development is simpler—no need for Java expertise alongside web development.
