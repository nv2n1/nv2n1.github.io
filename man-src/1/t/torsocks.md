---
title: "torsocks(1)"
name: "torsocks"
section: "1"
letter: "t"
url: "/docs/linux/man/1-torsocks/"
description: "torsocks — Shell wrapper to simplify the use of the"
---

<h2 class="name">NAME</h2>
<p> torsocks &#8212; Shell wrapper to simplify the use of the </p>
<p><a href="/docs/linux/man/8-torsocks/">torsocks</a>(8) library to transparently torify an application. </p>
<h2>SYNOPSIS</h2>
<p> torsocks [OPTIONS] [COMMAND [ARG &#8230;]] </p>
<h2>DESCRIPTION</h2>
<p> <code>torsocks</code> is a wrapper between the torsocks library and the application in order to make every Internet communication go through the Tor network. </p>
<p> By default, torsocks will assume that it should connect to the Tor SOCKS proxy running at 127.0.0.1 on port 9050 being the defaults of the Tor daemon. </p>
<p> In order to use a configuration file, torsocks tries to read the <code>/etc/tor/torsocks.conf</code> file or look for the environment variable TORSOCKS_CONF_FILE with the location of the file. If that file cannot be read, torsocks will use sensible defaults for most Tor installations. </p>
<p> For further information on configuration, see <code><a href="/docs/linux/man/5-torsocks-conf/">torsocks.conf</a>(5).</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of possible options and commands.</p>
<dt><code>&#8211;shell</code></p>
<dd> Create a new shell with LD_PRELOAD including <code><a href="/docs/linux/man/8-torsocks/">torsocks</a>(8)</code>.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version.</p>
<dt><code>-u, &#8211;user</code></p>
<dd> Set username for the SOCKS5 authentication. Use for circuit isolation in Tor. Note that you MUST have a password set either by the command line, environment variable or configuration file (<a href="/docs/linux/man/5-torsocks-conf/">torsocks.conf</a>(5).</p>
<dt><code>-p, &#8211;pass</code></p>
<dd> Set password for the SOCKS5 authentication. Use for circuit isolation in Tor. Note that you MUST have a username set either by the command line, environment variable or configuration file (<a href="/docs/linux/man/5-torsocks-conf/">torsocks.conf</a>(5)).</p>
<dt><code>-i, &#8211;isolate</code></p>
<dd> Automatic tor isolation. Set the username and password for the SOCKS5 authentication method to a PID/current time based value automatically. Username and Password MUST NOT be set.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Activate the debug mode. Output will be written on stderr.</p>
<dt><code>on | off</code></p>
<dd> This option adds or removes <code><a href="/docs/linux/man/8-torsocks/">torsocks</a>(8)</code> from the LD_PRELOAD environment variable for the current shell. If you want to use this option, you HAVE to source torsocks from your shell. </p>
<pre>
Add the torsocks library to LD_PRELOAD
$ . torsocks on
<br>
Remove the torsocks library from LD_PRELOAD
$ . torsocks off
</pre>
<dt><code>show | sh</code></p>
<dd> Show the current value of the LD_PRELOAD environment variable. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Please see <code><a href="/docs/linux/man/8-torsocks/">torsocks</a>(8)</code> for more detail on possible environment variables. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-torsocks/">torsocks</a>(8),</code> <code><a href="/docs/linux/man/5-torsocks-conf/">torsocks.conf</a>(5)</code> </p>
<h2>CREDITS</h2>
<p> torsocks is distributed under the GNU General Public License version 2. </p>
<p> A Web site is available at <a rel="nofollow" href="https://www.torproject.org">https://www.torproject.org</a> for more information. </p>
<p> You can also find the source code at <a rel="nofollow" href="https://git.torproject.org.">https://git.torproject.org.</a> </p>
<p> Mailing list for help is &lt;tor-talk [at] lists.torproject.org&gt; and for development use &lt;tor-dev [at] lists.torproject.org&gt;. You can find the project also on IRC server irc.oftc.net (OFTC) in #tor and #tor-dev. </p>
<h2>AUTHOR</h2>
<p> torsocks was originally written by Robert Hogan and has been rewritten by David Goulet &lt;dgoulet [at] torproject.org&gt; in 2013. </p>
<h2>Index</h2>
