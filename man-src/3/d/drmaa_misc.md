---
title: "drmaa_misc(3)"
name: "drmaa_misc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_misc/"
description: "drmaa_strerror, drmaa_get_contact, drmaa_version, drmaa_get_DRM_system – Miscellaneous DRMAA functions."
---

<h2 class="name">NAME</h2>
<p> drmaa_strerror, drmaa_get_contact, drmaa_version, drmaa_get_DRM_system &#8211; Miscellaneous DRMAA functions.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre><code>
const char *drmaa_strerror(
int&amp;nbsp;drmaa_errno
</code></pre>
<p> <code>);</code> </p>
<p>int drmaa_get_contact(<br />
char *contact,<br />
size_t&amp;nbsp;contact_len,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<p>int drmaa_version(<br />
unsigned int *major,<br />
unsigned int *minor,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<p>int drmaa_get_DRM_system(<br />
char *drm_system,<br />
size_t&amp;nbsp;drm_system_len,<br />
char *error_diagnosis,<br />
size_t&amp;nbsp;error_diag_len<br />
 <code>);</code> </p>
<pre><code>
int drmaa_get_DRMAA_implementation(
char *drm_impl,
size_t&amp;nbsp;drm_impl_len,
char *error_diagnosis,
size_t&amp;nbsp;error_diag_len
</code></pre>
<p> <code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The drmaa_strerror() function returns a message text associated with the DRMAA error number, <i>drmaa_errno</i>. For invalid DRMAA error codes `NULL&#8217; is returned.</p>
<h3>drmaa_get_contact()</h3>
<p> The drmaa_get_contact() returns an opaque string containing contact information related to the current DRMAA session to be used with the function. The opaque string contains the information required by drmaa_init() to reconnect to the current session instead of creating a new session. function. </p>
<p> The drmaa_get_contact() function returns the same value before and after is called. </p>
<h3>drmaa_version()</h3>
<p> The drmaa_version() function returns into the integers pointed to by <i>major</i> and <i>minor</i>, the major and minor version numbers of the DRMAA library. For a DRMAA 1.0 compliant implementation `1&#8242; and `0&#8242; will be returned in <i>major</i> and <i>minor</i>, respectively. </p>
<h3>drmaa_get_DRM_system()</h3>
<p> The drmaa_get_DRM_system() function returns into <i>drm_system</i> up to <i>drm_system_len</i> characters of a string containing xxQS_NAMExx product and version information. </p>
<p> The drmaa_get_DRM_system() function returns the same value before and after is called. </p>
<h3>drmaa_get_DRMAA_implementation()</h3>
<p> The drmaa_get_DRMAA_implementation() function returns into <i>drm_system</i> up to <i>drm_system_len</i> characters of a string containing the xxQS_NAMExx DRMAA implementation version information. In the current implementation, the drmaa_get_DRMAA_implementation() function returns the same result as the drmaa_get_DRM_system() function. </p>
<p> The drmaa_get_DRMAA_implementation() function returns the same value before and after is called. </p>
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
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</dl>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, drmaa_get_contact(), drmaa_version(), and drmaa_get_DRM_system() return DRMAA_ERRNO_SUCCESS. Other values indicate an error. Up to <i>error_diag_len</i> characters of error related diagnosis information is then provided in the buffer <i>error_diagnosis</i>. </p>
<h2>ERRORS</h2>
<p> The drmaa_get_contact(), drmaa_version(), drmaa_get_DRM_system(), and drmaa_get_DRMAA_implementation() can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_INTERNAL_ERROR</code></p>
<dd> Unexpected or internal DRMAA error, like system call failure, etc.</p>
<dt><code>DRMAA_ERRNO_DRM_COMMUNICATION_FAILURE</code></p>
<dd> Could not contact DRM system for this request.</p>
<dt><code>DRMAA_ERRNO_AUTH_FAILURE</code></p>
<dd> The specified request is not processed successfully due to authorization failure.</p>
<dt><code>DRMAA_ERRNO_INVALID_ARGUMENT</code></p>
<dd> The input value for an argument is invalid.</p>
<dt><code>DRMAA_ERRNO_NO_MEMORY</code></p>
<dd> Failed allocating memory.</dl>
<p> The drmaa_get_contact() and drmaa_get_DRM_system() can fail with:</p>
<dl>
<dt><code>DRMAA_ERRNO_NO_ACTIVE_SESSION</code></p>
<dd> Failed because there is no active session.</dl>
<h2>SEE ALSO</h2>
<h2>Index</h2>
