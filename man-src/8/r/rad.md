---
title: "rad(8)"
name: "rad"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rad/"
description: "rad – Router Advertisement Daemon (ratools/rad)"
---

<p>rad &#8211; Router Advertisement Daemon (ratools/rad)</p>
<h2>Synopsis</h2>
<p><code>rad</code> [<code>-s|&#8211;socket</code> <i>UNIXSOCKET</i>] [<code>-l|&#8211;loglevel</code> <i>LOGGING LEVEL</i>] <i>command</i>&#8230;</p>
<h2>Description</h2>
<p>rad is a fast, dynamic, multi-threading daemon for sending IPv6 Router Advertisements (RA). It is controlled via ractl.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;socket</code></p>
<dd>Override default path of the control socket.</p>
<dt><code>&#8211;loglevel</code></p>
<dd>Set logging level. Possible values are &#8216;info&#8217;, &#8216;warning&#8217;, and</dl>
<h2>Availability</h2>
<p><code>rad</code> is part of the ratools framework available from <a rel="nofollow" href="https://github.com/danrl/ratools">https://github.com/danrl/ratools</a></p>
<h2>Author</h2>
<p>Written by Dan Luedtke.</p>
