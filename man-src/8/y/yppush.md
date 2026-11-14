---
title: "yppush(8)"
name: "yppush"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yppush/"
description: "yppush – force propagation of changed NIS databases"
---

<p>yppush &#8211; force propagation of changed NIS databases</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/sbin/yppush</code> [-d&nbsp;<wbr><i>domain</i>] [-t&nbsp;<wbr><i>timeout</i>] [&#8211;parallel&nbsp;<wbr><i>#</i> | &#8211;port&nbsp;<wbr><i>port</i>] [-h&nbsp;<wbr><i>host</i>] [-v] <i>mapname</i>&#8230;</dl>
<h2>Description</h2>
<p><code>yppush</code></p>
<dd>copies updated NIS databases (or maps) from the master NIS server to the slave servers within a NIS domain. It is normally run only on the NIS master by <i>/var/yp/Makefile</i> after the master databases are changed. <i>/var/yp/Makefile</i> does not invoke <code>yppush</code> by default, the <code>NOPUSH=true</code> line must be commented out. <code>yppush</code> first constructs a list of NIS slave servers by reading the NIS map <code>ypservers</code> within the <i>domain.</i> A destination host (or a list of hosts with multiple -h commands) can also be specified on the command line. A &quot;transfer map&quot; request is sent to the NIS serger at each slave, along with the information needed by the transfer agent <a href="/docs/linux/man/8-ypxfr/">ypxfr</a>(8) to callback to yppush, which may be printed the result to stderr. Messages are also printed when a transfer is not possible; for instance when the request message is undeliverable. </p>
<p> To specify a port number or use any other <code>yppush</code> options you can edit <i>/var/yp/Makefile</i> directly.</p>
<h2>Options</h2>
<p><code>-d </code><i>domain</i></p>
<dl>
<dd>Specify a particular domain. The NIS domain of the local host system is used by default. If the local host&#8217;s domain name is not set, the domain name must be specified with this flag.</dl>
<p> <code>-t </code><i>timeout</i></p>
<dl>
<dd>The timeout flag is used to specify a timeout value in seconds. This timeout controls how long <code>yppush</code> will wait for a response from a slave server before sending a map transfer request to the next slave server in the list. By default, <code>yppush</code> will wait 90 seconds. For big maps, this is not long enough.</dl>
<p> <code>&#8211;parallel</code><i> #</i>,<code> -p </code><i>#</i></p>
<dl>
<dd><code>yppush</code> normally performs transfers serially, meaning that it will send a map transfer request to one slave server and then wait for it to respond before sending the next map transfer request to the next slave server. In environments with many slaves, it is more efficient to initiate several map transfers at once so that the transfers can take place in parallel. It is not possible to run in parallel and assign a fixed port with the <code>&#8211;port</code> flag</dl>
<p> <code>&#8211;port </code><i>port</i></p>
<dl>
<dd>specify a port for <code>yppush</code> to listen on. By default, <code>yppush</code> will ask <code><a href="/docs/linux/man/8-portmap/">portmap</a>(8)</code> to assign it a random port number. It is not possible to assign a port with this option and run in parallel with the <code>&#8211;parallel</code> or <code>-p</code> flag</dl>
<p> <code>-h </code><i>host</i></p>
<dl>
<dd>The host flag can be used to transfer a map to a user-specified machine or group of machines instead of the list of servers contained in the <code>ypservers</code> map. A list of hosts can be specified by using multiple instances of the <code>-h</code> flag.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Verbose mode: causes <code>yppush</code> to print debugging messages as it runs. Note specifying this flag twice makes <code>yppush</code> even more verbose.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-domainname/">domainname</a></code>(1), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-ypxfr/">ypxfr</a></code>(8)</p>
<h2>Bugs</h2>
<p>The mechanism for transferring NIS maps in NIS v1 is different that that in NIS version 2. This version of <code>yppush</code> has support for transferring maps to NIS v2 systems only.</p>
<h2>Author</h2>
<p>Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;</p>
