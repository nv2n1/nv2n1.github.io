---
title: "stdhashstdstring_viewstdwstring_viewstdu16string_viewstdu32string_view(3)"
name: "stdhashstdstring_viewstdwstring_viewstdu16string_viewstdu32string_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhashstdstring_viewstdwstring_viewstdu16string_viewstdu32string_view/"
---

std::hash(std::string_view,std::wstring_view,std::u16string_view,std::u32string_view) - std::hash(std::string_view,std::wstring_view,std::u16string_view,std::u32string_view)

<h2>Synopsis</h2>

Defined in header &lt;string_view&gt; 
template&lt;&gt; struct hash&lt;std::string_view&gt;; <i>(since C++17)</i> 
template&lt;&gt; struct hash&lt;std::wstring_view&gt;; <i>(since C++17)</i> 
template&lt;&gt; struct hash&lt;std::u8string_view&gt;; <i>(since C++20)</i> 
template&lt;&gt; struct hash&lt;std::u16string_view&gt;; <i>(since C++17)</i> 
template&lt;&gt; struct hash&lt;std::u32string_view&gt;; <i>(since C++17)</i> 
Template specializations of std::hash for the various view classes for hashing views. 
These hashes equal the hashes of corresponding std::basic_string classes: If S is one of the standard basic_string types, SV is the corresponding string view type, and s is an object of type S, then std::hash&lt;S&gt;()(s) == std::hash&lt;SV&gt;()(SV(s)). 

<h2>See also</h2>

hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
