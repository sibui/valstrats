"""Main module."""
from Grid import Grid
from Strat import Strat

g = Grid(10,10,0,"first");
g.populateSquare(0, 0, 'a');
g.populateSquare(0, 1, 'b');
g.populateSquare(1, 0, 'c');
g.populateSquare(1, 1, 'd');


h = Grid(10,10,1,"second");
h.populateSquare(0, 0, '1');
h.populateSquare(0, 1, '2');
h.populateSquare(1, 0, '3');
h.populateSquare(1, 1, '4');


s = Strat();
s.addGrid(g);
s.addGrid(h);
s.print();



