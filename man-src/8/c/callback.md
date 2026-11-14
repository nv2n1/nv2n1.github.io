---
title: "callback(8)"
name: "callback"
section: "8"
letter: "c"
url: "/docs/linux/man/8-callback/"
description: "callback – call a user back, presenting a login prompt"
---

<p>callback &#8211; call a user back, presenting a login prompt</p>
<h2>Synopsis</h2>
<p><code>callback</code> [<code>-x</code>&lt;debug<code>level&gt;</code>] [<code>-V</code>] [<code>-l</code>&lt;modem<code>lines&gt;</code>] [<code>-m</code>&lt;initstring&gt;<code>]</code> [<code>-s</code>&lt;speed&gt;<code>]</code> [<code>-d</code>] [<code>-S</code>] [<i>phone-number</i>]</p>
<h2>Description</h2>
<p>Call the given phone number (if none is given on the command line, ask user for one), and if a CONNECT is established, hand over control to <a href="/docs/linux/man/8-mgetty/">mgetty</a>(8) to present user with a login name prompt. <i>callback</i> is used for various purposes: * security: make sure your users are who they pretend to be by calling a well-known phone number. * cost savings: make your company call you back. <i>callback</i> can be called directly from the command line (but you must be &quot;root&quot; to do this, otherwise callback can&#8217;t signal mgetty), or from mgetty&#8217;s &quot;login.config&quot;. See the login.config file shipped with mgetty for an example. </p>
<h2>Options</h2>
<dl>
<dt>
<dt><code>-x &lt;debug level&gt;</code></p>
<dd>
<dd>Use the given level of verbosity for logging &#8211; 0 means no logging, 5 is really noisy.</p>
<dt><code>-V</code></p>
<dd>Print version number and quit.</p>
<dt><code>-d</code></p>
<dd>Do not go into the background. This is helpful for debugging.</p>
<dt><code>-l &lt;modem lines&gt;</code></p>
<dd>Use the given modem lines. Multiple lines can be separated by &quot;:&quot;, as with <a href="/docs/linux/man/8-sendfax/">sendfax</a>(8). Example: callback -l tty1a:tty2a</p>
<dt><code>-m &lt;init sequence&gt;</code></p>
<dd>Set the modem initialization sequence (as usual: expect send expect &#8230;). This can do nearly everything, as long as it leaves the modem command responses on (that is, no ATQ1 here!) and switches the modem to data mode (AT+FCLASS=0) if it is used in data/fax mode.</p>
<dt><code>-s &lt;speed&gt;</code></p>
<dd>This is the bit rate that should be used for the machine-modem connection. Usually you&#8217;ll set this via the &quot;speed &lt;nnnn&gt;&quot; option in &quot;callback.config&quot;.</p>
<dt><code>-S</code></p>
<dd>Use the line where callback is started from for dialing out. Callback can make use of multiple modem lines, and with this options, you can force it to use just one modem, the one where a call comes in. </p>
</dl>
<h2>Config File</h2>
<p><i>callback</i> will read all its configuration at run-time from a file, usually called /etc/mgetty+sendfax/callback.config. See the documentation in the mgetty.info manual for details.</p>
<h2>Diagnostics</h2>
<p>In most cases, <i>callback</i> can&#8217;t print any error messages to the console, because it must detach itself immediately from the terminal, in case someone wants to be called back on the modem line he called in. So, nothing to print messages to&#8230; </p>
<p> Because of this, all callback errors are logged to a protocol file (the extent of the data written is controlled by the &quot;-x&quot; option), especially including the reason why a call was not made, or what exactly failed. </p>
<p> Just two messages are printed on stdout, and those are self-explaining, a call from a non-root user, and an invalid option.</p>
<h2>Internals</h2>
<p>How does it work? </p>
<p> This is a bit tricky, because of the way <a href="/docs/linux/man/8-init/">init</a>(8) handles the <a href="/docs/linux/man/5-utmp/">utmp</a>(5) file. You can&#8217;t just have any program ask the user for a login name, and then start a &quot;login shell&quot;, it won&#8217;t work (this is for the same reason <i><a href="/docs/linux/man/8-mgetty/">mgetty</a>(8)</i> has to be started from /etc/inittab). </p>
<p> So, mgetty has to do the &quot;asking for login name&quot;. But I do not want to have all that dialout code in mgetty, bloating it even more. </p>
<p> The way it works is this: <i>callback</i> dials out on a modem device. It will only take a modem device that has a mgetty watching over it (!). When the connection is established (CONNECT), <i>callback</i> will send a signal SIGUSR1 to mgetty, which, in turn, will send the same signal back to signal &quot;I got your signal&quot;. <i>callback</i> then exits, and <i>mgetty</i> takes over the existing connection, prompts the user for a login name, and forks off /bin/login. </p>
<p> Conclusion: this will not work with mgetty versions before February 04, 1996 (no support for this signalling), and if it doesn&#8217;t work for you, please send me <code>BOTH</code> the mgetty and the callback log file, otherwise it&#8217;s very hard to find the bugs.</p>
<h2>Bugs</h2>
<p><i>callback</i> is &quot;alpha&quot; code, not very stable right now. <i>callback</i> is fairly dumb concerning retries. <i>callback</i> must be run as root. Most of the documentation consists of &quot;reading the source&quot;. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-mgetty/">mgetty</a>(8), <a href="/docs/linux/man/1-ct/">ct</a>(1)</p>
<h2>Author</h2>
<p><i>callback</i> is Copyright (C) 1993-1996 by Gert Doering, &lt;gert [at] greenie.muc.de&gt;.</p>
