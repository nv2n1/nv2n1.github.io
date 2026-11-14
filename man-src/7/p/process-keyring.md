---
title: "process-keyring(7)"
name: "process-keyring"
section: "7"
letter: "p"
url: "/docs/linux/man/7-process-keyring/"
description: "process-keyring – per-process shared keyring"
---

<p>process-keyring &#8211; per-process shared keyring</p>
<h2>Description</h2>
<p>The process keyring is a keyring used to anchor keys on behalf of a process. It is created only when a process requests it. The process keyring has the name (description) <i>_pid</i>. </p>
<p> A special serial number value, <code>KEY_SPEC_PROCESS_KEYRING</code>, is defined that can be used in lieu of the actual serial number of the calling process&#8217;s process keyring. </p>
<p> From the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) utility, &#8216;<code>@p</code>&#8216; can be used instead of a numeric key ID in much the same way, but since <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) is a program run after forking, this is of no utility. </p>
<p> A thread created using the <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) <code>CLONE_THREAD</code> flag has the same process keyring as the caller of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). When a new process is created using <code>fork</code>() it initially has no process keyring. A process&#8217;s process keyring is cleared on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). The process keyring is destroyed when the last thread that refers to it terminates. </p>
<p> If a process doesn&#8217;t have a process keyring when it is accessed, then the process keyring will be created if the keyring is to be modified; otherwise, the error <code>ENOKEY</code> results.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
