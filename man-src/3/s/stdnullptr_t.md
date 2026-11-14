---
title: "stdnullptr_t(3)"
name: "stdnullptr_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnullptr_t/"
---

std::nullptr_t - std::nullptr_t

<h2>Synopsis</h2>

Defined in header &lt;cstddef&gt; 
typedef decltype(nullptr) nullptr_t; <i>(since C++11)</i> 
std::nullptr_t is the type of the null pointer literal, nullptr. It is a distinct type that is not itself a pointer type or a pointer to member type. 

<h2>Example</h2>

If two or more overloads accept different pointer types, an overload for std::nullptr_t is necessary to accept a null pointer argument. 
 // Run this code <pre><code>#include &lt;cstddef&gt;

#include &lt;iostream&gt;
void f(int *pi)

{
    std::cout &lt;&lt; &quot;Pointer to integer overload\n&quot;;
}
void f(double *pd)

{
    std::cout &lt;&lt; &quot;Pointer to double overload\n&quot;;
}
void f(std::nullptr_t nullp)

{
    std::cout &lt;&lt; &quot;null pointer overload\n&quot;;
}
int main()

{
    int *pi;
    double *pd;
    f(pi);
    f(pd);
    f(nullptr); // would be ambiguous without void f(nullptr_t)
    // f(0);  // ambiguous call: all three functions are candidates
    // f(NULL); // ambiguous if NULL is an integral null pointer constant
    // (as is the case in most implementations)
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Pointer to integer overload 
&nbsp;<wbr>&nbsp;Pointer to double overload 
&nbsp;<wbr>&nbsp;null pointer overload

<h2>See also</h2>

nullptr the pointer literal which specifies a null pointer value <i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implementation-defined null pointer constant 
NULL (macro constant) 
is_null_pointer checks if a type is std::nullptr_t 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++14)</i> 
