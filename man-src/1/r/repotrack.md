---
title: "repotrack(1)"
name: "repotrack"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repotrack/"
description: "repotrack – track a package and its dependencies and download them"
---

<h2>NAME</h2>
<p> repotrack &#8211; track a package and its dependencies and download them</p>
<h2>SYNOPSIS</h2>
<p> <code>repotrack</code> [options] package1 [package2&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>repotrack</code> is a program for keeping track of a particular package and its dependencies. It will download one or more packages and all dependencies. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a help message, and then quit.</p>
<dt><code>-c CONFIG, &#8211;config=CONFIG</code></p>
<dd> Config file to use (defaults to /etc/yum.conf).</p>
<dt><code>-a ARCH, &#8211;arch=ARCH</code></p>
<dd> Act as if running the specified arch (default: current arch).</p>
<dt><code>-r REPOID, &#8211;repoid=REPOID</code></p>
<dd> Specify repo ids to query, can be specified multiple times (default is all enabled).</p>
<dt><code>-t, &#8211;tempcache</code></p>
<dd> Use a temp dir for storing/accessing yum-cache.</p>
<dt><code>-p DESTDIR, &#8211;download_path=DESTDIR</code></p>
<dd> Path to download packages to.</p>
<dt><code>-u, &#8211;urls</code></p>
<dd> Instead of downloading RPMs, list the URLs that would be downloaded.</p>
<dt><code>-n, &#8211;newest</code></p>
<dd> Toggle downloading only the newest packages (defaults to newest-only).</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Output as little information as possible. </p>
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
