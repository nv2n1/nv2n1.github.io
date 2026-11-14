---
title: "dcb-app(8)"
name: "dcb-app"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcb-app/"
description: "dcb-app – show / manipulate application priority table of the DCB (Data Center Bridging) subsystem"
---

<p>dcb-app &#8211; show / manipulate application priority table of the DCB (Data Center Bridging) subsystem</p>
<h2>Synopsis</h2>
<pre><code>dcb

[ OPTIONS ]

app

{ COMMAND | help }
</code></pre>
<p> <code>dcb app { show | flush } dev</code> DEV [ <code>default-prio</code> ] [ <code>ethtype-prio</code> ] [ <code>stream-port-prio</code> ] [ <code>dgram-port-prio</code> ] [ <code>port-prio</code> ] [ <code>dscp-prio</code> ]<br />
 <code>dcb ets { add | del | replace } dev</code> DEV [ <code>default-prio</code> <i>PRIO-LIST</i> ] [ <code>ethtype-prio</code> <i>ET-MAP</i> ] [ <code>stream-port-prio</code> <i>PORT-MAP</i> ] [ <code>dgram-port-prio</code> <i>PORT-MAP</i> ] [ <code>port-prio</code> <i>PORT-MAP</i> ] [ <code>dscp-prio</code> <i>DSCP-MAP</i> ] </p>
<pre><code>PRIO-LIST := [ PRIO-LIST ] PRIO
ET-MAP := [ ET-MAP ] ET-MAPPING
ET-MAPPING := ET:PRIO
PORT-MAP := [ PORT-MAP ] PORT-MAPPING
PORT-MAPPING := PORT:PRIO
DSCP-MAP := [ DSCP-MAP ] DSCP-MAPPING
DSCP-MAPPING := { DSCP | all }:PRIO
ET := { 0x600 .. 0xffff }
PORT := { 1 .. 65535 }
DSCP := { 0 .. 63 }
PRIO := { 0 .. 7 }
</code></pre>
<h2>Description</h2>
<p><code>dcb app</code> is used to configure APP table, or application priority table in the DCB (Data Center Bridging) subsystem. The APP table is used to assign priority to traffic based on value in one of several headers: EtherType, L4 destination port, or DSCP. It also allows configuration of port-default priority that is chosen if no other prioritization rule applies. DCB APP entries are 3-tuples of selector, protocol ID, and priority. Selector is an enumeration that picks one of the prioritization namespaces. Currently it mostly corresponds to configurable parameters described below. Protocol ID is a value in the selector namespace. E.g. for EtherType selector, protocol IDs are the individual EtherTypes, for DSCP they are individual code points. The priority is the priority that should be assigned to traffic that matches the selector and protocol ID. The APP table is a set of DCB APP entries. The only requirement is that duplicate entries are not added. Notably, it is valid to have conflicting priority assignment for the same selector and protocol ID. For example, the set of two APP entries (DSCP, 10, 1) and (DSCP, 10, 2), where packets with DSCP of 10 should get priority of both 1 and 2, form a well-defined APP table. The <code>dcb app</code> tool allows low-level management of the app table by adding and deleting individual APP 3-tuples through <code>add</code> and <code>del</code> commands. On the other other hand, the command <code>replace</code> does what one would typically want in this situation&#8211;first adds the new configuration, and then removes the obsolete one, so that only one prioritization is in effect for a given selector and protocol ID. </p>
<h2>Commands</h2>
<dl>
<dt><code>show</code></p>
<dd>Display all entries with a given selector. When no selector is given, shows all APP table entries categorized per selector. </p>
<dt><code>flush</code></p>
<dd>Remove all entries with a given selector. When no selector is given, removes all APP table entries. </p>
<dt><code>add</code></p>
<dd><code>del</code> Add and, respectively, remove individual APP 3-tuples to and from the DCB APP table. </p>
<dt><code>replace</code></p>
<dd>Take the list of entries mentioned as parameter, and add those that are not present in the APP table yet. Then remove those entries, whose selector and protocol ID have been mentioned as parameter, but not with the exact same priority. This has the effect of, for the given selector and protocol ID, causing that the table only contains the priority (or priorities) given as parameter. </p>
</dl>
<h2>Parameters</h2>
<p>The following table shows parameters in a way that they would be used with <code>add</code>, <code>del</code> and <code>replace</code> commands. For <code>show</code> and <code>flush</code>, the parameter name is to be used as a simple keyword without further arguments. </p>
<dl>
<dt><code>default-prio </code><i>PRIO-LIST</i></p>
<dd>The priority to be used for traffic the priority of which is otherwise unspecified. The argument is a list of individual priorities. Note that <code>default-prio</code> rules are configured as triplets (<code>EtherType</code>, <code>0</code>, <i>PRIO</i>). <code>dcb app</code> translates these rules to the symbolic name <code>default-prio</code> and back. </p>
<dt><code>ethtype-prio </code><i>ET-MAP</i></p>
<dd><i>ET-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are EtherType values. Values are priorities to be assigned to traffic with the matching EtherType. </p>
<dt><code>stream-port-prio </code><i>PORT-MAP</i></p>
<dd><code>dgram-port-prio </code><i>PORT-MAP</i> <code>port-prio </code><i>PORT-MAP</i> <i>PORT-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are L4 destination port numbers that match on, respectively, TCP and SCTP traffic, UDP and DCCP traffic, and either of those. Values are priorities that should be assigned to matching traffic. </p>
<dt><code>dscp-prio </code><i>DSCP-MAP</i></p>
<dd><i>DSCP-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are DSCP points, values are priorities assigned to traffic with matching DSCP. DSCP points can be written either direcly as numeric values, or using symbolic names specified in <code>/etc/iproute2/rt_dsfield</code> (however note that that file specifies full 8-bit dsfield values, whereas <code>dcb app</code> will only use the higher six bits). <code>dcb app show</code> will similarly format DSCP values as symbolic names if possible. The command line option <code>-N</code> turns the show translation off. </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>Prioritize traffic with DSCP 0 to priority 0, 24 to 3 and 48 to 6: </p>
<p> # dcb app add dev eth0 dscp-prio 0:0 24:3 48:6 </p>
<p> Add another rule to configure DSCP 24 to priority 2 and show the result: </p>
<p> # dcb app add dev eth0 dscp-prio 24:2<br />
 # dcb app show dev eth0 dscp-prio<br />
 dscp-prio 0:0 CS3:2 CS3:3 CS6:6<br />
 # dcb -N app show dev eth0 dscp-prio<br />
 dscp-prio 0:0 24:2 24:3 48:6 </p>
<p> Reconfigure the table so that the only rule for DSCP 24 is for assignment of priority 4: </p>
<p> # dcb app replace dev eth0 dscp-prio 24:4<br />
 # dcb app show dev eth0 dscp-prio<br />
 dscp-prio 0:0 24:4 48:6 </p>
<p> Flush all DSCP rules: </p>
<p> # dcb app flush dev eth0 dscp-prio<br />
 # dcb app show dev eth0 dscp-prio<br />
 (nothing)</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Petr Machata &lt;me [at] pmachata.org&gt;</p>
