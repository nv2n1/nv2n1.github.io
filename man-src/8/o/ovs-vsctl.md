---
title: "ovs-vsctl(8)"
name: "ovs-vsctl"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-vsctl/"
description: "ovs-vsctl – utility for querying and configuring ovs-vswitchd"
---

<p>ovs-vsctl &#8211; utility for querying and configuring <code>ovs-vswitchd</code></p>
<h2>Synopsis</h2>
<p><code>ovs-vsctl</code> [<i>options</i>] <code>&#8212;</code> [<i>options</i>] <i>command </i>[<i>args</i>] [<code>&#8212;</code> [<i>options</i>] <i>command </i>[<i>args</i>]]&#8230;</p>
<h2>Description</h2>
<p>The <code>ovs-vsctl</code> program configures <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8) by providing a high-level interface to its configuration database. See <code><a href="/docs/linux/man/5-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(5) for comprehensive documentation of the database schema. </p>
<p> <code>ovs-vsctl</code> connects to an <code>ovsdb-server</code> process that maintains an Open vSwitch configuration database. Using this connection, it queries and possibly applies changes to the database, depending on the supplied commands. Then, if it applied any changes, by default it waits until <code>ovs-vswitchd</code> has finished reconfiguring itself before it exits. (If you use <code>ovs-vsctl</code> when <code>ovs-vswitchd</code> is not running, use <code>&#8211;no-wait</code>.) </p>
<p> <code>ovs-vsctl</code> can perform any number of commands in a single run, implemented as a single atomic transaction against the database. </p>
<p> The <code>ovs-vsctl</code> command line begins with global options (see <code>OPTIONS</code> below for details). The global options are followed by one or more commands. Each command should begin with <code>&#8212;</code> by itself as a command-line argument, to separate it from the following commands. (The <code>&#8212;</code> before the first command is optional.) The command itself starts with command-specific options, if any, followed by the command name and any arguments. See <code>EXAMPLES</code> below for syntax examples.</p>
<h3>Linux VLAN Bridging Compatibility</h3>
<p>The <code>ovs-vsctl</code> program supports the model of a bridge implemented by Open vSwitch, in which a single bridge supports ports on multiple VLANs. In this model, each port on a bridge is either a trunk port that potentially passes packets tagged with 802.1Q headers that designate VLANs or it is assigned a single implicit VLAN that is never tagged with an 802.1Q header. </p>
<p> For compatibility with software designed for the Linux bridge, <code>ovs-vsctl</code> also supports a model in which traffic associated with a given 802.1Q VLAN is segregated into a separate bridge. A special form of the <code>add-br</code> command (see below) creates a &#8220;fake bridge&#8221; within an Open vSwitch bridge to simulate this behavior. When such a &#8220;fake bridge&#8221; is active, <code>ovs-vsctl</code> will treat it much like a bridge separate from its &#8220;parent bridge,&#8221; but the actual implementation in Open vSwitch uses only a single bridge, with ports on the fake bridge assigned the implicit VLAN of the fake bridge of which they are members. (A fake bridge for VLAN 0 receives packets that have no 802.1Q tag or a tag with VLAN 0.)</p>
<h2>Options</h2>
<p>The following options affect the behavior <code>ovs-vsctl</code> as a whole. Some individual commands also accept their own options, which are given just before the command name. If the first command on the command line has options, then those options must be separated from the global options by <code>&#8212;</code>.</p>
<dl>
<dt><code>&#8211;db=</code><i>server</i></p>
<dd>Sets <i>server</i> as the database server that <code>ovs-vsctl</code> contacts to query or modify configuration. The default is <code>unix:/var/run/openvswitch/db.sock</code>. <i>server</i> must take one of the following forms:</p>
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
<dt><code>&#8211;no-wait</code></p>
<dd>Prevents <code>ovs-vsctl</code> from waiting for <code>ovs-vswitchd</code> to reconfigure itself according to the modified database. This option should be used if <code>ovs-vswitchd</code> is not running; otherwise, <code>ovs-vsctl</code> will not exit until <code>ovs-vswitchd</code> starts.</p>
<dd>This option has no effect if the commands specified do not change the database.</p>
<dt><code>&#8211;no-syslog</code></p>
<dd>By default, <code>ovs-vsctl</code> logs its arguments and the details of any changes that it makes to the system log. This option disables this logging.</p>
<dd>This option is equivalent to <code>&#8211;verbose=vsctl:syslog:warn</code>.</p>
<dt><code>&#8211;oneline</code></p>
<dd>Modifies the output format so that the output for each command is printed on a single line. New-line characters that would otherwise separate lines are printed as <code>
</code>, and any instances of <code>\</code> that would otherwise appear in the output are doubled. Prints a blank line for each command that has no output. This option does not affect the formatting of output from the <code>list</code> or <code>find</code> commands; see <code>Table Formatting Options</code> below.</p>
<dt><code>&#8211;dry-run</code></p>
<dd>Prevents <code>ovs-vsctl</code> from actually modifying the database.</p>
<dt><code>-t </code><i>secs</i></p>
<dd>
<dt><code>&#8211;timeout=</code><i>secs</i></p>
<dd>By default, or with a <i>secs</i> of <code>0</code>, <code>ovs-vsctl</code> waits forever for a response from the database. This option limits runtime to approximately <i>secs</i> seconds. If the timeout expires, <code>ovs-vsctl</code> will exit with a <code>SIGALRM</code> signal. (A timeout would normally happen only if the database cannot be contacted, or if the system is overloaded.)</p>
<dt><code>&#8211;retry</code></p>
<dd>Without this option, if <code>ovs-vsctl</code> connects outward to the database server (the default) then <code>ovs-vsctl</code> will try to connect once and exit with an error if the connection fails (which usually means that <code>ovsdb-server</code> is not running).</p>
<dd>With this option, or if <code>&#8211;db</code> specifies that <code>ovs-vsctl</code> should listen for an incoming connection from the database server, then <code>ovs-vsctl</code> will wait for a connection to the database forever.</p>
<dd>Regardless of this setting, <code>&#8211;timeout</code> always limits how long <code>ovs-vsctl</code> will wait.</dl>
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
<dt><code>table</code></p>
<dd>2-D text tables with aligned columns.</p>
<dt><code>list</code> (default)</p>
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
<dd>The simple format described in the <code>Database Values</code> section below.</p>
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
<dd>Specifies a PEM file containing the private key used as <code>ovs-vsctl</code>&#8216;s identity for outgoing SSL connections.</p>
<dt><code>-c</code> <i>cert.pem</i></p>
<dd>
<dt><code>&#8211;certificate=</code><i>cert.pem</i></p>
<dd>Specifies a PEM file containing a certificate that certifies the private key specified on <code>-p</code> or <code>&#8211;private-key</code> to be trustworthy. The certificate must be signed by the certificate authority (CA) that the peer in SSL connections will use to verify it.</p>
<dt><code>-C</code> <i>cacert.pem</i></p>
<dd>
<dt><code>&#8211;ca-cert=</code><i>cacert.pem</i></p>
<dd>Specifies a PEM file containing the CA certificate that <code>ovs-vsctl</code> should use to verify certificates presented to it by SSL peers. (This may be the same certificate that SSL peers use to verify the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>, or it may be a different one, depending on the PKI design in use.)</p>
<dt><code>-C none</code></p>
<dd>
<dt><code>&#8211;ca-cert=none</code></p>
<dd>Disables verification of certificates presented by SSL peers. This introduces a security risk, because it means that certificates cannot be verified to be those of known trusted hosts.</p>
<dt><code>&#8211;bootstrap-ca-cert=</code><i>cacert.pem</i></p>
<dd>When <i>cacert.pem</i> exists, this option has the same effect as <code>-C</code> or <code>&#8211;ca-cert</code>. If it does not exist, then <code>ovs-vsctl</code> will attempt to obtain the CA certificate from the SSL peer on its first SSL connection and save it to the named PEM file. If it is successful, it will immediately drop the connection and reconnect, and from then on all SSL connections must be authenticated by a certificate signed by the CA certificate thus obtained.</p>
<dd><code>This option exposes the SSL connection to a man-in-the-middle attack obtaining the initial CA certificate</code>, but it may be useful for bootstrapping.</p>
<dd>This option is only useful if the SSL peer sends its CA certificate as part of the SSL certificate chain. The SSL protocol does not require the server to send the CA certificate.</p>
<dd>This option is mutually exclusive with <code>-C</code> and <code>&#8211;ca-cert</code>.</p>
<dt><code>&#8211;peer-ca-cert=</code><i>peer-cacert.pem</i></p>
<dd>Specifies a PEM file that contains one or more additional certificates to send to SSL peers. <i>peer-cacert.pem</i> should be the CA certificate used to sign <code>ovs-vsctl</code>&#8216;s own certificate, that is, the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>. If <code>ovs-vsctl</code>&#8216;s certificate is self-signed, then <code>&#8211;certificate</code> and <code>&#8211;peer-ca-cert</code> should specify the same file.</p>
<dd>This option is not useful in normal operation, because the SSL peer must already have the CA certificate for the peer to have any confidence in <code>ovs-vsctl</code>&#8216;s identity. However, this offers a way for a new installation to bootstrap the CA certificate on its first SSL connection.</p>
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
<dd><code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively. (If <code>&#8211;detach</code> is specified, <code>ovs-vsctl</code> closes its standard file descriptors, so logging to the console will have no effect.)</p>
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
<dd>Enables logging to a file. If <i>file</i> is specified, then it is used as the exact name for the log file. The default log file name used if <i>file</i> is omitted is <code>/var/log/openvswitch/ovs-vsctl.log</code>.</p>
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
<p>The commands implemented by <code>ovs-vsctl</code> are described in the sections below.</p>
<h3>Open vSwitch Commands</h3>
<p>These commands work with an Open vSwitch as a whole.</p>
<dl>
<dt><code>init</code></p>
<dd>Initializes the Open vSwitch database, if it is empty. If the database has already been initialized, this command has no effect.</p>
<dd>Any successful <code>ovs-vsctl</code> command automatically initializes the Open vSwitch database if it is empty. This command is provided to initialize the database without executing any other command.</p>
<dt><code>show</code></p>
<dd>Prints a brief overview of the database contents.</p>
<dt><code>emer-reset</code></p>
<dd>Reset the configuration into a clean state. It deconfigures OpenFlow controllers, OVSDB servers, and SSL, and deletes port mirroring, <code>fail_mode</code>, NetFlow, sFlow, and IPFIX configuration. This command also removes all <code>other-config</code> keys from all database records, except that <code>other-config:hwaddr</code> is preserved if it is present in a Bridge record. Other networking configuration is left as-is.</dl>
<h3>Bridge Commands</h3>
<p>These commands examine and manipulate Open vSwitch bridges.</p>
<dl>
<dt>[<code>&#8211;may-exist</code>] <code>add-br </code><i>bridge</i></p>
<dd>Creates a new bridge named <i>bridge</i>. Initially the bridge will have no ports (other than <i>bridge</i> itself).</p>
<dd>Without <code>&#8211;may-exist</code>, attempting to create a bridge that exists is an error. With <code>&#8211;may-exist</code>, this command does nothing if <i>bridge</i> already exists as a real bridge.</p>
<dt>[<code>&#8211;may-exist</code>] <code>add-br </code><i>bridge parent vlan</i></p>
<dd>Creates a &#8220;fake bridge&#8221; named <i>bridge</i> within the existing Open vSwitch bridge <i>parent</i>, which must already exist and must not itself be a fake bridge. The new fake bridge will be on 802.1Q VLAN <i>vlan</i>, which must be an integer between 0 and 4095. The parent bridge must not already have a fake bridge for <i>vlan</i>. Initially <i>bridge</i> will have no ports (other than <i>bridge</i> itself).</p>
<dd>Without <code>&#8211;may-exist</code>, attempting to create a bridge that exists is an error. With <code>&#8211;may-exist</code>, this command does nothing if <i>bridge</i> already exists as a VLAN bridge under <i>parent</i> for <i>vlan</i>.</p>
<dt>[<code>&#8211;if-exists</code>] <code>del-br </code><i>bridge</i></p>
<dd>Deletes <i>bridge</i> and all of its ports. If <i>bridge</i> is a real bridge, this command also deletes any fake bridges that were created with <i>bridge</i> as parent, including all of their ports.</p>
<dd>Without <code>&#8211;if-exists</code>, attempting to delete a bridge that does not exist is an error. With <code>&#8211;if-exists</code>, attempting to delete a bridge that does not exist has no effect.</p>
<dt>[<code>&#8211;real</code>|<code>&#8211;fake</code>] <code>list-br</code></p>
<dd>Lists all existing real and fake bridges on standard output, one per line. With <code>&#8211;real</code> or <code>&#8211;fake</code>, only bridges of that type are returned.</p>
<dt><code>br-exists </code><i>bridge</i></p>
<dd>Tests whether <i>bridge</i> exists as a real or fake bridge. If so, <code>ovs-vsctl</code> exits successfully with exit code 0. If not, <code>ovs-vsctl</code> exits unsuccessfully with exit code 2.</p>
<dt><code>br-to-vlan </code><i>bridge</i></p>
<dd>If <i>bridge</i> is a fake bridge, prints the bridge&#8217;s 802.1Q VLAN as a decimal integer. If <i>bridge</i> is a real bridge, prints 0.</p>
<dt><code>br-to-parent </code><i>bridge</i></p>
<dd>If <i>bridge</i> is a fake bridge, prints the name of its parent bridge. If <i>bridge</i> is a real bridge, print <i>bridge</i>.</p>
<dt><code>br-set-external-id </code><i>bridge key</i> [<i>value</i>]</p>
<dd>Sets or clears an &#8220;external ID&#8221; value on <i>bridge</i>. These values are intended to identify entities external to Open vSwitch with which <i>bridge</i> is associated, e.g. the bridge&#8217;s identifier in a virtualization management platform. The Open vSwitch database schema specifies well-known <i>key</i> values, but <i>key</i> and <i>value</i> are otherwise arbitrary strings.</p>
<dd>If <i>value</i> is specified, then <i>key</i> is set to <i>value</i> for <i>bridge</i>, overwriting any previous value. If <i>value</i> is omitted, then <i>key</i> is removed from <i>bridge</i>&#8216;s set of external IDs (if it was present).</p>
<dd>For real bridges, the effect of this command is similar to that of a <code>set</code> or <code>remove</code> command in the <code>external-ids</code> column of the <code>Bridge</code> table. For fake bridges, it actually modifies keys with names prefixed by <code>fake-bridge-</code> in the <code>Port</code> table.</p>
<dt><code>br-get-external-id </code><i>bridge</i> [<i>key</i>]</p>
<dd>Queries the external IDs on <i>bridge</i>. If <i>key</i> is specified, the output is the value for that <i>key</i> or the empty string if <i>key</i> is unset. If <i>key</i> is omitted, the output is <i>key</i><code>=</code><i>value</i>, one per line, for each key-value pair.</p>
<dd>For real bridges, the effect of this command is similar to that of a <code>get</code> command in the <code>external-ids</code> column of the <code>Bridge</code> table. For fake bridges, it queries keys with names prefixed by <code>fake-bridge-</code> in the <code>Port</code> table.</dl>
<h3>Port Commands</h3>
<p>These commands examine and manipulate Open vSwitch ports. These commands treat a bonded port as a single entity.</p>
<dl>
<dt><code>list-ports </code><i>bridge</i></p>
<dd>Lists all of the ports within <i>bridge</i> on standard output, one per line. The local port <i>bridge</i> is not included in the list.</p>
<dt>[<code>&#8211;may-exist</code>] <code>add-port </code><i>bridge port </i>[<i>column</i>[<code>:</code><i>key</i>]=<i>value</i>]&#8230;</p>
<dd>Creates on <i>bridge</i> a new port named <i>port</i> from the network device of the same name.</p>
<dd>Optional arguments set values of column in the Port record created by the command. For example, <code>tag=9</code> would make the port an access port for VLAN 9. The syntax is the same as that for the <code>set</code> command (see <code>Database Commands</code> below).</p>
<dd>Without <code>&#8211;may-exist</code>, attempting to create a port that exists is an error. With <code>&#8211;may-exist</code>, this command does nothing if <i>port</i> already exists on <i>bridge</i> and is not a bonded port.</p>
<dt>[<code>&#8211;fake-iface</code>] <code>add-bond </code><i>bridge port iface</i>&#8230; [<i>column</i>[<code>:</code><i>key</i>]=<i>value</i>]&#8230;</p>
<dd>Creates on <i>bridge</i> a new port named <i>port</i> that bonds together the network devices given as each <i>iface</i>. At least two interfaces must be named. If the interfaces are DPDK enabled then the transaction will need to include operations to explicitly set the interface type to &#8216;dpdk&#8217;.</p>
<dd>Optional arguments set values of column in the Port record created by the command. The syntax is the same as that for the <code>set</code> command (see <code>Database Commands</code> below).</p>
<dd>With <code>&#8211;fake-iface</code>, a fake interface with the name <i>port</i> is created. This should only be used for compatibility with legacy software that requires it.</p>
<dd>Without <code>&#8211;may-exist</code>, attempting to create a port that exists is an error. With <code>&#8211;may-exist</code>, this command does nothing if <i>port</i> already exists on <i>bridge</i> and bonds together exactly the specified interfaces.</p>
<dt>[<code>&#8211;if-exists</code>] <code>del-port </code>[<i>bridge</i>] <i>port</i></p>
<dd>Deletes <i>port</i>. If <i>bridge</i> is omitted, <i>port</i> is removed from whatever bridge contains it; if <i>bridge</i> is specified, it must be the real or fake bridge that contains <i>port</i>.</p>
<dd>Without <code>&#8211;if-exists</code>, attempting to delete a port that does not exist is an error. With <code>&#8211;if-exists</code>, attempting to delete a port that does not exist has no effect.</p>
<dt>[<code>&#8211;if-exists</code>] <code>&#8211;with-iface del-port </code>[<i>bridge</i>] <i>iface</i></p>
<dd>Deletes the port named <i>iface</i> or that has an interface named <i>iface</i>. If <i>bridge</i> is omitted, the port is removed from whatever bridge contains it; if <i>bridge</i> is specified, it must be the real or fake bridge that contains the port.</p>
<dd>Without <code>&#8211;if-exists</code>, attempting to delete the port for an interface that does not exist is an error. With <code>&#8211;if-exists</code>, attempting to delete the port for an interface that does not exist has no effect.</p>
<dt><code>port-to-br </code><i>port</i></p>
<dd>Prints the name of the bridge that contains <i>port</i> on standard output.</dl>
<h3>Interface Commands</h3>
<p>These commands examine the interfaces attached to an Open vSwitch bridge. These commands treat a bonded port as a collection of two or more interfaces, rather than as a single port.</p>
<dl>
<dt><code>list-ifaces </code><i>bridge</i></p>
<dd>Lists all of the interfaces within <i>bridge</i> on standard output, one per line. The local port <i>bridge</i> is not included in the list.</p>
<dt><code>iface-to-br </code><i>iface</i></p>
<dd>Prints the name of the bridge that contains <i>iface</i> on standard output.</dl>
<h3>OpenFlow Controller Connectivity</h3>
<p><code>ovs-vswitchd</code> can perform all configured bridging and switching locally, or it can be configured to communicate with one or more external OpenFlow controllers. The switch is typically configured to connect to a primary controller that takes charge of the bridge&#8217;s flow table to implement a network policy. In addition, the switch can be configured to listen to connections from service controllers. Service controllers are typically used for occasional support and maintenance, e.g. with <code>ovs-ofctl</code>.</p>
<dl>
<dt><code>get-controller</code> <i>bridge</i></p>
<dd>Prints the configured controller target.</p>
<dt><code>del-controller</code> <i>bridge</i></p>
<dd>Deletes the configured controller target.</p>
<dt><code>set-controller</code> <i>bridge</i> <i>target</i>&#8230;</p>
<dd>Sets the configured controller target or targets. Each <i>target</i> may use any of the following forms:</p>
<dl>
<dd>
<dl>
<dt><code>ssl:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>
<dt><code>tcp:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name) in IPv4 or IPv6 address format. Wrap IPv6 addresses in square brackets, e.g. <code>tcp:[::1]:6653</code>. For <code>ssl</code>, the <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory.</p>
<dd>If <i>port</i> is not specified, it defaults to 6653.</p>
<dt><code>unix:</code><i>file</i></p>
<dd>On POSIX, a Unix domain server socket named <i>file</i>.</p>
<dd>On Windows, a localhost TCP port written in <i>file</i>.</p>
<dt><code>pssl:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>
<dt><code>ptcp:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>Listens for OpenFlow connections on <i>port</i>. The default <i>port</i> is 6653. By default, connections are allowed from any IPv4 address. Specify <i>ip</i> as an IPv4 address or a bracketed IPv6 address (e.g. <code>ptcp:6653:[::1]</code>). DNS names may not be used. For <code>pssl</code>, the <code>&#8211;private-key</code>,<code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory.</p>
<dd>
<dt><code>punix:</code><i>file</i></p>
<dd>Listens for OpenFlow connections on the Unix domain server socket named <i>file</i>.</dl>
</dl>
</dl>
<p> <i>Controller Failure Settings</i> </p>
<p> When a controller is configured, it is, ordinarily, responsible for setting up all flows on the switch. Thus, if the connection to the controller fails, no new network connections can be set up. If the connection to the controller stays down long enough, no packets can pass through the switch at all. </p>
<p> If the value is <code>standalone</code>, or if neither of these settings is set, <code>ovs-vswitchd</code> will take over responsibility for setting up flows when no message has been received from the controller for three times the inactivity probe interval. In this mode, <code>ovs-vswitchd</code> causes the datapath to act like an ordinary MAC-learning switch. <code>ovs-vswitchd</code> will continue to retry connecting to the controller in the background and, when the connection succeeds, it discontinues its standalone behavior. </p>
<p> If this option is set to <code>secure</code>, <code>ovs-vswitchd</code> will not set up flows on its own when the controller connection fails.</p>
<dl>
<dt><code>get-fail-mode</code> <i>bridge</i></p>
<dd>Prints the configured failure mode.</p>
<dt><code>del-fail-mode</code> <i>bridge</i></p>
<dd>Deletes the configured failure mode.</p>
<dt><code>set-fail-mode</code> <i>bridge</i> <code>standalone</code>|<code>secure</code></p>
<dd>Sets the configured failure mode.</dl>
<h3>Manager Connectivity</h3>
<p>These commands manipulate the <code>manager_options</code> column in the <code>Open_vSwitch</code> table and rows in the <code>Managers</code> table. When <code>ovsdb-server</code> is configured to use the <code>manager_options</code> column for OVSDB connections (as described in <code>INSTALL.Linux</code> and in the startup scripts provided with Open vSwitch), this allows the administrator to use <code>ovs-vsctl</code> to configure database connections.</p>
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
<h3>SSL Configuration</h3>
<p>When <code>ovs-vswitchd</code> is configured to connect over SSL for management or controller connectivity, the following parameters are required:</p>
<dl>
<dt><i>private-key</i></p>
<dd>Specifies a PEM file containing the private key used as the virtual switch&#8217;s identity for SSL connections to the controller.</p>
<dt><i>certificate</i></p>
<dd>Specifies a PEM file containing a certificate, signed by the certificate authority (CA) used by the controller and manager, that certifies the virtual switch&#8217;s private key, identifying a trustworthy switch.</p>
<dt><i>ca-cert</i></p>
<dd>Specifies a PEM file containing the CA certificate used to verify that the virtual switch is connected to a trustworthy controller.</dl>
<p> These files are read only once, at <code>ovs-vswitchd</code> startup time. If their contents change, <code>ovs-vswitchd</code> must be killed and restarted. </p>
<p> These SSL settings apply to all SSL connections made by the virtual switch.</p>
<dl>
<dt><code>get-ssl</code></p>
<dd>Prints the SSL configuration.</p>
<dt><code>del-ssl</code></p>
<dd>Deletes the current SSL configuration.</p>
<dt>[<code>&#8211;bootstrap</code>] <code>set-ssl</code> <i>private-key</i> <i>certificate</i> <i>ca-cert</i></p>
<dd>Sets the SSL configuration. The <code>&#8211;bootstrap</code> option is described below.</dl>
<p> <i>CA Certificate Bootstrap</i> </p>
<p> Ordinarily, all of the files named in the SSL configuration must exist when <code>ovs-vswitchd</code> starts. However, if the <i>ca-cert</i> file does not exist and the <code>&#8211;bootstrap</code> option is given, then <code>ovs-vswitchd</code> will attempt to obtain the CA certificate from the controller on its first SSL connection and save it to the named PEM file. If it is successful, it will immediately drop the connection and reconnect, and from then on all SSL connections must be authenticated by a certificate signed by the CA certificate thus obtained. </p>
<p> <code>This option exposes the SSL connection to a man-in-the-middle attack obtaining the initial CA certificate</code>, but it may be useful for bootstrapping. </p>
<p> This option is only useful if the controller sends its CA certificate as part of the SSL certificate chain. The SSL protocol does not require the controller to send the CA certificate.</p>
<h3>Auto-Attach Commands</h3>
<p>The IETF Auto-Attach SPBM draft standard describes a compact method of using IEEE 802.1AB Link Layer Discovery Protocol (LLDP) together with a IEEE 802.1aq Shortest Path Bridging (SPB) network to automatically attach network devices to individual services in a SPB network. The intent here is to allow network applications and devices using OVS to be able to easily take advantage of features offered by industry standard SPB networks. A fundamental element of the Auto-Attach feature is to map traditional VLANs onto SPB I_SIDs. These commands manage the Auto-Attach I-SID/VLAN mappings.</p>
<dl>
<dt><code>add-aa-mapping </code><i>bridge i-sid vlan</i></p>
<dd>Creates a new Auto-Attach mapping on <i>bridge</i> for <i>i-sid</i> and <i>vlan</i>.</p>
<dt><code>del-aa-mapping </code><i>bridge i-sid vlan</i></p>
<dd>Deletes an Auto-Attach mapping on <i>bridge</i> for <i>i-sid</i> and <i>vlan</i>.</p>
<dt><code>get-aa-mapping </code><i>bridge</i></p>
<dd>Lists all of the Auto-Attach mappings within <i>bridge</i> on standard output.</dl>
<h3>Database Commands</h3>
<p>These commands query and modify the contents of <code>ovsdb</code> tables. They are a slight abstraction of the <code>ovsdb</code> interface and as such they operate at a lower level than other <code>ovs-vsctl</code> commands. </p>
<p> <i>Identifying Tables, Records, and Columns</i> </p>
<p> Each of these commands has a <i>table</i> parameter to identify a table within the database. Many of them also take a <i>record</i> parameter that identifies a particular record within a table. The <i>record</i> parameter may be the UUID for a record, and many tables offer additional ways to identify records. Some commands also take <i>column</i> parameters that identify a particular field within the records in a table. </p>
<p> The following tables are currently defined:</p>
<dl>
<dt><code>Open_vSwitch</code></p>
<dd>Global configuration for an <code>ovs-vswitchd</code>. This table contains exactly one record, identified by specifying <code>.</code> as the record name.</p>
<dt><code>Bridge</code></p>
<dd>Configuration for a bridge within an Open vSwitch. Records may be identified by bridge name.</p>
<dt><code>Port</code></p>
<dd>A bridge port. Records may be identified by port name.</p>
<dt><code>Interface</code></p>
<dd>A network device attached to a port. Records may be identified by name.</p>
<dt><code>Flow_Table</code></p>
<dd>Configuration for a particular OpenFlow flow table. Records may be identified by name.</p>
<dt><code>QoS</code></p>
<dd>Quality-of-service configuration for a <code>Port</code>. Records may be identified by port name.</p>
<dt><code>Queue</code></p>
<dd>Configuration for one queue within a <code>QoS</code> configuration. Records may only be identified by UUID.</p>
<dt><code>Mirror</code></p>
<dd>A port mirroring configuration attached to a bridge. Records may be identified by mirror name.</p>
<dt><code>Controller</code></p>
<dd>Configuration for an OpenFlow controller. A controller attached to a particular bridge may be identified by the bridge&#8217;s name.</p>
<dt><code>Manager</code></p>
<dd>Configuration for an OVSDB connection. Records may be identified by target (e.g. <code>tcp:1.2.3.4</code>).</p>
<dt><code>NetFlow</code></p>
<dd>A NetFlow configuration attached to a bridge. Records may be identified by bridge name.</p>
<dt><code>SSL</code></p>
<dd>The global SSL configuration for <code>ovs-vswitchd</code>. The record attached to the <code>Open_vSwitch</code> table may be identified by specifying <code>.</code> as the record name.</p>
<dt><code>sFlow</code></p>
<dd>An sFlow exporter configuration attached to a bridge. Records may be identified by bridge name.</p>
<dt><code>IPFIX</code></p>
<dd>An IPFIX exporter configuration attached to a bridge. Records may be identified by bridge name.</p>
<dt><code>Flow_Sample_Collector_Set</code></p>
<dd>An IPFIX exporter configuration attached to a bridge for sampling packets on a per-flow basis using OpenFlow <code>sample</code> actions.</p>
<dt><code>AutoAttach</code></p>
<dd>Configuration for Auto Attach within a bridge.</dl>
<p> Record names must be specified in full and with correct capitalization. Names of tables and columns are not case-sensitive, and <code>&#8212;</code> and <code>_</code> are treated interchangeably. Unique abbreviations are acceptable, e.g. <code>net</code> or <code>n</code> is sufficient to identify the <code>NetFlow</code> table. </p>
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
<dd>Either a universally unique identifier in the style of RFC 4122, e.g. <code>f81d4fae-7dec-11d0-a765-00a0c91e6bf6</code>, or an <code>@</code><i>name</i> defined by a <code>get</code> or <code>create</code> command within the same <code>ovs-vsctl</code> invocation.</dl>
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
<dd>The UUIDs shown for rows created in the same <code>ovs-vsctl</code> invocation will be wrong.</p>
<dt>[<code>&#8211;if-exists</code>] [<code>&#8211;id=@</code><i>name</i>] <code>get </code><i>table record </i>[<i>column</i>[<code>:</code><i>key</i>]]&#8230;</p>
<dd>Prints the value of each specified <i>column</i> in the given <i>record</i> in <i>table</i>. For map columns, a <i>key</i> may optionally be specified, in which case the value associated with <i>key</i> in the column is printed, instead of the entire map.</p>
<dd>Without <code>&#8211;if-exists</code>, it is an error if <i>record</i> does not exist or <i>key</i> is specified, if <i>key</i> does not exist in <i>record</i>. With <code>&#8211;if-exists</code>, a missing <i>record</i> yields no output and a missing <i>key</i> prints a blank line.</p>
<dd>If <code>@</code><i>name</i> is specified, then the UUID for <i>record</i> may be referred to by that name later in the same <code>ovs-vsctl</code> invocation in contexts where a UUID is expected.</p>
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
<dd>If <code>@</code><i>name</i> is specified, then the UUID for the new row may be referred to by that name elsewhere in the same <code>ovs-vsctl</code> invocation in contexts where a UUID is expected. Such references may precede or follow the <code>create</code> command.</p>
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
<dd>Consider specifying <code>&#8211;timeout=0</code> along with <code>&#8211;wait-until</code>, to prevent <code>ovs-vsctl</code> from terminating after waiting only at most 5 seconds.</p>
<dt><code>comment </code>[<i>arg</i>]&#8230;</p>
<dd>This command has no effect on behavior, but any database log record created by the command will include the command and its arguments.</dl>
<h2>Examples</h2>
<p>Create a new bridge named br0 and add port eth0 to it:</p>
<dl>
<dd><code>ovs-vsctl add-br br0</code><br />
 <code>ovs-vsctl add-port br0 eth0</code></dl>
<p> Alternatively, perform both operations in a single atomic transaction:</p>
<dl>
<dd><code>ovs-vsctl add-br br0 &#8212; add-port br0 eth0</code></dl>
<p> Delete bridge <code>br0</code>, reporting an error if it does not exist:</p>
<dl>
<dd><code>ovs-vsctl del-br br0</code></dl>
<p> Delete bridge <code>br0</code> if it exists:</p>
<dl>
<dd><code>ovs-vsctl &#8211;if-exists del-br br0</code></dl>
<p> Set the <code>qos</code> column of the <code>Port</code> record for <code>eth0</code> to point to a new <code>QoS</code> record, which in turn points with its queue 0 to a new <code>Queue</code> record:</p>
<dl>
<dd><code>ovs-vsctl &#8212; set port eth0 qos=@newqos &#8212; &#8211;id=@newqos create qos type=linux-htb other-config:max-rate=1000000 queues:0=@newqueue &#8212; &#8211;id=@newqueue create queue other-config:min-rate=1000000 other-config:max-rate=1000000</code></dl>
<h2>Configuration Cookbook</h2>
<h3>Port Configuration</h3>
<p>Add an &#8220;internal port&#8221; <code>vlan10</code> to bridge <code>br0</code> as a VLAN access port for VLAN 10, and configure it with an IP address:</p>
<dl>
<dd><code>ovs-vsctl add-port br0 vlan10 tag=10 &#8212; set Interface vlan10 type=internal</code></p>
<dd><code>ifconfig vlan10 192.168.0.123</code></dl>
<p> Add a GRE tunnel port <code>gre0</code> to remote IP address 1.2.3.4 to bridge <code>br0</code>:</p>
<dl>
<dd><code>ovs-vsctl add-port br0 gre0 &#8212; set Interface gre0 type=gre options:remote_ip=1.2.3.4</code></dl>
<h3>Port Mirroring</h3>
<p>Mirror all packets received or sent on <code>eth0</code> or <code>eth1</code> onto <code>eth2</code>, assuming that all of those ports exist on bridge <code>br0</code> (as a side-effect this causes any packets received on <code>eth2</code> to be ignored):</p>
<dl>
<dd><code>ovs-vsctl &#8212; set Bridge br0 mirrors=@m \</code></p>
<dd><code>&#8212; &#8211;id=@eth0 get Port eth0 \</code></p>
<dd><code>&#8212; &#8211;id=@eth1 get Port eth1 \</code></p>
<dd><code>&#8212; &#8211;id=@eth2 get Port eth2 \</code></p>
<dd><code>&#8212; &#8211;id=@m create Mirror name=mymirror select-dst-port=@eth0,@eth1 select-src-port=@eth0,@eth1 output-port=@eth2</code></dl>
<p> Remove the mirror created above from <code>br0</code>, which also destroys the Mirror record (since it is now unreferenced):</p>
<dl>
<dd><code>ovs-vsctl &#8212; &#8211;id=@rec get Mirror mymirror \</code></p>
<dd><code>&#8212; remove Bridge br0 mirrors @rec</code></dl>
<p> The following simpler command also works:</p>
<dl>
<dd><code>ovs-vsctl clear Bridge br0 mirrors</code></dl>
<h3>Quality of Service (QoS)</h3>
<p>Create a <code>linux-htb</code> QoS record that points to a few queues and use it on <code>eth0</code> and <code>eth1</code>:</p>
<dl>
<dd><code>ovs-vsctl &#8212; set Port eth0 qos=@newqos \</code></p>
<dd><code>&#8212; set Port eth1 qos=@newqos \</code></p>
<dd><code>&#8212; &#8211;id=@newqos create QoS type=linux-htb other-config:max-rate=1000000000 queues=0=@q0,1=@q1 \</code></p>
<dd><code>&#8212; &#8211;id=@q0 create Queue other-config:min-rate=100000000 other-config:max-rate=100000000 \</code></p>
<dd><code>&#8212; &#8211;id=@q1 create Queue other-config:min-rate=500000000</code></dl>
<p> Deconfigure the QoS record above from <code>eth1</code> only:</p>
<dl>
<dd><code>ovs-vsctl clear Port eth1 qos</code></dl>
<p> To deconfigure the QoS record from both <code>eth0</code> and <code>eth1</code> and then delete the QoS record (which must be done explicitly because unreferenced QoS records are not automatically destroyed):</p>
<dl>
<dd><code>ovs-vsctl &#8212; destroy QoS eth0 &#8212; clear Port eth0 qos &#8212; clear Port eth1 qos</code></dl>
<p> (This command will leave two unreferenced Queue records in the database. To delete them, use &quot;<code>ovs-vsctl list Queue</code>&quot; to find their UUIDs, then &quot;<code>ovs-vsctl destroy Queue </code><i>uuid1</i> <i>uuid2</i>&quot; to destroy each of them or use &quot;<code>ovs-vsctl &#8212; &#8211;all destroy Queue</code>&quot; to delete all records.)</p>
<h3>Connectivity Monitoring</h3>
<p>Monitor connectivity to a remote maintenance point on eth0.</p>
<dl>
<dd><code>ovs-vsctl set Interface eth0 cfm_mpid=1</code></dl>
<p> Deconfigure connectivity monitoring from above:</p>
<dl>
<dd><code>ovs-vsctl clear Interface eth0 cfm_mpid</code></dl>
<h3>NetFlow</h3>
<p>Configure bridge <code>br0</code> to send NetFlow records to UDP port 5566 on host 192.168.0.34, with an active timeout of 30 seconds:</p>
<dl>
<dd><code>ovs-vsctl &#8212; set Bridge br0 netflow=@nf \</code></p>
<dd><code>&#8212; &#8211;id=@nf create NetFlow targets=\&quot;192.168.0.34:5566\&quot; active-timeout=30</code></dl>
<p> Update the NetFlow configuration created by the previous command to instead use an active timeout of 60 seconds:</p>
<dl>
<dd><code>ovs-vsctl set NetFlow br0 active_timeout=60</code></dl>
<p> Deconfigure the NetFlow settings from <code>br0</code>, which also destroys the NetFlow record (since it is now unreferenced):</p>
<dl>
<dd><code>ovs-vsctl clear Bridge br0 netflow</code></dl>
<h3>sFlow</h3>
<p>Configure bridge <code>br0</code> to send sFlow records to a collector on 10.0.0.1 at port 6343, using <code>eth1</code>&#8216;s IP address as the source, with specific sampling parameters:</p>
<dl>
<dd><code>ovs-vsctl &#8212; &#8211;id=@s create sFlow agent=eth1 target=\&quot;10.0.0.1:6343\&quot; header=128 sampling=64 polling=10 \</code></p>
<dd><code>&#8212; set Bridge br0 sflow=@s</code></dl>
<p> Deconfigure sFlow from <code>br0</code>, which also destroys the sFlow record (since it is now unreferenced):</p>
<dl>
<dd><code>ovs-vsctl &#8212; clear Bridge br0 sflow</code></dl>
<h3>Ipfix</h3>
<p>Configure bridge <code>br0</code> to send one IPFIX flow record per packet sample to UDP port 4739 on host 192.168.0.34, with Observation Domain ID 123 and Observation Point ID 456, a flow cache active timeout of 1 minute (60 seconds), maximum flow cache size of 13 flows, and flows sampled on output port with tunnel info(sampling on input and output port is enabled by default if not disabled) :</p>
<dl>
<dd><code>ovs-vsctl &#8212; set Bridge br0 ipfix=@i \</code></p>
<dd><code>&#8212; &#8211;id=@i create IPFIX targets=\&quot;192.168.0.34:4739\&quot; obs_domain_id=123 obs_point_id=456 cache_active_timeout=60 cache_max_flows=13 \</code></p>
<dd><code>other_config:enable-input-sampling=false other_config:enable-tunnel-sampling=true</code></dl>
<p> Deconfigure the IPFIX settings from <code>br0</code>, which also destroys the IPFIX record (since it is now unreferenced):</p>
<dl>
<dd><code>ovs-vsctl clear Bridge br0 ipfix</code></dl>
<h3>802.1D Spanning Tree Protocol (STP)</h3>
<p>Configure bridge <code>br0</code> to participate in an 802.1D spanning tree:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 stp_enable=true</code></dl>
<p> Set the bridge priority of <code>br0</code> to 0x7800:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:stp-priority=0x7800</code></dl>
<p> Set the path cost of port <code>eth0</code> to 10:</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:stp-path-cost=10</code></dl>
<p> Deconfigure STP from above:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 stp_enable=false</code></dl>
<h3>Multicast Snooping</h3>
<p>Configure bridge <code>br0</code> to enable multicast snooping:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 mcast_snooping_enable=true</code></dl>
<p> Set the multicast snooping aging time <code>br0</code> to 300 seconds:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:mcast-snooping-aging-time=300</code></dl>
<p> Set the multicast snooping table size <code>br0</code> to 2048 entries:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:mcast-snooping-table-size=2048</code></dl>
<p> Disable flooding of unregistered multicast packets to all ports. When set to <code>true</code>, the switch will send unregistered multicast packets only to ports connected to multicast routers. When it is set to <code>false</code>, the switch will send them to all ports. This command disables the flood of unregistered packets on bridge <code>br0</code>.</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:mcast-snooping-disable-flood-unregistered=true</code></dl>
<p> Enable flooding of multicast packets (except Reports) on a specific port.</p>
<dl>
<dd><code>ovs-vsctl set Port eth1 other_config:mcast-snooping-flood=true</code></dl>
<p> Enable flooding of Reports on a specific port.</p>
<dl>
<dd><code>ovs-vsctl set Port eth1 other_config:mcast-snooping-flood-reports=true</code></dl>
<p> Deconfigure multicasting snooping from above:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 mcast_snooping_enable=false</code></dl>
<h3>802.1D-2004 Rapid Spanning Tree Protocol (RSTP)</h3>
<p>Configure bridge <code>br0</code> to participate in an 802.1D-2004 Rapid Spanning Tree:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 rstp_enable=true</code></dl>
<p> Set the bridge address of <code>br0</code> to 00:aa:aa:aa:aa:aa :</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:rstp-address=00:aa:aa:aa:aa:aa</code></dl>
<p> Set the bridge priority of <code>br0</code> to 0x7000. The value must be specified in decimal notation and should be a multiple of 4096 (if not, it is rounded down to the nearest multiple of 4096). The default priority value is 0x800 (32768).</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:rstp-priority=28672</code></dl>
<p> Set the bridge ageing time of <code>br0</code> to 1000 s. The ageing time value should be between 10 s and 1000000 s. The default value is 300 s.</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:rstp-ageing-time=1000</code></dl>
<p> Set the bridge force protocol version of <code>br0</code> to 0. The force protocol version has two acceptable values: 0 (STP compatibility mode) and 2 (normal operation).</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:rstp-force-protocol-version=0</code></dl>
<p> Set the bridge max age of <code>br0</code> to 10 s. The max age value should be between 6 s and 40 s. The default value is 20 s.</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:rstp-max-age=10</code></dl>
<p> Set the bridge forward delay of <code>br0</code> to 15 s. This value should be between 4 s and 30 s. The default value is 15 s.</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:rstp-forward-delay=15</code></dl>
<p> Set the bridge transmit hold count of <code>br0</code> to 7 s. This value should be between 1 s and 10 s. The default value is 6 s.</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 other_config:rstp-transmit-hold-count=7</code></dl>
<p> Enable RSTP on the Port <code>eth0</code>:</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-enable=true</code></dl>
<p> Disable RSTP on the Port <code>eth0</code>:</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-enable=false</code></dl>
<p> Set the priority of port <code>eth0</code> to 32. The value must be specified in decimal notation and should be a multiple of 16 (if not, it is rounded down to the nearest multiple of 16). The default priority value is 0x80 (128).</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-port-priority=32</code></dl>
<p> Set the port number of port <code>eth0</code> to 3:</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-port-num=3</code></dl>
<p> Set the path cost of port <code>eth0</code> to 150:</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-path-cost=150</code></dl>
<p> Set the admin edge value of port <code>eth0</code>:</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-port-admin-edge=true</code></dl>
<p> Set the auto edge value of port <code>eth0</code>:</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-port-auto-edge=true</code></dl>
<p> Set the admin point to point MAC value of port <code>eth0</code>. Acceptable values are <code>0</code> (not point-to-point), <code>1</code> (point-to-point, the default value) or <code>2</code> (automatic detection). The auto-detection mode is not currently implemented, and the value <code>2</code> has the same effect of <code>0</code> (not point-to-point).</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-admin-p2p-mac=1</code></dl>
<p> Set the admin port state value of port <code>eth0</code>. <code>true</code> is the default value.</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-admin-port-state=false</code></dl>
<p> Set the mcheck value of port <code>eth0</code>:</p>
<dl>
<dd><code>ovs-vsctl set Port eth0 other_config:rstp-port-mcheck=true</code></dl>
<p> Deconfigure RSTP from above:</p>
<dl>
<dd><code>ovs-vsctl set Bridge br0 rstp_enable=false</code></dl>
<h3>OpenFlow Version</h3>
<p>Configure bridge <code>br0</code> to support OpenFlow versions 1.0, 1.2, and 1.3:</p>
<dl>
<dd><code>ovs-vsctl set bridge br0 protocols=OpenFlow10,OpenFlow12,OpenFlow13</code></dl>
<h3>Flow Table Configuration</h3>
<p>Limit flow table 0 on bridge br0 to a maximum of 100 flows:</p>
<dl>
<dd><code>ovs-vsctl &#8212; &#8211;id=@ft create Flow_Table flow_limit=100 overflow_policy=refuse &#8212; set Bridge br0 flow_tables=0=@ft</code></dl>
<h2>Exit Status</h2>
<dl>
<dt>0</p>
<dd>Successful program execution.</p>
<dt>1</p>
<dd>Usage, syntax, or configuration file error.</p>
<dt>2</p>
<dd>The <i>bridge</i> argument to <code>br-exists</code> specified the name of a bridge that does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ovsdb-server/">ovsdb-server</a></code>(1), <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8), <code><a href="/docs/linux/man/5-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(5). </p>
