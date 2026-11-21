---

title: "mpd(1)"
name: "mpd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpd/"
description: "MPD – A daemon for playing music"
---

<p> MPD &#8211; A daemon for playing music</p>
<h2>SYNOPSIS</h2>
<p> <code>mpd</code> [<i>options</i>] [<i>CONF_FILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> MPD is a daemon for playing music. Music is played through the configured audio output(s) (which are generally local, but can be remote). The daemon stores info about all available music, and this info can be easily searched and retrieved. Player control, info retrieval, and playlist management can all be managed remotely. </p>
<p> MPD searches for a config file in <code>$XDG_CONFIG_HOME/mpd/mpd.conf</code> then <code>~/.mpdconf</code> then <code>/etc/mpd.conf</code> or uses CONF_FILE. </p>
<p> Read more about MPD at &lt;<code><a rel="nofollow" href="http://www.musicpd.org/">http://www.musicpd.org/</a></code>&gt;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Output a brief help message.</dd>
<dt><code>&#8211;kill</code></dt>
<dd> Kill the currently running mpd session. The pid_file parameter must be specified in the config file for this to work.</dd>
<dt><code>&#8211;no-daemon</code></dt>
<dd> Don&#8217;t detach from console.</dd>
<dt><code>&#8211;stderr</code></dt>
<dd> Print messages stderr.</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Verbose logging.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information.</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.mpdconf</code></dt>
<dd> User configuration file.</dd>
<dt><code>/etc/mpd.conf</code></dt>
<dd> Global configuration file.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-mpd-conf/">mpd.conf</a>(5), <a href="/docs/linux/man/1-mpc/">mpc</a>(1)</p>
<h2>BUGS</h2>
<p> If you find a bug, please report it at<br />
 &lt;<code><a rel="nofollow" href="http://bugs.musicpd.org/bug_report_page.php">http://bugs.musicpd.org/bug_report_page.php</a></code>&gt;.</p>
<h2>AUTHORS</h2>
<p> Max Kellermann &lt;max [at] duempel.org&gt; </p>
<p> Special thanks to all the people that provided feedback and patches. </p>
