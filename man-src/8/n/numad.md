---
title: "numad(8)"
name: "numad"
section: "8"
letter: "n"
url: "/docs/linux/man/8-numad/"
description: "numad – A user-level daemon that provides placement advice and process management for efficient use of CPUs and memory on systems with NUMA topology."
---

<p>numad &#8211; A user-level daemon that provides placement advice and process management for efficient use of CPUs and memory on systems with NUMA topology.</p>
<h2>Synopsis</h2>
<p>numad [<i>-dhvV</i>] </p>
<p> numad [<i>-C 0|1</i>] </p>
<p> numad [<i>-H THP_hugepage_scan_sleep_ms</i>] </p>
<p> numad [<i>-i [min_interval:]max_interval</i>] </p>
<p> numad [<i>-K 0|1</i>] </p>
<p> numad [<i>-l log_level</i>] </p>
<p> numad [<i>-m target_memory_locality</i>] </p>
<p> numad [<i>-p PID</i>] </p>
<p> numad [<i>-r PID</i>] </p>
<p> numad [<i>-R reserved-CPU-list</i>] </p>
<p> numad [<i>-S 0|1</i>] </p>
<p> numad [<i>-t logical_CPU_percent</i>] </p>
<p> numad [<i>-u target_utilization</i>] </p>
<p> numad [<i>-w NCPUS[:MB]</i>] </p>
<p> numad [<i>-x PID</i>]</p>
<h2>Description</h2>
<p>Numad is a system daemon that monitors NUMA topology and resource usage. It will attempt to locate processes for efficient NUMA locality and affinity, dynamically adjusting to changing system conditions. Numad also provides guidance to assist management applications with initial manual binding of CPU and memory resources for their processes. Note that numad is primarily intended for server consolidation environments, where there might be multiple applications or multiple virtual guests running on the same server system. Numad is most likely to have a positive effect when processes can be localized in a subset of the system&#8217;s NUMA nodes. If the entire system is dedicated to a large in-memory database application, for example &#8212; especially if memory accesses will likely remain unpredictable &#8212; numad will probably not improve performance.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code> &lt;<i>0|1</i>&gt;</p>
<dd>This option controls whether or not numad treats inactive file cache as available memory. By default, numad assumes it can count inactive file cache as &quot;free&quot; memory when considering resources to match with processes. Specify <i>-C 0</i> if numad should instead consider inactive file cache as a consumed resource.</p>
<dt><code>-d</code></p>
<dd>Debug output in log, sets the log level to LOG_DEBUG. Same effect as <i>-l 7</i>.</p>
<dt><code>-h</code></p>
<dd>Display usage help information and then exit.</p>
<dt><code>-H</code> &lt;<i>THP_scan_sleep_ms</i>&gt;</p>
<dd>Set the desired transparent hugepage scan interval in ms. The /sys/kernel/mm/tranparent_hugepage/khugepaged/scan_sleep_millisecs tunable is usually set to 10000ms by the operating system. The default is changed by numad to be 1000ms since it is helpful for the hugepage daemon to be more aggressive when memory moves between nodes. Specifying (<i>-H 0</i>) will cause numad to retain the system default value. You can also make the hugepage daemon more or less aggressive by specifying an alternate value with this option. For example, setting this value to 100ms (<i>-H 100</i>) might improve the performance of workloads which use many transparent hugepages.</p>
<dt><code>-i</code> &lt;<i>[min_interval:]max_interval</i>&gt;</p>
<dd>Sets the time interval that numad waits between system scans, in seconds to &lt;<i>max_interval</i>&gt;. Default &lt;<i>max_interval</i>&gt; is 15 seconds, default &lt;<i>min_interval</i>&gt; is 5 seconds. Setting a &lt;<i>max_interval</i>&gt; of zero will cause the daemon to exit. (This is the normal mechanism to terminate the daemon.) A bigger &lt;<i>max_interval</i>&gt; will decrease numad overhead but also decrease responsiveness to changing loads. The default numad max_interval can be changed in the numad.conf file.</p>
<dt><code>-K</code> &lt;<i>0|1</i>&gt;</p>
<dd>This option controls whether numad keeps interleaved memory spread across NUMA nodes, or attempts to merge interleaved memory to local NUMA nodes. The default is to merge interleaved memory. This is the appropriate setting to localize processes in a subset of the system&#8217;s NUMA nodes. If you are running a large, single-instance application that allocates interleaved memory because the workload will have continuous unpredictable memory access patterns (e.g. a large in-memory database), you might get better results by specifying <i>-K 1</i> to instruct numad to keep interleaved memory distributed.</p>
<dt><code>-l</code> &lt;<i>log_level</i>&gt;</p>
<dd>Sets the log level to &lt;<i>log_level</i>&gt;. Reasonable choices are 5, 6, or 7. The default value is 5. Note that CPU values are scaled by a factor of 100 internally and in the numad log files. Unfortunately, you don&#8217;t actually have that many CPUs.</p>
<dt><code>-m</code> &lt;<i>target_memory_locality</i>&gt;</p>
<dd>Set the desired memory locality threshold to stop moving process memory. Numad might stop retrying to coalesce process memory when more than this percentage of the process&#8217;s memory is already localized in the target node(s). The default is 90%. Numad will frequently localize more than the localization threshold percent, but it will not necessarily do so. Decrease the threshold to allow numad to leave more process memory distributed on various nodes. Increase the threshold to instruct numad to try to localize more memory. Acceptable values are between 50 and 100 percent. Note that setting the target memory locality to 100% might cause numad to continually retry to move memory that the kernel will never succesfully move.</p>
<dt><code>-p</code> &lt;<i>PID</i>&gt;</p>
<dd>Add PID to explicit inclusion list of processes to consider for managing, if the process also uses significant resources. Multiple <i>-p PID</i> options can be specified at daemon start, but after daemon start, only one PID can be added to the inclusion list per subsequent numad invocation. Use with -S to precisely control the scope of processes numad can manage. Note that the specified process will not necessarily be actively managed unless it also meets numad&#8217;s significance threshold &#8212; which is currently 300MB and half of a CPU.</p>
<dt><code>-r</code> &lt;<i>PID</i>&gt;</p>
<dd>Remove PID from both the explicit inclusion and the exclusion lists of processes. After daemon start, only one PID can be removed from the explicit process lists per subsequent numad invocation. Use with -S and -p and -x to precisely control the scope of processes numad can manage.</p>
<dt><code>-R</code> &lt;<i>CPU_LIST</i>&gt;</p>
<dd>Specify a list of CPUs that numad should assume are reserved for non-numad use. No processes will be bound to the specified CPUs by numad. This option is effective only when starting numad. You cannot change reserved CPUs dynamically while numad is already running.</p>
<dt><code>-S</code> &lt;<i>0|1</i>&gt;</p>
<dd>This option controls whether numad scans all system processes or only the processes on the explicit inclusion PID list. The default is to scan all processes. Use <i>-S 0</i> to scan only the explicit inclusion PID list. Use <i>-S 1</i> to again scan all system processes (excepting those on the explicit exclusion list). Starting numad as<br />
 <i>numad -S 0 -p &lt;PID-1&gt; -p &lt;PID-2&gt; -p &lt;PID-3&gt;</i><br />
 will limit scanning, and thus also automatic NUMA management, to only those three explicitly specified processes.</p>
<dt><code>-t</code> &lt;<i>logical_CPU_percent</i>&gt;</p>
<dd>Specify the resource value of logical CPUs. Hardware threads typically share most core resources, and so logical CPUs add only a fraction of CPU power for many workloads. By default numad considers logical CPUs to be only 20 percent of a dedicated hardware core.</p>
<dt><code>-u</code> &lt;<i>target_utilization</i>&gt;</p>
<dd>Set the desired maximum consumption percentage of a node. Default is 85%. Decrease the target value to maintain more available resource margin on each node. Increase the target value to more exhaustively consume node resources. If you have sized your workloads to precisely fit inside a NUMA node, specifying (<i>-u 100</i>) might improve system performance by telling numad to go ahead and consume all the resources in each node. It is possible to specify values up to 130 percent to oversubscribe CPUs in the nodes, but memory utilization is always capped at 100%. Use oversubscription values very carefully.</p>
<dt><code>-v</code></p>
<dd>Verbose output in log, sets the log level to LOG_INFO. Same effect as <i>-l 6</i>.</p>
<dt><code>-V</code></p>
<dd>Display version information and exit.</p>
<dt><code>-w</code> &lt;<i>NCPUS[:MB]</i>&gt;</p>
<dd>Queries numad for the best NUMA nodes to bind an entity that needs &lt;<i>NCPUS</i>&gt;. The amount of memory (in MBs) is optional, but should normally be specified as well &lt;<i>:MB</i>&gt; so numad can recommend NUMA nodes with available CPU capacity and adequate free memory. This query option can be used regardless of whether numad is running as a daemon. (An invocation using this option when numad is not running as a daemon, will not cause the daemon to start.) Output of this option is a string that contains a NUMA node list. For example: 2-3,6. The recommended node list could be saved in a shell variable (e.g., NODES) and then used as the node list parameter in a<br />
 <i>numactl -m $NODES -N $NODES &#8230; </i><br />
 command. See <a href="/docs/linux/man/8-numactl/">numactl</a>(8).</p>
<dt><code>-x</code> &lt;<i>PID</i>&gt;</p>
<dd>Add PID to explicit exclusion list of processes to blacklist from managing. Multiple <i>-x PID</i> options can be specified at daemon start, but after daemon start, only one PID can be added to the exclusion list per subsequent numad invocation. Use with -S to precisely control the scope of processes numad can manage.</dl>
<h2>Files</h2>
<p><i>/usr/bin/numad</i><br />
 <i>/etc/numad.conf</i><br />
 <i>/var/log/numad.log</i><br />
 <i>/var/run/numad.pid</i></p>
<h2>Environment Variables</h2>
<dl>
<dt>None.</p>
<dd></dl>
<h2>Examples</h2>
<p>Numad can be run as a system daemon and can be managed by the standard init mechanisms of the host. </p>
<p> If interactive (manual) control is desired, you can start the daemon manually by typing: </p>
<p> /usr/bin/numad </p>
<p> Subsequent numad invocations while the daemon is running can be used to dynamically change most run-time options. </p>
<p> You can terminate numad from running by typing: </p>
<p> /usr/bin/numad -i0</p>
<h2>Authors</h2>
<p>Bill Gray &lt;bgray [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-numactl/">numactl</a>(8) </p>
