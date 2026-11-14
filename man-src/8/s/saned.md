---
title: "saned(8)"
name: "saned"
section: "8"
letter: "s"
url: "/docs/linux/man/8-saned/"
description: "saned – SANE network daemon"
---

<p>saned &#8211; SANE network daemon</p>
<h2>Synopsis</h2>
<p><code>saned</code> <code>[ -a</code> <i>[ username ]</i> <code>]</code> <code>[ -u</code> <i>username</i> <code>]</code> <code>[ -b</code> <i>address</i> <code>]</code> <code>[ -p</code> <i>port</i> <code>]</code> <code>[ -l ]</code> <code>[ -D ]</code> <code>[ -o ]</code> <code>[ -d</code> <i>n</i> <code>]</code> <code>[ -e ]</code> <code>[ -h ]</code> </p>
<h2>Description</h2>
<p><code>saned</code> is the SANE (Scanner Access Now Easy) daemon that allows remote clients to access image acquisition devices available on the local host. </p>
<h2>Options</h2>
<p><code>saned</code> recognises the following options: </p>
<dl>
<dt><code>-a</code><i> [username]</i>, <code>&#8211;alone</code>[=<i>username]</i></p>
<dd>is equivalent to the combination of <code>-l -D -u</code> <i>username</i> options. However, <i>username</i> is optional and running user will only be set when specified. </p>
<dt><code>-u</code><i> username</i>, <code>&#8211;user</code>=<i>username</i></p>
<dd>requests that <code>saned</code> drop root privileges and run as the user (and group) associated with <i>username</i> after binding. </p>
<dt><code>-b</code><i> address</i>, <code>&#8211;bind</code>=<i>address</i></p>
<dd>tells <code>saned</code> to bind to the <i>address</i> given. </p>
<dt><code>-p</code><i> port</i>, <code>&#8211;port=</code><i>port</i></p>
<dd>tells <code>saned</code> to listen on the <i>port</i> given. A value of 0 tells <code>saned</code> to pick an unused port. The default is the <code>sane-port (6566).</code> </p>
<dt><code>-l</code>, <code>&#8211;listen</code></p>
<dd>requests that <code>saned</code> run in standalone daemon mode. In this mode, <code>saned</code> will listen for incoming client connections; <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) is not required for <code>saned</code> operations in this mode. </p>
<dt><code>-D</code>, <code>&#8211;daemonize</code></p>
<dd>will request <code>saned</code> to detach from the console and run in the background. </p>
<dt><code>-o</code>, <code>&#8211;once</code></p>
<dd>requests that <code>saned</code> exits after the first client disconnects. This is useful for debugging. </p>
<dt><code>-d</code><i> n</i>, <code>&#8211;debug</code>=<i>n</i></p>
<dd>sets the level of <code>saned</code> debug output to <i>n</i>. When compiled with debugging enabled, this flag may be followed by a number to request more or less debug info. The larger the number, the more verbose the debug output. E.g., <code>-d128</code> will request output of all debug info. A level of 0 produces no output at all. The default value is 2. </p>
<dt><code>-e</code>, <code>&#8211;stderr</code></p>
<dd>will divert <code>saned</code> debug output to stderr instead of the syslog default. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>displays a short help message.</dl>
<p> If <code>saned</code> is run from other programs such as <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8) and <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), check that program&#8217;s documentation on how to pass command-line options.</p>
<h2>Configuration</h2>
<p>First and foremost: <code>saned</code> is not intended to be exposed to the internet or other non-trusted networks. Make sure that access is limited by tcpwrappers and/or a firewall setup. Don&#8217;t depend only on <code>saned</code>&#8216;s own authentication. Don&#8217;t run <code>saned</code> as root if it&#8217;s not necessary. And do <code>not</code> install <code>saned</code> as setuid root. </p>
<p> The <i>saned.conf</i> configuration file contains both options for the daemon and the access list.</p>
<dl>
<dt><code>data_portrange</code> = <i>min_port</i> &#8211; <i>max_port</i></p>
<dd>Specify the port range to use for the data connection. Pick a port range between 1024 and 65535; don&#8217;t pick a too large port range, as it may have performance issues. Use this option if your <code>saned</code> server is sitting behind a firewall. If that firewall is a Linux machine, we strongly recommend using the Netfilter <i>nf_conntrack_sane</i> module instead.</p>
<dt><code>data_connect_timeout</code> = <i>timeout</i></p>
<dd>Specify the time in milliseconds that <code>saned</code> will wait for a data connection. Without this option, if the data connection is not done before the scanner reaches the end of scan, the scanner will continue to scan past the end and may damage it depending on the backend. Specify zero to have the old behavior. The default is 4000ms.</dl>
<p> The access list is a list of host names, IP addresses or IP subnets (CIDR notation) that are permitted to use local SANE devices. IPv6 addresses must be enclosed in brackets, and should always be specified in their compressed form. Connections from localhost are always permitted. Empty lines and lines starting with a hash mark (#) are ignored. A line containing the single character &#8220;+&#8221; is interpreted to match any hostname. This allows any remote machine to use your scanner and may present a security risk, so this shouldn&#8217;t be used unless you know what you&#8217;re doing. </p>
<p> A sample configuration file is shown below: </p>
<dl>
<dd># Daemon options<br />
 data_portrange = 10000 &#8211; 10100<br />
 # Access list<br />
 scan-client.somedomain.firm<br />
 # this is a comment<br />
 192.168.0.1<br />
 192.168.2.12/29<br />
 [::1]<br />
 [2001:db8:185e::42:12]/64</dl>
<p> The case of the host names does not matter, so AHost.COM is considered identical to ahost.com.</p>
<h2>Server Daemon Configuration</h2>
<p>For <code>saned</code> to work properly in its default mode of operation, it is also necessary to add the appropriate configuration for <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) or <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) (see below). Note that your <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) must support IPv6 if you want to connect to <code>saned</code> over IPv6; <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8), <code><a href="/docs/linux/man/8-openbsd-inetd/">openbsd-inetd</a></code>(8) and <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) are known to support IPv6, check the documentation for your <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) daemon. </p>
<p> In the sections below the configuration for <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8) and <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) are described in more detail. </p>
<p> For the configurations below it is necessary to add a line of the following form to <i>/etc/services</i>: </p>
<dl>
<dd>sane-port 6566/tcp # SANE network scanner daemon</dl>
<p> The official IANA short name for port 6566 is &quot;sane-port&quot;. The older name &quot;sane&quot; is now deprecated.</p>
<h2>Inetd Configuration</h2>
<p>It is required to add a single line to the <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) configuration file <i>(/etc/inetd.conf)</i> </p>
<p> The configuration line normally looks like this: </p>
<dl>
<dd>sane-port stream tcp nowait saned.saned /usr/sbin/saned saned</dl>
<p> However, if your system uses <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8) for additional security screening, you may want to disable <code>saned</code> access control by putting &#8220;+&#8221; in <i>saned.conf</i> and use a line of the following form in <i>/etc/inetd.conf</i> instead: </p>
<dl>
<dd>sane-port stream tcp nowait saned.saned /usr/sbin/tcpd /usr/sbin/saned</dl>
<p> Note that both examples assume that there is a <code>saned</code> group and a <code>saned</code> user. If you follow this example, please make sure that the access permissions on the special device are set such that <code>saned</code> can access the scanner (the program generally needs read and write access to scanner devices).</p>
<h2>Xinetd Configuration</h2>
<p>If <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8) is installed on your system instead of <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) the following example for <i>/etc/xinetd.conf</i> may be helpful: </p>
<dl>
<dd>
<pre># default: off
# description: The sane server accepts requests
# for network access to a local scanner via the
# network.
service sane-port
{
 port = 6566
 socket_type = stream
 wait = no
 user = saned
 group = saned
 server = /usr/sbin/saned
}</pre>
</dl>
<h2>Systemd Configuration</h2>
<p><code>saned</code> can be compiled with explicit <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) support. This will allow logging debugging information to be forwarded to the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) journal. The <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) support requires compilation with the systemd-devel package installed on the system. This is the preferred option. </p>
<p> <code>saned</code> can be used with <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) without the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) integration compiled in, but then logging of debug information is not supported. </p>
<p> The <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) configuration is different for the 2 options, so both are described below.</p>
<h2>Systemd configuration for saned with systemd support compiled in</h2>
<p>For <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) configuration we need to add 2 configuration files in <i>/etc/systemd/system</i>. </p>
<p> The first file we need to add here is called <i>saned.socket.</i> It shall have the following contents: </p>
<dl>
<dd>
<pre>[Unit]
Description=saned incoming socket
[Socket]
ListenStream=6566
Accept=yes
MaxConnections=1
[Install]
WantedBy=sockets.target</pre>
</dl>
<p> The second file to be added is <i>saned [at] .service</i> with the following contents: </p>
<dl>
<dd>
<pre>[Unit]
Description=Scanner Service
Requires=saned.socket
[Service]
ExecStart=/usr/sbin/saned
User=saned
Group=saned
StandardInput=null
StandardOutput=syslog
StandardError=syslog
Environment=SANE_CONFIG_DIR=/etc/sane.d
# If you need to debug your configuration uncomment the next line and
# change it as appropriate to set the desired debug options
# Environment=SANE_DEBUG_DLL=255 SANE_DEBUG_BJNP=5
[Install]
Also=saned.socket</pre>
</dl>
<p> You need to set an environment variable for <code>SANE_CONFIG_DIR</code> pointing to the directory where <code>saned</code> can find its configuration files. You will have to remove the # on the last line and set the variables for the desired debugging information if required. Multiple variables can be set by separating the assignments by spaces as shown in the example above. </p>
<p> Unlike <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8) and <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) allows debugging output from backends set using <code>SANE_DEBUG_XXX</code> to be captured. See the man-page for your backend to see what options are supported. With the service unit as described above, the debugging output is forwarded to the system log.</p>
<h2>Systemd configuration when saned is compiled without systemd support</h2>
<p>This configuration will also work when <code>saned</code> is compiled WITH <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) integration support, but it does not allow debugging information to be logged. </p>
<p> For <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) configuration for <code>saned</code>, we need to add 2 configuration files in <i>/etc/systemd/system</i>. </p>
<p> The first file we need to add here is called <i>saned.socket.</i> It is identical to the version for <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) with the support compiled in. It shall have the following contents: </p>
<dl>
<dd>
<pre>[Unit]
Description=saned incoming socket
[Socket]
ListenStream=6566
Accept=yes
MaxConnections=1
[Install]
WantedBy=sockets.target</pre>
</dl>
<p> The second file to be added is <i>saned [at] .service</i>. This one differs from the version with <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) integration compiled in: </p>
<dl>
<dd>
<pre>[Unit]
Description=Scanner Service
Requires=saned.socket
[Service]
ExecStart=/usr/sbin/saned
User=saned
Group=saned
StandardInput=socket
Environment=SANE_CONFIG_DIR=/etc/sane.d
[Install]
Also=saned.socket</pre>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/hosts.equiv</i></p>
<dd>The hosts listed in this file are permitted to access all local SANE devices. Caveat: this file imposes serious security risks and its use is not recommended.</p>
<dt><i>/etc/sane.d/saned.conf</i></p>
<dd>Contains a list of hosts permitted to access local SANE devices (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/etc/sane.d/saned.users</i></p>
<dd>If this file contains lines of the form </p>
<p> user:password:backend </p>
<p> access to the listed backends is restricted. A backend may be listed multiple times for different user/password combinations. The server uses MD5 hashing if supported by the client.</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order). </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xcam/">xcam</a></code>(1), <code><a href="/docs/linux/man/5-sane-dll/">sane-dll</a></code>(5), <code><a href="/docs/linux/man/5-sane-net/">sane-net</a></code>(5), <code><a href="/docs/linux/man/5-sane-backendname/">sane-backendname</a></code>(5), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)<br />
 <i><a rel="nofollow" href="http://www.penguin-breeder.org/?page=sane-net">http://www.penguin-breeder.org/?page=sane-net</a></i></p>
<h2>Author</h2>
<p>David Mosberger</p>
