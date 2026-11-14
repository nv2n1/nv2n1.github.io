---
title: "stdhashstdexperimentalstring_viewstdexperimentalwstring_viewstdexperimentalu16string_viewstdexperimentalu32string_view(3)"
name: "stdhashstdexperimentalstring_viewstdexperimentalwstring_viewstdexperimentalu16string_viewstdexperimentalu32string_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhashstdexperimentalstring_viewstdexperimentalwstring_viewstdexperimentalu16string_viewstdexperimentalu32string_view/"
---

std::hash(std::experimental::string_view,std::experimental::wstring_view,std::experimental::u16string_view,std::experimental::u32string_view) - std::hash(std::experimental::string_view,std::experimental::wstring_view,std::experimental::u16string_view,std::experimental::u32string_view)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / string_view&gt;

    template &lt;&gt;
    struct hash&lt;std::experimental::string_view&gt;;

template &lt;&gt;
struct hash&lt;std::experimental::wstring_view&gt;;
(library fundamentals TS)

    template &lt;&gt;
    struct hash&lt;std::experimental::u16string_view&gt;;

template &lt;&gt;
struct hash&lt;std::experimental::u32string_view&gt;;</code></pre> 
Template specializations of std::hash for the various view classes for hashing views. 

<h2>See also</h2>

hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
