---
title: "stdtype_infotype_info(3)"
name: "stdtype_infotype_info"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtype_infotype_info/"
---

std::type_info::~type_info - std::type_info::~type_info

<h2>Synopsis</h2>

<pre><code>virtual ~type_info();</code></pre> 
Destructs an object of type std::type_info. This destructor is public virtual, allowing objects of classes, derived from std::type_info to be safely deleted through pointers to base class. 
