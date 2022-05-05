# Exercise

Read through pages 87 - 95 of Gamma et al. (1995) which describe the Abstract Factory pattern. Then explain how this pattern can help with avoiding each of the following causes for redesign.

1. Creating an object by specifying a class explicitly
2. Dependence on hardware and software platforms
3. Dependence on object representations or implementations
4. Tight coupling

## Answer

1. By using abstract classes, which only provide an interface for creating products, we avoid having to change each class when changing concrete class. The concrete class can simply be changed once, and all abstract classes will adhere.
2. Abstract factor pattern is better for dynamically typed languages.
3. By using abstract classes, we are not directly creating objects, but rather interfaces. Thus we are not dependent on object representation or implementation
4. By using abstract classes, we can generate look-and-feel for specific user scenarios. Like orientation of the screen, or the operating system.

## Literature

Gamma, E., Helm, R., Johnson, R. and Vlissides, J. (1995). Design Patterns: Elements of Reusable Object-Oriented Software. Addison-Wesley
