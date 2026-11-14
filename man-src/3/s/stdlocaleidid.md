---
title: "stdlocaleidid(3)"
name: "stdlocaleidid"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocaleidid/"
---

std::locale::id::id - std::locale::id::id

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

id();
(1)

    id(const id &amp;) = delete;
(2)</code></pre> 
1) default constructor: creates an object of type std::locale::id with implementation-specific content. 
2) copy constructor is deleted; std::locale::id is not copyable. 

<h2>Notes</h2>

Because locales and facets must be available for the IO stream objects with static storage duration, such as std::cout, typical implementations let implicit default constructor zero-initialize the contents of std::locale::id during static initialization (before constructors run for static objects), and when a facet is added to any locale for the first time, the locale completes initialization of the facet's id. 
