---
title: "stdexperimentaloptionalvalue_or(3)"
name: "stdexperimentaloptionalvalue_or"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaloptionalvalue_or/"
---

std::experimental::optional&lt;T&gt;::value_or - std::experimental::optional&lt;T&gt;::value_or

<h2>Synopsis</h2>

<pre><code>template &lt;class U&gt;
(library fundamentals TS)

    constexpr T value_or(U &amp;&amp;default_value) const &amp;;

template &lt;class U&gt;
(library fundamentals TS)

    constexpr T value_or(U &amp;&amp;default_value) &amp;&amp;;</code></pre> 
Returns the contained value if *this has a value, otherwise returns default_value. 
1) Equivalent to bool(*this) ? **this : static_cast&lt;T&gt;(std::forward&lt;U&gt;(default_value)) 
2) Equivalent to bool(*this) ? std::move(**this) : static_cast&lt;T&gt;(std::forward&lt;U&gt;(default_value)) 

<h2>Parameters</h2>

default_value - the value to use in case *this is empty

<h2>Type requirements</h2>

- 
T must meet the requirements of CopyConstructible in order to use overload <b>(1)</b>. 
- 
T must meet the requirements of MoveConstructible in order to use overload <b>(2)</b>. 
- 
U&amp;&amp; must be convertible to T

<h2>Return value</h2>

The current value if *this has a value, or default_value otherwise. 

<h2>Exceptions</h2>

Any exception thrown by the selected constructor of the return value T.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;experimental/optional&gt;

#include &lt;iostream&gt;

#include &lt;cstdlib&gt;
std::experimental::optional&lt;const char *&gt; maybe_getenv(const char *n)

{
    if (const char *x = std::getenv(n))
        return x;
    else
        return {};
}

int main()

{
    std::cout &lt;&lt; maybe_getenv(&quot;MYPWD&quot;).value_or(&quot;(none)&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;<i>(none)</i>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value 
value <i>(public member function)</i> 
