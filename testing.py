def circle_area(r: int) -> int:
    PI = 3.14
    area_of_circle = PI * r**2
    return area_of_circle


def format_description(r, area):
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: float):
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius: "))
get_info(radius)
