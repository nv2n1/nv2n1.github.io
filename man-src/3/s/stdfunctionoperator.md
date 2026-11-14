---
title: "stdfunctionoperator(3)"
name: "stdfunctionoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfunctionoperator/"
---

std::function&lt;R(Args...)&gt;::operator= - std::function&lt;R(Args...)&gt;::operator=

<h2>Synopsis</h2>

<pre><code>function &amp;operator=(const function &amp;other);
(1)(since C++ 11)

    function &amp;
    operator=(function &amp;&amp;other);
(2)(since C++ 11)

    function &amp;
    operator=(std::nullptr_t);
(since C++ 11)(until C++ 17)

    function &amp;
    operator=(std::nullptr_t) noexcept;
(since C++ 17)

    template &lt;class F&gt;
    (3)(4)(since C++ 11)

        function &amp;
        operator=(F &amp;&amp;f);

template &lt;class F&gt;
(5)(since C++ 11)

    function &amp;
    operator=(std::reference_wrapper&lt;F&gt; f) noexcept;
Assigns a new target to std::function.

1) Assigns a copy of target of other, as if by executing function(other).swap(*this);

2) Moves the target of other to *this. other is in a valid state with an unspecified value.

3) Drops the current target. *this is empty after the call.

4) Sets the target of *this to the callable f, as if by executing function(std::forward&lt;F&gt;(f)).swap(*this);
.

    This
    operator does not participate in overload resolution unless f is Callable for argument types Args... and
    return type R.

    (since C++ 14)

        5) Sets the target of * this to a copy of f,
    as if by executing function(f).swap(*this);
</code></pre>

<h2>Parameters</h2>

other - another std::function object to copy the target of 
f - a callable to initialize the target with

<h2>Type requirements</h2>

- 
F must meet the requirements of Callable.

<h2>Return value</h2>

*this 

<h2>Notes</h2>

Even before allocator support was removed from std::function in C++17, these assignment operators use the default allocator rather than the allocator of *this or the allocator of other (see LWG_#2386). 

<h2>See also</h2>

assign assigns a new target 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(until C++17)</i> 
