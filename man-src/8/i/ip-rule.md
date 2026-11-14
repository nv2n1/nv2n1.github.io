---
title: "ip-rule(8)"
name: "ip-rule"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-rule/"
description: "ip-rule – routing policy database management"
---

<p>ip-rule &#8211; routing policy database management</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

rule

{ COMMAND |

    help }
</code></pre>
<p> <code>ip rule</code> [ <code>list</code> [ <i>SELECTOR</i> ]]<br />
 <code>ip rule</code> { <code>add</code> | <code>del</code> } <i>SELECTOR ACTION</i> </p>
<pre><code>ip rule

{ flush | save | restore }
SELECTOR := [

not ] [

from

PREFIX ] [

to

PREFIX ] [

tos

TOS ] [

fwmark

FWMARK[/MASK] ] [

iif

STRING ] [

oif

STRING ] [

pref

NUMBER ] [

l3mdev ] [

uidrange

NUMBER-NUMBER ] [

ipproto

PROTOCOL ] [

sport [

NUMBER |

NUMBER-NUMBER ] ] [

dport [

NUMBER |

NUMBER-NUMBER ] ] [

tun_id

TUN_ID ]

ACTION := [

table

TABLE_ID ] [

protocol

PROTO ] [

nat

ADDRESS ] [

realms

[SRCREALM/]DSTREALM ] [

goto

NUMBER ] SUPPRESSOR
SUPPRESSOR := [

suppress_prefixlength

NUMBER ] [

suppress_ifgroup

GROUP ]
TABLE_ID := [

local | main | default |

NUMBER ]
</code></pre>
<h2>Description</h2>
<p><i>ip rule</i> manipulates rules in the routing policy database control the route selection algorithm. Classic routing algorithms used in the Internet make routing decisions based only on the destination address of packets (and in theory, but not in practice, on the TOS field). In some circumstances we want to route packets differently depending not only on destination addresses, but also on other packet fields: source address, IP protocol, transport protocol ports or even packet payload. This task is called &#8216;policy routing&#8217;. To solve this task, the conventional destination based routing table, ordered according to the longest match rule, is replaced with a &#8216;routing policy database&#8217; (or RPDB), which selects routes by executing some set of rules. Each policy routing rule consists of a <code>selector</code> and an <code>action predicate.</code> The RPDB is scanned in order of decreasing priority (note that lower number means higher priority, see the description of <i>PREFERENCE</i> below). The selector of each rule is applied to {source address, destination address, incoming interface, tos, fwmark} and, if the selector matches the packet, the action is performed. The action predicate may return with success. In this case, it will either give a route or failure indication and the RPDB lookup is terminated. Otherwise, the RPDB program continues with the next rule. Semantically, the natural action is to select the nexthop and the output device. At startup time the kernel configures the default RPDB consisting of three rules:</p>
<dl>
<dt>1.</p>
<dd>Priority: 0, Selector: match anything, Action: lookup routing table <code>local</code> (ID 255). The <code>local</code> table is a special routing table containing high priority control routes for local and broadcast addresses.</p>
<dt>2.</p>
<dd>Priority: 32766, Selector: match anything, Action: lookup routing table <code>main</code> (ID 254). The <code>main</code> table is the normal routing table containing all non-policy routes. This rule may be deleted and/or overridden with other ones by the administrator.</p>
<dt>3.</p>
<dd>Priority: 32767, Selector: match anything, Action: lookup routing table <code>default</code> (ID 253). The <code>default</code> table is empty. It is reserved for some post-processing if no previous default rules selected the packet. This rule may also be deleted.  Each RPDB entry has additional attributes. F.e. each rule has a pointer to some routing table. NAT and masquerading rules have an attribute to select new IP address to translate/masquerade. Besides that, rules have some optional attributes, which routes have, namely <code>realms</code>. These values do not override those contained in the routing tables. They are only used if the route did not select any attributes. The RPDB may contain rules of the following types:</p>
<dl>
<dd><code>unicast</code> &#8211; the rule prescribes to return the route found in the routing table referenced by the rule. <code>blackhole</code> &#8211; the rule prescribes to silently drop the packet. <code>unreachable</code> &#8211; the rule prescribes to generate a &#8216;Network is unreachable&#8217; error. <code>prohibit</code> &#8211; the rule prescribes to generate &#8216;Communication is administratively prohibited&#8217; error. <code>nat</code> &#8211; the rule prescribes to translate the source address of the IP packet into some other value.</dl>
<dl>
<dt><code>ip rule add &#8211; insert a new rule</code></p>
<dd>
<dt><code>ip rule delete &#8211; delete a rule</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>type</code><i> TYPE </i><code>(default)</code></p>
<dd>the type of this rule. The list of valid types was given in the previous subsection.</p>
<dt><code>from</code><i> PREFIX</i></p>
<dd>select the source prefix to match.</p>
<dt><code>to</code><i> PREFIX</i></p>
<dd>select the destination prefix to match.</p>
<dt><code>iif</code><i> NAME</i></p>
<dd>select the incoming device to match. If the interface is loopback, the rule only matches packets originating from this host. This means that you may create separate routing tables for forwarded and local packets and, hence, completely segregate them.</p>
<dt><code>oif</code><i> NAME</i></p>
<dd>select the outgoing device to match. The outgoing interface is only available for packets originating from local sockets that are bound to a device.</p>
<dt><code>tos</code><i> TOS</i></p>
<dd>
<dt><code>dsfield</code><i> TOS</i></p>
<dd>select the TOS value to match.</p>
<dt><code>fwmark</code><i> MARK</i></p>
<dd>select the <code>fwmark</code> value to match.</p>
<dt><code>uidrange</code><i> NUMBER-NUMBER</i></p>
<dd>select the <code>uid</code> value to match.</p>
<dt><code>ipproto</code><i> PROTOCOL</i></p>
<dd>select the ip protocol value to match.</p>
<dt><code>sport</code><i> NUMBER | NUMBER-NUMBER</i></p>
<dd>select the source port value to match. supports port range.</p>
<dt><code>dport</code><i> NUMBER | NUMBER-NUMBER</i></p>
<dd>select the destination port value to match. supports port range.</p>
<dt><code>priority</code><i> PREFERENCE</i></p>
<dd>the priority of this rule. <i>PREFERENCE</i> is an unsigned integer value, higher number means lower priority, and rules get processed in order of increasing number. Each rule should have an explicitly set <i>unique</i> priority value. The options preference and order are synonyms with priority.</p>
<dt><code>table</code><i> TABLEID</i></p>
<dd>the routing table identifier to lookup if the rule selector matches. It is also possible to use lookup instead of table.</p>
<dt><code>protocol</code><i> PROTO</i></p>
<dd>the routing protocol who installed the rule in question. As an example when zebra installs a rule it would get RTPROT_ZEBRA as the installing protocol.</p>
<dt><code>suppress_prefixlength</code><i> NUMBER</i></p>
<dd>reject routing decisions that have a prefix length of NUMBER or less.</p>
<dt><code>suppress_ifgroup</code><i> GROUP</i></p>
<dd>reject routing decisions that use a device belonging to the interface group GROUP.</p>
<dt><code>realms</code><i> FROM/TO</i></p>
<dd>Realms to select if the rule matched and the routing table lookup succeeded. Realm <i>TO</i> is only used if the route did not select any realm.</p>
<dt><code>nat</code><i> ADDRESS</i></p>
<dd>The base of the IP address block to translate (for source addresses). The <i>ADDRESS</i> may be either the start of the block of NAT addresses (selected by NAT routes) or a local host address (or even zero). In the last case the router does not translate the packets, but masquerades them to this address. Using map-to instead of nat means the same thing. <code>Warning:</code> Changes to the RPDB made with these commands do not become active immediately. It is assumed that after a script finishes a batch of updates, it flushes the routing cache with <code>ip route flush cache</code>.</dl>
</dl>
<dt><code>ip rule flush &#8211; also dumps all the deleted rules.</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>protocol</code><i> PROTO</i></p>
<dd>Select the originating protocol.</dl>
</dl>
<dt><code>ip rule show &#8211; list rules</code></p>
<dd>This command has no arguments. The options list or lst are synonyms with show.</p>
<dt><code>ip rule save</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><code>protocol</code><i> PROTO</i></p>
<dd>Select the originating protocol.</dl>
</dl>
<dt>save rules table information to stdout</p>
<dd>
<dl>
<dd>This command behaves like <code>ip rule show</code> except that the output is raw data suitable for passing to <code>ip rule restore</code>.</dl>
<dt><code>ip rule restore</code></p>
<dd>restore rules table information from stdin</p>
<dl>
<dd>This command expects to read a data stream as returned from <code>ip rule save</code>. It will attempt to restore the rules table information exactly as it was at the time of the save. Any rules already in the table are left unchanged, and duplicates are not ignored.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
