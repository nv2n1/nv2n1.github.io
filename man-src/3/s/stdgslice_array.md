---
title: "stdgslice_array(3)"
name: "stdgslice_array"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgslice_array/"
---

std::gslice_array - std::gslice_array

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;valarray&gt;

template&lt; class T &gt; class gslice_array;</code></pre> 
std::gslice_array is a helper template used by std::gslice subscript operator. It has reference semantics to a subset of the array specified by the std::gslice object. 

<h2>Member types</h2>

Type Definition 
value_type T

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a gslice_array 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a gslice_array 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns contents 
operator= <i>(public member function)</i> 

 
operator+= 
operator-= 
operator*= 
operator/= performs arithmetic operation on the array referred by generic slice. 
operator%= <i>(public member function)</i> 
operator&amp;= 
operator|= 
operator^= 
operator&lt;&lt;= 
operator&gt;&gt;=

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;proxy to a subset of a valarray after applying a slice 
slice_array <i>(class template)</i> 
