def get_project_status():
    return "Smart Tomato Farm backend is working"


def health_check():
    return {
        "status": "ok",
        "service": "smart-tomato-farm-backend"
    }


if __name__ == "__main__":
    print(get_project_status())
    print(health_check())
