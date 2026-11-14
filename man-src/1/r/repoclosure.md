---
title: "repoclosure(1)"
name: "repoclosure"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repoclosure/"
description: "repoclosure – display a list of unresolved dependencies for a yum repository"
---

<h2>NAME</h2>
<p> repoclosure &#8211; display a list of unresolved dependencies for a yum repository</p>
<h2>SYNOPSIS</h2>
<p> <code>repoclosure</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>repoclosure</code> is a program that reads package metadata from one or more yum repositories, checks all dependencies, and displays a list of packages with unresolved dependencies. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a help message, and then quit.</p>
<dt><code>-c CONFIG, &#8211;config=CONFIG</code></p>
<dd> Config file to use (defaults to /etc/yum.conf).</p>
<dt><code>-a ARCH, &#8211;arch=ARCH</code></p>
<dd> Check packages of the given archs, can be specified multiple times (default: current arch).</p>
<dt><code>&#8211;basearch=BASEARCH</code></p>
<dd> Set the basearch for yum to run as.</p>
<dt><code>-b, &#8211;builddeps</code></p>
<dd> Check build dependencies only (needs source repos enabled).</p>
<dt><code>-l LOOKASIDE, &#8211;lookaside=LOOKASIDE</code></p>
<dd> Specify a lookaside repo id to query, can be specified multiple times.</p>
<dt><code>-r REPOID, &#8211;repoid=REPOID</code></p>
<dd> Specify repo ids to query, can be specified multiple times (default is all enabled).</p>
<dt><code>-t, &#8211;tempcache</code></p>
<dd> Use a temp dir for storing/accessing yum-cache.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Run quietly: no warnings printed to stderr.</p>
<dt><code>-n, &#8211;newest</code></p>
<dd> Check only the newest packages in the repos.</p>
<dt><code>&#8211;repofrompath=REPOID,PATH/URL</code></p>
<dd> Specify a path or url to a repository (same path as in a baseurl) to add to the repositories for this query. This option can be used multiple times. If you want to view only the pkgs from this repository combine this with &#8211;repoid. The repoid for the repository is specified by REPOID.</p>
<dt><code>-p PKG, &#8211;pkg=PKG</code></p>
<dd> Check closure for this package only</p>
<dt><code>-g GROUP, &#8211;group=GROUP</code></p>
<dd> Check closure for packages in this group only </p>
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
