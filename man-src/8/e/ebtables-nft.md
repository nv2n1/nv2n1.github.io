---
title: "ebtables-nft(8)"
name: "ebtables-nft"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ebtables-nft/"
description: "ebtables – Ethernet bridge frame table administration (nft-based)"
---

<p>ebtables &#8211; Ethernet bridge frame table administration (nft-based)</p>
<h2>Synopsis</h2>
<p><code>ebtables </code>[<code>-t</code> table ] <code>&#8211;</code>[<code>ACDI</code>] chain rule specification [match extensions] [watcher extensions] target<br />
 <code>ebtables </code>[<code>-t</code> table ] <code>-P</code> chain <code>ACCEPT</code> | <code>DROP</code> | <code>RETURN</code><br />
 <code>ebtables </code>[<code>-t</code> table ] <code>-F</code> [chain]<br />
 <code>ebtables </code>[<code>-t</code> table ] <code>-Z</code> [chain]<br />
 <code>ebtables </code>[<code>-t</code> table ] <code>-L</code> [<code>-Z</code>] [chain] [ [<code>&#8211;Ln</code>] | [<code>&#8211;Lx</code>] ] [<code>&#8211;Lc</code>] [<code>&#8211;Lmac2</code>]<br />
 <code>ebtables </code>[<code>-t</code> table ] <code>-N</code> chain [<code>-P ACCEPT </code>|<code> DROP </code>|<code> RETURN</code>]<br />
 <code>ebtables </code>[<code>-t</code> table ] <code>-X</code> [chain]<br />
 <code>ebtables </code>[<code>-t</code> table ] <code>-E</code> old-chain-name new-chain-name<br />
 <code>ebtables </code>[<code>-t</code> table ] <code>&#8211;init-table</code><br />
 <code>ebtables </code>[<code>-t</code> table ] [<code>&#8211;atomic-file</code> file] <code>&#8211;atomic-commit</code><br />
 <code>ebtables </code>[<code>-t</code> table ] [<code>&#8211;atomic-file</code> file] <code>&#8211;atomic-init</code><br />
 <code>ebtables </code>[<code>-t</code> table ] [<code>&#8211;atomic-file</code> file] <code>&#8211;atomic-save</code> </p>
<h2>Description</h2>
<p><code>ebtables</code> is an application program used to set up and maintain the tables of rules (inside the Linux kernel) that inspect Ethernet frames. It is analogous to the <code>iptables</code> application, but less complicated, due to the fact that the Ethernet protocol is much simpler than the IP protocol.</p>
<h3>Chains</h3>
<p>There are two ebtables tables with built-in chains in the Linux kernel. These tables are used to divide functionality into different sets of rules. Each set of rules is called a chain. Each chain is an ordered list of rules that can match Ethernet frames. If a rule matches an Ethernet frame, then a processing specification tells what to do with that matching frame. The processing specification is called a &#8216;target&#8217;. However, if the frame does not match the current rule in the chain, then the next rule in the chain is examined and so forth. The user can create new (user-defined) chains that can be used as the &#8216;target&#8217; of a rule. User-defined chains are very useful to get better performance over the linear traversal of the rules and are also essential for structuring the filtering rules into well-organized and maintainable sets of rules.</p>
<h3>Targets</h3>
<p>A firewall rule specifies criteria for an Ethernet frame and a frame processing specification called a target. When a frame matches a rule, then the next action performed by the kernel is specified by the target. The target can be one of these values: <code>ACCEPT</code>, <code>DROP</code>, <code>CONTINUE</code>, <code>RETURN</code>, an &#8216;extension&#8217; (see below) or a jump to a user-defined chain. </p>
<p> <code>ACCEPT</code> means to let the frame through. <code>DROP</code> means the frame has to be dropped. <code>CONTINUE</code> means the next rule has to be checked. This can be handy, f.e., to know how many frames pass a certain point in the chain, to log those frames or to apply multiple targets on a frame. <code>RETURN</code> means stop traversing this chain and resume at the next rule in the previous (calling) chain. For the extension targets please refer to the <code>TARGET EXTENSIONS</code> section of this man page.</p>
<h3>Tables</h3>
<p>As stated earlier, there are two ebtables tables in the Linux kernel. The table names are <code>filter</code> and <code>nat</code>. Of these two tables, the filter table is the default table that the command operates on. If you are working with the filter table, then you can drop the &#8216;-t filter&#8217; argument to the ebtables command. However, you will need to provide the -t argument for <code>nat</code> table. Moreover, the -t argument must be the first argument on the ebtables command line, if used.</p>
<dl>
<dt><code>-t, &#8211;table</code></p>
<dd><code>filter</code> is the default table and contains three built-in chains: <code>INPUT </code> (for frames destined for the bridge itself, on the level of the MAC destination address), <code>OUTPUT </code> (for locally-generated or (b)routed frames) and <code>FORWARD </code> (for frames being forwarded by the bridge). </p>
<p> <code>nat</code> is mostly used to change the mac addresses and contains three built-in chains: <code>PREROUTING </code> (for altering frames as soon as they come in), <code>OUTPUT </code> (for altering locally generated or (b)routed frames before they are bridged) and <code>POSTROUTING</code> (for altering frames as they are about to go out). A small note on the naming of chains PREROUTING and POSTROUTING: it would be more accurate to call them PREFORWARDING and POSTFORWARDING, but for all those who come from the iptables world to ebtables it is easier to have the same names. Note that you can change the name (<code>-E</code>) if you don&#8217;t like the default.</dl>
<h2>Ebtables Command Line Arguments</h2>
<p>After the initial ebtables &#8216;-t table&#8217; command line argument, the remaining arguments can be divided into several groups. These groups are commands, miscellaneous commands, rule specifications, match extensions, watcher extensions and target extensions.</p>
<h3>Commands</h3>
<p>The ebtables command arguments specify the actions to perform on the table defined with the -t argument. If you do not use the -t argument to name a table, the commands apply to the default filter table. Only one command may be used on the command line at a time, except when the commands <code>-L</code> and <code>-Z</code> are combined, the commands <code>-N</code> and <code>-P</code> are combined, or when <code>&#8211;atomic-file</code> is used.</p>
<dl>
<dt><code>-A, &#8211;append</code></p>
<dd>Append a rule to the end of the selected chain.</p>
<dt><code>-D, &#8211;delete</code></p>
<dd>Delete the specified rule or rules from the selected chain. There are two ways to use this command. The first is by specifying an interval of rule numbers to delete (directly after <code>-D</code>). Syntax: <i>start_nr</i>[<i>:end_nr</i>] (use <code>-L &#8211;Ln</code> to list the rules with their rule number). When <i>end_nr</i> is omitted, all rules starting from <i>start_nr</i> are deleted. Using negative numbers is allowed, for more details about using negative numbers, see the <code>-I</code> command. The second usage is by specifying the complete rule as it would have been specified when it was added. Only the first encountered rule that is the same as this specified rule, in other words the matching rule with the lowest (positive) rule number, is deleted.</p>
<dt><code>-C, &#8211;change-counters</code></p>
<dd>Change the counters of the specified rule or rules from the selected chain. There are two ways to use this command. The first is by specifying an interval of rule numbers to do the changes on (directly after <code>-C</code>). Syntax: <i>start_nr</i>[<i>:end_nr</i>] (use <code>-L &#8211;Ln</code> to list the rules with their rule number). The details are the same as for the <code>-D</code> command. The second usage is by specifying the complete rule as it would have been specified when it was added. Only the counters of the first encountered rule that is the same as this specified rule, in other words the matching rule with the lowest (positive) rule number, are changed. In the first usage, the counters are specified directly after the interval specification, in the second usage directly after <code>-C</code>. First the packet counter is specified, then the byte counter. If the specified counters start with a &#8216;+&#8217;, the counter values are added to the respective current counter values. If the specified counters start with a &#8216;-&#8216;, the counter values are decreased from the respective current counter values. No bounds checking is done. If the counters don&#8217;t start with &#8216;+&#8217; or &#8216;-&#8216;, the current counters are changed to the specified counters.</p>
<dt><code>-I, &#8211;insert</code></p>
<dd>Insert the specified rule into the selected chain at the specified rule number. If the rule number is not specified, the rule is added at the head of the chain. If the current number of rules equals <i>N</i>, then the specified number can be between <i>-N</i> and <i>N+1</i>. For a positive number <i>i</i>, it holds that <i>i</i> and <i>i-N-1</i> specify the same place in the chain where the rule should be inserted. The rule number 0 specifies the place past the last rule in the chain and using this number is therefore equivalent to using the <code>-A</code> command. Rule numbers structly smaller than 0 can be useful when more than one rule needs to be inserted in a chain.</p>
<dt><code>-P, &#8211;policy</code></p>
<dd>Set the policy for the chain to the given target. The policy can be <code>ACCEPT</code>, <code>DROP</code> or <code>RETURN</code>.</p>
<dt><code>-F, &#8211;flush</code></p>
<dd>Flush the selected chain. If no chain is selected, then every chain will be flushed. Flushing a chain does not change the policy of the chain, however.</p>
<dt><code>-Z, &#8211;zero</code></p>
<dd>Set the counters of the selected chain to zero. If no chain is selected, all the counters are set to zero. The <code>-Z</code> command can be used in conjunction with the <code>-L</code> command. When both the <code>-Z</code> and <code>-L</code> commands are used together in this way, the rule counters are printed on the screen before they are set to zero.</p>
<dt><code>-L, &#8211;list</code></p>
<dd>List all rules in the selected chain. If no chain is selected, all chains are listed.<br />
 The following options change the output of the <code>-L</code> command.<br />
 <code>&#8211;Ln</code><br />
 Places the rule number in front of every rule. This option is incompatible with the <code>&#8211;Lx</code> option.<br />
 <code>&#8211;Lc</code><br />
 Shows the counters at the end of each rule displayed by the <code>-L</code> command. Both a frame counter (pcnt) and a byte counter (bcnt) are displayed. The frame counter shows how many frames have matched the specific rule, the byte counter shows the sum of the frame sizes of these matching frames. Using this option in combination with the <code>&#8211;Lx</code> option causes the counters to be written out in the &#8216;<code>-c</code> &lt;pcnt&gt; &lt;bcnt&gt;&#8217; option format.<br />
 <code>&#8211;Lx</code><br />
 Changes the output so that it produces a set of ebtables commands that construct the contents of the chain, when specified. If no chain is specified, ebtables commands to construct the contents of the table are given, including commands for creating the user-defined chains (if any). You can use this set of commands in an ebtables boot or reload script. For example the output could be used at system startup. The <code>&#8211;Lx</code> option is incompatible with the <code>&#8211;Ln</code> listing option. Using the <code>&#8211;Lx</code> option together with the <code>&#8211;Lc</code> option will cause the counters to be written out in the &#8216;<code>-c</code> &lt;pcnt&gt; &lt;bcnt&gt;&#8217; option format.<br />
 <code>&#8211;Lmac2</code><br />
 Shows all MAC addresses with the same length, adding leading zeroes if necessary. The default representation omits leading zeroes in the addresses.</p>
<dt><code>-N, &#8211;new-chain</code></p>
<dd>Create a new user-defined chain with the given name. The number of user-defined chains is limited only by the number of possible chain names. A user-defined chain name has a maximum length of 31 characters. The standard policy of the user-defined chain is ACCEPT. The policy of the new chain can be initialized to a different standard target by using the <code>-P</code> command together with the <code>-N</code> command. In this case, the chain name does not have to be specified for the <code>-P</code> command.</p>
<dt><code>-X, &#8211;delete-chain</code></p>
<dd>Delete the specified user-defined chain. There must be no remaining references (jumps) to the specified chain, otherwise ebtables will refuse to delete it. If no chain is specified, all user-defined chains that aren&#8217;t referenced will be removed.</p>
<dt><code>-E, &#8211;rename-chain</code></p>
<dd>Rename the specified chain to a new name. Besides renaming a user-defined chain, you can rename a standard chain to a name that suits your taste. For example, if you like PREFORWARDING more than PREROUTING, then you can use the -E command to rename the PREROUTING chain. If you do rename one of the standard ebtables chain names, please be sure to mention this fact should you post a question on the ebtables mailing lists. It would be wise to use the standard name in your post. Renaming a standard ebtables chain in this fashion has no effect on the structure or functioning of the ebtables kernel table.</p>
<dt><code>&#8211;init-table</code></p>
<dd>Replace the current table data by the initial table data.</p>
<dt><code>&#8211;atomic-init</code></p>
<dd>Copy the kernel&#8217;s initial data of the table to the specified file. This can be used as the first action, after which rules are added to the file. The file can be specified using the <code>&#8211;atomic-file</code> command or through the <i>EBTABLES_ATOMIC_FILE</i> environment variable.</p>
<dt><code>&#8211;atomic-save</code></p>
<dd>Copy the kernel&#8217;s current data of the table to the specified file. This can be used as the first action, after which rules are added to the file. The file can be specified using the <code>&#8211;atomic-file</code> command or through the <i>EBTABLES_ATOMIC_FILE</i> environment variable.</p>
<dt><code>&#8211;atomic-commit</code></p>
<dd>Replace the kernel table data with the data contained in the specified file. This is a useful command that allows you to load all your rules of a certain table into the kernel at once, saving the kernel a lot of precious time and allowing atomic updates of the tables. The file which contains the table data is constructed by using either the <code>&#8211;atomic-init</code> or the <code>&#8211;atomic-save</code> command to generate a starting file. After that, using the <code>&#8211;atomic-file</code> command when constructing rules or setting the <i>EBTABLES_ATOMIC_FILE</i> environment variable allows you to extend the file and build the complete table before committing it to the kernel. This command can be very useful in boot scripts to populate the ebtables tables in a fast way.</dl>
<h3>Miscellanous Commands</h3>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd>Show the version of the ebtables userspace program.</p>
<dt><code>-h, &#8211;help </code>[<i>list of module names</i>]</p>
<dd>Give a brief description of the command syntax. Here you can also specify names of extensions and ebtables will try to write help about those extensions. E.g. <i>ebtables -h snat log ip arp</i>. Specify <i>list_extensions</i> to list all extensions supported by the userspace utility.</p>
<dt><code>-j, &#8211;jump </code><i>target</i></p>
<dd>The target of the rule. This is one of the following values: <code>ACCEPT</code>, <code>DROP</code>, <code>CONTINUE</code>, <code>RETURN</code>, a target extension (see <code>TARGET EXTENSIONS</code>) or a user-defined chain name.</p>
<dt><code>&#8211;atomic-file </code><i>file</i></p>
<dd>Let the command operate on the specified <i>file</i>. The data of the table to operate on will be extracted from the file and the result of the operation will be saved back into the file. If specified, this option should come before the command specification. An alternative that should be preferred, is setting the <i>EBTABLES_ATOMIC_FILE</i> environment variable.</p>
<dt><code>-M, &#8211;modprobe </code><i>program</i></p>
<dd>When talking to the kernel, use this <i>program</i> to try to automatically load missing kernel modules.</p>
<dt><code>&#8211;concurrent</code></p>
<dd>Use a file lock to support concurrent scripts updating the ebtables kernel tables. </p>
</dl>
<h3>Rule Specifications</h3>
<p>The following command line arguments make up a rule specification (as used in the add and delete commands). A &quot;!&quot; option before the specification inverts the test for that specification. Apart from these standard rule specifications there are some other command line arguments of interest. See both the <code>MATCH EXTENSIONS</code> and the <code>WATCHER EXTENSIONS</code> below.</p>
<dl>
<dt><code>-p, &#8211;protocol </code>[!] <i>protocol</i></p>
<dd>The protocol that was responsible for creating the frame. This can be a hexadecimal number, above <i>0x0600</i>, a name (e.g. <i>ARP</i> ) or <code>LENGTH</code>. The protocol field of the Ethernet frame can be used to denote the length of the header (802.2/802.3 networks). When the value of that field is below or equals <i>0x0600</i>, the value equals the size of the header and shouldn&#8217;t be used as a protocol number. Instead, all frames where the protocol field is used as the length field are assumed to be of the same &#8216;protocol&#8217;. The protocol name used in ebtables for these frames is <code>LENGTH</code>.<br />
 The file <code>/etc/ethertypes</code> can be used to show readable characters instead of hexadecimal numbers for the protocols. For example, <i>0x0800</i> will be represented by <i>IPV4</i>. The use of this file is not case sensitive. See that file for more information. The flag <code>&#8211;proto</code> is an alias for this option.</p>
<dt><code>-i, &#8211;in-interface </code>[!] <i>name</i></p>
<dd>The interface (bridge port) via which a frame is received (this option is useful in the <code>INPUT</code>, <code>FORWARD</code>, <code>PREROUTING</code> and <code>BROUTING</code> chains). If the interface name ends with &#8216;+&#8217;, then any interface name that begins with this name (disregarding &#8216;+&#8217;) will match. The flag <code>&#8211;in-if</code> is an alias for this option.</p>
<dt><code>&#8211;logical-in </code>[!] <i>name</i></p>
<dd>The (logical) bridge interface via which a frame is received (this option is useful in the <code>INPUT</code>, <code>FORWARD</code>, <code>PREROUTING</code> and <code>BROUTING</code> chains). If the interface name ends with &#8216;+&#8217;, then any interface name that begins with this name (disregarding &#8216;+&#8217;) will match.</p>
<dt><code>-o, &#8211;out-interface </code>[!] <i>name</i></p>
<dd>The interface (bridge port) via which a frame is going to be sent (this option is useful in the <code>OUTPUT</code>, <code>FORWARD</code> and <code>POSTROUTING</code> chains). If the interface name ends with &#8216;+&#8217;, then any interface name that begins with this name (disregarding &#8216;+&#8217;) will match. The flag <code>&#8211;out-if</code> is an alias for this option.</p>
<dt><code>&#8211;logical-out </code>[!] <i>name</i></p>
<dd>The (logical) bridge interface via which a frame is going to be sent (this option is useful in the <code>OUTPUT</code>, <code>FORWARD</code> and <code>POSTROUTING</code> chains). If the interface name ends with &#8216;+&#8217;, then any interface name that begins with this name (disregarding &#8216;+&#8217;) will match.</p>
<dt><code>-s, &#8211;source </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The source MAC address. Both mask and address are written as 6 hexadecimal numbers separated by colons. Alternatively one can specify Unicast, Multicast, Broadcast or BGA (Bridge Group Address):<br />
 <i>Unicast</i>=00:00:00:00:00:00/01:00:00:00:00:00, <i>Multicast</i>=01:00:00:00:00:00/01:00:00:00:00:00, <i>Broadcast</i>=ff:ff:ff:ff:ff:ff/ff:ff:ff:ff:ff:ff or <i>BGA</i>=01:80:c2:00:00:00/ff:ff:ff:ff:ff:ff. Note that a broadcast address will also match the multicast specification. The flag <code>&#8211;src</code> is an alias for this option.</p>
<dt><code>-d, &#8211;destination </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The destination MAC address. See <code>-s</code> (above) for more details on MAC addresses. The flag <code>&#8211;dst</code> is an alias for this option.</p>
<dt><code>-c, &#8211;set-counter </code><i>pcnt bcnt</i></p>
<dd>If used with <code>-A</code> or <code>-I</code>, then the packet and byte counters of the new rule will be set to <i>pcnt</i>, resp. <i>bcnt</i>. If used with the <code>-C</code> or <code>-D</code> commands, only rules with a packet and byte count equal to <i>pcnt</i>, resp. <i>bcnt</i> will match. </p>
</dl>
<h3>Match Extensions</h3>
<p>Ebtables extensions are dynamically loaded into the userspace tool, there is therefore no need to explicitly load them with a -m option like is done in iptables. These extensions deal with functionality supported by kernel modules supplemental to the core ebtables code.</p>
<h3>802_3</h3>
<p>Specify 802.3 DSAP/SSAP fields or SNAP type. The protocol must be specified as <i>LENGTH </i>(see the option <i> -p </i>above).</p>
<dl>
<dt><code>&#8211;802_3-sap </code>[!] <i>sap</i></p>
<dd>DSAP and SSAP are two one byte 802.3 fields. The bytes are always equal, so only one byte (hexadecimal) is needed as an argument.</p>
<dt><code>&#8211;802_3-type </code>[!] <i>type</i></p>
<dd>If the 802.3 DSAP and SSAP values are 0xaa then the SNAP type field must be consulted to determine the payload protocol. This is a two byte (hexadecimal) argument. Only 802.3 frames with DSAP/SSAP 0xaa are checked for type.</dl>
<h3>among</h3>
<p>Match a MAC address or MAC/IP address pair versus a list of MAC addresses and MAC/IP address pairs. A list entry has the following format: <i>xx:xx:xx:xx:xx:xx[=ip.ip.ip.ip][,]</i>. Multiple list entries are separated by a comma, specifying an IP address corresponding to the MAC address is optional. Multiple MAC/IP address pairs with the same MAC address but different IP address (and vice versa) can be specified. If the MAC address doesn&#8217;t match any entry from the list, the frame doesn&#8217;t match the rule (unless &quot;!&quot; was used).</p>
<dl>
<dt><code>&#8211;among-dst </code>[!] <i>list</i></p>
<dd>Compare the MAC destination to the given list. If the Ethernet frame has type <i>IPv4</i> or <i>ARP</i>, then comparison with MAC/IP destination address pairs from the list is possible.</p>
<dt><code>&#8211;among-src </code>[!] <i>list</i></p>
<dd>Compare the MAC source to the given list. If the Ethernet frame has type <i>IPv4</i> or <i>ARP</i>, then comparison with MAC/IP source address pairs from the list is possible.</p>
<dt><code>&#8211;among-dst-file </code>[!] <i>file</i></p>
<dd>Same as <code>&#8211;among-dst</code> but the list is read in from the specified file.</p>
<dt><code>&#8211;among-src-file </code>[!] <i>file</i></p>
<dd>Same as <code>&#8211;among-src</code> but the list is read in from the specified file.</dl>
<h3>arp</h3>
<p>Specify (R)ARP fields. The protocol must be specified as <i>ARP</i> or <i>RARP</i>.</p>
<dl>
<dt><code>&#8211;arp-opcode </code>[!] <i>opcode</i></p>
<dd>The (R)ARP opcode (decimal or a string, for more details see <code>ebtables -h arp</code>).</p>
<dt><code>&#8211;arp-htype </code>[!] <i>hardware type</i></p>
<dd>The hardware type, this can be a decimal or the string <i>Ethernet</i> (which sets <i>type</i> to 1). Most (R)ARP packets have Eternet as hardware type.</p>
<dt><code>&#8211;arp-ptype </code>[!] <i>protocol type</i></p>
<dd>The protocol type for which the (r)arp is used (hexadecimal or the string <i>IPv4</i>, denoting 0x0800). Most (R)ARP packets have protocol type IPv4.</p>
<dt><code>&#8211;arp-ip-src </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The (R)ARP IP source address specification.</p>
<dt><code>&#8211;arp-ip-dst </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The (R)ARP IP destination address specification.</p>
<dt><code>&#8211;arp-mac-src </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The (R)ARP MAC source address specification.</p>
<dt><code>&#8211;arp-mac-dst </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The (R)ARP MAC destination address specification.</p>
<dt>[!]<code> &#8211;arp-gratuitous</code></p>
<dd>Checks for ARP gratuitous packets: checks equality of IPv4 source address and IPv4 destination address inside the ARP header.</dl>
<h3>ip</h3>
<p>Specify IPv4 fields. The protocol must be specified as <i>IPv4</i>.</p>
<dl>
<dt><code>&#8211;ip-source </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The source IP address. The flag <code>&#8211;ip-src</code> is an alias for this option.</p>
<dt><code>&#8211;ip-destination </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The destination IP address. The flag <code>&#8211;ip-dst</code> is an alias for this option.</p>
<dt><code>&#8211;ip-tos </code>[!] <i>tos</i></p>
<dd>The IP type of service, in hexadecimal numbers. <code>IPv4</code>.</p>
<dt><code>&#8211;ip-protocol </code>[!] <i>protocol</i></p>
<dd>The IP protocol. The flag <code>&#8211;ip-proto</code> is an alias for this option.</p>
<dt><code>&#8211;ip-source-port </code>[!] <i>port1</i>[:<i>port2</i>]</p>
<dd>The source port or port range for the IP protocols 6 (TCP), 17 (UDP), 33 (DCCP) or 132 (SCTP). The <code>&#8211;ip-protocol</code> option must be specified as <i>TCP</i>, <i>UDP</i>, <i>DCCP</i> or <i>SCTP</i>. If <i>port1</i> is omitted, <i>0:port2</i> is used; if <i>port2</i> is omitted but a colon is specified, <i>port1:65535</i> is used. The flag <code>&#8211;ip-sport</code> is an alias for this option.</p>
<dt><code>&#8211;ip-destination-port </code>[!] <i>port1</i>[:<i>port2</i>]</p>
<dd>The destination port or port range for ip protocols 6 (TCP), 17 (UDP), 33 (DCCP) or 132 (SCTP). The <code>&#8211;ip-protocol</code> option must be specified as <i>TCP</i>, <i>UDP</i>, <i>DCCP</i> or <i>SCTP</i>. If <i>port1</i> is omitted, <i>0:port2</i> is used; if <i>port2</i> is omitted but a colon is specified, <i>port1:65535</i> is used. The flag <code>&#8211;ip-dport</code> is an alias for this option.</dl>
<h3>ip6</h3>
<p>Specify IPv6 fields. The protocol must be specified as <i>IPv6</i>.</p>
<dl>
<dt><code>&#8211;ip6-source </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The source IPv6 address. The flag <code>&#8211;ip6-src</code> is an alias for this option.</p>
<dt><code>&#8211;ip6-destination </code>[!] <i>address</i>[/<i>mask</i>]</p>
<dd>The destination IPv6 address. The flag <code>&#8211;ip6-dst</code> is an alias for this option.</p>
<dt><code>&#8211;ip6-tclass </code>[!] <i>tclass</i></p>
<dd>The IPv6 traffic class, in hexadecimal numbers.</p>
<dt><code>&#8211;ip6-protocol </code>[!] <i>protocol</i></p>
<dd>The IP protocol. The flag <code>&#8211;ip6-proto</code> is an alias for this option.</p>
<dt><code>&#8211;ip6-source-port </code>[!] <i>port1</i>[:<i>port2</i>]</p>
<dd>The source port or port range for the IPv6 protocols 6 (TCP), 17 (UDP), 33 (DCCP) or 132 (SCTP). The <code>&#8211;ip6-protocol</code> option must be specified as <i>TCP</i>, <i>UDP</i>, <i>DCCP</i> or <i>SCTP</i>. If <i>port1</i> is omitted, <i>0:port2</i> is used; if <i>port2</i> is omitted but a colon is specified, <i>port1:65535</i> is used. The flag <code>&#8211;ip6-sport</code> is an alias for this option.</p>
<dt><code>&#8211;ip6-destination-port </code>[!] <i>port1</i>[:<i>port2</i>]</p>
<dd>The destination port or port range for IPv6 protocols 6 (TCP), 17 (UDP), 33 (DCCP) or 132 (SCTP). The <code>&#8211;ip6-protocol</code> option must be specified as <i>TCP</i>, <i>UDP</i>, <i>DCCP</i> or <i>SCTP</i>. If <i>port1</i> is omitted, <i>0:port2</i> is used; if <i>port2</i> is omitted but a colon is specified, <i>port1:65535</i> is used. The flag <code>&#8211;ip6-dport</code> is an alias for this option.</p>
<dt><code>&#8211;ip6-icmp-type </code>[!] {<i>type</i>[:<i>type</i>]/<i>code</i>[:<i>code</i>]|<i>typename</i>}</p>
<dd>Specify ipv6-icmp type and code to match. Ranges for both type and code are supported. Type and code are separated by a slash. Valid numbers for type and range are 0 to 255. To match a single type including all valid codes, symbolic names can be used instead of numbers. The list of known type names is shown by the command </p>
<pre> ebtables --help ip6</pre>
<p>This option is only valid for &#8211;ip6-prococol ipv6-icmp.</dl>
<h3>limit</h3>
<p>This module matches at a limited rate using a token bucket filter. A rule using this extension will match until this limit is reached. It can be used with the <code>&#8211;log</code> watcher to give limited logging, for example. Its use is the same as the limit match of iptables.</p>
<dl>
<dt><code>&#8211;limit </code>[<i>value</i>]</p>
<dd>Maximum average matching rate: specified as a number, with an optional <i>/second</i>, <i>/minute</i>, <i>/hour</i>, or <i>/day</i> suffix; the default is <i>3/hour</i>.</p>
<dt><code>&#8211;limit-burst </code>[<i>number</i>]</p>
<dd>Maximum initial number of packets to match: this number gets recharged by one every time the limit specified above is not reached, up to this number; the default is <i>5</i>.</dl>
<h3>mark_m</h3>
<dl>
<dt><code>&#8211;mark </code>[!] [<i>value</i>][/<i>mask</i>]</p>
<dd>Matches frames with the given unsigned mark value. If a <i>value</i> and <i>mask</i> are specified, the logical AND of the mark value of the frame and the user-specified <i>mask</i> is taken before comparing it with the user-specified mark <i>value</i>. When only a mark <i>value</i> is specified, the packet only matches when the mark value of the frame equals the user-specified mark <i>value</i>. If only a <i>mask</i> is specified, the logical AND of the mark value of the frame and the user-specified <i>mask</i> is taken and the frame matches when the result of this logical AND is non-zero. Only specifying a <i>mask</i> is useful to match multiple mark values.</dl>
<h3>pkttype</h3>
<dl>
<dt><code>&#8211;pkttype-type </code>[!] <i>type</i></p>
<dd>Matches on the Ethernet &quot;class&quot; of the frame, which is determined by the generic networking code. Possible values: <i>broadcast</i> (MAC destination is the broadcast address), <i>multicast</i> (MAC destination is a multicast address), <i>host</i> (MAC destination is the receiving network device), or <i>otherhost</i> (none of the above).</dl>
<h3>stp</h3>
<p>Specify stp BPDU (bridge protocol data unit) fields. The destination address (<code>-d</code>) must be specified as the bridge group address <i></i>(<i>BGA</i>). For all options for which a range of values can be specified, it holds that if the lower bound is omitted (but the colon is not), then the lowest possible lower bound for that option is used, while if the upper bound is omitted (but the colon again is not), the highest possible upper bound for that option is used.</p>
<dl>
<dt><code>&#8211;stp-type </code>[!] <i>type</i></p>
<dd>The BPDU type (0-255), recognized non-numerical types are <i>config</i>, denoting a configuration BPDU (=0), and <i>tcn</i>, denothing a topology change notification BPDU (=128).</p>
<dt><code>&#8211;stp-flags </code>[!] <i>flag</i></p>
<dd>The BPDU flag (0-255), recognized non-numerical flags are <i>topology-change</i>, denoting the topology change flag (=1), and <i>topology-change-ack</i>, denoting the topology change acknowledgement flag (=128).</p>
<dt><code>&#8211;stp-root-prio </code>[!] [<i>prio</i>][:<i>prio</i>]</p>
<dd>The root priority (0-65535) range.</p>
<dt><code>&#8211;stp-root-addr </code>[!] [<i>address</i>][/<i>mask</i>]</p>
<dd>The root mac address, see the option <code>-s</code> for more details.</p>
<dt><code>&#8211;stp-root-cost </code>[!] [<i>cost</i>][:<i>cost</i>]</p>
<dd>The root path cost (0-4294967295) range.</p>
<dt><code>&#8211;stp-sender-prio </code>[!] [<i>prio</i>][:<i>prio</i>]</p>
<dd>The BPDU&#8217;s sender priority (0-65535) range.</p>
<dt><code>&#8211;stp-sender-addr </code>[!] [<i>address</i>][/<i>mask</i>]</p>
<dd>The BPDU&#8217;s sender mac address, see the option <code>-s</code> for more details.</p>
<dt><code>&#8211;stp-port </code>[!] [<i>port</i>][:<i>port</i>]</p>
<dd>The port identifier (0-65535) range.</p>
<dt><code>&#8211;stp-msg-age </code>[!] [<i>age</i>][:<i>age</i>]</p>
<dd>The message age timer (0-65535) range.</p>
<dt><code>&#8211;stp-max-age </code>[!] [<i>age</i>][:<i>age</i>]</p>
<dd>The max age timer (0-65535) range.</p>
<dt><code>&#8211;stp-hello-time </code>[!] [<i>time</i>][:<i>time</i>]</p>
<dd>The hello time timer (0-65535) range.</p>
<dt><code>&#8211;stp-forward-delay </code>[!] [<i>delay</i>][:<i>delay</i>]</p>
<dd>The forward delay timer (0-65535) range.</dl>
<h3>vlan</h3>
<p>Specify 802.1Q Tag Control Information fields. The protocol must be specified as <i>802_1Q</i> (0x8100).</p>
<dl>
<dt><code>&#8211;vlan-id </code>[!] <i>id</i></p>
<dd>The VLAN identifier field (VID). Decimal number from 0 to 4095.</p>
<dt><code>&#8211;vlan-prio </code>[!] <i>prio</i></p>
<dd>The user priority field, a decimal number from 0 to 7. The VID should be set to 0 (&quot;null VID&quot;) or unspecified (in the latter case the VID is deliberately set to 0).</p>
<dt><code>&#8211;vlan-encap </code>[!] <i>type</i></p>
<dd>The encapsulated Ethernet frame type/length. Specified as a hexadecimal number from 0x0000 to 0xFFFF or as a symbolic name from <code>/etc/ethertypes</code>. </p>
</dl>
<h3>Watcher Extensions</h3>
<p>Watchers only look at frames passing by, they don&#8217;t modify them nor decide to accept the frames or not. These watchers only see the frame if the frame matches the rule, and they see it before the target is executed.</p>
<h3>log</h3>
<p>The log watcher writes descriptive data about a frame to the syslog.</p>
<dl>
<dt><code>&#8211;log</code></p>
<dd>Log with the default loggin options: log-level= <i>info</i>, log-prefix=&quot;&quot;, no ip logging, no arp logging.</p>
<dt><code>&#8211;log-level </code><i>level</i></p>
<dd>Defines the logging level. For the possible values, see <code>ebtables -h log</code>. The default level is <i>info</i>.</p>
<dt><code>&#8211;log-prefix</code> <i>text</i></p>
<dd>Defines the prefix <i>text</i> to be printed at the beginning of the line with the logging information.</p>
<dt><code>&#8211;log-ip </code></p>
<dd>Will log the ip information when a frame made by the ip protocol matches the rule. The default is no ip information logging.</p>
<dt><code>&#8211;log-ip6 </code></p>
<dd>Will log the ipv6 information when a frame made by the ipv6 protocol matches the rule. The default is no ipv6 information logging.</p>
<dt><code>&#8211;log-arp</code></p>
<dd>Will log the (r)arp information when a frame made by the (r)arp protocols matches the rule. The default is no (r)arp information logging.</dl>
<h3>nflog</h3>
<p>The nflog watcher passes the packet to the loaded logging backend in order to log the packet. This is usually used in combination with nfnetlink_log as logging backend, which will multicast the packet through a <i>netlink</i> socket to the specified multicast group. One or more userspace processes may subscribe to the group to receive the packets.</p>
<dl>
<dt><code>&#8211;nflog</code></p>
<dd>Log with the default logging options</p>
<dt><code>&#8211;nflog-group </code><i>nlgroup</i></p>
<dd>The netlink group (1 &#8211; 2^32-1) to which packets are (only applicable for nfnetlink_log). The default value is 1.</p>
<dt><code>&#8211;nflog-prefix </code><i>prefix</i></p>
<dd>A prefix string to include in the log message, up to 30 characters long, useful for distinguishing messages in the logs.</p>
<dt><code>&#8211;nflog-range </code><i>size</i></p>
<dd>The number of bytes to be copied to userspace (only applicable for nfnetlink_log). nfnetlink_log instances may specify their own range, this option overrides it.</p>
<dt><code>&#8211;nflog-threshold </code><i>size</i></p>
<dd>Number of packets to queue inside the kernel before sending them to userspace (only applicable for nfnetlink_log). Higher values result in less overhead per packet, but increase delay until the packets reach userspace. The default value is 1.</dl>
<h3>ulog</h3>
<p>The ulog watcher passes the packet to a userspace logging daemon using netlink multicast sockets. This differs from the log watcher in the sense that the complete packet is sent to userspace instead of a descriptive text and that netlink multicast sockets are used instead of the syslog. This watcher enables parsing of packets with userspace programs, the physical bridge in and out ports are also included in the netlink messages. The ulog watcher module accepts 2 parameters when the module is loaded into the kernel (e.g. with modprobe): <code>nlbufsiz</code> specifies how big the buffer for each netlink multicast group is. If you say <i>nlbufsiz=8192</i>, for example, up to eight kB of packets will get accumulated in the kernel until they are sent to userspace. It is not possible to allocate more than 128kB. Please also keep in mind that this buffer size is allocated for each nlgroup you are using, so the total kernel memory usage increases by that factor. The default is 4096. <code>flushtimeout</code> specifies after how many hundredths of a second the queue should be flushed, even if it is not full yet. The default is 10 (one tenth of a second).</p>
<dl>
<dt><code>&#8211;ulog</code></p>
<dd>Use the default settings: ulog-prefix=&quot;&quot;, ulog-nlgroup=1, ulog-cprange=4096, ulog-qthreshold=1.</p>
<dt><code>&#8211;ulog-prefix </code><i>text</i></p>
<dd>Defines the prefix included with the packets sent to userspace.</p>
<dt><code>&#8211;ulog-nlgroup</code> <i>group</i></p>
<dd>Defines which netlink group number to use (a number from 1 to 32). Make sure the netlink group numbers used for the iptables ULOG target differ from those used for the ebtables ulog watcher. The default group number is 1.</p>
<dt><code>&#8211;ulog-cprange</code> <i>range</i></p>
<dd>Defines the maximum copy range to userspace, for packets matching the rule. The default range is 0, which means the maximum copy range is given by <code>nlbufsiz</code>. A maximum copy range larger than 128*1024 is meaningless as the packets sent to userspace have an upper size limit of 128*1024.</p>
<dt><code>&#8211;ulog-qthreshold</code> <i>threshold</i></p>
<dd>Queue at most <i>threshold</i> number of packets before sending them to userspace with a netlink socket. Note that packets can be sent to userspace before the queue is full, this happens when the ulog kernel timer goes off (the frequency of this timer depends on <code>flushtimeout</code>).</dl>
<h3>Target Extensions</h3>
<h3>arpreply</h3>
<p>The <code>arpreply</code> target can be used in the <code>PREROUTING</code> chain of the <code>nat</code> table. If this target sees an ARP request it will automatically reply with an ARP reply. The used MAC address for the reply can be specified. The protocol must be specified as <i>ARP</i>. When the ARP message is not an ARP request or when the ARP request isn&#8217;t for an IP address on an Ethernet network, it is ignored by this target (<code>CONTINUE</code>). When the ARP request is malformed, it is dropped (<code>DROP</code>).</p>
<dl>
<dt><code>&#8211;arpreply-mac </code><i>address</i></p>
<dd>Specifies the MAC address to reply with: the Ethernet source MAC and the ARP payload source MAC will be filled in with this address.</p>
<dt><code>&#8211;arpreply-target </code><i>target</i></p>
<dd>Specifies the standard target. After sending the ARP reply, the rule still has to give a standard target so ebtables knows what to do with the ARP request. The default target is <code>DROP</code>.</dl>
<h3>dnat</h3>
<p>The <code>dnat</code> target can only be used in the <code>PREROUTING</code> and <code>OUTPUT</code> chains of the <code>nat</code> table. It specifies that the destination MAC address has to be changed.</p>
<dl>
<dt><code>&#8211;to-destination </code><i>address</i></p>
<dd>Change the destination MAC address to the specified <i>address</i>. The flag <code>&#8211;to-dst</code> is an alias for this option.</p>
<dt><code>&#8211;dnat-target </code><i>target</i></p>
<dd>Specifies the standard target. After doing the dnat, the rule still has to give a standard target so ebtables knows what to do with the dnated frame. The default target is <code>ACCEPT</code>. Making it <code>CONTINUE</code> could let you use multiple target extensions on the same frame. Making it <code>DROP</code> only makes sense in the <code>BROUTING</code> chain but using the <code>redirect</code> target is more logical there. <code>RETURN</code> is also allowed. Note that using <code>RETURN</code> in a base chain is not allowed (for obvious reasons).</dl>
<h3>mark</h3>
<p>The <code>mark</code> target can be used in every chain of every table. It is possible to use the marking of a frame/packet in both ebtables and iptables, if the bridge-nf code is compiled into the kernel. Both put the marking at the same place. This allows for a form of communication between ebtables and iptables.</p>
<dl>
<dt><code>&#8211;mark-set </code><i>value</i></p>
<dd>Mark the frame with the specified non-negative <i>value</i>.</p>
<dt><code>&#8211;mark-or </code><i>value</i></p>
<dd>Or the frame with the specified non-negative <i>value</i>.</p>
<dt><code>&#8211;mark-and </code><i>value</i></p>
<dd>And the frame with the specified non-negative <i>value</i>.</p>
<dt><code>&#8211;mark-xor </code><i>value</i></p>
<dd>Xor the frame with the specified non-negative <i>value</i>.</p>
<dt><code>&#8211;mark-target </code><i>target</i></p>
<dd>Specifies the standard target. After marking the frame, the rule still has to give a standard target so ebtables knows what to do. The default target is <code>ACCEPT</code>. Making it <code>CONTINUE</code> can let you do other things with the frame in subsequent rules of the chain.</dl>
<h3>redirect</h3>
<p>The <code>redirect</code> target will change the MAC target address to that of the bridge device the frame arrived on. This target can only be used in the <code>PREROUTING</code> chain of the <code>nat</code> table. The MAC address of the bridge is used as destination address.&quot;</p>
<dl>
<dt><code>&#8211;redirect-target </code><i>target</i></p>
<dd>Specifies the standard target. After doing the MAC redirect, the rule still has to give a standard target so ebtables knows what to do. The default target is <code>ACCEPT</code>. Making it <code>CONTINUE</code> could let you use multiple target extensions on the same frame. Making it <code>DROP</code> in the <code>BROUTING</code> chain will let the frames be routed. <code>RETURN</code> is also allowed. Note that using <code>RETURN</code> in a base chain is not allowed.</dl>
<h3>snat</h3>
<p>The <code>snat</code> target can only be used in the <code>POSTROUTING</code> chain of the <code>nat</code> table. It specifies that the source MAC address has to be changed.</p>
<dl>
<dt><code>&#8211;to-source </code><i>address</i></p>
<dd>Changes the source MAC address to the specified <i>address</i>. The flag <code>&#8211;to-src</code> is an alias for this option.</p>
<dt><code>&#8211;snat-target </code><i>target</i></p>
<dd>Specifies the standard target. After doing the snat, the rule still has to give a standard target so ebtables knows what to do. The default target is <code>ACCEPT</code>. Making it <code>CONTINUE</code> could let you use multiple target extensions on the same frame. Making it <code>DROP</code> doesn&#8217;t make sense, but you could do that too. <code>RETURN</code> is also allowed. Note that using <code>RETURN</code> in a base chain is not allowed. </p>
<dt><code>&#8211;snat-arp </code></p>
<dd>Also change the hardware source address inside the arp header if the packet is an arp message and the hardware address length in the arp header is 6 bytes.
</dl>
<h2>Files</h2>
<p><i>/etc/ethertypes</i></p>
<h2>Environment Variables</h2>
<p><i>EBTABLES_ATOMIC_FILE</i></p>
<h2>Mailinglists</h2>
<p>See <code><a rel="nofollow" href="http://netfilter.org/mailinglists.html">http://netfilter.org/mailinglists.html</a></code></p>
<h2>Bugs</h2>
<p>The version of ebtables this man page ships with does not support the <code>broute</code> table. Also there is no support for <code>string</code> match. And finally, this list is probably not complete.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xtables-nft/">xtables-nft</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) See <code><a rel="nofollow" href="https://wiki.nftables.org">https://wiki.nftables.org</a></code> </p>
