---
title: "xm(1)"
name: "xm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xm/"
description: "xm – Xen management user interface"
---

<h2>SYNOPSIS</h2>
<p> <code>xm</code> <i>subcommand</i> [<i>args</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>xm</code> program is the main interface for managing Xen guest domains. The program can be used to create, pause, and shutdown domains. It can also be used to list current domains, enable or pin VCPUs, and attach or detach virtual block devices. </p>
<p> The basic structure of every <code>xm</code> command is almost always: </p>
<dl>
<dt>
</dt><dd> <code>xm</code> <i>subcommand</i> <i>domain-id</i> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]</dd></dl>
<p> Where <i>subcommand</i> is one of the subcommands listed below, <i>domain-id</i> is the numeric domain id, or the domain name (which will be internally translated to domain id), and <i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i> are subcommand specific options. There are a few exceptions to this rule in the cases where the subcommand in question acts on all domains, the entire machine, or directly on the Xen hypervisor. Those exceptions will be clear for each of those subcommands.</p>
<h2>NOTES</h2>
<p> All <code>xm</code> operations rely upon the Xen control daemon, aka <code>xend</code>. For any <code>xm</code> commands to run, xend must also be running. For this reason you should start xend as a service when your system first boots using Xen. </p>
<p> Most <code>xm</code> commands require root privileges to run due to the communications channels used to talk to the hypervisor. Running as non root will return an error. </p>
<p> Most <code>xm</code> commands act synchronously, except maybe create, shutdown, mem-set and vcpu-set. The fact that the <code>xm</code> command returned doesn&#8217;t necessarily mean that the action is complete and you must poll through xm list periodically to detect that the operation completed.</p>
<h2>DOMAIN SUBCOMMANDS</h2>
<p> The following subcommands manipulate domains directly. As stated previously, most commands take <i>domain-id</i> as the first parameter.</p>
<dl>
<dt><code>console</code> <i>domain-id</i></dt>
<dd> Attach to domain <i>domain-id</i>&#8216;s console. If you&#8217;ve set up your domains to have a traditional log in console this will look much like a normal text log in screen. </dd>
<p> This uses the back end xenconsole service which currently only works for para-virtual domains. </p>
<p> The attached console will perform much like a standard serial console, so running curses based interfaces over the console <code>is not advised</code>. Vi tends to get very odd when using it over this interface. </p>
<p> Use the key combination Ctrl+] to detach the domain console.</p>
<dt><code>create</code> <i>configfile</i> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] [<i>vars</i>]..</dt>
<dd> The create subcommand requires a config file and can optionally take a series of <i>vars</i> that add to or override variables defined in the config file. See xmdomain.cfg for full details of that file format, and possible options used in either the configfile or for <i>vars</i>. </dd>
<p> <i>configfile</i> can either be an absolute path to a file, or a relative path to a file located in /etc/xen. </p>
<p> Create will return <code>as soon</code> as the domain is started. This <code>does not</code> mean the guest <font SIZE="-1">OS</font> in the domain has actually booted, or is available for input. </p>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>&#8211;help_config</code></dt>
<dd> Print the available configuration variables <i>vars</i>. These variables may be used on the command line or in the configuration file <i>configfile</i>.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> No console output.</dd>
<dt><code>&#8211;path</code></dt>
<dd> Search path for configuration scripts. The value of <font SIZE="-1">PATH</font> is a colon-separated directory list.</dd>
<dt><code>-f=FILE</code>, <code>&#8211;defconfig=FILE</code></dt>
<dd> Use the given Python configuration script. The configuration script is loaded after arguments have been processed. Each command-line option sets a configuration variable named after its long option name, and these variables are placed in the environment of the script before it is loaded. Variables for options that may be repeated have list values. Other variables can be set using name=value on the command line. After the script is loaded, option values that were not set on the command line are replaced by the values set in the script.</dd>
<dt><code>-F=FILE</code>, <code>&#8211;config=FILE</code></dt>
<dd> Use the given <font SIZE="-1">SXP</font> formated configuration script. <font SIZE="-1">SXP</font> is the underlying configuration format used by Xen. <font SIZE="-1">SXP</font> configuration scripts can be hand-written or generated from Python configuration scripts, using the -n (dryrun) option to print the configuration. An <font SIZE="-1">SXP</font> formatted configuration file may also be generated for a given <i>domain-id</i> by redirecting the output from the the <code>xm list &#8211;long </code>domain-id to a file.</dd>
<dt><code>-n</code>, <code>&#8211;dryrun</code></dt>
<dd> Dry run &#8211; prints the resulting configuration in <font SIZE="-1">SXP</font> but does not create the domain.</dd>
<dt><code>-x</code>, <code>&#8211;xmldryrun</code></dt>
<dd> <font SIZE="-1">XML</font> dry run &#8211; prints the resulting configuration in <font SIZE="-1">XML</font> but does not create the domain.</dd>
<dt><code>-s</code>, <code>&#8211;skipdtd</code></dt>
<dd> Skip <font SIZE="-1">DTD</font> checking &#8211; skips checks on <font SIZE="-1">XML</font> before creating. Experimental. Can decrease create time.</dd>
<dt><code>-p</code>, <code>&#8211;paused</code></dt>
<dd> Leave the domain paused after it is created.</dd>
<dt><code>-c</code>, <code>&#8211;console_autoconnect</code></dt>
<dd> Attach console to the domain as soon as it has started. This is useful for determining issues with crashing domains.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>EXAMPLES</code></font></p>
</dd><dl>
<dt><i>with config file</i></dt>
<dd>
<pre>
  xm create Fedora4
</pre>
<p> This creates a domain with the file /etc/xen/Fedora4, and returns as soon as it is run.</p>
</dd><dt><i>without config file</i></dt>
<dd>
<pre>
  xm create /dev/null ramdisk=initrd.img \
     kernel=/boot/vmlinuz-2.6.12.6-xenU \
     name=ramdisk vif='' vcpus=1 \
     memory=64 root=/dev/ram0
</pre>
<p> This creates the domain without using a config file (more specifically using /dev/null as an empty config file), kernel and ramdisk as specified, setting the name of the domain to &#8220;ramdisk&#8221;, also disabling virtual networking. (This example comes from the xm-test test suite.)</dd></dl>
</dl>
<dl>
</dl>
<dt><code>delete</code></dt>
<dd> Remove a domain from Xend domain management. The <code>xm list</code> command shows the domain names.</dd>
<dt><code>destroy</code> <i>domain-id</i></dt>
<dd> Immediately terminate the domain <i>domain-id</i>. This doesn&#8217;t give the domain <font SIZE="-1">OS</font> any chance to react, and is the equivalent of ripping the power cord out on a physical machine. In most cases you will want to use the <code>shutdown</code> command instead.</dd>
<dt><code>domid</code> <i>domain-name</i></dt>
<dd> Converts a domain name to a domain id using xend&#8217;s internal mapping.</dd>
<dt><code>domname</code> <i>domain-id</i></dt>
<dd> Converts a domain id to a domain name using xend&#8217;s internal mapping.</dd>
<dt><code>dump-core</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <i>domain-id</i> [<i>filename</i>]</dt>
<dd> Dumps the virtual machine&#8217;s memory for the specified domain to the <i>filename</i> specified. The dump file will be written to a distribution specific directory for dump files. Such as: /var/lib/xen/dump or /var/xen/dump Defaults to dumping the core without pausing the domain if no <i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i> are specified. </dd>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>-L</code>, <code>&#8211;live</code></dt>
<dd> Dump core without pausing the domain.</dd>
<dt><code>-C</code>, <code>&#8211;crash</code></dt>
<dd> Crash domain after dumping core.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>help</code> [<code>&#8211;long</code>]</dt>
<dd> Displays the short help message (i.e. common commands). </dd>
<p> The <code>&#8211;long</code> option prints out the complete set of <code>xm</code> subcommands, grouped by function.</p>
<dt><code>list</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] [<i>domain-id</i> &#8230;]</dt>
<dd> Prints information about one or more domains. If no domains are specified it prints out information about all domains. </dd>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>-l</code>, <code>&#8211;long</code></dt>
<dd> The output for <code>xm list</code> is not the table view shown below, but instead presents the data in <font SIZE="-1">SXP</font> format.</dd>
<dt><code>&#8211;label</code></dt>
<dd> Security labels are added to the output of xm list and the lines are sorted by the labels (ignoring case). See the <font SIZE="-1">ACCESS</font> <font SIZE="-1">CONTROL</font> <font SIZE="-1">SUBCOMMAND</font> section of this man page for more information about labels.</dd>
<dt><code>&#8211;state=&lt;state</code>&gt;</dt>
<dd> Output information for VMs in the specified state.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>EXAMPLE</code></font> </p>
<p> An example format for the list is as follows: </p>
<pre><code>
Name ID Mem(MiB)
VCPUs State Time(s)
        Domain
    - 0 0 98 1 r-- -- -5068.6 Fedora3 164 128 1 r-- -- -7.6 Fedora4 165 128 1 -- -- --0.6 Mandrake2006 166 128 1 - b-- --3.6 Mandrake10 .2 167 128 1 -- -- --2.5 Suse9 .2 168 100 1 -- -- --1.8
</code></pre>
<p> Name is the name of the domain. <font SIZE="-1">ID</font> the numeric domain id. Mem is the desired amount of memory to allocate to the domain (although it may not be the currently allocated amount). VCPUs is the number of virtual CPUs allocated to the domain. State is the run state (see below). Time is the total run time of the domain as accounted for by Xen. </p>
<p> <font SIZE="-1"><code>STATES</code></font> </p>
<p> The State field lists 6 states for a Xen domain, and which ones the current domain is in.</p>
</dd><dl>
<dt><code>r &#8211; running</code></dt>
<dd> The domain is currently running on a <font SIZE="-1">CPU</font>.</dd>
<dt><code>b &#8211; blocked</code></dt>
<dd> The domain is blocked, and not running or runnable. This can be caused because the domain is waiting on <font SIZE="-1">IO</font> (a traditional wait state) or has gone to sleep because there was nothing else for it to do.</dd>
<dt><code>p &#8211; paused</code></dt>
<dd> The domain has been paused, usually occurring through the administrator running <code>xm pause</code>. When in a paused state the domain will still consume allocated resources like memory, but will not be eligible for scheduling by the Xen hypervisor.</dd>
<dt><code>s &#8211; shutdown</code></dt>
<dd> <font SIZE="-1">FIXME:</font> Why would you ever see this state?</dd>
<dt><code>c &#8211; crashed</code></dt>
<dd> The domain has crashed, which is always a violent ending. Usually this state can only occur if the domain has been configured not to restart on crash. See xmdomain.cfg for more info.</dd>
<dt><code>d &#8211; dying</code></dt>
<dd> The domain is in process of dying, but hasn&#8217;t completely shutdown or crashed. </dd>
<p> <font SIZE="-1">FIXME:</font> Is this right?</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>NOTES</code></font> </p>
</dd><dl>
<dt>
</dt><dd> The Time column is deceptive. Virtual <font SIZE="-1">IO</font> (network and block devices) used by domains requires coordination by Domain0, which means that Domain0 is actually charged for much of the time that a DomainU is doing <font SIZE="-1">IO</font>. Use of this time value to determine relative utilizations by domains is thus very suspect, as a high <font SIZE="-1">IO</font> workload may show as less utilized than a high <font SIZE="-1">CPU</font> workload. Consider yourself warned.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>mem-max</code> <i>domain-id</i> <i>mem</i></dt>
<dd> Specify the maximum amount of memory the domain is able to use. <i>mem</i> is specified in megabytes. </dd>
<p> The mem-max value may not correspond to the actual memory used in the domain, as it may balloon down its memory to give more back to the <font SIZE="-1">OS</font>.</p>
<dt><code>mem-set</code> <i>domain-id</i> <i>mem</i></dt>
<dd> Set the domain&#8217;s used memory using the balloon driver. </dd>
<p> Because this operation requires cooperation from the domain operating system, there is no guarantee that it will succeed. This command will definitely not work unless the domain has the required paravirt driver. </p>
<p> <code>Warning:</code> There is no good way to know in advance how small of a mem-set will make a domain unstable and cause it to crash. Be very careful when using this command on running domains.</p>
<dt><code>migrate</code> <i>domain-id</i> <i>host</i> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]</dt>
<dd> Migrate a domain to another host machine. Xend must be running on other host machine, it must be running the same version of Xen, it must have the migration <font SIZE="-1">TCP</font> port open and accepting connections from the source host, and there must be sufficient resources for the domain to run (memory, disk, etc). </dd>
<p> Migration is pretty complicated, and has many security implications. Please read the Xen User&#8217;s Guide to ensure you understand the ramifications and limitations on migration before attempting it in production. </p>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>-l</code>, <code>&#8211;live</code></dt>
<dd> Use live migration. This will migrate the domain between hosts without shutting down the domain. See the Xen User&#8217;s Guide for more information.</dd>
<dt><code>-r</code>, <code>&#8211;resource</code> <i>Mbs</i></dt>
<dd> Set maximum Mbs allowed for migrating the domain. This ensures that the network link is not saturated with migration traffic while attempting to do other useful work.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>new</code> <i>configfile</i> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] [<i>vars</i>]&#8230;</dt>
<dd> Adds a domain to Xend domain management. </dd>
<p> The new subcommand requires a config file and can optionally take a series of <i>vars</i> that add to or override variables defined in the config file. See xmdomain.cfg for full details of that file format, and possible options used in either the configfile or for <i>vars</i>. </p>
<p> <i>configfile</i> can either be an absolute path to a file, or a relative path to a file located in /etc/xen. </p>
<p> The new subcommand will return without starting the domain. The domain needs to be started using the <code>xm start</code> command. </p>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>&#8211;help_config</code></dt>
<dd> Print the available configuration variables <i>vars</i>. These variables may be used on the command line or in the configuration file <i>configfile</i>.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> No console output.</dd>
<dt><code>&#8211;path</code></dt>
<dd> Search path for configuration scripts. The value of <font SIZE="-1">PATH</font> is a colon-separated directory list.</dd>
<dt><code>-f=FILE</code>, <code>&#8211;defconfig=FILE</code></dt>
<dd> Use the given Python configuration script. The configuration script is loaded after arguments have been processed. Each command-line option sets a configuration variable named after its long option name, and these variables are placed in the environment of the script before it is loaded. Variables for options that may be repeated have list values. Other variables can be set using name=value on the command line. After the script is loaded, option values that were not set on the command line are replaced by the values set in the script.</dd>
<dt><code>-F=FILE</code>, <code>&#8211;config=FILE</code></dt>
<dd> Use the given <font SIZE="-1">SXP</font> formated configuration script. <font SIZE="-1">SXP</font> is the underlying configuration format used by Xen. <font SIZE="-1">SXP</font> configuration scripts can be hand-written or generated from Python configuration scripts, using the -n (dryrun) option to print the configuration. An <font SIZE="-1">SXP</font> formatted configuration file may also be generated for a given <i>domain-id</i> by redirecting the output from the the <code>xm list &#8211;long </code>domain-id to a file.</dd>
<dt><code>-n</code>, <code>&#8211;dryrun</code></dt>
<dd> Dry run &#8211; prints the resulting configuration in <font SIZE="-1">SXP</font> but does not create the domain.</dd>
<dt><code>-x</code>, <code>&#8211;xmldryrun</code></dt>
<dd> <font SIZE="-1">XML</font> dry run &#8211; prints the resulting configuration in <font SIZE="-1">XML</font> but does not create the domain.</dd>
<dt><code>-s</code>, <code>&#8211;skipdtd</code></dt>
<dd> Skip <font SIZE="-1">DTD</font> checking &#8211; skips checks on <font SIZE="-1">XML</font> before creating. Experimental. Can decrease create time.</dd>
<dt><code>-p</code>, <code>&#8211;paused</code></dt>
<dd> Leave the domain paused after it is created.</dd>
<dt><code>-c</code>, <code>&#8211;console_autoconnect</code></dt>
<dd> Attach console to the domain as soon as it has started. This is useful for determining issues with crashing domains.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>pause</code> <i>domain-id</i></dt>
<dd> Pause a domain. When in a paused state the domain will still consume allocated resources such as memory, but will not be eligible for scheduling by the Xen hypervisor.</dd>
<dt><code>reboot</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <i>domain-id</i></dt>
<dd> Reboot a domain. This acts just as if the domain had the <code>reboot</code> command run from the console. The command returns as soon as it has executed the reboot action, which may be significantly before the domain actually reboots. </dd>
<p> The behavior of what happens to a domain when it reboots is set by the <code>on_reboot</code> parameter of the xmdomain.cfg file when the domain was created. </p>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> Reboot all domains.</dd>
<dt><code>-w</code>, <code>&#8211;wait</code></dt>
<dd> Wait for reboot to complete before returning. This may take a while, as all services in the domain will have to be shut down cleanly.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>restore</code> <i>state-file</i></dt>
<dd> Build a domain from an <code>xm save</code> state file. See <code>save</code> for more info.</dd>
<dt><code>resume</code> <i>domain-name</i> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]</dt>
<dd> Moves a domain out of the suspended state and back into memory. </dd>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>-p</code>, &lt;&#8211;paused&gt;</dt>
<dd> Moves a domain back into memory but leaves the domain in a paused state. The <code>xm unpause</code> subcommand may then be used to bring it out of the paused state.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>save</code> <i>domain-id</i> <i>state-file</i></dt>
<dd> Saves a running domain to a state file so that it can be restored later. Once saved, the domain will no longer be running on the system, thus the memory allocated for the domain will be free for other domains to use. <code>xm restore</code> restores from this state file. </dd>
<p> This is roughly equivalent to doing a hibernate on a running computer, with all the same limitations. Open network connections may be severed upon restore, as <font SIZE="-1">TCP</font> timeouts may have expired.</p>
<dt><code>shutdown</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <i>domain-id</i></dt>
<dd> Gracefully shuts down a domain. This coordinates with the domain <font SIZE="-1">OS</font> to perform graceful shutdown, so there is no guarantee that it will succeed, and may take a variable length of time depending on what services must be shutdown in the domain. The command returns immediately after signally the domain unless that <code>-w</code> flag is used. </dd>
<p> The behavior of what happens to a domain when it reboots is set by the <code>on_shutdown</code> parameter of the xmdomain.cfg file when the domain was created. </p>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>-a</code></dt>
<dd> Shutdown <code>all</code> domains. Often used when doing a complete shutdown of a Xen system.</dd>
<dt><code>-w</code></dt>
<dd> Wait for the domain to complete shutdown before returning.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>start</code> <i>domain-name</i> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]</dt>
<dd> Start a Xend managed domain that was added using the <code>xm new</code> command. </dd>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>-p</code>, <code>&#8211;paused</code></dt>
<dd> Do not unpause domain after starting it.</dd>
<dt><code>-c</code>, <code>&#8211;console_autoconnect</code></dt>
<dd> Connect to the console after the domain is created.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>suspend</code> <i>domain-name</i></dt>
<dd> Suspend a domain to a state file so that it can be later resumed using the <code>xm resume</code> subcommand. Similar to the <code>xm save</code> subcommand although the state file may not be specified.</dd>
<dt><code>sysrq</code> <i>domain-id</i> <i>letter</i></dt>
<dd> Send a <i>Magic System Request</i> signal to the domain. For more information on available magic sys req operations, see sysrq.txt in your Linux Kernel sources.</dd>
<dt><code>unpause</code> <i>domain-id</i></dt>
<dd> Moves a domain out of the paused state. This will allow a previously paused domain to now be eligible for scheduling by the Xen hypervisor.</dd>
<dt><code>vcpu-set</code> <i>domain-id</i> <i>vcpu-count</i></dt>
<dd> Enables the <i>vcpu-count</i> virtual CPUs for the domain in question. Like mem-set, this command can only allocate up to the maximum virtual <font SIZE="-1">CPU</font> count configured at boot for the domain. </dd>
<p> If the <i>vcpu-count</i> is smaller than the current number of active VCPUs, the highest number VCPUs will be hotplug removed. This may be important for pinning purposes. </p>
<p> Attempting to set the VCPUs to a number larger than the initially configured <font SIZE="-1">VCPU</font> count is an error. Trying to set VCPUs to &lt; 1 will be quietly ignored. </p>
<p> Because this operation requires cooperation from the domain operating system, there is no guarantee that it will succeed. This command will not work with a full virt domain.</p>
<dt><code>vcpu-list</code> [<i>domain-id</i>]</dt>
<dd> Lists <font SIZE="-1">VCPU</font> information for a specific domain. If no domain is specified, <font SIZE="-1">VCPU</font> information for all domains will be provided.</dd>
<dt><code>vcpu-pin</code> <i>domain-id</i> <i>vcpu</i> <i>cpus</i></dt>
<dd> Pins the the <font SIZE="-1">VCPU</font> to only run on the specific CPUs. The keyword <code>all</code> can be used to apply the <i>cpus</i> list to all VCPUs in the domain. </dd>
<p> Normally VCPUs can float between available CPUs whenever Xen deems a different run state is appropriate. Pinning can be used to restrict this, by ensuring certain VCPUs can only run on certain physical CPUs.</dl>
<h2>XEN HOST SUBCOMMANDS</h2>
<dl>
<dt><code>dmesg</code> [<code>-c</code>]</dt>
<dd> Reads the Xen message buffer, similar to dmesg on a Linux system. The buffer contains informational, warning, and error messages created during Xen&#8217;s boot process. If you are having problems with Xen, this is one of the first places to look as part of problem determination. </dd>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><code>-c</code>, <code>&#8211;clear</code></dt>
<dd> Clears Xen&#8217;s message buffer.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>info</code></dt>
<dd> Print information about the Xen host in <i>name : value</i> format. When reporting a Xen bug, please provide this information as part of the bug report. </dd>
<p> Sample output looks as follows (lines wrapped manually to make the man page more readable): </p>
<pre>
 host                   : talon
 release                : 2.6.12.6-xen0
 version                : #1 Mon Nov 14 14:26:26 EST 2005
 machine                : i686
 nr_cpus                : 2
 nr_nodes               : 1
 cores_per_socket       : 1
 threads_per_core       : 1
 cpu_mhz                : 696
 hw_caps                : 0383fbff:00000000:00000000:00000040
 total_memory           : 767
 free_memory            : 37
 xen_major              : 3
 xen_minor              : 0
 xen_extra              : -devel
 xen_caps               : xen-3.0-x86_32
 xen_scheduler          : credit
 xen_pagesize           : 4096
 platform_params        : virt_start=0xfc000000
 xen_changeset          : Mon Nov 14 18:13:38 2005 +0100 
                          7793:090e44133d40
 cc_compiler            : gcc version 3.4.3 (Mandrakelinux 
                          10.2 3.4.3-7mdk)
 cc_compile_by          : sdague
 cc_compile_domain      : (none)
 cc_compile_date        : Mon Nov 14 14:16:48 EST 2005
 xend_config_format     : 3
</pre>
<p> <font SIZE="-1"><code>FIELDS</code></font> </p>
<p> Not all fields will be explained here, but some of the less obvious ones deserve explanation:</p>
<dl>
<dl>
<dt><code>hw_caps</code></dt>
<dd> A vector showing what hardware capabilities are supported by your processor. This is equivalent to, though more cryptic, the flags field in /proc/cpuinfo on a normal Linux machine.</dd>
<dt><code>free_memory</code></dt>
<dd> Available memory (in <font SIZE="-1">MB</font>) not allocated to Xen, or any other domains.</dd>
<dt><code>xen_caps</code></dt>
<dd> The Xen version and architecture. Architecture values can be one of: x86_32, x86_32p (i.e. <font SIZE="-1">PAE</font> enabled), x86_64, ia64.</dd>
<dt><code>xen_changeset</code></dt>
<dd> The Xen mercurial changeset id. Very useful for determining exactly what version of code your Xen system was built from.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>log</code></dt>
<dd> Print out the xend log. This log file can be found in /var/log/xend.log.</dd>
<dt><code>top</code></dt>
<dd> Executes the <code>xentop</code> command, which provides real time monitoring of domains. Xentop is a curses interface, and reasonably self explanatory.</dd>
<dt><code>uptime</code></dt>
<dd> Prints the current uptime of the domains running.</dd></dl>
<h2>SCHEDULER SUBCOMMANDS</h2>
<p> Xen ships with a number of domain schedulers, which can be set at boot time with the <code>sched=</code> parameter on the Xen command line. By default <code>credit</code> is used for scheduling. </p>
<p> <font SIZE="-1">FIXME:</font> we really need a scheduler expert to write up this section.</p>
<dl>
<dt><code>sched-credit</code> [ <code>-d</code> <i>domain-id</i> [ <code>-w</code>[<code>=</code><i></i><font SIZE="-1"><i>WEIGHT</i></font><i></i>] | <code>-c</code>[<code>=</code><i></i><font SIZE="-1"><i>CAP</i></font><i></i>] ] ]</dt>
<dd> Set credit scheduler parameters. The credit scheduler is a proportional fair share <font SIZE="-1">CPU</font> scheduler built from the ground up to be work conserving on <font SIZE="-1">SMP</font> hosts. </dd>
<p> Each domain (including Domain0) is assigned a weight and a cap. </p>
<p> <font SIZE="-1"><code>PARAMETERS</code></font></p>
<dl>
<dl>
<dt><i></i><font SIZE="-1"><i>WEIGHT</i></font><i></i></dt>
<dd> A domain with a weight of 512 will get twice as much <font SIZE="-1">CPU</font> as a domain with a weight of 256 on a contended host. Legal weights range from 1 to 65535 and the default is 256.</dd>
<dt><i></i><font SIZE="-1"><i>CAP</i></font><i></i></dt>
<dd> The cap optionally fixes the maximum amount of <font SIZE="-1">CPU</font> a domain will be able to consume, even if the host system has idle <font SIZE="-1">CPU</font> cycles. The cap is expressed in percentage of one physical <font SIZE="-1">CPU:</font> 100 is 1 physical <font SIZE="-1">CPU</font>, 50 is half a <font SIZE="-1">CPU</font>, 400 is 4 CPUs, etc. The default, 0, means there is no upper cap.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>sched-sedf</code> <i>period</i> <i>slice</i> <i>latency-hint</i> <i>extratime</i> <i>weight</i></dt>
<dd> Set Simple <font SIZE="-1">EDF</font> (Earliest Deadline First) scheduler parameters. This scheduler provides weighted <font SIZE="-1">CPU</font> sharing in an intuitive way and uses realtime-algorithms to ensure time guarantees. For more information see docs/misc/sedf_scheduler_mini-HOWTO.txt in the Xen distribution. </dd>
<p> <font SIZE="-1"><code>PARAMETERS</code></font></p>
<dl>
<dl>
<dt><i>period</i></dt>
<dd> The normal <font SIZE="-1">EDF</font> scheduling usage in nanoseconds</dd>
<dt><i>slice</i></dt>
<dd> The normal <font SIZE="-1">EDF</font> scheduling usage in nanoseconds </dd>
<p> <font SIZE="-1">FIXME:</font> these are lame, should explain more.</p>
<dt><i>latency-hint</i></dt>
<dd> Scaled period if domain is doing heavy I/O.</dd>
<dt><i>extratime</i></dt>
<dd> Flag for allowing domain to run in extra time.</dd>
<dt><i>weight</i></dt>
<dd> Another way of setting <font SIZE="-1">CPU</font> slice.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>EXAMPLES</code></font> </p>
<p> <i>normal </i><font SIZE="-1"><i>EDF</i></font><i> (20ms/5ms):</i> </p>
<pre>
    xm sched-sedf &lt;dom-id&gt; 20000000 5000000 0 0 0
</pre>
<p> <i>best-effort domains (i.e. non-realtime):</i> </p>
<pre>
    xm sched-sedf &lt;dom-id&gt; 20000000 0 0 1 0
</pre>
<p> <i>normal </i><font SIZE="-1"><i>EDF</i></font><i> (20ms/5ms) + share of extra-time:</i> </p>
<pre>
    xm sched-sedf &lt;dom-id&gt; 20000000 5000000 0 1 0
</pre>
<p> <i>4 domains with weights 2:3:4:2</i> </p>
<pre>
    xm sched-sedf &lt;d1&gt; 0 0 0 0 2
    xm sched-sedf &lt;d2&gt; 0 0 0 0 3
    xm sched-sedf &lt;d3&gt; 0 0 0 0 4
    xm sched-sedf &lt;d4&gt; 0 0 0 0 2
</pre>
<p> <i>1 fully-specified (10ms/3ms) domain, 3 other domains share available rest in 2:7:3 ratio:</i> </p>
<pre>
    xm sched-sedf &lt;d1&gt; 10000000 3000000 0 0 0
    xm sched-sedf &lt;d2&gt; 0 0 0 0 2
    xm sched-sedf &lt;d3&gt; 0 0 0 0 7
    xm sched-sedf &lt;d4&gt; 0 0 0 0 3
</pre>
</dd></dl>
</dl>
<h2>VIRTUAL DEVICE COMMANDS</h2>
<p> Most virtual devices can be added and removed while guests are running. The effect to the guest <font SIZE="-1">OS</font> is much the same as any hotplug event.</p>
<h3><font SIZE="-1">BLOCK</font> <font SIZE="-1">DEVICES</font></h3>
<dl>
<dt><code>block-attach</code> <i>domain-id</i> <i>be-dev</i> <i>fe-dev</i> <i>mode</i> [<i>bedomain-id</i>]</dt>
<dd> Create a new virtual block device. This will trigger a hotplug event for the guest. </dd>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dl>
<dt><i>domain-id</i></dt>
<dd> The domain id of the guest domain that the device will be attached to.</dd>
<dt><i>be-dev</i></dt>
<dd> The device in the backend domain (usually domain 0) to be exported. This can be specified as a physical partition (phy:sda7) or as a file mounted as loopback (file://path/to/loop.iso).</dd>
<dt><i>fe-dev</i></dt>
<dd> How the device should be presented to the guest domain. It can be specified as either a symbolic name, such as /dev/hdc, for common devices, or by device id, such as 0x1400 (/dev/hdc device id in hex).</dd>
<dt><i>mode</i></dt>
<dd> The access mode for the device from the guest domain. Supported modes are <code>w</code> (read/write) or <code>r</code> (read-only).</dd>
<dt><i>bedomain-id</i></dt>
<dd> The back end domain hosting the device. This defaults to domain 0.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>EXAMPLES</code></font></p>
</dd><dl>
<dt><i>Mount an </i><font SIZE="-1"><i>ISO</i></font><i> as a Disk</i></dt>
<dd> xm block-attach guestdomain file://path/to/dsl-2.0RC2.iso /dev/hdc ro </dd>
<p> This will mount the dsl <font SIZE="-1">ISO</font> as /dev/hdc in the guestdomain as a read only device. This will probably not be detected as a CD-ROM by the guest, but mounting /dev/hdc manually will work.</dl>
</dl>
<dl>
</dl>
<dt><code>block-detach</code> <i>domain-id</i> <i>devid</i> [<code>&#8211;force</code>]</dt>
<dd> Detach a domain&#8217;s virtual block device. <i>devid</i> may be the symbolic name or the numeric device id given to the device by domain 0. You will need to run <code>xm block-list</code> to determine that number. </dd>
<p> Detaching the device requires the cooperation of the domain. If the domain fails to release the device (perhaps because the domain is hung or is still using the device), the detach will fail. The <code>&#8211;force</code> parameter will forcefully detach the device, but may cause <font SIZE="-1">IO</font> errors in the domain.</p>
<dt><code>block-list</code> [<code>-l</code>|<code>&#8211;long</code>] <i>domain-id</i></dt>
<dd> List virtual block devices for a domain. The returned output is formatted as a list or as an S-Expression if the <code>&#8211;long</code> option was given.</dd></dl>
<h3><font SIZE="-1">NETWORK</font> <font SIZE="-1">DEVICES</font></h3>
<dl>
<dt><code>network-attach</code> <i>domain-id</i> [<code>script=</code><i>scriptname</i>] [<code>ip=</code><i>ipaddr</i>] [<code>mac=</code><i>macaddr</i>] [<code>bridge=</code><i>bridge-name</i>] [<code>backend=</code><i>bedomain-id</i>]</dt>
<dd> Creates a new network device in the domain specified by <i>domain-id</i>. It takes the following optional options:</dd></dl>
<p> <font SIZE="-1"><code>OPTIONS</code></font></p>
<dl>
<dt><code>script=</code><i>scriptname</i></dt>
<dd> Use the specified script name to bring up the network. Defaults to the default setting in xend-config.sxp for <code>vif-script</code>.</dd>
<dt><code>ip=</code><i>ipaddr</i></dt>
<dd> Passes the specified <font SIZE="-1">IP</font> Address to the adapter on creation. </dd>
<p> <font SIZE="-1">FIXME:</font> this currently appears to be <code>broken</code>. I&#8217;m not sure under what circumstances this should actually work.</p>
<dt><code>mac=</code><i>macaddr</i></dt>
<dd> The <font SIZE="-1">MAC</font> address that the domain will see on its Ethernet device. If the device is not specified it will be randomly generated with the 00:16:3e vendor id prefix.</dd>
<dt><code>bridge=</code><i>bridge-name</i></dt>
<dd> The name of the bridge to attach the vif to, in case you have more than one. This defaults to xenbr0.</dd>
<dt><code>backend=</code><i>bedomain-id</i></dt>
<dd> The backend domain id. By default this is domain 0.</dd>
<dt><code>network-detach</code> <i>domain-id</i> <i>devid</i></dt>
<dd> Removes the network device from the domain specified by <i>domain-id</i>. <i>devid</i> is the virtual interface device number within the domain (i.e. the 3 in vif22.3). </dd>
<p> <font SIZE="-1">FIXME:</font> this is currently <code>broken</code>. Network devices aren&#8217;t completely removed from domain 0.</p>
<dt><code>network-list</code> [<code>-l</code>|<code>&#8211;long</code>]&gt; <i>domain-id</i></dt>
<dd> List virtual network interfaces for a domain. The returned output is formatted as a list or as an S-Expression if the <code>&#8211;long</code> option was given.</dd></dl>
<h3><font SIZE="-1">VIRTUAL</font> <font SIZE="-1">TPM</font> <font SIZE="-1">DEVICES</font></h3>
<dl>
<dt><code>vtpm-list</code> [<code>-l</code>|<code>&#8211;long</code>] <i>domain-id</i></dt>
<dd> Show the virtual <font SIZE="-1">TPM</font> device for a domain. The returned output is formatted as a list or as an S-Expression if the <code>&#8211;long</code> option was given.</dd></dl>
<h2>VNET COMMANDS</h2>
<p> The Virtual Network interfaces for Xen. </p>
<p> <font SIZE="-1">FIXME:</font> This needs a lot more explanation, or it needs to be ripped out entirely.</p>
<dl>
<dt><code>vnet-list</code> [<code>-l</code>|<code>&#8211;long</code>]</dt>
<dd> List vnets.</dd>
<dt><code>vnet-create</code> <i>config</i></dt>
<dd> Create a vnet from a config file.</dd>
<dt><code>vnet-delete</code> <i>vnetid</i></dt>
<dd> Delete a vnet.</dd></dl>
<h2>ACCESS CONTROL SUBCOMMANDS</h2>
<p> Access Control in Xen consists of two components: (i) The Access Control Policy (<font SIZE="-1">ACP</font>) defines security labels and access rules based on these labels. (ii) The Access Control Module (<font SIZE="-1">ACM</font>) makes access control decisions by interpreting the policy when domains require to communicate or to access resources. The Xen access control has sufficient mechanisms in place to enforce the access decisions even against maliciously acting user domains (mandatory access control). </p>
<p> Access rights for domains in Xen are determined by the domain security label only and not based on the domain Name or <font SIZE="-1">ID</font>. The <font SIZE="-1">ACP</font> specifies security labels that can then be assigned to domains and resources. Every domain must be assigned exactly one security label, otherwise access control decisions could become indeterministic. ACPs are distinguished by their name, which is a parameter to most of the subcommands described below. Currently, the <font SIZE="-1">ACP</font> specifies two ways to interpret labels: </p>
<p> (1) Simple Type Enforcement: Labels are interpreted to decide access of domains to communication means and virtual or physical resources. Communication between domains as well as access to resources are forbidden by default and can only take place if they are explicitly allowed by the security policy. The proper assignment of labels to domains controls the sharing of information (directly through communication or indirectly through shared resources) between domains. This interpretation allows to control the overt (intended) communication channels in Xen. </p>
<p> (2) Chinese Wall: Labels are interpreted to decide which domains can co-exist (be run simultaneously) on the same system. This interpretation allows to prevent direct covert (unintended) channels and mitigates risks caused by imperfect core domain isolation (trade-off between security and other system requirements). For a short introduction to covert channels, please refer to <a rel="nofollow" href="http://www.multicians.org/timing-chn.html.">http://www.multicians.org/timing-chn.html.</a> </p>
<p> The following subcommands help you to manage security policies in Xen and to assign security labels to domains. To enable access control security in Xen, you must compile Xen with <font SIZE="-1">ACM</font> support enabled as described under &#8220;Configuring Security&#8221; below. There, you will find also examples of each subcommand described here.</p>
<dl>
<dt><code>setpolicy</code> <font SIZE="-1">ACM</font> <i>policy</i></dt>
<dd> Makes the given <font SIZE="-1">ACM</font> policy available to xend as a <i>xend-managed policy</i>. The policy is compiled and a mapping (.map) as well as a binary (.bin) version of the policy is created. The policy is loaded and the system&#8217;s bootloader is prepared to boot the system with this policy the next time it is started. </dd>
<dl>
<dt>
</dt><dd> <i>policy</i> is a dot-separated list of names. The last part is the file name pre-fix for the policy <font SIZE="-1">XML</font> file. The preceding name parts are translated into the local path pointing to the policy <font SIZE="-1">XML</font> file relative to the global policy root directory (/etc/xen/acm-security/policies). For example, example.chwall_ste.client_v1 denotes the policy file example/chwall_ste/client_v1-security_policy.xml relative to the global policy root directory.</dd></dl>
<dt><code>resetpolicy</code></dt>
<dd> Reset the system&#8217;s policy to the default state where the <font SIZE="-1">DEFAULT</font> policy is loaded and enforced. This operation may fail if for example guest VMs are running and and one of them uses a different label than what Domain-0 does. It is best to make sure that no guests are running before issuing this command.</dd>
<dt><code>getpolicy</code> [&#8211;dumpxml]</dt>
<dd> Displays information about the current xend-managed policy, such as name and type of the policy, the uuid xend has assigned to it on the local system, the version of the <font SIZE="-1">XML</font> representation and the status of the policy, such as whether it is currently loaded into Xen or whether the policy is automatically loaded during system boot. With the <i>&#8211;dumpxml</i> option, the <font SIZE="-1">XML</font> representation of the policy is displayed.</dd>
<dt><code>dumppolicy</code></dt>
<dd> Prints the current security policy state information of Xen.</dd>
<dt><code>labels</code> [<i>policy</i>] [<code>type=dom</code>|<code>res</code>|<code>any</code>]</dt>
<dd> Lists all labels of a <i>type</i> (domain, resource, or both) that are defined in the <i>policy</i>. Unless specified, the default <i>policy</i> is the currently enforced access control policy. The default for <i>type</i> is &#8216;dom&#8217;. The labels are arranged in alphabetical order.</dd>
<dt><code>addlabel</code> <i>label</i> <code>dom</code> <i>configfile</i> [<i>policy</i>]</dt>
<dd>
</dd><dt><code>addlabel</code> <i>label</i> <code>mgt</code> <i>domain name</i> [<i>policy type</i>:<i>policy</i>]</dt>
<dd>
</dd><dt><code>addlabel</code> <i>label</i> <code>res</code> <i>resource</i> [<i>policy</i>]</dt>
<dd>
</dd><dt><code>addlabel</code> <i>label</i> <code>vif-idx</code> <i>domain name</i> [<i>policy type</i>:<i>policy</i>]</dt>
<dd> Adds the security label with name <i>label</i> to a domain <i>configfile</i> (dom), a Xend-managed domain (mgt), to the global resource label file for the given <i>resource</i> (res), or to a managed domain&#8217;s virtual network interface (vif) that is specified by its index. Unless specified, the default <i>policy</i> is the currently enforced access control policy. This subcommand also verifies that the <i>policy</i> definition supports the specified <i>label</i> name. </dd>
<p> The only <i>policy type</i> that is currently supported is <i></i><font SIZE="-1"><i>ACM</i></font><i></i>.</p>
<dt><code>rmlabel</code> <code>dom</code> <i>configfile</i></dt>
<dd>
</dd><dt><code>rmlabel</code> <code>mgt</code> <i>domain name</i></dt>
<dd>
</dd><dt><code>rmlabel</code> <code>res</code> <i>resource</i></dt>
<dd>
</dd><dt><code>rmlabel</code> <code>vif-idx</code> <i>domain name</i></dt>
<dd> Works the same as the <code>addlabel</code> command (above), except that this command will remove the label from the domain <i>configfile</i> (dom), a Xend-managed domain (mgt), the global resource label file (res), or a managed domain&#8217;s network interface (vif).</dd>
<dt><code>getlabel</code> <code>dom</code> <i>configfile</i></dt>
<dd>
</dd><dt><code>getlabel</code> <code>mgt</code> <i>domain name</i></dt>
<dd>
</dd><dt><code>getlabel</code> <code>res</code> <i>resource</i></dt>
<dd>
</dd><dt><code>getlabel</code> <code>vif-idx</code> <i>domain name</i></dt>
<dd> Shows the label for a domain&#8217;s configuration in the given <i>configfile</i>, a xend-managed domain (mgt), a resource, or a managed domain&#8217;s network interface (vif).</dd>
<dt><code>resources</code></dt>
<dd> Lists all resources in the global resource label file. Each resource is listed with its associated label and policy name.</dd>
<dt><code>dry-run</code> <i>configfile</i></dt>
<dd> Determines if the specified <i>configfile</i> describes a domain with a valid security configuration for type enforcement. The test shows the policy decision made for each resource label against the domain label as well as the overall decision. </dd>
<p> <font SIZE="-1"><code>CONFIGURING</code></font><font SIZE="-1"><code>SECURITY</code></font></p>
<dl>
<dl>
<dt>
</dt><dd> In xen_source_dir/Config.mk set the following parameter: </dd>
<pre>
    XSM_ENABLE ?= y
    ACM_SECURITY ?= y
</pre>
<p> Then recompile and install xen and the security tools and then reboot: </p>
<pre>
    cd xen_source_dir; make clean; make install
    reboot into Xen
</pre>
</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>RESETTING</code></font><font SIZE="-1"><code>THE</code></font><font SIZE="-1"><code>SYSTEM</code></font><code>&#8216;S </code><font SIZE="-1"><code>SECURITY</code></font> </p>
</dd><dl>
<dt>
</dt><dd> To set the system&#8217;s security policy enforcement into its default state, the follow command can be issued. Make sure that no guests are running while doing this. </dd>
<pre>
    xm resetpolicy
</pre>
<p> After this command has successfully completed, the system&#8217;s <font SIZE="-1">DEFAULT</font> policy is enforced.</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>SETTING</code></font><code> A </code><font SIZE="-1"><code>SECURITY</code></font><font SIZE="-1"><code>POLICY</code></font> </p>
</dd><dl>
<dt>
</dt><dd> This step sets the system&#8217;s policy and automatically loads it into Xen for enforcement. </dd>
<pre>
    xm setpolicy ACM example.client_v1
</pre>
</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>LISTING</code></font><font SIZE="-1"><code>SECURITY</code></font><font SIZE="-1"><code>LABELS</code></font> </p>
</dd><dl>
<dt>
</dt><dd> This subcommand shows all labels that are defined and which can be attached to domains. </dd>
<pre>
    xm labels example.client_v1 type=dom
</pre>
<p> will print for our example policy: </p>
<pre>
        dom_BoincClient
        dom_Fun
        dom_HomeBanking
        dom_NetworkDomain
        dom_StorageDomain
        dom_SystemManagement
</pre>
</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>ATTACHING</code></font><code> A </code><font SIZE="-1"><code>SECURITY</code></font><font SIZE="-1"><code>LABEL</code></font><font SIZE="-1"><code>TO</code></font><code> A </code><font SIZE="-1"><code>DOMAIN</code></font> </p>
</dd><dl>
<dt>
</dt><dd> The <code>addlabel</code> subcommand can attach a security label to a domain configuration file, here a HomeBanking label. The example policy ensures that this domain does not share information with other non-homebanking user domains (i.e., domains labeled as dom_Fun or dom_Boinc) and that it will not run simultaneously with domains labeled as dom_Fun. </dd>
<p> We assume that the specified myconfig.xm configuration file actually instantiates a domain that runs workloads related to home-banking, probably just a browser environment for online-banking. </p>
<pre>
    xm addlabel dom_HomeBanking dom myconfig.xm
</pre>
<p> The very simple configuration file might now look as printed below. The <code>addlabel</code> subcommand added the <code>access_control</code> entry at the end of the file, consisting of a label name and the policy that specifies this label name: </p>
<pre><code>
    kernel = "/boot/vmlinuz-2.6.16-xen"
    ramdisk="/boot/U1_home_banking_ramdisk.img"
    memory = 164
    name = "homebanking"
    vif = [ '' ]
    dhcp = "dhcp"
    access_control = ['policy=example.chwall_ste.client_v1,
                       label=dom_HomeBanking']
</code></pre>
<p> Security labels must be assigned to domain configurations because these labels are essential for making access control decisions as early as during the configuration phase of a newly instantiated domain. Consequently, a security-enabled Xen hypervisor will only start domains that have a security label configured and whose security label is consistent with the currently enforced policy. Otherwise, starting the domain will fail with the error condition &#8220;operation not permitted&#8221;.</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>ATTACHING</code></font><code> A </code><font SIZE="-1"><code>SECURITY</code></font><font SIZE="-1"><code>LABEL</code></font><font SIZE="-1"><code>TO</code></font><code> A XEND-MANAGED </code><font SIZE="-1"><code>DOMAIN</code></font> </p>
</dd><dl>
<dt>
</dt><dd> The addlabel subcommand supports labeling of domains that are managed by xend. This includes domains that are currently running, such as for example Domain-0, or those that are in a dormant state. Depending on the state of the system, it is possible that the new label is rejected. An example for a reason for the rejection of the relabeling of a domain would be if a domain is currently allowed to access its labeled resources but due to the new label would be prevented from accessing one or more of them. </dd>
<pre>
    xm addlabel dom_Fun mgt Domain-0
</pre>
<p> This changes the label of Domain-0 to dom_Fun under the condition that this new label of Domain-0 would not prevent any other domain from accessing its resources that are provided through Domain-0, such as for example network or block device access.</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>ATTACHING</code></font><code> A </code><font SIZE="-1"><code>SECURITY</code></font><font SIZE="-1"><code>LABEL</code></font><font SIZE="-1"><code>TO</code></font><code> A </code><font SIZE="-1"><code>RESOURCE</code></font> </p>
</dd><dl>
<dt>
</dt><dd> The <code>addlabel</code> subcommand can also be used to attach a security label to a resource. Following the home banking example from above, we can label a disk resource (e.g., a physical partition or a file) to make it accessible to the home banking domain. The example policy provides a resource label, res_LogicalDiskPartition1(hda1), that is compatible with the HomeBanking domain label. </dd>
<pre>
    xm addlabel &quot;res_LogicalDiskPartition1(hda1)&quot; res phy:hda6
</pre>
<p> After labeling this disk resource, it can be attached to the domain by adding a line to the domain configuration file. The line below attaches this disk to the domain at boot time. </p>
<pre>
    disk = [ 'phy:hda6,sda2,w' ]
</pre>
<p> Alternatively, the resource can be attached after booting the domain by using the <code>block-attach</code> subcommand. </p>
<pre>
    xm block-attach homebanking phy:hda6 sda2 w
</pre>
<p> Note that labeled resources cannot be used when security is turned off. Any attempt to use labeled resources with security turned off will result in a failure with a corresponding error message. The solution is to enable security or, if security is no longer desired, to remove the resource label using the <code>rmlabel</code> subcommand.</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>STARTING</code></font><font SIZE="-1"><code>AND</code></font><font SIZE="-1"><code>LISTING</code></font><font SIZE="-1"><code>LABELED</code></font><font SIZE="-1"><code>DOMAINS</code></font> </p>
<pre>
    xm create myconfig.xm
    xm list --label
      Name         ID ...  Time(s)  Label
      homebanking  23 ...      4.4  dom_HomeBanking
      Domain-0      0 ...   2658.8  dom_SystemManagement
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>LISTING</code></font><font SIZE="-1"><code>LABELED</code></font><font SIZE="-1"><code>RESOURCES</code></font> </p>
<pre>
    xm resources
      phy:hda6
            type: ACM
          policy: example.chwall_ste.client_v1
          label:  res_LogicalDiskPartition1(hda1)
      file:/xen/disk_image/disk.img
            type: ACM
          policy: example.chwall_ste.client_v1
          label:  res_LogicalDiskPartition2(hda2)
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<p> <font SIZE="-1"><code>POLICY</code></font><font SIZE="-1"><code>REPRESENTATIONS</code></font> </p>
</dd><dl>
<dt>
</dt><dd> We distinguish three representations of the Xen access control policy: the source <font SIZE="-1">XML</font> version, its binary counterpart, and a mapping representation that enables the tools to deterministically translate back and forth between label names of the <font SIZE="-1">XML</font> policy and label identifiers of the binary policy. All three versions must be kept consistent to achieve predictable security guarantees. </dd>
<p> The <font SIZE="-1">XML</font> version is the version that users are supposed to create or change, either by manually editing the <font SIZE="-1">XML</font> file or by using the Xen policy generation tool (<code>xensec_gen</code>). After changing the <font SIZE="-1">XML</font> file, run the <code>setpolicy</code> subcommand to ensure that the new policy is available to xend. Use, for example, the subcommand <code>activatepolicy</code> to activate the changes during the next system reboot. </p>
<p> The binary version of the policy is derived from the <font SIZE="-1">XML</font> policy by tokenizing the specified labels and is used inside Xen only. It is created with the <code>setpolicy</code> subcommand. Essentially, the binary version is much more compact than the <font SIZE="-1">XML</font> version and is easier to evaluate during access control decisions. </p>
<p> The mapping version of the policy is created during the XML-to-binary policy translation (<code>setpolicy</code>) and is used by xend and the management tools to translate between label names used as input to the tools and their binary identifiers (ssidrefs) used inside Xen.</dl>
</dl>
<dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code>xmdomain.cfg</code>(5), <code><a href="/docs/linux/man/1-xentop/">xentop</a></code>(1)</p>
<h2>AUTHOR</h2>
<pre>
  Sean Dague &lt;sean at dague dot net&gt;
  Daniel Stekloff &lt;dsteklof at us dot ibm dot com&gt;
  Reiner Sailer &lt;sailer at us dot ibm dot com&gt;
  Stefan Berger &lt;stefanb at us dot ibm dot com&gt;
</pre>
<h2>BUGS</h2>
