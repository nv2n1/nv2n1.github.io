---
title: "spectool(1)"
name: "spectool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spectool/"
description: "spectool – manual page for spectool v1.0.10rpmdev1"
---

<h2>NAME</h2>
<p> spectool &#8211; manual page for spectool v1.0.10rpmdev1</p>
<h2>SYNOPSIS</h2>
<p> <code>spectool</code> [<i>&lt;options&gt;</i>] <i>&lt;specfile&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> Spectool is a tool to expand and download sources and patches from specfiles. </p>
<p> If you experience problems with specific specfiles, try to run</p>
<dl>
<dt>
<dd> rpmbuild <code>&#8211;nobuild</code> <code>&#8211;nodeps</code> &lt;specfile&gt;</dl>
<p> on the file which might give a clue why spectool fails on a file (ignore anything about missing sources or patches). The plan is to catch errors like this in spectool itself and warn the user about it in the future.</p>
<h2>OPTIONS</h2>
<h3>Operating mode:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;lf</code>, <code>&#8211;list-files</code></p>
<dd> lists the expanded sources/patches (default)</p>
<dt><code>-g</code>, <code>&#8211;gf</code>, <code>&#8211;get-files</code></p>
<dd> gets the sources/patches that are listed with a URL</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help screen</dl>
<h3>Files on which to operate:</h3>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> all files, sources and patches (default)</p>
<dt><code>-S</code>, <code>&#8211;sources</code></p>
<dd> all sources</p>
<dt><code>-P</code>, <code>&#8211;patches</code></p>
<dd> all patches</p>
<dt><code>-s</code>, <code>&#8211;source</code> x[,y[,&#8230;]]</p>
<dd> specified sources</p>
<dt><code>-p</code>, <code>&#8211;patch</code> a[,b[,&#8230;]]</p>
<dd> specified patches</dl>
<h3>Miscellaneous:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;define</code> &#8216;macro value&#8217;</p>
<dd> defines RPM macro &#8216;macro&#8217; to be &#8216;value&#8217;</p>
<dt><code>-C</code>, <code>&#8211;directory</code> dir</p>
<dd> download into specified directory (default &#8216;.&#8217;)</p>
<dt><code>-R</code>, <code>&#8211;sourcedir</code></p>
<dd> download into rpm&#8217;s %{_sourcedir}</p>
<dt><code>-n</code>, <code>&#8211;dryrun</code>, <code>&#8211;dry-run</code></p>
<dd> don&#8217;t download anything, just show what would be done</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> try to unlink and download if target files exist</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> output debug info, don&#8217;t clean up when done</dl>
<h2>FILES</h2>
<p> <i>/etc/rpmdevtools/curlrc</i></p>
<dl>
<dt>
<dd> optional <a href="/docs/linux/man/1-curl/">curl</a>(1) configuration </p>
</dl>
<h2>Index</h2>
