---
title: "stddynamic_extent(3)"
name: "stddynamic_extent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddynamic_extent/"
---

std::dynamic_extent - std::dynamic_extent

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;span&gt;

inline constexpr std::size_t dynamic_extent = std::numeric_limits&lt;std::size_t&gt;::max();  (since C++20)</code></pre> 
std::dynamic_extent is a constant of type std::size_t that is used to differentiate std::span of static and dynamic extent. 

<h2>Note</h2>

Since std::size_t is an unsigned type, an equivalent definition is: 

 
&nbsp;<wbr>&nbsp;inline constexpr std::size_t dynamic_extent = -1; 

 
See integral_conversions.

<h2>See also</h2>

span a non-owning view over a contiguous sequence of objects 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(C++20) 
