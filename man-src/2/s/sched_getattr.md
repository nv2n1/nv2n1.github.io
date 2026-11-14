---
title: "sched_getattr(2)"
name: "sched_getattr"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sched_getattr/"
description: "sched_setattr, sched_getattr – set and get scheduling policy and attributes"
---

<h2 class="name">NAME</h2>
<p> sched_setattr, sched_getattr &#8211; set and get scheduling policy and attributes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sched.h&gt;
int sched_setattr(pid_t pid, struct sched_attr *attr,
                  unsigned int flags);
int sched_getattr(pid_t pid, struct sched_attr *attr,
                  unsigned int size, unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<h3>sched_setattr()</h3>
<p> The <code>sched_setattr</code>() system call sets the scheduling policy and associated attributes for the thread whose ID is specified in <i>pid</i>. If <i>pid</i> equals zero, the scheduling policy and attributes of the calling thread will be set. </p>
<p> Currently, Linux supports the following &quot;normal&quot; (i.e., non-real-time) scheduling policies as values that may be specified in <i>policy</i>:</p>
<dl>
<dt><code>SCHED_OTHER</code></p>
<dd> the standard round-robin time-sharing policy;</p>
<dt><code>SCHED_BATCH</code></p>
<dd> for &quot;batch&quot; style execution of processes; and</p>
<dt><code>SCHED_IDLE</code></p>
<dd> for running <i>very</i> low priority background jobs.</dl>
<p> Various &quot;real-time&quot; policies are also supported, for special time-critical applications that need precise control over the way in which runnable threads are selected for execution. For the rules governing when a process may use these policies, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). The real-time policies that may be specified in <i>policy</i> are:</p>
<dl>
<dt><code>SCHED_FIFO</code></p>
<dd> a first-in, first-out policy; and</p>
<dt><code>SCHED_RR</code></p>
<dd> a round-robin policy.</dl>
<p> Linux also provides the following policy:</p>
<dl>
<dt><code>SCHED_DEADLINE</code></p>
<dd> a deadline scheduling policy; see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) for details.</dl>
<p> The <i>attr</i> argument is a pointer to a structure that defines the new scheduling policy and attributes for the specified thread. This structure has the following form: </p>
<p> struct sched_attr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of this structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 sched_policy;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Policy&nbsp;(SCHED_*)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 sched_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s32 sched_nice;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Nice value&nbsp;(SCHED_OTHER,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SCHED_BATCH)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 sched_priority;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Static priority&nbsp;(SCHED_FIFO,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SCHED_RR)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Remaining fields are for SCHED_DEADLINE&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 sched_runtime;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 sched_deadline;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64 sched_period; }; </p>
<p> The fields of the <i>sched_attr</i> structure are as follows:</p>
<dl>
<dt><code>size</code></p>
<dd> This field should be set to the size of the structure in bytes, as in <i>sizeof(struct sched_attr)</i>. If the provided structure is smaller than the kernel structure, any additional fields are assumed to be &#8216;0&#8217;. If the provided structure is larger than the kernel structure, the kernel verifies that all additional fields are 0; if they are not, <code>sched_setattr</code>() fails with the error <code>E2BIG</code> and updates <i>size</i> to contain the size of the kernel structure.</p>
<dt>
<dd> The above behavior when the size of the user-space <i>sched_attr</i> structure does not match the size of the kernel structure allows for future extensibility of the interface. Malformed applications that pass oversize structures won&#8217;t break in the future if the size of the kernel <i>sched_attr</i> structure is increased. In the future, it could also allow applications that know about a larger user-space <i>sched_attr</i> structure to determine whether they are running on an older kernel that does not support the larger structure.</p>
<dt><i>sched_policy</i></p>
<dd> This field specifies the scheduling policy, as one of the <code>SCHED_*</code> values listed above.</p>
<dt><i>sched_flags</i></p>
<dd> This field contains zero or more of the following flags that are ORed together to control scheduling behavior:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>SCHED_FLAG_RESET_ON_FORK</code></p>
<dd> Children created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) do not inherit privileged scheduling policies. See <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) for details.</p>
<dt><code>SCHED_FLAG_RECLAIM</code> (since Linux 4.13)</p>
<dd> This flag allows a <code>SCHED_DEADLINE</code> thread to reclaim bandwidth unused by other real-time threads.</p>
<dt><code>SCHED_FLAG_DL_OVERRUN</code> (since Linux 4.16)</p>
<dd> This flag allows an application to get informed about run-time overruns in <code>SCHED_DEADLINE</code> threads. Such overruns may be caused by (for example) coarse execution time accounting or incorrect parameter assignment. Notification takes the form of a <code>SIGXCPU</code> signal which is generated on each overrun.</p>
<dt>
<dd> This <code>SIGXCPU</code> signal is <i>process-directed</i> (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)) rather than thread-directed. This is probably a bug. On the one hand, <code>sched_setattr</code>() is being used to set a per-thread attribute. On the other hand, if the process-directed signal is delivered to a thread inside the process other than the one that had a run-time overrun, the application has no way of knowing which thread overran.</dl>
</dl>
<dt><i>sched_nice</i></p>
<dd> This field specifies the nice value to be set when specifying <i>sched_policy</i> as <code>SCHED_OTHER</code> or <code>SCHED_BATCH</code>. The nice value is a number in the range -20 (high priority) to +19 (low priority); see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<dt><i>sched_priority</i></p>
<dd> This field specifies the static priority to be set when specifying <i>sched_policy</i> as <code>SCHED_FIFO</code> or <code>SCHED_RR</code>. The allowed range of priorities for these policies can be determined using <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2) and <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2). For other policies, this field must be specified as 0.</p>
<dt><i>sched_runtime</i></p>
<dd> This field specifies the &quot;Runtime&quot; parameter for deadline scheduling. The value is expressed in nanoseconds. This field, and the next two fields, are used only for <code>SCHED_DEADLINE</code> scheduling; for further details, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<dt><i>sched_deadline</i></p>
<dd> This field specifies the &quot;Deadline&quot; parameter for deadline scheduling. The value is expressed in nanoseconds.</p>
<dt><i>sched_period</i></p>
<dd> This field specifies the &quot;Period&quot; parameter for deadline scheduling. The value is expressed in nanoseconds.</dl>
<p> The <i>flags</i> argument is provided to allow for future extensions to the interface; in the current implementation it must be specified as 0.</p>
<h3>sched_getattr()</h3>
<p> The <code>sched_getattr</code>() system call fetches the scheduling policy and the associated attributes for the thread whose ID is specified in <i>pid</i>. If <i>pid</i> equals zero, the scheduling policy and attributes of the calling thread will be retrieved. </p>
<p> The <i>size</i> argument should be set to the size of the <i>sched_attr</i> structure as known to user space. The value must be at least as large as the size of the initially published <i>sched_attr</i> structure, or the call fails with the error <code>EINVAL</code>. </p>
<p> The retrieved scheduling attributes are placed in the fields of the <i>sched_attr</i> structure pointed to by <i>attr</i>. The kernel sets <i>attr.size</i> to the size of its <i>sched_attr</i> structure. </p>
<p> If the caller-provided <i>attr</i> buffer is larger than the kernel&#8217;s <i>sched_attr</i> structure, the additional bytes in the user-space structure are not touched. If the caller-provided structure is smaller than the kernel <i>sched_attr</i> structure, the kernel will silently not return any values which would be stored outside the provided space. As with <code>sched_setattr</code>(), these semantics allow for future extensibility of the interface. </p>
<p> The <i>flags</i> argument is provided to allow for future extensions to the interface; in the current implementation it must be specified as 0.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sched_setattr</code>() and <code>sched_getattr</code>() return 0. On error, -1 is returned, and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<p> <code>sched_getattr</code>() and <code>sched_setattr</code>() can both fail for the following reasons:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>attr</i> is NULL; or <i>pid</i> is negative; or <i>flags</i> is not zero.</p>
<dt><code>ESRCH</code></p>
<dd> The thread whose ID is <i>pid</i> could not be found.</dl>
<p> In addition, <code>sched_getattr</code>() can fail for the following reasons:</p>
<dl>
<dt><code>E2BIG</code></p>
<dd> The buffer specified by <i>size</i> and <i>attr</i> is too small.</p>
<dt><code>EINVAL</code></p>
<dd> <i>size</i> is invalid; that is, it is smaller than the initial version of the <i>sched_attr</i> structure (48 bytes) or larger than the system page size.</dl>
<p> In addition, <code>sched_setattr</code>() can fail for the following reasons:</p>
<dl>
<dt><code>E2BIG</code></p>
<dd> The buffer specified by <i>size</i> and <i>attr</i> is larger than the kernel structure, and one or more of the excess bytes is nonzero.</p>
<dt><code>EBUSY</code></p>
<dd> <code>SCHED_DEADLINE</code> admission control failure, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>attr.sched_policy</i> is not one of the recognized policies; <i>attr.sched_flags</i> contains a flag other than <code>SCHED_FLAG_RESET_ON_FORK</code>; or <i>attr.sched_priority</i> is invalid; or <i>attr.sched_policy</i> is <code>SCHED_DEADLINE</code> and the deadline scheduling parameters in <i>attr</i> are invalid.</p>
<dt><code>EPERM</code></p>
<dd> The caller does not have appropriate privileges.</p>
<dt><code>EPERM</code></p>
<dd> The CPU affinity mask of the thread specified by <i>pid</i> does not include all CPUs in the system (see <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2)).</dl>
<h2>VERSIONS</h2>
<p> These system calls first appeared in Linux 3.14.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are nonstandard Linux extensions.</p>
<h2>NOTES</h2>
<p> <code>sched_setattr</code>() provides a superset of the functionality of <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2), and (other than the ability to set the priority of all processes belonging to a specified user or all processes in a specified group) <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2). Analogously, <code>sched_getattr</code>() provides a superset of the functionality of <code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_getparam/">sched_getparam</a></code>(2), and (partially) <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2).</p>
<h2>BUGS</h2>
<p> In Linux versions up to 3.15, <code>sched_setattr</code>() failed with the error <code>EFAULT</code> instead of <code>E2BIG</code> for the case described in ERRORS. </p>
<p> In Linux versions up to 5.3, <code>sched_getattr</code>() failed with the error <code>EFBIG</code> if the in-kernel <i>sched_attr</i> structure was larger than the <i>size</i> passed by user space.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chrt/">chrt</a></code>(1), <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_max/">sched_get_priority_max</a></code>(2), <code><a href="/docs/linux/man/2-sched_get_priority_min/">sched_get_priority_min</a></code>(2), <code><a href="/docs/linux/man/2-sched_getaffinity/">sched_getaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_getparam/">sched_getparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_getscheduler/">sched_getscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_rr_get_interval/">sched_rr_get_interval</a></code>(2), <code><a href="/docs/linux/man/2-sched_setaffinity/">sched_setaffinity</a></code>(2), <code><a href="/docs/linux/man/2-sched_setparam/">sched_setparam</a></code>(2), <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2), <code><a href="/docs/linux/man/2-sched_yield/">sched_yield</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), <code><a href="/docs/linux/man/3-pthread_getschedparam/">pthread_getschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setschedparam/">pthread_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setschedprio/">pthread_setschedprio</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-cpuset/">cpuset</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
