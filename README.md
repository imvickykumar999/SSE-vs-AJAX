# `Comparison: SSE vs. AJAX Polling`
[Screencast from 07-03-25 02:59:42 PM IST.webm](https://github.com/user-attachments/assets/fb9f1664-5523-452a-a205-7f3728f19716)

<br>

The **main difference** between `Server-Sent Events` **(SSE)** *v/s* `Asynchronous JavaScript and XML` **(AJAX)** implementations lies in how they **fetch real-time data** from the Django backend.

<br>

| Feature | **First HTML (SSE-based)** | **Second HTML (AJAX-based Polling)** |
|---------|-----------------|----------------------|
| **Data Fetching Method** | Uses **Server-Sent Events (SSE)** via `EventSource` | Uses **AJAX polling** with `$.ajax()` |
| **Efficiency** | **More efficient** – Uses a single connection to receive continuous updates | **Less efficient** – Sends a new request every second, adding load to the server |
| **Latency** | **Real-time** – Updates as soon as new data is available | **Delayed updates** – Dependent on polling interval (1 second in this case) |
| **Bandwidth Usage** | **Lower bandwidth** – The connection remains open, and only new data is pushed | **Higher bandwidth** – New request-response cycle every second |
| **Browser Support** | **Supported in all modern browsers** (except old versions of IE) | **Works in all browsers**, including older ones |
| **Reconnection Handling** | **Automatic reconnection** (if the server supports it) | Needs **manual handling** via `setTimeout(fetchStream, 1000)` |
| **Scalability** | **Better for large-scale applications** | **Can overload server** if many users make frequent requests |
