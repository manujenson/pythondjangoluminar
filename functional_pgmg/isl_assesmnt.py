isl=[
       {"Team":"mumbai","Played":16,"Won":10 ,"Drawn":4 ,"Lost":2,"GF":25,"GA":11,"GD":14,"Points":34},
       {"Team":"atk","Played":16,"Won":10 ,"Drawn":4 ,"Lost":2,"GF":25,"GA":11,"GD":14,"Points":33} ,
       { "Team":"goa","Played":16,"Won":5 ,"Drawn":8 ,"Lost":3,"GF":24,"GA":19,"GD":5,"Points":23},
       {"Team":"hyderabad","Played":16,"Won":5 ,"Drawn":8 ,"Lost":3,"GF":20,"GA":16,"GD":4,"Points":23},
       {"Team":"neastunited","Played":16,"Won":5 ,"Drawn":8 ,"Lost":3,"GF":21,"GA":20,"GD":1,"Points":23},
       { "Team":"benglore","Played":17,"Won":4 ,"Drawn":7 ,"Lost":6,"GF":19,"GA":21,"GD":-2,"Points":19},
       { "Team":"jahmsadpur","Played":16,"Won":4 ,"Drawn":6 ,"Lost":6,"GF":15,"GA":19,"GD":-4,"Points":18} ]



#highst team & point

from functools import reduce
point_high=list(filter(lambda Team:Team["Points"]==reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda Team:Team["Points"],isl))),isl))
print(point_high)


