---
title: "stdpiecewise_construct(3)"
name: "stdpiecewise_construct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpiecewise_construct/"
---

std::piecewise_construct - std::piecewise_construct

<h2>Synopsis</h2>

<pre><code>constexpr piecewise_construct_t piecewise_construct         (since C++11)

= std::piecewise_construct_t();                             (until C++17)

inline constexpr piecewise_construct_t piecewise_construct  (since C++17)

= std::piecewise_construct_t();</code></pre> 
The constant std::piecewise_construct is an instance of an empty struct tag type std::piecewise_construct_t. 

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

piecewise_construct_t tag type used to select correct function overload for piecewise construction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new pair 
constructor <i>(public member function of std::pair&lt;T1,T2&gt;)</i> 
