---
title: "supybot-test(1)"
name: "supybot-test"
section: "1"
letter: "s"
url: "/docs/linux/man/1-supybot-test/"
description: "supybot-test – Runs the test suite for a Supybot plugin"
---

<h2>NAME</h2>
<p> supybot-test &#8211; Runs the test suite for a Supybot plugin</p>
<h2>SYNOPSIS</h2>
<p> <code>supybot-test</code> [<i>options</i>]<i> plugins</i></p>
<h2>DESCRIPTION</h2>
<p> <code>supybot-test</code> Runs the test suite for a Supybot plugin</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-c</code>, <code>&#8211;clean</code></p>
<dd> Cleans the various data/conf/logs directories before running tests.</p>
<dt><code>-t</code> TIMEOUT, &#8211;timeout=TIMEOUT</p>
<dd> Specifies the timeout for tests to return responses.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Sets the verbose flag, logging extra information about each test that runs.</p>
<dt><code>&#8211;no-network</code></p>
<dd> Prevents the network-based tests from being run.</p>
<dt><code>&#8211;trace</code></p>
<dd> Traces all calls made. Unless you&#8217;re really in a pinch, you probably shouldn&#8217;t do this; it results in copious amounts of output.</p>
<dt>, &#8211;plugins-dir=PLUGINSDIR</p>
<dd> Looks in the given directory for plugins and loads the tests for all of them.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-python/">python</a></i>(1), <i><a href="/docs/linux/man/1-supybot/">supybot</a></i>(1), <i><a href="/docs/linux/man/1-supybot-botchk/">supybot-botchk</a></i>(1), <i><a href="/docs/linux/man/1-supybot-wizard/">supybot-wizard</a></i>(1), <i><a href="/docs/linux/man/1-supybot-adduser/">supybot-adduser</a></i>(1), <i><a href="/docs/linux/man/1-supybot-plugin-doc/">supybot-plugin-doc</a></i>(1), <i><a href="/docs/linux/man/1-supybot-plugin-create/">supybot-plugin-create</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by James McCoy &lt;vega dot james at gmail dot com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the Supybot license, a BSD-style license. </p>
<h2>Index</h2>
