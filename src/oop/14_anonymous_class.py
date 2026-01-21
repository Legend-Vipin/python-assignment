# 15. Anonymous Class/Object
# Concept: Class without a name, often used for short-lived objects
AnonymousClass = type("AnonymousClass", (), {
    "greet": lambda self: "Hello from an anonymous class!"
})

anonymous_instance = AnonymousClass()
print(anonymous_instance.greet())
