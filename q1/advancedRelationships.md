# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
The existing system contains my Car and Driver classes. The car contains informations about attributes such as brands, price, color, and speed. The driver class contains the information and how they are associated with their owned cars.
## Inheritance Relationship
#### Parent: Car
#### Child: SportsCar
#### Explanation: SportsCar is a type of a car. It inherits the common attribute and methods of the original parent class, but it may contain additional attributes or methods.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
#### Relationship: Car has an Engine.
#### Explanation: The car and engine has a compositional relationship because a car "technically" creates its own Engine because it is a part of the car in this peice of code.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
#### 1. I chose Car as the parent class and SportsCar as the child class because of their real life correlation wherein the SportsCar is a type of car. They have similar characteristics except for the fact the child class has an additional method and attribute related to turbo which makes the car faster.
#### 2. Inheritance makes the code less longer because you have to skip redefining a new class instead of just doing inheritance. It reuses all the attributes but adds new attributes and methods.
#### 3. The HAS-A relation I implemented was composition because the car creates its own engine. The engine is just a component in my system. Meaning the car owns the engine instead of being a seperate entity.
#### 4. Association basically means the two classes are connected but dont own each other. In part 3 the car is associated with the driver, but in this code the car directly owns the engine.
#### 5. Yes it follows the dry principle, Because I only pasted the car code once, so SportsCar can reuse the attribute of the parent class.
