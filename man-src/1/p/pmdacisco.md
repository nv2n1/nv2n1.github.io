---
title: "pmdacisco(1)"
name: "pmdacisco"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdacisco/"
description: "pmdacisco – Cisco router performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdacisco</code> &#8211; Cisco router performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/cisco/pmdacisco</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>] [<code>-P</code> <i>password</i>] [<code>-r</code> <i>refresh</i>] [<code>-s</code> <i>prompt</i>] [<code>-M</code> <i>username</i>] [<code>-x</code> <i>port</i>] <i>host:interface-spec</i> [&#8230;]<br />
 <code>$PCP_PMDAS_DIR/cisco/parse</code> [options] <i>host:interface-spec</i> [&#8230;]<br />
 <code>$PCP_PMDAS_DIR/cisco/probe</code> [<code>-P</code> <i>password</i>] [<code>-s</code> <i>prompt</i>] [<code>-U</code> <i>username</i>] [<code>-x</code> <i>port</i>] <i>host</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmdacisco</code> is a Performance Metrics Domain Agent (PMDA) which extracts performance metrics from one or more Cisco routers. </p>
<p> A brief description of the <code>pmdacisco</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>cisco.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdacisco</code> is started, i.e. <i>$PCP_LOG_DIR/pmcd</i>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-P</code></p>
<dd> By default, it is assumed that no user-level password is required to access the Cisco&#8217;s telnet port. If user-level passwords have been enabled on the Ciscos, then those passwords must be specified to <code>pmdacisco</code>. If specified with the <code>-P</code> option, <i>password</i> will be used as the default user-level password for all Ciscos. See also the INTERFACE IDENTIFICATION section below.</p>
<dt><code>-r</code></p>
<dd> <code>pmdacisco</code> will refresh the current values for all performance metrics by contacting each Cisco router once every <i>refresh</i> seconds. The default <i>refresh</i> is 120 seconds.</p>
<dt><code>-s</code></p>
<dd> The Cisco command prompt ends with the string <i>prompt</i>. The default value is &#8220;&gt;&#8221;. The only way <code>pmdacisco</code> can synchronize the sending of commands and the parsing of output is by recognizing <i>prompt</i> as a unique string that comes at the end of all output, i.e. as the command prompt when waiting for the next command.</p>
<dt><code>-U</code></p>
<dd> By default, it is assumed that no username login is required to access the Cisco&#8217;s telnet port. If username login has been enabled on the Ciscos, then the corresponding usernames must be specified to <code>pmdacisco</code>. If specified with the <code>-U</code> option, <i>username</i> will be used as the default username login for all Ciscos. See also the INTERFACE IDENTIFICATION section below.</p>
<dt><code>-M</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</p>
<dt><code>-x</code></p>
<dd> Connect to the Cisco via TCP port number <i>port</i> rather than the default 23 for a telnet connection.</dl>
<p> For each interface, once the telnet connection is established, <code>pmdacisco</code> is willing to wait up to 5 seconds for the Cisco to provide a new snapshot of the requested information. If this does not happen, the telnet connection is broken and no values are returned. This prevents <code>pmdacisco</code> tying up the Cisco&#8217;s telnet ports waiting indefinitely when the response from the router is not what is expected, e.g. if the format of the &#8220;show int&#8221; output changes, or the command is in error because an interface is no longer configured on the router.</p>
<h2>INTERFACE IDENTIFICATION</h2>
<p> As each Cisco router can support multiple network interfaces and/or multiple communications protocols, it is necessary to tell <code>pmdacisco</code> which interfaces are to be monitored. </p>
<p> The <i>host:interface-spec</i> arguments on the command line define a particular interface on a particular Cisco router. <i>host</i> should be a hostname or a &#8220;dot-notation&#8221; IP address that identifies the telnet port of a particular Cisco router. There are several components of the <i>interface-spec</i> as follows.</p>
<dl>
<dt>protocol</p>
<dd> One of the abbreviations <code>a</code>, <code>B</code>, <code>E</code>, <code>e</code>, <code>f</code>, <code>G</code>, <code>h</code>, <code>s</code> or <code>Vl</code> respectively for ATM, BRI (ISDN), FastEthernet, Ethernet, FDDI, GigabitEthernet, HSSI, serial or Vlan.</p>
<dt>interface</p>
<dd> Depending on the model of the Cisco, this will either be an integer, e.g. <code>s0</code>, or an integer followed by a slash (&#8220;/&#8221;) followed by a subinterface identification in one of a variety of syntactic forms, e.g. <code>e1/0</code>, <code>G0/0/1</code> or <code>s4/2.1</code>.</p>
<dl>
<dt>
<dd>
<p> To discover the valid interfaces on a particular Cisco, connect to the telnet port (using <code><a href="/docs/linux/man/1-telnet/">telnet</a></code>(1)) and enter the command &quot;show int&quot; and look for the interface identifiers following the keywords &#8220;Ethernet&#8221;, &#8220;Fddi&#8221;, &#8220;Serial&#8221;, etc. </p>
<p> Alternatively run the <code>probe</code> command.</dl>
<dt>username</p>
<dd> If there is a username login, and it is different to the default (see <code>-U</code> above), it may be optionally specified here by appending &#8220;@&#8221; and the username to the end of <i>interface-spec</i>.</p>
<dt>password</p>
<dd> If there is a user-level password, and it is different to the default (see <code>-P</code> above), it may be optionally specified here by appending a question mark (&#8220;?&#8221;) and the password to the end of <i>interface-spec</i>.</p>
<dt>prompt</p>
<dd> If the Cisco command prompt is different to the default (see <code>-s</code> above), it may be optionally specified here by appending an exclamation mark (&#8220;!&#8221;) and the prompt to the end of <i>interface-spec</i>.</dl>
<p> The following are examples of valid <i>interface-spec</i> arguments. </p>
<pre>
my-router:e1/2
123.456.789.0:s0
wancisco:f2/3?trust_me
somecisco:G1/0!myprompt
cisco34.foo.bar.com:e2?way2cool
mycisco:s2/2.1 [at] mylogin
yourcisco:E0/0@yourlogin?yourpassword
mycisco:E0/0@mylogin?mypassword!myprompt
</pre>
<h2>HELPER UTILITIES</h2>
<p> The <code>probe</code> command may be used to discover the names of all interfaces for a particular Cisco router identified by <i>host</i>. The <code>-P</code> argument is the same as for <code>pmdacisco</code>. </p>
<p> The <code>parse</code> command takes exactly the same arguments as <code>pmdacisco</code>, but executes outside the control of any <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and so may be used to diagnose problems with handling a particular Cisco router and/or one of its interfaces. </p>
<p> Additional diagnostic verbosity may be produced using the <code>-D appl0,appl1,appl2</code> command line option. <code>appl0</code> logs connect and disconnect events, login progress, high-level flow of control and extracted statistics. <code>appl1</code> traces all commands sent to the Cisco device. <code>appl2</code> logs tokenizing and parsing of the output from the Cisco device. Diagnostics are generated on standard error as each sample is fetched and parsed.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the Cisco performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/cisco
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/cisco
# ./Remove
</pre>
<p> <code>pmdacisco</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdacisco</code></p>
<dt><code>$PCP_PMDAS_DIR/cisco/help</code></p>
<dd> default help text file for the Cisco metrics</p>
<dt><code>$PCP_PMDAS_DIR/cisco/Install</code></p>
<dd> installation script for the <code>pmdacisco</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/cisco/Remove</code></p>
<dd> undo installation script for the <code>pmdacisco</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/cisco.log</code></p>
<dd> default log file for error messages and other information from <code>pmdacisco</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
