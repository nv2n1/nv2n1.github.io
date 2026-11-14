---
title: "stdexperimentalrangestagspecifier(3)"
name: "stdexperimentalrangestagspecifier"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangestagspecifier/"
---

std::experimental::ranges::TagSpecifier - std::experimental::ranges::TagSpecifier

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/utility&gt;

template&lt; class T &gt;                                        (ranges TS)

concept bool TagSpecifier = /* implementation-defined */;</code></pre> 
The concept TagSpecifier&lt;T&gt; is satisfied if and only if T is a tag specifier for use with ranges::tagged. 
The Ranges TS provides a set of tag specifiers in &lt;experimental/ranges/algorithm&gt;. Users cannot define their own tag specifiers. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;augument a tuple-like type with named accessors 
tagged <i>(class template)</i> 
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
