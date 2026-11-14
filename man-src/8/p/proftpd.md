---
title: "proftpd(8)"
name: "proftpd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-proftpd/"
description: "proftpd – Professional configurable, secure file transfer protocol server"
---

<p>proftpd &#8211; Professional configurable, secure file transfer protocol server</p>
<h2>Synopsis</h2>
<p><code>proftpd</code> [ <code>-hlntv</code> ] [ <code>-c</code><i> config-file</i> ] [ <code>-d</code><i> debuglevel</i> ] [ <code>-p</code><i> 0|1</i> ]</p>
<h2>Description</h2>
<p><code>proftpd</code> is the Professional File Transfer Protocol (FTP) server daemon. The server may be invoked by the Internet &quot;super-server&quot; <a href="/docs/linux/man/8-inetd/">inetd</a>(8) each time a connection to the FTP service is made, or alternatively it can be run as a standalone daemon. </p>
<p> Each successful and failed <a href="/docs/linux/man/1-ftp/">ftp</a>(1) session is logged using syslog with a facility of LOG_FTP. Note: LOG_FTP messages are not displayed by <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8) by default, and may have to be enabled in <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8)&#8217;s configuration file. </p>
<p> When <code>proftpd</code> is run in standalone mode and it receives a SIGHUP then it will reread its configuration file. When run in standalone mode without the <code>-n</code> option, the main <code>proftpd</code> daemon writes its process ID to <code>/run/proftpd/proftpd.pid</code> to make it easy to know which process to SIGHUP.</p>
<h2>Options</h2>
<dl>
<dt><code>-h,&#8211;help</code></p>
<dd>Display a short usage description, including all available options.</p>
<dt><code>-n,&#8211;nodaemon</code></p>
<dd>Runs the proftpd process in standalone mode (must be configured as such in the configuration file), but does not background the process or disassociate it from the controlling tty. Additionally, all output (log or debug messages) are sent to stderr, rather than the syslog mechanism. Most often used with the <code>-d option</code> for debugging.</p>
<dt><code>-q,&#8211;quiet</code></p>
<dd>Quiet mode; don&#8217;t send logging information to standard error when running with the <code>-n option</code>.</p>
<dt><code>-v,&#8211;version</code></p>
<dd>Displays the version number of ProFTPD to stdout.</p>
<dt><code>-D,&#8211;define</code><i> parameter</i></p>
<dd>Sets a configuration <i>parameter</i> which can be used &lt;IfDefine&gt;&#8230;&lt;/IfDefine&gt; sections in the configuration files to conditionally skip or process commands.</p>
<dt><code>-d,&#8211;debug</code><i> debuglevel</i></p>
<dd>Sets proftpd&#8217;s internal debug level (normally 0). The <i>debuglevel</i> should be an integer value from 0 to 10, with higher numbers producing more debug output. Normally, debug messages are sent to <code>syslog</code> using the <code>DEBUG</code> facility, however if the <code>-n option</code> is used, all such output is sent to stderr.</p>
<dt><code>-c,&#8211;config</code><i> config-file</i></p>
<dd>Specifies an alternate <i>config-file</i> to be parsed at startup, rather than the default configuration file. The default configuration file is <code>/etc/proftpd.conf</code> </p>
<dt><code>-N,&#8211;nocollision</code></p>
<dd>Disables address/port collision checking.</p>
<dt><code>-V,&#8211;settings</code></p>
<dd>Displays various compile-time settings and exits.</p>
<dt><code>-S,&#8211;serveraddr</code></p>
<dd>Specifies an IP address for the host machine, avoiding an DNS lookup of the hostname</p>
<dt><code>-t,&#8211;configtest</code></p>
<dd>Read the configuration file, report any syntax errors, and exit.</p>
<dt><code>-p,&#8211;persistent</code><i> 0|1</i></p>
<dd>Disables (0) or enables (1) the default persistent password support, which is determined at configure time for each platform. This option <code>only</code> affects the default support, it can still be overridden at run-time with the <code>PersistentPasswd</code> directive.</p>
<dt><code>-l,&#8211;list</code></p>
<dd>Lists all modules compiled into proftpd.</p>
<dt><code>-4,&#8211;ipv4</code></p>
<dd>Support IPv4 functionality <code>only</code>, regardless of whether the <code>&#8211;enable-ipv6</code> configure option was used.</p>
<dt><code>-6,&#8211;ipv6</code></p>
<dd>Support IPv6 connections and lookup of IPv6 addresses for server DNS names. This is enabled by default, if the <code>&#8211;enable-ipv6</code> configure option is used.</dl>
<h2>Files</h2>
<p><code>/usr/sbin/proftpd</code><br />
 <code>/etc/proftpd.conf</code><br />
 <code>/usr/bin/ftpwho</code><br />
 <code>/usr/bin/ftpcount</code><br />
 <code>/usr/bin/ftptop</code><br />
 <code>/usr/sbin/ftpshut</code><br />
 <code>/etc/ftpusers</code><br />
 <code>/var/log/xferlog</code><br />
 <code>/run/proftpd/proftpd.pid</code><br />
 <code>/run/proftpd/proftpd.scoreboard</code></p>
<h2>Authors</h2>
<p>ProFTPD is written and maintained by a number of people, full credits can be found on <code><a rel="nofollow" href="http://www.proftpd.org/credits.html">http://www.proftpd.org/credits.html</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-proftpd-conf/">proftpd.conf</a>(5),</code><a href="/docs/linux/man/8-inetd/">inetd</a>(8),<code><a href="/docs/linux/man/1-ftp/">ftp</a>(1),</code><a href="/docs/linux/man/1-ftpwho/">ftpwho</a>(1),<code><a href="/docs/linux/man/1-ftpcount/">ftpcount</a>(1),</code><a href="/docs/linux/man/8-ftpshut/">ftpshut</a>(8) Full documentation on ProFTPD, including configuration and FAQs, is available at <code><a rel="nofollow" href="http://www.proftpd.org/">http://www.proftpd.org/</a></code> For help/support, try the ProFTPD mailing lists, detailed on <code><a rel="nofollow" href="http://www.proftpd.org/lists.html">http://www.proftpd.org/lists.html</a></code> Report bugs at <code><a rel="nofollow" href="http://bugs.proftpd.org/">http://bugs.proftpd.org/</a></code> </p>
