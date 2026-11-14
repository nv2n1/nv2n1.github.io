---
title: "ovs-ofctl(8)"
name: "ovs-ofctl"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-ofctl/"
description: "ovs-ofctl – administer OpenFlow switches"
---

<p>ovs-ofctl &#8211; administer OpenFlow switches</p>
<h2>Synopsis</h2>
<p><code>ovs-ofctl</code> [<i>options</i>] <i>command </i>[<i>switch</i>] [<i>args</i>&#8230;]</p>
<h2>Description</h2>
<p>The <code>ovs-ofctl</code> program is a command line tool for monitoring and administering OpenFlow switches. It can also show the current state of an OpenFlow switch, including features, configuration, and table entries. It should work with any OpenFlow switch, not just Open vSwitch.</p>
<h3>OpenFlow Switch Management Commands</h3>
<p>These commands allow <code>ovs-ofctl</code> to monitor and administer an OpenFlow switch. It is able to show the current state of a switch, including features, configuration, and table entries. Most of these commands take an argument that specifies the method for connecting to an OpenFlow switch. The following connection methods are supported:</p>
<dl>
<dd>
<dl>
<dt><code>ssl:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>
<dt><code>tcp:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name) in IPv4 or IPv6 address format. Wrap IPv6 addresses in square brackets, e.g. <code>tcp:[::1]:6653</code>. For <code>ssl</code>, the <code>&#8211;private-key</code>, <code>&#8211;certificate</code>, and <code>&#8211;ca-cert</code> options are mandatory.</p>
<dd>If <i>port</i> is not specified, it defaults to 6653.</p>
<dt><code>unix:</code><i>file</i></p>
<dd>On POSIX, a Unix domain server socket named <i>file</i>.</p>
<dd>On Windows, a localhost TCP port written in <i>file</i>.</p>
<dt><i>file</i></p>
<dd>This is short for <code>unix:</code><i>file</i>, as long as <i>file</i> does not contain a colon.</p>
<dt><i>bridge</i></p>
<dd>This is short for <code>unix:/var/run/openvswitch/</code><i>bridge</i><code>.mgmt</code>, as long as <i>bridge</i> does not contain a colon.</p>
<dt>[<i>type</i><code>@</code>]<i>dp</i></p>
<dd>Attempts to look up the bridge associated with <i>dp</i> and open as above. If <i>type</i> is given, it specifies the datapath provider of <i>dp</i>, otherwise the default provider <code>system</code> is assumed.</dl>
</dl>
<dl>
<dt><code>show </code><i>switch</i></p>
<dd>Prints to the console information on <i>switch</i>, including information on its flow tables and ports.</p>
<dt><code>dump-tables </code><i>switch</i></p>
<dd>Prints to the console statistics for each of the flow tables used by <i>switch</i>.</p>
<dt><code>dump-table-features </code><i>switch</i></p>
<dd>Prints to the console features for each of the flow tables used by <i>switch</i>.</p>
<dt><code>dump-table-desc </code><i>switch</i></p>
<dd>Prints to the console configuration for each of the flow tables used by <i>switch</i> for OpenFlow 1.4+.</p>
<dt><code>mod-table </code><i>switch</i> <i>table_id</i> <i>setting</i></p>
<dd>This command configures flow table settings for OpenFlow table <i>table_id</i> within <i>switch</i>. The available settings depend on the OpenFlow version in use. In OpenFlow 1.1 and 1.2 (which must be enabled with the <code>-O</code> option) only, <code>mod-table</code> configures behavior when no flow is found when a packet is looked up in a flow table. The following <i>setting</i> values are available:</p>
<dl>
<dd>
<dl>
<dt><code>drop</code></p>
<dd>Drop the packet.</p>
<dt><code>continue</code></p>
<dd>Continue to the next table in the pipeline. (This is how an OpenFlow 1.0 switch always handles packets that do not match any flow, in tables other than the last one.)</p>
<dt><code>controller</code></p>
<dd>Send to controller. (This is how an OpenFlow 1.0 switch always handles packets that do not match any flow in the last table.)</dl>
</dl>
<dd>In OpenFlow 1.4 and later (which must be enabled with the <code>-O</code> option) only, <code>mod-table</code> configures the behavior when a controller attempts to add a flow to a flow table that is full. The following <i>setting</i> values are available:</p>
<dl>
<dd>
<dl>
<dt><code>evict</code></p>
<dd>Delete some existing flow from the flow table, according to the algorithm described for the <code>Flow_Table</code> table in <code><a href="/docs/linux/man/5-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(5).</p>
<dt><code>noevict</code></p>
<dd>Refuse to add the new flow. (Eviction might still be enabled through the <code>overflow_policy</code> column in the <code>Flow_Table</code> table documented in <code><a href="/docs/linux/man/5-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(5).)</p>
<dt><code>vacancy:</code><i>low</i><code>,</code><i>high</i></p>
<dd>Enables sending vacancy events to controllers using <code>TABLE_STATUS</code> messages, based on percentage thresholds <i>low</i> and <i>high</i>.</p>
<dt><code>novacancy</code></p>
<dd>Disables vacancy events.</dl>
</dl>
<dt><code>dump-ports </code><i>switch</i> [<i>netdev</i>]</p>
<dd>Prints to the console statistics for network devices associated with <i>switch</i>. If <i>netdev</i> is specified, only the statistics associated with that device will be printed. <i>netdev</i> can be an OpenFlow assigned port number or device name, e.g. <code>eth0</code>.</p>
<dt><code>dump-ports-desc </code><i>switch</i> [<i>port</i>]</p>
<dd>Prints to the console detailed information about network devices associated with <i>switch</i>. To dump only a specific port, specify its number as <i>port</i>. Otherwise, if <i>port</i> is omitted, or if it is specified as <code>ANY</code>, then all ports are printed. This is a subset of the information provided by the <code>show</code> command.</p>
<dd>If the connection to <i>switch</i> negotiates OpenFlow 1.0, 1.2, or 1.2, this command uses an OpenFlow extension only implemented in Open vSwitch (version 1.7 and later).</p>
<dd>Only OpenFlow 1.5 and later support dumping a specific port. Earlier versions of OpenFlow always dump all ports.</p>
<dt><code>mod-port </code><i>switch</i> <i>port</i> <i>action</i></p>
<dd>Modify characteristics of port <code>port</code> in <i>switch</i>. <i>port</i> may be an OpenFlow port number or name or the keyword <code>LOCAL</code> (the preferred way to refer to the OpenFlow local port). The <i>action</i> may be any one of the following:</p>
<dl>
<dd>
<dl>
<dt><code>up</code></p>
<dd>
<dt><code>down</code></p>
<dd>Enable or disable the interface. This is equivalent to <code>ifconfig up</code> or <code>ifconfig down</code> on a Unix system.</p>
<dt><code>stp</code></p>
<dd>
<dt><code>no-stp</code></p>
<dd>Enable or disable 802.1D spanning tree protocol (STP) on the interface. OpenFlow implementations that don&#8217;t support STP will refuse to enable it.</p>
<dt><code>receive</code></p>
<dd>
<dt><code>no-receive</code></p>
<dd>
<dt><code>receive-stp</code></p>
<dd>
<dt><code>no-receive-stp</code></p>
<dd>Enable or disable OpenFlow processing of packets received on this interface. When packet processing is disabled, packets will be dropped instead of being processed through the OpenFlow table. The <code>receive</code> or <code>no-receive</code> setting applies to all packets except 802.1D spanning tree packets, which are separately controlled by <code>receive-stp</code> or <code>no-receive-stp</code>.</p>
<dt><code>forward</code></p>
<dd>
<dt><code>no-forward</code></p>
<dd>Allow or disallow forwarding of traffic to this interface. By default, forwarding is enabled.</p>
<dt><code>flood</code></p>
<dd>
<dt><code>no-flood</code></p>
<dd>Controls whether an OpenFlow <code>flood</code> action will send traffic out this interface. By default, flooding is enabled. Disabling flooding is primarily useful to prevent loops when a spanning tree protocol is not in use.</p>
<dt><code>packet-in</code></p>
<dd>
<dt><code>no-packet-in</code></p>
<dd>Controls whether packets received on this interface that do not match a flow table entry generate a &#8220;packet in&#8221; message to the OpenFlow controller. By default, &#8220;packet in&#8221; messages are enabled.</dl>
</dl>
<dd>The <code>show</code> command displays (among other information) the configuration that <code>mod-port</code> changes.</p>
<dt><code>get-frags </code><i>switch</i></p>
<dd>Prints <i>switch</i>&#8216;s fragment handling mode. See <code>set-frags</code>, below, for a description of each fragment handling mode.</p>
<dd>The <code>show</code> command also prints the fragment handling mode among its other output.</p>
<dt><code>set-frags </code><i>switch frag_mode</i></p>
<dd>Configures <i>switch</i>&#8216;s treatment of IPv4 and IPv6 fragments. The choices for <i>frag_mode</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>normal</code></p>
<dd>Fragments pass through the flow table like non-fragmented packets. The TCP ports, UDP ports, and ICMP type and code fields are always set to 0, even for fragments where that information would otherwise be available (fragments with offset 0). This is the default fragment handling mode for an OpenFlow switch.</p>
<dt><code>drop</code></p>
<dd>Fragments are dropped without passing through the flow table.</p>
<dt><code>reassemble</code></p>
<dd>The switch reassembles fragments into full IP packets before passing them through the flow table. Open vSwitch does not implement this fragment handling mode.</p>
<dt><code>nx-match</code></p>
<dd>Fragments pass through the flow table like non-fragmented packets. The TCP ports, UDP ports, and ICMP type and code fields are available for matching for fragments with offset 0, and set to 0 in fragments with nonzero offset. This mode is a Nicira extension.</dl>
</dl>
<dd>See the description of <code>ip_frag</code>, below, for a way to match on whether a packet is a fragment and on its fragment offset.</p>
<dt><code>dump-flows </code><i>switch </i>[<i>flows</i>]</p>
<dd>Prints to the console all flow entries in <i>switch</i>&#8216;s tables that match <i>flows</i>. If <i>flows</i> is omitted, all flows in the switch are retrieved. See <code>Flow Syntax</code>, below, for the syntax of <i>flows</i>. The output format is described in <code>Table Entry Output</code>.</p>
<dd>By default, <code>ovs-ofctl</code> prints flow entries in the same order that the switch sends them, which is unlikely to be intuitive or consistent. See the description of <code>&#8211;sort</code> and <code>&#8211;rsort</code>, under <code>OPTIONS</code> below, to influence the display order.</p>
<dt><code>dump-aggregate </code><i>switch </i>[<i>flows</i>]</p>
<dd>Prints to the console aggregate statistics for flows in <i>switch</i>&#8216;s tables that match <i>flows</i>. If <i>flows</i> is omitted, the statistics are aggregated across all flows in the switch&#8217;s flow tables. See <code>Flow Syntax</code>, below, for the syntax of <i>flows</i>. The output format is described in <code>Table Entry Output</code>.</p>
<dt><code>queue-stats </code><i>switch </i>[<i>port </i>[<i>queue</i>]]</p>
<dd>Prints to the console statistics for the specified <i>queue</i> on <i>port</i> within <i>switch</i>. <i>port</i> can be an OpenFlow port number or name, the keyword <code>LOCAL</code> (the preferred way to refer to the OpenFlow local port), or the keyword <code>ALL</code>. Either of <i>port</i> or <i>queue</i> or both may be omitted (or equivalently the keyword <code>ALL</code>). If both are omitted, statistics are printed for all queues on all ports. If only <i>queue</i> is omitted, then statistics are printed for all queues on <i>port</i>; if only <i>port</i> is omitted, then statistics are printed for <i>queue</i> on every port where it exists.</dl>
<h3>OpenFlow 1.1+ Group Table Commands</h3>
<p>The following commands work only with switches that support OpenFlow 1.1 or later. Because support for OpenFlow 1.1 and later is still experimental in Open vSwitch, it is necessary to explicitly enable these protocol versions in <code>ovs-ofctl</code> (using <code>-O</code>) and in the switch itself (with the <code>protocols</code> column in the <code>Bridge</code> table). For more information, see &#8220;Q: What versions of OpenFlow does Open vSwitch support?&#8221; in the Open vSwitch FAQ.</p>
<dl>
<dt><code>dump-groups </code><i>switch</i> [<i>group</i>]</p>
<dd>Prints group entries in <i>switch</i>&#8216;s tables to console. To dump only a specific group, specify its number as <i>group</i>. Otherwise, if <i>group</i> is omitted, or if it is specified as <code>ALL</code>, then all groups are printed. Each line of output is a group entry as described in <code>Group Syntax</code> below.</p>
<dd>Only OpenFlow 1.5 and later support dumping a specific group. Earlier versions of OpenFlow always dump all groups.</p>
<dt><code>dump-group-features </code><i>switch</p>
<dd>Prints to the console the group features of the switch</i>.</p>
<dt><code>dump-group-stats </code><i>switch </i>[<i>groups</i>]</p>
<dd>Prints to the console statistics for the specified <i>groups in the switch</i>&#8216;s tables. If <i>groups</i> is omitted then statistics for all groups are printed. See <code>Group Syntax</code>, below, for the syntax of <i>groups</i>.</dl>
<h3>OpenFlow 1.3+ Switch Meter Table Commands</h3>
<p>These commands manage the meter table in an OpenFlow switch. In each case, <i>meter</i> specifies a meter entry in the format described in <code>Meter Syntax</code>, below. OpenFlow 1.3 introduced support for meters, so these commands only work with switches that support OpenFlow 1.3 or later. The caveats described for groups in the previous section also apply to meters.</p>
<dl>
<dt><code>add-meter </code><i>switch meter</i></p>
<dd>Add a meter entry to <i>switch</i>&#8216;s tables. The <i>meter</i> syntax is described in section <code>Meter Syntax</code>, below.</p>
<dt><code>mod-meter </code><i>switch meter</i></p>
<dd>Modify an existing meter.</p>
<dt><code>del-meters </code><i>switch</i></p>
<dd>
<dt><code>del-meter </code><i>switch</i> [<i>meter</i>]</p>
<dd>Delete entries from <i>switch</i>&#8216;s meter table. <i>meter</i> can specify a single meter with syntax <code>meter=</code><i>id</i>, or all meters with syntax <code>meter=all</code>.</p>
<dt><code>dump-meters </code><i>switch</i></p>
<dd>
<dt><code>dump-meter </code><i>switch</i> [<i>meter</i>]</p>
<dd>Print meter configuration. <i>meter</i> can specify a single meter with syntax <code>meter=</code><i>id</i>, or all meters with syntax <code>meter=all</code>.</p>
<dt><code>meter-stats </code><i>switch</i> [<i>meter</i>]</p>
<dd>Print meter statistics. <i>meter</i> can specify a single meter with syntax <code>meter=</code><i>id</i>, or all meters with syntax <code>meter=all</code>.</p>
<dt><code>meter-features </code><i>switch</i></p>
<dd>Print meter features.</dl>
<h3>OpenFlow Switch Flow Table Commands</h3>
<p>These commands manage the flow table in an OpenFlow switch. In each case, <i>flow</i> specifies a flow entry in the format described in <code>Flow Syntax</code>, below, <i>file</i> is a text file that contains zero or more flows in the same syntax, one per line, and the optional <code>&#8211;bundle</code> option operates the command as a single atomic transation, see option <code>&#8211;bundle</code>, below.</p>
<dl>
<dt>[<code>&#8211;bundle</code>] <code>add-flow </code><i>switch flow</i></p>
<dd>
<dt>[<code>&#8211;bundle</code>] <code>add-flow </code><i>switch </i><code>&#8211; &lt; </code><i>file</i></p>
<dd>
<dt>[<code>&#8211;bundle</code>] <code>add-flows </code><i>switch file</i></p>
<dd>Add each flow entry to <i>switch</i>&#8216;s tables. Each flow specification (e.g., each line in <i>file</i>) may start with <code>add</code>, <code>modify</code>, <code>delete</code>, <code>modify_strict</code>, or <code>delete_strict</code> keyword to specify whether a flow is to be added, modified, or deleted, and whether the modify or delete is strict or not. For backwards compatibility a flow specification without one of these keywords is treated as a flow add. All flow mods are executed in the order specified.</p>
<dt>[<code>&#8211;bundle</code>] [<code>&#8211;strict</code>] <code>mod-flows </code><i>switch flow</i></p>
<dd>
<dt>[<code>&#8211;bundle</code>] [<code>&#8211;strict</code>] <code>mod-flows </code><i>switch </i><code>&#8211; &lt; </code><i>file</i></p>
<dd>Modify the actions in entries from <i>switch</i>&#8216;s tables that match the specified flows. With <code>&#8211;strict</code>, wildcards are not treated as active for matching purposes.</p>
<dt>[<code>&#8211;bundle</code>] <code>del-flows </code><i>switch</i></p>
<dd>
<dt>[<code>&#8211;bundle</code>] [<code>&#8211;strict</code>] <code>del-flows </code><i>switch </i>[<i>flow</i>]</p>
<dd>
<dt>[<code>&#8211;bundle</code>] [<code>&#8211;strict</code>] <code>del-flows </code><i>switch </i><code>&#8211; &lt; </code><i>file</i></p>
<dd>Deletes entries from <i>switch</i>&#8216;s flow table. With only a <i>switch</i> argument, deletes all flows. Otherwise, deletes flow entries that match the specified flows. With <code>&#8211;strict</code>, wildcards are not treated as active for matching purposes.</p>
<dt>[<code>&#8211;bundle</code>] [<code>&#8211;readd</code>] <code>replace-flows </code><i>switch file</i></p>
<dd>Reads flow entries from <i>file</i> (or <code>stdin</code> if <i>file</i> is <code>&#8211;</code>) and queries the flow table from <i>switch</i>. Then it fixes up any differences, adding flows from <i>flow</i> that are missing on <i>switch</i>, deleting flows from <i>switch</i> that are not in <i>file</i>, and updating flows in <i>switch</i> whose actions, cookie, or timeouts differ in <i>file</i>.</p>
<dd>With <code>&#8211;readd</code>, <code>ovs-ofctl</code> adds all the flows from <i>file</i>, even those that exist with the same actions, cookie, and timeout in <i>switch</i>. This resets all the flow packet and byte counters to 0, which can be useful for debugging.</p>
<dt><code>diff-flows </code><i>source1 source2</i></p>
<dd>Reads flow entries from <i>source1</i> and <i>source2</i> and prints the differences. A flow that is in <i>source1</i> but not in <i>source2</i> is printed preceded by a <code>&#8211;</code>, and a flow that is in <i>source2</i> but not in <i>source1</i> is printed preceded by a <code>+</code>. If a flow exists in both <i>source1</i> and <i>source2</i> with different actions, cookie, or timeouts, then both versions are printed preceded by <code>&#8211;</code> and <code>+</code>, respectively.</p>
<dd><i>source1</i> and <i>source2</i> may each name a file or a switch. If a name begins with <code>/</code> or <code>.</code>, then it is considered to be a file name. A name that contains <code>:</code> is considered to be a switch. Otherwise, it is a file if a file by that name exists, a switch if not.</p>
<dd>For this command, an exit status of 0 means that no differences were found, 1 means that an error occurred, and 2 means that some differences were found.</p>
<dt><code>packet-out </code><i>switch in_port actions packet</i>&#8230;</p>
<dd>Connects to <i>switch</i> and instructs it to execute the OpenFlow <i>actions</i> on each <i>packet</i>. Each <code>packet</code> is specified as a series of hex digits. For the purpose of executing the actions, the packets are considered to have arrived on <i>in_port</i>, which may be an OpenFlow port number or name (e.g. <code>eth0</code>), the keyword <code>LOCAL</code> (the preferred way to refer to the OpenFlow &#8220;local&#8221; port), or the keyword <code>NONE</code> to indicate that the packet was generated by the switch itself.</dl>
<h3>OpenFlow Switch Group Table Commands</h3>
<p>These commands manage the group table in an OpenFlow switch. In each case, <i>group</i> specifies a group entry in the format described in <code>Group Syntax</code>, below, and <i>file</i> is a text file that contains zero or more groups in the same syntax, one per line.</p>
<dl>
<dt><code>add-group </code><i>switch group</i></p>
<dd>
<dt><code>add-group </code><i>switch </i><code>&#8211; &lt; </code><i>file</i></p>
<dd>
<dt><code>add-groups </code><i>switch file</i></p>
<dd>Add each group entry to <i>switch</i>&#8216;s tables.</p>
<dt><code>mod-group </code><i>switch group</i></p>
<dd>
<dt><code>mod-group </code><i>switch </i><code>&#8211; &lt; </code><i>file</i></p>
<dd>Modify the action buckets in entries from <i>switch</i>&#8216;s tables for each group entry.</p>
<dt><code>del-groups </code><i>switch</i></p>
<dd>
<dt><code>del-groups </code><i>switch </i>[<i>group</i>]</p>
<dd>
<dt><code>del-groups </code><i>switch </i><code>&#8211; &lt; </code><i>file</i></p>
<dd>Deletes entries from <i>switch</i>&#8216;s group table. With only a <i>switch</i> argument, deletes all groups. Otherwise, deletes the group for each group entry.</p>
<dt><code>insert-buckets </code><i>switch group</i></p>
<dd>
<dt><code>insert-buckets </code><i>switch </i><code>&#8211; &lt; </code><i>file</i></p>
<dd>Add buckets to an existing group present in the <i>switch</i>&#8216;s group table. If no <i>command_bucket_id</i> is present in the group specification then all buckets of the group are removed.</p>
<dt><code>remove-buckets </code><i>switch group</i></p>
<dd>
<dt><code>remove-buckets </code><i>switch </i><code>&#8211; &lt; </code><i>file</i></p>
<dd>Remove buckets to an existing group present in the <i>switch</i>&#8216;s group table. If no <i>command_bucket_id</i> is present in the group specification then all buckets of the group are removed.</dl>
<h3>OpenFlow Switch Tunnel TLV Table Commands</h3>
<p>Open vSwitch maintains a mapping table between tunnel option TLVs (defined by &lt;class, type, length&gt;) and NXM fields <code>tun_metadata</code><i>n</i>, where <i>n</i> ranges from 0 to 63, that can be operated on for the purposes of matches, actions, etc. This TLV table can be used for Geneve option TLVs or other protocols with options in same TLV format as Geneve options. This mapping must be explicitly specified by the user through the following commands. A TLV mapping is specified with the syntax <code>{class=</code><i>class</i><code>,type=</code><i>type</i><code>,len=</code><i>length</i><code>}-&gt;tun_metadata</code><i>n</i>. When an option mapping exists for a given <code>tun_metadata</code><i>n</i>, matching on the defined field becomes possible, e.g.: </p>
<pre><code>ovs-ofctl add-tlv-map br0 &quot;{class=0xffff,type=0,len=4}-&gt;tun_metadata0&quot;</code></pre>
<p> ovs-ofctl add-flow br0 tun_metadata0=1234,actions=controller</dl>
<p> A mapping should not be changed while it is in active use by a flow. The result of doing so is undefined. Currently, the TLV mapping table is shared between all OpenFlow switches in a given instance of Open vSwitch. This restriction will be lifted in the future to allow for easier management. These commands are Nicira extensions to OpenFlow and require Open vSwitch 2.5 or later.</p>
<dl>
<dt><code>add-TLV-map </code><i>switch option</i>[<code>,</code><i>option</i>]&#8230;</p>
<dd>Add each <i>option</i> to <i>switch</i>&#8216;s tables. Duplicate fields are rejected.</p>
<dt><code>del-TLV-map </code><i>switch </i>[<i>option</i>[<code>,</code><i>option</i>]]&#8230;</p>
<dd>Delete each <i>option</i> from <i>switch</i>&#8216;s table, or all option TLV mapping if no <i>option</i> is specified. Fields that aren&#8217;t mapped are ignored.</p>
<dt><code>dump-TLV-map </code><i>switch</i></p>
<dd>Show the currently mapped fields in the switch&#8217;s option table as well as switch capabilities.</dl>
<h3>OpenFlow Switch Monitoring Commands</h3>
<dl>
<dt><code>snoop </code><i>switch</i></p>
<dd>Connects to <i>switch</i> and prints to the console all OpenFlow messages received. Unlike other <code>ovs-ofctl</code> commands, if <i>switch</i> is the name of a bridge, then the <code>snoop</code> command connects to a Unix domain socket named <code>/var/run/openvswitch/</code><i>switch</i><code>.snoop</code>. <code>ovs-vswitchd</code> listens on such a socket for each bridge and sends to it all of the OpenFlow messages sent to or received from its configured OpenFlow controller. Thus, this command can be used to view OpenFlow protocol activity between a switch and its controller.</p>
<dd>When a switch has more than one controller configured, only the traffic to and from a single controller is output. If none of the controllers is configured as a master or a slave (using a Nicira extension to OpenFlow 1.0 or 1.1, or a standard request in OpenFlow 1.2 or later), then a controller is chosen arbitrarily among them. If there is a master controller, it is chosen; otherwise, if there are any controllers that are not masters or slaves, one is chosen arbitrarily; otherwise, a slave controller is chosen arbitrarily. This choice is made once at connection time and does not change as controllers reconfigure their roles.</p>
<dd>If a switch has no controller configured, or if the configured controller is disconnected, no traffic is sent, so monitoring will not show any traffic.</p>
<dt><code>monitor </code><i>switch</i> [<i>miss-len</i>] [<code>invalid_ttl</code>] [<code>watch:</code>[<i>spec</i>&#8230;]]</p>
<dd>Connects to <i>switch</i> and prints to the console all OpenFlow messages received. Usually, <i>switch</i> should specify the name of a bridge in the <code>ovs-vswitchd</code> database.</p>
<dd>If <i>miss-len</i> is provided, <code>ovs-ofctl</code> sends an OpenFlow &#8220;set configuration&#8221; message at connection setup time that requests <i>miss-len</i> bytes of each packet that misses the flow table. Open vSwitch does not send these and other asynchronous messages to an <code>ovs-ofctl monitor</code> client connection unless a nonzero value is specified on this argument. (Thus, if <i>miss-len</i> is not specified, very little traffic will ordinarily be printed.)</p>
<dd>If <code>invalid_ttl</code> is passed, <code>ovs-ofctl</code> sends an OpenFlow &#8220;set configuration&#8221; message at connection setup time that requests <code>INVALID_TTL_TO_CONTROLLER</code>, so that <code>ovs-ofctl monitor</code> can receive &#8220;packet-in&#8221; messages when TTL reaches zero on <code>dec_ttl</code> action.</p>
<dd><code>watch:</code>[<i>spec</i>&#8230;] causes <code>ovs-ofctl</code> to send a &#8220;monitor request&#8221; Nicira extension message to the switch at connection setup time. This message causes the switch to send information about flow table changes as they occur. The following comma-separated <i>spec</i> syntax is available:</p>
<dl>
<dd>
<dl>
<dt><code>!initial</code></p>
<dd>Do not report the switch&#8217;s initial flow table contents.</p>
<dt><code>!add</code></p>
<dd>Do not report newly added flows.</p>
<dt><code>!delete</code></p>
<dd>Do not report deleted flows.</p>
<dt><code>!modify</code></p>
<dd>Do not report modifications to existing flows.</p>
<dt><code>!own</code></p>
<dd>Abbreviate changes made to the flow table by <code>ovs-ofctl</code>&#8216;s own connection to the switch. (These could only occur using the <code>ofctl/send</code> command described below under <code>RUNTIME MANAGEMENT COMMANDS</code>.)</p>
<dt><code>!actions</code></p>
<dd>Do not report actions as part of flow updates.</p>
<dt><code>table=</code><i>number</i></p>
<dd>Limits the monitoring to the table with the given <i>number</i> between 0 and 254. By default, all tables are monitored.</p>
<dt><code>out_port=</code><i>port</i></p>
<dd>If set, only flows that output to <i>port</i> are monitored. The <i>port</i> may be an OpenFlow port number or keyword (e.g. <code>LOCAL</code>).</p>
<dt><i>field</i><code>=</code><i>value</i></p>
<dd>Monitors only flows that have <i>field</i> specified as the given <i>value</i>. Any syntax valid for matching on <code>dump-flows</code> may be used.</dl>
</dl>
<dd>This command may be useful for debugging switch or controller implementations. With <code>watch:</code>, it is particularly useful for observing how a controller updates flow tables.</dl>
<h3>OpenFlow Switch and Controller Commands</h3>
<p>The following commands, like those in the previous section, may be applied to OpenFlow switches, using any of the connection methods described in that section. Unlike those commands, these may also be applied to OpenFlow controllers.</p>
<dl>
<dt><code>probe </code><i>target</i></p>
<dd>Sends a single OpenFlow echo-request message to <i>target</i> and waits for the response. With the <code>-t</code> or <code>&#8211;timeout</code> option, this command can test whether an OpenFlow switch or controller is up and running.</p>
<dt><code>ping </code><i>target </i>[<i>n</i>]</p>
<dd>Sends a series of 10 echo request packets to <i>target</i> and times each reply. The echo request packets consist of an OpenFlow header plus <i>n</i> bytes (default: 64) of randomly generated payload. This measures the latency of individual requests.</p>
<dt><code>benchmark </code><i>target n count</i></p>
<dd>Sends <i>count</i> echo request packets that each consist of an OpenFlow header plus <i>n</i> bytes of payload and waits for each response. Reports the total time required. This is a measure of the maximum bandwidth to <i>target</i> for round-trips of <i>n</i>-byte messages.</dl>
<h3>Other Commands</h3>
<dl>
<dt><code>ofp-parse</code> <i>file</i></p>
<dd>Reads <i>file</i> (or <code>stdin</code> if <i>file</i> is <code>&#8211;</code>) as a series of OpenFlow messages in the binary format used on an OpenFlow connection, and prints them to the console. This can be useful for printing OpenFlow messages captured from a TCP stream.</p>
<dt><code>ofp-parse-pcap</code> <i>file</i> [<i>port</i>&#8230;]</p>
<dd>Reads <i>file</i>, which must be in the PCAP format used by network capture tools such as <code>tcpdump</code> or <code>wireshark</code>, extracts all the TCP streams for OpenFlow connections, and prints the OpenFlow messages in those connections in human-readable format on <code>stdout</code>.</p>
<dd>OpenFlow connections are distinguished by TCP port number. Non-OpenFlow packets are ignored. By default, data on TCP ports 6633 and 6653 are considered to be OpenFlow. Specify one or more <i>port</i> arguments to override the default.</p>
<dd>This command cannot usefully print SSL encrypted traffic. It does not understand IPv6.</dl>
<h3>Flow Syntax</h3>
<p>Some <code>ovs-ofctl</code> commands accept an argument that describes a flow or flows. Such flow descriptions comprise a series <i>field</i><code>=</code><i>value</i> assignments, separated by commas or white space. (Embedding spaces into a flow description normally requires quoting to prevent the shell from breaking the description into multiple arguments.) Flow descriptions should be in <code>normal form</code>. This means that a flow may only specify a value for an L3 field if it also specifies a particular L2 protocol, and that a flow may only specify an L4 field if it also specifies particular L2 and L3 protocol types. For example, if the L2 protocol type <code>dl_type</code> is wildcarded, then L3 fields <code>nw_src</code>, <code>nw_dst</code>, and <code>nw_proto</code> must also be wildcarded. Similarly, if <code>dl_type</code> or <code>nw_proto</code> (the L3 protocol type) is wildcarded, so must be the L4 fields <code>tcp_dst</code> and <code>tcp_src</code>. <code>ovs-ofctl</code> will warn about flows not in normal form. The following field assignments describe how a flow matches a packet. If any of these assignments is omitted from the flow syntax, the field is treated as a wildcard; thus, if all of them are omitted, the resulting flow matches all packets. The string <code>*</code> may be specified to explicitly mark any of these fields as a wildcard. (<code>*</code> should be quoted to protect it from shell expansion.)</p>
<dl>
<dt><code>in_port=</code><i>port</i></p>
<dd>Matches OpenFlow port <i>port</i>, which may be an OpenFlow port number or keyword (e.g. <code>LOCAL</code>). <code>ovs-ofctl show</code>.</p>
<dd>(The <code>resubmit</code> action can search OpenFlow flow tables with arbitrary <code>in_port</code> values, so flows that match port numbers that do not exist from an OpenFlow perspective can still potentially be matched.)</p>
<dt><code>dl_vlan=</code><i>vlan</i></p>
<dd>Matches IEEE 802.1q Virtual LAN tag <i>vlan</i>. Specify <code>0xffff</code> as <i>vlan</i> to match packets that are not tagged with a Virtual LAN; otherwise, specify a number between 0 and 4095, inclusive, as the 12-bit VLAN ID to match.</p>
<dt><code>dl_vlan_pcp=</code><i>priority</i></p>
<dd>Matches IEEE 802.1q Priority Code Point (PCP) <i>priority</i>, which is specified as a value between 0 and 7, inclusive. A higher value indicates a higher frame priority level.</p>
<dt><code>dl_src=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>
<dt><code>dl_dst=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>Matches an Ethernet source (or destination) address specified as 6 pairs of hexadecimal digits delimited by colons (e.g. <code>00:0A:E4:25:6B:B0</code>).</p>
<dt><code>dl_src=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>/</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>
<dt><code>dl_dst=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>/</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>Matches an Ethernet destination address specified as 6 pairs of hexadecimal digits delimited by colons (e.g. <code>00:0A:E4:25:6B:B0</code>), with a wildcard mask following the slash. Open vSwitch 1.8 and later support arbitrary masks for source and/or destination. Earlier versions only support masking the destination with the following masks:</p>
<dl>
<dd>
<dl>
<dt><code>01:00:00:00:00:00</code></p>
<dd>Match only the multicast bit. Thus, <code>dl_dst=01:00:00:00:00:00/01:00:00:00:00:00</code> matches all multicast (including broadcast) Ethernet packets, and <code>dl_dst=00:00:00:00:00:00/01:00:00:00:00:00</code> matches all unicast Ethernet packets.</p>
<dt><code>fe:ff:ff:ff:ff:ff</code></p>
<dd>Match all bits except the multicast bit. This is probably not useful.</p>
<dt><code>ff:ff:ff:ff:ff:ff</code></p>
<dd>Exact match (equivalent to omitting the mask).</p>
<dt><code>00:00:00:00:00:00</code></p>
<dd>Wildcard all bits (equivalent to <code>dl_dst=*</code>.)</dl>
</dl>
<dt><code>dl_type=</code><i>ethertype</i></p>
<dd>Matches Ethernet protocol type <i>ethertype</i>, which is specified as an integer between 0 and 65535, inclusive, either in decimal or as a hexadecimal number prefixed by <code>0x</code> (e.g. <code>0x0806</code> to match ARP packets).</p>
<dt><code>nw_src=</code><i>ip</i>[<code>/</code><i>netmask</i>]</p>
<dd>
<dt><code>nw_dst=</code><i>ip</i>[<code>/</code><i>netmask</i>]</p>
<dd>When <code>dl_type</code> is 0x0800 (possibly via shorthand, e.g. <code>ip</code> or <code>tcp</code>), matches IPv4 source (or destination) address <i>ip</i>, which may be specified as an IP address or host name (e.g. <code>192.168.1.1</code> or <code><a rel="nofollow" href="http://www.example.com">www.example.com</a></code>). The optional <i>netmask</i> allows restricting a match to an IPv4 address prefix. The netmask may be specified as a dotted quad (e.g. <code>192.168.1.0/255.255.255.0</code>) or as a CIDR block (e.g. <code>192.168.1.0/24</code>). Open vSwitch 1.8 and later support arbitrary dotted quad masks; earlier versions support only CIDR masks, that is, the dotted quads that are equivalent to some CIDR block.</p>
<dd>When <code>dl_type=0x0806</code> or <code>arp</code> is specified, matches the <code>ar_spa</code> or <code>ar_tpa</code> field, respectively, in ARP packets for IPv4 and Ethernet.</p>
<dd>When <code>dl_type=0x8035</code> or <code>rarp</code> is specified, matches the <code>ar_spa</code> or <code>ar_tpa</code> field, respectively, in RARP packets for IPv4 and Ethernet.</p>
<dd>When <code>dl_type</code> is wildcarded or set to a value other than 0x0800, 0x0806, or 0x8035, the values of <code>nw_src</code> and <code>nw_dst</code> are ignored (see <code>Flow Syntax</code> above).</p>
<dt><code>nw_proto=</code><i>proto</i></p>
<dd>
<dt><code>ip_proto=</code><i>proto</i></p>
<dd>When <code>ip</code> or <code>dl_type=0x0800</code> is specified, matches IP protocol type <i>proto</i>, which is specified as a decimal number between 0 and 255, inclusive (e.g. 1 to match ICMP packets or 6 to match TCP packets).</p>
<dd>When <code>ipv6</code> or <code>dl_type=0x86dd</code> is specified, matches IPv6 header type <i>proto</i>, which is specified as a decimal number between 0 and 255, inclusive (e.g. 58 to match ICMPv6 packets or 6 to match TCP). The header type is the terminal header as described in the <code>DESIGN</code> document.</p>
<dd>When <code>arp</code> or <code>dl_type=0x0806</code> is specified, matches the lower 8 bits of the ARP opcode. ARP opcodes greater than 255 are treated as 0.</p>
<dd>When <code>rarp</code> or <code>dl_type=0x8035</code> is specified, matches the lower 8 bits of the ARP opcode. ARP opcodes greater than 255 are treated as 0.</p>
<dd>When <code>dl_type</code> is wildcarded or set to a value other than 0x0800, 0x0806, 0x8035 or 0x86dd, the value of <code>nw_proto</code> is ignored (see <code>Flow Syntax</code> above).</p>
<dt><code>nw_tos=</code><i>tos</i></p>
<dd>Matches IP ToS/DSCP or IPv6 traffic class field <i>tos</i>, which is specified as a decimal number between 0 and 255, inclusive. Note that the two lower reserved bits are ignored for matching purposes.</p>
<dd>When <code>dl_type</code> is wildcarded or set to a value other than 0x0800 or 0x86dd, the value of <code>nw_tos</code> is ignored (see <code>Flow Syntax</code> above).</p>
<dt><code>ip_dscp=</code><i>dscp</i></p>
<dd>Matches IP ToS/DSCP or IPv6 traffic class field <i>dscp</i>, which is specified as a decimal number between 0 and 63, inclusive.</p>
<dd>When <code>dl_type</code> is wildcarded or set to a value other than 0x0800 or 0x86dd, the value of <code>ip_dscp</code> is ignored (see <code>Flow Syntax</code> above).</p>
<dt><code>nw_ecn=</code><i>ecn</i></p>
<dd>
<dt><code>ip_ecn=</code><i>ecn</i></p>
<dd>Matches <i>ecn</i> bits in IP ToS or IPv6 traffic class fields, which is specified as a decimal number between 0 and 3, inclusive.</p>
<dd>When <code>dl_type</code> is wildcarded or set to a value other than 0x0800 or 0x86dd, the value of <code>nw_ecn</code> is ignored (see <code>Flow Syntax</code> above).</p>
<dt><code>nw_ttl=</code><i>ttl</i></p>
<dd>Matches IP TTL or IPv6 hop limit value <i>ttl</i>, which is specified as a decimal number between 0 and 255, inclusive.</p>
<dd>When <code>dl_type</code> is wildcarded or set to a value other than 0x0800 or 0x86dd, the value of <code>nw_ttl</code> is ignored (see <code>Flow Syntax</code> above).</p>
<dd>
<dt><code>tcp_src=</code><i>port</i></p>
<dd>
<dt><code>tcp_dst=</code><i>port</i></p>
<dd>
<dt><code>udp_src=</code><i>port</i></p>
<dd>
<dt><code>udp_dst=</code><i>port</i></p>
<dd>
<dt><code>sctp_src=</code><i>port</i></p>
<dd>
<dt><code>sctp_dst=</code><i>port</i></p>
<dd>Matches a TCP, UDP, or SCTP source or destination port <i>port</i>, which is specified as a decimal number between 0 and 65535, inclusive.</p>
<dd>When <code>dl_type</code> and <code>nw_proto</code> are wildcarded or set to values that do not indicate an appropriate protocol, the values of these settings are ignored (see <code>Flow Syntax</code> above).</p>
<dt><code>tcp_src=</code><i>port</i><code>/</code><i>mask</i></p>
<dd>
<dt><code>tcp_dst=</code><i>port</i><code>/</code><i>mask</i></p>
<dd>
<dt><code>udp_src=</code><i>port</i><code>/</code><i>mask</i></p>
<dd>
<dt><code>udp_dst=</code><i>port</i><code>/</code><i>mask</i></p>
<dd>
<dt><code>sctp_src=</code><i>port</i><code>/</code><i>mask</i></p>
<dd>
<dt><code>sctp_dst=</code><i>port</i><code>/</code><i>mask</i></p>
<dd>Bitwise match on TCP (or UDP or SCTP) source or destination port. The <i>port</i> and <i>mask</i> are 16-bit numbers written in decimal or in hexadecimal prefixed by <code>0x</code>. Each 1-bit in <i>mask</i> requires that the corresponding bit in <i>port</i> must match. Each 0-bit in <i>mask</i> causes the corresponding bit to be ignored.</p>
<dd>Bitwise matches on transport ports are rarely useful in isolation, but a group of them can be used to reduce the number of flows required to match on a range of transport ports. For example, suppose that the goal is to match TCP source ports 1000 to 1999, inclusive. One way is to insert 1000 flows, each of which matches on a single source port. Another way is to look at the binary representations of 1000 and 1999, as follows:<br />
 <code>01111101000</code><br />
 <code>11111001111</code><br />
 and then to transform those into a series of bitwise matches that accomplish the same results:<br />
 <code>01111101xxx</code><br />
 <code>0111111xxxx</code><br />
 <code>10xxxxxxxxx</code><br />
 <code>110xxxxxxxx</code><br />
 <code>1110xxxxxxx</code><br />
 <code>11110xxxxxx</code><br />
 <code>1111100xxxx</code><br />
 which become the following when written in the syntax required by <code>ovs-ofctl</code>:<br />
 <code>tcp,tcp_src=0x03e8/0xfff8</code><br />
 <code>tcp,tcp_src=0x03f0/0xfff0</code><br />
 <code>tcp,tcp_src=0x0400/0xfe00</code><br />
 <code>tcp,tcp_src=0x0600/0xff00</code><br />
 <code>tcp,tcp_src=0x0700/0xff80</code><br />
 <code>tcp,tcp_src=0x0780/0xffc0</code><br />
 <code>tcp,tcp_src=0x07c0/0xfff0</code></p>
<dd>Only Open vSwitch 1.6 and later supports bitwise matching on transport ports.</p>
<dd>Like the exact-match forms described above, the bitwise match forms apply only when <code>dl_type</code> and <code>nw_proto</code> specify TCP or UDP or SCTP.</p>
<dt><code>tp_src=</code><i>port</i></p>
<dd>
<dt><code>tp_dst=</code><i>port</i></p>
<dd>These are deprecated generic forms of L4 port matches. In new code, please use the TCP-, UDP-, or SCTP-specific forms described above.</p>
<dt><code>tcp_flags=</code><i>flags</i><code>/</code><i>mask</i></p>
<dd>
<dt><code>tcp_flags=</code>[<code>+</code><i>flag</i>&#8230;][<code>&#8211;</code><i>flag</i>&#8230;]</p>
<dd>Bitwise match on TCP flags. The <i>flags</i> and <i>mask</i> are 16-bit numbers written in decimal or in hexadecimal prefixed by <code>0x</code>. Each 1-bit in <i>mask</i> requires that the corresponding bit in <i>flags</i> must match. Each 0-bit in <i>mask</i> causes the corresponding bit to be ignored.</p>
<dd>Alternatively, the flags can be specified by their symbolic names (listed below), each preceded by either <code>+</code> for a flag that must be set, or <code>&#8211;</code> for a flag that must be unset, without any other delimiters between the flags. Flags not mentioned are wildcarded. For example, <code>tcp,tcp_flags=+syn-ack</code> matches TCP SYNs that are not ACKs.</p>
<dd>TCP protocol currently defines 9 flag bits, and additional 3 bits are reserved (must be transmitted as zero), see RFCs 793, 3168, and 3540. The flag bits are, numbering from the least significant bit:</p>
<dl>
<dd>
<dl>
<dt><code>0: fin</code></p>
<dd>No more data from sender.</p>
<dt><code>1: syn</code></p>
<dd>Synchronize sequence numbers.</p>
<dt><code>2: rst</code></p>
<dd>Reset the connection.</p>
<dt><code>3: psh</code></p>
<dd>Push function.</p>
<dt><code>4: ack</code></p>
<dd>Acknowledgement field significant.</p>
<dt><code>5: urg</code></p>
<dd>Urgent pointer field significant.</p>
<dt><code>6: ece</code></p>
<dd>ECN Echo.</p>
<dt><code>7: cwr</code></p>
<dd>Congestion Windows Reduced.</p>
<dt><code>8: ns</code></p>
<dd>Nonce Sum.</p>
<dt><code>9-11:</code></p>
<dd>Reserved.</p>
<dt><code>12-15:</code></p>
<dd>Not matchable, must be zero.</dl>
</dl>
<dt><code>icmp_type=</code><i>type</i></p>
<dd>
<dt><code>icmp_code=</code><i>code</i></p>
<dd>When <code>dl_type</code> and <code>nw_proto</code> specify ICMP or ICMPv6, <i>type</i> matches the ICMP type and <i>code</i> matches the ICMP code. Each is specified as a decimal number between 0 and 255, inclusive.</p>
<dd>When <code>dl_type</code> and <code>nw_proto</code> take other values, the values of these settings are ignored (see <code>Flow Syntax</code> above).</p>
<dt><code>table=</code><i>number</i></p>
<dd>For flow dump commands, limits the flows dumped to those in the table with the given <i>number</i> between 0 and 254. If not specified (or if 255 is specified as <i>number</i>), then flows in all tables are dumped.</p>
<dd>For flow table modification commands, behavior varies based on the OpenFlow version used to connect to the switch:</p>
<dl>
<dd>
<dl>
<dt>OpenFlow 1.0</p>
<dd>OpenFlow 1.0 does not support <code>table</code> for modifying flows. <code>ovs-ofctl</code> will exit with an error if <code>table</code> (other than <code>table=255</code>) is specified for a switch that only supports OpenFlow 1.0.</p>
<dd>In OpenFlow 1.0, the switch chooses the table into which to insert a new flow. The Open vSwitch software switch always chooses table 0. Other Open vSwitch datapaths and other OpenFlow implementations may choose different tables.</p>
<dd>The OpenFlow 1.0 behavior in Open vSwitch for modifying or removing flows depends on whether <code>&#8211;strict</code> is used. Without <code>&#8211;strict</code>, the command applies to matching flows in all tables. With <code>&#8211;strict</code>, the command will operate on any single matching flow in any table; it will do nothing if there are matches in more than one table. (The distinction between these behaviors only matters if non-OpenFlow 1.0 commands were also used, because OpenFlow 1.0 alone cannot add flows with the same matching criteria to multiple tables.)</p>
<dt>OpenFlow 1.0 with table_id extension</p>
<dd>Open vSwitch implements an OpenFlow extension that allows the controller to specify the table on which to operate. <code>ovs-ofctl</code> automatically enables the extension when <code>table</code> is specified and OpenFlow 1.0 is used. <code>ovs-ofctl</code> automatically detects whether the switch supports the extension. As of this writing, this extension is only known to be implemented by Open vSwitch.</p>
<dd>With this extension, <code>ovs-ofctl</code> operates on the requested table when <code>table</code> is specified, and acts as described for OpenFlow 1.0 above when no <code>table</code> is specified (or for <code>table=255</code>).</p>
<dt>OpenFlow 1.1</p>
<dd>OpenFlow 1.1 requires flow table modification commands to specify a table. When <code>table</code> is not specified (or <code>table=255</code> is specified), <code>ovs-ofctl</code> defaults to table 0.</p>
<dt>OpenFlow 1.2 and later</p>
<dd>OpenFlow 1.2 and later allow flow deletion commands, but not other flow table modification commands, to operate on all flow tables, with the behavior described above for OpenFlow 1.0.</dl>
</dl>
<dt><code>metadata=</code><i>value</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches <i>value</i> either exactly or with optional <i>mask</i> in the metadata field. <i>value</i> and <i>mask</i> are 64-bit integers, by default in decimal (use a <code>0x</code> prefix to specify hexadecimal). Arbitrary <i>mask</i> values are allowed: a 1-bit in <i>mask</i> indicates that the corresponding bit in <i>value</i> must match exactly, and a 0-bit wildcards that bit. Matching on metadata was added in Open vSwitch 1.8.</dl>
<p> The following shorthand notations are also available:</p>
<dl>
<dt><code>ip</code></p>
<dd>Same as <code>dl_type=0x0800</code>.</p>
<dt><code>ipv6</code></p>
<dd>Same as <code>dl_type=0x86dd</code>.</p>
<dt><code>icmp</code></p>
<dd>Same as <code>dl_type=0x0800,nw_proto=1</code>.</p>
<dt><code>icmp6</code></p>
<dd>Same as <code>dl_type=0x86dd,nw_proto=58</code>.</p>
<dt><code>tcp</code></p>
<dd>Same as <code>dl_type=0x0800,nw_proto=6</code>.</p>
<dt><code>tcp6</code></p>
<dd>Same as <code>dl_type=0x86dd,nw_proto=6</code>.</p>
<dt><code>udp</code></p>
<dd>Same as <code>dl_type=0x0800,nw_proto=17</code>.</p>
<dt><code>udp6</code></p>
<dd>Same as <code>dl_type=0x86dd,nw_proto=17</code>.</p>
<dt><code>sctp</code></p>
<dd>Same as <code>dl_type=0x0800,nw_proto=132</code>.</p>
<dt><code>sctp6</code></p>
<dd>Same as <code>dl_type=0x86dd,nw_proto=132</code>.</p>
<dt><code>arp</code></p>
<dd>Same as <code>dl_type=0x0806</code>.</p>
<dt><code>rarp</code></p>
<dd>Same as <code>dl_type=0x8035</code>.</p>
<dt><code>mpls</code></p>
<dd>Same as <code>dl_type=0x8847</code>.</p>
<dt><code>mplsm</code></p>
<dd>Same as <code>dl_type=0x8848</code>.</dl>
<p> The following field assignments require support for the NXM (Nicira Extended Match) extension to OpenFlow. When one of these is specified, <code>ovs-ofctl</code> will automatically attempt to negotiate use of this extension. If the switch does not support NXM, then <code>ovs-ofctl</code> will report a fatal error.</p>
<dl>
<dt><code>vlan_tci=</code><i>tci</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches modified VLAN TCI <i>tci</i>. If <i>mask</i> is omitted, <i>tci</i> is the exact VLAN TCI to match; if <i>mask</i> is specified, then a 1-bit in <i>mask</i> indicates that the corresponding bit in <i>tci</i> must match exactly, and a 0-bit wildcards that bit. Both <i>tci</i> and <i>mask</i> are 16-bit values that are decimal by default; use a <code>0x</code> prefix to specify them in hexadecimal.</p>
<dd>The value that <code>vlan_tci</code> matches against is 0 for a packet that has no 802.1Q header. Otherwise, it is the TCI value from the 802.1Q header with the CFI bit (with value <code>0x1000</code>) forced to 1.</p>
<dd>Examples:</p>
<dl>
<dd>
<dl>
<dt><code>vlan_tci=0</code></p>
<dd>Match only packets without an 802.1Q header.</p>
<dt><code>vlan_tci=0xf123</code></p>
<dd>Match packets tagged with priority 7 in VLAN 0x123.</p>
<dt><code>vlan_tci=0x1123/0x1fff</code></p>
<dd>Match packets tagged with VLAN 0x123 (and any priority).</p>
<dt><code>vlan_tci=0x5000/0xf000</code></p>
<dd>Match packets tagged with priority 2 (in any VLAN).</p>
<dt><code>vlan_tci=0/0xfff</code></p>
<dd>Match packets with no 802.1Q header or tagged with VLAN 0 (and any priority).</p>
<dt><code>vlan_tci=0x5000/0xe000</code></p>
<dd>Match packets with no 802.1Q header or tagged with priority 2 (in any VLAN).</p>
<dt><code>vlan_tci=0/0xefff</code></p>
<dd>Match packets with no 802.1Q header or tagged with VLAN 0 and priority 0.</dl>
</dl>
<dd>Some of these matching possibilities can also be achieved with <code>dl_vlan</code> and <code>dl_vlan_pcp</code>.</p>
<dt><code>ip_frag=</code><i>frag_type</i></p>
<dd>When <code>dl_type</code> specifies IP or IPv6, <i>frag_type</i> specifies what kind of IP fragments or non-fragments to match. The following values of <i>frag_type</i> are supported:</p>
<dl>
<dd>
<dl>
<dt><code>no</code></p>
<dd>Matches only non-fragmented packets.</p>
<dt><code>yes</code></p>
<dd>Matches all fragments.</p>
<dt><code>first</code></p>
<dd>Matches only fragments with offset 0.</p>
<dt><code>later</code></p>
<dd>Matches only fragments with nonzero offset.</p>
<dt><code>not_later</code></p>
<dd>Matches non-fragmented packets and fragments with zero offset.</dl>
</dl>
<dd>The <code>ip_frag</code> match type is likely to be most useful in <code>nx-match</code> mode. See the description of the <code>set-frags</code> command, above, for more details.</p>
<dt><code>arp_spa=</code><i>ip</i>[<code>/</code><i>netmask</i>]</p>
<dd>
<dt><code>arp_tpa=</code><i>ip</i>[<code>/</code><i>netmask</i>]</p>
<dd>When <code>dl_type</code> specifies either ARP or RARP, <code>arp_spa</code> and <code>arp_tpa</code> match the source and target IPv4 address, respectively. An address may be specified as an IP address or host name (e.g. <code>192.168.1.1</code> or <code><a rel="nofollow" href="http://www.example.com">www.example.com</a></code>). The optional <i>netmask</i> allows restricting a match to an IPv4 address prefix. The netmask may be specified as a dotted quad (e.g. <code>192.168.1.0/255.255.255.0</code>) or as a CIDR block (e.g. <code>192.168.1.0/24</code>).</p>
<dt><code>arp_sha=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>
<dt><code>arp_tha=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>When <code>dl_type</code> specifies either ARP or RARP, <code>arp_sha</code> and <code>arp_tha</code> match the source and target hardware address, respectively. An address is specified as 6 pairs of hexadecimal digits delimited by colons (e.g. <code>00:0A:E4:25:6B:B0</code>).</p>
<dt><code>arp_sha=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>/</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>
<dt><code>arp_tha=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>/</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>When <code>dl_type</code> specifies either ARP or RARP, <code>arp_sha</code> and <code>arp_tha</code> match the source and target hardware address, respectively. An address is specified as 6 pairs of hexadecimal digits delimited by colons (e.g. <code>00:0A:E4:25:6B:B0</code>), with a wildcard mask following the slash.</p>
<dt><code>arp_op=</code><i>opcode</i></p>
<dd>When <code>dl_type</code> specifies either ARP or RARP, <code>arp_op</code> matches the ARP opcode. Only ARP opcodes between 1 and 255 should be specified for matching.</p>
<dt><code>ipv6_src=</code><i>ipv6</i>[<code>/</code><i>netmask</i>]</p>
<dd>
<dt><code>ipv6_dst=</code><i>ipv6</i>[<code>/</code><i>netmask</i>]</p>
<dd>When <code>dl_type</code> is 0x86dd (possibly via shorthand, e.g., <code>ipv6</code> or <code>tcp6</code>), matches IPv6 source (or destination) address <i>ipv6</i>, which may be specified as defined in RFC 2373. The preferred format is <i>x</i><code>:</code><i>x</i><code>:</code><i>x</i><code>:</code><i>x</i><code>:</code><i>x</i><code>:</code><i>x</i><code>:</code><i>x</i><code>:</code><i>x</i>, where <i>x</i> are the hexadecimal values of the eight 16-bit pieces of the address. A single instance of <code>::</code> may be used to indicate multiple groups of 16-bits of zeros. The optional <i>netmask</i> allows restricting a match to an IPv6 address prefix. A netmask is specified as an IPv6 address (e.g. <code>2001:db8:3c4d:1::/ffff:ffff:ffff:ffff::</code>) or a CIDR block (e.g. <code>2001:db8:3c4d:1::/64</code>). Open vSwitch 1.8 and later support arbitrary masks; earlier versions support only CIDR masks, that is, CIDR block and IPv6 addresses that are equivalent to CIDR blocks.</p>
<dt><code>ipv6_label=</code><i>label</i></p>
<dd>When <code>dl_type</code> is 0x86dd (possibly via shorthand, e.g., <code>ipv6</code> or <code>tcp6</code>), matches IPv6 flow label <i>label</i>.</p>
<dt><code>nd_target=</code><i>ipv6</i>[<code>/</code><i>netmask</i>]</p>
<dd>When <code>dl_type</code>, <code>nw_proto</code>, and <code>icmp_type</code> specify IPv6 Neighbor Discovery (ICMPv6 type 135 or 136), matches the target address <i>ipv6</i>. <i>ipv6</i> is in the same format described earlier for the <code>ipv6_src</code> and <code>ipv6_dst</code> fields.</p>
<dt><code>nd_sll=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>When <code>dl_type</code>, <code>nw_proto</code>, and <code>icmp_type</code> specify IPv6 Neighbor Solicitation (ICMPv6 type 135), matches the source link-layer address option. An address is specified as 6 pairs of hexadecimal digits delimited by colons.</p>
<dt><code>nd_tll=</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i><code>:</code><i>xx</i></p>
<dd>When <code>dl_type</code>, <code>nw_proto</code>, and <code>icmp_type</code> specify IPv6 Neighbor Advertisement (ICMPv6 type 136), matches the target link-layer address option. An address is specified as 6 pairs of hexadecimal digits delimited by colons.</p>
<dt><code>mpls_bos=</code><i>bos</i></p>
<dd>When <code>dl_type</code> is 0x8847 or 0x8848 (possibly via shorthand e.g., <code>mpls</code> or <code>mplsm</code>), matches the bottom-of-stack bit of the outer-most MPLS label stack entry. Valid values are 0 and 1.</p>
<dd>If 1 then for a packet with a well-formed MPLS label stack the bottom-of-stack bit indicates that the outer label stack entry is also the inner-most label stack entry and thus that is that there is only one label stack entry present. Conversely, if 0 then for a packet with a well-formed MPLS label stack the bottom-of-stack bit indicates that the outer label stack entry is not the inner-most label stack entry and thus there is more than one label stack entry present.</p>
<dt><code>mpls_label=</code><i>label</i></p>
<dd>When <code>dl_type</code> is 0x8847 or 0x8848 (possibly via shorthand e.g., <code>mpls</code> or <code>mplsm</code>), matches the label of the outer MPLS label stack entry. The label is a 20-bit value that is decimal by default; use a <code>0x</code> prefix to specify them in hexadecimal.</p>
<dt><code>mpls_tc=</code><i>tc</i></p>
<dd>When <code>dl_type</code> is 0x8847 or 0x8848 (possibly via shorthand e.g., <code>mpls</code> or <code>mplsm</code>), matches the traffic-class of the outer MPLS label stack entry. Valid values are between 0 (lowest) and 7 (highest).</p>
<dt><code>tun_id=</code><i>tunnel-id</i>[<code>/</code><i>mask</i>]</p>
<dd>
<dt><code>tunnel_id=</code><i>tunnel-id</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches tunnel identifier <i>tunnel-id</i>. Only packets that arrive over a tunnel that carries a key (e.g. GRE with the RFC 2890 key extension and a nonzero key value) will have a nonzero tunnel ID. If <i>mask</i> is omitted, <i>tunnel-id</i> is the exact tunnel ID to match; if <i>mask</i> is specified, then a 1-bit in <i>mask</i> indicates that the corresponding bit in <i>tunnel-id</i> must match exactly, and a 0-bit wildcards that bit.</p>
<dt><code>tun_flags=</code><i>flags</i></p>
<dd>Matches flags indicating various aspects of the tunnel encapsulation. Currently, there is only one flag defined:</p>
<dd><code>oam</code>: The tunnel protocol indicated that this is an OAM control packet.</p>
<dd>Flags can be prefixed by <code>+</code> or <code>&#8211;</code> to indicate that the flag should be matched as either present or not present, respectively. In addition, flags can be specified without a prefix and separated by <code>|</code> to indicate an exact match.</p>
<dd>Note that it is possible for newer version of Open vSwitch to introduce additional flags with varying meaning. It is therefore not recommended to use an exact match on this field since the behavior of these new flags is unknown and should be ignored.</p>
<dd>For non-tunneled packets, the value is 0.</p>
<dd>This field was introduced in Open vSwitch 2.5.</p>
<dt><code>tun_src=</code><i>ip</i>[<code>/</code><i>netmask</i>]</p>
<dd>
<dt><code>tun_dst=</code><i>ip</i>[<code>/</code><i>netmask</i>]</p>
<dd>Matches tunnel IPv4 source (or destination) address <i>ip</i>. Only packets that arrive over a tunnel will have nonzero tunnel addresses. The address may be specified as an IP address or host name (e.g. <code>192.168.1.1</code> or <code><a rel="nofollow" href="http://www.example.com">www.example.com</a></code>). The optional <i>netmask</i> allows restricting a match to a masked IPv4 address. The netmask may be specified as a dotted quad (e.g. <code>192.168.1.0/255.255.255.0</code>) or as a CIDR block (e.g. <code>192.168.1.0/24</code>).</p>
<dt><code>tun_gbp_id=</code><i>value</i>[<code>/</code><i>mask</i>]</p>
<dd>
<dt><code>tun_gbp_flags=</code><i>value</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches the group policy identifier and flags in the VXLAN header. Only packets that arrive over a VXLAN tunnel with the &quot;gbp&quot; extension enabled can have this field set. The fields may also be referred to by NXM_NX_TUN_GBP_ID[] (16 bits) and NXM_NX_TUN_GBP_FLAGS[] (8 bits) in the context of field manipulation actions. If these fields are set and the packet matched by the flow is encapsulated in a VXLAN-GBP tunnel, then the policy identifier and flags are transmitted to the destination VXLAN tunnel endpoint.</p>
<dd>The <code>tun_gbp_flags</code> field has the following format:</p>
<dd>+-+-+-+-+-+-+-+-+<br />
 |-|D|-|-|A|-|-|-|<br />
 +-+-+-+-+-+-+-+-+ <code>D :=</code> Don&#8217;t Learn bit. When set, this bit indicates that the egress tunnel endpoint MUST NOT learn the source address of the encapsulated frame. <code>A :=</code> Indicates that the group policy has already been applied to this packet. Policies MUST NOT be applied by devices when the A bit is set.</p>
<dd>For more information, please see the corresponding IETF draft: <a rel="nofollow" href="https://tools.ietf.org/html/draft-smith-vxlan-group-policy">https://tools.ietf.org/html/draft-smith-vxlan-group-policy</a></p>
<dt><code>tun_metadata</code><i>idx</i>[<code>=</code><i>value</i>[<code>/</code><i>mask</i>]]</p>
<dd>Matches <i>value</i> either exactly or with optional <i>mask</i> in tunnel metadata field number <i>idx</i> (numbered from 0 to 63). The act of specifying a field implies a match on the existence of that field in the packet in addition to the masked value. As a shorthand, it is possible to specify only the field name to simply match on an option being present.</p>
<dd>Tunnel metadata fields can be dynamically assigned onto the data contained in the option TLVs of packets (e.g. Geneve variable options stores zero or more options in TLV format and tunnel metadata can be assigned onto these option TLVs) using the commands described in the section <code>OpenFlow Switch Tunnel TLV Table Commands</code>. Once assigned, the length of the field is variable according to the size of the option. Before updating a mapping in the option table, flows with references to it should be removed, otherwise the result is non-deterministic.</p>
<dd>These fields were introduced in Open vSwitch 2.5.</p>
<dt><code>reg</code><i>idx</i><code>=</code><i>value</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches <i>value</i> either exactly or with optional <i>mask</i> in register number <i>idx</i>. The valid range of <i>idx</i> depends on the switch. <i>value</i> and <i>mask</i> are 32-bit integers, by default in decimal (use a <code>0x</code> prefix to specify hexadecimal). Arbitrary <i>mask</i> values are allowed: a 1-bit in <i>mask</i> indicates that the corresponding bit in <i>value</i> must match exactly, and a 0-bit wildcards that bit.</p>
<dd>When a packet enters an OpenFlow switch, all of the registers are set to 0. Only explicit actions change register values.</p>
<dt><code>xreg</code><i>idx</i><code>=</code><i>value</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches <i>value</i> either exactly or with optional <i>mask</i> in 64-bit &#8220;extended register&#8221; number <i>idx</i>. Each of the 64-bit extended registers overlays two of the 32-bit registers: <code>xreg0</code> overlays <code>reg0</code> and <code>reg1</code>, with <code>reg0</code> supplying the most-significant bits of <code>xreg0</code> and <code>reg1</code> the least-significant. <code>xreg1</code> similarly overlays <code>reg2</code> and <code>reg3</code>, and so on.</p>
<dd>These fields were added in Open vSwitch 2.3 to conform with the OpenFlow 1.5 specification. OpenFlow 1.5 calls these fields just the &#8220;packet registers,&#8221; but Open vSwitch already had 32-bit registers by that name, which is why Open vSwitch refers to the standard registers as &#8220;extended registers&#8221;.</p>
<dt><code>pkt_mark=</code><i>value</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches packet metadata mark <i>value</i> either exactly or with optional <i>mask</i>. The mark is associated data that may be passed into other system components in order to facilitate interaction between subsystems. On Linux this corresponds to the skb mark but the exact implementation is platform-dependent.</p>
<dt><code>actset_output=</code><i>port</i></p>
<dd>Matches the output port currently in the OpenFlow action set, where <i>port</i> may be an OpenFlow port number or keyword (e.g. <code>LOCAL</code>). If there is no output port in the OpenFlow action set, or if the output port will be ignored (e.g. because there is an output group in the OpenFlow action set), then the value will be <code>UNSET</code>.</p>
<dd>This field was introduced in Open vSwitch 2.4 to conform with the OpenFlow 1.5 specification.</p>
<dt><code>conj_id=</code><i>value</i></p>
<dd>Matches the given 32-bit <i>value</i> against the conjunction ID. This is used only with the <code>conjunction</code> action (see below).</p>
<dd>This field was introduced in Open vSwitch 2.4.</p>
<dt><code>ct_state=</code><i>flags</i><code>/</code><i>mask</i></p>
<dd>
<dt><code>ct_state=</code>[<code>+</code><i>flag</i>&#8230;][<code>&#8211;</code><i>flag</i>&#8230;]</p>
<dd>Bitwise match on connection state flags. This is used with the <code>ct</code> action (see below).</p>
<dd>The <code>ct_state</code> field provides information from a connection tracking module. It describes whether the packet has previously traversed the connection tracker (tracked, or trk) and, if it has been tracked, any additional information that the connection tracker was able to provide about the connection that the current packet belongs to.</p>
<dd>Individual packets may be in one of two states: Untracked or tracked. When the <code>ct</code> action is executed on a packet, it becomes tracked for the the remainder of OpenFlow pipeline processing. Once a packet has become tracked, the state of its corresponding connection may be determined. Note that the <code>ct_state</code> is only significant for the current <code>ct_zone</code>.</p>
<dd>Connections may be in one of two states: uncommitted or committed. Connections are uncommitted by default. To determine ongoing information about a connection, like whether the connection is established or not, the connection must be committed. When the <code>ct</code> action is executed on a packet with the <code>commit</code> parameter, the connection will become committed and will remain in this state until the end of the connection. Committed connections store state beyond the duration of packet processing.</p>
<dd>The <i>flags</i> and <i>mask</i> are 32-bit numbers written in decimal or in hexadecimal prefixed by <code>0x</code>. Each 1-bit in <i>mask</i> requires that the corresponding bit in <i>flags</i> must match. Each 0-bit in <i>mask</i> causes the corresponding bit to be ignored.</p>
<dd>Alternatively, the flags can be specified by their symbolic names (listed below), each preceded by either <code>+</code> for a flag that must be set, or <code>&#8211;</code> for a flag that must be unset, without any other delimiters between the flags. Flags not mentioned are wildcarded. For example, <code>tcp,ct_state=+trk-new</code> matches TCP packets that have been run through the connection tracker and do not establish a new connection.</p>
<dd>The following flags describe the state of the tracking:</p>
<dl>
<dd>
<dl>
<dt><code>0x01: new</code></p>
<dd>This is the beginning of a new connection. This flag may only be present for uncommitted connections.</p>
<dt><code>0x02: est</code></p>
<dd>This is part of an already existing connection. This flag may only be present for committed connections.</p>
<dt><code>0x04: rel</code></p>
<dd>This is a connection that is related to an existing connection, for instance ICMP &quot;destination unreachable&quot; messages or FTP data connections. This flag may only be present for committed connections.</p>
<dt><code>0x08: rpl</code></p>
<dd>The flow is in the reply direction, meaning it did not initiate the connection. This flag may only be present for committed connections.</p>
<dt><code>0x10: inv</code></p>
<dd>The state is invalid, meaning that the connection tracker couldn&#8217;t identify the connection. This flag is a catch-all for any problems that the connection tracker may have, for example:</p>
<dl>
<dd>&#8211; L3/L4 protocol handler is not loaded/unavailable. With the Linux kernel datapath, this may mean that the &quot;nf_conntrack_ipv4&quot; or &quot;nf_conntrack_ipv6&quot; modules are not loaded. &#8211; L3/L4 protocol handler determines that the packet is malformed. &#8211; Packets are unexpected length for protocol.</dl>
<dt><code>0x20: trk</code></p>
<dd>This packet is tracked, meaning that it has previously traversed the connection tracker. If this flag is not set, then no other flags will be set. If this flag is set, then the packet is tracked and other flags may also be set.</dl>
<p> This field was introduced in Open vSwitch 2.5.</dl>
</dl>
<p> The following fields are associated with the connection tracker and will only be populated for tracked packets. The <code>ct</code> action will populate these fields, and allows modification of some of the below fields.</p>
<dl>
<dt><code>ct_zone=</code><i>zone</p>
<dd>Matches the given 16-bit connection zone</i> exactly. This represents the most recent connection tracking context that <code>ct</code> was executed in. Each zone is an independent connection tracking context, so if you wish to track the same packet in multiple contexts then you must use the <code>ct</code> action multiple times. Introduced in Open vSwitch 2.5.</p>
<dt><code>ct_mark=</code><i>value</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches the given 32-bit connection mark <i>value</i> either exactly or with optional <i>mask</i>. This represents metadata associated with the connection that the current packet is part of. Introduced in Open vSwitch 2.5.</p>
<dt><code>ct_label=</code><i>value</i>[<code>/</code><i>mask</i>]</p>
<dd>Matches the given 128-bit connection labels <i>value</i> either exactly or with optional <i>mask</i>. This represents metadata associated with the connection that the current packet is part of. Introduced in Open vSwitch 2.5.</dl>
<p> Defining IPv6 flows (those with <code>dl_type</code> equal to 0x86dd) requires support for NXM. The following shorthand notations are available for IPv6-related flows:</p>
<dl>
<dt><code>ipv6</code></p>
<dd>Same as <code>dl_type=0x86dd</code>.</p>
<dt><code>tcp6</code></p>
<dd>Same as <code>dl_type=0x86dd,nw_proto=6</code>.</p>
<dt><code>udp6</code></p>
<dd>Same as <code>dl_type=0x86dd,nw_proto=17</code>.</p>
<dt><code>sctp6</code></p>
<dd>Same as <code>dl_type=0x86dd,nw_proto=132</code>.</p>
<dt><code>icmp6</code></p>
<dd>Same as <code>dl_type=0x86dd,nw_proto=58</code>.</dl>
<p> Finally, field assignments to <code>duration</code>, <code>n_packets</code>, or <code>n_bytes</code> are ignored to allow output from the <code>dump-flows</code> command to be used as input for other commands that parse flows. The <code>add-flow</code>, <code>add-flows</code>, and <code>mod-flows</code> commands require an additional field, which must be the final field specified:</p>
<dl>
<dt><code>actions=</code>[<i>action</i>][<code>,</code><i>action</i>&#8230;]</p>
<dd>Specifies a comma-separated list of actions to take on a packet when the flow entry matches. If no <i>action</i> is specified, then packets matching the flow are dropped. The following forms of <i>action</i> are supported:</p>
<dl>
<dd>
<dl>
<dt><i>port</i></p>
<dd>
<dt><code>output:</code><i>port</i></p>
<dd>Outputs the packet to OpenFlow port number <i>port</i>. If <i>port</i> is the packet&#8217;s input port, the packet is not output.</p>
<dt><code>output:</code><i>src</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</p>
<dd>Outputs the packet to the OpenFlow port number read from </code><i>src</i>, which must be an NXM field as described above. For example, <code>output:NXM_NX_REG0[16..31]</code> outputs to the OpenFlow port number written in the upper half of register 0. If the port number is the packet&#8217;s input port, the packet is not output.</p>
<dd>This form of <code>output</code> was added in Open vSwitch 1.3.0. This form of <code>output</code> uses an OpenFlow extension that is not supported by standard OpenFlow switches.</p>
<dt><code>group:</code><i>group_id</i></p>
<dd>Outputs the packet to the OpenFlow group <i>group_id</i>. Group tables are only supported in OpenFlow 1.1+. See Group Syntax for more details.</p>
<dt><code>normal</code></p>
<dd>Subjects the packet to the device&#8217;s normal L2/L3 processing. (This action is not implemented by all OpenFlow switches.)</p>
<dt><code>flood</code></p>
<dd>Outputs the packet on all switch physical ports other than the port on which it was received and any ports on which flooding is disabled (typically, these would be ports disabled by the IEEE 802.1D spanning tree protocol).</p>
<dt><code>all</code></p>
<dd>Outputs the packet on all switch physical ports other than the port on which it was received.</p>
<dt><code>local</code></p>
<dd>Outputs the packet on the &#8220;local port,&#8221; which corresponds to the network device that has the same name as the bridge.</p>
<dt><code>in_port</code></p>
<dd>Outputs the packet on the port from which it was received.</p>
<dt><code>controller(</code><i>key</i><code>=</code><i>value</i>&#8230;<code>)</p>
<dd>Sends the packet to the OpenFlow controller as a &#8220;packet in&#8221; message. The supported key-value pairs are:</p>
<dl>
<dd>
<dl>
<dt>max_len=</code><i>nbytes</i></p>
<dd>Limit to <i>nbytes</i> the number of bytes of the packet to send to the controller. By default the entire packet is sent.</p>
<dt><code>reason=</code><i>reason</i></p>
<dd>Specify <i>reason</i> as the reason for sending the message in the &#8220;packet in&#8221; message. The supported reasons are <code>action</code> (the default), <code>no_match</code>, and <code>invalid_ttl</code>.</p>
<dt><code>id=</code><i>controller-id</i></p>
<dd>Specify <i>controller-id</i>, a 16-bit integer, as the connection ID of the OpenFlow controller or controllers to which the &#8220;packet in&#8221; message should be sent. The default is zero. Zero is also the default connection ID for each controller connection, and a given controller connection will only have a nonzero connection ID if its controller uses the <code>NXT_SET_CONTROLLER_ID</code> Nicira extension to OpenFlow.</dl>
</dl>
<dd>Any <i>reason</i> other than <code>action</code> and any nonzero <i>controller-id</i> uses a Nicira vendor extension that, as of this writing, is only known to be implemented by Open vSwitch (version 1.6 or later).</p>
<dt><code>controller</code></p>
<dd>
<dt><code>controller</code>[<code>:</code><i>nbytes</i>]</p>
<dd>Shorthand for <code>controller()</code> or <code>controller(max_len=</code><i>nbytes</i><code>)</code>, respectively.</p>
<dt><code>enqueue(</code><i>port</i><code>,</code><i>queue</i><code>)</code></p>
<dd>Enqueues the packet on the specified <i>queue</i> within port <i>port</i>, which must be an OpenFlow port number or keyword (e.g. <code>LOCAL</code>). The number of supported queues depends on the switch; some OpenFlow implementations do not support queuing at all.</p>
<dt><code>drop</code></p>
<dd>Discards the packet, so no further processing or forwarding takes place. If a drop action is used, no other actions may be specified.</p>
<dt><code>mod_vlan_vid</code>:<i>vlan_vid</i></p>
<dd>Modifies the VLAN id on a packet. The VLAN tag is added or modified as necessary to match the value specified. If the VLAN tag is added, a priority of zero is used (see the <code>mod_vlan_pcp</code> action to set this).</p>
<dt><code>mod_vlan_pcp</code>:<i>vlan_pcp</i></p>
<dd>Modifies the VLAN priority on a packet. The VLAN tag is added or modified as necessary to match the value specified. Valid values are between 0 (lowest) and 7 (highest). If the VLAN tag is added, a vid of zero is used (see the <code>mod_vlan_vid</code> action to set this).</p>
<dt><code>strip_vlan</code></p>
<dd>Strips the VLAN tag from a packet if it is present.</p>
<dt><code>push_vlan</code>:<i>ethertype</i></p>
<dd>Push a new VLAN tag onto the packet. Ethertype is used as the Ethertype for the tag. Only ethertype 0x8100 should be used. (0x88a8 which the spec allows isn&#8217;t supported at the moment.) A priority of zero and the tag of zero are used for the new tag.</p>
<dt><code>push_mpls</code>:<i>ethertype</i></p>
<dd>Changes the packet&#8217;s Ethertype to <i>ethertype</i>, which must be either <code>0x8847</code> or <code>0x8848</code>, and pushes an MPLS LSE.</p>
<dd>If the packet does not already contain any MPLS labels then an initial label stack entry is pushed. The label stack entry&#8217;s label is 2 if the packet contains IPv6 and 0 otherwise, its default traffic control value is the low 3 bits of the packet&#8217;s DSCP value (0 if the packet is not IP), and its TTL is copied from the IP TTL (64 if the packet is not IP).</p>
<dd>If the packet does already contain an MPLS label, pushes a new outermost label as a copy of the existing outermost label.</p>
<dd>A limitation of the implementation is that processing of actions will stop if <code>push_mpls</code> follows another <code>push_mpls</code> unless there is a <code>pop_mpls</code> in between.</p>
<dt><code>pop_mpls</code>:<i>ethertype</i></p>
<dd>Strips the outermost MPLS label stack entry. Currently the implementation restricts <i>ethertype</i> to a non-MPLS Ethertype and thus <code>pop_mpls</code> should only be applied to packets with an MPLS label stack depth of one. A further limitation is that processing of actions will stop if <code>pop_mpls</code> follows another <code>pop_mpls</code> unless there is a <code>push_mpls</code> in between.</p>
<dt><code>mod_dl_src:</code><i>mac</i></p>
<dd>Sets the source Ethernet address to <i>mac</i>.</p>
<dt><code>mod_dl_dst:</code><i>mac</i></p>
<dd>Sets the destination Ethernet address to <i>mac</i>.</p>
<dt><code>mod_nw_src:</code><i>ip</i></p>
<dd>Sets the IPv4 source address to <i>ip</i>.</p>
<dt><code>mod_nw_dst:</code><i>ip</i></p>
<dd>Sets the IPv4 destination address to <i>ip</i>.</p>
<dt><code>mod_tp_src:</code><i>port</i></p>
<dd>Sets the TCP or UDP or SCTP source port to <i>port</i>.</p>
<dt><code>mod_tp_dst:</code><i>port</i></p>
<dd>Sets the TCP or UDP or SCTP destination port to <i>port</i>.</p>
<dt><code>mod_nw_tos:</code><i>tos</i></p>
<dd>Sets the DSCP bits in the IPv4 ToS/DSCP or IPv6 traffic class field to <i>tos</i>, which must be a multiple of 4 between 0 and 255. This action does not modify the two least significant bits of the ToS field (the ECN bits).</p>
<dt><code>mod_nw_ecn:</code><i>ecn</i></p>
<dd>Sets the ECN bits in the IPv4 ToS or IPv6 traffic class field to <i>ecn</i>, which must be a value between 0 and 3, inclusive. This action does not modify the six most significant bits of the field (the DSCP bits).</p>
<dd>Requires OpenFlow 1.1 or later.</p>
<dt><code>mod_nw_ttl:</code><i>ttl</i></p>
<dd>Sets the IPv4 TTL or IPv6 hop limit field to <i>ttl</i>, which is specified as a decimal number between 0 and 255, inclusive. Switch behavior when setting <i>ttl</i> to zero is not well specified, though.</p>
<dd>Requires OpenFlow 1.1 or later.</dl>
</dl>
<dd>The following actions are Nicira vendor extensions that, as of this writing, are only known to be implemented by Open vSwitch:</p>
<dl>
<dd>
<dl>
<dt><code>resubmit:</code><i>port</i></p>
<dd>
<dt><code>resubmit(</code>[<i>port</i>]<code>,</code>[<i>table</i>]<code>)</p>
<dd>Re-searches this OpenFlow flow table (or the table whose number is specified by </code><i>table</i>) with the <code>in_port</code> field replaced by <i>port</i> (if <i>port</i> is specified) and executes the actions found, if any, in addition to any other actions in this flow entry.</p>
<dd>Recursive <code>resubmit</code> actions are obeyed up to an implementation-defined maximum depth. Open vSwitch 1.0.1 and earlier did not support recursion; Open vSwitch before 1.2.90 did not support <i>table</i>.</p>
<dt><code>set_tunnel:</code><i>id</i></p>
<dd>
<dt><code>set_tunnel64:</code><i>id</i></p>
<dd>If outputting to a port that encapsulates the packet in a tunnel and supports an identifier (such as GRE), sets the identifier to <i>id</i>. If the <code>set_tunnel</code> form is used and <i>id</i> fits in 32 bits, then this uses an action extension that is supported by Open vSwitch 1.0 and later. Otherwise, if <i>id</i> is a 64-bit value, it requires Open vSwitch 1.1 or later.</p>
<dt><code>set_queue:</code><i>queue</i></p>
<dd>Sets the queue that should be used to <i>queue</i> when packets are output. The number of supported queues depends on the switch; some OpenFlow implementations do not support queuing at all.</p>
<dt><code>pop_queue</code></p>
<dd>Restores the queue to the value it was before any <code>set_queue</code> actions were applied.</p>
<dt><code>ct</code></p>
<dd>
<dt><code>ct(</code>[<i>argument</i>][<code>,</code><i>argument</i>&#8230;]<code>)</p>
<dd>Send the packet through the connection tracker. Refer to the ct_state</code> documentation above for possible packet and connection states. The following arguments are supported:</p>
<dl>
<dd>
<dl>
<dt><code>commit</code></p>
<dd>
<dl>
<dd>Commit the connection to the connection tracking module. Information about the connection will be stored beyond the lifetime of the packet in the pipeline. Some <code>ct_state</code> flags are only available for committed connections.</dl>
<dt><code>table=</code><i>number</i></p>
<dd>Fork pipeline processing in two. The original instance of the packet will continue processing the current actions list as an untracked packet. An additional instance of the packet will be sent to the connection tracker, which will be re-injected into the OpenFlow pipeline to resume processing in table <i>number</i>, with the <code>ct_state</code> and other ct match fields set. If the <code>table</code> is not specified, then the packet which is submitted to the connection tracker is not re-injected into the OpenFlow pipeline. It is strongly recommended to specify a table later than the current table to prevent loops.</p>
<dt><code>zone=</code><i>value</i></p>
<dd>
<dt><code>zone=</code><i>src</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code></p>
<dd>A 16-bit context id that can be used to isolate connections into separate domains, allowing overlapping network addresses in different zones. If a zone is not provided, then the default is to use zone zero. The <code>zone</code> may be specified either as an immediate 16-bit <i>value</i>, or may be provided from an NXM field <i>src</i>. The <i>start</i> and <i>end</i> pair are inclusive, and must specify a 16-bit range within the field. This value is copied to the <code>ct_zone</code> match field for packets which are re-injected into the pipeline using the <code>table</code> option.</p>
<dt><code>exec(</code>[<i>action</i>][<code>,</code><i>action</i>&#8230;]<code>)</code></p>
<dd>Perform actions within the context of connection tracking. This is a restricted set of actions which are in the same format as their specifications as part of a flow. Only actions which modify the <code>ct_mark</code> or <code>ct_label</code> fields are accepted within the <code>exec</code> action, and these fields may only be modified with this option. For example:</p>
<dl>
<dd>
<dl>
<dt><code>set_field:</code><i>value</i>-&gt;ct_mark</p>
<dd>Store a 32-bit metadata value with the connection. If the connection is committed, then subsequent lookups for packets in this connection will populate the <code>ct_mark</code> flow field when the packet is sent to the connection tracker with the <code>table</code> specified.</p>
<dt><code>set_field:</code><i>value</i>-&gt;ct_label</p>
<dd>Store a 128-bit metadata value with the connection. If the connection is committed, then subsequent lookups for packets in this connection will populate the <code>ct_label</code> flow field when the packet is sent to the connection tracker with the <code>table</code> specified.</dl>
</dl>
<dd>The <code>commit</code> parameter should be specified to use <code>exec(&#8230;)</code>.</p>
<dt><code>alg=</code><i>alg</i></p>
<dd>Specify application layer gateway <i>alg</i> to track specific connection types. Supported types include:</p>
<dl>
<dd>
<dl>
<dt><code>ftp</code></p>
<dd>Look for negotiation of FTP data connections. If a subsequent FTP data connection arrives which is related, the <code>ct</code> action will set the <code>rel</code> flag in the <code>ct_state</code> field for packets sent through <code>ct</code>.</dl>
</dl>
<dd>When committing related connections, the <code>ct_mark</code> for that connection is inherited from the current <code>ct_mark</code> stored with the original connection (ie, the connection created by <code>ct(alg=&#8230;)</code>).</dl>
</dl>
<dd>The <code>ct</code> action may be used as a primitive to construct stateful firewalls by selectively committing some traffic, then matching the <code>ct_state</code> to allow established connections while denying new connections. The following flows provide an example of how to implement a simple firewall that allows new connections from port 1 to port 2, and only allows established connections to send traffic from port 2 to port 1:<br />
&nbsp;<wbr><code>table=0,priority=1,action=drop<br />
&nbsp;<wbr>table=0,priority=10,arp,action=normal<br />
&nbsp;<wbr>table=0,priority=100,ip,ct_state=-trk,action=ct(table=1)<br />
&nbsp;<wbr>table=1,in_port=1,ip,ct_state=+trk+new,action=ct(commit),2<br />
&nbsp;<wbr>table=1,in_port=1,ip,ct_state=+trk+est,action=2<br />
&nbsp;<wbr>table=1,in_port=2,ip,ct_state=+trk+new,action=drop<br />
&nbsp;<wbr>table=1,in_port=2,ip,ct_state=+trk+est,action=1</code></p>
<dd>If <code>ct</code> is executed on IP (or IPv6) fragments, then the message is implicitly reassembled before sending to the connection tracker and refragmented upon <code>output</code>, to the original maximum received fragment size. Reassembly occurs within the context of the <code>zone</code>, meaning that IP fragments in different zones are not assembled together. Pipeline processing for the initial fragments is halted; When the final fragment is received, the message is assembled and pipeline processing will continue for that flow. Because packet ordering is not guaranteed by IP protocols, it is not possible to determine which IP fragment will cause message reassembly (and therefore continue pipeline processing). As such, it is strongly recommended that multiple flows should not execute <code>ct</code> to reassemble fragments from the same IP message.</p>
<dd>Currently, connection tracking is only available on Linux kernels with the nf_conntrack module loaded. The <code>ct</code> action was introduced in Open vSwitch 2.5.</p>
<dt><code>dec_ttl</code></p>
<dd>
<dt><code>dec_ttl(</code><i>id1</i>[<code>,</code><i>id2</i>]&#8230;<code>)</code></p>
<dd>Decrement TTL of IPv4 packet or hop limit of IPv6 packet. If the TTL or hop limit is initially zero or decrementing would make it so, no decrement occurs, as packets reaching TTL zero must be rejected. Instead, a &#8220;packet-in&#8221; message with reason code <code>OFPR_INVALID_TTL</code> is sent to each connected controller that has enabled receiving them, if any. Processing the current set of actions then stops. However, if the current set of actions was reached through &#8220;resubmit&#8221; then remaining actions in outer levels resume processing.</p>
<dd>This action also optionally supports the ability to specify a list of valid controller ids. Each of the controllers in the list will receive the &#8220;packet_in&#8221; message only if they have registered to receive the invalid ttl packets. If controller ids are not specified, the &#8220;packet_in&#8221; message will be sent only to the controllers having controller id zero which have registered for the invalid ttl packets.</p>
<dt><code>set_mpls_label</code>:<i>label</i></p>
<dd>Set the label of the outer MPLS label stack entry of a packet. <i>label</i> should be a 20-bit value that is decimal by default; use a <code>0x</code> prefix to specify them in hexadecimal.</p>
<dt><code>set_mpls_tc</code>:<i>tc</i></p>
<dd>Set the traffic-class of the outer MPLS label stack entry of a packet. <i>tc</i> should be a in the range 0 to 7 inclusive.</p>
<dt><code>set_mpls_ttl</code>:<i>ttl</i></p>
<dd>Set the TTL of the outer MPLS label stack entry of a packet. <i>ttl</i> should be in the range 0 to 255 inclusive.</p>
<dt><code>dec_mpls_ttl</code></p>
<dd>Decrement TTL of the outer MPLS label stack entry of a packet. If the TTL is initially zero or decrementing would make it so, no decrement occurs. Instead, a &#8220;packet-in&#8221; message with reason code <code>OFPR_INVALID_TTL</code> is sent to the main controller (id zero), if it has enabled receiving them. Processing the current set of actions then stops. However, if the current set of actions was reached through &#8220;resubmit&#8221; then remaining actions in outer levels resume processing.</p>
<dt><code>note:</code>[<i>hh</i>]&#8230;</p>
<dd>Does nothing at all. Any number of bytes represented as hex digits <i>hh</i> may be included. Pairs of hex digits may be separated by periods for readability. The <code>note</code> action&#8217;s format doesn&#8217;t include an exact length for its payload, so the provided bytes will be padded on the right by enough bytes with value 0 to make the total number 6 more than a multiple of 8.</p>
<dt><code>move:</code><i>src</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]-&gt;</code><i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code></p>
<dd>Copies the named bits from field <i>src</i> to field <i>dst</i>. <i>src</i> and <i>dst</i> must be NXM field names as defined in <code>nicira-ext.h</code>, e.g. <code>NXM_OF_UDP_SRC</code> or <code>NXM_NX_REG0</code>. Each <i>start</i> and <i>end</i> pair, which are inclusive, must specify the same number of bits and must fit within its respective field. Shorthands for <code>[</code><i>start</i><code>..</code><i>end</i><code>]</code> exist: use <code>[</code><i>bit</i><code>]</code> to specify a single bit or <code>[]</code> to specify an entire field.</p>
<dd>Examples: <code>move:NXM_NX_REG0[0..5]-&gt;NXM_NX_REG1[26..31]</code> copies the six bits numbered 0 through 5, inclusive, in register 0 into bits 26 through 31, inclusive; <code>move:NXM_NX_REG0[0..15]-&gt;NXM_OF_VLAN_TCI[]</code> copies the least significant 16 bits of register 0 into the VLAN TCI field.</p>
<dd>In OpenFlow 1.0 through 1.4, <code>move</code> ordinarily uses an Open vSwitch extension to OpenFlow. In OpenFlow 1.5, <code>move</code> uses the OpenFlow 1.5 standard <code>copy_field</code> action. The ONF has also made <code>copy_field</code> available as an extension to OpenFlow 1.3. Open vSwitch 2.4 and later understands this extension and uses it if a controller uses it, but for backward compatibility with older versions of Open vSwitch, <code>ovs-ofctl</code> does not use it.</p>
<dt><code>set_field:</code><i>value</i>[/<i>mask</i>]<code>-&gt;</code><i>dst</p>
<dd>
<dt></i><code>load:</code><i>value</i><code>-&gt;</code><i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</p>
<dd>Loads a literal value into a field or part of a field. With set_field</code>, <code>value</code> and the optional <code>mask</code> are given in the customary syntax for field <i>dst</i>, which is expressed as a field name. For example, <code>set_field:00:11:22:33:44:55-&gt;eth_src</code> sets the Ethernet source address to 00:11:22:33:44:55. With <code>load</code>, <i>value</i> must be an integer value (in decimal or prefixed by <code>0x</code> for hexadecimal) and <i>dst</i> is the NXM or OXM name for the field. For example, <code>load:0x001122334455-&gt;OXM_OF_ETH_DST[]</code> has the same effect as the prior <code>set_field</code> example.</p>
<dd>The two forms exist for historical reasons. Open vSwitch 1.1 introduced <code>NXAST_REG_LOAD</code> as a Nicira extension to OpenFlow 1.0 and used <code>load</code> to express it. Later, OpenFlow 1.2 introduced a standard <code>OFPAT_SET_FIELD</code> action that was restricted to loading entire fields, so Open vSwitch added the form <code>set_field</code> with this restriction. OpenFlow 1.5 extended <code>OFPAT_SET_FIELD</code> to the point that it became a superset of <code>NXAST_REG_LOAD</code>. Open vSwitch translates either syntax as necessary for the OpenFlow version in use: in OpenFlow 1.0 and 1.1, <code>NXAST_REG_LOAD</code>; in OpenFlow 1.2, 1.3, and 1.4, <code>NXAST_REG_LOAD</code> for <code>load</code> or for loading a subfield, <code>OFPAT_SET_FIELD</code> otherwise; and OpenFlow 1.5 and later, <code>OFPAT_SET_FIELD</code>.</p>
<dt><code>push:</code><i>src</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</p>
<dd>Pushes </code><i>start</i> to <i>end</i> bits inclusive, in fields on top of the stack.</p>
<dd>Example: <code>push:NXM_NX_REG2[0..5]</code> push the value stored in register 2 bits 0 through 5, inclusive, on to the internal stack.</p>
<dt><code>pop:</code><i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</p>
<dd>Pops from the top of the stack, retrieves the </code><i>start</i> to <i>end</i> bits inclusive, from the value popped and store them into the corresponding bits in <i>dst</i>.</p>
<dd>Example: <code>pop:NXM_NX_REG2[0..5]</code> pops the value from top of the stack. Set register 2 bits 0 through 5, inclusive, based on bits 0 through 5 from the value just popped.</p>
<dt><code>multipath(</code><i>fields</i><code>, </code><i>basis</i><code>, </code><i>algorithm</i><code>, </code><i>n_links</i><code>, </code><i>arg</i><code>, </code><i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>])</code></p>
<dd>Hashes <i>fields</i> using <i>basis</i> as a universal hash parameter, then the applies multipath link selection <i>algorithm</i> (with parameter <i>arg</i>) to choose one of <i>n_links</i> output links numbered 0 through <i>n_links</i> minus 1, and stores the link into <i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code>, which must be an NXM field as described above.</p>
<dd><i>fields</i> must be one of the following:</p>
<dl>
<dd>
<dl>
<dt><code>eth_src</code></p>
<dd>Hashes Ethernet source address only.</p>
<dt><code>symmetric_l4</code></p>
<dd>Hashes Ethernet source, destination, and type, VLAN ID, IPv4/IPv6 source, destination, and protocol, and TCP or SCTP (but not UDP) ports. The hash is computed so that pairs of corresponding flows in each direction hash to the same value, in environments where L2 paths are the same in each direction. UDP ports are not included in the hash to support protocols such as VXLAN that use asymmetric ports in each direction.</p>
<dt><code>symmetric_l3l4</code></p>
<dd>Hashes IPv4/IPv6 source, destination, and protocol, and TCP or SCTP (but not UDP) ports. Like <code>symmetric_l4</code>, this is a symmetric hash, but by excluding L2 headers it is more effective in environments with asymmetric L2 paths (e.g. paths involving VRRP IP addresses on a router). Not an effective hash function for protocols other than IPv4 and IPv6, which hash to a constant zero.</p>
<dt><code>symmetric_l3l4+udp</code></p>
<dd>Like <code>symmetric_l3l4+udp</code>, but UDP ports are included in the hash. This is a more effective hash when asymmetric UDP protocols such as VXLAN are not a consideration.</dl>
</dl>
<dd><i>algorithm</i> must be one of <code>modulo_n</code>, <code>hash_threshold</code>, <code>hrw</code>, and <code>iter_hash</code>. Only the <code>iter_hash</code> algorithm uses <i>arg</i>.</p>
<dd>Refer to <code>nicira-ext.h</code> for more details.</p>
<dt><code>bundle(</code><i>fields</i><code>, </code><i>basis</i><code>, </code><i>algorithm</i><code>, </code><i>slave_type</i><code>, slaves:[</code><i>s1</i><code>, </code><i>s2</i><code>, &#8230;])</code></p>
<dd>Hashes <i>fields</i> using <i>basis</i> as a universal hash parameter, then applies the bundle link selection <i>algorithm</i> to choose one of the listed slaves represented as <i>slave_type</i>. Currently the only supported <i>slave_type</i> is <code>ofport</code>. Thus, each <i>s1</i> through <i>sN</i> should be an OpenFlow port number. Outputs to the selected slave.</p>
<dd>Currently, <i>fields</i> must be either <code>eth_src</code>, <code>symmetric_l4</code>, <code>symmetric_l3l4</code>, or <code>symmetric_l3l4+udp</code>, and <i>algorithm</i> must be one of <code>hrw</code> and <code>active_backup</code>.</p>
<dd>Example: <code>bundle(eth_src,0,hrw,ofport,slaves:4,8)</code> uses an Ethernet source hash with basis 0, to select between OpenFlow ports 4 and 8 using the Highest Random Weight algorithm.</p>
<dd>Refer to <code>nicira-ext.h</code> for more details.</p>
<dt><code>bundle_load(</code><i>fields</i><code>, </code><i>basis</i><code>, </code><i>algorithm</i><code>, </code><i>slave_type</i><code>, </code><i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>], slaves:[</code><i>s1</i><code>, </code><i>s2</i><code>, &#8230;])</code></p>
<dd>Has the same behavior as the <code>bundle</code> action, with one exception. Instead of outputting to the selected slave, it writes its selection to <i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code>, which must be an NXM field as described above.</p>
<dd>Example: <code>bundle_load(eth_src, 0, hrw, ofport, NXM_NX_REG0[], slaves:4, 8)</code> uses an Ethernet source hash with basis 0, to select between OpenFlow ports 4 and 8 using the Highest Random Weight algorithm, and writes the selection to <code>NXM_NX_REG0[]</code>.</p>
<dd>Refer to <code>nicira-ext.h</code> for more details.</p>
<dt><code>learn(</code><i>argument</i>[<code>,</code><i>argument</i>]&#8230;<code>)</code></p>
<dd>This action adds or modifies a flow in an OpenFlow table, similar to <code>ovs-ofctl &#8211;strict mod-flows</code>. The arguments specify the flow&#8217;s match fields, actions, and other properties, as follows. At least one match criterion and one action argument should ordinarily be specified.</p>
<dl>
<dd>
<dl>
<dt><code>idle_timeout=</code><i>seconds</i></p>
<dd>
<dt><code>hard_timeout=</code><i>seconds</i></p>
<dd>
<dt><code>priority=</code><i>value</i></p>
<dd>
<dt><code>cookie=</code><i>value</i></p>
<dd>
<dt><code>send_flow_rem</code></p>
<dd>These arguments have the same meaning as in the usual <code>ovs-ofctl</code> flow syntax.</p>
<dt><code>fin_idle_timeout=</code><i>seconds</i></p>
<dd>
<dt><code>fin_hard_timeout=</code><i>seconds</i></p>
<dd>Adds a <code>fin_timeout</code> action with the specified arguments to the new flow. This feature was added in Open vSwitch 1.5.90.</p>
<dt><code>table=</code><i>number</i></p>
<dd>The table in which the new flow should be inserted. Specify a decimal number between 0 and 254. The default, if <code>table</code> is unspecified, is table 1.</p>
<dt><code>delete_learned</code></p>
<dd>This flag enables deletion of the learned flows when the flow with the <code>learn</code> action is removed. Specifically, when the last <code>learn</code> action with this flag and particular <code>table</code> and <code>cookie</code> values is removed, the switch deletes all of the flows in the specified table with the specified cookie.</p>
<dd>This flag was added in Open vSwitch 2.4.</p>
<dt><i>field</i><code>=</code><i>value</i></p>
<dd>
<dt><i>field</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]=</code><i>src</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code></p>
<dd>
<dt><i>field</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code></p>
<dd>Adds a match criterion to the new flow.</p>
<dd>The first form specifies that <i>field</i> must match the literal <i>value</i>, e.g. <code>dl_type=0x0800</code>. All of the fields and values for <code>ovs-ofctl</code> flow syntax are available with their usual meanings.</p>
<dd>The second form specifies that <i>field</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code> in the new flow must match <i>src</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code> taken from the flow currently being processed.</p>
<dd>The third form is a shorthand for the second form. It specifies that <i>field</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code> in the new flow must match <i>field</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code> taken from the flow currently being processed.</p>
<dt><code>load:</code><i>value</i><code>-&gt;</code><i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</p>
<dd>
<dt>load:</code><i>src</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]-&gt;</code><i>dst</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</p>
<dd>Adds a load</code> action to the new flow.</p>
<dd>The first form loads the literal <i>value</i> into bits <i>start</i> through <i>end</i>, inclusive, in field <i>dst</i>. Its syntax is the same as the <code>load</code> action described earlier in this section.</p>
<dd>The second form loads <i>src</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code>, a value from the flow currently being processed, into bits <i>start</i> through <i>end</i>, inclusive, in field <i>dst</i>.</p>
<dt><code>output:</code><i>field</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code></p>
<dd>Add an <code>output</code> action to the new flow&#8217;s actions, that outputs to the OpenFlow port taken from <i>field</i><code>[</code><i>start</i><code>..</code><i>end</i><code>]</code>, which must be an NXM field as described above.</dl>
</dl>
<dd>For best performance, segregate learned flows into a table (using <code>table=</code><i>number</i>) that is not used for any other flows except possibly for a lowest-priority &#8220;catch-all&#8221; flow, that is, a flow with no match criteria. (This is why the default <code>table</code> is 1, to keep the learned flows separate from the primary flow table 0.)</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>clear_actions</code></p>
<dd>Clears all the actions in the action set immediately.</p>
<dt><code>write_actions(</code>[<i>action</i>][<code>,</code><i>action</i>&#8230;]<code>)</p>
<dd>Add the specific actions to the action set. The syntax of </code><i>actions</i> is the same as in the <code>actions=</code> field. The action set is carried between flow tables and then executed at the end of the pipeline.</p>
<dd>The actions in the action set are applied in the following order, as required by the OpenFlow specification, regardless of the order in which they were added to the action set. Except as specified otherwise below, the action set only holds at most a single action of each type. When more than one action of a single type is written to the action set, the one written later replaces the earlier action:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd><code>strip_vlan</code> </p>
<dd><code>pop_mpls</code></p>
<dt>2.</p>
<dd><code>push_mpls</code></p>
<dt>3.</p>
<dd><code>push_vlan</code></p>
<dt>4.</p>
<dd><code>dec_ttl</code> </p>
<dd><code>dec_mpls_ttl</code></p>
<dt>5.</p>
<dd><code>load</code> </p>
<dd><code>move</code> </p>
<dd><code>mod_dl_dst</code> </p>
<dd><code>mod_dl_src</code> </p>
<dd><code>mod_nw_dst</code> </p>
<dd><code>mod_nw_src</code> </p>
<dd><code>mod_nw_tos</code> </p>
<dd><code>mod_nw_ecn</code> </p>
<dd><code>mod_nw_ttl</code> </p>
<dd><code>mod_tp_dst</code> </p>
<dd><code>mod_tp_src</code> </p>
<dd><code>mod_vlan_pcp</code> </p>
<dd><code>mod_vlan_vid</code> </p>
<dd><code>set_field</code> </p>
<dd><code>set_tunnel</code> </p>
<dd><code>set_tunnel64</code> </p>
<dd>The action set can contain any number of these actions, with cumulative effect. They will be applied in the order as added. That is, when multiple actions modify the same part of a field, the later modification takes effect, and when they modify different parts of a field (or different fields), then both modifications are applied.</p>
<dt>6.</p>
<dd><code>set_queue</code></p>
<dt>7.</p>
<dd><code>group</code> </p>
<dd><code>output</code> </p>
<dd><code>resubmit</code> </p>
<dd>If more than one of these actions is present, then the one listed earliest above is executed and the others are ignored, regardless of the order in which they were added to the action set. (If none of these actions is present, the action set has no real effect, because the modified packet is not sent anywhere and thus the modifications are not visible.)</dl>
</dl>
<dd>Only the actions listed above may be written to the action set.</p>
<dt><code>write_metadata:</code><i>value</i>[/<i>mask</i>]</p>
<dd>Updates the metadata field for the flow. If <i>mask</i> is omitted, the metadata field is set exactly to <i>value</i>; if <i>mask</i> is specified, then a 1-bit in <i>mask</i> indicates that the corresponding bit in the metadata field will be replaced with the corresponding bit from <i>value</i>. Both <i>value</i> and <i>mask</i> are 64-bit values that are decimal by default; use a <code>0x</code> prefix to specify them in hexadecimal.</p>
<dt><code>meter</code>:<i>meter_id</i></p>
<dd>Apply the <i>meter_id</i> before any other actions. If a meter band rate is exceeded, the packet may be dropped, or modified, depending on the meter band type. See the description of the <code>Meter Table Commands</code>, above, for more details.</p>
<dt><code>goto_table</code>:<i>table</i></p>
<dd>Indicates the next table in the process pipeline.</p>
<dt><code>fin_timeout(</code><i>argument</i>[<code>,</code><i>argument</i>]<code>)</p>
<dd>This action changes the idle timeout or hard timeout, or both, of this OpenFlow rule when the rule matches a TCP packet with the FIN or RST flag. When such a packet is observed, the action reduces the rule&#8217;s timeouts to those specified on the action. If the rule&#8217;s existing timeout is already shorter than the one that the action specifies, then that timeout is unaffected.</p>
<dd></code><i>argument</i> takes the following forms:</p>
<dl>
<dd>
<dl>
<dt><code>idle_timeout=</code><i>seconds</i></p>
<dd>Causes the flow to expire after the given number of seconds of inactivity.</p>
<dt><code>hard_timeout=</code><i>seconds</i></p>
<dd>Causes the flow to expire after the given number of seconds, regardless of activity. (<i>seconds</i> specifies time since the flow&#8217;s creation, not since the receipt of the FIN or RST.)</dl>
</dl>
<dd>This action was added in Open vSwitch 1.5.90.</p>
<dt><code>sample(</code><i>argument</i>[<code>,</code><i>argument</i>]&#8230;<code>)</code></p>
<dd>Samples packets and sends one sample for every sampled packet.</p>
<dd><i>argument</i> takes the following forms:</p>
<dl>
<dd>
<dl>
<dt><code>probability=</code><i>packets</i></p>
<dd>The number of sampled packets out of 65535. Must be greater or equal to 1.</p>
<dt><code>collector_set_id=</code><i>id</i></p>
<dd>The unsigned 32-bit integer identifier of the set of sample collectors to send sampled packets to. Defaults to 0.</p>
<dt><code>obs_domain_id=</code><i>id</i></p>
<dd>When sending samples to IPFIX collectors, the unsigned 32-bit integer Observation Domain ID sent in every IPFIX flow record. Defaults to 0.</p>
<dt><code>obs_point_id=</code><i>id</i></p>
<dd>When sending samples to IPFIX collectors, the unsigned 32-bit integer Observation Point ID sent in every IPFIX flow record. Defaults to 0.</dl>
</dl>
<dd>Refer to <code><a href="/docs/linux/man/8-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(8) for more details on configuring sample collector sets.</p>
<dd>This action was added in Open vSwitch 1.10.90.</p>
<dt><code>exit</code></p>
<dd>This action causes Open vSwitch to immediately halt execution of further actions. Those actions which have already been executed are unaffected. Any further actions, including those which may be in other tables, or different levels of the <code>resubmit</code> call stack, are ignored. Actions in the action set is still executed (specify <code>clear_actions</code> before <code>exit</code> to discard them).</p>
<dt><code>conjunction(</code><i>id</i><code>, </code><i>k</i><code>/</code><i>n</i><code>)</code></p>
<dd>An individual OpenFlow flow can match only a single value for each field. However, situations often arise where one wants to match one of a set of values within a field or fields. For matching a single field against a set, it is straightforward and efficient to add multiple flows to the flow table, one for each value in the set. For example, one might use the following flows to send packets with IP source address <i>a</i>, <i>b</i>, <i>c</i>, or <i>d</i> to the OpenFlow controller:</p>
<dl>
<dd><code>ip,ip_src=</code><i>a</i><code> actions=controller</code><br />
 <code>ip,ip_src=</code><i>b</i><code> actions=controller</code><br />
 <code>ip,ip_src=</code><i>c</i><code> actions=controller</code><br />
 <code>ip,ip_src=</code><i>d</i><code> actions=controller</code>
</dl>
<dd>Similarly, these flows send packets with IP destination address <i>e</i>, <i>f</i>, <i>g</i>, or <i>h</i> to the OpenFlow controller:</p>
<dl>
<dd><code>ip,ip_dst=</code><i>e</i><code> actions=controller</code><br />
 <code>ip,ip_dst=</code><i>f</i><code> actions=controller</code><br />
 <code>ip,ip_dst=</code><i>g</i><code> actions=controller</code><br />
 <code>ip,ip_dst=</code><i>h</i><code> actions=controller</code>
</dl>
<dd>Installing all of the above flows in a single flow table yields a disjunctive effect: a packet is sent to the controller if <code>ip_src</code> mo {<i>a</i>,<i>b</i>,<i>c</i>,<i>d</i>} or <code>ip_dst</code> mo {<i>e</i>,<i>f</i>,<i>g</i>,<i>h</i>} (or both). (Pedantically, if both of the above sets of flows are present in the flow table, they should have different priorities, because OpenFlow says that the results are undefined when two flows with same priority can both match a single packet.)</p>
<dd>Suppose, on the other hand, one wishes to match conjunctively, that is, to send a packet to the controller only if both <code>ip_src</code> mo {<i>a</i>,<i>b</i>,<i>c</i>,<i>d</i>} and <code>ip_dst</code> mo {<i>e</i>,<i>f</i>,<i>g</i>,<i>h</i>}. This requires 4 &#215; 4 = 16 flows, one for each possible pairing of <code>ip_src</code> and <code>ip_dst</code>. That is acceptable for our small example, but it does not gracefully extend to larger sets or greater numbers of dimensions.</p>
<dd>The <code>conjunction</code> action is a solution for conjunctive matches that is built into Open vSwitch. A <code>conjunction</code> action ties groups of individual OpenFlow flows into higher-level &#8220;conjunctive flows&#8221;. Each group corresponds to one dimension, and each flow within the group matches one possible value for the dimension. A packet that matches one flow from each group matches the conjunctive flow.</p>
<dd>To implement a conjunctive flow with <code>conjunction</code>, assign the conjunctive flow a 32-bit <i>id</i>, which must be unique within an OpenFlow table. Assign each of the <i>n</i> &ge; 2 dimensions a unique number from 1 to <i>n</i>; the ordering is unimportant. Add one flow to the OpenFlow flow table for each possible value of each dimension with <code>conjunction(</code><i>id, k</i><code>/</code><i>n</i><code>)</code> as the flow&#8217;s actions, where <i>k</i> is the number assigned to the flow&#8217;s dimension. Together, these flows specify the conjunctive flow&#8217;s match condition. When the conjunctive match condition is met, Open vSwitch looks up one more flow that specifies the conjunctive flow&#8217;s actions and receives its statistics. This flow is found by setting <code>conj_id</code> to the specified <i>id</i> and then again searching the flow table.</p>
<dd>The following flows provide an example. Whenever the IP source is one of the values in the flows that match on the IP source (dimension 1 of 2), <i>and</i> the IP destination is one of the values in the flows that match on IP destination (dimension 2 of 2), Open vSwitch searches for a flow that matches <code>conj_id</code> against the conjunction ID (1234), finding the first flow listed below.</p>
<dl>
<dd><code>conj_id=1234 actions=controller</code><br />
 <code>ip,ip_src=10.0.0.1 actions=conjunction(1234, 1/2)</code><br />
 <code>ip,ip_src=10.0.0.4 actions=conjunction(1234, 1/2)</code><br />
 <code>ip,ip_src=10.0.0.6 actions=conjunction(1234, 1/2)</code><br />
 <code>ip,ip_src=10.0.0.7 actions=conjunction(1234, 1/2)</code><br />
 <code>ip,ip_dst=10.0.0.2 actions=conjunction(1234, 2/2)</code><br />
 <code>ip,ip_dst=10.0.0.5 actions=conjunction(1234, 2/2)</code><br />
 <code>ip,ip_dst=10.0.0.7 actions=conjunction(1234, 2/2)</code><br />
 <code>ip,ip_dst=10.0.0.8 actions=conjunction(1234, 2/2)</code></dl>
<dd>Many subtleties exist:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>In the example above, every flow in a single dimension has the same form, that is, dimension 1 matches on <code>ip_src</code>, dimension 2 on <code>ip_dst</code>, but this is not a requirement. Different flows within a dimension may match on different bits within a field (e.g. IP network prefixes of different lengths, or TCP/UDP port ranges as bitwise matches), or even on entirely different fields (e.g. to match packets for TCP source port 80 or TCP destination port 80).</p>
<dt>&bull;</p>
<dd>The flows within a dimension can vary their matches across more than one field, e.g. to match only specific pairs of IP source and destination addresses or L4 port numbers.</p>
<dt>&bull;</p>
<dd>A flow may have multiple <code>conjunction</code> actions, with different <i>id</i> values. This is useful for multiple conjunctive flows with overlapping sets. If one conjunctive flow matches packets with both <code>ip_src</code> mo {<i>a</i>,<i>b</i>} and <code>ip_dst</code> mo {<i>d</i>,<i>e</i>} and a second conjunctive flow matches <code>ip_src</code> mo {<i>b</i>,<i>c</i>} and <code>ip_dst</code> mo {<i>f</i>,<i>g</i>}, for example, then the flow that matches <code>ip_src=</code><i>b</i> would have two <code>conjunction</code> actions, one for each conjunctive flow. The order of <code>conjunction</code> actions within a list of actions is not significant.</p>
<dt>&bull;</p>
<dd>A flow with <code>conjunction</code> actions may also include <code>note</code> actions for annotations, but not any other kind of actions. (They would not be useful because they would never be executed.)</p>
<dt>&bull;</p>
<dd>All of the flows that constitute a conjunctive flow with a given <i>id</i> must have the same priority. (Flows with the same <i>id</i> but different priorities are currently treated as different conjunctive flows, that is, currently <i>id</i> values need only be unique within an OpenFlow table at a given priority. This behavior isn&#8217;t guaranteed to stay the same in later releases, so please use <i>id</i> values unique within an OpenFlow table.)</p>
<dt>&bull;</p>
<dd>Conjunctive flows must not overlap with each other, at a given priority, that is, any given packet must be able to match at most one conjunctive flow at a given priority. Overlapping conjunctive flows yield unpredictable results.</p>
<dt>&bull;</p>
<dd>Following a conjunctive flow match, the search for the flow with <code>conj_id=</code><i>id</i> is done in the same general-purpose way as other flow table searches, so one can use flows with <code>conj_id=</code><i>id</i> to act differently depending on circumstances. (One exception is that the search for the <code>conj_id=</code><i>id</i> flow itself ignores conjunctive flows, to avoid recursion.) If the search with <code>conj_id=</code><i>id</i> fails, Open vSwitch acts as if the conjunctive flow had not matched at all, and continues searching the flow table for other matching flows.</p>
<dt>&bull;</p>
<dd>OpenFlow prerequisite checking occurs for the flow with <code>conj_id=</code><i>id</i> in the same way as any other flow, e.g. in an OpenFlow 1.1+ context, putting a <code>mod_nw_src</code> action into the example above would require adding an <code>ip</code> match, like this:</p>
<dl>
<dd><code>conj_id=1234,ip actions=mod_nw_src:1.2.3.4,controller</code>
</dl>
<dt>&bull;</p>
<dd>OpenFlow prerequisite checking also occurs for the individual flows that comprise a conjunctive match in the same way as any other flow.</p>
<dt>&bull;</p>
<dd>The flows that constitute a conjunctive flow do not have useful statistics. They are never updated with byte or packet counts, and so on. (For such a flow, therefore, the idle and hard timeouts work much the same way.)</p>
<dt>&bull;</p>
<dd>Conjunctive flows can be a useful building block for negation, that is, inequality matches like <code>tcp_src</code> &ne; 80. To implement an inequality match, convert it to a pair of range matches, e.g. 0 &le; <code>tcp_src&nbsp;<wbr>&lt; 80 and 80 &lt; tcp_src</code> &le; 65535, then convert each of the range matches into a collection of bitwise matches as explained above in the description of <code>tcp_src</code>.</p>
<dt>&bull;</p>
<dd>Sometimes there is a choice of which flows include a particular match. For example, suppose that we added an extra constraint to our example, to match on <code>ip_src</code> mo {<i>a</i>,<i>b</i>,<i>c</i>,<i>d</i>} and <code>ip_dst</code> mo {<i>e</i>,<i>f</i>,<i>g</i>,<i>h</i>} and <code>tcp_dst</code> = <i>i</i>. One way to implement this is to add the new constraint to the <code>conj_id</code> flow, like this:</p>
<dl>
<dd><code>conj_id=1234,tcp,tcp_dst=</code><i>i</i><code> actions=mod_nw_src:1.2.3.4,controller</code>
</dl>
<dd><i>but this is not recommended</i> because of the cost of the extra flow table lookup. Instead, add the constraint to the individual flows, either in one of the dimensions or (slightly better) all of them.</p>
<dt>&bull;</p>
<dd>A conjunctive match must have <i>n</i> &ge; 2 dimensions (otherwise a conjunctive match is not necessary). Open vSwitch enforces this.</p>
<dt>&bull;</p>
<dd>Each dimension within a conjunctive match should ordinarily have more than one flow. Open vSwitch does not enforce this.</dl>
</dl>
<dd>The <code>conjunction</code> action and <code>conj_id</code> field were introduced in Open vSwitch 2.4.</dl>
</dl>
</dl>
<p> An opaque identifier called a cookie can be used as a handle to identify a set of flows:</p>
<dl>
<dt><code>cookie=</code><i>value</i></p>
<dd>A cookie can be associated with a flow using the <code>add-flow</code>, <code>add-flows</code>, and <code>mod-flows</code> commands. <i>value</i> can be any 64-bit number and need not be unique among flows. If this field is omitted, a default cookie value of 0 is used.</p>
<dt><code>cookie=</code><i>value</i><code>/</code><i>mask</i></p>
<dd>When using NXM, the cookie can be used as a handle for querying, modifying, and deleting flows. <i>value</i> and <i>mask</i> may be supplied for the <code>del-flows</code>, <code>mod-flows</code>, <code>dump-flows</code>, and <code>dump-aggregate</code> commands to limit matching cookies. A 1-bit in <i>mask</i> indicates that the corresponding bit in <i>cookie</i> must match exactly, and a 0-bit wildcards that bit. A mask of -1 may be used to exactly match a cookie.</p>
<dd>The <code>mod-flows</code> command can update the cookies of flows that match a cookie by specifying the <i>cookie</i> field twice (once with a mask for matching and once without to indicate the new value):</p>
<dl>
<dd>
<dl>
<dt><code>ovs-ofctl mod-flows br0 cookie=1,actions=normal</code></p>
<dd>Change all flows&#8217; cookies to 1 and change their actions to <code>normal</code>.</p>
<dt><code>ovs-ofctl mod-flows br0 cookie=1/-1,cookie=2,actions=normal</code></p>
<dd>Update cookies with a value of 1 to 2 and change their actions to <code>normal</code>.</dl>
</dl>
<dd>The ability to match on cookies was added in Open vSwitch 1.5.0.</dl>
<p> The following additional field sets the priority for flows added by the <code>add-flow</code> and <code>add-flows</code> commands. For <code>mod-flows</code> and <code>del-flows</code> when <code>&#8211;strict</code> is specified, priority must match along with the rest of the flow specification. For <code>mod-flows</code> without <code>&#8211;strict</code>, priority is only significant if the command creates a new flow, that is, non-strict <code>mod-flows</code> does not match on priority and will not change the priority of existing flows. Other commands do not allow priority to be specified.</p>
<dl>
<dt><code>priority=</code><i>value</i></p>
<dd>The priority at which a wildcarded entry will match in comparison to others. <i>value</i> is a number between 0 and 65535, inclusive. A higher <i>value</i> will match before a lower one. An exact-match entry will always have priority over an entry containing wildcards, so it has an implicit priority value of 65535. When adding a flow, if the field is not specified, the flow&#8217;s priority will default to 32768.</p>
<dd>OpenFlow leaves behavior undefined when two or more flows with the same priority can match a single packet. Some users expect &#8220;sensible&#8221; behavior, such as more specific flows taking precedence over less specific flows, but OpenFlow does not specify this and Open vSwitch does not implement it. Users should therefore take care to use priorities to ensure the behavior that they expect.</dl>
<p> The <code>add-flow</code>, <code>add-flows</code>, and <code>mod-flows</code> commands support the following additional options. These options affect only new flows. Thus, for <code>add-flow</code> and <code>add-flows</code>, these options are always significant, but for <code>mod-flows</code> they are significant only if the command creates a new flow, that is, their values do not update or affect existing flows.</p>
<dl>
<dt><code>idle_timeout=</code><i>seconds</i></p>
<dd>Causes the flow to expire after the given number of seconds of inactivity. A value of 0 (the default) prevents a flow from expiring due to inactivity.</p>
<dt><code>hard_timeout=</code><i>seconds</i></p>
<dd>Causes the flow to expire after the given number of seconds, regardless of activity. A value of 0 (the default) gives the flow no hard expiration deadline.</p>
<dt><code>importance=</code><i>value</i></p>
<dd>Sets the importance of a flow. The flow entry eviction mechanism can use importance as a factor in deciding which flow to evict. A value of 0 (the default) makes the flow non-evictable on the basis of importance. Specify a value between 0 and 65535.</p>
<dd>Only OpenFlow 1.4 and later support <code>importance</code>.</p>
<dt><code>send_flow_rem</code></p>
<dd>Marks the flow with a flag that causes the switch to generate a &#8220;flow removed&#8221; message and send it to interested controllers when the flow later expires or is removed.</p>
<dt><code>check_overlap</code></p>
<dd>Forces the switch to check that the flow match does not overlap that of any different flow with the same priority in the same table. (This check is expensive so it is best to avoid it.)</dl>
<p> The <code>dump-flows</code>, <code>dump-aggregate</code>, <code>del-flow</code> and <code>del-flows</code> commands support these additional optional fields:</p>
<dl>
<dt><code>out_port=</code><i>port</i></p>
<dd>If set, a matching flow must include an output action to <i>port</i>, which must be an OpenFlow port number or name (e.g. <code>local</code>).</p>
<dt><code>out_group=</code><i>port</i></p>
<dd>If set, a matching flow must include an <code>group</code> action naming <i>group</i>, which must be an OpenFlow group number. This field is supported in Open vSwitch 2.5 and later and requires OpenFlow 1.1 or later.</dl>
<h3>Table Entry Output</h3>
<p>The <code>dump-tables</code> and <code>dump-aggregate</code> commands print information about the entries in a datapath&#8217;s tables. Each line of output is a flow entry as described in <code>Flow Syntax</code>, above, plus some additional fields:</p>
<dl>
<dt><code>duration=</code><i>secs</i></p>
<dd>The time, in seconds, that the entry has been in the table. <i>secs</i> includes as much precision as the switch provides, possibly to nanosecond resolution.</p>
<dt><code>n_packets</code></p>
<dd>The number of packets that have matched the entry.</p>
<dt><code>n_bytes</code></p>
<dd>The total number of bytes from packets that have matched the entry.</dl>
<p> The following additional fields are included only if the switch is Open vSwitch 1.6 or later and the NXM flow format is used to dump the flow (see the description of the <code>&#8211;flow-format</code> option below). The values of these additional fields are approximations only and in particular <code>idle_age</code> will sometimes become nonzero even for busy flows.</p>
<dl>
<dt><code>hard_age=</code><i>secs</i></p>
<dd>The integer number of seconds since the flow was added or modified. <code>hard_age</code> is displayed only if it differs from the integer part of <code>duration</code>. (This is separate from <code>duration</code> because <code>mod-flows</code> restarts the <code>hard_timeout</code> timer without zeroing <code>duration</code>.)</p>
<dt><code>idle_age=</code><i>secs</i></p>
<dd>The integer number of seconds that have passed without any packets passing through the flow.</dl>
<h3>Group Syntax</h3>
<p>Some <code>ovs-ofctl</code> commands accept an argument that describes a group or groups. Such flow descriptions comprise a series <i>field</i><code>=</code><i>value</i> assignments, separated by commas or white space. (Embedding spaces into a group description normally requires quoting to prevent the shell from breaking the description into multiple arguments.). Unless noted otherwise only the last instance of each field is honoured.</p>
<dl>
<dt><code>group_id=</code><i>id</i></p>
<dd>The integer group id of group. When this field is specified in <code>del-groups</code> or <code>dump-groups</code>, the keyword &quot;all&quot; may be used to designate all groups. This field is required.</p>
<dt><code>type=</code><i>type</i></p>
<dd>The type of the group. The <code>add-group</code>, <code>add-groups</code> and <code>mod-groups</code> commands require this field. It is prohibited for other commands. The following keywords designated the allowed types:</p>
<dl>
<dd>
<dl>
<dt><code>all</code></p>
<dd>Execute all buckets in the group.</p>
<dt><code>select</code></p>
<dd>Execute one bucket in the group. The switch should select the bucket in such a way that should implement equal load sharing is achieved. The switch may optionally select the bucket based on bucket weights.</p>
<dt><code>indirect</code></p>
<dd>Executes the one bucket in the group.</p>
<dt><code>ff</code></p>
<dd>
<dt><code>fast_failover</code></p>
<dd>Executes the first live bucket in the group which is associated with a live port or group.</dl>
</dl>
<dt><code>command_bucket_id=</code><i>id</i></p>
<dd>The bucket to operate on. The <code>insert-buckets</code> and <code>remove-buckets</code> commands require this field. It is prohibited for other commands. <i>id</i> may be an integer or one of the following keywords:</p>
<dl>
<dd>
<dl>
<dt><code>all</code></p>
<dd>Operate on all buckets in the group. Only valid when used with the <code>remove-buckets</code> command in which case the effect is to remove all buckets from the group.</p>
<dt><code>first</code></p>
<dd>Operate on the first bucket present in the group. In the case of the <code>insert-buckets</code> command the effect is to insert new bucets just before the first bucket already present in the group; or to replace the buckets of the group if there are no buckets already present in the group. In the case of the <code>remove-buckets</code> command the effect is to remove the first bucket of the group; or do nothing if there are no buckets present in the group.</p>
<dt><code>last</code></p>
<dd>Operate on the last bucket present in the group. In the case of the <code>insert-buckets</code> command the effect is to insert new bucets just after the last bucket already present in the group; or to replace the buckets of the group if there are no buckets already present in the group. In the case of the <code>remove-buckets</code> command the effect is to remove the last bucket of the group; or do nothing if there are no buckets present in the group.</dl>
</dl>
<dd>If <i>id</i> is an integer then it should correspond to the <code>bucket_id</code> of a bucket present in the group. In case of the <code>insert-buckets</code> command the effect is to insert buckets just before the bucket in the group whose <code>bucket_id</code> is <i>id</i>. In case of the <code>iremove-buckets</code> command the effect is to remove the in the group whose <code>bucket_id</code> is <i>id</i>. It is an error if there is no bucket persent group in whose <code>bucket_id</code> is <i>id</i>.</p>
<dt><code>selection_method</code>=<i>method</i></p>
<dd>The selection method used to select a bucket for a select group. This is a string of 1 to 15 bytes in length known to lower layers. This field is optional for <code>add-group</code>, <code>add-groups</code> and <code>mod-group</code> commands on groups of type <code>select</code>. Prohibited otherwise. The default value is the empty string.</p>
<dd>Other than the empty string, <code>hash</code> is currently the only defined selection method.</p>
<dd>This option will use a Netronome OpenFlow extension which is only supported when using Open vSwitch 2.4 and later with OpenFlow 1.5 and later.</p>
<dt><code>selection_method_param</code>=<i>param</i></p>
<dd>64-bit integer parameter to the selection method selected by the <code>selection_method</code> field. The parameter&#8217;s use is defined by the lower-layer that implements the <code>selection_method</code>. It is optional if the <code>selection_method</code> field is specified as a non-empty string. Prohibited otherwise. The default value is zero.</p>
<dd>This option will use a Netronome OpenFlow extension which is only supported when using Open vSwitch 2.4 and later with OpenFlow 1.5 and later.</p>
<dt><code>fields</code>=<i>field</i></p>
<dd>
<dt><code>fields(</code><i>field</i>[<code>=</code><i>mask</i>]&#8230;<code>)</code></p>
<dd>The field parameters to selection method selected by the <code>selection_method</code> field. The syntax is described in <code>Flow Syntax</code> with the additional restrictions that if a value is provided it is treated as a wildcard mask and wildcard masks following a slash are prohibited. The pre-requisites of fields must be provided by any flows that output to the group. The use of the fields is defined by the lower-layer that implements the <code>selection_method</code>. They are optional if the <code>selection_method</code> field is specified as a non-empty string. Prohibited otherwise. The default is no fields.</p>
<dd>This option will use a Netronome OpenFlow extension which is only supported when using Open vSwitch 2.4 and later with OpenFlow 1.5 and later.</p>
<dt><code>bucket</code>=<i>bucket_parameters</i></p>
<dd>The <code>add-group</code>, <code>add-groups</code> and <code>mod-group</code> commands require at least one bucket field. Bucket fields must appear after all other fields. Multiple bucket fields to specify multiple buckets. The order in which buckets are specified corresponds to their order in the group. If the type of the group is &quot;indirect&quot; then only one group may be specified. <i>bucket_parameters</i> consists of a list of <i>field</i><code>=</code><i>value</i> assignments, separated by commas or white space followed by a comma-separated list of actions. The fields for <i>bucket_parameters</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>bucket_id=</code><i>id</i></p>
<dd>The 32-bit integer group id of the bucket. Values greater than 0xffffff00 are reserved. This field was added in Open vSwitch 2.4 to conform with the OpenFlow 1.5 specification. It is not supported when earlier versions of OpenFlow are used. Open vSwitch will automatically allocate bucket ids when they are not specified.</p>
<dt><code>actions=</code>[<i>action</i>][<code>,</code><i>action</i>&#8230;]</p>
<dd>The syntax of actions are identical to the <code>actions=</code> field described in <code>Flow Syntax</code> above. Specyfing <code>actions=</code> is optional, any unknown bucket parameter will be interpreted as an action.</p>
<dt><code>weight=</code><i>value</i></p>
<dd>The relative weight of the bucket as an integer. This may be used by the switch during bucket select for groups whose <code>type</code> is <code>select</code>.</p>
<dt><code>watch_port=</code><i>port</i></p>
<dd>Port used to determine liveness of group. This or the <code>watch_group</code> field is required for groups whose <code>type</code> is <code>ff</code> or <code>fast_failover</code>.</p>
<dt><code>watch_group=</code><i>group_id</i></p>
<dd>Group identifier of group used to determine liveness of group. This or the <code>watch_port</code> field is required for groups whose <code>type</code> is <code>ff</code> or <code>fast_failover</code>.</dl>
</dl>
</dl>
<h3>Meter Syntax</h3>
<p>The meter table commands accept an argument that describes a meter. Such meter descriptions comprise a series <i>field</i><code>=</code><i>value</i> assignments, separated by commas or white space. (Embedding spaces into a group description normally requires quoting to prevent the shell from breaking the description into multiple arguments.). Unless noted otherwise only the last instance of each field is honoured.</p>
<dl>
<dt><code>meter=</code><i>id</i></p>
<dd>The integer meter id of the meter. When this field is specified in <code>del-meter</code>, <code>dump-meter</code>, or <code>meter-stats</code>, the keyword &quot;all&quot; may be used to designate all meters. This field is required, exept for <code>meter-stats</code>, which dumps all stats when this field is not specified.</p>
<dt><code>kbps</code></p>
<dd>
<dt><code>pktps</code></p>
<dd>The unit for the meter band rate parameters, either kilobits per second, or packets per second, respectively. One of these must be specified. The burst size unit corresponds to the rate unit by dropping the &quot;per second&quot;, i.e., burst is in units of kilobits or packets, respectively.</p>
<dt><code>burst</code></p>
<dd>Specify burst size for all bands, or none of them, if this flag is not given.</p>
<dt><code>stats</code></p>
<dd>Collect meter and band statistics.</p>
<dt><code>bands</code>=<i>band_parameters</i></p>
<dd>The <code>add-meter</code> and <code>mod-meter</code> commands require at least one band specification. Bands must appear after all other fields.</p>
<dl>
<dd>
<dl>
<dt><code>type=</code><i>type</i></p>
<dd>The type of the meter band. This keyword starts a new band specification. Each band specifies a rate above which the band is to take some action. The action depends on the band type. If multiple bands&#8217; rate is exceeded, then the band with the highest rate among the exceeded bands is selected. The following keywords designate the allowed meter band types:</p>
<dl>
<dd>
<dl>
<dt><code>drop</code></p>
<dd>Drop packets exceeding the band&#8217;s rate limit.</dl>
</dl>
<dt>The other <i>band_parameters</i> are:</p>
<dd>
<dt><code>rate=</code><i>value</i></p>
<dd>The relative rate limit for this band, in kilobits per second or packets per second, depending on the meter flags defined above.</p>
<dt><code>burst_size=</code><i>size</i></p>
<dd>The maximum burst allowed for the band. If <code>pktps</code> is specified, then <i>size</i> is a packet count, otherwise it is in kilobits. If unspecified, the switch is free to select some reasonable value depending on its configuration.</dl>
</dl>
</dl>
<h2>Options</h2>
<dl>
<dt><code>&#8211;strict</code></p>
<dd>Uses strict matching when running flow modification commands.</p>
<dt><code>&#8211;bundle</code></p>
<dd>Execute flow mods as an OpenFlow 1.4 atomic bundle transaction.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Within a bundle, all flow mods are processed in the order they appear and as a single atomic transaction, meaning that if one of them fails, the whole transaction fails and none of the changes are made to the <i>switch</i>&#8216;s flow table, and that each given datapath packet traversing the OpenFlow tables sees the flow tables either as before the transaction, or after all the flow mods in the bundle have been successfully applied.</p>
<dt>&bull;</p>
<dd>The beginning and the end of the flow table modification commands in a bundle are delimited with OpenFlow 1.4 bundle control messages, which makes it possible to stream the included commands without explicit OpenFlow barriers, which are otherwise used after each flow table modification command. This may make large modifications execute faster as a bundle.</p>
<dt>&bull;</p>
<dd>Bundles require OpenFlow 1.4 or higher. An explicit <code>-O OpenFlow14</code> option is not needed, but you may need to enable OpenFlow 1.4 support for OVS by setting the OVSDB <i>protocols</i> column in the <i>bridge</i> table.</dl>
</dl>
<dt><code>-O </code>[<i>version</i>[<code>,</code><i>version</i>]&#8230;]</p>
<dd>
<dt><code>&#8211;protocols=</code>[<i>version</i>[<code>,</code><i>version</i>]&#8230;]</p>
<dd>Sets the OpenFlow protocol versions that are allowed when establishing an OpenFlow session.</p>
<dd>The following versions are considered to be ready for general use. These protocol versions are enabled by default:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>OpenFlow10</code>, for OpenFlow 1.0.</dl>
</dl>
<dd>Support for the following protocol versions is provided for testing and development purposes. They are not enabled by default:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>OpenFlow11</code>, for OpenFlow 1.1.</p>
<dt>&bull;</p>
<dd><code>OpenFlow12</code>, for OpenFlow 1.2.</p>
<dt>&bull;</p>
<dd><code>OpenFlow13</code>, for OpenFlow 1.3.</dl>
</dl>
<dt><code>-F </code><i>format</i>[<code>,</code><i>format</i>&#8230;]</p>
<dd>
<dt><code>&#8211;flow-format=</code><i>format</i>[<code>,</code><i>format</i>&#8230;]</p>
<dd><code>ovs-ofctl</code> supports the following individual flow formats, any number of which may be listed as <i>format</i>:</p>
<dl>
<dd>
<dl>
<dt><code>OpenFlow10-table_id</code></p>
<dd>This is the standard OpenFlow 1.0 flow format. All OpenFlow switches and all versions of Open vSwitch support this flow format.</p>
<dt><code>OpenFlow10+table_id</code></p>
<dd>This is the standard OpenFlow 1.0 flow format plus a Nicira extension that allows <code>ovs-ofctl</code> to specify the flow table in which a particular flow should be placed. Open vSwitch 1.2 and later supports this flow format.</p>
<dt><code>NXM-table_id</code> (Nicira Extended Match)</p>
<dd>This Nicira extension to OpenFlow is flexible and extensible. It supports all of the Nicira flow extensions, such as <code>tun_id</code> and registers. Open vSwitch 1.1 and later supports this flow format.</p>
<dt><code>NXM+table_id</code> (Nicira Extended Match)</p>
<dd>This combines Nicira Extended match with the ability to place a flow in a specific table. Open vSwitch 1.2 and later supports this flow format.</p>
<dt><code>OXM-OpenFlow12</code></p>
<dd>
<dt><code>OXM-OpenFlow13</code></p>
<dd>
<dt><code>OXM-OpenFlow14</code></p>
<dd>These are the standard OXM (OpenFlow Extensible Match) flow format in OpenFlow 1.2, 1.3, and 1.4, respectively.</dl>
</dl>
<dd><code>ovs-ofctl</code> also supports the following abbreviations for collections of flow formats:</p>
<dl>
<dd>
<dl>
<dt><code>any</code></p>
<dd>Any supported flow format.</p>
<dt><code>OpenFlow10</code></p>
<dd><code>OpenFlow10-table_id</code> or <code>OpenFlow10+table_id</code>.</p>
<dt><code>NXM</code></p>
<dd><code>NXM-table_id</code> or <code>NXM+table_id</code>.</p>
<dt><code>OXM</code></p>
<dd><code>OXM-OpenFlow12</code>, <code>OXM-OpenFlow13</code>, or <code>OXM-OpenFlow14</code>.</dl>
</dl>
<dd>For commands that modify the flow table, <code>ovs-ofctl</code> by default negotiates the most widely supported flow format that supports the flows being added. For commands that query the flow table, <code>ovs-ofctl</code> by default uses the most advanced format supported by the switch.</p>
<dd>This option, where <i>format</i> is a comma-separated list of one or more of the formats listed above, limits <code>ovs-ofctl</code>&#8216;s choice of flow format. If a command cannot work as requested using one of the specified flow formats, <code>ovs-ofctl</code> will report a fatal error.</p>
<dt><code>-P </code><i>format</i></p>
<dd>
<dt><code>&#8211;packet-in-format=</code><i>format</i></p>
<dd><code>ovs-ofctl</code> supports the following packet_in formats, in order of increasing capability:</p>
<dl>
<dd>
<dl>
<dt><code>openflow10</code></p>
<dd>This is the standard OpenFlow 1.0 packet in format. It should be supported by all OpenFlow switches.</p>
<dt><code>nxm</code> (Nicira Extended Match)</p>
<dd>This packet_in format includes flow metadata encoded using the NXM format.</dl>
</dl>
<dd>Usually, <code>ovs-ofctl</code> prefers the <code>nxm</code> packet_in format, but will allow the switch to choose its default if <code>nxm</code> is unsupported. When <i>format</i> is one of the formats listed in the above table, <code>ovs-ofctl</code> will insist on the selected format. If the switch does not support the requested format, <code>ovs-ofctl</code> will report a fatal error. This option only affects the <code>monitor</code> command.</p>
<dt><code>&#8211;timestamp</code></p>
<dd>Print a timestamp before each received packet. This option only affects the <code>monitor</code>, <code>snoop</code>, and <code>ofp-parse-pcap</code> commands.</p>
<dt><code>-m</code></p>
<dd>
<dt><code>&#8211;more</code></p>
<dd>Increases the verbosity of OpenFlow messages printed and logged by <code>ovs-ofctl</code> commands. Specify this option more than once to increase verbosity further.</p>
<dt><code>&#8211;sort</code>[<code>=</code><i>field</i>]</p>
<dd>
<dt><code>&#8211;rsort</code>[<code>=</code><i>field</i>]</p>
<dd>Display output sorted by flow <i>field</i> in ascending (<code>&#8211;sort</code>) or descending (<code>&#8211;rsort</code>) order, where <i>field</i> is any of the fields that are allowed for matching or <code>priority</code> to sort by priority. When <i>field</i> is omitted, the output is sorted by priority. Specify these options multiple times to sort by multiple fields.</p>
<dd>Any given flow will not necessarily specify a value for a given field. This requires special treatement:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A flow that does not specify any part of a field that is used for sorting is sorted after all the flows that do specify the field. For example, <code>&#8211;sort=tcp_src</code> will sort all the flows that specify a TCP source port in ascending order, followed by the flows that do not specify a TCP source port at all.</p>
<dt>&bull;</p>
<dd>A flow that only specifies some bits in a field is sorted as if the wildcarded bits were zero. For example, <code>&#8211;sort=nw_src</code> would sort a flow that specifies <code>nw_src=192.168.0.0/24</code> the same as <code>nw_src=192.168.0.0</code>.</dl>
</dl>
<dd>These options currently affect only <code>dump-flows</code> output. The following options are valid on POSIX based platforms.</p>
<dt><code>&#8211;pidfile</code>[<code>=</code><i>pidfile</i>]</p>
<dd>Causes a file (by default, <code>ovs-ofctl.pid</code>) to be created indicating the PID of the running process. If the <i>pidfile</i> argument is not specified, or if it does not begin with <code>/</code>, then it is created in <code>/var/run/openvswitch</code>.</p>
<dd>If <code>&#8211;pidfile</code> is not specified, no pidfile is created.</p>
<dt><code>&#8211;overwrite-pidfile</code></p>
<dd>By default, when <code>&#8211;pidfile</code> is specified and the specified pidfile already exists and is locked by a running process, <code>ovs-ofctl</code> refuses to start. Specify <code>&#8211;overwrite-pidfile</code> to cause it to instead overwrite the pidfile.</p>
<dd>When <code>&#8211;pidfile</code> is not specified, this option has no effect.</p>
<dt><code>&#8211;detach</code></p>
<dd>Runs <code>ovs-ofctl</code> as a background process. The process forks, and in the child it starts a new session, closes the standard file descriptors (which has the side effect of disabling logging to the console), and changes its current directory to the root (unless <code>&#8211;no-chdir</code> is specified). After the child completes its initialization, the parent exits. <code>ovs-ofctl</code> detaches only when executing the <code>monitor</code> or <code>snoop</code> commands.</p>
<dt><code>&#8211;monitor</code></p>
<dd>Creates an additional process to monitor the <code>ovs-ofctl</code> daemon. If the daemon dies due to a signal that indicates a programming error (<code>SIGABRT</code>, <code>SIGALRM</code>, <code>SIGBUS</code>, <code>SIGFPE</code>, <code>SIGILL</code>, <code>SIGPIPE</code>, <code>SIGSEGV</code>, <code>SIGXCPU</code>, or <code>SIGXFSZ</code>) then the monitor process starts a new copy of it. If the daemon dies or exits for another reason, the monitor process exits.</p>
<dd>This option is normally used with <code>&#8211;detach</code>, but it also functions without it.</p>
<dt><code>&#8211;no-chdir</code></p>
<dd>By default, when <code>&#8211;detach</code> is specified, <code>ovs-ofctl</code> changes its current working directory to the root directory after it detaches. Otherwise, invoking <code>ovs-ofctl</code> from a carelessly chosen directory would prevent the administrator from unmounting the file system that holds that directory.</p>
<dd>Specifying <code>&#8211;no-chdir</code> suppresses this behavior, preventing <code>ovs-ofctl</code> from changing its current working directory. This may be useful for collecting core files, since it is common behavior to write core dumps into the current working directory and the root directory is not a good directory to use.</p>
<dd>This option has no effect when <code>&#8211;detach</code> is not specified.</p>
<dt><code>&#8211;user</code></p>
<dd>Causes <code>ovs-ofctl</code> to run as a different user specified in &quot;user:group&quot;, thus dropping most of the root privileges. Short forms &quot;user&quot; and &quot;:group&quot; are also allowed, with current user or group are assumed respectively. Only daemons started by the root user accepts this argument.</p>
<dd>On Linux, daemons will be granted CAP_IPC_LOCK and CAP_NET_BIND_SERVICES before dropping root privileges. Daemons interact with datapath, such as ovs-vswitchd, will be granted two additional capabilities, namely CAP_NET_ADMIN and CAP_NET_RAW. The capability change will apply even if new user is &quot;root&quot;.</p>
<dd>On Windows, this option is not currently supported. For security reasons, specifying this option will cause the daemon process not to start.</p>
<dt><code>&#8211;unixctl=</code><i>socket</i></p>
<dd>Sets the name of the control socket on which <code>ovs-ofctl</code> listens for runtime management commands (see <code>RUNTIME MANAGEMENT COMMANDS</code>, below). If <i>socket</i> does not begin with <code>/</code>, it is interpreted as relative to <code>/var/run/openvswitch</code>. If <code>&#8211;unixctl</code> is not used at all, the default socket is <code>/var/run/openvswitch/ovs-ofctl.</code><i>pid</i><code>.ctl</code>, where <i>pid</i> is <code>ovs-ofctl</code>&#8216;s process ID.</p>
<dd>On Windows, uses a kernel chosen TCP port on the localhost to listen for runtime management commands. The kernel chosen TCP port value is written in a file whose absolute path is pointed by <i>socket</i>. If <code>&#8211;unixctl</code> is not used at all, the file is created as <code>ovs-ofctl.ctl</code> in the configured <i>OVS_RUNDIR</i> directory.</p>
<dd>Specifying <code>none</code> for <i>socket</i> disables the control socket feature.</dl>
<h3>Public Key Infrastructure Options</h3>
<dl>
<dt><code>-p</code> <i>privkey.pem</i></p>
<dd>
<dt><code>&#8211;private-key=</code><i>privkey.pem</i></p>
<dd>Specifies a PEM file containing the private key used as <code>ovs-ofctl</code>&#8216;s identity for outgoing SSL connections.</p>
<dt><code>-c</code> <i>cert.pem</i></p>
<dd>
<dt><code>&#8211;certificate=</code><i>cert.pem</i></p>
<dd>Specifies a PEM file containing a certificate that certifies the private key specified on <code>-p</code> or <code>&#8211;private-key</code> to be trustworthy. The certificate must be signed by the certificate authority (CA) that the peer in SSL connections will use to verify it.</p>
<dt><code>-C</code> <i>cacert.pem</i></p>
<dd>
<dt><code>&#8211;ca-cert=</code><i>cacert.pem</i></p>
<dd>Specifies a PEM file containing the CA certificate that <code>ovs-ofctl</code> should use to verify certificates presented to it by SSL peers. (This may be the same certificate that SSL peers use to verify the certificate specified on <code>-c</code> or <code>&#8211;certificate</code>, or it may be a different one, depending on the PKI design in use.)</p>
<dt><code>-C none</code></p>
<dd>
<dt><code>&#8211;ca-cert=none</code></p>
<dd>Disables verification of certificates presented by SSL peers. This introduces a security risk, because it means that certificates cannot be verified to be those of known trusted hosts.</p>
<dt><code>-v</code>[<i>spec</i>]</p>
<dd>
<dt><code>&#8211;verbose=</code>[<i>spec</i>]</p>
<dd>Sets logging levels. Without any <i>spec</i>, sets the log level for every module and destination to <code>dbg</code>. Otherwise, <i>spec</i> is a list of words separated by spaces or commas or colons, up to one from each category below:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A valid module name, as displayed by the <code>vlog/list</code> command on <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), limits the log level change to the specified module.</p>
<dt>&bull;</p>
<dd><code>syslog</code>, <code>console</code>, or <code>file</code>, to limit the log level change to only to the system log, to the console, or to a file, respectively. (If <code>&#8211;detach</code> is specified, <code>ovs-ofctl</code> closes its standard file descriptors, so logging to the console will have no effect.)</p>
<dd>On Windows platform, <code>syslog</code> is accepted as a word and is only useful along with the <code>&#8211;syslog-target</code> option (the word has no effect otherwise).</p>
<dt>&bull;</p>
<dd><code>off</code>, <code>emer</code>, <code>err</code>, <code>warn</code>, <code>info</code>, or <code>dbg</code>, to control the log level. Messages of the given severity or higher will be logged, and messages of lower severity will be filtered out. <code>off</code> filters out all messages. See <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a definition of each log level.</dl>
</dl>
<dd>Case is not significant within <i>spec</i>.</p>
<dd>Regardless of the log levels set for <code>file</code>, logging to a file will not take place unless <code>&#8211;log-file</code> is also specified (see below).</p>
<dd>For compatibility with older versions of OVS, <code>any</code> is accepted as a word but has no effect.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd>Sets the maximum logging verbosity level, equivalent to <code>&#8211;verbose=dbg</code>.</p>
<dt><code>-vPATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>
<dt><code>&#8211;verbose=PATTERN:</code><i>destination</i><code>:</code><i>pattern</i></p>
<dd>Sets the log pattern for <i>destination</i> to <i>pattern</i>. Refer to <code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) for a description of the valid syntax for <i>pattern</i>.</p>
<dt><code>-vFACILITY:</code><i>facility</i></p>
<dd>
<dt><code>&#8211;verbose=FACILITY:</code><i>facility</i></p>
<dd>Sets the RFC5424 facility of the log message. <i>facility</i> can be one of <code>kern</code>, <code>user</code>, <code>mail</code>, <code>daemon</code>, <code>auth</code>, <code>syslog</code>, <code>lpr</code>, <code>news</code>, <code>uucp</code>, <code>clock</code>, <code>ftp</code>, <code>ntp</code>, <code>audit</code>, <code>alert</code>, <code>clock2</code>, <code>local0</code>, <code>local1</code>, <code>local2</code>, <code>local3</code>, <code>local4</code>, <code>local5</code>, <code>local6</code> or <code>local7</code>. If this option is not specified, <code>daemon</code> is used as the default for the local system syslog and <code>local0</code> is used while sending a message to the target provided via the <code>&#8211;syslog-target</code> option.</p>
<dt><code>&#8211;log-file</code>[<code>=</code><i>file</i>]</p>
<dd>Enables logging to a file. If <i>file</i> is specified, then it is used as the exact name for the log file. The default log file name used if <i>file</i> is omitted is <code>/var/log/openvswitch/ovs-ofctl.log</code>.</p>
<dt><code>&#8211;syslog-target=</code><i>host</i><code>:</code><i>port</i></p>
<dd>Send syslog messages to UDP <i>port</i> on <i>host</i>, in addition to the system syslog. The <i>host</i> must be a numerical IP address, not a hostname.</p>
<dt><code>&#8211;syslog-method=</code><i>method</i></p>
<dd>Specify <i>method</i> how syslog messages should be sent to syslog daemon. Following forms are supported:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>libc</code>, use libc <code>syslog()</code> function. This is the default behavior. Downside of using this options is that libc adds fixed prefix to every message before it is actually sent to the syslog daemon over <code>/dev/log</code> UNIX domain socket.</p>
<dt>&bull;</p>
<dd><code>unix:</code><i>file</i>, use UNIX domain socket directly. It is possible to specify arbitrary message format with this option. However, <code>rsyslogd 8.9</code> and older versions use hard coded parser function anyway that limits UNIX domain socket use. If you want to use arbitrary message format with older <code>rsyslogd</code> versions, then use UDP socket to localhost IP address instead.</p>
<dt>&bull;</p>
<dd><code>udp:</code><i>ip</i>:<i>port</i>, use UDP socket. With this method it is possible to use arbitrary message format also with older <code>rsyslogd</code>. When sending syslog messages over UDP socket extra precaution needs to be taken into account, for example, syslog daemon needs to be configured to listen on the specified UDP port, accidental iptables rules could be interfering with local syslog traffic and there are some security considerations that apply to UDP sockets, but do not apply to UNIX domain sockets.</dl>
</dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Prints a brief help message to the console.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Prints version information to the console.</dl>
<h2>Runtime Management Commands</h2>
<p><code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8) can send commands to a running <code>ovs-ofctl</code> process. The supported commands are listed below.</p>
<dl>
<dt><code>exit</code></p>
<dd>Causes <code>ovs-ofctl</code> to gracefully terminate. This command applies only when executing the <code>monitor</code> or <code>snoop</code> commands.</p>
<dt><code>ofctl/set-output-file </code><i>file</i></p>
<dd>Causes all subsequent output to go to <i>file</i> instead of stderr. This command applies only when executing the <code>monitor</code> or <code>snoop</code> commands.</p>
<dt><code>ofctl/send </code><i>ofmsg</i>&#8230;</p>
<dd>Sends each <i>ofmsg</i>, specified as a sequence of hex digits that express an OpenFlow message, on the OpenFlow connection. This command is useful only when executing the <code>monitor</code> command.</p>
<dt><code>ofctl/barrier</code></p>
<dd>Sends an OpenFlow barrier request on the OpenFlow connection and waits for a reply. This command is useful only for the <code>monitor</code> command.</dl>
<h2>Examples</h2>
<p>The following examples assume that <code>ovs-vswitchd</code> has a bridge named <code>br0</code> configured.</p>
<dl>
<dt><code>ovs-ofctl dump-tables br0</code></p>
<dd>Prints out the switch&#8217;s table stats. (This is more interesting after some traffic has passed through.)</p>
<dt><code>ovs-ofctl dump-flows br0</code></p>
<dd>Prints the flow entries in the switch.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ovs-appctl/">ovs-appctl</a></code>(8), <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8) <code><a href="/docs/linux/man/8-ovs-vswitchd-conf-db/">ovs-vswitchd.conf.db</a></code>(8) </p>
