---
title: "sestatus(8)"
name: "sestatus"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sestatus/"
description: "sestatus – SELinux status tool"
---

<p>sestatus &#8211; SELinux status tool </p>
<h2>Synopsis</h2>
<p><code>sestatus</code> <i>[-v] [-b] </i> This tool is used to get the status of a system running SELinux. </p>
<h2>Description</h2>
<p>This manual page describes the <code>sestatus</code> program. This tool is used to get the status of a system running SELinux. It displays data about whether SELinux is enabled or disabled, location of key directories, and the loaded policy with its status as shown in the example:</p>
<dl>
<dd>&gt; sestatus<br />
 SELinux status: enabled<br />
 SELinuxfs mount: /selinux<br />
 SELinux root directory: /etc/selinux<br />
 Loaded policy name: targeted<br />
 Current mode: permissive<br />
 Mode from config file: enforcing<br />
 Policy MLS status: enabled<br />
 Policy deny_unknown status: allow<br />
 Max kernel policy version: 26</dl>
<p> <code>sestatus</code> can also be used to display:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>The security context of files and processes listed in the <i>/etc/sestatus.conf</i> file. The format of this file is described in <code><a href="/docs/linux/man/5-sestatus-conf/">sestatus.conf</a></code>(5).</p>
<dt>&#8211;</p>
<dd>The status of booleans.</dl>
</dl>
<h2>Options</h2>
<p><code>-v</code></p>
<dl>
<dd>Displays the contexts of files and processes listed in the <i>/etc/sestatus.conf</i> file. It also checks whether the file is a symbolic link, if so then the context of the target file is also shown. </p>
<p> The following contexts will always be displayed:</p>
<dl>
<dd>The current process context<br />
 The init process context<br />
 The controlling terminal file context</dl>
</dl>
<p> <code>-b</code></p>
<dl>
<dd>Display the current state of booleans.</dl>
<h2>Files</h2>
<p><i>/etc/sestatus.conf</i></p>
<h2>Author</h2>
<p>This man page was written by Daniel Walsh &lt;dwalsh [at] redhat.com&gt;.<br />
 The program was written by Chris PeBenito &lt;pebenito [at] gentoo.org&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/5-sestatus-conf/">sestatus.conf</a></code>(5) </p>
