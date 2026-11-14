---
title: "krb5_pac_verify(3)"
name: "krb5_pac_verify"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_pac_verify/"
description: "Heimdal Kerberos 5 PAC handling functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 PAC handling functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_pac_get_buffer</code> (krb5_context, krb5_pac, uint32_t, krb5_data *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_pac_verify</code> (krb5_context, const krb5_pac, time_t, krb5_const_principal, const krb5_keyblock *, const krb5_keyblock *)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_pac_get_buffer (krb5_contextcontext, krb5_pacp, uint32_ttype, krb5_data *data)</h3>
<p> Get the PAC buffer of specific type from the pac. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>p</i> the pac structure returned by krb5_pac_parse().<br />
 <i>type</i> type of buffer to get<br />
 <i>data</i> return data, free with <code>krb5_data_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_pac_verify (krb5_contextcontext, const krb5_pacpac, time_tauthtime, krb5_const_principalprincipal, const krb5_keyblock *server, const krb5_keyblock *privsvr)</h3>
<p> Verify the PAC. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>pac</i> the pac structure returned by krb5_pac_parse().<br />
 <i>authtime</i> The time of the ticket the PAC belongs to.<br />
 <i>principal</i> the principal to verify.<br />
 <i>server</i> The service key, most always be given.<br />
 <i>privsvr</i> The KDC key, may be given.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns 0 to indicate success. Otherwise an kerberos et error code is returned, see <code>krb5_get_error_message()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
