---
title: "stdexperimentalany_cast(3)"
name: "stdexperimentalany_cast"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalany_cast/"
---

std::experimental::any_cast - std::experimental::any_cast

<h2>Synopsis</h2>

<pre><code>template &lt;class ValueType&gt;
(1)(library fundamentals TS)

    ValueType any_cast(const any &amp;operand);

template &lt;class ValueType&gt;
(2)(library fundamentals TS)

    ValueType any_cast(any &amp;operand);

template &lt;class ValueType&gt;
(3)(library fundamentals TS)

    ValueType any_cast(any &amp;&amp;operand);

template &lt;class ValueType&gt;
(4)(library fundamentals TS)

    const ValueType *any_cast(const any *operand) noexcept;

template &lt;class ValueType&gt;
(5)(library fundamentals TS)

    ValueType *any_cast(any *operand) noexcept;</code></pre> 
Performs type-safe access to the contained object. 
For (1-3), the program is ill-formed if ValueType is not a reference and std::is_copy_constructible&lt;ValueType&gt;::value is false. 

<h2>Parameters</h2>

operand - target any object

<h2>Return value</h2>

1) Returns *any_cast&lt;std::add_const_t&lt;std::remove_reference_t&lt;ValueType&gt;&gt;&gt;(&amp;operand). 
2-3) Returns *any_cast&lt;std::remove_reference_t&lt;ValueType&gt;&gt;(&amp;operand). 
4-5) If operand is not a null pointer, and the typeid of the requested ValueType matches that of the contents of operand, a pointer to the value contained by operand, otherwise a null pointer. 

<h2>Exceptions</h2>

1-3) Throws bad_any_cast if the typeid of the requested ValueType does not match that of the contents of operand.
