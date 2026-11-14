---
title: "stdexperimentalbasic_string_view(3)"
name: "stdexperimentalbasic_string_view"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalbasic_string_view/"
---

std::experimental::basic_string_view&lt;CharT,Traits&gt;::to_string,std::experimental::basic_string_view&lt;CharT,Traits&gt;::operatorbasic_string - std::experimental::basic_string_view&lt;CharT,Traits&gt;::to_string,std::experimental::basic_string_view&lt;CharT,Traits&gt;::operatorbasic_string

<h2>Synopsis</h2>

<pre><code>template &lt;class Allocator = allocator&lt;CharT&gt;&gt;

basic_string&lt;CharT, Traits, Allocator&gt;(library fundamentals TS)

    to_string(const Allocator &amp;a = Allocator()) const;

template &lt;class Allocator&gt;
(library fundamentals TS)

    explicit
    operator basic_string&lt;CharT, Traits, Allocator&gt;() const;</code></pre> 
Creates a basic_string with a copy of the content of the current view. 

<h2>Template parameters</h2>

Allocator - Allocator type used to allocate internal storage

<h2>Parameters</h2>

a - Allocator instance to use for allocating the new string

<h2>Return value</h2>

A basic_string containing a copy of the characters of the current view. 

<h2>Complexity</h2>

Linear in size()
