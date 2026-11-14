---
title: "nftables(8)"
name: "nftables"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nftables/"
description: "nft – Administration tool of the nftables framework for packet filtering and classification"
---

<p>nft &#8211; Administration tool of the nftables framework for packet filtering and classification</p>
<h2>Synopsis</h2>
<pre><code>nft</code> [ <code>-nNscaeSupyjt</code> ] [ <code>-I</code> <i>directory</i> ] [ <code>-f</code> <i>filename</i> | <code>-i</code> | <i>cmd</i> ...]
<code>nft</code> <code>-h</code>
<code>nft</code> <code>-v</code></pre>
<h2>Description</h2>
<p>nft is the command line tool used to set up, maintain and inspect packet filtering and classification rules in the Linux kernel, in the nftables framework. The Linux kernel subsystem is known as nf_tables, and &#8216;nf&#8217; stands for Netfilter.</p>
<h2>Options</h2>
<p>The command accepts several different options which are documented here in groups for better understanding of their meaning. You can get information about options by running <code>nft &#8211;help</code>. </p>
<p> <code>General options:</code> </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Show help message and all options.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dd>Show version.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Show long version information, including compile-time configuration.</dl>
<p> <code>Ruleset input handling options that specify to how to load rulesets:</code> </p>
<p> <code>-f</code>, <code>&#8211;file </code><i>filename</i></p>
<dl>
<dd>Read input from <i>filename</i>. If <i>filename</i> is -, read from stdin.</dl>
<p> <code>-D</code>, <code>&#8211;define </code><i>name=value</i></p>
<dl>
<dd>Define a variable. You can only combine this option with <i>-f</i>.</dl>
<p> <code>-i</code>, <code>&#8211;interactive</code></p>
<dl>
<dd>Read input from an interactive readline CLI. You can use quit to exit, or use the EOF marker, normally this is CTRL-D.</dl>
<p> <code>-I</code>, <code>&#8211;includepath directory</code></p>
<dl>
<dd>Add the directory <i>directory</i> to the list of directories to be searched for included files. This option may be specified multiple times.</dl>
<p> <code>-c</code>, <code>&#8211;check</code></p>
<dl>
<dd>Check commands validity without actually applying the changes.</dl>
<p> <code>-o</code>, <code>&#8211;optimize</code></p>
<dl>
<dd>Optimize your ruleset. You can combine this option with <i>-c</i> to inspect the proposed optimizations.</dl>
<p> <code>Ruleset list output formatting that modify the output of the list ruleset command:</code> </p>
<p> <code>-a</code>, <code>&#8211;handle</code></p>
<dl>
<dd>Show object handles in output.</dl>
<p> <code>-s</code>, <code>&#8211;stateless</code></p>
<dl>
<dd>Omit stateful information of rules and stateful objects.</dl>
<p> <code>-t</code>, <code>&#8211;terse</code></p>
<dl>
<dd>Omit contents of sets from output.</dl>
<p> <code>-S</code>, <code>&#8211;service</code></p>
<dl>
<dd>Translate ports to service names as defined by /etc/services.</dl>
<p> <code>-N</code>, <code>&#8211;reversedns</code></p>
<dl>
<dd>Translate IP address to names via reverse DNS lookup. This may slow down your listing since it generates network traffic.</dl>
<p> <code>-u</code>, <code>&#8211;guid</code></p>
<dl>
<dd>Translate numeric UID/GID to names as defined by /etc/passwd and /etc/group.</dl>
<p> <code>-n</code>, <code>&#8211;numeric</code></p>
<dl>
<dd>Print fully numerical output.</dl>
<p> <code>-y</code>, <code>&#8211;numeric-priority</code></p>
<dl>
<dd>Display base chain priority numerically.</dl>
<p> <code>-p</code>, <code>&#8211;numeric-protocol</code></p>
<dl>
<dd>Display layer 4 protocol numerically.</dl>
<p> <code>-T</code>, <code>&#8211;numeric-time</code></p>
<dl>
<dd>Show time, day and hour values in numeric format.</dl>
<p> <code>Command output formatting:</code> </p>
<p> <code>-e</code>, <code>&#8211;echo</code></p>
<dl>
<dd>When inserting items into the ruleset using <code>add</code>, <code>insert</code> or <code>replace</code> commands, print notifications just like <code>nft monitor</code>.</dl>
<p> <code>-j</code>, <code>&#8211;json</code></p>
<dl>
<dd>Format output in JSON. See <a href="/docs/linux/man/5-libnftables-json/">libnftables-json</a>(5) for a schema description.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code> <i>level</i></p>
<dl>
<dd>Enable debugging output. The debug level can be any of <code>scanner</code>, <code>parser</code>, <code>eval</code>, <code>netlink</code>, <code>mnl</code>, <code>proto-ctx</code>, <code>segtree</code>, <code>all</code>. You can combine more than one by separating by the <i>,</i> symbol, for example <i>-d eval,mnl</i>.</dl>
<h2>Input File Formats</h2>
<h3>Lexical Conventions</h3>
<p>Input is parsed line-wise. When the last character of a line, just before the newline character, is a non-quoted backslash (\), the next line is treated as a continuation. Multiple commands on the same line can be separated using a semicolon (;). </p>
<p> A hash sign (#) begins a comment. All following characters on the same line are ignored. </p>
<p> Identifiers begin with an alphabetic character (a-z,A-Z), followed by zero or more alphanumeric characters (a-z,A-Z,0-9) and the characters slash (/), backslash (\), underscore (_) and dot (.). Identifiers using different characters or clashing with a keyword need to be enclosed in double quotes (&quot;).</p>
<h3>Include Files</h3>
<dl>
<dd>
<pre><code>include</code> <i>filename</i></pre>
</dl>
<p> Other files can be included by using the <code>include</code> statement. The directories to be searched for include files can be specified using the <code>-I</code>/<code>&#8211;includepath</code> option. You can override this behaviour either by prepending &#8216;./&#8217; to your path to force inclusion of files located in the current working directory (i.e. relative path) or / for file location expressed as an absolute path. </p>
<p> If <code>-I</code>/<code>&#8211;includepath</code> is not specified, then nft relies on the default directory that is specified at compile time. You can retrieve this default directory via the <code>-h</code>/<code>&#8211;help</code> option. </p>
<p> Include statements support the usual shell wildcard symbols (<code>,?,[]). Having no matches for an include statement is not an error, if wildcard symbols are used in the include statement. This allows having potentially empty include directories for statements like </code><code>include &quot;/etc/firewall/rules/</code><code>&quot;</code>. The wildcard matches are loaded in alphabetical order. Files beginning with dot (.) are not matched by include statements.</p>
<h3>Symbolic Variables</h3>
<dl>
<dd>
<pre><code>define</code> <i>variable</i> <code>=</code> <i>expr</i>
<code>undefine</code> <i>variable</i>
<code>redefine</code> <i>variable</i> <code>=</code> <i>expr</i>
<code>$variable</code></pre>
</dl>
<p> Symbolic variables can be defined using the <code>define</code> statement. Variable references are expressions and can be used to initialize other variables. The scope of a definition is the current block and all blocks contained within. Symbolic variables can be undefined using the <code>undefine</code> statement, and modified using the <code>redefine</code> statement. </p>
<p> <code>Using symbolic variables</code>. </p>
<dl>
<dd>
<pre>define int_if1 = eth0
define int_if2 = eth1
define int_ifs = { $int_if1, $int_if2 }
redefine int_if2 = wlan0
undefine int_if2
filter input iif $int_ifs accept</pre>
</dl>
<h2>Address Families</h2>
<p>Address families determine the type of packets which are processed. For each address family, the kernel contains so called hooks at specific stages of the packet processing paths, which invoke nftables if rules for these hooks exist. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>ip</code> </td>
<td>
<p> IPv4 address family.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>ip6</code> </td>
<td>
<p> IPv6 address family.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>inet</code> </td>
<td>
<p> Internet (IPv4/IPv6) address family.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>arp</code> </td>
<td>
<p> ARP address family, handling IPv4 ARP packets.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>bridge</code> </td>
<td>
<p> Bridge address family, handling packets which traverse a bridge device.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>netdev</code> </td>
<td>
<p> Netdev address family, handling packets on ingress and egress.
</td>
</tr>
</table>
<p> All nftables objects exist in address family specific namespaces, therefore all identifiers include an address family. If an identifier is specified without an address family, the <code>ip</code> family is used by default.</p>
<h3>Ipv4/Ipv6/Inet Address Families</h3>
<p>The IPv4/IPv6/Inet address families handle IPv4, IPv6 or both types of packets. They contain five hooks at different packet processing stages in the network stack. </p>
<p> <code>Table 1. IPv4/IPv6/Inet address family hooks</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Hook </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> prerouting </td>
<td>
<p> All packets entering the system are processed by the prerouting hook. It is invoked before the routing process and is used for early filtering or changing packet attributes that affect routing.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> input </td>
<td>
<p> Packets delivered to the local system are processed by the input hook.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> forward </td>
<td>
<p> Packets forwarded to a different host are processed by the forward hook.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> output </td>
<td>
<p> Packets sent by local processes are processed by the output hook.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> postrouting </td>
<td>
<p> All packets leaving the system are processed by the postrouting hook.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ingress </td>
<td>
<p> All packets entering the system are processed by this hook. It is invoked before layer 3 protocol handlers, hence before the prerouting hook, and it can be used for filtering and policing. Ingress is only available for Inet family (since Linux kernel 5.10).
</td>
</tr>
</table>
<h3>Arp Address Family</h3>
<p>The ARP address family handles ARP packets received and sent by the system. It is commonly used to mangle ARP packets for clustering. </p>
<p> <code>Table 2. ARP address family hooks</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Hook </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> input </td>
<td>
<p> Packets delivered to the local system are processed by the input hook.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> output </td>
<td>
<p> Packets send by the local system are processed by the output hook.
</td>
</tr>
</table>
<h3>Bridge Address Family</h3>
<p>The bridge address family handles Ethernet packets traversing bridge devices. </p>
<p> The list of supported hooks is identical to IPv4/IPv6/Inet address families above.</p>
<h3>Netdev Address Family</h3>
<p>The Netdev address family handles packets from the device ingress and egress path. This family allows you to filter packets of any ethertype such as ARP, VLAN 802.1q, VLAN 802.1ad (Q-in-Q) as well as IPv4 and IPv6 packets. </p>
<p> <code>Table 3. Netdev address family hooks</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Hook </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ingress </td>
<td>
<p> All packets entering the system are processed by this hook. It is invoked after the network taps (ie. <code>tcpdump</code>), right after <code>tc</code> ingress and before layer 3 protocol handlers, it can be used for early filtering and policing.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> egress </td>
<td>
<p> All packets leaving the system are processed by this hook. It is invoked after layer 3 protocol handlers and before <code>tc</code> egress. It can be used for late filtering and policing.
</td>
</tr>
</table>
<p> Tunneled packets (such as <code>vxlan</code>) are processed by netdev family hooks both in decapsulated and encapsulated (tunneled) form. So a packet can be filtered on the overlay network as well as on the underlying network. </p>
<p> Note that the order of netfilter and <code>tc</code> is mirrored on ingress versus egress. This ensures symmetry for NAT and other packet mangling. </p>
<p> Ingress packets which are redirected out some other interface are only processed by netfilter on egress if they have passed through netfilter ingress processing before. Thus, ingress packets which are redirected by <code>tc</code> are not subjected to netfilter. But they are if they are redirected by <code>netfilter</code> on ingress. Conceptually, tc and netfilter can be thought of as layers, with netfilter layered above tc: If the packet hasn&#8217;t been passed up from the tc layer to the netfilter layer, it&#8217;s not subjected to netfilter on egress.</p>
<h2>Ruleset</h2>
<dl>
<dd>
<pre>{<code>list</code> | <code>flush</code>} <code>ruleset</code> [<i>family</i>]</pre>
</dl>
<p> The <code>ruleset</code> keyword is used to identify the whole set of tables, chains, etc. currently in place in kernel. The following <code>ruleset</code> commands exist: </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>list</code> </td>
<td>
<p> Print the ruleset in human-readable format.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>flush</code> </td>
<td>
<p> Clear the whole ruleset. Note that, unlike iptables, this will remove all tables and whatever they contain, effectively leading to an empty ruleset &#8211; no packet filtering will happen anymore, so the kernel accepts any valid packet it receives.
</td>
</tr>
</table>
<p> It is possible to limit <code>list</code> and <code>flush</code> to a specific address family only. For a list of valid family names, see the section called &#8220;ADDRESS FAMILIES&#8221; above. </p>
<p> By design, <code>list ruleset</code> command output may be used as input to <code>nft -f</code>. Effectively, this is the nft-equivalent of <code>iptables-save</code> and <code>iptables-restore</code>.</p>
<h2>Tables</h2>
<dl>
<dd>
<pre>{<code>add</code> | <code>create</code>} <code>table</code> [<i>family</i>] <i>table</i> [ {<code>comment</code> <i>comment</i> <code>;</code><i>} </i><i></i><code>{ flags</code><i> 'flags</i> <code>; }</code>]
{<code>delete</code> | <code>list</code> | <code>flush</code>} <code>table</code> [<i>family</i>] <i>table</i>
<code>list tables</code> [<i>family</i>]
<code>delete table</code> [<i>family</i>] <code>handle</code> <i>handle</i></pre>
</dl>
<p> Tables are containers for chains, sets and stateful objects. They are identified by their address family and their name. The address family must be one of <code>ip</code>, <code>ip6</code>, <code>inet</code>, <code>arp</code>, <code>bridge</code>, <code>netdev</code>. The <code>inet</code> address family is a dummy family which is used to create hybrid IPv4/IPv6 tables. The <code>meta expression nfproto</code> keyword can be used to test which family (ipv4 or ipv6) context the packet is being processed in. When no address family is specified, <code>ip</code> is used by default. The only difference between add and create is that the former will not return an error if the specified table already exists while <code>create</code> will return an error. </p>
<p> <code>Table 4. Table flags</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Flag </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dormant </td>
<td>
<p> table is not evaluated any more (base chains are unregistered).
</td>
</tr>
</table>
<p> <code>Add, change, delete a table</code>. </p>
<dl>
<dd>
<pre># start nft in interactive mode
nft --interactive
# create a new table.
create table inet mytable
# add a new base chain: get input packets
add chain inet mytable myin { type filter hook input priority filter; }
# add a single counter to the chain
add rule inet mytable myin counter
# disable the table temporarily -- rules are not evaluated anymore
add table inet mytable { flags dormant; }
# make table active again:
add table inet mytable</pre>
</dl>
<table>
<tr VALIGN=top>
<td>
<p> <code>add</code> </td>
<td>
<p> Add a new table for the given family with the given name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>delete</code> </td>
<td>
<p> Delete the specified table.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>list</code> </td>
<td>
<p> List all chains and rules of the specified table.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>flush</code> </td>
<td>
<p> Flush all chains and rules of the specified table.
</td>
</tr>
</table>
<h2>Chains</h2>
<dl>
<dd>
<pre>{<code>add</code> | <code>create</code>} <code>chain</code> [<i>family</i>] <i>table</i> <i>chain</i> [<code>{ type</code> <i>type</i> <code>hook</code> <i>hook</i> [<code>device</code> <i>device</i>] <code>priority</code> <i>priority</i> <code>;</code> [<code>policy</code> <i>policy</i> <code>;</code>] [<code>comment</code> <i>comment</i> <code>;</code><i>] </i><i></i><code>}</code><i>]
{</i><i></i><code>delete</code><i> | </i><i></i><code>list</code><i> | </i><i></i><code>flush</code><i>} </i><i></i><code>chain</code><i> ['family</i>] <i>table</i> <i>chain</i>
<code>list chains</code> [<i>family</i>]
<code>delete chain</code> [<i>family</i>] <i>table</i> <code>handle</code> <i>handle</i>
<code>rename chain</code> [<i>family</i>] <i>table</i> <i>chain</i> <i>newname</i></pre>
</dl>
<p> Chains are containers for rules. They exist in two kinds, base chains and regular chains. A base chain is an entry point for packets from the networking stack, a regular chain may be used as jump target and is used for better rule organization. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>add</code> </td>
<td>
<p> Add a new chain in the specified table. When a hook and priority value are specified, the chain is created as a base chain and hooked up to the networking stack.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>create</code> </td>
<td>
<p> Similar to the <code>add</code> command, but returns an error if the chain already exists.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>delete</code> </td>
<td>
<p> Delete the specified chain. The chain must not contain any rules or be used as jump target.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>rename</code> </td>
<td>
<p> Rename the specified chain.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>list</code> </td>
<td>
<p> List all rules of the specified chain.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>flush</code> </td>
<td>
<p> Flush all rules of the specified chain.
</td>
</tr>
</table>
<p> For base chains, <code>type</code>, <code>hook</code> and <code>priority</code> parameters are mandatory. </p>
<p> <code>Table 5. Supported chain types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Type </code></td>
<td><code> Families </code></td>
<td><code> Hooks </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> filter </td>
<td>
<p> all </td>
<td>
<p> all </td>
<td>
<p> Standard chain type to use in doubt.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nat </td>
<td>
<p> ip, ip6, inet </td>
<td>
<p> prerouting, input, output, postrouting </td>
<td>
<p> Chains of this type perform Native Address Translation based on conntrack entries. Only the first packet of a connection actually traverses this chain &#8211; its rules usually define details of the created conntrack entry (NAT statements for instance).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> route </td>
<td>
<p> ip, ip6 </td>
<td>
<p> output </td>
<td>
<p> If a packet has traversed a chain of this type and is about to be accepted, a new route lookup is performed if relevant parts of the IP header have changed. This allows to e.g. implement policy routing selectors in nftables.
</td>
</tr>
</table>
<p> Apart from the special cases illustrated above (e.g. <code>nat</code> type not supporting <code>forward</code> hook or <code>route</code> type only supporting <code>output</code> hook), there are three further quirks worth noticing: </p>
<dl>
<dd>&bull; The netdev family supports merely two combinations, namely <code>filter</code> type with <code>ingress</code> hook and <code>filter</code> type with <code>egress</code> hook. Base chains in this family also require the <code>device</code> parameter to be present since they exist per interface only.</dl>
<dl>
<dd>&bull; The arp family supports only the <code>input</code> and <code>output</code> hooks, both in chains of type <code>filter</code>.</dl>
<dl>
<dd>&bull; The inet family also supports the <code>ingress</code> hook (since Linux kernel 5.10), to filter IPv4 and IPv6 packet at the same location as the netdev <code>ingress</code> hook. This inet hook allows you to share sets and maps between the usual <code>prerouting</code>, <code>input</code>, <code>forward</code>, <code>output</code>, <code>postrouting</code> and this <code>ingress</code> hook.</dl>
<p> The <code>priority</code> parameter accepts a signed integer value or a standard priority name which specifies the order in which chains with the same <code>hook</code> value are traversed. The ordering is ascending, i.e. lower priority values have precedence over higher ones. </p>
<p> Standard priority values can be replaced with easily memorizable names. Not all names make sense in every family with every hook (see the compatibility matrices below) but their numerical value can still be used for prioritizing chains. </p>
<p> These names and values are defined and made available based on what priorities are used by xtables when registering their default chains. </p>
<p> Most of the families use the same values, but bridge uses different ones from the others. See the following tables that describe the values and compatibility. </p>
<p> <code>Table 6. Standard priority names, family and hook compatibility matrix</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Value </code></td>
<td><code> Families </code></td>
<td><code> Hooks </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> raw </td>
<td>
<p> -300 </td>
<td>
<p> ip, ip6, inet </td>
<td>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mangle </td>
<td>
<p> -150 </td>
<td>
<p> ip, ip6, inet </td>
<td>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dstnat </td>
<td>
<p> -100 </td>
<td>
<p> ip, ip6, inet </td>
<td>
<p> prerouting
</td>
</tr>
<tr VALIGN=top>
<td>
<p> filter </td>
<td>
<p> 0 </td>
<td>
<p> ip, ip6, inet, arp, netdev </td>
<td>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td>
<p> security </td>
<td>
<p> 50 </td>
<td>
<p> ip, ip6, inet </td>
<td>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td>
<p> srcnat </td>
<td>
<p> 100 </td>
<td>
<p> ip, ip6, inet </td>
<td>
<p> postrouting
</td>
</tr>
</table>
<p> <code>Table 7. Standard priority names and hook compatibility for the bridge family</code> </p>
<table BORDER>
<tr VALIGN=top>
<td>
<p> Name </td>
<td>
<p> Value </td>
<td>
<p> Hooks
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dstnat </td>
<td>
<p> -300 </td>
<td>
<p> prerouting
</td>
</tr>
<tr VALIGN=top>
<td>
<p> filter </td>
<td>
<p> -200 </td>
<td>
<p> all
</td>
</tr>
<tr VALIGN=top>
<td>
<p> out </td>
<td>
<p> 100 </td>
<td>
<p> output
</td>
</tr>
<tr VALIGN=top>
<td>
<p> srcnat </td>
<td>
<p> 300 </td>
<td>
<p> postrouting
</td>
</tr>
</table>
<p> Basic arithmetic expressions (addition and subtraction) can also be achieved with these standard names to ease relative prioritizing, e.g. <code>mangle &#8211; 5</code> stands for <code>-155</code>. Values will also be printed like this until the value is not further than 10 from the standard value. </p>
<p> Base chains also allow to set the chain&#8217;s <code>policy</code>, i.e. what happens to packets not explicitly accepted or refused in contained rules. Supported policy values are <code>accept</code> (which is the default) or <code>drop</code>.</p>
<h2>Rules</h2>
<dl>
<dd>
<pre>{<code>add</code> | <code>insert</code>} <code>rule</code> [<i>family</i>] <i>table</i> <i>chain</i> [<code>handle</code> <i>handle</i> | <code>index</code> <i>index</i>] <i>statement</i> ... [<code>comment</code> <i>comment</i>]
<code>replace rule</code> [<i>family</i>] <i>table</i> <i>chain</i> <code>handle</code> <i>handle</i> <i>statement</i> ... [<code>comment</code> <i>comment</i>]
<code>delete rule</code> [<i>family</i>] <i>table</i> <i>chain</i> <code>handle</code> <i>handle</i></pre>
</dl>
<p> Rules are added to chains in the given table. If the family is not specified, the ip family is used. Rules are constructed from two kinds of components according to a set of grammatical rules: expressions and statements. </p>
<p> The add and insert commands support an optional location specifier, which is either a <i>handle</i> or the <i>index</i> (starting at zero) of an existing rule. Internally, rule locations are always identified by <i>handle</i> and the translation from <i>index</i> happens in userspace. This has two potential implications in case a concurrent ruleset change happens after the translation was done: The effective rule index might change if a rule was inserted or deleted before the referred one. If the referred rule was deleted, the command is rejected by the kernel just as if an invalid <i>handle</i> was given. </p>
<p> A <i>comment</i> is a single word or a double-quoted (&quot;) multi-word string which can be used to make notes regarding the actual rule. <code>Note:</code> If you use bash for adding rules, you have to escape the quotation marks, e.g. \&quot;enable ssh for servers\&quot;. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>add</code> </td>
<td>
<p> Add a new rule described by the list of statements. The rule is appended to the given chain unless a location is specified, in which case the rule is inserted after the specified rule.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>insert</code> </td>
<td>
<p> Same as <code>add</code> except the rule is inserted at the beginning of the chain or before the specified rule.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>replace</code> </td>
<td>
<p> Similar to <code>add</code>, but the rule replaces the specified rule.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>delete</code> </td>
<td>
<p> Delete the specified rule.
</td>
</tr>
</table>
<p> <code>add a rule to ip table output chain</code>. </p>
<dl>
<dd>
<pre>nft add rule filter output ip daddr 192.168.0.0/24 accept # 'ip filter' is assumed
# same command, slightly more verbose
nft add rule ip filter output ip daddr 192.168.0.0/24 accept</pre>
</dl>
<p> <code>delete rule from inet table</code>. </p>
<dl>
<dd>
<pre># nft -a list ruleset
table inet filter {
 chain input {
 type filter hook input priority filter; policy accept;
 ct state established,related accept # handle 4
 ip saddr 10.1.1.1 tcp dport ssh accept # handle 5
 ...
# delete the rule with handle 5
nft delete rule inet filter input handle 5</pre>
</dl>
<h2>Sets</h2>
<p>nftables offers two kinds of set concepts. Anonymous sets are sets that have no specific name. The set members are enclosed in curly braces, with commas to separate elements when creating the rule the set is used in. Once that rule is removed, the set is removed as well. They cannot be updated, i.e. once an anonymous set is declared it cannot be changed anymore except by removing/altering the rule that uses the anonymous set. </p>
<p> <code>Using anonymous sets to accept particular subnets and ports</code>. </p>
<dl>
<dd>
<pre>nft add rule filter input ip saddr { 10.0.0.0/8, 192.168.0.0/16 } tcp dport { 22, 443 } accept</pre>
</dl>
<p> Named sets are sets that need to be defined first before they can be referenced in rules. Unlike anonymous sets, elements can be added to or removed from a named set at any time. Sets are referenced from rules using an @ prefixed to the sets name. </p>
<p> <code>Using named sets to accept addresses and ports</code>. </p>
<dl>
<dd>
<pre>nft add rule filter input ip saddr @allowed_hosts tcp dport @allowed_ports accept</pre>
</dl>
<p> The sets allowed_hosts and allowed_ports need to be created first. The next section describes nft set syntax in more detail. </p>
<dl>
<dd>
<pre><code>add set</code> [<i>family</i>] <i>table</i> <i>set</i> <code>{ type</code> <i>type</i> | <code>typeof</code> <i>expression</i> <code>;</code> [<code>flags</code> <i>flags</i> <code>;</code>] [<code>timeout</code> <i>timeout</i> <code>;</code>] [<code>gc-interval</code> <i>gc-interval</i> <code>;</code>] [<code>elements = {</code> <i>element</i>[<code>,</code> ...] <code>} ;</code>] [<code>size</code> <i>size</i> <code>;</code>] [<code>comment</code> <i>comment</i> <code>;</code><i>] [</i><i></i><code>policy</code><i> 'policy</i> <code>;</code>] [<code>auto-merge ;</code>] <code>}</code>
{<code>delete</code> | <code>list</code> | <code>flush</code>} <code>set</code> [<i>family</i>] <i>table</i> <i>set</i>
<code>list sets</code> [<i>family</i>]
<code>delete set</code> [<i>family</i>] <i>table</i> <code>handle</code> <i>handle</i>
{<code>add</code> | <code>delete</code>} <code>element</code> [<i>family</i>] <i>table</i> <i>set</i> <code>{</code> <i>element</i>[<code>,</code> ...] <code>}</code></pre>
</dl>
<p> Sets are element containers of a user-defined data type, they are uniquely identified by a user-defined name and attached to tables. Their behaviour can be tuned with the flags that can be specified at set creation time. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>add</code> </td>
<td>
<p> Add a new set in the specified table. See the Set specification table below for more information about how to specify properties of a set.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>delete</code> </td>
<td>
<p> Delete the specified set.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>list</code> </td>
<td>
<p> Display the elements in the specified set.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>flush</code> </td>
<td>
<p> Remove all elements from the specified set.
</td>
</tr>
</table>
<p> <code>Table 8. Set specifications</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> data type of set elements </td>
<td>
<p> string: ipv4_addr, ipv6_addr, ether_addr, inet_proto, inet_service, mark
</td>
</tr>
<tr VALIGN=top>
<td>
<p> typeof </td>
<td>
<p> data type of set element </td>
<td>
<p> expression to derive the data type from
</td>
</tr>
<tr VALIGN=top>
<td>
<p> flags </td>
<td>
<p> set flags </td>
<td>
<p> string: constant, dynamic, interval, timeout
</td>
</tr>
<tr VALIGN=top>
<td>
<p> timeout </td>
<td>
<p> time an element stays in the set, mandatory if set is added to from the packet path (ruleset) </td>
<td>
<p> string, decimal followed by unit. Units are: d, h, m, s
</td>
</tr>
<tr VALIGN=top>
<td>
<p> gc-interval </td>
<td>
<p> garbage collection interval, only available when timeout or flag timeout are active </td>
<td>
<p> string, decimal followed by unit. Units are: d, h, m, s
</td>
</tr>
<tr VALIGN=top>
<td>
<p> elements </td>
<td>
<p> elements contained by the set </td>
<td>
<p> set data type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> size </td>
<td>
<p> maximum number of elements in the set, mandatory if set is added to from the packet path (ruleset) </td>
<td>
<p> unsigned integer (64 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> policy </td>
<td>
<p> set policy </td>
<td>
<p> string: performance [default], memory
</td>
</tr>
<tr VALIGN=top>
<td>
<p> auto-merge </td>
<td>
<p> automatic merge of adjacent/overlapping set elements (only for interval sets) </td>
<td>
</td>
</tr>
</table>
<h2>Maps</h2>
<dl>
<dd>
<pre><code>add map</code> [<i>family</i>] <i>table</i> <i>map</i> <code>{ type</code> <i>type</i> | <code>typeof</code> <i>expression</i> [<code>flags</code> <i>flags</i> <code>;</code>] [<code>elements = {</code> <i>element</i>[<code>,</code> ...] <code>} ;</code>] [<code>size</code> <i>size</i> <code>;</code>] [<code>comment</code> <i>comment</i> <code>;</code><i>] [</i><i></i><code>policy</code><i> 'policy</i> <code>;</code>] <code>}</code>
{<code>delete</code> | <code>list</code> | <code>flush</code>} <code>map</code> [<i>family</i>] <i>table</i> <i>map</i>
<code>list maps</code> [<i>family</i>]</pre>
</dl>
<p> Maps store data based on some specific key used as input. They are uniquely identified by a user-defined name and attached to tables. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>add</code> </td>
<td>
<p> Add a new map in the specified table.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>delete</code> </td>
<td>
<p> Delete the specified map.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>list</code> </td>
<td>
<p> Display the elements in the specified map.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>flush</code> </td>
<td>
<p> Remove all elements from the specified map.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>add element</code> </td>
<td>
<p> Comma-separated list of elements to add into the specified map.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>delete element</code> </td>
<td>
<p> Comma-separated list of element keys to delete from the specified map.
</td>
</tr>
</table>
<p> <code>Table 9. Map specifications</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> data type of map elements </td>
<td>
<p> string: ipv4_addr, ipv6_addr, ether_addr, inet_proto, inet_service, mark, counter, quota. Counter and quota can&#8217;t be used as keys
</td>
</tr>
<tr VALIGN=top>
<td>
<p> typeof </td>
<td>
<p> data type of set element </td>
<td>
<p> expression to derive the data type from
</td>
</tr>
<tr VALIGN=top>
<td>
<p> flags </td>
<td>
<p> map flags </td>
<td>
<p> string: constant, interval
</td>
</tr>
<tr VALIGN=top>
<td>
<p> elements </td>
<td>
<p> elements contained by the map </td>
<td>
<p> map data type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> size </td>
<td>
<p> maximum number of elements in the map </td>
<td>
<p> unsigned integer (64 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> policy </td>
<td>
<p> map policy </td>
<td>
<p> string: performance [default], memory
</td>
</tr>
</table>
<h2>Elements</h2>
<dl>
<dd>
<pre>{<code>add</code> | <code>create</code> | <code>delete</code> | <code>get</code> } <code>element</code> [<i>family</i>] <i>table</i> <i>set</i> <code>{</code> <i>ELEMENT</i>[<code>,</code> ...] <code>}</code>
<i>ELEMENT</i> := <i>key_expression</i> <i>OPTIONS</i> [<code>:</code> <i>value_expression</i>]
<i>OPTIONS</i> := [<code>timeout</code> <i>TIMESPEC</i>] [<code>expires</code> <i>TIMESPEC</i>] [<code>comment</code> <i>string</i>]
<i>TIMESPEC</i> := [<i>num</i><code>d</code>][<i>num</i><code>h</code>][<i>num</i><code>m</code>][<i>num</i>[<code>s</code>]]</pre>
</dl>
<p> Element-related commands allow to change contents of named sets and maps. <i>key_expression</i> is typically a value matching the set type. <i>value_expression</i> is not allowed in sets but mandatory when adding to maps, where it matches the data part in its type definition. When deleting from maps, it may be specified but is optional as <i>key_expression</i> uniquely identifies the element. </p>
<p> <code>create</code> command is similar to <code>add</code> with the exception that none of the listed elements may already exist. </p>
<p> <code>get</code> command is useful to check if an element is contained in a set which may be non-trivial in very large and/or interval sets. In the latter case, the containing interval is returned instead of just the element itself. </p>
<p> <code>Table 10. Element options</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Option </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> timeout </td>
<td>
<p> timeout value for sets/maps with flag <code>timeout</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> expires </td>
<td>
<p> the time until given element expires, useful for ruleset replication only
</td>
</tr>
<tr VALIGN=top>
<td>
<p> comment </td>
<td>
<p> per element comment field
</td>
</tr>
</table>
<h2>Flowtables</h2>
<dl>
<dd>
<pre>{<code>add</code> | <code>create</code>} <code>flowtable</code> [<i>family</i>] <i>table</i> <i>flowtable</i> <code>{ hook</code> <i>hook</i> <code>priority</code> <i>priority</i> <code>; devices = {</code> <i>device</i>[<code>,</code> ...] <code>} ; }</code>
<code>list flowtables</code> [<i>family</i>]
{<code>delete</code> | <code>list</code>} <code>flowtable</code> [<i>family</i>] <i>table</i> <i>flowtable</i>
<code>delete</code> <code>flowtable</code> [<i>family</i>] <i>table</i> <code>handle</code> <i>handle</i></pre>
</dl>
<p> Flowtables allow you to accelerate packet forwarding in software. Flowtables entries are represented through a tuple that is composed of the input interface, source and destination address, source and destination port; and layer 3/4 protocols. Each entry also caches the destination interface and the gateway address &#8211; to update the destination link-layer address &#8211; to forward packets. The ttl and hoplimit fields are also decremented. Hence, flowtables provides an alternative path that allow packets to bypass the classic forwarding path. Flowtables reside in the ingress hook that is located before the prerouting hook. You can select which flows you want to offload through the flow expression from the forward chain. Flowtables are identified by their address family and their name. The address family must be one of ip, ip6, or inet. The inet address family is a dummy family which is used to create hybrid IPv4/IPv6 tables. When no address family is specified, ip is used by default. </p>
<p> The <code>priority</code> can be a signed integer or <code>filter</code> which stands for 0. Addition and subtraction can be used to set relative priority, e.g. filter + 5 equals to 5. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>add</code> </td>
<td>
<p> Add a new flowtable for the given family with the given name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>delete</code> </td>
<td>
<p> Delete the specified flowtable.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>list</code> </td>
<td>
<p> List all flowtables.
</td>
</tr>
</table>
<h2>Listing</h2>
<dl>
<dd>
<pre><code>list { secmarks | synproxys | flow tables | meters | hooks }</code> [<i>family</i>]
<code>list { secmarks | synproxys | flow tables | meters | hooks } table</code> [<i>family</i>] <i>table</i>
<code>list ct { timeout | expectation | helper | helpers } table</code> [<i>family</i>] <i>table</i></pre>
</dl>
<p> Inspect configured objects. <code>list hooks</code> shows the full hook pipeline, including those registered by kernel modules, such as nf_conntrack.</p>
<h2>Stateful Objects</h2>
<dl>
<dd>
<pre>{<code>add</code> | <code>delete</code> | <code>list</code> | <code>reset</code>} <i>type</i> [<i>family</i>] <i>table</i> <i>object</i>
<code>delete</code> <i>type</i> [<i>family</i>] <i>table</i> <code>handle</code> <i>handle</i>
<code>list counters</code> [<i>family</i>]
<code>list quotas</code> [<i>family</i>]
<code>list limits</code> [<i>family</i>]</pre>
</dl>
<p> Stateful objects are attached to tables and are identified by a unique name. They group stateful information from rules, to reference them in rules the keywords &quot;type name&quot; are used e.g. &quot;counter name&quot;. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>add</code> </td>
<td>
<p> Add a new stateful object in the specified table.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>delete</code> </td>
<td>
<p> Delete the specified object.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>list</code> </td>
<td>
<p> Display stateful information the object holds.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>reset</code> </td>
<td>
<p> List-and-reset stateful object.
</td>
</tr>
</table>
<h3>Ct Helper</h3>
<dl>
<dd>
<pre><code>add</code> <code>ct helper</code> [<i>family</i>] <i>table</i> <i>name</i> <code>{ type</code> <i>type</i> <code>protocol</code> <i>protocol</i> <code>;</code> [<code>l3proto</code> <i>family</i> <code>;</code>] <code>}</code>
<code>delete</code> <code>ct helper</code> [<i>family</i>] <i>table</i> <i>name</i>
<code>list</code> <code>ct helpers</code></pre>
</dl>
<p> Ct helper is used to define connection tracking helpers that can then be used in combination with the <code>ct helper set</code> statement. <i>type</i> and <i>protocol</i> are mandatory, l3proto is derived from the table family by default, i.e. in the inet table the kernel will try to load both the ipv4 and ipv6 helper backends, if they are supported by the kernel. </p>
<p> <code>Table 11. conntrack helper specifications</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> name of helper type </td>
<td>
<p> quoted string (e.g. &quot;ftp&quot;)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> protocol </td>
<td>
<p> layer 4 protocol of the helper </td>
<td>
<p> string (e.g. ip)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> l3proto </td>
<td>
<p> layer 3 protocol of the helper </td>
<td>
<p> address family (e.g. ip)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> comment </td>
<td>
<p> per ct helper comment field </td>
<td>
<p> string
</td>
</tr>
</table>
<p> <code>defining and assigning ftp helper</code>. </p>
<dl>
<dd>
<pre>Unlike iptables, helper assignment needs to be performed after the conntrack
lookup has completed, for example with the default 0 hook priority.
table inet myhelpers {
 ct helper ftp-standard {
 type &quot;ftp&quot; protocol tcp
 }
 chain prerouting {
 type filter hook prerouting priority filter;
 tcp dport 21 ct helper set &quot;ftp-standard&quot;
 }
}</pre>
</dl>
<h3>Ct Timeout</h3>
<dl>
<dd>
<pre><code>add</code> <code>ct timeout</code> [<i>family</i>] <i>table</i> <i>name</i> <code>{ protocol</code> <i>protocol</i> <code>; policy = {</code> <i>state</i><code>:</code> <i>value</i> [<code>,</code> ...] <code>} ;</code> [<code>l3proto</code> <i>family</i> <code>;</code>] <code>}</code>
<code>delete</code> <code>ct timeout</code> [<i>family</i>] <i>table</i> <i>name</i>
<code>list</code> <code>ct timeouts</code></pre>
</dl>
<p> Ct timeout is used to update connection tracking timeout values.Timeout policies are assigned with the <code>ct timeout set</code> statement. <i>protocol</i> and <i>policy</i> are mandatory, l3proto is derived from the table family by default. </p>
<p> <code>Table 12. conntrack timeout specifications</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> protocol </td>
<td>
<p> layer 4 protocol of the timeout object </td>
<td>
<p> string (e.g. ip)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> state </td>
<td>
<p> connection state name </td>
<td>
<p> string (e.g. &quot;established&quot;)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> value </td>
<td>
<p> timeout value for connection state </td>
<td>
<p> unsigned integer
</td>
</tr>
<tr VALIGN=top>
<td>
<p> l3proto </td>
<td>
<p> layer 3 protocol of the timeout object </td>
<td>
<p> address family (e.g. ip)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> comment </td>
<td>
<p> per ct timeout comment field </td>
<td>
<p> string
</td>
</tr>
</table>
<p> tcp connection state names that can have a specific timeout value are: </p>
<p> <i>close</i>, <i>close_wait</i>, <i>established</i>, <i>fin_wait</i>, <i>last_ack</i>, <i>retrans</i>, <i>syn_recv</i>, <i>syn_sent</i>, <i>time_wait</i> and <i>unack</i>. </p>
<p> You can use <i>sysctl -a |grep net.netfilter.nf_conntrack_tcp_timeout_</i> to view and change the system-wide defaults. <i>ct timeout</i> allows for flow-specific settings, without changing the global timeouts. </p>
<p> For example, tcp port 53 could have much lower settings than other traffic. </p>
<p> udp state names that can have a specific timeout value are <i>replied</i> and <i>unreplied</i>. </p>
<p> <code>defining and assigning ct timeout policy</code>. </p>
<dl>
<dd>
<pre>table ip filter {
 ct timeout customtimeout {
 protocol tcp;
 l3proto ip
 policy = { established: 120, close: 20 }
 }
 chain output {
 type filter hook output priority filter; policy accept;
 ct timeout set &quot;customtimeout&quot;
 }
}</pre>
</dl>
<p> <code>testing the updated timeout policy</code>. </p>
<dl>
<dd>
<pre>% conntrack -E
It should display:
[UPDATE] tcp 6 120 ESTABLISHED src=172.16.19.128 dst=172.16.19.1
sport=22 dport=41360 [UNREPLIED] src=172.16.19.1 dst=172.16.19.128
sport=41360 dport=22</pre>
</dl>
<h3>Ct Expectation</h3>
<dl>
<dd>
<pre><code>add</code> <code>ct expectation</code> [<i>family</i>] <i>table</i> <i>name</i> <code>{ protocol</code> <i>protocol</i> <code>; dport</code> <i>dport</i> <code>; timeout</code> <i>timeout</i> <code>; size</code> <i>size</i> <code>; [*l3proto</code> <i>family</i> <code>;</code>] <code>}</code>
<code>delete</code> <code>ct expectation</code> [<i>family</i>] <i>table</i> <i>name</i>
<code>list</code> <code>ct expectations</code></pre>
</dl>
<p> Ct expectation is used to create connection expectations. Expectations are assigned with the <code>ct expectation set</code> statement. <i>protocol</i>, <i>dport</i>, <i>timeout</i> and <i>size</i> are mandatory, l3proto is derived from the table family by default. </p>
<p> <code>Table 13. conntrack expectation specifications</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> protocol </td>
<td>
<p> layer 4 protocol of the expectation object </td>
<td>
<p> string (e.g. ip)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dport </td>
<td>
<p> destination port of expected connection </td>
<td>
<p> unsigned integer
</td>
</tr>
<tr VALIGN=top>
<td>
<p> timeout </td>
<td>
<p> timeout value for expectation </td>
<td>
<p> unsigned integer
</td>
</tr>
<tr VALIGN=top>
<td>
<p> size </td>
<td>
<p> size value for expectation </td>
<td>
<p> unsigned integer
</td>
</tr>
<tr VALIGN=top>
<td>
<p> l3proto </td>
<td>
<p> layer 3 protocol of the expectation object </td>
<td>
<p> address family (e.g. ip)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> comment </td>
<td>
<p> per ct expectation comment field </td>
<td>
<p> string
</td>
</tr>
</table>
<p> <code>defining and assigning ct expectation policy</code>. </p>
<dl>
<dd>
<pre>table ip filter {
 ct expectation expect {
 protocol udp
 dport 9876
 timeout 2m
 size 8
 l3proto ip
 }
 chain input {
 type filter hook input priority filter; policy accept;
 ct expectation set &quot;expect&quot;
 }
}</pre>
</dl>
<h3>Counter</h3>
<dl>
<dd>
<pre><code>add</code> <code>counter</code> [<i>family</i>] <i>table</i> <i>name</i> [<code>{</code> [ <code>packets</code> <i>packets</i> <code>bytes</code> <i>bytes</i> <i>;</i> ] [ <code>comment</code> <i>comment</i> <i>;</i> <code>}</code>]
<code>delete</code> <code>counter</code> [<i>family</i>] <i>table</i> <i>name</i>
<code>list</code> <code>counters</code></pre>
</dl>
<p> <code>Table 14. Counter specifications</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> packets </td>
<td>
<p> initial count of packets </td>
<td>
<p> unsigned integer (64 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> bytes </td>
<td>
<p> initial count of bytes </td>
<td>
<p> unsigned integer (64 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> comment </td>
<td>
<p> per counter comment field </td>
<td>
<p> string
</td>
</tr>
</table>
<p> <code>Using named counters</code>. </p>
<dl>
<dd>
<pre>nft add counter filter http
nft add rule filter input tcp dport 80 counter name \&quot;http\&quot;</pre>
</dl>
<p> <code>Using named counters with maps</code>. </p>
<dl>
<dd>
<pre>nft add counter filter http
nft add counter filter https
nft add rule filter input counter name tcp dport map { 80 : \&quot;http\&quot;, 443 : \&quot;https\&quot; }</pre>
</dl>
<h3>Quota</h3>
<dl>
<dd>
<pre><code>add</code> <code>quota</code> [<i>family</i>] <i>table</i> <i>name</i> <code>{</code> [<code>over</code>|<code>until</code>] <i>bytes</i> <i>BYTE_UNIT</i> [ <code>used</code> <i>bytes</i> <i>BYTE_UNIT</i> ] <i>;</i> [ <code>comment</code> <i>comment</i> <i>;</i> ] <code>}</code>
BYTE_UNIT := bytes | kbytes | mbytes
<code>delete</code> <code>quota</code> [<i>family</i>] <i>table</i> <i>name</i>
<code>list</code> <code>quotas</code></pre>
</dl>
<p> <code>Table 15. Quota specifications</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> quota </td>
<td>
<p> quota limit, used as the quota name </td>
<td>
<p> Two arguments, unsigned integer (64 bit) and string: bytes, kbytes, mbytes. &quot;over&quot; and &quot;until&quot; go before these arguments
</td>
</tr>
<tr VALIGN=top>
<td>
<p> used </td>
<td>
<p> initial value of used quota </td>
<td>
<p> Two arguments, unsigned integer (64 bit) and string: bytes, kbytes, mbytes
</td>
</tr>
<tr VALIGN=top>
<td>
<p> comment </td>
<td>
<p> per quota comment field </td>
<td>
<p> string
</td>
</tr>
</table>
<p> <code>Using named quotas</code>. </p>
<dl>
<dd>
<pre>nft add quota filter user123 { over 20 mbytes }
nft add rule filter input ip saddr 192.168.10.123 quota name \&quot;user123\&quot;</pre>
</dl>
<p> <code>Using named quotas with maps</code>. </p>
<dl>
<dd>
<pre>nft add quota filter user123 { over 20 mbytes }
nft add quota filter user124 { over 20 mbytes }
nft add rule filter input quota name ip saddr map { 192.168.10.123 : \&quot;user123\&quot;, 192.168.10.124 : \&quot;user124\&quot; }</pre>
</dl>
<h2>Expressions</h2>
<p>Expressions represent values, either constants like network addresses, port numbers, etc., or data gathered from the packet during ruleset evaluation. Expressions can be combined using binary, logical, relational and other types of expressions to form complex or relational (match) expressions. They are also used as arguments to certain types of operations, like NAT, packet marking etc. </p>
<p> Each expression has a data type, which determines the size, parsing and representation of symbolic values and type compatibility with other expressions.</p>
<h3>Describe Command</h3>
<dl>
<dd>
<pre><code>describe</code> <i>expression</i> | <i>data type</i></pre>
</dl>
<p> The <code>describe</code> command shows information about the type of an expression and its data type. A data type may also be given, in which nft will display more information about the type. </p>
<p> <code>The describe command</code>. </p>
<dl>
<dd>
<pre>$ nft describe tcp flags
payload expression, datatype tcp_flag (TCP flag) (basetype bitmask, integer), 8 bits
predefined symbolic constants:
fin 0x01
syn 0x02
rst 0x04
psh 0x08
ack 0x10
urg 0x20
ecn 0x40
cwr 0x80</pre>
</dl>
<h2>Data Types</h2>
<p>Data types determine the size, parsing and representation of symbolic values and type compatibility of expressions. A number of global data types exist, in addition some expression types define further data types specific to the expression type. Most data types have a fixed size, some however may have a dynamic size, f.i. the string type. Some types also have predefined symbolic constants. Those can be listed using the nft <code>describe</code> command: </p>
<dl>
<dd>
<pre>$ nft describe ct_state
datatype ct_state (conntrack state) (basetype bitmask, integer), 32 bits
pre-defined symbolic constants (in hexadecimal):
invalid 0x00000001
new ...</pre>
</dl>
<p> Types may be derived from lower order types, f.i. the IPv4 address type is derived from the integer type, meaning an IPv4 address can also be specified as an integer value. </p>
<p> In certain contexts (set and map definitions), it is necessary to explicitly specify a data type. Each type has a name which is used for this.</p>
<h3>Integer Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Integer </td>
<td>
<p> integer </td>
<td>
<p> variable </td>
<td>
<p> &#8211;
</td>
</tr>
</table>
<p> The integer type is used for numeric values. It may be specified as a decimal, hexadecimal or octal number. The integer type does not have a fixed size, its size is determined by the expression for which it is used.</p>
<h3>Bitmask Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Bitmask </td>
<td>
<p> bitmask </td>
<td>
<p> variable </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The bitmask type (<code>bitmask</code>) is used for bitmasks.</p>
<h3>String Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> String </td>
<td>
<p> string </td>
<td>
<p> variable </td>
<td>
<p> &#8211;
</td>
</tr>
</table>
<p> The string type is used for character strings. A string begins with an alphabetic character (a-zA-Z) followed by zero or more alphanumeric characters or the characters /, -, _ and .. In addition, anything enclosed in double quotes (&quot;) is recognized as a string. </p>
<p> <code>String specification</code>. </p>
<dl>
<dd>
<pre># Interface name
filter input iifname eth0
# Weird interface name
filter input iifname &quot;(eth0)&quot;</pre>
</dl>
<h3>Link Layer Address Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Link layer address </td>
<td>
<p> lladdr </td>
<td>
<p> variable </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The link layer address type is used for link layer addresses. Link layer addresses are specified as a variable amount of groups of two hexadecimal digits separated using colons (:). </p>
<p> <code>Link layer address specification</code>. </p>
<dl>
<dd>
<pre># Ethernet destination MAC address
filter input ether daddr 20:c9:d0:43:12:d9</pre>
</dl>
<h3>Ipv4 Address Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> IPV4 address </td>
<td>
<p> ipv4_addr </td>
<td>
<p> 32 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The IPv4 address type is used for IPv4 addresses. Addresses are specified in either dotted decimal, dotted hexadecimal, dotted octal, decimal, hexadecimal, octal notation or as a host name. A host name will be resolved using the standard system resolver. </p>
<p> <code>IPv4 address specification</code>. </p>
<dl>
<dd>
<pre># dotted decimal notation
filter output ip daddr 127.0.0.1
# host name
filter output ip daddr localhost</pre>
</dl>
<h3>Ipv6 Address Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> IPv6 address </td>
<td>
<p> ipv6_addr </td>
<td>
<p> 128 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The IPv6 address type is used for IPv6 addresses. Addresses are specified as a host name or as hexadecimal halfwords separated by colons. Addresses might be enclosed in square brackets (&quot;[]&quot;) to differentiate them from port numbers. </p>
<p> <code>IPv6 address specification</code>. </p>
<dl>
<dd>
<pre># abbreviated loopback address
filter output ip6 daddr ::1</pre>
</dl>
<p> <code>IPv6 address specification with bracket notation</code>. </p>
<dl>
<dd>
<pre># without [] the port number (22) would be parsed as part of the
# ipv6 address
ip6 nat prerouting tcp dport 2222 dnat to [1ce::d0]:22</pre>
</dl>
<h3>Boolean Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> Boolean </td>
<td>
<p> boolean </td>
<td>
<p> 1 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The boolean type is a syntactical helper type in userspace. Its use is in the right-hand side of a (typically implicit) relational expression to change the expression on the left-hand side into a boolean check (usually for existence). </p>
<p> <code>Table 16. The following keywords will automatically resolve into a boolean type with given value</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> exists </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> missing </td>
<td>
<p> 0
</td>
</tr>
</table>
<p> <code>Table 17. expressions support a boolean comparison</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Expression </code></td>
<td><code> Behaviour </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> fib </td>
<td>
<p> Check route existence.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> exthdr </td>
<td>
<p> Check IPv6 extension header existence.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> tcp option </td>
<td>
<p> Check TCP option header existence.
</td>
</tr>
</table>
<p> <code>Boolean specification</code>. </p>
<dl>
<dd>
<pre># match if route exists
filter input fib daddr . iif oif exists
# match only non-fragmented packets in IPv6 traffic
filter input exthdr frag missing
# match if TCP timestamp option is present
filter input tcp option timestamp exists</pre>
</dl>
<h3>Icmp Type Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ICMP Type </td>
<td>
<p> icmp_type </td>
<td>
<p> 8 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The ICMP Type type is used to conveniently specify the ICMP header&#8217;s type field. </p>
<p> <code>Table 18. Keywords may be used when specifying the ICMP type</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> echo-reply </td>
<td>
<p> 0
</td>
</tr>
<tr VALIGN=top>
<td>
<p> destination-unreachable </td>
<td>
<p> 3
</td>
</tr>
<tr VALIGN=top>
<td>
<p> source-quench </td>
<td>
<p> 4
</td>
</tr>
<tr VALIGN=top>
<td>
<p> redirect </td>
<td>
<p> 5
</td>
</tr>
<tr VALIGN=top>
<td>
<p> echo-request </td>
<td>
<p> 8
</td>
</tr>
<tr VALIGN=top>
<td>
<p> router-advertisement </td>
<td>
<p> 9
</td>
</tr>
<tr VALIGN=top>
<td>
<p> router-solicitation </td>
<td>
<p> 10
</td>
</tr>
<tr VALIGN=top>
<td>
<p> time-exceeded </td>
<td>
<p> 11
</td>
</tr>
<tr VALIGN=top>
<td>
<p> parameter-problem </td>
<td>
<p> 12
</td>
</tr>
<tr VALIGN=top>
<td>
<p> timestamp-request </td>
<td>
<p> 13
</td>
</tr>
<tr VALIGN=top>
<td>
<p> timestamp-reply </td>
<td>
<p> 14
</td>
</tr>
<tr VALIGN=top>
<td>
<p> info-request </td>
<td>
<p> 15
</td>
</tr>
<tr VALIGN=top>
<td>
<p> info-reply </td>
<td>
<p> 16
</td>
</tr>
<tr VALIGN=top>
<td>
<p> address-mask-request </td>
<td>
<p> 17
</td>
</tr>
<tr VALIGN=top>
<td>
<p> address-mask-reply </td>
<td>
<p> 18
</td>
</tr>
</table>
<p> <code>ICMP Type specification</code>. </p>
<dl>
<dd>
<pre># match ping packets
filter output icmp type { echo-request, echo-reply }</pre>
</dl>
<h3>Icmp Code Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ICMP Code </td>
<td>
<p> icmp_code </td>
<td>
<p> 8 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The ICMP Code type is used to conveniently specify the ICMP header&#8217;s code field. </p>
<p> <code>Table 19. Keywords may be used when specifying the ICMP code</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> net-unreachable </td>
<td>
<p> 0
</td>
</tr>
<tr VALIGN=top>
<td>
<p> host-unreachable </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> prot-unreachable </td>
<td>
<p> 2
</td>
</tr>
<tr VALIGN=top>
<td>
<p> port-unreachable </td>
<td>
<p> 3
</td>
</tr>
<tr VALIGN=top>
<td>
<p> frag-needed </td>
<td>
<p> 4
</td>
</tr>
<tr VALIGN=top>
<td>
<p> net-prohibited </td>
<td>
<p> 9
</td>
</tr>
<tr VALIGN=top>
<td>
<p> host-prohibited </td>
<td>
<p> 10
</td>
</tr>
<tr VALIGN=top>
<td>
<p> admin-prohibited </td>
<td>
<p> 13
</td>
</tr>
</table>
<h3>Icmpv6 Type Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ICMPv6 Type </td>
<td>
<p> icmpx_code </td>
<td>
<p> 8 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The ICMPv6 Type type is used to conveniently specify the ICMPv6 header&#8217;s type field. </p>
<p> <code>Table 20. keywords may be used when specifying the ICMPv6 type:</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> destination-unreachable </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> packet-too-big </td>
<td>
<p> 2
</td>
</tr>
<tr VALIGN=top>
<td>
<p> time-exceeded </td>
<td>
<p> 3
</td>
</tr>
<tr VALIGN=top>
<td>
<p> parameter-problem </td>
<td>
<p> 4
</td>
</tr>
<tr VALIGN=top>
<td>
<p> echo-request </td>
<td>
<p> 128
</td>
</tr>
<tr VALIGN=top>
<td>
<p> echo-reply </td>
<td>
<p> 129
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mld-listener-query </td>
<td>
<p> 130
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mld-listener-report </td>
<td>
<p> 131
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mld-listener-done </td>
<td>
<p> 132
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mld-listener-reduction </td>
<td>
<p> 132
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nd-router-solicit </td>
<td>
<p> 133
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nd-router-advert </td>
<td>
<p> 134
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nd-neighbor-solicit </td>
<td>
<p> 135
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nd-neighbor-advert </td>
<td>
<p> 136
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nd-redirect </td>
<td>
<p> 137
</td>
</tr>
<tr VALIGN=top>
<td>
<p> router-renumbering </td>
<td>
<p> 138
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ind-neighbor-solicit </td>
<td>
<p> 141
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ind-neighbor-advert </td>
<td>
<p> 142
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mld2-listener-report </td>
<td>
<p> 143
</td>
</tr>
</table>
<p> <code>ICMPv6 Type specification</code>. </p>
<dl>
<dd>
<pre># match ICMPv6 ping packets
filter output icmpv6 type { echo-request, echo-reply }</pre>
</dl>
<h3>Icmpv6 Code Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ICMPv6 Code </td>
<td>
<p> icmpv6_code </td>
<td>
<p> 8 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The ICMPv6 Code type is used to conveniently specify the ICMPv6 header&#8217;s code field. </p>
<p> <code>Table 21. keywords may be used when specifying the ICMPv6 code</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> no-route </td>
<td>
<p> 0
</td>
</tr>
<tr VALIGN=top>
<td>
<p> admin-prohibited </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> addr-unreachable </td>
<td>
<p> 3
</td>
</tr>
<tr VALIGN=top>
<td>
<p> port-unreachable </td>
<td>
<p> 4
</td>
</tr>
<tr VALIGN=top>
<td>
<p> policy-fail </td>
<td>
<p> 5
</td>
</tr>
<tr VALIGN=top>
<td>
<p> reject-route </td>
<td>
<p> 6
</td>
</tr>
</table>
<h3>Icmpvx Code Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ICMPvX Code </td>
<td>
<p> icmpv6_type </td>
<td>
<p> 8 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The ICMPvX Code type abstraction is a set of values which overlap between ICMP and ICMPv6 Code types to be used from the inet family. </p>
<p> <code>Table 22. keywords may be used when specifying the ICMPvX code</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> no-route </td>
<td>
<p> 0
</td>
</tr>
<tr VALIGN=top>
<td>
<p> port-unreachable </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> host-unreachable </td>
<td>
<p> 2
</td>
</tr>
<tr VALIGN=top>
<td>
<p> admin-prohibited </td>
<td>
<p> 3
</td>
</tr>
</table>
<h3>Conntrack Types</h3>
<p><code>Table 23. overview of types used in ct expression and statement</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> conntrack state </td>
<td>
<p> ct_state </td>
<td>
<p> 4 byte </td>
<td>
<p> bitmask
</td>
</tr>
<tr VALIGN=top>
<td>
<p> conntrack direction </td>
<td>
<p> ct_dir </td>
<td>
<p> 8 bit </td>
<td>
<p> integer
</td>
</tr>
<tr VALIGN=top>
<td>
<p> conntrack status </td>
<td>
<p> ct_status </td>
<td>
<p> 4 byte </td>
<td>
<p> bitmask
</td>
</tr>
<tr VALIGN=top>
<td>
<p> conntrack event bits </td>
<td>
<p> ct_event </td>
<td>
<p> 4 byte </td>
<td>
<p> bitmask
</td>
</tr>
<tr VALIGN=top>
<td>
<p> conntrack label </td>
<td>
<p> ct_label </td>
<td>
<p> 128 bit </td>
<td>
<p> bitmask
</td>
</tr>
</table>
<p> For each of the types above, keywords are available for convenience: </p>
<p> <code>Table 24. conntrack state (ct_state)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> invalid </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> established </td>
<td>
<p> 2
</td>
</tr>
<tr VALIGN=top>
<td>
<p> related </td>
<td>
<p> 4
</td>
</tr>
<tr VALIGN=top>
<td>
<p> new </td>
<td>
<p> 8
</td>
</tr>
<tr VALIGN=top>
<td>
<p> untracked </td>
<td>
<p> 64
</td>
</tr>
</table>
<p> <code>Table 25. conntrack direction (ct_dir)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> original </td>
<td>
<p> 0
</td>
</tr>
<tr VALIGN=top>
<td>
<p> reply </td>
<td>
<p> 1
</td>
</tr>
</table>
<p> <code>Table 26. conntrack status (ct_status)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> expected </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> seen-reply </td>
<td>
<p> 2
</td>
</tr>
<tr VALIGN=top>
<td>
<p> assured </td>
<td>
<p> 4
</td>
</tr>
<tr VALIGN=top>
<td>
<p> confirmed </td>
<td>
<p> 8
</td>
</tr>
<tr VALIGN=top>
<td>
<p> snat </td>
<td>
<p> 16
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dnat </td>
<td>
<p> 32
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dying </td>
<td>
<p> 512
</td>
</tr>
</table>
<p> <code>Table 27. conntrack event bits (ct_event)</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> new </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> related </td>
<td>
<p> 2
</td>
</tr>
<tr VALIGN=top>
<td>
<p> destroy </td>
<td>
<p> 4
</td>
</tr>
<tr VALIGN=top>
<td>
<p> reply </td>
<td>
<p> 8
</td>
</tr>
<tr VALIGN=top>
<td>
<p> assured </td>
<td>
<p> 16
</td>
</tr>
<tr VALIGN=top>
<td>
<p> protoinfo </td>
<td>
<p> 32
</td>
</tr>
<tr VALIGN=top>
<td>
<p> helper </td>
<td>
<p> 64
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mark </td>
<td>
<p> 128
</td>
</tr>
<tr VALIGN=top>
<td>
<p> seqadj </td>
<td>
<p> 256
</td>
</tr>
<tr VALIGN=top>
<td>
<p> secmark </td>
<td>
<p> 512
</td>
</tr>
<tr VALIGN=top>
<td>
<p> label </td>
<td>
<p> 1024
</td>
</tr>
</table>
<p> Possible keywords for conntrack label type (ct_label) are read at runtime from /etc/connlabel.conf.</p>
<h3>Dccp Pkttype Type</h3>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Keyword </code></td>
<td><code> Size </code></td>
<td><code> Base type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> DCCP packet type </td>
<td>
<p> dccp_pkttype </td>
<td>
<p> 4 bit </td>
<td>
<p> integer
</td>
</tr>
</table>
<p> The DCCP packet type abstracts the different legal values of the respective four bit field in the DCCP header, as stated by RFC4340. Note that possible values 10-15 are considered reserved and therefore not allowed to be used. In iptables&#8217; <code>dccp</code> match, these values are aliased <i>INVALID</i>. With nftables, one may simply match on the numeric value range, i.e. <code>10-15</code>. </p>
<p> <code>Table 28. keywords may be used when specifying the DCCP packet type</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> request </td>
<td>
<p> 0
</td>
</tr>
<tr VALIGN=top>
<td>
<p> response </td>
<td>
<p> 1
</td>
</tr>
<tr VALIGN=top>
<td>
<p> data </td>
<td>
<p> 2
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ack </td>
<td>
<p> 3
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dataack </td>
<td>
<p> 4
</td>
</tr>
<tr VALIGN=top>
<td>
<p> closereq </td>
<td>
<p> 5
</td>
</tr>
<tr VALIGN=top>
<td>
<p> close </td>
<td>
<p> 6
</td>
</tr>
<tr VALIGN=top>
<td>
<p> reset </td>
<td>
<p> 7
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sync </td>
<td>
<p> 8
</td>
</tr>
<tr VALIGN=top>
<td>
<p> syncack </td>
<td>
<p> 9
</td>
</tr>
</table>
<h2>Primary Expressions</h2>
<p>The lowest order expression is a primary expression, representing either a constant or a single datum from a packet&#8217;s payload, meta data or a stateful module.</p>
<h3>Meta Expressions</h3>
<dl>
<dd>
<pre><code>meta</code> {<code>length</code> | <code>nfproto</code> | <code>l4proto</code> | <code>protocol</code> | <code>priority</code>}
[<code>meta</code>] {<code>mark</code> | <code>iif</code> | <code>iifname</code> | <code>iiftype</code> | <code>oif</code> | <code>oifname</code> | <code>oiftype</code> | <code>skuid</code> | <code>skgid</code> | <code>nftrace</code> | <code>rtclassid</code> | <code>ibrname</code> | <code>obrname</code> | <code>pkttype</code> | <code>cpu</code> | <code>iifgroup</code> | <code>oifgroup</code> | <code>cgroup</code> | <code>random</code> | <code>ipsec</code> | <code>iifkind</code> | <code>oifkind</code> | <code>time</code> | <code>hour</code> | <code>day</code> }</pre>
</dl>
<p> A meta expression refers to meta data associated with a packet. </p>
<p> There are two types of meta expressions: unqualified and qualified meta expressions. Qualified meta expressions require the meta keyword before the meta key, unqualified meta expressions can be specified by using the meta key directly or as qualified meta expressions. Meta l4proto is useful to match a particular transport protocol that is part of either an IPv4 or IPv6 packet. It will also skip any IPv6 extension headers present in an IPv6 packet. </p>
<p> meta iif, oif, iifname and oifname are used to match the interface a packet arrived on or is about to be sent out on. </p>
<p> iif and oif are used to match on the interface index, whereas iifname and oifname are used to match on the interface name. This is not the same &#8212; assuming the rule </p>
<dl>
<dd>
<pre>filter input meta iif &quot;foo&quot;</pre>
</dl>
<p> Then this rule can only be added if the interface &quot;foo&quot; exists. Also, the rule will continue to match even if the interface &quot;foo&quot; is renamed to &quot;bar&quot;. </p>
<p> This is because internally the interface index is used. In case of dynamically created interfaces, such as tun/tap or dialup interfaces (ppp for example), it might be better to use iifname or oifname instead. </p>
<p> In these cases, the name is used so the interface doesn&#8217;t have to exist to add such a rule, it will stop matching if the interface gets renamed and it will match again in case interface gets deleted and later a new interface with the same name is created. </p>
<p> Like with iptables, wildcard matching on interface name prefixes is available for <code>iifname</code> and <code>oifname</code> matches by appending an asterisk (*) character. Note however that unlike iptables, nftables does not accept interface names consisting of the wildcard character only &#8211; users are supposed to just skip those always matching expressions. In order to match on literal asterisk character, one may escape it using backslash (\). </p>
<p> <code>Table 29. Meta expression types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> length </td>
<td>
<p> Length of the packet in bytes </td>
<td>
<p> integer (32-bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nfproto </td>
<td>
<p> real hook protocol family, useful only in inet table </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> l4proto </td>
<td>
<p> layer 4 protocol, skips ipv6 extension headers </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> protocol </td>
<td>
<p> EtherType protocol value </td>
<td>
<p> ether_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> priority </td>
<td>
<p> TC packet priority </td>
<td>
<p> tc_handle
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mark </td>
<td>
<p> Packet mark </td>
<td>
<p> mark
</td>
</tr>
<tr VALIGN=top>
<td>
<p> iif </td>
<td>
<p> Input interface index </td>
<td>
<p> iface_index
</td>
</tr>
<tr VALIGN=top>
<td>
<p> iifname </td>
<td>
<p> Input interface name </td>
<td>
<p> ifname
</td>
</tr>
<tr VALIGN=top>
<td>
<p> iiftype </td>
<td>
<p> Input interface type </td>
<td>
<p> iface_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oif </td>
<td>
<p> Output interface index </td>
<td>
<p> iface_index
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oifname </td>
<td>
<p> Output interface name </td>
<td>
<p> ifname
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oiftype </td>
<td>
<p> Output interface hardware type </td>
<td>
<p> iface_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sdif </td>
<td>
<p> Slave device input interface index </td>
<td>
<p> iface_index
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sdifname </td>
<td>
<p> Slave device interface name </td>
<td>
<p> ifname
</td>
</tr>
<tr VALIGN=top>
<td>
<p> skuid </td>
<td>
<p> UID associated with originating socket </td>
<td>
<p> uid
</td>
</tr>
<tr VALIGN=top>
<td>
<p> skgid </td>
<td>
<p> GID associated with originating socket </td>
<td>
<p> gid
</td>
</tr>
<tr VALIGN=top>
<td>
<p> rtclassid </td>
<td>
<p> Routing realm </td>
<td>
<p> realm
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ibrname </td>
<td>
<p> Input bridge interface name </td>
<td>
<p> ifname
</td>
</tr>
<tr VALIGN=top>
<td>
<p> obrname </td>
<td>
<p> Output bridge interface name </td>
<td>
<p> ifname
</td>
</tr>
<tr VALIGN=top>
<td>
<p> pkttype </td>
<td>
<p> packet type </td>
<td>
<p> pkt_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cpu </td>
<td>
<p> cpu number processing the packet </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> iifgroup </td>
<td>
<p> incoming device group </td>
<td>
<p> devgroup
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oifgroup </td>
<td>
<p> outgoing device group </td>
<td>
<p> devgroup
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cgroup </td>
<td>
<p> control group id </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> random </td>
<td>
<p> pseudo-random number </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ipsec </td>
<td>
<p> true if packet was ipsec encrypted </td>
<td>
<p> boolean (1 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> iifkind </td>
<td>
<p> Input interface kind </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oifkind </td>
<td>
<p> Output interface kind </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> time </td>
<td>
<p> Absolute time of packet reception </td>
<td>
<p> Integer (32 bit) or string
</td>
</tr>
<tr VALIGN=top>
<td>
<p> day </td>
<td>
<p> Day of week </td>
<td>
<p> Integer (8 bit) or string
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hour </td>
<td>
<p> Hour of day </td>
<td>
<p> String
</td>
</tr>
</table>
<p> <code>Table 30. Meta expression specific types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> iface_index </td>
<td>
<p> Interface index (32 bit number). Can be specified numerically or as name of an existing interface.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ifname </td>
<td>
<p> Interface name (16 byte string). Does not have to exist.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> iface_type </td>
<td>
<p> Interface type (16 bit number).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> uid </td>
<td>
<p> User ID (32 bit number). Can be specified numerically or as user name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> gid </td>
<td>
<p> Group ID (32 bit number). Can be specified numerically or as group name.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> realm </td>
<td>
<p> Routing Realm (32 bit number). Can be specified numerically or as symbolic name defined in /etc/iproute2/rt_realms.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> devgroup_type </td>
<td>
<p> Device group (32 bit number). Can be specified numerically or as symbolic name defined in /etc/iproute2/group.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> pkt_type </td>
<td>
<p> Packet type: <code>host</code> (addressed to local host), <code>broadcast</code> (to all), <code>multicast</code> (to group), <code>other</code> (addressed to another host).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ifkind </td>
<td>
<p> Interface kind (16 byte string). See TYPES in <a href="/docs/linux/man/8-ip-link/">ip-link</a>(8) for a list.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> time </td>
<td>
<p> Either an integer or a date in ISO format. For example: &quot;2019-06-06 17:00&quot;. Hour and seconds are optional and can be omitted if desired. If omitted, midnight will be assumed. The following three would be equivalent: &quot;2019-06-06&quot;, &quot;2019-06-06 00:00&quot; and &quot;2019-06-06 00:00:00&quot;. When an integer is given, it is assumed to be a UNIX timestamp.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> day </td>
<td>
<p> Either a day of week (&quot;Monday&quot;, &quot;Tuesday&quot;, etc.), or an integer between 0 and 6. Strings are matched case-insensitively, and a full match is not expected (e.g. &quot;Mon&quot; would match &quot;Monday&quot;). When an integer is given, 0 is Sunday and 6 is Saturday.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hour </td>
<td>
<p> A string representing an hour in 24-hour format. Seconds can optionally be specified. For example, 17:00 and 17:00:00 would be equivalent.
</td>
</tr>
</table>
<p> <code>Using meta expressions</code>. </p>
<dl>
<dd>
<pre># qualified meta expression
filter output meta oif eth0
filter forward meta iifkind { &quot;tun&quot;, &quot;veth&quot; }
# unqualified meta expression
filter output oif eth0
# incoming packet was subject to ipsec processing
raw prerouting meta ipsec exists accept</pre>
</dl>
<h3>Socket Expression</h3>
<dl>
<dd>
<pre><code>socket</code> {<code>transparent</code> | <code>mark</code> | <code>wildcard</code>}
<code>socket</code> <code>cgroupv2</code> <code>level</code> <i>NUM</i></pre>
</dl>
<p> Socket expression can be used to search for an existing open TCP/UDP socket and its attributes that can be associated with a packet. It looks for an established or non-zero bound listening socket (possibly with a non-local address). You can also use it to match on the socket cgroupv2 at a given ancestor level, e.g. if the socket belongs to cgroupv2 <i>a/b</i>, ancestor level 1 checks for a matching on cgroup <i>a</i> and ancestor level 2 checks for a matching on cgroup <i>b</i>. </p>
<p> <code>Table 31. Available socket attributes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> transparent </td>
<td>
<p> Value of the IP_TRANSPARENT socket option in the found socket. It can be 0 or 1. </td>
<td>
<p> boolean (1 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mark </td>
<td>
<p> Value of the socket mark (SOL_SOCKET, SO_MARK). </td>
<td>
<p> mark
</td>
</tr>
<tr VALIGN=top>
<td>
<p> wildcard </td>
<td>
<p> Indicates whether the socket is wildcard-bound (e.g. 0.0.0.0 or ::0). </td>
<td>
<p> boolean (1 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cgroupv2 </td>
<td>
<p> cgroup version 2 for this socket (path from /sys/fs/cgroup) </td>
<td>
<p> cgroupv2
</td>
</tr>
</table>
<p> <code>Using socket expression</code>. </p>
<dl>
<dd>
<pre># Mark packets that correspond to a transparent socket. &quot;socket wildcard 0&quot;
# means that zero-bound listener sockets are NOT matched (which is usually
# exactly what you want).
table inet x {
 chain y {
 type filter hook prerouting priority mangle; policy accept;
 socket transparent 1 socket wildcard 0 mark set 0x00000001 accept
 }
}
# Trace packets that corresponds to a socket with a mark value of 15
table inet x {
 chain y {
 type filter hook prerouting priority mangle; policy accept;
 socket mark 0x0000000f nftrace set 1
 }
}
# Set packet mark to socket mark
table inet x {
 chain y {
 type filter hook prerouting priority mangle; policy accept;
 tcp dport 8080 mark set socket mark
 }
}
# Count packets for cgroupv2 &quot;user.slice&quot; at level 1
table inet x {
 chain y {
 type filter hook input priority filter; policy accept;
 socket cgroupv2 level 1 &quot;user.slice&quot; counter
 }
}</pre>
</dl>
<h3>Osf Expression</h3>
<dl>
<dd>
<pre><code>osf</code> [<code>ttl</code> {<code>loose</code> | <code>skip</code>}] {<code>name</code> | <code>version</code>}</pre>
</dl>
<p> The osf expression does passive operating system fingerprinting. This expression compares some data (Window Size, MSS, options and their order, DF, and others) from packets with the SYN bit set. </p>
<p> <code>Table 32. Available osf attributes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ttl </td>
<td>
<p> Do TTL checks on the packet to determine the operating system. </td>
<td>
<p> string
</td>
</tr>
<tr VALIGN=top>
<td>
<p> version </td>
<td>
<p> Do OS version checks on the packet. </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> name </td>
<td>
<p> Name of the OS signature to match. All signatures can be found at pf.os file. Use &quot;unknown&quot; for OS signatures that the expression could not detect. </td>
<td>
<p> string
</td>
</tr>
</table>
<p> <code>Available ttl values</code>. </p>
<dl>
<dd>
<pre>If no TTL attribute is passed, make a true IP header and fingerprint TTL true comparison. This generally works for LANs.
* loose: Check if the IP header's TTL is less than the fingerprint one. Works for globally-routable addresses.
* skip: Do not compare the TTL at all.</pre>
</dl>
<p> <code>Using osf expression</code>. </p>
<dl>
<dd>
<pre># Accept packets that match the &quot;Linux&quot; OS genre signature without comparing TTL.
table inet x {
 chain y {
 type filter hook input priority filter; policy accept;
 osf ttl skip name &quot;Linux&quot;
 }
}</pre>
</dl>
<h3>Fib Expressions</h3>
<dl>
<dd>
<pre><code>fib</code> {<code>saddr</code> | <code>daddr</code> | <code>mark</code> | <code>iif</code> | <code>oif</code>} [<code>.</code> ...] {<code>oif</code> | <code>oifname</code> | <code>type</code>}</pre>
</dl>
<p> A fib expression queries the fib (forwarding information base) to obtain information such as the output interface index a particular address would use. The input is a tuple of elements that is used as input to the fib lookup functions. </p>
<p> <code>Table 33. fib expression specific types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oif </td>
<td>
<p> Output interface index </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> oifname </td>
<td>
<p> Output interface name </td>
<td>
<p> string
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> Address type </td>
<td>
<p> fib_addrtype
</td>
</tr>
</table>
<p> Use <code>nft</code> <code>describe</code> <code>fib_addrtype</code> to get a list of all address types. </p>
<p> <code>Using fib expressions</code>. </p>
<dl>
<dd>
<pre># drop packets without a reverse path
filter prerouting fib saddr . iif oif missing drop
In this example, 'saddr . iif' looks up routing information based on the source address and the input interface.
oif picks the output interface index from the routing information.
If no route was found for the source address/input interface combination, the output interface index is zero.
In case the input interface is specified as part of the input key, the output interface index is always the same as the input interface index or zero.
If only 'saddr oif' is given, then oif can be any interface index or zero.
# drop packets to address not configured on incoming interface
filter prerouting fib daddr . iif type != { local, broadcast, multicast } drop
# perform lookup in a specific 'blackhole' table (0xdead, needs ip appropriate ip rule)
filter prerouting meta mark set 0xdead fib daddr . mark type vmap { blackhole : drop, prohibit : jump prohibited, unreachable : drop }</pre>
</dl>
<h3>Routing Expressions</h3>
<dl>
<dd>
<pre><code>rt</code> [<code>ip</code> | <code>ip6</code>] {<code>classid</code> | <code>nexthop</code> | <code>mtu</code> | <code>ipsec</code>}</pre>
</dl>
<p> A routing expression refers to routing data associated with a packet. </p>
<p> <code>Table 34. Routing expression types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> classid </td>
<td>
<p> Routing realm </td>
<td>
<p> realm
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nexthop </td>
<td>
<p> Routing nexthop </td>
<td>
<p> ipv4_addr/ipv6_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mtu </td>
<td>
<p> TCP maximum segment size of route </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ipsec </td>
<td>
<p> route via ipsec tunnel or transport </td>
<td>
<p> boolean
</td>
</tr>
</table>
<p> <code>Table 35. Routing expression specific types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> realm </td>
<td>
<p> Routing Realm (32 bit number). Can be specified numerically or as symbolic name defined in /etc/iproute2/rt_realms.
</td>
</tr>
</table>
<p> <code>Using routing expressions</code>. </p>
<dl>
<dd>
<pre># IP family independent rt expression
filter output rt classid 10
# IP family dependent rt expressions
ip filter output rt nexthop 192.168.0.1
ip6 filter output rt nexthop fd00::1
inet filter output rt ip nexthop 192.168.0.1
inet filter output rt ip6 nexthop fd00::1
# outgoing packet will be encapsulated/encrypted by ipsec
filter output rt ipsec exists</pre>
</dl>
<h3>Ipsec Expressions</h3>
<dl>
<dd>
<pre><code>ipsec</code> {<code>in</code> | <code>out</code>} [ <code>spnum</code> <i>NUM</i> ] {<code>reqid</code> | <code>spi</code>}
<code>ipsec</code> {<code>in</code> | <code>out</code>} [ <code>spnum</code> <i>NUM</i> ] {<code>ip</code> | <code>ip6</code>} {<code>saddr</code> | <code>daddr</code>}</pre>
</dl>
<p> An ipsec expression refers to ipsec data associated with a packet. </p>
<p> The <i>in</i> or <i>out</i> keyword needs to be used to specify if the expression should examine inbound or outbound policies. The <i>in</i> keyword can be used in the prerouting, input and forward hooks. The <i>out</i> keyword applies to forward, output and postrouting hooks. The optional keyword spnum can be used to match a specific state in a chain, it defaults to 0. </p>
<p> <code>Table 36. Ipsec expression types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> reqid </td>
<td>
<p> Request ID </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> spi </td>
<td>
<p> Security Parameter Index </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> saddr </td>
<td>
<p> Source address of the tunnel </td>
<td>
<p> ipv4_addr/ipv6_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> daddr </td>
<td>
<p> Destination address of the tunnel </td>
<td>
<p> ipv4_addr/ipv6_addr
</td>
</tr>
</table>
<h3>Numgen Expression</h3>
<dl>
<dd>
<pre><code>numgen</code> {<code>inc</code> | <code>random</code>} <code>mod</code> <i>NUM</i> [ <code>offset</code> <i>NUM</i> ]</pre>
</dl>
<p> Create a number generator. The <code>inc</code> or <code>random</code> keywords control its operation mode: In <code>inc</code> mode, the last returned value is simply incremented. In <code>random</code> mode, a new random number is returned. The value after <code>mod</code> keyword specifies an upper boundary (read: modulus) which is not reached by returned numbers. The optional <code>offset</code> allows to increment the returned value by a fixed offset. </p>
<p> A typical use-case for <code>numgen</code> is load-balancing: </p>
<p> <code>Using numgen expression</code>. </p>
<dl>
<dd>
<pre># round-robin between 192.168.10.100 and 192.168.20.200:
add rule nat prerouting dnat to numgen inc mod 2 map \
 { 0 : 192.168.10.100, 1 : 192.168.20.200 }
# probability-based with odd bias using intervals:
add rule nat prerouting dnat to numgen random mod 10 map \
 { 0-2 : 192.168.10.100, 3-9 : 192.168.20.200 }</pre>
</dl>
<h3>Hash Expressions</h3>
<dl>
<dd>
<pre><code>jhash</code> {<code>ip saddr</code> | <code>ip6 daddr</code> | <code>tcp dport</code> | <code>udp sport</code> | <code>ether saddr</code>} [<code>.</code> ...] <code>mod</code> <i>NUM</i> [ <code>seed</code> <i>NUM</i> ] [ <code>offset</code> <i>NUM</i> ]
<code>symhash</code> <code>mod</code> <i>NUM</i> [ <code>offset</code> <i>NUM</i> ]</pre>
</dl>
<p> Use a hashing function to generate a number. The functions available are <code>jhash</code>, known as Jenkins Hash, and <code>symhash</code>, for Symmetric Hash. The <code>jhash</code> requires an expression to determine the parameters of the packet header to apply the hashing, concatenations are possible as well. The value after <code>mod</code> keyword specifies an upper boundary (read: modulus) which is not reached by returned numbers. The optional <code>seed</code> is used to specify an init value used as seed in the hashing function. The optional <code>offset</code> allows to increment the returned value by a fixed offset. </p>
<p> A typical use-case for <code>jhash</code> and <code>symhash</code> is load-balancing: </p>
<p> <code>Using hash expressions</code>. </p>
<dl>
<dd>
<pre># load balance based on source ip between 2 ip addresses:
add rule nat prerouting dnat to jhash ip saddr mod 2 map \
 { 0 : 192.168.10.100, 1 : 192.168.20.200 }
# symmetric load balancing between 2 ip addresses:
add rule nat prerouting dnat to symhash mod 2 map \
 { 0 : 192.168.10.100, 1 : 192.168.20.200 }</pre>
</dl>
<h2>Payload Expressions</h2>
<p>Payload expressions refer to data from the packet&#8217;s payload.</p>
<h3>Ethernet Header Expression</h3>
<dl>
<dd>
<pre><code>ether</code> {<code>daddr</code> | <code>saddr</code> | <code>type</code>}</pre>
</dl>
<p> <code>Table 37. Ethernet header expression types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> daddr </td>
<td>
<p> Destination MAC address </td>
<td>
<p> ether_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> saddr </td>
<td>
<p> Source MAC address </td>
<td>
<p> ether_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> EtherType </td>
<td>
<p> ether_type
</td>
</tr>
</table>
<h3>Vlan Header Expression</h3>
<dl>
<dd>
<pre><code>vlan</code> {<code>id</code> | <code>dei</code> | <code>pcp</code> | <code>type</code>}</pre>
</dl>
<p> <code>Table 38. VLAN header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> id </td>
<td>
<p> VLAN ID (VID) </td>
<td>
<p> integer (12 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dei </td>
<td>
<p> Drop Eligible Indicator </td>
<td>
<p> integer (1 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> pcp </td>
<td>
<p> Priority code point </td>
<td>
<p> integer (3 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> EtherType </td>
<td>
<p> ether_type
</td>
</tr>
</table>
<h3>Arp Header Expression</h3>
<dl>
<dd>
<pre><code>arp</code> {<code>htype</code> | <code>ptype</code> | <code>hlen</code> | <code>plen</code> | <code>operation</code> | <code>saddr</code> { <code>ip</code> | <code>ether</code> } | <code>daddr</code> { <code>ip</code> | <code>ether</code> }</pre>
</dl>
<p> <code>Table 39. ARP header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> htype </td>
<td>
<p> ARP hardware type </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ptype </td>
<td>
<p> EtherType </td>
<td>
<p> ether_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hlen </td>
<td>
<p> Hardware address len </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> plen </td>
<td>
<p> Protocol address len </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> operation </td>
<td>
<p> Operation </td>
<td>
<p> arp_op
</td>
</tr>
<tr VALIGN=top>
<td>
<p> saddr ether </td>
<td>
<p> Ethernet sender address </td>
<td>
<p> ether_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> daddr ether </td>
<td>
<p> Ethernet target address </td>
<td>
<p> ether_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> saddr ip </td>
<td>
<p> IPv4 sender address </td>
<td>
<p> ipv4_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> daddr ip </td>
<td>
<p> IPv4 target address </td>
<td>
<p> ipv4_addr
</td>
</tr>
</table>
<h3>Ipv4 Header Expression</h3>
<dl>
<dd>
<pre><code>ip</code> {<code>version</code> | <code>hdrlength</code> | <code>dscp</code> | <code>ecn</code> | <code>length</code> | <code>id</code> | <code>frag-off</code> | <code>ttl</code> | <code>protocol</code> | <code>checksum</code> | <code>saddr</code> | <code>daddr</code> }</pre>
</dl>
<p> <code>Table 40. IPv4 header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> version </td>
<td>
<p> IP header version (4) </td>
<td>
<p> integer (4 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hdrlength </td>
<td>
<p> IP header length including options </td>
<td>
<p> integer (4 bit) FIXME scaling
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dscp </td>
<td>
<p> Differentiated Services Code Point </td>
<td>
<p> dscp
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ecn </td>
<td>
<p> Explicit Congestion Notification </td>
<td>
<p> ecn
</td>
</tr>
<tr VALIGN=top>
<td>
<p> length </td>
<td>
<p> Total packet length </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> id </td>
<td>
<p> IP ID </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> frag-off </td>
<td>
<p> Fragment offset </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ttl </td>
<td>
<p> Time to live </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> protocol </td>
<td>
<p> Upper layer protocol </td>
<td>
<p> inet_proto
</td>
</tr>
<tr VALIGN=top>
<td>
<p> checksum </td>
<td>
<p> IP header checksum </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> saddr </td>
<td>
<p> Source address </td>
<td>
<p> ipv4_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> daddr </td>
<td>
<p> Destination address </td>
<td>
<p> ipv4_addr
</td>
</tr>
</table>
<h3>Icmp Header Expression</h3>
<dl>
<dd>
<pre><code>icmp</code> {<code>type</code> | <code>code</code> | <code>checksum</code> | <code>id</code> | <code>sequence</code> | <code>gateway</code> | <code>mtu</code>}</pre>
</dl>
<p> This expression refers to ICMP header fields. When using it in <code>inet</code>, <code>bridge</code> or <code>netdev</code> families, it will cause an implicit dependency on IPv4 to be created. To match on unusual cases like ICMP over IPv6, one has to add an explicit <code>meta protocol ip6</code> match to the rule. </p>
<p> <code>Table 41. ICMP header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> ICMP type field </td>
<td>
<p> icmp_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> code </td>
<td>
<p> ICMP code field </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> checksum </td>
<td>
<p> ICMP checksum field </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> id </td>
<td>
<p> ID of echo request/response </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sequence </td>
<td>
<p> sequence number of echo request/response </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> gateway </td>
<td>
<p> gateway of redirects </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mtu </td>
<td>
<p> MTU of path MTU discovery </td>
<td>
<p> integer (16 bit)
</td>
</tr>
</table>
<h3>Igmp Header Expression</h3>
<dl>
<dd>
<pre><code>igmp</code> {<code>type</code> | <code>mrt</code> | <code>checksum</code> | <code>group</code>}</pre>
</dl>
<p> This expression refers to IGMP header fields. When using it in <code>inet</code>, <code>bridge</code> or <code>netdev</code> families, it will cause an implicit dependency on IPv4 to be created. To match on unusual cases like IGMP over IPv6, one has to add an explicit <code>meta protocol ip6</code> match to the rule. </p>
<p> <code>Table 42. IGMP header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> IGMP type field </td>
<td>
<p> igmp_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mrt </td>
<td>
<p> IGMP maximum response time field </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> checksum </td>
<td>
<p> IGMP checksum field </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> group </td>
<td>
<p> Group address </td>
<td>
<p> integer (32 bit)
</td>
</tr>
</table>
<h3>Ipv6 Header Expression</h3>
<dl>
<dd>
<pre><code>ip6</code> {<code>version</code> | <code>dscp</code> | <code>ecn</code> | <code>flowlabel</code> | <code>length</code> | <code>nexthdr</code> | <code>hoplimit</code> | <code>saddr</code> | <code>daddr</code>}</pre>
</dl>
<p> This expression refers to the ipv6 header fields. Caution when using <code>ip6 nexthdr</code>, the value only refers to the next header, i.e. <code>ip6 nexthdr tcp</code> will only match if the ipv6 packet does not contain any extension headers. Packets that are fragmented or e.g. contain a routing extension headers will not be matched. Please use <code>meta l4proto</code> if you wish to match the real transport header and ignore any additional extension headers instead. </p>
<p> <code>Table 43. IPv6 header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> version </td>
<td>
<p> IP header version (6) </td>
<td>
<p> integer (4 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dscp </td>
<td>
<p> Differentiated Services Code Point </td>
<td>
<p> dscp
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ecn </td>
<td>
<p> Explicit Congestion Notification </td>
<td>
<p> ecn
</td>
</tr>
<tr VALIGN=top>
<td>
<p> flowlabel </td>
<td>
<p> Flow label </td>
<td>
<p> integer (20 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> length </td>
<td>
<p> Payload length </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nexthdr </td>
<td>
<p> Nexthdr protocol </td>
<td>
<p> inet_proto
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hoplimit </td>
<td>
<p> Hop limit </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> saddr </td>
<td>
<p> Source address </td>
<td>
<p> ipv6_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> daddr </td>
<td>
<p> Destination address </td>
<td>
<p> ipv6_addr
</td>
</tr>
</table>
<p> <code>Using ip6 header expressions</code>. </p>
<dl>
<dd>
<pre># matching if first extension header indicates a fragment
ip6 nexthdr ipv6-frag</pre>
</dl>
<h3>Icmpv6 Header Expression</h3>
<dl>
<dd>
<pre><code>icmpv6</code> {<code>type</code> | <code>code</code> | <code>checksum</code> | <code>parameter-problem</code> | <code>packet-too-big</code> | <code>id</code> | <code>sequence</code> | <code>max-delay</code>}</pre>
</dl>
<p> This expression refers to ICMPv6 header fields. When using it in <code>inet</code>, <code>bridge</code> or <code>netdev</code> families, it will cause an implicit dependency on IPv6 to be created. To match on unusual cases like ICMPv6 over IPv4, one has to add an explicit <code>meta protocol ip</code> match to the rule. </p>
<p> <code>Table 44. ICMPv6 header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> ICMPv6 type field </td>
<td>
<p> icmpv6_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> code </td>
<td>
<p> ICMPv6 code field </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> checksum </td>
<td>
<p> ICMPv6 checksum field </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> parameter-problem </td>
<td>
<p> pointer to problem </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> packet-too-big </td>
<td>
<p> oversized MTU </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> id </td>
<td>
<p> ID of echo request/response </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sequence </td>
<td>
<p> sequence number of echo request/response </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> max-delay </td>
<td>
<p> maximum response delay of MLD queries </td>
<td>
<p> integer (16 bit)
</td>
</tr>
</table>
<h3>Tcp Header Expression</h3>
<dl>
<dd>
<pre><code>tcp</code> {<code>sport</code> | <code>dport</code> | <code>sequence</code> | <code>ackseq</code> | <code>doff</code> | <code>reserved</code> | <code>flags</code> | <code>window</code> | <code>checksum</code> | <code>urgptr</code>}</pre>
</dl>
<p> <code>Table 45. TCP header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sport </td>
<td>
<p> Source port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dport </td>
<td>
<p> Destination port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sequence </td>
<td>
<p> Sequence number </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ackseq </td>
<td>
<p> Acknowledgement number </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> doff </td>
<td>
<p> Data offset </td>
<td>
<p> integer (4 bit) FIXME scaling
</td>
</tr>
<tr VALIGN=top>
<td>
<p> reserved </td>
<td>
<p> Reserved area </td>
<td>
<p> integer (4 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> flags </td>
<td>
<p> TCP flags </td>
<td>
<p> tcp_flag
</td>
</tr>
<tr VALIGN=top>
<td>
<p> window </td>
<td>
<p> Window </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> checksum </td>
<td>
<p> Checksum </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> urgptr </td>
<td>
<p> Urgent pointer </td>
<td>
<p> integer (16 bit)
</td>
</tr>
</table>
<h3>Udp Header Expression</h3>
<dl>
<dd>
<pre><code>udp</code> {<code>sport</code> | <code>dport</code> | <code>length</code> | <code>checksum</code>}</pre>
</dl>
<p> <code>Table 46. UDP header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sport </td>
<td>
<p> Source port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dport </td>
<td>
<p> Destination port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> length </td>
<td>
<p> Total packet length </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> checksum </td>
<td>
<p> Checksum </td>
<td>
<p> integer (16 bit)
</td>
</tr>
</table>
<h3>Udp-Lite Header Expression</h3>
<dl>
<dd>
<pre><code>udplite</code> {<code>sport</code> | <code>dport</code> | <code>checksum</code>}</pre>
</dl>
<p> <code>Table 47. UDP-Lite header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sport </td>
<td>
<p> Source port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dport </td>
<td>
<p> Destination port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> checksum </td>
<td>
<p> Checksum </td>
<td>
<p> integer (16 bit)
</td>
</tr>
</table>
<h3>Sctp Header Expression</h3>
<dl>
<dd>
<pre><code>sctp</code> {<code>sport</code> | <code>dport</code> | <code>vtag</code> | <code>checksum</code>}
<code>sctp chunk</code> <i>CHUNK</i> [ <i>FIELD</i> ]
<i>CHUNK</i> := <code>data</code> | <code>init</code> | <code>init-ack</code> | <code>sack</code> | <code>heartbeat</code> |
 <code>heartbeat-ack</code> | <code>abort</code> | <code>shutdown</code> | <code>shutdown-ack</code> | <code>error</code> |
 <code>cookie-echo</code> | <code>cookie-ack</code> | <code>ecne</code> | <code>cwr</code> | <code>shutdown-complete</code>
 | <code>asconf-ack</code> | <code>forward-tsn</code> | <code>asconf</code>
<i>FIELD</i> := <i>COMMON_FIELD</i> | <i>DATA_FIELD</i> | <i>INIT_FIELD</i> | <i>INIT_ACK_FIELD</i> |
 <i>SACK_FIELD</i> | <i>SHUTDOWN_FIELD</i> | <i>ECNE_FIELD</i> | <i>CWR_FIELD</i> |
 <i>ASCONF_ACK_FIELD</i> | <i>FORWARD_TSN_FIELD</i> | <i>ASCONF_FIELD</i>
<i>COMMON_FIELD</i> := <code>type</code> | <code>flags</code> | <code>length</code>
<i>DATA_FIELD</i> := <code>tsn</code> | <code>stream</code> | <code>ssn</code> | <code>ppid</code>
<i>INIT_FIELD</i> := <code>init-tag</code> | <code>a-rwnd</code> | <code>num-outbound-streams</code> |
 <code>num-inbound-streams</code> | <code>initial-tsn</code>
<i>INIT_ACK_FIELD</i> := <i>INIT_FIELD</i>
<i>SACK_FIELD</i> := <code>cum-tsn-ack</code> | <code>a-rwnd</code> | <code>num-gap-ack-blocks</code> |
 <code>num-dup-tsns</code>
<i>SHUTDOWN_FIELD</i> := <code>cum-tsn-ack</code>
<i>ECNE_FIELD</i> := <code>lowest-tsn</code>
<i>CWR_FIELD</i> := <code>lowest-tsn</code>
<i>ASCONF_ACK_FIELD</i> := <code>seqno</code>
<i>FORWARD_TSN_FIELD</i> := <code>new-cum-tsn</code>
<i>ASCONF_FIELD</i> := <code>seqno</code></pre>
</dl>
<p> <code>Table 48. SCTP header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sport </td>
<td>
<p> Source port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dport </td>
<td>
<p> Destination port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> vtag </td>
<td>
<p> Verification Tag </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> checksum </td>
<td>
<p> Checksum </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> chunk </td>
<td>
<p> Search chunk in packet </td>
<td>
<p> without <i>FIELD</i>, boolean indicating existence
</td>
</tr>
</table>
<p> <code>Table 49. SCTP chunk fields</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Width in bits </code></td>
<td><code> Chunk </code></td>
<td><code> Notes </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> 8 </td>
<td>
<p> all </td>
<td>
<p> not useful, defined by chunk type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> flags </td>
<td>
<p> 8 </td>
<td>
<p> all </td>
<td>
<p> semantics defined on per-chunk basis
</td>
</tr>
<tr VALIGN=top>
<td>
<p> length </td>
<td>
<p> 16 </td>
<td>
<p> all </td>
<td>
<p> length of this chunk in bytes excluding padding
</td>
</tr>
<tr VALIGN=top>
<td>
<p> tsn </td>
<td>
<p> 32 </td>
<td>
<p> data </td>
<td>
<p> transmission sequence number
</td>
</tr>
<tr VALIGN=top>
<td>
<p> stream </td>
<td>
<p> 16 </td>
<td>
<p> data </td>
<td>
<p> stream identifier
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ssn </td>
<td>
<p> 16 </td>
<td>
<p> data </td>
<td>
<p> stream sequence number
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ppid </td>
<td>
<p> 32 </td>
<td>
<p> data </td>
<td>
<p> payload protocol identifier
</td>
</tr>
<tr VALIGN=top>
<td>
<p> init-tag </td>
<td>
<p> 32 </td>
<td>
<p> init, init-ack </td>
<td>
<p> initiate tag
</td>
</tr>
<tr VALIGN=top>
<td>
<p> a-rwnd </td>
<td>
<p> 32 </td>
<td>
<p> init, init-ack, sack </td>
<td>
<p> advertised receiver window credit
</td>
</tr>
<tr VALIGN=top>
<td>
<p> num-outbound-streams </td>
<td>
<p> 16 </td>
<td>
<p> init, init-ack </td>
<td>
<p> number of outbound streams
</td>
</tr>
<tr VALIGN=top>
<td>
<p> num-inbound-streams </td>
<td>
<p> 16 </td>
<td>
<p> init, init-ack </td>
<td>
<p> number of inbound streams
</td>
</tr>
<tr VALIGN=top>
<td>
<p> initial-tsn </td>
<td>
<p> 32 </td>
<td>
<p> init, init-ack </td>
<td>
<p> initial transmit sequence number
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cum-tsn-ack </td>
<td>
<p> 32 </td>
<td>
<p> sack, shutdown </td>
<td>
<p> cumulative transmission sequence number acknowledged
</td>
</tr>
<tr VALIGN=top>
<td>
<p> num-gap-ack-blocks </td>
<td>
<p> 16 </td>
<td>
<p> sack </td>
<td>
<p> number of Gap Ack Blocks included
</td>
</tr>
<tr VALIGN=top>
<td>
<p> num-dup-tsns </td>
<td>
<p> 16 </td>
<td>
<p> sack </td>
<td>
<p> number of duplicate transmission sequence numbers received
</td>
</tr>
<tr VALIGN=top>
<td>
<p> lowest-tsn </td>
<td>
<p> 32 </td>
<td>
<p> ecne, cwr </td>
<td>
<p> lowest transmission sequence number
</td>
</tr>
<tr VALIGN=top>
<td>
<p> seqno </td>
<td>
<p> 32 </td>
<td>
<p> asconf-ack, asconf </td>
<td>
<p> sequence number
</td>
</tr>
<tr VALIGN=top>
<td>
<p> new-cum-tsn </td>
<td>
<p> 32 </td>
<td>
<p> forward-tsn </td>
<td>
<p> new cumulative transmission sequence number
</td>
</tr>
</table>
<h3>Dccp Header Expression</h3>
<dl>
<dd>
<pre><code>dccp</code> {<code>sport</code> | <code>dport</code> | <code>type</code>}</pre>
</dl>
<p> <code>Table 50. DCCP header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sport </td>
<td>
<p> Source port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dport </td>
<td>
<p> Destination port </td>
<td>
<p> inet_service
</td>
</tr>
<tr VALIGN=top>
<td>
<p> type </td>
<td>
<p> Packet type </td>
<td>
<p> dccp_pkttype
</td>
</tr>
</table>
<h3>Authentication Header Expression</h3>
<dl>
<dd>
<pre><code>ah</code> {<code>nexthdr</code> | <code>hdrlength</code> | <code>reserved</code> | <code>spi</code> | <code>sequence</code>}</pre>
</dl>
<p> <code>Table 51. AH header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nexthdr </td>
<td>
<p> Next header protocol </td>
<td>
<p> inet_proto
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hdrlength </td>
<td>
<p> AH Header length </td>
<td>
<p> integer (8 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> reserved </td>
<td>
<p> Reserved area </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> spi </td>
<td>
<p> Security Parameter Index </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sequence </td>
<td>
<p> Sequence number </td>
<td>
<p> integer (32 bit)
</td>
</tr>
</table>
<h3>Encrypted Security Payload Header Expression</h3>
<dl>
<dd>
<pre><code>esp</code> {<code>spi</code> | <code>sequence</code>}</pre>
</dl>
<p> <code>Table 52. ESP header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> spi </td>
<td>
<p> Security Parameter Index </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sequence </td>
<td>
<p> Sequence number </td>
<td>
<p> integer (32 bit)
</td>
</tr>
</table>
<h3>Ipcomp Header Expression</h3>
<p><code>comp</code> {<code>nexthdr</code> | <code>flags</code> | <code>cpi</code>} </p>
<p> <code>Table 53. IPComp header expression</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nexthdr </td>
<td>
<p> Next header protocol </td>
<td>
<p> inet_proto
</td>
</tr>
<tr VALIGN=top>
<td>
<p> flags </td>
<td>
<p> Flags </td>
<td>
<p> bitmask
</td>
</tr>
<tr VALIGN=top>
<td>
<p> cpi </td>
<td>
<p> compression Parameter Index </td>
<td>
<p> integer (16 bit)
</td>
</tr>
</table>
<h3>Raw Payload Expression</h3>
<dl>
<dd>
<pre><code>@</code><i>base</i><code>,</code><i>offset</i><code>,</code><i>length</i></pre>
</dl>
<p> The raw payload expression instructs to load <i>length</i> bits starting at <i>offset</i> bits. Bit 0 refers to the very first bit &#8212; in the C programming language, this corresponds to the topmost bit, i.e. 0x80 in case of an octet. They are useful to match headers that do not have a human-readable template expression yet. Note that nft will not add dependencies for Raw payload expressions. If you e.g. want to match protocol fields of a transport header with protocol number 5, you need to manually exclude packets that have a different transport header, for instance by using <code>meta l4proto 5</code> before the raw expression. </p>
<p> <code>Table 54. Supported payload protocol bases</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Base </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ll </td>
<td>
<p> Link layer, for example the Ethernet header
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nh </td>
<td>
<p> Network header, for example IPv4 or IPv6
</td>
</tr>
<tr VALIGN=top>
<td>
<p> th </td>
<td>
<p> Transport Header, for example TCP
</td>
</tr>
</table>
<p> <code>Matching destination port of both UDP and TCP</code>. </p>
<dl>
<dd>
<pre>inet filter input meta l4proto {tcp, udp} @th,16,16 { 53, 80 }</pre>
</dl>
<p> The above can also be written as </p>
<dl>
<dd>
<pre>inet filter input meta l4proto {tcp, udp} th dport { 53, 80 }</pre>
</dl>
<p> it is more convenient, but like the raw expression notation no dependencies are created or checked. It is the users responsibility to restrict matching to those header types that have a notion of ports. Otherwise, rules using raw expressions will errnously match unrelated packets, e.g. mis-interpreting ESP packets SPI field as a port. </p>
<p> <code>Rewrite arp packet target hardware address if target protocol address matches a given address</code>. </p>
<dl>
<dd>
<pre>input meta iifname enp2s0 arp ptype 0x0800 arp htype 1 arp hlen 6 arp plen 4 @nh,192,32 0xc0a88f10 @nh,144,48 set 0x112233445566 accept</pre>
</dl>
<h3>Extension Header Expressions</h3>
<p>Extension header expressions refer to data from variable-sized protocol headers, such as IPv6 extension headers, TCP options and IPv4 options. </p>
<p> nftables currently supports matching (finding) a given ipv6 extension header, TCP option or IPv4 option. </p>
<dl>
<dd>
<pre><code>hbh</code> {<code>nexthdr</code> | <code>hdrlength</code>}
<code>frag</code> {<code>nexthdr</code> | <code>frag-off</code> | <code>more-fragments</code> | <code>id</code>}
<code>rt</code> {<code>nexthdr</code> | <code>hdrlength</code> | <code>type</code> | <code>seg-left</code>}
<code>dst</code> {<code>nexthdr</code> | <code>hdrlength</code>}
<code>mh</code> {<code>nexthdr</code> | <code>hdrlength</code> | <code>checksum</code> | <code>type</code>}
<code>srh</code> {<code>flags</code> | <code>tag</code> | <code>sid</code> | <code>seg-left</code>}
<code>tcp option</code> {<code>eol</code> | <code>nop</code> | <code>maxseg</code> | <code>window</code> | <code>sack-perm</code> | <code>sack</code> | <code>sack0</code> | <code>sack1</code> | <code>sack2</code> | <code>sack3</code> | <code>timestamp</code>} <i>tcp_option_field</i>
<code>ip option</code> { lsrr | ra | rr | ssrr } <i>ip_option_field</i></pre>
</dl>
<p> The following syntaxes are valid only in a relational expression with boolean type on right-hand side for checking header existence only: </p>
<dl>
<dd>
<pre><code>exthdr</code> {<code>hbh</code> | <code>frag</code> | <code>rt</code> | <code>dst</code> | <code>mh</code>}
<code>tcp option</code> {<code>eol</code> | <code>nop</code> | <code>maxseg</code> | <code>window</code> | <code>sack-perm</code> | <code>sack</code> | <code>sack0</code> | <code>sack1</code> | <code>sack2</code> | <code>sack3</code> | <code>timestamp</code>}
<code>ip option</code> { lsrr | ra | rr | ssrr }</pre>
</dl>
<p> <code>Table 55. IPv6 extension headers</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> hbh </td>
<td>
<p> Hop by Hop
</td>
</tr>
<tr VALIGN=top>
<td>
<p> rt </td>
<td>
<p> Routing Header
</td>
</tr>
<tr VALIGN=top>
<td>
<p> frag </td>
<td>
<p> Fragmentation header
</td>
</tr>
<tr VALIGN=top>
<td>
<p> dst </td>
<td>
<p> dst options
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mh </td>
<td>
<p> Mobility Header
</td>
</tr>
<tr VALIGN=top>
<td>
<p> srh </td>
<td>
<p> Segment Routing Header
</td>
</tr>
</table>
<p> <code>Table 56. TCP Options</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> TCP option fields </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> eol </td>
<td>
<p> End if option list </td>
<td>
<p> &#8211;
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nop </td>
<td>
<p> 1 Byte TCP Nop padding option </td>
<td>
<p> &#8211;
</td>
</tr>
<tr VALIGN=top>
<td>
<p> maxseg </td>
<td>
<p> TCP Maximum Segment Size </td>
<td>
<p> length, size
</td>
</tr>
<tr VALIGN=top>
<td>
<p> window </td>
<td>
<p> TCP Window Scaling </td>
<td>
<p> length, count
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sack-perm </td>
<td>
<p> TCP SACK permitted </td>
<td>
<p> length
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sack </td>
<td>
<p> TCP Selective Acknowledgement (alias of block 0) </td>
<td>
<p> length, left, right
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sack0 </td>
<td>
<p> TCP Selective Acknowledgement (block 0) </td>
<td>
<p> length, left, right
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sack1 </td>
<td>
<p> TCP Selective Acknowledgement (block 1) </td>
<td>
<p> length, left, right
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sack2 </td>
<td>
<p> TCP Selective Acknowledgement (block 2) </td>
<td>
<p> length, left, right
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sack3 </td>
<td>
<p> TCP Selective Acknowledgement (block 3) </td>
<td>
<p> length, left, right
</td>
</tr>
<tr VALIGN=top>
<td>
<p> timestamp </td>
<td>
<p> TCP Timestamps </td>
<td>
<p> length, tsval, tsecr
</td>
</tr>
</table>
<p> TCP option matching also supports raw expression syntax to access arbitrary options: </p>
<dl>
<dd>
<pre><code>tcp option</code></pre>
</dl>
<dl>
<dd>
<pre><code>tcp option</code> <code>@</code><i>number</i><code>,</code><i>offset</i><code>,</code><i>length</i></pre>
</dl>
<p> <code>Table 57. IP Options</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> IP option fields </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> lsrr </td>
<td>
<p> Loose Source Route </td>
<td>
<p> type, length, ptr, addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ra </td>
<td>
<p> Router Alert </td>
<td>
<p> type, length, value
</td>
</tr>
<tr VALIGN=top>
<td>
<p> rr </td>
<td>
<p> Record Route </td>
<td>
<p> type, length, ptr, addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ssrr </td>
<td>
<p> Strict Source Route </td>
<td>
<p> type, length, ptr, addr
</td>
</tr>
</table>
<p> <code>finding TCP options</code>. </p>
<dl>
<dd>
<pre>filter input tcp option sack-perm exists counter</pre>
</dl>
<p> <code>matching TCP options</code>. </p>
<dl>
<dd>
<pre>filter input tcp option maxseg size lt 536</pre>
</dl>
<p> <code>matching IPv6 exthdr</code>. </p>
<dl>
<dd>
<pre>ip6 filter input frag more-fragments 1 counter</pre>
</dl>
<p> <code>finding IP option</code>. </p>
<dl>
<dd>
<pre>filter input ip option lsrr exists counter</pre>
</dl>
<h3>Conntrack Expressions</h3>
<p>Conntrack expressions refer to meta data of the connection tracking entry associated with a packet. </p>
<p> There are three types of conntrack expressions. Some conntrack expressions require the flow direction before the conntrack key, others must be used directly because they are direction agnostic. The <code>packets</code>, <code>bytes</code> and <code>avgpkt</code> keywords can be used with or without a direction. If the direction is omitted, the sum of the original and the reply direction is returned. The same is true for the <code>zone</code>, if a direction is given, the zone is only matched if the zone id is tied to the given direction. </p>
<dl>
<dd>
<pre><code>ct</code> {<code>state</code> | <code>direction</code> | <code>status</code> | <code>mark</code> | <code>expiration</code> | <code>helper</code> | <code>label</code> | <code>count</code> | <code>id</code>}
<code>ct</code> [<code>original</code> | <code>reply</code>] {<code>l3proto</code> | <code>protocol</code> | <code>bytes</code> | <code>packets</code> | <code>avgpkt</code> | <code>zone</code>}
<code>ct</code> {<code>original</code> | <code>reply</code>} {<code>proto-src</code> | <code>proto-dst</code>}
<code>ct</code> {<code>original</code> | <code>reply</code>} {<code>ip</code> | <code>ip6</code>} {<code>saddr</code> | <code>daddr</code>}</pre>
</dl>
<p> The conntrack-specific types in this table are described in the sub-section CONNTRACK TYPES above. </p>
<p> <code>Table 58. Conntrack expressions</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> state </td>
<td>
<p> State of the connection </td>
<td>
<p> ct_state
</td>
</tr>
<tr VALIGN=top>
<td>
<p> direction </td>
<td>
<p> Direction of the packet relative to the connection </td>
<td>
<p> ct_dir
</td>
</tr>
<tr VALIGN=top>
<td>
<p> status </td>
<td>
<p> Status of the connection </td>
<td>
<p> ct_status
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mark </td>
<td>
<p> Connection mark </td>
<td>
<p> mark
</td>
</tr>
<tr VALIGN=top>
<td>
<p> expiration </td>
<td>
<p> Connection expiration time </td>
<td>
<p> time
</td>
</tr>
<tr VALIGN=top>
<td>
<p> helper </td>
<td>
<p> Helper associated with the connection </td>
<td>
<p> string
</td>
</tr>
<tr VALIGN=top>
<td>
<p> label </td>
<td>
<p> Connection tracking label bit or symbolic name defined in connlabel.conf in the nftables include path </td>
<td>
<p> ct_label
</td>
</tr>
<tr VALIGN=top>
<td>
<p> l3proto </td>
<td>
<p> Layer 3 protocol of the connection </td>
<td>
<p> nf_proto
</td>
</tr>
<tr VALIGN=top>
<td>
<p> saddr </td>
<td>
<p> Source address of the connection for the given direction </td>
<td>
<p> ipv4_addr/ipv6_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> daddr </td>
<td>
<p> Destination address of the connection for the given direction </td>
<td>
<p> ipv4_addr/ipv6_addr
</td>
</tr>
<tr VALIGN=top>
<td>
<p> protocol </td>
<td>
<p> Layer 4 protocol of the connection for the given direction </td>
<td>
<p> inet_proto
</td>
</tr>
<tr VALIGN=top>
<td>
<p> proto-src </td>
<td>
<p> Layer 4 protocol source for the given direction </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> proto-dst </td>
<td>
<p> Layer 4 protocol destination for the given direction </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> packets </td>
<td>
<p> packet count seen in the given direction or sum of original and reply </td>
<td>
<p> integer (64 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> bytes </td>
<td>
<p> byte count seen, see description for <code>packets</code> keyword </td>
<td>
<p> integer (64 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> avgpkt </td>
<td>
<p> average bytes per packet, see description for <code>packets</code> keyword </td>
<td>
<p> integer (64 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> zone </td>
<td>
<p> conntrack zone </td>
<td>
<p> integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> count </td>
<td>
<p> number of current connections </td>
<td>
<p> integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> id </td>
<td>
<p> Connection id </td>
<td>
<p> ct_id
</td>
</tr>
</table>
<p> <code>restrict the number of parallel connections to a server</code>. </p>
<dl>
<dd>
<pre>nft add set filter ssh_flood '{ type ipv4_addr; flags dynamic; }'
nft add rule filter input tcp dport 22 add @ssh_flood '{ ip saddr ct count over 2 }' reject</pre>
</dl>
<h2>Statements</h2>
<p>Statements represent actions to be performed. They can alter control flow (return, jump to a different chain, accept or drop the packet) or can perform actions, such as logging, rejecting a packet, etc. </p>
<p> Statements exist in two kinds. Terminal statements unconditionally terminate evaluation of the current rule, non-terminal statements either only conditionally or never terminate evaluation of the current rule, in other words, they are passive from the ruleset evaluation perspective. There can be an arbitrary amount of non-terminal statements in a rule, but only a single terminal statement as the final statement.</p>
<h3>Verdict Statement</h3>
<p>The verdict statement alters control flow in the ruleset and issues policy decisions for packets. </p>
<dl>
<dd>
<pre>{<code>accept</code> | <code>drop</code> | <code>queue</code> | <code>continue</code> | <code>return</code>}
{<code>jump</code> | <code>goto</code>} <i>chain</i></pre>
</dl>
<p> <code>accept</code> and <code>drop</code> are absolute verdicts &#8212; they terminate ruleset evaluation immediately. </p>
<table>
<tr VALIGN=top>
<td>
<p> <code>accept</code> </td>
<td>
<p> Terminate ruleset evaluation and accept the packet. The packet can still be dropped later by another hook, for instance accept in the forward hook still allows to drop the packet later in the postrouting hook, or another forward base chain that has a higher priority number and is evaluated afterwards in the processing pipeline.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>drop</code> </td>
<td>
<p> Terminate ruleset evaluation and drop the packet. The drop occurs instantly, no further chains or hooks are evaluated. It is not possible to accept the packet in a later chain again, as those are not evaluated anymore for the packet.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>queue</code> </td>
<td>
<p> Terminate ruleset evaluation and queue the packet to userspace. Userspace must provide a drop or accept verdict. In case of accept, processing resumes with the next base chain hook, not the rule following the queue verdict.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>continue</code> </td>
<td>
<p> Continue ruleset evaluation with the next rule. This is the default behaviour in case a rule issues no verdict.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>return</code> </td>
<td>
<p> Return from the current chain and continue evaluation at the next rule in the last chain. If issued in a base chain, it is equivalent to the base chain policy.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>jump</code> <i>chain</i> </td>
<td>
<p> Continue evaluation at the first rule in <i>chain</i>. The current position in the ruleset is pushed to a call stack and evaluation will continue there when the new chain is entirely evaluated or a <code>return</code> verdict is issued. In case an absolute verdict is issued by a rule in the chain, ruleset evaluation terminates immediately and the specific action is taken.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> <code>goto</code> <i>chain</i> </td>
<td>
<p> Similar to <code>jump</code>, but the current position is not pushed to the call stack, meaning that after the new chain evaluation will continue at the last chain instead of the one containing the goto statement.
</td>
</tr>
</table>
<p> <code>Using verdict statements</code>. </p>
<dl>
<dd>
<pre># process packets from eth0 and the internal network in from_lan
# chain, drop all packets from eth0 with different source addresses.
filter input iif eth0 ip saddr 192.168.0.0/24 jump from_lan
filter input iif eth0 drop</pre>
</dl>
<h3>Payload Statement</h3>
<dl>
<dd>
<pre><i>payload_expression</i> <code>set</code> <i>value</i></pre>
</dl>
<p> The payload statement alters packet content. It can be used for example to set ip DSCP (diffserv) header field or ipv6 flow labels. </p>
<p> <code>route some packets instead of bridging</code>. </p>
<dl>
<dd>
<pre># redirect tcp:http from 192.160.0.0/16 to local machine for routing instead of bridging
# assumes 00:11:22:33:44:55 is local MAC address.
bridge input meta iif eth0 ip saddr 192.168.0.0/16 tcp dport 80 meta pkttype set unicast ether daddr set 00:11:22:33:44:55</pre>
</dl>
<p> <code>Set IPv4 DSCP header field</code>. </p>
<dl>
<dd>
<pre>ip forward ip dscp set 42</pre>
</dl>
<h3>Extension Header Statement</h3>
<dl>
<dd>
<pre><i>extension_header_expression</i> <code>set</code> <i>value</i></pre>
</dl>
<p> The extension header statement alters packet content in variable-sized headers. This can currently be used to alter the TCP Maximum segment size of packets, similar to TCPMSS. </p>
<p> <code>change tcp mss</code>. </p>
<dl>
<dd>
<pre>tcp flags syn tcp option maxseg size set 1360
# set a size based on route information:
tcp flags syn tcp option maxseg size set rt mtu</pre>
</dl>
<h3>Log Statement</h3>
<dl>
<dd>
<pre><code>log</code> [<code>prefix</code> <i>quoted_string</i>] [<code>level</code> <i>syslog-level</i>] [<code>flags</code> <i>log-flags</i>]
<code>log</code> <code>group</code> <i>nflog_group</i> [<code>prefix</code> <i>quoted_string</i>] [<code>queue-threshold</code> <i>value</i>] [<code>snaplen</code> <i>size</i>]
<code>log level audit</code></pre>
</dl>
<p> The log statement enables logging of matching packets. When this statement is used from a rule, the Linux kernel will print some information on all matching packets, such as header fields, via the kernel log (where it can be read with <a href="/docs/linux/man/1-dmesg/">dmesg</a>(1) or read in the syslog). </p>
<p> In the second form of invocation (if <i>nflog_group</i> is specified), the Linux kernel will pass the packet to nfnetlink_log which will send the log through a netlink socket to the specified group. One userspace process may subscribe to the group to receive the logs, see <a href="/docs/linux/man/8-man/">man</a>(8) ulogd for the Netfilter userspace log daemon and libnetfilter_log documentation for details in case you would like to develop a custom program to digest your logs. </p>
<p> In the third form of invocation (if level audit is specified), the Linux kernel writes a message into the audit buffer suitably formatted for reading with auditd. Therefore no further formatting options (such as prefix or flags) are allowed in this mode. </p>
<p> This is a non-terminating statement, so the rule evaluation continues after the packet is logged. </p>
<p> <code>Table 59. log statement options</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> prefix </td>
<td>
<p> Log message prefix </td>
<td>
<p> quoted string
</td>
</tr>
<tr VALIGN=top>
<td>
<p> level </td>
<td>
<p> Syslog level of logging </td>
<td>
<p> string: emerg, alert, crit, err, warn [default], notice, info, debug, audit
</td>
</tr>
<tr VALIGN=top>
<td>
<p> group </td>
<td>
<p> NFLOG group to send messages to </td>
<td>
<p> unsigned integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> snaplen </td>
<td>
<p> Length of packet payload to include in netlink message </td>
<td>
<p> unsigned integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> queue-threshold </td>
<td>
<p> Number of packets to queue inside the kernel before sending them to userspace </td>
<td>
<p> unsigned integer (32 bit)
</td>
</tr>
</table>
<p> <code>Table 60. log-flags</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Flag </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> tcp sequence </td>
<td>
<p> Log TCP sequence numbers.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> tcp options </td>
<td>
<p> Log options from the TCP packet header.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ip options </td>
<td>
<p> Log options from the IP/IPv6 packet header.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> skuid </td>
<td>
<p> Log the userid of the process which generated the packet.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> ether </td>
<td>
<p> Decode MAC addresses and protocol.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> all </td>
<td>
<p> Enable all log flags listed above.
</td>
</tr>
</table>
<p> <code>Using log statement</code>. </p>
<dl>
<dd>
<pre># log the UID which generated the packet and ip options
ip filter output log flags skuid flags ip options
# log the tcp sequence numbers and tcp options from the TCP packet
ip filter output log flags tcp sequence,options
# enable all supported log flags
ip6 filter output log flags all</pre>
</dl>
<h3>Reject Statement</h3>
<dl>
<dd>
<pre><code>reject</code> [ <code>with</code> <i>REJECT_WITH</i> ]
<i>REJECT_WITH</i> := <code>icmp</code> <i>icmp_code</i> |
 <code>icmpv6</code> <i>icmpv6_code</i> |
 <code>icmpx</code> <i>icmpx_code</i> |
 <code>tcp reset</code></pre>
</dl>
<p> A reject statement is used to send back an error packet in response to the matched packet otherwise it is equivalent to drop so it is a terminating statement, ending rule traversal. This statement is only valid in base chains using the <code>input</code>, <code>forward</code> or <code>output</code> hooks, and user-defined chains which are only called from those chains. </p>
<p> <code>Table 61. different ICMP reject variants are meant for use in different table families</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Variant </code></td>
<td><code> Family </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> icmp </td>
<td>
<p> ip </td>
<td>
<p> icmp_code
</td>
</tr>
<tr VALIGN=top>
<td>
<p> icmpv6 </td>
<td>
<p> ip6 </td>
<td>
<p> icmpv6_code
</td>
</tr>
<tr VALIGN=top>
<td>
<p> icmpx </td>
<td>
<p> inet </td>
<td>
<p> icmpx_code
</td>
</tr>
</table>
<p> For a description of the different types and a list of supported keywords refer to DATA TYPES section above. The common default reject value is <code>port-unreachable</code>. </p>
<p> Note that in bridge family, reject statement is only allowed in base chains which hook into input or prerouting.</p>
<h3>Counter Statement</h3>
<p>A counter statement sets the hit count of packets along with the number of bytes. </p>
<dl>
<dd>
<pre><code>counter</code> <code>packets</code> <i>number</i> <code>bytes</code> <i>number</i>
<code>counter</code> { <code>packets</code> <i>number</i> | <code>bytes</code> <i>number</i> }</pre>
</dl>
<h3>Conntrack Statement</h3>
<p>The conntrack statement can be used to set the conntrack mark and conntrack labels. </p>
<dl>
<dd>
<pre><code>ct</code> {<code>mark</code> | <code>event</code> | <code>label</code> | <code>zone</code>} <code>set</code> <i>value</i></pre>
</dl>
<p> The ct statement sets meta data associated with a connection. The zone id has to be assigned before a conntrack lookup takes place, i.e. this has to be done in prerouting and possibly output (if locally generated packets need to be placed in a distinct zone), with a hook priority of <code>raw</code> (-300). </p>
<p> Unlike iptables, where the helper assignment happens in the raw table, the helper needs to be assigned after a conntrack entry has been found, i.e. it will not work when used with hook priorities equal or before -200. </p>
<p> <code>Table 62. Conntrack statement types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> event </td>
<td>
<p> conntrack event bits </td>
<td>
<p> bitmask, integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> helper </td>
<td>
<p> name of ct helper object to assign to the connection </td>
<td>
<p> quoted string
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mark </td>
<td>
<p> Connection tracking mark </td>
<td>
<p> mark
</td>
</tr>
<tr VALIGN=top>
<td>
<p> label </td>
<td>
<p> Connection tracking label </td>
<td>
<p> label
</td>
</tr>
<tr VALIGN=top>
<td>
<p> zone </td>
<td>
<p> conntrack zone </td>
<td>
<p> integer (16 bit)
</td>
</tr>
</table>
<p> <code>save packet nfmark in conntrack</code>. </p>
<dl>
<dd>
<pre>ct mark set meta mark</pre>
</dl>
<p> <code>set zone mapped via interface</code>. </p>
<dl>
<dd>
<pre>table inet raw {
 chain prerouting {
 type filter hook prerouting priority raw;
 ct zone set iif map { &quot;eth1&quot; : 1, &quot;veth1&quot; : 2 }
 }
 chain output {
 type filter hook output priority raw;
 ct zone set oif map { &quot;eth1&quot; : 1, &quot;veth1&quot; : 2 }
 }
}</pre>
</dl>
<p> <code>restrict events reported by ctnetlink</code>. </p>
<dl>
<dd>
<pre>ct event set new,related,destroy</pre>
</dl>
<h3>Notrack Statement</h3>
<p>The notrack statement allows to disable connection tracking for certain packets. </p>
<dl>
<dd>
<pre><code>notrack</code></pre>
</dl>
<p> Note that for this statement to be effective, it has to be applied to packets before a conntrack lookup happens. Therefore, it needs to sit in a chain with either prerouting or output hook and a hook priority of -300 (<code>raw</code>) or less. </p>
<p> See SYNPROXY STATEMENT for an example usage.</p>
<h3>Meta Statement</h3>
<p>A meta statement sets the value of a meta expression. The existing meta fields are: priority, mark, pkttype, nftrace. </p>
<dl>
<dd>
<pre><code>meta</code> {<code>mark</code> | <code>priority</code> | <code>pkttype</code> | <code>nftrace</code>} <code>set</code> <i>value</i></pre>
</dl>
<p> A meta statement sets meta data associated with a packet. </p>
<p> <code>Table 63. Meta statement types</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Keyword </code></td>
<td><code> Description </code></td>
<td><code> Value </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> priority </td>
<td>
<p> TC packet priority </td>
<td>
<p> tc_handle
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mark </td>
<td>
<p> Packet mark </td>
<td>
<p> mark
</td>
</tr>
<tr VALIGN=top>
<td>
<p> pkttype </td>
<td>
<p> packet type </td>
<td>
<p> pkt_type
</td>
</tr>
<tr VALIGN=top>
<td>
<p> nftrace </td>
<td>
<p> ruleset packet tracing on/off. Use <code>monitor trace</code> command to watch traces </td>
<td>
<p> 0, 1
</td>
</tr>
</table>
<h3>Limit Statement</h3>
<dl>
<dd>
<pre><code>limit rate</code> [<code>over</code>] <i>packet_number</i> <code>/</code> <i>TIME_UNIT</i> [<code>burst</code> <i>packet_number</i> <code>packets</code>]
<code>limit rate</code> [<code>over</code>] <i>byte_number</i> <i>BYTE_UNIT</i> <code>/</code> <i>TIME_UNIT</i> [<code>burst</code> <i>byte_number</i> <i>BYTE_UNIT</i>]
<i>TIME_UNIT</i> := <code>second</code> | <code>minute</code> | <code>hour</code> | <code>day</code>
<i>BYTE_UNIT</i> := <code>bytes</code> | <code>kbytes</code> | <code>mbytes</code></pre>
</dl>
<p> A limit statement matches at a limited rate using a token bucket filter. A rule using this statement will match until this limit is reached. It can be used in combination with the log statement to give limited logging. The optional <code>over</code> keyword makes it match over the specified rate. Default <code>burst</code> is 5. if you specify <code>burst</code>, it must be non-zero value. </p>
<p> <code>Table 64. limit statement values</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Value </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> packet_number </td>
<td>
<p> Number of packets </td>
<td>
<p> unsigned integer (32 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> byte_number </td>
<td>
<p> Number of bytes </td>
<td>
<p> unsigned integer (32 bit)
</td>
</tr>
</table>
<h3>Nat Statements</h3>
<dl>
<dd>
<pre><code>snat</code> [[<code>ip</code> | <code>ip6</code>] <code>to</code>] <i>ADDR_SPEC</i> [<code>:</code><i>PORT_SPEC</i>] [<i>FLAGS</i>]
<code>dnat</code> [[<code>ip</code> | <code>ip6</code>] <code>to</code>] <i>ADDR_SPEC</i> [<code>:</code><i>PORT_SPEC</i>] [<i>FLAGS</i>]
<code>masquerade</code> [<code>to :</code><i>PORT_SPEC</i>] [<i>FLAGS</i>]
<code>redirect</code> [<code>to :</code><i>PORT_SPEC</i>] [<i>FLAGS</i>]
<i>ADDR_SPEC</i> := <i>address</i> | <i>address</i> <code>-</code> <i>address</i>
<i>PORT_SPEC</i> := <i>port</i> | <i>port</i> <code>-</code> <i>port</i>
<i>FLAGS</i> := <i>FLAG</i> [<code>,</code> <i>FLAGS</i>]
<i>FLAG</i> := <code>persistent</code> | <code>random</code> | <code>fully-random</code></pre>
</dl>
<p> The nat statements are only valid from nat chain types. </p>
<p> The <code>snat</code> and <code>masquerade</code> statements specify that the source address of the packet should be modified. While <code>snat</code> is only valid in the postrouting and input chains, <code>masquerade</code> makes sense only in postrouting. The dnat and redirect statements are only valid in the prerouting and output chains, they specify that the destination address of the packet should be modified. You can use non-base chains which are called from base chains of nat chain type too. All future packets in this connection will also be mangled, and rules should cease being examined. </p>
<p> The <code>masquerade</code> statement is a special form of snat which always uses the outgoing interface&#8217;s IP address to translate to. It is particularly useful on gateways with dynamic (public) IP addresses. </p>
<p> The <code>redirect</code> statement is a special form of dnat which always translates the destination address to the local host&#8217;s one. It comes in handy if one only wants to alter the destination port of incoming traffic on different interfaces. </p>
<p> When used in the inet family (available with kernel 5.2), the dnat and snat statements require the use of the ip and ip6 keyword in case an address is provided, see the examples below. </p>
<p> Before kernel 4.18 nat statements require both prerouting and postrouting base chains to be present since otherwise packets on the return path won&#8217;t be seen by netfilter and therefore no reverse translation will take place. </p>
<p> <code>Table 65. NAT statement values</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Expression </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> address </td>
<td>
<p> Specifies that the source/destination address of the packet should be modified. You may specify a mapping to relate a list of tuples composed of arbitrary expression key with address value. </td>
<td>
<p> ipv4_addr, ipv6_addr, e.g. abcd::1234, or you can use a mapping, e.g. meta mark map { 10 : 192.168.1.2, 20 : 192.168.1.3 }
</td>
</tr>
<tr VALIGN=top>
<td>
<p> port </td>
<td>
<p> Specifies that the source/destination address of the packet should be modified. </td>
<td>
<p> port number (16 bit)
</td>
</tr>
</table>
<p> <code>Table 66. NAT statement flags</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Flag </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> persistent </td>
<td>
<p> Gives a client the same source-/destination-address for each connection.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> random </td>
<td>
<p> In kernel 5.0 and newer this is the same as fully-random. In earlier kernels the port mapping will be randomized using a seeded MD5 hash mix using source and destination address and destination port.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> fully-random </td>
<td>
<p> If used then port mapping is generated based on a 32-bit pseudo-random algorithm.
</td>
</tr>
</table>
<p> <code>Using NAT statements</code>. </p>
<dl>
<dd>
<pre># create a suitable table/chain setup for all further examples
add table nat
add chain nat prerouting { type nat hook prerouting priority dstnat; }
add chain nat postrouting { type nat hook postrouting priority srcnat; }
# translate source addresses of all packets leaving via eth0 to address 1.2.3.4
add rule nat postrouting oif eth0 snat to 1.2.3.4
# redirect all traffic entering via eth0 to destination address 192.168.1.120
add rule nat prerouting iif eth0 dnat to 192.168.1.120
# translate source addresses of all packets leaving via eth0 to whatever
# locally generated packets would use as source to reach the same destination
add rule nat postrouting oif eth0 masquerade
# redirect incoming TCP traffic for port 22 to port 2222
add rule nat prerouting tcp dport 22 redirect to :2222
# inet family:
# handle ip dnat:
add rule inet nat prerouting dnat ip to 10.0.2.99
# handle ip6 dnat:
add rule inet nat prerouting dnat ip6 to fe80::dead
# this masquerades both ipv4 and ipv6:
add rule inet nat postrouting meta oif ppp0 masquerade</pre>
</dl>
<h3>Tproxy Statement</h3>
<p>Tproxy redirects the packet to a local socket without changing the packet header in any way. If any of the arguments is missing the data of the incoming packet is used as parameter. Tproxy matching requires another rule that ensures the presence of transport protocol header is specified. </p>
<dl>
<dd>
<pre><code>tproxy to</code> <i>address</i><code>:</code><i>port</i>
<code>tproxy to</code> {<i>address</i> | <code>:</code><i>port</i>}</pre>
</dl>
<p> This syntax can be used in <code>ip/ip6</code> tables where network layer protocol is obvious. Either IP address or port can be specified, but at least one of them is necessary. </p>
<dl>
<dd>
<pre><code>tproxy</code> {<code>ip</code> | <code>ip6</code>} <code>to</code> <i>address</i>[<code>:</code><i>port</i>]
<code>tproxy to :</code><i>port</i></pre>
</dl>
<p> This syntax can be used in <code>inet</code> tables. The <code>ip/ip6</code> parameter defines the family the rule will match. The <code>address</code> parameter must be of this family. When only <code>port</code> is defined, the address family should not be specified. In this case the rule will match for both families. </p>
<p> <code>Table 67. tproxy attributes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> address </td>
<td>
<p> IP address the listening socket with IP_TRANSPARENT option is bound to.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> port </td>
<td>
<p> Port the listening socket with IP_TRANSPARENT option is bound to.
</td>
</tr>
</table>
<p> <code>Example ruleset for tproxy statement</code>. </p>
<dl>
<dd>
<pre>table ip x {
 chain y {
 type filter hook prerouting priority mangle; policy accept;
 tcp dport ntp tproxy to 1.1.1.1
 udp dport ssh tproxy to :2222
 }
}
table ip6 x {
 chain y {
 type filter hook prerouting priority mangle; policy accept;
 tcp dport ntp tproxy to [dead::beef]
 udp dport ssh tproxy to :2222
 }
}
table inet x {
 chain y {
 type filter hook prerouting priority mangle; policy accept;
 tcp dport 321 tproxy to :ssh
 tcp dport 99 tproxy ip to 1.1.1.1:999
 udp dport 155 tproxy ip6 to [dead::beef]:smux
 }
}</pre>
</dl>
<h3>Synproxy Statement</h3>
<p>This statement will process TCP three-way-handshake parallel in netfilter context to protect either local or backend system. This statement requires connection tracking because sequence numbers need to be translated. </p>
<dl>
<dd>
<pre><code>synproxy</code> [<code>mss</code> <i>mss_value</i>] [<code>wscale</code> <i>wscale_value</i>] [<i>SYNPROXY_FLAGS</i>]</pre>
</dl>
<p> <code>Table 68. synproxy statement attributes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> mss </td>
<td>
<p> Maximum segment size announced to clients. This must match the backend.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> wscale </td>
<td>
<p> Window scale announced to clients. This must match the backend.
</td>
</tr>
</table>
<p> <code>Table 69. synproxy statement flags</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Flag </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> sack-perm </td>
<td>
<p> Pass client selective acknowledgement option to backend (will be disabled if not present).
</td>
</tr>
<tr VALIGN=top>
<td>
<p> timestamp </td>
<td>
<p> Pass client timestamp option to backend (will be disabled if not present, also needed for selective acknowledgement and window scaling).
</td>
</tr>
</table>
<p> <code>Example ruleset for synproxy statement</code>. </p>
<dl>
<dd>
<pre>Determine tcp options used by backend, from an external system
 tcpdump -pni eth0 -c 1 'tcp[tcpflags] == (tcp-syn|tcp-ack)'
 port 80 &amp;
 telnet 192.0.2.42 80
 18:57:24.693307 IP 192.0.2.42.80 &gt; 192.0.2.43.48757:
 Flags [S.], seq 360414582, ack 788841994, win 14480,
 options [mss 1460,sackOK,
 TS val 1409056151 ecr 9690221,
 nop,wscale 9],
 length 0
Switch tcp_loose mode off, so conntrack will mark out-of-flow packets as state INVALID.
 echo 0 &gt; /proc/sys/net/netfilter/nf_conntrack_tcp_loose
Make SYN packets untracked.
 table ip x {
 chain y {
 type filter hook prerouting priority raw; policy accept;
 tcp flags syn notrack
 }
 }
Catch UNTRACKED (SYN packets) and INVALID (3WHS ACK packets) states and send
them to SYNPROXY. This rule will respond to SYN packets with SYN+ACK
syncookies, create ESTABLISHED for valid client response (3WHS ACK packets) and
drop incorrect cookies. Flags combinations not expected during 3WHS will not
match and continue (e.g. SYN+FIN, SYN+ACK). Finally, drop invalid packets, this
will be out-of-flow packets that were not matched by SYNPROXY.
 table ip x {
 chain z {
 type filter hook input priority filter; policy accept;
 ct state invalid, untracked synproxy mss 1460 wscale 9 timestamp sack-perm
 ct state invalid drop
 }
 }</pre>
</dl>
<h3>Flow Statement</h3>
<p>A flow statement allows us to select what flows you want to accelerate forwarding through layer 3 network stack bypass. You have to specify the flowtable name where you want to offload this flow. </p>
<p> <code>flow add @</code><i>flowtable</i></p>
<h3>Queue Statement</h3>
<p>This statement passes the packet to userspace using the nfnetlink_queue handler. The packet is put into the queue identified by its 16-bit queue number. Userspace can inspect and modify the packet if desired. Userspace must then drop or re-inject the packet into the kernel. See libnetfilter_queue documentation for details. </p>
<dl>
<dd>
<pre><code>queue</code> [<code>flags</code> <i>QUEUE_FLAGS</i>] [<code>to</code> <i>queue_number</i>]
<code>queue</code> [<code>flags</code> <i>QUEUE_FLAGS</i>] [<code>to</code> <i>queue_number_from</i> - <i>queue_number_to</i>]
<code>queue</code> [<code>flags</code> <i>QUEUE_FLAGS</i>] [<code>to</code> <i>QUEUE_EXPRESSION</i> ]
<i>QUEUE_FLAGS</i> := <i>QUEUE_FLAG</i> [<code>,</code> <i>QUEUE_FLAGS</i>]
<i>QUEUE_FLAG</i> := <code>bypass</code> | <code>fanout</code>
<i>QUEUE_EXPRESSION</i> := <code>numgen</code> | <code>hash</code> | <code>symhash</code> | <code>MAP STATEMENT</code></pre>
</dl>
<p> QUEUE_EXPRESSION can be used to compute a queue number at run-time with the hash or numgen expressions. It also allows to use the map statement to assign fixed queue numbers based on external inputs such as the source ip address or interface names. </p>
<p> <code>Table 70. queue statement values</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Value </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> queue_number </td>
<td>
<p> Sets queue number, default is 0. </td>
<td>
<p> unsigned integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> queue_number_from </td>
<td>
<p> Sets initial queue in the range, if fanout is used. </td>
<td>
<p> unsigned integer (16 bit)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> queue_number_to </td>
<td>
<p> Sets closing queue in the range, if fanout is used. </td>
<td>
<p> unsigned integer (16 bit)
</td>
</tr>
</table>
<p> <code>Table 71. queue statement flags</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Flag </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> bypass </td>
<td>
<p> Let packets go through if userspace application cannot back off. Before using this flag, read libnetfilter_queue documentation for performance tuning recommendations.
</td>
</tr>
<tr VALIGN=top>
<td>
<p> fanout </td>
<td>
<p> Distribute packets between several queues.
</td>
</tr>
</table>
<h3>Dup Statement</h3>
<p>The dup statement is used to duplicate a packet and send the copy to a different destination. </p>
<dl>
<dd>
<pre><code>dup to</code> <i>device</i>
<code>dup to</code> <i>address</i> <code>device</code> <i>device</i></pre>
</dl>
<p> <code>Table 72. Dup statement values</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Expression </code></td>
<td><code> Description </code></td>
<td><code> Type </code>
</td>
</tr>
<tr VALIGN=top>
<td>
<p> address </td>
<td>
<p> Specifies that the copy of the packet should be sent to a new gateway. </td>
<td>
<p> ipv4_addr, ipv6_addr, e.g. abcd::1234, or you can use a mapping, e.g. ip saddr map { 192.168.1.2 : 10.1.1.1 }
</td>
</tr>
<tr VALIGN=top>
<td>
<p> device </td>
<td>
<p> Specifies that the copy should be transmitted via device. </td>
<td>
<p> string
</td>
</tr>
</table>
<p> <code>Using the dup statement</code>. </p>
<dl>
<dd>
<pre># send to machine with ip address 10.2.3.4 on eth0
ip filter forward dup to 10.2.3.4 device &quot;eth0&quot;
# copy raw frame to another interface
netdev ingress dup to &quot;eth0&quot;
dup to &quot;eth0&quot;
# combine with map dst addr to gateways
dup to ip daddr map { 192.168.7.1 : &quot;eth0&quot;, 192.168.7.2 : &quot;eth1&quot; }</pre>
</dl>
<h3>Fwd Statement</h3>
<p>The fwd statement is used to redirect a raw packet to another interface. It is only available in the netdev family ingress and egress hooks. It is similar to the dup statement except that no copy is made. </p>
<p> <code>fwd to</code> <i>device</i></p>
<h3>Set Statement</h3>
<p>The set statement is used to dynamically add or update elements in a set from the packet path. The set setname must already exist in the given table and must have been created with one or both of the dynamic and the timeout flags. The dynamic flag is required if the set statement expression includes a stateful object. The timeout flag is implied if the set is created with a timeout, and is required if the set statement updates elements, rather than adding them. Furthermore, these sets should specify both a maximum set size (to prevent memory exhaustion), and their elements should have a timeout (so their number will not grow indefinitely) either from the set definition or from the statement that adds or updates them. The set statement can be used to e.g. create dynamic blacklists. </p>
<dl>
<dd>
<pre>{<code>add</code> | <code>update</code>} <code>@</code><i>setname</i> <code>{</code> <i>expression</i> [<code>timeout</code> <i>timeout</i>] [<code>comment</code> <i>string</i>] <code>}</code></pre>
</dl>
<p> <code>Example for simple blacklist</code>. </p>
<dl>
<dd>
<pre># declare a set, bound to table &quot;filter&quot;, in family &quot;ip&quot;.
# Timeout and size are mandatory because we will add elements from packet path.
# Entries will timeout after one minute, after which they might be
# re-added if limit condition persists.
nft add set ip filter blackhole \
 &quot;{ type ipv4_addr; flags dynamic; timeout 1m; size 65536; }&quot;
# declare a set to store the limit per saddr.
# This must be separate from blackhole since the timeout is different
nft add set ip filter flood \
 &quot;{ type ipv4_addr; flags dynamic; timeout 10s; size 128000; }&quot;
# whitelist internal interface.
nft add rule ip filter input meta iifname &quot;internal&quot; accept
# drop packets coming from blacklisted ip addresses.
nft add rule ip filter input ip saddr @blackhole counter drop
# add source ip addresses to the blacklist if more than 10 tcp connection
# requests occurred per second and ip address.
nft add rule ip filter input tcp flags syn tcp dport ssh \
 add @flood { ip saddr limit rate over 10/second } \
 add @blackhole { ip saddr } \
 drop
# inspect state of the sets.
nft list set ip filter flood
nft list set ip filter blackhole
# manually add two addresses to the blackhole.
nft add element filter blackhole { 10.2.3.4, 10.23.1.42 }</pre>
</dl>
<h3>Map Statement</h3>
<p>The map statement is used to lookup data based on some specific input key. </p>
<dl>
<dd>
<pre><i>expression</i> <code>map</code> <code>{</code> <i>MAP_ELEMENTS</i> <code>}</code>
<i>MAP_ELEMENTS</i> := <i>MAP_ELEMENT</i> [<code>,</code> <i>MAP_ELEMENTS</i>]
<i>MAP_ELEMENT</i> := <i>key</i> <code>:</code> <i>value</i></pre>
</dl>
<p> The <i>key</i> is a value returned by <i>expression</i>. </p>
<p> <code>Using the map statement</code>. </p>
<dl>
<dd>
<pre># select DNAT target based on TCP dport:
# connections to port 80 are redirected to 192.168.1.100,
# connections to port 8888 are redirected to 192.168.1.101
nft add rule ip nat prerouting dnat tcp dport map { 80 : 192.168.1.100, 8888 : 192.168.1.101 }
# source address based SNAT:
# packets from net 192.168.1.0/24 will appear as originating from 10.0.0.1,
# packets from net 192.168.2.0/24 will appear as originating from 10.0.0.2
nft add rule ip nat postrouting snat to ip saddr map { 192.168.1.0/24 : 10.0.0.1, 192.168.2.0/24 : 10.0.0.2 }</pre>
</dl>
<h3>Vmap Statement</h3>
<p>The verdict map (vmap) statement works analogous to the map statement, but contains verdicts as values. </p>
<dl>
<dd>
<pre><i>expression</i> <code>vmap</code> <code>{</code> <i>VMAP_ELEMENTS</i> <code>}</code>
<i>VMAP_ELEMENTS</i> := <i>VMAP_ELEMENT</i> [<code>,</code> <i>VMAP_ELEMENTS</i>]
<i>VMAP_ELEMENT</i> := <i>key</i> <code>:</code> <i>verdict</i></pre>
</dl>
<p> <code>Using the vmap statement</code>. </p>
<dl>
<dd>
<pre># jump to different chains depending on layer 4 protocol type:
nft add rule ip filter input ip protocol vmap { tcp : jump tcp-chain, udp : jump udp-chain , icmp : jump icmp-chain }</pre>
</dl>
<h2>Additional Commands</h2>
<p>These are some additional commands included in nft.</p>
<h3>Monitor</h3>
<p>The monitor command allows you to listen to Netlink events produced by the nf_tables subsystem. These are either related to creation and deletion of objects or to packets for which <code>meta nftrace</code> was enabled. When they occur, nft will print to stdout the monitored events in either JSON or native nft format. </p>
<dl>
<dd>
<pre><code>monitor</code> [<code>new</code> | <code>destroy</code>] <i>MONITOR_OBJECT</i>
<code>monitor</code> <code>trace</code>
<i>MONITOR_OBJECT</i> := <code>tables</code> | <code>chains</code> | <code>sets</code> | <code>rules</code> | <code>elements</code> | <code>ruleset</code></pre>
</dl>
<p> To filter events related to a concrete object, use one of the keywords in <i>MONITOR_OBJECT</i>. </p>
<p> To filter events related to a concrete action, use keyword <code>new</code> or <code>destroy</code>. </p>
<p> The second form of invocation takes no further options and exclusively prints events generated for packets with <code>nftrace</code> enabled. </p>
<p> Hit ^C to finish the monitor operation. </p>
<p> <code>Listen to all events, report in native nft format</code>. </p>
<dl>
<dd>
<pre>% nft monitor</pre>
</dl>
<p> <code>Listen to deleted rules, report in JSON format</code>. </p>
<dl>
<dd>
<pre>% nft -j monitor destroy rules</pre>
</dl>
<p> <code>Listen to both new and destroyed chains, in native nft format</code>. </p>
<dl>
<dd>
<pre>% nft monitor chains</pre>
</dl>
<p> <code>Listen to ruleset events such as table, chain, rule, set, counters and quotas, in native nft format</code>. </p>
<dl>
<dd>
<pre>% nft monitor ruleset</pre>
</dl>
<p> <code>Trace incoming packets from host 10.0.0.1</code>. </p>
<dl>
<dd>
<pre>% nft add rule filter input ip saddr 10.0.0.1 meta nftrace set 1
% nft monitor trace</pre>
</dl>
<h2>Error Reporting</h2>
<p>When an error is detected, nft shows the line(s) containing the error, the position of the erroneous parts in the input stream and marks up the erroneous parts using carets (^). If the error results from the combination of two expressions or statements, the part imposing the constraints which are violated is marked using tildes (~). </p>
<p> For errors returned by the kernel, nft cannot detect which parts of the input caused the error and the entire command is marked. </p>
<p> <code>Error caused by single incorrect expression</code>. </p>
<dl>
<dd>
<pre>&lt;cmdline&gt;:1:19-22: Error: Interface does not exist
filter output oif eth0
 ^^^^</pre>
</dl>
<p> <code>Error caused by invalid combination of two expressions</code>. </p>
<dl>
<dd>
<pre>&lt;cmdline&gt;:1:28-36: Error: Right hand side of relational expression (==) must be constant
filter output tcp dport == tcp dport
 ~~ ^^^^^^^^^</pre>
</dl>
<p> <code>Error returned by the kernel</code>. </p>
<dl>
<dd>
<pre>&lt;cmdline&gt;:0:0-23: Error: Could not process rule: Operation not permitted
filter output oif wlan0
^^^^^^^^^^^^^^^^^^^^^^^</pre>
</dl>
<h2>Exit Status</h2>
<p>On success, nft exits with a status of 0. Unspecified errors cause it to exit with a status of 1, memory allocation errors with a status of 2, unable to open Netlink socket with 3.</p>
<h2>See Also</h2>
<dl>
<dd>
<pre><a href="//www.systutorials.com/docs/linux/man/3-libnftables/">libnftables</a>(3), <a href="//www.systutorials.com/docs/linux/man/5-libnftables-json/">libnftables-json</a>(5), <a href="//www.systutorials.com/docs/linux/man/8-iptables/">iptables</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-ip6tables/">ip6tables</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-arptables/">arptables</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-ebtables/">ebtables</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-ip/">ip</a>(8), <a href="//www.systutorials.com/docs/linux/man/8-tc/">tc</a>(8)</pre>
</dl>
<p> There is an official wiki at: <a rel="nofollow" href="https://wiki.nftables.org">https://wiki.nftables.org</a></p>
<h2>Authors</h2>
<p>nftables was written by Patrick McHardy and Pablo Neira Ayuso, among many other contributors from the Netfilter community.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2008-2014 Patrick McHardy &lt;kaber [at] trash.net&gt; Copyright &#169; 2013-2018 Pablo Neira Ayuso &lt;pablo [at] netfilter.org&gt; </p>
<p> nftables is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software Foundation. </p>
<p> This documentation is licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0 license, CC BY-SA 4.0 <a rel="nofollow" href="http://creativecommons.org/licenses/by-sa/4.0/.">http://creativecommons.org/licenses/by-sa/4.0/.</a></p>
