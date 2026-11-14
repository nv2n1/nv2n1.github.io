---
title: "papi_get_real_cyc(3)"
name: "papi_get_real_cyc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_real_cyc/"
description: "PAPI_get_real_cyc –"
---

<p>PAPI_get_real_cyc &#8211; </p>
<p> get real time counter value in clock cycles Returns the total real time passed since some arbitrary starting point. The time is returned in clock cycles. This call is equivalent to wall clock time.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> s = PAPI_get_real_cyc();
 your_slow_code();
 e = PAPI_get_real_cyc();
 printf(&quot;Wallclock cycles: %lld
&quot;,e-s);
* </pre>
<p>&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>PAPIF PAPI <code>PAPI_get_virt_usec</code> <code>PAPI_get_virt_cyc</code> <code>PAPI_library_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
