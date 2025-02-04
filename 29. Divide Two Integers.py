class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Handle edge case: Overflow when dividing INT_MIN by -1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)  # XOR to check opposite signs

        # Convert both numbers to positive
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Bitwise shifting approach
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  # Keep doubling until it exceeds dividend
                temp <<= 1  # Double divisor
                multiple <<= 1  # Track how many times we doubled

            dividend -= temp  # Subtract the highest possible multiple
            quotient += multiple  # Add how many times we subtracted

        # Apply sign
        if negative:
            quotient = -quotient

        # Ensure the result is within 32-bit bounds
        return max(INT_MIN, min(INT_MAX, quotient))
