---
title: "stdsub_matchcompare(3)"
name: "stdsub_matchcompare"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsub_matchcompare/"
---

std::sub_match&lt;BidirIt&gt;::compare - std::sub_match&lt;BidirIt&gt;::compare

<h2>Synopsis</h2>

<pre><code>int compare(const sub_match &amp;m) const;
(1)(since C++ 11)

    int compare(const string_type &amp;s) const;
(2)(since C++ 11)

    int compare(const value_type *c) const;
(3)(since C++ 11)</code></pre> 
1) Compares two sub_match directly by comparing their underlying character sequences. Equivalent to str().compare(m.str()). 
2) Compares a sub_match with a std::basic_string. Equivalent to str().compare(s). 
3) Compares a sub_match with a null-terminated sequence of the underlying character type pointed to by s. Equivalent to str().compare(c). 
This function is infrequently used directly by application code. Instead, one of the non-member comparison operators are used. 

<h2>Parameters</h2>

m - a reference to another sub_match 
s - a reference to a string to compare to 
c - a pointer to a null-terminated character sequence of the underlying value_type to compare to

<h2>Return value</h2>

A value less than zero if this sub_match is less than the other character sequence, zero if the both underlying character sequences are equal, greater than zero if this sub_match is greater than the other character sequence. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings 
compare <i>(public member function of std::basic_string&lt;CharT,Traits,Allocator&gt;)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts to the underlying string type 
str <i>(public member function)</i> 
operator_string_type 
operator== 
operator!= compares two sub_match objects 
operator&lt; <i>(function template)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
