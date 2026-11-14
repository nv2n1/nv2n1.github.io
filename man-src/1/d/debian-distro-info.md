---
title: "debian-distro-info(1)"
name: "debian-distro-info"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debian-distro-info/"
description: "debian-distro-info – provides information about Debian’s distributions"
---

<h2 class="name">NAME</h2>
<p> debian-distro-info &#8211; provides information about Debian&#8217;s distributions </p>
<h2>SYNOPSIS</h2>
<p> <code>debian-distro-info</code> [<i>OPTIONS</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;date</code>=<i>DATE</p>
<dd> date for calculating the version (default: today)</p>
<dt></i><code>-h</code>, <code>&#8211;help</code></p>
<dd> display help message and exit</p>
<dt><code>&#8211;alias</code>=<i>DIST</p>
<dd> print the alias (oldstable, stable, testing, unstable) relative to the distribution codename passed as an argument. Only distribution codenames composed of lower case ASCII letters are accepted, and if the distribution does not qualify as oldstable, stable, testing, or unstable, then the same codename passed as argument is returned.</p>
<dt></i><code>-a</code>, <code>&#8211;all</code></p>
<dd> list all known versions</p>
<dt><code>-y</code>[<i>MILESTONE</i>], <code>&#8211;days</code>[=<i>MILESTONE</i>]</p>
<dd> display number of days until specified version reaches the specified milestone. <i>MILESTONE</i> may be one of <i>created</i>, <i>release</i>, or <i>eol</i>. If no milestone is specified, assume <i>release</i>. For options that return a list, display the normal output followed by whitespace and the number of days until the specified milestone. If milestone cannot be calculated, the string &#8216;(unknown)&#8217; is displayed. Unless one of <code>-c</code>, <code>-f</code> or <code>-r</code> is specified, only the number of days will be displayed.</p>
<dt><code>-d</code>, <code>&#8211;devel</code></p>
<dd> latest development version</p>
<dt><code>-o</code>, <code>&#8211;old</code></p>
<dd> latest old (stable) version</p>
<dt><code>&#8211;series</code>=<i>SERIES</p>
<dd> series to calculate the version for</p>
<dt></i><code>-s</code>, <code>&#8211;stable</code></p>
<dd> latest stable version</p>
<dt><code>&#8211;supported</code></p>
<dd> list of all supported versions, including development releases</p>
<dt><code>-t</code>, <code>&#8211;testing</code></p>
<dd> latest testing version</p>
<dt><code>&#8211;unsupported</code></p>
<dd> list of all unsupported stable versions</p>
<dt><code>-c</code>, <code>&#8211;codename</code></p>
<dd> print the codename (default)</p>
<dt><code>-r</code>, <code>&#8211;release</code></p>
<dd> print the release version</p>
<dt><code>-f</code>, <code>&#8211;fullname</code></p>
<dd> print the full name</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-distro-info/">distro-info</a></code>(1), <code><a href="/docs/linux/man/1-ubuntu-distro-info/">ubuntu-distro-info</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The script and this manual page was written by Benjamin Drung &lt;bdrung [at] debian.org&gt;. </p>
<h2>Index</h2>
