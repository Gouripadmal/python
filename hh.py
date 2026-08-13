blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

blog = 0
name = 0

for views in blog_views:
    blog += views

    if views > 1000:
        print("Trending")
        name += 1

    elif 500 <= views <= 1000:
        print("Average")

    else:
        print("Low Traffic")

print("Total number of views:", blog)
print("Number of Trending posts:", name)