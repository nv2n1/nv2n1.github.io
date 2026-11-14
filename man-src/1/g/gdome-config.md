---
title: "gdome-config(1)"
name: "gdome-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdome-config/"
description: "gdome-config – script to get information about the installed version of gdome2"
---

<h2>NAME</h2>
<p> gdome-config &#8211; script to get information about the installed version of gdome2</p>
<h2>SYNOPSIS</h2>
<p> <code>gdome-config</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;exec-prefix<i>[=DIR]</i>] [&#8211;libs] [&#8211;cflags] [&#8211;version] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> <i>gdome-config</i> is a tool that is used to determine the compile and linker flags that should be used to compile and link programs that use <i>gdome2</i>.</p>
<h2>OPTIONS</h2>
<p> <i>gdome-config</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the currently installed version of <i>gdome2</i> on the standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link a <i>gdome2</i> program.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile a <i>gdome2</i> program.</p>
<dt><code>&#8211;prefix=DIR</code></p>
<dd> If specified, use DIR instead of the installation prefix that <i>gdome2</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<dt><code>&#8211;exec-prefix=DIR</code></p>
<dd> If specified, use DIR instead of the installation exec prefix that <i>gdome2</i> was built when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a short help text and exit.</dl>
<h2>AUTHOR</h2>
<p> This manual page was added by Enrico Zini &lt;zinie [at] cs.unibo.it&gt; for the Debian GNU/Linux system (but may be used by others). The page was made editing the manpage written by Fredrik Hallenberg &lt;hallon [at] lysator.liu.se&gt; for the libxml2 Debian GNU/Linux package. </p>
<h2>Index</h2>
