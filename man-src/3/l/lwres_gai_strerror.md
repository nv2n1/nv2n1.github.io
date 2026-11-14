---
title: "lwres_gai_strerror(3)"
name: "lwres_gai_strerror"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lwres_gai_strerror/"
description: "lwres_gai_strerror – print suitable error string"
---

<h2 class="name">NAME</h2>
<p> lwres_gai_strerror &#8211; print suitable error string </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;lwres/netdb.h&gt;
</code></pre>
<dl>
<dt> <code>char * gai_strerror(int&nbsp;<wbr></code><i>ecode</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>lwres_gai_strerror()</code></p>
<dd>returns an error message corresponding to an error code returned by <code>getaddrinfo()</code>. The following error codes and their meaning are defined in <i>include/lwres/netdb.h</i>. </p>
<p> <code>EAI_ADDRFAMILY</code></p>
<dl>
<dt>
<dd> address family for hostname not supported</dl>
<p> <code>EAI_AGAIN</code></p>
<dl>
<dt>
<dd> temporary failure in name resolution</dl>
<p> <code>EAI_BADFLAGS</code></p>
<dl>
<dt>
<dd> invalid value for <code>ai_flags</code></dl>
<p> <code>EAI_FAIL</code></p>
<dl>
<dt>
<dd> non-recoverable failure in name resolution</dl>
<p> <code>EAI_FAMILY</code></p>
<dl>
<dt>
<dd> <code>ai_family</code> not supported</dl>
<p> <code>EAI_MEMORY</code></p>
<dl>
<dt>
<dd> memory allocation failure</dl>
<p> <code>EAI_NODATA</code></p>
<dl>
<dt>
<dd> no address associated with hostname</dl>
<p> <code>EAI_NONAME</code></p>
<dl>
<dt>
<dd> hostname or servname not provided, or not known</dl>
<p> <code>EAI_SERVICE</code></p>
<dl>
<dt>
<dd> servname not supported for <code>ai_socktype</code></dl>
<p> <code>EAI_SOCKTYPE</code></p>
<dl>
<dt>
<dd> <code>ai_socktype</code> not supported</dl>
<p> <code>EAI_SYSTEM</code></p>
<dl>
<dt>
<dd> system error returned in errno</dl>
<p> The message invalid error code is returned if <i>ecode</i> is out of range. </p>
<p> <code>ai_flags</code>, <code>ai_family</code> and <code>ai_socktype</code> are elements of the <code>struct addrinfo</code> used by <code>lwres_getaddrinfo()</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3), <code><a href="/docs/linux/man/3-lwres_getaddrinfo/">lwres_getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code>RFC2133</code>().</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004, 2005, 2007 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium. </p>
<h2>Index</h2>
