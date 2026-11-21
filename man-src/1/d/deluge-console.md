---
title: "deluge-console(1)"
name: "deluge-console"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deluge-console/"
description: "deluge-console – a bittorrent client curses interface"
---

<h2>SYNOPSIS</h2>
<p> <code>deluge-console [options]</code> </p>
<h2>DESCRIPTION</h2>
<p> Deluge utilizes a client/server model, with &#8216;deluged&#8217; being the daemon process and &#8216;deluge-console&#8217; being used to launch a console user-interface. </p>
<p> You can pass console commands directly from the command line and run multiple commands by separating them with a semi-colon (;).</p>
<h3>Console Commands:</h3>
<p>&nbsp;<wbr>info quit pause help resume del plugin cache add exit connect debug rm config recheck halt </p>
<h2>OPTIONS</h2>
<h3>General Options</h3>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>path</i>,&nbsp;<wbr><code>&#8211;config=</code><i>path</i></dt>
<dd> Set the config directory location. </dd>
</dl>
<h3>Logging Options</h3>
<dl>
<dt><code>-l&nbsp;<wbr></code><i>file</i>,&nbsp;<wbr><code>&#8211;logfile=</code><i>file</i></dt>
<dd> Output to designated logfile instead of stdout</dd>
<dt><code>-L&nbsp;<wbr></code><i>loglevel</i>,&nbsp;<wbr><code>&#8211;loglevel=</code><i>loglevel</i></dt>
<dd> Set the log level (default is error): <code>none, info, warning, error, critical, debug</code></dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Sets the log level to &#8216;none&#8217;, same as `-L none` </dd>
</dl>
<h3>Help Options</h3>
<dl>
<dt><code>-v, &#8211;version</code></dt>
<dd> Show program&#8217;s version number and exit.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show help message and exit. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-deluge/">deluge</a>(1),</code> <code><a href="/docs/linux/man/1-deluged/">deluged</a>(1),</code> <code><a href="/docs/linux/man/1-deluge-web/">deluge-web</a>(1)</code> </p>
<h2>AUTHORS</h2>
<p> <code>Deluge Team: <a rel="nofollow" href="http://www.deluge-torrent.org">http://www.deluge-torrent.org</a></code> </p>
