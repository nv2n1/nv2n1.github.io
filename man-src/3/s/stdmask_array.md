---
title: "stdmask_array(3)"
name: "stdmask_array"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmask_array/"
---

std::mask_array - std::mask_array

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;valarray&gt;

template&lt; class T &gt; class mask_array;</code></pre> 
std::mask_array is a helper template used by the valarray_subscript_operator with std::valarray&lt;bool&gt; argument. It has reference semantics and provides access to the subset of the valarray consisting of the elements whose indices correspond to true values in the std::valarray&lt;bool&gt; mask. 

<h2>Member types</h2>

Type Definition 
value_type T

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a mask_array 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a mask_array 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns contents 
operator= <i>(public member function)</i> 

 
operator+= 
operator-= 
operator*= 
operator/= performs arithmetic operation on the array referred by mask. 
operator%= <i>(public member function)</i> 
operator&amp;= 
operator|= 
operator^= 
operator&lt;&lt;= 
operator&gt;&gt;=

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;valarray&gt;
int main()

{
    std::valarray&lt;int&gt; data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::cout &lt;&lt; &quot;Initial valarray: &quot;;
    for (int n : data)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    data[data &gt; 5] = -1;
    // the type of data&gt;5 is std::valarray&lt;bool&gt;
    // the type of data[data&gt;5] is std::mask_array&lt;int&gt;
    std::cout &lt;&lt; &quot;After v[v&gt;5]=-1:  &quot;;
    for (int n : data)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Initial valarray: 0 1 2 3 4 5 6 7 8 9 
&nbsp;<wbr>&nbsp;After v[v&gt;5]=-1: 0 1 2 3 4 5 -1 -1 -1 -1
