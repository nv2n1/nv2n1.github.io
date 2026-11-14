---
title: "sasldblistusers2(8)"
name: "sasldblistusers2"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sasldblistusers2/"
description: "sasldblistusers2 – list users in sasldb"
---

<p>sasldblistusers2 &#8211; list users in sasldb</p>
<h2>Synopsis</h2>
<p><code>sasldblistusers2</code> [<code>-f file</code>] [<code>-v</code>]</p>
<h2>Description</h2>
<p><i>sasldblistusers2</i> is used to list the users in the SASL password database (usually /etc/sasldb2). This will NOT list all the users in /etc/passwd, shadow, PAM, etc. only those created by SASL (via <i>saslpasswd2</i>).</p>
<h2>Options</h2>
<dl>
<dt><code>-f file</code></p>
<dd>use <code>file</code> for sasldb</p>
<dt><code>-v</code></p>
<dd>Print libsasl2 version number and exit.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-saslpasswd2/">saslpasswd2</a>(8)</p>
<dl>
<dt>rfc4422 &#8211; Simple Authentication and Security Layer (SASL)</p>
<dd>
