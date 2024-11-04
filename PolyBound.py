from shapely.geometry import Polygon
import unittest

def calculate_minimum_bounding_rectangle(coords):
    """
    Calculate the minimum bounding rectangle of a given polygon.

    Args:
        coords (list of tuple): A list of (x, y) coordinates representing the vertices of a polygon.

    Returns:
        list of tuple: Coordinates of the minimum bounding rectangle.
    """
    # Initialize the polygon object from the coordinates
    polygon = Polygon(coords)
    
    # Calculate the minimum rotated rectangle (MBR)
    mbr = polygon.minimum_rotated_rectangle
    
    # Extract and return the coordinates of the MBR
    return list(mbr.exterior.coords)

### Unit Tests
class TestMinimumBoundingRectangle(unittest.TestCase):
    def test_square(self):
        """Test MBR for a square (expected to be the square itself)."""
        coords = [(1, 1), (1, 4), (4, 4), (4, 1)]
        expected = [(1, 1), (1, 4), (4, 4), (4, 1), (1, 1)]
        result = calculate_minimum_bounding_rectangle(coords)
        self.assertAlmostEqual(result, expected, "MBR does not match expected square coordinates.")
        
    def test_rectangle(self):
        """Test MBR for a simple rectangle."""
        coords = [(1, 1), (1, 5), (5, 5), (5, 1)]
        expected = [(1, 1), (1, 5), (5, 5), (5, 1), (1, 1)]
        result = calculate_minimum_bounding_rectangle(coords)
        self.assertAlmostEqual(result, expected, "MBR does not match expected rectangle coordinates.")
    
    def test_irregular_polygon(self):
        """Test MBR for an irregular polygon to verify rotation handling."""
        coords = [(0, 0), (1, 3), (4, 2), (3, 0)]
        result = calculate_minimum_bounding_rectangle(coords)
        self.assertEqual(len(result), 5, "MBR should have 5 points (4 vertices + closing point).")
    
    def test_triangle(self):
        """Test MBR for a triangle."""
        coords = [(1, 1), (3, 5), (6, 1)]
        result = calculate_minimum_bounding_rectangle(coords)
        self.assertEqual(len(result), 5, "MBR should have 5 points for a triangular shape.")
    
if __name__ == "__main__":
    # Run all unit tests
    unittest.main()
