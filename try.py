
# 888888888888888888888888888888888888888888888888888888888888
def fitness_function(popula):
    previous = 50
    for i in range(0, x):
        for j in range(0, edges):
            val = val + popula[i][j][0]
        if val < previous:
            previous = val
    print(previous)
fitness_function(a_3d_list)




def findIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    return [px, py]
#print(findIntersection(61,150,207,191,33,20,114,120))
point_of_intersection_var=findIntersection(1,1,4,5,4,5,5,3)
def intersection_conformation(x1, y1, x2, y2, x3, y3, x4, y4,point_of_intersection):
    if (point_of_intersection[0]==x1 and point_of_intersection[1]==y1) or (point_of_intersection[0]==x2 and point_of_intersection[1]==y2) or (point_of_intersection[0]==x3 and point_of_intersection[1]==y3) or (point_of_intersection[0]==x4 and point_of_intersection[1]==y4):
        #print('not intersecting')
        return 0
    else:
        #print('intersecting')
        return 1
intersection_conformation(61,150,207,191,33,20,114,120,point_of_intersection_var)