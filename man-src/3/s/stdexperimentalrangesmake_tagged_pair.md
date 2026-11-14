---
title: "stdexperimentalrangesmake_tagged_pair(3)"
name: "stdexperimentalrangesmake_tagged_pair"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesmake_tagged_pair/"
---

std::experimental::ranges::make_tagged_pair - std::experimental::ranges::make_tagged_pair

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / utility&gt;

    template &lt;TagSpecifier Tag1, TagSpecifier Tag2, class T1, class T2&gt;
    (ranges TS)

        constexpr ranges::tagged&lt;/*see below*/, Tag1, Tag2&gt; make_tagged_pair(T1 &amp;&amp;x, T2 &amp;&amp;y);
Convenience function for creating a tagged pair, deducing the element types from the arguments (the tag specifiers must be explicitly specified).

The see below portion of the return type is decltype(std::make_pair(std::forward&lt;T1&gt;(x), std::forward&lt;T2&gt;(y))).
</code></pre>

<h2>Return value</h2>

R(std::forward&lt;T1&gt;(x), std::forward&lt;T2&gt;(y)), where R is the return type. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a type represents a tag specifier and its element type 
TaggedType (concept) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;augument a tuple-like type with named accessors 
tagged <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alias template for a tagged std::pair 
tagged_pair (alias template) 
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
