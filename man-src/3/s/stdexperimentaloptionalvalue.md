---
title: "stdexperimentaloptionalvalue(3)"
name: "stdexperimentaloptionalvalue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaloptionalvalue/"
---

std::experimental::optional&lt;T&gt;::value - std::experimental::optional&lt;T&gt;::value

<h2>Synopsis</h2>

<pre><code>constexpr T &amp;value() &amp;;
(1)(library fundamentals TS)

    constexpr const T &amp;value() const &amp;;

constexpr T &amp;&amp;value() &amp;&amp;;
(2)(library fundamentals TS)

    constexpr const T &amp;&amp;value() const &amp;&amp;;
Returns the contained value.

1) Equivalent to return bool(*this) ? *val : throw bad_optional_access();

2) Equivalent to return bool(*this) ? std::move(*val) : throw bad_optional_access();
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A reference to the contained value. 

<h2>Exceptions</h2>

std::experimental::bad_optional_access if *this does not contain a value.

<h2>Notes</h2>

The dereference operator operator*() does not check if this optional contains a value, which may be more efficient than value(). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;experimental/optional&gt;

#include &lt;iostream&gt;

int main()

{
    std::experimental::optional&lt;int&gt; opt = {};
    try {
        int n = opt.value();
    } catch (const std::logic_error &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;optional&lt;T&gt;::value: not engaged

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value if available, another value otherwise 
value_or <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the contained value 
operator-&gt; <i>(public member function)</i> 
operator* 
bad_optional_access exception indicating checked access to an optional that doesn't contain a value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(library fundamentals TS) 
