This module contains base classes or wrappers for creating Python design patterns easily.

### Signleton

Create a class inheriting from SingletonBase, and that's it.

```python

{!./docs_src/design_patterns/singletons/singleton.py!}

```

### NamedSingleton

Create a class inheriting from NamedSingletonBase and its first argument should always be name, which is a string. Then when you call this class with name *my_instance* let's say, and if you have never called it with the name *my_instance*, then the instance will be created. Otherwise, you will get the instance created when you called the class with that name before. 

```python

{!./docs_src/design_patterns/singletons/named_singleton.py!}

```