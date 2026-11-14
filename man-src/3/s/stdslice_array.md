---
title: "stdslice_array(3)"
name: "stdslice_array"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdslice_array/"
---

std::slice_array - std::slice_array

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;valarray&gt;

template&lt; class T &gt; class slice_array;</code></pre> 
std::slice_array is a helper template used by std::slice subscript operator. It has reference semantics to a subset of the array specified by the std::slice object. 

<h2>Member types</h2>

Type Definition 
value_type T

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a slice_array 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a slice_array 
destructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns contents 
operator= <i>(public member function)</i> 

 
operator+= 
operator-= 
operator*= 
operator/= performs arithmetic operation on the array referred by slice. 
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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;proxy to a subset of a valarray after applying a gslice 
gslice_array <i>(class template)</i> 
