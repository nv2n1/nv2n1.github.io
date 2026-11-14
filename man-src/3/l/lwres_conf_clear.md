---
title: "lwres_conf_clear(3)"
name: "lwres_conf_clear"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_conf_clear/"
description: "lwres_conf_init, lwres_conf_clear, lwres_conf_parse, lwres_conf_print, lwres_conf_get – lightweight resolver configuration"
---

<h2 class="name">NAME</h2>
<p> lwres_conf_init, lwres_conf_clear, lwres_conf_parse, lwres_conf_print, lwres_conf_get &#8211; lightweight resolver configuration </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/lwres.h&gt;
</code></pre>
<dl>
<dt> <code>void lwres_conf_init(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>);</code></p>
<dt> <code>void lwres_conf_clear(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_conf_parse(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, const char&nbsp;<wbr>*</code><i>filename</i><code>);</code></p>
<dt> <code>lwres_result_t lwres_conf_print(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>, FILE&nbsp;<wbr>*</code><i>fp</i><code>);</code></p>
<dt> <code>lwres_conf_t * lwres_conf_get(lwres_context_t&nbsp;<wbr>*</code><i>ctx</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>lwres_conf_init()</code></p>
<dd>creates an empty <code>lwres_conf_t</code> structure for lightweight resolver context <i>ctx</i>. </p>
<p> <code>lwres_conf_clear()</code> frees up all the internal memory used by that <code>lwres_conf_t</code> structure in resolver context <i>ctx</i>. </p>
<p> <code>lwres_conf_parse()</code> opens the file <i>filename</i> and parses it to initialise the resolver context <i>ctx</i>&#8216;s <code>lwres_conf_t</code> structure. </p>
<p> <code>lwres_conf_print()</code> prints the <code>lwres_conf_t</code> structure for resolver context <i>ctx</i> to the <code>FILE</code> <i>fp</i>.</p>
<h2>RETURN VALUES</h2>
<p> <code>lwres_conf_parse()</code> returns <code>LWRES_R_SUCCESS</code> if it successfully read and parsed <i>filename</i>. It returns <code>LWRES_R_FAILURE</code> if <i>filename</i> could not be opened or contained incorrect resolver statements. </p>
<p> <code>lwres_conf_print()</code> returns <code>LWRES_R_SUCCESS</code> unless an error occurred when converting the network addresses to a numeric host address string. If this happens, the function returns <code>LWRES_R_FAILURE</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3), <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5).</p>
<h2>FILES</h2>
<p> <i>/etc/resolv.conf</i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
