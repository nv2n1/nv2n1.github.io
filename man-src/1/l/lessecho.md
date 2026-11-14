---
title: "lessecho(1)"
name: "lessecho"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lessecho/"
description: "lessecho – expand metacharacters"
---

<h2 class="name">NAME</h2>
<p> lessecho &#8211; expand metacharacters </p>
<h2>SYNOPSIS</h2>
<p> <code>lessecho</code> <i>[-ox] [-cx] [-pn] [-dn] [-mx] [-nn] [-ex] [-a] file &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <i>lessecho</i> is a program that simply echos its arguments on standard output. But any metacharacter in the output is preceded by an &quot;escape&quot; character, which by default is a backslash.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below.</p>
<dl>
<dt><code>-ex</code></p>
<dd> Specifies &quot;x&quot;, rather than backslash, to be the escape char for metachars. If x is &quot;-&quot;, no escape char is used and arguments containing metachars are surrounded by quotes instead.</p>
<dt><code>-ox</code></p>
<dd> Specifies &quot;x&quot;, rather than double-quote, to be the open quote character, which is used if the -e- option is specified.</p>
<dt><code>-cx</code></p>
<dd> Specifies &quot;x&quot; to be the close quote character.</p>
<dt><code>-pn</code></p>
<dd> Specifies &quot;n&quot; to be the open quote character, as an integer.</p>
<dt><code>-dn</code></p>
<dd> Specifies &quot;n&quot; to be the close quote character, as an integer.</p>
<dt><code>-mx</code></p>
<dd> Specifies &quot;x&quot; to be a metachar. By default, no characters are considered metachars.</p>
<dt><code>-nn</code></p>
<dd> Specifies &quot;n&quot; to be a metachar, as an integer.</p>
<dt><code>-fn</code></p>
<dd> Specifies &quot;n&quot; to be the escape char for metachars, as an integer.</p>
<dt><code>-a</code></p>
<dd> Specifies that all arguments are to be quoted. The default is that only arguments containing metacharacters are quoted.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-less/">less</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas Schoepf &lt;schoepf [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
<p> Report bugs at <a rel="nofollow" href="https://github.com/gwsw/less/issues.">https://github.com/gwsw/less/issues.</a> </p>
<h2>Index</h2>
