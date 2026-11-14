---
title: "service_seusers(5)"
name: "service_seusers"
section: "5"
letter: "s"
url: "/docs/linux/man/5-service_seusers/"
description: "service_seusers – The SELinux GNU/Linux user and service to SELinux user mapping configuration files"
---

<p>service_seusers &#8211; The SELinux GNU/Linux user and service to SELinux user mapping configuration files</p>
<h2>Description</h2>
<p>These are optional files that allow services to define an SELinux user when authenticating via SELinux-aware login applications such as <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8). </p>
<p> There is one file for each GNU/Linux user name that will be required to run a service with a specific SELinux user name. </p>
<p> The path for each configuration file is formed by the path returned by <code><a href="/docs/linux/man/3-selinux_policy_root/">selinux_policy_root</a></code>(3) with <i>/logins/username</i> appended (where <i>username</i> is a file representing the GNU/Linux user name). The default services directory is located at:</p>
<dl>
<dd><i>/etc/selinux/{SELINUXTYPE}/logins</i></dl>
<p> Where <i>{SELINUXTYPE}</i> is the entry from the selinux configuration file <i>config</i> (see <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5)). </p>
<p> <code><a href="/docs/linux/man/3-getseuser/">getseuser</a></code>(3) reads this file to map services to an SELinux user.</p>
<h2>File Format</h2>
<p>Each line within the <i>username</i> file is formatted as follows with each component separated by a colon:</p>
<dl>
<dd><i>service</i><code>:</code><i>seuser</i>[<code>:</code><i>range</i>]</dl>
<p> Where:</p>
<dl>
<dd><i>service</i></p>
<dl>
<dd>The service name used by the application.</dl>
<p> <i>seuser</i></p>
<dl>
<dd>The SELinux user name.</dl>
<p> <i>range</i></p>
<dl>
<dd>The range for MCS/MLS policies.</dl>
</dl>
<h2>Examples</h2>
<p>Example 1 &#8211; for the &#8216;root&#8217; user:</p>
<dl>
<dd># ./logins/root<br />
 ipa:user_u:s0<br />
 this_service:unconfined_u:s0</dl>
<p> Example 2 &#8211; for GNU/Linux user &#8216;rch&#8217;:</p>
<dl>
<dd># ./logins/rch<br />
 ipa:unconfined_u:s0<br />
 that_service:unconfined_u:s0</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-pam/">PAM</a></code>(8), <code><a href="/docs/linux/man/3-selinux_policy_root/">selinux_policy_root</a></code>(3), <code><a href="/docs/linux/man/3-getseuser/">getseuser</a></code>(3), <code><a href="/docs/linux/man/5-selinux_config/">selinux_config</a></code>(5) </p>
