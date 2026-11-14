---
title: "stdas_const(3)"
name: "stdas_const"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdas_const/"
---

std::as_const - std::as_const

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;utility&gt;

    template &lt;class T&gt;
    (1)(since C++ 17)

        constexpr std::add_const_t&lt;T&gt; &amp;as_const(T &amp;t) noexcept;

template &lt;class T&gt;
(2)(since C++ 17)

    void as_const(const T &amp;&amp;) = delete;</code></pre> 
1) Forms lvalue reference to const type of t 
2) const rvalue reference overload is deleted to disallow rvalue arguments 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;constexpr std::add_const_t&lt;T&gt;&amp; as_const(T&amp; t) noexcept 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return t; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;string&gt;

#include &lt;cassert&gt;

#include &lt;utility&gt;

#include &lt;type_traits&gt;
int main()

{
    std::string mutableString = &quot;Hello World!&quot;;
    const std::string &amp;constView = std::as_const(mutableString);
    assert(&amp;constView == &amp;mutableString);
    assert(&amp;std::as_const(mutableString) == &amp;mutableString);
    using WhatTypeIsIt = std::remove_reference_t&lt;decltype(std::as_const(mutableString))&gt;;
    static_assert(std::is_same&lt;std::remove_const_t&lt;WhatTypeIsIt&gt;, std::string&gt;::value,
                  &quot;WhatTypeIsIt should be some kind of string.&quot;);
    static_assert(!std::is_same&lt;WhatTypeIsIt, std::string&gt;::value,
                  &quot;WhatTypeIsIt shouldn't be a mutable string.&quot;);
}
</code></pre>

<h2>See also</h2>

is_const checks if a type is const-qualified 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
add_cv 
add_const 
add_volatile adds const or/and volatile specifiers to the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
remove_cv 
remove_const 
remove_volatile removes const or/and volatile specifiers from the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
