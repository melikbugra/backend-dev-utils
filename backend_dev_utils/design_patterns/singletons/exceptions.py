class SingletonInstanceNotFoundError(Exception):
    """
    Exception raised when trying to reset or access a non-existent instance.
    """

    def __init__(self, cls_name: str, instance_name: str = None):
        if instance_name:
            self.message = (
                f"No instance with name '{instance_name}' exists in {cls_name} class."
            )
        else:
            self.message = f"No instance of '{cls_name}' exists."
        super().__init__(self.message)
