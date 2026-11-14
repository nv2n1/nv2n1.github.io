---
title: "krb5_rd_req(3)"
name: "krb5_rd_req"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_rd_req/"
description: "krb5_mk_req krb5_mk_req_exact krb5_mk_req_extended krb5_rd_req krb5_rd_req_with_keyblock krb5_mk_rep krb5_mk_rep_exact krb5_mk_rep_extended krb5_rd_rep krb5_build_ap_req krb5_verify_ap_req – create..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_mk_req</code> <code>krb5_mk_req_exact</code> <code>krb5_mk_req_extended</code> <code>krb5_rd_req</code> <code>krb5_rd_req_with_keyblock</code> <code>krb5_mk_rep</code> <code>krb5_mk_rep_exact</code> <code>krb5_mk_rep_extended</code> <code>krb5_rd_rep</code> <code>krb5_build_ap_req</code> <code>krb5_verify_ap_req</code> &#8211; create and read application authentication request </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_mk_req Fa krb5_context context Fa krb5_auth_context *auth_context Fa const krb5_flags ap_req_options Fa const char *service Fa const char *hostname Fa krb5_data *in_data Fa krb5_ccache ccache Fa krb5_data *outbuf Fc Ft krb5_error_code Fo krb5_mk_req_extended Fa krb5_context context Fa krb5_auth_context *auth_context Fa const krb5_flags ap_req_options Fa krb5_data *in_data Fa krb5_creds *in_creds Fa krb5_data *outbuf Fc Ft krb5_error_code Fo krb5_rd_req Fa krb5_context context Fa krb5_auth_context *auth_context Fa const krb5_data *inbuf Fa krb5_const_principal server Fa krb5_keytab keytab Fa krb5_flags *ap_req_options Fa krb5_ticket **ticket Fc Ft krb5_error_code Fo krb5_build_ap_req Fa krb5_context context Fa krb5_enctype enctype Fa krb5_creds *cred Fa krb5_flags ap_options Fa krb5_data authenticator Fa krb5_data *retdata Fc Ft krb5_error_code Fo krb5_verify_ap_req Fa krb5_context context Fa krb5_auth_context *auth_context Fa krb5_ap_req *ap_req Fa krb5_const_principal server Fa krb5_keyblock *keyblock Fa krb5_flags flags Fa krb5_flags *ap_req_options Fa krb5_ticket **ticket Fc</p>
<h2>DESCRIPTION</h2>
<p> The functions documented in this manual page document the functions that facilitates the exchange between a Kerberos client and server. They are the core functions used in the authentication exchange between the client and the server. </p>
<p> The <code>krb5_mk_req</code> and <code>krb5_mk_req_extended</code> creates the Kerberos message <code>KRB_AP_REQ</code> that is sent from the client to the server as the first packet in a client/server exchange. The result that should be sent to server is stored in Fa outbuf . </p>
<p> Fa auth_context should be allocated with Fn krb5_auth_con_init or <code>NULL</code> passed in, in that case, it will be allocated and freed internally. </p>
<p> The input data Fa in_data will have a checksum calculated over it and checksum will be transported in the message to the server. </p>
<p> Fa ap_req_options can be set to one or more of the following flags: </p>
<dl>
<dt><code>AP_OPTS_USE_SESSION_KEY</code></p>
<dd> Use the session key when creating the request, used for user to user authentication.</p>
<dt><code>AP_OPTS_MUTUAL_REQUIRED</code></p>
<dd> Mark the request as mutual authenticate required so that the receiver returns a mutual authentication packet.</dl>
<p> The <code>krb5_rd_req</code> read the AP_REQ in Fa inbuf and verify and extract the content. If Fa server is specified, that server will be fetched from the Fa keytab and used unconditionally. If Fa server is <code>NULL</code> the Fa keytab will be search for a matching principal. </p>
<p> The Fa keytab argument specifies what keytab to search for receiving principals. The arguments Fa ap_req_options and Fa ticket returns the content. </p>
<p> When the AS-REQ is a user to user request, neither of Fa keytab or Fa principal are used, instead Fn krb5_rd_req expects the session key to be set in Fa auth_context . </p>
<p> The <code>krb5_verify_ap_req</code> and <code>krb5_build_ap_req</code> both constructs and verify the AP_REQ message, should not be used by external code.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5.conf5 </p>
<h2>Index</h2>
