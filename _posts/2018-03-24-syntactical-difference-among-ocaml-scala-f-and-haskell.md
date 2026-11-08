---
title: "Syntax Differences Between OCaml, Scala, F#, and Haskell"
date: 2018-03-24 08:20:10 +0000
layout: post
canonical: https://www.systutorials.com/syntactical-difference-among-ocaml-scala-f-and-haskell/
---

These four languages share functional programming roots but diverge significantly in syntax and design philosophy. Here’s a practical reference for anyone transitioning between them or evaluating which to use.

## Basic Function Definition

**OCaml:**

``` ocaml
let add x y = x + y

let rec factorial n =
  if n <= 1 then 1 else n * factorial (n - 1)
```

**F#:**

``` fsharp
let add x y = x + y

let rec factorial n =
    if n <= 1 then 1 else n * factorial (n - 1)
```

**Scala:**

``` scala
def add(x: Int, y: Int): Int = x + y

def factorial(n: Int): Int =
  if (n <= 1) 1 else n * factorial(n - 1)
```

**Haskell:**

``` haskell
add x y = x + y

factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial (n - 1)
```

## Type Annotations

OCaml and F# use similar type inference but differ in annotation style. Scala requires explicit types in most contexts. Haskell uses type classes extensively.

**OCaml type annotation:**

``` ocaml
let add (x : int) (y : int) : int = x + y
```

**F# type annotation:**

``` fsharp
let add (x : int) (y : int) : int = x + y
```

**Scala type annotation:**

``` scala
def add(x: Int, y: Int): Int = x + y
```

**Haskell type annotation:**

``` haskell
add :: Int -> Int -> Int
add x y = x + y
```

## Pattern Matching

All four support pattern matching, but syntax varies.

**OCaml:**

``` ocaml
match list with
| [] -> "empty"
| [x] -> "one element"
| x :: tail -> "multiple elements"
```

**F#:**

``` fsharp
match list with
| [] -> "empty"
| [x] -> "one element"
| x :: tail -> "multiple elements"
```

**Scala:**

``` scala
list match {
  case Nil => "empty"
  case List(x) => "one element"
  case x :: tail => "multiple elements"
}
```

**Haskell:**

``` haskell
case list of
  [] -> "empty"
  [x] -> "one element"
  (x:xs) -> "multiple elements"
```

## List Operations

**OCaml:**

``` ocaml
let numbers = [1; 2; 3; 4; 5]
let mapped = List.map (fun x -> x * 2) numbers
let filtered = List.filter (fun x -> x > 2) numbers
```

**F#:**

``` fsharp
let numbers = [1; 2; 3; 4; 5]
let mapped = List.map (fun x -> x * 2) numbers
let filtered = List.filter (fun x -> x > 2) numbers
```

**Scala:**

``` scala
val numbers = List(1, 2, 3, 4, 5)
val mapped = numbers.map(x => x * 2)
val filtered = numbers.filter(x => x > 2)
```

**Haskell:**

``` haskell
let numbers = [1, 2, 3, 4, 5]
let mapped = map (* 2) numbers
let filtered = filter (> 2) numbers
```

## Lambda Expressions

**OCaml:**

``` ocaml
fun x -> x * 2
```

**F#:**

``` fsharp
fun x -> x * 2
```

**Scala:**

``` scala
x => x * 2
```

**Haskell:**

``` haskell
\x -> x * 2
```

## Immutability and Variables

**OCaml and F#** use `let` for immutable bindings by default. Mutable references require explicit syntax.

**OCaml mutable:**

``` ocaml
let counter = ref 0
counter := !counter + 1
```

**F# mutable:**

``` fsharp
let mutable counter = 0
counter <- counter + 1
```

**Scala** distinguishes with `val` (immutable) and `var` (mutable).

``` scala
val immutable = 10
var mutable = 10
```

**Haskell** is purely functional; all bindings are immutable.

``` haskell
let x = 10
-- x cannot be reassigned
```

## Key Philosophical Differences

**OCaml and F#** are ML-family languages with similar syntax. F# runs on .NET, while OCaml is more research-oriented and has stronger module system features.

**Scala** targets the JVM with object-oriented and functional paradigms coexisting. It supports operator overloading and more flexible syntax.

**Haskell** is purely functional and lazy by default. It enforces immutability at language level and requires monadic patterns for side effects. Its type system is the most powerful, with type classes providing ad-hoc polymorphism.

## Practical Considerations

Choose based on your ecosystem: Scala for JVM projects, F# for .NET teams, OCaml for compiler development and formal verification, Haskell for strongly-typed systems and mathematical computing. Syntax differences become muscle memory quickly—the real distinction is in typing discipline and runtime behavior.
