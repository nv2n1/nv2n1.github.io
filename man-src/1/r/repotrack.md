---

title: "repotrack(1)"
name: "repotrack"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repotrack/"
description: "repotrack – track a package and its dependencies and download them"
---

<p> repotrack &#8211; track a package and its dependencies and download them</p>
<h2>SYNOPSIS</h2>
<p> <code>repotrack</code> [options] package1 [package2&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>repotrack</code> is a program for keeping track of a particular package and its dependencies. It will download one or more packages and all dependencies. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a help message, and then quit.</dd>
<dt><code>-c CONFIG, &#8211;config=CONFIG</code></dt>
<dd> Config file to use (defaults to /etc/yum.conf).</dd>
<dt><code>-a ARCH, &#8211;arch=ARCH</code></dt>
<dd> Act as if running the specified arch (default: current arch).</dd>
<dt><code>-r REPOID, &#8211;repoid=REPOID</code></dt>
<dd> Specify repo ids to query, can be specified multiple times (default is all enabled).</dd>
<dt><code>-t, &#8211;tempcache</code></dt>
<dd> Use a temp dir for storing/accessing yum-cache.</dd>
<dt><code>-p DESTDIR, &#8211;download_path=DESTDIR</code></dt>
<dd> Path to download packages to.</dd>
<dt><code>-u, &#8211;urls</code></dt>
<dd> Instead of downloading RPMs, list the URLs that would be downloaded.</dd>
<dt><code>-n, &#8211;newest</code></dt>
<dd> Toggle downloading only the newest packages (defaults to newest-only).</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Output as little information as possible. </dd>
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
