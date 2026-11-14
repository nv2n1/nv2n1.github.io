---
title: "nslcd(8)"
name: "nslcd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nslcd/"
description: "nslcd – local LDAP name service daemon"
---

<p>nslcd &#8211; local LDAP name service daemon</p>
<h2>Synopsis</h2>
<p><code>nslcd</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>nslcd</code> is a daemon that will do LDAP queries for local processes that want to do user, group and other naming lookups (NSS) or do user authentication, authorisation or password modification (PAM). </p>
<p> <code>nslcd</code> is configured through a configuration file (see <code><a href="/docs/linux/man/5-nslcd-conf/">nslcd.conf</a></code>(5)). </p>
<p> See the included README for information on configuring the LDAP server.</p>
<h2>Options</h2>
<p><code>nslcd</code> accepts the following options:</p>
<dl>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd>Check if the daemon is running. This causes <code>nslcd</code> to return 0 if the daemon is already running and 1 if it is not.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Enable debugging mode. <code>nslcd</code> will not put itself in the background and sends verbose debugging info to stderr. <code>nslcd</code> will handle connections as usual. This option is for debugging purposes only. Specify this option multiple times to also include more detailed logging from the LDAP library.</p>
<dt><code>&#8211;help</code></p>
<dd>Display short help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output version information and exit.</dl>
<h2>Files</h2>
<p><i>/etc/nslcd.conf</i> &#8211; the configuration file (see <code><a href="/docs/linux/man/5-nslcd-conf/">nslcd.conf</a></code>(5))</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nslcd-conf/">nslcd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>This manual was written by Arthur de Jong &lt;arthur [at] arthurdejong.org&gt;.</p>
