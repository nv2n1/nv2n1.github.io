---
title: "slapd-passwd(5)"
name: "slapd-passwd"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-passwd/"
description: "slapd-passwd – /etc/passwd backend to slapd"
---

<p>slapd-passwd &#8211; /etc/passwd backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The PASSWD backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) serves up the user account information listed in the system <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5) file. This backend is provided for demonstration purposes only. The DN of each entry is &quot;uid=&lt;username&gt;,&lt;suffix&gt;&quot;. Note that non-base searches scan the entire passwd file, and are best suited for hosts with small passwd files.</p>
<h2>Configuration</h2>
<p>This <code>slapd.conf</code> option applies to the PASSWD backend database. That is, it must follow a &quot;database passwd&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page.</p>
<dl>
<dt><code>file &lt;filename&gt;</code></p>
<dd>Specifies an alternate passwd file to use. The default is <code>/etc/passwd</code>.</dl>
<h2>Access Control</h2>
<p>The <code>passwd</code> backend does not honor any of the access control semantics described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5). Only <code>read (=r)</code> access to the <code>entry</code> pseudo-attribute and to the other attribute values of the entries returned by the <code>search</code> operation is honored, which is performed by the frontend.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</p>
<dt>/etc/passwd</p>
<dd>user account information</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5). </p>
