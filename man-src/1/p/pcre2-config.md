---
title: "pcre2-config(1)"
name: "pcre2-config"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcre2-config/"
description: "pcre2-config – program to return PCRE2 configuration"
---

<h2 class="name">NAME</h2>
<p> pcre2-config &#8211; program to return PCRE2 configuration </p>
<h2>SYNOPSIS</h2>
<pre><code>
pcre2 - config[--prefix][--exec - prefix][--version]
              [--libs8][--libs16][--libs32][--libs - posix]
              [--cflags][--cflags - posix]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>pcre2-config</code> returns the configuration of the installed PCRE2 libraries and the options required to compile a program to use them. Some of the options apply only to the 8-bit, or 16-bit, or 32-bit libraries, respectively, and are not available for libraries that have not been built. If an unavailable option is encountered, the &quot;usage&quot; information is output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;prefix</code></p>
<dd> Writes the directory prefix used in the PCRE2 installation for architecture independent files (<i>/usr</i> on many systems, <i>/usr/local</i> on some systems) to the standard output.</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd> Writes the directory prefix used in the PCRE2 installation for architecture dependent files (normally the same as <code>&#8211;prefix</code>) to the standard output.</p>
<dt><code>&#8211;version</code></p>
<dd> Writes the version number of the installed PCRE2 libraries to the standard output.</p>
<dt><code>&#8211;libs8</code></p>
<dd> Writes to the standard output the command line options required to link with the 8-bit PCRE2 library (<code>-lpcre2-8</code> on many systems).</p>
<dt><code>&#8211;libs16</code></p>
<dd> Writes to the standard output the command line options required to link with the 16-bit PCRE2 library (<code>-lpcre2-16</code> on many systems).</p>
<dt><code>&#8211;libs32</code></p>
<dd> Writes to the standard output the command line options required to link with the 32-bit PCRE2 library (<code>-lpcre2-32</code> on many systems).</p>
<dt><code>&#8211;libs-posix</code></p>
<dd> Writes to the standard output the command line options required to link with PCRE2&#8217;s POSIX API wrapper library (<code>-lpcre2-posix</code> <code>-lpcre2-8</code> on many systems).</p>
<dt><code>&#8211;cflags</code></p>
<dd> Writes to the standard output the command line options required to compile files that use PCRE2 (this may include some <code>-I</code> options, but is blank on many systems).</p>
<dt><code>&#8211;cflags-posix</code></p>
<dd> Writes to the standard output the command line options required to compile files that use PCRE2&#8217;s POSIX API wrapper library (this may include some <code>-I</code> options, but is blank on many systems).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-pcre2/">pcre2</a>(3)</code></p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Mark Baker for the Debian GNU/Linux system. It has been subsequently revised as a generic PCRE2 man page.</p>
<h2>REVISION</h2>
<pre>
Last updated: 28 September 2014
</pre>
<h2>Index</h2>
