---
title: "stdremove_reference(3)"
name: "stdremove_reference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremove_reference/"
---

std::remove_reference - std::remove_reference

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct remove_reference;</code></pre> 
If the type T is a reference type, provides the member typedef type which is the type referred to by T. Otherwise type is T. 

<h2>Member types</h2>

Name Definition 
type the type referred by T or T if it is not a reference

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using remove_reference_t = typename remove_reference&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_reference {typedef T type;}; 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_reference&lt;T&amp;&gt; {typedef T type;}; 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; struct remove_reference&lt;T&amp;&amp;&gt; {typedef T type;};

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt; // std::cout

#include &lt;type_traits&gt; // std::is_same
template &lt;class T1, class T2&gt;

void print_is_same()
{
    std::cout &lt;&lt; std::is_same&lt;T1, T2&gt;() &lt;&lt; '\n';
}
int main()
{
    std::cout &lt;&lt; std::boolalpha;
    print_is_same&lt;int, int&gt;();
    print_is_same&lt;int, int &amp;&gt;();
    print_is_same&lt;int, int &amp;&amp;&gt;();
    print_is_same&lt;int, std::remove_reference&lt;int&gt;::type&gt;();
    print_is_same&lt;int, std::remove_reference&lt;int &amp;&gt;::type&gt;();
    print_is_same&lt;int, std::remove_reference&lt;int &amp;&amp;&gt;::type&gt;();
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;false 
&nbsp;<wbr>&nbsp;false 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true

<h2>See also</h2>

is_reference checks if a type is either a lvalue reference or rvalue reference 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
add_lvalue_reference 
add_rvalue_reference adds a lvalue or rvalue reference to the given type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
remove_cvref combines std::remove_cv and std::remove_reference 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(C++20) 
