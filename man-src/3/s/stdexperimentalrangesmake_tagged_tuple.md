---
title: "stdexperimentalrangesmake_tagged_tuple(3)"
name: "stdexperimentalrangesmake_tagged_tuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesmake_tagged_tuple/"
---

std::experimental::ranges::make_tagged_tuple - std::experimental::ranges::make_tagged_tuple

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / tuple&gt;

    template &lt;TagSpecifier... Tags, class... Types&gt;

requires sizeof...(Tags) == sizeof...(Types)(ranges TS)

                                constexpr ranges::tagged&lt;/*see below*/, Tags...&gt; make_tagged_tuple(Types &amp;&amp;...t);
Convenience function for creating a tagged tuple, deducing the element types from the arguments (the tag specifiers must be explicitly specified).

The see below portion of the return type is decltype(std::make_tuple(std::forward&lt;Types&gt;(t)...)).
</code></pre>

<h2>Return value</h2>

R(std::forward&lt;Types&gt;(t)...), where R is the return type. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a type represents a tag specifier and its element type 
TaggedType (concept) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;augument a tuple-like type with named accessors 
tagged <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alias template for a tagged std::pair 
tagged_pair (alias template) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;convenience function for creating a tagged_pair 
make_tagged_pair <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alias template for a tagged std::tuple 
tagged_tuple (alias template) 
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
