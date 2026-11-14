---
title: "tap2deb(1)"
name: "tap2deb"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tap2deb/"
description: "tap2deb – create Debian packages which wrap .tap files"
---

<h2>NAME</h2>
<p> tap2deb &#8211; create Debian packages which wrap .tap files</p>
<h2>SYNOPSIS</h2>
<p> <code>tap2deb</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> Create a ready to upload Debian package in &quot;.build&quot;</p>
<dl>
<dt><code>-u</code>, <code>&#8211;unsigned</code></p>
<dd> do not sign the Debian package</p>
<dt><code>-t</code>, <code>&#8211;tapfile</code> <i>&lt;tapfile&gt;</i></p>
<dd> Build the application around the given .tap (default twistd.tap)</p>
<dt><code>-y</code>, <code>&#8211;type</code> <i>&lt;type&gt;</i></p>
<dd> The configuration has the given type . Allowable types are <code>tap</code>, <code>source</code>, <code>xml</code> and <code>python</code>. The first three types are <code>mktap</code> output formats, while the last one is a manual building of application (see <code><a href="/docs/linux/man/1-twistd/">twistd</a>(1)</code>, the <code>-y</code> option).</p>
<dt><code>-p</code>, <code>&#8211;protocol</code> <i>&lt;protocol&gt;</i></p>
<dd> The name of the protocol this will be used to serve. This is intended as a part of the description. Default is the name of the tapfile, minus any extensions.</p>
<dt><code>-d</code>, <code>&#8211;debfile</code> <i>&lt;debfile&gt;</i></p>
<dd> The name of the debian package. Default is &#8216;twisted-&#8216;+protocol.</p>
<dt><code>-V</code>, <code>&#8211;set-version</code> <i>&lt;version&gt;</i></p>
<dd> The version of the Debian package. The default is 1.0</p>
<dt><code>-e</code>, <code>&#8211;description</code> <i>&lt;description&gt;</i></p>
<dd> The one-line description. Default is uninteresting.</p>
<dt><code>-l</code>, <code>&#8211;long_description</code> <i>&lt;long_description&gt;</i></p>
<dd> A multi-line description. Default is explanation about this being an automatic package created from tap2deb.</p>
<dt><code>-m</code>, <code>&#8211;maintainer</code> <i>&lt;maintainer&gt;</i></p>
<dd> The maintainer, as &quot;Name Lastname &lt;email address&gt;&quot;. This will go in the meta-files, as well as be used as the id to sign the package.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</dl>
<h2>AUTHOR</h2>
<p> Written by Moshe Zadka, based on twistd&#8217;s help messages</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2008 Twisted Matrix Laboratories.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
