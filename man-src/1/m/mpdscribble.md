---

title: "mpdscribble(1)"
name: "mpdscribble"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpdscribble/"
description: "mpdscribble – A Music Player Daemon (MPD) client which submits information about tracks being played to a scrobbler (e.g. last.fm)."
---

<p> mpdscribble &#8211; A Music Player Daemon (MPD) client which submits information about tracks being played to a scrobbler (e.g. last.fm).</p>
<h2>SYNOPSIS</h2>
<p> <code>mpdscribble [options] </code></p>
<h2>DESCRIPTION</h2>
<p> <code>mpdscribble</code> is a client for MPD, the Music Player Daemon. mpdscribble connects to an MPD running on the local network and works in parallel with other MPD clients on the network. </p>
<p> By default it will get the hostname and port for mpd from the MPD_HOST and MPD_PORT environment variables. mpdscribble will use localhost:6600 if those are not set. The hostname and port can also be specified in the configuration file or on the command line. </p>
<p> $ mpdscribble &#8211;host myhost &#8211;port=12345 </p>
<p> Values specified on the command line override values from the configuration file or environment variables. </p>
<p> If you want to use mpdscribble with a password-protected MPD, set the environment variable MPD_HOST to password [at] host, or specify the host in the configuration file similarly. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Display help and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display version information and exit.</dd>
<dt><code>&#8211;no-daemon</code></dt>
<dd> Don&#8217;t daemonize mpdscribble, run it in foreground.</dd>
<dt><code>&#8211;pidfile FILE</code></dt>
<dd> Write the process id to this file.</dd>
<dt><code>&#8211;daemon-user USERNAME</code></dt>
<dd> Change to this system user after daemonization.</dd>
<dt><code>&#8211;log FILE</code></dt>
<dd> Specify log file. The special value &quot;syslog&quot; makes mpdscribble use the local syslog daemon (which is the default). &quot;-&quot; means log to stderr.</dd>
<dt><code>&#8211;conf FILE</code></dt>
<dd> Read configuration options from file. /etc/mpdscribble.conf is used by default (if &#8211;sysconfdir=/etc).</dd>
<dt><code>&#8211;host [PASSWORD@]HOSTNAME</code></dt>
<dd> Specify host protected by password. To connect via Unix Domain Socket, specify an absolute path here.</dd>
<dt><code>&#8211;port PORT</code></dt>
<dd> Specify which port the MPD listens on.</dd>
<dt><code>&#8211;proxy URL</code></dt>
<dd> HTTP proxy URL.</dd>
<dt><code>&#8211;verbose LEVEL</code></dt>
<dd> Specify how verbosely mpdscribble should log. Possible values are 0 to 3, defaulting to 1.</dd></dl>
<h2>CONFIGURATION</h2>
<p> mpdscribble looks for its configuration file first at ~/.mpdscribble/mpdscribble.conf and then at /etc/mpdscribble.conf (if &#8211;sysconfdir=/etc) but this can be overridden by specifying an alternate configuration file using the command line option &#8211;conf. </p>
<p> Supported configuration options:</p>
<dl>
<dt><code>pidfile = FILE</code></dt>
<dd> Write the process id to this file.</dd>
<dt><code>log = FILE</code></dt>
<dd> The file to which mpdscribble should output debugging information. The special value &quot;syslog&quot; makes mpdscribble use the local syslog daemon (which is the default). &quot;-&quot; means log to stderr.</dd>
<dt><code>host = [PASSWORD@]HOSTNAME</code></dt>
<dd> The host running MPD, possibly protected by a password. To connect via Unix Domain Socket, specify an absolute path here.</dd>
<dt><code>port = PORT</code></dt>
<dd> The port that the MPD listens on and mpdscribble should try to connect to.</dd>
<dt><code>proxy = URL</code></dt>
<dd> HTTP proxy URL.</dd>
<dt><code>verbose = 0, 1, 2, 3</code></dt>
<dd> How verbose mpdscribble&#8217;s logging should be. Default is 1. &quot;0&quot; means log only critical errors (e.g. &quot;out of memory&quot;); &quot;1&quot; also logs non-critical errors (e.g. &quot;server unreachable&quot;); &quot;2&quot; logs informational messages (e.g. &quot;new song&quot;); &quot;3&quot; prints a lot of debugging messages.</dd></dl>
<h2>SCROBBLERS</h2>
<p> These options are followed by at least one scrobbler section (choose a unique section name like &quot;libre.fm&quot; which only appears in the log file; the name &quot;mpdscribble&quot; is reserved).</p>
<dl>
<dt><code>url = URL</code></dt>
<dd> The handshake URL of the scrobbler. Example: &quot;<a rel="nofollow" href="http://post.audioscrobbler.com/">http://post.audioscrobbler.com/</a>&quot;, &quot;<a href="http://turtle.libre.fm/">http://turtle.libre.fm/</a>&quot;</dd>
<dt><code>username = USERNAME</code></dt>
<dd> Your audioscrobbler username.</dd>
<dt><code>password = MD5SUM</code></dt>
<dd> Your Last.fm password, either cleartext or its MD5 sum.</dd>
<dt><code>journal = FILE</code></dt>
<dd> The file where mpdscribble should store its journal in case you do not have a connection to the scrobbler. This option used to be called &quot;cache&quot;. It is optional.</dd></dl>
<h2>FILES</h2>
<p> <i>/etc/mpdscribble.conf</i></p>
<dl>
<dt>
</dt><dd> The system wide configuration file.</dd></dl>
<p> <i>~/.mpdscribble/mpdscribble.conf</i></p>
<dl>
<dt>
</dt><dd> Per user configuration file.</dd></dl>
<p> <i>/var/cache/mpdscribble/mpdscribble.cache</i></p>
<dl>
<dt>
</dt><dd> The system wide Last.fm cache file.</dd></dl>
<p> <i>~/.mpdscribble/mpdscribble.cache</i></p>
<dl>
<dt>
</dt><dd> Per user Last.fm cache file.</dd></dl>
<p> <i>/var/log/mpdscribble/mpdscribble.log</i></p>
<dl>
<dt>
</dt><dd> The system wide log file.</dd></dl>
<p> <i>~/.mpdscribble/mpdscribble.log</i></p>
<dl>
<dt>
</dt><dd> Per user log file.</dd></dl>
<h2>BUGS</h2>
<p> File permissions on cache/log file may be insecure by default. </p>
<p> Please report new bugs to the MPD bug tracker: <a rel="nofollow" href="http://www.musicpd.org/mantis">http://www.musicpd.org/mantis</a> </p>
<h2>CREDITS</h2>
<p> Current maintainer: Max Kellermann &lt;max [at] duempel.org&gt;</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://max.kellermann.name/">http://max.kellermann.name/</a></dd></dl>
<p> Original author: Kuno Woudt &lt;kuno [at] frob.nl&gt;</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.audioscrobbler.com/user/warp/">http://www.audioscrobbler.com/user/warp/</a></dd></dl>
<p> Various patches: Nikki</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.audioscrobbler.com/user/cikkolata/">http://www.audioscrobbler.com/user/cikkolata/</a></dd></dl>
<p> The name mpdscribble coined by: honey in #audioscrobbler</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.audioscrobbler.com/user/honeypea/">http://www.audioscrobbler.com/user/honeypea/</a></dd></dl>
<p> Manpage written by: Trevor Caira &lt;trevor.caira [at] gmail.com&gt;</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.audioscrobbler.com/user/TrevorCaira/">http://www.audioscrobbler.com/user/TrevorCaira/</a></dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpd/">mpd</a></code>(1), <code><a href="/docs/linux/man/1-mpc/">mpc</a></code>(1) </p>
