---
title: "mpd(1)"
name: "mpd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpd/"
description: "MPD – A daemon for playing music"
---

<h2>NAME</h2>
<p> MPD &#8211; A daemon for playing music</p>
<h2>SYNOPSIS</h2>
<p> <code>mpd</code> [<i>options</i>] [<i>CONF_FILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> MPD is a daemon for playing music. Music is played through the configured audio output(s) (which are generally local, but can be remote). The daemon stores info about all available music, and this info can be easily searched and retrieved. Player control, info retrieval, and playlist management can all be managed remotely. </p>
<p> MPD searches for a config file in <code>$XDG_CONFIG_HOME/mpd/mpd.conf</code> then <code>~/.mpdconf</code> then <code>/etc/mpd.conf</code> or uses CONF_FILE. </p>
<p> Read more about MPD at &lt;<code><a rel="nofollow" href="http://www.musicpd.org/">http://www.musicpd.org/</a></code>&gt;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Output a brief help message.</p>
<dt><code>&#8211;kill</code></p>
<dd> Kill the currently running mpd session. The pid_file parameter must be specified in the config file for this to work.</p>
<dt><code>&#8211;no-daemon</code></p>
<dd> Don&#8217;t detach from console.</p>
<dt><code>&#8211;stderr</code></p>
<dd> Print messages stderr.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Verbose logging.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information.</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.mpdconf</code></p>
<dd> User configuration file.</p>
<dt><code>/etc/mpd.conf</code></p>
<dd> Global configuration file.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-mpd-conf/">mpd.conf</a>(5), <a href="/docs/linux/man/1-mpc/">mpc</a>(1)</p>
<h2>BUGS</h2>
<p> If you find a bug, please report it at<br />
 &lt;<code><a rel="nofollow" href="http://bugs.musicpd.org/bug_report_page.php">http://bugs.musicpd.org/bug_report_page.php</a></code>&gt;.</p>
<h2>AUTHORS</h2>
<p> Max Kellermann &lt;max [at] duempel.org&gt; </p>
<p> Special thanks to all the people that provided feedback and patches. </p>
<h2>Index</h2>
