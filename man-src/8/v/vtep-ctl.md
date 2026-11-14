---
title: "vtep-ctl(8)"
name: "vtep-ctl"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vtep-ctl/"
description: "vtep-ctl – utility for querying and configuring a VTEP database"
---

<p>vtep-ctl &#8211; utility for querying and configuring a VTEP database</p>
<h2>Synopsis</h2>
<p><code>vtep-ctl</code> [<i>options</i>] <code>&#8212;</code> [<i>options</i>] <i>command </i>[<i>args</i>] [<code>&#8212;</code> [<i>options</i>] <i>command </i>[<i>args</i>]]&#8230;</p>
<h2>Description</h2>
<p>The <code>vtep-ctl</code> program configures a VTEP database. See <code><a href="/docs/linux/man/5-vtep/">vtep</a></code>(5) for comprehensive documentation of the database schema. </p>
<p> <code>vtep-ctl</code> connects to an <code>ovsdb-server</code> process that maintains a VTEP configuration database. Using this connection, it queries and possibly applies changes to the database, depending on the supplied commands. </p>
<p> <code>vtep-ctl</code> can perform any number of commands in a single run, implemented as a single atomic transaction against the database. </p>
<p> The <code>vtep-ctl</code> command line begins with global options (see <code>OPTIONS</code> below for details). The global options are followed by one or more commands. Each command should begin with <code>&#8212;</code> by itself as a command-line argument, to separate it from the following commands. (The <code>&#8212;</code> before the first command is optional.) The command itself starts with command-specific options, if any, followed by the command name and any arguments. See <code>EXAMPLES</code> below for syntax examples.</p>
<h2>Options</h2>
<p>The following options affect the behavior <code>vtep-ctl</code> as a whole. Some individual commands also accept their own options, which are given just before the command name. If the first command on the command line has options, then those options must be separated from the global options by <code>&#8212;</code>.</p>
<dl>
<dt><code>&#8211;db=</code><i>server</i></p>
<dd>Sets <i>server</i> as the database server that <code>vtep-ctl</code> contacts to query or modify configuration. The default is <code>unix:/var/run/openvswitch/db.sock</code>. <i>server</i> must take one of the following forms:</p>
<dl>
<dd>
<dl>
<dt><code>ssl:</code><i>ip</i><code>:</code><i>port</i></p>
<dd>The specified SSL <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name) in IPv4 or IPv6 address format. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>ssl:[::1]:6640</code>. The <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory when this form is used.</p>
<dt><code>tcp:</code><i>ip</i><code>:</code><i>port</i></p>
<dd>Connect to the given TCP <i>port</i> on <i>ip</i>, where <i>ip</i> can be IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>tcp:[::1]:6640</code>.</p>
<dt><code>unix:</code><i>file</i></p>
<dd>On POSIX, connect to the Unix domain server socket named <i>file</i>.</p>
<dd>On Windows, connect to a localhost TCP port whose value is written in <i>file</i>.</p>
<dt><code>pssl:</code><i>port</i>[<code>:</code><i>ip</i>]</p>
<dd>Listen on the given SSL <i>port</i> for a connection. By default, connections are not bound to a particular local IP address and it listens only on IPv4 (but not IPv6) addresses, but specifying <i>ip</i> limits connections to those from the given <i>ip</i>, either IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>pssl:6640:[::1]</code>. The <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory when this form is used.</p>
<dt><code>ptcp:</code><i>port</i>[<code>:</code><i>ip</i>]</p>
<dd>Listen on the given TCP <i>port</i> for a connection. By default, connections are not bound to a particular local IP address and it listens only on IPv4 (but not IPv6) addresses, but <i>ip</i> may be specified to listen only for connections to the given <i>ip</i>, either IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>ptcp:6640:[::1]</code>.</p>
<dt><code>punix:</code><i>file</i></p>
<dd>On POSIX, listen on the Unix domain server socket named <i>file</i> for a connection.</p>
<dd>On Windows, listen on a kernel chosen TCP port on the localhost. The kernel chosen TCP port value is written in <i>file</i>.</dl>
</dl>
<dt><code>&#8211;no-syslog</code></p>
<dd>By default, <code>vtep-ctl</code> logs its arguments and the details of any changes that it makes to the system log. This option disables this logging.</p>
<dd>This option is equivalent to <code>&#8211;verbose=vtep_ctl:syslog:warn</code>.</p>
<dt><code>&#8211;oneline</code></p>
<dd>Modifies the output format so that the output for each command is printed on a single line. New-line characters that would otherwise separate lines are printed as <code>
</code>, and any instances of <code>\</code> that would otherwise appear in the output are doubled. Prints a blank line for each command that has no output. This option does not affect the formatting of output from the <code>list</code> or <code>find</code> commands; see <code>Table Formatting Options</code> below.</p>
<dt><code>&#8211;dry-run</code></p>
<dd>Prevents <code>vtep-ctl</code> from actually modifying the database.</p>
<dt><code>-t </code><i>secs</i></p>
<dd>
<dt><code>&#8211;timeout=</code><i>secs</i></p>
<dd>By default, or with a <i>secs</i> of <code>0</code>, <code>vtep-ctl</code> waits forever for a response from the database. This option limits runtime to approximately <i>secs</i> seconds. If the timeout expires, <code>vtep-ctl</code> will exit with a <code>SIGALRM</code> signal. (A timeout would normally happen only if the database cannot be contacted, or if the system is overloaded.)</dl>
<h3>Table Formatting Options</h3>
<p>These options control the format of output from the <code>list</code> and <code>find</code> commands.</p>
<dl>
<dt><code>-f </code><i>format</i></p>
<dd>
<dt><code>&#8211;format=</code><i>format</i></p>
<dd>Sets the type of table formatting. The following types of <i>format</i> are available:</p>
<dl>
<dd>
<dl>
<dt><code>table</code> (default)</p>
<dd>2-D text tables with aligned columns.</p>
<dt><code>list</code></p>
<dd>A list with one column per line and rows separated by a blank line.</p>
<dt><code>html</code></p>
<dd>HTML tables.</p>
<dt><code>csv</code></p>
<dd>Comma-separated values as defined in RFC 4180.</p>
<dt><code>json</code></p>
<dd>JSON format as defined in RFC 4627. The output is a sequence of JSON objects, each of which corresponds to one table. Each JSON object has the following members with the noted values:</p>
<dl>
<dd>
<dl>
<dt><code>caption</code></p>
<dd>The table&#8217;s caption. This member is omitted if the table has no caption.</p>
<dt><code>headings</code></p>
<dd>An array with one element per table column. Each array element is a string giving the corresponding column&#8217;s heading.</p>
<dt><code>data</code></p>
<dd>An array with one element per table row. Each element is also an array with one element per table column. The elements of this second-level array are the cells that constitute the table. Cells that represent OVSDB data or data types are expressed in the format described in the OVSDB specification; other cells are simply expressed as text strings.</dl>
</dl>
</dl>
</dl>
<dt><code>-d </code><i>format</i></p>
<dd>
<dt><code>&#8211;data=</code><i>format</i></p>
<dd>Sets the formatting for cells within output tables. The following types of <i>format</i> are available:</p>
<dl>
<dd>
<dl>
<dt><code>string</code> (default)</p>
<dd>The simple format described in the <code>Database Values</code> section of <code><a href="/docs/linux/man/8-ovs-vsctl/">ovs-vsctl</a></code>(8).</p>
<dt><code>bare</code></p>
<dd>The simple format with punctuation stripped off: <code>[]</code> and <code>{}</code> are omitted around sets, maps, and empty columns, items within sets and maps are space-separated, and strings are never quoted. This format may be easier for scripts to parse.</p>
<dt><code>json</code></p>
<dd>JSON.</dl>
</dl>
<dd>The <code>json</code> output format always outputs cells in JSON format, ignoring this option.</p>
<dt><code>&#8211;no-heading</code></p>
<dd>This option suppresses the heading row that otherwise appears in the first row of table output.</p>
<dt><code>&#8211;pretty</code></p>
<dd>By default, JSON in output is printed as compactly as possible. This option causes JSON in output to be printed in a more readable fashion. Members of objects and elements of arrays are printed one per line, with indentation.</p>
<dd>This option does not affect JSON in tables, which is always printed compactly.</p>
<dt><code>&#8211;bare</code></p>
<dd>Equivalent to <code>&#8211;format=list &#8211;data=bare &#8211;no-headings</code>.</dl>
<h3>Public Key Infrastructure Options</h3>
<dl>
<dt><code>-p</code> <i>privkey.pem</i></p>
<dd>
<dt><code>&#8211;private-key=</code><i>privkey.pem</i></p>
<dd>Specifies a PEM file containing the private key used as <code>vtep-ctl</code>&#8216;s identity for outgoing SSL connections.</p>
<dt><code>-c</code> <i>cert.pem</i></p>
<dd>
<dt><code>&#8211;certificate=</code><i>cert.pem</i></p>
<dd>Specifies a PEM file containing a certificate that certifies the private key specified on <code>-p</code> or <code>&#8211;private-key</code> to be trustworthy. The certificate must be signed by the certificate authority (CA) that the peer in SSL connections will use to verify it.</p>
<dt><code>-C</code> <i>cacert.pem</i></p>
<dd>
<dt><code>&#8211;ca-cert=</code><i>cacert.pem</i></p>
<dd>Specifies a PEM file containing the CA certificate that <code>vtep-ctl</code> should use to verify certificates presented to it by SSL peers. (This may be the same certificate that SSL peers use to verify the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>, or it may be a different one, depending on the PKI design in use.)</p>
<dt><code>-C none</code></p>
<dd>
<dt><code>&#8211;ca-cert=none</code></p>
<dd>Disables verification of certificates presented by SSL peers. This introduces a security risk, because it means that certificates cannot be verified to be those of known trusted hosts.</p>
<dt><code>&#8211;bootstrap-ca-cert=</code><i>cacert.pem</i></p>
<dd>When <i>cacert.pem</i> exists, this option has the same effect as <code>-C</code> or <code>&#8211;ca-cert</code>. If it does not exist, then <code>vtep-ctl</code> will attempt to obtain the CA certificate from the SSL peer on its first SSL connection and save it to the named PEM file. If it is successful, it will immediately drop the connection and reconnect, and from then on all SSL connections must be authenticated by a certificate signed by the CA certificate thus obtained.</p>
<dd><code>This option exposes the SSL connection to a man-in-the-middle attack obtaining the initial CA certificate</code>, but it may be useful for bootstrapping.</p>
<dd>This option is only useful if the SSL peer sends its CA certificate as part of the SSL certificate chain. The SSL protocol does not require the server to send the CA certificate.</p>
<dd>This option is mutually exclusive with <code>-C</code> and <code>&#8211;ca-cert</code>.</p>
<dt><code>&#8211;peer-ca-cert=</code><i>peer-cacert.pem</i></p>
<dd>Specifies a PEM file that contains one or more additional certificates to send to SSL peers. <i>peer-cacert.pem</i> should be the CA certificate used to sign <code>vtep-ctl</code>&#8216;s own certificate, that is, the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>. If <code>vtep-ctl</code>&#8216;s certificate is self-signed, then <code>&#8211;certificate</code> and <code>&#8211;peer-ca-cert</code> should specify the same file.</p>
<dd>This option is not useful in normal operation, because the SSL peer must already have the CA certificate for the peer to have any confidence in <code>vtep-ctl</code>&#8216;s identity. However, this offers a way for a new installation to bootstrap the CA certificate on its first SSL connection.</p>
<dt><code>-v</code>[<i>spec</i>]</p>
<dd>
<dt><code>&#8211;verbose=</code>[<i>spec</i>]</p>
<dd>Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd><code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively. (If <code>&#8211;detach</code> is specified, <code>vtep-ctl</code> closes its standard file descriptors, so logging to the console will have no effect.)</p>
<dd>On Windows platform, <code>syslog</code> is accepted as a word and is only useful along with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd><code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages. See <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a definition of each log level.</dl>
</dl>
<dd>Case is not significant within <i>spec</i>.</p>
<dd>Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless <code>&#8211;log-file</code> is also specified (see below).</p>
<dd>For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Sets the maximum logging verbosity level, equivalent to <code>&#8211;verbose=dbg</code>.</p>
<dt><code>-vPATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>
<dt><code>&#8211;verbose=PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>Sets the log pattern for <i>destination</i> to <i>pattern</i>. Refer to <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a description of the valid syntax for <i>pattern</i>.</p>
<dt><code>-vFACILITY:</code><i>facility</i></p>
<dd>
<dt><code>&#8211;verbose=FACILITY:</code><i>facility</i></p>
<dd>Sets the RFC5424 facility of the log message. <i>facility</i> can be one of <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>clock</code>, <code>ftp</code>, <code>ntp</code>, <code>audit</code>, <code>alert</code>, <code>clock2</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>, <code>local4</code>, <code>local5</code>, <code>local6</code> or <code>local7</code>. If this option is not specified, <code>daemon</code> is used as the default for the local system syslog and <code>local0</code> is used while sending a message to the target provided via the <code>&#8211;syslog-target</code> option.</p>
<dt><code>&#8211;log-file</code>[<code>=</code><i>file</i>]</p>
<dd>Enables logging to a file. If <i>file</i> is specified, then it is used as the exact name for the log file. The default log file name used if <i>file</i> is omitted is <code>/var/log/openvswitch/vtep-ctl.log</code>.</p>
<dt><code>&#8211;syslog-target=</code><i>host</i><code>:</code><i>port</i></p>
<dd>Send syslog messages to UDP <i>port</i> on <i>host</i>, in addition to the system syslog. The <i>host</i> must be a numerical IP address, not a hostname.</p>
<dt><code>&#8211;syslog-method=</code><i>method</i></p>
<dd>Specify <i>method</i> how syslog messages should be sent to syslog daemon. Following forms are supported:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>libc</code>, use libc <code>syslog()</code> function. This is the default behavior. Downside of using this options is that libc adds fixed prefix to every message before it is actually sent to the syslog daemon over <code>/dev/log</code> UNIX domain socket.</p>
<dt>&bull;</p>
<dd><code>unix:</code><i>file</i>, use UNIX domain socket directly. It is possible to specify arbitrary message format with this option. However, <code>rsyslogd 8.9</code> and older versions use hard coded parser function anyway that limits UNIX domain socket use. If you want to use arbitrary message format with older <code>rsyslogd</code> versions, then use UDP socket to localhost IP address instead.</p>
<dt>&bull;</p>
<dd><code>udp:</code><i>ip</i>:<i>port</i>, use UDP socket. With this method it is possible to use arbitrary message format also with older <code>rsyslogd</code>. When sending syslog messages over UDP socket extra precaution needs to be taken into account, for example, syslog daemon needs to be configured to listen on the specified UDP port, accidental iptables rules could be interfering with local syslog traffic and there are some security considerations that apply to UDP sockets, but do not apply to UNIX domain sockets.</dl>
</dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Prints a brief help message to the console.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Prints version information to the console.</dl>
<h2>Commands</h2>
<p>The commands implemented by <code>vtep-ctl</code> are described in the sections below.</p>
<h3>Physical Switch Commands</h3>
<p>These commands examine and manipulate physical switches.</p>
<dl>
<dt>[<code>&#8211;may-exist</code>] <code>add-ps </code><i>pswitch</i></p>
<dd>Creates a new physical switch named <i>pswitch</i>. Initially the switch will have no ports.</p>
<dd>Without <code>&#8211;may-exist</code>, attempting to create a switch that exists is an error. With <code>&#8211;may-exist</code>, this command does nothing if <i>pswitch</i> already exists.</p>
<dt>[<code>&#8211;if-exists</code>] <code>del-ps </code><i>pswitch</i></p>
<dd>Deletes <i>pswitch</i> and all of its ports.</p>
<dd>Without <code>&#8211;if-exists</code>, attempting to delete a switch that does not exist is an error. With <code>&#8211;if-exists</code>, attempting to delete a switch that does not exist has no effect.</p>
<dt><code>list-ps</code></p>
<dd>Lists all existing physical switches on standard output, one per line.</p>
<dt><code>ps-exists </code><i>pswitch</i></p>
<dd>Tests whether <i>pswitch</i> exists. If so, <code>vtep-ctl</code> exits successfully with exit code 0. If not, <code>vtep-ctl</code> exits unsuccessfully with exit code 2.</dl>
<h3>Port Commands</h3>
<p>These commands examine and manipulate VTEP physical ports.</p>
<dl>
<dt><code>list-ports </code><i>pswitch</i></p>
<dd>Lists all of the ports within <i>pswitch</i> on standard output, one per line.</p>
<dt>[<code>&#8211;may-exist</code>] <code>add-port </code><i>pswitch port</i></p>
<dd>Creates on <i>pswitch</i> a new port named <i>port</i> from the network device of the same name.</p>
<dd>Without <code>&#8211;may-exist</code>, attempting to create a port that exists is an error. With <code>&#8211;may-exist</code>, this command does nothing if <i>port</i> already exists on <i>pswitch</i>.</p>
<dt>[<code>&#8211;if-exists</code>] <code>del-port </code>[<i>pswitch</i>] <i>port</i></p>
<dd>Deletes <i>port</i>. If <i>pswitch</i> is omitted, <i>port</i> is removed from whatever switch contains it; if <i>pswitch</i> is specified, it must be the switch that contains <i>port</i>.</p>
<dd>Without <code>&#8211;if-exists</code>, attempting to delete a port that does not exist is an error. With <code>&#8211;if-exists</code>, attempting to delete a port that does not exist has no effect.</dl>
<h3>Logical Switch Commands</h3>
<p>These commands examine and manipulate logical switches.</p>
<dl>
<dt>[<code>&#8211;may-exist</code>] <code>add-ls </code><i>lswitch</i></p>
<dd>Creates a new logical switch named <i>lswitch</i>. Initially the switch will have no locator bindings.</p>
<dd>Without <code>&#8211;may-exist</code>, attempting to create a switch that exists is an error. With <code>&#8211;may-exist</code>, this command does nothing if <i>lswitch</i> already exists.</p>
<dt>[<code>&#8211;if-exists</code>] <code>del-ls </code><i>lswitch</i></p>
<dd>Deletes <i>lswitch</i>.</p>
<dd>Without <code>&#8211;if-exists</code>, attempting to delete a switch that does not exist is an error. With <code>&#8211;if-exists</code>, attempting to delete a switch that does not exist has no effect.</p>
<dt><code>list-ls</code></p>
<dd>Lists all existing logical switches on standard output, one per line.</p>
<dt><code>ls-exists </code><i>lswitch</i></p>
<dd>Tests whether <i>lswitch</i> exists. If so, <code>vtep-ctl</code> exits successfully with exit code 0. If not, <code>vtep-ctl</code> exits unsuccessfully with exit code 2.</p>
<dt><code>bind-ls </code><i>pswitch port vlan lswitch</i></p>
<dd>Bind logical switch <i>lswitch</i> to the <i>port</i>/<i>vlan</i> combination on the physical switch <i>pswitch</i>.</p>
<dt><code>unbind-ls </code><i>pswitch port vlan</i></p>
<dd>Remove the logical switch binding from the <i>port</i>/<i>vlan</i> combination on the physical switch <i>pswitch</i>.</p>
<dt><code>list-bindings </code><i>pswitch port</i></p>
<dd>List the logical switch bindings for <i>port</i> on the physical switch <i>pswitch</i>.</dl>
<h3>Local MAC Binding Commands</h3>
<p>These commands examine and manipulate local MAC bindings for the logical switch. The local maps are written by the VTEP to refer to MACs it has learned on its physical ports.</p>
<dl>
<dt><code>add-ucast-local </code><i>lswitch mac</i> [<i>encap</i>] <i>ip</i></p>
<dd>Map the unicast Ethernet address <i>mac</i> to the physical location <i>ip</i> using encapsulation <i>encap</i> on <i>lswitch</i>. If <i>encap</i> is not specified, the default is &quot;vxlan_over_ipv4&quot;. The local mappings are used by the VTEP to refer to MACs learned on its physical ports.</p>
<dt><code>del-ucast-local </code><i>lswitch mac</i></p>
<dd>Remove the local unicast Ethernet address <i>mac</i> map from <i>lswitch</i>. The local mappings are used by the VTEP to refer to MACs learned on its physical ports.</p>
<dt><code>add-mcast-local </code><i>lswitch mac</i> [<i>encap</i>] <i>ip</i></p>
<dd>Add physical location <i>ip</i> using encapsulation <i>encap</i> to the local mac binding table for multicast Ethernet address <i>mac</i> on <i>lswitch</i>. If <i>encap</i> is not specified, the default is &quot;vxlan_over_ipv4&quot;. The local mappings are used by the VTEP to refer to MACs learned on its physical ports.</p>
<dt><code>del-mcast-local </code><i>lswitch mac</i> [<i>encap</i>] <i>ip</i></p>
<dd>Remove physical location <i>ip</i> using encapsulation <i>encap</i> from the local mac binding table for multicast Ethernet address <i>mac</i> on <i>lswitch</i>. If <i>encap</i> is not specified, the default is &quot;vxlan_over_ipv4&quot;. The local mappings are used by the VTEP to refer to MACs learned on its physical ports.</p>
<dt><code>clear-local-macs </code><i>lswitch</i></p>
<dd>Clear the local MAC bindings for <i>lswitch</i>.</p>
<dt><code>list-local-macs </code><i>lswitch</i></p>
<dd>List the local MAC bindings for <i>lswitch</i>, one per line.</dl>
<h3>Remote MAC Binding Commands</h3>
<p>These commands examine and manipulate local and remote MAC bindings for the logical switch. The remote maps are written by the network virtualization controller to refer to MACs that it has learned.</p>
<dl>
<dt><code>add-ucast-remote </code><i>lswitch mac</i> [<i>encap</i>] <i>ip</i></p>
<dd>Map the unicast Ethernet address <i>mac</i> to the physical location <i>ip</i> using encapsulation <i>encap</i> on <i>lswitch</i>. If <i>encap</i> is not specified, the default is &quot;vxlan_over_ipv4&quot;. The remote mappings are used by the network virtualization platform to refer to MACs that it has learned.</p>
<dt><code>del-ucast-remote </code><i>lswitch mac</i></p>
<dd>Remove the remote unicast Ethernet address <i>mac</i> map from <i>lswitch</i>. The remote mappings are used by the network virtualization platform to refer to MACs that it has learned.</p>
<dt><code>add-mcast-remote </code><i>lswitch mac</i> [<i>encap</i>] <i>ip</i></p>
<dd>Add physical location <i>ip</i> using encapsulation <i>encap</i> to the remote mac binding table for multicast Ethernet address <i>mac</i> on <i>lswitch</i>. If <i>encap</i> is not specified, the default is &quot;vxlan_over_ipv4&quot;. The remote mappings are used by the network virtualization platform to refer to MACs that it has learned.</p>
<dt><code>del-mcast-remote </code><i>lswitch mac</i> [<i>encap</i>] <i>ip</i></p>
<dd>Remove physical location <i>ip</i> using encapsulation <i>encap</i> from the remote mac binding table for multicast Ethernet address <i>mac</i> on <i>lswitch</i>. If <i>encap</i> is not specified, the default is &quot;vxlan_over_ipv4&quot;. The remote mappings are used by the network virtualization platform to refer to MACs that it has learned.</p>
<dt><code>clear-remote-macs </code><i>lswitch</i></p>
<dd>Clear the remote MAC bindings for <i>lswitch</i>.</p>
<dt><code>list-remote-macs </code><i>lswitch</i></p>
<dd>List the remote MAC bindings for <i>lswitch</i>, one per line.</dl>
<h3>Manager Connectivity</h3>
<p>These commands manipulate the <code>managers</code> column in the <code>Global</code> table and rows in the <code>Managers</code> table. When <code>ovsdb-server</code> is configured to use the <code>managers</code> column for OVSDB connections (as described in <code>INSTALL.Linux</code> and in the startup scripts provided with Open vSwitch), this allows the administrator to use <code>vtep-ctl</code> to configure database connections.</p>
<dl>
<dt><code>get-manager</code></p>
<dd>Prints the configured manager(s).</p>
<dt><code>del-manager</code></p>
<dd>Deletes the configured manager(s).</p>
<dt><code>set-manager</code> <i>target</i>&#8230;</p>
<dd>Sets the configured manager target or targets. Each <i>target</i> may use any of the following forms:</p>
<dl>
<dd>
<dl>
<dt><code>ssl:</code><i>ip</i><code>:</code><i>port</i></p>
<dd>The specified SSL <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name) in IPv4 or IPv6 address format. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>ssl:[::1]:6640</code>. The <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory when this form is used.</p>
<dt><code>tcp:</code><i>ip</i><code>:</code><i>port</i></p>
<dd>Connect to the given TCP <i>port</i> on <i>ip</i>, where <i>ip</i> can be IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>tcp:[::1]:6640</code>.</p>
<dt><code>unix:</code><i>file</i></p>
<dd>On POSIX, connect to the Unix domain server socket named <i>file</i>.</p>
<dd>On Windows, connect to a localhost TCP port whose value is written in <i>file</i>.</p>
<dt><code>pssl:</code><i>port</i>[<code>:</code><i>ip</i>]</p>
<dd>Listen on the given SSL <i>port</i> for a connection. By default, connections are not bound to a particular local IP address and it listens only on IPv4 (but not IPv6) addresses, but specifying <i>ip</i> limits connections to those from the given <i>ip</i>, either IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>pssl:6640:[::1]</code>. The <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory when this form is used.</p>
<dt><code>ptcp:</code><i>port</i>[<code>:</code><i>ip</i>]</p>
<dd>Listen on the given TCP <i>port</i> for a connection. By default, connections are not bound to a particular local IP address and it listens only on IPv4 (but not IPv6) addresses, but <i>ip</i> may be specified to listen only for connections to the given <i>ip</i>, either IPv4 or IPv6 address. If <i>ip</i> is an IPv6 address, then wrap <i>ip</i> with square brackets, e.g.: <code>ptcp:6640:[::1]</code>.</p>
<dt><code>punix:</code><i>file</i></p>
<dd>On POSIX, listen on the Unix domain server socket named <i>file</i> for a connection.</p>
<dd>On Windows, listen on a kernel chosen TCP port on the localhost. The kernel chosen TCP port value is written in <i>file</i>.</dl>
</dl>
</dl>
<h3>Database Commands</h3>
<p>These commands query and modify the contents of <code>ovsdb</code> tables. They are a slight abstraction of the <code>ovsdb</code> interface and as such they operate at a lower level than other <code>vtep-ctl</code> commands. </p>
<p> <i>Identifying Tables, Records, and Columns</i> </p>
<p> Each of these commands has a <i>table</i> parameter to identify a table within the database. Many of them also take a <i>record</i> parameter that identifies a particular record within a table. The <i>record</i> parameter may be the UUID for a record, and many tables offer additional ways to identify records. Some commands also take <i>column</i> parameters that identify a particular field within the records in a table. </p>
<p> The following tables are currently defined:</p>
<dl>
<dt><code>Global</code></p>
<dd>Top-level configuration for a hardware VTEP. This table contains exactly one record, identified by specifying <code>.</code> as the record name.</p>
<dt><code>Manager</code></p>
<dd>Configuration for an OVSDB connection. Records may be identified by target (e.g. <code>tcp:1.2.3.4</code>).</p>
<dt><code>Physical_Switch</code></p>
<dd>A physical switch that implements a VTEP. Records may be identified by physical switch name.</p>
<dt><code>Physical_Port</code></p>
<dd>A port within a physical switch.</p>
<dt><code>Logical_Binding_Stats</code></p>
<dd>Reports statistics for the logical switch with which a VLAN on a physical port is associated.</p>
<dt><code>Logical_Switch</code></p>
<dd>A logical Ethernet switch. Records may be identified by logical switch name.</p>
<dt><code>Ucast_Macs_Local</code></p>
<dd>Mapping of locally discovered unicast MAC addresses to tunnels.</p>
<dt><code>Ucast_Macs_Remote</code></p>
<dd>Mapping of remotely programmed unicast MAC addresses to tunnels.</p>
<dt><code>Mcast_Macs_Local</code></p>
<dd>Mapping of locally discovered multicast MAC addresses to tunnels.</p>
<dt><code>Mcast_Macs_Remote</code></p>
<dd>Mapping of remotely programmed multicast MAC addresses to tunnels.</p>
<dt><code>Physical_Locator_Set</code></p>
<dd>A set of one or more physical locators.</p>
<dt><code>Physical_Locator</code></p>
<dd>Identifies an endpoint to which logical switch traffic may be encapsulated and forwarded. Records may be identified by physical locator name.</dl>
<p> Record names must be specified in full and with correct capitalization. Names of tables and columns are not case-sensitive, and <code>&#8212;</code> and <code>_</code> are treated interchangeably. Unique abbreviations are acceptable, e.g. <code>man</code> or <code>m</code> is sufficient to identify the <code>Manager</code> table. </p>
<p> <i>Database Values</i> </p>
<p> Each column in the database accepts a fixed type of data. The currently defined basic types, and their representations, are:</p>
<dl>
<dt>integer</p>
<dd>A decimal integer in the range -2**63 to 2**63-1, inclusive.</p>
<dt>real</p>
<dd>A floating-point number.</p>
<dt>Boolean</p>
<dd>True or false, written <code>true</code> or <code>false</code>, respectively.</p>
<dt>string</p>
<dd>An arbitrary Unicode string, except that null bytes are not allowed. Quotes are optional for most strings that begin with an English letter or underscore and consist only of letters, underscores, hyphens, and periods. However, <code>true</code> and <code>false</code> and strings that match the syntax of UUIDs (see below) must be enclosed in double quotes to distinguish them from other basic types. When double quotes are used, the syntax is that of strings in JSON, e.g. backslashes may be used to escape special characters. The empty string must be represented as a pair of double quotes (<code>&quot;&quot;</code>).</p>
<dt>UUID</p>
<dd>Either a universally unique identifier in the style of RFC 4122, e.g. <code>f81d4fae-7dec-11d0-a765-00a0c91e6bf6</code>, or an <code>@</code><i>name</i> defined by a <code>get</code> or <code>create</code> command within the same <code>vtep-ctl</code> invocation.</dl>
<p> Multiple values in a single column may be separated by spaces or a single comma. When multiple values are present, duplicates are not allowed, and order is not important. Conversely, some database columns can have an empty set of values, represented as <code>[]</code>, and square brackets may optionally enclose other non-empty sets or single values as well. </p>
<p> A few database columns are &#8220;maps&#8221; of key-value pairs, where the key and the value are each some fixed database type. These are specified in the form <i>key</i><code>=</code><i>value</i>, where <i>key</i> and <i>value</i> follow the syntax for the column&#8217;s key type and value type, respectively. When multiple pairs are present (separated by spaces or a comma), duplicate keys are not allowed, and again the order is not important. Duplicate values are allowed. An empty map is represented as <code>{}</code>. Curly braces may optionally enclose non-empty maps as well (but use quotes to prevent the shell from expanding <code>other-config={0=x,1=y}</code> into <code>other-config=0=x other-config=1=y</code>, which may not have the desired effect). </p>
<p> <i>Database Command Syntax</i></p>
<dl>
<dt>[<code>&#8211;if-exists</code>] [<code>&#8211;columns=</code><i>column</i>[<code>,</code><i>column</i>]&#8230;] <code>list </code><i>table </i>[<i>record</i>]&#8230;</p>
<dd>Lists the data in each specified <i>record</i>. If no records are specified, lists all the records in <i>table</i>.</p>
<dd>If <code>&#8211;columns</code> is specified, only the requested columns are listed, in the specified order. Otherwise, all columns are listed, in alphabetical order by column name.</p>
<dd>Without <code>&#8211;if-exists</code>, it is an error if any specified <i>record</i> does not exist. With <code>&#8211;if-exists</code>, the command ignores any <i>record</i> that does not exist, without producing any output.</p>
<dt>[<code>&#8211;columns=</code><i>column</i>[<code>,</code><i>column</i>]&#8230;] <code>find </code><i>table </i>[<i>column</i>[<code>:</code><i>key</i>]<code>=</code><i>value</i>]&#8230;</p>
<dd>Lists the data in each record in <i>table</i> whose <i>column</i> equals <i>value</i> or, if <i>key</i> is specified, whose <i>column</i> contains a <i>key</i> with the specified <i>value</i>. The following operators may be used where <code>=</code> is written in the syntax summary:</p>
<dl>
<dd>
<dl>
<dt><code>= != &lt; &gt; &lt;= &gt;=</code></p>
<dd>Selects records in which <i>column</i>[<code>:</code><i>key</i>] equals, does not equal, is less than, is greater than, is less than or equal to, or is greater than or equal to <i>value</i>, respectively.</p>
<dd>Consider <i>column</i>[<code>:</code><i>key</i>] and <i>value</i> as sets of elements. Identical sets are considered equal. Otherwise, if the sets have different numbers of elements, then the set with more elements is considered to be larger. Otherwise, consider a element from each set pairwise, in increasing order within each set. The first pair that differs determines the result. (For a column that contains key-value pairs, first all the keys are compared, and values are considered only if the two sets contain identical keys.)</p>
<dt><code>{=} {!=}</code></p>
<dd>Test for set equality or inequality, respectively.</p>
<dt><code>{&lt;=}</code></p>
<dd>Selects records in which <i>column</i>[<code>:</code><i>key</i>] is a subset of <i>value</i>. For example, <code>flood-vlans{&lt;=}1,2</code> selects records in which the <code>flood-vlans</code> column is the empty set or contains 1 or 2 or both.</p>
<dt><code>{&lt;}</code></p>
<dd>Selects records in which <i>column</i>[<code>:</code><i>key</i>] is a proper subset of <i>value</i>. For example, <code>flood-vlans{&lt;}1,2</code> selects records in which the <code>flood-vlans</code> column is the empty set or contains 1 or 2 but not both.</p>
<dt><code>{&gt;=} {&gt;}</code></p>
<dd>Same as <code>{&lt;=}</code> and <code>{&lt;}</code>, respectively, except that the relationship is reversed. For example, <code>flood-vlans{&gt;=}1,2</code> selects records in which the <code>flood-vlans</code> column contains both 1 and 2.</dl>
</dl>
<dd>For arithmetic operators (<code>= != &lt; &gt; &lt;= &gt;=</code>), when <i>key</i> is specified but a particular record&#8217;s <i>column</i> does not contain <i>key</i>, the record is always omitted from the results. Thus, the condition <code>other-config:mtu!=1500</code> matches records that have a <code>mtu</code> key whose value is not 1500, but not those that lack an <code>mtu</code> key.</p>
<dd>For the set operators, when <i>key</i> is specified but a particular record&#8217;s <i>column</i> does not contain <i>key</i>, the comparison is done against an empty set. Thus, the condition <code>other-config:mtu{!=}1500</code> matches records that have a <code>mtu</code> key whose value is not 1500 and those that lack an <code>mtu</code> key.</p>
<dd>Don&#8217;t forget to escape <code>&lt;</code> or <code>&gt;</code> from interpretation by the shell.</p>
<dd>If <code>&#8211;columns</code> is specified, only the requested columns are listed, in the specified order. Otherwise all columns are listed, in alphabetical order by column name.</p>
<dd>The UUIDs shown for rows created in the same <code>vtep-ctl</code> invocation will be wrong.</p>
<dt>[<code>&#8211;if-exists</code>] [<code>&#8211;id=@</code><i>name</i>] <code>get </code><i>table record </i>[<i>column</i>[<code>:</code><i>key</i>]]&#8230;</p>
<dd>Prints the value of each specified <i>column</i> in the given <i>record</i> in <i>table</i>. For map columns, a <i>key</i> may optionally be specified, in which case the value associated with <i>key</i> in the column is printed, instead of the entire map.</p>
<dd>Without <code>&#8211;if-exists</code>, it is an error if <i>record</i> does not exist or <i>key</i> is specified, if <i>key</i> does not exist in <i>record</i>. With <code>&#8211;if-exists</code>, a missing <i>record</i> yields no output and a missing <i>key</i> prints a blank line.</p>
<dd>If <code>@</code><i>name</i> is specified, then the UUID for <i>record</i> may be referred to by that name later in the same <code>vtep-ctl</code> invocation in contexts where a UUID is expected.</p>
<dd>Both <code>&#8211;id</code> and the <i>column</i> arguments are optional, but usually at least one or the other should be specified. If both are omitted, then <code>get</code> has no effect except to verify that <i>record</i> exists in <i>table</i>.</p>
<dd><code>&#8211;id</code> and <code>&#8211;if-exists</code> cannot be used together.</p>
<dt>[<code>&#8211;if-exists</code>] <code>set </code><i>table record column</i>[<code>:</code><i>key</i>]<code>=</code><i>value</i>&#8230;</p>
<dd>Sets the value of each specified <i>column</i> in the given <i>record</i> in <i>table</i> to <i>value</i>. For map columns, a <i>key</i> may optionally be specified, in which case the value associated with <i>key</i> in that column is changed (or added, if none exists), instead of the entire map.</p>
<dd>Without <code>&#8211;if-exists</code>, it is an error if <i>record</i> does not exist. With <code>&#8211;if-exists</code>, this command does nothing if <i>record</i> does not exist.</p>
<dt>[<code>&#8211;if-exists</code>] <code>add </code><i>table record column </i>[<i>key</i><code>=</code>]<i>value</i>&#8230;</p>
<dd>Adds the specified value or key-value pair to <i>column</i> in <i>record</i> in <i>table</i>. If <i>column</i> is a map, then <i>key</i> is required, otherwise it is prohibited. If <i>key</i> already exists in a map column, then the current <i>value</i> is not replaced (use the <code>set</code> command to replace an existing value).</p>
<dd>Without <code>&#8211;if-exists</code>, it is an error if <i>record</i> does not exist. With <code>&#8211;if-exists</code>, this command does nothing if <i>record</i> does not exist.</p>
<dt>[<code>&#8211;if-exists</code>] <code>remove </code><i>table record column </i><i>value</i>&#8230;</p>
<dd>
<dt>[<code>&#8211;if-exists</code>] <code>remove </code><i>table record column </i><i>key</i>&#8230;</p>
<dd>
<dt>[<code>&#8211;if-exists</code>] <code>remove </code><i>table record column </i><i>key</i><code>=</code><i>value</i>&#8230;</p>
<dd>Removes the specified values or key-value pairs from <i>column</i> in <i>record</i> in <i>table</i>. The first form applies to columns that are not maps: each specified <i>value</i> is removed from the column. The second and third forms apply to map columns: if only a <i>key</i> is specified, then any key-value pair with the given <i>key</i> is removed, regardless of its value; if a <i>value</i> is given then a pair is removed only if both key and value match.</p>
<dd>It is not an error if the column does not contain the specified key or value or pair.</p>
<dd>Without <code>&#8211;if-exists</code>, it is an error if <i>record</i> does not exist. With <code>&#8211;if-exists</code>, this command does nothing if <i>record</i> does not exist.</p>
<dt>[<code>&#8211;if-exists</code>] <code>clear</code> <i>table record column</i>&#8230;</p>
<dd>Sets each <i>column</i> in <i>record</i> in <i>table</i> to the empty set or empty map, as appropriate. This command applies only to columns that are allowed to be empty.</p>
<dd>Without <code>&#8211;if-exists</code>, it is an error if <i>record</i> does not exist. With <code>&#8211;if-exists</code>, this command does nothing if <i>record</i> does not exist.</p>
<dt>[<code>&#8211;id=@</code><i>name</i>] <code>create</code> <i>table column</i>[<code>:</code><i>key</i>]<code>=</code><i>value</i>&#8230;</p>
<dd>Creates a new record in <i>table</i> and sets the initial values of each <i>column</i>. Columns not explicitly set will receive their default values. Outputs the UUID of the new row.</p>
<dd>If <code>@</code><i>name</i> is specified, then the UUID for the new row may be referred to by that name elsewhere in the same <code>vtep-ctl</code> invocation in contexts where a UUID is expected. Such references may precede or follow the <code>create</code> command.</p>
<dl>
<dd>
<dl>
<dt>Caution (ovs-vsctl as exmaple)</p>
<dd>Records in the Open vSwitch database are significant only when they can be reached directly or indirectly from the <code>Open_vSwitch</code> table. Except for records in the <code>QoS</code> or <code>Queue</code> tables, records that are not reachable from the <code>Open_vSwitch</code> table are automatically deleted from the database. This deletion happens immediately, without waiting for additional <code>ovs-vsctl</code> commands or other database activity. Thus, a <code>create</code> command must generally be accompanied by additional commands <i>within the same </i><code>ovs-vsctl</code><i> invocation</i> to add a chain of references to the newly created record from the top-level <code>Open_vSwitch</code> record. The <code>EXAMPLES</code> section gives some examples that show how to do this.</dl>
</dl>
<dt>[<code>&#8211;if-exists</code>] <code>destroy </code><i>table record</i>&#8230;</p>
<dd>Deletes each specified <i>record</i> from <i>table</i>. Unless <code>&#8211;if-exists</code> is specified, each <i>record</i>s must exist.</p>
<dt><code>&#8211;all destroy </code><i>table</i></p>
<dd>Deletes all records from the <i>table</i>.</p>
<dl>
<dd>
<dl>
<dt>Caution (ovs-vsctl as exmaple)</p>
<dd>The <code>destroy</code> command is only useful for records in the <code>QoS</code> or <code>Queue</code> tables. Records in other tables are automatically deleted from the database when they become unreachable from the <code>Open_vSwitch</code> table. This means that deleting the last reference to a record is sufficient for deleting the record itself. For records in these tables, <code>destroy</code> is silently ignored. See the <code>EXAMPLES</code> section below for more information.</dl>
</dl>
<dt><code>wait-until </code><i>table record </i>[<i>column</i>[<code>:</code><i>key</i>]<code>=</code><i>value</i>]&#8230;</p>
<dd>Waits until <i>table</i> contains a record named <i>record</i> whose <i>column</i> equals <i>value</i> or, if <i>key</i> is specified, whose <i>column</i> contains a <i>key</i> with the specified <i>value</i>. Any of the operators <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, or <code>&gt;=</code> may be substituted for <code>=</code> to test for inequality, less than, greater than, less than or equal to, or greater than or equal to, respectively. (Don&#8217;t forget to escape <code>&lt;</code> or <code>&gt;</code> from interpretation by the shell.)</p>
<dd>If no <i>column</i>[<code>:</code><i>key</i>]<code>=</code><i>value</i> arguments are given, this command waits only until <i>record</i> exists. If more than one such argument is given, the command waits until all of them are satisfied.</p>
<dl>
<dd>
<dl>
<dt>Caution (ovs-vsctl as exmaple)</p>
<dd>Usually <code>wait-until</code> should be placed at the beginning of a set of <code>ovs-vsctl</code> commands. For example, <code>wait-until bridge br0 &#8212; get bridge br0 datapath_id</code> waits until a bridge named <code>br0</code> is created, then prints its <code>datapath_id</code> column, whereas <code>get bridge br0 datapath_id &#8212; wait-until bridge br0</code> will abort if no bridge named <code>br0</code> exists when <code>ovs-vsctl</code> initially connects to the database.</dl>
</dl>
<dd>Consider specifying <code>&#8211;timeout=0</code> along with <code>&#8211;wait-until</code>, to prevent <code>vtep-ctl</code> from terminating after waiting only at most 5 seconds.</p>
<dt><code>comment </code>[<i>arg</i>]&#8230;</p>
<dd>This command has no effect on behavior, but any database log record created by the command will include the command and its arguments.</dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd>Successful program execution.</p>
<dt>1</p>
<dd>Usage, syntax, or configuration file error.</p>
<dt>2</p>
<dd>The <i>switch</i> argument to <code>ps-exists</code> specified the name of a physical switch that does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ovsdb-server/">ovsdb-server</a></code>(1), <code><a href="/docs/linux/man/5-vtep/">vtep</a></code>(5). </p>
