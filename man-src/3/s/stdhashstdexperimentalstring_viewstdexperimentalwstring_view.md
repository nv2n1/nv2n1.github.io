---
title: "stdhashstdexperimentalstring_viewstdexperimentalwstring_view(3)"
name: "stdhashstdexperimentalstring_viewstdexperimentalwstring_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhashstdexperimentalstring_viewstdexperimentalwstring_view/"
---

std::hash(std::experimental::string_view,std::experimental::wstring_view, - std::hash(std::experimental::string_view,std::experimental::wstring_view,

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / string_view&gt;

    template &lt;&gt;
    struct hash&lt;std::experimental::string_view&gt;;</code></pre> 
template&lt;&gt;&nbsp;<wbr>struct hash&lt;std::experimental::wstring_view&gt;;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(library fundamentals 
template&lt;&gt;&nbsp;<wbr>struct hash&lt;std::experimental::u16string_view&gt;;&nbsp;<wbr>&nbsp;<wbr>TS) <pre><code>template &lt;&gt;
struct hash&lt;std::experimental::u32string_view&gt;;</code></pre> 
Template specializations of std::hash for the various view classes for hashing 
views. 

<h2>See also</h2>

hash&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hash function object 
<i>(C++11)</i>&nbsp;<wbr><i>(class template)</i> 
