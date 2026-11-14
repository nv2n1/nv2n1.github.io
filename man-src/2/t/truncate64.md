---
title: "truncate64(2)"
name: "truncate64"
section: "2"
letter: "t"
url: "/docs/linux/man/2-truncate64/"
description: "truncate, ftruncate – truncate a file to a specified length"
---

<h2 class="name">NAME</h2>
<p> truncate, ftruncate &#8211; truncate a file to a specified length </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code><br />
 <code>#include &lt;sys/types.h&gt;</code> </p>
<p> <code>int truncate(const char *</code><i>path</i><code>, off_t </code><i>length</i><code>);</code><br />
 <code>int ftruncate(int </code><i>fd</i><code>, off_t </code><i>length</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>truncate</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<p> <code>ftruncate</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.3.5:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>truncate</code>() and <code>ftruncate</code>() functions cause the regular file named by <i>path</i> or referenced by <i>fd</i> to be truncated to a size of precisely <i>length</i> bytes. </p>
<p> If the file previously was larger than this size, the extra data is lost. If the file previously was shorter, it is extended, and the extended part reads as null bytes (&#8216;
