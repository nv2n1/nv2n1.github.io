---
title: "curl_mprintf(3)"
name: "curl_mprintf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_mprintf/"
description: "curl_maprintf, curl_mfprintf, curl_mprintf, curl_msnprintf, curl_msprintf curl_mvaprintf, curl_mvfprintf, curl_mvprintf, curl_mvsnprintf, curl_mvsprintf – formatted output conversion"
---

<h2>NAME</h2>
<p> curl_maprintf, curl_mfprintf, curl_mprintf, curl_msnprintf, curl_msprintf curl_mvaprintf, curl_mvfprintf, curl_mvprintf, curl_mvsnprintf, curl_mvsprintf &#8211; formatted output conversion</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/mprintf.h&gt;</code> </p>
<p> <code>int curl_mprintf(const char *</code><i>format</i><code>, &#8230;);</code><br />
 <code>int curl_mfprintf(FILE *</code><i>fd</i><code>, const char *</code><i>format</i><code>, &#8230;);</code><br />
 <code>int curl_msprintf(char *</code><i>buffer</i><code>, const char *</code><i>format</i><code>, &#8230;);</code><br />
 <code>int curl_msnprintf(char *</code><i>buffer</i><code>, size_t </code><i>maxlength</i><code>, const char *</code><i>format</i><code>, &#8230;);</code><br />
 <code>int curl_mvprintf(const char *</code><i>format</i><code>, va_list </code><i>args</i><code>);</code><br />
 <code>int curl_mvfprintf(FILE *</code><i>fd</i><code>, const char *</code><i>format</i><code>, va_list </code><i>args</i><code>);</code><br />
 <code>int curl_mvsprintf(char *</code><i>buffer</i><code>, const char *</code><i>format</i><code>, va_list </code><i>args</i><code>);</code><br />
 <code>int curl_mvsnprintf(char *</code><i>buffer</i><code>, size_t </code><i>maxlength</i><code>, const char *</code><i>format</i><code>, va_list </code><i>args</i><code>);</code><br />
 <code>char *curl_maprintf(const char *</code><i>format</i><code>, &#8230;);</code><br />
 <code>char *curl_mvaprintf(const char *</code><i>format</i><code>, va_list </code><i>args</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> These are all functions that produce output according to a format string and given arguments. These are mostly clones of the well-known C-style functions and there will be no detailed explanation of all available formatting rules and usage here. </p>
<p> See this table for notable exceptions.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>curl_mprintf()</code></p>
<dd> Normal printf() clone.</p>
<dt><code>curl_mfprintf()</code></p>
<dd> Normal fprintf() clone.</p>
<dt><code>curl_msprintf()</code></p>
<dd> Normal sprintf() clone.</p>
<dt><code>curl_msnprintf()</code></p>
<dd> snprintf() clone. Many systems don&#8217;t have this. It is just like <code>sprintf</code> but with an extra argument after the buffer that specifies the length of the target buffer.</p>
<dt><code>curl_mvprintf()</code></p>
<dd> Normal vprintf() clone.</p>
<dt><code>curl_mvfprintf()</code></p>
<dd> Normal vfprintf() clone.</p>
<dt><code>curl_mvsprintf()</code></p>
<dd> Normal vsprintf() clone.</p>
<dt><code>curl_mvsnprintf()</code></p>
<dd> vsnprintf() clone. Many systems don&#8217;t have this. It is just like <code>vsprintf</code> but with an extra argument after the buffer that specifies the length of the target buffer.</p>
<dt><code>curl_maprintf()</code></p>
<dd> Like printf() but returns the output string as a malloc()ed string. The returned string must be free()ed by the receiver.</p>
<dt><code>curl_mvaprintf()</code></p>
<dd> Like curl_maprintf() but takes a va_list pointer argument instead of a variable amount of arguments.</dl>
</dl>
<p> To easily use all these cloned functions instead of the normal ones, #define _MPRINTF_REPLACE before you include the &lt;curl/mprintf.h&gt; file. Then all the normal names like printf, fprintf, sprintf etc will use the curl-functions instead.</p>
<h2>AVAILABILITY</h2>
<p> These function will be removed from the public libcurl API in a near future. They will instead be made &quot;available&quot; by source code access only, and then as curlx_-prefixed functions. See lib/README.curlx for further details.</p>
<h2>RETURN VALUE</h2>
<p> The <code>curl_maprintf</code> and <code>curl_mvaprintf</code> functions return a pointer to a newly allocated string, or NULL if it failed. </p>
<p> All other functions return the number of characters they actually outputted.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-vprintf/">vprintf</a></code>(3) </p>
<h2>Index</h2>
