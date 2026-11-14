---
title: "globus_gram_client_job_info_destroy(3)"
name: "globus_gram_client_job_info_destroy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_client_job_info_destroy/"
description: "GRAM Client API –"
---

<h2 class="name">NAME</h2>
<p> GRAM Client API &#8211; </p>
<h3>Modules</h3>
<p> <code>Job state callbacks</code> </p>
<p> <code>GRAM Job Functions</code> </p>
<p> <code>GRAM Client Attribute Functions</code> </p>
<h3>Functions</h3>
<p> void <code>globus_gram_client_debug</code> (void)<br />
 <i>Enable GRAM debugging. </i><br />
 int <code>globus_gram_client_version</code> (void)<br />
 <i>Return GRAM protocol version. </i><br />
 int <code>globus_gram_client_set_credentials</code> (gss_cred_id_t new_credentials)<br />
 <i>Set the default GRAM credential. </i><br />
 const char * <code>globus_gram_client_error_string</code> (int error_code)<br />
 <i>Get a description of a a GRAM error code. </i><br />
 int <code>globus_gram_client_job_contact_free</code> (char *job_contact)<br />
 <i>Free a job contact string. </i><br />
 void <code>globus_gram_client_job_info_destroy</code> (<code>globus_gram_client_job_info_t</code> *info)<br />
 <i>Free memory associated with a globus_gram_client_job_info_t structure. </i></p>
<h2>Detailed Description</h2>
<p> The resource management API provides function for requesting that a job be started or terminated, as well as for requesting information about the status of a job.</p>
<h2>Function Documentation</h2>
<h3>void globus_gram_client_debug (void)</h3>
<p> Enable GRAM debugging. The <code>globus_gram_client_debug()</code> function enables the displaying of internal GRAM debug messages to standard output. Most of the information printed by this debugging system is related to errors that occur during GRAM Client API functions. The messages printed to standard output are not structured in any way. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h3>const char* globus_gram_client_error_string (interror_code)</h3>
<p> Get a description of a a GRAM error code. The <code>globus_gram_client_error_string()</code> function takes a GRAM error code value and returns the associated error code string. The string is statically allocated by the Globus GRAM Client library and should not be modified or freed. The string is intended to complete a sentence of the form &#8216;[operation] failed because &#8230;&#8217; </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>error_code</i> The error code to translate into a string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_gram_client_error_string()</code> function returns a static string containing an explanation of the error.</dl>
<h3>int globus_gram_client_job_contact_free (char *job_contact)</h3>
<p> Free a job contact string. Releases the resources storing a job contact string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> A job contact string returned in a successful call to <code>globus_gram_client_job_request()</code></dl>
<p> The <code>globus_gram_client_job_contact_free()</code> function frees a job contact string that was allocated by a call to one of the functions in the <code>globus_gram_client_job_request()</code> family. The free() function can be used in place of this function. After this function returns, the string pointed to by the <i>job_contact</i> parameter has an undefined value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> Pointer to a job contact string returned by a GRAM client API function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function always returns GLOBUS_SUCCESS.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success</dl>
<h3>void globus_gram_client_job_info_destroy (<code>globus_gram_client_job_info_t</code> *info)</h3>
<p> Free memory associated with a globus_gram_client_job_info_t structure. The <code>globus_gram_client_job_info_destroy()</code> function frees data pointed to by the <i>extensions</i> and <i>job_contact</i> fields of the <i>globus_gram_client_job_info_t</i> structure pointed to by the <i>info</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>info</i> A structure containing data to free.</dl>
<h3>int globus_gram_client_set_credentials (gss_cred_id_tnew_credentials)</h3>
<p> Set the default GRAM credential. The <code>globus_gram_client_set_credentials()</code> function causes subsequent GRAM operations to use the GSSAPI credential <i>new_credentials</i>. These operations include job requests, job signals, callback registration, and job state callbacks. After this function returns, the caller must not use the credential, as it may be freed by GRAM when it is no longer needed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>new_credentials</i> New GSSAPI credential to use.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_set_credentials()</code> returns GLOBUS_SUCCESS. There are no error values returned by this fucntion.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success</dl>
<h3>int globus_gram_client_version (void)</h3>
<p> Return GRAM protocol version. The <code>globus_gram_client_version()</code> function returns the version of the GRAM protocol understood by this implementation. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The integer protocol revision.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAM">Author</a></p>
<dd></dl>
