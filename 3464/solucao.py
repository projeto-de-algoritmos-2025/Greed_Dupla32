import bisect

class Solution(object):
    def maxDistance(self, side_length, points_list, k_value):
        """
        :type side_length: int
        :type points_list: List[List[int]]
        :type k_value: int
        :rtype: int
        """
        converted_points = []
        
        def transform_coordinates(x_coord, y_coord):
            if y_coord == 0:
                return x_coord
            elif x_coord == side_length:
                return side_length + y_coord
            elif y_coord == side_length:
                return 3 * side_length - x_coord 
            elif x_coord == 0:
                return 4 * side_length - y_coord
            
        for point in points_list:
            x, y = point
            converted_points.append(transform_coordinates(x, y))
            
        converted_points.sort()
        extended_points = converted_points + [4 * side_length + p for p in converted_points]
        
        def is_possible(distance):
            if distance > side_length:
                return False
                
            start = bisect.bisect_left(extended_points, extended_points[0] + distance)
            
            if start >= len(converted_points):
                return False
            
            for i in range(start):
                valid = True
                current = i
                for _ in range(k_value - 1):
                    next_pos = bisect.bisect_left(extended_points, extended_points[current] + distance)
                    if next_pos >= i + len(converted_points):
                        valid = False
                        break
                    current = next_pos
                
                if valid and extended_points[i + len(converted_points)] - extended_points[current] >= distance:
                    return True
                
            return False

        low = 1
        high = side_length + 1
        while low < high:
            mid = (low + high) // 2
            
            if is_possible(mid):
                low = mid + 1
            else:
                high = mid 
                
        return low - 1