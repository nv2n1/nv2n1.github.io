---
title: "Dynamic Function Calls in PHP: Variables, call_user_func(), and Callables"
date: 2018-04-08 09:05:57 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-call-a-function-by-its-name-as-a-string-in-php/
---

PHP lets you call functions dynamically when you don’t know the function name until runtime. This is essential for plugin systems, routing handlers, API dispatchers, and configuration-driven logic. The approach you choose affects both performance and safety.

## Direct Variable Function Invocation

The simplest approach treats a string variable as a callable:

``` php
$func = 'strlen';
echo $func('hello');  // outputs: 5
```

This works for any function in the global namespace, but it has no built-in error handling. If the function doesn’t exist, you’ll get a fatal error.

Always validate before calling:

``` php
$func = 'some_function';
if (function_exists($func)) {
    $func();
} else {
    trigger_error("Function $func does not exist", E_USER_WARNING);
}
```

## Using call_user_func()

`call_user_func()` provides better error handling and works with callbacks more reliably:

``` php
$func = 'strlen';
$result = call_user_func($func, 'hello');  // outputs: 5
```

Pass multiple arguments as separate parameters:

``` php
function add($a, $b) {
    return $a + $b;
}

$func = 'add';
echo call_user_func($func, 5, 3);  // outputs: 8
```

## Calling Instance and Static Methods

For instance methods, pass an array with the object and method name:

``` php
class Calculator {
    public function multiply($a, $b) {
        return $a * $b;
    }
}

$calc = new Calculator();
$method = 'multiply';
echo call_user_func([$calc, $method], 4, 5);  // outputs: 20
```

For static methods, pass the class name as a string in an array:

``` php
class MathOps {
    public static function divide($a, $b) {
        return $a / $b;
    }
}

echo call_user_func(['MathOps', 'divide'], 20, 4);  // outputs: 5
```

Alternatively, use the `ClassName::methodName` string syntax:

``` php
echo call_user_func('MathOps::divide', 20, 4);  // outputs: 5
```

## Using call_user_func_array()

When arguments are already in an array, `call_user_func_array()` unpacks them automatically:

``` php
$func = 'array_merge';
$arrays = [[1, 2], [3, 4], [5, 6]];
$result = call_user_func_array($func, $arrays);  // [1, 2, 3, 4, 5, 6]
```

This is cleaner than manual unpacking with the spread operator:

``` php
function greet($greeting, $name, $punctuation) {
    return "$greeting, $name$punctuation";
}

$args = ['Hello', 'World', '!'];
echo call_user_func_array('greet', $args);  // Hello, World!
```

## Modern PHP: Callable Type Hints

In PHP 7.1+, use `callable` type hints for better code clarity and IDE support:

``` php
function execute_handler(callable $handler, ...$args) {
    return $handler(...$args);
}

execute_handler('strlen', 'test');        // works
execute_handler([$obj, 'method']);        // works
execute_handler(static fn($x) => $x * 2); // works with closures
```

The `callable` type hint enforces that the variable is actually callable before execution, catching errors earlier.

## Comparison: Variable Functions vs call_user_func()

Direct variable invocation is marginally faster but offers no validation:

``` php
// Direct: Fast, no error checking
$func = 'nonexistent';
$func();  // Fatal error: Call to undefined function nonexistent()

// call_user_func(): Safer, clearer intent
call_user_func('nonexistent');  // Warning: First argument is expected to be a valid callback
```

Use variable functions (`$func()`) only when performance is critical and you fully control the input. Use `call_user_func()` for user-supplied input or when you need validation.

## Practical Example: Router with Type Safety

``` php
class Router {
    private $routes = [];

    public function register(string $path, callable $handler): void {
        $this->routes[$path] = $handler;
    }

    public function dispatch(string $path) {
        if (!isset($this->routes[$path])) {
            http_response_code(404);
            return 'Not found';
        }

        $handler = $this->routes[$path];
        return call_user_func($handler);
    }
}

$router = new Router();
$router->register('/users', 'get_users');
$router->register('/posts', [PostController::class, 'list']);
$router->register('/status', fn() => 'OK');

echo $router->dispatch('/users');
```

Using `callable` type hints prevents invalid callbacks from being registered, catching errors during registration rather than dispatch.

## Performance Considerations

For tight loops calling the same function repeatedly, cache the callable reference and use variable functions:

``` php
$func = 'expensive_operation';
if (!function_exists($func)) {
    die("Function not found");
}

for ($i = 0; $i < 1000000; $i++) {
    $func($data);  // Faster than repeated call_user_func()
}
```

Variable functions avoid the function call overhead of `call_user_func()`. In modern PHP (8.0+), the performance gap is negligible unless you’re in a critical loop with millions of iterations.

For most application code, use `call_user_func()` or callable type hints for safety and clarity. Reserve direct variable functions for performance-critical paths where you control all inputs.
