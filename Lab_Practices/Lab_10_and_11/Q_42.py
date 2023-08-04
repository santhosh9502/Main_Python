def young_old(p1,p2,p3):
    ages = [p1, p2, p3]
    oldest = max(ages)
    youngest = min(ages)
    return oldest, youngest

p1 = 43
p2 = 23
p3 = 90

oldest,youngest = young_old(p1, p2, p3)
print(f"oldest is {oldest}")
print(f"youngest is {youngest}")
