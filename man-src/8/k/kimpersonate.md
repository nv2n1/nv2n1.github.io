---
title: "kimpersonate(8)"
name: "kimpersonate"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kimpersonate/"
description: "kimpersonate – impersonate a user when there exist a srvtab, keyfile or KeyFile"
---

<p><code>kimpersonate</code> &#8211; impersonate a user when there exist a srvtab, keyfile or KeyFile</p>
<h2>Synopsis</h2>
<p>[-<code>s </code><i>string | &#8211;</i><code>-server= </code><i>string</i> ] [-<code>c </code><i>string | &#8211;</i><code>-client= </code><i>string</i> ] [-<code>k </code><i>string | &#8211;</i><code>-keytab= </code><i>string</i> ] [-<code>5 | &#8211;krb5</code> ] [-<code>e </code><i>integer | &#8211;</i><code>-expire-time= </code><i>integer</i> ] [-<code>a </code><i>string | &#8211;</i><code>-client-address= </code><i>string</i> ] [-<code>t </code><i>string | &#8211;</i><code>-enc-type= </code><i>string</i> ] [-<code>-session-enc-type= </code><i>string</i> ] [-<code>f </code><i>string | &#8211;</i><code>-ticket-flags= </code><i>string</i> ] [-<code>-verbose</code> ] [-<code>-version</code> ] [-<code>-help</code> ]</p>
<h2>Description</h2>
<p>The program creates a &quot;fake&quot; ticket using the service-key of the service. The service key can be read from a Kerberos 5 keytab, AFS KeyFile or (if compiled with support for Kerberos 4) a Kerberos 4 srvtab. Supported options:</p>
<dl>
<dt><code>-s </code><i>string </i><code>, &#8211;server= </code><i>string</i></p>
<dd>name of server principal</p>
<dt><code>-c </code><i>string </i><code>, &#8211;client= </code><i>string</i></p>
<dd>name of client principal</p>
<dt><code>-k </code><i>string </i><code>, &#8211;keytab= </code><i>string</i></p>
<dd>name of keytab file</p>
<dt><code>-5 , &#8211;krb5</code></p>
<dd>create a Kerberos 5 ticket</p>
<dt><code>-e </code><i>integer </i><code>, &#8211;expire-time= </code><i>integer</i></p>
<dd>lifetime of ticket in seconds</p>
<dt><code>-a </code><i>string </i><code>, &#8211;client-address= </code><i>string</i></p>
<dd>address of client</p>
<dt><code>-t </code><i>string </i><code>, &#8211;enc-type= </code><i>string</i></p>
<dd>encryption type (defaults to &quot;aes256-cts-hmac-sha1-96&quot;)</p>
<dt><code>&#8211;session-enc-type= </code><i>string</i></p>
<dd>session encryption type (defaults to enc-type or &quot;des-cbc-crc&quot; for afs service tickets)</p>
<dt><code>-f </code><i>string </i><code>, &#8211;ticket-flags= </code><i>string</i></p>
<dd>ticket flags for krb5 ticket</p>
<dt><code>&#8211;verbose</code></p>
<dd>Verbose output</p>
<dt><code>&#8211;version</code></p>
<dd>Print version</p>
<dt><code>&#8211;help</code></p>
<dd></dl>
<h2>Files</h2>
<p>Uses /etc/krb5.keytab, /etc/srvtab and /usr/afs/etc/KeyFile when available and the &#8211;<code>k</code> option is used with an appropriate prefix.</p>
<h2>Examples</h2>
<p>can be used in <code>samba</code> root preexec option or for debugging. -s host/hummel.e.kth.se [at] E.KTH.SE -c lha [at] E.KTH.SE -5 will create a Kerberos 5 ticket for lha [at] E.KTH.SE for the host hummel.e.kth.se if there exists a keytab entry for it in /etc/krb5.keytab</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kinit/">kinit</a>(1), <a href="/docs/linux/man/1-klist/">klist</a>(1)</p>
<h2>Authors</h2>
<p>Love Hornquist Astrand &lt;lha [at] kth.se&gt;</p>
