---
title: "dhcpd-leases(5)"
name: "dhcpd-leases"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dhcpd-leases/"
description: "dhcpd.leases – DHCP client lease database"
---

<p>dhcpd.leases &#8211; DHCP client lease database</p>
<h2>Description</h2>
<p>The Internet Systems Consortium DHCP Server keeps a persistent database of leases that it has assigned. This database is a free-form ASCII file containing a series of lease declarations. Every time a lease is acquired, renewed or released, its new value is recorded at the end of the lease file. So if more than one declaration appears for a given lease, the last one in the file is the current one. </p>
<p> When dhcpd is first installed, there is no lease database. However, dhcpd requires that a lease database be present before it will start. To make the initial lease database, just create an empty file called /var/lib/dhcpd/dhcpd.leases. You can do this with: </p>
<pre> touch /var/lib/dhcpd/dhcpd.leases</pre>
<p>In order to prevent the lease database from growing without bound, the file is rewritten from time to time. First, a temporary lease database is created and all known leases are dumped to it. Then, the old lease database is renamed /var/lib/dhcpd/dhcpd.leases~. Finally, the newly written lease database is moved into place.</p>
<h2>Format</h2>
<p>Lease descriptions are stored in a format that is parsed by the same recursive descent parser used to read the <code><a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5)</code> and <code><a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5)</code> files. Lease files can contain lease declarations, and also group and subgroup declarations, host declarations and failover state declarations. Group, subgroup and host declarations are used to record objects created using the OMAPI protocol. </p>
<p> The lease file is a log-structured file &#8211; whenever a lease changes, the contents of that lease are written to the end of the file. This means that it is entirely possible and quite reasonable for there to be two or more declarations of the same lease in the lease file at the same time. In that case, the instance of that particular lease that appears last in the file is the one that is in effect. </p>
<p> Group, subgroup and host declarations in the lease file are handled in the same manner, except that if any of these objects are deleted, a <i>rubout</i> is written to the lease file. This is just the same declaration, with <code>{ deleted; }</code> in the scope of the declaration. When the lease file is rewritten, any such rubouts that can be eliminated are eliminated. It is possible to delete a declaration in the <code>dhcpd.conf</code> file; in this case, the rubout can never be eliminated from the <code>dhcpd.leases</code> file.</p>
<h2>The Lease Declaration</h2>
<p><code>lease </code><i>ip-address</i><code> { </code><i>statements&#8230;</i><code> }</code> </p>
<p> Each lease declaration includes the single IP address that has been leased to the client. The statements within the braces define the duration of the lease and to whom it is assigned. </p>
<pre><code>starts </code><i>date</i><code>;</code>
<code>ends </code><i>date</i><code>;</code>
<code>tstp </code><i>date</i><code>;</code>
<code>tsfp </code><i>date</i><code>;</code>
<code>atsfp </code><i>date</i><code>;</code>
<code>cltt </code><i>date</i><code>;</code></pre>
<p>The start and end time of a lease are recorded using the <code>starts</code> and <code>ends</code> statements. The <code>tstp</code> statement is specified if the failover protocol is being used, and indicates what time the peer has been told the lease expires. The <code>tsfp</code> statement is also specified if the failover protocol is being used, and indicates the lease expiry time that the peer has acknowledged. The <code>atsfp</code> statement is the actual time sent from the failover partner. The <code>cltt</code> statement is the client&#8217;s last transaction time. </p>
<p> The <i>date</i> is specified in two ways, depending on the configuration value for the <code>db-time-format</code> parameter. If it was set to <i>default</i>, then the <i>date</i> fields appear as follows: </p>
<p> <i>weekday year</i><code>/</code><i>month</i><code>/</code><i>day hour</i><code>:</code><i>minute</i><code>:</code><i>second</i> </p>
<p> The weekday is present to make it easy for a human to tell when a lease expires &#8211; it&#8217;s specified as a number from zero to six, with zero being Sunday. The day of week is ignored on input. The year is specified with the century, so it should generally be four digits except for really long leases. The month is specified as a number starting with 1 for January. The day of the month is likewise specified starting with 1. The hour is a number between 0 and 23, the minute a number between 0 and 59, and the second also a number between 0 and 59. </p>
<p> Lease times are specified in Universal Coordinated Time (UTC), not in the local time zone. There is probably nowhere in the world where the times recorded on a lease are always the same as wall clock times. On most unix machines, you can display the current time in UTC by typing <code>date -u</code>. </p>
<p> If the <code>db-time-format</code> was configured to <i>local</i>, then the <i>date</i> fields appear as follows: </p>
<p>&nbsp;<wbr><code>epoch</code>&nbsp;<wbr><i>&lt;seconds-since-epoch&gt;</i><code>;&nbsp;<wbr>#</code>&nbsp;<wbr><i>&lt;day-name&gt;&nbsp;<wbr>&lt;month-name&gt; &lt;day-number&gt; &lt;hours&gt;</i><code>:</code><i>&lt;minutes&gt;</i><code>:</code><i>&lt;seconds&gt; &lt;year&gt;</i> </p>
<p> The <i>seconds-since-epoch</i> is as according to the system&#8217;s local clock (often referred to as &quot;unix time&quot;). The <code>#</code> symbol supplies a comment that describes what actual time this is as according to the system&#8217;s configured timezone, at the time the value was written. It is provided only for human inspection. </p>
<p> If a lease will never expire, <i>date</i> is <code>never</code> instead of an actual date. </p>
<p> <code>hardware </code><i>hardware-type mac-address</i><code>;</code> </p>
<p> The hardware statement records the MAC address of the network interface on which the lease will be used. It is specified as a series of hexadecimal octets, separated by colons. </p>
<p> <code>uid </code><i>client-identifier</i><code>;</code> </p>
<p> The <code>uid</code> statement records the client identifier used by the client to acquire the lease. Clients are not required to send client identifiers, and this statement only appears if the client did in fact send one. Client identifiers are normally an ARP type (1 for ethernet) followed by the MAC address, just like in the <code>hardware</code><i> statement, but this is not required. </p>
<p> The client identifier is recorded as a colon-separated hexadecimal list or as a quoted string. If it is recorded as a quoted string and it contains one or more non-printable characters, those characters are represented as octal escapes &#8211; a backslash character followed by three octal digits. </p>
<p> </i><code>client-hostname </code><i>hostname</i><code>;</code> </p>
<p> Most DHCP clients will send their hostname in the <i>host-name</i> option. If a client sends its hostname in this way, the hostname is recorded on the lease with a <code>client-hostname</code> statement. This is not required by the protocol, however, so many specialized DHCP clients do not send a host-name option. </p>
<p> <code>abandoned;</code> </p>
<p> The <code>abandoned</code> statement indicates that the DHCP server has abandoned the lease. In that case, the <code>abandoned</code> statement will be used to indicate that the lease should not be reassigned. Please see the <code><a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5)</code> manual page for information about abandoned leases. </p>
<p> <code>binding state </code><i>state</i><code>;</code> <code>next binding state </code><i>state</i><code>;</code> </p>
<p> The <code>binding state</code> statement declares the lease&#8217;s binding state. When the DHCP server is not configured to use the failover protocol, a lease&#8217;s binding state will be either <code>active</code> or <code>free</code>. The failover protocol adds some additional transitional states, as well as the <code>backup</code> state, which indicates that the lease is available for allocation by the failover secondary. </p>
<p> The <code>next binding state</code> statement indicates what state the lease will move to when the current state expires. The time when the current state expires is specified in the <i>ends</i> statement. </p>
<p> <code>option agent.circuit-id </code><i>string</i>; <code>option agent.remote-id </code><i>string</i>; </p>
<p> The <code>option agent.circuit-id</code> and <code>option agent.remote-id</code> statements are used to record the circuit ID and remote ID options send by the relay agent, if the relay agent uses the <i>relay agent information option</i>. This allows these options to be used consistently in conditional evaluations even when the client is contacting the server directly rather than through its relay agent. </p>
<p> <code>set </code><i>variable</i><code> = </code><i>value</i><code>;</code> </p>
<p> The <code>set</code> statement sets the value of a variable on the lease. For general information on variables, see the <code><a href="/docs/linux/man/5-dhcp-eval/">dhcp-eval</a>(5)</code> manual page. </p>
<p> <code>The </code><i>ddns-text</i><code> variable</code> </p>
<p> The <i>ddns-text</i> variable is used to record the value of the client&#8217;s TXT identification record when the interim ddns update style has been used to update the DNS for a particular lease. </p>
<p> <code>The </code><i>ddns-fwd-name</i><code> variable</code> </p>
<p> The <i>ddns-fwd-name</i><code> variable records the value of the name used in updating the client&#8217;s A record if a DDNS update has been successfully done by the server. The server may also have used this name to update the client&#8217;s PTR record. </p>
<p> The </code><i>ddns-client-fqdn</i><code> variable</code> </p>
<p> If the server is configured to use the interim ddns update style, and is also configured to allow clients to update their own fqdns, and the client did in fact update its own fqdn, then the <i>ddns-client-fqdn</i> variable records the name that the client has indicated it is using. This is the name that the server will have used to update the client&#8217;s PTR record in this case. </p>
<p> <code>The </code><i>ddns-rev-name</i><code> variable</code> </p>
<p> If the server successfully updates the client&#8217;s PTR record, this variable will record the name that the DHCP server used for the PTR record. The name to which the PTR record points will be either the <i>ddns-fwd-name</i> or the <i>ddns-client-fqdn</i>. </p>
<p> <code>The </code><i>vendor-class-identifier</i><code> variable</code> </p>
<p> The server retains the client-supplied Vendor Class Identifier option for informational purposes, and to render them in DHCPLEASEQUERY responses. </p>
<p> <code>on </code><i>events</i><code> { </code><i>statements&#8230;</i><code> }</code> The <code>on</code><i> statement records a list of statements to execute if a certain event occurs. The possible events that can occur for an active lease are </i><code>release</code> and <code>expiry</code>. More than one event can be specified &#8211; if so, the events are separated by &#8216;|&#8217; characters. </p>
<p> <code>bootp;</code> <code>reserved;</code> These two statements are effectively flags. If present, they indicate that the BOOTP and RESERVED failover flags, respectively, should be set. BOOTP and RESERVED dynamic leases are treated differently than normal dynamic leases, as they may only be used by the client to which they are currently allocated.</p>
<h2>The Failover Peer State Declaration</h2>
<p>The state of any failover peering arrangements is also recorded in the lease file, using the <code>failover peer</code> statement: </p>
<pre><code>failover peer </code><i>name</i><code> state {</code>
<code>my state </code><i>state</i><code> at </code><i>date</i><code>;</code>
<code>peer state </code><i>state</i><code> at </code><i>date</i><code>;</code>
<code>}</code></pre>
<p>The states of the peer named <i>name</i> is being recorded. Both the state of the running server (<code>my state</code>) and the other failover partner (<i>peer state</i>) are recorded. The following states are possible: <code>unknown-state</code>, <code>partner-down</code>, <code>normal</code>, <code>communications-interrupted</code>, <code>resolution-interrupted</code>, <code>potential-conflict</code>, <code>recover</code>, <code>recover-done</code>, <code>shutdown</code>, <code>paused</code>, and <code>startup</code>.</p>
<h2>Files</h2>
<p><code>/var/lib/dhcpd/dhcpd.leases /var/lib/dhcpd/dhcpd.leases~</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8), <a href="/docs/linux/man/5-dhcp-options/">dhcp-options</a>(5), <a href="/docs/linux/man/5-dhcp-eval/">dhcp-eval</a>(5), <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5), RFC2132, RFC2131.</p>
<h2>Author</h2>
<p><code><a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8)</code> was written by Ted Lemon under a contract with Vixie Labs. Funding for this project was provided by Internet Systems Consortium. Information about Internet Systems Consortium can be found at: <code><a rel="nofollow" href="https://www.isc.org/">https://www.isc.org/</a></code></p>
