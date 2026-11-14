---
title: "flickcurl-config(1)"
name: "flickcurl-config"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flickcurl-config/"
description: "flickcurl-config – script to get information about the installed version of flickcurl"
---

<h2>NAME</h2>
<p> flickcurl-config &#8211; script to get information about the installed version of flickcurl</p>
<h2>SYNOPSIS</h2>
<p> <code>flickcurl-config</code> [ <i>OPTION</i> ]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> This program is <code>DEPRECATED</code> and <a href="/docs/linux/man/1-pkg-config/">pkg-config</a>(1) should be used to get flickcurl library parameters and dependencies. The compiling and linking flags are likely to not work since they do not import dependendent libraries (such as Raptor).</dl>
<p> Known values for OPTION are:</p>
<dl>
<dt><code>&#8211;prefix</code></p>
<dd> Get the flickcurl installation prefix.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print library linking information.</p>
<dt><code>&#8211;private-libs</code></p>
<dd> Print library private/static linking information.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print pre-processor and compiler flags</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information</p>
<dt><code>&#8211;version-decimal</code></p>
<dd> Output version as a decimal integer.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Kumar Appaiah &lt;akumar [at] ee.iitm.ac.in&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
