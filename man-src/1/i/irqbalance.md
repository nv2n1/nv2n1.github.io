---
title: "irqbalance(1)"
name: "irqbalance"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irqbalance/"
description: "irqbalance – distribute hardware interrupts across processors on a multiprocessor system"
---

<h2 class="name">NAME</h2>
<p> irqbalance &#8211; distribute hardware interrupts across processors on a multiprocessor system </p>
<h2>SYNOPSIS</h2>
<pre>
<code>irqbalance</code>
</pre>
<h2>DESCRIPTION</h2>
<p> The purpose of <code>irqbalance</code> is to distribute hardware interrupts across processors on a multiprocessor system in order to increase performance. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o, &#8211;oneshot</code></p>
<dd> Causes irqbalance to be run once, after which the daemon exits.</p>
<dt>
<dd> <code>-d, &#8211;debug</code> Causes irqbalance to print extra debug information. Implies &#8211;foreground. </p>
<dt><code>-f, &#8211;foreground</code></p>
<dd> Causes irqbalance to run in the foreground (without &#8211;debug). </p>
<dt><code>-j, &#8211;journal</code></p>
<dd> Enables log output optimized for systemd-journal. </p>
<dt><code>-p, &#8211;powerthresh=&lt;threshold&gt;</code></p>
<dd> Set the threshold at which we attempt to move a CPU into powersave mode If more than &lt;threshold&gt; CPUs are more than 1 standard deviation below the average CPU softirq workload, and no CPUs are more than 1 standard deviation above (and have more than 1 IRQ assigned to them), attempt to place 1 CPU in powersave mode. In powersave mode, a CPU will not have any IRQs balanced to it, in an effort to prevent that CPU from waking up without need. </p>
<dt><code>-i, &#8211;banirq=&lt;irqnum&gt;</code></p>
<dd> Add the specified IRQ to the set of banned IRQs. irqbalance will not affect the affinity of any IRQs on the banned list, allowing them to be specified manually. This option is additive and can be specified multiple times. For example to ban IRQs 43 and 44 from balancing, use the following command line: <code>irqbalance &#8211;banirq=43 &#8211;banirq=44</code> </p>
<dt><code>-m, &#8211;banmod=&lt;module_name&gt;</code></p>
<dd> Add the specified module to the set of banned modules, similar to &#8211;banirq. irqbalance will not affect the affinity of any IRQs of given modules, allowing them to be specified manually. This option is additive and can be specified multiple times. For example to ban all IRQs of module foo and module bar from balancing, use the following command line: <code>irqbalance &#8211;banmod=foo &#8211;banmod=bar</code> </p>
<dt><code>-c, &#8211;deepestcache=&lt;integer&gt;</code></p>
<dd> This allows a user to specify the cache level at which irqbalance partitions cache domains. Specifying a deeper cache may allow a greater degree of flexibility for irqbalance to assign IRQ affinity to achieve greater performance increases, but setting a cache depth too large on some systems (specifically where all CPUs on a system share the deepest cache level), will cause irqbalance to see balancing as unnecessary. <code>irqbalance &#8211;deepestcache=2</code></dl>
<p> The default value for deepestcache is 2. </p>
<dl>
<dt><code>-l, &#8211;policyscript=&lt;script&gt;</code></p>
<dd> When specified, the referenced script or directory will execute once for each discovered IRQ, with the sysfs device path and IRQ number passed as arguments. Note that the device path argument will point to the parent directory from which the IRQ attributes directory may be directly opened. Policy scripts specified need to be owned and executable by the user of irqbalance process, if a directory is specified, non-executable files will be skipped. The script may specify zero or more key=value pairs that will guide irqbalance in the management of that IRQ. Key=value pairs are printed by the script on stdout and will be captured and interpreted by irqbalance. Irqbalance expects a zero exit code from the provided utility. Recognized key=value pairs are:</p>
<dt><i>ban=[true | false]</i></p>
<dd> Directs irqbalance to exclude the passed in IRQ from balancing.</p>
<dt><i>balance_level=[none | package | cache | core]</i></p>
<dd> This allows a user to override the balance level of a given IRQ. By default the balance level is determined automatically based on the pci device class of the device that owns the IRQ.</p>
<dt><i>numa_node=&lt;integer&gt;</i></p>
<dd> This allows a user to override the NUMA node that sysfs indicates a given device IRQ is local to. Often, systems will not specify this information in ACPI, and as a result devices are considered equidistant from all NUMA nodes in a system. This option allows for that hardware provided information to be overridden, so that irqbalance can bias IRQ affinity for these devices toward its most local node. Note that specifying a -1 here forces irqbalance to consider an interrupt from a device to be equidistant from all nodes.</p>
<dt>Note that, if a directory is specified rather than a regular file, all files in</p>
<dd> the directory will be considered policy scripts, and executed on adding of an irq to a database. If such a directory is specified, scripts in the directory must additionally exit with one of the following exit codes:</p>
<dt><i>0</i></p>
<dd> This indicates the script has a policy for the referenced irq, and that further script processing should stop</p>
<dt><i>1</i></p>
<dd> This indicates that the script has no policy for the referenced irq, and that script processing should continue</p>
<dt><i>2</i></p>
<dd> This indicates that an error has occurred in the script, and it should be skipped (further processing to continue) </p>
<dt><code>-s, &#8211;pid=&lt;file&gt;</code></p>
<dd> Have irqbalance write its process id to the specified file. By default no pidfile is written. The written pidfile is automatically unlinked when irqbalance exits. It is ignored when used with &#8211;debug or &#8211;foreground.</p>
<dt><code>-t, &#8211;interval=&lt;time&gt;</code></p>
<dd> Set the measurement time for irqbalance. irqbalance will sleep for &lt;time&gt; seconds between samples of the irq load on the system cpus. Defaults to 10.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>IRQBALANCE_ONESHOT</code></p>
<dd> Same as &#8211;oneshot. </p>
<dt><code>IRQBALANCE_DEBUG</code></p>
<dd> Same as &#8211;debug. </p>
<dt><code>IRQBALANCE_BANNED_CPUS</code></p>
<dd> Provides a mask of CPUs which irqbalance should ignore and never assign interrupts to. If not specified, irqbalance use mask of isolated and adaptive-ticks CPUs on the system as the default value. This is a hexmask without the leading ’0x’. On systems with large numbers of processors, each group of eight hex digits is separated by a comma ’,’. i.e. ‘export IRQBALANCE_BANNED_CPUS=fc0‘ would prevent irqbalance from assigning irqs to the 7th-12th cpus (cpu6-cpu11) or ‘export IRQBALANCE_BANNED_CPUS=ff000000,00000001‘ would prevent irqbalance from assigning irqs to the 1st (cpu0) and 57th-64th cpus (cpu56-cpu63). Notes: This environment variable will be discarded, please use IRQBALANCE_BANNED_CPULIST instead. Before deleting this environment variable, Introduce a deprecation period first for the consider of compatibility. </p>
<dt><code>IRQBALANCE_BANNED_CPULIST</code></p>
<dd> Provides a cpulist which irqbalance should ignore and never assign interrupts to. If not specified, irqbalance use mask of isolated and adaptive-ticks CPUs on the system as the default value. </p>
</dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGHUP</code></p>
<dd> Forces a rescan of the available IRQs and system topology. </p>
</dl>
<h2>API</h2>
<p> irqbalance is able to communicate via socket and return it&#8217;s current assignment tree and setup, as well as set new settings based on sent values. Socket is abstract, with a name in form of <code>irqbalance&lt;PID&gt;.sock</code> , where &lt;PID&gt; is the process ID of irqbalance instance to communicate with. Possible values to send:</p>
<dl>
<dt><code>stats</code></p>
<dd> Retrieve assignment tree of IRQs to CPUs, in recursive manner. For each CPU node in tree, it&#8217;s type, number, load and whether the save mode is active are sent. For each assigned IRQ type, it&#8217;s number, load, number of IRQs since last rebalancing and it&#8217;s class are sent. Refer to types.h file for explanation of defines.</p>
<dt><code>setup</code></p>
<dd> Get the current value of sleep interval, mask of banned CPUs and list of banned IRQs.</p>
<dt><code>settings sleep &lt;s&gt;</code></p>
<dd> Set new value of sleep interval, &lt;s&gt; &gt;= 1.</p>
<dt><code>settings cpus &lt;cpu_number1&gt; &lt;cpu_number2&gt; &#8230;</code></p>
<dd> Ban listed CPUs from IRQ handling, all old values of banned CPUs are forgotten.</p>
<dt><code>settings ban irqs &lt;irq1&gt; &lt;irq2&gt; &#8230;</code></p>
<dd> Ban listed IRQs from being balanced, all old values of banned IRQs are forgotten.</dl>
<p> irqbalance checks SCM_CREDENTIALS of sender (only root user is allowed to interact). Based on chosen tools, ancillary message with credentials needs to be sent with request. </p>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="https://github.com/Irqbalance/irqbalance">https://github.com/Irqbalance/irqbalance</a> </p>
<h2>Index</h2>
