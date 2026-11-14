---
title: "pmcd(1)"
name: "pmcd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmcd/"
description: "pmcd – performance metrics collector daemon"
---

<h2>NAME</h2>
<p> <code>pmcd</code> &#8211; performance metrics collector daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>pmcd</code> [<code>-AfQSv</code>] [<code>-c</code> <i>config</i>] [<code>-C</code> <i>dirname</i>] [<code>-H</code> <i>hostname</i>] [<code>-i</code> <i>ipaddress</i>] [<code>-l</code> <i>logfile</i>] [<code>-L</code> <i>bytes</i>] [<code>-M</code> <i>certname</i>] [<code>&#8211;</code>[<code>n</code>|<code>N</code>] <i>pmnsfile</i>] [<code>-p</code> <i>port</i>[,<i>port</i> &#8230;]] [<code>-P</code> <i>passfile</i>] [<code>-q</code> <i>timeout</i>] [<code>-s</code> <i>sockname</i>] [<code>-T</code> <i>traceflag</i>] [<code>-t</code> <i>timeout</i>] [<code>-U</code> <i>username</i>] [<code>-x</code> <i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmcd</code> is the collector used by the Performance Co-Pilot (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)) to gather performance metrics on a system. As a rule, there must be an instance of <code>pmcd</code> running on a system for any performance metrics to be available to the PCP. </p>
<p> <code>pmcd</code> accepts connections from client applications running either on the same machine or remotely and provides them with metrics and other related information from the machine that <code>pmcd</code> is executing on. <code>pmcd</code> delegates most of this request servicing to a collection of Performance Metrics Domain Agents (or just agents), where each agent is responsible for a particular group of metrics, known as the domain of the agent. For example the <code>postgresql</code> agent is responsible for reporting information relating to the PostgreSQL database, such as the transaction and query counts, indexing and replication statistics, and so on. </p>
<p> The agents may be processes started by <code>pmcd</code>, independent processes or Dynamic Shared Objects (DSOs, see <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3)) attached to <code>pmcd</code>&#8216;s address space. The configuration section below describes how connections to agents are specified. </p>
<p> The options to <code>pmcd</code> are as follows.</p>
<dl>
<dt><code>-A</code></p>
<dd> Disable service advertisement. By default, <code>pmcd</code> will advertise its presence on the network using any available mechanisms (such as Avahi/DNS-SD), assisting remote monitoring tools with finding it. These mechanisms are disabled with this option.</p>
<dt><code>-c</code> <i>config</i></p>
<dd> On startup <code>pmcd</code> uses a configuration file from either the <i>$PCP_PMCDCONF_PATH</i>, configuration variable in <i>/etc/pcp.conf</i>, or an environment variable of the same name. However, these values may be overridden with <i>config</i> using this option. The format of this configuration file is described below.</p>
<dt><code>-C</code> <i>dirname</i></p>
<dd> Specify the path to the Network Security Services certificate database, for (optional) secure connections. The default is <code>/etc/pki/nssdb</code>. Refer also to the <code>-P</code> option. If it does not already exist, this database can be created using the <code>certutil</code> utility. This process and other certificate database maintenance information is provided in the <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) manual page and the online PCP tutorials.</p>
<dt><code>-f</code></p>
<dd> By default <code>pmcd</code> is started as a daemon. The <code>-f</code> option indicates that it should run in the foreground. This is most useful when trying to diagnose problems with misbehaving agents.</p>
<dt><code>-H</code> <i>hostname</i></p>
<dd> This option can be used to set the hostname that <code>pmcd</code> will use to represent this instance of itself. This is used by client tools like <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) when reporting on the (possibly remote) host. If this option is not set, the pmcd.hostname metric will match that returned by <code><a href="/docs/linux/man/1-pmhostname/">pmhostname</a></code>(1). Refer to the manual page for that tool for full details on how the hostname is evaluated.</p>
<dt><code>-i</code> <i>ipaddress</i></p>
<dd> This option is usually only used on hosts with more than one network interface. If no <code>-i</code> options are specified <code>pmcd</code> accepts connections made to any of its host&#8217;s IP (Internet Protocol) addresses. The <code>-i</code> option is used to specify explicitly an IP address that connections should be accepted on. <i>ipaddress</i> should be in the standard dotted form (e.g. 100.23.45.6). The <code>-i</code> option may be used multiple times to define a list of IP addresses. Connections made to any other IP addresses the host has will be refused. This can be used to limit connections to one network interface if the host is a network gateway. It is also useful if the host takes over the IP address of another host that has failed. In such a situation only the standard IP addresses of the host should be given (not the ones inherited from the failed host). This allows PCP applications to determine that a host has failed, rather than connecting to the host that has assumed the identity of the failed host.</p>
<dt><code>-l</code> <i>logfile</i></p>
<dd> By default a log file named <i>pmcd.log</i> is written in the directory <code>$PCP_LOG_DIR/pmcd</code>. The <code>-l</code> option causes the log file to be written to <i>logfile</i> instead of the default. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-L</code> <i>bytes</i></p>
<dd> <i>PDU</i>s received by <code>pmcd </code> from monitoring clients are restricted to a maximum size of 65536 bytes by default to defend against Denial of Service attacks. The <code>-L </code> option may be used to change the maximum incoming <i>PDU </i> size.</p>
<dt><code>-M</code> <i>certname</i></p>
<dd> By default, pmcd will try to use a certificate called <code>PCP Collector certificate .</code> The <code>-M</code> option allows this to be changed.</p>
<dt><code>-n</code> <i>pmnsfile</i></p>
<dd> Normally <code>pmcd</code> loads the default Performance Metrics Name Space (PMNS) from <code>$PCP_VAR_DIR/pmns/root</code>, however if the <code>-n</code> option is specified an alternative namespace is loaded from the file <i>pmnsfile</i>.</p>
<dt><code>-N</code> <i>pmnsfile</i></p>
<dd> Same function as <code>-n</code>, except for the handling of duplicate Performance Metric Identifiers (PMIDs) in <i>pmnsfile</i> &#8211; duplicate names are allowed with <code>-n</code> they are not allowed with <code>-N</code>.</p>
<dt><code>-P</code> <i>passfile</i></p>
<dd> Specify the path to a file containing the Network Security Services certificate database password for (optional) secure connections, and for databases that are password protected. Refer also to the <code>-C</code> option. When using this option, great care should be exercised to ensure appropriate ownership (&quot;pcp&quot; user, typically) and permissions on this file (0400, so as to be unreadable by any user other than the user running the <code>pmcd</code> process).</p>
<dt><code>-q</code> <i>timeout</i></p>
<dd> The pmcd to agent version exchange protocol (new in PCP 2.0 &#8211; introduced to provide backward compatibility) uses this timeout to specify how long pmcd should wait before assuming that no version response is coming from an agent. If this timeout is reached, the agent is assumed to be an agent which does not understand the PCP 2.0 protocol. The default timeout interval is five seconds, but the <code>-q</code> option allows an alternative timeout interval (which must be greater than zero) to be specified. The unit of time is seconds.</p>
<dt><code>-Q</code></p>
<dd> Require that all remote client connections provide a certficate.</p>
<dt><code>-S</code></p>
<dd> Require that all client connections provide user credentials. This means that only unix domain sockets, or authenticated connections are permitted (requires secure sockets support). If any user or group access control requirements are specified in the pmcd configuration file, then this mode of operation is automatically entered, whether the <code>-S</code> flag is specified or not.</p>
<dt><code>-s</code> <i>sockname</i></p>
<dd> Specify the path to a local unix domain socket (for platforms supporting this socket family only). The default value is <i>$PCP_RUN_DIR/pmcd.socket</i>.</p>
<dt><code>-t</code> <i>timeout</i></p>
<dd> To prevent misbehaving clients or agents from hanging the entire Performance Metrics Collection System (PMCS), <code>pmcd</code> uses timeouts on PDU exchanges with clients and agents running as processes. By default the timeout interval is five seconds. The <code>-t</code> option allows an alternative timeout interval in seconds to be specified. If <i>timeout</i> is zero, timeouts are turned off. It is almost impossible to use the debugger interactively on an agent unless timeouts have been turned off for its &quot;parent&quot; <code>pmcd</code>.</p>
<dl>
<dt>
<dd>
<p> Once <code>pmcd</code> is running, the timeout may be dynamically modified by storing an integer value (the timeout in seconds) into the metric <code>pmcd.control.timeout</code> via <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1).</dl>
<dt><code>-T</code> <i>traceflag</i></p>
<dd> To assist with error diagnosis for agents and/or clients of <code>pmcd</code> that are not behaving correctly, an internal event tracing mechanism is supported within <code>pmcd</code>. The value of <i>traceflag</i> is interpreted as a bit field with the following control functions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>1</code> enable client connection tracing</p>
<dt><code>2</code></p>
<dd> enable PDU tracing</p>
<dt><code>256</code></p>
<dd> unbuffered event tracing</dl>
<p> By default, event tracing is buffered using a circular buffer that is over-written as new events are recorded. The default buffer size holds the last 20 events, although this number may be over-ridden by using <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) to modify the metric <code>pmcd.control.tracebufs</code>. </p>
<p> Similarly once <code>pmcd</code> is running, the event tracing control may be dynamically modified by storing 1 (enable) or 0 (disable) into the metrics <code>pmcd.control.traceconn</code>, <code>pmcd.control.tracepdu</code> and <code>pmcd.control.tracenobuf</code>. These metrics map to the bit fields associated with the <i>traceflag</i> argument for the <code>-T</code> option. </p>
<p> When operating in buffered mode, the event trace buffer will be dumped whenever an agent connection is terminated by <code>pmcd</code>, or when any value is stored into the metric <code>pmcd.control.dumptrace</code> via <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1). </p>
<p> In unbuffered mode, <code>every</code> event will be reported when it occurs.</dl>
<dt><code>-U</code> <i>username</i></p>
<dd> User account under which to run <code>pmcd</code>. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</p>
<dt><code>-v</code></p>
<dd> Verify the <code>pmcd</code> configuration file, reporting on any errors then exiting with a status indicating verification success or failure.</p>
<dt><code>-x</code> <i>file</i></p>
<dd> Before the <code>pmcd</code> <i>logfile</i> can be opened, <code>pmcd</code> may encounter a fatal error which prevents it from starting. By default, the output describing this error is sent to <code>/dev/tty</code> but it may redirected to <i>file</i>.</dl>
<p> If a PDU exchange with an agent times out, the agent has violated the requirement that it delivers metrics with little or no delay. This is deemed a protocol failure and the agent is disconnected from <code>pmcd</code>. Any subsequent requests for information from the agent will fail with a status indicating that there is no agent to provide it. </p>
<p> It is possible to specify access control to <code>pmcd</code> based on users, groups and hosts. This allows one to prevent users, groups of users, and certain hosts from accessing the metrics provided by <code>pmcd</code> and is described in more detail in the Section on ACCESS CONTROL below.</p>
<h2>CONFIGURATION</h2>
<p> On startup <code>pmcd</code> looks for a configuration file named <i>$PCP_PMCDCONF_PATH</i>. This file specifies which agents cover which performance metrics domains and how <code>pmcd</code> should make contact with the agents. An optional section specifying access controls may follow the agent configuration data. </p>
<p> <code>Warning</code>: <code>pmcd</code> is usually started as part of the boot sequence and runs initially as root. The configuration file may contain shell commands to create agents, which will be executed by root. To prevent security breaches the configuration file should be writable only by root. The use of absolute path names is also recommended. </p>
<p> The case of the reserved words in the configuration file is unimportant, but elsewhere, the case is preserved. </p>
<p> Blank lines and comments are permitted (even encouraged) in the configuration file. A comment begins with a &#8220;#&#8221; character and finishes at the end of the line. A line may be continued by ensuring that the last character on the line is a &#8220;\&#8221; (backslash). A comment on a continued line ends at the end of the continued line. Spaces may be included in lexical elements by enclosing the entire element in double quotes. A double quote preceded by a backslash is always a literal double quote. A &#8220;#&#8221; in double quotes or preceded by a backslash is treated literally rather than as a comment delimiter. Lexical elements and separators are described further in the following sections.</p>
<h2>AGENT CONFIGURATION</h2>
<p> Each line of the agent configuration section of the configuration file contains details of how to connect <code>pmcd</code> to one of its agents and specifies which metrics domain the agent deals with. An agent may be attached as a DSO, or via a socket, or a pair of pipes. </p>
<p> Each line of the agent configuration section of the configuration file must be either an agent specification, a comment, or a blank line. Lexical elements are separated by whitespace characters, however a single agent specification may not be broken across lines unless a <code>\</code> (backslash) is used to continue the line. </p>
<p> Each agent specification must start with a textual label (string) followed by an integer in the range 1 to 510. The label is a tag used to refer to the agent and the integer specifies the domain for which the agent supplies data. This domain identifier corresponds to the domain portion of the PMIDs handled by the agent. Each agent must have a unique label and domain identifier. </p>
<p> For DSO agents a line of the form:</p>
<dl>
<dt>
<dd> <i>label</i> <i>domain-no</i> <code>dso</code> <i>entry-point</i> <i>path</i></dl>
<p> should appear. Where,</p>
<dl>
<dt>
<dd> <i>label</i> is a string identifying the agent</p>
<dt><i>domain-no</i></p>
<dd> is an unsigned integer specifying the agent&#8217;s domain in the range 1 to 510</p>
<dt><i>entry-point</i></p>
<dd> is the name of an initialization function which will be called when the DSO is loaded</p>
<dt><i>path</i></p>
<dd> designates the location of the DSO and this is expected to be an absolute pathname. <code>pmcd</code> is only able to load DSO agents that have the same <i>simabi</i> (Subprogram Interface Model ABI, or calling conventions) as it does (i.e. only one of the <i>simabi</i> versions will be applicable). The <i>simabi</i> version of a running <code>pmcd</code> may be determined by fetching <code>pmcd.simabi</code>. Alternatively, the <code><a href="/docs/linux/man/1-file/">file</a></code>(1) command may be used to determine the <i>simabi</i> version from the <code>pmcd</code> executable.</p>
<dt>
<dd> For a relative <i>path</i> the environment variable <code>PMCD_PATH</code> defines a colon (:) separated list of directories to search when trying to locate the agent DSO. The default search path is <code>$PCP_SHARE_DIR/lib:/usr/pcp/lib</code>.</dl>
<p> For agents providing socket connections, a line of the form</p>
<dl>
<dt>
<dd> <i>label</i> <i>domain-no</i> <code>socket</code> <i>addr-family</i> <i>address</i> [ <i>command</i> ]</dl>
<p> should appear. Where,</p>
<dl>
<dt>
<dd> <i>label</i> is a string identifying the agent</p>
<dt><i>domain-no</i></p>
<dd> is an unsigned integer specifying the agent&#8217;s domain in the range 1 to 510</p>
<dt><i>addr-family</i></p>
<dd> designates whether the socket is in the <code>AF_INET,</code> <code>AF_INET6</code> or <code>AF_UNIX</code> domain, and the corresponding values for this parameter are <code>inet,</code> <code>ipv6</code> and <code>unix</code> respectively.</p>
<dt><i>address</i></p>
<dd> specifies the address of the socket within the previously specified <i>addr-family.</i> For <code>unix</code> sockets, the address should be the name of an agent&#8217;s socket on the local host (a valid address for the UNIX domain). For <code>inet</code> and <code>ipv6</code> sockets, the address may be either a port number or a port name which may be used to connect to an agent on the local host. There is no syntax for specifying an agent on a remote host as a <code>pmcd</code> deals only with agents on the same machine.</p>
<dt><i>command</i></p>
<dd> is an optional parameter used to specify a command line to start the agent when <code>pmcd</code> initializes. If <i>command</i> is not present, <code>pmcd</code> assumes that the specified agent has already been created. The <i>command</i> is considered to start from the first non-white character after the socket address and finish at the next newline that isn&#8217;t preceded by a backslash. After a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) the <i>command</i> is passed unmodified to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) to instantiate the agent.</dl>
<p> For agents interacting with the <code>pmcd</code> via stdin/stdout, a line of the form:</p>
<dl>
<dt>
<dd> <i>label</i> <i>domain-no</i> <code>pipe</code> <i>protocol</i> <i>command</i></dl>
<p> should appear. Where,</p>
<dl>
<dt>
<dd> <i>label</i> is a string identifying the agent</p>
<dt><i>domain-no</i></p>
<dd> is an unsigned integer specifying the agent&#8217;s domain</p>
<dt><i>protocol</i></p>
<dd> The value for this parameter should be <code>binary</code>. </p>
<dt>
<dd> Additionally, the <i>protocol</i> can include the <code>notready</code> keyword to indicate that the agent must be marked as not being ready to process requests from <code>pmcd</code>. The agent will explicitly notify the <code>pmcd</code> when it is ready to process the requests by sending <code>PM_ERR_PMDAREADY</code> PDU.</p>
<dt><i>command</i></p>
<dd> specifies a command line to start the agent when <code>pmcd</code> initializes. Note that <i>command</i> is mandatory for pipe-based agents. The <i>command</i> is considered to start from the first non-white character after the <i>protocol</i> parameter and finish at the next newline that isn&#8217;t preceded by a backslash. After a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) the <i>command</i> is passed unmodified to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) to instantiate the agent.</dl>
<h2>ACCESS CONTROL CONFIGURATION</h2>
<p> The access control section of the configuration file is optional, but if present it must follow the agent configuration data. The case of reserved words is ignored, but elsewhere case is preserved. Lexical elements in the access control section are separated by whitespace or the special delimiter characters: square brackets (&#8220;[&#8221; and &#8220;]&#8221;), braces (&#8220;{&#8221; and &#8220;}&#8221;), colon (&#8220;:&#8221;), semicolon (&#8220;;&#8221;) and comma (&#8220;,&#8221;). The special characters are not treated as special in the agent configuration section. Lexical elements may be quoted (double quotes) as necessary. </p>
<p> The access control section of the file must start with a line of the form:</p>
<dl>
<dt><code>[access]</code></p>
<dd></dl>
<p> Leading and trailing whitespace may appear around and within the brackets and the case of the <code>access</code> keyword is ignored. No other text may appear on the line except a trailing comment. </p>
<p> Following this line, the remainder of the configuration file should contain lines that allow or disallow operations from particular hosts or groups of hosts. </p>
<p> There are two kinds of operations that occur via <code>pmcd</code>:</p>
<dl>
<dt><code>fetch</code></p>
<dd> allows retrieval of information from <code>pmcd</code>. This may be information about a metric (e.g. its description, instance domain or help text) or a value for a metric.</p>
<dt><code>store</code></p>
<dd> allows <code>pmcd</code> to be used to store metric values in agents that permit store operations. This may be the actual value of the metric (e.g. resetting a counter to zero). Alternatively, it may be a value used by the PMDA to introduce a change to some aspect of monitoring of that metric (e.g. server side event filtering) &#8211; possibly even only for the active client tool performing the store operation, and not others.</dl>
<p> Access to <code>pmcd</code> can be granted in three ways &#8211; by user, group of users, or at a host level. In the latter, all users on a host are granted the same level of access, unless the user or group access control mechanism is also in use. </p>
<p> User names and group names will be verified using the local <code>/etc/passwd</code> and <code>/etc/groups</code> files (or an alternative directory service), using the <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) and <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) routines. </p>
<p> Hosts may be identified by name, IP address, IPv6 address or by the special host specifications &#8220;&quot;unix:&quot;&#8221; or &#8220;&quot;local:&quot;&#8221;. &#8220;&quot;unix:&quot;&#8221; refers to <code>pmcd&#8217;s</code> unix domain socket, on supported platforms. &#8220;&quot;local:&quot;&#8221; is equivalent to specifying &#8220;&quot;unix:&quot;&#8221; and &#8220;localhost&#8220;. </p>
<p> Wildcards may also be specified by ending the host identifier with the single wildcard character &#8220;*&#8221; as the last-given component of an address. The wildcard &#8220;&quot;.*&quot;&#8221; refers to all inet (IPv4) addresses. The wildcard &#8220;&quot;:*&quot;&#8221; refers to all IPv6 addresses. If an IPv6 wildcard contains a &#8220;::&#8221; component, then the final &#8220;*&#8221; refers to the final 16 bits of the address only, otherwise it refers to the remaining unspecified bits of the address. </p>
<p> The wildcard &#8220;*&#8221; refers to all users, groups or host addresses, including &#8220;&quot;unix:&quot;&#8221;. Names of users, groups or hosts may not be wildcarded. </p>
<p> The following are all valid host identifiers: </p>
<pre>
boing
localhost
giggle.melbourne.sgi.com
129.127.112.2
129.127.114.*
129.*
.*
fe80::223:14ff:feaf:b62c
fe80::223:14ff:feaf:*
fe80:*
:*
&quot;unix:&quot;
&quot;local:&quot;
*
</pre>
<p> The following are not valid host identifiers: </p>
<pre>
*.melbourne
129.127.*.*
129.*.114.9
129.127*
fe80::223:14ff:*:*
fe80::223:14ff:*:b62c
fe80*
</pre>
<p> The first example is not allowed because only (numeric) IP addresses may contain a wildcard. The second and fifth examples are not valid because there is more than one wildcard character. The third and sixth contain an embedded wildcard, the fourth and seventh have a wildcard character that is not the last component of the address (the last components are <tt>127*</tt> and <tt>fe80*</tt> respectively). </p>
<p> The name <code>localhost</code> is given special treatment to make the behavior of host wildcarding consistent. Rather than being 127.0.0.1 and ::1, it is mapped to the primary inet and IPv6 addresses associated with the name of the host on which <code>pmcd</code> is running. Beware of this when running <code>pmcd</code> on multi-homed hosts. </p>
<p> Access for users, groups or hosts are allowed or disallowed by specifying statements of the form:</p>
<dl>
<dt>
<dd> <code>allow users</code> <i>userlist</i> <code>:</code> <i>operations</i> <code>;</code><br />
 <code>disallow users</code> <i>userlist</i> <code>:</code> <i>operations</i> <code>;</code><br />
 <code>allow groups</code> <i>grouplist</i> <code>:</code> <i>operations</i> <code>;</code><br />
 <code>disallow groups</code> <i>grouplist</i> <code>:</code> <i>operations</i> <code>;</code><br />
 <code>allow hosts</code> <i>hostlist</i> <code>:</code> <i>operations</i> <code>;</code><br />
 <code>disallow hosts</code> <i>hostlist</i> <code>:</code> <i>operations</i> <code>;</code></dl>
<dl>
<dt><i>list</i></p>
<dd> <i>userlist</i>, <i>grouplist</i> and <i>hostlist</i> are comma separated lists of one or more users, groups or host identifiers.</p>
<dt><i>operations</i></p>
<dd> is a comma separated list of the operation types described above, <code>all</code> (which allows/disallows all operations), or <code>all except</code> <i>operations</i> (which allows/disallows all operations except those listed).</dl>
<p> Either plural or singular forms of <code>users</code>, <code>groups</code>, and <code>hosts</code> keywords are allowed. If this keyword is omitted, a default of <code>hosts</code> will be used. This behaviour is for backward-compatibility only, it is preferable to be explicit. </p>
<p> Where no specific <code>allow</code> or <code>disallow</code> statement applies to an operation, the default is to allow the operation from all users, groups and hosts. In the trivial case when there is no access control section in the configuration file, all operations from all users, groups, and hosts are permitted. </p>
<p> If a new connection to <code>pmcd</code> is attempted by a user, group or host that is not permitted to perform any operations, the connection will be closed immediately after an error response <code>PM_ERR_PERMISSION</code> has been sent to the client attempting the connection. </p>
<p> Statements with the same level of wildcarding specifying identical hosts may not contradict each other. For example if a host named <code>clank</code> had an IP address of 129.127.112.2, specifying the following two rules would be erroneous: </p>
<pre>
allow host clank : fetch, store;
disallow host 129.127.112.2 : all except fetch;
</pre>
<p> because they both refer to the same host, but disagree as to whether the <code>fetch</code> operation is permitted from that host. </p>
<p> Statements containing more specific host specifications override less specific ones according to the level of wildcarding. For example a rule of the form </p>
<pre>
allow host clank : all;
</pre>
<p> overrides </p>
<pre>
disallow host 129.127.112.* : all except fetch;
</pre>
<p> because the former contains a specific host name (equivalent to a fully specified IP address), whereas the latter has a wildcard. In turn, the latter would override </p>
<pre>
disallow host * : all;
</pre>
<p> It is possible to limit the number of connections from a user, group or host to <code>pmcd</code>. This may be done by adding a clause of the form</p>
<dl>
<dt>
<dd> <code>maximum</code> <i>n</i> <code>connections</code></dl>
<p> to the <i>operations</i> list of an <code>allow</code> statement. Such a clause may not be used in a <code>disallow</code> statement. Here, <i>n</i> is the maximum number of connections that will be accepted from the user, group or host matching the identifier(s) used in the statement. </p>
<p> An access control statement with a list of user, group or host identifiers is equivalent to a set of access control statements, with each specifying one of the identifiers in the list and all with the same access controls (both permissions and connection limits). A group should be used if you want users to contribute to a shared connection limit. A wildcard should be used if you want hosts to contribute to a shared connection limit. </p>
<p> When a new client requests a connection, and <code>pmcd</code> has determined that the client has permission to connect, it searches the matching list of access control statements for the most specific match containing a connection limit. For brevity, this will be called the limiting statement. If there is no limiting statement, the client is granted a connection. If there is a limiting statement and the number of <code>pmcd</code> clients with user ID, group ID, or IP addresses that match the identifier in the limiting statement is less than the connection limit in the statement, the connection is allowed. Otherwise the connection limit has been reached and the client is refused a connection. </p>
<p> Group access controls and the wildcarding in host identifiers means that once <code>pmcd</code> actually accepts a connection from a client, the connection may contribute to the current connection count of more than one access control statement &#8211; the client&#8217;s host may match more than one access control statement, and similarly the user ID may be in more than one group. This may be significant for subsequent connection requests. </p>
<p> Note that <code>pmcd</code> enters a mode where it runs effectively with a higher-level of security as soon as a user or group access control section is added to the configuration. In this mode only authenticated connections are allowed &#8211; either from a SASL authenticated connection, or a Unix domain socket (which implicitly passes client credentials). This is the same mode that is entered explicitly using the <code>-S</code> option. Assuming permission is allowed, one can determine whether <code>pmcd</code> is running in this mode by querying the value of the <i>pmcd.feature.creds_required</i> metric. </p>
<p> Note also that because most specific match semantics are used when checking the connection limit, for the host-based access control case, priority is given to clients with more specific host identifiers. It is also possible to exceed connection limits in some situations. Consider the following:</p>
<dl>
<dt>
<dd> allow host clank : all, maximum 5 connections;<br />
 allow host * : all except store, maximum 2 connections;</dl>
<p> This says that only 2 client connections at a time are permitted for all hosts other than &quot;clank&quot;, which is permitted 5. If a client from host &quot;boing&quot; is the first to connect to <code>pmcd</code>, its connection is checked against the second statement (that is the most specific match with a connection limit). As there are no other clients, the connection is accepted and contributes towards the limit for only the second statement above. If the next client connects from &quot;clank&quot;, its connection is checked against the limit for the first statement. There are no other connections from &quot;clank&quot;, so the connection is accepted. Once this connection is accepted, it counts towards <code>both</code> statements&#8217; limits because &quot;clank&quot; matches the host identifier in both statements. Remember that the decision to accept a new connection is made using only the most specific matching access control statement with a connection limit. Now, the connection limit for the second statement has been reached. Any connections from hosts other than &quot;clank&quot; will be refused. </p>
<p> If instead, <code>pmcd</code> with no clients saw three successive connections arrived from &quot;boing&quot;, the first two would be accepted and the third refused. After that, if a connection was requested from &quot;clank&quot; it would be accepted. It matches the first statement, which is more specific than the second, so the connection limit in the first is used to determine that the client has the right to connect. Now there are 3 connections contributing to the second statement&#8217;s connection limit. Even though the connection limit for the second statement has been exceeded, the earlier connections from &quot;boing&quot; are maintained. The connection limit is only checked at the time a client attempts a connection rather than being re-evaluated every time a new client connects to <code>pmcd</code>. </p>
<p> This gentle scheme is designed to allow reasonable limits to be imposed on a first come first served basis, with specific exceptions. </p>
<p> As illustrated by the example above, a client&#8217;s connection is honored once it has been accepted. However, <code>pmcd</code> reconfiguration (see the next section) re-evaluates all the connection counts and will cause client connections to be dropped where connection limits have been exceeded.</p>
<h2>RECONFIGURING PMCD</h2>
<p> If the configuration file has been changed or if an agent is not responding because it has terminated or the PMNS has been changed, <code>pmcd</code> may be reconfigured by sending it a SIGHUP, as in </p>
<pre>
# pmsignal -a -s HUP pmcd
</pre>
<p> When <code>pmcd</code> receives a SIGHUP, it checks the configuration file for changes. If the file has been modified, it is reparsed and the contents become the new configuration. If there are errors in the configuration file, the existing configuration is retained and the contents of the file are ignored. Errors are reported in the <code>pmcd</code> log file. </p>
<p> It also checks the PMNS file for changes. If the PMNS file has been modified, then it is reloaded. Use of <code><a href="/docs/linux/man/1-tail/">tail</a></code>(1) on the log file is recommended while reconfiguring <code>pmcd</code>. </p>
<p> If the configuration for an agent has changed (any parameter except the agent&#8217;s label is different), the agent is restarted. Agents whose configurations do not change are not restarted. Any existing agents not present in the new configuration are terminated. Any deceased agents are that are still listed are restarted. </p>
<p> Sometimes it is necessary to restart an agent that is still running, but malfunctioning. Simply stop the agent (e.g. using SIGTERM from <code><a href="/docs/linux/man/1-pmsignal/">pmsignal</a></code>(1)), then send <code>pmcd</code> a SIGHUP, which will cause the agent to be restarted.</p>
<h2>STARTING AND STOPPING PMCD</h2>
<p> Normally, <code>pmcd</code> is started automatically at boot time and stopped when the system is being brought down. Under certain circumstances it is necessary to start or stop <code>pmcd</code> manually. To do this one must become superuser and type </p>
<pre>
# $PCP_RC_DIR/pmcd start
</pre>
<p> to start <code>pmcd</code>, or </p>
<pre>
# $PCP_RC_DIR/pmcd stop
</pre>
<p> to stop <code>pmcd</code>. Starting <code>pmcd</code> when it is already running is the same as stopping it and then starting it again. </p>
<p> Sometimes it may be necessary to restart <code>pmcd</code> during another phase of the boot process. Time-consuming parts of the boot process are often put into the background to allow the system to become available sooner (e.g. mounting huge databases). If an agent run by <code>pmcd</code> requires such a task to complete before it can run properly, it is necessary to restart or reconfigure <code>pmcd</code> after the task completes. Consider, for example, the case of mounting a database in the background while booting. If the PMDA which provides the metrics about the database cannot function until the database is mounted and available but <code>pmcd</code> is started before the database is ready, the PMDA will fail (however <code>pmcd</code> will still service requests for metrics from other domains). If the database is initialized by running a shell script, adding a line to the end of the script to reconfigure <code>pmcd</code> (by sending it a SIGHUP) will restart the PMDA (if it exited because it couldn&#8217;t connect to the database). If the PMDA didn&#8217;t exit in such a situation it would be necessary to restart <code>pmcd</code> because if the PMDA was still running <code>pmcd</code> would not restart it. </p>
<p> Normally <code>pmcd</code> listens for client connections on TCP/IP port number 44321 (registered at <i><a rel="nofollow" href="http://www.iana.org/">http://www.iana.org/</a></i>). Either the environment variable <code>PMCD_PORT</code> or the <code>-p</code> command line option may be used to specify alternative port number(s) when <code>pmcd</code> is started; in each case, the specification is a comma-separated list of one or more numerical port numbers. Should both methods be used or multiple <code>-p</code> options appear on the command line, <code>pmcd</code> will listen on the union of the set of ports specified via all <code>-p</code> options and the <code>PMCD_PORT</code> environment variable. If non-default ports are used with <code>pmcd</code> care should be taken to ensure that <code>PMCD_PORT</code> is also set in the environment of any client application that will connect to <code>pmcd</code>, or that the extended host specification syntax is used (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for details).</p>
<h2>FILES</h2>
<dl>
<dt><i>$PCP_PMCDCONF_PATH</i></p>
<dd> default configuration file</p>
<dt><i>$PCP_PMCDOPTIONS_PATH</i></p>
<dd> command line options to <code>pmcd</code> when launched from <code>$PCP_RC_DIR/pmcd</code> All the command line option lines should start with a hyphen as the first character.</p>
<dt><code>$PCP_SYSCONFIG_DIR/pmcd</code></p>
<dd> additional environment variables that will be set when <code>pmcd</code> executes. Only settings of the form &quot;PMCD_VARIABLE=value&quot; will be honoured.</p>
<dt><code>./pmcd.log</code></p>
<dd> (or <code>$PCP_LOG_DIR/pmcd/pmcd.log</code> when started automatically)</p>
<dt><code>$PCP_RUN_DIR/pmcd.pid</code></p>
<dd> contains an ascii decimal representation of the process ID of <code>pmcd</code> , when it&#8217;s running.<br />
 All messages and diagnostics are directed here</p>
<dt><code>/etc/pki/nssdb</code></p>
<dd> default Network Security Services (NSS) certificate database directory, used for optional Secure Socket Layer connections. This database can be created and queried using the NSS <code>certutil</code> tool, amongst others.</p>
<dt><code>/etc/passwd</code></p>
<dd> user names, user identifiers and primary group identifiers, used for access control specifications</p>
<dt><code>/etc/groups</code></p>
<dd> group names, group identifiers and group members, used for access control specifications</dl>
<h2>ENVIRONMENT</h2>
<p> In addition to the PCP environment variables described in the <code>PCP ENVIRONMENT</code> section below, the <code>PMCD_PORT</code> variable is also recognised as the TCP/IP port for incoming connections (default <i>44321</i>), and the <code>PMCD_SOCKET</code> variable is also recognised as the path to be used for the Unix domain socket. </p>
<p> If set to the value 1, the <code>PMCD_LOCAL</code> environment variable will cause <code>pmcd</code> to run in a localhost-only mode of operation, where it binds only to the loopback interface. The <i>pmcd.feature.local</i> metric can be queried to determine if <code>pmcd</code> is running in this mode. </p>
<p> The <code>PMCD_MAXPENDING</code> variable can be set to indicate the maximum length to which the queue of pending client connections may grow. </p>
<p> The <code>PMCD_ROOT_AGENT</code> variable controls whether or not <code>pmcd</code> or <code>pmdaroot</code> (when available), start subsequent pmdas. When set to a non-zero value, <code>pmcd</code> will opt to have <code>pmdaroot</code> start, and stop, PMDAs. </p>
<p> The <code>PMCD_RESTART_AGENTS</code> variable determines the behaviour of <code>pmcd</code> in the presence of child PMDAs that have been observed to exit (this is a typical response in the presence of very large, usually domain-induced, PDU latencies). When set to a non-zero value, <code>pmcd</code> will attempt to restart such PMDAS once every minute. When set to zero, it uses the original behaviour of just logging the failure.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> If <code>pmcd</code> is already running the message &quot;Error: OpenRequestSocket bind: Address may already be in use&quot; will appear. This may also appear if <code>pmcd</code> was shutdown with an outstanding request from a client. In this case, a request socket has been left in the TIME_WAIT state and until the system closes it down (after some timeout period) it will not be possible to run <code>pmcd</code>. </p>
<p> In addition to the standard <code>PCP</code> debugging flags, see <code><a href="/docs/linux/man/1-pmdbg/">pmdbg</a></code>(1), <code>pmcd</code> currently uses <code>DBG_TRACE_APPL0</code> for tracing I/O and termination of agents, <code>DBG_TRACE_APPL1</code> for tracing access control and <code>DBG_TRACE_APPL2</code> for tracing the configuration file scanner and parser.</p>
<h2>CAVEATS</h2>
<p> <code>pmcd</code> does not explicitly terminate its children (agents), it only closes their pipes. If an agent never checks for a closed pipe it may not terminate. </p>
<p> The configuration file parser will only read lines of less than 1200 characters. This is intended to prevent accidents with binary files. </p>
<p> The timeouts controlled by the <code>-t</code> option apply to IPC between <code>pmcd</code> and the PMDAs it spawns. This is independent of settings of the environment variables <code>PMCD_CONNECT_TIMEOUT</code> and <code>PMCD_REQUEST_TIMEOUT</code> (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)) which may be used respectively to control timeouts for client applications trying to connect to <code>pmcd</code> and trying to receive information from <code>pmcd</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmdbg/">pmdbg</a></code>(1), <code><a href="/docs/linux/man/1-pmerr/">pmerr</a></code>(1), <code><a href="/docs/linux/man/1-pmgenmap/">pmgenmap</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmrep/">pmrep</a></code>(1), <code><a href="/docs/linux/man/1-pmstat/">pmstat</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3), <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
