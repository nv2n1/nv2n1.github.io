---
title: "ipc_namespaces(7)"
name: "ipc_namespaces"
section: "7"
letter: "i"
url: "/docs/linux/man/7-ipc_namespaces/"
description: "ipc_namespaces – overview of Linux IPC namespaces"
---

<p>ipc_namespaces &#8211; overview of Linux IPC namespaces</p>
<h2>Description</h2>
<p>IPC namespaces isolate certain IPC resources, namely, System V IPC objects (see <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)) and (since Linux 2.6.30) POSIX message queues (see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)). The common characteristic of these IPC mechanisms is that IPC objects are identified by mechanisms other than filesystem pathnames. </p>
<p> Each IPC namespace has its own set of System V IPC identifiers and its own POSIX message queue filesystem. Objects created in an IPC namespace are visible to all other processes that are members of that namespace, but are not visible to processes in other IPC namespaces. </p>
<p> The following <i>/proc</i> interfaces are distinct in each IPC namespace:</p>
<dl>
<dt>*</p>
<dd>The POSIX message queue interfaces in <i>/proc/sys/fs/mqueue</i>.</p>
<dt>*</p>
<dd>The System V IPC interfaces in <i>/proc/sys/kernel</i>, namely: <i>msgmax</i>, <i>msgmnb</i>, <i>msgmni</i>, <i>sem</i>, <i>shmall</i>, <i>shmmax</i>, <i>shmmni</i>, and <i>shm_rmid_forced</i>.</p>
<dt>*</p>
<dd>The System V IPC interfaces in <i>/proc/sysvipc</i>.</dl>
<p> When an IPC namespace is destroyed (i.e., when the last process that is a member of the namespace terminates), all IPC objects in the namespace are automatically destroyed. </p>
<p> Use of IPC namespaces requires a kernel that is configured with the <code>CONFIG_IPC_NS</code> option.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nsenter/">nsenter</a></code>(1), <code><a href="/docs/linux/man/1-unshare/">unshare</a></code>(1), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
