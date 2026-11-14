---
title: "knopwatchd(8)"
name: "knopwatchd"
section: "8"
letter: "k"
url: "/docs/linux/man/8-knopwatchd/"
description: "knopwatchd – \"FwKnop Watch Daemon\" checks to make sure knopmd, knoptm and fwknop daemons are running."
---

<p><code>knopwatchd</code> &#8211; &quot;FwKnop Watch Daemon&quot; checks to make sure knopmd, knoptm and fwknop daemons are running.</p>
<h2>Synopsis</h2>
<p><code>knopwatchd [options]</code></p>
<h2>Description</h2>
<p><code>knopwatchd</code> checks on an interval of every five seconds to make sure that knopmd, knoptm and fwknopd are running on the box. If any of the three daemons have died, knopwatchd will restart the daemon and notify each email address listed in the EMAIL_ADDRESSES variable that the daemon has been restarted. <code>knopwatchd</code> uses the fwknop.conf configuration file which by default is located at /etc/fwknop/, but a different path can be specified on the command line.</p>
<h2>Options</h2>
<dl>
<dt><code>-c&nbsp;<wbr>&lt;config-file&gt;</code></p>
<dd>Specify path to config file instead of using the default configuration file /etc/fwknop/fwknop.conf.</p>
<dt><code>-D</code></p>
<dd>Dump the configuration values that <code>knopwatchd</code> derives from /etc/fwknop/fwknop.conf (or other override files) on STDERR.</p>
<dt><code>-h</code></p>
<dd>Display usage information and exit.</p>
<dt><code>-O&nbsp;<wbr>&lt;config-file&gt;</code></p>
<dd>Override config variable values that are normally read from the /etc/fwknop/fwknop.conf file with values from the specified file. Multiple override config files can be given as a comma separated list.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fwknop/">fwknop</a></code>(8), <code><a href="/docs/linux/man/8-fwknopd/">fwknopd</a></code>(8), <code><a href="/docs/linux/man/8-knopmd/">knopmd</a></code>(8),</p>
<h2>Author</h2>
<p>Michael Rash (mbr [at] cipherdyne.org)</p>
<h2>Distribution</h2>
<p><code>fwknop</code> is distributed under the GNU General Public License (GPL), and the latest version may be downloaded from <code><a rel="nofollow" href="http://www.cipherdyne.org">http://www.cipherdyne.org</a></code></p>
