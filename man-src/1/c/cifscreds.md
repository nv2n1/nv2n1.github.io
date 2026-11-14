---
title: "cifscreds(1)"
name: "cifscreds"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cifscreds/"
description: "cifscreds – manage NTLM credentials in kernel keyring"
---

<h2 class="name">NAME</h2>
<p> cifscreds &#8211; manage NTLM credentials in kernel keyring </p>
<h2>SYNOPSIS</h2>
<p> cifscreds add|clear|clearall|update [-u username] [-d] host|domain</p>
<h2>DESCRIPTION</h2>
<p> The <code>cifscreds</code> program is a tool for managing credentials (username and password) for the purpose of establishing sessions in multiuser mounts. </p>
<p> When a cifs filesystem is mounted with the &#8220;multiuser&#8221; option, and does not use krb5 authentication, it needs to be able to get the credentials for each user from somewhere. The <code>cifscreds</code> program is the tool used to provide these credentials to the kernel. </p>
<p> The first non-option argument to cifscreds is a command (see the <font SIZE="-1"><code>COMMANDS</code></font> section below). The second non-option argument is a hostname or address, or an <font SIZE="-1">NT</font> domain name.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>add</code></p>
<dd> Add credentials to the kernel to be used for connecting to the given server, or servers in the given domain.</p>
<dt><code>clear</code></p>
<dd> Clear credentials for a particular host or domain from the kernel.</p>
<dt><code>clearall</code></p>
<dd> Clear all cifs credentials from the kernel.</p>
<dt><code>update</code></p>
<dd> Update stored credentials in the kernel with a new username and password.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;domain</code></p>
<dd> The provided host/domain argument is a <font SIZE="-1">NT</font> domainname. </p>
<p> Ordinarily the second argument provided to cifscreds is treated as a hostname or <font SIZE="-1">IP</font> address. This option causes the cifscreds program to treat that argument as an <font SIZE="-1">NT</font> domainname instead. </p>
<p> If there are not host specific credentials for the mounted server, then the kernel will next look for a set of domain credentials equivalent to the domain= option provided at mount time.</p>
<dt><code>-u</code>, <code>&#8211;username</code></p>
<dd> Ordinarily, the username is derived from the unix username of the user adding the credentials. This option allows the user to substitute a different username.</dl>
<h2>NOTES</h2>
<p> The cifscreds utility requires a kernel built with support for the <code>login</code> key type. That key type was added in v3.3 in mainline Linux kernels. </p>
<p> Since <code>cifscreds</code> adds keys to the session keyring, it is highly recommended that one use <code>pam_keyinit</code> to ensure that a session keyring is established at login time.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></i>(8)</p>
<h2>AUTHORS</h2>
<p> The cifscreds program was originally developed by Igor Druzhinin &lt;jaxbrigs [at] gmail.com&gt;. This manpage and a redesign of the code was done by Jeff Layton &lt;jlayton [at] samba.org&gt;. </p>
<h2>Index</h2>
