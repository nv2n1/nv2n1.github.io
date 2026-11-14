---
title: "aptitude-create-state-bundle(1)"
name: "aptitude-create-state-bundle"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aptitude-create-state-bundle/"
description: "aptitude-create-state-bundle – bundle the current aptitude state"
---

<h2 class="name">NAME</h2>
<p> aptitude-create-state-bundle &#8211; bundle the current aptitude state </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>aptitude-create-state-bundle</code> [&lt;<i>options</i>&gt;&#8230;] &lt;<i>output-file</i>&gt;</dl>
<h2>DESCRIPTION</h2>
<p> <code>aptitude-create-state-bundle</code></p>
<dd>produces a compressed archive storing the files that are required to replicate the current package archive state. The following files and directories are included in the bundle: </p>
<dl>
<dt>
<dd> &bull; <code>$HOME</code>/.aptitude</dl>
<dl>
<dt>
<dd> &bull; /var/lib/aptitude</dl>
<dl>
<dt>
<dd> &bull; /var/lib/apt</dl>
<dl>
<dt>
<dd> &bull; /var/cache/apt/*.bin</dl>
<dl>
<dt>
<dd> &bull; /etc/apt</dl>
<dl>
<dt>
<dd> &bull; /var/lib/dpkg/status</dl>
<p> The output of this program can be used as an argument to <code><a href="/docs/linux/man/1-aptitude-run-state-bundle/">aptitude-run-state-bundle</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;force-bzip2</code></p>
<dl>
<dt>
<dd> Override the autodetection of which compression algorithm to use. By default, <code>aptitude-create-state-bundle</code> uses <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) if it is available, and <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) otherwise. Passing this option forces the use of <code>bzip2</code> even if it doesn&#8217;t appear to be available.</dl>
<p> <code>&#8211;force-gzip</code></p>
<dl>
<dt>
<dd> Override the autodetection of which compression algorithm to use. By default, <code>aptitude-create-state-bundle</code> uses <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) if it is available, and <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) otherwise. Passing this option forces the use of <code>gzip</code> even if <code>bzip2</code> is available.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a brief usage message, then exit.</dl>
<p> <code>&#8211;print-inputs</code></p>
<dl>
<dt>
<dd> Instead of creating a bundle, display a list of the files and directories that the program would include if it generated a bundle.</dl>
<h2>FILE FORMAT</h2>
<p> The bundle file is simply a <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) file compressed with <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1) or <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), with each of the input directory trees rooted at &#8220;.&#8221;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aptitude-run-state-bundle/">aptitude-run-state-bundle</a></code>(1), <code><a href="/docs/linux/man/8-aptitude/">aptitude</a></code>(8), <code><a href="/docs/linux/man/8-apt/">apt</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> <code>Daniel Burrows</code> &lt;dburrows [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright 2007 Daniel Burrows. </p>
<p> This manual page is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This manual page is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA. </p>
<h2>Index</h2>
