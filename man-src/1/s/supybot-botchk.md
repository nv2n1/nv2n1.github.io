---
title: "supybot-botchk(1)"
name: "supybot-botchk"
section: "1"
letter: "s"
url: "/docs/linux/man/1-supybot-botchk/"
description: "supybot-botchk – A script to start Supybot if it’s not already running."
---

<h2>NAME</h2>
<p> supybot-botchk &#8211; A script to start Supybot if it&#8217;s not already running.</p>
<h2>SYNOPSIS</h2>
<p> <code>supybot-botchk</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>supybot-botchk</code> is a script that will start Supybot if it detects that one is not currently running. This can be useful for scheduling <i><a href="/docs/linux/man/1-supybot/">supybot</a></i>(1) to run via <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Use verbose output when running the script.</p>
<dt><code>&#8211;botdir=</code><i>BOTDIR</i></p>
<dd> Determines which directory the bot be started in.</p>
<dt><code>&#8211;pidfile=</code><i>PIDFILE</i></p>
<dd> Specifies the name of the pidfile to look for. This should be relative to the given botdir.</p>
<dt><code>&#8211;supybot=</code><i>SUPYBOT</i></p>
<dd> Specifies the location of <i><a href="/docs/linux/man/1-supybot/">supybot</a></i>(1). If this is not given, it is assumed that <i><a href="/docs/linux/man/1-supybot/">supybot</a></i>(1) is in the user&#8217;s $PATH.</p>
<dt><code>&#8211;conffile=</code><i>CONFFILE</i></p>
<dd> Specifies the path to the bot&#8217;s configuration file. This will be used when (re)starting the bot.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-python/">python</a></i>(1), <i><a href="/docs/linux/man/1-supybot/">supybot</a></i>(1), <i><a href="/docs/linux/man/1-supybot-test/">supybot-test</a></i>(1), <i><a href="/docs/linux/man/1-supybot-wizard/">supybot-wizard</a></i>(1), <i><a href="/docs/linux/man/1-supybot-adduser/">supybot-adduser</a></i>(1), <i><a href="/docs/linux/man/1-supybot-plugin-doc/">supybot-plugin-doc</a></i>(1), <i><a href="/docs/linux/man/1-supybot-plugin-create/">supybot-plugin-create</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by James McCoy &lt;vega dot james at gmail dot com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the Supybot license, a BSD-style license. </p>
<h2>Index</h2>
