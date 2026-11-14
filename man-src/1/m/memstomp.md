---
title: "memstomp(1)"
name: "memstomp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-memstomp/"
description: "memstomp – detect function calls with overlapping memory regions"
---

<h2>NAME</h2>
<p> memstomp &#8211; detect function calls with overlapping memory regions</p>
<h2>SYNOPSIS</h2>
<p> <code>memstomp</code> [<code>-dk</code>] <i>application</i> [<i>argument</i>&#8230;] </p>
<p> <code>memstomp</code> <code>-h</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>memstomp</code> utility identifies function calls that use overlapping memory regions in situations when such an overlap is not allowed by various standards. When a problem is detected, memstomp displays a backtrace to help you debug the problem, and if executed with the <code>&#8211;debug-info</code> command line option, it even uses the available debugging information. Since the backtrace code is not thread safe, memstomp also allows you to use the <code>&#8211;kill</code> option to immediately terminate the analyzed program when an invalid function call is detected. </p>
<p> This version of memstomp inspects the following function calls: <code>memcpy</code>(), <code>memccpy</code>(), <code>mempcpy</code>(), <code>strcpy</code>(), <code>stpcpy</code>(), <code>strncpy</code>(), <code>stpncpy</code>(), <code>strcat</code>(), <code>strncat</code>(), <code>wmemcpy</code>(), <code>wmempcpy</code>(), <code>wcscpy</code>(), <code>wcsncpy</code>(), <code>wcscat</code>(), and <code>wcsncat</code>().</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug-info</code></p>
<dd> Make use of debugging information to produce more detailed stack traces.</p>
<dt><code>-k</code>, <code>&#8211;kill</code></p>
<dd> Kill the analyzed application when a problem is detected.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Be less verbose</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3), <code><a href="/docs/linux/man/3-mempcpy/">mempcpy</a></code>(3), <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-stpcpy/">stpcpy</a></code>(3), <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3), <code><a href="/docs/linux/man/3-stpncpy/">stpncpy</a></code>(3), <code><a href="/docs/linux/man/3-strcat/">strcat</a></code>(3), <code><a href="/docs/linux/man/3-strncat/">strncat</a></code>(3), <code><a href="/docs/linux/man/3-wmemcpy/">wmemcpy</a></code>(3), <code><a href="/docs/linux/man/3-wmempcpy/">wmempcpy</a></code>(3), <code><a href="/docs/linux/man/3-wcscpy/">wcscpy</a></code>(3), <code><a href="/docs/linux/man/3-wcsncpy/">wcsncpy</a></code>(3), <code><a href="/docs/linux/man/3-wcscat/">wcscat</a></code>(3), <code><a href="/docs/linux/man/3-wcsncat/">wcsncat</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> Lennart Poettering &lt;lennart [at] poettering.net&gt;<br />
 William Cohen &lt;wcohen [at] redhat.com&gt; </p>
<h2>Index</h2>
