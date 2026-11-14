---
title: "ipc(5)"
name: "ipc"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipc/"
description: "svipc – System V interprocess communication mechanisms"
---

<p>svipc &#8211; System V interprocess communication mechanisms</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/msg.h&gt;
#include &lt;sys/sem.h&gt;
#include &lt;sys/shm.h&gt;</code></pre>
<h2>Description</h2>
<p>This manual page refers to the Linux implementation of the System V interprocess communication (IPC) mechanisms: message queues, semaphore sets, and shared memory segments. In the following, the word <i>resource</i> means an instantiation of one among such mechanisms.</p>
<h3>Resource access permissions</h3>
<p>For each resource, the system uses a common structure of type <i>struct ipc_perm</i> to store information needed in determining permissions to perform an IPC operation. The <i>ipc_perm</i> structure includes the following members: </p>
<pre><code>struct ipc_perm {
    uid_t cuid;          /* creator user ID */
    gid_t cgid;          /* creator group ID */
    uid_t uid;           /* owner user ID */
    gid_t gid;           /* owner group ID */
    unsigned short mode; /* r/w permissions */
};</code></pre>
<p> The <i>mode</i> member of the <i>ipc_perm</i> structure defines, with its lower 9 bits, the access permissions to the resource for a process executing an IPC system call. The permissions are interpreted as follows: </p>
<pre> 0400 Read by user.
 0200 Write by user.
 0040 Read by group.
 0020 Write by group.
 0004 Read by others.
 0002 Write by others.</pre>
<p>Bits 0100, 0010, and 0001 (the execute bits) are unused by the system. Furthermore, &quot;write&quot; effectively means &quot;alter&quot; for a semaphore set. The same system header file also defines the following symbolic constants:</p>
<dl>
<dt><code>IPC_CREAT</code></p>
<dd>Create entry if key doesn&#8217;t exist.</p>
<dt><code>IPC_EXCL</code></p>
<dd>Fail if key exists.</p>
<dt><code>IPC_NOWAIT</code></p>
<dd>Error if request must wait.</p>
<dt><code>IPC_PRIVATE</code></p>
<dd>Private key.</p>
<dt><code>IPC_RMID</code></p>
<dd>Remove resource.</p>
<dt><code>IPC_SET</code></p>
<dd>Set resource options.</p>
<dt><code>IPC_STAT</code></p>
<dd>Get resource options.</dl>
<p> Note that <code>IPC_PRIVATE</code> is a <i>key_t</i> type, while all the other symbolic constants are flag fields and can be OR&#8217;ed into an <i>int</i> type variable.</p>
<h3>Message queues</h3>
<p>A message queue is uniquely identified by a positive integer (its <i>msqid</i>) and has an associated data structure of type <i>struct msqid_ds</i>, defined in <i>&lt;sys/msg.h&gt;</i>, containing the following members: struct msqid_ds {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ipc_perm msg_perm;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msgqnum_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_qnum;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;no of messages on queue&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msglen_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_qbytes;&nbsp;<wbr>&nbsp;/*&nbsp;bytes max on a queue&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_lspid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of last&nbsp;<a href="/docs/linux/man/2-msgsnd/">msgsnd</a>(2)&nbsp;call&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_lrpid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of last&nbsp;<a href="/docs/linux/man/2-msgrcv/">msgrcv</a>(2)&nbsp;call&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_stime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;last&nbsp;<a href="/docs/linux/man/2-msgsnd/">msgsnd</a>(2)&nbsp;time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_rtime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;last&nbsp;<a href="/docs/linux/man/2-msgrcv/">msgrcv</a>(2)&nbsp;time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_ctime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;last change time&nbsp;*/ };</p>
<dl>
<dt><i>msg_perm</i></p>
<dd><i>ipc_perm</i> structure that specifies the access permissions on the message queue.</p>
<dt><i>msg_qnum</i></p>
<dd>Number of messages currently on the message queue.</p>
<dt><i>msg_qbytes</i></p>
<dd>Maximum number of bytes of message text allowed on the message queue.</p>
<dt><i>msg_lspid</i></p>
<dd>ID of the process that performed the last <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2) system call.</p>
<dt><i>msg_lrpid</i></p>
<dd>ID of the process that performed the last <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2) system call.</p>
<dt><i>msg_stime</i></p>
<dd>Time of the last <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2) system call.</p>
<dt><i>msg_rtime</i></p>
<dd>Time of the last <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2) system call.</p>
<dt><i>msg_ctime</i></p>
<dd>Time of the last system call that changed a member of the <i>msqid_ds</i> structure.</dl>
<h3>Semaphore sets</h3>
<p>A semaphore set is uniquely identified by a positive integer (its <i>semid</i>) and has an associated data structure of type <i>struct semid_ds</i>, defined in <i>&lt;sys/sem.h&gt;</i>, containing the following members:</p>
<dl>
<dd>struct semid_ds {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ipc_perm sem_perm;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sem_otime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;last operation time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sem_ctime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;last change time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;<wbr>&nbsp;sem_nsems;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;count of sems in set&nbsp;*/ };</p>
<dt><i>sem_perm</i></p>
<dd><i>ipc_perm</i> structure that specifies the access permissions on the semaphore set.</p>
<dt><i>sem_otime</i></p>
<dd>Time of last <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2) system call.</p>
<dt><i>sem_ctime</i></p>
<dd>Time of last <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2) system call that changed a member of the above structure or of one semaphore belonging to the set.</p>
<dt><i>sem_nsems</i></p>
<dd>Number of semaphores in the set. Each semaphore of the set is referenced by a nonnegative integer ranging from <code>0</code> to <i>sem_nsems-1</i>.</dl>
<p> A semaphore is a data structure of type <i>struct sem</i> containing the following members: struct sem {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semval;&nbsp;<wbr>&nbsp;/*&nbsp;semaphore value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int sempid;&nbsp;<wbr>&nbsp;/*&nbsp;PID of process that last modified&nbsp;*/ };</p>
<dl>
<dt><i>semval</i></p>
<dd>Semaphore value: a nonnegative integer.</p>
<dt><i>sempid</i></p>
<dd>PID of the last process that modified the value of this semaphore.</dl>
<h3>Shared memory segments</h3>
<p>A shared memory segment is uniquely identified by a positive integer (its <i>shmid</i>) and has an associated data structure of type <i>struct shmid_ds</i>, defined in <i>&lt;sys/shm.h&gt;</i>, containing the following members: struct shmid_ds {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ipc_perm shm_perm;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_segsz;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;size of segment&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_cpid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of creator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_lpid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID, last operation&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shmatt_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_nattch;&nbsp;<wbr>&nbsp;/*&nbsp;no. of current attaches&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_atime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;time of last attach&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_dtime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;time of last detach&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shm_ctime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;time of last change&nbsp;*/ };</p>
<dl>
<dt><i>shm_perm</i></p>
<dd><i>ipc_perm</i> structure that specifies the access permissions on the shared memory segment.</p>
<dt><i>shm_segsz</i></p>
<dd>Size in bytes of the shared memory segment.</p>
<dt><i>shm_cpid</i></p>
<dd>ID of the process that created the shared memory segment.</p>
<dt><i>shm_lpid</i></p>
<dd>ID of the last process that executed a <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) or <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2) system call.</p>
<dt><i>shm_nattch</i></p>
<dd>Number of current alive attaches for this shared memory segment.</p>
<dt><i>shm_atime</i></p>
<dd>Time of the last <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2) system call.</p>
<dt><i>shm_dtime</i></p>
<dd>Time of the last <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2) system call.</p>
<dt><i>shm_ctime</i></p>
<dd>Time of the last <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2) system call that changed <i>shmid_ds</i>.</dl>
<h3>IPC namespaces</h3>
<p>For a discussion of the interaction of System V IPC objects and IPC namespaces, see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ipcmk/">ipcmk</a></code>(1), <code><a href="/docs/linux/man/1-ipcrm/">ipcrm</a></code>(1), <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1), <code><a href="/docs/linux/man/1-lsipc/">lsipc</a></code>(1), <code><a href="/docs/linux/man/2-ipc/">ipc</a></code>(2), <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 4.15 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
