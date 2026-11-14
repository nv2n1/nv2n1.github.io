---
title: "slapd-ldif(5)"
name: "slapd-ldif"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-ldif/"
description: "slapd-ldif – LDIF backend to slapd"
---

<p>slapd-ldif &#8211; LDIF backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The LDIF backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) is a basic storage backend that stores entries in text files in LDIF format, and exploits the filesystem to create the tree structure of the database. It is intended as a cheap, low performance easy to use backend, and it is exploited by higher-level internal structures to provide a permanent storage.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the LDIF backend database. That is, they must follow a &quot;database ldif&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page.</p>
<dl>
<dt><code>directory &lt;dir&gt;</code></p>
<dd>Specify the directory where the database tree starts. The directory must exist and grant appropriate permissions (rwx) to the identity slapd is running with.</dl>
<h2>Access Control</h2>
<p>The <code>LDIF</code> backend does not honor any of the access control semantics described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5). Only <code>read (=r)</code> access to the <code>entry</code> pseudo-attribute and to the other attribute values of the entries returned by the <code>search</code> operation is honored, which is performed by the frontend.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5).</p>
<h2>Author</h2>
<p>Eric Stokes</p>
