---
title: "semctl(2)"
name: "semctl"
section: "2"
letter: "s"
url: "/docs/linux/man/2-semctl/"
description: "semctl – System V semaphore control operations"
---

<h2 class="name">NAME</h2>
<p> semctl &#8211; System V semaphore control operations </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ipc.h&gt;
#include &lt;sys/sem.h&gt;
#include &lt;sys/types.h&gt;
int semctl(int semid, int semnum, int cmd, ...);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>semctl</code>() performs the control operation specified by <i>cmd</i> on the System V semaphore set identified by <i>semid</i>, or on the <i>semnum</i>-th semaphore of that set. (The semaphores in a set are numbered starting at 0.) </p>
<p> This function has three or four arguments, depending on <i>cmd</i>. When there are four, the fourth has the type <i>union semun</i>. The <i>calling program</i> must define this union as follows: </p>
<p> union semun {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;val;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Value for SETVAL&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct semid_ds&nbsp;*buf;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Buffer for IPC_STAT, IPC_SET&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<wbr>&nbsp;*array;&nbsp;<wbr>&nbsp;/*&nbsp;Array for GETALL, SETALL&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct seminfo&nbsp;<wbr>&nbsp;*__buf;&nbsp;<wbr>&nbsp;/*&nbsp;Buffer for IPC_INFO<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(Linux-specific)&nbsp;*/ }; </p>
<p> The <i>semid_ds</i> data structure is defined in <i>&lt;sys/sem.h&gt;</i> as follows: </p>
<p> struct semid_ds {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ipc_perm sem_perm;&nbsp;<wbr>&nbsp;/*&nbsp;Ownership and permissions&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sem_otime;&nbsp;/*&nbsp;Last semop time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sem_ctime;&nbsp;/*&nbsp;Creation time/time of last<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;modification via semctl()&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;<wbr>&nbsp;sem_nsems;&nbsp;/*&nbsp;No. of semaphores in set&nbsp;*/ }; </p>
<p> The fields of the <i>semid_ds</i> structure are as follows:</p>
<dl>
<dt><i>sem_perm</i></p>
<dd> This is an <i>ipc_perm</i> structure (see below) that specifies the access permissions on the semaphore set.</p>
<dt><i>sem_otime</i></p>
<dd> Time of last <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) system call.</p>
<dt><i>sem_ctime</i></p>
<dd> Time of creation of semaphore set or time of last <code>semctl</code>() <code>IPCSET</code>, <code>SETVAL</code>, or <code>SETALL</code> operation.</p>
<dt><i>sem_nsems</i></p>
<dd> Number of semaphores in the set. Each semaphore of the set is referenced by a nonnegative integer ranging from <code>0</code> to <i>sem_nsems-1</i>.</dl>
<p> The <i>ipc_perm</i> structure is defined as follows (the highlighted fields are settable using <code>IPC_SET</code>): </p>
<p> struct ipc_perm {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__key;&nbsp;/*&nbsp;Key supplied to&nbsp;<a href="/docs/linux/man/2-semget/">semget</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>uid</code>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective UID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>gid</code>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective GID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cuid;&nbsp;<wbr>&nbsp;/*&nbsp;Effective UID of creator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cgid;&nbsp;<wbr>&nbsp;/*&nbsp;Effective GID of creator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<code>mode</code>;&nbsp;<wbr>&nbsp;/*&nbsp;Permissions&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;__seq;&nbsp;/*&nbsp;Sequence number&nbsp;*/ }; </p>
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
<p> In effect, &quot;write&quot; means &quot;alter&quot; for a semaphore set. Bits 0100, 0010, and 0001 (the execute bits) are unused by the system. </p>
<p> Valid values for <i>cmd</i> are:</p>
<dl>
<dt><code>IPC_STAT</code></p>
<dd> Copy information from the kernel data structure associated with <i>semid</i> into the <i>semid_ds</i> structure pointed to by <i>arg.buf</i>. The argument <i>semnum</i> is ignored. The calling process must have read permission on the semaphore set.</p>
<dt><code>IPC_SET</code></p>
<dd> Write the values of some members of the <i>semid_ds</i> structure pointed to by <i>arg.buf</i> to the kernel data structure associated with this semaphore set, updating also its <i>sem_ctime</i> member.</p>
<dt>
<dd> The following members of the structure are updated: <i>sem_perm.uid</i>, <i>sem_perm.gid</i>, and (the least significant 9 bits of) <i>sem_perm.mode</i>.</p>
<dt>
<dd> The effective UID of the calling process must match the owner (<i>sem_perm.uid</i>) or creator (<i>sem_perm.cuid</i>) of the semaphore set, or the caller must be privileged. The argument <i>semnum</i> is ignored.</p>
<dt><code>IPC_RMID</code></p>
<dd> Immediately remove the semaphore set, awakening all processes blocked in <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) calls on the set (with an error return and <i>errno</i> set to <code>EIDRM</code>). The effective user ID of the calling process must match the creator or owner of the semaphore set, or the caller must be privileged. The argument <i>semnum</i> is ignored.</p>
<dt><code>IPC_INFO</code> (Linux-specific)</p>
<dd> Return information about system-wide semaphore limits and parameters in the structure pointed to by <i>arg.__buf</i>. This structure is of type <i>seminfo</i>, defined in <i>&lt;sys/sem.h&gt;</i> if the <code>_GNU_SOURCE</code> feature test macro is defined:</p>
<dt>
<dd> struct seminfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semmap;&nbsp;<wbr>&nbsp;/*&nbsp;Number of entries in semaphore<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map;&nbsp;unused within kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semmni;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of semaphore sets&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semmns;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of semaphores in all<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;semaphore sets&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semmnu;&nbsp;<wbr>&nbsp;/*&nbsp;System-wide maximum number of undo<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;structures;&nbsp;unused within kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semmsl;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of semaphores in a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semopm;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of operations for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/2-semop/">semop</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semume;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of undo entries per<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;process;&nbsp;unused within kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semusz;&nbsp;<wbr>&nbsp;/*&nbsp;Size of struct sem_undo&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semvmx;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum semaphore value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semaem;&nbsp;<wbr>&nbsp;/*&nbsp;Max. value that can be recorded for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;semaphore adjustment&nbsp;(SEM_UNDO)&nbsp;*/ };</p>
<dt>
<dd> The <i>semmsl</i>, <i>semmns</i>, <i>semopm</i>, and <i>semmni</i> settings can be changed via <i>/proc/sys/kernel/sem</i>; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for details.</p>
<dt><code>SEM_INFO</code> (Linux-specific)</p>
<dd> Return a <i>seminfo</i> structure containing the same information as for <code>IPC_INFO</code>, except that the following fields are returned with information about system resources consumed by semaphores: the <i>semusz</i> field returns the number of semaphore sets that currently exist on the system; and the <i>semaem</i> field returns the total number of semaphores in all semaphore sets on the system.</p>
<dt><code>SEM_STAT</code> (Linux-specific)</p>
<dd> Return a <i>semid_ds</i> structure as for <code>IPC_STAT</code>. However, the <i>semid</i> argument is not a semaphore identifier, but instead an index into the kernel&#8217;s internal array that maintains information about all semaphore sets on the system.</p>
<dt><code>SEM_STAT_ANY</code> (Linux-specific, since Linux 4.17)</p>
<dd> Return a <i>seminfo</i> structure containing the same information as for <code>SEM_STAT</code>. However, <i>sem_perm.mode</i> is not checked for read access for <i>semid</i> meaning that any user can employ this operation (just as any user may read <i>/proc/sysvipc/sem</i> to obtain the same information).</p>
<dt><code>GETALL</code></p>
<dd> Return <code>semval</code> (i.e., the current value) for all semaphores of the set into <i>arg.array</i>. The argument <i>semnum</i> is ignored. The calling process must have read permission on the semaphore set.</p>
<dt><code>GETNCNT</code></p>
<dd> Return the <code>semncnt</code> value for the <i>semnum</i>-th semaphore of the set (i.e., the number of processes waiting for the semaphore&#8217;s value to increase). The calling process must have read permission on the semaphore set.</p>
<dt><code>GETPID</code></p>
<dd> Return the <code>sempid</code> value for the <i>semnum</i>-th semaphore of the set. This is the PID of the process that last performed an operation on that semaphore (but see NOTES). The calling process must have read permission on the semaphore set.</p>
<dt><code>GETVAL</code></p>
<dd> Return <code>semval</code> (i.e., the semaphore value) for the <i>semnum</i>-th semaphore of the set. The calling process must have read permission on the semaphore set.</p>
<dt><code>GETZCNT</code></p>
<dd> Return the <code>semzcnt</code> value for the <i>semnum</i>-th semaphore of the set (i.e., the number of processes waiting for the semaphore value to become 0). The calling process must have read permission on the semaphore set.</p>
<dt><code>SETALL</code></p>
<dd> Set the <code>semval</code> values for all semaphores of the set using <i>arg.array</i>, updating also the <i>sem_ctime</i> member of the <i>semid_ds</i> structure associated with the set. Undo entries (see <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2)) are cleared for altered semaphores in all processes. If the changes to semaphore values would permit blocked <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) calls in other processes to proceed, then those processes are woken up. The argument <i>semnum</i> is ignored. The calling process must have alter (write) permission on the semaphore set.</p>
<dt><code>SETVAL</code></p>
<dd> Set the semaphore value <code>(</code>semval<code>)</code> to <i>arg.val</i> for the <i>semnum</i>-th semaphore of the set, updating also the <i>sem_ctime</i> member of the <i>semid_ds</i> structure associated with the set. Undo entries are cleared for altered semaphores in all processes. If the changes to semaphore values would permit blocked <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) calls in other processes to proceed, then those processes are woken up. The calling process must have alter permission on the semaphore set.</dl>
<h2>RETURN VALUE</h2>
<p> On failure, <code>semctl</code>() returns -1 with <i>errno</i> indicating the error. </p>
<p> Otherwise, the system call returns a nonnegative value depending on <i>cmd</i> as follows:</p>
<dl>
<dt><code>GETNCNT</code></p>
<dd> the value of <code>semncnt</code>.</p>
<dt><code>GETPID</code></p>
<dd> the value of <code>sempid</code>.</p>
<dt><code>GETVAL</code></p>
<dd> the value of <code>semval</code>.</p>
<dt><code>GETZCNT</code></p>
<dd> the value of <code>semzcnt</code>.</p>
<dt><code>IPC_INFO</code></p>
<dd> the index of the highest used entry in the kernel&#8217;s internal array recording information about all semaphore sets. (This information can be used with repeated <code>SEM_STAT</code> or <code>SEM_STAT_ANY</code> operations to obtain information about all semaphore sets on the system.)</p>
<dt><code>SEM_INFO</code></p>
<dd> as for <code>IPC_INFO</code>.</p>
<dt><code>SEM_STAT</code></p>
<dd> the identifier of the semaphore set whose index was given in <i>semid</i>.</p>
<dt><code>SEM_STAT_ANY</code></p>
<dd> as for <code>SEM_STAT</code>.</dl>
<p> All other <i>cmd</i> values return 0 on success.</p>
<h2>ERRORS</h2>
<p> On failure, <i>errno</i> will be set to one of the following:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The argument <i>cmd</i> has one of the values <code>GETALL</code>, <code>GETPID</code>, <code>GETVAL</code>, <code>GETNCNT</code>, <code>GETZCNT</code>, <code>IPC_STAT</code>, <code>SEM_STAT</code>, <code>SEM_STAT_ANY</code>, <code>SETALL</code>, or <code>SETVAL</code> and the calling process does not have the required permissions on the semaphore set and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EFAULT</code></p>
<dd> The address pointed to by <i>arg.buf</i> or <i>arg.array</i> isn&#8217;t accessible.</p>
<dt><code>EIDRM</code></p>
<dd> The semaphore set was removed.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid value for <i>cmd</i> or <i>semid</i>. Or: for a <code>SEM_STAT</code> operation, the index value specified in <i>semid</i> referred to an array slot that is currently unused.</p>
<dt><code>EPERM</code></p>
<dd> The argument <i>cmd</i> has the value <code>IPC_SET</code> or <code>IPC_RMID</code> but the effective user ID of the calling process is not the creator (as found in <i>sem_perm.cuid</i>) or the owner (as found in <i>sem_perm.uid</i>) of the semaphore set, and the process does not have the <code>CAP_SYS_ADMIN</code> capability.</p>
<dt><code>ERANGE</code></p>
<dd> The argument <i>cmd</i> has the value <code>SETALL</code> or <code>SETVAL</code> and the value to which <code>semval</code> is to be set (for some semaphore of the set) is less than 0 or greater than the implementation limit <code>SEMVMX</code>.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4. </p>
<p> POSIX.1 specifies the <i>sem_nsems</i> field of the <i>semid_ds</i> structure as having the type <i>unsigned short</i>, and the field is so defined on most other systems. It was also so defined on Linux 2.2 and earlier, but, since Linux 2.4, the field has the type <i>unsigned long</i>.</p>
<h2>NOTES</h2>
<p> The inclusion of <i>&lt;sys/types.h&gt;</i> and <i>&lt;sys/ipc.h&gt;</i> isn&#8217;t required on Linux or by any version of POSIX. However, some old implementations required the inclusion of these header files, and the SVID also documented their inclusion. Applications intended to be portable to such old systems may need to include these header files. </p>
<p> The <code>IPC_INFO</code>, <code>SEM_STAT</code>, and <code>SEM_INFO</code> operations are used by the <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1) program to provide information on allocated resources. In the future these may modified or moved to a <i>/proc</i> filesystem interface. </p>
<p> Various fields in a <i>struct semid_ds</i> were typed as <i>short</i> under Linux 2.2 and have become <i>long</i> under Linux 2.4. To take advantage of this, a recompilation under glibc-2.1.91 or later should suffice. (The kernel distinguishes old and new calls by an <code>IPC_64</code> flag in <i>cmd</i>.) </p>
<p> In some earlier versions of glibc, the <i>semun</i> union was defined in <i>&lt;sys/sem.h&gt;</i>, but POSIX.1 requires that the caller define this union. On versions of glibc where this union is <i>not</i> defined, the macro <code>_SEM_SEMUN_UNDEFINED</code> is defined in <i>&lt;sys/sem.h&gt;</i>. </p>
<p> The following system limit on semaphore sets affects a <code>semctl</code>() call:</p>
<dl>
<dt><code>SEMVMX</code></p>
<dd> Maximum value for <code>semval</code>: implementation dependent (32767).</dl>
<p> For greater portability, it is best to always call <code>semctl</code>() with four arguments.</p>
<h3>The sempid value</h3>
<p> POSIX.1 defines <i>sempid</i> as the &quot;process ID of [the] last operation&quot; on a semaphore, and explicitly notes that this value is set by a successful <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) call, with the implication that no other interface affects the <i>sempid</i> value. </p>
<p> While some implementations conform to the behavior specified in POSIX.1, others do not. (The fault here probably lies with POSIX.1 inasmuch as it likely failed to capture the full range of existing implementation behaviors.) Various other implementations also update <i>sempid</i> for the other operations that update the value of a semaphore: the <code>SETVAL</code> and <code>SETALL</code> operations, as well as the semaphore adjustments performed on process termination as a consequence of the use of the <code>SEM_UNDO</code> flag (see <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2)). </p>
<p> Linux also updates <i>sempid</i> for <code>SETVAL</code> operations and semaphore adjustments. However, somewhat inconsistently, up to and including Linux 4.5, the kernel did not update <i>sempid</i> for <code>SETALL</code> operations. This was rectified in Linux 4.6.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-shmop/">shmop</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
