---
title: "ngircd(8)"
name: "ngircd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ngircd/"
description: "ngIRCd – the \"next generation\" IRC daemon"
---

<p>ngIRCd &#8211; the &quot;next generation&quot; IRC daemon</p>
<h2>Synopsis</h2>
<p><code>ngircd</code> [ <i>Options</i> ]</p>
<h2>Description</h2>
<p><code>ngIRCd</code> is a free, portable and lightweight Internet Relay Chat server for small or private networks, developed under the GNU General Public License (GPL). It is easy to configure, can cope with dynamic IP addresses, and supports IPv6, SSL-protected connections as well as PAM for authentication. It is written from scratch and not based on the original IRCd. </p>
<p> The name ngIRCd means <i>next generation IRC daemon,</i> which is a little bit exaggerated: <i>lightweight Internet Relay Chat server</i> most probably would have been a better name :-) </p>
<p> Currently supported platforms include AIX, A/UX, FreeBSD, HP-UX, Hurd, IRIX, Linux, Mac OS X, Minix, NetBSD, OpenBSD, Solaris, and Windows with Cygwin. As ngIRCd relies on UNIX standards and uses GNU automake and GNU autoconf there are good chances that it also supports other UNIX-based operating systems as well. </p>
<p> By default ngIRCd logs diagnostic and informational messages using the syslog mechanism, or writes directly to the console when running in the foreground (see below).</p>
<h2>Options</h2>
<p>The default behavior of <code>ngircd</code> is to read its standard configuration file (see below), to detach from the controlling terminal and to wait for clients. </p>
<p> You can use these options to modify this default:</p>
<dl>
<dt><code>-f</code> <i>file</i>, <code>&#8211;config</code> <i>file</i></dt>
<dd>Use <i>file</i> as configuration file.</dd>
<dt><code>-n</code>, <code>&#8211;nodaemon</code></dt>
<dd>Don&#8217;t fork a child and don&#8217;t detach from controlling terminal. All log messages go to the console and you can use CTRL-C to terminate the server.</dd>
<dt><code>-p</code>, <code>&#8211;passive</code></dt>
<dd>Disable automatic connections to other servers. You can use the IRC command CONNECT later on as IRC Operator to link this ngIRCd to other servers.</dd>
<dt><code>-t</code>, <code>&#8211;configtest</code></dt>
<dd>Read, validate and display the configuration; then exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Output version information and exit.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Display a brief help text and exit.</dd></dl>
<h2>Files</h2>
<p><i>/etc/ngircd.conf</i></p>
<dl>
<dd>The system wide default configuration file.</dd></dl>
<p> <i>/etc/ngircd.motd</i></p>
<dl>
<dd>Default &quot;message of the day&quot; (MOTD).</dd></dl>
<h2>Signals</h2>
<p>The daemon understands the following signals:</p>
<dl>
<dt><code>TERM</code></dt>
<dd>Shut down all connections and terminate the daemon.</dd>
<dt><code>HUP</code></dt>
<dd>Shut down all listening sockets, re-read the configuration file and re-initialize the daemon.</dd></dl>
<h2>Hints</h2>
<p>It&#8217;s wise to use &quot;ngircd &#8211;configtest&quot; to validate the configuration file after changing it.</p>
<h2>Debugging</h2>
<p>When ngIRCd is compiled with debug code, that is, its source code has been ./configure&#8217;d with &quot;&#8211;enable-debug&quot; and/or &quot;&#8211;enable-sniffer&quot; (witch enables debug mode automatically as well), you can use two more command line options and two more signals to debug problems with the daemon itself or IRC clients: </p>
<p> <code>Options:</code></p>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd>Enable debug mode and log extra messages.</dd>
<dt><code>-s</code>, <code>&#8211;sniffer</code></dt>
<dd>Enable IRC protocol sniffer, which logs all sent and received IRC commands to the console/syslog. This option requires that ngIRCd has been ./configure&#8217;d with &quot;&#8211;enable-sniffer&quot; and enables debug mode automatically, too.</dd></dl>
<p> <code>Signals:</code></p>
<dl>
<dt><code>USR1</code></dt>
<dd>Toggle debug mode on and off during runtime.</dd>
<dt><code>USR2</code></dt>
<dd>Dump internal server state to the console/syslog when debug mode is on (use command line option &#8211;debug or signal USR1).</dd></dl>
<h2>Authors</h2>
<p>Alexander Barton, &lt;alex [at] barton.de&gt;<br/>
 Florian Westphal, &lt;fw [at] strlen.de&gt; </p>
<p> Homepage: <a rel="nofollow" href="http://ngircd.barton.de/">http://ngircd.barton.de/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ngircd-conf/">ngircd.conf</a></code>(5), <code><a href="/docs/linux/man/8-ircd/">ircd</a></code>(8) </p>
