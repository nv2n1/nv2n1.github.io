---
title: "repomanage(1)"
name: "repomanage"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repomanage/"
description: "repomanage – list the newest or oldest RPM packages in a directory"
---

<h2>NAME</h2>
<p> repomanage &#8211; list the newest or oldest RPM packages in a directory</p>
<h2>SYNOPSIS</h2>
<p> <code>repomanage</code> [options] directory</p>
<h2>DESCRIPTION</h2>
<p> <code>repomanage</code> is a program to manage a directory of RPM packages. It displays a list of the newest or oldest packages in a directory for easy piping to xargs or similar programs. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a help message, and then quit.</p>
<dt><code>-o, &#8211;old</code></p>
<dd> Print the oldest packages.</p>
<dt><code>-n, &#8211;new</code></p>
<dd> Print the newest packages.</p>
<dt><code>-s, &#8211;space</code></p>
<dd> Space-separated instead of newline-separated output.</p>
<dt><code>-k KEEP, &#8211;keep=KEEP</code></p>
<dd> Newest N packages to keep &#8211; defaults to 1.</p>
<dt><code>-c, &#8211;nocheck</code></p>
<dd> Do not check package payload signatures/digests. </p>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
<h2>Index</h2>
