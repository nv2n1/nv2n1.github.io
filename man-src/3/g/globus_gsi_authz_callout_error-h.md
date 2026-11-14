---
title: "globus_gsi_authz_callout_error-h(3)"
name: "globus_gsi_authz_callout_error-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_authz_callout_error-h/"
description: "globus_gsi_authz_callout_error.h – GSI Authorization Callout Error API."
---

<p>globus_gsi_authz_callout_error.h &#8211; GSI Authorization Callout Error API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GSI_AUTHZ_CALLOUT_ERROR_MODULE</code> (&amp;globus_gsi_authz_callout_error_module)<br />
 <i>Module descriptor. </i><br />
 #define <code>GLOBUS_GSI_AUTHZ_CALLOUT_ERROR</code>(__RESULT, __TYPE, __ERRSTR)<br />
 <i>Create an authorization callout error object. </i><br />
 #define <code>GLOBUS_GSI_AUTHZ_CALLOUT_ERRNO_ERROR</code>(__RESULT, __ERRNO)<br />
 <i>Create an authorization callout error object with an errno. </i></p>
<h3>Enumerations</h3>
<p>enum <code>globus_gsi_authz_callout_error_t</code> { <code>GLOBUS_GSI_AUTHZ_CALLOUT_AUTHZ_CALLOUT_ERROR</code> = 0, <code>GLOBUS_GSI_AUTHZ_CALLOUT_AUTHZ_DENIED_BY_CALLOUT</code> = 1, <code>GLOBUS_GSI_AUTHZ_CALLOUT_CONFIGURATION_ERROR</code> = 2, <code>GLOBUS_GSI_AUTHZ_CALLOUT_SYSTEM_ERROR</code> = 3, <code>GLOBUS_GSI_AUTHZ_CALLOUT_CREDENTIAL_ERROR</code> = 4, <code>GLOBUS_GSI_AUTHZ_CALLOUT_BAD_ARGUMENT_ERROR</code> = 5 }<br />
 <i>Error codes. </i></p>
<h2>Detailed Description</h2>
<p>GSI Authorization Callout Error API. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_authz_callout_error from the source code.</p>
