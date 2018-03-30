## Fast Incremental Cycle Detection On Directed Graph

- cycle_detect.py: 
    - cycle_detection(edges): yields networkx.DiGraph each time when encounter cycle
        - edges: [(source, target),]
        - time complexity: Õ(m√n)
- test.py:
    - command arg: #nodes #edges

This is an implementation based on the following published paper：

@inproceedings{Bernstein:2018:ITS:3174304.3175268,

 author = {Bernstein, Aaron and Chechik, Shiri},
 
 title = {Incremental Topological Sort and Cycle Detection in [Equation] Expected Total Time},
 
 booktitle = {Proceedings of the Twenty-Ninth Annual ACM-SIAM Symposium on Discrete Algorithms},
 
 series = {SODA '18},
 
 year = {2018},
 
 isbn = {978-1-6119-7503-1},
 
 location = {New Orleans, Louisiana},
 
 pages = {21--34},
 
 numpages = {14},
 
 url = {http://dl.acm.org/citation.cfm?id=3174304.3175268},
 
 acmid = {3175268},
 
 publisher = {Society for Industrial and Applied Mathematics},
 
 address = {Philadelphia, PA, USA},
}
