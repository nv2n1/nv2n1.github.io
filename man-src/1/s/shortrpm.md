---
title: "shortrpm(1)"
name: "shortrpm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shortrpm/"
description: "shortrpm – Short-circuit binary RPM package build"
---

<h2>NAME</h2>
<p> <code>shortrpm</code> &#8211; Short-circuit binary RPM package build</p>
<h2>SYNOPSIS</h2>
<p> <code>shortrpm</code> [-<code>-bb</code> ] [-<code>&#8211;short-circuit</code> ] [<i>rpmbuild options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>shortrpm</code> tricks <a href="/docs/linux/man/1-rpmbuild/">rpmbuild</a>(1) into thinking certain scriptlets in SPEC file are empty, effectively skipping their run and proceeding to build the binary package from files from previous %install scriptlet run in BuildRoot. The trickery only takes place if both <i>-bb</i> and <i>&#8211;short-circuit</i> options are specified. </p>
<p> See <a href="/docs/linux/man/1-rpmbuild/">rpmbuild</a>(1) manual for descriptions of all options.</p>
<h2>BUGS</h2>
<p> Line numbers in eventual error messages may not correspond to actual line numbers in SPEC file. </p>
<p> <a href="/docs/linux/man/3-open/">open</a>(3) function is overriden for rpmbuild&#8217;s children as well. </p>
<p> If <a href="/docs/linux/man/1-rpmbuild/">rpmbuild</a>(1) crashes when using <code>shortrpm</code> please do not send problem report to RPM developers unless you can reproduce the problem with clean RPM as well.</p>
<h2>AUTHORS</h2>
<p> <code>shortrpm</code> was written by Lubomir Rintel &lt;lkundrak [at] v3.sk&gt;. </p>
<p> Latest version can be obtained from &lt;<a rel="nofollow" href="http://v3.sk/~lkundrak/shortrpm">http://v3.sk/~lkundrak/shortrpm</a>&gt;. </p>
<h2>Index</h2>
