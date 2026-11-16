---
title: "ractl(8)"
name: "ractl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-ractl/"
description: "ractl – Router Advertisement Control (ratools/ractl)"
---

<p>ractl &#8211; Router Advertisement Control (ratools/ractl)</p>
<h2>Synopsis</h2>
<p><code>ractl</code> [<code>-s|&#8211;socket</code> <i>UNIXSOCKET</i>] <i>command</i>&#8230;</p>
<h2>Description</h2>
<p>Control program for the Router Advertisement Daemin (ratools/rad) providing an easy to use command line interface.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;socket</code></dt>
<dd>Override default path of the control socket.</dd></dl>
<h2>Built-In Commands</h2>
<dl>
<dt><code>dump</code></dt>
<dd>Print configuration of all Router Advertisements to stdout.</dd>
<dt><code>show</code></dt>
<dd>Show all Router Advertisements.</dd>
<dt><code>version</code></dt>
<dd>Show version information for ratools/ractl.</dd>
<dt><code>loglevel</code></dt>
<dd>Set logging level of rad. Possible values are &#8216;info&#8217;, &#8216;warning&#8217;, and</dd></dl>
<h2>Module Commands</h2>
<p>There are more commands provided by modules. To learn more about them, have a look at the module&#8217;s manual pages.</p>
<h2>Availability</h2>
<p><code>ractl</code> is part of the ratools framework available from <a rel="nofollow" href="https://github.com/danrl/ratools">https://github.com/danrl/ratools</a></p>
<h2>Author</h2>
<p>Written by Dan Luedtke.</p>
