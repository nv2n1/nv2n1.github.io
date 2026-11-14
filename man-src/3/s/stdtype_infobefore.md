---
title: "stdtype_infobefore(3)"
name: "stdtype_infobefore"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtype_infobefore/"
---

std::type_info::before - std::type_info::before

<h2>Synopsis</h2>

<pre><code>bool before(const type_info &amp;rhs) const;</code></pre> 
Returns true if the type of this type_info precedes the type of rhs in the implementation's collation order. No guarantees are given; in particular, the collation order can change between the invocations of the same program. 

<h2>Parameters</h2>

rhs - another type information object to compare to

<h2>Return value</h2>

true if the type of this type_info precedes the type of rhs in the implementation's collation order. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;typeinfo&gt;
int main()

{
    if (typeid(int).before(typeid(char)))
        std::cout &lt;&lt; &quot;int goes before char in this implementation.\n&quot;;
    else
        std::cout &lt;&lt; &quot;char goes before int in this implementation.\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;char goes before int in this implementation.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the objects refer to the same type 
operator== <i>(public member function)</i> 
operator!= 
