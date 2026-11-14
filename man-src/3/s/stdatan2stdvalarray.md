---
title: "stdatan2stdvalarray(3)"
name: "stdatan2stdvalarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatan2stdvalarray/"
---

std::atan2(std::valarray) - std::atan2(std::valarray)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;valarray&gt;

    template &lt;class T&gt;
    (1)

        std::valarray&lt;T&gt; atan2(const std::valarray&lt;T&gt; &amp;y, const std::valarray&lt;T&gt; &amp;x);

template &lt;class T&gt;

std::valarray&lt;T&gt; atan2(const std::valarray&lt;T&gt; &amp;y, (2)

                                                      const typename std::valarray&lt;T&gt;::value_type &amp;vx);

template &lt;class T&gt;

std::valarray&lt;T&gt; atan2(const typename std::valarray&lt;T&gt;::value_type &amp;vy, (3)

                                                                            const std::valarray&lt;T&gt; &amp;x);</code></pre> 
Computes the inverse tangent of y/x using the signs of arguments to correctly determine quadrant. 
1) Computes the inverse tangent of each pair of corresponding values from y and x. 
The behavior is undefined if x.size() != y.size(). 
2) Computes the inverse tangent of vx and each value in the numeric array y. 
3) Computes the inverse tangent of vy and each value in the numeric array x. 

<h2>Parameters</h2>

x, y - numeric arrays to compute inverse tangent of 
vy, vx - values to compute inverse tangent of

<h2>Return value</h2>

A numeric array containing the results of computation of inverse tangent. 

<h2>Notes</h2>

Unqualified function (atan2) is used to perform the computation. If such function is not available, std::atan2 is used due to argument dependent lookup.

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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::asin to each element of valarray 
asin(std::valarray) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::acos to each element of valarray 
acos(std::valarray) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::atan to each element of valarray 
atan(std::valarray) <i>(function template)</i> 
atan2 
atan2f 
atan2l arc tangent, using signs to determine quadrants 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the phase angle 
arg <i>(function template)</i> 
