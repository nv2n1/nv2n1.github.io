---
title: "krb5_digest_probe(3)"
name: "krb5_digest_probe"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_digest_probe/"
description: "Heimdal Kerberos 5 digest service –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 digest service &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_digest_probe</code> (krb5_context context, krb5_realm realm, krb5_ccache ccache, unsigned *flags)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_digest_probe (krb5_contextcontext, krb5_realmrealm, krb5_ccacheccache, unsigned *flags)</h3>
<p> Get the supported/allowed mechanism for this principal. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Keberos context.<br />
 <i>realm</i> The realm of the KDC.<br />
 <i>ccache</i> The credential cache to use when talking to the KDC.<br />
 <i>flags</i> The supported mechanism.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
