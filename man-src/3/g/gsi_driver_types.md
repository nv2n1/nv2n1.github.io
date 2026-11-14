---
title: "gsi_driver_types(3)"
name: "gsi_driver_types"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gsi_driver_types/"
description: "Types –"
---

<h2 class="name">NAME</h2>
<p> Types &#8211; </p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_xio_gsi_delegation_init_callback_t</code> )(globus_result_t result, void *user_arg) </p>
<p> typedef void(* <code>globus_xio_gsi_delegation_accept_callback_t</code> )(globus_result_t result, gss_cred_id_t delegated_cred, OM_uint32 time_rec, void *user_arg) </p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_gsi_protection_level_t</code> { <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_NONE</code>, <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_INTEGRITY</code>, <code>GLOBUS_XIO_GSI_PROTECTION_LEVEL_PRIVACY</code> } </p>
<p> enum <code>globus_xio_gsi_delegation_mode_t</code> { <code>GLOBUS_XIO_GSI_DELEGATION_MODE_NONE</code>, <code>GLOBUS_XIO_GSI_DELEGATION_MODE_LIMITED</code>, <code>GLOBUS_XIO_GSI_DELEGATION_MODE_FULL</code> } </p>
<p> enum <code>globus_xio_gsi_proxy_mode_t</code> { <code>GLOBUS_XIO_GSI_PROXY_MODE_FULL</code>, <code>GLOBUS_XIO_GSI_PROXY_MODE_LIMITED</code>, <code>GLOBUS_XIO_GSI_PROXY_MODE_MANY</code> } </p>
<p> enum <code>globus_xio_gsi_authorization_mode_t</code> { <code>GLOBUS_XIO_GSI_NO_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_SELF_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_IDENTITY_AUTHORIZATION</code>, <code>GLOBUS_XIO_GSI_HOST_AUTHORIZATION</code> } </p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* <code>globus_xio_gsi_delegation_init_callback_t</code>)(globus_result_t result, void *user_arg)</h3>
<p> Globus XIO GSI init delegation callback.</p>
<h3>typedef void(* <code>globus_xio_gsi_delegation_accept_callback_t</code>)(globus_result_t result, gss_cred_id_t delegated_cred, OM_uint32 time_rec, void *user_arg)</h3>
<p> Globus XIO GSI init delegation callback.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_gsi_protection_level_t</code></h3>
<p> Globus XIO GSI protection levels. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_GSI_PROTECTION_LEVEL_NONE </i></p>
<dd> No security.</p>
<dt><i>GLOBUS_XIO_GSI_PROTECTION_LEVEL_INTEGRITY </i></p>
<dd> Messages are signed.</p>
<dt><i>GLOBUS_XIO_GSI_PROTECTION_LEVEL_PRIVACY </i></p>
<dd> Messages are signed and encrypted.</dl>
<h3>enum <code>globus_xio_gsi_delegation_mode_t</code></h3>
<p> Globus XIO GSI delegation modes. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_GSI_DELEGATION_MODE_NONE </i></p>
<dd> No delegation.</p>
<dt><i>GLOBUS_XIO_GSI_DELEGATION_MODE_LIMITED </i></p>
<dd> Delegate a limited proxy.</p>
<dt><i>GLOBUS_XIO_GSI_DELEGATION_MODE_FULL </i></p>
<dd> Delegate a full proxy.</dl>
<h3>enum <code>globus_xio_gsi_proxy_mode_t</code></h3>
<p> Globus XIO GSI proxy modes. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_GSI_PROXY_MODE_FULL </i></p>
<dd> Accept only full proxies.</p>
<dt><i>GLOBUS_XIO_GSI_PROXY_MODE_LIMITED </i></p>
<dd> Accept full proxies and limited proxies if they are the only limited proxy in the cert chain.</p>
<dt><i>GLOBUS_XIO_GSI_PROXY_MODE_MANY </i></p>
<dd> Accept both full and limited proxies unconditionally.</dl>
<h3>enum <code>globus_xio_gsi_authorization_mode_t</code></h3>
<p> Globus XIO GSI authorization modes. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_GSI_NO_AUTHORIZATION </i></p>
<dd> Do not perform any authorization. This will cause a error when used in conjunction with delegation on the init/client side.</p>
<dt><i>GLOBUS_XIO_GSI_SELF_AUTHORIZATION </i></p>
<dd> Authorize the peer if the peer has the same identity as ourselves.</p>
<dt><i>GLOBUS_XIO_GSI_IDENTITY_AUTHORIZATION </i></p>
<dd> Authorize the peer if the peer identity matches the identity set in the target name.</p>
<dt><i>GLOBUS_XIO_GSI_HOST_AUTHORIZATION </i></p>
<dd> Authorize the peer if the identity of the peer matches the identity of the peer hostname.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio gsi driver from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
