---
title: "heimdal-kpasswd(1)"
name: "heimdal-kpasswd"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-kpasswd/"
description: "kpasswd – Kerberos 5 password changing program"
---

<h2 class="name">NAME</h2>
<p> <code>kpasswd</code> &#8211; Kerberos 5 password changing program </p>
<h2>SYNOPSIS</h2>
<p> [-<code>-admin-principal= </code><i>principal</i> ] [-<code>c </code><i>cache | </i> &#8211;<code>-cache= </code><i>cache</i> ] [<i>principal &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> is the client for changing passwords. </p>
<p> If administrator principal is given that principal is used to change the password. </p>
<p> Multiple passwords for different users can be changed at the same time, then the administrator principal will be used. If the administrator isn&#8217;t specified on the command prompt, the principal of the default credential cache will be used. </p>
<p> If a credential cache is given, the &#8211;<code>-admin-principal</code> flag is ignored and use the default name of the credential cache is used instead.</p>
<h2>DIAGNOSTICS</h2>
<p> If the password quality check fails or some other error occurs, an explanation is printed.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-kpasswdd/">kpasswdd</a>(8) </p>
<h2>Index</h2>
