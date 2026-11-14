---
title: "papi_address_map_t(3)"
name: "papi_address_map_t"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_address_map_t/"
description: "PAPI_address_map_t –"
---

<p>PAPI_address_map_t &#8211; </p>
<p> get the executable&#8217;s address space info</p>
<h2>Synopsis</h2>
<h3>Data Fields</h3>
<p>char <code>name</code> [1024] </p>
<p> caddr_t <code>text_start</code> </p>
<p> caddr_t <code>text_end</code> </p>
<p> caddr_t <code>data_start</code> </p>
<p> caddr_t <code>data_end</code> </p>
<p> caddr_t <code>bss_start</code> </p>
<p> caddr_t <code>bss_end</code> </p>
<h2>Field Documentation</h2>
<h3>caddr_t PAPI_address_map_t::bss_end</h3>
<p>End address of program bss segment</p>
<h3>caddr_t PAPI_address_map_t::bss_start</h3>
<p>Start address of program bss segment</p>
<h3>caddr_t PAPI_address_map_t::data_end</h3>
<p>End address of program data segment</p>
<h3>caddr_t PAPI_address_map_t::data_start</h3>
<p>Start address of program data segment</p>
<h3>caddr_t PAPI_address_map_t::text_end</h3>
<p>End address of program text segment</p>
<h3>caddr_t PAPI_address_map_t::text_start</h3>
<p>Start address of program text segment </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
