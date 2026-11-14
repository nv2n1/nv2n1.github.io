---
title: "stdrel_opsoperator(3)"
name: "stdrel_opsoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrel_opsoperator/"
---

std::rel_ops::operator!=,&gt;,&lt;=,&gt;= - std::rel_ops::operator!=,&gt;,&lt;=,&gt;=

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;utility&gt;

    template &lt;class T&gt;
    (1)(deprecated in C++ 20)

        bool
        operator!=(const T &amp;lhs, const T &amp;rhs);

template &lt;class T&gt;
(2)(deprecated in C++ 20)

    bool
    operator&gt;(const T &amp;lhs, const T &amp;rhs);

template &lt;class T&gt;
(3)(deprecated in C++ 20)

    bool
    operator&lt;=(const T &amp;lhs, const T &amp;rhs);

template &lt;class T&gt;
(4)(deprecated in C++ 20)

    bool
    operator&gt;=(const T &amp;lhs, const T &amp;rhs);</code></pre> 
Given a user-defined operator== and operator&lt; for objects of type T, implements the usual semantics of other comparison operators. 
1) Implements operator!= in terms of operator==. 
2) Implements operator&gt; in terms of operator&lt;. 
3) Implements operator&lt;= in terms of operator&lt;. 
4) Implements operator&gt;= in terms of operator&lt;. 

<h2>Parameters</h2>

lhs - left-hand argument 
rhs - right-hand argument

<h2>Return value</h2>

1) Returns true if lhs is not equal to rhs. 
2) Returns true if lhs is greater than rhs. 
3) Returns true if lhs is less or equal to rhs. 
4) Returns true if lhs is greater or equal to rhs. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;namespace rel_ops { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator!=( const T&amp; lhs, const T&amp; rhs ) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return !(lhs == rhs); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;namespace rel_ops { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator&gt;( const T&amp; lhs, const T&amp; rhs ) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return rhs &lt; lhs; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;namespace rel_ops { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator&lt;=( const T&amp; lhs, const T&amp; rhs ) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return !(rhs &lt; lhs); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} 

 
Fourth version 

 
&nbsp;<wbr>&nbsp;namespace rel_ops { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool operator&gt;=( const T&amp; lhs, const T&amp; rhs ) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return !(lhs &lt; rhs); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

Boost.operators provides a more versatile alternative to std::rel_ops 
As of C++20, std::rel_ops are deprecated in favor of operator&lt;=&gt;. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;
struct Foo {
    int n;
};
bool operator==(const Foo &amp;lhs, const Foo &amp;rhs)

{
    return lhs.n == rhs.n;
}
bool operator&lt;(const Foo &amp;lhs, const Foo &amp;rhs)

{
    return lhs.n &lt; rhs.n;
}
int main()

{
    Foo f1 = {1};
    Foo f2 = {2};
    using namespace std::rel_ops;
    std::cout &lt;&lt; std::boolalpha;
    std::cout &lt;&lt; &quot;not equal?     : &quot; &lt;&lt; (f1 != f2) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;greater?       : &quot; &lt;&lt; (f1 &gt; f2) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;less equal?    : &quot; &lt;&lt; (f1 &lt;= f2) &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;greater equal? : &quot; &lt;&lt; (f1 &gt;= f2) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;not equal? : true 
&nbsp;<wbr>&nbsp;greater? : false 
&nbsp;<wbr>&nbsp;less equal? : true 
&nbsp;<wbr>&nbsp;greater equal? : false
