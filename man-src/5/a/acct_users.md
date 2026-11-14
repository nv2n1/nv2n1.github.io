---
title: "acct_users(5)"
name: "acct_users"
section: "5"
letter: "a"
url: "/docs/linux/man/5-acct_users/"
description: "acct_users – user accounting file for the FreeRADIUS server"
---

<p>acct_users &#8211; user accounting file for the FreeRADIUS server</p>
<h2>Description</h2>
<p>The <code>acct_users</code> file resides in the radius database directory, by default <code>/etc/raddb</code>. It contains a series of configuration directives which are used by the <i>files</i> module to decide how to log accounting messages. The format of this file is identical to that of the <code>users</code> file, except that it controls the response to accounting requests, not authentication requests. </p>
<h2>Files</h2>
<p>/etc/raddb/acct_users</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-radclient/">radclient</a></code>(1), <code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-dictionary/">dictionary</a></code>(5), <code><a href="/docs/linux/man/5-users/">users</a></code>(5) </p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] ox.org&gt;</p>
