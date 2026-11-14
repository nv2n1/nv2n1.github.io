---
title: "papi_mpx_info_t(3)"
name: "papi_mpx_info_t"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_mpx_info_t/"
description: "PAPI_mpx_info_t –"
---

<p>PAPI_mpx_info_t &#8211; </p>
<h2>Synopsis</h2>
<h3>Data Fields</h3>
<p>int <code>timer_sig</code> </p>
<p> int <code>timer_num</code> </p>
<p> int <code>timer_us</code> </p>
<h2>Detailed Description</h2>
<h2>Field Documentation</h2>
<h3>int PAPI_mpx_info_t::timer_num</h3>
<p>Number of the itimer or POSIX 1 timer used by the multiplex timer: PAPI_ITIMER</p>
<h3>int PAPI_mpx_info_t::timer_sig</h3>
<p>Signal number used by the multiplex timer, 0 if not: PAPI_SIGNAL</p>
<h3>int PAPI_mpx_info_t::timer_us</h3>
<p>uS between switching of sets: PAPI_MPX_DEF_US </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
