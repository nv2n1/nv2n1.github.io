---
title: "krb5_v4compat(3)"
name: "krb5_v4compat"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_v4compat/"
description: "Heimdal Kerberos 4 compatiblity functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 4 compatiblity functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb524_convert_creds_kdc</code> (krb5_context context, krb5_creds *in_cred, struct credentials *v4creds) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb524_convert_creds_kdc_ccache</code> (krb5_context context, krb5_ccache ccache, krb5_creds *in_cred, struct credentials *v4creds) <code>KRB5_DEPRECATED_FUNCTION</code>(&#8216;Use X instead&#8217;)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb524_convert_creds_kdc (krb5_contextcontext, krb5_creds *in_cred, struct credentials *v4creds)</h3>
<p> Convert the v5 credentials in in_cred to v4-dito in v4creds. This is done by sending them to the 524 function in the KDC. If `in_cred&#8217; doesn&#8217;t contain a DES session key, then a new one is gotten from the KDC and stored in the cred cache `ccache&#8217;. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>in_cred</i> the credential to convert<br />
 <i>v4creds</i> the converted credential</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb524_convert_creds_kdc_ccache (krb5_contextcontext, krb5_ccacheccache, krb5_creds *in_cred, struct credentials *v4creds)</h3>
<p> Convert the v5 credentials in in_cred to v4-dito in v4creds, check the credential cache ccache before checking with the KDC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>ccache</i> credential cache used to check for des-ticket.<br />
 <i>in_cred</i> the credential to convert<br />
 <i>v4creds</i> the converted credential</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
