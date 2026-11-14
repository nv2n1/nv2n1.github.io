---
title: "transmission-gtk(1)"
name: "transmission-gtk"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transmission-gtk/"
description: "transmission-gtk – a bittorrent client"
---

<h2 class="name">NAME</h2>
<p> <code>transmission-gtk</code> &#8211; a bittorrent client </p>
<h2>SYNOPSIS</h2>
<p> <code>transmission-gtk</code> &#8211;<code>?</code><br />
<code>transmission-gtk</code> [-<code>pqm</code> ] [<i>torrent-file &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>transmission-gtk</code> is a fast and easy BitTorrent client. </p>
<p> BitTorrent is a peer-to-peer file transfer protocol which uses a metainfo file (usually with the .torrent file extension) and a central tracker to distribute file data amongst a group of peers. For more information on the BitTorrent protocol see <a rel="nofollow" href="http://www.bittorrent.org/">http://www.bittorrent.org/</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-? &#8211;help</code></p>
<dd> Show help options</p>
<dt><code>-p &#8211;paused</code></p>
<dd> Start with all torrents paused</p>
<dt><code>-m &#8211;minimized</code></p>
<dd> Start minimized in notification area</p>
<dt><code>-g, &#8211;config-dir </code><i>directory</i></p>
<dd> Where to look for configuration files. This can be used to swap between using the cli, daemon, gtk, and qt clients. See <a rel="nofollow" href="https://github.com/transmission/transmission/wiki/Configuration-Files">https://github.com/transmission/transmission/wiki/Configuration-Files</a> for more information.</dl>
<p> Multiple .torrent files may be added at startup by appending them on the command line. If <code>transmission-gtk</code> is already running, the torrents will be added to the running instance.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRANSMISSION_HOME</code></p>
<dd> Sets the default config-dir.</p>
<dt><code>http_proxy</code></p>
<dd> libcurl uses this environment variable when performing tracker announces. If set, this overrides the GNOME proxy preferences.</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.config/transmission</code></p>
<dd> The config-dir used when neither [<code>TRANSMISSION_HOME</code> ] nor [-<code>g</code> ] is specified.</dl>
<h2>AUTHORS</h2>
<p> An -nosplit <code>transmission-gtk</code> was written by An Charles Kerr , An Josh Elsasser , An Eric Petit , An Mitchell Livingston , and An Mike Gelfand .</p>
<h2>SEE ALSO</h2>
<p> transmission-create1, transmission-daemon1, transmission-edit1, transmission-gtk1, transmission-qt1, transmission-remote1, transmission-show1 </p>
<p> <a rel="nofollow" href="https://transmissionbt.com/">https://transmissionbt.com/</a> </p>
<h2>Index</h2>
