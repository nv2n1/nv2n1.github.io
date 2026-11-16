---
title: "snmpd(8)"
name: "snmpd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-snmpd/"
description: "snmpd – daemon to respond to SNMP request packets."
---

<p>snmpd &#8211; daemon to respond to SNMP request packets.</p>
<h2>Synopsis</h2>
<p><code>snmpd</code> [OPTIONS] [LISTENING ADDRESSES]</p>
<h2>Description</h2>
<p><code>snmpd</code> is an SNMP agent which binds to a port and awaits requests from SNMP management software. Upon receiving a request, it processes the request(s), collects the requested information and/or performs the requested operation(s) and returns the information to the sender.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></dt>
<dd>Log the source addresses of incoming requests.</dd>
<dt><code>-A</code></dt>
<dd>Append to the log file rather than truncating it.</dd>
<dt><code>-c </code><i>FILE</i></dt>
<dd>Read <i>FILE</i> as a configuration file (or a comma-separated list of configuration files). Note that the loaded file will only understand snmpd.conf tokens, unless the configuration type is specified in the file as described in the snmp_config man page under SWITCHING CONFIGURATION TYPES IN MID-FILE.</dd>
<dt><code>-C</code></dt>
<dd>Do not read any configuration files except the ones optionally specified by the <code>-c </code> option. Note that this behaviour also covers the persistent configuration files. This may result in dynamically-assigned values being reset following an agent restart, unless the relevant persistent config files are explicitly loaded using the <code>-c </code> option.</dd>
<dt><code>-d</code></dt>
<dd>Dump (in hexadecimal) the sent and received SNMP packets.</dd>
<dt><code>-D</code><i>[TOKEN[,&#8230;]]</i></dt>
<dd>Turn on debugging output for the given <i>TOKEN</i>(s). Without any tokens specified, it defaults to printing all the tokens (which is equivalent to the keyword &quot;ALL&quot;). You might want to try <i>ALL</i> for extremely verbose output. Note: You can not put a space between the -D flag and the listed TOKENs.</dd>
<dt><code>-f</code></dt>
<dd>Do not fork() from the calling shell.</dd>
<dt><code>-g </code><i>GID</i></dt>
<dd>Change to the numerical group ID <i>GID</i> after opening listening sockets.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display a brief usage message and then exit.</dd>
<dt><code>-H</code></dt>
<dd>Display a list of configuration file directives understood by the agent and then exit.</dd>
<dt><code>-I </code><i>[-]INITLIST</i></dt>
<dd>Specifies which modules should (or should not) be initialized when the agent starts up. If the comma-separated <i>INITLIST</i> is preceded with a &#8216;-&#8216;, it is the list of modules that should <i>not</i> be started. Otherwise this is the list of the <i>only</i> modules that should be started. </dd>
<p> To get a list of compiled modules, run the agent with the arguments <i>-Dmib_init -H</i> (assuming debugging support has been compiled in).</p>
<dt><code>-L[efos]</code></dt>
<dd>Specify where logging output should be directed (standard error or output, to a file or via syslog). See LOGGING OPTIONS in snmpcmd(5) for details.</dd>
<dt><code>-m</code> <i>MIBLIST</i></dt>
<dd>Specifies a colon separated list of MIB modules to load for this application. This overrides the environment variable MIBS. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details.</dd>
<dt><code>-M</code> <i>DIRLIST</i></dt>
<dd>Specifies a colon separated list of directories to search for MIBs. This overrides the environment variable MIBDIRS. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details.</dd>
<dt><code>-n </code><i>NAME</i></dt>
<dd>Set an alternative application name (which will affect the configuration files loaded). By default this will be <i>snmpd</i>, regardless of the name of the actual binary.</dd>
<dt><code>-p </code><i>FILE</i></dt>
<dd>Save the process ID of the daemon in <i>FILE</i>.</dd>
<dt><code>-q</code></dt>
<dd>Print simpler output for easier automated parsing.</dd>
<dt><code>-r</code></dt>
<dd>Do not require root access to run the daemon. Specifically, do not exit if files only accessible to root (such as /dev/kmem etc.) cannot be opened.</dd>
<dt><code>-u </code><i>UID</i></dt>
<dd>Change to the user ID <i>UID</i> (which can be given in numerical or textual form) after opening listening sockets.</dd>
<dt><code>-U</code></dt>
<dd>Instructs the agent to not remove its pid file (see the <code>-p</code> option) on shutdown. Overrides the leave_pidfile token in the <i>snmpd.conf</i> file, see <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5).</i></dd>
<dt><code>-v, &#8211;version</code></dt>
<dd>Print version information for the agent and then exit.</dd>
<dt><code>-V</code></dt>
<dd>Symbolically dump SNMP transactions.</dd>
<dt><code>-x </code><i>ADDRESS</i></dt>
<dd>Listens for AgentX connections on the specified address rather than the default &quot;/var/agentx/master&quot;. The address can either be a Unix domain socket path, or the address of a network interface. The format is the same as the format of listening addresses described below.</dd>
<dt><code>-X</code></dt>
<dd>Run as an AgentX subagent rather than as an SNMP master agent.</dd>
<dt><code>&#8212;</code><i>name=value</i></dt>
<dd>Allows one to specify any token (&quot;name&quot;) supported in the <i>snmpd.conf</i> file and sets its value to &quot;value&quot;. Overrides the corresponding token in the <i>snmpd.conf</i> file. See <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> for the full list of tokens.</dd></dl>
<h2>Listening Addresses</h2>
<p>By default, <code>snmpd</code> listens for incoming SNMP requests on UDP port 161 on all IPv4 interfaces. However, it is possible to modify this behaviour by specifying one or more listening addresses as arguments to <code>snmpd</code>. A listening address takes the form:</p>
<dl>
<dd>[&lt;transport-specifier&gt;:]&lt;transport-address&gt;</dd></dl>
<p> At its simplest, a listening address may consist only of a port number, in which case <code>snmpd</code> listens on that UDP port on all IPv4 interfaces. Otherwise, the &lt;transport-address&gt; part of the specification is parsed according to the following table:</p>
<dl>
<dd>
</dd><dl>
<dt><code>&lt;transport-specifier&gt;</code></dt>
<dd><code>&lt;transport-address&gt; format</code></dd>
<dt>udp <i>(default)</i></dt>
<dd>hostname[:port] <i>or</i> IPv4-address[:port]</dd>
<dt>tcp</dt>
<dd>hostname[:port] <i>or</i> IPv4-address[:port]</dd>
<dt>unix</dt>
<dd>pathname</dd>
<dt>ipx</dt>
<dd>[network]:node[/port]</dd>
<dt><i></i>aal5pvc <i>or</i> pvc</dt>
<dd>[interface.][VPI.]VCI</dd>
<dt><i></i>udp6 <i>or</i> udpv6 <i>or</i> udpipv6</dt>
<dd>hostname[:port] <i>or</i> IPv6-address[:port]</dd>
<dt><i></i>tcp6 <i>or</i> tcpv6 <i>or</i> tcpipv6</dt>
<dd>hostname[:port] <i>or</i> IPv6-address[:port]</dd>
<dt><i></i>ssh</dt>
<dd>hostname:port</dd>
<dt><i></i>dtlsudp</dt>
<dd>hostname:port</dd></dl>
</dl>
<p> Note that &lt;transport-specifier&gt; strings are case-insensitive so that, for example, &quot;tcp&quot; and &quot;TCP&quot; are equivalent. Here are some examples, along with their interpretation:</p>
<dl>
<dt><i>127.0.0.1:161</i></dt>
<dd>listen on UDP port 161, but only on the loopback interface. This prevents <code>snmpd</code> being queried remotely. The port specification &quot;:161&quot; is not strictly necessary since that is the default SNMP port.</dd>
<dt><i>TCP:1161</i></dt>
<dd>listen on TCP port 1161 on all IPv4 interfaces.</dd>
<dt><i>ipx:/40000</i></dt>
<dd>listen on IPX port 40000 on all IPX interfaces.</dd>
<dt><i>unix:/tmp/local-agent</i></dt>
<dd>listen on the Unix domain socket <i>/tmp/local-agent</i>.</dd>
<dt><i>/tmp/local-agent</i></dt>
<dd>is identical to the previous specification, since the Unix domain is assumed if the first character of the &lt;transport-address&gt; is &#8216;/&#8217;.</dd>
<dt><i>PVC:161</i></dt>
<dd>listen on the AAL5 permanent virtual circuit with VPI=0 and VCI=161 (decimal) on the first ATM adapter in the machine.</dd>
<dt><i>udp6:10161</i></dt>
<dd>listen on port 10161 on all IPv6 interfaces.</dd>
<dt><i>ssh:127.0.0.1:22</i></dt>
<dd>Allows connections from the snmp subsystem on the ssh server on port 22. The details of using SNMP over SSH are defined below.</dd>
<dt><i>dtlsudp:127.0.0.1:9161</i></dt>
<dd>Listen for connections over DTLS on UDP port 9161. The snmp.conf file must have the <i>serverCert,</i> configuration tokens defined.</dd></dl>
<p> Note that not all the transport domains listed above will always be available; for instance, hosts with no IPv6 support will not be able to use udp6 transport addresses, and attempts to do so will result in the error &quot;Error opening specified endpoint&quot;. Likewise, since AAL5 PVC support is only currently available on Linux, it will fail with the same error on other platforms.</p>
<h2>Transport Specific Notes</h2>
<dl>
<dd>
</dd><dl>
<dt>ssh</dt>
<dd>The SSH transport, on the server side, is actually just a unix named pipe that can be connected to via a ssh subsystem configured in the main ssh server. The pipe location (configurable with the sshtosnmpsocket token in snmp.conf) is <i>/var/net-snmp/sshtosnmp.</i> Packets should be submitted to it via the sshtosnmp application, which also sends the user ID as well when starting the connection. The TSM security model should be used when packets should process it.</dd>
<dd>The <i>sshtosnmp</i> command knows how to connect to this pipe and talk to it. It should be configured in the <i>OpenSSH sshd</i> configuration file (which is normally <i>/etc/ssh/sshd_config</i> using the following configuration line:</dd>
<dd>Subsystem snmp /usr/local/bin/sshtosnmp</dd>
<dd>The <i>sshtosnmp</i> command will need read/write access to the <i>/var/net-snmp/sshtosnmp</i> pipe. Although it should be fairly safe to grant access to the average user since it still requires modifications to the ACM settings before the user can perform operations, paranoid administrators may want to make the /var/net-snmp directory accessible only by users in a particular group. Use the <i>sshtosnmpsocketperms</i> snmp.conf configure option to set the permissions, owner and group of the created socket.</dd>
<dd>Access control can be granted to the user &quot;foo&quot; using the following style of simple snmpd.conf settings:</dd>
<dd>rouser -s tsm foo authpriv</dd>
<dd>Note that &quot;authpriv&quot; is acceptable assuming as SSH protects everything that way (assuming you have a non-insane setup). snmpd has no notion of how SSH has actually protected a packet and thus the snmp agent assumes all packets passed through the SSH transport have been protected at the authpriv level.</dd>
<dt>dtlsudp</dt>
<dd>The DTLS protocol, which is based off of TLS, requires both client and server certificates to establish the connection and authenticate both sides. In order to do this, the client will need to configure the snmp.conf file with the <i>clientCert</i> configuration tokens. The server will need to configure the snmp.conf file with the <i>serverCert</i> configuration tokens defined.</dd>
<dd>Access control setup is similar to the ssh transport as the TSM security model should be used to protect the packet.</dd></dl>
</dl>
<h2>Configuration Files</h2>
<p><code>snmpd</code> checks for the existence of and parses the following files:</p>
<dl>
<dt><code>/etc/snmp/snmp.conf</code></dt>
<dd>Common configuration for the agent and applications. See <i><a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5)</i> for details.</dd>
<dt><code>/etc/snmp/snmpd.conf</code></dt>
<dd>
</dd><dt><code>/etc/snmp/snmpd.local.conf</code></dt>
<dd>Agent-specific configuration. See <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> for details. These files are optional and may be used to configure access control, trap generation, subagent protocols and much else besides.</dd>
<dd>In addition to these two configuration files in /etc/snmp, the agent will read any files with the names <i>snmpd.conf</i> and <i>snmpd.local.conf</i> in a colon separated path specified in the SNMPCONFPATH environment variable.</dd>
<dt><code>/usr/share/snmp/mibs/</code></dt>
<dd>The agent will also load all files in this directory as MIBs. It will not, however, load any file that begins with a &#8216;.&#8217; or descend into subdirectories.</dd></dl>
<h2>See Also</h2>
<p>(in recommended reading order) <a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5), <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5), <a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5) </p>
