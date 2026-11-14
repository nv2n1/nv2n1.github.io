---
title: "deluge-console(1)"
name: "deluge-console"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deluge-console/"
description: "deluge-console – a bittorrent client curses interface"
---

<h2 class="name">NAME</h2>
<p> deluge-console &#8211; a bittorrent client curses interface</p>
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
<dt><code>-c&nbsp;<wbr></code><i>path</i>,&nbsp;<wbr><code>&#8211;config=</code><i>path</i></p>
<dd> Set the config directory location. </p>
</dl>
<h3>Logging Options</h3>
<dl>
<dt><code>-l&nbsp;<wbr></code><i>file</i>,&nbsp;<wbr><code>&#8211;logfile=</code><i>file</i></p>
<dd> Output to designated logfile instead of stdout</p>
<dt><code>-L&nbsp;<wbr></code><i>loglevel</i>,&nbsp;<wbr><code>&#8211;loglevel=</code><i>loglevel</i></p>
<dd> Set the log level (default is error): <code>none, info, warning, error, critical, debug</code></p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Sets the log level to &#8216;none&#8217;, same as `-L none` </p>
</dl>
<h3>Help Options</h3>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Show program&#8217;s version number and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help message and exit. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-deluge/">deluge</a>(1),</code> <code><a href="/docs/linux/man/1-deluged/">deluged</a>(1),</code> <code><a href="/docs/linux/man/1-deluge-web/">deluge-web</a>(1)</code> </p>
<h2>AUTHORS</h2>
<p> <code>Deluge Team: <a rel="nofollow" href="http://www.deluge-torrent.org">http://www.deluge-torrent.org</a></code> </p>
<h2>Index</h2>
