# @staticmethod decorator bounds method to class, not to an instance, so it doesn't require self parameter
# However method decorated with @staticmethod can still be called from instance
# @staticmethod is good way to "hide" functions that are only used by the class or can be logically connected with it


def without_decorator():
    print("This is a method created without decorator")


class StaticClass:
    # Staticmethod decorator is almost equal to assigning function to class this way
    without_decorator = without_decorator

    @staticmethod
    def with_decorator():
        print("This is a method created with decorator")


if __name__ == "__main__":
    instance = StaticClass()

    # Method created with decorator can be called on class and on instance
    StaticClass.with_decorator()
    instance.with_decorator()

    # However function assigned to class cannot be called on instance
    try:
        StaticClass.without_decorator()
        instance.without_decorator()
    except Exception as e:
        print(e)
