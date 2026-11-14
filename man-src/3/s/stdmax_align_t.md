---
title: "stdmax_align_t(3)"
name: "stdmax_align_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmax_align_t/"
---

std::max_align_t - std::max_align_t

<h2>Synopsis</h2>

Defined in header &lt;cstddef&gt; 
typedef /*implementation-defined*/ max_align_t; <i>(since C++11)</i> 
std::max_align_t is a trivial standard-layout type whose alignment_requirement is at least as strict (as large) as that of every scalar type. 

<h2>Notes</h2>

Pointers returned by allocation functions such as std::malloc are suitably aligned for any object, which means they are aligned at least as strictly as std::max_align_t. 
std::max_align_t is usually synonymous with the largest scalar type, which is long double on most platforms, and its alignment requirement is either 8 or 16. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstddef&gt;

int main()

{
    std::cout &lt;&lt; alignof(std::max_align_t) &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;16

<h2>See also</h2>

alignof_operator queries alignment requirements of a type <i>(since C++11)</i> 
alignment_of obtains the type's alignment requirements 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_scalar checks if a type is a scalar type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
