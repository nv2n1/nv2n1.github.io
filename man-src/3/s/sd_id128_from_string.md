---
title: "sd_id128_from_string(3)"
name: "sd_id128_from_string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_id128_from_string/"
description: "sd_id128_to_string, sd_id128_from_string – Format or parse 128-bit IDs as strings"
---

<p>sd_id128_to_string, sd_id128_from_string &#8211; Format or parse 128-bit IDs as strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-id128.h&gt;

char *sd_id128_to_string(sd_id128_t id, char s[33]);

int sd_id128_from_string(const char *s, sd_id128_t *ret);</code></pre>
<h2>Description</h2>
<p><code>sd_id128_to_string()</code></p>
<dd>formats a 128-bit ID as a character string. It expects the ID and a string array capable of storing 33 characters. The ID will be formatted as 32 lowercase hexadecimal digits and be terminated by a <code>NUL</code> byte. </p>
<p> <code>sd_id128_from_string()</code> implements the reverse operation: it takes a 33 character string with 32 hexadecimal digits (either lowercase or uppercase, terminated by <code>NUL</code>) and parses them back into a 128-bit ID returned in <i>ret</i>. Alternatively, this call can also parse a 37-character string with a 128-bit ID formatted as RFC UUID. </p>
<p> For more information about the &quot;sd_id128_t&quot; type see <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3). Note that these calls operate the same way on all architectures, i.e. the results do not depend on endianness. </p>
<p> When formatting a 128-bit ID into a string, it is often easier to use a format string for <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3). This is easily done using the <code>SD_ID128_FORMAT_STR</code> and <code>SD_ID128_FORMAT_VAL()</code> macros. For more information see <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3).</p>
<h2>Return Value</h2>
<p><code>sd_id128_to_string()</code> always succeeds and returns a pointer to the string array passed in. <code>sd_id128_from_string</code> returns 0 on success, in which case <i>ret</i> is filled in, or a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_id128_to_string()</code> and <code>sd_id128_from_string()</code> interfaces are available as a shared library, which can be compiled and linked to with the &quot;libsystemd&quot;&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-id128/">sd-id128</a></code>(3), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) </p>
