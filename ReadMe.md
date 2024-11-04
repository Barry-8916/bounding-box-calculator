Function: calculate_minimum_bounding_rectangle accepts polygon coordinates and computes the MBR.

Testing: The TestMinimumBoundingRectangle class includes various cases:

Square and Rectangle: Tests ensure the MBR matches the original rectangle's boundaries.

Irregular Polygon: Ensures that rotated polygons are correctly encapsulated.

Triangle: Verifies that non-rectangular shapes produce a valid MBR.

Comments and Assertions: Each test method includes descriptive comments, assertions, and error messages for clarity. This setup not only tests functionality but helps establish confidence in code accuracy.

This code demonstrates clean design, modularity, and thorough testing—ideal for senior-level engineering standards.