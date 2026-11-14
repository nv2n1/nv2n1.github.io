---
title: "curl_getenv(3)"
name: "curl_getenv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_getenv/"
description: "curl_getenv – return value for environment name"
---

<h2>NAME</h2>
<p> curl_getenv &#8211; return value for environment name</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>char *curl_getenv(const char *</code><i>name</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> curl_getenv() is a portable wrapper for the getenv() function, meant to emulate its behaviour and provide an identical interface for all operating systems libcurl builds on (including win32).</p>
<h2>AVAILABILITY</h2>
<p> This function will be removed from the public libcurl API in a near future. It will instead be made &quot;available&quot; by source code access only, and then as curlx_getenv().</p>
<h2>RETURN VALUE</h2>
<p> If successful, curl_getenv() returns a pointer to the value of the specified environment. The memory it refers to is malloc()ed so the application must free() this when the data is no longer needed. When <i><a href="/docs/linux/man/3-curl_getenv/">curl_getenv</a>(3)</i> fails to find the specified name, it returns a null pointer.</p>
<h2>NOTE</h2>
<p> Under unix operating systems, there isn&#8217;t any point in returning an allocated memory, although other systems won&#8217;t work properly if this isn&#8217;t done. The unix implementation thus has to suffer slightly from the drawbacks of other systems.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/3C-getenv/">getenv</a></code>(3C), </p>
<h2>Index</h2>
