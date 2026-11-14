---
title: "avahi-daemon(8)"
name: "avahi-daemon"
section: "8"
letter: "a"
url: "/docs/linux/man/8-avahi-daemon/"
description: "avahi-daemon – The Avahi mDNS/DNS-SD daemon"
---

<p>avahi-daemon &#8211; The Avahi mDNS/DNS-SD daemon</p>
<h2>Synopsis</h2>
<p><code>avahi-daemon [</code><i>options</i><code>] </p>
<p> avahi-daemon &#8211;kill </p>
<p> avahi-daemon &#8211;reload </p>
<p> avahi-daemon &#8211;check </code></p>
<h2>Description</h2>
<p>The Avahi mDNS/DNS-SD daemon implements Apple&#8217;s Zeroconf architecture (also known as &quot;Rendezvous&quot; or &quot;Bonjour&quot;). The daemon registers local IP addresses and static services using mDNS/DNS-SD and provides two IPC APIs for local programs to make use of the mDNS record cache the avahi-daemon maintains. First there is the so called &quot;simple protocol&quot; which is used exclusively by avahi-dnsconfd (a daemon which configures unicast DNS servers using server info published via mDNS) and nss-mdns (a libc NSS plugin, providing name resolution via mDNS). Finally there is the D-Bus interface which provides a rich object oriented interface to D-Bus enabled applications. </p>
<p> Upon startup avahi-daemon interprets its configuration file <i>/etc/avahi/avahi-daemon.conf</i> and reads XML fragments from <i>/etc/avahi/services/*.service</i> which may define static DNS-SD services. If you enable <code>publish-resolv-conf-dns-servers</code> in <i>avahi-daemon.conf</i> the file <i>/etc/resolv.conf</i> will be read, too.</p>
<h2>Options</h2>
<dl>
<dt><code>-f | &#8211;file=</code> <i>FILE</i></p>
<dd>Specify the configuration file to read. (default: /etc/avahi/avahi-daemon.conf)</p>
<dt><code>-D | &#8211;daemonize</code></p>
<dd>Daemonize after startup. Implies <code>&#8211;syslog</code>.</p>
<dt><code>-s | &#8211;syslog</code></p>
<dd>Log to syslog instead of STDERR. Implied by <code>&#8211;daemonize</code>.</p>
<dt><code>&#8211;debug</code></p>
<dd>Increase verbosity to debug level.</p>
<dt><code>&#8211;no-rlimits</code></p>
<dd>Don&#8217;t enforce resource limits as specified in the configuration file. (See <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a>(2)</code> for more information)</p>
<dt><code>&#8211;no-drop-root</code></p>
<dd>Don&#8217;t drop root privileges after startup and don&#8217;t require daemon to be started as root. We recommend not to use this option.</p>
<dt><code>&#8211;no-chroot</code></p>
<dd>Don&#8217;t <code><a href="/docs/linux/man/2-chroot/">chroot</a>(2)</code> the daemon. This option is only available when compiled with chroot() support.</p>
<dt><code>&#8211;no-proc-title</code></p>
<dd>Don&#8217;t change the process name while running. Unless this option is specified avahi-daemon will reflect its current state and the selected host name in the process title.</p>
<dt><code>-k | &#8211;kill</code></p>
<dd>Kill an already running avahi-daemon. (equivalent to sending a SIGTERM)</p>
<dt><code>-r | &#8211;reload</code></p>
<dd>Tell an already running avahi-daemon to reread <i>/etc/resolv.conf</i> (in case you enabled <code>publish-resolv-conf-dns-servers</code> in <i>avahi-daemon.conf</i>) the files from <i>/etc/avahi/services/</i>. Please note that this will not reload the <i>/etc/avahi/avahi-daemon.conf</i>. (equivalent to sending a SIGHUP)</p>
<dt><code>-c | &#8211;check</code></p>
<dd>Return 0 as return code when avahi-daemon is already running.</p>
<dt><code>-h | &#8211;help</code></p>
<dd>Show help</p>
<dt><code>-v | &#8211;version</code></p>
<dd>Show version information</dl>
<h2>Files</h2>
<p><i>/etc/avahi/avahi-daemon.conf</i>: the default configuration file for avahi-daemon, <code><a href="/docs/linux/man/5-avahi-daemon-conf/">avahi-daemon.conf</a>(5)</code> for more information. </p>
<p> <i>/etc/avahi/hosts</i>: additional static hostname mappings to publish in mDNS, see <code><a href="/docs/linux/man/5-avahi-hosts/">avahi.hosts</a>(5)</code> for more information. </p>
<p> <i>/etc/avahi/services/*.service</i>: static service definitions, see <code><a href="/docs/linux/man/5-avahi-service/">avahi.service</a>(5)</code> for more information.</p>
<h2>Signals</h2>
<p><i>SIGINT, SIGTERM</i>: avahi-daemon will shutdown. (Same as <code>&#8211;kill</code>). </p>
<p> <i>SIGHUP</i>: avahi-daemon will reload unicast DNS server data from <i>/etc/resolv.conf</i> and static service definitions from <i>/etc/avahi/services/</i>. (Same as <code>&#8211;reload</code>) </p>
<p> <i>SIGUSR1</i>: avahi-daemon will dump local and remote cached resource record data to syslog.</p>
<h2>Authors</h2>
<p>The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-avahi-daemon-conf/">avahi-daemon.conf</a>(5)</code>, <code><a href="/docs/linux/man/5-avahi-hosts/">avahi.hosts</a>(5)</code>, <code><a href="/docs/linux/man/5-avahi-service/">avahi.service</a>(5)</code>, <code><a href="/docs/linux/man/8-avahi-dnsconfd/">avahi-dnsconfd</a>(8)</code>, <code><a href="/docs/linux/man/1-avahi-set-host-name/">avahi-set-host-name</a>(1)</code> </p>
<p> <a rel="nofollow" href="http://avahi.org/wiki/AvahiAndUnicastDotLocal">http://avahi.org/wiki/AvahiAndUnicastDotLocal</a> documents the problems when using Avahi in a unicast DNS zone .local.</p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth.</p>
