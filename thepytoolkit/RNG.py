import time

# TIME USED FOR A RANDOM SEED

class RNG:
    # RNG GENERATOR
    """
    THIS IS THE CLASS FOR HANDLING EVERYTHING
    """
    def __init__(self, seed=None):  # Initialise the class

        """
        Seed the random number generator, keep the state of it below the 64-bit integer.
        :param seed: The seed for the random number generator, if NONE, use the time.time_ns() function to grab the time in nanoseconds.
        """
        self.seed = seed

        if seed is None:
            seed = int(time.time_ns())

        self.state = seed & 0xFFFFFFFFFFFFFFFF #64-BIT INTEGER, KEEPS IT BELOW IT


        self.a = 6364136223846793005 # THE SUGGESTED INCREMENT
        self.c = 1
        self.m = 2**64 # Multiplier

    def __next__(self):
        self.state = (self.a * self.state + self.c) % self.m # INPUTTING THE FORMULA WITH "STATE" AS THE current number

        return self.state >> 32

    def randint(self, a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("The two arguments should be integers.")
        if a > b:
            raise ValueError("Int. A should be lesser or = to B.")

        return a + self.__next__() % (b - a + 1)

    def randfloat(self, a, b):
        if not (isinstance(a, float) and isinstance(b, float)):
            raise ValueError("The two arguments should be floats.")
        if a > b:
            raise ValueError("Int. A should be lesser or = to B.")

        zero_to_one = self.__next__() / 0xFFFFFFFF

        return a + (zero_to_one * (b - a)) # I found the fix on the internet

    def bits(self, num):

        if num < 0:
            number = self.randint(num, 0)
            binary = bin(number)[3:]
            return "-" + str(binary)
        else:
            number = self.randint(0, num)
            binary = bin(number)[2:]

            return binary

    def choice(self, thing):

        array_Length = len(thing)
        try:
            if array_Length == 0:
                return "The string/array is empty."

            elif array_Length >= 1:
                choice = self.randint(-1, array_Length - 1)
                return thing[choice]

        except Exception as e:
            raise ValueError("The string/list is empty, or their is no string/list! ERROR: " + str(e))

        return None

generator = RNG()

# Create a class instance.
if __name__ == "__main__":
    pass
