# Homework №3
## **Range** and **Account** programs.

 Regular programs made by Arsen Martirosyan (aka *Archibald1707*).
 No license required.

## Terms and conditions

### 1. Range

 Implement the Range abstract data type, which represents a closed integer range.
 **Range** must support the following operations.

 Construction:
 - Create an empty interval.
 - Create interval [min; max] on the endpoints.

Binary operations:
 - Intersection of intervals.
 - Union of intersecting intervals.

Unary predicates:
 - Checking the interval for emptiness.
 - Checking if a point is in an interval.

Binary predicates:
 - Checking two intervals for equality.
 - Checking two intervals for intersection.
 - Checking an interval for occurrence in another.

Other:
 - Lists all points in the interval in ascending order.
 - Calculation of the minimum interval.
 - Calculation of the maximum interval.
 - Calculation of the string representation of the interval, for example, in the format of the form [-3; 7].

> Note: It is understood that the operation of listing all the points of the interval will return an iterator that allows you to iterate over the points, and not just return a list of numbers or display them on the screen.

 > Tip: Don't forget to also think about proper and consistent naming of these operations.
 > Tip: If it is possible and accepted in your programming language to implement some operations as operators, then do it.
 > Tip: Similarly, if there are any conventions about the interface of some typical operations, then it is worth following them. For example, in JavaScript, the string representation is calculated using a method named toString. Your language may also have similar conventions.
 
### 2. Account

 Implement an Account abstract data type that represents a model of a bank checking account. The account is kept in arbitrary units and does not allow reaching a negative balance. Account must support the following operations:
 - Deposit funds to the account.
 - Withdraw funds from the account.
 - Generate an account statement.

 ##### An example of a statement format:
 
 ```
Time Amount Balance
28.09.2021 13:37:00 +500 500
28.09.2021 13:37:01 -100 400
```

 > Tip: Think about how to test the code correctly, taking into account the fact that, among other things, you will need to test the correctness of the output of different operation execution times in the statement.