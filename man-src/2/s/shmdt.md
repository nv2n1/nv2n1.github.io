---
title: "shmdt(2)"
name: "shmdt"
section: "2"
letter: "s"
url: "/docs/linux/man/2-shmdt/"
description: "shmat, shmdt – System V shared memory operations"
---

<h2 class="name">NAME</h2>
<p> shmat, shmdt &#8211; System V shared memory operations </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/shm.h&gt;
#include &lt;sys/types.h&gt;
void *shmat(int shmid, const void *shmaddr, int shmflg);
int shmdt(const void *shmaddr);
</code></pre>
<h2>DESCRIPTION</h2>
<h3>shmat()</h3>
<p> <code>shmat</code>() attaches the System V shared memory segment identified by <i>shmid</i> to the address space of the calling process. The attaching address is specified by <i>shmaddr</i> with one of the following criteria:</p>
<dl>
<dt>&bull;</p>
<dd> If <i>shmaddr</i> is NULL, the system chooses a suitable (unused) page-aligned address to attach the segment.</p>
<dt>&bull;</p>
<dd> If <i>shmaddr</i> isn&#8217;t NULL and <code>SHM_RND</code> is specified in <i>shmflg</i>, the attach occurs at the address equal to <i>shmaddr</i> rounded down to the nearest multiple of <code>SHMLBA</code>.</p>
<dt>&bull;</p>
<dd> Otherwise, <i>shmaddr</i> must be a page-aligned address at which the attach occurs.</dl>
<p> In addition to <code>SHM_RND</code>, the following flags may be specified in the <i>shmflg</i> bit-mask argument:</p>
<dl>
<dt><code>SHM_EXEC</code> (Linux-specific; since Linux 2.6.9)</p>
<dd> Allow the contents of the segment to be executed. The caller must have execute permission on the segment.</p>
<dt><code>SHM_RDONLY</code></p>
<dd> Attach the segment for read-only access. The process must have read permission for the segment. If this flag is not specified, the segment is attached for read and write access, and the process must have read and write permission for the segment. There is no notion of a write-only shared memory segment.</p>
<dt><code>SHM_REMAP</code> (Linux-specific)</p>
<dd> This flag specifies that the mapping of the segment should replace any existing mapping in the range starting at <i>shmaddr</i> and continuing for the size of the segment. (Normally, an <code>EINVAL</code> error would result if a mapping already exists in this address range.) In this case, <i>shmaddr</i> must not be NULL.</dl>
<p> The <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2) value of the calling process is not altered by the attach. The segment will automatically be detached at process exit. The same segment may be attached as a read and as a read-write one, and more than once, in the process&#8217;s address space. </p>
<p> A successful <code>shmat</code>() call updates the members of the <i>shmid_ds</i> structure (see <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2)) associated with the shared memory segment as follows:</p>
<dl>
<dt>&bull;</p>
<dd> <i>shm_atime</i> is set to the current time.</p>
<dt>&bull;</p>
<dd> <i>shm_lpid</i> is set to the process-ID of the calling process.</p>
<dt>&bull;</p>
<dd> <i>shm_nattch</i> is incremented by one.</dl>
<h3>shmdt()</h3>
<p> <code>shmdt</code>() detaches the shared memory segment located at the address specified by <i>shmaddr</i> from the address space of the calling process. The to-be-detached segment must be currently attached with <i>shmaddr</i> equal to the value returned by the attaching <code>shmat</code>() call. </p>
<p> On a successful <code>shmdt</code>() call, the system updates the members of the <i>shmid_ds</i> structure associated with the shared memory segment as follows:</p>
<dl>
<dt>&bull;</p>
<dd> <i>shm_dtime</i> is set to the current time.</p>
<dt>&bull;</p>
<dd> <i>shm_lpid</i> is set to the process-ID of the calling process.</p>
<dt>&bull;</p>
<dd> <i>shm_nattch</i> is decremented by one. If it becomes 0 and the segment is marked for deletion, the segment is deleted.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>shmat</code>() returns the address of the attached shared memory segment; on error, <i>(void&nbsp;*)&nbsp;-1</i> is returned, and <i>errno</i> is set to indicate the cause of the error. </p>
<p> On success, <code>shmdt</code>() returns 0; on error -1 is returned, and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<p> When <code>shmat</code>() fails, <i>errno</i> is set to one of the following:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The calling process does not have the required permissions for the requested attach type, and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EIDRM</code></p>
<dd> <i>shmid</i> points to a removed identifier.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid <i>shmid</i> value, unaligned (i.e., not page-aligned and <code>SHM_RND</code> was not specified) or invalid <i>shmaddr</i> value, or can&#8217;t attach segment at <i>shmaddr</i>, or <code>SHM_REMAP</code> was specified and <i>shmaddr</i> was NULL.</p>
<dt><code>ENOMEM</code></p>
<dd> Could not allocate memory for the descriptor or for the page tables.</dl>
<p> When <code>shmdt</code>() fails, <i>errno</i> is set as follows:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> There is no shared memory segment attached at <i>shmaddr</i>; or, <i>shmaddr</i> is not aligned on a page boundary.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4. </p>
<p> In SVID 3 (or perhaps earlier), the type of the <i>shmaddr</i> argument was changed from <i>char&nbsp;*</i> into <i>const void&nbsp;*</i>, and the returned type of <code>shmat</code>() from <i>char&nbsp;*</i> into <i>void&nbsp;*</i>.</p>
<h2>NOTES</h2>
<p> After a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the child inherits the attached shared memory segments. </p>
<p> After an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), all attached shared memory segments are detached from the process. </p>
<p> Upon <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), all attached shared memory segments are detached from the process. </p>
<p> Using <code>shmat</code>() with <i>shmaddr</i> equal to NULL is the preferred, portable way of attaching a shared memory segment. Be aware that the shared memory segment attached in this way may be attached at different addresses in different processes. Therefore, any pointers maintained within the shared memory must be made relative (typically to the starting address of the segment), rather than absolute. </p>
<p> On Linux, it is possible to attach a shared memory segment even if it is already marked to be deleted. However, POSIX.1 does not specify this behavior and many other implementations do not support it. </p>
<p> The following system parameter affects <code>shmat</code>():</p>
<dl>
<dt><code>SHMLBA</code></p>
<dd> Segment low boundary address multiple. When explicitly specifying an attach address in a call to <code>shmat</code>(), the caller should ensure that the address is a multiple of this value. This is necessary on some architectures, in order either to ensure good CPU cache performance or to ensure that different attaches of the same segment have consistent views within the CPU cache. <code>SHMLBA</code> is normally some multiple of the system page size. (On many Linux architectures, <code>SHMLBA</code> is the same as the system page size.)</dl>
<p> The implementation places no intrinsic per-process limit on the number of shared memory segments (<code>SHMSEG</code>).</p>
<h2>EXAMPLES</h2>
<p> The two programs shown below exchange a string using a shared memory segment. Further details about the programs are given below. First, we show a shell session demonstrating their use. </p>
<p> In one terminal window, we run the &quot;reader&quot; program, which creates a System V shared memory segment and a System V semaphore set. The program prints out the IDs of the created objects, and then waits for the semaphore to change value. </p>
<p> $ <code>./svshm_string_read</code> shmid = 1114194; semid = 15 </p>
<p> In another terminal window, we run the &quot;writer&quot; program. The &quot;writer&quot; program takes three command-line arguments: the IDs of the shared memory segment and semaphore set created by the &quot;reader&quot;, and a string. It attaches the existing shared memory segment, copies the string to the shared memory, and modifies the semaphore value. </p>
<p> $ <code>./svshm_string_write 1114194 15 &#8216;Hello, world&#8217;</code> </p>
<p> Returning to the terminal where the &quot;reader&quot; is running, we see that the program has ceased waiting on the semaphore and has printed the string that was copied into the shared memory segment by the writer: </p>
<p> Hello, world</p>
<h3>Program source: svshm_string.h</h3>
<p> The following header file is included by the &quot;reader&quot; and &quot;writer&quot; programs. </p>
<p> #include &lt;sys/types.h&gt; #include &lt;sys/ipc.h&gt; #include &lt;sys/shm.h&gt; #include &lt;sys/sem.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> union semun { /* Used in calls to semctl() */<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;val;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct semid_ds&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;array; #if defined(__linux__)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct seminfo&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__buf; #endif }; </p>
<p> #define MEM_SIZE 4096</p>
<h3>Program source: svshm_string_read.c</h3>
<p> The &quot;reader&quot; program creates a shared memory segment and a semaphore set containing one semaphore. It then attaches the shared memory object into its address space and initializes the semaphore value to 1. Finally, the program waits for the semaphore value to become 0, and afterwards prints the string that has been copied into the shared memory segment by the &quot;writer&quot;. </p>
<p> /* svshm_string_read.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Licensed under GNU General Public License v2 or later. */ #include &quot;svshm_string.h&quot; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semid, shmid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union semun arg, dummy;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sembuf sop;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*addr; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Create shared memory and semaphore set containing one<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;semaphore&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;shmid&nbsp;=&nbsp;shmget(IPC_PRIVATE, MEM_SIZE, IPC_CREAT | 0600);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(shmid&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;shmget&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;semid&nbsp;=&nbsp;semget(IPC_PRIVATE, 1, IPC_CREAT | 0600);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(shmid&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;shmget&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Attach shared memory into our address space&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr&nbsp;=&nbsp;shmat(shmid, NULL, SHM_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(addr&nbsp;==&nbsp;(void&nbsp;*)&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;shmat&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Initialize semaphore 0 in set with value 1&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;arg.val&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(semctl(semid, 0, SETVAL, arg)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;semctl&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;shmid&nbsp;=&nbsp;%d;&nbsp;semid&nbsp;=&nbsp;%d
&quot;, shmid, semid); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for semaphore value to become 0&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sop.sem_num&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sop.sem_op&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sop.sem_flg&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(semop(semid,&nbsp;&amp;sop, 1)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;semop&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Print the string from shared memory&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s
&quot;, addr); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Remove shared memory and semaphore set&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(shmctl(shmid, IPC_RMID, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;shmctl&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(semctl(semid, 0, IPC_RMID, dummy)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;semctl&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h3>Program source: svshm_string_write.c</h3>
<p> The writer program takes three command-line arguments: the IDs of the shared memory segment and semaphore set that have already been created by the &quot;reader&quot;, and a string. It attaches the shared memory segment into its address space, and then decrements the semaphore value to 0 in order to inform the &quot;reader&quot; that it can now examine the contents of the shared memory. </p>
<p> /* svshm_string_write.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Licensed under GNU General Public License v2 or later. */ #include &quot;svshm_string.h&quot; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semid, shmid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sembuf sop;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t len; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;4)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s shmid semid string
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len&nbsp;=&nbsp;strlen(argv[3])&nbsp;+&nbsp;1;&nbsp;<wbr>&nbsp;/*&nbsp;+1 to include trailing&nbsp;&#8216;
