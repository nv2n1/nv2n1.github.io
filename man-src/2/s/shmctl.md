---
title: "shmctl(2)"
name: "shmctl"
section: "2"
letter: "s"
url: "/docs/linux/man/2-shmctl/"
description: "shmctl – System V shared memory control"
---

<h2 class="name">NAME</h2>
<p> shmctl &#8211; System V shared memory control </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/ipc.h&gt;</code><br />
 <code>#include &lt;sys/shm.h&gt;</code> </p>
<p> <code>int shmctl(int </code><i>shmid</i><code>, int </code><i>cmd</i><code>, struct shmid_ds *</code><i>buf</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>shmctl</code>() performs the control operation specified by <i>cmd</i> on the System V shared memory segment whose identifier is given in <i>shmid</i>. </p>
<p> The <i>buf</i> argument is a pointer to a <i>shmid_ds</i> structure, defined in <i>&lt;sys/shm.h&gt;</i> as follows: </p>
<p> struct shmid_ds {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ipc_perm shm_perm;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ownership and permissions&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_segsz;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of segment&nbsp;(bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_atime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Last attach time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_dtime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Last detach time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_ctime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Creation time/time of last<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;modification via shmctl()&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_cpid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of creator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_lpid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of last&nbsp;<a href="/docs/linux/man/2-shmat/">shmat</a>(2)/<a href="/docs/linux/man/2-shmdt/">shmdt</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shmatt_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_nattch;&nbsp;<wbr>&nbsp;/*&nbsp;No. of current attaches&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230; }; </p>
<p> The fields of the <i>shmid_ds</i> structure are as follows:</p>
<dl>
<dt><i>shm_perm</i></p>
<dd> This is an <i>ipc_perm</i> structure (see below) that specifies the access permissions on the shared memory segment.</p>
<dt><i>shm_segsz</i></p>
<dd> Size in bytes of the shared memory segment.</p>
<dt><i>shm_atime</i></p>
<dd> Time of the last <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) system call that attached this segment.</p>
<dt><i>shm_dtime</i></p>
<dd> Time of the last <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2) system call that detached tgis segment.</p>
<dt><i>shm_ctime</i></p>
<dd> Time of creation of segment or time of the last <code>shmctl</code>() <code>IPC_SET</code> operation.</p>
<dt><i>shm_cpid</i></p>
<dd> ID of the process that created the shared memory segment.</p>
<dt><i>shm_lpid</i></p>
<dd> ID of the last process that executed a <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) or <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2) system call on this segment.</p>
<dt><i>shm_nattch</i></p>
<dd> Number of processes that have this segment attached.</dl>
<p> The <i>ipc_perm</i> structure is defined as follows (the highlighted fields are settable using <code>IPC_SET</code>): </p>
<p> struct ipc_perm {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__key;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Key supplied to&nbsp;<a href="/docs/linux/man/2-shmget/">shmget</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>uid</code>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective UID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>gid</code>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective GID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cuid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective UID of creator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cgid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective GID of creator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<code>mode</code>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;<code>Permissions</code>&nbsp;+&nbsp;SHM_DEST and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SHM_LOCKED flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;__seq;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Sequence number&nbsp;*/ }; </p>
<p> The least significant 9 bits of the <i>mode</i> field of the <i>ipc_perm</i> structure define the access permissions for the shared memory segment. The permission bits are as follows: </p>
<table>
<tr VALIGN=top>
<td>0400</td>
<td>Read by user
</td>
</tr>
<tr VALIGN=top>
<td>0200</td>
<td>Write by user
</td>
</tr>
<tr VALIGN=top>
<td>0040</td>
<td>Read by group
</td>
</tr>
<tr VALIGN=top>
<td>0020</td>
<td>Write by group
</td>
</tr>
<tr VALIGN=top>
<td>0004</td>
<td>Read by others
</td>
</tr>
<tr VALIGN=top>
<td>0002</td>
<td>Write by others
</td>
</tr>
</table>
<p> Bits 0100, 0010, and 0001 (the execute bits) are unused by the system. (It is not necessary to have execute permission on a segment in order to perform a <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) call with the <code>SHM_EXEC</code> flag.) </p>
<p> Valid values for <i>cmd</i> are:</p>
<dl>
<dt><code>IPC_STAT</code></p>
<dd> Copy information from the kernel data structure associated with <i>shmid</i> into the <i>shmid_ds</i> structure pointed to by <i>buf</i>. The caller must have read permission on the shared memory segment.</p>
<dt><code>IPC_SET</code></p>
<dd> Write the values of some members of the <i>shmid_ds</i> structure pointed to by <i>buf</i> to the kernel data structure associated with this shared memory segment, updating also its <i>shm_ctime</i> member.</p>
<dt>
<dd> The following fields are updated: <i>shm_perm.uid</i>, <i>shm_perm.gid</i>, and (the least significant 9 bits of) <i>shm_perm.mode</i>.</p>
<dt>
<dd> The effective UID of the calling process must match the owner (<i>shm_perm.uid</i>) or creator (<i>shm_perm.cuid</i>) of the shared memory segment, or the caller must be privileged.</p>
<dt><code>IPC_RMID</code></p>
<dd> Mark the segment to be destroyed. The segment will actually be destroyed only after the last process detaches it (i.e., when the <i>shm_nattch</i> member of the associated structure <i>shmid_ds</i> is zero). The caller must be the owner or creator of the segment, or be privileged. The <i>buf</i> argument is ignored.</p>
<dt>
<dd> If a segment has been marked for destruction, then the (nonstandard) <code>SHM_DEST</code> flag of the <i>shm_perm.mode</i> field in the associated data structure retrieved by <code>IPC_STAT</code> will be set.</p>
<dt>
<dd> The caller <i>must</i> ensure that a segment is eventually destroyed; otherwise its pages that were faulted in will remain in memory or swap.</p>
<dt>
<dd> See also the description of <i>/proc/sys/kernel/shm_rmid_forced</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt><code>IPC_INFO</code> (Linux-specific)</p>
<dd> Return information about system-wide shared memory limits and parameters in the structure pointed to by <i>buf</i>. This structure is of type <i>shminfo</i> (thus, a cast is required), defined in <i>&lt;sys/shm.h&gt;</i> if the <code>_GNU_SOURCE</code> feature test macro is defined:</p>
<dt>
<dd> struct shminfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long shmmax;&nbsp;/*&nbsp;Maximum segment size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long shmmin;&nbsp;/*&nbsp;Minimum segment size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;always 1&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long shmmni;&nbsp;/*&nbsp;Maximum number of segments&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long shmseg;&nbsp;/*&nbsp;Maximum number of segments<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;that a process can attach;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unused within kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long shmall;&nbsp;/*&nbsp;Maximum number of pages of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shared memory, system-wide&nbsp;*/ };</p>
<dt>
<dd> The <i>shmmni</i>, <i>shmmax</i>, and <i>shmall</i> settings can be changed via <i>/proc</i> files of the same name; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for details.</p>
<dt><code>SHM_INFO</code> (Linux-specific)</p>
<dd> Return a <i>shm_info</i> structure whose fields contain information about system resources consumed by shared memory. This structure is defined in <i>&lt;sys/shm.h&gt;</i> if the <code>_GNU_SOURCE</code> feature test macro is defined:</p>
<dt>
<dd> struct shm_info {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;used_ids;&nbsp;/*&nbsp;#&nbsp;of currently existing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;segments&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long shm_tot;&nbsp;<wbr>&nbsp;/*&nbsp;Total number of shared<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory pages&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long shm_rss;&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of resident shared<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory pages&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long shm_swp;&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of swapped shared<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory pages&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long swap_attempts;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Unused since Linux 2.4&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long swap_successes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Unused since Linux 2.4&nbsp;*/ };</p>
<dt><code>SHM_STAT</code> (Linux-specific)</p>
<dd> Return a <i>shmid_ds</i> structure as for <code>IPC_STAT</code>. However, the <i>shmid</i> argument is not a segment identifier, but instead an index into the kernel&#8217;s internal array that maintains information about all shared memory segments on the system.</p>
<dt><code>SHM_STAT_ANY</code> (Linux-specific, since Linux 4.17)</p>
<dd> Return a <i>shmid_ds</i> structure as for <code>SHM_STAT</code>. However, <i>shm_perm.mode</i> is not checked for read access for <i>shmid</i>, meaning that any user can employ this operation (just as any user may read <i>/proc/sysvipc/shm</i> to obtain the same information).</dl>
<p> The caller can prevent or allow swapping of a shared memory segment with the following <i>cmd</i> values:</p>
<dl>
<dt><code>SHM_LOCK</code> (Linux-specific)</p>
<dd> Prevent swapping of the shared memory segment. The caller must fault in any pages that are required to be present after locking is enabled. If a segment has been locked, then the (nonstandard) <code>SHM_LOCKED</code> flag of the <i>shm_perm.mode</i> field in the associated data structure retrieved by <code>IPC_STAT</code> will be set.</p>
<dt><code>SHM_UNLOCK</code> (Linux-specific)</p>
<dd> Unlock the segment, allowing it to be swapped out.</dl>
<p> In kernels before 2.6.10, only a privileged process could employ <code>SHM_LOCK</code> and <code>SHM_UNLOCK</code>. Since kernel 2.6.10, an unprivileged process can employ these operations if its effective UID matches the owner or creator UID of the segment, and (for <code>SHM_LOCK</code>) the amount of memory to be locked falls within the <code>RLIMIT_MEMLOCK</code> resource limit (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)).</p>
<h2>RETURN VALUE</h2>
<p> A successful <code>IPC_INFO</code> or <code>SHM_INFO</code> operation returns the index of the highest used entry in the kernel&#8217;s internal array recording information about all shared memory segments. (This information can be used with repeated <code>SHM_STAT</code> or <code>SHM_STAT_ANY</code> operations to obtain information about all shared memory segments on the system.) A successful <code>SHM_STAT</code> operation returns the identifier of the shared memory segment whose index was given in <i>shmid</i>. Other operations return 0 on success. </p>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> <code>IPC_STAT</code> or <code>SHM_STAT</code> is requested and <i>shm_perm.mode</i> does not allow read access for <i>shmid</i>, and the calling process does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EFAULT</code></p>
<dd> The argument <i>cmd</i> has value <code>IPC_SET</code> or <code>IPC_STAT</code> but the address pointed to by <i>buf</i> isn&#8217;t accessible.</p>
<dt><code>EIDRM</code></p>
<dd> <i>shmid</i> points to a removed identifier.</p>
<dt><code>EINVAL</code></p>
<dd> <i>shmid</i> is not a valid identifier, or <i>cmd</i> is not a valid command. Or: for a <code>SHM_STAT</code> or <code>SHM_STAT_ANY</code> operation, the index value specified in <i>shmid</i> referred to an array slot that is currently unused.</p>
<dt><code>ENOMEM</code></p>
<dd> (In kernels since 2.6.9), <code>SHM_LOCK</code> was specified and the size of the to-be-locked segment would mean that the total bytes in locked shared memory segments would exceed the limit for the real user ID of the calling process. This limit is defined by the <code>RLIMIT_MEMLOCK</code> soft resource limit (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)).</p>
<dt><code>EOVERFLOW</code></p>
<dd> <code>IPC_STAT</code> is attempted, and the GID or UID value is too large to be stored in the structure pointed to by <i>buf</i>.</p>
<dt><code>EPERM</code></p>
<dd> <code>IPC_SET</code> or <code>IPC_RMID</code> is attempted, and the effective user ID of the calling process is not that of the creator (found in <i>shm_perm.cuid</i>), or the owner (found in <i>shm_perm.uid</i>), and the process was not privileged (Linux: did not have the <code>CAP_SYS_ADMIN</code> capability).</p>
<dt>
<dd> Or (in kernels before 2.6.9), <code>SHM_LOCK</code> or <code>SHM_UNLOCK</code> was specified, but the process was not privileged (Linux: did not have the <code>CAP_IPC_LOCK</code> capability). (Since Linux 2.6.9, this error can also occur if the <code>RLIMIT_MEMLOCK</code> is 0 and the caller is not privileged.)</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>NOTES</h2>
<p> The inclusion of <i>&lt;sys/types.h&gt;</i> and <i>&lt;sys/ipc.h&gt;</i> isn&#8217;t required on Linux or by any version of POSIX. However, some old implementations required the inclusion of these header files, and the SVID also documented their inclusion. Applications intended to be portable to such old systems may need to include these header files. </p>
<p> The <code>IPC_INFO</code>, <code>SHM_STAT</code>, and <code>SHM_INFO</code> operations are used by the <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1) program to provide information on allocated resources. In the future, these may modified or moved to a <i>/proc</i> filesystem interface. </p>
<p> Linux permits a process to attach (<code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2)) a shared memory segment that has already been marked for deletion using <i>shmctl(IPC_RMID)</i>. This feature is not available on other UNIX implementations; portable applications should avoid relying on it. </p>
<p> Various fields in a <i>struct shmid_ds</i> were typed as <i>short</i> under Linux 2.2 and have become <i>long</i> under Linux 2.4. To take advantage of this, a recompilation under glibc-2.1.91 or later should suffice. (The kernel distinguishes old and new calls by an <code>IPC_64</code> flag in <i>cmd</i>.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/2-shmop/">shmop</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
