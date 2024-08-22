import json
import random
import time

start_id = 567


def create_data():
    global start_id
    patient = "Carrie Fisher"

    data = {
        "id": start_id,
        "patient": patient,
        "time": time.asctime(),
        "heart_rate": int(random.gauss(80, 1)),
        "respiratory_rate": int(random.gauss(12, 2)),
        "heart_rate_variability": 65,
        "body_temperature": random.gauss(99, 0.5),
        "blood_pressure": {
            "systolic": int(random.gauss(105, 2)),
            "diastolic": int(random.gauss(70, 1)),
        },
        "activity": "Walking",
        "message": "Hello, this is a COMP216 test message",
    }

    data_car = {
        "id": 567,
        "make": "Honda",
        "model": "Civic Type-R",
        "housepower": int(random.gauss(300, 2)),
        "maketime": time.asctime(),
        "drivetrain": "6-speed manual transmission",
        "dimensions": {
            "height": int(random.gauss(1406, 10)),
            "width": int(random.gauss(1889, 9)),
            "weelbase": int(random.gauss(2735, 8)),
        },
        "message": "Hello, this is a COMP216 test message",
    }

    start_id += 1
    return data_car


def print_data(data):
    print()
    print(f"ID: {data['id']}")
    print(f"Make: {data['make']}")
    print(f"Model: {data['model']}")
    print(f"Housepower: {data['housepower']}")
    print(f"Manufacture Time: {data['maketime']}")
    print(f"Drivetrain: {data['drivetrain']}")
    print(f"Dimension:")
    print(f"   Height: {data['dimensions']['height']}")
    print(f"   Width: {data['dimensions']['width']}")
    print(f"   Wheelbase: {data['dimensions']['weelbase']}")
    print(f"Message: {data['message']}")


if __name__ == "__main__":

    data = create_data()
    print_data(data)
