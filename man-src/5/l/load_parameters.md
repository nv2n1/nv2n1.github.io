---
title: "load_parameters(5)"
name: "load_parameters"
section: "5"
letter: "l"
url: "/docs/linux/man/5-load_parameters/"
description: "load_parameters – xxQS_NAMExx default load parameters"
---

<p>load_parameters &#8211; xxQS_NAMExx default load parameters</p>
<h2>Description</h2>
<p>The load parameters reported by the execution daemon by default currently are:</p>
<dl>
<dt><code>arch</code></p>
<dd>An architecture string compiled into the sge_execd describing the operating system architecture for which the execd is targeted. Possible values include: </p>
<pre> aix51 for IBM AIX 5.1, 5.3
 darwin-x86 for Apple Mac OS/X x86
 darwin-ppc for Apple Mac OS/X PowerPC
 hp11 for HP HP-UX 11.x 32-bit
 hp11-64 for HP HP-UX 11.x 64-bit
 lx-amd64 for GNU/Linux x86_64
 lx-x86 for GNU/Linux x86
 sol-sparc64 for Sun Solaris Sparc64
 sol-x86 for Sun Solaris x86
 sol-amd64 for Sun Solaris x86_64
 win32-x86 for Windows x86</pre>
<p>Note that an sge_execd for a particular architecture may run on multiple OS versions. In this case, the architecture string delivered by the execution daemon may be misleading.</p>
<dt><code>num_proc</code></p>
<dd>The number of processors provided by the execution host. The host is defined by a single Internet address, i.e. rack mounted multi host systems are counted as a cluster rather than a single multi headed machine. In the case of &quot;hardware threads&quot; (&quot;CMT&quot; or &quot;SMT&quot;), normally num_proc is the number of such threads which are activated.</dl>
<p> The following load information is only available under IBM AIX if xxQS_NAMExx is built with the perfstat library (which is now the default):</p>
<dl>
<dt><code>load_short</code></p>
<dd>The short time average OS run queue length. It is the first of the value triple reported by <i><a href="/docs/linux/man/1-uptime/">uptime</a></i>(1). Many implementations provide a 1 minute average with this value.</p>
<dt><code>load_medium</code></p>
<dd>The medium time average OS run queue length. It is the second of the value triple reported by <i><a href="/docs/linux/man/1-uptime/">uptime</a></i>(1). Many implementations provide a 5 minute average with this value.</p>
<dt><code>load_long</code></p>
<dd>The long time average OS run queue length. It is the third of the value triple reported by <i><a href="/docs/linux/man/1-uptime/">uptime</a></i>(1). Many implementations provide a 10 or 15 minute average with this value.</p>
<dt><code>load_avg</code></p>
<dd>The same as load_medium.</p>
<dt><code>np_load_short</code></p>
<dd>The same as load_short but divided by the number of processors. This value allows comparing the load of single and multi-headed hosts.</p>
<dt><code>np_load_medium</code></p>
<dd>The same as load_medium but divided by the number of processors. This value allows comparing the load of single and multi-headed hosts.</p>
<dt><code>np_load_long</code></p>
<dd>The same as load_long but divided by the number of processors. This value allows comparing the load of single and multi-headed hosts.</p>
<dt><code>np_load_avg</code></p>
<dd>The same as load_avg but divided by the number of processors. This value allows comparing the load of single and multi-headed hosts.</p>
<dt><code>cpu</code></p>
<dd>The percentage of CPU time not in idle state.</dl>
<p> The following load information is only available under IBM AIX if xxQS_NAMExx is built with the perfstat library (which is now the default):</p>
<dl>
<dt><code>mem_free</code></p>
<dd>The amount of free real memory.</p>
<dt><code>swap_free</code></p>
<dd>The amount of free swap memory.</p>
<dt><code>virtual_free</code></p>
<dd>The sum of mem_free and swap_free.</p>
<dt><code>mem_used</code></p>
<dd>The amount of memory used.</p>
<dt><code>swap_used</code></p>
<dd>The amount of swap space used.</p>
<dt><code>virtual_used</code></p>
<dd>The sum of mem_used and swap_used.</p>
<dt><code>mem_total</code></p>
<dd>The total amount of memory (free+used).</p>
<dt><code>swap_total</code></p>
<dd>The total amount of swap space (free+used).</p>
<dt><code>virtual_total</code></p>
<dd>The sum of mem_total and swap_total.</dl>
<p> The following load information is ONLY available under Windows:</p>
<dl>
<dt><code>display_win_gui</code></p>
<dd>The host is capable of displaying the GUI of a Windows job.</dl>
<p> The following load information is only available if xxQS_NAMExx was built with the hwloc library (the default) and if hwloc supports the system.</p>
<dl>
<dt><code>m_topology_inuse</code></p>
<dd>The host cpu topology string reported by an execution host. This might be &quot;NONE&quot; if the topology cannot be determined; otherwise it is a string consisting of the upper and lowercase letters &quot;S&quot;, &quot;C&quot;, &quot;T&quot;, &quot;c&quot;, and &quot;t&quot;. The sequence of letters within that string represents the hardware topology where &quot;S&quot; represents a socket, &quot;C&quot; or &quot;c&quot; a core, and &quot;T&quot; or &quot;t&quot; a hardware thread. </p>
<p> The string &quot;SCCSCCSCCSCC&quot; will returned by a host that has 4 sockets where each of those sockets has two cores. All cores are available because all &quot;C&quot;s appear in capital letters. </p>
<p> If lowercase letters are used then this means that the corresponding core or thread is already in use because there is at least one running xxQS_NAMExx job bound to it. </p>
<p> &quot;SCCSCcSCCscc&quot; means that core 2 on socket 2 and also core 1 and core 2 on socket 4 are in use.</p>
<dt><code>m_topology</code></p>
<dd>Like m_topology_inuse, except that it represents the architecture, not the use of it, i.e. it doesn&#8217;t contain lower case letters.</p>
<dt><code>m_socket</code></p>
<dd>Number of sockets available on the reporting host (e.g. &quot;SCCSCCSCCSCC&quot; =&gt; m_socket=4)</p>
<dt><code>m_core</code></p>
<dd>Number of cores reported for all sockets on a host (e.g. &quot;SCCSCCSCCSCC&quot; =&gt; m_core=2)</p>
<dt><code>m_thread</code></p>
<dd>Number of hardware threads reported for all cores on a host, which should be equal to num_proc (e.g. &quot;SCTTCTTCTTCTT&quot; =&gt; m_thread=8)</dl>
<h3>Static Load Values</h3>
<p>The &quot;static&quot; load values (which may be selected with <code>qhost -l</code> or <code>qselect -l</code>) are: arch, num_proc, mem_total, swap_total, virtual_total, m_topology, m_socket, m_core, m_thread.</p>
<h2>See Also</h2>
