---
title: "semget(2)"
name: "semget"
section: "2"
letter: "s"
url: "/docs/linux/man/2-semget/"
description: "semget – get a System V semaphore set identifier"
---

<h2 class="name">NAME</h2>
<p> semget &#8211; get a System V semaphore set identifier </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ipc.h&gt;
#include &lt;sys/sem.h&gt;
#include &lt;sys/types.h&gt;
</code></pre>
<p> <code>int semget(key_t </code><i>key</i><code>,</code> <code>int </code><i>nsems</i><code>,</code> <code>int </code><i>semflg</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>semget</code>() system call returns the System V semaphore set identifier associated with the argument <i>key</i>. It may be used either to obtain the identifier of a previously created semaphore set (when <i>semflg</i> is zero and <i>key</i> does not have the value <code>IPC_PRIVATE</code>), or to create a new set. </p>
<p> A new set of <i>nsems</i> semaphores is created if <i>key</i> has the value <code>IPC_PRIVATE</code> or if no existing semaphore set is associated with <i>key</i> and <code>IPC_CREAT</code> is specified in <i>semflg</i>. </p>
<p> If <i>semflg</i> specifies both <code>IPC_CREAT</code> and <code>IPC_EXCL</code> and a semaphore set already exists for <i>key</i>, then <code>semget</code>() fails with <i>errno</i> set to <code>EEXIST</code>. (This is analogous to the effect of the combination <code>O_CREAT | O_EXCL</code> for <code><a href="/docs/linux/man/2-open/">open</a></code>(2).) </p>
<p> Upon creation, the least significant 9 bits of the argument <i>semflg</i> define the permissions (for owner, group and others) for the semaphore set. These bits have the same format, and the same meaning, as the <i>mode</i> argument of <code><a href="/docs/linux/man/2-open/">open</a></code>(2) (though the execute permissions are not meaningful for semaphores, and write permissions mean permission to alter semaphore values). </p>
<p> When creating a new semaphore set, <code>semget</code>() initializes the set&#8217;s associated data structure, <i>semid_ds</i> (see <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2)), as follows:</p>
<dl>
<dt>&bull;</p>
<dd> <i>sem_perm.cuid</i> and <i>sem_perm.uid</i> are set to the effective user ID of the calling process.</p>
<dt>&bull;</p>
<dd> <i>sem_perm.cgid</i> and <i>sem_perm.gid</i> are set to the effective group ID of the calling process.</p>
<dt>&bull;</p>
<dd> The least significant 9 bits of <i>sem_perm.mode</i> are set to the least significant 9 bits of <i>semflg</i>.</p>
<dt>&bull;</p>
<dd> <i>sem_nsems</i> is set to the value of <i>nsems</i>.</p>
<dt>&bull;</p>
<dd> <i>sem_otime</i> is set to 0.</p>
<dt>&bull;</p>
<dd> <i>sem_ctime</i> is set to the current time.</dl>
<p> The argument <i>nsems</i> can be 0 (a don&#8217;t care) when a semaphore set is not being created. Otherwise, <i>nsems</i> must be greater than 0 and less than or equal to the maximum number of semaphores per semaphore set (<code>SEMMSL</code>). </p>
<p> If the semaphore set already exists, the permissions are verified.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the return value will be the semaphore set identifier (a nonnegative integer), otherwise, -1 is returned, with <i>errno</i> indicating the error.</p>
<h2>ERRORS</h2>
<p> On failure, <i>errno</i> will be set to one of the following:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> A semaphore set exists for <i>key</i>, but the calling process does not have permission to access the set, and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EEXIST</code></p>
<dd> <code>IPC_CREAT</code> and <code>IPC_EXCL</code> were specified in <i>semflg</i>, but a semaphore set already exists for <i>key</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>nsems</i> is less than 0 or greater than the limit on the number of semaphores per semaphore set (<code>SEMMSL</code>).</p>
<dt><code>EINVAL</code></p>
<dd> A semaphore set corresponding to <i>key</i> already exists, but <i>nsems</i> is larger than the number of semaphores in that set.</p>
<dt><code>ENOENT</code></p>
<dd> No semaphore set exists for <i>key</i> and <i>semflg</i> did not specify <code>IPC_CREAT</code>.</p>
<dt><code>ENOMEM</code></p>
<dd> A semaphore set has to be created but the system does not have enough memory for the new data structure.</p>
<dt><code>ENOSPC</code></p>
<dd> A semaphore set has to be created but the system limit for the maximum number of semaphore sets (<code>SEMMNI</code>), or the system wide maximum number of semaphores (<code>SEMMNS</code>), would be exceeded.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, POSIX.1-2001.</p>
<h2>NOTES</h2>
<p> The inclusion of <i>&lt;sys/types.h&gt;</i> and <i>&lt;sys/ipc.h&gt;</i> isn&#8217;t required on Linux or by any version of POSIX. However, some old implementations required the inclusion of these header files, and the SVID also documented their inclusion. Applications intended to be portable to such old systems may need to include these header files. </p>
<p> <code>IPC_PRIVATE</code> isn&#8217;t a flag field but a <i>key_t</i> type. If this special value is used for <i>key</i>, the system call ignores all but the least significant 9 bits of <i>semflg</i> and creates a new semaphore set (on success).</p>
<h3>Semaphore initialization</h3>
<p> The values of the semaphores in a newly created set are indeterminate. (POSIX.1-2001 and POSIX.1-2008 are explicit on this point, although POSIX.1-2008 notes that a future version of the standard may require an implementation to initialize the semaphores to 0.) Although Linux, like many other implementations, initializes the semaphore values to 0, a portable application cannot rely on this: it should explicitly initialize the semaphores to the desired values. </p>
<p> Initialization can be done using <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2) <code>SETVAL</code> or <code>SETALL</code> operation. Where multiple peers do not know who will be the first to initialize the set, checking for a nonzero <i>sem_otime</i> in the associated data structure retrieved by a <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2) <code>IPC_STAT</code> operation can be used to avoid races.</p>
<h3>Semaphore limits</h3>
<p> The following limits on semaphore set resources affect the <code>semget</code>() call:</p>
<dl>
<dt><code>SEMMNI</code></p>
<dd> System-wide limit on the number of semaphore sets. On Linux systems before version 3.19, the default value for this limit was 128. Since Linux 3.19, the default value is 32,000. On Linux, this limit can be read and modified via the fourth field of <i>/proc/sys/kernel/sem</i>.</p>
<dt><code>SEMMSL</code></p>
<dd> Maximum number of semaphores per semaphore ID. On Linux systems before version 3.19, the default value for this limit was 250. Since Linux 3.19, the default value is 32,000. On Linux, this limit can be read and modified via the first field of <i>/proc/sys/kernel/sem</i>.</p>
<dt><code>SEMMNS</code></p>
<dd> System-wide limit on the number of semaphores: policy dependent (on Linux, this limit can be read and modified via the second field of <i>/proc/sys/kernel/sem</i>). Note that the number of semaphores system-wide is also limited by the product of <code>SEMMSL</code> and <code>SEMMNI</code>.</dl>
<h2>BUGS</h2>
<p> The name choice <code>IPC_PRIVATE</code> was perhaps unfortunate, <code>IPC_NEW</code> would more clearly show its function.</p>
<h2>EXAMPLES</h2>
<p> The program shown below uses <code>semget</code>() to create a new semaphore set or retrieve the ID of an existing set. It generates the <i>key</i> for <code>semget</code>() using <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3). The first two command-line arguments are used as the <i>pathname</i> and <i>proj_id</i> arguments for <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3). The third command-line argument is an integer that specifies the <i>nsems</i> argument for <code>semget</code>(). Command-line options can be used to specify the <code>IPC_CREAT</code> (<i>-c</i>) and <code>IPC_EXCL</code> (<i>-x</i>) flags for the call to <code>semget</code>(). The usage of this program is demonstrated below. </p>
<p> We first create two files that will be used to generate keys using <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3), create two semaphore sets using those files, and then list the sets using <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1): </p>
<p> $ <code>touch mykey mykey2</code> $ <code>./t_semget -c mykey p 1</code> ID = 9 $ <code>./t_semget -c mykey2 p 2</code> ID = 10 $ <code>ipcs -s</code> </p>
<p> &#8212;&#8212; Semaphore Arrays &#8212;&#8212;&#8211; key semid owner perms nsems 0x7004136d 9 mtk 600 1 0x70041368 10 mtk 600 2 </p>
<p> Next, we demonstrate that when <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2) is given the same <i>key</i> (as generated by the same arguments to <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3)), it returns the ID of the already existing semaphore set: </p>
<p> $ <code>./t_semget -c mykey p 1</code> ID = 9 </p>
<p> Finally, we demonstrate the kind of collision that can occur when <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3) is given different <i>pathname</i> arguments that have the same inode number: </p>
<p> $ <code>ln mykey link</code> $ <code>ls -i1 link mykey</code> 2233197 link 2233197 mykey $ <code>./t_semget link p 1</code> # Generates same key as &#8216;mykey&#8217; ID = 9</p>
<h3>Program source</h3>
<p> /* t_semget.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Licensed under GNU General Public License v2 or later. */ #include &lt;sys/types.h&gt; #include &lt;sys/ipc.h&gt; #include &lt;sys/sem.h&gt; #include &lt;sys/stat.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> static void usage(const char *pname) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;[-cx]&nbsp;pathname proj-id num-sems
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pname);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-c&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Use IPC_CREAT flag
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-x&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Use IPC_EXCL flag
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int semid, nsems, flags, opt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_t key; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;((opt&nbsp;=&nbsp;getopt(argc, argv,&nbsp;&quot;cx&quot;))&nbsp;!=&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(opt)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;c&#8217;: flags |=&nbsp;IPC_CREAT;&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;x&#8217;: flags |=&nbsp;IPC_EXCL;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:&nbsp;<wbr>&nbsp;usage(argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;optind&nbsp;+&nbsp;3)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usage(argv[0]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key&nbsp;=&nbsp;ftok(argv[optind], argv[optind&nbsp;+&nbsp;1][0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(key&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;ftok&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nsems&nbsp;=&nbsp;atoi(argv[optind&nbsp;+&nbsp;2]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;semid&nbsp;=&nbsp;semget(key, nsems, flags | 0600);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(semid&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;semget&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;ID&nbsp;=&nbsp;%d
&quot;, semid); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-semctl/">semctl</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
