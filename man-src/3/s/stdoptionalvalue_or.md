---
title: "stdoptionalvalue_or(3)"
name: "stdoptionalvalue_or"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoptionalvalue_or/"
description: "std::optional<T>::value_or – std::optional<T>::value_or"
---

<p>std::optional&lt;T&gt;::value_or &#8211; std::optional&lt;T&gt;::value_or</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class U&gt;
(since C++ 17)

    constexpr T value_or(U &amp;&amp;default_value) const &amp;;

template &lt;class U&gt;
(since C++ 17)

    constexpr T value_or(U &amp;&amp;default_value) &amp;&amp;;</code></pre>
<p>Returns the contained value if *this has a value, otherwise returns default_value.<br />
1) Equivalent to bool(*this) ? **this : static_cast&lt;T&gt;(std::forward&lt;U&gt;(default_value))<br />
2) Equivalent to bool(*this) ? std::move(**this) : static_cast&lt;T&gt;(std::forward&lt;U&gt;(default_value)) </p>
<h2>Parameters</h2>
<p>default_value &#8211; the value to use in case *this is empty</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
T must meet the requirements of CopyConstructible in order to use overload <code>(1)</code>.<br />
&#8211;<br />
T must meet the requirements of MoveConstructible in order to use overload <code>(2)</code>.<br />
&#8211;<br />
U&amp;&amp; must be convertible to T</p>
<h2>Return value</h2>
<p>The current value if *this has a value, or default_value otherwise. </p>
<h2>Exceptions</h2>
<p>Any exception thrown by the selected constructor of the return value T.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;optional&gt;

#include &lt;iostream&gt;

#include &lt;cstdlib&gt;
std::optional&lt;const char *&gt; maybe_getenv(const char *n)

{
    if (const char *x = std::getenv(n))
        return x;
    else
        return {};
}

int main()

{
    std::cout &lt;&lt; maybe_getenv(&quot;MYPWD&quot;).value_or(&quot;(none)&quot;) &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;<i>(none)</i></p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the contained value<br />
value <i>(public member function)</i> </p>
