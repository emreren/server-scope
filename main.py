from fastapi import FastAPI
import psutil

app = FastAPI()

def get_top_processes(key, count=5):
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', key]):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return sorted(processes, key=lambda x: x[key], reverse=True)[:count]

@app.get("/metrics")
async def get_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    return {
        "cpu_usage": f"{cpu_usage} %",
        "memory_usage": {
            "total": f"{memory_info.total / (1024 ** 3):.2f} GB",
            "used": f"{memory_info.used / (1024 ** 3):.2f} GB",
            "free": f"{memory_info.available / (1024 ** 3):.2f} GB",
            "percentage": f"{memory_info.percent} %"
        },
        "disk_usage": {
            "total": f"{disk_info.total / (1024 ** 3):.2f} GB",
            "used": f"{disk_info.used / (1024 ** 3):.2f} GB",
            "free": f"{disk_info.free / (1024 ** 3):.2f} GB",
            "percentage": f"{disk_info.percent} %"
        },
        "top_5_cpu_processes": get_top_processes('cpu_percent'),
        "top_5_memory_processes": get_top_processes('memory_info')
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
