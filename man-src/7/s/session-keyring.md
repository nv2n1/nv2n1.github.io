---
title: "session-keyring(7)"
name: "session-keyring"
section: "7"
letter: "s"
url: "/docs/linux/man/7-session-keyring/"
description: "session-keyring – session shared process keyring"
---

<p>session-keyring &#8211; session shared process keyring</p>
<h2>Description</h2>
<p>The session keyring is a keyring used to anchor keys on behalf of a process. It is typically created by <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8) when a user logs in and a link will be added that refers to the <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7). Optionally, PAM may revoke the session keyring on logout. (In typical configurations, PAM does do this revocation.) The session keyring has the name (description) <i>_ses</i>. </p>
<p> A special serial number value, <code>KEY_SPEC_SESSION_KEYRING</code>, is defined that can be used in lieu of the actual serial number of the calling process&#8217;s session keyring. </p>
<p> From the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) utility, &#8216;<code>@s</code>&#8216; can be used instead of a numeric key ID in much the same way. </p>
<p> A process&#8217;s session keyring is inherited across <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), and <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2). The session keyring is preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), even when the executable is set-user-ID or set-group-ID or has capabilities. The session keyring is destroyed when the last process that refers to it exits. </p>
<p> If a process doesn&#8217;t have a session keyring when it is accessed, then, under certain circumstances, the <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7) will be attached as the session keyring and under others a new session keyring will be created. (See <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7) for further details.)</p>
<h3>Special operations</h3>
<p>The <i>keyutils</i> library provides the following special operations for manipulating session keyrings:</p>
<dl>
<dt><code><a href="/docs/linux/man/3-keyctl_join_session_keyring/">keyctl_join_session_keyring</a></code>(3)</p>
<dd>This operation allows the caller to change the session keyring that it subscribes to. The caller can join an existing keyring with a specified name (description), create a new keyring with a given name, or ask the kernel to create a new &quot;anonymous&quot; session keyring with the name &quot;_ses&quot;. (This function is an interface to the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_JOIN_SESSION_KEYRING</code> operation.)</p>
<dt><code><a href="/docs/linux/man/3-keyctl_session_to_parent/">keyctl_session_to_parent</a></code>(3)</p>
<dd>This operation allows the caller to make the parent process&#8217;s session keyring to the same as its own. For this to succeed, the parent process must have identical security attributes and must be single threaded. (This function is an interface to the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_SESSION_TO_PARENT</code> operation.)</dl>
<p> These operations are also exposed through the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) utility as: </p>
<p> keyctl session keyctl session &#8211; [&lt;prog&gt; &lt;arg1&gt; &lt;arg2&gt; &#8230;] keyctl session &lt;name&gt; [&lt;prog&gt; &lt;arg1&gt; &lt;arg2&gt; &#8230;] </p>
<p> and: </p>
<p> keyctl new_session</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_join_session_keyring/">keyctl_join_session_keyring</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_session_to_parent/">keyctl_session_to_parent</a></code>(3), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7), <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
