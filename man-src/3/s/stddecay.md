---
title: "stddecay(3)"
name: "stddecay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddecay/"
---

std::decay - std::decay

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 11)

        struct decay;</code></pre> 
Applies lvalue-to-rvalue, array-to-pointer, and function-to-pointer implicit conversions to the type T, removes cv-qualifiers, and defines the resulting type as the member typedef type. Formally: 
* If T names the type &quot;array of U&quot; or &quot;reference to array of U&quot;, the member typedef type is U*. 
* Otherwise, if T is a function type F or a reference thereto, the member typedef type is std::add_pointer&lt;F&gt;::type. 
* Otherwise, the member typedef type is std::remove_cv&lt;std::remove_reference&lt;T&gt;::type&gt;::type. 
These conversions model the type conversion applied to all function arguments when passed by value. 

<h2>Member types</h2>

Name Definition 
type the result of applying the decay type conversions to T

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++14)</i> 
using decay_t = typename decay&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;struct decay { 
&nbsp;<wbr>&nbsp;private: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::remove_reference&lt;T&gt;::type U; 
&nbsp;<wbr>&nbsp;public: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::conditional&lt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_array&lt;U&gt;::value, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::remove_extent&lt;U&gt;::type*, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::conditional&lt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_function&lt;U&gt;::value, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::add_pointer&lt;U&gt;::type, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::remove_cv&lt;U&gt;::type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt;::type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt;::type type; 
&nbsp;<wbr>&nbsp;};

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
template &lt;typename T, typename U&gt;

struct decay_equiv : std::is_same&lt;typename std::decay&lt;T&gt;::type, U&gt;::type

{
};
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; decay_equiv&lt;int, int&gt;::value &lt;&lt; '\n'
              &lt;&lt; decay_equiv&lt;int &amp;, int&gt;::value &lt;&lt; '\n'
              &lt;&lt; decay_equiv&lt;int &amp;&amp;, int&gt;::value &lt;&lt; '\n'
              &lt;&lt; decay_equiv&lt;const int &amp;, int&gt;::value &lt;&lt; '\n'
              &lt;&lt; decay_equiv&lt;int[2], int *&gt;::value &lt;&lt; '\n'
              &lt;&lt; decay_equiv&lt;int(int), int (*)(int)&gt;::value &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true 
&nbsp;<wbr>&nbsp;true

<h2>See also</h2>

remove_cvref combines std::remove_cv and std::remove_reference 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(C++20) 
implicit_conversion array-to-pointer, function-to-pointer, lvalue-to-rvalue conversions 
