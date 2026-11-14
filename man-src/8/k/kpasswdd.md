---
title: "kpasswdd(8)"
name: "kpasswdd"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kpasswdd/"
description: "kpasswdd – Kerberos 5 password changing server"
---

<p><code>kpasswdd</code> &#8211; Kerberos 5 password changing server</p>
<h2>Synopsis</h2>
<p>-words [-<code>-addresses= </code><i>address</i> ] [-<code>-check-library= </code><i>library</i> ] [-<code>-check-function= </code><i>function</i> ] [-<code>k </code><i>kspec | </i> &#8211;<code>-keytab= </code><i>kspec</i> ] [-<code>r </code><i>realm | </i> &#8211;<code>-realm= </code><i>realm</i> ] [-<code>p </code><i>string | </i> &#8211;<code>-port= </code><i>string</i> ] [-<code>-version</code> ] [-<code>-help</code> ]</p>
<h2>Description</h2>
<p>serves request for password changes. It listens on UDP port 464 (service kpasswd) and processes requests when they arrive. It changes the database directly and should thus only run on the master KDC. Supported options:</p>
<dl>
<dt><code>&#8211;addresses= </code><i>address</i></p>
<dd>For each till the argument is given, add the address to what kpasswdd should listen too.</p>
<dt><code>&#8211;check-library= </code><i>library</i></p>
<dd>If your system has support for dynamic loading of shared libraries, you can use an external function to check password quality. This option specifies which library to load.</p>
<dt><code>&#8211;check-function= </code><i>function</i></p>
<dd>This is the function to call in the loaded library. The function should look like this: Ft const char * Fn passwd_check krb5_context context krb5_principal principal krb5_data *password Fa context is an initialized context; Fa principal is the one who tries to change passwords, and Fa password is the new password. Note that the password (in Fa password-&gt;data ) is not zero terminated.</p>
<dt><code>-k </code><i>kspec , &#8211;</i><code>-keytab= </code><i>kspec</i></p>
<dd>Keytab to get authentication key from.</p>
<dt><code>-r </code><i>realm , &#8211;</i><code>-realm= </code><i>realm</i></p>
<dd>Default realm.</p>
<dt><code>-p </code><i>string , &#8211;</i><code>-port= </code><i>string</i></p>
<dd>Port to listen on (default service kpasswd &#8211; 464).</dl>
<h2>Diagnostics</h2>
<p>If an error occurs, the error message is returned to the user and/or logged to syslog.</p>
<h2>Bugs</h2>
<p>The default password quality checks are too basic.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kpasswd/">kpasswd</a>(1), <a href="/docs/linux/man/8-kdc/">kdc</a>(8) </p>
