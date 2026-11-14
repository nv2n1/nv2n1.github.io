---
title: "local-users(5)"
name: "local-users"
section: "5"
letter: "l"
url: "/docs/linux/man/5-local-users/"
description: "local.users – The SELinux local users configuration file"
---

<p>local.users &#8211; The SELinux local users configuration file</p>
<h2>Description</h2>
<p>The file contains local user definitions in the form of policy language user statements and is only found on older SELinux systems as it has been deprecated and replaced by the <code><a href="/docs/linux/man/8-semange/">semange</a></code>(8) services. </p>
<p> This file is only read by <code><a href="/docs/linux/man/3-selinux_mkload_policy/">selinux_mkload_policy</a></code>(3) when <code>SETLOCALDEFS</code> in the SELinux <i>config</i> file (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)) is set to <i>1</i>. </p>
<p> <code><a href="/docs/linux/man/3-selinux_users_path/">selinux_users_path</a></code>(3) will return the active policy path to the directory where this file is located. The default local users file is:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/contexts/users/local.users</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)).</p>
<h2>File Format</h2>
<p>The file consists of one or more entries terminated with &#8216;<code>;</code>&#8216;, each on a separate line as follows:</p>
<dl>
<dd><code>user </code><i>seuser_id </i><code>roles </code><i>role_id</i> [[<code>level </code><i>level</i>] [<code>range </code><i>range</i>]]<code>;</code></dl>
<p> Where:</p>
<dl>
<dd><code>user</code></p>
<dl>
<dd>The user keyword.</dl>
<p> <i>seuser_id</i></p>
<dl>
<dd>The SELinux user identifier.</dl>
<p> <code>roles</code></p>
<dl>
<dd>The roles keyword.</dl>
<p> <i>role_id</i></p>
<dl>
<dd>One or more previously declared role identifiers. Multiple role identifiers consist of a space separated list enclosed in braces &#8216;{}&#8217;.</dl>
<p> <code>level</code></p>
<dl>
<dd>If MLS/MCS is configured, the level keyword.</dl>
<p> <i>level</i></p>
<dl>
<dd>The users default security level. Note that only the sensitivity component of the level (e.g. s0) is required.</dl>
<p> <code>range</code></p>
<dl>
<dd>If MLS/MCS is configured, the range keyword.</dl>
<p> <i>range</i></p>
<dl>
<dd>The current and clearance levels that the user can run. These are separated by a hyphen &#8216;<code>&#8211;</code>&#8216; as shown in the <code>EXAMPLE</code> section.</dl>
</dl>
<h2>Example</h2>
<p># ./users/local.users<br />
 user test_u roles staff_r level s0 range s0 &#8211; s15:c0.c1023;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-semanage/">semanage</a></code>(8), <code><a href="/docs/linux/man/3-selinux_users_path/">selinux_users_path</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5), <code><a href="/docs/linux/man/3-selinux_mkload_policy/">selinux_mkload_policy</a></code>(3) </p>
