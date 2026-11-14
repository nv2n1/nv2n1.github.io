---
title: "stdbit_xor(3)"
name: "stdbit_xor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbit_xor/"
---

std::bit_xor&lt;void&gt; - std::bit_xor&lt;void&gt;

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;functional&gt;

    template &lt;&gt;
    (since C++ 14)

        class bit_xor&lt;void&gt;;</code></pre> 
std::bit_xor&lt;&gt; is a specialization of std::bit_xor with parameter and return type deduced. 

<h2>Member types</h2>

Member type Definition 
is_transparent /* unspecified */

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies operator^ to lhs and rhs 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::bit_xor&lt;&gt;::operator() 

 

 
template&lt; class T, class U&gt; 
constexpr auto operator()( T&amp;&amp; lhs, U&amp;&amp; rhs ) const 
-&gt; decltype(std::forward&lt;T&gt;(lhs) ^ std::forward&lt;U&gt;(rhs)); 

 
Returns the result of lhs ^ rhs.

<h2>Parameters</h2>

lhs, rhs - values to compute bitwise XOR for

<h2>Return value</h2>

The result of lhs ^ rhs. 

<h2>Notes</h2>

The member type is_transparent indicates to the caller that this function object is a transparent function object: it accepts arguments of arbitrary types and uses perfect forwarding, which avoids unnecessary copying and conversion when the function object is used in heterogeneous context, or with rvalue arguments. In particular, template functions such as std::set::find and std::set::lower_bound make use of this member type on their Compare types. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
