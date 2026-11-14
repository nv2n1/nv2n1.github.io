---
title: "stdexperimentalrangestagged_pair(3)"
name: "stdexperimentalrangestagged_pair"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangestagged_pair/"
---

std::experimental::ranges::tagged_pair - std::experimental::ranges::tagged_pair

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/utility&gt;

template&lt; TaggedType T1, TaggedType T2 &gt;         (ranges TS)

using tagged_pair = /* see below */;</code></pre> 
Convenience alias template for naming a ranges::tagged wrapping a std::pair. 
A TaggedType is a function type S(T), where S is a TagSpecifier and T is the type of the element. 
tagged_pair&lt;S1(T1), S2(T2)&gt; is an alias for ranges::tagged&lt;std::pair&lt;T1, T2&gt;, S1, S2&gt;. 

<h2>Notes</h2>

Because a function type is used to &quot;glue&quot; the tag specifier and the corresponding element type together, the usual parameter type adjustments apply. In particular, top-level cv-qualifiers are removed and array types are adjusted to pointers: tagged_pair&lt;tag::in(const int* const), tag::out(int[])&gt; is ranges::tagged&lt;std::pair&lt;const int*, int*&gt;, tag::in, tag::out&gt;. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a type represents a tag specifier and its element type 
TaggedType (concept) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;augument a tuple-like type with named accessors 
tagged <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;convenience function for creating a tagged_pair 
make_tagged_pair <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alias template for a tagged std::tuple 
tagged_tuple (alias template) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;convenience function for creating a tagged_tuple 
make_tagged_tuple <i>(function template)</i> 
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
