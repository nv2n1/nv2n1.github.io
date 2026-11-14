---
title: "k5identity(5)"
name: "k5identity"
section: "5"
letter: "k"
url: "/docs/linux/man/5-k5identity/"
description: "k5identity – Kerberos V5 client principal selection rules"
---

<p>k5identity &#8211; Kerberos V5 client principal selection rules</p>
<h2>Description</h2>
<p>The .k5identity file, which resides in a user&#8217;s home directory, contains a list of rules for selecting a client principals based on the server being accessed. These rules are used to choose a credential cache within the cache collection when possible. </p>
<p> Blank lines and lines beginning with <code>#</code> are ignored. Each line has the form: <i>principal</i> <i>field</i>=<i>value</i> &#8230; </p>
<p> If the server principal meets all of the field constraints, then principal is chosen as the client principal. The following fields are recognized:</p>
<dl>
<dt><code>realm</code></p>
<dd>If the realm of the server principal is known, it is matched against <i>value</i>, which may be a pattern using shell wildcards. For host-based server principals, the realm will generally only be known if there is a <i>domain_realm</i> section in <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i> with a mapping for the hostname.</p>
<dt><code>service</code></p>
<dd>If the server principal is a host-based principal, its service component is matched against <i>value</i>, which may be a pattern using shell wildcards.</p>
<dt><code>host</code></p>
<dd>If the server principal is a host-based principal, its hostname component is converted to lower case and matched against <i>value</i>, which may be a pattern using shell wildcards. </p>
<p> If the server principal matches the constraints of multiple lines in the .k5identity file, the principal from the first matching line is used. If no line matches, credentials will be selected some other way, such as the realm heuristic or the current primary cache.</dl>
<h2>Example</h2>
<p>The following example .k5identity file selects the client principal <code>alice [at] KRBTEST.COM</code> if the server principal is within that realm, the principal <code>alice/root [at] EXAMPLE.COM</code> if the server host is within a servers subdomain, and the principal <code>alice/mail [at] EXAMPLE.COM</code> when accessing the IMAP service on <code>mail.example.com</code>: </p>
<pre>alice [at] KRBTEST.COM realm=KRBTEST.COM
alice/root [at] EXAMPLE.COM host=*.servers.example.com
alice/mail [at] EXAMPLE.COM host=mail.example.com service=imap</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kerberos/">kerberos</a>(1), <i><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2017, MIT</p>
