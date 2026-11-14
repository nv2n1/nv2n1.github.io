---
title: "snmpnetstat(1)"
name: "snmpnetstat"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpnetstat/"
description: "snmpnetstat – display networking status and configuration information from a network entity via SNMP"
---

<h2>NAME</h2>
<p> snmpnetstat &#8211; display networking status and configuration information from a network entity via SNMP</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpnetstat</code> [COMMON OPTIONS] [-Ca] [-Cn] AGENT<br />
 <code>snmpnetstat</code> [COMMON OPTIONS] [-Ci] [-Co] [-Cr] [-Cn] [-Cs] AGENT<br />
 <code>snmpnetstat</code> [COMMON OPTIONS] [-Ci] [-Cn] [-CI interface] AGENT [interval]<br />
 <code>snmpnetstat</code> [COMMON OPTIONS] [-Ca] [-Cn] [-Cs] [-Cp protocol] AGENT</p>
<h2>DESCRIPTION</h2>
<p> The <code>snmpnetstat </code> command symbolically displays the values of various network-related information retrieved from a remote system using the SNMP protocol. There are a number of output formats, depending on the options for the information presented. The first form of the command displays a list of active sockets. The second form presents the values of other network-related information according to the option selected. Using the third form, with an <i>interval</i> specified, <i>snmpnetstat</i> will continuously display the information regarding packet traffic on the configured network interfaces. The fourth form displays statistics about the named protocol. </p>
<p> <code>snmpnetstat</code> will issue GETBULK requests to query for information if at least protocol version <i>v2</i> is used. </p>
<p> AGENT identifies a target SNMP agent, which is instrumented to monitor the given objects. At its simplest, the AGENT specification will consist of a hostname or an IPv4 address. In this situation, the command will attempt communication with the agent, using UDP/IPv4 to port 161 of the given target host. See <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1) for a full list of the possible formats for AGENT. </p>
<h2>OPTIONS</h2>
<p> The options have the following meaning: </p>
<p> <code>COMMON OPTIONS</code><br />
&nbsp;<wbr>Please see <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for a list of possible values for common options as well as their descriptions. </p>
<p> <code>-Ca</code> With the default display, show the state of all sockets; normally sockets used by server processes are not shown. </p>
<p> <code>-Ci</code> Show the state of all of the network interfaces. The interface display provides a table of cumulative statistics regarding packets transferred, errors, and collisions. The network addresses of the interface and the maximum transmission unit (&#8220;mtu&#8221;) are also displayed. </p>
<p> <code>-Co</code> Show an abbreviated interface status, giving octets in place of packets. This is useful when enquiring virtual interfaces (such as Frame-Relay circuits) on a router. </p>
<p> <code>-CI</code><i> interface</i> Show information only about this interface; used with an <i>interval</i> as described below. </p>
<p> <code>-Cn</code> Show network addresses as numbers (normally <i>snmpnetstat</i> interprets addresses and attempts to display them symbolically). This option may be used with any of the display formats. </p>
<p> <code>-Cp</code><i> protocol</i> Show statistics about <i>protocol,</i> which is either a well-known name for a protocol or an alias for it. Some protocol names and aliases are listed in the file <i>/etc/protocols</i>. A null response typically means that there are no interesting numbers to report. The program will complain if <i>protocol</i> is unknown or if there is no statistics routine for it. </p>
<p> <code>-Cs</code> Show per-protocol statistics. When used with the <code>-Cr</code> option, show routing statistics instead. </p>
<p> <code>-Cr</code> Show the routing tables. When <code>-Cs</code> is also present, show per-protocol routing statistics instead of the routing tables. </p>
<p> <code>-CR</code><i> repeaters</i> For GETBULK requests, <i>repeaters</i> specifies the max-repeaters value to use. </p>
<p> When snmpnetstat is invoked with an interval argument, it displays a running count of statistics related to network interfaces. <i>interval</i> is the number of seconds between reporting of statistics. </p>
<p> <i>The Active Sockets Display (default)</i> </p>
<p> The default display, for active sockets, shows the local and remote addresses, protocol, and the internal state of the protocol. Address formats are of the form &#8220;host.port&#8221; or &#8220;network.port&#8221; if a socket&#8217;s address specifies a network but no specific host address. When known, the host and network addresses are displayed symbolically according to the data bases <i>/etc/hosts and</i> <i>/etc/networks,</i> respectively. If a symbolic name for an address is unknown, or if the <code>-Cn</code> option is specified, the address is printed numerically, according to the address family. For more information regarding the Internet &#8220;dot format,&#8221; refer to <i><a href="//www.systutorials.com/docs/linux/man/3N-inet/">inet</a>(3N).</i> Unspecified, or &#8220;wildcard&#8221;, addresses and ports appear as &#8220;*&#8221;. </p>
<p> <i>The Interface Display</i> </p>
<p> The interface display provides a table of cumulative statistics regarding packets transferred, errors, and col- lisions. The network addresses of the interface and the maximum transmission unit (&#8220;mtu&#8221;) are also displayed. </p>
<p> <i>The Routing Table Display</i> </p>
<p> The routing table display indicates the available routes and their status. Each route consists of a destination host or network and a gateway to use in forwarding pack- ets. The flags field shows the state of the route (&#8220;U&#8221; if &#8220;up&#8221;), whether the route is to a gateway (&#8220;G&#8221;), whether the route was created dynamically by a redirect (&#8220;D&#8221;), and whether the route has been modified by a redirect (&#8220;M&#8221;). Direct routes are created for each interface attached to the local host; the gateway field for such entries shows the address of the outgoing inter- face. The interface entry indicates the network interface utilized for the route. </p>
<p> <i>The Interface Display with an Interval</i> </p>
<p> When <i>snmpnetstat</i> is invoked with an <i>interval</i> argument, it displays a running count of statistics related to network interfaces. This display consists of a column for the primary interface and a column summarizing information for all interfaces. The primary interface may be replaced with another interface with the <code>-CI</code> option. The first line of each screen of information contains a summary since the system was last rebooted. Subsequent lines of output show values accumulated over the preceding interval. </p>
<p> <i>The Active Sockets Display for a </i> <i>Single Protocol</i> </p>
<p> When a protocol is specified with the <code>-Cp</code> option, the information displayed is similar to that in the default display for active sockets, except the display is limited to the given protocol.</p>
<h2>EXAMPLES</h2>
<p> Example of using snmpnetstat to display active sockets (default): </p>
<p> % snmpnetstat -v 2c -c public -Ca testhost </p>
<pre>
Active Internet (tcp) Connections (including servers)
Proto Local Address                Foreign Address                 (state)
tcp   *.echo                        *.*                            LISTEN
tcp   *.discard                     *.*                            LISTEN
tcp   *.daytime                     *.*                            LISTEN
tcp   *.chargen                     *.*                            LISTEN
tcp   *.ftp                         *.*                            LISTEN
tcp   *.telnet                      *.*                            LISTEN
tcp   *.smtp                        *.*                            LISTEN
...
Active Internet (udp) Connections
Proto Local Address
udp    *.echo
udp    *.discard
udp    *.daytime
udp    *.chargen
udp    *.time
...
</pre>
<p> % snmpnetstat -v 2c -c public -Ci testhost </p>
<pre>
Name     Mtu Network    Address          Ipkts   Ierrs    Opkts Oerrs Queue
eri0    1500 10.6.9/24  testhost     170548881  245601   687976     0    0
lo0     8232 127        localhost      7530982       0  7530982     0    0
</pre>
<p> Example of using snmpnetstat to show statistics about a specific protocol: </p>
<pre>
% snmpnetstat -v 2c -c public -Cp tcp testhost
Active Internet (tcp) Connections
Proto Local Address                Foreign Address                 (state)
tcp   *.echo                        *.*                            LISTEN
tcp   *.discard                     *.*                            LISTEN
tcp   *.daytime                     *.*                            LISTEN
tcp   *.chargen                     *.*                            LISTEN
tcp   *.ftp                         *.*                            LISTEN
tcp   *.telnet                      *.*                            LISTEN
tcp   *.smtp                        *.*                            LISTEN
...
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-iostat/">iostat</a>(1), <a href="/docs/linux/man/1-vmstat/">vmstat</a>(1), <a href="/docs/linux/man/5-hosts/">hosts</a>(5), <a href="/docs/linux/man/5-networks/">networks</a>(5), <a href="/docs/linux/man/5-protocols/">protocols</a>(5), <a href="/docs/linux/man/5-services/">services</a>(5).</p>
<h2>BUGS</h2>
<p> The notion of errors is ill-defined. </p>
<h2>Index</h2>
