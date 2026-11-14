---
title: "stdpiecewise_construct_t(3)"
name: "stdpiecewise_construct_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpiecewise_construct_t/"
---

std::piecewise_construct_t - std::piecewise_construct_t

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;utility&gt;

    struct piecewise_construct_t {
};
(since C++ 11)(until C++ 17)

    struct piecewise_construct_t {
    explicit piecewise_construct_t() = default;
};
(since C++ 17)</code></pre> 
std::piecewise_construct_t is an empty struct tag type used to disambiguate between different functions that take two tuple arguments. 
The overloads that do not use std::piecewise_construct_t assume that each tuple argument becomes the element of a pair. The overloads that use std::piecewise_construct_t assume that each tuple argument is used to construct, piecewise, a new object of specified type, which will become the element of the pair. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;

#include &lt;tuple&gt;
struct Foo {
    Foo(std::tuple&lt;int, float&gt;)
    {
        std::cout &lt;&lt; &quot;Constructed a Foo from a tuple\n&quot;;
    }
    Foo(int, float)
    {
        std::cout &lt;&lt; &quot;Constructed a Foo from an int and a float\n&quot;;
    }
};
int main()

{
    std::tuple&lt;int, float&gt; t(1, 3.14);
    std::pair&lt;Foo, Foo&gt; p1(t, t);
    std::pair&lt;Foo, Foo&gt; p2(std::piecewise_construct, t, t);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Constructed a Foo from a tuple 
&nbsp;<wbr>&nbsp;Constructed a Foo from a tuple 
&nbsp;<wbr>&nbsp;Constructed a Foo from an int and a float 
&nbsp;<wbr>&nbsp;Constructed a Foo from an int and a float

<h2>See also</h2>

piecewise_construct an object of type piecewise_construct_t used to disambiguate functions for piecewise construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(constant) 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new pair 
constructor <i>(public member function of std::pair&lt;T1,T2&gt;)</i> 
