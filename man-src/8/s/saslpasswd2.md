---
title: "saslpasswd2(8)"
name: "saslpasswd2"
section: "8"
letter: "s"
url: "/docs/linux/man/8-saslpasswd2/"
description: "saslpasswd2 – set a user’s sasl password"
---

<p>saslpasswd2 &#8211; set a user&#8217;s sasl password</p>
<h2>Synopsis</h2>
<p><code>saslpasswd2</code> [<code>-p</code>] [<code>-d</code>] [<code>-c</code>] [<code>-n</code>] [<code>-f file</code>] [<code>-u domain</code>] [<code>-a appname</code>] [<code>-v</code>] <code>userid</code></p>
<h2>Description</h2>
<p><i>saslpasswd2</i> is used by a server administrator to set a user&#8217;s sasl password for server programs and SASL mechanisms which use the standard libsasl database of user secrets.</p>
<h2>Options</h2>
<dl>
<dt><code>-p</code></p>
<dd>Pipe mode &#8211; saslpasswd2 will neither prompt for the password nor verify that it was entered correctly. This is the default when standard input is not a terminal.</p>
<dt><code>-c</code></p>
<dd>Creates an entry for the user if the user doesn&#8217;t already exist. This is mutually exclusive with the <code>-d</code> (delete user) flag.</p>
<dt><code>-d</code></p>
<dd>Deletes the entry for the user. This is mutually exclusive with the <code>-c</code> (create user) flag.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t set the plaintext <i>userPassword</i> property for the user. Only mechanism-specific secrets will be set (e.g. OTP, SRP)</p>
<dt><code>-u domain</code></p>
<dd>use <code>domain</code> for user domain (realm).</p>
<dt><code>-f file</code></p>
<dd>use <code>file</code> for sasldb</p>
<dt><code>-a appname</code></p>
<dd>use <code>appname</code> as application name.</p>
<dt><code>-v</code></p>
<dd>Print libsasl2 version number and exit.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-sasldblistusers2/">sasldblistusers2</a>(8)</p>
<dl>
<dt>rfc4422 &#8211; Simple Authentication and Security Layer (SASL)</p>
<dd>
