---
title: "papi_addr_range_option_t(3)"
name: "papi_addr_range_option_t"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_addr_range_option_t/"
description: "PAPI_addr_range_option_t –"
---

<p>PAPI_addr_range_option_t &#8211; </p>
<p> address range specification for range restricted counting if both are zero, range is disabled</p>
<h2>Synopsis</h2>
<h3>Data Fields</h3>
<p>int <code>eventset</code> </p>
<p> caddr_t <code>start</code> </p>
<p> caddr_t <code>end</code> </p>
<p> int <code>start_off</code> </p>
<p> int <code>end_off</code> </p>
<h2>Field Documentation</h2>
<h3>caddr_t PAPI_addr_range_option_t::end</h3>
<p>user requested end address of an address range</p>
<h3>int PAPI_addr_range_option_t::end_off</h3>
<p>hardware specified offset from end address</p>
<h3>int PAPI_addr_range_option_t::eventset</h3>
<p>eventset to restrict</p>
<h3>caddr_t PAPI_addr_range_option_t::start</h3>
<p>user requested start address of an address range</p>
<h3>int PAPI_addr_range_option_t::start_off</h3>
<p>hardware specified offset from start address </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
