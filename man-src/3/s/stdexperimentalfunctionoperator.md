---
title: "stdexperimentalfunctionoperator(3)"
name: "stdexperimentalfunctionoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfunctionoperator/"
---

std::experimental::function&lt;R(Args...)&gt;::operator= - std::experimental::function&lt;R(Args...)&gt;::operator=

<h2>Synopsis</h2>

<pre><code>function &amp;operator=(const function &amp;other);
(1)(library fundamentals TS)

    function &amp;
    operator=(function &amp;&amp;other);
(2)(library fundamentals TS)

    function &amp;
    operator=(std::nullptr_t) noexcept;
(3)(library fundamentals TS)

    template &lt;class F&gt;
    (4)(library fundamentals TS)

        function &amp;
        operator=(F &amp;&amp;f);

template &lt;class F&gt;
(5)(library fundamentals TS)

    function &amp;
    operator=(std::reference_wrapper&lt;F&gt; f);
Assigns a new target to std::experimental::function.In the description below, let ALLOCATOR_OF(f) be the allocator specified in the construction of f, or the value of std::experimental::pmr::get_default_resource() at the time of construction if no allocator was specified.

1) Assigns a copy of target of other, as if by executing function(std::allocator_arg, ALLOCATOR_OF(*this), other).swap(*this);

2) Moves the target of other to *this, as if by executing function(std::allocator_arg, ALLOCATOR_OF(*this), std::move(other)).swap(*this);. other is in a valid state with an unspecified value.

3) Destroys the target of *this. *this is empty after the call. The memory resource returned by get_memory_resource() after the assignment is equivalent to the memory resource before the assignment, but the address may change.

4) Sets the target of *this to the callable f, as if by executing function(std::allocator_arg, ALLOCATOR_OF(*this),std::forward&lt;F&gt;(f)).swap(*this);
.This operator does not participate in overload resolution unless f is Callable for argument types Args... and return type R.

    5) Sets the target of * this to a copy of f,
    as if by executing function(std::allocator_arg, ALLOCATOR_OF(*this), f).swap(*this);
</code></pre>

<h2>Parameters</h2>

other - another std::experimental::function object to copy or move from 
f - a callable to initialize the target with

<h2>Type requirements</h2>

- 
F must meet the requirements of Callable.

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

1-2,4-5) <i>(none)</i>
