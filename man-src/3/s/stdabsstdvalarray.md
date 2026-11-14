---
title: "stdabsstdvalarray(3)"
name: "stdabsstdvalarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdabsstdvalarray/"
---

std::abs(std::valarray) - std::abs(std::valarray)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;valarray&gt;

    template &lt;class T&gt;

    valarray&lt;T&gt; abs(const valarray&lt;T&gt; &amp;va);</code></pre> 
Computes absolute value of each element in the value array. 

<h2>Parameters</h2>

va - value array to apply the operation to

<h2>Return value</h2>

Value array containing absolute values of the values in va. 

<h2>Notes</h2>

Unqualified function (abs) is used to perform the computation. If such function is not available, std::abs is used due to argument dependent lookup.

The function can be implemented with the return type different from std::valarray. In this case, the replacement type has the following properties:
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All const member functions of std::valarray are provided. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::valarray, std::slice_array, std::gslice_array, std::mask_array and std::indirect_array can be constructed from the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting an argument of type const std::valarray&amp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;except begin() and end() 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i> should also accept the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting two arguments of type const std::valarray&amp; should accept every combination of const std::valarray&amp; and the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The return type does not add more than two levels of template nesting over the most deeply-nested argument type. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;valarray&lt;T&gt; abs( const valarray&lt;T&gt;&amp; va ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;valarray&lt;T&gt; other = va; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (T &amp;i : other) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;i = abs(i); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return other; // proxy object may be returned 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;valarray&gt;

#include &lt;iostream&gt;
int main()

{
    std::valarray&lt;int&gt; v{1, -2, 3, -4, 5, -6, 7, -8};
    std::valarray&lt;int&gt; v2 = std::abs(v);
    for (auto n : v2) {
        std::cout &lt;&lt; n &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 3 4 5 6 7 8

<h2>See also</h2>

abs(int) 
labs 
llabs computes absolute value of an integral value (|x|) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
abs(float) 
fabs 
fabsf 
fabsl absolute value of a floating point value (|x|) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number 
abs(std::complex) <i>(function template)</i> 
