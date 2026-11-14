---
title: "stdremove_extent(3)"
name: "stdremove_extent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremove_extent/"
---

std::remove_extent - std::remove_extent

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct remove_extent;</code></pre> 
If T is an array of some type X, provides the member typedef type equal to X, otherwise type is T. Note that if T is a multidimensional array, only the first dimension is removed. 

<h2>Member types</h2>

Name Definition 
type the type of the element of T

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using remove_extent_t = typename remove_extent&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct remove_extent { typedef T type; }; 

 
&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct remove_extent&lt;T[]&gt; { typedef T type; }; 

 
&nbsp;<wbr>&nbsp;template&lt;class T, std::size_t N&gt; 
&nbsp;<wbr>&nbsp;struct remove_extent&lt;T[N]&gt; { typedef T type; };

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;algorithm&gt;

#include &lt;type_traits&gt;
template &lt;class A&gt;

typename std::enable_if&lt;std::rank&lt;A&gt;::value == 1&gt;::type

print_1d(const A &amp;a)

{
    copy(a, a + std::extent&lt;A&gt;::value,
         std::ostream_iterator&lt;typename std::remove_extent&lt;A&gt;::type&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; '\n';
}
int main()

{
    int a[][3] = &#123;&#123;1, 2, 3}, {4, 5, 6}};

    //  print_1d(a); // compile-time error
    print_1d(a[1]);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4 5 6

<h2>See also</h2>

is_array checks if a type is an array type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
rank obtains the number of dimensions of an array type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
extent obtains the size of an array type along a specified dimension 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
remove_all_extents removes all extents from the given array type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
