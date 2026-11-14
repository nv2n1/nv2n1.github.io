---
title: "ip6tables(8)"
name: "ip6tables"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip6tables/"
description: "iptables/ip6tables — administration tool for IPv4/IPv6 packet filtering and NAT"
---

<p>iptables/ip6tables &#8212; administration tool for IPv4/IPv6 packet filtering and NAT</p>
<h2>Synopsis</h2>
<p><code>iptables</code> [<code>-t</code> <i>table</i>] {<code>-A</code>|<code>-C</code>|<code>-D</code>} <i>chain</i> <i>rule-specification</i> </p>
<p> <code>ip6tables</code> [<code>-t</code> <i>table</i>] {<code>-A</code>|<code>-C</code>|<code>-D</code>} <i>chain rule-specification</i> </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] <code>-I</code> <i>chain</i> [<i>rulenum</i>] <i>rule-specification</i> </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] <code>-R</code> <i>chain rulenum rule-specification</i> </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] <code>-D</code> <i>chain rulenum</i> </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] <code>-S</code> [<i>chain</i> [<i>rulenum</i>]] </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] {<code>-F</code>|<code>-L</code>|<code>-Z</code>} [<i>chain</i> [<i>rulenum</i>]] [<i>options&#8230;</i>] </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] <code>-N</code> <i>chain</i> </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] <code>-X</code> [<i>chain</i>] </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] <code>-P</code> <i>chain target</i> </p>
<p> <code>iptables</code> [<code>-t</code> <i>table</i>] <code>-E</code> <i>old-chain-name new-chain-name</i> </p>
<p> rule-specification = [<i>matches&#8230;</i>] [<i>target</i>] </p>
<p> match = <code>-m</code> <i>matchname</i> [<i>per-match-options</i>] </p>
<p> target = <code>-j</code> <i>targetname</i> [<i>per-target-options</i>]</p>
<h2>Description</h2>
<p><code>Iptables</code> and <code>ip6tables</code> are used to set up, maintain, and inspect the tables of IPv4 and IPv6 packet filter rules in the Linux kernel. Several different tables may be defined. Each table contains a number of built-in chains and may also contain user-defined chains. </p>
<p> Each chain is a list of rules which can match a set of packets. Each rule specifies what to do with a packet that matches. This is called a `target&#8217;, which may be a jump to a user-defined chain in the same table.</p>
<h2>Targets</h2>
<p>A firewall rule specifies criteria for a packet and a target. If the packet does not match, the next rule in the chain is examined; if it does match, then the next rule is specified by the value of the target, which can be the name of a user-defined chain, one of the targets described in <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8), or one of the special values <code>ACCEPT</code>, <code>DROP</code> or <code>RETURN</code>. </p>
<p> <code>ACCEPT</code> means to let the packet through. <code>DROP</code> means to drop the packet on the floor. <code>RETURN</code> means stop traversing this chain and resume at the next rule in the previous (calling) chain. If the end of a built-in chain is reached or a rule in a built-in chain with target <code>RETURN</code> is matched, the target specified by the chain policy determines the fate of the packet.</p>
<h2>Tables</h2>
<p>There are currently five independent tables (which tables are present at any time depends on the kernel configuration options and which modules are present).</p>
<dl>
<dt><code>-t</code>, <code>&#8211;table</code> <i>table</i></p>
<dd>This option specifies the packet matching table which the command should operate on. If the kernel is configured with automatic module loading, an attempt will be made to load the appropriate module for that table if it is not already there. </p>
<p> The tables are as follows:</p>
<dl>
<dd>
<dl>
<dt><code>filter</code>:</p>
<dd>This is the default table (if no -t option is passed). It contains the built-in chains <code>INPUT</code> (for packets destined to local sockets), <code>FORWARD</code> (for packets being routed through the box), and <code>OUTPUT</code> (for locally-generated packets).</p>
<dt><code>nat</code>:</p>
<dd>This table is consulted when a packet that creates a new connection is encountered. It consists of four built-ins: <code>PREROUTING</code> (for altering packets as soon as they come in), <code>INPUT</code> (for altering packets destined for local sockets), <code>OUTPUT</code> (for altering locally-generated packets before routing), and <code>POSTROUTING</code> (for altering packets as they are about to go out). IPv6 NAT support is available since kernel 3.7.</p>
<dt><code>mangle</code>:</p>
<dd>This table is used for specialized packet alteration. Until kernel 2.4.17 it had two built-in chains: <code>PREROUTING</code> (for altering incoming packets before routing) and <code>OUTPUT</code> (for altering locally-generated packets before routing). Since kernel 2.4.18, three other built-in chains are also supported: <code>INPUT</code> (for packets coming into the box itself), <code>FORWARD</code> (for altering packets being routed through the box), and <code>POSTROUTING</code> (for altering packets as they are about to go out).</p>
<dt><code>raw</code>:</p>
<dd>This table is used mainly for configuring exemptions from connection tracking in combination with the NOTRACK target. It registers at the netfilter hooks with higher priority and is thus called before ip_conntrack, or any other IP tables. It provides the following built-in chains: <code>PREROUTING</code> (for packets arriving via any network interface) <code>OUTPUT</code> (for packets generated by local processes)</p>
<dt><code>security</code>:</p>
<dd>This table is used for Mandatory Access Control (MAC) networking rules, such as those enabled by the <code>SECMARK</code> and <code>CONNSECMARK</code> targets. Mandatory Access Control is implemented by Linux Security Modules such as SELinux. The security table is called after the filter table, allowing any Discretionary Access Control (DAC) rules in the filter table to take effect before MAC rules. This table provides the following built-in chains: <code>INPUT</code> (for packets coming into the box itself), <code>OUTPUT</code> (for altering locally-generated packets before routing), and <code>FORWARD</code> (for altering packets being routed through the box).</dl>
</dl>
</dl>
<h2>Options</h2>
<p>The options that are recognized by <code>iptables</code> and <code>ip6tables</code> can be divided into several different groups.</p>
<h3>Commands</h3>
<p>These options specify the desired action to perform. Only one of them can be specified on the command line unless otherwise stated below. For long versions of the command and option names, you need to use only enough letters to ensure that <code>iptables</code> can differentiate it from all other options.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;append</code> <i>chain rule-specification</i></p>
<dd>Append one or more rules to the end of the selected chain. When the source and/or destination names resolve to more than one address, a rule will be added for each possible address combination.</p>
<dt><code>-C</code>, <code>&#8211;check</code> <i>chain rule-specification</i></p>
<dd>Check whether a rule matching the specification does exist in the selected chain. This command uses the same logic as <code>-D</code> to find a matching entry, but does not alter the existing iptables configuration and uses its exit code to indicate success or failure.</p>
<dt><code>-D</code>, <code>&#8211;delete</code> <i>chain rule-specification</i></p>
<dd>
<dt><code>-D</code>, <code>&#8211;delete</code> <i>chain rulenum</i></p>
<dd>Delete one or more rules from the selected chain. There are two versions of this command: the rule can be specified as a number in the chain (starting at 1 for the first rule) or a rule to match.</p>
<dt><code>-I</code>, <code>&#8211;insert</code> <i>chain</i> [<i>rulenum</i>] <i>rule-specification</i></p>
<dd>Insert one or more rules in the selected chain as the given rule number. So, if the rule number is 1, the rule or rules are inserted at the head of the chain. This is also the default if no rule number is specified.</p>
<dt><code>-R</code>, <code>&#8211;replace</code> <i>chain rulenum rule-specification</i></p>
<dd>Replace a rule in the selected chain. If the source and/or destination names resolve to multiple addresses, the command will fail. Rules are numbered starting at 1.</p>
<dt><code>-L</code>, <code>&#8211;list</code> [<i>chain</i>]</p>
<dd>List all rules in the selected chain. If no chain is selected, all chains are listed. Like every other iptables command, it applies to the specified table (filter is the default), so NAT rules get listed by </p>
<pre> iptables -t nat -n -L</pre>
<p>Please note that it is often used with the <code>-n</code> option, in order to avoid long reverse DNS lookups. It is legal to specify the <code>-Z</code> (zero) option as well, in which case the chain(s) will be atomically listed and zeroed. The exact output is affected by the other arguments given. The exact rules are suppressed until you use </p>
<pre> iptables -L -v</pre>
<p>or <code><a href="/docs/linux/man/8-iptables-save/">iptables-save</a></code>(8).</p>
<dt><code>-S</code>, <code>&#8211;list-rules</code> [<i>chain</i>]</p>
<dd>Print all rules in the selected chain. If no chain is selected, all chains are printed like iptables-save. Like every other iptables command, it applies to the specified table (filter is the default).</p>
<dt><code>-F</code>, <code>&#8211;flush</code> [<i>chain</i>]</p>
<dd>Flush the selected chain (all the chains in the table if none is given). This is equivalent to deleting all the rules one by one.</p>
<dt><code>-Z</code>, <code>&#8211;zero</code> [<i>chain</i> [<i>rulenum</i>]]</p>
<dd>Zero the packet and byte counters in all chains, or only the given chain, or only the given rule in a chain. It is legal to specify the <code>-L</code>, <code>&#8211;list</code> (list) option as well, to see the counters immediately before they are cleared. (See above.)</p>
<dt><code>-N</code>, <code>&#8211;new-chain</code> <i>chain</i></p>
<dd>Create a new user-defined chain by the given name. There must be no target of that name already.</p>
<dt><code>-X</code>, <code>&#8211;delete-chain</code> [<i>chain</i>]</p>
<dd>Delete the optional user-defined chain specified. There must be no references to the chain. If there are, you must delete or replace the referring rules before the chain can be deleted. The chain must be empty, i.e. not contain any rules. If no argument is given, it will attempt to delete every non-builtin chain in the table.</p>
<dt><code>-P</code>, <code>&#8211;policy</code> <i>chain target</i></p>
<dd>Set the policy for the built-in (non-user-defined) chain to the given target. The policy target must be either <code>ACCEPT</code> or <code>DROP</code>.</p>
<dt><code>-E</code>, <code>&#8211;rename-chain</code> <i>old-chain new-chain</i></p>
<dd>Rename the user specified chain to the user supplied name. This is cosmetic, and has no effect on the structure of the table.</p>
<dt><code>-h</code></p>
<dd>Help. Give a (currently very brief) description of the command syntax.</dl>
<h3>Parameters</h3>
<p>The following parameters make up a rule specification (as used in the add, delete, insert, replace and append commands).</p>
<dl>
<dt><code>-4</code>, <code>&#8211;ipv4</code></p>
<dd>This option has no effect in iptables and iptables-restore. If a rule using the <code>-4</code> option is inserted with (and only with) ip6tables-restore, it will be silently ignored. Any other uses will throw an error. This option allows IPv4 and IPv6 rules in a single rule file for use with both iptables-restore and ip6tables-restore.</p>
<dt><code>-6</code>, <code>&#8211;ipv6</code></p>
<dd>If a rule using the <code>-6</code> option is inserted with (and only with) iptables-restore, it will be silently ignored. Any other uses will throw an error. This option allows IPv4 and IPv6 rules in a single rule file for use with both iptables-restore and ip6tables-restore. This option has no effect in ip6tables and ip6tables-restore.</p>
<dt>[<code>!</code>] <code>-p</code>, <code>&#8211;protocol</code> <i>protocol</i></p>
<dd>The protocol of the rule or of the packet to check. The specified protocol can be one of <code>tcp</code>, <code>udp</code>, <code>udplite</code>, <code>icmp</code>, <code>icmpv6</code>,<code>esp</code>, <code>ah</code>, <code>sctp</code>, <code>mh</code> or the special keyword &quot;<code>all</code>&quot;, or it can be a numeric value, representing one of these protocols or a different one. A protocol name from /etc/protocols is also allowed. A &quot;!&quot; argument before the protocol inverts the test. The number zero is equivalent to <code>all</code>. &quot;<code>all</code>&quot; will match with all protocols and is taken as default when this option is omitted. Note that, in ip6tables, IPv6 extension headers except <code>esp</code> are not allowed. <code>esp</code> and <code>ipv6-nonext</code> can be used with Kernel version 2.6.11 or later. The number zero is equivalent to <code>all</code>, which means that you cannot test the protocol field for the value 0 directly. To match on a HBH header, even if it were the last, you cannot use <code>-p 0</code>, but always need <code>-m hbh</code>.</p>
<dt>[<code>!</code>] <code>-s</code>, <code>&#8211;source</code> <i>address</i>[<code>/</code><i>mask</i>][<code>,</code><i>&#8230;</i>]</p>
<dd>Source specification. <i>Address</i> can be either a network name, a hostname, a network IP address (with <code>/</code><i>mask</i>), or a plain IP address. Hostnames will be resolved once only, before the rule is submitted to the kernel. Please note that specifying any name to be resolved with a remote query such as DNS is a really bad idea. The <i>mask</i> can be either an ipv4 network mask (for iptables) or a plain number, specifying the number of 1&#8217;s at the left side of the network mask. Thus, an iptables mask of <i>24</i> is equivalent to <i>255.255.255.0</i>. A &quot;!&quot; argument before the address specification inverts the sense of the address. The flag <code>&#8211;src</code> is an alias for this option. Multiple addresses can be specified, but this will <code>expand to multiple rules</code> (when adding with -A), or will cause multiple rules to be deleted (with -D).</p>
<dt>[<code>!</code>] <code>-d</code>, <code>&#8211;destination</code> <i>address</i>[<code>/</code><i>mask</i>][<code>,</code><i>&#8230;</i>]</p>
<dd>Destination specification. See the description of the <code>-s</code> (source) flag for a detailed description of the syntax. The flag <code>&#8211;dst</code> is an alias for this option.</p>
<dt><code>-m</code>, <code>&#8211;match</code> <i>match</i></p>
<dd>Specifies a match to use, that is, an extension module that tests for a specific property. The set of matches make up the condition under which a target is invoked. Matches are evaluated first to last as specified on the command line and work in short-circuit fashion, i.e. if one extension yields false, evaluation will stop.</p>
<dt><code>-j</code>, <code>&#8211;jump</code> <i>target</i></p>
<dd>This specifies the target of the rule; i.e., what to do if the packet matches it. The target can be a user-defined chain (other than the one this rule is in), one of the special builtin targets which decide the fate of the packet immediately, or an extension (see <code>EXTENSIONS</code> below). If this option is omitted in a rule (and <code>-g</code> is not used), then matching the rule will have no effect on the packet&#8217;s fate, but the counters on the rule will be incremented.</p>
<dt><code>-g</code>, <code>&#8211;goto</code> <i>chain</i></p>
<dd>This specifies that the processing should continue in a user specified chain. Unlike the &#8211;jump option return will not continue processing in this chain but instead in the chain that called us via &#8211;jump.</p>
<dt>[<code>!</code>] <code>-i</code>, <code>&#8211;in-interface</code> <i>name</i></p>
<dd>Name of an interface via which a packet was received (only for packets entering the <code>INPUT</code>, <code>FORWARD</code> and <code>PREROUTING</code> chains). When the &quot;!&quot; argument is used before the interface name, the sense is inverted. If the interface name ends in a &quot;+&quot;, then any interface which begins with this name will match. If this option is omitted, any interface name will match.</p>
<dt>[<code>!</code>] <code>-o</code>, <code>&#8211;out-interface</code> <i>name</i></p>
<dd>Name of an interface via which a packet is going to be sent (for packets entering the <code>FORWARD</code>, <code>OUTPUT</code> and <code>POSTROUTING</code> chains). When the &quot;!&quot; argument is used before the interface name, the sense is inverted. If the interface name ends in a &quot;+&quot;, then any interface which begins with this name will match. If this option is omitted, any interface name will match.</p>
<dt>[<code>!</code>] <code>-f</code>, <code>&#8211;fragment</code></p>
<dd>This means that the rule only refers to second and further IPv4 fragments of fragmented packets. Since there is no way to tell the source or destination ports of such a packet (or ICMP type), such a packet will not match any rules which specify them. When the &quot;!&quot; argument precedes the &quot;-f&quot; flag, the rule will only match head fragments, or unfragmented packets. This option is IPv4 specific, it is not available in ip6tables.</p>
<dt><code>-c</code>, <code>&#8211;set-counters</code> <i>packets bytes</i></p>
<dd>This enables the administrator to initialize the packet and byte counters of a rule (during <code>INSERT</code>, <code>APPEND</code>, <code>REPLACE</code> operations).</dl>
<h3>Other Options</h3>
<p>The following additional options can be specified:</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Verbose output. This option makes the list command show the interface name, the rule options (if any), and the TOS masks. The packet and byte counters are also listed, with the suffix &#8216;K&#8217;, &#8216;M&#8217; or &#8216;G&#8217; for 1000, 1,000,000 and 1,000,000,000 multipliers respectively (but see the <code>-x</code> flag to change this). For appending, insertion, deletion and replacement, this causes detailed information on the rule or rules to be printed. <code>-v</code> may be specified multiple times to possibly emit more detailed debug statements.</p>
<dt><code>-w</code>, <code>&#8211;wait</code> [<i>seconds</i>]</p>
<dd>Wait for the xtables lock. To prevent multiple instances of the program from running concurrently, an attempt will be made to obtain an exclusive lock at launch. By default, the program will exit if the lock cannot be obtained. This option will make the program wait (indefinitely or for optional <i>seconds</i>) until the exclusive lock can be obtained.</p>
<dt><code>-W</code>, <code>&#8211;wait-interval</code> <i>microseconds</i></p>
<dd>Interval to wait per each iteration. When running latency sensitive applications, waiting for the xtables lock for extended durations may not be acceptable. This option will make each iteration take the amount of time specified. The default interval is 1 second. This option only works with <code>-w</code>.</p>
<dt><code>-n</code>, <code>&#8211;numeric</code></p>
<dd>Numeric output. IP addresses and port numbers will be printed in numeric format. By default, the program will try to display them as host names, network names, or services (whenever applicable).</p>
<dt><code>-x</code>, <code>&#8211;exact</code></p>
<dd>Expand numbers. Display the exact value of the packet and byte counters, instead of only the rounded number in K&#8217;s (multiples of 1000) M&#8217;s (multiples of 1000K) or G&#8217;s (multiples of 1000M). This option is only relevant for the <code>-L</code> command.</p>
<dt><code>&#8211;line-numbers</code></p>
<dd>When listing rules, add line numbers to the beginning of each rule, corresponding to that rule&#8217;s position in the chain.</p>
<dt><code>&#8211;modprobe=</code><i>command</i></p>
<dd>When adding or inserting rules into a chain, use <i>command</i> to load any necessary modules (targets, match extensions, etc). </p>
</dl>
<h2>Lock File</h2>
<p>iptables uses the <i>/run/xtables.lock</i> file to take an exclusive lock at launch. </p>
<p> The <code>XTABLES_LOCKFILE</code> environment variable can be used to override the default setting.</p>
<h2>Match And Target Extensions</h2>
<p>iptables can use extended packet matching and target modules. A list of these is available in the <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8) manpage.</p>
<h2>Diagnostics</h2>
<p>Various error messages are printed to standard error. The exit code is 0 for correct functioning. Errors which appear to be caused by invalid or abused command line parameters cause an exit code of 2, and other errors cause an exit code of 1.</p>
<h2>Bugs</h2>
<p>Bugs? What&#8217;s this? ;-) Well, you might want to have a look at <a rel="nofollow" href="http://bugzilla.netfilter.org/">http://bugzilla.netfilter.org/</a></p>
<h2>Compatibility With Ipchains</h2>
<p>This <code>iptables</code> is very similar to ipchains by Rusty Russell. The main difference is that the chains <code>INPUT</code> and <code>OUTPUT</code> are only traversed for packets coming into the local host and originating from the local host respectively. Hence every packet only passes through one of the three chains (except loopback traffic, which involves both INPUT and OUTPUT chains); previously a forwarded packet would pass through all three. </p>
<p> The other main difference is that <code>-i</code> refers to the input interface; <code>-o</code> refers to the output interface, and both are available for packets entering the <code>FORWARD</code> chain. </p>
<p> The various forms of NAT have been separated out; <code>iptables</code> is a pure packet filter when using the default `filter&#8217; table, with optional extension modules. This should simplify much of the previous confusion over the combination of IP masquerading and packet filtering seen previously. So the following options are handled differently: </p>
<pre> -j MASQ
 -M -S
 -M -L</pre>
<p>There are several other changes in iptables.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-iptables-apply/">iptables-apply</a></code>(8), <code><a href="/docs/linux/man/8-iptables-save/">iptables-save</a></code>(8), <code><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></code>(8), <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8), </p>
<p> The packet-filtering-HOWTO details iptables usage for packet filtering, the NAT-HOWTO details NAT, the netfilter-extensions-HOWTO details the extensions that are not in the standard distribution, and the netfilter-hacking-HOWTO details the netfilter internals.<br />
 See <code><a rel="nofollow" href="http://www.netfilter.org/">http://www.netfilter.org/</a></code>.</p>
<h2>Authors</h2>
<p>Rusty Russell originally wrote iptables, in early consultation with Michael Neuling. </p>
<p> Marc Boucher made Rusty abandon ipnatctl by lobbying for a generic packet selection framework in iptables, then wrote the mangle table, the owner match, the mark stuff, and ran around doing cool stuff everywhere. </p>
<p> James Morris wrote the TOS target, and tos match. </p>
<p> Jozsef Kadlecsik wrote the REJECT target. </p>
<p> Harald Welte wrote the ULOG and NFQUEUE target, the new libiptc, as well as the TTL, DSCP, ECN matches and targets. </p>
<p> The Netfilter Core Team is: Jozsef Kadlecsik, Pablo Neira Ayuso, Eric Leblond, Florian Westphal and Arturo Borrero Gonzalez. Emeritus Core Team members are: Marc Boucher, Martin Josefsson, Yasuyuki Kozakai, James Morris, Harald Welte and Rusty Russell. </p>
<p> Man page originally written by Herve Eychenne &lt;rv [at] wallfire.org&gt;.</p>
<h2>Version</h2>
<p>This manual page applies to iptables/ip6tables 1.8.7.</p>
