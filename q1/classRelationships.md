# Class Relationships: Association and Multiplicity 
## Previous Work 
[Part I - Classes and Objects](classObjectUML.md) 
[Part II - Class Attributes and Methods](classAttributesMethods.md) 
## Existing Class 
#### Class: Cars
#### Description: A type of vehicle with different brands.
## New Related Class 
#### Class: Driver
#### Description: The one in control of the car or any vehicle.
## Association 
#### Relationship: A car needs a driver to be used, and a driver needs a car to be able to go to some places.
#### Explanation:  A car needs a driver to be used, and a driver needs a car to be able to go to some places.
## Multiplicity
#### Multiplicity: 
###### Car:
| Minimum and Maximum of Atributes | Description/Label |
|---|---|
| 4 | Wheels of the car |
| 1..* | Chairs |
| * | Bodykits and mods |
| 1 | Engine |
| 0..2 | Turbo |
###### Driver:
| Minimum and Maximum of Atributes | Description/Label |
|---|---|
| 1 | Steering wheel to hold |
| 0..* | Traffic violations |
| * | Cars owned |
| 1 | Current Car Operating |

## Updated UML Class Diagram
#### Explanation: 
## UML Class Relationship Diagram 
![Class Relationship Diagram](images/classRelationshipDiagram.png) 
## Python Implementation 
[View Python Source](classRelationships.py) 
## Test Run 
![Relationship Test Run](images/relationshipTestRun.png) 
## Object Relationship Diagram 
![Object Relationship Diagram](images/objectRelationshipDiagram.png) 
## Analysis 
### What is the association between your two classes? 
The association is that my two classes are connected to each other because a driver can own or drive cars. The drivers can also acess the information of their owned cars.
### What multiplicity did you choose and why? 
I chose 4 for wheels because a car requires 4 wheels to be driven properly. I chose 1 to many seats for a car because there are some types of cars that only have one seat such as race cars, and there are cars that have more than 4 seats such as vans and SUVs. I chose many for bodykits and design because a car can have many design choices. By design there is only 1 engine for a car and it only varies due to size or modifications. A car can also have turbo or not I chose 2 as the maximum because from what I remember the max is twin turbos therefore 2. A driver can only hold one steering wheel. Have none or many traffic violations or tickets. A driver may also have more than 1 vehicle. And a driver can only operate one car at a time due to him having to be physically present.
### How did you implement the relationship in Python? 
I connected it by making the car require a driver, and the driver can affect the car by causing accidents through the private attribute "Luck".
### Why did you store an object reference instead of copying its data? 
So the driver can access the actual car object and affect its luck attribute.
### If your relationship uses many, why is a list appropriate? 
The list is required to store the objects instead of their names.
