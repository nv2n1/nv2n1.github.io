---
title: "user-session-keyring(7)"
name: "user-session-keyring"
section: "7"
letter: "u"
url: "/docs/linux/man/7-user-session-keyring/"
description: "user-session-keyring – per-user default session keyring"
---

<p>user-session-keyring &#8211; per-user default session keyring</p>
<h2>Description</h2>
<p>The user session keyring is a keyring used to anchor keys on behalf of a user. Each UID the kernel deals with has its own user session keyring that is shared by all processes with that UID. The user session keyring has a name (description) of the form <i>_uid_ses.&lt;UID&gt;</i> where <i>&lt;UID&gt;</i> is the user ID of the corresponding user. </p>
<p> The user session keyring is associated with the record that the kernel maintains for the UID. It comes into existence upon the first attempt to access either the user session keyring, the <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), or the <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7). The keyring remains pinned in existence so long as there are processes running with that real UID or files opened by those processes remain open. (The keyring can also be pinned indefinitely by linking it into another keyring.) </p>
<p> The user session keyring is created on demand when a thread requests it or when a thread asks for its <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7) and that keyring doesn&#8217;t exist. In the latter case, a user session keyring will be created and, if the session keyring wasn&#8217;t to be created, the user session keyring will be set as the process&#8217;s actual session keyring. </p>
<p> The user session keyring is searched by <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) if the actual session keyring does not exist and is ignored otherwise. </p>
<p> A special serial number value, <code>KEY_SPEC_USER_SESSION_KEYRING</code>, is defined that can be used in lieu of the actual serial number of the calling process&#8217;s user session keyring. </p>
<p> From the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) utility, &#8216;<code>@us</code>&#8216; can be used instead of a numeric key ID in much the same way. </p>
<p> User session keyrings are independent of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), and <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) excepting that the keyring is destroyed when the UID record is destroyed when the last process pinning it exits. </p>
<p> If a user session keyring does not exist when it is accessed, it will be created. </p>
<p> Rather than relying on the user session keyring, it is strongly recommended&#8212;especially if the process is running as root&#8212;that a <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7) be set explicitly, for example by <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8).</p>
<h2>Notes</h2>
<p>The user session keyring was added to support situations where a process doesn&#8217;t have a session keyring, perhaps because it was created via a pathway that didn&#8217;t involve PAM (e.g., perhaps it was a daemon started by <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8)). In such a scenario, the user session keyring acts as a substitute for the <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
