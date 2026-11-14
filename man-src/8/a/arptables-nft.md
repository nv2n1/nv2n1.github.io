---
title: "arptables-nft(8)"
name: "arptables-nft"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arptables-nft/"
description: "arptables – ARP table administration (nft-based)"
---

<p>arptables &#8211; ARP table administration (nft-based)</p>
<h2>Synopsis</h2>
<p><code>arptables </code>[<code>-t table</code>]<code> &#8211;</code>[<code>AD</code>]<code> chain rule-specification </code>[<code>options</code>]<br />
 <code>arptables </code>[<code>-t table</code>]<code> &#8211;</code>[<code>RI</code>]<code> chain rulenum rule-specification </code>[<code>options</code>]<br />
 <code>arptables </code>[<code>-t table</code>]<code> -D chain rulenum </code>[<code>options</code>]<br />
 <code>arptables </code>[<code>-t table</code>]<code> &#8211;</code>[<code>LFZ</code>][<code>chain</code>][<code>options</code>]<br />
 <code>arptables </code>[<code>-t table</code>]<code> &#8211;</code>[<code>NX</code>]<code> chain</code><br />
 <code>arptables </code>[<code>-t table</code>]<code> -E old-chain-name new-chain-name</code><br />
 <code>arptables </code>[<code>-t table</code>]<code> -P chain target </code>[<code>options</code>] </p>
<h2>Description</h2>
<p><code>arptables</code> is a user space tool, it is used to set up and maintain the tables of ARP rules in the Linux kernel. These rules inspect the ARP frames which they see. <code>arptables</code> is analogous to the <code>iptables</code> user space tool, but <code>arptables</code> is less complicated.</p>
<h3>Chains</h3>
<p>The kernel table is used to divide functionality into different sets of rules. Each set of rules is called a chain. Each chain is an ordered list of rules that can match ARP frames. If a rule matches an ARP frame, then a processing specification tells what to do with that matching frame. The processing specification is called a &#8216;target&#8217;. However, if the frame does not match the current rule in the chain, then the next rule in the chain is examined and so forth. The user can create new (user-defined) chains which can be used as the &#8216;target&#8217; of a rule.</p>
<h3>Targets</h3>
<p>A firewall rule specifies criteria for an ARP frame and a frame processing specification called a target. When a frame matches a rule, then the next action performed by the kernel is specified by the target. The target can be one of these values: <i>ACCEPT</i>, <i>DROP</i>, <i>CONTINUE</i>, <i>RETURN</i>, an &#8216;extension&#8217; (see below) or a user-defined chain. </p>
<p> <i>ACCEPT</i> means to let the frame through. <i>DROP</i> means the frame has to be dropped. <i>CONTINUE</i> means the next rule has to be checked. This can be handy to know how many frames pass a certain point in the chain or to log those frames. <i>RETURN</i> means stop traversing this chain and resume at the next rule in the previous (calling) chain. For the extension targets please see the <code>TARGET EXTENSIONS</code> section of this man page.</p>
<h3>Tables</h3>
<p>There is only one ARP table in the Linux kernel. The table is <code>filter.</code> You can drop the &#8216;-t filter&#8217; argument to the arptables command. The -t argument must be the first argument on the arptables command line, if used.</p>
<dl>
<dt><code>-t, &#8211;table</code></p>
<dd><code>filter</code>, is the only table and contains two built-in chains: <code>INPUT </code> (for frames destined for the host) and <code>OUTPUT </code> (for locally-generated frames). </p>
</dl>
<h2>Arptables Command Line Arguments</h2>
<p>After the initial arptables command line argument, the remaining arguments can be divided into several different groups. These groups are commands, miscellaneous commands, rule-specifications, match-extensions, and watcher-extensions.</p>
<h3>Commands</h3>
<p>The arptables command arguments specify the actions to perform on the table defined with the -t argument. If you do not use the -t argument to name a table, the commands apply to the default filter table. With the exception of the <code>-Z</code> command, only one command may be used on the command line at a time.</p>
<dl>
<dt><code>-A, &#8211;append</code></p>
<dd>Append a rule to the end of the selected chain.</p>
<dt><code>-D, &#8211;delete</code></p>
<dd>Delete the specified rule from the selected chain. There are two ways to use this command. The first is by specifying an interval of rule numbers to delete, syntax: start_nr[:end_nr]. Using negative numbers is allowed, for more details about using negative numbers, see the -I command. The second usage is by specifying the complete rule as it would have been specified when it was added.</p>
<dt><code>-I, &#8211;insert</code></p>
<dd>Insert the specified rule into the selected chain at the specified rule number. If the current number of rules equals N, then the specified number can be between -N and N+1. For a positive number i, it holds that i and i-N-1 specify the same place in the chain where the rule should be inserted. The number 0 specifies the place past the last rule in the chain and using this number is therefore equivalent with using the -A command.</p>
<dt><code>-R, &#8211;replace</code></p>
<dd>Replaces the specified rule into the selected chain at the specified rule number. If the current number of rules equals N, then the specified number can be between 1 and N. i specifies the place in the chain where the rule should be replaced.</p>
<dt><code>-P, &#8211;policy</code></p>
<dd>Set the policy for the chain to the given target. The policy can be <code>ACCEPT</code>, <code>DROP</code> or <code>RETURN</code>.</p>
<dt><code>-F, &#8211;flush</code></p>
<dd>Flush the selected chain. If no chain is selected, then every chain will be flushed. Flushing the chain does not change the policy of the chain, however.</p>
<dt><code>-Z, &#8211;zero</code></p>
<dd>Set the counters of the selected chain to zero. If no chain is selected, all the counters are set to zero. The <code>-Z</code> command can be used in conjunction with the <code>-L</code> command. When both the <code>-Z</code> and <code>-L</code> commands are used together in this way, the rule counters are printed on the screen before they are set to zero.</p>
<dt><code>-L, &#8211;list</code></p>
<dd>List all rules in the selected chain. If no chain is selected, all chains are listed.</p>
<dt><code>-N, &#8211;new-chain</code></p>
<dd>Create a new user-defined chain with the given name. The number of user-defined chains is unlimited. A user-defined chain name has maximum length of 31 characters.</p>
<dt><code>-X, &#8211;delete-chain</code></p>
<dd>Delete the specified user-defined chain. There must be no remaining references to the specified chain, otherwise <code>arptables</code> will refuse to delete it. If no chain is specified, all user-defined chains that aren&#8217;t referenced will be removed.</p>
<dt><code>-E, &#8211;rename-chain</code></p>
<dd>Rename the specified chain to a new name. Besides renaming a user-defined chain, you may rename a standard chain name to a name that suits your taste. For example, if you like PREBRIDGING more than PREROUTING, then you can use the -E command to rename the PREROUTING chain. If you do rename one of the standard <code>arptables</code> chain names, please be sure to mention this fact should you post a question on the <code>arptables</code> mailing lists. It would be wise to use the standard name in your post. Renaming a standard <code>arptables</code> chain in this fashion has no effect on the structure or function of the <code>arptables</code> kernel table. </p>
</dl>
<h3>Miscellanous Commands</h3>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd>Show the version of the arptables userspace program.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Give a brief description of the command syntax.</p>
<dt><code>-j, &#8211;jump </code><i>target</i></p>
<dd>The target of the rule. This is one of the following values: <code>ACCEPT</code>, <code>DROP</code>, <code>CONTINUE</code>, <code>RETURN</code>, a target extension (see <code>TARGET EXTENSIONS</code>) or a user-defined chain name.</p>
<dt><code>-c, &#8211;set-counters </code><i>PKTS BYTES</i></p>
<dd>This enables the administrator to initialize the packet and byte counters of a rule (during <code>INSERT,</code> <code>APPEND,</code> <code>REPLACE</code> operations). </p>
</dl>
<h3>Rule-Specifications</h3>
<p>The following command line arguments make up a rule specification (as used in the add and delete commands). A &quot;!&quot; option before the specification inverts the test for that specification. Apart from these standard rule specifications there are some other command line arguments of interest.</p>
<dl>
<dt><code>-s, &#8211;source-ip </code>[!] <i>address</i>[/<i>mask]</i></p>
<dd>The Source IP specification.</p>
<dt><code>-d, &#8211;destination-ip </code>[!] <i>address</i>[/<i>mask]</i></p>
<dd>The Destination IP specification.</p>
<dt><code>&#8211;source-mac </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The source mac address. Both mask and address are written as 6 hexadecimal numbers separated by colons.</p>
<dt><code>&#8211;destination-mac </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The destination mac address. Both mask and address are written as 6 hexadecimal numbers separated by colons.</p>
<dt><code>-i, &#8211;in-interface </code>[!] <i>name</i></p>
<dd>The interface via which a frame is received (for the <code>INPUT</code> chain). The flag <code>&#8211;in-if</code> is an alias for this option.</p>
<dt><code>-o, &#8211;out-interface </code>[!] <i>name</i></p>
<dd>The interface via which a frame is going to be sent (for the <code>OUTPUT</code> chain). The flag <code>&#8211;out-if</code> is an alias for this option.</p>
<dt><code>-l, &#8211;h-length </code><i>length</i>[/<i>mask</i>]</p>
<dd>The hardware length (nr of bytes)</p>
<dt><code>&#8211;opcode </code><i>code</i>[/<i>mask</i>]</p>
<dd>The operation code (2 bytes). Available values are: <code>1</code>=<code>Request</code> <code>2</code>=<code>Reply</code> <code>3</code>=<code>Request_Reverse</code> <code>4</code>=<code>Reply_Reverse</code> <code>5</code>=<code>DRARP_Request</code> <code>6</code>=<code>DRARP_Reply</code> <code>7</code>=<code>DRARP_Error</code> <code>8</code>=<code>InARP_Request</code> <code>9</code>=<code>ARP_NAK</code>.</p>
<dt><code>&#8211;h-type </code><i>type</i>[/<i>mask</i>]</p>
<dd>The hardware type (2 bytes, hexadecimal). Available values are: <code>1</code>=<code>Ethernet</code>.</p>
<dt><code>&#8211;proto-type </code><i>type</i>[/<i>mask</i>]</p>
<dd>The protocol type (2 bytes). Available values are: <code>0x800</code>=<code>IPv4</code>. </p>
</dl>
<h3>Target-Extensions</h3>
<p><code>arptables</code> extensions are precompiled into the userspace tool. So there is no need to explicitly load them with a -m option like in <code>iptables</code>. However, these extensions deal with functionality supported by supplemental kernel modules.</p>
<h3>mangle</h3>
<dl>
<dt><code>&#8211;mangle-ip-s IP address</code></p>
<dd>Mangles Source IP Address to given value.</p>
<dt><code>&#8211;mangle-ip-d IP address</code></p>
<dd>Mangles Destination IP Address to given value.</p>
<dt><code>&#8211;mangle-mac-s MAC address</code></p>
<dd>Mangles Source MAC Address to given value.</p>
<dt><code>&#8211;mangle-mac-d MAC address</code></p>
<dd>Mangles Destination MAC Address to given value.</p>
<dt><code>&#8211;mangle-target target </code></p>
<dd>Target of ARP mangle operation (<code>DROP</code>, <code>CONTINUE</code> or <code>ACCEPT</code> &#8212; default is <code>ACCEPT</code>).</dl>
<h3>Classify</h3>
<p>This module allows you to set the skb-&gt;priority value (and thus clas- sify the packet into a specific CBQ class). </p>
<dl>
<dt><code>&#8211;set-class major:minor</code></p>
<dd>Set the major and minor class value. The values are always interpreted as hexadecimal even if no 0x prefix is given. </p>
</dl>
<h3>Mark</h3>
<p>This module allows you to set the skb-&gt;mark value (and thus classify the packet by the mark in u32) </p>
<dl>
<dt><code>&#8211;set-mark mark</code></p>
<dd>Set the mark value. The values are always interpreted as hexadecimal even if no 0x prefix is given </p>
<dt><code>&#8211;and-mark mark</code></p>
<dd>Binary AND the mark with bits. </p>
<dt><code>&#8211;or-mark mark</code></p>
<dd>Binary OR the mark with bits. </p>
</dl>
<h2>Notes</h2>
<p>In this nft-based version of <code>arptables</code>, support for <code>FORWARD</code> chain has not been implemented. Since ARP packets are &quot;forwarded&quot; only by Linux bridges, the same may be achieved using <code>FORWARD</code> chain in <code>ebtables</code>. </p>
<h2>Mailinglists</h2>
<p>See <code><a rel="nofollow" href="http://netfilter.org/mailinglists.html">http://netfilter.org/mailinglists.html</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xtables-nft/">xtables-nft</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/8-ebtables/">ebtables</a></code>(8), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) See <code><a rel="nofollow" href="https://wiki.nftables.org">https://wiki.nftables.org</a></code> </p>
