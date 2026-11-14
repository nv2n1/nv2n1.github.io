---
title: "stdvariantvalueless_by_exception(3)"
name: "stdvariantvalueless_by_exception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariantvalueless_by_exception/"
---

std::variant&lt;Types...&gt;::valueless_by_exception - std::variant&lt;Types...&gt;::valueless_by_exception

<h2>Synopsis</h2>

constexpr bool valueless_by_exception() const noexcept; <i>(since C++17)</i> 
Returns false if and only if the variant holds a value. 

<h2>Notes</h2>

A variant may become valueless in the following situations: 
* (guaranteed) an exception is thrown during the move initialization of the contained value from the temporary in copy_assignment 
* (guaranteed) an exception is thrown during the move initialization of the contained value during move_assignment 
* (optionally) an exception is thrown when initializing the contained value during a type-changing assignment 
* (optionally) an exception is thrown when initializing the contained value during a type-changing emplace 
Since variant is never permitted to allocate dynamic memory, previous value cannot be retained in these situations. 
This applies even to variants of non-class types:  
A variant that is valueless by exception is treated as being in an invalid state: index returns variant_npos, get and visit throw bad_variant_access. 
