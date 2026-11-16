---
title: "deluged(1)"
name: "deluged"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deluged/"
description: "deluged – a bittorrent client daemon"
---

<h2 class="name">NAME</h2>
<p> deluged &#8211; a bittorrent client daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>deluged [options]</code> </p>
<h2>DESCRIPTION</h2>
<p> Deluge utilizes a client/server model, with &#8216;deluged&#8217; being the daemon process and &#8216;deluge&#8217; being used to launch a user-interface. </p>
<p> By default, &#8216;deluged&#8217; will run as a daemon, to prevent this you can run deluged with the -d option. This option is useful for running deluged with the start-stop-daemon. </p>
<h2>OPTIONS</h2>
<h3>General Options</h3>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>path</i>,&nbsp;<wbr><code>&#8211;config=</code><i>path</i></dt>
<dd> Set the config directory location. </dd>
</dl>
<h3>Daemon Options</h3>
<dl>
<dt><code>-p&nbsp;<wbr></code><i>port</i>,&nbsp;<wbr><code>&#8211;port=</code><i>port</i></dt>
<dd> Port daemon will listen on, default is 58846</dd>
<dt><code>-i&nbsp;<wbr></code><i>ip_address</i>,&nbsp;<wbr><code>&#8211;interface=</code><i>ip_address</i></dt>
<dd> Interface daemon will listen for bittorrent connections on, this should be an IP address</dd>
<dt><code>-u&nbsp;<wbr></code><i>ip_address</i>,&nbsp;<wbr><code>&#8211;ui-interface=</code><i>ip_address</i></dt>
<dd> Interface daemon will listen for UI connections on, this should be an IP address</dd>
<dt><code>-d, &#8211;do-not-daemonize</code></dt>
<dd> Do not daemonize</dd>
<dt><code>-P&nbsp;<wbr></code><i>file</i>,&nbsp;<wbr><code>&#8211;pidfile=</code><i>file</i></dt>
<dd> Use pidfile to store process id </dd>
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
<p> <code><a href="/docs/linux/man/1-deluge/">deluge</a>(1),</code> <code><a href="/docs/linux/man/1-deluge-web/">deluge-web</a>(1),</code> <code><a href="/docs/linux/man/1-deluge-console/">deluge-console</a>(1)</code> </p>
<h2>AUTHORS</h2>
<p> <code>Deluge Team: <a rel="nofollow" href="http://www.deluge-torrent.org">http://www.deluge-torrent.org</a></code> </p>
<h2>Index</h2>
