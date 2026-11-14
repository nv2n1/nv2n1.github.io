---
title: "stdexpstdvalarray(3)"
name: "stdexpstdvalarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexpstdvalarray/"
---

std::exp(std::valarray) - std::exp(std::valarray)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;valarray&gt;

    template &lt;class T&gt;

    valarray&lt;T&gt; exp(const valarray&lt;T&gt; &amp;va);</code></pre> 
For each element in va computes e raised to the power equal to the value of the element. 

<h2>Parameters</h2>

va - value array to apply the operation to

<h2>Return value</h2>

Value array containing e raised by the values in va. 

<h2>Notes</h2>

Unqualified function (exp) is used to perform the computation. If such function is not available, std::exp is used due to argument dependent lookup.

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
&nbsp;<wbr>&nbsp;valarray&lt;T&gt; exp( const valarray&lt;T&gt;&amp; va ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;valarray&lt;T&gt; other = va; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (T &amp;i : other) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;i = exp(i); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return other; // proxy object may be returned 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

This example demonstrates the Euler's identity eiπ 
= -1 and the related exponents. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;

#include &lt;valarray&gt;
int main()

{
    const double pi = std::acos(-1);
    std::valarray&lt;std::complex&lt;double&gt;&gt; v = {
        {0, 0}, {0, pi / 2}, {0, pi}, {0, 3 * pi / 2}, {0, 2 * pi}};
    std::valarray&lt;std::complex&lt;double&gt;&gt; v2 = std::exp(v);
    for (auto n : v2) {
        std::cout &lt;&lt; std::fixed &lt;&lt; n &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(1.000000,0.000000) 
&nbsp;<wbr>&nbsp;(0.000000,1.000000) 
&nbsp;<wbr>&nbsp;(-1.000000,0.000000) 
&nbsp;<wbr>&nbsp;(-0.000000,-1.000000) 
&nbsp;<wbr>&nbsp;(1.000000,-0.000000)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::log to each element of valarray 
log(std::valarray) <i>(function template)</i> 
exp 
expf 
expl returns e raised to the given power (ex) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex base e exponential 
exp(std::complex) <i>(function template)</i> 
