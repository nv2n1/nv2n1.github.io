---
title: "stdconditional(3)"
name: "stdconditional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdconditional/"
---

std::conditional - std::conditional

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;bool B, class T, class F&gt;
    (since C++ 11)

        struct conditional;</code></pre> 
Provides member typedef type, which is defined as T if B is true at compile time, or as F if B is false. 

<h2>Member types</h2>

Member type Definition 
type T if B == true, F if B == false

<h2>Helper types</h2>

template&lt; bool B, class T, class F &gt; <i>(since C++14)</i> 
using conditional_t = typename conditional&lt;B,T,F&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;bool B, class T, class F&gt; 
&nbsp;<wbr>&nbsp;struct conditional { typedef T type; }; 

 
&nbsp;<wbr>&nbsp;template&lt;class T, class F&gt; 
&nbsp;<wbr>&nbsp;struct conditional&lt;false, T, F&gt; { typedef F type; };

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;typeinfo&gt;
int main()

{
    typedef std::conditional&lt;true, int, double&gt;::type Type1;
    typedef std::conditional&lt;false, int, double&gt;::type Type2;
    typedef std::conditional&lt;sizeof(int) &gt;= sizeof(double), int, double&gt;::type Type3;
    std::cout &lt;&lt; typeid(Type1).name() &lt;&lt; '\n';
    std::cout &lt;&lt; typeid(Type2).name() &lt;&lt; '\n';
    std::cout &lt;&lt; typeid(Type3).name() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;int 
&nbsp;<wbr>&nbsp;double 
&nbsp;<wbr>&nbsp;double

<h2>See also</h2>

enable_if hides a function overload or template specialization based on compile-time boolean 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
