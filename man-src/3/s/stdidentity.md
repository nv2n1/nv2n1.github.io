---
title: "stdidentity(3)"
name: "stdidentity"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdidentity/"
---

std::identity - std::identity

<h2>Synopsis</h2>

Defined in header &lt;functional&gt; 
struct identity; <i>(since C++20)</i> 
std::identity is a function object type whose operator() returns its argument unchanged. 

<h2>Member types</h2>

Member type Definition 
is_transparent /* unspecified */

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the argument unchanged 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::identity::operator() 

 

 
template&lt; class T&gt; 
constexpr T&amp;&amp; operator()( T&amp;&amp; t ) const noexcept; 

 
Returns std::forward&lt;T&gt;(t).

<h2>Parameters</h2>

t - argument to return

<h2>Return value</h2>

std::forward&lt;T&gt;(t). 

<h2>Notes</h2>

The member type is_transparent indicates to the caller that this function object is a transparent function object: it accepts arguments of arbitrary types and uses perfect forwarding, which avoids unnecessary copying and conversion when the function object is used in heterogeneous context, or with rvalue arguments. In particular, template functions such as std::set::find and std::set::lower_bound make use of this member type on their Compare types. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
