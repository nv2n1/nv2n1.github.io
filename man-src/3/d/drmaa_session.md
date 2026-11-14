---
title: "drmaa_session(3)"
name: "drmaa_session"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_session/"
description: "drmaa_init, drmaa_exit – Start/finish xxQS_NAMExx DRMAA session"
---

<h2 class="name">NAME</h2>
<p> drmaa_init, drmaa_exit &#8211; Start/finish xxQS_NAMExx DRMAA session</p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre><code>
int drmaa_init(
const char *contact,
char *error_diagnosis,
size_t&amp;nbsp;error_diag_len
</code></pre>
<p> <code>);</code> </p>
<pre>
<code>int drmaa_exit(</code>
<dl><dt><dd><code>char *</code><i>error_diagnosis</i><code>,</code>
<code>size_t&nbsp;</code><i>error_diag_len</i>
</dl>
</pre>
<p> <code>);</code></p>
<h2>DESCRIPTION</h2>
<h3>drmaa_init()</h3>
<p> The drmaa_init() function initializes the xxQS_NAMExx DRMAA API library for all threads of the process and creates a new DRMAA session. This routine must be called once before any other DRMAA call, except for and Except for the above listed functions, no DRMAA functions may be called before the drmaa_init() function <i>completes</i>. Any DRMAA function which is called before the drmaa_init() function completes will return a DRMAA_ERRNO_NO_ACTIVE_SESSION error. <i>Contact</i> is an implementation dependent string which may be used to specify which xxQS_NAMExx cell to use. If <i>contact</i> is NULL, the default xxQS_NAMExx cell will be used. In the 1.0 implementation <i>contact</i> may have the following value: <code>session=</code><i>session_id</i>. To determine the session_id, the function should be called after the session has already been initialized. By passing the <code>session=</code><i>session_id</i> string to the drmaa_init() function, instead of creating a new session, DRMAA will attempt to reconnect to the session indicated by the <i>session_id</i>. The result of reconnecting to a previous session is that all jobs previously submitted in that session <code>that are still running</code> will be available in the DRMAA session. Note, however, that jobs which ended before the call to drmaa_init() may not be available or may have no associated exit information or resource usage data. </p>
<h3>drmaa_exit()</h3>
<p> The drmaa_exit() function closes the DRMAA session for all threads and must be called before process termination. The drmaa_exit() function may be called only once by a single thread in the process and may only be called after the drmaa_init() function has completed. Any DRMAA function, other than which is called after the drmaa_exit() function completes will return a DRMAA_ERRNO_NO_ACTIVE_SESSION error. </p>
<p> The drmaa_exit() function does necessary clean up of the DRMAA session state, including unregistering from the If the drmaa_exit() function is not called, the qmaster will store events for the DRMAA client until the connection times out, causing extra work for the qmaster and consuming system resources. </p>
<p> Submitted jobs are not affected by the drmaa_exit() function. </p>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell to be used. To address a xxQS_NAMExx cell xxQS_NAMExx uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which the xxqs_name_sxx_qmaster is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</dl>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, drmaa_init() and drmaa_exit() return DRMAA_ERRNO_SUCCESS. Other values indicate an error. Up to <i>error_diag_len</i> characters of error related diagnosis information is then provided in the buffer <i>error_diagnosis</i>. </p>
<h2>ERRORS</h2>
<p> The drmaa_init() and drmaa_exit() functions can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_INTERNAL_ERROR</code></p>
<dd> Unexpected or internal DRMAA error, like system call failure, etc.</p>
<dt><code>DRMAA_ERRNO_DRM_COMMUNICATION_FAILURE</code></p>
<dd> Could not contact DRM system for this request.</p>
<dt><code>DRMAA_ERRNO_AUTH_FAILURE</code></p>
<dd> The specified request is not processed successfully due to authorization failure.</p>
<dt><code>DRMAA_ERRNO_INVALID_ARGUMENT</code></p>
<dd> The input value for an argument is invalid.</dl>
<p> The drmaa_init() function can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_INVALID_CONTACT_STRING</code></p>
<dd> Initialization failed due to invalid contact string.</p>
<dt><code>DRMAA_ERRNO_DEFAULT_CONTACT_STRING_ERROR</code></p>
<dd> Could not use the default contact string to connect to DRM system.</p>
<dt><code>DRMAA_ERRNO_DRMS_INIT_FAILED</code></p>
<dd> Initialization failed due to failure to init DRM system.</p>
<dt><code>DRMAA_ERRNO_ALREADY_ACTIVE_SESSION</code></p>
<dd> Initialization failed due to existing DRMAA session.</p>
<dt><code>DRMAA_ERRNO_NO_MEMORY</code></p>
<dd> Failed allocating memory.</dl>
<p> The drmaa_exit() function can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_NO_ACTIVE_SESSION</code></p>
<dd> Failed because there is no active session.</p>
<dt><code>DRMAA_ERRNO_DRMS_EXIT_ERROR</code></p>
<dd> DRM system disengagement failed.</dl>
<h2>SEE ALSO</h2>
<h2>Index</h2>
