import math

# assuming you have extracted the following info from the profile's image.
eye_size = 0.47    # [cm^2]
eye_width = 24.2   # [mm]
eye_height = 23.7  # [mm]

iris_width = 20.2  # [mm]
iris_height = 19.7 # [mm]

def eye_roundness(iris_width, iris_height, eye_size):
    return (math.pi*iris_width/2*iris_height/2) / eye_size

def eye_ratio(eye_height, eye_width):
    return eye_height / eye_width

def meet_criteria(size, roundness, ratio):
    if size > 0.45 and \
        roundness >= 0.69 and \
        ratio >= 0.59:
            print("I’m sorry I wasn’t part of your past, can I make it up by being in your future?")

roundness = eye_roundness(iris_width, iris_height,eye_size)
ratio = eye_ratio(iris_height, iris_width)

meet_criteria(eye_size, roundness, ratio)
