---
title: "stdsqrtstdvalarray(3)"
name: "stdsqrtstdvalarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsqrtstdvalarray/"
---

std::sqrt(std::valarray) - std::sqrt(std::valarray)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;valarray&gt;

    template &lt;class T&gt;

    valarray&lt;T&gt; sqrt(const valarray&lt;T&gt; &amp;va);</code></pre> 
For each element in va computes the square root of the value of the element. 

<h2>Parameters</h2>

va - value array to apply the operation to

<h2>Return value</h2>

Value array containing square roots of the values in va. 

<h2>Notes</h2>

Unqualified function (sqrt) is used to perform the computation. If such function is not available, std::sqrt is used due to argument dependent lookup.

The function can be implemented with the return type different from std::valarray. In this case, the replacement type has the following properties:
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All const member functions of std::valarray are provided. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::valarray, std::slice_array, std::gslice_array, std::mask_array and std::indirect_array can be constructed from the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting an argument of type const std::valarray&amp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;except begin() and end() 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i> should also accept the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting two arguments of type const std::valarray&amp; should accept every combination of const std::valarray&amp; and the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The return type does not add more than two levels of template nesting over the most deeply-nested argument type. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;valarray&lt;T&gt; sqrt(const valarray&lt;T&gt;&amp; va) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;valarray&lt;T&gt; other = va; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (T &amp;i : other) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;i = sqrt(i); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return other; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Finds real roots of multiple quadratic equations. 
 // Run this code <pre><code>#include &lt;valarray&gt;

#include &lt;iostream&gt;
int main()

{
    std::valarray&lt;double&gt; a(1, 8);
    std::valarray&lt;double&gt; b{1, 2, 3, 4, 5, 6, 7, 8};
    std::valarray&lt;double&gt; c = -b;
    // literals must also be of type T (double in this case)
    std::valarray&lt;double&gt; d = std::sqrt((b * b - 4.0 * a * c));
    std::valarray&lt;double&gt; x1 = (-b - d) / (2.0 * a);
    std::valarray&lt;double&gt; x2 = (-b + d) / (2.0 * a);
    std::cout &lt;&lt; &quot;quadratic equation    root 1,  root 2&quot;
              &lt;&lt; &quot;\n&quot;;
    for (size_t i = 0; i &lt; a.size(); ++i) {
        std::cout &lt;&lt; a[i] &lt;&lt; &quot;x\u00B2 + &quot; &lt;&lt; b[i] &lt;&lt; &quot;x + &quot; &lt;&lt; c[i] &lt;&lt; &quot; = 0   &quot;;
        std::cout &lt;&lt; x1[i] &lt;&lt; &quot;, &quot; &lt;&lt; x2[i] &lt;&lt; &quot;\n&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;quadratic equation root 1, root 2 
&nbsp;<wbr>&nbsp;1x² + 1x + -1 = 0 -1.61803, 0.618034 
&nbsp;<wbr>&nbsp;1x² + 2x + -2 = 0 -2.73205, 0.732051 
&nbsp;<wbr>&nbsp;1x² + 3x + -3 = 0 -3.79129, 0.791288 
&nbsp;<wbr>&nbsp;1x² + 4x + -4 = 0 -4.82843, 0.828427 
&nbsp;<wbr>&nbsp;1x² + 5x + -5 = 0 -5.8541, 0.854102 
&nbsp;<wbr>&nbsp;1x² + 6x + -6 = 0 -6.87298, 0.872983 
&nbsp;<wbr>&nbsp;1x² + 7x + -7 = 0 -7.88748, 0.887482 
&nbsp;<wbr>&nbsp;1x² + 8x + -8 = 0 -8.89898, 0.898979

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::pow to two valarrays or a valarray and a value 
pow(std::valarray) <i>(function template)</i> 
sqrt 
sqrtf computes square root ( 
sqrtl √ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex square root in the range of the right half-plane 
sqrt(std::complex) <i>(function template)</i> 
