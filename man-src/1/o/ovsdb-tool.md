---
title: "ovsdb-tool(1)"
name: "ovsdb-tool"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ovsdb-tool/"
description: "ovsdb-tool – Open vSwitch database management utility"
---

<h2 class="name">NAME</h2>
<p> ovsdb-tool &#8211; Open vSwitch database management utility </p>
<h2>SYNOPSIS</h2>
<p> <code>ovsdb-tool </code>[<i>options</i>] <code>create </code>[<i>db</i> [<i>schema</i>]]<br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>compact </code>[<i>db</i> [<i>target</i>]]<br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>convert </code>[<i>db</i> [<i>schema </i>[<i>target</i>]]]<br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>needs-conversion </code>[<i>db</i> [<i>schema</i>]]<br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>db-version </code>[<i>db</i>]<br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>schema-version </code>[<i>schema</i>]<br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>db-cksum </code>[<i>db</i>]<br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>schema-cksum </code>[<i>schema</i>]<br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>query </code>[<i>db</i>] <i>transaction</i><br />
 <code>ovsdb-tool </code>[<i>options</i>] <code>transact </code>[<i>db</i>] <i>transaction</i><br />
 <code>ovsdb-tool </code>[<i>options</i>] [<code>-m</code> | <code>&#8211;more</code>]&#8230; <code>show-log </code>[<i>db</i>]<br />
 <code>ovsdb-tool help</code></p>
<dl>
<dt>Logging options:</p>
<dd> [<code>-v</code>[<i>module</i>[<code>:</code><i>destination</i>[<code>:</code><i>level</i>]]]]&#8230;<br />
 [<code>&#8211;verbose[=</code><i>module</i>[<code>:</code><i>destination</i>[<code>:</code><i>level</i>]]]]&#8230;<br />
 [<code>&#8211;log-file</code>[<code>=</code><i>file</i>]]</p>
<dt>Common options:</p>
<dd> [<code>-h</code> | <code>&#8211;help</code>] [<code>-V</code> | <code>&#8211;version</code>] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>ovsdb-tool</code> program is a command-line tool for managing Open vSwitch database (OVSDB) files. It does not interact directly with running Open vSwitch database servers (instead, use <code>ovsdb-client</code>).</p>
<h3>Basic Commands</h3>
<dl>
<dt><code>create</code><i> db schema</i></p>
<dd> Reads an OVSDB schema from the file named <i>schema</i> and creates a new OVSDB database file named <i>db</i> using that schema. The new database is initially empty. This command will not overwrite an existing <i>db</i>.</p>
<dt>
<dd> <i>schema</i> must contain an OVSDB schema in JSON format. Refer to the OVSDB specification for details.</p>
<dt><code>compact</code><i> db </i>[<i>target</i>]</p>
<dd> Reads <i>db</i> and writes a compacted version. If <i>target</i> is specified, the compacted version is written as a new file named <i>target</i>, which must not already exist. If <i>target</i> is omitted, then the compacted version of the database replaces <i>db</i> in-place.</p>
<dt><code>convert</code><i> db schema </i>[<i>target</i>]</p>
<dd> Reads <i>db</i>, translating it into to the schema specified in <i>schema</i>, and writes out the new interpretation. If <i>target</i> is specified, the translated version is written as a new file named <i>target</i>, which must not already exist. If <i>target</i> is omitted, then the translated version of the database replaces <i>db</i> in-place.</p>
<dt>
<dd> This command can do simple &#8220;upgrades&#8221; and &#8220;downgrades&#8221; on a database&#8217;s schema. The data in <i>db</i> must be valid when interpreted under <i>schema</i>, with only one exception: data in <i>db</i> for tables and columns that do not exist in <i>schema</i> are ignored. Columns that exist in <i>schema</i> but not in <i>db</i> are set to their default values. All of <i>schema</i>&#8216;s constraints apply in full.</p>
<dt><code>needs-conversion</code><i> db schema</i></p>
<dd> Reads the schema embedded in <i>db</i> and the standalone schema in <i>schema</i> and compares them. If the schemas are the same, prints <code>no</code> on stdout; if they differ, print <code>yes</code>.</p>
<dt><code>db-version</code><i> db</i></p>
<dd>
<dt><code>schema-version</code><i> schema</i></p>
<dd> Prints the version number in the schema embedded within the database <i>db</i> or in the standalone schema <i>schema</i> on stdout. A schema version number has the form <i>x</i><code>.</code><i>y</i><code>.</code><i>z</i>. See <code><a href="/docs/linux/man/5-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(5) for details.</p>
<dt>
<dd> Schema version numbers and Open vSwitch version numbers are independent.</p>
<dt>
<dd> If <i>schema</i> or <i>db</i> was created before schema versioning was introduced, then it will not have a version number and this command will print a blank line.</p>
<dt><code>db-cksum</code><i> db</i></p>
<dd>
<dt><code>schema-cksum</code><i> schema</i></p>
<dd> Prints the checksum in the schema embedded within the database <i>db</i> or of the standalone schema <i>schema</i> on stdout.</p>
<dt>
<dd> If <i>schema</i> or <i>db</i> was created before schema checksums were introduced, then it will not have a checksum and this command will print a blank line.</p>
<dt><code>query</code><i> db transaction</i></p>
<dd> Opens <i>db</i>, executes <i>transaction</i> on it, and prints the results. The <i>transaction</i> must be a JSON array in the format of the <code>params</code> array for the JSON-RPC <code>transact</code> method, as described in the OVSDB specification.</p>
<dt>
<dd> The <i>db</i> is opened for read-only access, so this command may safely run concurrently with other database activity, including <code>ovsdb-server</code> and other database writers. The <i>transaction</i> may specify database modifications, but these will have no effect on <i>db</i>.</p>
<dt><code>transact</code><i> db transaction</i></p>
<dd> Opens <i>db</i>, executes <i>transaction</i> on it, prints the results, and commits any changes to <i>db</i>. The <i>transaction</i> must be a JSON array in the format of the <code>params</code> array for the JSON-RPC <code>transact</code> method, as described in the OVSDB specification.</p>
<dt>
<dd> The <i>db</i> is opened and locked for read/write access, so this command will fail if the database is opened for writing by any other process, including <code><a href="/docs/linux/man/1-ovsdb-server/">ovsdb-server</a></code>(1). Use <code><a href="/docs/linux/man/1-ovsdb-client/">ovsdb-client</a></code>(1), instead, to write to a database that is served by <code><a href="/docs/linux/man/1-ovsdb-server/">ovsdb-server</a></code>(1).</p>
<dt><code>show-log</code><i> db</i></p>
<dd> Prints a summary of the records in <i>db</i>&#8216;s log, including the time and date at which each database change occurred and any associated comment. This may be useful for debugging.</p>
<dt>
<dd> To increase the verbosity of output, add <code>-m</code> (or <code>&#8211;more</code>) one or more times to the command line. With one <code>-m</code>, <code>show-log</code> prints a summary of the records added, deleted, or modified by each transaction. With two <code>-m</code>s, <code>show-log</code> also prints the values of the columns modified by each change to a record.</dl>
<h2>OPTIONS</h2>
<h3>Logging Options</h3>
<dl>
<dt><code>-v</code>[<i>spec</i>]</p>
<dd>
<dt><code>&#8211;verbose=</code>[<i>spec</i>]</p>
<dd> Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd> <code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively. (If <code>&#8211;detach</code> is specified, <code>ovsdb-tool</code> closes its standard file descriptors, so logging to the console will have no effect.)</p>
<dt>
<dd> On Windows platform, <code>syslog</code> is accepted as a word and is only useful along with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd> <code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages. See <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a definition of each log level.</dl>
</dl>
<dt>
<dd> Case is not significant within <i>spec</i>.</p>
<dt>
<dd> Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless <code>&#8211;log-file</code> is also specified (see below).</p>
<dt>
<dd> For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Sets the maximum logging verbosity level, equivalent to <code>&#8211;verbose=dbg</code>.</p>
<dt><code>-vPATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>
<dt><code>&#8211;verbose=PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd> Sets the log pattern for <i>destination</i> to <i>pattern</i>. Refer to <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a description of the valid syntax for <i>pattern</i>.</p>
<dt><code>-vFACILITY:</code><i>facility</i></p>
<dd>
<dt><code>&#8211;verbose=FACILITY:</code><i>facility</i></p>
<dd> Sets the RFC5424 facility of the log message. <i>facility</i> can be one of <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>clock</code>, <code>ftp</code>, <code>ntp</code>, <code>audit</code>, <code>alert</code>, <code>clock2</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>, <code>local4</code>, <code>local5</code>, <code>local6</code> or <code>local7</code>. If this option is not specified, <code>daemon</code> is used as the default for the local system syslog and <code>local0</code> is used while sending a message to the target provided via the <code>&#8211;syslog-target</code> option.</p>
<dt><code>&#8211;log-file</code>[<code>=</code><i>file</i>]</p>
<dd> Enables logging to a file. If <i>file</i> is specified, then it is used as the exact name for the log file. The default log file name used if <i>file</i> is omitted is <code>/var/log/openvswitch/ovsdb-tool.log</code>.</p>
<dt><code>&#8211;syslog-target=</code><i>host</i><code>:</code><i>port</i></p>
<dd> Send syslog messages to UDP <i>port</i> on <i>host</i>, in addition to the system syslog. The <i>host</i> must be a numerical IP address, not a hostname.</p>
<dt><code>&#8211;syslog-method=</code><i>method</i></p>
<dd> Specify <i>method</i> how syslog messages should be sent to syslog daemon. Following forms are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>libc</code>, use libc <code>syslog()</code> function. This is the default behavior. Downside of using this options is that libc adds fixed prefix to every message before it is actually sent to the syslog daemon over <code>/dev/log</code> UNIX domain socket.</p>
<dt>&bull;</p>
<dd> <code>unix:</code><i>file</i>, use UNIX domain socket directly. It is possible to specify arbitrary message format with this option. However, <code>rsyslogd 8.9</code> and older versions use hard coded parser function anyway that limits UNIX domain socket use. If you want to use arbitrary message format with older <code>rsyslogd</code> versions, then use UDP socket to localhost IP address instead.</p>
<dt>&bull;</p>
<dd> <code>udp:</code><i>ip</i>:<i>port</i>, use UDP socket. With this method it is possible to use arbitrary message format also with older <code>rsyslogd</code>. When sending syslog messages over UDP socket extra precaution needs to be taken into account, for example, syslog daemon needs to be configured to listen on the specified UDP port, accidental iptables rules could be interfering with local syslog traffic and there are some security considerations that apply to UDP sockets, but do not apply to UNIX domain sockets.</dl>
</dl>
</dl>
<h3>Other Options</h3>
<dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Prints a brief help message to the console.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Prints version information to the console.</dl>
<h2>FILES</h2>
<p> The default <i>db</i> is <code>/etc/openvswitch/conf.db</code>. The default <i>schema</i> is <code>/usr/share/openvswitch/vswitch.ovsschema</code>. The <code>help</code> command also displays these defaults.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ovsdb-server/">ovsdb-server</a></code>(1), <code><a href="/docs/linux/man/1-ovsdb-client/">ovsdb-client</a></code>(1), and the OVSDB specification. </p>
<h2>Index</h2>
