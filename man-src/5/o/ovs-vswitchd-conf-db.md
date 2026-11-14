---
title: "ovs-vswitchd-conf-db(5)"
name: "ovs-vswitchd-conf-db"
section: "5"
letter: "o"
url: "/docs/linux/man/5-ovs-vswitchd-conf-db/"
description: "ovs-vswitchd46conf46db – Open_vSwitch database schema"
---

<p>ovs-vswitchd46conf46db &#8211; Open_vSwitch database schema </p>
<p> A database with this schema holds the configuration for one Open vSwitch daemon46 The top-level configuration for the daemon is the <code>Open_vSwitch</code> table, which must have exactly one record46 Records in other tables are significant only when they can be reached directly or indirectly from the <code>Open_vSwitch</code> table46 Records that are not reachable from the <code>Open_vSwitch</code> table are automatically deleted from the database, except for records in a few distinguished &#8220;root set&#8221; tables46</p>
<h3>Common Columns</h3>
<p>Most tables contain two special columns, named <code>other_config</code> and <code>external_ids</code>46 These columns have the same form and purpose each place that they appear, so we describe them here to save space later46</p>
<dl>
<dd>
<dl>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd>Key-value pairs for configuring rarely used features46 Supported keys, along with the forms taken by their values, are documented individually for each table46</p>
<dd>A few tables do not have <code>other_config</code> columns because no key-value pairs have yet been defined for them46</p>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd>Key-value pairs for use by external frameworks that integrate with Open vSwitch, rather than by Open vSwitch itself46 System integrators should either use the Open vSwitch development mailing list to coordinate on common key-value definitions, or choose key names that are likely to be unique46 In some cases, where key-value pairs have been defined that are likely to be widely useful, they are documented individually for each table46</dl>
</dl>
<h2>Table Summary</h2>
<p>The following list summarizes the purpose of each of the tables in the <code>Open_vSwitch</code> database. Each table is described in more detail on a later page.</p>
<dl>
<dt>Table</p>
<dd>Purpose </p>
<dt> <code>Open_vSwitch</code></p>
<dd>Open vSwitch configuration46 </p>
<dt> <code>Bridge</code></p>
<dd>Bridge configuration46 </p>
<dt> <code>Port</code></p>
<dd>Port configuration46 </p>
<dt> <code>Interface</code></p>
<dd>One physical network device in a Port46 </p>
<dt> <code>Flow_Table</code></p>
<dd>OpenFlow table configuration </p>
<dt> <code>QoS</code></p>
<dd>Quality of Service configuration </p>
<dt> <code>Queue</code></p>
<dd>QoS output queue46 </p>
<dt> <code>Mirror</code></p>
<dd>Port mirroring46 </p>
<dt> <code>Controller</code></p>
<dd>OpenFlow controller configuration46 </p>
<dt> <code>Manager</code></p>
<dd>OVSDB management connection46 </p>
<dt> <code>NetFlow</code></p>
<dd>NetFlow configuration46 </p>
<dt> <code>SSL</code></p>
<dd>SSL configuration46 </p>
<dt> <code>sFlow</code></p>
<dd>sFlow configuration46 </p>
<dt> <code>IPFIX</code></p>
<dd>IPFIX configuration46 </p>
<dt> <code>Flow_Sample_Collector_Set</code></p>
<dd>Flow_Sample_Collector_Set configuration46 </p>
<dt> <code>AutoAttach</code></p>
<dd>AutoAttach configuration46</dl>
<h2>Open_vSwitch TABLE</h2>
<p>Configuration for an Open vSwitch daemon46 There must be exactly one record in the <code>Open_vSwitch</code> table46</p>
<h3>Summary:</h3>
<dl>
<dt> <i>Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>bridges</code></p>
<dd>set of <code>Bridge</code>s </p>
<dt> <code>ssl</code></p>
<dd>optional <code>SSL</code> </p>
<dt> <code>external_ids : system-id</code></p>
<dd>optional string </p>
<dt> <code>external_ids : xs-system-uuid</code></p>
<dd>optional string </p>
<dt> <code>other_config : stats-update-interval</code></p>
<dd>optional string, containing an integer, at least 5,000 </p>
<dt> <code>other_config : flow-restore-wait</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : flow-limit</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>other_config : max-idle</code></p>
<dd>optional string, containing an integer, at least 500 </p>
<dt> <code>other_config : n-dpdk-rxqs</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : pmd-cpu-mask</code></p>
<dd>optional string </p>
<dt> <code>other_config : n-handler-threads</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : n-revalidator-threads</code></p>
<dd>optional string, containing an integer, at least 1</dl>
</dl>
<dt> <i>Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>next_cfg</code></p>
<dd>integer </p>
<dt> <code>cur_cfg</code></p>
<dd>integer </p>
<dt> <i>Statistics:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : enable-statistics</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>statistics : cpu</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>statistics : load_average</code></p>
<dd>optional string </p>
<dt> <code>statistics : memory</code></p>
<dd>optional string </p>
<dt> <code>statistics : process_NAME</code></p>
<dd>optional string </p>
<dt> <code>statistics : file_systems</code></p>
<dd>optional string</dl>
</dl>
</dl>
</dl>
<dt> <i>Version Reporting:</i></p>
<dl>
<dd>
<dl>
<dt> <code>ovs_version</code></p>
<dd>optional string </p>
<dt> <code>db_version</code></p>
<dd>optional string </p>
<dt> <code>system_type</code></p>
<dd>optional string </p>
<dt> <code>system_version</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>Capabilities:</i></p>
<dl>
<dd>
<dl>
<dt> <code>datapath_types</code></p>
<dd>set of strings </p>
<dt> <code>iface_types</code></p>
<dd>set of strings</dl>
</dl>
<dt> <i>Database Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>manager_options</code></p>
<dd>set of <code>Manager</code>s</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config</code></p>
<dd>map of string-string pairs </p>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<p><i>Configuration:</i></p>
<dl>
<dt><code>bridges</code>: set of <code>Bridge</code>s</p>
<dd>Set of bridges managed by the daemon46</p>
<dt><code>ssl</code>: optional <code>SSL</code></p>
<dd>SSL used globally by the daemon46</p>
<dt><code>external_ids : system-id</code>: optional string</p>
<dd>A unique identifier for the Open vSwitch&#8217;s physical host46 The form of the identifier depends on the type of the host46 On a Citrix XenServer, this will likely be the same as <code>external_ids:xs-system-uuid</code>46</p>
<dt><code>external_ids : xs-system-uuid</code>: optional string</p>
<dd>The Citrix XenServer universally unique identifier for the physical host as displayed by <code>xe host-list</code>46</p>
<dt><code>other_config : stats-update-interval</code>: optional string, containing an integer, at least 5,000</p>
<dd>Interval for updating statistics to the database, in milliseconds46 This option will affect the update of the <code>statistics</code> column in the following tables: <code>Port</code>, <code>Interface </code>, <code>Mirror</code>46</p>
<dd>Default value is 5000 ms46</p>
<dd>Getting statistics more frequently can be achieved via OpenFlow46</p>
<dt><code>other_config : flow-restore-wait</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>When <code>ovs-vswitchd</code> starts up, it has an empty flow table and therefore it handles all arriving packets in its default fashion according to its configuration, by dropping them or sending them to an OpenFlow controller or switching them as a standalone switch46 This behavior is ordinarily desirable46 However, if <code>ovs-vswitchd</code> is restarting as part of a &#8220;hot-upgrade,&#8221; then this leads to a relatively long period during which packets are mishandled46</p>
<dd>This option allows for improvement46 When <code>ovs-vswitchd</code> starts with this value set as <code>true</code>, it will neither flush or expire previously set datapath flows nor will it send and receive any packets to or from the datapath46 When this value is later set to <code>false</code>, <code>ovs-vswitchd</code> will start receiving packets from the datapath and re-setup the flows46</p>
<dd>Thus, with this option, the procedure for a hot-upgrade of <code>ovs-vswitchd</code> becomes roughly the following:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Stop <code>ovs-vswitchd</code>46</p>
<dt>2.</p>
<dd>Set <code>other_config:flow-restore-wait</code> to <code>true</code>46</p>
<dt>3.</p>
<dd>Start <code>ovs-vswitchd</code>46</p>
<dt>4.</p>
<dd>Use <code>ovs-ofctl</code> (or some other program, such as an OpenFlow controller) to restore the OpenFlow flow table to the desired state46</p>
<dt>5.</p>
<dd>Set <code>other_config:flow-restore-wait</code> to <code>false</code> (or remove it entirely from the database)46</dl>
</dl>
<dd>The <code>ovs-ctl</code>&#8216;s &#8220;restart&#8221; and &#8220;force-reload-kmod&#8221; functions use the above config option during hot upgrades46</p>
<dt><code>other_config : flow-limit</code>: optional string, containing an integer, at least 0</p>
<dd>The maximum number of flows allowed in the datapath flow table46 Internally OVS will choose a flow limit which will likely be lower than this number, based on real time network conditions46 Tweaking this value is discouraged unless you know exactly what you&#8217;re doing46</p>
<dd>The default is 20000046</p>
<dt><code>other_config : max-idle</code>: optional string, containing an integer, at least 500</p>
<dd>The maximum time (in ms) that idle flows will remain cached in the datapath46 Internally OVS will check the validity and activity for datapath flows regularly and may expire flows quicker than this number, based on real time network conditions46 Tweaking this value is discouraged unless you know exactly what you&#8217;re doing46</p>
<dd>The default is 1000046</p>
<dt><code>other_config : n-dpdk-rxqs</code>: optional string, containing an integer, at least 1</p>
<dd>Specifies the maximum number of rx queues to be created for each dpdk interface46 If not specified or specified to 0, one rx queue will be created for each dpdk interface by default46</p>
<dt><code>other_config : pmd-cpu-mask</code>: optional string</p>
<dd>Specifies CPU mask for setting the cpu affinity of PMD (Poll Mode Driver) threads46 Value should be in the form of hex string, similar to the dpdk EAL &#8216;-c COREMASK&#8217; option input or the &#8216;taskset&#8217; mask input46</p>
<dd>The lowest order bit corresponds to the first CPU core46 A set bit means the corresponding core is available and a pmd thread will be created and pinned to it46 If the input does not cover all cores, those uncovered cores are considered not set46</p>
<dd>If not specified, one pmd thread will be created for each numa node and pinned to any available core on the numa node by default46</p>
<dt><code>other_config : n-handler-threads</code>: optional string, containing an integer, at least 1</p>
<dd>Specifies the number of threads for software datapaths to use for handling new flows46 The default the number of online CPU cores minus the number of revalidators46</p>
<dd>This configuration is per datapath46 If you have more than one software datapath (e46g46 some <code>system</code> bridges and some <code>netdev</code> bridges), then the total number of threads is <code>n-handler-threads</code> times the number of software datapaths46</p>
<dt><code>other_config : n-revalidator-threads</code>: optional string, containing an integer, at least 1</p>
<dd>Specifies the number of threads for software datapaths to use for revalidating flows in the datapath46 Typically, there is a direct correlation between the number of revalidator threads, and the number of flows allowed in the datapath46 The default is the number of cpu cores divided by four plus one46 If <code>n-handler-threads</code> is set, the default changes to the number of cpu cores minus the number of handler threads46</p>
<dd>This configuration is per datapath46 If you have more than one software datapath (e46g46 some <code>system</code> bridges and some <code>netdev</code> bridges), then the total number of threads is <code>n-handler-threads</code> times the number of software datapaths46</dl>
<p> <i>Status:</i></p>
<dl>
<dt><code>next_cfg</code>: integer</p>
<dd>Sequence number for client to increment46 When a client modifies any part of the database configuration and wishes to wait for Open vSwitch to finish applying the changes, it may increment this sequence number46</p>
<dt><code>cur_cfg</code>: integer</p>
<dd>Sequence number that Open vSwitch sets to the current value of <code>next_cfg</code> after it finishes applying a set of configuration changes46</dl>
<p> <i>Statistics:</i> The <code>statistics</code> column contains key-value pairs that report statistics about a system running an Open vSwitch46 These are updated periodically (currently, every 5 seconds)46 Key-value pairs that cannot be determined or that do not apply to a platform are omitted46</p>
<dl>
<dt><code>other_config : enable-statistics</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Statistics are disabled by default to avoid overhead in the common case when statistics gathering is not useful46 Set this value to <code>true</code> to enable populating the <code>statistics</code> column or to <code>false</code> to explicitly disable it46</p>
<dt><code>statistics : cpu</code>: optional string, containing an integer, at least 1</p>
<dd>Number of CPU processors, threads, or cores currently online and available to the operating system on which Open vSwitch is running, as an integer46 This may be less than the number installed, if some are not online or if they are not available to the operating system46</p>
<dd>Open vSwitch userspace processes are not multithreaded, but the Linux kernel-based datapath is46</p>
<dt><code>statistics : load_average</code>: optional string</p>
<dd>A comma-separated list of three floating-point numbers, representing the system load average over the last 1, 5, and 15 minutes, respectively46</p>
<dt><code>statistics : memory</code>: optional string</p>
<dd>A comma-separated list of integers, each of which represents a quantity of memory in kilobytes that describes the operating system on which Open vSwitch is running46 In respective order, these values are:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Total amount of RAM allocated to the OS46</p>
<dt>2.</p>
<dd>RAM allocated to the OS that is in use46</p>
<dt>3.</p>
<dd>RAM that can be flushed out to disk or otherwise discarded if that space is needed for another purpose46 This number is necessarily less than or equal to the previous value46</p>
<dt>4.</p>
<dd>Total disk space allocated for swap46</p>
<dt>5.</p>
<dd>Swap space currently in use46</dl>
</dl>
<dd>On Linux, all five values can be determined and are included46 On other operating systems, only the first two values can be determined, so the list will only have two values46</p>
<dt><code>statistics : process_NAME</code>: optional string</p>
<dd>One such key-value pair, with <code>NAME</code> replaced by a process name, will exist for each running Open vSwitch daemon process, with <i>name</i> replaced by the daemon&#8217;s name (e46g46 <code>process_ovs-vswitchd</code>)46 The value is a comma-separated list of integers46 The integers represent the following, with memory measured in kilobytes and durations in milliseconds:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>The process&#8217;s virtual memory size46</p>
<dt>2.</p>
<dd>The process&#8217;s resident set size46</p>
<dt>3.</p>
<dd>The amount of user and system CPU time consumed by the process46</p>
<dt>4.</p>
<dd>The number of times that the process has crashed and been automatically restarted by the monitor46</p>
<dt>5.</p>
<dd>The duration since the process was started46</p>
<dt>6.</p>
<dd>The duration for which the process has been running46</dl>
</dl>
<dd>The interpretation of some of these values depends on whether the process was started with the <code>&#8211;monitor</code>46 If it was not, then the crash count will always be 0 and the two durations will always be the same46 If <code>&#8211;monitor</code> was given, then the crash count may be positive; if it is, the latter duration is the amount of time since the most recent crash and restart46</p>
<dd>There will be one key-value pair for each file in Open vSwitch&#8217;s &#8220;run directory&#8221; (usually <code>/var/run/openvswitch</code>) whose name ends in <code>46pid</code>, whose contents are a process ID, and which is locked by a running process46 The <i>name</i> is taken from the pidfile&#8217;s name46</p>
<dd>Currently Open vSwitch is only able to obtain all of the above detail on Linux systems46 On other systems, the same key-value pairs will be present but the values will always be the empty string46</p>
<dt><code>statistics : file_systems</code>: optional string</p>
<dd>A space-separated list of information on local, writable file systems46 Each item in the list describes one file system and consists in turn of a comma-separated list of the following:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Mount point, e46g46 <code>/</code> or <code>/var/log</code>46 Any spaces or commas in the mount point are replaced by underscores46</p>
<dt>2.</p>
<dd>Total size, in kilobytes, as an integer46</p>
<dt>3.</p>
<dd>Amount of storage in use, in kilobytes, as an integer46</dl>
</dl>
<dd>This key-value pair is omitted if there are no local, writable file systems or if Open vSwitch cannot obtain the needed information46</dl>
<p> <i>Version Reporting:</i> These columns report the types and versions of the hardware and software running Open vSwitch46 We recommend in general that software should test whether specific features are supported instead of relying on version number checks46 These values are primarily intended for reporting to human administrators46</p>
<dl>
<dt><code>ovs_version</code>: optional string</p>
<dd>The Open vSwitch version number, e46g46 <code>1461460</code>46</p>
<dt><code>db_version</code>: optional string</p>
<dd>The database schema version number in the form <i>major</i><code>46</code><i>minor</i><code>46</code><i>tweak</i>, e46g46 <code>1462463</code>46 Whenever the database schema is changed in a non-backward compatible way (e46g46 deleting a column or a table), <i>major</i> is incremented46 When the database schema is changed in a backward compatible way (e46g46 adding a new column), <i>minor</i> is incremented46 When the database schema is changed cosmetically (e46g46 reindenting its syntax), <i>tweak</i> is incremented46</p>
<dd>The schema version is part of the database schema, so it can also be retrieved by fetching the schema using the Open vSwitch database protocol46</p>
<dt><code>system_type</code>: optional string</p>
<dd>An identifier for the type of system on top of which Open vSwitch runs, e46g46 <code>XenServer</code> or <code>KVM</code>46</p>
<dd>System integrators are responsible for choosing and setting an appropriate value for this column46</p>
<dt><code>system_version</code>: optional string</p>
<dd>The version of the system identified by <code>system_type</code>, e46g46 <code>546646100-39265p</code> on XenServer 546646100 build 3926546</p>
<dd>System integrators are responsible for choosing and setting an appropriate value for this column46</dl>
<p> <i>Capabilities:</i> These columns report capabilities of the Open vSwitch instance46</p>
<dl>
<dt><code>datapath_types</code>: set of strings</p>
<dd>This column reports the different dpifs registered with the system46 These are the values that this instance supports in the <code>datapath_type</code> column of the <code>Bridge</code> table46</p>
<dt><code>iface_types</code>: set of strings</p>
<dd>This column reports the different netdevs registered with the system46 These are the values that this instance supports in the <code>type</code> column of the <code>Interface</code> table46</dl>
<p> <i>Database Configuration:</i> These columns primarily configure the Open vSwitch database (<code>ovsdb-server</code>), not the Open vSwitch switch (<code>ovs-vswitchd</code>)46 The OVSDB database also uses the <code>ssl</code> settings46 </p>
<p> The Open vSwitch switch does read the database configuration to determine remote IP addresses to which in-band control should apply46</p>
<dl>
<dt><code>manager_options</code>: set of <code>Manager</code>s</p>
<dd>Database clients to which the Open vSwitch database server should connect or to which it should listen, along with options for how these connection should be configured46 See the <code>Manager</code> table for more information46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Bridge TABLE</h2>
<p>Configuration for a bridge within an <code>Open_vSwitch</code>46 </p>
<p> A <code>Bridge</code> record represents an Ethernet switch with one or more &#8220;ports,&#8221; which are the <code>Port</code> records pointed to by the <code>Bridge</code>&#8216;s <code>ports</code> column46</p>
<h3>Summary:</h3>
<dl>
<dt> <i>Core Features:</i></p>
<dl>
<dd>
<dl>
<dt> <code>name</code></p>
<dd>immutable string (must be unique within table) </p>
<dt> <code>ports</code></p>
<dd>set of <code>Port</code>s </p>
<dt> <code>mirrors</code></p>
<dd>set of <code>Mirror</code>s </p>
<dt> <code>netflow</code></p>
<dd>optional <code>NetFlow</code> </p>
<dt> <code>sflow</code></p>
<dd>optional <code>sFlow</code> </p>
<dt> <code>ipfix</code></p>
<dd>optional <code>IPFIX</code> </p>
<dt> <code>flood_vlans</code></p>
<dd>set of up to 4,096 integers, in range 0 to 4,095 </p>
<dt> <code>auto_attach</code></p>
<dd>optional <code>AutoAttach</code></dl>
</dl>
<dt> <i>OpenFlow Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>controller</code></p>
<dd>set of <code>Controller</code>s </p>
<dt> <code>flow_tables</code></p>
<dd>map of integer-<code>Flow_Table</code> pairs, key in range 0 to 254 </p>
<dt> <code>fail_mode</code></p>
<dd>optional string, either <code>secure</code> or <code>standalone</code> </p>
<dt> <code>datapath_id</code></p>
<dd>optional string </p>
<dt> <code>datapath_version</code></p>
<dd>string </p>
<dt> <code>other_config : datapath-id</code></p>
<dd>optional string </p>
<dt> <code>other_config : dp-desc</code></p>
<dd>optional string </p>
<dt> <code>other_config : disable-in-band</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : in-band-queue</code></p>
<dd>optional string, containing an integer, in range 0 to 4,294,967,295 </p>
<dt> <code>protocols</code></p>
<dd>set of strings, one of <code>OpenFlow11</code>, <code>OpenFlow10</code>, <code>OpenFlow13</code>, <code>OpenFlow12</code>, <code>OpenFlow15</code>, or <code>OpenFlow14</code></dl>
</dl>
<dt> <i>Spanning Tree Configuration:</i></p>
<dl>
<dd>
<dd>
<dl>
<dt> <i>STP Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>stp_enable</code></p>
<dd>boolean </p>
<dt> <code>other_config : stp-system-id</code></p>
<dd>optional string </p>
<dt> <code>other_config : stp-priority</code></p>
<dd>optional string, containing an integer, in range 0 to 65,535 </p>
<dt> <code>other_config : stp-hello-time</code></p>
<dd>optional string, containing an integer, in range 1 to 10 </p>
<dt> <code>other_config : stp-max-age</code></p>
<dd>optional string, containing an integer, in range 6 to 40 </p>
<dt> <code>other_config : stp-forward-delay</code></p>
<dd>optional string, containing an integer, in range 4 to 30 </p>
<dt> <code>other_config : mcast-snooping-aging-time</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : mcast-snooping-table-size</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : mcast-snooping-disable-flood-unregistered</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>STP Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>status : stp_bridge_id</code></p>
<dd>optional string </p>
<dt> <code>status : stp_designated_root</code></p>
<dd>optional string </p>
<dt> <code>status : stp_root_path_cost</code></p>
<dd>optional string</dl>
</dl>
</dl>
</dl>
<dt> <i>Rapid Spanning Tree:</i></p>
<dl>
<dd>
<dd>
<dl>
<dt> <i>RSTP Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>rstp_enable</code></p>
<dd>boolean </p>
<dt> <code>other_config : rstp-address</code></p>
<dd>optional string </p>
<dt> <code>other_config : rstp-priority</code></p>
<dd>optional string, containing an integer, in range 0 to 61,440 </p>
<dt> <code>other_config : rstp-ageing-time</code></p>
<dd>optional string, containing an integer, in range 10 to 1,000,000 </p>
<dt> <code>other_config : rstp-force-protocol-version</code></p>
<dd>optional string, containing an integer </p>
<dt> <code>other_config : rstp-max-age</code></p>
<dd>optional string, containing an integer, in range 6 to 40 </p>
<dt> <code>other_config : rstp-forward-delay</code></p>
<dd>optional string, containing an integer, in range 4 to 30 </p>
<dt> <code>other_config : rstp-transmit-hold-count</code></p>
<dd>optional string, containing an integer, in range 1 to 10</dl>
</dl>
<dt> <i>RSTP Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>rstp_status : rstp_bridge_id</code></p>
<dd>optional string </p>
<dt> <code>rstp_status : rstp_root_id</code></p>
<dd>optional string </p>
<dt> <code>rstp_status : rstp_root_path_cost</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>rstp_status : rstp_designated_id</code></p>
<dd>optional string </p>
<dt> <code>rstp_status : rstp_designated_port_id</code></p>
<dd>optional string </p>
<dt> <code>rstp_status : rstp_bridge_port_id</code></p>
<dd>optional string</dl>
</dl>
</dl>
</dl>
<dt> <i>Multicast Snooping Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>mcast_snooping_enable</code></p>
<dd>boolean</dl>
</dl>
<dt> <i>Other Features:</i></p>
<dl>
<dd>
<dl>
<dt> <code>datapath_type</code></p>
<dd>string </p>
<dt> <code>external_ids : bridge-id</code></p>
<dd>optional string </p>
<dt> <code>external_ids : xs-network-uuids</code></p>
<dd>optional string </p>
<dt> <code>other_config : hwaddr</code></p>
<dd>optional string </p>
<dt> <code>other_config : forward-bpdu</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : mac-aging-time</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : mac-table-size</code></p>
<dd>optional string, containing an integer, at least 1</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config</code></p>
<dd>map of string-string pairs </p>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<p><i>Core Features:</i></p>
<dl>
<dt><code>name</code>: immutable string (must be unique within table)</p>
<dd>Bridge identifier46 Should be alphanumeric and no more than about 8 bytes long46 Must be unique among the names of ports, interfaces, and bridges on a host46</p>
<dt><code>ports</code>: set of <code>Port</code>s</p>
<dd>Ports included in the bridge46</p>
<dt><code>mirrors</code>: set of <code>Mirror</code>s</p>
<dd>Port mirroring configuration46</p>
<dt><code>netflow</code>: optional <code>NetFlow</code></p>
<dd>NetFlow configuration46</p>
<dt><code>sflow</code>: optional <code>sFlow</code></p>
<dd>sFlow(R) configuration46</p>
<dt><code>ipfix</code>: optional <code>IPFIX</code></p>
<dd>IPFIX configuration46</p>
<dt><code>flood_vlans</code>: set of up to 4,096 integers, in range 0 to 4,095</p>
<dd>VLAN IDs of VLANs on which MAC address learning should be disabled, so that packets are flooded instead of being sent to specific ports that are believed to contain packets&#8217; destination MACs46 This should ordinarily be used to disable MAC learning on VLANs used for mirroring (RSPAN VLANs)46 It may also be useful for debugging46</p>
<dd>SLB bonding (see the <code>bond_mode</code> column in the <code>Port</code> table) is incompatible with <code>flood_vlans</code>46 Consider using another bonding mode or a different type of mirror instead46</p>
<dt><code>auto_attach</code>: optional <code>AutoAttach</code></p>
<dd>Auto Attach configuration46</dl>
<p> <i>OpenFlow Configuration:</i></p>
<dl>
<dt><code>controller</code>: set of <code>Controller</code>s</p>
<dd>OpenFlow controller set46 If unset, then no OpenFlow controllers will be used46</p>
<dd>If there are primary controllers, removing all of them clears the flow table46 If there are no primary controllers, adding one also clears the flow table46 Other changes to the set of controllers, such as adding or removing a service controller, adding another primary controller to supplement an existing primary controller, or removing only one of two primary controllers, have no effect on the flow table46</p>
<dt><code>flow_tables</code>: map of integer-<code>Flow_Table</code> pairs, key in range 0 to 254</p>
<dd>Configuration for OpenFlow tables46 Each pair maps from an OpenFlow table ID to configuration for that table46</p>
<dt><code>fail_mode</code>: optional string, either <code>secure</code> or <code>standalone</code></p>
<dd>When a controller is configured, it is, ordinarily, responsible for setting up all flows on the switch46 Thus, if the connection to the controller fails, no new network connections can be set up46 If the connection to the controller stays down long enough, no packets can pass through the switch at all46 This setting determines the switch&#8217;s response to such a situation46 It may be set to one of the following:</p>
<dl>
<dd>
<dl>
<dt><code>standalone</code></p>
<dd>If no message is received from the controller for three times the inactivity probe interval (see <code>inactivity_probe</code>), then Open vSwitch will take over responsibility for setting up flows46 In this mode, Open vSwitch causes the bridge to act like an ordinary MAC-learning switch46 Open vSwitch will continue to retry connecting to the controller in the background and, when the connection succeeds, it will discontinue its standalone behavior46</p>
<dt><code>secure</code></p>
<dd>Open vSwitch will not set up flows on its own when the controller connection fails or when no controllers are defined46 The bridge will continue to retry connecting to any defined controllers forever46</dl>
</dl>
<dd>The default is <code>standalone</code> if the value is unset, but future versions of Open vSwitch may change the default46</p>
<dd>The <code>standalone</code> mode can create forwarding loops on a bridge that has more than one uplink port unless STP is enabled46 To avoid loops on such a bridge, configure <code>secure</code> mode or enable STP (see <code>stp_enable</code>)46</p>
<dd>When more than one controller is configured, <code>fail_mode</code> is considered only when none of the configured controllers can be contacted46</p>
<dd>Changing <code>fail_mode</code> when no primary controllers are configured clears the flow table46</p>
<dt><code>datapath_id</code>: optional string</p>
<dd>Reports the OpenFlow datapath ID in use46 Exactly 16 hex digits46 (Setting this column has no useful effect46 Set <code>other-config:datapath-id</code> instead46)</p>
<dt><code>datapath_version</code>: string</p>
<dd>Reports the version number of the Open vSwitch datapath in use46 This allows management software to detect and report discrepancies between Open vSwitch userspace and datapath versions46 (The <code>ovs_version</code> column in the <code>Open_vSwitch</code> reports the Open vSwitch userspace version46) The version reported depends on the datapath in use:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>When the kernel module included in the Open vSwitch source tree is used, this column reports the Open vSwitch version from which the module was taken46</p>
<dt>&bull;</p>
<dd>When the kernel module that is part of the upstream Linux kernel is used, this column reports <code>&lt;unknown&gt;</code>46</p>
<dt>&bull;</p>
<dd>When the datapath is built into the <code>ovs-vswitchd</code> binary, this column reports <code>&lt;built-in&gt;</code>46 A built-in datapath is by definition the same version as the rest of the Open VSwitch userspace46</p>
<dt>&bull;</p>
<dd>Other datapaths (such as the Hyper-V kernel datapath) currently report <code>&lt;unknown&gt;</code>46</dl>
</dl>
<dd>A version discrepancy between <code>ovs-vswitchd</code> and the datapath in use is not normally cause for alarm46 The Open vSwitch kernel datapaths for Linux and Hyper-V, in particular, are designed for maximum inter-version compatibility: any userspace version works with with any kernel version46 Some reasons do exist to insist on particular user/kernel pairings46 First, newer kernel versions add new features, that can only be used by new-enough userspace, e46g46 VXLAN tunneling requires certain minimal userspace and kernel versions46 Second, as an extension to the first reason, some newer kernel versions add new features for enhancing performance that only new-enough userspace versions can take advantage of46</p>
<dt><code>other_config : datapath-id</code>: optional string</p>
<dd>Exactly 16 hex digits to set the OpenFlow datapath ID to a specific value46 May not be all-zero46</p>
<dt><code>other_config : dp-desc</code>: optional string</p>
<dd>Human readable description of datapath46 It it a maximum 256 byte-long free-form string to describe the datapath for debugging purposes, e46g46 <code>switch3 in room 3120</code>46</p>
<dt><code>other_config : disable-in-band</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>If set to <code>true</code>, disable in-band control on the bridge regardless of controller and manager settings46</p>
<dt><code>other_config : in-band-queue</code>: optional string, containing an integer, in range 0 to 4,294,967,295</p>
<dd>A queue ID as a nonnegative integer46 This sets the OpenFlow queue ID that will be used by flows set up by in-band control on this bridge46 If unset, or if the port used by an in-band control flow does not have QoS configured, or if the port does not have a queue with the specified ID, the default queue is used instead46</p>
<dt><code>protocols</code>: set of strings, one of <code>OpenFlow11</code>, <code>OpenFlow10</code>, <code>OpenFlow13</code>, <code>OpenFlow12</code>, <code>OpenFlow15</code>, or <code>OpenFlow14</code></p>
<dd>List of OpenFlow protocols that may be used when negotiating a connection with a controller46 OpenFlow 1460, 1461, 1462, and 1463 are enabled by default if this column is empty46</p>
<dd>OpenFlow 1464 is not enabled by default because its implementation is missing features46</p>
<dd>OpenFlow 1465 has the same risks as OpenFlow 1464, but it is even more experimental because the OpenFlow 1465 specification is still under development and thus subject to change46 Pass <code>&#8211;enable-of15</code> to <code>ovs-vswitchd</code> to allow OpenFlow 1465 to be enabled46</dl>
<p> <i>Spanning Tree Configuration:</i> The IEEE 802461D Spanning Tree Protocol (STP) is a network protocol that ensures loop-free topologies46 It allows redundant links to be included in the network to provide automatic backup paths if the active links fails46 </p>
<p> These settings configure the slower-to-converge but still widely supported version of Spanning Tree Protocol, sometimes known as 802461D-199846 Open vSwitch also supports the newer Rapid Spanning Tree Protocol (RSTP), documented later in the section titled <code>Rapid Spanning Tree Configuration</code>46 </p>
<p> <i>STP Configuration:</i></p>
<dl>
<dt><code>stp_enable</code>: boolean</p>
<dd>Enable spanning tree on the bridge46 By default, STP is disabled on bridges46 Bond, internal, and mirror ports are not supported and will not participate in the spanning tree46</p>
<dd>STP and RSTP are mutually exclusive46 If both are enabled, RSTP will be used46</p>
<dt><code>other_config : stp-system-id</code>: optional string</p>
<dd>The bridge&#8217;s STP identifier (the lower 48 bits of the bridge-id) in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>46 By default, the identifier is the MAC address of the bridge46</p>
<dt><code>other_config : stp-priority</code>: optional string, containing an integer, in range 0 to 65,535</p>
<dd>The bridge&#8217;s relative priority value for determining the root bridge (the upper 16 bits of the bridge-id)46 A bridge with the lowest bridge-id is elected the root46 By default, the priority is 0x800046</p>
<dt><code>other_config : stp-hello-time</code>: optional string, containing an integer, in range 1 to 10</p>
<dd>The interval between transmissions of hello messages by designated ports, in seconds46 By default the hello interval is 2 seconds46</p>
<dt><code>other_config : stp-max-age</code>: optional string, containing an integer, in range 6 to 40</p>
<dd>The maximum age of the information transmitted by the bridge when it is the root bridge, in seconds46 By default, the maximum age is 20 seconds46</p>
<dt><code>other_config : stp-forward-delay</code>: optional string, containing an integer, in range 4 to 30</p>
<dd>The delay to wait between transitioning root and designated ports to <code>forwarding</code>, in seconds46 By default, the forwarding delay is 15 seconds46</p>
<dt><code>other_config : mcast-snooping-aging-time</code>: optional string, containing an integer, at least 1</p>
<dd>The maximum number of seconds to retain a multicast snooping entry for which no packets have been seen46 The default is currently 300 seconds (5 minutes)46 The value, if specified, is forced into a reasonable range, currently 15 to 3600 seconds46</p>
<dt><code>other_config : mcast-snooping-table-size</code>: optional string, containing an integer, at least 1</p>
<dd>The maximum number of multicast snooping addresses to learn46 The default is currently 204846 The value, if specified, is forced into a reasonable range, currently 10 to 1,000,00046</p>
<dt><code>other_config : mcast-snooping-disable-flood-unregistered</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>If set to <code>false</code>, unregistered multicast packets are forwarded to all ports46 If set to <code>true</code>, unregistered multicast packets are forwarded to ports connected to multicast routers46</dl>
<p> <i>STP Status:</i> These key-value pairs report the status of 802461D-199846 They are present only if STP is enabled (via the <code>stp_enable</code> column)46</p>
<dl>
<dt><code>status : stp_bridge_id</code>: optional string</p>
<dd>The bridge ID used in spanning tree advertisements, in the form <i>xxxx</i>46<i>yyyyyyyyyyyy</i> where the <i>x</i>s are the STP priority, the <i>y</i>s are the STP system ID, and each <i>x</i> and <i>y</i> is a hex digit46</p>
<dt><code>status : stp_designated_root</code>: optional string</p>
<dd>The designated root for this spanning tree, in the same form as <code>status:stp_bridge_id</code>46 If this bridge is the root, this will have the same value as <code>status:stp_bridge_id</code>, otherwise it will differ46</p>
<dt><code>status : stp_root_path_cost</code>: optional string</p>
<dd>The path cost of reaching the designated bridge46 A lower number is better46 The value is 0 if this bridge is the root, otherwise it is higher46</dl>
<p> <i>Rapid Spanning Tree:</i> Rapid Spanning Tree Protocol (RSTP), like STP, is a network protocol that ensures loop-free topologies46 RSTP superseded STP with the publication of 802461D-200446 Compared to STP, RSTP converges more quickly and recovers more quickly from failures46 </p>
<p> <i>RSTP Configuration:</i></p>
<dl>
<dt><code>rstp_enable</code>: boolean</p>
<dd>Enable Rapid Spanning Tree on the bridge46 By default, RSTP is disabled on bridges46 Bond, internal, and mirror ports are not supported and will not participate in the spanning tree46</p>
<dd>STP and RSTP are mutually exclusive46 If both are enabled, RSTP will be used46</p>
<dt><code>other_config : rstp-address</code>: optional string</p>
<dd>The bridge&#8217;s RSTP address (the lower 48 bits of the bridge-id) in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>46 By default, the address is the MAC address of the bridge46</p>
<dt><code>other_config : rstp-priority</code>: optional string, containing an integer, in range 0 to 61,440</p>
<dd>The bridge&#8217;s relative priority value for determining the root bridge (the upper 16 bits of the bridge-id)46 A bridge with the lowest bridge-id is elected the root46 By default, the priority is 0x8000 (32768)46 This value needs to be a multiple of 4096, otherwise it&#8217;s rounded to the nearest inferior one46</p>
<dt><code>other_config : rstp-ageing-time</code>: optional string, containing an integer, in range 10 to 1,000,000</p>
<dd>The Ageing Time parameter for the Bridge46 The default value is 300 seconds46</p>
<dt><code>other_config : rstp-force-protocol-version</code>: optional string, containing an integer</p>
<dd>The Force Protocol Version parameter for the Bridge46 This can take the value 0 (STP Compatibility mode) or 2 (the default, normal operation)46</p>
<dt><code>other_config : rstp-max-age</code>: optional string, containing an integer, in range 6 to 40</p>
<dd>The maximum age of the information transmitted by the Bridge when it is the Root Bridge46 The default value is 2046</p>
<dt><code>other_config : rstp-forward-delay</code>: optional string, containing an integer, in range 4 to 30</p>
<dd>The delay used by STP Bridges to transition Root and Designated Ports to Forwarding46 The default value is 1546</p>
<dt><code>other_config : rstp-transmit-hold-count</code>: optional string, containing an integer, in range 1 to 10</p>
<dd>The Transmit Hold Count used by the Port Transmit state machine to limit transmission rate46 The default value is 646</dl>
<p> <i>RSTP Status:</i> These key-value pairs report the status of 802461D-200446 They are present only if RSTP is enabled (via the <code>rstp_enable</code> column)46</p>
<dl>
<dt><code>rstp_status : rstp_bridge_id</code>: optional string</p>
<dd>The bridge ID used in rapid spanning tree advertisements, in the form <i>x</i>46<i>yyy</i>46<i>zzzzzzzzzzzz</i> where <i>x</i> is the RSTP priority, the <i>y</i>s are a locally assigned system ID extension, the <i>z</i>s are the STP system ID, and each <i>x</i>, <i>y</i>, or <i>z</i> is a hex digit46</p>
<dt><code>rstp_status : rstp_root_id</code>: optional string</p>
<dd>The root of this spanning tree, in the same form as <code>rstp_status:rstp_bridge_id</code>46 If this bridge is the root, this will have the same value as <code>rstp_status:rstp_bridge_id</code>, otherwise it will differ46</p>
<dt><code>rstp_status : rstp_root_path_cost</code>: optional string, containing an integer, at least 0</p>
<dd>The path cost of reaching the root46 A lower number is better46 The value is 0 if this bridge is the root, otherwise it is higher46</p>
<dt><code>rstp_status : rstp_designated_id</code>: optional string</p>
<dd>The RSTP designated ID, in the same form as <code>rstp_status:rstp_bridge_id</code>46</p>
<dt><code>rstp_status : rstp_designated_port_id</code>: optional string</p>
<dd>The RSTP designated port ID, as a 4-digit hex number46</p>
<dt><code>rstp_status : rstp_bridge_port_id</code>: optional string</p>
<dd>The RSTP bridge port ID, as a 4-digit hex number46</dl>
<p> <i>Multicast Snooping Configuration:</i> Multicast snooping (RFC 4541) monitors the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery traffic between hosts and multicast routers46 The switch uses what IGMP and MLD snooping learns to forward multicast traffic only to interfaces that are connected to interested receivers46 Currently it supports IGMPv1, IGMPv2, IGMPv3, MLDv1 and MLDv2 protocols46</p>
<dl>
<dt><code>mcast_snooping_enable</code>: boolean</p>
<dd>Enable multicast snooping on the bridge46 For now, the default is disabled46</dl>
<p> <i>Other Features:</i></p>
<dl>
<dt><code>datapath_type</code>: string</p>
<dd>Name of datapath provider46 The kernel datapath has type <code>system</code>46 The userspace datapath has type <code>netdev</code>46 A manager may refer to the <code>datapath_types</code> column of the <code>Open_vSwitch</code> table for a list of the types accepted by this Open vSwitch instance46</p>
<dt><code>external_ids : bridge-id</code>: optional string</p>
<dd>A unique identifier of the bridge46 On Citrix XenServer this will commonly be the same as <code>external_ids:xs-network-uuids</code>46</p>
<dt><code>external_ids : xs-network-uuids</code>: optional string</p>
<dd>Semicolon-delimited set of universally unique identifier(s) for the network with which this bridge is associated on a Citrix XenServer host46 The network identifiers are RFC 4122 UUIDs as displayed by, e46g46, <code>xe network-list</code>46</p>
<dt><code>other_config : hwaddr</code>: optional string</p>
<dd>An Ethernet address in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i> to set the hardware address of the local port and influence the datapath ID46</p>
<dt><code>other_config : forward-bpdu</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Controls forwarding of BPDUs and other network control frames when NORMAL action is invoked46 When this option is <code>false</code> or unset, frames with reserved Ethernet addresses (see table below) will not be forwarded46 When this option is <code>true</code>, such frames will not be treated specially46</p>
<dd>The above general rule has the following exceptions:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If STP is enabled on the bridge (see the <code>stp_enable</code> column in the <code>Bridge</code> table), the bridge processes all received STP packets and never passes them to OpenFlow or forwards them46 This is true even if STP is disabled on an individual port46</p>
<dt>&bull;</p>
<dd>If LLDP is enabled on an interface (see the <code>lldp</code> column in the <code>Interface</code> table), the interface processes received LLDP packets and never passes them to OpenFlow or forwards them46</dl>
</dl>
<dd>Set this option to <code>true</code> if the Open vSwitch bridge connects different Ethernet networks and is not configured to participate in STP46</p>
<dd>This option affects packets with the following destination MAC addresses:</p>
<dl>
<dd>
<dl>
<dt><code>01:80:c2:00:00:00</code></p>
<dd>IEEE 802461D Spanning Tree Protocol (STP)46</p>
<dt><code>01:80:c2:00:00:01</code></p>
<dd>IEEE Pause frame46</p>
<dt><code>01:80:c2:00:00:0</code><i>x</i></p>
<dd>Other reserved protocols46</p>
<dt><code>00:e0:2b:00:00:00</code></p>
<dd>Extreme Discovery Protocol (EDP)46</p>
<dt><code>00:e0:2b:00:00:04</code> and <code>00:e0:2b:00:00:06</code></p>
<dd>Ethernet Automatic Protection Switching (EAPS)46</p>
<dt><code>01:00:0c:cc:cc:cc</code></p>
<dd>Cisco Discovery Protocol (CDP), VLAN Trunking Protocol (VTP), Dynamic Trunking Protocol (DTP), Port Aggregation Protocol (PAgP), and others46</p>
<dt><code>01:00:0c:cc:cc:cd</code></p>
<dd>Cisco Shared Spanning Tree Protocol PVSTP+46</p>
<dt><code>01:00:0c:cd:cd:cd</code></p>
<dd>Cisco STP Uplink Fast46</p>
<dt><code>01:00:0c:00:00:00</code></p>
<dd>Cisco Inter Switch Link46</p>
<dt><code>01:00:0c:cc:cc:c</code><i>x</i></p>
<dd>Cisco CFM46</dl>
</dl>
<dt><code>other_config : mac-aging-time</code>: optional string, containing an integer, at least 1</p>
<dd>The maximum number of seconds to retain a MAC learning entry for which no packets have been seen46 The default is currently 300 seconds (5 minutes)46 The value, if specified, is forced into a reasonable range, currently 15 to 3600 seconds46</p>
<dd>A short MAC aging time allows a network to more quickly detect that a host is no longer connected to a switch port46 However, it also makes it more likely that packets will be flooded unnecessarily, when they are addressed to a connected host that rarely transmits packets46 To reduce the incidence of unnecessary flooding, use a MAC aging time longer than the maximum interval at which a host will ordinarily transmit packets46</p>
<dt><code>other_config : mac-table-size</code>: optional string, containing an integer, at least 1</p>
<dd>The maximum number of MAC addresses to learn46 The default is currently 204846 The value, if specified, is forced into a reasonable range, currently 10 to 1,000,00046</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Port TABLE</h2>
<p>A port within a <code>Bridge</code>46 </p>
<p> Most commonly, a port has exactly one &#8220;interface,&#8221; pointed to by its <code>interfaces</code> column46 Such a port logically corresponds to a port on a physical Ethernet switch46 A port with more than one interface is a &#8220;bonded port&#8221; (see <code>Bonding Configuration</code>)46 </p>
<p> Some properties that one might think as belonging to a port are actually part of the port&#8217;s <code>Interface</code> members46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>name</code></p>
<dd>immutable string (must be unique within table) </p>
<dt> <code>interfaces</code></p>
<dd>set of 1 or more <code>Interface</code>s </p>
<dt> <i>VLAN Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>vlan_mode</code></p>
<dd>optional string, one of <code>access</code>, <code>native-tagged</code>, <code>native-untagged</code>, or <code>trunk</code> </p>
<dt> <code>tag</code></p>
<dd>optional integer, in range 0 to 4,095 </p>
<dt> <code>trunks</code></p>
<dd>set of up to 4,096 integers, in range 0 to 4,095 </p>
<dt> <code>other_config : priority-tags</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>Bonding Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>bond_mode</code></p>
<dd>optional string, one of <code>active-backup</code>, <code>balance-tcp</code>, or <code>balance-slb</code> </p>
<dt> <code>other_config : bond-hash-basis</code></p>
<dd>optional string, containing an integer </p>
<dt> <i>Link Failure Detection:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : bond-detect-mode</code></p>
<dd>optional string, either <code>miimon</code> or <code>carrier</code> </p>
<dt> <code>other_config : bond-miimon-interval</code></p>
<dd>optional string, containing an integer </p>
<dt> <code>bond_updelay</code></p>
<dd>integer </p>
<dt> <code>bond_downdelay</code></p>
<dd>integer</dl>
</dl>
<dt> <i>LACP Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>lacp</code></p>
<dd>optional string, one of <code>active</code>, <code>passive</code>, or <code>off</code> </p>
<dt> <code>other_config : lacp-system-id</code></p>
<dd>optional string </p>
<dt> <code>other_config : lacp-system-priority</code></p>
<dd>optional string, containing an integer, in range 1 to 65,535 </p>
<dt> <code>other_config : lacp-time</code></p>
<dd>optional string, either <code>slow</code> or <code>fast</code> </p>
<dt> <code>other_config : lacp-fallback-ab</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>Rebalancing Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : bond-rebalance-interval</code></p>
<dd>optional string, containing an integer, in range 0 to 10,000</dl>
</dl>
<dt> <code>bond_fake_iface</code></p>
<dd>boolean</dl>
</dl>
<dt> <i>Spanning Tree Protocol:</i></p>
<dl>
<dd>
<dd>
<dl>
<dt> <i>STP Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : stp-enable</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : stp-port-num</code></p>
<dd>optional string, containing an integer, in range 1 to 255 </p>
<dt> <code>other_config : stp-port-priority</code></p>
<dd>optional string, containing an integer, in range 0 to 255 </p>
<dt> <code>other_config : stp-path-cost</code></p>
<dd>optional string, containing an integer, in range 0 to 65,535</dl>
</dl>
<dt> <i>STP Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>status : stp_port_id</code></p>
<dd>optional string </p>
<dt> <code>status : stp_state</code></p>
<dd>optional string, one of <code>disabled</code>, <code>forwarding</code>, <code>learning</code>, <code>listening</code>, or <code>blocking</code> </p>
<dt> <code>status : stp_sec_in_state</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : stp_role</code></p>
<dd>optional string, one of <code>designated</code>, <code>alternate</code>, or <code>root</code></dl>
</dl>
</dl>
</dl>
<dt> <i>Rapid Spanning Tree Protocol:</i></p>
<dl>
<dd>
<dd>
<dl>
<dt> <i>RSTP Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : rstp-enable</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : rstp-port-priority</code></p>
<dd>optional string, containing an integer, in range 0 to 240 </p>
<dt> <code>other_config : rstp-port-num</code></p>
<dd>optional string, containing an integer, in range 1 to 4,095 </p>
<dt> <code>other_config : rstp-port-path-cost</code></p>
<dd>optional string, containing an integer </p>
<dt> <code>other_config : rstp-port-admin-edge</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : rstp-port-auto-edge</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : rstp-port-mcheck</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>RSTP Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>rstp_status : rstp_port_id</code></p>
<dd>optional string </p>
<dt> <code>rstp_status : rstp_port_role</code></p>
<dd>optional string, one of <code>Backup</code>, <code>Designated</code>, <code>Alternate</code>, <code>Root</code>, or <code>Disabled</code> </p>
<dt> <code>rstp_status : rstp_port_state</code></p>
<dd>optional string, one of <code>Disabled</code>, <code>Discarding</code>, <code>Forwarding</code>, or <code>Learning</code> </p>
<dt> <code>rstp_status : rstp_designated_bridge_id</code></p>
<dd>optional string </p>
<dt> <code>rstp_status : rstp_designated_port_id</code></p>
<dd>optional string </p>
<dt> <code>rstp_status : rstp_designated_path_cost</code></p>
<dd>optional string, containing an integer</dl>
</dl>
<dt> <i>RSTP Statistics:</i></p>
<dl>
<dd>
<dl>
<dt> <code>rstp_statistics : rstp_tx_count</code></p>
<dd>optional integer </p>
<dt> <code>rstp_statistics : rstp_rx_count</code></p>
<dd>optional integer </p>
<dt> <code>rstp_statistics : rstp_error_count</code></p>
<dd>optional integer </p>
<dt> <code>rstp_statistics : rstp_uptime</code></p>
<dd>optional integer</dl>
</dl>
</dl>
</dl>
<dt> <i>Multicast Snooping:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : mcast-snooping-flood</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : mcast-snooping-flood-reports</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>Other Features:</i></p>
<dl>
<dd>
<dl>
<dt> <code>qos</code></p>
<dd>optional <code>QoS</code> </p>
<dt> <code>mac</code></p>
<dd>optional string </p>
<dt> <code>fake_bridge</code></p>
<dd>boolean </p>
<dt> <code>external_ids : fake-bridge-id-*</code></p>
<dd>optional string </p>
<dt> <code>other_config : transient</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <code>bond_active_slave</code></p>
<dd>optional string </p>
<dt> <i>Port Statistics:</i></p>
<dl>
<dd>
<dd>
<dl>
<dt> <i>Statistics: STP transmit and receive counters:</i></p>
<dl>
<dd>
<dl>
<dt> <code>statistics : stp_tx_count</code></p>
<dd>optional integer </p>
<dt> <code>statistics : stp_rx_count</code></p>
<dd>optional integer </p>
<dt> <code>statistics : stp_error_count</code></p>
<dd>optional integer</dl>
</dl>
</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config</code></p>
<dd>map of string-string pairs </p>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>name</code>: immutable string (must be unique within table)</p>
<dd>Port name46 Should be alphanumeric and no more than about 8 bytes long46 May be the same as the interface name, for non-bonded ports46 Must otherwise be unique among the names of ports, interfaces, and bridges on a host46</p>
<dt><code>interfaces</code>: set of 1 or more <code>Interface</code>s</p>
<dd>The port&#8217;s interfaces46 If there is more than one, this is a bonded Port46</dl>
<p> <i>VLAN Configuration:</i> Bridge ports support the following types of VLAN configuration:</p>
<dl>
<dd>
<dl>
<dt>trunk</p>
<dd>A trunk port carries packets on one or more specified VLANs specified in the <code>trunks</code> column (often, on every VLAN)46 A packet that ingresses on a trunk port is in the VLAN specified in its 802461Q header, or VLAN 0 if the packet has no 802461Q header46 A packet that egresses through a trunk port will have an 802461Q header if it has a nonzero VLAN ID46</p>
<dd>Any packet that ingresses on a trunk port tagged with a VLAN that the port does not trunk is dropped46</p>
<dt>access</p>
<dd>An access port carries packets on exactly one VLAN specified in the <code>tag</code> column46 Packets egressing on an access port have no 802461Q header46</p>
<dd>Any packet with an 802461Q header with a nonzero VLAN ID that ingresses on an access port is dropped, regardless of whether the VLAN ID in the header is the access port&#8217;s VLAN ID46</p>
<dt>native-tagged</p>
<dd>A native-tagged port resembles a trunk port, with the exception that a packet without an 802461Q header that ingresses on a native-tagged port is in the &#8220;native VLAN&#8221; (specified in the <code>tag</code> column)46</p>
<dt>native-untagged</p>
<dd>A native-untagged port resembles a native-tagged port, with the exception that a packet that egresses on a native-untagged port in the native VLAN will not have an 802461Q header46</dl>
</dl>
<p> A packet will only egress through bridge ports that carry the VLAN of the packet, as described by the rules above46</p>
<dl>
<dt><code>vlan_mode</code>: optional string, one of <code>access</code>, <code>native-tagged</code>, <code>native-untagged</code>, or <code>trunk</code></p>
<dd>The VLAN mode of the port, as described above46 When this column is empty, a default mode is selected as follows:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If <code>tag</code> contains a value, the port is an access port46 The <code>trunks</code> column should be empty46</p>
<dt>&bull;</p>
<dd>Otherwise, the port is a trunk port46 The <code>trunks</code> column value is honored if it is present46</dl>
</dl>
<dt><code>tag</code>: optional integer, in range 0 to 4,095</p>
<dd>For an access port, the port&#8217;s implicitly tagged VLAN46 For a native-tagged or native-untagged port, the port&#8217;s native VLAN46 Must be empty if this is a trunk port46</p>
<dt><code>trunks</code>: set of up to 4,096 integers, in range 0 to 4,095</p>
<dd>For a trunk, native-tagged, or native-untagged port, the 802461Q VLAN or VLANs that this port trunks; if it is empty, then the port trunks all VLANs46 Must be empty if this is an access port46</p>
<dd>A native-tagged or native-untagged port always trunks its native VLAN, regardless of whether <code>trunks</code> includes that VLAN46</p>
<dt><code>other_config : priority-tags</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>An 802461Q header contains two important pieces of information: a VLAN ID and a priority46 A frame with a zero VLAN ID, called a &#8220;priority-tagged&#8221; frame, is supposed to be treated the same way as a frame without an 802461Q header at all (except for the priority)46</p>
<dd>However, some network elements ignore any frame that has 802461Q header at all, even when the VLAN ID is zero46 Therefore, by default Open vSwitch does not output priority-tagged frames, instead omitting the 802461Q header entirely if the VLAN ID is zero46 Set this key to <code>true</code> to enable priority-tagged frames on a port46</p>
<dd>Regardless of this setting, Open vSwitch omits the 802461Q header on output if both the VLAN ID and priority would be zero46</p>
<dd>All frames output to native-tagged ports have a nonzero VLAN ID, so this setting is not meaningful on native-tagged ports46</dl>
<p> <i>Bonding Configuration:</i> A port that has more than one interface is a &#8220;bonded port46&#8221; Bonding allows for load balancing and fail-over46 </p>
<p> The following types of bonding will work with any kind of upstream switch46 On the upstream switch, do not configure the interfaces as a bond:</p>
<dl>
<dd>
<dl>
<dt><code>balance-slb</code></p>
<dd>Balances flows among slaves based on source MAC address and output VLAN, with periodic rebalancing as traffic patterns change46</p>
<dt><code>active-backup</code></p>
<dd>Assigns all flows to one slave, failing over to a backup slave when the active slave is disabled46 This is the only bonding mode in which interfaces may be plugged into different upstream switches46</dl>
</dl>
<p> The following modes require the upstream switch to support 802463ad with successful LACP negotiation46 If LACP negotiation fails and other-config:lacp-fallback-ab is true, then <code>active-backup</code> mode is used:</p>
<dl>
<dd>
<dl>
<dt><code>balance-tcp</code></p>
<dd>Balances flows among slaves based on L2, L3, and L4 protocol information such as destination MAC address, IP address, and TCP port46</dl>
</dl>
<p> These columns apply only to bonded ports46 Their values are otherwise ignored46</p>
<dl>
<dt><code>bond_mode</code>: optional string, one of <code>active-backup</code>, <code>balance-tcp</code>, or <code>balance-slb</code></p>
<dd>The type of bonding used for a bonded port46 Defaults to <code>active-backup</code> if unset46</p>
<dt><code>other_config : bond-hash-basis</code>: optional string, containing an integer</p>
<dd>An integer hashed along with flows when choosing output slaves in load balanced bonds46 When changed, all flows will be assigned different hash values possibly causing slave selection decisions to change46 Does not affect bonding modes which do not employ load balancing such as <code>active-backup</code>46</dl>
<p> <i>Link Failure Detection:</i> An important part of link bonding is detecting that links are down so that they may be disabled46 These settings determine how Open vSwitch detects link failure46</p>
<dl>
<dt><code>other_config : bond-detect-mode</code>: optional string, either <code>miimon</code> or <code>carrier</code></p>
<dd>The means used to detect link failures46 Defaults to <code>carrier</code> which uses each interface&#8217;s carrier to detect failures46 When set to <code>miimon</code>, will check for failures by polling each interface&#8217;s MII46</p>
<dt><code>other_config : bond-miimon-interval</code>: optional string, containing an integer</p>
<dd>The interval, in milliseconds, between successive attempts to poll each interface&#8217;s MII46 Relevant only when <code>other_config:bond-detect-mode</code> is <code>miimon</code>46</p>
<dt><code>bond_updelay</code>: integer</p>
<dd>The number of milliseconds for which the link must stay up on an interface before the interface is considered to be up46 Specify <code>0</code> to enable the interface immediately46</p>
<dd>This setting is honored only when at least one bonded interface is already enabled46 When no interfaces are enabled, then the first bond interface to come up is enabled immediately46</p>
<dt><code>bond_downdelay</code>: integer</p>
<dd>The number of milliseconds for which the link must stay down on an interface before the interface is considered to be down46 Specify <code>0</code> to disable the interface immediately46</dl>
<p> <i>LACP Configuration:</i> LACP, the Link Aggregation Control Protocol, is an IEEE standard that allows switches to automatically detect that they are connected by multiple links and aggregate across those links46 These settings control LACP behavior46</p>
<dl>
<dt><code>lacp</code>: optional string, one of <code>active</code>, <code>passive</code>, or <code>off</code></p>
<dd>Configures LACP on this port46 LACP allows directly connected switches to negotiate which links may be bonded46 LACP may be enabled on non-bonded ports for the benefit of any switches they may be connected to46 <code>active</code> ports are allowed to initiate LACP negotiations46 <code>passive</code> ports are allowed to participate in LACP negotiations initiated by a remote switch, but not allowed to initiate such negotiations themselves46 If LACP is enabled on a port whose partner switch does not support LACP, the bond will be disabled, unless other-config:lacp-fallback-ab is set to true46 Defaults to <code>off</code> if unset46</p>
<dt><code>other_config : lacp-system-id</code>: optional string</p>
<dd>The LACP system ID of this <code>Port</code>46 The system ID of a LACP bond is used to identify itself to its partners46 Must be a nonzero MAC address46 Defaults to the bridge Ethernet address if unset46</p>
<dt><code>other_config : lacp-system-priority</code>: optional string, containing an integer, in range 1 to 65,535</p>
<dd>The LACP system priority of this <code>Port</code>46 In LACP negotiations, link status decisions are made by the system with the numerically lower priority46</p>
<dt><code>other_config : lacp-time</code>: optional string, either <code>slow</code> or <code>fast</code></p>
<dd>The LACP timing which should be used on this <code>Port</code>46 By default <code>slow</code> is used46 When configured to be <code>fast</code> LACP heartbeats are requested at a rate of once per second causing connectivity problems to be detected more quickly46 In <code>slow</code> mode, heartbeats are requested at a rate of once every 30 seconds46</p>
<dt><code>other_config : lacp-fallback-ab</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Determines the behavior of openvswitch bond in LACP mode46 If the partner switch does not support LACP, setting this option to <code>true</code> allows openvswitch to fallback to active-backup46 If the option is set to <code>false</code>, the bond will be disabled46 In both the cases, once the partner switch is configured to LACP mode, the bond will use LACP46</dl>
<p> <i>Rebalancing Configuration:</i> These settings control behavior when a bond is in <code>balance-slb</code> or <code>balance-tcp</code> mode46</p>
<dl>
<dt><code>other_config : bond-rebalance-interval</code>: optional string, containing an integer, in range 0 to 10,000</p>
<dd>For a load balanced bonded port, the number of milliseconds between successive attempts to rebalance the bond, that is, to move flows from one interface on the bond to another in an attempt to keep usage of each interface roughly equal46 If zero, load balancing is disabled on the bond (link failure still cause flows to move)46 If less than 1000ms, the rebalance interval will be 1000ms46</p>
<dt><code>bond_fake_iface</code>: boolean</p>
<dd>For a bonded port, whether to create a fake internal interface with the name of the port46 Use only for compatibility with legacy software that requires this46</dl>
<p> <i>Spanning Tree Protocol:</i> The configuration here is only meaningful, and the status is only populated, when 802461D-1998 Spanning Tree Protocol is enabled on the port&#8217;s <code>Bridge</code> with its <code>stp_enable</code> column46 </p>
<p> <i>STP Configuration:</i></p>
<dl>
<dt><code>other_config : stp-enable</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>When STP is enabled on a bridge, it is enabled by default on all of the bridge&#8217;s ports except bond, internal, and mirror ports (which do not work with STP)46 If this column&#8217;s value is <code>false</code>, STP is disabled on the port46</p>
<dt><code>other_config : stp-port-num</code>: optional string, containing an integer, in range 1 to 255</p>
<dd>The port number used for the lower 8 bits of the port-id46 By default, the numbers will be assigned automatically46 If any port&#8217;s number is manually configured on a bridge, then they must all be46</p>
<dt><code>other_config : stp-port-priority</code>: optional string, containing an integer, in range 0 to 255</p>
<dd>The port&#8217;s relative priority value for determining the root port (the upper 8 bits of the port-id)46 A port with a lower port-id will be chosen as the root port46 By default, the priority is 0x8046</p>
<dt><code>other_config : stp-path-cost</code>: optional string, containing an integer, in range 0 to 65,535</p>
<dd>Spanning tree path cost for the port46 A lower number indicates a faster link46 By default, the cost is based on the maximum speed of the link46</dl>
<p> <i>STP Status:</i></p>
<dl>
<dt><code>status : stp_port_id</code>: optional string</p>
<dd>The port ID used in spanning tree advertisements for this port, as 4 hex digits46 Configuring the port ID is described in the <code>stp-port-num</code> and <code>stp-port-priority</code> keys of the <code>other_config</code> section earlier46</p>
<dt><code>status : stp_state</code>: optional string, one of <code>disabled</code>, <code>forwarding</code>, <code>learning</code>, <code>listening</code>, or <code>blocking</code></p>
<dd>STP state of the port46</p>
<dt><code>status : stp_sec_in_state</code>: optional string, containing an integer, at least 0</p>
<dd>The amount of time this port has been in the current STP state, in seconds46</p>
<dt><code>status : stp_role</code>: optional string, one of <code>designated</code>, <code>alternate</code>, or <code>root</code></p>
<dd>STP role of the port46</dl>
<p> <i>Rapid Spanning Tree Protocol:</i> The configuration here is only meaningful, and the status and statistics are only populated, when 802461D-1998 Spanning Tree Protocol is enabled on the port&#8217;s <code>Bridge</code> with its <code>stp_enable</code> column46 </p>
<p> <i>RSTP Configuration:</i></p>
<dl>
<dt><code>other_config : rstp-enable</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>When RSTP is enabled on a bridge, it is enabled by default on all of the bridge&#8217;s ports except bond, internal, and mirror ports (which do not work with RSTP)46 If this column&#8217;s value is <code>false</code>, RSTP is disabled on the port46</p>
<dt><code>other_config : rstp-port-priority</code>: optional string, containing an integer, in range 0 to 240</p>
<dd>The port&#8217;s relative priority value for determining the root port, in multiples of 1646 By default, the port priority is 0x80 (128)46 Any value in the lower 4 bits is rounded off46 The significant upper 4 bits become the upper 4 bits of the port-id46 A port with the lowest port-id is elected as the root46</p>
<dt><code>other_config : rstp-port-num</code>: optional string, containing an integer, in range 1 to 4,095</p>
<dd>The local RSTP port number, used as the lower 12 bits of the port-id46 By default the port numbers are assigned automatically, and typically may not correspond to the OpenFlow port numbers46 A port with the lowest port-id is elected as the root46</p>
<dt><code>other_config : rstp-port-path-cost</code>: optional string, containing an integer</p>
<dd>The port path cost46 The Port&#8217;s contribution, when it is the Root Port, to the Root Path Cost for the Bridge46 By default the cost is automatically calculated from the port&#8217;s speed46</p>
<dt><code>other_config : rstp-port-admin-edge</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>The admin edge port parameter for the Port46 Default is <code>false</code>46</p>
<dt><code>other_config : rstp-port-auto-edge</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>The auto edge port parameter for the Port46 Default is <code>true</code>46</p>
<dt><code>other_config : rstp-port-mcheck</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>The mcheck port parameter for the Port46 Default is <code>false</code>46 May be set to force the Port Protocol Migration state machine to transmit RST BPDUs for a MigrateTime period, to test whether all STP Bridges on the attached LAN have been removed and the Port can continue to transmit RSTP BPDUs46 Setting mcheck has no effect if the Bridge is operating in STP Compatibility mode46</p>
<dd>Changing the value from <code>true</code> to <code>false</code> has no effect, but needs to be done if this behavior is to be triggered again by subsequently changing the value from <code>false</code> to <code>true</code>46</dl>
<p> <i>RSTP Status:</i></p>
<dl>
<dt><code>rstp_status : rstp_port_id</code>: optional string</p>
<dd>The port ID used in spanning tree advertisements for this port, as 4 hex digits46 Configuring the port ID is described in the <code>rstp-port-num</code> and <code>rstp-port-priority</code> keys of the <code>other_config</code> section earlier46</p>
<dt><code>rstp_status : rstp_port_role</code>: optional string, one of <code>Backup</code>, <code>Designated</code>, <code>Alternate</code>, <code>Root</code>, or <code>Disabled</code></p>
<dd>RSTP role of the port46</p>
<dt><code>rstp_status : rstp_port_state</code>: optional string, one of <code>Disabled</code>, <code>Discarding</code>, <code>Forwarding</code>, or <code>Learning</code></p>
<dd>RSTP state of the port46</p>
<dt><code>rstp_status : rstp_designated_bridge_id</code>: optional string</p>
<dd>The port&#8217;s RSTP designated bridge ID, in the same form as <code>rstp_status:rstp_bridge_id</code> in the <code>Bridge</code> table46</p>
<dt><code>rstp_status : rstp_designated_port_id</code>: optional string</p>
<dd>The port&#8217;s RSTP designated port ID, as 4 hex digits46</p>
<dt><code>rstp_status : rstp_designated_path_cost</code>: optional string, containing an integer</p>
<dd>The port&#8217;s RSTP designated path cost46 Lower is better46</dl>
<p> <i>RSTP Statistics:</i></p>
<dl>
<dt><code>rstp_statistics : rstp_tx_count</code>: optional integer</p>
<dd>Number of RSTP BPDUs transmitted through this port46</p>
<dt><code>rstp_statistics : rstp_rx_count</code>: optional integer</p>
<dd>Number of valid RSTP BPDUs received by this port46</p>
<dt><code>rstp_statistics : rstp_error_count</code>: optional integer</p>
<dd>Number of invalid RSTP BPDUs received by this port46</p>
<dt><code>rstp_statistics : rstp_uptime</code>: optional integer</p>
<dd>The duration covered by the other RSTP statistics, in seconds46</dl>
<p> <i>Multicast Snooping:</i></p>
<dl>
<dt><code>other_config : mcast-snooping-flood</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>If set to <code>true</code>, multicast packets (except Reports) are unconditionally forwarded to the specific port46</p>
<dt><code>other_config : mcast-snooping-flood-reports</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>If set to <code>true</code>, multicast Reports are unconditionally forwarded to the specific port46</dl>
<p> <i>Other Features:</i></p>
<dl>
<dt><code>qos</code>: optional <code>QoS</code></p>
<dd>Quality of Service configuration for this port46</p>
<dt><code>mac</code>: optional string</p>
<dd>The MAC address to use for this port for the purpose of choosing the bridge&#8217;s MAC address46 This column does not necessarily reflect the port&#8217;s actual MAC address, nor will setting it change the port&#8217;s actual MAC address46</p>
<dt><code>fake_bridge</code>: boolean</p>
<dd>Does this port represent a sub-bridge for its tagged VLAN within the Bridge? See <a href="/docs/linux/man/8-ovs-vsctl/">ovs-vsctl</a>(8) for more information46</p>
<dt><code>external_ids : fake-bridge-id-*</code>: optional string</p>
<dd>External IDs for a fake bridge (see the <code>fake_bridge</code> column) are defined by prefixing a <code>Bridge</code> <code>external_ids</code> key with <code>fake-bridge-</code>, e46g46 <code>fake-bridge-xs-network-uuids</code>46</p>
<dt><code>other_config : transient</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>If set to <code>true</code>, the port will be removed when <code>ovs-ctl start &#8211;delete-transient-ports</code> is used46</p>
<dt><code>bond_active_slave</code>: optional string</p>
<dd>For a bonded port, record the mac address of the current active slave46</dl>
<p> <i>Port Statistics:</i> Key-value pairs that report port statistics46 The update period is controlled by <code>other_config:stats-update-interval</code> in the <code>Open_vSwitch</code> table46 </p>
<p> <i>Statistics: STP transmit and receive counters:</i></p>
<dl>
<dt><code>statistics : stp_tx_count</code>: optional integer</p>
<dd>Number of STP BPDUs sent on this port by the spanning tree library46</p>
<dt><code>statistics : stp_rx_count</code>: optional integer</p>
<dd>Number of STP BPDUs received on this port and accepted by the spanning tree library46</p>
<dt><code>statistics : stp_error_count</code>: optional integer</p>
<dd>Number of bad STP BPDUs received on this port46 Bad BPDUs include runt packets and those with an unexpected protocol ID46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Interface TABLE</h2>
<p>An interface within a <code>Port</code>46</p>
<h3>Summary:</h3>
<dl>
<dt> <i>Core Features:</i></p>
<dl>
<dd>
<dl>
<dt> <code>name</code></p>
<dd>immutable string (must be unique within table) </p>
<dt> <code>ifindex</code></p>
<dd>optional integer, in range 0 to 4,294,967,295 </p>
<dt> <code>mac_in_use</code></p>
<dd>optional string </p>
<dt> <code>mac</code></p>
<dd>optional string </p>
<dt> <code>error</code></p>
<dd>optional string </p>
<dt> <i>OpenFlow Port Number:</i></p>
<dl>
<dd>
<dl>
<dt> <code>ofport</code></p>
<dd>optional integer </p>
<dt> <code>ofport_request</code></p>
<dd>optional integer, in range 1 to 65,279</dl>
</dl>
</dl>
</dl>
<dt> <i>System-Specific Details:</i></p>
<dl>
<dd>
<dl>
<dt> <code>type</code></p>
<dd>string</dl>
</dl>
<dt> <i>Tunnel Options:</i></p>
<dl>
<dd>
<dl>
<dt> <code>options : remote_ip</code></p>
<dd>optional string </p>
<dt> <code>options : local_ip</code></p>
<dd>optional string </p>
<dt> <code>options : in_key</code></p>
<dd>optional string </p>
<dt> <code>options : out_key</code></p>
<dd>optional string </p>
<dt> <code>options : key</code></p>
<dd>optional string </p>
<dt> <code>options : tos</code></p>
<dd>optional string </p>
<dt> <code>options : ttl</code></p>
<dd>optional string </p>
<dt> <code>options : df_default</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <i>Tunnel Options: vxlan only:</i></p>
<dl>
<dd>
<dl>
<dt> <code>options : exts</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>Tunnel Options: gre, ipsec_gre, geneve, and vxlan:</i></p>
<dl>
<dd>
<dl>
<dt> <code>options : csum</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>Tunnel Options: ipsec_gre only:</i></p>
<dl>
<dd>
<dl>
<dt> <code>options : peer_cert</code></p>
<dd>optional string </p>
<dt> <code>options : certificate</code></p>
<dd>optional string </p>
<dt> <code>options : private_key</code></p>
<dd>optional string </p>
<dt> <code>options : psk</code></p>
<dd>optional string</dl>
</dl>
</dl>
</dl>
<dt> <i>Patch Options:</i></p>
<dl>
<dd>
<dl>
<dt> <code>options : peer</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>Interface Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>admin_state</code></p>
<dd>optional string, either <code>down</code> or <code>up</code> </p>
<dt> <code>link_state</code></p>
<dd>optional string, either <code>down</code> or <code>up</code> </p>
<dt> <code>link_resets</code></p>
<dd>optional integer </p>
<dt> <code>link_speed</code></p>
<dd>optional integer </p>
<dt> <code>duplex</code></p>
<dd>optional string, either <code>full</code> or <code>half</code> </p>
<dt> <code>mtu</code></p>
<dd>optional integer </p>
<dt> <code>lacp_current</code></p>
<dd>optional boolean </p>
<dt> <code>status</code></p>
<dd>map of string-string pairs </p>
<dt> <code>status : driver_name</code></p>
<dd>optional string </p>
<dt> <code>status : driver_version</code></p>
<dd>optional string </p>
<dt> <code>status : firmware_version</code></p>
<dd>optional string </p>
<dt> <code>status : source_ip</code></p>
<dd>optional string </p>
<dt> <code>status : tunnel_egress_iface</code></p>
<dd>optional string </p>
<dt> <code>status : tunnel_egress_iface_carrier</code></p>
<dd>optional string, either <code>down</code> or <code>up</code></dl>
</dl>
<dt> <i>Statistics:</i></p>
<dl>
<dd>
<dd>
<dl>
<dt> <i>Statistics: Successful transmit and receive counters:</i></p>
<dl>
<dd>
<dl>
<dt> <code>statistics : rx_packets</code></p>
<dd>optional integer </p>
<dt> <code>statistics : rx_bytes</code></p>
<dd>optional integer </p>
<dt> <code>statistics : tx_packets</code></p>
<dd>optional integer </p>
<dt> <code>statistics : tx_bytes</code></p>
<dd>optional integer</dl>
</dl>
<dt> <i>Statistics: Receive errors:</i></p>
<dl>
<dd>
<dl>
<dt> <code>statistics : rx_dropped</code></p>
<dd>optional integer </p>
<dt> <code>statistics : rx_frame_err</code></p>
<dd>optional integer </p>
<dt> <code>statistics : rx_over_err</code></p>
<dd>optional integer </p>
<dt> <code>statistics : rx_crc_err</code></p>
<dd>optional integer </p>
<dt> <code>statistics : rx_errors</code></p>
<dd>optional integer</dl>
</dl>
<dt> <i>Statistics: Transmit errors:</i></p>
<dl>
<dd>
<dl>
<dt> <code>statistics : tx_dropped</code></p>
<dd>optional integer </p>
<dt> <code>statistics : collisions</code></p>
<dd>optional integer </p>
<dt> <code>statistics : tx_errors</code></p>
<dd>optional integer</dl>
</dl>
</dl>
</dl>
<dt> <i>Ingress Policing:</i></p>
<dl>
<dd>
<dl>
<dt> <code>ingress_policing_rate</code></p>
<dd>integer, at least 0 </p>
<dt> <code>ingress_policing_burst</code></p>
<dd>integer, at least 0</dl>
</dl>
<dt> <i>Bidirectional Forwarding Detection (BFD):</i></p>
<dl>
<dd>
<dd>
<dl>
<dt> <i>BFD Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>bfd : enable</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd : min_rx</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>bfd : min_tx</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>bfd : decay_min_rx</code></p>
<dd>optional string, containing an integer </p>
<dt> <code>bfd : forwarding_if_rx</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd : cpath_down</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd : check_tnl_key</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd : bfd_local_src_mac</code></p>
<dd>optional string </p>
<dt> <code>bfd : bfd_local_dst_mac</code></p>
<dd>optional string </p>
<dt> <code>bfd : bfd_remote_dst_mac</code></p>
<dd>optional string </p>
<dt> <code>bfd : bfd_src_ip</code></p>
<dd>optional string </p>
<dt> <code>bfd : bfd_dst_ip</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>BFD Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>bfd_status : state</code></p>
<dd>optional string, one of <code>down</code>, <code>init</code>, <code>up</code>, or <code>admin_down</code> </p>
<dt> <code>bfd_status : forwarding</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>bfd_status : diagnostic</code></p>
<dd>optional string </p>
<dt> <code>bfd_status : remote_state</code></p>
<dd>optional string, one of <code>down</code>, <code>init</code>, <code>up</code>, or <code>admin_down</code> </p>
<dt> <code>bfd_status : remote_diagnostic</code></p>
<dd>optional string </p>
<dt> <code>bfd_status : flap_count</code></p>
<dd>optional string, containing an integer, at least 0</dl>
</dl>
</dl>
</dl>
<dt> <i>Connectivity Fault Management:</i></p>
<dl>
<dd>
<dl>
<dt> <code>cfm_mpid</code></p>
<dd>optional integer </p>
<dt> <code>cfm_flap_count</code></p>
<dd>optional integer </p>
<dt> <code>cfm_fault</code></p>
<dd>optional boolean </p>
<dt> <code>cfm_fault_status : recv</code></p>
<dd>none </p>
<dt> <code>cfm_fault_status : rdi</code></p>
<dd>none </p>
<dt> <code>cfm_fault_status : maid</code></p>
<dd>none </p>
<dt> <code>cfm_fault_status : loopback</code></p>
<dd>none </p>
<dt> <code>cfm_fault_status : overflow</code></p>
<dd>none </p>
<dt> <code>cfm_fault_status : override</code></p>
<dd>none </p>
<dt> <code>cfm_fault_status : interval</code></p>
<dd>none </p>
<dt> <code>cfm_remote_opstate</code></p>
<dd>optional string, either <code>down</code> or <code>up</code> </p>
<dt> <code>cfm_health</code></p>
<dd>optional integer, in range 0 to 100 </p>
<dt> <code>cfm_remote_mpids</code></p>
<dd>set of integers </p>
<dt> <code>other_config : cfm_interval</code></p>
<dd>optional string, containing an integer </p>
<dt> <code>other_config : cfm_extended</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : cfm_demand</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : cfm_opstate</code></p>
<dd>optional string, either <code>down</code> or <code>up</code> </p>
<dt> <code>other_config : cfm_ccm_vlan</code></p>
<dd>optional string, containing an integer, in range 1 to 4,095 </p>
<dt> <code>other_config : cfm_ccm_pcp</code></p>
<dd>optional string, containing an integer, in range 1 to 7</dl>
</dl>
<dt> <i>Bonding Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : lacp-port-id</code></p>
<dd>optional string, containing an integer, in range 1 to 65,535 </p>
<dt> <code>other_config : lacp-port-priority</code></p>
<dd>optional string, containing an integer, in range 1 to 65,535 </p>
<dt> <code>other_config : lacp-aggregation-key</code></p>
<dd>optional string, containing an integer, in range 1 to 65,535</dl>
</dl>
<dt> <i>Virtual Machine Identifiers:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids : attached-mac</code></p>
<dd>optional string </p>
<dt> <code>external_ids : iface-id</code></p>
<dd>optional string </p>
<dt> <code>external_ids : iface-status</code></p>
<dd>optional string, either <code>active</code> or <code>inactive</code> </p>
<dt> <code>external_ids : xs-vif-uuid</code></p>
<dd>optional string </p>
<dt> <code>external_ids : xs-network-uuid</code></p>
<dd>optional string </p>
<dt> <code>external_ids : vm-id</code></p>
<dd>optional string </p>
<dt> <code>external_ids : xs-vm-uuid</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>VLAN Splinters:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : enable-vlan-splinters</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>Auto Attach Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>lldp : enable</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config</code></p>
<dd>map of string-string pairs </p>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<p><i>Core Features:</i></p>
<dl>
<dt><code>name</code>: immutable string (must be unique within table)</p>
<dd>Interface name46 Should be alphanumeric and no more than about 8 bytes long46 May be the same as the port name, for non-bonded ports46 Must otherwise be unique among the names of ports, interfaces, and bridges on a host46</p>
<dt><code>ifindex</code>: optional integer, in range 0 to 4,294,967,295</p>
<dd>A positive interface index as defined for SNMP MIB-II in RFCs 1213 and 2863, if the interface has one, otherwise 046 The ifindex is useful for seamless integration with protocols such as SNMP and sFlow46</p>
<dt><code>mac_in_use</code>: optional string</p>
<dd>The MAC address in use by this interface46</p>
<dt><code>mac</code>: optional string</p>
<dd>Ethernet address to set for this interface46 If unset then the default MAC address is used:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>For the local interface, the default is the lowest-numbered MAC address among the other bridge ports, either the value of the <code>mac</code> in its <code>Port</code> record, if set, or its actual MAC (for bonded ports, the MAC of its slave whose name is first in alphabetical order)46 Internal ports and bridge ports that are used as port mirroring destinations (see the <code>Mirror</code> table) are ignored46</p>
<dt>&bull;</p>
<dd>For other internal interfaces, the default MAC is randomly generated46</p>
<dt>&bull;</p>
<dd>External interfaces typically have a MAC address associated with their hardware46</dl>
</dl>
<dd>Some interfaces may not have a software-controllable MAC address46</p>
<dt><code>error</code>: optional string</p>
<dd>If the configuration of the port failed, as indicated by -1 in <code>ofport</code>, Open vSwitch sets this column to an error description in human readable form46 Otherwise, Open vSwitch clears this column46</dl>
<p> <i>OpenFlow Port Number:</i> When a client adds a new interface, Open vSwitch chooses an OpenFlow port number for the new port46 If the client that adds the port fills in <code>ofport_request</code>, then Open vSwitch tries to use its value as the OpenFlow port number46 Otherwise, or if the requested port number is already in use or cannot be used for another reason, Open vSwitch automatically assigns a free port number46 Regardless of how the port number was obtained, Open vSwitch then reports in <code>ofport</code> the port number actually assigned46 </p>
<p> Open vSwitch limits the port numbers that it automatically assigns to the range 1 through 32,767, inclusive46 Controllers therefore have free use of ports 32,768 and up46</p>
<dl>
<dt><code>ofport</code>: optional integer</p>
<dd>OpenFlow port number for this interface46 Open vSwitch sets this column&#8217;s value, so other clients should treat it as read-only46</p>
<dd>The OpenFlow &#8220;local&#8221; port (<code>OFPP_LOCAL</code>) is 65,53446 The other valid port numbers are in the range 1 to 65,279, inclusive46 Value -1 indicates an error adding the interface46</p>
<dt><code>ofport_request</code>: optional integer, in range 1 to 65,279</p>
<dd>Requested OpenFlow port number for this interface46</p>
<dd>A client should ideally set this column&#8217;s value in the same database transaction that it uses to create the interface46 Open vSwitch version 2461 and later will honor a later request for a specific port number, althuogh it might confuse some controllers: OpenFlow does not have a way to announce a port number change, so Open vSwitch represents it over OpenFlow as a port deletion followed immediately by a port addition46</p>
<dd>If <code>ofport_request</code> is set or changed to some other port&#8217;s automatically assigned port number, Open vSwitch chooses a new port number for the latter port46</dl>
<p> <i>System-Specific Details:</i></p>
<dl>
<dt><code>type</code>: string</p>
<dd>The interface type46 The types supported by a particular instance of Open vSwitch are listed in the <code>iface_types</code> column in the <code>Open_vSwitch</code> table46 The following types are defined:</p>
<dl>
<dd>
<dl>
<dt><code>system</code></p>
<dd>An ordinary network device, e46g46 <code>eth0</code> on Linux46 Sometimes referred to as &#8220;external interfaces&#8221; since they are generally connected to hardware external to that on which the Open vSwitch is running46 The empty string is a synonym for <code>system</code>46</p>
<dt><code>internal</code></p>
<dd>A simulated network device that sends and receives traffic46 An internal interface whose <code>name</code> is the same as its bridge&#8217;s <code>name</code> is called the &#8220;local interface46&#8221; It does not make sense to bond an internal interface, so the terms &#8220;port&#8221; and &#8220;interface&#8221; are often used imprecisely for internal interfaces46</p>
<dt><code>tap</code></p>
<dd>A TUN/TAP device managed by Open vSwitch46</p>
<dt><code>geneve</code></p>
<dd>An Ethernet over Geneve (<code><a rel="nofollow" href="http://tools46ietf46org/html/draft-ietf-nvo3-geneve-00">http://tools46ietf46org/html/draft-ietf-nvo3-geneve-00</a></code>) IPv4 tunnel46 A description of how to match and set Geneve options can be found in the <code>ovs-ofctl</code> manual page46</p>
<dt><code>gre</code></p>
<dd>An Ethernet over RFC 2890 Generic Routing Encapsulation over IPv4 tunnel46</p>
<dt><code>ipsec_gre</code></p>
<dd>An Ethernet over RFC 2890 Generic Routing Encapsulation over IPv4 IPsec tunnel46</p>
<dt><code>vxlan</code></p>
<dd>An Ethernet tunnel over the UDP-based VXLAN protocol described in RFC 734846</p>
<dd>Open vSwitch uses UDP destination port 478946 The source port used for VXLAN traffic varies on a per-flow basis and is in the ephemeral port range46</p>
<dt><code>lisp</code></p>
<dd>A layer 3 tunnel over the experimental, UDP-based Locator/ID Separation Protocol (RFC 6830)46</p>
<dd>Only IPv4 and IPv6 packets are supported by the protocol, and they are sent and received without an Ethernet header46 Traffic to/from LISP ports is expected to be configured explicitly, and the ports are not intended to participate in learning based switching46 As such, they are always excluded from packet flooding46</p>
<dt><code>stt</code></p>
<dd>The Stateless TCP Tunnel (STT) is particularly useful when tunnel endpoints are in end-systems, as it utilizes the capabilities of standard network interface cards to improve performance46 STT utilizes a TCP-like header inside the IP header46 It is stateless, i46e46, there is no TCP connection state of any kind associated with the tunnel46 The TCP-like header is used to leverage the capabilities of existing network interface cards, but should not be interpreted as implying any sort of connection state between endpoints46 Since the STT protocol does not engage in the usual TCP 3-way handshake, so it will have difficulty traversing stateful firewalls46 The protocol is documented at <a rel="nofollow" href="http://www46ietf46org/archive/id/draft-davie-stt-0646txt">http://www46ietf46org/archive/id/draft-davie-stt-0646txt</a> All traffic uses a default destination port of 747146 STT is only available in kernel datapath on kernel 3465 or newer46</p>
<dt><code>patch</code></p>
<dd>A pair of virtual devices that act as a patch cable46</p>
<dt><code>null</code></p>
<dd>An ignored interface46 Deprecated and slated for removal in February 201346</dl>
</dl>
</dl>
<p> <i>Tunnel Options:</i> These options apply to interfaces with <code>type</code> of <code>geneve</code>, <code>gre</code>, <code>ipsec_gre</code>, <code>vxlan</code>, <code>lisp</code> and <code>stt</code>46 </p>
<p> Each tunnel must be uniquely identified by the combination of <code>type</code>, <code>options:remote_ip</code>, <code>options:local_ip</code>, and <code>options:in_key</code>46 If two ports are defined that are the same except one has an optional identifier and the other does not, the more specific one is matched first46 <code>options:in_key</code> is considered more specific than <code>options:local_ip</code> if a port defines one and another port defines the other46</p>
<dl>
<dt><code>options : remote_ip</code>: optional string</p>
<dd>Required46 The remote tunnel endpoint, one of:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>An IPv4 address (not a DNS name), e46g46 <code>1924616846046123</code>46 Only unicast endpoints are supported46</p>
<dt>&bull;</p>
<dd>The word <code>flow</code>46 The tunnel accepts packets from any remote tunnel endpoint46 To process only packets from a specific remote tunnel endpoint, the flow entries may match on the <code>tun_src</code> field46 When sending packets to a <code>remote_ip=flow</code> tunnel, the flow actions must explicitly set the <code>tun_dst</code> field to the IP address of the desired remote tunnel endpoint, e46g46 with a <code>set_field</code> action46</dl>
</dl>
<dd>The remote tunnel endpoint for any packet received from a tunnel is available in the <code>tun_src</code> field for matching in the flow table46</p>
<dt><code>options : local_ip</code>: optional string</p>
<dd>Optional46 The tunnel destination IP that received packets must match46 Default is to match all addresses46 If specified, may be one of:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>An IPv4 address (not a DNS name), e46g46 <code>192461684612463</code>46</p>
<dt>&bull;</p>
<dd>The word <code>flow</code>46 The tunnel accepts packets sent to any of the local IP addresses of the system running OVS46 To process only packets sent to a specific IP address, the flow entries may match on the <code>tun_dst</code> field46 When sending packets to a <code>local_ip=flow</code> tunnel, the flow actions may explicitly set the <code>tun_src</code> field to the desired IP address, e46g46 with a <code>set_field</code> action46 However, while routing the tunneled packet out, the local system may override the specified address with the local IP address configured for the outgoing system interface46</p>
<dd>This option is valid only for tunnels also configured with the <code>remote_ip=flow</code> option46</dl>
</dl>
<dd>The tunnel destination IP address for any packet received from a tunnel is available in the <code>tun_dst</code> field for matching in the flow table46</p>
<dt><code>options : in_key</code>: optional string</p>
<dd>Optional46 The key that received packets must contain, one of:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>0</code>46 The tunnel receives packets with no key or with a key of 046 This is equivalent to specifying no <code>options:in_key</code> at all46</p>
<dt>&bull;</p>
<dd>A positive 24-bit (for Geneve, VXLAN, and LISP), 32-bit (for GRE) or 64-bit (for STT) number46 The tunnel receives only packets with the specified key46</p>
<dt>&bull;</p>
<dd>The word <code>flow</code>46 The tunnel accepts packets with any key46 The key will be placed in the <code>tun_id</code> field for matching in the flow table46 The <code>ovs-ofctl</code> manual page contains additional information about matching fields in OpenFlow flows46</dl>
</dl>
<dd>
<dt><code>options : out_key</code>: optional string</p>
<dd>Optional46 The key to be set on outgoing packets, one of:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>0</code>46 Packets sent through the tunnel will have no key46 This is equivalent to specifying no <code>options:out_key</code> at all46</p>
<dt>&bull;</p>
<dd>A positive 24-bit (for Geneve, VXLAN and LISP), 32-bit (for GRE) or 64-bit (for STT) number46 Packets sent through the tunnel will have the specified key46</p>
<dt>&bull;</p>
<dd>The word <code>flow</code>46 Packets sent through the tunnel will have the key set using the <code>set_tunnel</code> Nicira OpenFlow vendor extension (0 is used in the absence of an action)46 The <code>ovs-ofctl</code> manual page contains additional information about the Nicira OpenFlow vendor extensions46</dl>
</dl>
<dt><code>options : key</code>: optional string</p>
<dd>Optional46 Shorthand to set <code>in_key</code> and <code>out_key</code> at the same time46</p>
<dt><code>options : tos</code>: optional string</p>
<dd>Optional46 The value of the ToS bits to be set on the encapsulating packet46 ToS is interpreted as DSCP and ECN bits, ECN part must be zero46 It may also be the word <code>inherit</code>, in which case the ToS will be copied from the inner packet if it is IPv4 or IPv6 (otherwise it will be 0)46 The ECN fields are always inherited46 Default is 046</p>
<dt><code>options : ttl</code>: optional string</p>
<dd>Optional46 The TTL to be set on the encapsulating packet46 It may also be the word <code>inherit</code>, in which case the TTL will be copied from the inner packet if it is IPv4 or IPv6 (otherwise it will be the system default, typically 64)46 Default is the system default TTL46</p>
<dt><code>options : df_default</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Optional46 If enabled, the Don&#8217;t Fragment bit will be set on tunnel outer headers to allow path MTU discovery46 Default is enabled; set to <code>false</code> to disable46</dl>
<p> <i>Tunnel Options: vxlan only:</i></p>
<dl>
<dt><code>options : exts</code>: optional string</p>
<dd>Optional46 Comma separated list of optional VXLAN extensions to enable46 The following extensions are supported:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><code>gbp</code>: VXLAN-GBP allows to transport the group policy context of a packet across the VXLAN tunnel to other network peers46 See the field description of <code>tun_gbp_id</code> and <code>tun_gbp_flags</code> in <a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a>(8) for additional information46 (<code><a rel="nofollow" href="https://tools46ietf46org/html/draft-smith-vxlan-group-policy">https://tools46ietf46org/html/draft-smith-vxlan-group-policy</a></code>)</dl>
</dl>
</dl>
<p> <i>Tunnel Options: gre, ipsec_gre, geneve, and vxlan:</i> <code>gre</code>, <code>ipsec_gre</code>, <code>geneve</code>, and <code>vxlan</code> interfaces support these options46</p>
<dl>
<dt><code>options : csum</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Optional46 Compute encapsulation header (either GRE or UDP) checksums on outgoing packets46 Default is disabled, set to <code>true</code> to enable46 Checksums present on incoming packets will be validated regardless of this setting46</p>
<dd>When using the upstream Linux kernel module, computation of checksums for <code>geneve</code> and <code>vxlan</code> requires Linux kernel version 4460 or higher46 <code>gre</code> supports checksums for all versions of Open vSwitch that support GRE46 The out of tree kernel module distributed as part of OVS can compute all tunnel checksums on any kernel version that it is compatible with46</p>
<dd>This option is supported for <code>ipsec_gre</code>, but not useful because GRE checksums are weaker than, and redundant with, IPsec payload authentication46</dl>
<p> <i>Tunnel Options: ipsec_gre only:</i> Only <code>ipsec_gre</code> interfaces support these options46</p>
<dl>
<dt><code>options : peer_cert</code>: optional string</p>
<dd>Required for certificate authentication46 A string containing the peer&#8217;s certificate in PEM format46 Additionally the host&#8217;s certificate must be specified with the <code>certificate</code> option46</p>
<dt><code>options : certificate</code>: optional string</p>
<dd>Required for certificate authentication46 The name of a PEM file containing a certificate that will be presented to the peer during authentication46</p>
<dt><code>options : private_key</code>: optional string</p>
<dd>Optional for certificate authentication46 The name of a PEM file containing the private key associated with <code>certificate</code>46 If <code>certificate</code> contains the private key, this option may be omitted46</p>
<dt><code>options : psk</code>: optional string</p>
<dd>Required for pre-shared key authentication46 Specifies a pre-shared key for authentication that must be identical on both sides of the tunnel46</dl>
<p> <i>Patch Options:</i> Only <code>patch</code> interfaces support these options46</p>
<dl>
<dt><code>options : peer</code>: optional string</p>
<dd>The <code>name</code> of the <code>Interface</code> for the other side of the patch46 The named <code>Interface</code>&#8216;s own <code>peer</code> option must specify this <code>Interface</code>&#8216;s name46 That is, the two patch interfaces must have reversed <code>name</code> and <code>peer</code> values46</dl>
<p> <i>Interface Status:</i> Status information about interfaces attached to bridges, updated every 5 seconds46 Not all interfaces have all of these properties; virtual interfaces don&#8217;t have a link speed, for example46 Non-applicable columns will have empty values46</p>
<dl>
<dt><code>admin_state</code>: optional string, either <code>down</code> or <code>up</code></p>
<dd>The administrative state of the physical network link46</p>
<dt><code>link_state</code>: optional string, either <code>down</code> or <code>up</code></p>
<dd>The observed state of the physical network link46 This is ordinarily the link&#8217;s carrier status46 If the interface&#8217;s <code>Port</code> is a bond configured for miimon monitoring, it is instead the network link&#8217;s miimon status46</p>
<dt><code>link_resets</code>: optional integer</p>
<dd>The number of times Open vSwitch has observed the <code>link_state</code> of this <code>Interface</code> change46</p>
<dt><code>link_speed</code>: optional integer</p>
<dd>The negotiated speed of the physical network link46 Valid values are positive integers greater than 046</p>
<dt><code>duplex</code>: optional string, either <code>full</code> or <code>half</code></p>
<dd>The duplex mode of the physical network link46</p>
<dt><code>mtu</code>: optional integer</p>
<dd>The MTU (maximum transmission unit); i46e46 the largest amount of data that can fit into a single Ethernet frame46 The standard Ethernet MTU is 1500 bytes46 Some physical media and many kinds of virtual interfaces can be configured with higher MTUs46</p>
<dd>This column will be empty for an interface that does not have an MTU as, for example, some kinds of tunnels do not46</p>
<dt><code>lacp_current</code>: optional boolean</p>
<dd>Boolean value indicating LACP status for this interface46 If true, this interface has current LACP information about its LACP partner46 This information may be used to monitor the health of interfaces in a LACP enabled port46 This column will be empty if LACP is not enabled46</p>
<dt><code>status</code>: map of string-string pairs</p>
<dd>Key-value pairs that report port status46 Supported status values are <code>type</code>-dependent; some interfaces may not have a valid <code>status:driver_name</code>, for example46</p>
<dt><code>status : driver_name</code>: optional string</p>
<dd>The name of the device driver controlling the network adapter46</p>
<dt><code>status : driver_version</code>: optional string</p>
<dd>The version string of the device driver controlling the network adapter46</p>
<dt><code>status : firmware_version</code>: optional string</p>
<dd>The version string of the network adapter&#8217;s firmware, if available46</p>
<dt><code>status : source_ip</code>: optional string</p>
<dd>The source IP address used for an IPv4 tunnel end-point, such as <code>gre</code>46</p>
<dt><code>status : tunnel_egress_iface</code>: optional string</p>
<dd>Egress interface for tunnels46 Currently only relevant for tunnels on Linux systems, this column will show the name of the interface which is responsible for routing traffic destined for the configured <code>options:remote_ip</code>46 This could be an internal interface such as a bridge port46</p>
<dt><code>status : tunnel_egress_iface_carrier</code>: optional string, either <code>down</code> or <code>up</code></p>
<dd>Whether carrier is detected on <code>status:tunnel_egress_iface</code>46</dl>
<p> <i>Statistics:</i> Key-value pairs that report interface statistics46 The current implementation updates these counters periodically46 The update period is controlled by <code>other_config:stats-update-interval</code> in the <code>Open_vSwitch</code> table46 Future implementations may update them when an interface is created, when they are queried (e46g46 using an OVSDB <code>select</code> operation), and just before an interface is deleted due to virtual interface hot-unplug or VM shutdown, and perhaps at other times, but not on any regular periodic basis46 </p>
<p> These are the same statistics reported by OpenFlow in its <code>struct ofp_port_stats</code> structure46 If an interface does not support a given statistic, then that pair is omitted46 </p>
<p> <i>Statistics: Successful transmit and receive counters:</i></p>
<dl>
<dt><code>statistics : rx_packets</code>: optional integer</p>
<dd>Number of received packets46</p>
<dt><code>statistics : rx_bytes</code>: optional integer</p>
<dd>Number of received bytes46</p>
<dt><code>statistics : tx_packets</code>: optional integer</p>
<dd>Number of transmitted packets46</p>
<dt><code>statistics : tx_bytes</code>: optional integer</p>
<dd>Number of transmitted bytes46</dl>
<p> <i>Statistics: Receive errors:</i></p>
<dl>
<dt><code>statistics : rx_dropped</code>: optional integer</p>
<dd>Number of packets dropped by RX46</p>
<dt><code>statistics : rx_frame_err</code>: optional integer</p>
<dd>Number of frame alignment errors46</p>
<dt><code>statistics : rx_over_err</code>: optional integer</p>
<dd>Number of packets with RX overrun46</p>
<dt><code>statistics : rx_crc_err</code>: optional integer</p>
<dd>Number of CRC errors46</p>
<dt><code>statistics : rx_errors</code>: optional integer</p>
<dd>Total number of receive errors, greater than or equal to the sum of the above46</dl>
<p> <i>Statistics: Transmit errors:</i></p>
<dl>
<dt><code>statistics : tx_dropped</code>: optional integer</p>
<dd>Number of packets dropped by TX46</p>
<dt><code>statistics : collisions</code>: optional integer</p>
<dd>Number of collisions46</p>
<dt><code>statistics : tx_errors</code>: optional integer</p>
<dd>Total number of transmit errors, greater than or equal to the sum of the above46</dl>
<p> <i>Ingress Policing:</i> These settings control ingress policing for packets received on this interface46 On a physical interface, this limits the rate at which traffic is allowed into the system from the outside; on a virtual interface (one connected to a virtual machine), this limits the rate at which the VM is able to transmit46 </p>
<p> Policing is a simple form of quality-of-service that simply drops packets received in excess of the configured rate46 Due to its simplicity, policing is usually less accurate and less effective than egress QoS (which is configured using the <code>QoS</code> and <code>Queue</code> tables)46 </p>
<p> Policing is currently implemented only on Linux46 The Linux implementation uses a simple &#8220;token bucket&#8221; approach:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>The size of the bucket corresponds to <code>ingress_policing_burst</code>46 Initially the bucket is full46</p>
<dt>&bull;</p>
<dd>Whenever a packet is received, its size (converted to tokens) is compared to the number of tokens currently in the bucket46 If the required number of tokens are available, they are removed and the packet is forwarded46 Otherwise, the packet is dropped46</p>
<dt>&bull;</p>
<dd>Whenever it is not full, the bucket is refilled with tokens at the rate specified by <code>ingress_policing_rate</code>46</dl>
</dl>
<p> Policing interacts badly with some network protocols, and especially with fragmented IP packets46 Suppose that there is enough network activity to keep the bucket nearly empty all the time46 Then this token bucket algorithm will forward a single packet every so often, with the period depending on packet size and on the configured rate46 All of the fragments of an IP packets are normally transmitted back-to-back, as a group46 In such a situation, therefore, only one of these fragments will be forwarded and the rest will be dropped46 IP does not provide any way for the intended recipient to ask for only the remaining fragments46 In such a case there are two likely possibilities for what will happen next: either all of the fragments will eventually be retransmitted (as TCP will do), in which case the same problem will recur, or the sender will not realize that its packet has been dropped and data will simply be lost (as some UDP-based protocols will do)46 Either way, it is possible that no forward progress will ever occur46</p>
<dl>
<dt><code>ingress_policing_rate</code>: integer, at least 0</p>
<dd>Maximum rate for data received on this interface, in kbps46 Data received faster than this rate is dropped46 Set to <code>0</code> (the default) to disable policing46</p>
<dt><code>ingress_policing_burst</code>: integer, at least 0</p>
<dd>Maximum burst size for data received on this interface, in kb46 The default burst size if set to <code>0</code> is 1000 kb46 This value has no effect if <code>ingress_policing_rate</code> is <code>0</code>46</p>
<dd>Specifying a larger burst size lets the algorithm be more forgiving, which is important for protocols like TCP that react severely to dropped packets46 The burst size should be at least the size of the interface&#8217;s MTU46 Specifying a value that is numerically at least as large as 10% of <code>ingress_policing_rate</code> helps TCP come closer to achieving the full rate46</dl>
<p> <i>Bidirectional Forwarding Detection (BFD):</i> BFD, defined in RFC 5880 and RFC 5881, allows point-to-point detection of connectivity failures by occasional transmission of BFD control messages46 Open vSwitch implements BFD to serve as a more popular and standards compliant alternative to CFM46 </p>
<p> BFD operates by regularly transmitting BFD control messages at a rate negotiated independently in each direction46 Each endpoint specifies the rate at which it expects to receive control messages, and the rate at which it is willing to transmit them46 Open vSwitch uses a detection multiplier of three, meaning that an endpoint signals a connectivity fault if three consecutive BFD control messages fail to arrive46 In the case of a unidirectional connectivity issue, the system not receiving BFD control messages signals the problem to its peer in the messages it transmits46 </p>
<p> The Open vSwitch implementation of BFD aims to comply faithfully with RFC 5880 requirements46 Open vSwitch does not implement the optional Authentication or &#8220;Echo Mode&#8221; features46 </p>
<p> <i>BFD Configuration:</i> A controller sets up key-value pairs in the <code>bfd</code> column to enable and configure BFD46</p>
<dl>
<dt><code>bfd : enable</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>True to enable BFD on this <code>Interface</code>46 If not specified, BFD will not be enabled by default46</p>
<dt><code>bfd : min_rx</code>: optional string, containing an integer, at least 1</p>
<dd>The shortest interval, in milliseconds, at which this BFD session offers to receive BFD control messages46 The remote endpoint may choose to send messages at a slower rate46 Defaults to <code>1000</code>46</p>
<dt><code>bfd : min_tx</code>: optional string, containing an integer, at least 1</p>
<dd>The shortest interval, in milliseconds, at which this BFD session is willing to transmit BFD control messages46 Messages will actually be transmitted at a slower rate if the remote endpoint is not willing to receive as quickly as specified46 Defaults to <code>100</code>46</p>
<dt><code>bfd : decay_min_rx</code>: optional string, containing an integer</p>
<dd>An alternate receive interval, in milliseconds, that must be greater than or equal to <code>bfd:min_rx</code>46 The implementation switches from <code>bfd:min_rx</code> to <code>bfd:decay_min_rx</code> when there is no obvious incoming data traffic at the interface, to reduce the CPU and bandwidth cost of monitoring an idle interface46 This feature may be disabled by setting a value of 046 This feature is reset whenever <code>bfd:decay_min_rx</code> or <code>bfd:min_rx</code> changes46</p>
<dt><code>bfd : forwarding_if_rx</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>When <code>true</code>, traffic received on the <code>Interface</code> is used to indicate the capability of packet I/O46 BFD control packets are still transmitted and received46 At least one BFD control packet must be received every 100 * <code>bfd:min_rx</code> amount of time46 Otherwise, even if traffic are received, the <code>bfd:forwarding</code> will be <code>false</code>46</p>
<dt><code>bfd : cpath_down</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Set to true to notify the remote endpoint that traffic should not be forwarded to this system for some reason other than a connectivty failure on the interface being monitored46 The typical underlying reason is &#8220;concatenated path down,&#8221; that is, that connectivity beyond the local system is down46 Defaults to false46</p>
<dt><code>bfd : check_tnl_key</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Set to true to make BFD accept only control messages with a tunnel key of zero46 By default, BFD accepts control messages with any tunnel key46</p>
<dt><code>bfd : bfd_local_src_mac</code>: optional string</p>
<dd>Set to an Ethernet address in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i> to set the MAC used as source for transmitted BFD packets46 The default is the mac address of the BFD enabled interface46</p>
<dt><code>bfd : bfd_local_dst_mac</code>: optional string</p>
<dd>Set to an Ethernet address in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i> to set the MAC used as destination for transmitted BFD packets46 The default is <code>00:23:20:00:00:01</code>46</p>
<dt><code>bfd : bfd_remote_dst_mac</code>: optional string</p>
<dd>Set to an Ethernet address in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i> to set the MAC used for checking the destination of received BFD packets46 Packets with different destination MAC will not be considered as BFD packets46 If not specified the destination MAC address of received BFD packets are not checked46</p>
<dt><code>bfd : bfd_src_ip</code>: optional string</p>
<dd>Set to an IPv4 address to set the IP address used as source for transmitted BFD packets46 The default is <code>16946254461461</code>46</p>
<dt><code>bfd : bfd_dst_ip</code>: optional string</p>
<dd>Set to an IPv4 address to set the IP address used as destination for transmitted BFD packets46 The default is <code>16946254461460</code>46</dl>
<p> <i>BFD Status:</i> The switch sets key-value pairs in the <code>bfd_status</code> column to report the status of BFD on this interface46 When BFD is not enabled, with <code>bfd:enable</code>, the switch clears all key-value pairs from <code>bfd_status</code>46</p>
<dl>
<dt><code>bfd_status : state</code>: optional string, one of <code>down</code>, <code>init</code>, <code>up</code>, or <code>admin_down</code></p>
<dd>Reports the state of the BFD session46 The BFD session is fully healthy and negotiated if <code>UP</code>46</p>
<dt><code>bfd_status : forwarding</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Reports whether the BFD session believes this <code>Interface</code> may be used to forward traffic46 Typically this means the local session is signaling <code>UP</code>, and the remote system isn&#8217;t signaling a problem such as concatenated path down46</p>
<dt><code>bfd_status : diagnostic</code>: optional string</p>
<dd>A diagnostic code specifying the local system&#8217;s reason for the last change in session state46 The error messages are defined in section 4461 of [RFC 5880]46</p>
<dt><code>bfd_status : remote_state</code>: optional string, one of <code>down</code>, <code>init</code>, <code>up</code>, or <code>admin_down</code></p>
<dd>Reports the state of the remote endpoint&#8217;s BFD session46</p>
<dt><code>bfd_status : remote_diagnostic</code>: optional string</p>
<dd>A diagnostic code specifying the remote system&#8217;s reason for the last change in session state46 The error messages are defined in section 4461 of [RFC 5880]46</p>
<dt><code>bfd_status : flap_count</code>: optional string, containing an integer, at least 0</p>
<dd>Counts the number of <code>bfd_status:forwarding</code> flaps since start46 A flap is considered as a change of the <code>bfd_status:forwarding</code> value46</dl>
<p> <i>Connectivity Fault Management:</i> 802461ag Connectivity Fault Management (CFM) allows a group of Maintenance Points (MPs) called a Maintenance Association (MA) to detect connectivity problems with each other46 MPs within a MA should have complete and exclusive interconnectivity46 This is verified by occasionally broadcasting Continuity Check Messages (CCMs) at a configurable transmission interval46 </p>
<p> According to the 802461ag specification, each Maintenance Point should be configured out-of-band with a list of Remote Maintenance Points it should have connectivity to46 Open vSwitch differs from the specification in this area46 It simply assumes the link is faulted if no Remote Maintenance Points are reachable, and considers it not faulted otherwise46 </p>
<p> When operating over tunnels which have no <code>in_key</code>, or an <code>in_key</code> of <code>flow</code>46 CFM will only accept CCMs with a tunnel key of zero46</p>
<dl>
<dt><code>cfm_mpid</code>: optional integer</p>
<dd>A Maintenance Point ID (MPID) uniquely identifies each endpoint within a Maintenance Association46 The MPID is used to identify this endpoint to other Maintenance Points in the MA46 Each end of a link being monitored should have a different MPID46 Must be configured to enable CFM on this <code>Interface</code>46</p>
<dd>According to the 802461ag specification, MPIDs can only range between [1, 8191]46 However, extended mode (see <code>other_config:cfm_extended</code>) supports eight byte MPIDs46</p>
<dt><code>cfm_flap_count</code>: optional integer</p>
<dd>Counts the number of cfm fault flapps since boot46 A flap is considered to be a change of the <code>cfm_fault</code> value46</p>
<dt><code>cfm_fault</code>: optional boolean</p>
<dd>Indicates a connectivity fault triggered by an inability to receive heartbeats from any remote endpoint46 When a fault is triggered on <code>Interface</code>s participating in bonds, they will be disabled46</p>
<dd>Faults can be triggered for several reasons46 Most importantly they are triggered when no CCMs are received for a period of 3465 times the transmission interval46 Faults are also triggered when any CCMs indicate that a Remote Maintenance Point is not receiving CCMs but able to send them46 Finally, a fault is triggered if a CCM is received which indicates unexpected configuration46 Notably, this case arises when a CCM is received which advertises the local MPID46</p>
<dt><code>cfm_fault_status : recv</code>: none</p>
<dd>Indicates a CFM fault was triggered due to a lack of CCMs received on the <code>Interface</code>46</p>
<dt><code>cfm_fault_status : rdi</code>: none</p>
<dd>Indicates a CFM fault was triggered due to the reception of a CCM with the RDI bit flagged46 Endpoints set the RDI bit in their CCMs when they are not receiving CCMs themselves46 This typically indicates a unidirectional connectivity failure46</p>
<dt><code>cfm_fault_status : maid</code>: none</p>
<dd>Indicates a CFM fault was triggered due to the reception of a CCM with a MAID other than the one Open vSwitch uses46 CFM broadcasts are tagged with an identification number in addition to the MPID called the MAID46 Open vSwitch only supports receiving CCM broadcasts tagged with the MAID it uses internally46</p>
<dt><code>cfm_fault_status : loopback</code>: none</p>
<dd>Indicates a CFM fault was triggered due to the reception of a CCM advertising the same MPID configured in the <code>cfm_mpid</code> column of this <code>Interface</code>46 This may indicate a loop in the network46</p>
<dt><code>cfm_fault_status : overflow</code>: none</p>
<dd>Indicates a CFM fault was triggered because the CFM module received CCMs from more remote endpoints than it can keep track of46</p>
<dt><code>cfm_fault_status : override</code>: none</p>
<dd>Indicates a CFM fault was manually triggered by an administrator using an <code>ovs-appctl</code> command46</p>
<dt><code>cfm_fault_status : interval</code>: none</p>
<dd>Indicates a CFM fault was triggered due to the reception of a CCM frame having an invalid interval46</p>
<dt><code>cfm_remote_opstate</code>: optional string, either <code>down</code> or <code>up</code></p>
<dd>When in extended mode, indicates the operational state of the remote endpoint as either <code>up</code> or <code>down</code>46 See <code>other_config:cfm_opstate</code>46</p>
<dt><code>cfm_health</code>: optional integer, in range 0 to 100</p>
<dd>Indicates the health of the interface as a percentage of CCM frames received over 21 <code>other_config:cfm_interval</code>s46 The health of an interface is undefined if it is communicating with more than one <code>cfm_remote_mpids</code>46 It reduces if healthy heartbeats are not received at the expected rate, and gradually improves as healthy heartbeats are received at the desired rate46 Every 21 <code>other_config:cfm_interval</code>s, the health of the interface is refreshed46</p>
<dd>As mentioned above, the faults can be triggered for several reasons46 The link health will deteriorate even if heartbeats are received but they are reported to be unhealthy46 An unhealthy heartbeat in this context is a heartbeat for which either some fault is set or is out of sequence46 The interface health can be 100 only on receiving healthy heartbeats at the desired rate46</p>
<dt><code>cfm_remote_mpids</code>: set of integers</p>
<dd>When CFM is properly configured, Open vSwitch will occasionally receive CCM broadcasts46 These broadcasts contain the MPID of the sending Maintenance Point46 The list of MPIDs from which this <code>Interface</code> is receiving broadcasts from is regularly collected and written to this column46</p>
<dt><code>other_config : cfm_interval</code>: optional string, containing an integer</p>
<dd>The interval, in milliseconds, between transmissions of CFM heartbeats46 Three missed heartbeat receptions indicate a connectivity fault46</p>
<dd>In standard operation only intervals of 3, 10, 100, 1,000, 10,000, 60,000, or 600,000 ms are supported46 Other values will be rounded down to the nearest value on the list46 Extended mode (see <code>other_config:cfm_extended</code>) supports any interval up to 65,535 ms46 In either mode, the default is 1000 ms46</p>
<dd>We do not recommend using intervals less than 100 ms46</p>
<dt><code>other_config : cfm_extended</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>When <code>true</code>, the CFM module operates in extended mode46 This causes it to use a nonstandard destination address to avoid conflicting with compliant implementations which may be running concurrently on the network46 Furthermore, extended mode increases the accuracy of the <code>cfm_interval</code> configuration parameter by breaking wire compatibility with 802461ag compliant implementations46 And extended mode allows eight byte MPIDs46 Defaults to <code>false</code>46</p>
<dt><code>other_config : cfm_demand</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>When <code>true</code>, and <code>other_config:cfm_extended</code> is true, the CFM module operates in demand mode46 When in demand mode, traffic received on the <code>Interface</code> is used to indicate liveness46 CCMs are still transmitted and received46 At least one CCM must be received every 100 * <code>other_config:cfm_interval</code> amount of time46 Otherwise, even if traffic are received, the CFM module will raise the connectivity fault46</p>
<dd>Demand mode has a couple of caveats:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>To ensure that ovs-vswitchd has enough time to pull statistics from the datapath, the fault detection interval is set to 3465 * MAX(<code>other_config:cfm_interval</code>, 500) ms46</p>
<dt>&bull;</p>
<dd>To avoid ambiguity, demand mode disables itself when there are multiple remote maintenance points46</p>
<dt>&bull;</p>
<dd>If the <code>Interface</code> is heavily congested, CCMs containing the <code>other_config:cfm_opstate</code> status may be dropped causing changes in the operational state to be delayed46 Similarly, if CCMs containing the RDI bit are not received, unidirectional link failures may not be detected46</dl>
</dl>
<dt><code>other_config : cfm_opstate</code>: optional string, either <code>down</code> or <code>up</code></p>
<dd>When <code>down</code>, the CFM module marks all CCMs it generates as operationally down without triggering a fault46 This allows remote maintenance points to choose not to forward traffic to the <code>Interface</code> on which this CFM module is running46 Currently, in Open vSwitch, the opdown bit of CCMs affects <code>Interface</code>s participating in bonds, and the bundle OpenFlow action46 This setting is ignored when CFM is not in extended mode46 Defaults to <code>up</code>46</p>
<dt><code>other_config : cfm_ccm_vlan</code>: optional string, containing an integer, in range 1 to 4,095</p>
<dd>When set, the CFM module will apply a VLAN tag to all CCMs it generates with the given value46 May be the string <code>random</code> in which case each CCM will be tagged with a different randomly generated VLAN46</p>
<dt><code>other_config : cfm_ccm_pcp</code>: optional string, containing an integer, in range 1 to 7</p>
<dd>When set, the CFM module will apply a VLAN tag to all CCMs it generates with the given PCP value, the VLAN ID of the tag is governed by the value of <code>other_config:cfm_ccm_vlan</code>46 If <code>other_config:cfm_ccm_vlan</code> is unset, a VLAN ID of zero is used46</dl>
<p> <i>Bonding Configuration:</i></p>
<dl>
<dt><code>other_config : lacp-port-id</code>: optional string, containing an integer, in range 1 to 65,535</p>
<dd>The LACP port ID of this <code>Interface</code>46 Port IDs are used in LACP negotiations to identify individual ports participating in a bond46</p>
<dt><code>other_config : lacp-port-priority</code>: optional string, containing an integer, in range 1 to 65,535</p>
<dd>The LACP port priority of this <code>Interface</code>46 In LACP negotiations <code>Interface</code>s with numerically lower priorities are preferred for aggregation46</p>
<dt><code>other_config : lacp-aggregation-key</code>: optional string, containing an integer, in range 1 to 65,535</p>
<dd>The LACP aggregation key of this <code>Interface</code>46 <code>Interface</code>s with different aggregation keys may not be active within a given <code>Port</code> at the same time46</dl>
<p> <i>Virtual Machine Identifiers:</i> These key-value pairs specifically apply to an interface that represents a virtual Ethernet interface connected to a virtual machine46 These key-value pairs should not be present for other types of interfaces46 Keys whose names end in <code>-uuid</code> have values that uniquely identify the entity in question46 For a Citrix XenServer hypervisor, these values are UUIDs in RFC 4122 format46 Other hypervisors may use other formats46</p>
<dl>
<dt><code>external_ids : attached-mac</code>: optional string</p>
<dd>The MAC address programmed into the &#8220;virtual hardware&#8221; for this interface, in the form <i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>:<i>xx</i>46 For Citrix XenServer, this is the value of the <code>MAC</code> field in the VIF record for this interface46</p>
<dt><code>external_ids : iface-id</code>: optional string</p>
<dd>A system-unique identifier for the interface46 On XenServer, this will commonly be the same as <code>external_ids:xs-vif-uuid</code>46</p>
<dt><code>external_ids : iface-status</code>: optional string, either <code>active</code> or <code>inactive</code></p>
<dd>Hypervisors may sometimes have more than one interface associated with a given <code>external_ids:iface-id</code>, only one of which is actually in use at a given time46 For example, in some circumstances XenServer has both a &#8220;tap&#8221; and a &#8220;vif&#8221; interface for a single <code>external_ids:iface-id</code>, but only uses one of them at a time46 A hypervisor that behaves this way must mark the currently in use interface <code>active</code> and the others <code>inactive</code>46 A hypervisor that never has more than one interface for a given <code>external_ids:iface-id</code> may mark that interface <code>active</code> or omit <code>external_ids:iface-status</code> entirely46</p>
<dd>During VM migration, a given <code>external_ids:iface-id</code> might transiently be marked <code>active</code> on two different hypervisors46 That is, <code>active</code> means that this <code>external_ids:iface-id</code> is the active instance within a single hypervisor, not in a broader scope46 There is one exception: some hypervisors support &#8220;migration&#8221; from a given hypervisor to itself (most often for test purposes)46 During such a &#8220;migration,&#8221; two instances of a single <code>external_ids:iface-id</code> might both be briefly marked <code>active</code> on a single hypervisor46</p>
<dt><code>external_ids : xs-vif-uuid</code>: optional string</p>
<dd>The virtual interface associated with this interface46</p>
<dt><code>external_ids : xs-network-uuid</code>: optional string</p>
<dd>The virtual network to which this interface is attached46</p>
<dt><code>external_ids : vm-id</code>: optional string</p>
<dd>The VM to which this interface belongs46 On XenServer, this will be the same as <code>external_ids:xs-vm-uuid</code>46</p>
<dt><code>external_ids : xs-vm-uuid</code>: optional string</p>
<dd>The VM to which this interface belongs46</dl>
<p> <i>VLAN Splinters:</i> The &#8220;VLAN splinters&#8221; feature increases Open vSwitch compatibility with buggy network drivers in old versions of Linux that do not properly support VLANs when VLAN devices are not used, at some cost in memory and performance46 </p>
<p> When VLAN splinters are enabled on a particular interface, Open vSwitch creates a VLAN device for each in-use VLAN46 For sending traffic tagged with a VLAN on the interface, it substitutes the VLAN device46 Traffic received on the VLAN device is treated as if it had been received on the interface on the particular VLAN46 </p>
<p> VLAN splinters consider a VLAN to be in use if:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>The VLAN is the <code>tag</code> value in any <code>Port</code> record46</p>
<dt>&bull;</p>
<dd>The VLAN is listed within the <code>trunks</code> column of the <code>Port</code> record of an interface on which VLAN splinters are enabled46 An empty <code>trunks</code> does not influence the in-use VLANs: creating 4,096 VLAN devices is impractical because it will exceed the current 1,024 port per datapath limit46</p>
<dt>&bull;</p>
<dd>An OpenFlow flow within any bridge matches the VLAN46</dl>
</dl>
<p> The same set of in-use VLANs applies to every interface on which VLAN splinters are enabled46 That is, the set is not chosen separately for each interface but selected once as the union of all in-use VLANs based on the rules above46 </p>
<p> It does not make sense to enable VLAN splinters on an interface for an access port, or on an interface that is not a physical port46 </p>
<p> VLAN splinters are deprecated46 When broken device drivers are no longer in widespread use, we will delete this feature46</p>
<dl>
<dt><code>other_config : enable-vlan-splinters</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Set to <code>true</code> to enable VLAN splinters on this interface46 Defaults to <code>false</code>46</p>
<dd>VLAN splinters increase kernel and userspace memory overhead, so do not use them unless they are needed46</p>
<dd>VLAN splinters do not support 802461p priority tags46 Received priorities will appear to be 0, regardless of their actual values, and priorities on transmitted packets will also be cleared to 046</dl>
<p> <i>Auto Attach Configuration:</i> Auto Attach configuration for a particular interface46</p>
<dl>
<dt><code>lldp : enable</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>True to enable LLDP on this <code>Interface</code>46 If not specified, LLDP will be disabled by default46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Flow_Table TABLE</h2>
<p>Configuration for a particular OpenFlow table46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>name</code></p>
<dd>optional string </p>
<dt> <i>Eviction Policy:</i></p>
<dl>
<dd>
<dl>
<dt> <code>flow_limit</code></p>
<dd>optional integer, at least 0 </p>
<dt> <code>overflow_policy</code></p>
<dd>optional string, either <code>refuse</code> or <code>evict</code> </p>
<dt> <code>groups</code></p>
<dd>set of strings</dl>
</dl>
<dt> <i>Classifier Optimization:</i></p>
<dl>
<dd>
<dl>
<dt> <code>prefixes</code></p>
<dd>set of up to 3 strings</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>name</code>: optional string</p>
<dd>The table&#8217;s name46 Set this column to change the name that controllers will receive when they request table statistics, e46g46 <code>ovs-ofctl dump-tables</code>46 The name does not affect switch behavior46</dl>
<p> <i>Eviction Policy:</i> Open vSwitch supports limiting the number of flows that may be installed in a flow table, via the <code>flow_limit</code> column46 When adding a flow would exceed this limit, by default Open vSwitch reports an error, but there are two ways to configure Open vSwitch to instead delete (&#8220;evict&#8221;) a flow to make room for the new one:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Set the <code>overflow_policy</code> column to <code>evict</code>46</p>
<dt>&bull;</p>
<dd>Send an OpenFlow 1464+ &#8220;table mod request&#8221; to enable eviction for the flow table (e46g46 <code>ovs-ofctl -O OpenFlow14 mod-table br0 0 evict</code> to enable eviction on flow table 0 of bridge <code>br0</code>)46</dl>
</dl>
<p> When a flow must be evicted due to overflow, the flow to evict is chosen through an approximation of the following algorithm46 This algorithm is used regardless of how eviction was enabled:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Divide the flows in the table into groups based on the values of the fields or subfields specified in the <code>groups</code> column, so that all of the flows in a given group have the same values for those fields46 If a flow does not specify a given field, that field&#8217;s value is treated as 046 If <code>groups</code> is empty, then all of the flows in the flow table are treated as a single group46</p>
<dt>2.</p>
<dd>Consider the flows in the largest group, that is, the group that contains the greatest number of flows46 If two or more groups all have the same largest number of flows, consider the flows in all of those groups46</p>
<dt>3.</p>
<dd>If the flows under consideration have different importance values, eliminate from consideration any flows except those with the lowest importance46 (&#8220;Importance,&#8221; a 16-bit integer value attached to each flow, was introduced in OpenFlow 146446 Flows inserted with older versions of OpenFlow always have an importance of 046)</p>
<dt>4.</p>
<dd>Among the flows under consideration, choose the flow that expires soonest for eviction46</dl>
</dl>
<p> The eviction process only considers flows that have an idle timeout or a hard timeout46 That is, eviction never deletes permanent flows46 (Permanent flows do count against <code>flow_limit</code>46)</p>
<dl>
<dt><code>flow_limit</code>: optional integer, at least 0</p>
<dd>If set, limits the number of flows that may be added to the table46 Open vSwitch may limit the number of flows in a table for other reasons, e46g46 due to hardware limitations or for resource availability or performance reasons46</p>
<dt><code>overflow_policy</code>: optional string, either <code>refuse</code> or <code>evict</code></p>
<dd>Controls the switch&#8217;s behavior when an OpenFlow flow table modification request would add flows in excess of <code>flow_limit</code>46 The supported values are:</p>
<dl>
<dd>
<dl>
<dt><code>refuse</code></p>
<dd>Refuse to add the flow or flows46 This is also the default policy when <code>overflow_policy</code> is unset46</p>
<dt><code>evict</code></p>
<dd>Delete a flow chosen according to the algorithm described above46</dl>
</dl>
<dt><code>groups</code>: set of strings</p>
<dd>When <code>overflow_policy</code> is <code>evict</code>, this controls how flows are chosen for eviction when the flow table would otherwise exceed <code>flow_limit</code> flows46 Its value is a set of NXM fields or sub-fields, each of which takes one of the forms <i>field</i><code>[]</code> or <i>field</i><code>[</code><i>start</i><code>4646</code><i>end</i><code>]</code>, e46g46 <code>NXM_OF_IN_PORT[]</code>46 Please see <code>nicira-ext46h</code> for a complete list of NXM field names46</p>
<dd>Open vSwitch ignores any invalid or unknown field specifications46</p>
<dd>When eviction is not enabled, via <code>overflow_policy</code> or an OpenFlow 1464+ &#8220;table mod,&#8221; this column has no effect46</dl>
<p> <i>Classifier Optimization:</i></p>
<dl>
<dt><code>prefixes</code>: set of up to 3 strings</p>
<dd>This string set specifies which fields should be used for address prefix tracking46 Prefix tracking allows the classifier to skip rules with longer than necessary prefixes, resulting in better wildcarding for datapath flows46</p>
<dd>Prefix tracking may be beneficial when a flow table contains matches on IP address fields with different prefix lengths46 For example, when a flow table contains IP address matches on both full addresses and proper prefixes, the full address matches will typically cause the datapath flow to un-wildcard the whole address field (depending on flow entry priorities)46 In this case each packet with a different address gets handed to the userspace for flow processing and generates its own datapath flow46 With prefix tracking enabled for the address field in question packets with addresses matching shorter prefixes would generate datapath flows where the irrelevant address bits are wildcarded, allowing the same datapath flow to handle all the packets within the prefix in question46 In this case many userspace upcalls can be avoided and the overall performance can be better46</p>
<dd>This is a performance optimization only, so packets will receive the same treatment with or without prefix tracking46</p>
<dd>The supported fields are: <code>tun_id</code>, <code>tun_src</code>, <code>tun_dst</code>, <code>nw_src</code>, <code>nw_dst</code> (or aliases <code>ip_src</code> and <code>ip_dst</code>), <code>ipv6_src</code>, and <code>ipv6_dst</code>46 (Using this feature for <code>tun_id</code> would only make sense if the tunnel IDs have prefix structure similar to IP addresses46)</p>
<dd>By default, the <code>prefixes=ip_dst,ip_src</code> are used on each flow table46 This instructs the flow classifier to track the IP destination and source addresses used by the rules in this specific flow table46</p>
<dd>The keyword <code>none</code> is recognized as an explicit override of the default values, causing no prefix fields to be tracked46</p>
<dd>To set the prefix fields, the flow table record needs to exist:</p>
<dl>
<dd>
<dl>
<dt><code>ovs-vsctl set Bridge br0 flow_tables:0=@N1 &#8212; &#8211;id=@N1 create Flow_Table name=table0</code></p>
<dd>Creates a flow table record for the OpenFlow table number 046</p>
<dt><code>ovs-vsctl set Flow_Table table0 prefixes=ip_dst,ip_src</code></p>
<dd>Enables prefix tracking for IP source and destination address fields46</dl>
</dl>
<dd>There is a maximum number of fields that can be enabled for any one flow table46 Currently this limit is 346</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>QoS TABLE</h2>
<p>Quality of Service (QoS) configuration for each Port that references it46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>type</code></p>
<dd>string </p>
<dt> <code>queues</code></p>
<dd>map of integer-<code>Queue</code> pairs, key in range 0 to 4,294,967,295 </p>
<dt> <i>Configuration for linux-htb and linux-hfsc:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : max-rate</code></p>
<dd>optional string, containing an integer</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config</code></p>
<dd>map of string-string pairs </p>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>type</code>: string</p>
<dd>The type of QoS to implement46 The currently defined types are listed below:</p>
<dl>
<dd>
<dl>
<dt><code>linux-htb</code></p>
<dd>Linux &#8220;hierarchy token bucket&#8221; classifier46 See <a href="/docs/linux/man/8-tc-htb/">tc-htb</a>(8) (also at <code><a rel="nofollow" href="http://linux46die46net/man/8/tc-htb">http://linux46die46net/man/8/tc-htb</a></code>) and the HTB manual (<code><a rel="nofollow" href="http://luxik46cdi46cz/~devik/qos/htb/manual/userg46htm">http://luxik46cdi46cz/~devik/qos/htb/manual/userg46htm</a></code>) for information on how this classifier works and how to configure it46</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>linux-hfsc</code></p>
<dd>Linux &quot;Hierarchical Fair Service Curve&quot; classifier46 See <code><a rel="nofollow" href="http://linux-ip46net/articles/hfsc46en/">http://linux-ip46net/articles/hfsc46en/</a></code> for information on how this classifier works46</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>linux-sfq</code></p>
<dd>Linux &#8220;Stochastic Fairness Queueing&#8221; classifier46 See <code><a href="/docs/linux/man/8-tc-sfq/">tc-sfq</a></code>(8) (also at <code><a rel="nofollow" href="http://linux46die46net/man/8/tc-sfq">http://linux46die46net/man/8/tc-sfq</a></code>) for information on how this classifier works46</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>linux-codel</code></p>
<dd>Linux &#8220;Controlled Delay&#8221; classifier46 See <code><a href="/docs/linux/man/8-tc-codel/">tc-codel</a></code>(8) (also at <code><a rel="nofollow" href="http://man746org/linux/man-pages/man8/tc-codel46846html">http://man746org/linux/man-pages/man8/tc-codel46846html</a></code>) for information on how this classifier works46</dl>
</dl>
<dl>
<dd>
<dl>
<dt><code>linux-fq_codel</code></p>
<dd>Linux &#8220;Fair Queuing with Controlled Delay&#8221; classifier46 See <code><a href="/docs/linux/man/8-tc-fq_codel/">tc-fq_codel</a></code>(8) (also at <code><a rel="nofollow" href="http://man746org/linux/man-pages/man8/tc-fq_codel46846html">http://man746org/linux/man-pages/man8/tc-fq_codel46846html</a></code>) for information on how this classifier works46</dl>
</dl>
<dt><code>queues</code>: map of integer-<code>Queue</code> pairs, key in range 0 to 4,294,967,295</p>
<dd>A map from queue numbers to <code>Queue</code> records46 The supported range of queue numbers depend on <code>type</code>46 The queue numbers are the same as the <code>queue_id</code> used in OpenFlow in <code>struct ofp_action_enqueue</code> and other structures46</p>
<dd>Queue 0 is the &#8220;default queue46&#8221; It is used by OpenFlow output actions when no specific queue has been set46 When no configuration for queue 0 is present, it is automatically configured as if a <code>Queue</code> record with empty <code>dscp</code> and <code>other_config</code> columns had been specified46 (Before version 1466, Open vSwitch would leave queue 0 unconfigured in this case46 With some queuing disciplines, this dropped all packets destined for the default queue46)</dl>
<p> <i>Configuration for linux-htb and linux-hfsc:</i> The <code>linux-htb</code> and <code>linux-hfsc</code> classes support the following key-value pair:</p>
<dl>
<dt><code>other_config : max-rate</code>: optional string, containing an integer</p>
<dd>Maximum rate shared by all queued traffic, in bit/s46 Optional46 If not specified, for physical interfaces, the default is the link rate46 For other interfaces or if the link rate cannot be determined, the default is currently 100 Mbps46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Queue TABLE</h2>
<p>A configuration for a port output queue, used in configuring Quality of Service (QoS) features46 May be referenced by <code>queues</code> column in <code>QoS</code> table46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>dscp</code></p>
<dd>optional integer, in range 0 to 63 </p>
<dt> <i>Configuration for linux-htb QoS:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : min-rate</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : max-rate</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : burst</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : priority</code></p>
<dd>optional string, containing an integer, in range 0 to 4,294,967,295</dl>
</dl>
<dt> <i>Configuration for linux-hfsc QoS:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : min-rate</code></p>
<dd>optional string, containing an integer, at least 1 </p>
<dt> <code>other_config : max-rate</code></p>
<dd>optional string, containing an integer, at least 1</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config</code></p>
<dd>map of string-string pairs </p>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>dscp</code>: optional integer, in range 0 to 63</p>
<dd>If set, Open vSwitch will mark all traffic egressing this <code>Queue</code> with the given DSCP bits46 Traffic egressing the default <code>Queue</code> is only marked if it was explicitly selected as the <code>Queue</code> at the time the packet was output46 If unset, the DSCP bits of traffic egressing this <code>Queue</code> will remain unchanged46</dl>
<p> <i>Configuration for linux-htb QoS:</i> <code>QoS</code> <code>type</code> <code>linux-htb</code> may use <code>queue_id</code>s less than 6144046 It has the following key-value pairs defined46</p>
<dl>
<dt><code>other_config : min-rate</code>: optional string, containing an integer, at least 1</p>
<dd>Minimum guaranteed bandwidth, in bit/s46</p>
<dt><code>other_config : max-rate</code>: optional string, containing an integer, at least 1</p>
<dd>Maximum allowed bandwidth, in bit/s46 Optional46 If specified, the queue&#8217;s rate will not be allowed to exceed the specified value, even if excess bandwidth is available46 If unspecified, defaults to no limit46</p>
<dt><code>other_config : burst</code>: optional string, containing an integer, at least 1</p>
<dd>Burst size, in bits46 This is the maximum amount of &#8220;credits&#8221; that a queue can accumulate while it is idle46 Optional46 Details of the <code>linux-htb</code> implementation require a minimum burst size, so a too-small <code>burst</code> will be silently ignored46</p>
<dt><code>other_config : priority</code>: optional string, containing an integer, in range 0 to 4,294,967,295</p>
<dd>A queue with a smaller <code>priority</code> will receive all the excess bandwidth that it can use before a queue with a larger value receives any46 Specific priority values are unimportant; only relative ordering matters46 Defaults to 0 if unspecified46</dl>
<p> <i>Configuration for linux-hfsc QoS:</i> <code>QoS</code> <code>type</code> <code>linux-hfsc</code> may use <code>queue_id</code>s less than 6144046 It has the following key-value pairs defined46</p>
<dl>
<dt><code>other_config : min-rate</code>: optional string, containing an integer, at least 1</p>
<dd>Minimum guaranteed bandwidth, in bit/s46</p>
<dt><code>other_config : max-rate</code>: optional string, containing an integer, at least 1</p>
<dd>Maximum allowed bandwidth, in bit/s46 Optional46 If specified, the queue&#8217;s rate will not be allowed to exceed the specified value, even if excess bandwidth is available46 If unspecified, defaults to no limit46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Mirror TABLE</h2>
<p>A port mirror within a <code>Bridge</code>46 </p>
<p> A port mirror configures a bridge to send selected frames to special &#8220;mirrored&#8221; ports, in addition to their normal destinations46 Mirroring traffic may also be referred to as SPAN or RSPAN, depending on how the mirrored traffic is sent46 </p>
<p> When a packet enters an Open vSwitch bridge, it becomes eligible for mirroring based on its ingress port and VLAN46 As the packet travels through the flow tables, each time it is output to a port, it becomes eligible for mirroring based on the egress port and VLAN46 In Open vSwitch 2465 and later, mirroring occurs just after a packet first becomes eligible, using the packet as it exists at that point; in Open vSwitch 2464 and earlier, mirroring occurs only after a packet has traversed all the flow tables, using the original packet as it entered the bridge46 This makes a difference only when the flow table modifies the packet: in Open vSwitch 2464, the modifications are never visible to mirrors, whereas in Open vSwitch 2465 and later modifications made before the first output that makes it eligible for mirroring to a particular destination are visible46 </p>
<p> A packet that enters an Open vSwitch bridge is mirrored to a particular destination only once, even if it is eligible for multiple reasons46 For example, a packet would be mirrored to a particular <code>output_port</code> only once, even if it is selected for mirroring to that port by <code>select_dst_port</code> and <code>select_src_port</code> in the same or different <code>Mirror</code> records46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>name</code></p>
<dd>string </p>
<dt> <i>Selecting Packets for Mirroring:</i></p>
<dl>
<dd>
<dl>
<dt> <code>select_all</code></p>
<dd>boolean </p>
<dt> <code>select_dst_port</code></p>
<dd>set of weak reference to <code>Port</code>s </p>
<dt> <code>select_src_port</code></p>
<dd>set of weak reference to <code>Port</code>s </p>
<dt> <code>select_vlan</code></p>
<dd>set of up to 4,096 integers, in range 0 to 4,095</dl>
</dl>
<dt> <i>Mirroring Destination Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>output_port</code></p>
<dd>optional weak reference to <code>Port</code> </p>
<dt> <code>output_vlan</code></p>
<dd>optional integer, in range 1 to 4,095</dl>
</dl>
<dt> <i>Statistics: Mirror counters:</i></p>
<dl>
<dd>
<dl>
<dt> <code>statistics : tx_packets</code></p>
<dd>optional integer </p>
<dt> <code>statistics : tx_bytes</code></p>
<dd>optional integer</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>name</code>: string</p>
<dd>Arbitrary identifier for the <code>Mirror</code>46</dl>
<p> <i>Selecting Packets for Mirroring:</i> To be selected for mirroring, a given packet must enter or leave the bridge through a selected port and it must also be in one of the selected VLANs46</p>
<dl>
<dt><code>select_all</code>: boolean</p>
<dd>If true, every packet arriving or departing on any port is selected for mirroring46</p>
<dt><code>select_dst_port</code>: set of weak reference to <code>Port</code>s</p>
<dd>Ports on which departing packets are selected for mirroring46</p>
<dt><code>select_src_port</code>: set of weak reference to <code>Port</code>s</p>
<dd>Ports on which arriving packets are selected for mirroring46</p>
<dt><code>select_vlan</code>: set of up to 4,096 integers, in range 0 to 4,095</p>
<dd>VLANs on which packets are selected for mirroring46 An empty set selects packets on all VLANs46</dl>
<p> <i>Mirroring Destination Configuration:</i> These columns are mutually exclusive46 Exactly one of them must be nonempty46</p>
<dl>
<dt><code>output_port</code>: optional weak reference to <code>Port</code></p>
<dd>Output port for selected packets, if nonempty46</p>
<dd>Specifying a port for mirror output reserves that port exclusively for mirroring46 No frames other than those selected for mirroring via this column will be forwarded to the port, and any frames received on the port will be discarded46</p>
<dd>The output port may be any kind of port supported by Open vSwitch46 It may be, for example, a physical port (sometimes called SPAN) or a GRE tunnel46</p>
<dt><code>output_vlan</code>: optional integer, in range 1 to 4,095</p>
<dd>Output VLAN for selected packets, if nonempty46</p>
<dd>The frames will be sent out all ports that trunk <code>output_vlan</code>, as well as any ports with implicit VLAN <code>output_vlan</code>46 When a mirrored frame is sent out a trunk port, the frame&#8217;s VLAN tag will be set to <code>output_vlan</code>, replacing any existing tag; when it is sent out an implicit VLAN port, the frame will not be tagged46 This type of mirroring is sometimes called RSPAN46</p>
<dd>See the documentation for <code>other_config:forward-bpdu</code> in the <code>Interface</code> table for a list of destination MAC addresses which will not be mirrored to a VLAN to avoid confusing switches that interpret the protocols that they represent46</p>
<dd><code>Please note:</code> Mirroring to a VLAN can disrupt a network that contains unmanaged switches46 Consider an unmanaged physical switch with two ports: port 1, connected to an end host, and port 2, connected to an Open vSwitch configured to mirror received packets into VLAN 123 on port 246 Suppose that the end host sends a packet on port 1 that the physical switch forwards to port 246 The Open vSwitch forwards this packet to its destination and then reflects it back on port 2 in VLAN 12346 This reflected packet causes the unmanaged physical switch to replace the MAC learning table entry, which correctly pointed to port 1, with one that incorrectly points to port 246 Afterward, the physical switch will direct packets destined for the end host to the Open vSwitch on port 2, instead of to the end host on port 1, disrupting connectivity46 If mirroring to a VLAN is desired in this scenario, then the physical switch must be replaced by one that learns Ethernet addresses on a per-VLAN basis46 In addition, learning should be disabled on the VLAN containing mirrored traffic46 If this is not done then intermediate switches will learn the MAC address of each end host from the mirrored traffic46 If packets being sent to that end host are also mirrored, then they will be dropped since the switch will attempt to send them out the input port46 Disabling learning for the VLAN will cause the switch to correctly send the packet out all ports configured for that VLAN46 If Open vSwitch is being used as an intermediate switch, learning can be disabled by adding the mirrored VLAN to <code>flood_vlans</code> in the appropriate <code>Bridge</code> table or tables46</p>
<dd>Mirroring to a GRE tunnel has fewer caveats than mirroring to a VLAN and should generally be preferred46</dl>
<p> <i>Statistics: Mirror counters:</i> Key-value pairs that report mirror statistics46 The update period is controlled by <code>other_config:stats-update-interval</code> in the <code>Open_vSwitch</code> table46</p>
<dl>
<dt><code>statistics : tx_packets</code>: optional integer</p>
<dd>Number of packets transmitted through this mirror46</p>
<dt><code>statistics : tx_bytes</code>: optional integer</p>
<dd>Number of bytes transmitted through this mirror46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Controller TABLE</h2>
<p>An OpenFlow controller46 </p>
<p> Open vSwitch supports two kinds of OpenFlow controllers:</p>
<dl>
<dd>
<dl>
<dt>Primary controllers</p>
<dd>This is the kind of controller envisioned by the OpenFlow 1460 specification46 Usually, a primary controller implements a network policy by taking charge of the switch&#8217;s flow table46</p>
<dd>Open vSwitch initiates and maintains persistent connections to primary controllers, retrying the connection each time it fails or drops46 The <code>fail_mode</code> column in the <code>Bridge</code> table applies to primary controllers46</p>
<dd>Open vSwitch permits a bridge to have any number of primary controllers46 When multiple controllers are configured, Open vSwitch connects to all of them simultaneously46 Because OpenFlow 1460 does not specify how multiple controllers coordinate in interacting with a single switch, more than one primary controller should be specified only if the controllers are themselves designed to coordinate with each other46 (The Nicira-defined <code>NXT_ROLE</code> OpenFlow vendor extension may be useful for this46)</p>
<dt>Service controllers</p>
<dd>These kinds of OpenFlow controller connections are intended for occasional support and maintenance use, e46g46 with <code>ovs-ofctl</code>46 Usually a service controller connects only briefly to inspect or modify some of a switch&#8217;s state46</p>
<dd>Open vSwitch listens for incoming connections from service controllers46 The service controllers initiate and, if necessary, maintain the connections from their end46 The <code>fail_mode</code> column in the <code>Bridge</code> table does not apply to service controllers46</p>
<dd>Open vSwitch supports configuring any number of service controllers46</dl>
</dl>
<p> The <code>target</code> determines the type of controller46</p>
<h3>Summary:</h3>
<dl>
<dt> <i>Core Features:</i></p>
<dl>
<dd>
<dl>
<dt> <code>target</code></p>
<dd>string </p>
<dt> <code>connection_mode</code></p>
<dd>optional string, either <code>in-band</code> or <code>out-of-band</code></dl>
</dl>
<dt> <i>Controller Failure Detection and Handling:</i></p>
<dl>
<dd>
<dl>
<dt> <code>max_backoff</code></p>
<dd>optional integer, at least 1,000 </p>
<dt> <code>inactivity_probe</code></p>
<dd>optional integer</dl>
</dl>
<dt> <i>Asynchronous Messages:</i></p>
<dl>
<dd>
<dl>
<dt> <code>enable_async_messages</code></p>
<dd>optional boolean </p>
<dt> <i>Controller Rate Limiting:</i></p>
<dl>
<dd>
<dl>
<dt> <code>controller_rate_limit</code></p>
<dd>optional integer, at least 100 </p>
<dt> <code>controller_burst_limit</code></p>
<dd>optional integer, at least 25 </p>
<dt> <i>Controller Rate Limiting Statistics:</i></p>
<dl>
<dd>
<dl>
<dt> <code>status : packet-in-TYPE-bypassed</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : packet-in-TYPE-queued</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : packet-in-TYPE-dropped</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : packet-in-TYPE-backlog</code></p>
<dd>optional string, containing an integer, at least 0</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<dt> <i>Additional In-Band Configuration:</i></p>
<dl>
<dd>
<dl>
<dt> <code>local_ip</code></p>
<dd>optional string </p>
<dt> <code>local_netmask</code></p>
<dd>optional string </p>
<dt> <code>local_gateway</code></p>
<dd>optional string</dl>
</dl>
<dt> <i>Controller Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>is_connected</code></p>
<dd>boolean </p>
<dt> <code>role</code></p>
<dd>optional string, one of <code>slave</code>, <code>other</code>, or <code>master</code> </p>
<dt> <code>status : last_error</code></p>
<dd>optional string </p>
<dt> <code>status : state</code></p>
<dd>optional string, one of <code>ACTIVE</code>, <code>VOID</code>, <code>CONNECTING</code>, <code>IDLE</code>, or <code>BACKOFF</code> </p>
<dt> <code>status : sec_since_connect</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : sec_since_disconnect</code></p>
<dd>optional string, containing an integer, at least 1</dl>
</dl>
<dt> <i>Connection Parameters:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : dscp</code></p>
<dd>optional string, containing an integer</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs </p>
<dt> <code>other_config</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<p><i>Core Features:</i></p>
<dl>
<dt><code>target</code>: string</p>
<dd>Connection method for controller46</p>
<dd>The following connection methods are currently supported for primary controllers:</p>
<dl>
<dd>
<dl>
<dt><code>ssl:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified SSL <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name)46 The <code>ssl</code> column in the <code>Open_vSwitch</code> table must point to a valid SSL configuration when this form is used46</p>
<dd>If <i>port</i> is not specified, it defaults to 665346</p>
<dd>SSL support is an optional feature that is not always built as part of Open vSwitch46</p>
<dt><code>tcp:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified TCP <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name), where <i>ip</i> can be IPv4 or IPv6 address46 If <i>ip</i> is an IPv6 address, wrap it in square brackets, e46g46 <code>tcp:[::1]:6653</code>46</p>
<dd>If <i>port</i> is not specified, it defaults to 665346</dl>
</dl>
<dd>The following connection methods are currently supported for service controllers:</p>
<dl>
<dd>
<dl>
<dt><code>pssl:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>Listens for SSL connections on the specified TCP <i>port</i>46 If <i>ip</i>, which must be expressed as an IP address (not a DNS name), is specified, then connections are restricted to the specified local IP address (either IPv4 or IPv6)46 If <i>ip</i> is an IPv6 address, wrap it in square brackets, e46g46 <code>pssl:6653:[::1]</code>46</p>
<dd>If <i>port</i> is not specified, it defaults to 665346 If <i>ip</i> is not specified then it listens only on IPv4 (but not IPv6) addresses46 The <code>ssl</code> column in the <code>Open_vSwitch</code> table must point to a valid SSL configuration when this form is used46</p>
<dd>If <i>port</i> is not specified, it currently to 665346</p>
<dd>SSL support is an optional feature that is not always built as part of Open vSwitch46</p>
<dt><code>ptcp:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>Listens for connections on the specified TCP <i>port</i>46 If <i>ip</i>, which must be expressed as an IP address (not a DNS name), is specified, then connections are restricted to the specified local IP address (either IPv4 or IPv6)46 If <i>ip</i> is an IPv6 address, wrap it in square brackets, e46g46 <code>ptcp:6653:[::1]</code>46 If <i>ip</i> is not specified then it listens only on IPv4 addresses46</p>
<dd>If <i>port</i> is not specified, it defaults to 665346</dl>
</dl>
<dd>When multiple controllers are configured for a single bridge, the <code>target</code> values must be unique46 Duplicate <code>target</code> values yield unspecified results46</p>
<dt><code>connection_mode</code>: optional string, either <code>in-band</code> or <code>out-of-band</code></p>
<dd>If it is specified, this setting must be one of the following strings that describes how Open vSwitch contacts this OpenFlow controller over the network:</p>
<dl>
<dd>
<dl>
<dt><code>in-band</code></p>
<dd>In this mode, this controller&#8217;s OpenFlow traffic travels over the bridge associated with the controller46 With this setting, Open vSwitch allows traffic to and from the controller regardless of the contents of the OpenFlow flow table46 (Otherwise, Open vSwitch would never be able to connect to the controller, because it did not have a flow to enable it46) This is the most common connection mode because it is not necessary to maintain two independent networks46</p>
<dt><code>out-of-band</code></p>
<dd>In this mode, OpenFlow traffic uses a control network separate from the bridge associated with this controller, that is, the bridge does not use any of its own network devices to communicate with the controller46 The control network must be configured separately, before or after <code>ovs-vswitchd</code> is started46</dl>
</dl>
<dd>If not specified, the default is implementation-specific46</dl>
<p> <i>Controller Failure Detection and Handling:</i></p>
<dl>
<dt><code>max_backoff</code>: optional integer, at least 1,000</p>
<dd>Maximum number of milliseconds to wait between connection attempts46 Default is implementation-specific46</p>
<dt><code>inactivity_probe</code>: optional integer</p>
<dd>Maximum number of milliseconds of idle time on connection to controller before sending an inactivity probe message46 If Open vSwitch does not communicate with the controller for the specified number of seconds, it will send a probe46 If a response is not received for the same additional amount of time, Open vSwitch assumes the connection has been broken and attempts to reconnect46 Default is implementation-specific46 A value of 0 disables inactivity probes46</dl>
<p> <i>Asynchronous Messages:</i> OpenFlow switches send certain messages to controllers spontanenously, that is, not in response to any request from the controller46 These messages are called &#8220;asynchronous messages46&#8221; These columns allow asynchronous messages to be limited or disabled to ensure the best use of network resources46</p>
<dl>
<dt><code>enable_async_messages</code>: optional boolean</p>
<dd>The OpenFlow protocol enables asynchronous messages at time of connection establishment, which means that a controller can receive asynchronous messages, potentially many of them, even if it turns them off immediately after connecting46 Set this column to <code>false</code> to change Open vSwitch behavior to disable, by default, all asynchronous messages46 The controller can use the <code>NXT_SET_ASYNC_CONFIG</code> Nicira extension to OpenFlow to turn on any messages that it does want to receive, if any46</dl>
<p> <i>Controller Rate Limiting:</i> A switch can forward packets to a controller over the OpenFlow protocol46 Forwarding packets this way at too high a rate can overwhelm a controller, frustrate use of the OpenFlow connection for other purposes, increase the latency of flow setup, and use an unreasonable amount of bandwidth46 Therefore, Open vSwitch supports limiting the rate of packet forwarding to a controller46 </p>
<p> There are two main reasons in OpenFlow for a packet to be sent to a controller: either the packet &#8220;misses&#8221; in the flow table, that is, there is no matching flow, or a flow table action says to send the packet to the controller46 Open vSwitch limits the rate of each kind of packet separately at the configured rate46 Therefore, the actual rate that packets are sent to the controller can be up to twice the configured rate, when packets are sent for both reasons46 </p>
<p> This feature is specific to forwarding packets over an OpenFlow connection46 It is not general-purpose QoS46 See the <code>QoS</code> table for quality of service configuration, and <code>ingress_policing_rate</code> in the <code>Interface</code> table for ingress policing configuration46</p>
<dl>
<dt><code>controller_rate_limit</code>: optional integer, at least 100</p>
<dd>The maximum rate at which the switch will forward packets to the OpenFlow controller, in packets per second46 If no value is specified, rate limiting is disabled46</p>
<dt><code>controller_burst_limit</code>: optional integer, at least 25</p>
<dd>When a high rate triggers rate-limiting, Open vSwitch queues packets to the controller for each port and transmits them to the controller at the configured rate46 This value limits the number of queued packets46 Ports on a bridge share the packet queue fairly46</p>
<dd>This value has no effect unless <code>controller_rate_limit</code> is configured46 The current default when this value is not specified is one-quarter of <code>controller_rate_limit</code>, meaning that queuing can delay forwarding a packet to the controller by up to 250 ms46</dl>
<p> <i>Controller Rate Limiting Statistics:</i> These values report the effects of rate limiting46 Their values are relative to establishment of the most recent OpenFlow connection, or since rate limiting was enabled, whichever happened more recently46 Each consists of two values, one with <code>TYPE</code> replaced by <code>miss</code> for rate limiting flow table misses, and the other with <code>TYPE</code> replaced by <code>action</code> for rate limiting packets sent by OpenFlow actions46 </p>
<p> These statistics are reported only when controller rate limiting is enabled46</p>
<dl>
<dt><code>status : packet-in-TYPE-bypassed</code>: optional string, containing an integer, at least 0</p>
<dd>Number of packets sent directly to the controller, without queuing, because the rate did not exceed the configured maximum46</p>
<dt><code>status : packet-in-TYPE-queued</code>: optional string, containing an integer, at least 0</p>
<dd>Number of packets added to the queue to send later46</p>
<dt><code>status : packet-in-TYPE-dropped</code>: optional string, containing an integer, at least 0</p>
<dd>Number of packets added to the queue that were later dropped due to overflow46 This value is less than or equal to <code>status:packet-in-TYPE-queued</code>46</p>
<dt><code>status : packet-in-TYPE-backlog</code>: optional string, containing an integer, at least 0</p>
<dd>Number of packets currently queued46 The other statistics increase monotonically, but this one fluctuates between 0 and the <code>controller_burst_limit</code> as conditions change46</dl>
<p> <i>Additional In-Band Configuration:</i> These values are considered only in in-band control mode (see <code>connection_mode</code>)46 </p>
<p> When multiple controllers are configured on a single bridge, there should be only one set of unique values in these columns46 If different values are set for these columns in different controllers, the effect is unspecified46</p>
<dl>
<dt><code>local_ip</code>: optional string</p>
<dd>The IP address to configure on the local port, e46g46 <code>1924616846046123</code>46 If this value is unset, then <code>local_netmask</code> and <code>local_gateway</code> are ignored46</p>
<dt><code>local_netmask</code>: optional string</p>
<dd>The IP netmask to configure on the local port, e46g46 <code>2554625546255460</code>46 If <code>local_ip</code> is set but this value is unset, then the default is chosen based on whether the IP address is class A, B, or C46</p>
<dt><code>local_gateway</code>: optional string</p>
<dd>The IP address of the gateway to configure on the local port, as a string, e46g46 <code>19246168460461</code>46 Leave this column unset if this network has no gateway46</dl>
<p> <i>Controller Status:</i></p>
<dl>
<dt><code>is_connected</code>: boolean</p>
<dd><code>true</code> if currently connected to this controller, <code>false</code> otherwise46</p>
<dt><code>role</code>: optional string, one of <code>slave</code>, <code>other</code>, or <code>master</code></p>
<dd>The level of authority this controller has on the associated bridge46 Possible values are:</p>
<dl>
<dd>
<dl>
<dt><code>other</code></p>
<dd>Allows the controller access to all OpenFlow features46</p>
<dt><code>master</code></p>
<dd>Equivalent to <code>other</code>, except that there may be at most one master controller at a time46 When a controller configures itself as <code>master</code>, any existing master is demoted to the <code>slave</code> role46</p>
<dt><code>slave</code></p>
<dd>Allows the controller read-only access to OpenFlow features46 Attempts to modify the flow table will be rejected with an error46 Slave controllers do not receive OFPT_PACKET_IN or OFPT_FLOW_REMOVED messages, but they do receive OFPT_PORT_STATUS messages46</dl>
</dl>
<dt><code>status : last_error</code>: optional string</p>
<dd>A human-readable description of the last error on the connection to the controller; i46e46 <code>strerror(errno)</code>46 This key will exist only if an error has occurred46</p>
<dt><code>status : state</code>: optional string, one of <code>ACTIVE</code>, <code>VOID</code>, <code>CONNECTING</code>, <code>IDLE</code>, or <code>BACKOFF</code></p>
<dd>The state of the connection to the controller:</p>
<dl>
<dd>
<dl>
<dt><code>VOID</code></p>
<dd>Connection is disabled46</p>
<dt><code>BACKOFF</code></p>
<dd>Attempting to reconnect at an increasing period46</p>
<dt><code>CONNECTING</code></p>
<dd>Attempting to connect46</p>
<dt><code>ACTIVE</code></p>
<dd>Connected, remote host responsive46</p>
<dt><code>IDLE</code></p>
<dd>Connection is idle46 Waiting for response to keep-alive46</dl>
</dl>
<dd>These values may change in the future46 They are provided only for human consumption46</p>
<dt><code>status : sec_since_connect</code>: optional string, containing an integer, at least 0</p>
<dd>The amount of time since this controller last successfully connected to the switch (in seconds)46 Value is empty if controller has never successfully connected46</p>
<dt><code>status : sec_since_disconnect</code>: optional string, containing an integer, at least 1</p>
<dd>The amount of time since this controller last disconnected from the switch (in seconds)46 Value is empty if controller has never disconnected46</dl>
<p> <i>Connection Parameters:</i> Additional configuration for a connection between the controller and the Open vSwitch46</p>
<dl>
<dt><code>other_config : dscp</code>: optional string, containing an integer</p>
<dd>The Differentiated Service Code Point (DSCP) is specified using 6 bits in the Type of Service (TOS) field in the IP header46 DSCP provides a mechanism to classify the network traffic and provide Quality of Service (QoS) on IP networks46 The DSCP value specified here is used when establishing the connection between the controller and the Open vSwitch46 If no value is specified, a default value of 48 is chosen46 Valid DSCP values must be in the range 0 to 6346</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd></dl>
<h2>Manager TABLE</h2>
<p>Configuration for a database connection to an Open vSwitch database (OVSDB) client46 </p>
<p> This table primarily configures the Open vSwitch database (<code>ovsdb-server</code>), not the Open vSwitch switch (<code>ovs-vswitchd</code>)46 The switch does read the table to determine what connections should be treated as in-band46 </p>
<p> The Open vSwitch database server can initiate and maintain active connections to remote clients46 It can also listen for database connections46</p>
<h3>Summary:</h3>
<dl>
<dt> <i>Core Features:</i></p>
<dl>
<dd>
<dl>
<dt> <code>target</code></p>
<dd>string (must be unique within table) </p>
<dt> <code>connection_mode</code></p>
<dd>optional string, either <code>in-band</code> or <code>out-of-band</code></dl>
</dl>
<dt> <i>Client Failure Detection and Handling:</i></p>
<dl>
<dd>
<dl>
<dt> <code>max_backoff</code></p>
<dd>optional integer, at least 1,000 </p>
<dt> <code>inactivity_probe</code></p>
<dd>optional integer</dl>
</dl>
<dt> <i>Status:</i></p>
<dl>
<dd>
<dl>
<dt> <code>is_connected</code></p>
<dd>boolean </p>
<dt> <code>status : last_error</code></p>
<dd>optional string </p>
<dt> <code>status : state</code></p>
<dd>optional string, one of <code>ACTIVE</code>, <code>VOID</code>, <code>CONNECTING</code>, <code>IDLE</code>, or <code>BACKOFF</code> </p>
<dt> <code>status : sec_since_connect</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : sec_since_disconnect</code></p>
<dd>optional string, containing an integer, at least 0 </p>
<dt> <code>status : locks_held</code></p>
<dd>optional string </p>
<dt> <code>status : locks_waiting</code></p>
<dd>optional string </p>
<dt> <code>status : locks_lost</code></p>
<dd>optional string </p>
<dt> <code>status : n_connections</code></p>
<dd>optional string, containing an integer, at least 2 </p>
<dt> <code>status : bound_port</code></p>
<dd>optional string, containing an integer</dl>
</dl>
<dt> <i>Connection Parameters:</i></p>
<dl>
<dd>
<dl>
<dt> <code>other_config : dscp</code></p>
<dd>optional string, containing an integer</dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs </p>
<dt> <code>other_config</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<p><i>Core Features:</i></p>
<dl>
<dt><code>target</code>: string (must be unique within table)</p>
<dd>Connection method for managers46</p>
<dd>The following connection methods are currently supported:</p>
<dl>
<dd>
<dl>
<dt><code>ssl:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified SSL <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name)46 The <code>ssl</code> column in the <code>Open_vSwitch</code> table must point to a valid SSL configuration when this form is used46</p>
<dd>If <i>port</i> is not specified, it defaults to 664046</p>
<dd>SSL support is an optional feature that is not always built as part of Open vSwitch46</p>
<dt><code>tcp:</code><i>ip</i>[<code>:</code><i>port</i>]</p>
<dd>The specified TCP <i>port</i> on the host at the given <i>ip</i>, which must be expressed as an IP address (not a DNS name), where <i>ip</i> can be IPv4 or IPv6 address46 If <i>ip</i> is an IPv6 address, wrap it in square brackets, e46g46 <code>tcp:[::1]:6640</code>46</p>
<dd>If <i>port</i> is not specified, it defaults to 664046</p>
<dt><code>pssl:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>Listens for SSL connections on the specified TCP <i>port</i>46 Specify 0 for <i>port</i> to have the kernel automatically choose an available port46 If <i>ip</i>, which must be expressed as an IP address (not a DNS name), is specified, then connections are restricted to the specified local IP address (either IPv4 or IPv6 address)46 If <i>ip</i> is an IPv6 address, wrap in square brackets, e46g46 <code>pssl:6640:[::1]</code>46 If <i>ip</i> is not specified then it listens only on IPv4 (but not IPv6) addresses46 The <code>ssl</code> column in the <code>Open_vSwitch</code> table must point to a valid SSL configuration when this form is used46</p>
<dd>If <i>port</i> is not specified, it defaults to 664046</p>
<dd>SSL support is an optional feature that is not always built as part of Open vSwitch46</p>
<dt><code>ptcp:</code>[<i>port</i>][<code>:</code><i>ip</i>]</p>
<dd>Listens for connections on the specified TCP <i>port</i>46 Specify 0 for <i>port</i> to have the kernel automatically choose an available port46 If <i>ip</i>, which must be expressed as an IP address (not a DNS name), is specified, then connections are restricted to the specified local IP address (either IPv4 or IPv6 address)46 If <i>ip</i> is an IPv6 address, wrap it in square brackets, e46g46 <code>ptcp:6640:[::1]</code>46 If <i>ip</i> is not specified then it listens only on IPv4 addresses46</p>
<dd>If <i>port</i> is not specified, it defaults to 664046</dl>
</dl>
<dd>When multiple managers are configured, the <code>target</code> values must be unique46 Duplicate <code>target</code> values yield unspecified results46</p>
<dt><code>connection_mode</code>: optional string, either <code>in-band</code> or <code>out-of-band</code></p>
<dd>If it is specified, this setting must be one of the following strings that describes how Open vSwitch contacts this OVSDB client over the network:</p>
<dl>
<dd>
<dl>
<dt><code>in-band</code></p>
<dd>In this mode, this connection&#8217;s traffic travels over a bridge managed by Open vSwitch46 With this setting, Open vSwitch allows traffic to and from the client regardless of the contents of the OpenFlow flow table46 (Otherwise, Open vSwitch would never be able to connect to the client, because it did not have a flow to enable it46) This is the most common connection mode because it is not necessary to maintain two independent networks46</p>
<dt><code>out-of-band</code></p>
<dd>In this mode, the client&#8217;s traffic uses a control network separate from that managed by Open vSwitch, that is, Open vSwitch does not use any of its own network devices to communicate with the client46 The control network must be configured separately, before or after <code>ovs-vswitchd</code> is started46</dl>
</dl>
<dd>If not specified, the default is implementation-specific46</dl>
<p> <i>Client Failure Detection and Handling:</i></p>
<dl>
<dt><code>max_backoff</code>: optional integer, at least 1,000</p>
<dd>Maximum number of milliseconds to wait between connection attempts46 Default is implementation-specific46</p>
<dt><code>inactivity_probe</code>: optional integer</p>
<dd>Maximum number of milliseconds of idle time on connection to the client before sending an inactivity probe message46 If Open vSwitch does not communicate with the client for the specified number of seconds, it will send a probe46 If a response is not received for the same additional amount of time, Open vSwitch assumes the connection has been broken and attempts to reconnect46 Default is implementation-specific46 A value of 0 disables inactivity probes46</dl>
<p> <i>Status:</i></p>
<dl>
<dt><code>is_connected</code>: boolean</p>
<dd><code>true</code> if currently connected to this manager, <code>false</code> otherwise46</p>
<dt><code>status : last_error</code>: optional string</p>
<dd>A human-readable description of the last error on the connection to the manager; i46e46 <code>strerror(errno)</code>46 This key will exist only if an error has occurred46</p>
<dt><code>status : state</code>: optional string, one of <code>ACTIVE</code>, <code>VOID</code>, <code>CONNECTING</code>, <code>IDLE</code>, or <code>BACKOFF</code></p>
<dd>The state of the connection to the manager:</p>
<dl>
<dd>
<dl>
<dt><code>VOID</code></p>
<dd>Connection is disabled46</p>
<dt><code>BACKOFF</code></p>
<dd>Attempting to reconnect at an increasing period46</p>
<dt><code>CONNECTING</code></p>
<dd>Attempting to connect46</p>
<dt><code>ACTIVE</code></p>
<dd>Connected, remote host responsive46</p>
<dt><code>IDLE</code></p>
<dd>Connection is idle46 Waiting for response to keep-alive46</dl>
</dl>
<dd>These values may change in the future46 They are provided only for human consumption46</p>
<dt><code>status : sec_since_connect</code>: optional string, containing an integer, at least 0</p>
<dd>The amount of time since this manager last successfully connected to the database (in seconds)46 Value is empty if manager has never successfully connected46</p>
<dt><code>status : sec_since_disconnect</code>: optional string, containing an integer, at least 0</p>
<dd>The amount of time since this manager last disconnected from the database (in seconds)46 Value is empty if manager has never disconnected46</p>
<dt><code>status : locks_held</code>: optional string</p>
<dd>Space-separated list of the names of OVSDB locks that the connection holds46 Omitted if the connection does not hold any locks46</p>
<dt><code>status : locks_waiting</code>: optional string</p>
<dd>Space-separated list of the names of OVSDB locks that the connection is currently waiting to acquire46 Omitted if the connection is not waiting for any locks46</p>
<dt><code>status : locks_lost</code>: optional string</p>
<dd>Space-separated list of the names of OVSDB locks that the connection has had stolen by another OVSDB client46 Omitted if no locks have been stolen from this connection46</p>
<dt><code>status : n_connections</code>: optional string, containing an integer, at least 2</p>
<dd>When <code>target</code> specifies a connection method that listens for inbound connections (e46g46 <code>ptcp:</code> or <code>pssl:</code>) and more than one connection is actually active, the value is the number of active connections46 Otherwise, this key-value pair is omitted46</p>
<dd>When multiple connections are active, status columns and key-value pairs (other than this one) report the status of one arbitrarily chosen connection46</p>
<dt><code>status : bound_port</code>: optional string, containing an integer</p>
<dd>When <code>target</code> is <code>ptcp:</code> or <code>pssl:</code>, this is the TCP port on which the OVSDB server is listening46 (This is is particularly useful when <code>target</code> specifies a port of 0, allowing the kernel to choose any available port46)</dl>
<p> <i>Connection Parameters:</i> Additional configuration for a connection between the manager and the Open vSwitch Database46</p>
<dl>
<dt><code>other_config : dscp</code>: optional string, containing an integer</p>
<dd>The Differentiated Service Code Point (DSCP) is specified using 6 bits in the Type of Service (TOS) field in the IP header46 DSCP provides a mechanism to classify the network traffic and provide Quality of Service (QoS) on IP networks46 The DSCP value specified here is used when establishing the connection between the manager and the Open vSwitch46 If no value is specified, a default value of 48 is chosen46 Valid DSCP values must be in the range 0 to 6346</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd>
<dt><code>other_config</code>: map of string-string pairs</p>
<dd></dl>
<h2>NetFlow TABLE</h2>
<p>A NetFlow target46 NetFlow is a protocol that exports a number of details about terminating IP flows, such as the principals involved and duration46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>targets</code></p>
<dd>set of 1 or more strings </p>
<dt> <code>engine_id</code></p>
<dd>optional integer, in range 0 to 255 </p>
<dt> <code>engine_type</code></p>
<dd>optional integer, in range 0 to 255 </p>
<dt> <code>active_timeout</code></p>
<dd>integer, at least -1 </p>
<dt> <code>add_id_to_interface</code></p>
<dd>boolean </p>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>targets</code>: set of 1 or more strings</p>
<dd>NetFlow targets in the form <i>ip</i><code>:</code><i>port</i>46 The <i>ip</i> must be specified numerically, not as a DNS name46</p>
<dt><code>engine_id</code>: optional integer, in range 0 to 255</p>
<dd>Engine ID to use in NetFlow messages46 Defaults to datapath index if not specified46</p>
<dt><code>engine_type</code>: optional integer, in range 0 to 255</p>
<dd>Engine type to use in NetFlow messages46 Defaults to datapath index if not specified46</p>
<dt><code>active_timeout</code>: integer, at least -1</p>
<dd>The interval at which NetFlow records are sent for flows that are still active, in seconds46 A value of <code>0</code> requests the default timeout (currently 600 seconds); a value of <code>-1</code> disables active timeouts46</p>
<dd>The NetFlow passive timeout, for flows that become inactive, is not configurable46 It will vary depending on the Open vSwitch version, the forms and contents of the OpenFlow flow tables, CPU and memory usage, and network activity46 A typical passive timeout is about a second46</p>
<dt><code>add_id_to_interface</code>: boolean</p>
<dd>If this column&#8217;s value is <code>false</code>, the ingress and egress interface fields of NetFlow flow records are derived from OpenFlow port numbers46 When it is <code>true</code>, the 7 most significant bits of these fields will be replaced by the least significant 7 bits of the engine id46 This is useful because many NetFlow collectors do not expect multiple switches to be sending messages from the same host, so they do not store the engine information which could be used to disambiguate the traffic46</p>
<dd>When this option is enabled, a maximum of 508 ports are supported46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Ssl Table</h2>
<p>SSL configuration for an Open_vSwitch46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>private_key</code></p>
<dd>string </p>
<dt> <code>certificate</code></p>
<dd>string </p>
<dt> <code>ca_cert</code></p>
<dd>string </p>
<dt> <code>bootstrap_ca_cert</code></p>
<dd>boolean </p>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>private_key</code>: string</p>
<dd>Name of a PEM file containing the private key used as the switch&#8217;s identity for SSL connections to the controller46</p>
<dt><code>certificate</code>: string</p>
<dd>Name of a PEM file containing a certificate, signed by the certificate authority (CA) used by the controller and manager, that certifies the switch&#8217;s private key, identifying a trustworthy switch46</p>
<dt><code>ca_cert</code>: string</p>
<dd>Name of a PEM file containing the CA certificate used to verify that the switch is connected to a trustworthy controller46</p>
<dt><code>bootstrap_ca_cert</code>: boolean</p>
<dd>If set to <code>true</code>, then Open vSwitch will attempt to obtain the CA certificate from the controller on its first SSL connection and save it to the named PEM file46 If it is successful, it will immediately drop the connection and reconnect, and from then on all SSL connections must be authenticated by a certificate signed by the CA certificate thus obtained46 <code>This option exposes the SSL connection to a man-in-the-middle attack obtaining the initial CA certificate46</code> It may still be useful for bootstrapping46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>sFlow TABLE</h2>
<p>A set of sFlow(R) targets46 sFlow is a protocol for remote monitoring of switches46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>agent</code></p>
<dd>optional string </p>
<dt> <code>header</code></p>
<dd>optional integer </p>
<dt> <code>polling</code></p>
<dd>optional integer </p>
<dt> <code>sampling</code></p>
<dd>optional integer </p>
<dt> <code>targets</code></p>
<dd>set of 1 or more strings </p>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>agent</code>: optional string</p>
<dd>Name of the network device whose IP address should be reported as the &#8220;agent address&#8221; to collectors46 If not specified, the agent device is figured from the first target address and the routing table46 If the routing table does not contain a route to the target, the IP address defaults to the <code>local_ip</code> in the collector&#8217;s <code>Controller</code>46 If an agent IP address cannot be determined any of these ways, sFlow is disabled46</p>
<dt><code>header</code>: optional integer</p>
<dd>Number of bytes of a sampled packet to send to the collector46 If not specified, the default is 128 bytes46</p>
<dt><code>polling</code>: optional integer</p>
<dd>Polling rate in seconds to send port statistics to the collector46 If not specified, defaults to 30 seconds46</p>
<dt><code>sampling</code>: optional integer</p>
<dd>Rate at which packets should be sampled and sent to the collector46 If not specified, defaults to 400, which means one out of 400 packets, on average, will be sent to the collector46</p>
<dt><code>targets</code>: set of 1 or more strings</p>
<dd>sFlow targets in the form <i>ip</i><code>:</code><i>port</i>46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Ipfix Table</h2>
<p>Configuration for sending packets to IPFIX collectors46 </p>
<p> IPFIX is a protocol that exports a number of details about flows46 The IPFIX implementation in Open vSwitch samples packets at a configurable rate, extracts flow information from those packets, optionally caches and aggregates the flow information, and sends the result to one or more collectors46 </p>
<p> IPFIX in Open vSwitch can be configured two different ways:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>With <code>per-bridge sampling</code>, Open vSwitch performs IPFIX sampling automatically on all packets that pass through a bridge46 To configure per-bridge sampling, create an <code>IPFIX</code> record and point a <code>Bridge</code> table&#8217;s <code>ipfix</code> column to it46 The <code>Flow_Sample_Collector_Set</code> table is not used for per-bridge sampling46</p>
<dt>&bull;</p>
<dd>With <code>flow-based sampling</code>, <code>sample</code> actions in the OpenFlow flow table drive IPFIX sampling46 See <code><a href="/docs/linux/man/8-ovs-ofctl/">ovs-ofctl</a></code>(8) for a description of the <code>sample</code> action46</p>
<dd>Flow-based sampling also requires database configuration: create a <code>IPFIX</code> record that describes the IPFIX configuration and a <code>Flow_Sample_Collector_Set</code> record that points to the <code>Bridge</code> whose flow table holds the <code>sample</code> actions and to <code>IPFIX</code> record46 The <code>ipfix</code> in the <code>Bridge</code> table is not used for flow-based sampling46</dl>
</dl>
<h3>Summary:</h3>
<dl>
<dt> <code>targets</code></p>
<dd>set of strings </p>
<dt> <code>cache_active_timeout</code></p>
<dd>optional integer, in range 0 to 4,200 </p>
<dt> <code>cache_max_flows</code></p>
<dd>optional integer, in range 0 to 4,294,967,295 </p>
<dt> <i>Per-Bridge Sampling:</i></p>
<dl>
<dd>
<dl>
<dt> <code>sampling</code></p>
<dd>optional integer, in range 1 to 4,294,967,295 </p>
<dt> <code>obs_domain_id</code></p>
<dd>optional integer, in range 0 to 4,294,967,295 </p>
<dt> <code>obs_point_id</code></p>
<dd>optional integer, in range 0 to 4,294,967,295 </p>
<dt> <code>other_config : enable-tunnel-sampling</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : enable-input-sampling</code></p>
<dd>optional string, either <code>true</code> or <code>false</code> </p>
<dt> <code>other_config : enable-output-sampling</code></p>
<dd>optional string, either <code>true</code> or <code>false</code></dl>
</dl>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>targets</code>: set of strings</p>
<dd>IPFIX target collectors in the form <i>ip</i><code>:</code><i>port</i>46</p>
<dt><code>cache_active_timeout</code>: optional integer, in range 0 to 4,200</p>
<dd>The maximum period in seconds for which an IPFIX flow record is cached and aggregated before being sent46 If not specified, defaults to 046 If 0, caching is disabled46</p>
<dt><code>cache_max_flows</code>: optional integer, in range 0 to 4,294,967,295</p>
<dd>The maximum number of IPFIX flow records that can be cached at a time46 If not specified, defaults to 046 If 0, caching is disabled46</dl>
<p> <i>Per-Bridge Sampling:</i> These values affect only per-bridge sampling46 See above for a description of the differences between per-bridge and flow-based sampling46</p>
<dl>
<dt><code>sampling</code>: optional integer, in range 1 to 4,294,967,295</p>
<dd>The rate at which packets should be sampled and sent to each target collector46 If not specified, defaults to 400, which means one out of 400 packets, on average, will be sent to each target collector46</p>
<dt><code>obs_domain_id</code>: optional integer, in range 0 to 4,294,967,295</p>
<dd>The IPFIX Observation Domain ID sent in each IPFIX packet46 If not specified, defaults to 046</p>
<dt><code>obs_point_id</code>: optional integer, in range 0 to 4,294,967,295</p>
<dd>The IPFIX Observation Point ID sent in each IPFIX flow record46 If not specified, defaults to 046</p>
<dt><code>other_config : enable-tunnel-sampling</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>Set to <code>true</code> to enable sampling and reporting tunnel header 7-tuples in IPFIX flow records46 Tunnel sampling is disabled by default46</p>
<dd>The following enterprise entities report the sampled tunnel info:</p>
<dl>
<dd>
<dl>
<dt>tunnelType:</p>
<dd>ID: 891, and enterprise ID 6876 (VMware)46</p>
<dd>type: unsigned 8-bit integer46</p>
<dd>data type semantics: identifier46</p>
<dd>description: Identifier of the layer 2 network overlay network encapsulation type: 0x01 VxLAN, 0x02 GRE, 0x03 LISP, 0x05 IPsec+GRE, 0x07 GENEVE46</p>
<dt>tunnelKey:</p>
<dd>ID: 892, and enterprise ID 6876 (VMware)46</p>
<dd>type: variable-length octetarray46</p>
<dd>data type semantics: identifier46</p>
<dd>description: Key which is used for identifying an individual traffic flow within a VxLAN (24-bit VNI), GENEVE (24-bit VNI), GRE (32-bit key), or LISP (24-bit instance ID) tunnel46 The key is encoded in this octetarray as a 3-, 4-, or 8-byte integer ID in network byte order46</p>
<dt>tunnelSourceIPv4Address:</p>
<dd>ID: 893, and enterprise ID 6876 (VMware)46</p>
<dd>type: unsigned 32-bit integer46</p>
<dd>data type semantics: identifier46</p>
<dd>description: The IPv4 source address in the tunnel IP packet header46</p>
<dt>tunnelDestinationIPv4Address:</p>
<dd>ID: 894, and enterprise ID 6876 (VMware)46</p>
<dd>type: unsigned 32-bit integer46</p>
<dd>data type semantics: identifier46</p>
<dd>description: The IPv4 destination address in the tunnel IP packet header46</p>
<dt>tunnelProtocolIdentifier:</p>
<dd>ID: 895, and enterprise ID 6876 (VMware)46</p>
<dd>type: unsigned 8-bit integer46</p>
<dd>data type semantics: identifier46</p>
<dd>description: The value of the protocol number in the tunnel IP packet header46 The protocol number identifies the tunnel IP packet payload type46</p>
<dt>tunnelSourceTransportPort:</p>
<dd>ID: 896, and enterprise ID 6876 (VMware)46</p>
<dd>type: unsigned 16-bit integer46</p>
<dd>data type semantics: identifier46</p>
<dd>description: The source port identifier in the tunnel transport header46 For the transport protocols UDP, TCP, and SCTP, this is the source port number given in the respective header46</p>
<dt>tunnelDestinationTransportPort:</p>
<dd>ID: 897, and enterprise ID 6876 (VMware)46</p>
<dd>type: unsigned 16-bit integer46</p>
<dd>data type semantics: identifier46</p>
<dd>description: The destination port identifier in the tunnel transport header46 For the transport protocols UDP, TCP, and SCTP, this is the destination port number given in the respective header46</dl>
</dl>
<dt><code>other_config : enable-input-sampling</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>By default, Open vSwitch samples and reports flows at bridge port input in IPFIX flow records46 Set this column to <code>false</code> to disable input sampling46</p>
<dt><code>other_config : enable-output-sampling</code>: optional string, either <code>true</code> or <code>false</code></p>
<dd>By default, Open vSwitch samples and reports flows at bridge port output in IPFIX flow records46 Set this column to <code>false</code> to disable output sampling46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>Flow_Sample_Collector_Set TABLE</h2>
<p>A set of IPFIX collectors of packet samples generated by OpenFlow <code>sample</code> actions46 This table is used only for IPFIX flow-based sampling, not for per-bridge sampling (see the <code>IPFIX</code> table for a description of the two forms)46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>id</code></p>
<dd>integer, in range 0 to 4,294,967,295 </p>
<dt> <code>bridge</code> <code>Bridge</code> </p>
<dt> <code>ipfix</code></p>
<dd>optional <code>IPFIX</code> </p>
<dt> <i>Common Columns:</i></p>
<dl>
<dd>
<dl>
<dt> <code>external_ids</code></p>
<dd>map of string-string pairs</dl>
</dl>
</dl>
<h3>Details:</h3>
<dl>
<dt><code>id</code>: integer, in range 0 to 4,294,967,295</p>
<dd>The ID of this collector set, unique among the bridge&#8217;s collector sets, to be used as the <code>collector_set_id</code> in OpenFlow <code>sample</code> actions46</p>
<dt><code>bridge</code>: <code>Bridge</code></p>
<dd>The bridge into which OpenFlow <code>sample</code> actions can be added to send packet samples to this set of IPFIX collectors46</p>
<dt><code>ipfix</code>: optional <code>IPFIX</code></p>
<dd>Configuration of the set of IPFIX collectors to send one flow record per sampled packet to46</dl>
<p> <i>Common Columns:</i> The overall purpose of these columns is described under <code>Common Columns</code> at the beginning of this document46</p>
<dl>
<dt><code>external_ids</code>: map of string-string pairs</p>
<dd></dl>
<h2>AutoAttach TABLE</h2>
<p>Auto Attach configuration within a bridge46 The IETF Auto-Attach SPBM draft standard describes a compact method of using IEEE 802461AB Link Layer Discovery Protocol (LLDP) together with a IEEE 802461aq Shortest Path Bridging (SPB) network to automatically attach network devices to individual services in a SPB network46 The intent here is to allow network applications and devices using OVS to be able to easily take advantage of features offered by industry standard SPB networks46 </p>
<p> Auto Attach (AA) uses LLDP to communicate between a directly connected Auto Attach Client (AAC) and Auto Attach Server (AAS)46 The LLDP protocol is extended to add two new Type-Length-Value tuples (TLVs)46 The first new TLV supports the ongoing discovery of directly connected AA correspondents46 Auto Attach operates by regularly transmitting AA discovery TLVs between the AA client and AA server46 By exchanging these discovery messages, both the AAC and AAS learn the system name and system description of their peer46 In the OVS context, OVS operates as the AA client and the AA server resides on a switch at the edge of the SPB network46 </p>
<p> Once AA discovery has been completed the AAC then uses the second new TLV to deliver identifier mappings from the AAC to the AAS46 A primary feature of Auto Attach is to facilitate the mapping of VLANs defined outside the SPB network onto service ids (ISIDs) defined within the SPM network46 By doing so individual external VLANs can be mapped onto specific SPB network services46 These VLAN id to ISID mappings can be configured and managed locally using new options added to the ovs-vsctl command46 </p>
<p> The Auto Attach OVS feature does not provide a full implementation of the LLDP protocol46 Support for the mandatory TLVs as defined by the LLDP standard and support for the AA TLV extensions is provided46 LLDP protocol support in OVS can be enabled or disabled on a port by port basis46 LLDP support is disabled by default46</p>
<h3>Summary:</h3>
<dl>
<dt> <code>system_name</code></p>
<dd>string </p>
<dt> <code>system_description</code></p>
<dd>string </p>
<dt> <code>mappings</code></p>
<dd>map of integer-integer pairs, key in range 0 to 16,777,215, value in range 0 to 4,095</dl>
<h3>Details:</h3>
<dl>
<dt><code>system_name</code>: string</p>
<dd>The system_name string is exported in LLDP messages46 It should uniquely identify the bridge in the network46</p>
<dt><code>system_description</code>: string</p>
<dd>The system_description string is exported in LLDP messages46 It should describe the type of software and hardware46</p>
<dt><code>mappings</code>: map of integer-integer pairs, key in range 0 to 16,777,215, value in range 0 to 4,095</p>
<dd>A mapping from SPB network Individual Service Identifier (ISID) to VLAN id46 </p>
</dl>
