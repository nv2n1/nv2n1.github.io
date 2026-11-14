---
title: "hman(1)"
name: "hman"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hman/"
description: "hman – browse the on-line manual pages"
---

<h2 class="name">NAME</h2>
<p> hman &#8211; browse the on-line manual pages </p>
<h2>SYNOPSIS</h2>
<p> <code>hman</code> [ -P <i>browser</i> ] [ -H <i>host</i> ] [ <i>section</i> ] <i>name</i><br />
 <code>hman</code> [ -P <i>browser</i> ] [ -H <i>host</i> ] [ <i>section</i> ] [ index ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>hman</code> script is an interface to <a href="/docs/linux/man/1-man2html/">man2html</a>(1) that allows you to enter man page requests at the command line and view the output in your favourite browser. The behaviour reminds of that of <code><a href="/docs/linux/man/1-man/">man</a></code>(1) so that many people will be able to alias <code>hman</code> to <code>man</code>. If the browser used is netscape, and an incarnation of netscape is running already, <code>hman</code> will pass the request to the existing browser. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-P browser</code></p>
<dd> Specify which browser (like lynx, xmosaic, arena, chimera, netscape, amaya, &#8230;) to use. This option overrides the <code>MANHTMLPAGER</code> environment variable. The default is <code>sensible-browser</code>.<br />
 A special value <i>lynxcgi</i> can be used for the non-httpd version of <code>lynx</code>, but this requires the <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1) command to be installed and approprietly configured.</p>
<dt><code>-H host</code></p>
<dd> Specify from what host to get the man pages. This option overrides the <code>MANHTMLHOST</code> environment variable. The default is <code>localhost</code>. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>MANHTMLPAGER</p>
<dd> The default browser to use is selected using this environment variable.</p>
<dt>MANHTMLHOST</p>
<dd> The default host to use is selected using this environment variable. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a></code>(1), <code><a href="/docs/linux/man/1-man2html/">man2html</a></code>(1), <code><a href="/docs/linux/man/1-arena/">arena</a></code>(1), <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1), <code><a href="/docs/linux/man/1-sensible-browser/">sensible-browser</a></code>(1), <code><a href="/docs/linux/man/1-netscape/">netscape</a></code>(1), <code><a href="/docs/linux/man/1-xmosaic/">xmosaic</a></code>(1), <code><a href="/docs/linux/man/1-glimpse/">glimpse</a></code>(1) </p>
<p> <a rel="nofollow" href="http://www.mcom.com/newsref/std/x-remote.html">http://www.mcom.com/newsref/std/x-remote.html</a> </p>
<h2>Index</h2>
