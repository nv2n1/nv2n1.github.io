---
title: "stdpowstdvalarray(3)"
name: "stdpowstdvalarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpowstdvalarray/"
---

std::pow(std::valarray) - std::pow(std::valarray)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;valarray&gt;

    template &lt;class T&gt;
    (1)

        std::valarray&lt;T&gt; pow(const std::valarray&lt;T&gt; &amp;base, const std::valarray&lt;T&gt; &amp;exp);

template &lt;class T&gt;

std::valarray&lt;T&gt; pow(const std::valarray&lt;T&gt; &amp;base, (2)

                                                       const typename std::valarray&lt;T&gt;::value_type &amp;vexp);

template &lt;class T&gt;

std::valarray&lt;T&gt; pow(const typename std::valarray&lt;T&gt;::value_type &amp;vbase, (3)

                                                                             const std::valarray&lt;T&gt; &amp;exp);</code></pre> 
Raises a value to a power. 
1) Computes the values of each element in the numeric array base raised to the power specified by the corresponding element from the numeric array exp. 
The behavior is undefined if base.size() != exp.size(). 
2) Computes the values of each element in the numeric array base raised to the power vexp. 
3) Computes the values of vbase raised to the power defined by the elements in the numeric array exp. 

<h2>Parameters</h2>

base - numeric array containing the values of the base 
exp - numeric array containing the values of the exponent 
vbase - a value defining the base 
vexp - a value defining the exponent

<h2>Return value</h2>

A numeric array containing the results of exponentiation. 

<h2>Notes</h2>

Unqualified function (pow) is used to perform the computation. If such function is not available, std::pow is used due to argument dependent lookup.

The function can be implemented with the return type different from std::valarray. In this case, the replacement type has the following properties:
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All const member functions of std::valarray are provided. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::valarray, std::slice_array, std::gslice_array, std::mask_array and std::indirect_array can be constructed from the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting an argument of type const std::valarray&amp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;except begin() and end() 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i> should also accept the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting two arguments of type const std::valarray&amp; should accept every combination of const std::valarray&amp; and the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The return type does not add more than two levels of template nesting over the most deeply-nested argument type. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. <pre><code>DR       Applied to Behavior as published                                                                      Correct behavior

LWG_3074 C++98      T is deduced from both the scalar and the valarray for (2-3), disallowing mixed-type calls only deduce T from the valarray

</code></pre>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::sqrt to each element of valarray 
sqrt(std::valarray) <i>(function template)</i> 
pow 
powf 
powl raises a number to the given power (xy) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex power, one or both arguments may be a complex number 
pow(std::complex) <i>(function template)</i> 
