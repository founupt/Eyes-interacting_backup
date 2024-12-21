import numpy as np

desired_coords = [
    (960, 540),
    (500, 400),
    (300, 300),
    (1200, 700),
    (470, 439),
    (492, 427),
    (545, 427),
    (524, 446),
]

actual_coords = [
    (955, 540),  
    (505, 405),  
    (295, 303),  
    (1210, 695),  
    (470, 439),  
    (492, 428),  
    (545, 422), 
    (532, 450),  
]

def calculate_accuracy(desired_coords, actual_coords, threshold=10):
    if len(desired_coords) != len(actual_coords):
        raise ValueError("Số lượng tọa độ mong muốn và tọa độ thực không khớp!")

    errors = []
    accurate_points = 0

    for desired, actual in zip(desired_coords, actual_coords):
        error = np.sqrt((desired[0] - actual[0]) ** 2 + (desired[1] - actual[1]) ** 2)
        errors.append(error)

        if error <= threshold:
            accurate_points += 1

    accuracy = (accurate_points / len(desired_coords)) * 100

    return errors, accuracy

threshold = 10  
errors, accuracy = calculate_accuracy(desired_coords, actual_coords, threshold)

print("Sai số Euclidean từng cặp tọa độ:")
for error in errors:
    print(f"{error:.2f}")  
print(f"Độ chính xác với ngưỡng {threshold} pixels: {accuracy:.2f}%")