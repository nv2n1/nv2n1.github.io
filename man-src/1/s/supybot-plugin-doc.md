---
title: "supybot-plugin-doc(1)"
name: "supybot-plugin-doc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-supybot-plugin-doc/"
description: "supybot-plugin-doc – Generates the documentation for a Supybot plugin"
---

<h2>NAME</h2>
<p> supybot-plugin-doc &#8211; Generates the documentation for a Supybot plugin</p>
<h2>SYNOPSIS</h2>
<p> <code>supybot-plugin-doc</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>supybot-plugin-doc</code> is used to generate documentation (StructuredText or reStructuredText format) for a <i><a href="/docs/linux/man/1-supybot/">supybot</a></i>(1) plugin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-c</code>, <code>&#8211;clean</code></p>
<dd> Clean the various data/conf/log directories after generating the docs.</p>
<dt><code>-o</code>, <code>&#8211;output-dir=</code><i>OUTPUTDIR</i></p>
<dd> Specifies the directory in which to write the documentation for the plugin.</p>
<dt><code>-f</code>, <code>&#8211;format=</code><i>FORMAT</i></p>
<dd> Specifies which output format to use. Choices are &#8216;rst&#8217; or &#8216;stx&#8217;.</p>
<dt><code>&#8211;plugins-dir=</code><i>PLUGINSDIRS</i></p>
<dd> Looks in the given directory for plugins and generates documentation for all of them.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-python/">python</a></i>(1), <i><a href="/docs/linux/man/1-supybot/">supybot</a></i>(1), <i><a href="/docs/linux/man/1-supybot-test/">supybot-test</a></i>(1), <i><a href="/docs/linux/man/1-supybot-botchk/">supybot-botchk</a></i>(1), <i><a href="/docs/linux/man/1-supybot-wizard/">supybot-wizard</a></i>(1), <i><a href="/docs/linux/man/1-supybot-adduser/">supybot-adduser</a></i>(1), <i><a href="/docs/linux/man/1-supybot-plugin-create/">supybot-plugin-create</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by James McCoy &lt;vega dot james at gmail dot com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the Supybot license, a BSD-style license. </p>
<h2>Index</h2>
