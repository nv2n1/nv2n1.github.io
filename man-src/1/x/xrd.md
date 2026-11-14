---
title: "xrd(1)"
name: "xrd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrd/"
description: "xrd – xrootd file and directory meta-data utility"
---

<h2>NAME</h2>
<p> xrd &#8211; xrootd file and directory meta-data utility</p>
<h2>SYNOPSIS</h2>
<pre><code>
xrd[host][options][command] options : [-DSpname stringval][-DIpname numberval][options]
                                                          [-Oopaqueinfo][-h]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>This tool is DEPRECATED. Please use xrdfs instead.</code> </p>
<p> The <code>xrd</code> utility executes meta-data oriented operations (e.g., ls, mv, rm, etc.) on one or more xrootd servers. Usage synopsis can be displayed by typing &quot;<code>xrd -h</code>&quot;. Command help is available by invoking <code>xrd</code> with no command line options or parameters and then typing &quot;help&quot; in response to the input prompt.</p>
<h2>OPTIONS</h2>
<p> <code>-DS</code><i>pname stringval</i></p>
<dl>
<dt>
<dd> set the internal parameter <i>pname</i> with the string value <i>stringval</i>. </p>
</dl>
<p> <code>-DI</code><i>pname numberval</i></p>
<dl>
<dt>
<dd> set the internal parameter <i>pname</i> with the numeric value <i>numberval</i>. </p>
</dl>
<p> <code>-O</code><i>opaqueinfo</i></p>
<dl>
<dt>
<dd> add opaque information <i>opaqueinfo</i> to any path. </p>
</dl>
<p> <code>-h</code> display usage information.</p>
<h2>NOTES</h2>
<p> See XrdClientConst.hh for a list of parameters. Documentation for all components associated with <code>xrd</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>DIAGNOSTICS</h2>
<p> Errors yield an error message and a non-zero exit status.</p>
<h2>LICENSE</h2>
<p> License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>SUPPORT LEVEL</h2>
<p> The <code>xrd</code> command is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center> </p>
<h2>Index</h2>
