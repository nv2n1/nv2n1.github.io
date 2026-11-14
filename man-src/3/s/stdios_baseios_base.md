---
title: "stdios_baseios_base(3)"
name: "stdios_baseios_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseios_base/"
---

std::ios_base::~ios_base - std::ios_base::~ios_base

<h2>Synopsis</h2>

<pre><code>virtual ~ios_base();</code></pre> 
Destroys the ios_base object. 
Before any of the member functions would yield undefined results, calls callbacks, registered by register_callback() passing erase_event as parameter. 
No operations on rdbuf are performed, it is not destroyed. 
