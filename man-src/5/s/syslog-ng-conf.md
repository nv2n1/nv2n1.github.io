---
title: "syslog-ng-conf(5)"
name: "syslog-ng-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-syslog-ng-conf/"
description: "syslog-ng.conf – syslog-ng configuration file"
---

<p>syslog-ng.conf &#8211; syslog-ng configuration file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>syslog-ng.conf</code></dl>
<h2>Description</h2>
<dd>This manual page is only an abstract; for the complete documentation of syslog-ng, see m[blue]<code>The syslog-ng Open Source Edition Administrator Guide</code>m[]<font SIZE="-2">[1]</font> or m[blue]<code>the official syslog-ng website</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> The syslog-ng OSE application is a flexible and highly scalable system logging application. Typically, syslog-ng is used to manage log messages and implement centralized logging, where the aim is to collect the log messages of several devices on a single, central log server. The different devices &#8211; called syslog-ng clients &#8211; all run syslog-ng, and collect the log messages from the various applications, files, and other <i>sources</i>. The clients send all important log messages to the remote syslog-ng server, where the server sorts and stores them. </p>
<p> The syslog-ng application reads incoming messages and forwards them to the selected <i>destinations</i>. The syslog-ng application can receive messages from files, remote hosts, and other <i>sources</i>. </p>
<p> Log messages enter syslog-ng in one of the defined sources, and are sent to one or more <i>destinations</i>. </p>
<p> Sources and destinations are independent objects; <i>log paths</i> define what syslog-ng does with a message, connecting the sources to the destinations. A log path consists of one or more sources and one or more destinations; messages arriving from a source are sent to every destination listed in the log path. A log path defined in syslog-ng is called a <i>log statement</i>. </p>
<p> Optionally, log paths can include <i>filters</i>. Filters are rules that select only certain messages, for example, selecting only messages sent by a specific application. If a log path includes filters, syslog-ng sends only the messages satisfying the filter rules to the destinations set in the log path.</p>
<h2>Configuring Syslog-Ng</h2>
<dl>
<dd>&bull; The main body of the configuration file consists of object definitions: sources, destinations, logpaths define which log message are received and where they are sent. All identifiers, option names and attributes, and any other strings used in the syslog-ng configuration file are case sensitive. Objects must be defined before they are referenced in another statement. Object definitions (also called statements) have the following syntax: </p>
<dl>
<dd>
<pre>object_type object_id {&lt;options&gt;};</pre>
</dl>
<dl>
<dd>&bull; <i>Type of the object</i>: One of <i>source</i>, <i>destination</i>, <i>log</i>, <i>filter</i>, <i>parser</i>, <i>rewrite</i> rule, or <i>template</i>.</dl>
<dl>
<dd>&bull; <i>Identifier of the object</i>: A unique name identifying the object. When using a reserved word as an identifier, enclose the identifier in quotation marks. </p>
<dl>
<dd><font SIZE="+1"> <code>Tip</code> </font><br />
 Use identifiers that refer to the type of the object they identify. For example, prefix source objects with <i>s_</i>, destinations with <i>d_</i>, and so on. </p>
</dl>
</dl>
<dl>
<dd>&bull; <i>Parameters</i>: The parameters of the object, enclosed in braces <i>{parameters}</i>.</dl>
<dl>
<dd>&bull; <i>Semicolon</i>: Object definitions end with a semicolon (<i>;</i>).</dl>
<p> For example, the following line defines a source and calls it <i>s_internal</i>. </p>
<dl>
<dd>
<pre>source s_internal { internal(); };</pre>
</dl>
<p> The object can be later referenced in other statements using its ID, for example, the previous source is used as a parameter of the following log statement: </p>
<dl>
<dd>
<pre>log { source(s_internal); destination(d_file); };</pre>
</dl>
</dl>
<dl>
<dd>&bull; The parameters and options within a statement are similar to function calls of the C programming language: the name of the option followed by a list of its parameters enclosed within brackets and terminated with a semicolon. </p>
<dl>
<dd>
<pre>option(parameter1, parameter2); option2(parameter1, parameter2);</pre>
</dl>
<p> For example, the following source statement has three options; the first two options (<i>file()</i> and <i>follow_freq()</i>) have a single parameter, while the third one (<i>flags()</i>) has two parameters: </p>
<dl>
<dd>
<pre>source s_tail { file(&quot;/var/log/apache/access.log&quot;
 <a href="//www.systutorials.com/docs/linux/man/1-follow_freq/">follow_freq</a>(1) flags(no-parse, validate-utf8)); };</pre>
</dl>
<p> Objects may have required and optional parameters. Required parameters are positional, meaning that they must be specified in a defined order. Optional parameters can be specified in any order using the option(value) format. If a parameter (optional or required) is not specified, its default value is used. The parameters and their default values are listed in the reference section of the particular object. </p>
<p> <code>Example 1. Using required and optional parameters</code> The <i>unix-stream()</i> source driver has a single required argument: the name of the socket to listen on. Optional parameters follow the socket name in any order, so the following source definitions have the same effect: </p>
<dl>
<dd>
<pre>source s_demo_stream1 {
 unix-stream(&quot;/dev/log&quot; max-connections(10) group(log)); };
source s_demo_stream2 {
 unix-stream(&quot;/dev/log&quot; group(log) max-connections(10)); };</pre>
</dl>
</dl>
<dl>
<dd>&bull; Some options are global options, or can be set globally, for example, whether syslog-ng OSE should use DNS resolution to resolve IP addresses. Global options are detailed in ???. </p>
<dl>
<dd>
<pre>options { use_dns(no); };</pre>
</dl>
</dl>
<dl>
<dd>&bull; All identifiers, attributes, and any other strings used in the syslog-ng configuration file are case sensitive.</dl>
<dl>
<dd>&bull; Objects can be used before definition.</dl>
<dl>
<dd>&bull; To add comments to the configuration file, start a line with <i>#</i> and write your comments. These lines are ignored by syslog-ng. </p>
<dl>
<dd>
<pre># Comment: This is a stream source
source s_demo_stream {
 unix-stream(&quot;/dev/log&quot; max-connections(10) group(log)); };</pre>
</dl>
</dl>
<p> The syntax of log statements is as follows: </p>
<dl>
<dd>
<pre>log {
 source(s1); source(s2); ...
 optional_element(filter1|parser1|rewrite1); optional_element(filter2|parser2|rewrite2);...
 destination(d1); destination(d2); ...
 flags(flag1[, flag2...]);
 };</pre>
</dl>
<p> The following log statement sends all messages arriving to the localhost to a remote server. </p>
<dl>
<dd>
<pre>source s_localhost { tcp(ip(127.0.0.1) port(1999) ); };
destination d_tcp { tcp(&quot;10.1.2.3&quot; port(1999); localport(999)); };
log { source(s_localhost); destination(d_tcp); };</pre>
</dl>
<p> The syslog-ng application has a number of global options governing DNS usage, the timestamp format used, and other general points. Each option may have parameters, similarly to driver specifications. To set global options, add an option statement to the syslog-ng configuration file using the following syntax: </p>
<dl>
<dd>
<pre>options { option1(params); option2(params); ... };</pre>
</dl>
<p> The sources, destinations, and filters available in syslog-ng are listed below. For details, see m[blue]<code>The syslog-ng Administrator Guide</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> &#8211; .sp<br />
 <code>Table 1. Source drivers available in syslog-ng</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> internal() </td>
<td> Messages generated internally in syslog-ng.
</td>
</tr>
<tr VALIGN=top>
<td> file() </td>
<td> Opens the specified file and reads messages.
</td>
</tr>
<tr VALIGN=top>
<td> pipe(), fifo </td>
<td> Opens the specified named pipe and reads messages.
</td>
</tr>
<tr VALIGN=top>
<td> pacct() </td>
<td> Reads messages from the process accounting logs on Linux.
</td>
</tr>
<tr VALIGN=top>
<td> program() </td>
<td> Opens the specified application and reads messages from its standard output.
</td>
</tr>
<tr VALIGN=top>
<td> sun-stream(), sun-streams() </td>
<td> Opens the specified <i>STREAMS</i> device on Solaris systems and reads incoming messages.
</td>
</tr>
<tr VALIGN=top>
<td> syslog() </td>
<td> Listens for incoming messages using the new IETF-standard syslog protocol.
</td>
</tr>
<tr VALIGN=top>
<td> system() </td>
<td> Automatically detects which platform syslog-ng OSE is running on, and collects the native log messages of that platform.
</td>
</tr>
<tr VALIGN=top>
<td> tcp(), tcp6() </td>
<td> Listens on the specified TCP port for incoming messages using the BSD-syslog protocol over IPv4 and IPv6 networks, respectively.
</td>
</tr>
<tr VALIGN=top>
<td> udp(), udp6() </td>
<td> Listens on the specified UDP port for incoming messages using the BSD-syslog protocol over IPv4 and IPv6 networks, respectively.
</td>
</tr>
<tr VALIGN=top>
<td> unix-dgram() </td>
<td> Opens the specified unix socket in <i>SOCK_DGRAM</i> mode and listens for incoming messages.
</td>
</tr>
<tr VALIGN=top>
<td> unix-stream() </td>
<td> Opens the specified unix socket in <i>SOCK_STREAM</i> mode and listens for incoming messages.
</td>
</tr>
</table>
<p> <code>Table 2. Destination drivers available in syslog-ng</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> file() </td>
<td> Writes messages to the specified file.
</td>
</tr>
<tr VALIGN=top>
<td> fifo(), pipe() </td>
<td> Writes messages to the specified named pipe.
</td>
</tr>
<tr VALIGN=top>
<td> program() </td>
<td> Forks and launches the specified program, and sends messages to its standard input.
</td>
</tr>
<tr VALIGN=top>
<td> sql() </td>
<td> Sends messages into an SQL database. In addition to the standard syslog-ng packages, the <i>sql()</i> destination requires database-specific packages to be installed. Refer to the section appropriate for your platform in ???.
</td>
</tr>
<tr VALIGN=top>
<td> syslog() </td>
<td> Sends messages to the specified remote host using the IETF-syslog protocol. The IETF standard supports message transport using the UDP, TCP, and TLS networking protocols.
</td>
</tr>
<tr VALIGN=top>
<td> tcp() and tcp6() </td>
<td> Sends messages to the specified TCP port of a remote host using the BSD-syslog protocol over IPv4 and IPv6, respectively.
</td>
</tr>
<tr VALIGN=top>
<td> udp() and udp6() </td>
<td> Sends messages to the specified UDP port of a remote host using the BSD-syslog protocol over IPv4 and IPv6, respectively.
</td>
</tr>
<tr VALIGN=top>
<td> unix-dgram() </td>
<td> Sends messages to the specified unix socket in <i>SOCK_DGRAM</i> style (BSD).
</td>
</tr>
<tr VALIGN=top>
<td> unix-stream() </td>
<td> Sends messages to the specified unix socket in <i>SOCK_STREAM</i> style (Linux).
</td>
</tr>
<tr VALIGN=top>
<td> usertty() </td>
<td> Sends messages to the terminal of the specified user, if the user is logged in.
</td>
</tr>
</table>
<p> <code>Table 3. Filter functions available in syslog-ng OSE</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> facility() </td>
<td> Filter messages based on the sending facility.
</td>
</tr>
<tr VALIGN=top>
<td> filter() </td>
<td> Call another filter function.
</td>
</tr>
<tr VALIGN=top>
<td> host() </td>
<td> Filter messages based on the sending host.
</td>
</tr>
<tr VALIGN=top>
<td> level() or priority() </td>
<td> Filter messages based on their priority.
</td>
</tr>
<tr VALIGN=top>
<td> match() </td>
<td> Use a regular expression to filter messages based on a specified header or content field.
</td>
</tr>
<tr VALIGN=top>
<td> message() </td>
<td> Use a regular expression to filter messages based their content.
</td>
</tr>
<tr VALIGN=top>
<td> netmask() </td>
<td> Filter messages based on the IP address of the sending host.
</td>
</tr>
<tr VALIGN=top>
<td> program() </td>
<td> Filter messages based on the sending application.
</td>
</tr>
<tr VALIGN=top>
<td> source() </td>
<td> Select messages of the specified syslog-ng OSE source statement.
</td>
</tr>
<tr VALIGN=top>
<td> tags() </td>
<td> Select messages having the specified tag.
</td>
</tr>
</table>
<h2>Files</h2>
<p>/home/algernon/install/syslog-ng/3.5/ </p>
<p> /home/algernon/install/syslog-ng/3.5/etc/syslog-ng.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-syslog-ng/">syslog-ng</a></code>(8) </p>
<p> m[blue]<code>The syslog-ng OSE 3.3 Administrator Guide</code>m[]<font SIZE="-2">[1]</font> </p>
<p> If you experience any problems or need help with syslog-ng, visit m[blue]<code>visit the syslog-ng wiki</code>m[]<font SIZE="-2">[3]</font> or the m[blue]<code>syslog-ng mailing list</code>m[]<font SIZE="-2">[4]</font>. </p>
<p> For news and notifications about of syslog-ng, visit the m[blue]<code>syslog-ng Insider Blog</code>m[]<font SIZE="-2">[5]</font>.</p>
<h2>Author</h2>
<p>This manual page was written by the BalaBit Documentation Team &lt;documentation [at] balabit.com&gt;.</p>
<h2>Copyright</h2>
<h3></h3>
<p>The authors grant permission to copy, distribute and/or modify this manual page under the terms of the GNU General Public License Version 2 or newer (GPL v2+).</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><code>The syslog-ng Open Source Edition Administrator Guide</code></p>
<dl>
<dd><a rel="nofollow" href="http://www.balabit.com/support/documentation/">http://www.balabit.com/support/documentation/</a></dl>
<dt> 2.</p>
<dd>the official syslog-ng website</p>
<dl>
<dd><a rel="nofollow" href="http://www.balabit.com/network-security/syslog-ng/">http://www.balabit.com/network-security/syslog-ng/</a></dl>
<dt> 3.</p>
<dd>visit the syslog-ng wiki</p>
<dl>
<dd><a rel="nofollow" href="http://www.balabit.com/wiki/syslog-ng-faq">http://www.balabit.com/wiki/syslog-ng-faq</a></dl>
<dt> 4.</p>
<dd><code>syslog-ng mailing list</code></p>
<dl>
<dd><a rel="nofollow" href="https://lists.balabit.hu/mailman/listinfo/syslog-ng">https://lists.balabit.hu/mailman/listinfo/syslog-ng</a></dl>
<dt> 5.</p>
<dd><code>syslog-ng Insider Blog</code></p>
<dl>
<dd><a rel="nofollow" href="http://insider.blogs.balabit.com">http://insider.blogs.balabit.com</a></dl>
