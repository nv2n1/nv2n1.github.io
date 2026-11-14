---
title: "stdfilesystemhash_value(3)"
name: "stdfilesystemhash_value"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemhash_value/"
---

std::filesystem::hash_value - std::filesystem::hash_value

<h2>Synopsis</h2>

Defined in header &lt;filesystem&gt; 
std::size_t hash_value( const path&amp; p ) noexcept; <i>(since C++17)</i> 

<h2>Parameters</h2>

p - a std::filesystem::path object

<h2>Return value</h2>

A hash value such that if for two paths, p1 == p2 then hash_value(p1) == hash_value(p2). 

<h2>Notes</h2>

Equality of two paths is determined by comparing each component separately, so, for example &quot;a//b&quot; equals &quot;a/b&quot; and has the same hash_value 
hash_value originates from the boost.filesystem library where it was used for interoperability with boost.hash (which calls_hash_value where available) 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares the lexical representations of two paths lexicographically 
compare <i>(public member function)</i> 
hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
