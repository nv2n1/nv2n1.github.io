---
title: "stdget_pointer_safety(3)"
name: "stdget_pointer_safety"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdget_pointer_safety/"
---

std::get_pointer_safety - std::get_pointer_safety

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
std::pointer_safety get_pointer_safety() noexcept; <i>(since C++11)</i> 
Obtains the implementation-defined pointer safety model, which is a value of type std::pointer_safety. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The pointer safety used by this implementation. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
int main()

{
    std::cout &lt;&lt; &quot;Pointer safety: &quot;;
    switch (std::get_pointer_safety()) {
    case std::pointer_safety::strict:
        std::cout &lt;&lt; &quot;strict\n&quot;;
        break;
    case std::pointer_safety::preferred:
        std::cout &lt;&lt; &quot;preferred\n&quot;;
        break;
    case std::pointer_safety::relaxed:
        std::cout &lt;&lt; &quot;relaxed\n&quot;;
        break;
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Pointer safety: relaxed

<h2>See also</h2>

pointer_safety lists pointer safety models 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
