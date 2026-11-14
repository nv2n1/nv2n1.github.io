---
title: "ntp_acc(5)"
name: "ntp_acc"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ntp_acc/"
description: "ntp_acc – Access Control Options"
---

<p>ntp_acc &#8211; Access Control Options</p>
<h2>&nbsp;<wbr></h2>
<h2>Access Control Support</h2>
<p>The <code>ntpd</code> daemon implements a general purpose access control list (ACL) containing address/match entries sorted first by increasing address values and then by increasing mask values. A match occurs when the bitwise AND of the mask and the packet source address is equal to the bitwise AND of the mask and address in the list. The list is searched in order with the last match found defining the restriction flags associated with the entry. </p>
<p> An example may clarify how it works. Our campus has two class-B networks, 128.4 for the ECE and CIS departments and 128.175 for the rest of campus. Let&#8217;s assume (not true!) that subnet 128.4.1 homes critical services like class rosters and spread sheets. A suitable ACL might be </p>
<pre>restrict default nopeer # deny new associations
restrict 128.175.0.0 mask 255.255.0.0 # allow campus access
restrict 128.4.0.0 mask 255.255.0.0 none # allow ECE and CIS access
restrict 128.4.1.0 mask 255.255.255.0 notrust # require authentication on subnet 1
restrict time.nist.gov # allow access</pre>
<p>While this facility may be useful for keeping unwanted, broken or malicious clients from congesting innocent servers, it should not be considered an alternative to the NTP authentication facilities. Source address based restrictions are easily circumvented by a determined cracker.</p>
<h2>Access Control Commands</h2>
<dl>
<dd>
<dl>
<dt><code>discard [ average </code><i>avg</i><code> ][ minimum </code><i>min</i><code> ] [ monitor </code><i>prob</i><code> ]</code></p>
<dd>Set the parameters of the rate control facility which protects the server from client abuse. If the <code>limited</code> flag is present in the ACL, packets that violate these limits are discarded. If in addition the <code>kod</code> restriction is present, a kiss-o&#8217;-death packet is returned. </p>
<dl>
<dd>
<dl>
<dt><code>average </code><i>avg</i></p>
<dd>Specify the minimum average interpacket spacing (minimum average headway time) in log2 s with default 3.</p>
<dt><code>minimum </code><i>min</i></p>
<dd>Specify the minimum interpacket spacing (guard time) in log2 s with default 1.</p>
<dt><code>monitor</code></p>
<dd>Specify the probability of discard for packets that overflow the rate-control window. This is a performance optimization for servers with aggregate arrivals of 1000 packets per second or more.</dl>
</dl>
<dt><code>restrict </code><i>address</i><code> [mask </code><i>mask</i><code>] [</code><i>flag</i><code>][&#8230;]</code></p>
<dd>The <i>address</i> argument expressed in dotted-quad form is the address of a host or network. Alternatively, the <i>address</i> argument can be a valid host DNS name, but it must be resolvable at the time when <code>ntpd</code> is started and if it&#8217;s resolved to multiple addresses, only the first address will be added to the list. The <i>mask</i> argument expressed in dotted-quad form defaults to 255.255.255.255, meaning that the <i>address</i> is treated as the address of an individual host. A default entry (address 0.0.0.0, mask 0.0.0.0) is always included and is always the first entry in the list. Note that the text string <code>default</code>, with no mask option, may be used to indicate the default entry. Some flags have the effect to deny service, some have the effect to enable service and some are conditioned by other flags. The flags. are not orthogonal, in that more restrictive flags will often make less restrictive ones redundant. The flags that deny service are classed in two categories, those that restrict time service and those that restrict informational queries and attempts to do run-time reconfiguration of the server. One or more of the following flags may be specified: </p>
<dl>
<dd>
<dl>
<dt><code>flake</code></p>
<dd>Discard received NTP packets with probability 0.1; that is, on average drop one packet in ten. This is for testing and amusement. The name comes from Bob Braden&#8217;s <i>flakeway</i>, which once did a similar thing for early Internet testing.</p>
<dt><code>ignore</code></p>
<dd>Deny packets of all kinds, including <code>ntpq</code> and <code>ntpdc</code> queries.</p>
<dt><code>kod</code></p>
<dd>Send a kiss-o&#8217;-death (KoD) packet if the <code>limited</code> flag is present and a packet violates the rate limits established by the <code>discard</code> command. KoD packets are themselves rate limited for each source address separately. If this flag is not present, packets that violate the rate limits are discarded.</p>
<dt><code>limited</code></p>
<dd>Deny time service if the packet violates the rate limits established by the <code>discard</code> command. This does not apply to <code>ntpq</code> and <code>ntpdc</code> queries.</p>
<dt><code>lowpriotrap</code></p>
<dd>Declare traps set by matching hosts to be low priority. The number of traps a server can maintain is limited (the current limit is 3). Traps are usually assigned on a first come, first served basis, with later trap requestors being denied service. This flag modifies the assignment algorithm by allowing low priority traps to be overridden by later requests for normal priority traps.</p>
<dt><code>mssntp</code></p>
<dd>Enable Microsoft Windows MS-SNTP authentication using Active Directory services. Note: Potential users should be aware that these services involve a TCP connection to another process that could potentially block, denying services to other users. Therefore, this flag should be used only for a dedicated server with no clients other than MS-SNTP.</p>
<dt><code>nomodify</code></p>
<dd>Deny <code>ntpq</code> and <code>ntpdc</code> queries which attempt to modify the state of the server (i.e., run time reconfiguration). Queries which return information are permitted.</p>
<dt><code>noquery</code></p>
<dd>Deny <code>ntpq</code> and <code>ntpdc</code> queries. Time service is not affected.</p>
<dt><code>nopeer</code></p>
<dd>Deny packets that might mobilize an association unless authenticated. This includes broadcast, symmetric-active and manycast server packets when a configured association does not exist. Note that this flag does not apply to packets that do not attempt to mobilize an association.</p>
<dt><code>noserve</code></p>
<dd>Deny all packets except <code>ntpq</code> and <code>ntpdc</code> queries.</p>
<dt><code>notrap</code></p>
<dd>Decline to provide mode 6 control message trap service to matching hosts. The trap service is a subsystem of the <code>ntpdc</code> control message protocol which is intended for use by remote event logging programs.</p>
<dt><code>notrust</code></p>
<dd>Deny packets that are not cryptographically authenticated. Note carefully how this flag interacts with the <code>auth</code> option of the <code>enable</code> and <code>disable</code> commands. If <code>auth</code> is enabled, which is the default, authentication is required for all packets that might mobilize an association. If <code>auth</code> is disabled, but the <code>notrust</code> flag is not present, an association can be mobilized whether or not authenticated. If <code>auth</code> is disabled, but the <code>notrust</code> flag is present, authentication is required only for the specified address/mask range.</p>
<dt><code>ntpport</code></p>
<dd>
<dt><code>non-ntpport</code></p>
<dd>This is actually a match algorithm modifier, rather than a restriction flag. Its presence causes the restriction entry to be matched only if the source port in the packet is the standard NTP UDP port (123). Both <code>ntpport</code> and <code>non-ntpport</code> may be specified. The <code>ntpport</code> is considered more specific and is sorted later in the list.</p>
<dt><code>version</code></p>
<dd>Deny packets that do not match the current NTP version.</dl>
</dl>
<p> Default restriction list entries with the flags <code>ignore, ntpport</code>, for each of the local host&#8217;s interface addresses are inserted into the table at startup to prevent the server from attempting to synchronize to its own time. A default entry is also always present, though if it is otherwise unconfigured; no flags are associated with the default entry (i.e., everything besides your own NTP server is unrestricted).</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-ntp-conf/">ntp.conf</a>(5) The official HTML documentation. This file was automatically generated from HTML source. </p>
