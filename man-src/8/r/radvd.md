---
title: "radvd(8)"
name: "radvd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radvd/"
description: "radvd – router advertisement daemon for IPv6"
---

<p>radvd &#8211; router advertisement daemon for IPv6</p>
<h2>Synopsis</h2>
<p><code>radvd</code> <code>[ -hsvc ]</code> <code>[ -d </code><i>debuglevel</i><code> ]</code> <code>[ -C </code><i>configfile</i><code> ]</code> <code>[ -p </code><i>pidfile</i><code> ]</code> <code>[ -m </code><i>logmethod</i><code> ]</code> <code>[ -l </code><i>logfile</i><code> ]</code> <code>[ -f </code><i>facility</i><code> ]</code> <code>[ -t </code><i>chrootdir</i><code> ]</code> <code>[ -u </code><i>username</i><code> ]</code> </p>
<h2>Description</h2>
<p><code>radvd</code> is the router advertisement daemon for IPv6. It listens to router solicitations and sends router advertisements as described in &quot;Neighbor Discovery for IP Version 6 (IPv6)&quot; (RFC 4861). With these advertisements hosts can automatically configure their addresses and some other parameters. They also can choose a default router based on these advertisements. Note that if debugging is not enabled, <code>radvd</code> will not start if IPv6 forwarding is disabled. IPv6 forwarding can be controlled via <a href="/docs/linux/man/8-sysctl/">sysctl</a>(8), <code>net.ipv6.conf.all.forwarding</code> on Linux or <code>net.inet6.ip6.forwarding</code> on BSD. Similarly, the configuration file must not be writable by others, and if non-root operation is requested, not even by self/own group. </p>
<h2>Options</h2>
<p>For every one character option there is also a long option, which is listed right next to the &quot;short&quot; option name: </p>
<dl>
<dt><code>-v</code>,<code> &#8211;version</code></p>
<dd>Displays the version of <i>radvd</i> and then aborts.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd>Displays a short usage description and then aborts.</p>
<dt><code>-s</code>,<code> &#8211;singleprocess</code></p>
<dd>On Linux if <i>username</i> is specified, privilege separation is enabled and there will be two processes. This option disables privilege separation, and as a result, the non-privileged radvd process does not have permissions to change interface configuration.</p>
<dt><code>-n</code>,<code> &#8211;nodaemon</code></p>
<dd>Prevent the daemonizing.</p>
<dt><code>-c</code>,<code> &#8211;configtest</code></p>
<dd>Test configuration and do startup tests and then exit.</p>
<dt><code>-d </code>debuglevel,<code> &#8211;debug </code>debuglevel</p>
<dd>With this option you turn on debugging information. The debugging level is an integer in the range from 1 to 5, from quiet to very verbose. A debugging level of 0 completely turns off debugging. If a debugging level greater than 0 is used, <i>radvd</i> doesn&#8217;t background itself on start. The default debugging level is 0.</p>
<dt><code>-C </code>configfile,<code> &#8211;config </code>configfile</p>
<dd>Specifies an alternate config file. Normally the compiled in default <i>/etc/radvd.conf</i> is used.</p>
<dt><code>-p </code>pidfile,<code> &#8211;pidfile </code>pidfile</p>
<dd>Specifies an alternate pidfile. Normally the compiled in default <i>/var/run/radvd/radvd.pid</i> is used.</p>
<dt><code>-m </code>method,<code> &#8211;logmethod </code>method</p>
<dd>Specifies the logging method to use. Possibly values are:</p>
<dl>
<dd>
<dl>
<dt><code>none</code></p>
<dd>Completely disables any logging.</p>
<dt><code>logfile</code></p>
<dd>Logs to the logfile which is specified by the <i>-l</i> option. If no logfile is specified on the command line, then a compiled in default is used (see next option).</p>
<dt><code>stderr</code></p>
<dd>Logs to standard error.</p>
<dt><code>stderr_syslog</code></p>
<dd>Logs only the high messages (of at least LOG_ERR priority) to standard error, and everything to syslog (default method).</p>
<dt><code>syslog</code></p>
<dd>Logs to syslog.</dl>
</dl>
</dl>
<dl>
<dt><code>-l </code>logfile,<code> &#8211;logfile </code>logfile</p>
<dd>Specifies the logfile to use when using the logging method <i>logfile</i>. The default logfile is <i>/var/log/radvd.log</i>.</p>
<dt><code>-f </code>facility,<code> &#8211;facility </code>facility</p>
<dd>Specifies the facility (as an integer) when using syslog logging. Default is LOG_DAEMON.</p>
<dt><code>-t </code>chrootdir,<code> &#8211;chrootdir </code>chrootdir</p>
<dd>If specified, switches to <i>chrootdir</i> before doing anything else. This directory and its subdirectories must have been populated first. For security reasons, <i>-u </i> must always be used when using <i>chrootdir</i>. </p>
<p> Note that on Linux <i>radvd</i> requires access to the <i>/proc</i> filesystem, so it is more challenging to set up the chroot environment.</p>
<dt><code>-u </code>username,<code> &#8211;username </code>username</p>
<dd>If specified, drops root privileges and changes user ID to <i>username</i> and group ID to the primary group of <i>username</i>. This is recommended for security reasons. You might also need to use <i>-p</i> to point to a file in a <i>username</i> -writable directory (e.g. /var/run/radvd/radvd.pid).</dl>
<h2>Files</h2>
<pre>/usr/sbin/radvd
/etc/radvd.conf
/var/run/radvd/radvd.pid
/var/log/radvd.log</pre>
<h2>Bugs</h2>
<p>There certainly are some bugs. If you find them or have other suggestions please contact Reuben Hawkins &lt;reubenhwk [at] gmail.com&gt;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-radvd-conf/">radvd.conf</a></code>(5), <code><a href="/docs/linux/man/8-radvdump/">radvdump</a></code>(8)</p>
<h2>Authors</h2>
<pre>Pedro Roque &lt;roque [at] di.fc.ul.pt&gt; - wrote first version for Linux
Lars Fenneberg &lt;lf [at] elemental.net&gt; - previous maintainer
Nathan Lutchansky &lt;lutchann [at] litech.org&gt; - previous maintainer
Reuben Hawkins &lt;reubenhwk [at] gmail.com&gt; - current maintainer
Craig Metz &lt;cmetz [at] inner.net&gt; - port to NRL's IPv6 code for BSD4.4
Marko Myllynen &lt;myllynen [at] lut.fi&gt; - RFC 2461 update, Mobile IPv6 support
Jim Paris &lt;jim [at] jtan.com&gt; - Privilege separation support
Reuben Hawkins &lt;reubenhwk [at] gmail.com&gt; - Many fixes and cleanups
Pierre Ossman &lt;pierre [at] ossman.eu&gt; - RFC6106 (DNSSL) support</pre>
