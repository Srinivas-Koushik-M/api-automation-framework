import threading

class ContextManager:
    _context = threading.local()

    @classmethod
    def set_value(cls, key, value):
        if not hasattr(cls._context, "data"):
            cls._context.data = {}
        cls._context.data[key] = value

    @classmethod
    def get_value(cls, key):
        if not hasattr(cls._context, "data"):
            return None
        return cls._context.data.get(key)

    @classmethod
    def remove_value(cls, key):
        if hasattr(cls._context, "data"):
            cls._context.data.pop(key, None)

    @classmethod
    def clear(cls):
        if hasattr(cls._context, "data"):
            cls._context.data.clear()