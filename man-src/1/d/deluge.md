---
title: "deluge(1)"
name: "deluge"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deluge/"
description: "deluge – a bittorrent client"
---

<h2 class="name">NAME</h2>
<p> deluge &#8211; a bittorrent client</p>
<h2>SYNOPSIS</h2>
<p> <code>deluge [options]</code> [<i>torrent-file</i>] </p>
<h2>DESCRIPTION</h2>
<p> Deluge utilizes a client/server model, with &#8216;deluged&#8217; being the daemon process and &#8216;deluge&#8217; being used to launch a user-interface. </p>
<p> By default, Deluge will run in &#8216;Classic&#8217; mode where the daemon functionality will be hidden and the GtkUI will automatically launch a &#8216;deluged&#8217; process. You can turn this off in the Preferences dialog. </p>
<h2>OPTIONS</h2>
<h3>General Options</h3>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>path</i>,&nbsp;<wbr><code>&#8211;config=</code><i>path</i></p>
<dd> Set the config directory location. </p>
</dl>
<h3>UI Options</h3>
<dl>
<dt><code>-u&nbsp;<wbr></code><i>ui</i>,&nbsp;<wbr><code>&#8211;ui=</code><i>ui</i></p>
<dd> The UI that you wish to launch, current options include: gtk, web or console</p>
<dt><code>-s&nbsp;<wbr></code><i>default_ui</i>,&nbsp;<wbr><code>&#8211;set-default-ui=</code><i>default_ui</i></p>
<dd> Sets the default UI to be run when no UI is specified</p>
<dt><code>-a&nbsp;<wbr></code><i>args</i>,&nbsp;<wbr><code>&#8211;args=</code><i>args</i></p>
<dd> Arguments to pass to a UI, -a &#8216;&#8211;option args&#8217; </p>
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
<p> <code><a href="/docs/linux/man/1-deluged/">deluged</a>(1),</code> <code><a href="/docs/linux/man/1-deluge-web/">deluge-web</a>(1),</code> <code><a href="/docs/linux/man/1-deluge-console/">deluge-console</a>(1)</code> </p>
<h2>AUTHORS</h2>
<p> <code>Deluge Team: <a rel="nofollow" href="http://www.deluge-torrent.org">http://www.deluge-torrent.org</a></code> </p>
<h2>Index</h2>
