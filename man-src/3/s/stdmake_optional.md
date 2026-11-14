---
title: "stdmake_optional(3)"
name: "stdmake_optional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_optional/"
---

std::make_optional - std::make_optional

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;optional&gt;

    template &lt;class T&gt;
    (1)(since C++ 17)

        constexpr std::optional&lt;std::decay_t&lt;T&gt;&gt; make_optional(T &amp;&amp;value);

template &lt;class T, class... Args&gt;
(2)(since C++ 17)

    constexpr std::optional&lt;T&gt; make_optional(Args &amp;&amp;...args);

template &lt;class T, class U, class... Args&gt;
(3)(since C++ 17)

    constexpr std::optional&lt;T&gt; make_optional(std::initializer_list&lt;U&gt; il, Args &amp;&amp;...args);
1) Creates an optional object from value. Effectively calls std::optional&lt;std::decay_t&lt;T&gt;&gt;(std::forward&lt;T&gt;(value))

2) Creates an optional object constructed in-place from args.... Equivalent to return std::optional&lt;T&gt;(std::in_place, std::forward&lt;Args&gt;(args)...);.

3) Creates an optional object constructed in-place from il and args.... Equivalent to return std::optional&lt;T&gt;(std::in_place, il, std::forward&lt;Args&gt;(args)...);
.
</code></pre>

<h2>Parameters</h2>

value - the value to construct optional object with 
il, args - arguments to be passed to the constructor of T.

<h2>Return value</h2>

The constructed optional object. 

<h2>Exceptions</h2>

Throws any exception thrown by the constructor of T.

<h2>Notes</h2>

T need not be movable for overloads (2-3) due to guaranteed copy elision. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the optional object 
constructor <i>(public member function)</i> 
