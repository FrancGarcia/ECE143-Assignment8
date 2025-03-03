import numpy as np

def find_convex_cover(pvertices, clist):
    """
    Return a list of the circle centers with the sum of their areas minimized
    and with the vertices from the pvertices within at least one circle from clist.

    :param: pvertices: An (n-1)-long iterable of polygon vertices that make up the convex polygon.
    :param clist: A list of (x_i,y_i) tuples of circle-centers that are within the convex polygon.

    :return: An m-long list of radii, r_i, corresponding to the m circle-centers.
    """
    assert(iter(pvertices)), "Polygon vertices must be iterable"
    assert(len(pvertices) > 2), "List of polygon vertices must be greater than 2 to form a polygon"
    for p in pvertices:
        assert(iter(p) and len(p) == 2 and isinstance(p[0],(int,float)) and isinstance(p[1],(int,float))), "The list of point vertices must contain valid coordinates"

    assert(isinstance(clist, list)), "List of circle centers must contain tuples of the (x_i,y_i) centers"
    assert(len(clist) > 0), "clist must not be empty"
    for c in clist:
        assert(isinstance(c,tuple) and len(c) == 2 and isinstance(c[0],(int,float)) and isinstance(c[1],(int,float))), "The list of circle centers must contain tuples of valid coordinates"

    pvertices = np.array(pvertices)  
    clist = np.array(clist) 
    m = len(clist)  
    n = len(pvertices) 
    distances = np.linalg.norm(pvertices[:,None,:] - clist[None,:,:], axis=-1)
    min_indices = np.argmin(distances, axis=1)
    radius = np.zeros(m)
    for i,index in enumerate(min_indices):
        radius[index] = max(radius[index], distances[i,index])
    return radius.tolist()

if __name__ == "__main__":
    pvertices = np.array([[ 0.573,  0.797],           
                        [ 0.688,  0.402],                                                              
                        [ 0.747,  0.238],                                                              
                        [ 0.802,  0.426],                                                              
                        [ 0.757,  0.796],                                                              
                        [ 0.589,  0.811]]) 
    clist = [(0.7490863467660889, 0.4917635308023209),                                       
              (0.6814339441396109, 0.6199470305156477),                                                
              (0.7241617773773865, 0.6982813914515696),                                                
              (0.6600700275207232, 0.7516911829987891),                                                
              (0.6315848053622062, 0.7730550996176769),                                                
              (0.7348437356868305, 0.41342916986639894),                                               
              (0.7597683050755328, 0.31729154508140384)]
    print(find_convex_cover(pvertices,clist))
