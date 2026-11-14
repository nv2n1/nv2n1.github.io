---
title: "dhcp6c(8)"
name: "dhcp6c"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dhcp6c/"
description: "dhcp6c – DHCPv6 client daemon"
---

<p><code>dhcp6c</code> &#8211; DHCPv6 client daemon</p>
<h2>Synopsis</h2>
<p>[-<code>c </code><i>configfile</i> ] [-<code>Ddfi</code> ] [-<code>p </code><i>pid-file</i> ] [-<code>P </code><i>profile</i> ] <i>interface</i> [<i>interfaces&#8230;</i> ]</p>
<h2>Description</h2>
<p>works as a DHCPv6 client and gets information from DHCPv6 servers to configure the specified <i>interface</i> Multiple <i>interfaces</i> can be specified separated by spaces or tabs, in which case will work on all the interfaces simultaneously. </p>
<p> The command line options are:</p>
<dl>
<dt><code>-c </code><i>configfile</i></p>
<dd>Use <i>configfile</i> as the configuration file.</p>
<dt><code>-d</code></p>
<dd>Print debugging messages.</p>
<dt><code>-D</code></p>
<dd>Even more debugging information is printed.</p>
<dt><code>-f</code></p>
<dd>Foreground mode (useful when debugging). Although usually prints warning, debugging, or error messages to <a href="/docs/linux/man/8-syslog/">syslog</a>(8), it prints the messages to standard error if this option is specified.</p>
<dt><code>-i</code></p>
<dd>Info-req mode. In this mode, stateless DHCPv6 is executed with the folllowing configuration, and the obtained info is written to stdout. After this output, is terminated. (suits for a use in shell-script etc). </p>
<pre> interface (interface given in the argument) {
 information-only;
 script (a script which displays the received information to stdout);
 };</pre>
<p>Since the configuration is internally generated, you cannot provide a configuration in this mode. If you want to have different actions for the stateless DHCPv6 information, you should write an appropriate configuration and invoke without this option.</p>
<dt><code>-p </code><i>pid-file</i></p>
<dd>Use <i>pid-file</i> to dump the process ID of <code>.</code></p>
<dt><code>-P </code><i>profile</i></p>
<dd>Use the given <i>profile</i> defined in the configuration file for <i>interfaces</i> which do not have a specific configuration.</dl>
<p> The program will daemonize itself on invocation unless the &#8211;<code>f</code> or &#8211;<code>i</code> option is specified. </p>
<p> Upon receipt of the <code>SIGHUP</code> or <code>SIGTERM</code> signals, will remove all stateful resources from the system. In the former case the daemon will then reinvoke itself, while it will stop running in the latter case. In either case, will send DHCPv6 Release messages to release resources assigned from servers.</p>
<h2>Files</h2>
<dl>
<dt><code>/var/run/dhcp6c.pid </code></p>
<dd>is the default file that contains pid of the currently running <code>dhcp6c</code></p>
<dt><code>/etc/wide-dhcpv6/dhcp6c.conf </code></p>
<dd>is the default configuration file.</p>
<dt><code>/var/lib/dhcpv6/dhcp6c_duid </code></p>
<dd>is the file to store the client&#8217;s DUID.</dl>
<h2>Configuration Script</h2>
<p>When receives a reply message, it will invoke a supplementary configuration script specified in the dhcp6c.conf5 file. The daemon will provide the script with configuration parameters as environment variables, which include: </p>
<dl>
<dt><code>REASON</code></p>
<dd>The reason why the script is invoked. As of this writing, the value is always &quot;NBI&quot; and thus meaningless.</p>
<dt><code>new_domain_name_servers</code></p>
<dd>A list of available DNS servers, each of which is an IPv6 numeric address and is separated by a white space character.</p>
<dt><code>new_domain_name</code></p>
<dd>A list of DNS names, which provides DNS name search path.</p>
<dt><code>new_ntp_servers</code></p>
<dd>A list of available NTP servers, each of which is an IPv6 numeric address and is separated by a white space character.</p>
<dt><code>new_sip_servers</code></p>
<dd>A list of available SIP server addresses, each of which is an IPv6 numeric address and is separated by a white space character.</p>
<dt><code>new_sip_name</code></p>
<dd>A list of SIP server domain names.</p>
<dt><code>new_nis_servers</code></p>
<dd>A list of available NIS server addresses, each of which is an IPv6 numeric address and is separated by a white space character.</p>
<dt><code>new_nis_name</code></p>
<dd>A list of NIS domain names.</p>
<dt><code>new_nisp_servers</code></p>
<dd>A list of available NIS+ server addresses, each of which is an IPv6 numeric address and is separated by a white space character.</p>
<dt><code>new_nisp_name</code></p>
<dd>A list of NIS+ domain names.</p>
<dt><code>new_bcmcs_servers</code></p>
<dd>A list of available BCMCS server addresses, each of which is an IPv6 numeric address and is separated by a white space character.</p>
<dt><code>new_bcmcs_name</code></p>
<dd>A list of BCMCS server domain names.</dl>
<p> Note that the daemon does not always provide all the parameters. It sets an environment variable only when the corresponding configuration parameter is provided by the DHCPv6 server.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-daemon/">daemon</a>(3), dhcp6c.conf5, <a href="/docs/linux/man/8-dhcp6s/">dhcp6s</a>(8)</p>
<dl>
<dd>Ralph Droms, Editor 2003 <i>Dynamic Host Configuration Protocol for IPv6 (DHCPv6)</i> <i>RFC 3315</i></dl>
<h2>History</h2>
<p>The command first appeared in WIDE/KAME IPv6 protocol stack kit.</p>
<h2>Bugs</h2>
<p>is incomplete and violates DHCPv6 protocol spec, in several aspects. In particular, temporary address assignment is intentionally omitted. Information Refresh Time Option is not recognized in Info-req mode, since terminates after it receives a REPLY message. </p>
