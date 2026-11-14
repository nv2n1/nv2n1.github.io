---
title: "stdexperimentalrangesidentity(3)"
name: "stdexperimentalrangesidentity"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesidentity/"
---

std::experimental::ranges::identity - std::experimental::ranges::identity

<h2>Synopsis</h2>

Defined in header &lt;experimental/ranges/functional&gt; 
struct identity; (ranges TS) 
ranges::identity is a function object type whose operator() returns its argument unchanged. It is used as the default projection for all Ranges TS algorithms. 

<h2>Member types</h2>

Member type Definition 
is_transparent /* unspecified */

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the argument unchanged 
operator() <i>(public member function)</i> 

 

 
&nbsp;std::experimental::ranges::identity::operator() 

 

 
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
