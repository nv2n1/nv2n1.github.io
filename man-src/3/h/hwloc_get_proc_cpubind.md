---
title: "hwloc_get_proc_cpubind(3)"
name: "hwloc_get_proc_cpubind"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_get_proc_cpubind/"
description: "hwlocality_cpubinding – CPU binding"
---

<h2 class="name">NAME</h2>
<p> hwlocality_cpubinding &#8211; CPU binding </p>
<h3>Enumerations</h3>
<p> enum <code>hwloc_cpubind_flags_t</code> { <code>HWLOC_CPUBIND_PROCESS</code>, <code>HWLOC_CPUBIND_THREAD</code>, <code>HWLOC_CPUBIND_STRICT</code>, <code>HWLOC_CPUBIND_NOMEMBIND</code> } </p>
<h3>Functions</h3>
<p> int <code>hwloc_set_cpubind</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, int flags) </p>
<p> int <code>hwloc_get_cpubind</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> set, int flags) </p>
<p> int <code>hwloc_set_proc_cpubind</code> (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_const_cpuset_t</code> set, int flags) </p>
<p> int <code>hwloc_get_proc_cpubind</code> (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_cpuset_t</code> set, int flags) </p>
<p> int <code>hwloc_set_thread_cpubind</code> (<code>hwloc_topology_t</code> topology, hwloc_thread_t thread, <code>hwloc_const_cpuset_t</code> set, int flags) </p>
<p> int <code>hwloc_get_thread_cpubind</code> (<code>hwloc_topology_t</code> topology, hwloc_thread_t thread, <code>hwloc_cpuset_t</code> set, int flags) </p>
<p> int <code>hwloc_get_last_cpu_location</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> set, int flags) </p>
<p> int <code>hwloc_get_proc_last_cpu_location</code> (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_cpuset_t</code> set, int flags) </p>
<h2>Detailed Description</h2>
<p> It is often useful to call <code>hwloc_bitmap_singlify()</code> first so that a single CPU remains in the set. This way, the process will not even migrate between different CPUs inside the given set. Some operating systems also only support that kind of binding. </p>
<p> Some operating systems do not provide all hwloc-supported mechanisms to bind processes, threads, etc. <code>hwloc_topology_get_support()</code> may be used to query about the actual CPU binding support in the currently used operating system. </p>
<p> When the requested binding operation is not available and the <code>HWLOC_CPUBIND_STRICT</code> flag was passed, the function returns -1. errno is set to ENOSYS when it is not possible to bind the requested kind of object processes/threads. errno is set to EXDEV when the requested cpuset can not be enforced (e.g. some systems only allow one CPU, and some other systems only allow one NUMA node). </p>
<p> If <code>HWLOC_CPUBIND_STRICT</code> was not passed, the function may fail as well, or the operating system may use a slightly different operation (with side-effects, smaller binding set, etc.) when the requested operation is not exactly supported. </p>
<p> The most portable version that should be preferred over the others, whenever possible, is the following one which just binds the current program, assuming it is single-threaded: </p>
<pre>
hwloc_set_cpubind(topology, set, 0),
</pre>
<p> If the program may be multithreaded, the following one should be preferred to only bind the current thread: </p>
<pre>
hwloc_set_cpubind(topology, set, HWLOC_CPUBIND_THREAD),
</pre>
<p> <code>See also:</code></p>
<dl>
<dt>
<dd> Some example codes are available under doc/examples/ in the source tree.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> To unbind, just call the binding function with either a full cpuset or a cpuset equal to the system cpuset. </p>
<p> On some operating systems, CPU binding may have effects on memory binding, see <code>HWLOC_CPUBIND_NOMEMBIND</code> </p>
<p> Running lstopo &#8211;top or hwloc-ps can be a very convenient tool to check how binding actually happened.</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_cpubind_flags_t</code></h3>
<p> Process/Thread binding flags. These bit flags can be used to refine the binding policy. </p>
<p> The default (0) is to bind the current process, assumed to be single-threaded, in a non-strict way. This is the most portable way to bind as all operating systems usually provide it. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Not all systems support all kinds of binding. See the &#8216;Detailed Description&#8217; section of <code>CPU binding</code> for a description of errors that can occur.</dl>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_CPUBIND_PROCESS </i></p>
<dd> Bind all threads of the current (possibly) multithreaded process.</p>
<dt><i>HWLOC_CPUBIND_THREAD </i></p>
<dd> Bind current thread of current process.</p>
<dt><i>HWLOC_CPUBIND_STRICT </i></p>
<dd> Request for strict binding from the OS. By default, when the designated CPUs are all busy while other CPUs are idle, operating systems may execute the thread/process on those other CPUs instead of the designated CPUs, to let them progress anyway. Strict binding means that the thread/process will _never_ execute on other cpus than the designated CPUs, even when those are busy with other tasks and other CPUs are idle.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Depending on the operating system, strict binding may not be possible (e.g., the OS does not implement it) or not allowed (e.g., for an administrative reasons), and the function will fail in that case.</dl>
<p> When retrieving the binding of a process, this flag checks whether all its threads actually have the same binding. If the flag is not given, the binding of each thread will be accumulated. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This flag is meaningless when retrieving the binding of a thread.</dl>
<dl>
<dt><i>HWLOC_CPUBIND_NOMEMBIND </i></p>
<dd> Avoid any effect on memory binding. On some operating systems, some CPU binding function would also bind the memory on the corresponding NUMA node. It is often not a problem for the application, but if it is, setting this flag will make hwloc avoid using OS functions that would also bind memory. This will however reduce the support of CPU bindings, i.e. potentially return -1 with errno set to ENOSYS in some cases.</dl>
<p> This flag is only meaningful when used with functions that set the CPU binding. It is ignored when used with functions that get CPU binding information.</p>
<h2>Function Documentation</h2>
<h3>int hwloc_get_cpubind (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> set, int flags)</h3>
<p> Get current process or thread binding. Writes into set the physical cpuset which the process or thread (according to <i>flags</i>) was last bound to.</p>
<h3>int hwloc_get_last_cpu_location (<code>hwloc_topology_t</code> topology, <code>hwloc_cpuset_t</code> set, int flags)</h3>
<p> Get the last physical CPU where the current process or thread ran. The operating system may move some tasks from one processor to another at any time according to their binding, so this function may return something that is already outdated. </p>
<p> flags can include either <code>HWLOC_CPUBIND_PROCESS</code> or <code>HWLOC_CPUBIND_THREAD</code> to specify whether the query should be for the whole process (union of all CPUs on which all threads are running), or only the current thread. If the process is single-threaded, flags can be set to zero to let hwloc use whichever method is available on the underlying OS.</p>
<h3>int hwloc_get_proc_cpubind (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_cpuset_t</code> set, int flags)</h3>
<p> Get the current physical binding of process pid. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_pid_t is pid_t on Unix platforms, and HANDLE on native Windows platforms. </p>
<p> As a special case on Linux, if a tid (thread ID) is supplied instead of a pid (process ID) and <code>HWLOC_CPUBIND_THREAD</code> is passed in flags, the binding for that specific thread is returned. </p>
<p> On non-Linux systems, <code>HWLOC_CPUBIND_THREAD</code> can not be used in flags.</dl>
<h3>int hwloc_get_proc_last_cpu_location (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_cpuset_t</code> set, int flags)</h3>
<p> Get the last physical CPU where a process ran. The operating system may move some tasks from one processor to another at any time according to their binding, so this function may return something that is already outdated. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_pid_t is pid_t on Unix platforms, and HANDLE on native Windows platforms. </p>
<p> As a special case on Linux, if a tid (thread ID) is supplied instead of a pid (process ID) and <code>HWLOC_CPUBIND_THREAD</code> is passed in flags, the last CPU location of that specific thread is returned. </p>
<p> On non-Linux systems, <code>HWLOC_CPUBIND_THREAD</code> can not be used in flags.</dl>
<h3>int hwloc_get_thread_cpubind (<code>hwloc_topology_t</code> topology, hwloc_thread_t thread, <code>hwloc_cpuset_t</code> set, int flags)</h3>
<p> Get the current physical binding of thread tid. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_thread_t is pthread_t on Unix platforms, and HANDLE on native Windows platforms. </p>
<p> <code>HWLOC_CPUBIND_PROCESS</code> can not be used in flags.</dl>
<h3>int hwloc_set_cpubind (<code>hwloc_topology_t</code> topology, <code>hwloc_const_cpuset_t</code> set, int flags)</h3>
<p> Bind current process or thread on cpus given in physical bitmap set. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 with errno set to ENOSYS if the action is not supported </p>
<p> -1 with errno set to EXDEV if the binding cannot be enforced</dl>
<h3>int hwloc_set_proc_cpubind (<code>hwloc_topology_t</code> topology, hwloc_pid_t pid, <code>hwloc_const_cpuset_t</code> set, int flags)</h3>
<p> Bind a process pid on cpus given in physical bitmap set. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_pid_t is pid_t on Unix platforms, and HANDLE on native Windows platforms. </p>
<p> As a special case on Linux, if a tid (thread ID) is supplied instead of a pid (process ID) and <code>HWLOC_CPUBIND_THREAD</code> is passed in flags, the binding is applied to that specific thread. </p>
<p> On non-Linux systems, <code>HWLOC_CPUBIND_THREAD</code> can not be used in flags.</dl>
<h3>int hwloc_set_thread_cpubind (<code>hwloc_topology_t</code> topology, hwloc_thread_t thread, <code>hwloc_const_cpuset_t</code> set, int flags)</h3>
<p> Bind a thread thread on cpus given in physical bitmap set. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> hwloc_thread_t is pthread_t on Unix platforms, and HANDLE on native Windows platforms. </p>
<p> <code>HWLOC_CPUBIND_PROCESS</code> can not be used in flags.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAQ">Author</a></p>
<dd></dl>
