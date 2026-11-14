---
title: "ovs-ctl(8)"
name: "ovs-ctl"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-ctl/"
description: "ovs-ctl – OVS startup helper script"
---

<p>ovs-ctl &#8211; OVS startup helper script</p>
<h2>Synopsis</h2>
<p><code>ovs-ctl</code> <code>&#8211;system-id=random</code>|<i>uuid</i> [<i>options</i>] <code>start<br />
 ovs-ctl stop<br />
 ovs-ctl</code> <code>&#8211;system-id=random</code>|<i>uuid</i> [<i>options</i>] <code>restart<br />
 ovs-ctl status<br />
 ovs-ctl version<br />
 ovs-ctl [</code><i>options</i>] <code>load-kmod</code><br />
 <code>ovs-ctl &#8211;system-id=random</code>|<i>uuid</i> [<i>options</i>] <code>force-reload-kmod</code><br />
 <code>ovs-ctl </code>[<code>&#8211;protocol=</code><i>protocol</i>] [<code>&#8211;sport=</code><i>sport</i>] [<code>&#8211;dport=</code><i>dport</i>] <code>enable-protocol</code><br />
 <code>ovs-ctl help </code>| <code>-h </code>| <code>&#8211;help<br />
 ovs-ctl &#8211;version </code></p>
<h2>Description</h2>
<p>The <code>ovs-ctl</code> program starts, stops, and checks the status of Open vSwitch daemons. It is not meant to be invoked directly by system administrators but to be called internally by system startup scripts. </p>
<p> Each of <code>ovs-ctl</code>&#8216;s commands is described separately below.</p>
<h2>The &#8220;start&#8221; command</h2>
<p>The <code>start</code> command starts Open vSwitch. It performs the following tasks:</p>
<dl>
<dt>1.</p>
<dd>Loads the Open vSwitch kernel module. If this fails, and the Linux bridge module is loaded but no bridges exist, it tries to unload the bridge module and tries loading the Open vSwitch kernel module again. (This is because the Open vSwitch kernel module cannot coexist with the Linux bridge module before 2.6.37.)</dl>
<p> The <code>start</code> command skips the following steps if <code>ovsdb-server</code> is already running:</p>
<dl>
<dt>2.</p>
<dd>If the Open vSwitch database file does not exist, it creates it. If the database does exist, but it has an obsolete version, it upgrades it to the latest schema.</p>
<dt>3.</p>
<dd>Starts <code>ovsdb-server</code>.</p>
<dt>4.</p>
<dd>Initializes a few values inside the database.</p>
<dt>5.</p>
<dd>If the <code>&#8211;delete-bridges</code> option was used, deletes all of the bridges from the database.</p>
<dt>6.</p>
<dd>If the <code>&#8211;delete-transient-ports</code> option was used, deletes all ports that have <code>other_config:transient</code> set to true.</dl>
<p> The <code>start</code> command skips the following step if <code>ovs-vswitchd</code> is already running:</p>
<dl>
<dt>7.</p>
<dd>Starts <code>ovs-vswitchd</code>.</dl>
<h3>Options</h3>
<p>Several command-line options influence the <code>start</code> command&#8217;s behavior. Some form of the following option should ordinarily be specified:</p>
<dl>
<dt><code>&#8211;system-id=</code><i>uuid</i></p>
<dd>
<dt><code>&#8211;system-id=random</code></p>
<dd>This specifies a unique system identifier to store into <code>external-ids:system-id</code> in the database&#8217;s <code>Open_vSwitch</code> table. Remote managers that talk to the Open vSwitch database server over network protocols use this value to identify and distinguish Open vSwitch instances, so it should be unique (at least) within OVS instances that will connect to a single controller.</p>
<dd>When <code>random</code> is specified, <code>ovs-ctl</code> will generate a random ID that persists from one run to another (stored in a file). When another string is specified <code>ovs-ctl</code> uses it literally.</dl>
<p> The following options should be specified if the defaults are not suitable:</p>
<dl>
<dt><code>&#8211;system-type=</code><i>type</i></p>
<dd>
<dt><code>&#8211;system-version=</code><i>version</i></p>
<dd>Sets the value to store in the <code>system-type</code> and <code>system-version</code> columns, respectively, in the database&#8217;s <code>Open_vSwitch</code> table. Remote managers may use these values to determine the kind of system to which they are connected (primarily for display to human administrators).</p>
<dd>When not specified, <code>ovs-ctl</code> uses values from the optional <code>system-type.conf</code> and <code>system-version.conf</code> files(see section <code>FILES</code>) or it uses the <code>lsb_release</code> program, if present, to provide reasonable defaults.</dl>
<p> The following options are also likely to be useful:</p>
<dl>
<dt><code>&#8211;external-id=&quot;</code><i>name</i><code>=</code><i>value</i><code>&quot;</p>
<dd>Sets external-ids:</code><i>name</i> to <i>value</i> in the database&#8217;s <code>Open_vSwitch</code> table. Specifying this option multiple times adds multiple key-value pairs.</p>
<dt><code>&#8211;delete-bridges</code></p>
<dd>Ordinarily Open vSwitch bridges persist from one system boot to the next, as long as the database is preserved. Some environments instead expect to re-create all of the bridges and other configuration state on every boot. This option supports that, by deleting all Open vSwitch bridges after starting <code>ovsdb-server</code> but before starting <code>ovs-vswitchd</code>.</p>
<dt><code>&#8211;delete-transient-ports</code></p>
<dd>Deletes all ports that have the other_config:transient value set to true. This is important on certain environments where some ports are going to be recreated after reboot, but other ports need to be persisted in the database.</dl>
<p> The following options are less important:</p>
<dl>
<dt><code>&#8211;daemon-cwd=</code><i>directory</i></p>
<dd>Specifies the current working directory that the OVS daemons should run from. The default is <code>/</code> (the root directory) if this option is not specified. (This option is useful because most systems create core files in a process&#8217;s current working directory and because a file system that is in use as a process&#8217;s current working directory cannot be unmounted.)</p>
<dt><code>&#8211;no-force-corefiles</code></p>
<dd>By default, <code>ovs-ctl</code> enables core dumps for the OVS daemons. This option disables that behavior.</p>
<dt><code>&#8211;no-mlockall</code></p>
<dd>By default <code>ovs-ctl</code> passes <code>&#8211;mlockall</code> to <code>ovs-vswitchd</code>, requesting that it lock all of its virtual memory, preventing it from being paged to disk. This option suppresses that behavior.</p>
<dt><code>&#8211;ovsdb-server-priority=</code><i>niceness</i></p>
<dd>
<dt><code>&#8211;ovs-vswitchd-priority=</code><i>niceness</i></p>
<dd>Sets the <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1) level used for each daemon. All of them default to <code>-10</code>.</p>
<dt><code>&#8211;ovsdb-server-wrapper=</code><i>wrapper</i></p>
<dd>
<dt><code>&#8211;ovs-vswitchd-wrapper=</code><i>wrapper</i></p>
<dd>Configures the specified daemon to run under <i>wrapper</i>, which is one of the following:</p>
<dl>
<dd>
<dl>
<dt><code>valgrind</code></p>
<dd>Run the daemon under <code><a href="/docs/linux/man/1-valgrind/">valgrind</a></code>(1), if it is installed, logging to <i>daemon</i><code>.valgrind.log.</code><i>pid</i> in the log directory.</p>
<dt><code>strace</code></p>
<dd>Run the daemon under <code><a href="/docs/linux/man/1-strace/">strace</a></code>(1), if it is installed, logging to <i>daemon</i><code>.strace.log.</code><i>pid</i> in the log directory.</p>
<dt><code>glibc</code></p>
<dd>Enable GNU C library features designed to find memory errors.</dl>
</dl>
<dd>By default, no wrapper is used.</p>
<dd>Each of the wrappers can expose bugs in Open vSwitch that lead to incorrect operation, including crashes. The <code>valgrind</code> and <code>strace</code> wrappers greatly slow daemon operations so they should not be used in production. They also produce voluminous logs that can quickly fill small disk partitions. The <code>glibc</code> wrapper is less resource-intensive but still somewhat slows the daemons.</dl>
<p> The following options control file locations. They should only be used if the default locations cannot be used. See <code>FILES</code>, below, for more information.</p>
<dl>
<dt><code>&#8211;db-file=</code><i>file</i></p>
<dd>Overrides the file name for the OVS database.</p>
<dt><code>&#8211;db-sock=</code><i>socket</i></p>
<dd>Overrides the file name for the Unix domain socket used to connect to <code>ovsdb-server</code>.</p>
<dt><code>&#8211;db-schema=</code><i>schema</i></p>
<dd>Overrides the file name for the OVS database schema.</p>
<dt><code>&#8211;extra-dbs=</code><i>file</i></p>
<dd>Adds <i>file</i> as an extra database for <code>ovsdb-server</code> to serve out. Multiple space-separated file names may also be specified. <i>file</i> should begin with <code>/</code>; if it does not, then it will be taken as relative to <i>dbdir</i>.</dl>
<h2>The &#8220;stop&#8221; command</h2>
<p>The <code>stop</code> command does not unload the Open vSwitch kernel modules. </p>
<p> This command does nothing and finishes successfully if the OVS daemons aren&#8217;t running.</p>
<h2>The &#8220;restart&#8221; command</h2>
<p>The <code>restart</code> command performs a <code>stop</code> followed by a <code>start</code> command. The command can take the same options as that of the <code>start</code> command. In addition, it saves and restores OpenFlow flows for each individual bridge.</p>
<h2>The &#8220;status&#8221; command</h2>
<p>The <code>status</code> command checks whether the OVS daemons <code>ovs-vswitchd</code> and <code>ovsdb-server</code> are running and prints messages with that information. It exits with status 0 if the daemons are running, 1 otherwise.</p>
<h2>The &#8220;version&#8221; command</h2>
<p>The <code>version</code> command runs <code>ovsdb-server &#8211;version</code> and <code>ovs-vswitchd &#8211;version</code>.</p>
<h2>The &#8220;force-reload-kmod&#8221; command</h2>
<p>The <code>force-reload-kmod</code> command allows upgrading the Open vSwitch kernel module without rebooting. It performs the following tasks:</p>
<dl>
<dt>1.</p>
<dd>Gets a list of OVS &#8220;internal&#8221; interfaces, that is, network devices implemented by Open vSwitch. The most common examples of these are bridge &#8220;local ports&#8221;.</p>
<dt>2.</p>
<dd>Saves the OpenFlow flows of each bridge.</p>
<dt>3.</p>
<dd>Stops the Open vSwitch daemons, as if by a call to <code>ovs-ctl stop</code>.</p>
<dt>4.</p>
<dd>Saves the kernel configuration state of the OVS internal interfaces listed in step 1, including IP and IPv6 addresses and routing table entries.</p>
<dt>5.</p>
<dd>Unloads the Open vSwitch kernel module (including the bridge compatibility module if it is loaded).</p>
<dt>6.</p>
<dd>Starts OVS back up, as if by a call to <code>ovs-ctl start</code>. This reloads the kernel module, restarts the OVS daemons and finally restores the saved OpenFlow flows.</p>
<dt>7.</p>
<dd>Restores the kernel configuration state that was saved in step 4.</p>
<dt>8.</p>
<dd>Checks for daemons that may need to be restarted because they have packet sockets that are listening on old instances of Open vSwitch kernel interfaces and, if it finds any, prints a warning on stdout. DHCP is a common example: if the ISC DHCP client is running on an OVS internal interface, then it will have to be restarted after completing the above procedure. (It would be nice if <code>ovs-ctl</code> could restart daemons automatically, but the details are far too specific to a particular distribution and installation.)</dl>
<p> <code>force-kmod-reload</code> internally stops and starts OVS, so it accepts all of the options accepted by the <code>start</code> command.</p>
<h2>The &#8220;load-kmod&#8221; command</h2>
<p>The <code>load-kmod</code> command loads the openvswitch kernel modules if they are not already loaded. This operation also occurs as part of the <code>start</code> command. The motivation for providing the <code>load-kmod</code> command is to allow errors when loading modules to be handled separatetly from other errors that may occur when running the <code>start</code> command. </p>
<p> By default the <code>load-kmod</code> command attempts to load the openvswitch kernel module.</p>
<h2>The &#8220;enable-protocol&#8221; command</h2>
<p>The <code>enable-protocol</code> command checks for rules related to a specified protocol in the system&#8217;s <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8) configuration. If there are no rules specifically related to that protocol, then it inserts a rule to accept the specified protocol. </p>
<p> More specifically:</p>
<dl>
<dt>&bull;</p>
<dd>If <code>iptables</code> is not installed or not enabled, this command does nothing, assuming that lack of filtering means that the protocol is enabled.</p>
<dt>&bull;</p>
<dd>If the <code>INPUT</code> chain has a rule that matches the specified protocol, then this command does nothing, assuming that whatever rule is installed reflects the system administrator&#8217;s decisions.</p>
<dt>&bull;</p>
<dd>Otherwise, this command installs a rule that accepts traffic of the specified protocol.</dl>
<p> This command normally completes successfully, even if it does nothing. Only the failure of an attempt to insert a rule normally causes it to return an exit code other than 0. The following options control the protocol to be enabled:</p>
<dl>
<dt><code>&#8211;protocol=</code><i>protocol</i></p>
<dd>The name of the IP protocol to be enabled, such as <code>gre</code> or <code>tcp</code>. The default is <code>gre</code>.</p>
<dt><code>&#8211;sport=</code><i>sport</i></p>
<dd>
<dt><code>&#8211;dport=</code><i>dport</i></p>
<dd>TCP or UDP source or destination port to match. These are optional and allowed only with <code>&#8211;protocol=tcp</code> or <code>&#8211;protocol=udp</code>.</dl>
<h2>The &#8220;help&#8221; command</h2>
<p>Prints a usage message and exits successfully.</p>
<h2>Options</h2>
<p>In addition to the options listed for each command above, this option controls the behavior of several of <code>ovs-ctl</code>&#8216;s commands.</p>
<h2>Exit Status</h2>
<p><code>ovs-ctl</code> exits with status 0 on success and nonzero on failure. The <code>start</code> command is considered to succeed if OVS is already started; the <code>stop</code> command is considered to succeed if OVS is already stopped.</p>
<h2>Environment</h2>
<p>The following environment variables affect <code>ovs-ctl</code>:</p>
<dl>
<dt><code>PATH</code></p>
<dd><code>ovs-ctl</code> does not hardcode the location of any of the programs that it runs. <code>ovs-ctl</code> will add the <i>sbindir</i> and <i>bindir</i> that were specified at <code>configure</code> time to <code>PATH</code>, if they are not already present.</p>
<dt><code>OVS_LOGDIR</code></p>
<dd>
<dt><code>OVS_RUNDIR</code></p>
<dd>
<dt><code>OVS_DBDIR</code></p>
<dd>
<dt><code>OVS_SYSCONFDIR</code></p>
<dd>
<dt><code>OVS_PKGDATADIR</code></p>
<dd>
<dt><code>OVS_BINDIR</code></p>
<dd>
<dt><code>OVS_SBINDIR</code></p>
<dd>Setting one of these variables in the environment overrides the respective <code>configure</code> option, both for <code>ovs-ctl</code> itself and for the other Open vSwitch programs that it runs.</dl>
<h2>Files</h2>
<p><code>ovs-ctl</code> uses the following files:</p>
<dl>
<dt><code>ovs-lib</p>
<dd>Shell function library used internally by ovs-ctl</code>. It must be installed in the same directory as <code>ovs-ctl</code>.</p>
<dt><i>logdir</i><code>/</code><i>daemon</i><code>.log</code></p>
<dd>Per-daemon logfiles.</p>
<dt><i>rundir</i><code>/</code><i>daemon</i><code>.pid</code></p>
<dd>Per-daemon pidfiles to track whether a daemon is running and with what process ID.</p>
<dt><i>pkgdatadir</i><code>/vswitch.ovsschema</code></p>
<dd>The OVS database schema used to initialize the database (use <code>&#8211;db-schema to override this location).</p>
<dt></code><i>dbdir</i><code>/conf.db</code></p>
<dd>The OVS database (use <code>&#8211;db-file</code> to override this location).</p>
<dt><i>rundir</i><code>/openvswitch/db.sock</code></p>
<dd>The Unix domain socket used for local communication with <code>ovsdb-server</code> (use <code>&#8211;db-sock</code> to override this location).</p>
<dt><i>sysconfdir</i><code>/openvswitch/system-id.conf</code></p>
<dd>The persistent system UUID created and read by <code>&#8211;system-id=random</code>.</p>
<dt><i>sysconfdir</i><code>/openvswitch/system-type.conf</code></p>
<dd>
<dt><i>sysconfdir</i><code>/openvswitch/system-version.conf</code></p>
<dd>The <code>system-type</code> and <code>system-version</code> values stored in the database&#8217;s <code>Open_vSwitch</code> table when not specified as a command-line option.</dl>
<h2>Example</h2>
<p>The files <code>debian/openvswitch-switch.init</code> and <code>xenserver/etc_init.d_openvswitch</code> in the Open vSwitch source distribution are good examples of how to use <code>ovs-ctl</code>.</p>
<h2>See Also</h2>
<p><code>README.md</code>, <code>INSTALL.Linux.md</code>, <code><a href="/docs/linux/man/8-ovsdb-server/">ovsdb-server</a></code>(8), <code><a href="/docs/linux/man/8-ovs-vswitchd/">ovs-vswitchd</a></code>(8). </p>
