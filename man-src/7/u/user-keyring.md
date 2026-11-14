---
title: "user-keyring(7)"
name: "user-keyring"
section: "7"
letter: "u"
url: "/docs/linux/man/7-user-keyring/"
description: "user-keyring – per-user keyring"
---

<p>user-keyring &#8211; per-user keyring</p>
<h2>Description</h2>
<p>The user keyring is a keyring used to anchor keys on behalf of a user. Each UID the kernel deals with has its own user keyring that is shared by all processes with that UID. The user keyring has a name (description) of the form <i>_uid.&lt;UID&gt;</i> where <i>&lt;UID&gt;</i> is the user ID of the corresponding user. </p>
<p> The user keyring is associated with the record that the kernel maintains for the UID. It comes into existence upon the first attempt to access either the user keyring, the <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7), or the <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7). The keyring remains pinned in existence so long as there are processes running with that real UID or files opened by those processes remain open. (The keyring can also be pinned indefinitely by linking it into another keyring.) </p>
<p> Typically, the user keyring is created by <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8) when a user logs in. </p>
<p> The user keyring is not searched by default by <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2). When <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8) creates a session keyring, it adds to it a link to the user keyring so that the user keyring will be searched when the session keyring is. </p>
<p> A special serial number value, <code>KEY_SPEC_USER_KEYRING</code>, is defined that can be used in lieu of the actual serial number of the calling process&#8217;s user keyring. </p>
<p> From the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) utility, &#8216;<code>@u</code>&#8216; can be used instead of a numeric key ID in much the same way. </p>
<p> User keyrings are independent of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), and <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) excepting that the keyring is destroyed when the UID record is destroyed when the last process pinning it exits. </p>
<p> If it is necessary for a key associated with a user to exist beyond the UID record being garbage collected&#8212;for example, for use by a <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) script&#8212;then the <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7) should be used instead. </p>
<p> If a user keyring does not exist when it is accessed, it will be created.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7), <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
