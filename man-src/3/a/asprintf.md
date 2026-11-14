---
title: "asprintf(3)"
name: "asprintf"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asprintf/"
description: "asprintf, vasprintf – print to allocated string"
---

<h2 class="name">NAME</h2>
<p> asprintf, vasprintf &#8211; print to allocated string </p>
<h2>SYNOPSIS</h2>
<p> <code>#define _GNU_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */<br />
 <code>#include &lt;stdio.h&gt;</code> </p>
<p> <code>int asprintf(char **</code><i>strp</i><code>, const char *</code><i>fmt</i><code>, &#8230;);</code> </p>
<p> <code>int vasprintf(char **</code><i>strp</i><code>, const char *</code><i>fmt</i><code>, va_list </code><i>ap</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The functions <code>asprintf</code>() and <code>vasprintf</code>() are analogs of <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3), except that they allocate a string large enough to hold the output including the terminating null byte (&#8216;
