---
title: "globus_gram_client_callback_disallow(3)"
name: "globus_gram_client_callback_disallow"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_client_callback_disallow/"
description: "Job state callbacks –"
---

<h2 class="name">NAME</h2>
<p> Job state callbacks &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_gram_client_job_info_s</code><br />
 <i>Extensible job information structure. </i></p>
<h3>Typedefs</h3>
<p> typedef void(* <code>globus_gram_client_callback_func_t</code> )(void *user_callback_arg, char *job_contact, int state, int errorcode)<br />
 <i>Signature for GRAM state notification callback functions. </i><br />
 typedef struct<br />
 <code>globus_gram_client_job_info_s</code> <code>globus_gram_client_job_info_t</code>&quot;<br />
 <i>Extensible job information structure. </i><br />
 typedef void(* <code>globus_gram_client_info_callback_func_t</code> )(void *user_callback_arg, const char *job_contact, <code>globus_gram_client_job_info_t</code> *job_info)<br />
 <i>Signature for GRAM state notification callback functions with extension support. </i><br />
 typedef void(* <code>globus_gram_client_nonblocking_func_t</code> )(void *user_callback_arg, globus_gram_protocol_error_t operation_failure_code, const char *job_contact, globus_gram_protocol_job_state_t job_state, globus_gram_protocol_error_t job_failure_code)<br />
 <i>Signature for callbacks signalling completion of non-blocking GRAM requests. </i></p>
<h3>Functions</h3>
<p> int <code>globus_gram_client_callback_allow</code> (<code>globus_gram_client_callback_func_t</code> callback_func, void *user_callback_arg, char **callback_contact)<br />
 <i>Begin listening for job state change callbacks. </i><br />
 int <code>globus_gram_client_info_callback_allow</code> (<code>globus_gram_client_info_callback_func_t</code> callback_func, void *user_callback_arg, char **callback_contact)<br />
 <i>Begin listening for job state change callbacks. </i><br />
 int <code>globus_gram_client_callback_disallow</code> (char *callback_contact)<br />
 <i>Stop listening for job state change callbacks. </i></p>
<h2>Detailed Description</h2>
<h2>Typedef Documentation</h2>
<h3>typedef void(* globus_gram_client_callback_func_t)(void *user_callback_arg, char *job_contact, int state, int errorcode)</h3>
<p> Signature for GRAM state notification callback functions. The globus_gram_client_callback_func_t type describes the function signature for job state callbacks. A pointer to a function of this type is passed to the <code>globus_gram_client_callback_allow()</code> function to create a callback contact. The contact string can be passed to <code>globus_gram_client_job_request()</code> or <code>globus_gram_client_job_callback_register()</code> to let the job management service know to where to send information on GRAM job state changes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_callback_arg</i> A pointer to application-specific data.<br />
 <i>job_contact</i> A string containing the job contact. This string indicates which job this callback is referring to. It should in most cases match the return value <i>job_contact</i> from a call to <code>globus_gram_client_job_request()</code> or in the <i>job_contact</i> parameter to the globus_gram_client_nonblocking_func_t used with <code>globus_gram_client_register_job_request()</code>. However, in some cases, the port number in the job contact URL may change if the job manager is restarted.<br />
 <i>state</i> The new state (one of the #globus_gram_protocol_job_state_t values) of the job.<br />
 <i>errorcode</i> The error code if the <i>state</i> parameter is equal to GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED.</dl>
<h3>typedef void(* globus_gram_client_info_callback_func_t)(void *user_callback_arg, const char *job_contact, <code>globus_gram_client_job_info_t</code> *job_info)</h3>
<p> Signature for GRAM state notification callback functions with extension support. The <code>globus_gram_client_info_callback_func_t</code> type describes the function signature for job state callbacks that carry any GRAM protocol extensions beyond the set used in GRAM2. A pointer to a function of this type is passed to the <code>globus_gram_client_info_callback_allow()</code> function to create a callback contact that can handle extensions. The contact string can be passed to <code>globus_gram_client_job_request()</code> or <code>globus_gram_client_job_callback_register()</code> to let the job management service know to where to send information on GRAM job state changes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_callback_arg</i> Application-specific callback information.<br />
 <i>job_contact</i> Job this information is related to<br />
 <i>job_info</i> Job state and extensions</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_info_callback_allow()</code></dl>
<h3>typedef struct <code>globus_gram_client_job_info_s</code></h3>
<p>&nbsp;<wbr><code>globus_gram_client_job_info_t</code>&quot; </p>
<p> Extensible job information structure. The <code>globus_gram_client_job_info_t</code> data type is used to pass protocol extensions along with the standard job status information included in the GRAM2 protocol. This structure contains the information returned in job state callbacks plus a hash table of extension entries that contain #globus_gram_protocol_extension_t name-value pairs.</p>
<h3>typedef void(* globus_gram_client_nonblocking_func_t)(void *user_callback_arg, globus_gram_protocol_error_t operation_failure_code, const char *job_contact, globus_gram_protocol_job_state_t job_state, globus_gram_protocol_error_t job_failure_code)</h3>
<p> Signature for callbacks signalling completion of non-blocking GRAM requests. The <code>globus_gram_client_info_callback_func_t</code> type describes the function signature for callbacks which indicate that a GRAM operation has completed. A pointer to a function of this type is passed to the following functions:</p>
<dl>
<dt>&bull;</p>
<dd> <code>globus_gram_client_register_job_request()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gram_client_register_job_cancel()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gram_client_register_job_status()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gram_client_register_job_refresh_credentials()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gram_client_register_job_signal()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gram_client_register_job_callback_registration()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gram_client_register_job_callback_unregistration()</code></p>
<dt>&bull;</p>
<dd> <code>globus_gram_client_register_ping()</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>user_callback_arg</i> Application-specific callback information.<br />
 <i>operation_failure_code</i> The result of the nonblocking operation , indicating whether the operation was processed by the job manager successfully or not.<br />
 <i>job_contact</i> A string containing the job contact associated with this non-blocking operation.<br />
 <i>job_state</i> The state (one of the #globus_gram_protocol_job_state_t values) of the job related to this non-blocking operation.<br />
 <i>job_failure_code</i> The error code of the job request if the job_state parameter is GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED. Otherwise, its value is undefined.</dl>
<h2>Function Documentation</h2>
<h3>int globus_gram_client_callback_allow (<code>globus_gram_client_callback_func_t</code>callback_func, void *user_callback_arg, char **callback_contact)</h3>
<p> Begin listening for job state change callbacks. The <code>globus_gram_client_callback_allow()</code> function initializes a GRAM protocol service in the current process which will process job state updates from GRAM Job Managers. The URL to contact this service is returned and may be used with the <code>globus_gram_client_job_request()</code> or globus_gram_client_callback_register() family of functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_func</i> A pointer to a function to call when a new job state update is received.<br />
 <i>user_callback_arg</i> A pointer to application-specific data which is passed to the function pointed to by <i>callback_func</i> as its <i>user_callback_arg</i> parameter.<br />
 <i>callback_contact</i> An output parameter that points to a string that will be allocated and set to the URL that the GRAM callback listener is waiting on.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_callback_allow()</code> returns <i>GLOBUS_SUCCESS</i> opens a TCP port to accept job state updates and modifies the value pointed to by the <i>callback_contact</i> parameter as described above. If an error occurs, <code>globus_gram_client_callback_allow()</code> returns an integer error code.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_callback_disallow (char *callback_contact)</h3>
<p> Stop listening for job state change callbacks. The <code>globus_gram_client_callback_disallow()</code> function stops the GRAM protocol handler associated with a callback contact from receiving further messages. After this function returns, no further callbacks for this contact will be called. Furthermore, the network port associated with the protocol handler will be released. </p>
<p> This function can only be used to disable a callback contact created in the current process. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_contact</i> A callback contact string that refers to a protocol handler in the current process.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_callback_disallow()</code> returns <i>GLOBUS_SUCCESS</i>, closes the network port associated with the <i>callback_contact</i> parameter and stops further callbacks from occurring. If an error occurs, <code>globus_gram_client_callback_disallow()</code> returns an integer error code.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_CALLBACK_NOT_FOUND</i> Callback not found</dl>
<h3>int globus_gram_client_info_callback_allow (<code>globus_gram_client_info_callback_func_t</code>callback_func, void *user_callback_arg, char **callback_contact)</h3>
<p> Begin listening for job state change callbacks. The <code>globus_gram_client_info_callback_allow()</code> function initializes a GRAM protocol service in the current process which will process job state updates from GRAM Job Managers. The URL to contact this service is returned and may be used with the <code>globus_gram_client_job_request_with_info()</code> or <code>globus_gram_client_register_job_status_with_info()</code> family of functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>callback_func</i> A pointer to a function to call when a new job state update is received. The function signature of this parameter supports GRAM protocol extensions.<br />
 <i>user_callback_arg</i> A pointer to application-specific data which is passed to the function pointed to by <i>callback_func</i> as its <i>user_callback_arg</i> parameter.<br />
 <i>callback_contact</i> An output parameter that points to a string that will be allocated and set to the URL that the GRAM callback listener is waiting on.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_callback_allow()</code> returns <i>GLOBUS_SUCCESS</i> opens a TCP port to accept job state updates and modifies the value pointed to by the <i>callback_contact</i> parameter as described above. If an error occurs, <code>globus_gram_client_callback_allow()</code> returns an integer error code.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Function Documentation</a></p>
<dd>
<dt><a href="#lbAP">Author</a></p>
<dd></dl>
