---
title: "futex(2)"
name: "futex"
section: "2"
letter: "f"
url: "/docs/linux/man/2-futex/"
description: "futex – fast user-space locking"
---

<h2 class="name">NAME</h2>
<p> futex &#8211; fast user-space locking </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/futex.h&gt;
#include &lt;stdint.h&gt;
#include &lt;sys/time.h&gt;
long futex(uint32_t *uaddr, int futex_op, uint32_t val,
           const struct timespec *timeout, /* or: uint32_t val2 */
           uint32_t *uaddr2, uint32_t val3);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>futex</code>() system call provides a method for waiting until a certain condition becomes true. It is typically used as a blocking construct in the context of shared-memory synchronization. When using futexes, the majority of the synchronization operations are performed in user space. A user-space program employs the <code>futex</code>() system call only when it is likely that the program has to block for a longer time until the condition becomes true. Other <code>futex</code>() operations can be used to wake any processes or threads waiting for a particular condition. </p>
<p> A futex is a 32-bit value&#8212;referred to below as a <i>futex word</i>&#8212;whose address is supplied to the <code>futex</code>() system call. (Futexes are 32 bits in size on all platforms, including 64-bit systems.) All futex operations are governed by this value. In order to share a futex between processes, the futex is placed in a region of shared memory, created using (for example) <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) or <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2). (Thus, the futex word may have different virtual addresses in different processes, but these addresses all refer to the same location in physical memory.) In a multithreaded program, it is sufficient to place the futex word in a global variable shared by all threads. </p>
<p> When executing a futex operation that requests to block a thread, the kernel will block only if the futex word has the value that the calling thread supplied (as one of the arguments of the <code>futex</code>() call) as the expected value of the futex word. The loading of the futex word&#8217;s value, the comparison of that value with the expected value, and the actual blocking will happen atomically and will be totally ordered with respect to concurrent operations performed by other threads on the same futex word. Thus, the futex word is used to connect the synchronization in user space with the implementation of blocking by the kernel. Analogously to an atomic compare-and-exchange operation that potentially changes shared memory, blocking via a futex is an atomic compare-and-block operation. </p>
<p> One use of futexes is for implementing locks. The state of the lock (i.e., acquired or not acquired) can be represented as an atomically accessed flag in shared memory. In the uncontended case, a thread can access or modify the lock state with atomic instructions, for example atomically changing it from not acquired to acquired using an atomic compare-and-exchange instruction. (Such instructions are performed entirely in user mode, and the kernel maintains no information about the lock state.) On the other hand, a thread may be unable to acquire a lock because it is already acquired by another thread. It then may pass the lock&#8217;s flag as a futex word and the value representing the acquired state as the expected value to a <code>futex</code>() wait operation. This <code>futex</code>() operation will block if and only if the lock is still acquired (i.e., the value in the futex word still matches the &quot;acquired state&quot;). When releasing the lock, a thread has to first reset the lock state to not acquired and then execute a futex operation that wakes threads blocked on the lock flag used as a futex word (this can be further optimized to avoid unnecessary wake-ups). See <code><a href="/docs/linux/man/7-futex/">futex</a></code>(7) for more detail on how to use futexes. </p>
<p> Besides the basic wait and wake-up futex functionality, there are further futex operations aimed at supporting more complex use cases. </p>
<p> Note that no explicit initialization or destruction is necessary to use futexes; the kernel maintains a futex (i.e., the kernel-internal implementation artifact) only while operations such as <code>FUTEX_WAIT</code>, described below, are being performed on a particular futex word.</p>
<h3>Arguments</h3>
<p> The <i>uaddr</i> argument points to the futex word. On all platforms, futexes are four-byte integers that must be aligned on a four-byte boundary. The operation to perform on the futex is specified in the <i>futex_op</i> argument; <i>val</i> is a value whose meaning and purpose depends on <i>futex_op</i>. </p>
<p> The remaining arguments (<i>timeout</i>, <i>uaddr2</i>, and <i>val3</i>) are required only for certain of the futex operations described below. Where one of these arguments is not required, it is ignored. </p>
<p> For several blocking operations, the <i>timeout</i> argument is a pointer to a <i>timespec</i> structure that specifies a timeout for the operation. However, notwithstanding the prototype shown above, for some operations, the least significant four bytes of this argument are instead used as an integer whose meaning is determined by the operation. For these operations, the kernel casts the <i>timeout</i> value first to <i>unsigned long,</i> then to <i>uint32_t</i>, and in the remainder of this page, this argument is referred to as <i>val2</i> when interpreted in this fashion. </p>
<p> Where it is required, the <i>uaddr2</i> argument is a pointer to a second futex word that is employed by the operation. </p>
<p> The interpretation of the final integer argument, <i>val3</i>, depends on the operation.</p>
<h3>Futex operations</h3>
<p> The <i>futex_op</i> argument consists of two parts: a command that specifies the operation to be performed, bitwise ORed with zero or more options that modify the behaviour of the operation. The options that may be included in <i>futex_op</i> are as follows:</p>
<dl>
<dt><code>FUTEX_PRIVATE_FLAG</code> (since Linux 2.6.22)</p>
<dd> This option bit can be employed with all futex operations. It tells the kernel that the futex is process-private and not shared with another process (i.e., it is being used for synchronization only between threads of the same process). This allows the kernel to make some additional performance optimizations.</p>
<dt>
<dd> As a convenience, <i>&lt;linux/futex.h&gt;</i> defines a set of constants with the suffix <code>_PRIVATE</code> that are equivalents of all of the operations listed below, but with the <code>FUTEX_PRIVATE_FLAG</code> ORed into the constant value. Thus, there are <code>FUTEX_WAIT_PRIVATE</code>, <code>FUTEX_WAKE_PRIVATE</code>, and so on.</p>
<dt><code>FUTEX_CLOCK_REALTIME</code> (since Linux 2.6.28)</p>
<dd> This option bit can be employed only with the <code>FUTEX_WAIT_BITSET</code>, <code>FUTEX_WAIT_REQUEUE_PI</code>, and (since Linux 4.5) <code>FUTEX_WAIT</code> operations.</p>
<dt>
<dd> If this option is set, the kernel measures the <i>timeout</i> against the <code>CLOCK_REALTIME</code> clock.</p>
<dt>
<dd> If this option is not set, the kernel measures the <i>timeout</i> against the <code>CLOCK_MONOTONIC</code> clock.</dl>
<p> The operation specified in <i>futex_op</i> is one of the following:</p>
<dl>
<dt><code>FUTEX_WAIT</code> (since Linux 2.6.0)</p>
<dd> This operation tests that the value at the futex word pointed to by the address <i>uaddr</i> still contains the expected value <i>val</i>, and if so, then sleeps waiting for a <code>FUTEX_WAKE</code> operation on the futex word. The load of the value of the futex word is an atomic memory access (i.e., using atomic machine instructions of the respective architecture). This load, the comparison with the expected value, and starting to sleep are performed atomically and totally ordered with respect to other futex operations on the same futex word. If the thread starts to sleep, it is considered a waiter on this futex word. If the futex value does not match <i>val</i>, then the call fails immediately with the error <code>EAGAIN</code>.</p>
<dt>
<dd> The purpose of the comparison with the expected value is to prevent lost wake-ups. If another thread changed the value of the futex word after the calling thread decided to block based on the prior value, and if the other thread executed a <code>FUTEX_WAKE</code> operation (or similar wake-up) after the value change and before this <code>FUTEX_WAIT</code> operation, then the calling thread will observe the value change and will not start to sleep.</p>
<dt>
<dd> If the <i>timeout</i> is not NULL, the structure it points to specifies a timeout for the wait. (This interval will be rounded up to the system clock granularity, and is guaranteed not to expire early.) The timeout is by default measured according to the <code>CLOCK_MONOTONIC</code> clock, but, since Linux 4.5, the <code>CLOCK_REALTIME</code> clock can be selected by specifying <code>FUTEX_CLOCK_REALTIME</code> in <i>futex_op</i>. If <i>timeout</i> is NULL, the call blocks indefinitely.</p>
<dt>
<dd> <i>Note</i>: for <code>FUTEX_WAIT</code>, <i>timeout</i> is interpreted as a <i>relative</i> value. This differs from other futex operations, where <i>timeout</i> is interpreted as an absolute value. To obtain the equivalent of <code>FUTEX_WAIT</code> with an absolute timeout, employ <code>FUTEX_WAIT_BITSET</code> with <i>val3</i> specified as <code>FUTEX_BITSET_MATCH_ANY</code>.</p>
<dt>
<dd> The arguments <i>uaddr2</i> and <i>val3</i> are ignored.</p>
<dt><code>FUTEX_WAKE</code> (since Linux 2.6.0)</p>
<dd> This operation wakes at most <i>val</i> of the waiters that are waiting (e.g., inside <code>FUTEX_WAIT</code>) on the futex word at the address <i>uaddr</i>. Most commonly, <i>val</i> is specified as either 1 (wake up a single waiter) or <code>INT_MAX</code> (wake up all waiters). No guarantee is provided about which waiters are awoken (e.g., a waiter with a higher scheduling priority is not guaranteed to be awoken in preference to a waiter with a lower priority).</p>
<dt>
<dd> The arguments <i>timeout</i>, <i>uaddr2</i>, and <i>val3</i> are ignored.</p>
<dt><code>FUTEX_FD</code> (from Linux 2.6.0 up to and including Linux 2.6.25)</p>
<dd> This operation creates a file descriptor that is associated with the futex at <i>uaddr</i>. The caller must close the returned file descriptor after use. When another process or thread performs a <code>FUTEX_WAKE</code> on the futex word, the file descriptor indicates as being readable with <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7)</p>
<dt>
<dd> The file descriptor can be used to obtain asynchronous notifications: if <i>val</i> is nonzero, then, when another process or thread executes a <code>FUTEX_WAKE</code>, the caller will receive the signal number that was passed in <i>val</i>.</p>
<dt>
<dd> The arguments <i>timeout</i>, <i>uaddr2</i>, and <i>val3</i> are ignored.</p>
<dt>
<dd> Because it was inherently racy, <code>FUTEX_FD</code> has been removed from Linux 2.6.26 onward.</p>
<dt><code>FUTEX_REQUEUE</code> (since Linux 2.6.0)</p>
<dd> This operation performs the same task as <code>FUTEX_CMP_REQUEUE</code> (see below), except that no check is made using the value in <i>val3</i>. (The argument <i>val3</i> is ignored.)</p>
<dt><code>FUTEX_CMP_REQUEUE</code> (since Linux 2.6.7)</p>
<dd> This operation first checks whether the location <i>uaddr</i> still contains the value <i>val3</i>. If not, the operation fails with the error <code>EAGAIN</code>. Otherwise, the operation wakes up a maximum of <i>val</i> waiters that are waiting on the futex at <i>uaddr</i>. If there are more than <i>val</i> waiters, then the remaining waiters are removed from the wait queue of the source futex at <i>uaddr</i> and added to the wait queue of the target futex at <i>uaddr2</i>. The <i>val2</i> argument specifies an upper limit on the number of waiters that are requeued to the futex at <i>uaddr2</i>.</p>
<dt>
<dd> The load from <i>uaddr</i> is an atomic memory access (i.e., using atomic machine instructions of the respective architecture). This load, the comparison with <i>val3</i>, and the requeueing of any waiters are performed atomically and totally ordered with respect to other operations on the same futex word.</p>
<dt>
<dd> Typical values to specify for <i>val</i> are 0 or 1. (Specifying <code>INT_MAX</code> is not useful, because it would make the <code>FUTEX_CMP_REQUEUE</code> operation equivalent to <code>FUTEX_WAKE</code>.) The limit value specified via <i>val2</i> is typically either 1 or <code>INT_MAX</code>. (Specifying the argument as 0 is not useful, because it would make the <code>FUTEX_CMP_REQUEUE</code> operation equivalent to <code>FUTEX_WAIT</code>.)</p>
<dt>
<dd> The <code>FUTEX_CMP_REQUEUE</code> operation was added as a replacement for the earlier <code>FUTEX_REQUEUE</code>. The difference is that the check of the value at <i>uaddr</i> can be used to ensure that requeueing happens only under certain conditions, which allows race conditions to be avoided in certain use cases.</p>
<dt>
<dd> Both <code>FUTEX_REQUEUE</code> and <code>FUTEX_CMP_REQUEUE</code> can be used to avoid &quot;thundering herd&quot; wake-ups that could occur when using <code>FUTEX_WAKE</code> in cases where all of the waiters that are woken need to acquire another futex. Consider the following scenario, where multiple waiter threads are waiting on B, a wait queue implemented using a futex:</p>
<dt>
<dd> lock(A) while (!check_value(V)) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unlock(A);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;block_on(B);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lock(A); }; unlock(A);</p>
<dt>
<dd> If a waker thread used <code>FUTEX_WAKE</code>, then all waiters waiting on B would be woken up, and they would all try to acquire lock A. However, waking all of the threads in this manner would be pointless because all except one of the threads would immediately block on lock A again. By contrast, a requeue operation wakes just one waiter and moves the other waiters to lock A, and when the woken waiter unlocks A then the next waiter can proceed.</p>
<dt><code>FUTEX_WAKE_OP</code> (since Linux 2.6.14)</p>
<dd> This operation was added to support some user-space use cases where more than one futex must be handled at the same time. The most notable example is the implementation of <code><a href="/docs/linux/man/3-pthread_cond_signal/">pthread_cond_signal</a></code>(3), which requires operations on two futexes, the one used to implement the mutex and the one used in the implementation of the wait queue associated with the condition variable. <code>FUTEX_WAKE_OP</code> allows such cases to be implemented without leading to high rates of contention and context switching.</p>
<dt>
<dd> The <code>FUTEX_WAKE_OP</code> operation is equivalent to executing the following code atomically and totally ordered with respect to other futex operations on any of the two supplied futex words:</p>
<dt>
<dd> uint32_t oldval = *(uint32_t *) uaddr2; *(uint32_t *) uaddr2 = oldval <i>op</i> <i>oparg</i>; futex(uaddr, FUTEX_WAKE, val, 0, 0, 0); if (oldval <i>cmp</i> <i>cmparg</i>)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;futex(uaddr2, FUTEX_WAKE, val2, 0, 0, 0);</p>
<dt>
<dd> In other words, <code>FUTEX_WAKE_OP</code> does the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> saves the original value of the futex word at <i>uaddr2</i> and performs an operation to modify the value of the futex at <i>uaddr2</i>; this is an atomic read-modify-write memory access (i.e., using atomic machine instructions of the respective architecture)</p>
<dt>*</p>
<dd> wakes up a maximum of <i>val</i> waiters on the futex for the futex word at <i>uaddr</i>; and</p>
<dt>*</p>
<dd> dependent on the results of a test of the original value of the futex word at <i>uaddr2</i>, wakes up a maximum of <i>val2</i> waiters on the futex for the futex word at <i>uaddr2</i>.</dl>
</dl>
<dt>
<dd> The operation and comparison that are to be performed are encoded in the bits of the argument <i>val3</i>. Pictorially, the encoding is:</p>
<dt>
<dd> +&#8212;+&#8212;+&#8212;&#8212;&#8212;&#8211;+&#8212;&#8212;&#8212;&#8211;+ |op |cmp| oparg | cmparg | +&#8212;+&#8212;+&#8212;&#8212;&#8212;&#8211;+&#8212;&#8212;&#8212;&#8211;+<br />
&nbsp;<wbr>&nbsp;4&nbsp;<wbr>&nbsp;<wbr>&nbsp;4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;==&nbsp;#&nbsp;of bits</p>
<dt>
<dd> Expressed in code, the encoding is:</p>
<dt>
<dd> #define FUTEX_OP(op, oparg, cmp, cmparg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(((op&nbsp;&amp;&nbsp;0xf)&nbsp;&lt;&lt;&nbsp;28)&nbsp;|&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;((cmp&nbsp;&amp;&nbsp;0xf)&nbsp;&lt;&lt;&nbsp;24)&nbsp;|&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;((oparg&nbsp;&amp;&nbsp;0xfff)&nbsp;&lt;&lt;&nbsp;12)&nbsp;|&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(cmparg&nbsp;&amp;&nbsp;0xfff))</p>
<dt>
<dd> In the above, <i>op</i> and <i>cmp</i> are each one of the codes listed below. The <i>oparg</i> and <i>cmparg</i> components are literal numeric values, except as noted below.</p>
<dt>
<dd> The <i>op</i> component has one of the following values:</p>
<dt>
<dd> FUTEX_OP_SET 0 /* uaddr2 = oparg; */ FUTEX_OP_ADD 1 /* uaddr2 += oparg; */ FUTEX_OP_OR 2 /* uaddr2 |= oparg; */ FUTEX_OP_ANDN 3 /* uaddr2 &amp;= ~oparg; */ FUTEX_OP_XOR 4 /* uaddr2 ha= oparg; */</p>
<dt>
<dd> In addition, bitwise ORing the following value into <i>op</i> causes <i>(1&nbsp;&lt;&lt;&nbsp;oparg)</i> to be used as the operand:</p>
<dt>
<dd> FUTEX_OP_ARG_SHIFT 8 /* Use (1 &lt;&lt; oparg) as operand */</p>
<dt>
<dd> The <i>cmp</i> field is one of the following:</p>
<dt>
<dd> FUTEX_OP_CMP_EQ 0 /* if (oldval == cmparg) wake */ FUTEX_OP_CMP_NE 1 /* if (oldval != cmparg) wake */ FUTEX_OP_CMP_LT 2 /* if (oldval &lt; cmparg) wake */ FUTEX_OP_CMP_LE 3 /* if (oldval &lt;= cmparg) wake */ FUTEX_OP_CMP_GT 4 /* if (oldval &gt; cmparg) wake */ FUTEX_OP_CMP_GE 5 /* if (oldval &gt;= cmparg) wake */</p>
<dt>
<dd> The return value of <code>FUTEX_WAKE_OP</code> is the sum of the number of waiters woken on the futex <i>uaddr</i> plus the number of waiters woken on the futex <i>uaddr2</i>.</p>
<dt><code>FUTEX_WAIT_BITSET</code> (since Linux 2.6.25)</p>
<dd> This operation is like <code>FUTEX_WAIT</code> except that <i>val3</i> is used to provide a 32-bit bit mask to the kernel. This bit mask, in which at least one bit must be set, is stored in the kernel-internal state of the waiter. See the description of <code>FUTEX_WAKE_BITSET</code> for further details.</p>
<dt>
<dd> If <i>timeout</i> is not NULL, the structure it points to specifies an absolute timeout for the wait operation. If <i>timeout</i> is NULL, the operation can block indefinitely.</p>
<dt>
<dd> The <i>uaddr2</i> argument is ignored.</p>
<dt><code>FUTEX_WAKE_BITSET</code> (since Linux 2.6.25)</p>
<dd> This operation is the same as <code>FUTEX_WAKE</code> except that the <i>val3</i> argument is used to provide a 32-bit bit mask to the kernel. This bit mask, in which at least one bit must be set, is used to select which waiters should be woken up. The selection is done by a bitwise AND of the &quot;wake&quot; bit mask (i.e., the value in <i>val3</i>) and the bit mask which is stored in the kernel-internal state of the waiter (the &quot;wait&quot; bit mask that is set using <code>FUTEX_WAIT_BITSET</code>). All of the waiters for which the result of the AND is nonzero are woken up; the remaining waiters are left sleeping.</p>
<dt>
<dd> The effect of <code>FUTEX_WAIT_BITSET</code> and <code>FUTEX_WAKE_BITSET</code> is to allow selective wake-ups among multiple waiters that are blocked on the same futex. However, note that, depending on the use case, employing this bit-mask multiplexing feature on a futex can be less efficient than simply using multiple futexes, because employing bit-mask multiplexing requires the kernel to check all waiters on a futex, including those that are not interested in being woken up (i.e., they do not have the relevant bit set in their &quot;wait&quot; bit mask).</p>
<dt>
<dd> The constant <code>FUTEX_BITSET_MATCH_ANY</code>, which corresponds to all 32 bits set in the bit mask, can be used as the <i>val3</i> argument for <code>FUTEX_WAIT_BITSET</code> and <code>FUTEX_WAKE_BITSET</code>. Other than differences in the handling of the <i>timeout</i> argument, the <code>FUTEX_WAIT</code> operation is equivalent to <code>FUTEX_WAIT_BITSET</code> with <i>val3</i> specified as <code>FUTEX_BITSET_MATCH_ANY</code>; that is, allow a wake-up by any waker. The <code>FUTEX_WAKE</code> operation is equivalent to <code>FUTEX_WAKE_BITSET</code> with <i>val3</i> specified as <code>FUTEX_BITSET_MATCH_ANY</code>; that is, wake up any waiter(s).</p>
<dt>
<dd> The <i>uaddr2</i> and <i>timeout</i> arguments are ignored.</dl>
<h3>Priority-inheritance futexes</h3>
<p> Linux supports priority-inheritance (PI) futexes in order to handle priority-inversion problems that can be encountered with normal futex locks. Priority inversion is the problem that occurs when a high-priority task is blocked waiting to acquire a lock held by a low-priority task, while tasks at an intermediate priority continuously preempt the low-priority task from the CPU. Consequently, the low-priority task makes no progress toward releasing the lock, and the high-priority task remains blocked. </p>
<p> Priority inheritance is a mechanism for dealing with the priority-inversion problem. With this mechanism, when a high-priority task becomes blocked by a lock held by a low-priority task, the priority of the low-priority task is temporarily raised to that of the high-priority task, so that it is not preempted by any intermediate level tasks, and can thus make progress toward releasing the lock. To be effective, priority inheritance must be transitive, meaning that if a high-priority task blocks on a lock held by a lower-priority task that is itself blocked by a lock held by another intermediate-priority task (and so on, for chains of arbitrary length), then both of those tasks (or more generally, all of the tasks in a lock chain) have their priorities raised to be the same as the high-priority task. </p>
<p> From a user-space perspective, what makes a futex PI-aware is a policy agreement (described below) between user space and the kernel about the value of the futex word, coupled with the use of the PI-futex operations described below. (Unlike the other futex operations described above, the PI-futex operations are designed for the implementation of very specific IPC mechanisms.) </p>
<p> The PI-futex operations described below differ from the other futex operations in that they impose policy on the use of the value of the futex word:</p>
<dl>
<dt>*</p>
<dd> If the lock is not acquired, the futex word&#8217;s value shall be 0.</p>
<dt>*</p>
<dd> If the lock is acquired, the futex word&#8217;s value shall be the thread ID (TID; see <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2)) of the owning thread.</p>
<dt>*</p>
<dd> If the lock is owned and there are threads contending for the lock, then the <code>FUTEX_WAITERS</code> bit shall be set in the futex word&#8217;s value; in other words, this value is:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FUTEX_WAITERS | TID</p>
<dt>
<dd> (Note that is invalid for a PI futex word to have no owner and <code>FUTEX_WAITERS</code> set.)</dl>
<p> With this policy in place, a user-space application can acquire an unacquired lock or release a lock using atomic instructions executed in user mode (e.g., a compare-and-swap operation such as <i>cmpxchg</i> on the x86 architecture). Acquiring a lock simply consists of using compare-and-swap to atomically set the futex word&#8217;s value to the caller&#8217;s TID if its previous value was 0. Releasing a lock requires using compare-and-swap to set the futex word&#8217;s value to 0 if the previous value was the expected TID. </p>
<p> If a futex is already acquired (i.e., has a nonzero value), waiters must employ the <code>FUTEX_LOCK_PI</code> operation to acquire the lock. If other threads are waiting for the lock, then the <code>FUTEX_WAITERS</code> bit is set in the futex value; in this case, the lock owner must employ the <code>FUTEX_UNLOCK_PI</code> operation to release the lock. </p>
<p> In the cases where callers are forced into the kernel (i.e., required to perform a <code>futex</code>() call), they then deal directly with a so-called RT-mutex, a kernel locking mechanism which implements the required priority-inheritance semantics. After the RT-mutex is acquired, the futex value is updated accordingly, before the calling thread returns to user space. </p>
<p> It is important to note that the kernel will update the futex word&#8217;s value prior to returning to user space. (This prevents the possibility of the futex word&#8217;s value ending up in an invalid state, such as having an owner but the value being 0, or having waiters but not having the <code>FUTEX_WAITERS</code> bit set.) </p>
<p> If a futex has an associated RT-mutex in the kernel (i.e., there are blocked waiters) and the owner of the futex/RT-mutex dies unexpectedly, then the kernel cleans up the RT-mutex and hands it over to the next waiter. This in turn requires that the user-space value is updated accordingly. To indicate that this is required, the kernel sets the <code>FUTEX_OWNER_DIED</code> bit in the futex word along with the thread ID of the new owner. User space can detect this situation via the presence of the <code>FUTEX_OWNER_DIED</code> bit and is then responsible for cleaning up the stale state left over by the dead owner. </p>
<p> PI futexes are operated on by specifying one of the values listed below in <i>futex_op</i>. Note that the PI futex operations must be used as paired operations and are subject to some additional requirements:</p>
<dl>
<dt>*</p>
<dd> <code>FUTEX_LOCK_PI</code> and <code>FUTEX_TRYLOCK_PI</code> pair with <code>FUTEX_UNLOCK_PI</code>. <code>FUTEX_UNLOCK_PI</code> must be called only on a futex owned by the calling thread, as defined by the value policy, otherwise the error <code>EPERM</code> results.</p>
<dt>*</p>
<dd> <code>FUTEX_WAIT_REQUEUE_PI</code> pairs with <code>FUTEX_CMP_REQUEUE_PI</code>. This must be performed from a non-PI futex to a distinct PI futex (or the error <code>EINVAL</code> results). Additionally, <i>val</i> (the number of waiters to be woken) must be 1 (or the error <code>EINVAL</code> results).</dl>
<p> The PI futex operations are as follows:</p>
<dl>
<dt><code>FUTEX_LOCK_PI</code> (since Linux 2.6.18)</p>
<dd> This operation is used after an attempt to acquire the lock via an atomic user-mode instruction failed because the futex word has a nonzero value&#8212;specifically, because it contained the (PID-namespace-specific) TID of the lock owner.</p>
<dt>
<dd> The operation checks the value of the futex word at the address <i>uaddr</i>. If the value is 0, then the kernel tries to atomically set the futex value to the caller&#8217;s TID. If the futex word&#8217;s value is nonzero, the kernel atomically sets the <code>FUTEX_WAITERS</code> bit, which signals the futex owner that it cannot unlock the futex in user space atomically by setting the futex value to 0. After that, the kernel:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Tries to find the thread which is associated with the owner TID.</p>
<dt>2.</p>
<dd> Creates or reuses kernel state on behalf of the owner. (If this is the first waiter, there is no kernel state for this futex, so kernel state is created by locking the RT-mutex and the futex owner is made the owner of the RT-mutex. If there are existing waiters, then the existing state is reused.)</p>
<dt>3.</p>
<dd> Attaches the waiter to the futex (i.e., the waiter is enqueued on the RT-mutex waiter list).</dl>
</dl>
<dt>
<dd> If more than one waiter exists, the enqueueing of the waiter is in descending priority order. (For information on priority ordering, see the discussion of the <code>SCHED_DEADLINE</code>, <code>SCHED_FIFO</code>, and <code>SCHED_RR</code> scheduling policies in <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).) The owner inherits either the waiter&#8217;s CPU bandwidth (if the waiter is scheduled under the <code>SCHED_DEADLINE</code> policy) or the waiter&#8217;s priority (if the waiter is scheduled under the <code>SCHED_RR</code> or <code>SCHED_FIFO</code> policy). This inheritance follows the lock chain in the case of nested locking and performs deadlock detection.</p>
<dt>
<dd> The <i>timeout</i> argument provides a timeout for the lock attempt. If <i>timeout</i> is not NULL, the structure it points to specifies an absolute timeout, measured against the <code>CLOCK_REALTIME</code> clock. If <i>timeout</i> is NULL, the operation will block indefinitely.</p>
<dt>
<dd> The <i>uaddr2</i>, <i>val</i>, and <i>val3</i> arguments are ignored.</p>
<dt><code>FUTEX_TRYLOCK_PI</code> (since Linux 2.6.18)</p>
<dd> This operation tries to acquire the lock at <i>uaddr</i>. It is invoked when a user-space atomic acquire did not succeed because the futex word was not 0.</p>
<dt>
<dd> Because the kernel has access to more state information than user space, acquisition of the lock might succeed if performed by the kernel in cases where the futex word (i.e., the state information accessible to use-space) contains stale state (<code>FUTEX_WAITERS</code> and/or <code>FUTEX_OWNER_DIED</code>). This can happen when the owner of the futex died. User space cannot handle this condition in a race-free manner, but the kernel can fix this up and acquire the futex.</p>
<dt>
<dd> The <i>uaddr2</i>, <i>val</i>, <i>timeout</i>, and <i>val3</i> arguments are ignored.</p>
<dt><code>FUTEX_UNLOCK_PI</code> (since Linux 2.6.18)</p>
<dd> This operation wakes the top priority waiter that is waiting in <code>FUTEX_LOCK_PI</code> on the futex address provided by the <i>uaddr</i> argument.</p>
<dt>
<dd> This is called when the user-space value at <i>uaddr</i> cannot be changed atomically from a TID (of the owner) to 0.</p>
<dt>
<dd> The <i>uaddr2</i>, <i>val</i>, <i>timeout</i>, and <i>val3</i> arguments are ignored.</p>
<dt><code>FUTEX_CMP_REQUEUE_PI</code> (since Linux 2.6.31)</p>
<dd> This operation is a PI-aware variant of <code>FUTEX_CMP_REQUEUE</code>. It requeues waiters that are blocked via <code>FUTEX_WAIT_REQUEUE_PI</code> on <i>uaddr</i> from a non-PI source futex (<i>uaddr</i>) to a PI target futex (<i>uaddr2</i>).</p>
<dt>
<dd> As with <code>FUTEX_CMP_REQUEUE</code>, this operation wakes up a maximum of <i>val</i> waiters that are waiting on the futex at <i>uaddr</i>. However, for <code>FUTEX_CMP_REQUEUE_PI</code>, <i>val</i> is required to be 1 (since the main point is to avoid a thundering herd). The remaining waiters are removed from the wait queue of the source futex at <i>uaddr</i> and added to the wait queue of the target futex at <i>uaddr2</i>.</p>
<dt>
<dd> The <i>val2</i> and <i>val3</i> arguments serve the same purposes as for <code>FUTEX_CMP_REQUEUE</code>.</p>
<dt><code>FUTEX_WAIT_REQUEUE_PI</code> (since Linux 2.6.31)</p>
<dd> Wait on a non-PI futex at <i>uaddr</i> and potentially be requeued (via a <code>FUTEX_CMP_REQUEUE_PI</code> operation in another task) onto a PI futex at <i>uaddr2</i>. The wait operation on <i>uaddr</i> is the same as for <code>FUTEX_WAIT</code>.</p>
<dt>
<dd> The waiter can be removed from the wait on <i>uaddr</i> without requeueing on <i>uaddr2</i> via a <code>FUTEX_WAKE</code> operation in another task. In this case, the <code>FUTEX_WAIT_REQUEUE_PI</code> operation fails with the error <code>EAGAIN</code>.</p>
<dt>
<dd> If <i>timeout</i> is not NULL, the structure it points to specifies an absolute timeout for the wait operation. If <i>timeout</i> is NULL, the operation can block indefinitely.</p>
<dt>
<dd> The <i>val3</i> argument is ignored.</p>
<dt>
<dd> The <code>FUTEX_WAIT_REQUEUE_PI</code> and <code>FUTEX_CMP_REQUEUE_PI</code> were added to support a fairly specific use case: support for priority-inheritance-aware POSIX threads condition variables. The idea is that these operations should always be paired, in order to ensure that user space and the kernel remain in sync. Thus, in the <code>FUTEX_WAIT_REQUEUE_PI</code> operation, the user-space application pre-specifies the target of the requeue that takes place in the <code>FUTEX_CMP_REQUEUE_PI</code> operation.</dl>
<h2>RETURN VALUE</h2>
<p> In the event of an error (and assuming that <code>futex</code>() was invoked via <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2)), all operations return -1 and set <i>errno</i> to indicate the cause of the error. </p>
<p> The return value on success depends on the operation, as described in the following list:</p>
<dl>
<dt><code>FUTEX_WAIT</code></p>
<dd> Returns 0 if the caller was woken up. Note that a wake-up can also be caused by common futex usage patterns in unrelated code that happened to have previously used the futex word&#8217;s memory location (e.g., typical futex-based implementations of Pthreads mutexes can cause this under some conditions). Therefore, callers should always conservatively assume that a return value of 0 can mean a spurious wake-up, and use the futex word&#8217;s value (i.e., the user-space synchronization scheme) to decide whether to continue to block or not.</p>
<dt><code>FUTEX_WAKE</code></p>
<dd> Returns the number of waiters that were woken up.</p>
<dt><code>FUTEX_FD</code></p>
<dd> Returns the new file descriptor associated with the futex.</p>
<dt><code>FUTEX_REQUEUE</code></p>
<dd> Returns the number of waiters that were woken up.</p>
<dt><code>FUTEX_CMP_REQUEUE</code></p>
<dd> Returns the total number of waiters that were woken up or requeued to the futex for the futex word at <i>uaddr2</i>. If this value is greater than <i>val</i>, then the difference is the number of waiters requeued to the futex for the futex word at <i>uaddr2</i>.</p>
<dt><code>FUTEX_WAKE_OP</code></p>
<dd> Returns the total number of waiters that were woken up. This is the sum of the woken waiters on the two futexes for the futex words at <i>uaddr</i> and <i>uaddr2</i>.</p>
<dt><code>FUTEX_WAIT_BITSET</code></p>
<dd> Returns 0 if the caller was woken up. See <code>FUTEX_WAIT</code> for how to interpret this correctly in practice.</p>
<dt><code>FUTEX_WAKE_BITSET</code></p>
<dd> Returns the number of waiters that were woken up.</p>
<dt><code>FUTEX_LOCK_PI</code></p>
<dd> Returns 0 if the futex was successfully locked.</p>
<dt><code>FUTEX_TRYLOCK_PI</code></p>
<dd> Returns 0 if the futex was successfully locked.</p>
<dt><code>FUTEX_UNLOCK_PI</code></p>
<dd> Returns 0 if the futex was successfully unlocked.</p>
<dt><code>FUTEX_CMP_REQUEUE_PI</code></p>
<dd> Returns the total number of waiters that were woken up or requeued to the futex for the futex word at <i>uaddr2</i>. If this value is greater than <i>val</i>, then difference is the number of waiters requeued to the futex for the futex word at <i>uaddr2</i>.</p>
<dt><code>FUTEX_WAIT_REQUEUE_PI</code></p>
<dd> Returns 0 if the caller was successfully requeued to the futex for the futex word at <i>uaddr2</i>.</dl>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> No read access to the memory of a futex word.</p>
<dt><code>EAGAIN</code></p>
<dd> (<code>FUTEX_WAIT</code>, <code>FUTEX_WAIT_BITSET</code>, <code>FUTEX_WAIT_REQUEUE_PI</code>) The value pointed to by <i>uaddr</i> was not equal to the expected value <i>val</i> at the time of the call.</p>
<dt>
<dd> <code>Note</code>: on Linux, the symbolic names <code>EAGAIN</code> and <code>EWOULDBLOCK</code> (both of which appear in different parts of the kernel futex code) have the same value.</p>
<dt><code>EAGAIN</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE</code>, <code>FUTEX_CMP_REQUEUE_PI</code>) The value pointed to by <i>uaddr</i> is not equal to the expected value <i>val3</i>.</p>
<dt><code>EAGAIN</code></p>
<dd> (<code>FUTEX_LOCK_PI</code>, <code>FUTEX_TRYLOCK_PI</code>, <code>FUTEX_CMP_REQUEUE_PI</code>) The futex owner thread ID of <i>uaddr</i> (for <code>FUTEX_CMP_REQUEUE_PI</code>: <i>uaddr2</i>) is about to exit, but has not yet handled the internal state cleanup. Try again.</p>
<dt><code>EDEADLK</code></p>
<dd> (<code>FUTEX_LOCK_PI</code>, <code>FUTEX_TRYLOCK_PI</code>, <code>FUTEX_CMP_REQUEUE_PI</code>) The futex word at <i>uaddr</i> is already locked by the caller.</p>
<dt><code>EDEADLK</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE_PI</code>) While requeueing a waiter to the PI futex for the futex word at <i>uaddr2</i>, the kernel detected a deadlock.</p>
<dt><code>EFAULT</code></p>
<dd> A required pointer argument (i.e., <i>uaddr</i>, <i>uaddr2</i>, or <i>timeout</i>) did not point to a valid user-space address.</p>
<dt><code>EINTR</code></p>
<dd> A <code>FUTEX_WAIT</code> or <code>FUTEX_WAIT_BITSET</code> operation was interrupted by a signal (see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)). In kernels before Linux 2.6.22, this error could also be returned for a spurious wakeup; since Linux 2.6.22, this no longer happens.</p>
<dt><code>EINVAL</code></p>
<dd> The operation in <i>futex_op</i> is one of those that employs a timeout, but the supplied <i>timeout</i> argument was invalid (<i>tv_sec</i> was less than zero, or <i>tv_nsec</i> was not less than 1,000,000,000).</p>
<dt><code>EINVAL</code></p>
<dd> The operation specified in <i>futex_op</i> employs one or both of the pointers <i>uaddr</i> and <i>uaddr2</i>, but one of these does not point to a valid object&#8212;that is, the address is not four-byte-aligned.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_WAIT_BITSET</code>, <code>FUTEX_WAKE_BITSET</code>) The bit mask supplied in <i>val3</i> is zero.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE_PI</code>) <i>uaddr</i> equals <i>uaddr2</i> (i.e., an attempt was made to requeue to the same futex).</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_FD</code>) The signal number supplied in <i>val</i> is invalid.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_WAKE</code>, <code>FUTEX_WAKE_OP</code>, <code>FUTEX_WAKE_BITSET</code>, <code>FUTEX_REQUEUE</code>, <code>FUTEX_CMP_REQUEUE</code>) The kernel detected an inconsistency between the user-space state at <i>uaddr</i> and the kernel state&#8212;that is, it detected a waiter which waits in <code>FUTEX_LOCK_PI</code> on <i>uaddr</i>.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_LOCK_PI</code>, <code>FUTEX_TRYLOCK_PI</code>, <code>FUTEX_UNLOCK_PI</code>) The kernel detected an inconsistency between the user-space state at <i>uaddr</i> and the kernel state. This indicates either state corruption or that the kernel found a waiter on <i>uaddr</i> which is waiting via <code>FUTEX_WAIT</code> or <code>FUTEX_WAIT_BITSET</code>.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE_PI</code>) The kernel detected an inconsistency between the user-space state at <i>uaddr2</i> and the kernel state; that is, the kernel detected a waiter which waits via <code>FUTEX_WAIT</code> or <code>FUTEX_WAIT_BITSET</code> on <i>uaddr2</i>.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE_PI</code>) The kernel detected an inconsistency between the user-space state at <i>uaddr</i> and the kernel state; that is, the kernel detected a waiter which waits via <code>FUTEX_WAIT</code> or <code>FUTEX_WAIT_BITESET</code> on <i>uaddr</i>.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE_PI</code>) The kernel detected an inconsistency between the user-space state at <i>uaddr</i> and the kernel state; that is, the kernel detected a waiter which waits on <i>uaddr</i> via <code>FUTEX_LOCK_PI</code> (instead of <code>FUTEX_WAIT_REQUEUE_PI</code>).</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE_PI</code>) An attempt was made to requeue a waiter to a futex other than that specified by the matching <code>FUTEX_WAIT_REQUEUE_PI</code> call for that waiter.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE_PI</code>) The <i>val</i> argument is not 1.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid argument.</p>
<dt><code>ENFILE</code></p>
<dd> (<code>FUTEX_FD</code>) The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOMEM</code></p>
<dd> (<code>FUTEX_LOCK_PI</code>, <code>FUTEX_TRYLOCK_PI</code>, <code>FUTEX_CMP_REQUEUE_PI</code>) The kernel could not allocate memory to hold state information.</p>
<dt><code>ENOSYS</code></p>
<dd> Invalid operation specified in <i>futex_op</i>.</p>
<dt><code>ENOSYS</code></p>
<dd> The <code>FUTEX_CLOCK_REALTIME</code> option was specified in <i>futex_op</i>, but the accompanying operation was neither <code>FUTEX_WAIT</code>, <code>FUTEX_WAIT_BITSET</code>, nor <code>FUTEX_WAIT_REQUEUE_PI</code>.</p>
<dt><code>ENOSYS</code></p>
<dd> (<code>FUTEX_LOCK_PI</code>, <code>FUTEX_TRYLOCK_PI</code>, <code>FUTEX_UNLOCK_PI</code>, <code>FUTEX_CMP_REQUEUE_PI</code>, <code>FUTEX_WAIT_REQUEUE_PI</code>) A run-time check determined that the operation is not available. The PI-futex operations are not implemented on all architectures and are not supported on some CPU variants.</p>
<dt><code>EPERM</code></p>
<dd> (<code>FUTEX_LOCK_PI</code>, <code>FUTEX_TRYLOCK_PI</code>, <code>FUTEX_CMP_REQUEUE_PI</code>) The caller is not allowed to attach itself to the futex at <i>uaddr</i> (for <code>FUTEX_CMP_REQUEUE_PI</code>: the futex at <i>uaddr2</i>). (This may be caused by a state corruption in user space.)</p>
<dt><code>EPERM</code></p>
<dd> (<code>FUTEX_UNLOCK_PI</code>) The caller does not own the lock represented by the futex word.</p>
<dt><code>ESRCH</code></p>
<dd> (<code>FUTEX_LOCK_PI</code>, <code>FUTEX_TRYLOCK_PI</code>, <code>FUTEX_CMP_REQUEUE_PI</code>) The thread ID in the futex word at <i>uaddr</i> does not exist.</p>
<dt><code>ESRCH</code></p>
<dd> (<code>FUTEX_CMP_REQUEUE_PI</code>) The thread ID in the futex word at <i>uaddr2</i> does not exist.</p>
<dt><code>ETIMEDOUT</code></p>
<dd> The operation in <i>futex_op</i> employed the timeout specified in <i>timeout</i>, and the timeout expired before the operation completed.</dl>
<h2>VERSIONS</h2>
<p> Futexes were first made available in a stable kernel release with Linux 2.6.0. </p>
<p> Initial futex support was merged in Linux 2.5.7 but with different semantics from what was described above. A four-argument system call with the semantics described in this page was introduced in Linux 2.5.40. A fifth argument was added in Linux 2.5.70, and a sixth argument was added in Linux 2.6.7.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> Several higher-level programming abstractions are implemented via futexes, including POSIX semaphores and various POSIX threads synchronization mechanisms (mutexes, condition variables, read-write locks, and barriers).</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates use of futexes in a program where a parent process and a child process use a pair of futexes located inside a shared anonymous mapping to synchronize access to a shared resource: the terminal. The two processes each write <i>nloops</i> (a command-line argument that defaults to 5 if omitted) messages to the terminal and employ a synchronization protocol that ensures that they alternate in writing messages. Upon running this program we see output such as the following: </p>
<p> $ <code>./futex_demo</code> Parent (18534) 0 Child (18535) 0 Parent (18534) 1 Child (18535) 1 Parent (18534) 2 Child (18535) 2 Parent (18534) 3 Child (18535) 3 Parent (18534) 4 Child (18535) 4</p>
<h3>Program source</h3>
<p> /* futex_demo.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Usage: futex_demo&nbsp;[nloops]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(Default: 5) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Demonstrate the use of futexes in a program where parent and child<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;use a pair of futexes located inside a shared anonymous mapping to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;synchronize access to a shared resource: the terminal. The two<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;processes each write&nbsp;&#8216;num-loops&#8217;&nbsp;messages to the terminal and employ<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;a synchronization protocol that ensures that they alternate in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;writing messages. */ #define _GNU_SOURCE #include &lt;stdio.h&gt; #include &lt;errno.h&gt; #include &lt;stdatomic.h&gt; #include &lt;stdint.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;sys/wait.h&gt; #include &lt;sys/mman.h&gt; #include &lt;sys/syscall.h&gt; #include &lt;linux/futex.h&gt; #include &lt;sys/time.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static uint32_t *futex1, *futex2, *iaddr; </p>
<p> static int futex(uint32_t *uaddr, int futex_op, uint32_t val,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const struct timespec&nbsp;*timeout, uint32_t&nbsp;*uaddr2, uint32_t val3) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return syscall(SYS_futex, uaddr, futex_op, val,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;timeout, uaddr2, val3); } </p>
<p> /* Acquire the futex pointed to by &#8216;futexp&#8217;: wait for its value to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;become 1, and then set the value to 0.&nbsp;*/ </p>
<p> static void fwait(uint32_t *futexp) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long s; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;atomic_compare_exchange_strong(ptr, oldval, newval)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically performs the equivalent of: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(*ptr&nbsp;==&nbsp;*oldval)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*ptr&nbsp;=&nbsp;newval; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;It returns true if the test yielded true and&nbsp;*ptr was updated.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(1)&nbsp;{ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Is the futex available?&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const uint32_t one&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(atomic_compare_exchange_strong(futexp,&nbsp;&amp;one, 0))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Yes&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Futex is not available;&nbsp;wait&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;futex(futexp, FUTEX_WAIT, 0, NULL, NULL, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;==&nbsp;-1&nbsp;&amp;&amp;&nbsp;errno&nbsp;!=&nbsp;EAGAIN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;futex-FUTEX_WAIT&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} } </p>
<p> /* Release the futex pointed to by &#8216;futexp&#8217;: if the futex currently<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;has the value 0, set its value to 1 and the wake any futex waiters,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;so that if the peer is blocked in fwait(), it can proceed.&nbsp;*/ </p>
<p> static void fpost(uint32_t *futexp) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long s; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;atomic_compare_exchange_strong()&nbsp;was described<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in comments above&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const uint32_t zero&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(atomic_compare_exchange_strong(futexp,&nbsp;&amp;zero, 1))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;futex(futexp, FUTEX_WAKE, 1, NULL, NULL, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;<wbr>&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;futex-FUTEX_WAKE&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t childPid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nloops; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setbuf(stdout, NULL); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nloops&nbsp;=&nbsp;(argc&nbsp;&gt;&nbsp;1)&nbsp;?&nbsp;atoi(argv[1])&nbsp;: 5; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create a shared anonymous mapping that will hold the futexes.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since the futexes are being shared between processes, we<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;subsequently use the&nbsp;&quot;shared&quot;&nbsp;futex operations&nbsp;(i.e., not the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ones suffixed&nbsp;&quot;_PRIVATE&quot;)&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iaddr&nbsp;=&nbsp;mmap(NULL, sizeof(*iaddr)&nbsp;*&nbsp;2, PROT_READ | PROT_WRITE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MAP_ANONYMOUS | MAP_SHARED, -1, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(iaddr&nbsp;==&nbsp;MAP_FAILED)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mmap&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;futex1&nbsp;=&nbsp;&amp;iaddr[0];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;futex2&nbsp;=&nbsp;&amp;iaddr[1]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*futex1&nbsp;=&nbsp;0;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;State: unavailable&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*futex2&nbsp;=&nbsp;1;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;State: available&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create a child process that inherits the shared anonymous<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mapping&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;childPid&nbsp;=&nbsp;fork();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(childPid&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;fork&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(childPid&nbsp;==&nbsp;0)&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Child&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;nloops;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fwait(futex1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Child&nbsp;<wbr>&nbsp;(%jd)&nbsp;%d
&quot;,&nbsp;(intmax_t)&nbsp;getpid(), j);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpost(futex2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parent falls through to here&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;nloops;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fwait(futex2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Parent&nbsp;(%jd)&nbsp;%d
&quot;,&nbsp;(intmax_t)&nbsp;getpid(), j);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpost(futex1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wait(NULL); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2), <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2), <code><a href="/docs/linux/man/3-pthread_mutexattr_getprotocol/">pthread_mutexattr_getprotocol</a></code>(3), <code><a href="/docs/linux/man/7-futex/">futex</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7) </p>
<p> The following kernel source files:</p>
<dl>
<dt>*</p>
<dd> <i>Documentation/pi-futex.txt</i></p>
<dt>*</p>
<dd> <i>Documentation/futex-requeue-pi.txt</i></p>
<dt>*</p>
<dd> <i>Documentation/locking/rt-mutex.txt</i></p>
<dt>*</p>
<dd> <i>Documentation/locking/rt-mutex-design.txt</i></p>
<dt>*</p>
<dd> <i>Documentation/robust-futex-ABI.txt</i></dl>
<p> Franke, H., Russell, R., and Kirwood, M., 2002. <i>Fuss, Futexes and Furwocks: Fast Userlevel Locking in Linux</i> (from proceedings of the Ottawa Linux Symposium 2002), </p>
<p> Hart, D., 2009. <i>A futex overview and update</i>, </p>
<p> Hart, D. and Guniguntala, D., 2009. <i>Requeue-PI: Making Glibc Condvars PI-Aware</i> (from proceedings of the 2009 Real-Time Linux Workshop), </p>
<p> Drepper, U., 2011. <i>Futexes Are Tricky</i>, </p>
<p> Futex example library, futex-*.tar.bz2 at </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
