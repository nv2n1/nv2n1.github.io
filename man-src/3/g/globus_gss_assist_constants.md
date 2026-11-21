---
title: "globus_gss_assist_constants(3)"
name: "globus_gss_assist_constants"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gss_assist_constants/"
description: "GSI GSS Assist Constants –"
---

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
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_SUCCESS </i></dt>
<dd> Success</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_ARGUMENTS </i></dt>
<dd> No user entry in gridmap file</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_USER_ID_DOESNT_MATCH </i></dt>
<dd> Error user ID doesn&#8217;t match</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_IN_GRIDMAP_NO_USER_ENTRY </i></dt>
<dd> Error with arguments passed to function</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_GRIDMAP </i></dt>
<dd> Error querying gridmap file</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_INVALID_GRIDMAP_FORMAT </i></dt>
<dd> Invalid gridmap file format</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_ERRNO </i></dt>
<dd> System Error</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_INIT </i></dt>
<dd> Error during context initialization</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_WRAP </i></dt>
<dd> Error during message wrap</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_TOKEN </i></dt>
<dd> Error with token</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_EXPORTING_CONTEXT </i></dt>
<dd> Error exporting context</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_IMPORTING_CONTEXT </i></dt>
<dd> Error importing context</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_INITIALIZING_CALLOUT_HANDLE </i></dt>
<dd> Error initializing callout handle</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_WITH_CALLOUT_CONFIG </i></dt>
<dd> Error reading callout configuration</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_CALLOUT_ERROR </i></dt>
<dd> Error invoking callout</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_GSSAPI_ERROR </i></dt>
<dd> A GSSAPI returned an error</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_GRIDMAP_LOOKUP_FAILED </i></dt>
<dd> Gridmap lookup failure</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_BUFFER_TOO_SMALL </i></dt>
<dd> Caller provided insufficient buffer space for local identity</dd>
<dt><i>GLOBUS_GSI_GSS_ASSIST_ERROR_CANONICALIZING_HOSTNAME </i></dt>
<dd> Failed to obtain canonical host name</dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gss_assist from the source code. </p>
