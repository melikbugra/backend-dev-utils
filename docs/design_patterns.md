This module contains base classes or wrappers for creating Python design patterns easily.

### Singleton

Create a class inheriting from SingletonBase, and that's it.

```python

{!./docs_src/design_patterns/singletons/singleton.py!}

```

### NamedSingleton

Create a class inheriting from NamedSingletonBase and its first argument should always be name, which is a string. Then when you call this class with name *instance1* let's say, and if you have never called it with the name *instance1*, then the instance will be created. Otherwise, you will get the instance created when you called the class with that name before. 

```python

{!./docs_src/design_patterns/singletons/named_singleton.py!}

```