---
title: "stdnegate(3)"
name: "stdnegate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnegate/"
---

std::negate&lt;void&gt; - std::negate&lt;void&gt;

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;functional&gt;

    template &lt;&gt;
    (since C++ 14)

        class negate&lt;void&gt;;</code></pre> 
std::negate&lt;&gt; is a specialization of std::negate with parameter and return type deduced. 

<h2>Member types</h2>

Member type Definition 
is_transparent /* unspecified */

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns its negated argument 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::negate&lt;&gt;::operator() 

 

 
template&lt; class T &gt; 
constexpr auto operator()( T&amp;&amp; arg ) const 
-&gt; decltype(-std::forward&lt;T&gt;(arg)); 

 
Returns the result of negating arg (or whatever the unary operator- is overloaded to do)

<h2>Parameters</h2>

arg - value to negate

<h2>Return value</h2>

The result of -arg. 

<h2>Notes</h2>

The member type is_transparent indicates to the caller that this function object is a transparent function object: it accepts arguments of arbitrary types and uses perfect forwarding, which avoids unnecessary copying and conversion when the function object is used in heterogeneous context, or with rvalue arguments. In particular, template functions such as std::set::find and std::set::lower_bound make use of this member type on their Compare types. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
