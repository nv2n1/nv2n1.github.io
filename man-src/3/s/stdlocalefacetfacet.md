---
title: "stdlocalefacetfacet(3)"
name: "stdlocalefacetfacet"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocalefacetfacet/"
---

std::locale::facet::facet - std::locale::facet::facet

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    explicit facet(std::size_t refs = 0);
(1)

    facet(const facet &amp;) = delete;
(2)</code></pre> 
1) creates a facet with starting reference count refs. If refs is non-zero, the facet will not be deleted when the last locale referencing it goes out of scope. A facet with static or dynamic storage duration should always be constructed with a non-zero refs. 
2) copy constructor is deleted; std::locale::facet is not copyable. 
