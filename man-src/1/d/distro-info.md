---
title: "distro-info(1)"
name: "distro-info"
section: "1"
letter: "d"
url: "/docs/linux/man/1-distro-info/"
description: "distro-info – provides information about the distributions’ releases"
---

<h2>SYNOPSIS</h2>
<p> <code>distro-info</code> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>distro-info</code> is a symlink to the distro-info command for your distribution. On Debian it links to <code>debian-distro-info</code> and on Ubuntu it links to <code>ubuntu-distro-info</code>. All options described in this manual page are available in all <code>distro-info</code> commands. All other options, which are not described here, are distribution specific.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;date</code>=<i>DATE</dt>
<dd> date for calculating the version (default: today)</dd>
<dt></i><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display help message and exit</dd>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> list all known versions</dd>
<dt><code>-y</code>[<i>MILESTONE</i>], <code>&#8211;days</code>[=<i>MILESTONE</i>]</dt>
<dd> display number of days until specified version reaches the specified milestone. <i>MILESTONE</i> may be one of <i>created</i>, <i>release</i>, <i>eol</i>, or <i>eol-server</i>. If no milestone is specified, assume <i>release</i>. For options that return a list, display the normal output followed by whitespace and the number of days until the specified milestone.</dd>
<dt><code>-d</code>, <code>&#8211;devel</code></dt>
<dd> latest development version</dd>
<dt><code>&#8211;series</code>=<i>SERIES</dt>
<dd> series to calculate the version for</dd>
<dt></i><code>-s</code>, <code>&#8211;stable</code></dt>
<dd> latest stable version</dd>
<dt><code>&#8211;supported</code></dt>
<dd> list of all supported versions, including development releases</dd>
<dt><code>&#8211;unsupported</code></dt>
<dd> list of all unsupported stable versions</dd>
<dt><code>-c</code>, <code>&#8211;codename</code></dt>
<dd> print the codename (default)</dd>
<dt><code>-r</code>, <code>&#8211;release</code></dt>
<dd> print the release version</dd>
<dt><code>-f</code>, <code>&#8211;fullname</code></dt>
<dd> print the full name</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-debian-distro-info/">debian-distro-info</a></code>(1), <code><a href="/docs/linux/man/1-ubuntu-distro-info/">ubuntu-distro-info</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The script and this manual page was written by Benjamin Drung &lt;bdrung [at] debian.org&gt;. </p>
