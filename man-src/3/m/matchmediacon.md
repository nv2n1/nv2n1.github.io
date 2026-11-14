---
title: "matchmediacon(3)"
name: "matchmediacon"
section: "3"
letter: "m"
url: "/docs/linux/man/3-matchmediacon/"
description: "matchmediacon – get the default SELinux security context for the specified mediatype from the policy"
---

<h2 class="name">NAME</h2>
<p> matchmediacon &#8211; get the default SELinux security context for the specified mediatype from the policy </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int matchmediacon(const char *</code><i>media</i><code>, char **</code><i>con</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>matchmediacon</code>() matches the specified media type with the media contexts configuration and sets the security context <i>con</i> to refer to the resulting context. </p>
<p> <code>Note:</code> Caller must free returned security context <i>con</i> using <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success or -1 otherwise.</p>
<h2>Files</h2>
<p> <i>/etc/selinux/{POLICYTYPE}/contexts/files/media</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) </p>
<h2>Index</h2>
