---
title: "stdanyoperator(3)"
name: "stdanyoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdanyoperator/"
---

std::any::operator= - std::any::operator=

<h2>Synopsis</h2>

<pre><code>any &amp;operator=(const any &amp;rhs);
(1)(since C++ 17)

    any &amp;
    operator=(any &amp;&amp;rhs) noexcept;
(2)(since C++ 17)

    template &lt;typename ValueType&gt;
    (3)(since C++ 17)

        any &amp;
        operator=(ValueType &amp;&amp;rhs);</code></pre> 
Assigns contents to the contained value. 
1) Assigns by copying the state of rhs, as if by any(rhs).swap(*this). 
2) Assigns by moving the state of rhs, as if by any(std::move(rhs)).swap(*this). rhs is left in a valid but unspecified state after the assignment. 
3) Assigns the type and value of rhs, as if by any(std::forward&lt;ValueType&gt;(rhs)).swap(*this). This overload only participates in overload resolution if std::decay_t&lt;ValueType&gt; is not the same type as any and std::is_copy_constructible_v&lt;std::decay_t&lt;ValueType&gt;&gt; is true. . 

<h2>Template parameters</h2>

ValueType - contained value type

<h2>Type requirements</h2>

- 
std::decay_t&lt;ValueType&gt; must meet the requirements of CopyConstructible.

<h2>Parameters</h2>

rhs - object whose contained value to assign

<h2>Return value</h2>

*this 

<h2>Exceptions</h2>

1,3) Throws bad_alloc or any exception thrown by the constructor of the contained type. If an exception is thrown, there are no effects <i>(strong exception guarantee)</i>.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an any object 
constructor <i>(public member function)</i> 
