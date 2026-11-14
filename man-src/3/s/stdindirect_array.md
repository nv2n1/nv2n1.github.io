---
title: "stdindirect_array(3)"
name: "stdindirect_array"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdindirect_array/"
---

std::indirect_array - std::indirect_array

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;valarray&gt;

template&lt; class T &gt; class indirect_array;</code></pre> 
std::gslice_array is a helper template used by std::indirect_array subscript operator. It has reference semantics to a subset of the array specified by an indirect array (std::valarray&lt;std::size_t&gt; object). 

<h2>Member types</h2>

Type Definition 
value_type T

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a indirect_array 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a indirect_array 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns contents 
operator= <i>(public member function)</i> 

 
operator+= 
operator-= 
operator*= 
operator/= performs arithmetic operation on the array referred by indirect array. 
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
    std::valarray&lt;std::size_t&gt; idx = {0, 2, 4, 6, 8};
    std::cout &lt;&lt; &quot;Original valarray: &quot;;
    for (int n : data)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    data[idx] += data[idx]; // double the values at indexes 'idx'
    // the type of data[idx] is std::indirect_array&lt;int&gt;
    std::cout &lt;&lt; &quot;After indirect modification: &quot;;
    for (int n : data)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Original valarray: 0 1 2 3 4 5 6 7 8 9 
&nbsp;<wbr>&nbsp;After indirect modification: 0 1 4 3 8 5 12 7 16 9
