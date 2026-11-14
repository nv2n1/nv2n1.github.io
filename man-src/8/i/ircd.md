---
title: "ircd(8)"
name: "ircd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ircd/"
description: "ircd – The IRCD-Hybrid Internet Relay Chat server"
---

<p>ircd &#8211; The IRCD-Hybrid Internet Relay Chat server</p>
<h2>Synopsis</h2>
<dl>
<dt><code>ircd</code></p>
<dd>[-configfile filename] [-dlinefile filename] [-klinefile filename] [-xlinefile filename] [-logfile filename] [-pidfile filename] [-foreground] [-version]</dl>
<h2>Description</h2>
<p><i>ircd</i> is the server (daemon) program for the Internet Relay Chat Program. The <i>ircd</i> is a server in that its function is to &quot;serve&quot; the client program <i><a href="/docs/linux/man/1-irc/">irc</a>(1)</i> and other compatible programs with messages and commands. All commands and user messages are passed directly to the <i>ircd</i> for processing and relaying to other IRC servers. </p>
<p> This is <i>ircd-hybrid</i>, the highly modified (and hopefully improved) variant of the original ircd program by Jarkko Oikarinen.</p>
<h2>Options</h2>
<dl>
<dt><code>-configfile filename</code></p>
<dd>Specifies the ircd.conf file to be used for this <i>ircd</i>. The option is used to override the default ircd.conf given at compile time. By default, this is &quot;etc/ircd.conf&quot; within the prefix you installed the <i>ircd</i> in.</p>
<dt><code>-dlinefile filename</code></p>
<dd>
<dt><code>-klinefile filename</code></p>
<dd>
<dt><code>-xlinefile filename</code></p>
<dd>Specifies the files to be used for D-lines (host bans), K-lines (hostmask bans), and X-lines (gecos bans), which by default are within the etc/ directory of your installation prefix as dline.conf, kline.conf, and xline.conf.</p>
<dt><code>-logfile filename</code></p>
<dd>Specifies an alternative logfile to be used than that specified in defaults.h</p>
<dt><code>-pidfile filename</code></p>
<dd>Specifies the file used by the <i>ircd</i> to store its process ID. The option is used to override the default ircd.pid given at compile time.</p>
<dt><code>-foreground</code></p>
<dd>Makes <i>ircd</i> run in the foreground</p>
<dt><code>-version</code></p>
<dd>Makes <i>ircd</i> print its version, and exit.</dl>
<h2>Usage</h2>
<p>If you plan to connect your <i>ircd</i> server to an existing IRC network, you will need to alter your local IRC configuration file (typically named &quot;ircd.conf&quot;) so that it will accept and make connections to other <i>IRC</i> servers. This file contains the hostnames, IP addresses, and sometimes passwords for connections to other ircds around the world. </p>
<p> The example ircd.conf in the etc/ directory documents itself. Read it carefully or you may expose a risk on your network simply by having your ircd running!</p>
<h2>Booting The Server</h2>
<p>It is sufficient to type <code>ircd</code> at the command line to start ircd-hybrid into the background. If you wish to run ircd in the foreground (perhaps for debugging purposes), use the <code>-foreground</code> parameter. </p>
<p> The ircd-hybrid package in your distribution may ship with an rc-script which handles this for you. In Debian, it is <code>/etc/init.d/ircd-hybrid.</code></p>
<h2>Example</h2>
<p># ircd -configfile /usr/share/ircd/ircd.conf -logfile /var/log/ircd.log </p>
<p> Starts <code>ircd</code> with the config file /usr/share/ircd/ircd.conf and with a log file /var/log/ircd.log. It implicitly forks back to the console &#8212; to prevent this use -foreground. </p>
<p> Many of the above paths are hardcoded at compile time in the <code>include/defaults.h</code> file, so it may be convenient to edit these to suit your needs before you compile the ircd.</p>
<h2>Copyright</h2>
<p>(c) 1988,1989 University of Oulu, Computing Center, Finland, </p>
<p> (c) 1988,1989 Department of Information Processing Science, University of Oulu, Finland </p>
<p> (c) 1988-1991 Jarkko Oikarinen </p>
<p> (c) 1997-2003 The IRCD-Hybrid project. </p>
<p> For full COPYRIGHT see the LICENSE file within the IRC source package.</p>
<h2>Bugs</h2>
<p>If you find a bug and you have a core file from ircd as a result, use a debugger like <code><a href="/docs/linux/man/1-gdb/">gdb</a>(1)</code> to process the core file and send a backtrace to <code>bugs [at] ircd-hybrid.org</code>. </p>
<h2>Authors</h2>
<p>irc2.8 and earlier: Jarkko Oikarinen, currently jto [at] tolsun.oulu.fi. See doc/old/Authors for more credits. </p>
<p> ircd-hybrid-7: the IRCD-Hybrid Project, bugs [at] ircd-hybrid.org. </p>
<p> Manual page written by Jeff Trim, jtrim [at] orion.cair.du.edu, later modified by jto [at] tolsun.oulu.fi. </p>
<p> Updated by W. Campbell, wcampbel [at] botbay.net, Edward Brocklesby, ejb [at] klamath.uucp.leguin.org.uk, and highly revised by Joshua Kwan (joshk [at] triplehelix.org) for the Debian distribution.</p>
