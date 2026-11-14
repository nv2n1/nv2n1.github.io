---
title: "stdhash(3)"
name: "stdhash"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdhash/"
---

std::hash&lt;std::variant&gt; - std::hash&lt;std::variant&gt;

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;variant&gt;

    template &lt;class... Types&gt;
    (since C++ 17)

        struct hash&lt;std::variant&lt;Types...&gt;&gt;;</code></pre> 
The template specialization of std::hash for the std::variant template allows users to obtain hashes of variant objects. 
The specialization std::hash&lt;std::variant&lt;Types...&gt;&gt; is enabled (see std::hash) if every specialization in std::hash&lt;std::remove_const_t&lt;Types&gt;&gt;... is enabled, and is disabled otherwise. 
The member functions of this specialization are not guaranteed to be noexcept. 

<h2>Template parameters</h2>

Types - the types of the alternatives supported by the variant object

<h2>Notes</h2>

Unlike std::hash&lt;std::optional&gt;, hash of a variant does not typically equal the hash of the contained value; this makes it possible to distinguish std::variant&lt;int, int&gt; holding the same value as different alternatives. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

hash hash function object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
