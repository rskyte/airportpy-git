## Airport

An simple airport model; planes can land and take off, airports have capacities and weather conditions can ground planes/prevent landings.

#### Prerequisites

Python 3.6^ - get the latest [here](https://www.python.org/downloads/)

#### Implementation (in python REPL)
```
$ cd airportpy-git
$ python3
```
```
>>> import sys
>>> sys.path.append('./airportpy')
>>> from src.airport import Airport
>>> from src.plane import Plane
>>> plane_1 = Plane()
>>> plane_2 = Plane()
>>> plane_3 = Plane()
>>> plane_4 = Plane()
>>> airport = Airport(3)
>>> airport.land(plane_1)
>>> airport.land(plane_2)
>>> airport.land(plane_3)
>>> airport.land(plane_4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./airportpy/src/airport.py", line 16, in land
    raise Exception
Exception
>>> airport.land(plane_3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./airportpy/src/airport.py", line 16, in land
    raise Exception
Exception
>>> airport.take_off(plane_3)
>>> airport.take_off(plane_2)
>>> airport.take_off(plane 2)
  File "<stdin>", line 1
    airport.take_off(plane 2)
                           ^
SyntaxError: invalid syntax
>>> airport.take_off(plane_2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./airportpy/src/airport.py", line 22, in take_off
    raise Exception 
Exception
>>> 
```

#### Running Tests
```
$ cd airportpy-git
$ python3 airportpy/test/runner.py
```

#### User Stories
```
As an air traffic controller 
So I can get passengers to a destination 
I want to instruct a plane to land at an airport

As an air traffic controller 
So I can get passengers on the way to their destination 
I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport

As an air traffic controller 
To ensure safety 
I want to prevent takeoff when weather is stormy 

As an air traffic controller 
To ensure safety 
I want to prevent landing when weather is stormy 

As an air traffic controller 
To ensure safety 
I want to prevent landing when the airport is full 

As the system designer
So that the software can be used for many different airports
I would like a default airport capacity that can be overridden as appropriate
```