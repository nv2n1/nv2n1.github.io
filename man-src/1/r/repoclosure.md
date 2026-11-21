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
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a help message, and then quit.</dd>
<dt><code>-c CONFIG, &#8211;config=CONFIG</code></dt>
<dd> Config file to use (defaults to /etc/yum.conf).</dd>
<dt><code>-a ARCH, &#8211;arch=ARCH</code></dt>
<dd> Check packages of the given archs, can be specified multiple times (default: current arch).</dd>
<dt><code>&#8211;basearch=BASEARCH</code></dt>
<dd> Set the basearch for yum to run as.</dd>
<dt><code>-b, &#8211;builddeps</code></dt>
<dd> Check build dependencies only (needs source repos enabled).</dd>
<dt><code>-l LOOKASIDE, &#8211;lookaside=LOOKASIDE</code></dt>
<dd> Specify a lookaside repo id to query, can be specified multiple times.</dd>
<dt><code>-r REPOID, &#8211;repoid=REPOID</code></dt>
<dd> Specify repo ids to query, can be specified multiple times (default is all enabled).</dd>
<dt><code>-t, &#8211;tempcache</code></dt>
<dd> Use a temp dir for storing/accessing yum-cache.</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Run quietly: no warnings printed to stderr.</dd>
<dt><code>-n, &#8211;newest</code></dt>
<dd> Check only the newest packages in the repos.</dd>
<dt><code>&#8211;repofrompath=REPOID,PATH/URL</code></dt>
<dd> Specify a path or url to a repository (same path as in a baseurl) to add to the repositories for this query. This option can be used multiple times. If you want to view only the pkgs from this repository combine this with &#8211;repoid. The repoid for the repository is specified by REPOID.</dd>
<dt><code>-p PKG, &#8211;pkg=PKG</code></dt>
<dd> Check closure for this package only</dd>
<dt><code>-g GROUP, &#8211;group=GROUP</code></dt>
<dd> Check closure for packages in this group only </dd>
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
