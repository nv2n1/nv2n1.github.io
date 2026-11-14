---
title: "papi_sprofil_t(3)"
name: "papi_sprofil_t"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_sprofil_t/"
description: "PAPI_sprofil_t –"
---

<p>PAPI_sprofil_t &#8211; </p>
<h2>Synopsis</h2>
<h3>Data Fields</h3>
<p>void * <code>pr_base</code> </p>
<p> unsigned <code>pr_size</code> </p>
<p> caddr_t <code>pr_off</code> </p>
<p> unsigned <code>pr_scale</code> </p>
<h2>Detailed Description</h2>
<h2>Field Documentation</h2>
<h3>void* PAPI_sprofil_t::pr_base</h3>
<p>buffer base</p>
<h3>caddr_t PAPI_sprofil_t::pr_off</h3>
<p>pc start address (offset)</p>
<h3>unsigned PAPI_sprofil_t::pr_scale</h3>
<p>pc scaling factor: fixed point fraction 0xffff ~= 1, 0x8000 == .5, 0x4000 == .25, etc. also, two extensions 0x1000 == 1, 0x2000 == 2</p>
<h3>unsigned PAPI_sprofil_t::pr_size</h3>
<p>buffer size </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
