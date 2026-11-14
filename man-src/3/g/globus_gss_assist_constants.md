---
title: "globus_gss_assist_constants(3)"
name: "globus_gss_assist_constants"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_constants/"
description: "GSI GSS Assist Constants –"
---

<h2 class="name">NAME</h2>
<p> GSI GSS Assist Constants &#8211; </p>
<p> Constant Definitions.</p>
<h3>Enumerations</h3>
<p> enum <code>globus_gsi_gss_assist_error_t</code> { <code>GLOBUS_GSI_GSS_ASSIST_ERROR_SUCCESS</code> = 0, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_ARGUMENTS</code> = 1, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_USER_ID_DOESNT_MATCH</code> = 2, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_IN_GRIDMAP_NO_USER_ENTRY</code> = 3, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_GRIDMAP</code> = 4, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_INVALID_GRIDMAP_FORMAT</code> = 5, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_ERRNO</code> = 6, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_INIT</code> = 7, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_WRAP</code> = 8, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_TOKEN</code> = 9, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_EXPORTING_CONTEXT</code> = 10, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_IMPORTING_CONTEXT</code> = 11, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_INITIALIZING_CALLOUT_HANDLE</code> = 12, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_CALLOUT_CONFIG</code> = 13, <code>GLOBUS_GSI_GSS_ASSIST_CALLOUT_ERROR</code> = 14, <code>GLOBUS_GSI_GSS_ASSIST_GSSAPI_ERROR</code> = 15, <code>GLOBUS_GSI_GSS_ASSIST_GRIDMAP_LOOKUP_FAILED</code> = 16, <code>GLOBUS_GSI_GSS_ASSIST_BUFFER_TOO_SMALL</code> = 17, <code>GLOBUS_GSI_GSS_ASSIST_ERROR_CANONICALIZING_HOSTNAME</code> = 18 } </p>
<h2>Detailed Description</h2>
<p> Constant Definitions. </p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gsi_gss_assist_error_t</code></h3>
<p> GSI GSS Assist Error codes </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_SUCCESS </i></p>
<dd> Success</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_ARGUMENTS </i></p>
<dd> No user entry in gridmap file</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_USER_ID_DOESNT_MATCH </i></p>
<dd> Error user ID doesn&#8217;t match</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_IN_GRIDMAP_NO_USER_ENTRY </i></p>
<dd> Error with arguments passed to function</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_GRIDMAP </i></p>
<dd> Error querying gridmap file</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_INVALID_GRIDMAP_FORMAT </i></p>
<dd> Invalid gridmap file format</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_ERRNO </i></p>
<dd> System Error</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_INIT </i></p>
<dd> Error during context initialization</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_WRAP </i></p>
<dd> Error during message wrap</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_TOKEN </i></p>
<dd> Error with token</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_EXPORTING_CONTEXT </i></p>
<dd> Error exporting context</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_IMPORTING_CONTEXT </i></p>
<dd> Error importing context</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_INITIALIZING_CALLOUT_HANDLE </i></p>
<dd> Error initializing callout handle</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_CALLOUT_CONFIG </i></p>
<dd> Error reading callout configuration</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_CALLOUT_ERROR </i></p>
<dd> Error invoking callout</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_GSSAPI_ERROR </i></p>
<dd> A GSSAPI returned an error</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_GRIDMAP_LOOKUP_FAILED </i></p>
<dd> Gridmap lookup failure</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_BUFFER_TOO_SMALL </i></p>
<dd> Caller provided insufficient buffer space for local identity</p>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_CANONICALIZING_HOSTNAME </i></p>
<dd> Failed to obtain canonical host name</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAG">Author</a></p>
<dd></dl>
