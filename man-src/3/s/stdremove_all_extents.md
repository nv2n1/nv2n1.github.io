---
title: "stdremove_all_extents(3)"
name: "stdremove_all_extents"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremove_all_extents/"
---

std::remove_all_extents - std::remove_all_extents

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct remove_all_extents;</code></pre> 
If T is a multidimensional array of some type X, provides the member typedef type equal to X, otherwise type is T. 

<h2>Member types</h2>

Name Definition 
type the type of the element of T

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using remove_all_extents_t = typename remove_all_extents&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct remove_all_extents { typedef T type;}; 

 
&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct remove_all_extents&lt;T[]&gt; { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename remove_all_extents&lt;T&gt;::type type; 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;template&lt;class T, std::size_t N&gt; 
&nbsp;<wbr>&nbsp;struct remove_all_extents&lt;T[N]&gt; { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename remove_all_extents&lt;T&gt;::type type; 
&nbsp;<wbr>&nbsp;};

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;

#include &lt;typeinfo&gt;
template &lt;class A&gt;

void foo(const A &amp;)

{
    typedef typename std::remove_all_extents&lt;A&gt;::type Type;
    std::cout &lt;&lt; &quot;underlying type: &quot; &lt;&lt; typeid(Type).name() &lt;&lt; '\n';
}
int main()

{
    float a1[1][2][3];
    int a2[3][2];
    float a3[1][1][1][1][2];
    double a4[2][3];
    foo(a1);
    foo(a2);
    foo(a3);
    foo(a4);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;underlying type: f 
&nbsp;<wbr>&nbsp;underlying type: i 
&nbsp;<wbr>&nbsp;underlying type: f 
&nbsp;<wbr>&nbsp;underlying type: d

<h2>See also</h2>

is_array checks if a type is an array type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
rank obtains the number of dimensions of an array type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
extent obtains the size of an array type along a specified dimension 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
remove_extent removes one extent from the given array type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
