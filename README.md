# Nurse and Glow 💉✨

A microservices-based appointment and user registration system for a fictional clinic, deployed locally using Kubernetes and monitored with Prometheus and Grafana.

---

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Monitoring Setup](#monitoring-setup)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [License](#license)

---

## ✨ Features

- ✅ **User Service** - Registers new users and exposes metrics
- ✅ **Appointment Service** - Handles appointment requests and exposes metrics
- ✅ **Dockerized** - For local containerized builds
- ✅ **Kubernetes** - Deployed locally on Minikube
- ✅ **Monitoring** - Integrated with Prometheus + Grafana dashboards

---

## 🛠️ Tech Stack

- Python (Flask)
- Docker
- Kubernetes (Minikube)
- Prometheus
- Grafana

---

## 🚀 Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/drewdrew08/nurse-and-glow.git
cd nurse-and-glow
```

### Build Docker Images
```bash
cd user_service
sudo docker build -t user-service .

cd ../appointment_service
sudo docker build -t appointment-service .
```

### Start Minikube
```bash
minikube start --driver=docker
```

### Apply Kubernetes Deployments
```bash
kubectl apply -f k8s/user-deployment.yaml
kubectl apply -f k8s/appointment-deployment.yaml
```

---

## 🔍 Monitoring Setup

### Install Prometheus & Grafana
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace
```

### Apply ServiceMonitors
```bash
kubectl apply -f k8s/user-servicemonitor.yaml
kubectl apply -f k8s/appointment-servicemonitor.yaml
```

### Access Dashboards
```bash
# Grafana Dashboard
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80

# Prometheus Dashboard
kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090:9090
```

Login to Grafana:
- **URL**: http://localhost:3000
- **Username**: `admin`
- **Password**: `prom-operator`

---

## 📁 Project Structure

```
nurse-and-glow/
├── user_service/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── appointment_service/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── k8s/
│   ├── user-deployment.yaml
│   ├── appointment-deployment.yaml
│   ├── user-servicemonitor.yaml
│   └── appointment-servicemonitor.yaml
└── README.md
```


## 🖼️ Screenshots
![image](https://github.com/user-attachments/assets/256669a6-1e73-4225-ab7c-152fc5bc9135)

![appointments](https://github.com/user-attachments/assets/f371889a-4313-40f6-8426-d03735629688)

![user_registration](https://github.com/user-attachments/assets/241ecf3c-3084-4a4e-ad8d-1fb854c04fdf)



---

## 📄 License

MIT License — for educational use only.

