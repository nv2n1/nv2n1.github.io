---
title: "msgget(2)"
name: "msgget"
section: "2"
letter: "m"
url: "/docs/linux/man/2-msgget/"
description: "msgget – get a System V message queue identifier"
---

<h2 class="name">NAME</h2>
<p> msgget &#8211; get a System V message queue identifier </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ipc.h&gt;
#include &lt;sys/msg.h&gt;
#include &lt;sys/types.h&gt;
int msgget(key_t key, int msgflg);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>msgget</code>() system call returns the System V message queue identifier associated with the value of the <i>key</i> argument. It may be used either to obtain the identifier of a previously created message queue (when <i>msgflg</i> is zero and <i>key</i> does not have the value <code>IPC_PRIVATE</code>), or to create a new set. </p>
<p> A new message queue is created if <i>key</i> has the value <code>IPC_PRIVATE</code> or <i>key</i> isn&#8217;t <code>IPC_PRIVATE</code>, no message queue with the given key <i>key</i> exists, and <code>IPC_CREAT</code> is specified in <i>msgflg</i>. </p>
<p> If <i>msgflg</i> specifies both <code>IPC_CREAT</code> and <code>IPC_EXCL</code> and a message queue already exists for <i>key</i>, then <code>msgget</code>() fails with <i>errno</i> set to <code>EEXIST</code>. (This is analogous to the effect of the combination <code>O_CREAT | O_EXCL</code> for <code><a href="/docs/linux/man/2-open/">open</a></code>(2).) </p>
<p> Upon creation, the least significant bits of the argument <i>msgflg</i> define the permissions of the message queue. These permission bits have the same format and semantics as the permissions specified for the <i>mode</i> argument of <code><a href="/docs/linux/man/2-open/">open</a></code>(2). (The execute permissions are not used.) </p>
<p> If a new message queue is created, then its associated data structure <i>msqid_ds</i> (see <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2)) is initialized as follows:</p>
<dl>
<dt>&bull;</p>
<dd> <i>msg_perm.cuid</i> and <i>msg_perm.uid</i> are set to the effective user ID of the calling process.</p>
<dt>&bull;</p>
<dd> <i>msg_perm.cgid</i> and <i>msg_perm.gid</i> are set to the effective group ID of the calling process.</p>
<dt>&bull;</p>
<dd> The least significant 9 bits of <i>msg_perm.mode</i> are set to the least significant 9 bits of <i>msgflg</i>.</p>
<dt>&bull;</p>
<dd> <i>msg_qnum</i>, <i>msg_lspid</i>, <i>msg_lrpid</i>, <i>msg_stime</i>, and <i>msg_rtime</i> are set to 0.</p>
<dt>&bull;</p>
<dd> <i>msg_ctime</i> is set to the current time.</p>
<dt>&bull;</p>
<dd> <i>msg_qbytes</i> is set to the system limit <code>MSGMNB</code>.</dl>
<p> If the message queue already exists the permissions are verified, and a check is made to see if it is marked for destruction.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the return value will be the message queue identifier (a nonnegative integer), otherwise -1 with <i>errno</i> indicating the error.</p>
<h2>ERRORS</h2>
<p> On failure, <i>errno</i> is set to one of the following values:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> A message queue exists for <i>key</i>, but the calling process does not have permission to access the queue, and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EEXIST</code></p>
<dd> <code>IPC_CREAT</code> and <code>IPC_EXCL</code> were specified in <i>msgflg</i>, but a message queue already exists for <i>key</i>.</p>
<dt><code>ENOENT</code></p>
<dd> No message queue exists for <i>key</i> and <i>msgflg</i> did not specify <code>IPC_CREAT</code>.</p>
<dt><code>ENOMEM</code></p>
<dd> A message queue has to be created but the system does not have enough memory for the new data structure.</p>
<dt><code>ENOSPC</code></p>
<dd> A message queue has to be created but the system limit for the maximum number of message queues (<code>MSGMNI</code>) would be exceeded.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>NOTES</h2>
<p> The inclusion of <i>&lt;sys/types.h&gt;</i> and <i>&lt;sys/ipc.h&gt;</i> isn&#8217;t required on Linux or by any version of POSIX. However, some old implementations required the inclusion of these header files, and the SVID also documented their inclusion. Applications intended to be portable to such old systems may need to include these header files. </p>
<p> <code>IPC_PRIVATE</code> isn&#8217;t a flag field but a <i>key_t</i> type. If this special value is used for <i>key</i>, the system call ignores everything but the least significant 9 bits of <i>msgflg</i> and creates a new message queue (on success). </p>
<p> The following is a system limit on message queue resources affecting a <code>msgget</code>() call:</p>
<dl>
<dt><code>MSGMNI</code></p>
<dd> System-wide limit on the number of message queues. Before Linux 3.19, the default value for this limit was calculated using a formula based on available system memory. Since Linux 3.19, the default value is 32,000. On Linux, this limit can be read and modified via <i>/proc/sys/kernel/msgmni</i>.</dl>
<h3>Linux notes</h3>
<p> Until version 2.3.20, Linux would return <code>EIDRM</code> for a <code>msgget</code>() on a message queue scheduled for deletion.</p>
<h2>BUGS</h2>
<p> The name choice <code>IPC_PRIVATE</code> was perhaps unfortunate, <code>IPC_NEW</code> would more clearly show its function.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
