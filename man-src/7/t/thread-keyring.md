---
title: "thread-keyring(7)"
name: "thread-keyring"
section: "7"
letter: "t"
url: "/docs/linux/man/7-thread-keyring/"
description: "thread-keyring – per-thread keyring"
---

<p>thread-keyring &#8211; per-thread keyring</p>
<h2>Description</h2>
<p>The thread keyring is a keyring used to anchor keys on behalf of a process. It is created only when a thread requests it. The thread keyring has the name (description) <i>_tid</i>. </p>
<p> A special serial number value, <code>KEY_SPEC_THREAD_KEYRING</code>, is defined that can be used in lieu of the actual serial number of the calling thread&#8217;s thread keyring. </p>
<p> From the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) utility, &#8216;<code>@t</code>&#8216; can be used instead of a numeric key ID in much the same way, but as <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) is a program run after forking, this is of no utility. </p>
<p> Thread keyrings are not inherited across <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) and <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and are cleared by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). A thread keyring is destroyed when the thread that refers to it terminates. </p>
<p> Initially, a thread does not have a thread keyring. If a thread doesn&#8217;t have a thread keyring when it is accessed, then it will be created if it is to be modified; otherwise the operation fails with the error <code>ENOKEY</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
