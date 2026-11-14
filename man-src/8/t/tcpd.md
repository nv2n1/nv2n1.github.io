---
title: "tcpd(8)"
name: "tcpd"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcpd/"
---

tcpd - access control facility for internet services

<h2>Description</h2>

The <i>tcpd</i> program can be set up to monitor incoming requests for <i>telnet</i>, <i>finger</i>, <i>ftp</i>, <i>exec</i>, <i>rsh</i>, <i>rlogin</i>, <i>tftp</i>, <i>talk</i>, <i>comsat</i> and other services that have a one-to-one mapping onto executable files. 

 The program supports both 4.3BSD-style sockets and System V.4-style TLI. Functionality may be limited when the protocol underneath TLI is not an internet protocol. 

 Operation is as follows: whenever a request for service arrives, the <i>inetd</i> daemon is tricked into running the <i>tcpd</i> program instead of the desired server. <i>tcpd</i> logs the request and does some additional checks. When all is well, <i>tcpd</i> runs the appropriate server program and goes away. 

 Optional features are: pattern-based access control, client username lookups with the RFC 931 etc. protocol, protection against hosts that pretend to have someone elses host name, and protection against hosts that pretend to have someone elses network address.

<h2>Logging</h2>

Connections that are monitored by <i>tcpd</i> are reported through the <i><a HREF="/docs/linux/man/3-syslog/">syslog</a></i>(3) facility. Each record contains a time stamp, the client host name and the name of the requested service. The information can be useful to detect unwanted activities, especially when logfile information from several hosts is merged. 

 In order to find out where your logs are going, examine the syslog configuration file, usually /etc/syslog.conf.

<h2>Access Control</h2>

Optionally, <i>tcpd</i> supports a simple form of access control that is based on pattern matching. The access-control software provides hooks for the execution of shell commands when a pattern fires. For details, see the <i><a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a></i>(5) manual page.

<h2>Host Name Verification</h2>

The authentication scheme of some protocols (<i>rlogin, rsh</i>) relies on host names. Some implementations believe the host name that they get from any random name server; other implementations are more careful but use a flawed algorithm. 

 <i>tcpd</i> verifies the client host name that is returned by the address-&gt;name DNS server by looking at the host name and address that are returned by the name-&gt;address DNS server. If any discrepancy is detected, <i>tcpd</i> concludes that it is dealing with a host that pretends to have someone elses host name. 

 If the sources are compiled with -DPARANOID, <i>tcpd</i> will drop the connection in case of a host name/address mismatch. Otherwise, the hostname can be matched with the <i>PARANOID</i> wildcard, after which suitable action can be taken.

<h2>Host Address Spoofing</h2>

Optionally, <i>tcpd</i> disables source-routing socket options on every connection that it deals with. This will take care of most attacks from hosts that pretend to have an address that belongs to someone elses network. UDP services do not benefit from this protection. This feature must be turned on at compile time.

<h2>Rfc 931</h2>

When RFC 931 etc. lookups are enabled (compile-time option) <i>tcpd</i> will attempt to establish the name of the client user. This will succeed only if the client host runs an RFC 931-compliant daemon. Client user name lookups will not work for datagram-oriented connections, and may cause noticeable delays in the case of connections from PCs.

<h2>Examples</h2>

The details of using <i>tcpd</i> depend on pathname information that was compiled into the program.

<h2>Example 1</h2>

This example applies when <i>tcpd</i> expects that the original network daemons will be moved to an &quot;other&quot; place. 

 In order to monitor access to the <i>finger</i> service, move the original finger daemon to the &quot;other&quot; place and install tcpd in the place of the original finger daemon. No changes are required to configuration files. <pre># mkdir /other/place
# mv /usr/etc/in.fingerd /other/place
# cp tcpd /usr/etc/in.fingerd</pre>The example assumes that the network daemons live in /usr/etc. On some systems, network daemons live in /usr/sbin or in /usr/libexec, or have no `in.' prefix to their name.

<h2>Example 2</h2>

This example applies when <i>tcpd</i> expects that the network daemons are left in their original place. 

 In order to monitor access to the <i>finger</i> service, perform the following edits on the <i>inetd</i> configuration file (usually <i>/etc/inetd.conf</i> or <i>/etc/inet/inetd.conf</i>): <pre><br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>finger stream tcp nowait nobody /usr/etc/in.fingerd in.fingerd
becomes:
<br>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>finger stream tcp nowait nobody /some/where/tcpd in.fingerd</pre>The example assumes that the network daemons live in /usr/etc. On some systems, network daemons live in /usr/sbin or in /usr/libexec, the daemons have no `in.' prefix to their name, or there is no userid field in the inetd configuration file. 

 Similar changes will be needed for the other services that are to be covered by <i>tcpd</i>. Send a `kill -HUP' to the <i><a HREF="/docs/linux/man/8-inetd/">inetd</a></i>(8) process to make the changes effective. AIX users may also have to execute the `inetimp' command.

<h2>Example 3</h2>

In the case of daemons that do not live in a common directory (&quot;secret&quot; or otherwise), edit the <i>inetd</i> configuration file so that it specifies an absolute path name for the process name field. For example: <pre> ntalk dgram udp wait root /some/where/tcpd /usr/local/lib/ntalkd</pre>Only the last component (ntalkd) of the pathname will be used for access control and logging.

<h2>Bugs</h2>

Some UDP (and RPC) daemons linger around for a while after they have finished their work, in case another request comes in. In the inetd configuration file these services are registered with the <i>wait</i> option. Only the request that started such a daemon will be logged. 

 The program does not work with RPC services over TCP. These services are registered as <i>rpc/tcp</i> in the inetd configuration file. The only non-trivial service that is affected by this limitation is <i>rexd</i>, which is used by the <i><a HREF="/docs/linux/man/1-on/">on</a>(1)</i> command. This is no great loss. On most systems, <i>rexd</i> is less secure than a wildcard in /etc/hosts.equiv. 

 RPC broadcast requests (for example: <i>rwall, rup, rusers</i>) always appear to come from the responding host. What happens is that the client broadcasts the request to all <i>portmap</i> daemons on its network; each <i>portmap</i> daemon forwards the request to a local daemon. As far as the <i>rwall</i> etc. daemons know, the request comes from the local host.

<h2>Files</h2>

The default locations of the host access control tables are: 

 /etc/hosts.allow 
 /etc/hosts.deny

<h2>See Also</h2>

<pre><a HREF="//www.systutorials.com/docs/linux/man/5-hosts_access/">hosts_access</a>(5), format of the tcpd access control tables.
<a HREF="//www.systutorials.com/docs/linux/man/5-syslog.conf/">syslog.conf</a>(5), format of the syslogd control file.
<a HREF="//www.systutorials.com/docs/linux/man/5-inetd.conf/">inetd.conf</a>(5), format of the inetd control file.</pre>

<h2>Authors</h2>

<pre>Wietse Venema (wietse [at] wzv.win.tue.nl),
Department of Mathematics and Computing Science,
Eindhoven University of Technology
Den Dolech 2, P.O. Box 513, 
5600 MB Eindhoven, The Netherlands</pre>
