---
title: "stdexperimentalrangestaggedtype(3)"
name: "stdexperimentalrangestaggedtype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangestaggedtype/"
---

std::experimental::ranges::TaggedType - std::experimental::ranges::TaggedType

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/utility&gt;

template&lt; class T &gt;                                      (ranges TS)

concept bool TaggedType = /* implementation-defined */;</code></pre> 
The concept TaggedType&lt;T&gt; is satisfied if and only if T is a unary function type of the form R(A), where R is a TagSpecifier. 
Such types are used with the convenience alias templates tagged_tuple and tagged_pair. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alias template for a tagged std::tuple 
tagged_tuple (alias template) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alias template for a tagged std::pair 
tagged_pair (alias template) 
in 
in1 
in2 
out 
out1 tag specifiers for use with ranges::tagged 
out2 <i>(class)</i> 
fun 
min 
max 
begin 
end 
