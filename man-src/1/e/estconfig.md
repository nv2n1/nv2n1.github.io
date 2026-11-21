---
title: "estconfig(1)"
name: "estconfig"
section: "1"
letter: "e"
url: "/docs/linux/man/1-estconfig/"
description: "estconfig – configuration utility of Hyper Estraier"
---

<h2>SYNOPSIS</h2>
<p> <code>estconfig &#8211;version</code> </p>
<p> <code>estconfig &#8211;prefix</code> </p>
<p> <code>estconfig &#8211;execprefix</code> </p>
<p> <code>estconfig &#8211;headdir</code> </p>
<p> <code>estconfig &#8211;libdir</code> </p>
<p> <code>estconfig &#8211;bindir</code> </p>
<p> <code>estconfig &#8211;libexecdir</code> </p>
<p> <code>estconfig &#8211;datadir</code> </p>
<p> <code>estconfig &#8211;cflags</code> </p>
<p> <code>estconfig &#8211;ldflags</code> </p>
<p> <code>estconfig &#8211;libs</code> </p>
<p> <code>estconfig &#8211;mtlibs</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>estconfig</code> is useful for integration of an application or a system using Hyper Estraier. It outputs setting and configurations of Hyper Estraier.</p>
<dl>
<dt><code>estconfig &#8211;version</code></dt>
<dd> to output version information.</dd>
<dt><code>estconfig &#8211;prefix</code></dt>
<dd> to output the prefix of the destination of installation.</dd>
<dt><code>estconfig &#8211;execprefix</code></dt>
<dd> to output the prefix of the files depending on the platform.</dd>
<dt><code>estconfig &#8211;headdir</code></dt>
<dd> to output the prefix of the headers.</dd>
<dt><code>estconfig &#8211;libdir</code></dt>
<dd> to output the prefix of the libraries.</dd>
<dt><code>estconfig &#8211;bindir</code></dt>
<dd> to output the prefix of the commands.</dd>
<dt><code>estconfig &#8211;libexecdir</code></dt>
<dd> to output the prefix of the CGI script.</dd>
<dt><code>estconfig &#8211;datadir</code></dt>
<dd> to output the prefix of the configuration files.</dd>
<dt><code>estconfig &#8211;cflags</code></dt>
<dd> to output the compiler options to be specified when building.</dd>
<dt><code>estconfig &#8211;ldflags</code></dt>
<dd> to output the linker options to be specified when building.</dd>
<dt><code>estconfig &#8211;libs</code></dt>
<dd> to output the libraries to be specified when building.</dd>
<dt><code>estconfig &#8211;mtlibs</code></dt>
<dd> to output the libraries for applications with multi thread.</dd></dl>
<p> estconfig always returns 0 as the exit status. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-estcmd/">estcmd</a></code>(1), <code><a href="/docs/linux/man/1-estmaster/">estmaster</a></code>(1), <code><a href="/docs/linux/man/1-estcall/">estcall</a></code>(1), <code><a href="/docs/linux/man/1-estwaver/">estwaver</a></code>(1), <code>estraier</code>(3) <code>estnode</code>(3) </p>
<p> Please see <code><a rel="nofollow" href="http://hyperestraier.sourceforge.net/pguide-en.html">http://hyperestraier.sourceforge.net/pguide-en.html</a></code> for detail. </p>
