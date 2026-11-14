---
title: "globus-rls-reporter(8)"
name: "globus-rls-reporter"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-rls-reporter/"
description: "globus-rls-reporter – Globus Replica Location Service MDS Reporter"
---

<p>globus-rls-reporter &#8211; Globus Replica Location Service MDS Reporter</p>
<h2>Synopsis</h2>
<p><code>globus-rls-reporter</code> [ <i>rls-server</i> ] [ <i>-c certfile</i> ] [ <i>-d distinguished-name</i> ] [ <i>-k keyfile</i> ] [ <i>-v</i> ]</p>
<h2>Description</h2>
<p><code>globus-rls-reporter</code> retrieves statistics from <i>rls-server</i> and reports them in LDAP LDIF format, suitable for parsing by MDS. <i>rls-server</i> defaults to <a href="rls://localhost">rls://localhost</a> if not specified. <i>Distinguished-name</i> defaults to &quot;RLS=stats, Mds-Vo-name=local, o=grid&quot;.</p>
<h2>Options</h2>
<dl>
<dt><code>-c certfile</code></p>
<dd>X509 certificate file to use for authentication to RLS server. By default it&#8217;s the host certificate in /etc/grid-security/hostcert.pem.</p>
<dt><code>-d distinguished-name</code></p>
<dd>Distinguished name to use when reporting to MDS. By default it is &quot;RLS=stats, Mds-Vo-name=local, o=grid&quot;.</p>
<dt><code>-k keyfile</code></p>
<dd>X509 key file to use for authentication to RLS server. By default it&#8217;s the host key file in /etc/grid-security/hostkey.pem.</p>
<dt><code>-v</code></p>
<dd>Show version and exit.</dl>
<h2>Seel Also</h2>
<p><a href="/docs/linux/man/8-globus-rls-server/">globus-rls-server</a>(8), globus_rls_client man pages</p>
