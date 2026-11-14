---
title: "globus_gram_jobmanager_callout_bad_creds(3)"
name: "globus_gram_jobmanager_callout_bad_creds"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_jobmanager_callout_bad_creds/"
description: "Datatypes –"
---

<p>Datatypes &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_gram_jobmanager_callout_error_t</code> { <code>GLOBUS_GRAM_JOBMANAGER_CALLOUT_BAD_CREDS</code> = 0, <code>GLOBUS_GRAM_JOBMANAGER_CALLOUT_AUTHZ_SYSTEM_ERROR</code> = 1, <code>GLOBUS_GRAM_JOBMANAGER_CALLOUT_AUTHZ_DENIED</code> = 2, <code>GLOBUS_GRAM_JOBMANAGER_CALLOUT_AUTHZ_DENIED_INVALID_JOB</code> = 3, <code>GLOBUS_GRAM_JOBMANAGER_CALLOUT_AUTHZ_DENIED_BAD_EXECUTABLE</code> = 4, <code>GLOBUS_GRAM_JOBMANAGER_CALLOUT_ERROR_LAST</code> = 5 } </p>
<h2>Detailed Description</h2>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gram_jobmanager_callout_error_t</code></h3>
<p>GRAM Jobmanager Callout Error codes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GRAM_JOBMANAGER_CALLOUT_BAD_CREDS </i></p>
<dd>Credentials not accepted</p>
<dt><i>GLOBUS_GRAM_JOBMANAGER_CALLOUT_AUTHZ_SYSTEM_ERROR </i></p>
<dd>Authorization system misconfigured</p>
<dt><i>GLOBUS_GRAM_JOBMANAGER_CALLOUT_AUTHZ_DENIED </i></p>
<dd>Authorization denied</p>
<dt><i>GLOBUS_GRAM_JOBMANAGER_CALLOUT_AUTHZ_DENIED_INVALID_JOB </i></p>
<dd>Authorization denied &#8211; invalid job id</p>
<dt><i>GLOBUS_GRAM_JOBMANAGER_CALLOUT_AUTHZ_DENIED_BAD_EXECUTABLE </i></p>
<dd>Authorization denied &#8211; executable not allowed</p>
<dt><i>GLOBUS_GRAM_JOBMANAGER_CALLOUT_ERROR_LAST </i></p>
<dd>Last marker &#8211; never used</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gram_job_manager_callout_error from the source code.</p>
