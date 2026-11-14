---
title: "sched_getaffinity(2)"
name: "sched_getaffinity"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sched_getaffinity/"
description: "sched_setaffinity, sched_getaffinity – set and get a thread’s CPU affinity mask"
---

<h2 class="name">NAME</h2>
<p> sched_setaffinity, sched_getaffinity &#8211; set and get a thread&#8217;s CPU affinity mask </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sched.h&gt;
int sched_setaffinity(pid_t pid, size_t cpusetsize,
                      const cpu_set_t *mask);
int sched_getaffinity(pid_t pid, size_t cpusetsize,
                      cpu_set_t *mask);
</code></pre>
<h2>DESCRIPTION</h2>
<p> A thread&#8217;s CPU affinity mask determines the set of CPUs on which it is eligible to run. On a multiprocessor system, setting the CPU affinity mask can be used to obtain performance benefits. For example, by dedicating one CPU to a particular thread (i.e., setting the affinity mask of that thread to specify a single CPU, and setting the affinity mask of all other threads to exclude that CPU), it is possible to ensure maximum execution speed for that thread. Restricting a thread to run on a single CPU also avoids the performance cost caused by the cache invalidation that occurs when a thread ceases to execute on one CPU and then recommences execution on a different CPU. </p>
<p> A CPU affinity mask is represented by the <i>cpu_set_t</i> structure, a &quot;CPU set&quot;, pointed to by <i>mask</i>. A set of macros for manipulating CPU sets is described in <code><a href="/docs/linux/man/3-cpu_set/">CPU_SET</a></code>(3). </p>
<p> <code>sched_setaffinity</code>() sets the CPU affinity mask of the thread whose ID is <i>pid</i> to the value specified by <i>mask</i>. If <i>pid</i> is zero, then the calling thread is used. The argument <i>cpusetsize</i> is the length (in bytes) of the data pointed to by <i>mask</i>. Normally this argument would be specified as <i>sizeof(cpu_set_t)</i>. </p>
<p> If the thread specified by <i>pid</i> is not currently running on one of the CPUs specified in <i>mask</i>, then that thread is migrated to one of the CPUs specified in <i>mask</i>. </p>
<p> <code>sched_getaffinity</code>() writes the affinity mask of the thread whose ID is <i>pid</i> into the <i>cpu_set_t</i> structure pointed to by <i>mask</i>. The <i>cpusetsize</i> argument specifies the size (in bytes) of <i>mask</i>. If <i>pid</i> is zero, then the mask of the calling thread is returned.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sched_setaffinity</code>() and <code>sched_getaffinity</code>() return 0 (but see &quot;C library/kernel differences&quot; below, which notes that the underlying <code>sched_getaffinity</code>() differs in its return value). On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> A supplied memory address was invalid.</p>
<dt><code>EINVAL</code></p>
<dd> The affinity bit mask <i>mask</i> contains no processors that are currently physically on the system and permitted to the thread according to any restrictions that may be imposed by <i>cpuset</i> cgroups or the &quot;cpuset&quot; mechanism described in <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> (<code>sched_getaffinity</code>() and, in kernels before 2.6.9, <code>sched_setaffinity</code>()) <i>cpusetsize</i> is smaller than the size of the affinity mask used by the kernel.</p>
<dt><code>EPERM</code></p>
<dd> (<code>sched_setaffinity</code>()) The calling thread does not have appropriate privileges. The caller needs an effective user ID equal to the real user ID or effective user ID of the thread identified by <i>pid</i>, or it must possess the <code>CAP_SYS_NICE</code> capability in the user namespace of the thread <i>pid</i>.</p>
<dt><code>ESRCH</code></p>
<dd> The thread whose ID is <i>pid</i> could not be found.</dl>
<h2>VERSIONS</h2>
<p> The CPU affinity system calls were introduced in Linux kernel 2.5.8. The system call wrappers were introduced in glibc 2.3. Initially, the glibc interfaces included a <i>cpusetsize</i> argument, typed as <i>unsigned int</i>. In glibc 2.3.3, the <i>cpusetsize</i> argument was removed, but was then restored in glibc 2.3.4, with type <i>size_t</i>.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>NOTES</h2>
<p> After a call to <code>sched_setaffinity</code>(), the set of CPUs on which the thread will actually run is the intersection of the set specified in the <i>mask</i> argument and the set of CPUs actually present on the system. The system may further restrict the set of CPUs on which the thread runs if the &quot;cpuset&quot; mechanism described in <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7) is being used. These restrictions on the actual set of CPUs on which the thread will run are silently imposed by the kernel. </p>
<p> There are various ways of determining the number of CPUs available on the system, including: inspecting the contents of <i>/proc/cpuinfo</i>; using <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3) to obtain the values of the <code>_SC_NPROCESSORS_CONF</code> and <code>_SC_NPROCESSORS_ONLN</code> parameters; and inspecting the list of CPU directories under <i>/sys/devices/system/cpu/</i>. </p>
<p> <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) has a description of the Linux scheduling scheme. </p>
<p> The affinity mask is a per-thread attribute that can be adjusted independently for each of the threads in a thread group. The value returned from a call to <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2) can be passed in the argument <i>pid</i>. Specifying <i>pid</i> as 0 will set the attribute for the calling thread, and passing the value returned from a call to <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2) will set the attribute for the main thread of the thread group. (If you are using the POSIX threads API, then use <code><a href="/docs/linux/man/3-pthread_setaffinity_np/">pthread_setaffinity_np</a></code>(3) instead of <code>sched_setaffinity</code>().) </p>
<p> The <i>isolcpus</i> boot option can be used to isolate one or more CPUs at boot time, so that no processes are scheduled onto those CPUs. Following the use of this boot option, the only way to schedule processes onto the isolated CPUs is via <code>sched_setaffinity</code>() or the <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7) mechanism. For further information, see the kernel source file <i>Documentation/admin-guide/kernel-parameters.txt</i>. As noted in that file, <i>isolcpus</i> is the preferred mechanism of isolating CPUs (versus the alternative of manually setting the CPU affinity of all processes on the system). </p>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s CPU affinity mask. The affinity mask is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h3>C library/kernel differences</h3>
<p> This manual page describes the glibc interface for the CPU affinity calls. The actual system call interface is slightly different, with the <i>mask</i> being typed as <i>unsigned long&nbsp;*</i>, reflecting the fact that the underlying implementation of CPU sets is a simple bit mask. </p>
<p> On success, the raw <code>sched_getaffinity</code>() system call returns the number of bytes placed copied into the <i>mask</i> buffer; this will be the minimum of <i>cpusetsize</i> and the size (in bytes) of the <i>cpumask_t</i> data type that is used internally by the kernel to represent the CPU set bit mask.</p>
<h3>Handling systems with large CPU affinity masks</h3>
<p> The underlying system calls (which represent CPU masks as bit masks of type <i>unsigned long&nbsp;*</i>) impose no restriction on the size of the CPU mask. However, the <i>cpu_set_t</i> data type used by glibc has a fixed size of 128 bytes, meaning that the maximum CPU number that can be represented is 1023. If the kernel CPU affinity mask is larger than 1024, then calls of the form: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sched_getaffinity(pid, sizeof(cpu_set_t),&nbsp;&amp;mask); </p>
<p> fail with the error <code>EINVAL</code>, the error produced by the underlying system call for the case where the <i>mask</i> size specified in <i>cpusetsize</i> is smaller than the size of the affinity mask used by the kernel. (Depending on the system CPU topology, the kernel affinity mask can be substantially larger than the number of active CPUs in the system.) </p>
<p> When working on systems with large kernel CPU affinity masks, one must dynamically allocate the <i>mask</i> argument (see <code><a href="/docs/linux/man/3-cpu_alloc/">CPU_ALLOC</a></code>(3)). Currently, the only way to do this is by probing for the size of the required mask using <code>sched_getaffinity</code>() calls with increasing mask sizes (until the call does not fail with the error <code>EINVAL</code>). </p>
<p> Be aware that <code><a href="/docs/linux/man/3-cpu_alloc/">CPU_ALLOC</a></code>(3) may allocate a slightly larger CPU set than requested (because CPU sets are implemented as bit masks allocated in units of <i>sizeof(long)</i>). Consequently, <code>sched_getaffinity</code>() can set bits beyond the requested allocation size, because the kernel sees a few additional bits. Therefore, the caller should iterate over the bits in the returned set, counting those which are set, and stop upon reaching the value returned by <code><a href="/docs/linux/man/3-cpu_count/">CPU_COUNT</a></code>(3) (rather than iterating over the number of bits requested to be allocated).</p>
<h2>EXAMPLES</h2>
<p> The program below creates a child process. The parent and child then each assign themselves to a specified CPU and execute identical loops that consume some CPU time. Before terminating, the parent waits for the child to complete. The program takes three command-line arguments: the CPU number for the parent, the CPU number for the child, and the number of loop iterations that both processes should perform. </p>
<p> As the sample runs below demonstrate, the amount of real and CPU time consumed when running the program will depend on intra-core caching effects and whether the processes are using the same CPU. </p>
<p> We first employ <code><a href="/docs/linux/man/1-lscpu/">lscpu</a></code>(1) to determine that this (x86) system has two cores, each with two CPUs: </p>
<p> $ <code>lscpu | egrep -i &#8216;core.*:|socket&#8217;</code> Thread(s) per core: 2 Core(s) per socket: 2 Socket(s): 1 </p>
<p> We then time the operation of the example program for three cases: both processes running on the same CPU; both processes running on different CPUs on the same core; and both processes running on different CPUs on different cores. </p>
<p> $ <code>time -p ./a.out 0 0 100000000</code> real 14.75 user 3.02 sys 11.73 $ <code>time -p ./a.out 0 1 100000000</code> real 11.52 user 3.98 sys 19.06 $ <code>time -p ./a.out 0 3 100000000</code> real 7.89 user 3.29 sys 12.07</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;sched.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;sys/wait.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cpu_set_t set;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int parentCPU, childCPU;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nloops; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;4)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s parent-cpu child-cpu num-loops
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parentCPU&nbsp;=&nbsp;atoi(argv[1]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;childCPU&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nloops&nbsp;=&nbsp;atoi(argv[3]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CPU_ZERO(&amp;set); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(fork())&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case -1:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Error&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;fork&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case 0:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Child&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CPU_SET(childCPU,&nbsp;&amp;set); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sched_setaffinity(getpid(), sizeof(set),&nbsp;&amp;set)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;sched_setaffinity&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;nloops;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;getppid(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parent&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CPU_SET(parentCPU,&nbsp;&amp;set); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sched_setaffinity(getpid(), sizeof(set),&nbsp;&amp;set)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;sched_setaffinity&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;nloops;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;getppid(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wait(NULL);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for child to terminate&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lscpu/">lscpu</a></code>(1), <code><a href="/docs/linux/man/1-nproc/">nproc</a></code>(1), <code><a href="/docs/linux/man/1-taskset/">taskset</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-getcpu/">getcpu</a></code>(2), <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2), <code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), <code><a href="/docs/linux/man/3-cpu_set/">CPU_SET</a></code>(3), <code><a href="/docs/linux/man/3-get_nprocs/">get_nprocs</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setaffinity_np/">pthread_setaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-sched_getcpu/">sched_getcpu</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
