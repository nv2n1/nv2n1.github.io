---
title: "krb5_mk_priv(3)"
name: "krb5_mk_priv"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_mk_priv/"
description: "krb5_mk_safe krb5_mk_priv – generates integrity protected and/or encrypted messages"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_mk_safe</code> <code>krb5_mk_priv</code> &#8211; generates integrity protected and/or encrypted messages </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> Ft krb5_error_code Fn krb5_mk_priv krb5_context context krb5_auth_context auth_context const krb5_data *userdata krb5_data *outbuf krb5_replay_data *outdata Ft krb5_error_code Fn krb5_mk_safe krb5_context context krb5_auth_context auth_context const krb5_data *userdata krb5_data *outbuf krb5_replay_data *outdata</p>
<h2>DESCRIPTION</h2>
<p> Fn krb5_mk_safe and Fn krb5_mk_priv formats <code>KRB-SAFE</code> (integrity protected) and <code>KRB-PRIV</code> (also encrypted) messages into Fa outbuf . The actual message data is taken from Fa userdata . If the <code>KRB5_AUTH_CONTEXT_DO_SEQUENCE</code> or <code>KRB5_AUTH_CONTEXT_DO_TIME</code> flags are set in the Fa auth_context , sequence numbers and time stamps are generated. If the <code>KRB5_AUTH_CONTEXT_RET_SEQUENCE</code> or <code>KRB5_AUTH_CONTEXT_RET_TIME</code> flags are set they are also returned in the Fa outdata parameter.</p>
<h2>SEE ALSO</h2>
<p> krb5_auth_con_init3, krb5_rd_priv3, krb5_rd_safe3 </p>
<h2>Index</h2>
