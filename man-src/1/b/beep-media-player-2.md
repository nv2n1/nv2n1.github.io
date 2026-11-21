---
title: "beep-media-player-2(1)"
name: "beep-media-player-2"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beep-media-player-2/"
description: "BMP – Media Player"
---

<h2>NAME</h2>
<p> BMP &#8211; Media Player</p>
<h2>SYNOPSIS</h2>
<p> <code>beep-media-player-2 [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>BMP</i> is a media player</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display version and paths/files used by the current BMPx installation</dd>
<dt><code>-c, &#8211;configure</code></dt>
<dd> Prints the arguments passed to configure for the installed version of BMPx</dd>
<dt><code>-n, &#8211;no-network</code></dt>
<dd> Start BMPx in &quot;offline&quot; mode, that is, don&#8217;t enable network dependent sources (Last.fm, Radios), and don&#8217;t use network dependent services (Musicbrainz)</dd>
<dt><code>-u, &#8211;uris</code></dt>
<dd> Parse the command line arguments as URIs to play (this is the default anyway so this option shouldn&#8217;t be really needed; legacy reasons)</dd>
<dt><code>-f, &#8211;files</code></dt>
<dd> By default, beep-media-player-2 will expect the arguments passed to it on the commandline without options to be URIs (e.g. file:///music/file.ogg, or <a rel="nofollow" href="http://somehost.com/stream.ogg">http://somehost.com/stream.ogg</a>); using this switch will make it treat the arguments as filenames of locally (on this host) acecssible files instead</dd>
<dt><code>&#8211;ppaus</code></dt>
<dd> Pause/Resume Playback</dd>
<dt><code>&#8211;ppnext</code></dt>
<dd> Skip to the next Track/Item</dd>
<dt><code>&#8211;pprev</code></dt>
<dd> Skip to the previous Track/Item</dd></dl>
<h2>FILES/PATHS</h2>
<dl>
<dt>~/.config/bmpx/logs/</dt>
<dd> Log directory, to which all log files are written to unless &#8211;no-log is used.</dd>
<dt>~/.config/bmpx/config.xml</dt>
<dd> Configuration file (please run beep-media-player-2 &#8211;version for a full list of paths and files used by BMP)</dd>
<dt>~/.config/bmpx/feedlist.opml</dt>
<dd> Podcast feedlist in OPML format (adding a feed there while BMP isn&#8217;t running will make it load the feed when started up the next time)</dd>
<dt>~/.local/share/bmpx/library-N-N-N.mlib</dt>
<dd> SQlite library file</dd></dl>
<h2>OTHER INFO</h2>
<p> The BMPx web site is <a rel="nofollow" href="http://bmpx.beep-media-player.org">http://bmpx.beep-media-player.org</a> </p>
