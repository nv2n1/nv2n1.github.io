---
title: "stdbasic_ios(3)"
name: "stdbasic_ios"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_ios/"
---

std::basic_ios&lt;CharT,Traits&gt;::~basic_ios - std::basic_ios&lt;CharT,Traits&gt;::~basic_ios

<h2>Synopsis</h2>

<pre><code>virtual ~basic_ios();</code></pre> 
Destroys the basic_ios object. No operations on rdbuf are performed, it is not destroyed. 

<h2>Notes</h2>

This destructor is virtual because the base class destructor, ios_base::~ios_base is virtual. 
