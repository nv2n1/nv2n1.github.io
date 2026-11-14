---
title: "stdnothrow(3)"
name: "stdnothrow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnothrow/"
---

std::nothrow - std::nothrow

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;new&gt;

    extern const std::nothrow_t nothrow;</code></pre> 
std::nothrow is a constant of type std::nothrow_t used to disambiguate the overloads of throwing and non-throwing allocation_functions. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;new&gt;
int main()

{
    try {
        while (true) {
            new int[100000000ul]; // throwing overload
        }
    } catch (const std::bad_alloc &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '\n';
    }
    while (true) {
        int *p = new (std::nothrow) int[100000000ul]; // non-throwing overload
        if (p == nullptr) {
            std::cout &lt;&lt; &quot;Allocation returned nullptr\n&quot;;
            break;
        }
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;std::bad_alloc 
&nbsp;<wbr>&nbsp;Allocation returned nullptr

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tag type used to select an non-throwing allocation function 
nothrow_t <i>(class)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions 
operator_new <i>(function)</i> 
operator_new[] 
