---
title: "globus_gram_client_register_job_cancel(3)"
name: "globus_gram_client_register_job_cancel"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_client_register_job_cancel/"
description: "GRAM Job Functions –"
---

<h2 class="name">NAME</h2>
<p> GRAM Job Functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_gram_client_register_ping</code> (const char *resource_manager_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Send a ping request to a GRAM service. </i><br />
 int <code>globus_gram_client_ping</code> (const char *resource_manager_contact)<br />
 <i>Send a ping request to a GRAM service. </i><br />
 int <code>globus_gram_client_get_jobmanager_version</code> (const char *resource_manager_contact, globus_hashtable_t *extensions)<br />
 <i>Get version information from a job manager. </i><br />
 int <code>globus_gram_client_register_get_jobmanager_version</code> (const char *resource_manager_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_info_callback_func_t</code> info_callback, void *callback_arg)<br />
 <i>Get version information from a job manager without blocking. </i><br />
 int <code>globus_gram_client_register_job_request</code> (const char *resource_manager_contact, const char *description, int job_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Send a job request to a GRAM service. </i><br />
 int <code>globus_gram_client_job_request</code> (const char *resource_manager_contact, const char *description, int job_state_mask, const char *callback_contact, char **job_contact)<br />
 <i>Send a job request to a GRAM service. </i><br />
 int <code>globus_gram_client_register_job_request_with_info</code> (const char *resource_manager_contact, const char *description, int job_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_info_callback_func_t</code> callback, void *callback_arg)<br />
 <i>Send a job request to a GRAM service with extensions-aware callback. </i><br />
 int <code>globus_gram_client_job_request_with_info</code> (const char *resource_manager_contact, const char *description, int job_state_mask, const char *callback_contact, char **job_contact, <code>globus_gram_client_job_info_t</code> *info)<br />
 <i>Send a job request to a GRAM service and parse extensions in the response. </i><br />
 int <code>globus_gram_client_job_cancel</code> (const char *job_contact)<br />
 <i>Cancel a GRAM job. </i><br />
 int <code>globus_gram_client_register_job_cancel</code> (const char *job_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Cancel a GRAM job. </i><br />
 int <code>globus_gram_client_job_signal</code> (const char *job_contact, globus_gram_protocol_job_signal_t signal, const char *signal_arg, int *job_status, int *failure_code)<br />
 <i>Send a signal a GRAM job. </i><br />
 int <code>globus_gram_client_register_job_signal</code> (const char *job_contact, globus_gram_protocol_job_signal_t signal, const char *signal_arg, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Send a signal a GRAM job. </i><br />
 int <code>globus_gram_client_job_status</code> (const char *job_contact, int *job_status, int *failure_code)<br />
 <i>Send a status query to a GRAM job. </i><br />
 int <code>globus_gram_client_register_job_status</code> (const char *job_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Send a status query to a GRAM job. </i><br />
 int <code>globus_gram_client_register_job_status_with_info</code> (const char *job_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_info_callback_func_t</code> info_callback, void *callback_arg)<br />
 <i>Send a status query to a GRAM job. </i><br />
 int <code>globus_gram_client_job_status_with_info</code> (const char *job_contact, <code>globus_gram_client_job_info_t</code> *info)<br />
 <i>Send a status query to a GRAM job. </i><br />
 int <code>globus_gram_client_job_callback_register</code> (const char *job_contact, int job_state_mask, const char *callback_contact, int *job_status, int *failure_code)<br />
 <i>Register a new callback contact to be notified for job state changes. </i><br />
 int <code>globus_gram_client_job_callback_unregister</code> (const char *job_contact, const char *callback_contact, int *job_status, int *failure_code)<br />
 <i>Unregister a callback contact to stop job state change notifications. </i><br />
 int <code>globus_gram_client_job_refresh_credentials</code> (char *job_contact, gss_cred_id_t creds)<br />
 <i>Delegate a new credential to a job. </i><br />
 int <code>globus_gram_client_register_job_refresh_credentials</code> (char *job_contact, gss_cred_id_t creds, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Delegate a new credential to a job. </i><br />
 int <code>globus_gram_client_register_job_callback_registration</code> (const char *job_contact, int job_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Register a new callback contact to be notified for job state changes. </i><br />
 int <code>globus_gram_client_register_job_callback_unregistration</code> (const char *job_contact, const char *callback_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Unregister a callback contact to stop job state change notifications. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int globus_gram_client_get_jobmanager_version (const char *resource_manager_contact, globus_hashtable_t *extensions)</h3>
<p> Get version information from a job manager. The <code>globus_gram_client_get_jobmanager_version()</code> function sends a message to a GRAM service which returns information about the job manager version in the value pointed to by the <i>extensions</i> parameter. Note that job managers prior to GT5 do not support the version request and so will return a GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED error. This function blocks while processing this request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resource_manager_contact</i> A NULL-terminated character string containing a <code>GRAM contact</code>.<br />
 <i>extensions</i> A pointer to a hash table which will be initialized to contain the version information returned by the service. The extensions defined by GRAM5 are <i>toolkit-version</i> and <i>version</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_get_jobmanager_version()</code> function returns GLOBUS_SUCCESS and modifies the <i>extensions</i> parameter as described above. If an error occurs, the integer error code will be returned and the value pointed to by the <i>extensions</i> parameter is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_BAD_GATEKEEPER_CONTACT</i> Bad gatekeeper contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> NULL parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_job_callback_register (const char *job_contact, intjob_state_mask, const char *callback_contact, int *job_status, int *failure_code)</h3>
<p> Register a new callback contact to be notified for job state changes. The <code>globus_gram_client_job_callback_register()</code> function contacts a GRAM service managing a job and instructs it to send subsequent job state callbacks to the client listening for callbacks at the contact url named by the <i>callback_contact</i> parameter. This function blocks until the registration operation either completes or exits. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to contact. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>job_state_mask</i> A bitwise-or of the GLOBUS_GRAM_PROTOCOL_JOB_STATE_* states that the job manager will send job state notification messages for to the contact named by <i>callback_contact</i>.<br />
 <i>callback_contact</i> A URL string containing a GRAM client callback. This string is normally be generated by a process calling <code>globus_gram_client_callback_allow()</code>.<br />
 <i>job_status</i> An output parameter pointing to an integer to set to the status of the job after the registration message has been processed.<br />
 <i>failure_code</i> An output parameter that points to an integer to be set to the reason why the job failed if its current status is <i>GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED</i>. If the job has not failed, the value will be set to 0.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_job_callback_register()</code> function returns <i>GLOBUS_SUCCESS</i>, sends a registration request the job named by <i>job_contact</i> and parses the service response, modifying the values pointed to by the <i>job_status</i> and <i>failure_code</i> parameters as described above. If an error occurs, <code>globus_gram_client_job_callback_register()</code> returns an integer error code indicating why it can&#8217;t register the callback contact. The return code may be any value defined by the <i>globus_gram_protocol_error_t</i> enumeration in addition to those listed below.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_job_callback_unregister (const char *job_contact, const char *callback_contact, int *job_status, int *failure_code)</h3>
<p> Unregister a callback contact to stop job state change notifications. The <code>globus_gram_client_job_callback_unregister()</code> function contacts a GRAM service managing a job and instructs it to stop sending job state callbacks to the client listening for callbacks at the contact url named by the <i>callback_contact</i> parameter. This function blocks until the unregistration operation either completes or exits. It is possible that callbacks related to the job arrive at the contact after this function returns depending on network delays. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to contact. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>callback_contact</i> A URL string containing a GRAM client callback. This string is normally be generated by a process calling <code>globus_gram_client_callback_allow()</code>.<br />
 <i>job_status</i> An output parameter pointing to an integer to set to the status of the job after the registration message has been processed.<br />
 <i>failure_code</i> An output parameter that points to an integer to be set to the reason why the job failed if its current status is <i>GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED</i>. If the job has not failed, the value will be set to 0.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_job_callback_unregister()</code> function returns <i>GLOBUS_SUCCESS</i>, sends an unregister request the job named by <i>job_contact</i> and parses the service response, modifying the values pointed to by the <i>job_status</i> and <i>failure_code</i> parameters as described above. If an error occurs, <code>globus_gram_client_job_callback_unregister()</code> returns an integer error code indicating why it can&#8217;t unregister the callback contact. The return code may be any value defined by the <i>globus_gram_protocol_error_t</i> enumeration in addition to those listed below.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_job_cancel (const char *job_contact)</h3>
<p> Cancel a GRAM job. The <code>globus_gram_client_job_cancel()</code> function cancels a GRAM job. Depending on the job&#8217;s current state, this cancellation may be immediate or require a delay for interacting with the LRM servicing the job. Notification when the job has been successfully canceled will be sent to all client contacts registered for notifications after the cancellation has been completely processed. Unlike, <code>globus_gram_client_register_job_cancel()</code>, <code>globus_gram_client_job_cancel()</code> blocks until the job cancel request has been processed by the service. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> A NULL-terminated character string containing a GRAM job contact that this function will contact to cancel the job.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon succes, <code>globus_gram_client_job_cancel()</code> returns <i>GLOBUS_SUCCESS</i> if the cancellation was successful posted to the service. If an error occurs, <code>globus_gram_client_job_cancel()</code> returns one of the #globus_gram_protocol_error_t values values indicating why the client could not cancel the job.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_register_job_cancel()</code></dl>
<h3>int globus_gram_client_job_refresh_credentials (char *job_contact, gss_cred_id_tcreds)</h3>
<p> Delegate a new credential to a job. The <code>globus_gram_client_job_refresh_credentials()</code> function sends a &#8216;renew&#8217; signal to a GRAM service and then initiates the delegation of a new credential to the job manager and job. This prevents errors that can occur when a credential expires. This function blocks until the delegation has completed or failed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to contact. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>creds</i> A GSSAPI credential handle which will be used to authenticate with the job manager and sign the delegated credential. This parameter&#8217;s value may be set to <i>GSS_C_NO_CREDENTIAL</i> to indicate the desire to use this process&#8217;s default credential.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_job_refresh_credentials()</code> function returns <i>GLOBUS_SUCCESS</i>, sends an proxy renew request the job named by <i>job_contact</i>, parses the service response and performs a GSSAPI delegation to send a new credential to the job service. If an error occurs, <code>globus_gram_client_job_refresh_credentials()</code> returns an integer error code indicating why it can&#8217;t refresh the job service&#8217;s credential. The return code may be any value defined by the <i>globus_gram_protocol_error_t</i> enumeration in addition to those listed below.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_job_request (const char *resource_manager_contact, const char *description, intjob_state_mask, const char *callback_contact, char **job_contact)</h3>
<p> Send a job request to a GRAM service. The <code>globus_gram_client_job_request()</code> function sends a GRAM protocol message to a service to request that it start a job on behalf of the client. Unlike, <code>globus_gram_client_register_job_request()</code>, <code>globus_gram_client_job_request()</code> blocks until the job request has been processed by the service. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resource_manager_contact</i> A NULL-terminated character string containing a <code>GRAM contact</code> that this function will contact.<br />
 <i>description</i> A pointer to a string containing the job request information formatted in RSL syntax.<br />
 <i>job_state_mask</i> A bitwise-or of the GLOBUS_GRAM_PROTOCOL_JOB_STATE_* states that the job manager will send job state notification messages for to the contact named by <i>callback_contact</i>.<br />
 <i>callback_contact</i> A GRAM listener contact that the job manager will send job state notification messages to.<br />
 <i>job_contact</i> An output parameter pointing to a string that will be set to the job contact for this job. This value will only be set if the job request is successful or the two-phase commit protocol is being used and the return code is <i>GLOBUS_GRAM_PROTOCOL_ERROR_WAITING_FOR_COMMIT</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_job_request()</code> returns GLOBUS_SUCCESS and modifies the value pointed to by <i>job_contact</i> as described above. If an error occurs, this function returns an integer error code and the value pointed to by <i>job_contact</i>. In addition to the error codes described below, any #globus_gram_protocol_error_t value may be returned as a cause for the job to fail.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_job_request_with_info (const char *resource_manager_contact, const char *description, intjob_state_mask, const char *callback_contact, char **job_contact, <code>globus_gram_client_job_info_t</code> *info)</h3>
<p> Send a job request to a GRAM service and parse extensions in the response. The <code>globus_gram_client_job_request_with_info()</code> function sends a GRAM protocol message to a service to request that it start a job on behalf of the client. Unlike, <code>globus_gram_client_register_job_request_with_info()</code>, <code>globus_gram_client_job_request_with_info()</code> blocks until the job request has been processed by the service. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resource_manager_contact</i> A NULL-terminated character string containing a <code>GRAM contact</code> that this function will contact.<br />
 <i>description</i> A pointer to a string containing the job request information formatted in RSL syntax.<br />
 <i>job_state_mask</i> A bitwise-or of the GLOBUS_GRAM_PROTOCOL_JOB_STATE_* states that the job manager will send job state notification messages for to the contact named by <i>callback_contact</i>.<br />
 <i>callback_contact</i> A GRAM listener contact that the job manager will send job state notification messages to.<br />
 <i>job_contact</i> An output parameter pointing to a string that will be set to the job contact for this job. This value will only be set if the job request is successful or the two-phase commit protocol is being used and the return code is <i>GLOBUS_GRAM_PROTOCOL_ERROR_WAITING_FOR_COMMIT</i>.<br />
 <i>info</i> An output parameter pointing to a structure to hold the extensions in the GRAM response. The caller is responsible for destroying this by calling the <code>globus_gram_client_job_info_destroy()</code> function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_job_request_with_info()</code> returns GLOBUS_SUCCESS and modifies the values pointed to by <i>job_contact</i> and <i>info</i> as described above. If an error occurs, this function returns an integer error code and the value pointed to by <i>job_contact</i>. In addition to the error codes described below, any #globus_gram_protocol_error_t value may be returned as a cause for the job to fail.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_job_signal (const char *job_contact, globus_gram_protocol_job_signal_tsignal, const char *signal_arg, int *job_status, int *failure_code)</h3>
<p> Send a signal a GRAM job. The <code>globus_gram_client_job_signal()</code> function sends a signal message to a job managed by the GRAM service. Signals consist of a signal number and an optional string argument. The meanings of the signals supported by the GRAM job manager are defined in the GRAM Protocol documentation. Unlike <code>globus_gram_client_register_job_signal()</code>, this function blocks until the signal has been delivered and acknowledged by the GRAM service. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job manager to contact. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>signal</i> The signal code to send to the job manager.<br />
 <i>signal_arg</i> Parameters for the signal, as described in the documentation for the #globus_gram_protocol_job_signal_t enumeration.<br />
 <i>job_status</i> An output parameter pointing to an integer to set to the status of the job after the signal has been processed.<br />
 <i>failure_code</i> An output parameter pointing to an integer to set to the reason why the job has failed if the value pointed to by <i>job_status</i> is set to <i>GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED</i> by this function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_job_signal()</code> returns GLOBUS_SUCCESS after sending the signal and receiving a response and modifies the <i>job_status</i> and <i>failure_code</i> parameters as described above. If an error occurs, this function returns an integer error code indicating why the client could not signal the job.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_register_job_signal()</code></dl>
<h3>int globus_gram_client_job_status (const char *job_contact, int *job_status, int *failure_code)</h3>
<p> Send a status query to a GRAM job. The globus_gram_client_status() function queries the current status of the job associated with the job contact, returning its current status, as well as the job&#8217;s failure reason if it has failed in this function&#8217;s return parameters. This function blocks until the service has responded to the status query. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to query. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>job_status</i> An output parameter that points to an integer to be set to the current status of the job named by the <i>job_contact</i> parameter.<br />
 <i>failure_code</i> An output parameter that points to an integer to be set to the reason why the job failed if its current status is <i>GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED</i>. If the job has not failed, the value will be set to 0.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_job_status()</code> function returns <i>GLOBUS_SUCCESS</i>, sends a job state query to the job named by <i>job_contact</i> and parses the service response, modifying the values pointed to by <i>job_status</i> and <i>failure_code</i> as described above. If an error occurs, <code>globus_gram_client_job_status()</code> returns an integer error code.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_job_status_with_info (const char *job_contact, <code>globus_gram_client_job_info_t</code> *info)</h3>
<p> Send a status query to a GRAM job. The globus_gram_client_status_with_info() function queries the current status of the job associated with the job contact, returning its current status, as well as the job&#8217;s failure reason if it has failed in this function&#8217;s return parameters. This function blocks until the service has responded to the status query. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to query. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>info</i> An output parameter that points to a globus_gram_client_job_info_t structure which will be populated with the state information associated with the job named by the <i>job_contact</i> parameter. The caller is responsible for calling <code>globus_gram_client_job_info_destroy()</code> to free the state pointed to by this parameter if this function returns <i>GLOBUS_SUCCESS</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_job_status_with_info()</code> function returns <i>GLOBUS_SUCCESS</i>, sends a job state query to the job named by <i>job_contact</i> and parses the service response, modifying the structure pointed to by <i>info</i> as described above. If an error occurs, <code>globus_gram_client_job_status_with_info()</code> returns an integer error code.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_ping (const char *resource_manager_contact)</h3>
<p> Send a ping request to a GRAM service. The <code>globus_gram_client_ping()</code> function sends a specially-formatted GRAM protocol message which checks to see if a Gatekeeper is running on a given PORT, and whether that Gatekeeper is configured to support the desired job manager service. This is used for diagnostic purposes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resource_manager_contact</i> A NULL-terminated character string containing a <code>GRAM contact</code> that this function will contact.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_ping()</code> contacts the gatekeeper service and returns <i>GLOBUS_SUCCESS</i>. If an error occurs, this function returns an integer error code.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_register_get_jobmanager_version (const char *resource_manager_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_info_callback_func_t</code>info_callback, void *callback_arg)</h3>
<p> Get version information from a job manager without blocking. The <code>globus_gram_client_register_get_jobmanager_version()</code> function sends a message to a GRAM service which returns information about the job manager version to the function pointed to by the <i>info_callback</i> function. Note that job managers prior to GT5 do not support the version request and so will return a GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED error. This function blocks while processing this request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resource_manager_contact</i> A NULL-terminated character string containing a <code>GRAM contact</code>.<br />
 <i>attr</i> A set of client attributes to use to contact the gatekeeper. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>info_callback</i> A pointer to a function to call when the version request has completed or failed.<br />
 <i>callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>info_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_register_get_jobmanager_version()</code> function returns GLOBUS_SUCCESS and begins processing the version request to contact <i>resource_manager_contact</i>; when complete, the <i>info_callback</i> function will be called. If an error occurs, the integer error code will be returned and the value pointed to by the <i>extensions</i> parameter is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_BAD_GATEKEEPER_CONTACT</i> Bad gatekeeper contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> NULL parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_register_job_callback_registration (const char *job_contact, intjob_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_nonblocking_func_t</code>register_callback, void *register_callback_arg)</h3>
<p> Register a new callback contact to be notified for job state changes. The <code>globus_gram_client_register_job_callback_registration()</code> function initiates the protocol to contact a GRAM service and request that it send subsequent job state callbacks to the client listening for callbacks at the contact url named by the <i>callback_contact</i> parameter. This function returns as soon as it has validated its parameters and begun sending the GRAM message. When the registration is complete, the function pointed to by <i>register_callback</i> is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to contact. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>job_state_mask</i> A bitwise-or of the GLOBUS_GRAM_PROTOCOL_JOB_STATE_* states that the job manager will send job state notification messages for to the contact named by <i>callback_contact</i>.<br />
 <i>callback_contact</i> A URL string containing a GRAM client callback. This string is normally be generated by a process calling <code>globus_gram_client_callback_allow()</code>.<br />
 <i>attr</i> A set of client attributes to use to contact the job. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>register_callback</i> A pointer to a function to call when the registration request has completed or failed.<br />
 <i>register_callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>register_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_register_job_callback_registration()</code> function returns <i>GLOBUS_SUCCESS</i>, begins to send a registration request to the job named by <i>job_contact</i>, and schedules the <i>register_callback</i> to be called once the registration completes or fails. If an error occurs, this function returns an integer error code indicating why it can&#8217;t process the request.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_job_callback_register()</code></dl>
<h3>int globus_gram_client_register_job_callback_unregistration (const char *job_contact, const char *callback_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_nonblocking_func_t</code>register_callback, void *register_callback_arg)</h3>
<p> Unregister a callback contact to stop job state change notifications. The <code>globus_gram_client_register_job_callback_unregistration()</code> function initiates the protocol to contact a GRAM service and request that it stop sending job state callbacks to the client listening at the contact url named by the <i>callback_contact</i> parameter. This function returns as soon as it has validated its parameters and begun sending the GRAM message. When the unregistration is complete, the function pointed to by <i>register_callback</i> is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to contact. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>callback_contact</i> A URL string containing a GRAM client callback. This string is normally be generated by a process calling <code>globus_gram_client_callback_allow()</code>.<br />
 <i>attr</i> A set of client attributes to use to contact the job. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>register_callback</i> A pointer to a function to call when the registration request has completed or failed.<br />
 <i>register_callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>register_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_register_job_callback_unregistration()</code> function returns <i>GLOBUS_SUCCESS</i>, begins sending an unregister request to the job named by <i>job_contact</i> and schedules the function pointed to by the <i>register_callback</i> parameter to be called. If an error occurs, <code>globus_gram_client_register_job_callback_unregistration()</code> returns an integer error code indicating why it can&#8217;t process the unregister request.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_job_callback_unregister()</code></dl>
<h3>int globus_gram_client_register_job_cancel (const char *job_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_nonblocking_func_t</code>register_callback, void *register_callback_arg)</h3>
<p> Cancel a GRAM job. The <code>globus_gram_client_register_job_cancel()</code> function sends a message to a GRAM service to cancel a GRAM job. Depending on the job&#8217;s current state, this cancellation may be immediate or require a delay for interacting with the LRM servicing the job. In either case, this function returns as soon as it is able to start sending the message. Notification when the job has been successfully canceled will be sent to all client contacts registered for notifications after the cancellation has been completely processed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> A NULL-terminated character string containing a GRAM job contact that this function will contact to cancel the job.<br />
 <i>attr</i> A set of client attributes to use to contact the job. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>register_callback</i> A pointer to a function to call when the job_request request has completed or failed.<br />
 <i>register_callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>register_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon succes, <code>globus_gram_client_register_job_cancel()</code> returns <i>GLOBUS_SUCCESS</i> if the cancellation was successful posted to the service. If an error occurs, <code>globus_gram_client_register_job_cancel()</code> returns one an integer error code indicating why it could not cancel the job.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_job_cancel()</code></dl>
<h3>int globus_gram_client_register_job_refresh_credentials (char *job_contact, gss_cred_id_tcreds, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_nonblocking_func_t</code>register_callback, void *register_callback_arg)</h3>
<p> Delegate a new credential to a job. The <code>globus_gram_client_register_job_refresh_credentials()</code> function sends a &#8216;renew&#8217; signal to a GRAM service and then initiates the delegation of a new credential to the job manager and job. This prevents errors that can occur when a credential expires. This function returns as soon as it has determined that its parameters are valid and it has begun to send the message to the GRAM service. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to contact. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>creds</i> A GSSAPI credential handle which will be used to authenticate with the job manager and sign the delegated credential. This parameter&#8217;s value may be set to <i>GSS_C_NO_CREDENTIAL</i> to indicate the desire to use this process&#8217;s default credential.<br />
 <i>attr</i> A set of client attributes to use to contact the job. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>register_callback</i> A pointer to a function to call when the status request has completed or failed.<br />
 <i>register_callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>register_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_job_refresh_credentials()</code> function returns <i>GLOBUS_SUCCESS</i> and begins sending the &#8216;renew&#8217; request to the GRAM service. If an error occurs, <code>globus_gram_client_job_refresh_credentials()</code> returns an integer error code indicating why it can&#8217;t refresh the job service&#8217;s credential. The return code may be any value defined by the <i>globus_gram_protocol_error_t</i> enumeration in addition to those listed below.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_register_job_request (const char *resource_manager_contact, const char *description, intjob_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_nonblocking_func_t</code>register_callback, void *register_callback_arg)</h3>
<p> Send a job request to a GRAM service. The <code>globus_gram_client_register_job_request()</code> function sends a GRAM protocol message to a service to request that it start a job on behalf of the client. </p>
<p> If <code>globus_gram_client_register_job_request()</code> determines that this request could not be processed before contacting the gatekeeper (for example, a malformed <i>resource_manager_contact</i>), it will return an error, and the <i>regiser_callback</i> function will not be called. Otherwise, the success or failure an be determined by the <i>operation_failure_code</i> parameter to the function pointed to by the <i>register_callback</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resource_manager_contact</i> A NULL-terminated character string containing a <code>GRAM contact</code> that this function will contact.<br />
 <i>description</i> A pointer to a string containing the job request information formatted in RSL syntax.<br />
 <i>job_state_mask</i> A bitwise-or of the GLOBUS_GRAM_PROTOCOL_JOB_STATE_* states that the job manager will send job state notification messages for to the contact named by <i>callback_contact</i>.<br />
 <i>callback_contact</i> A GRAM listener contact that the job manager will send job state notification messages to.<br />
 <i>attr</i> A set of client attributes to use to contact the gatekeeper. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>register_callback</i> A pointer to a function to call when the job_request request has completed or failed.<br />
 <i>register_callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>register_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_register_job_request()</code> returns GLOBUS_SUCCESS and the <i>register_callback</i> function will be called once the job request operation completes. If an error occurs, this function returns an integer error code and the function pointed to by the <i>register_callback</i> parameter will not be called.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_register_job_request_with_info (const char *resource_manager_contact, const char *description, intjob_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_info_callback_func_t</code>callback, void *callback_arg)</h3>
<p> Send a job request to a GRAM service with extensions-aware callback. The <code>globus_gram_client_register_job_request_with_info()</code> function sends a GRAM protocol message to a service to request that it start a job on behalf of the client. </p>
<p> If <code>globus_gram_client_register_job_request_with_info()</code> determines that this request could not be processed before contacting the gatekeeper (for example, a malformed <i>resource_manager_contact</i>), it will return an error, and the <i>callback</i> function will not be called. Otherwise, the success or failure an be determined by the <i>operation_failure_code</i> parameter to the function pointed to by the <i>callback</i> parameter. The difference between this function and <i></i><code>globus_gram_client_register_job_request()</code> is the function signature of the callback function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resource_manager_contact</i> A NULL-terminated character string containing a <code>GRAM contact</code> that this function will contact.<br />
 <i>description</i> A pointer to a string containing the job request information formatted in RSL syntax.<br />
 <i>job_state_mask</i> A bitwise-or of the GLOBUS_GRAM_PROTOCOL_JOB_STATE_* states that the job manager will send job state notification messages for to the contact named by <i>callback_contact</i>.<br />
 <i>callback_contact</i> A GRAM listener contact that the job manager will send job state notification messages to.<br />
 <i>attr</i> A set of client attributes to use to contact the gatekeeper. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>callback</i> A pointer to a function to call when the job_request request has completed or failed.<br />
 <i>callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_register_job_request_with_info()</code> returns GLOBUS_SUCCESS and the <i>callback</i> function will be called once the job request operation completes. If an error occurs, this function returns an integer error code and the function pointed to by the <i>callback</i> parameter will not be called.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h3>int globus_gram_client_register_job_signal (const char *job_contact, globus_gram_protocol_job_signal_tsignal, const char *signal_arg, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_nonblocking_func_t</code>register_callback, void *register_callback_arg)</h3>
<p> Send a signal a GRAM job. The <code>globus_gram_client_register_job_signal()</code> function sends a signal message to a job managed by the GRAM service. Signals consist of a signal number and an optional string argument. The meanings of the signals supported by the GRAM job manager are defined in the GRAM Protocol documentation. This function returns as soon as it has determined that its parameters are valid and it has begun to send the message to the GRAM service. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job manager to contact. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>signal</i> The signal code to send to the job manager.<br />
 <i>signal_arg</i> Parameters for the signal, as described in the documentation for the #globus_gram_protocol_job_signal_t enumeration.<br />
 <i>attr</i> A set of client attributes to use to contact the job. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>register_callback</i> A pointer to a function to call when the signal request has completed or failed.<br />
 <i>register_callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>register_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, globus_gram_client_job_register_signal() returns GLOBUS_SUCCESS after beginnning to send the signal to the GRAM job and registers the <i>register_callback</i> function to be called once that has completed. If an error occurs, this function returns an integer error code indicating why the client could not signal the job.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_register_job_signal()</code></dl>
<h3>int globus_gram_client_register_job_status (const char *job_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_nonblocking_func_t</code>register_callback, void *register_callback_arg)</h3>
<p> Send a status query to a GRAM job. The <code>globus_gram_client_register_job_status()</code> function initiates a query of the current status of the job associated with the <i>job</i> contact parameter. The job&#8217;s status and failure code are passed to the function pointed to by the <i>register_callback</i> parameter. This function returns as soon as it has begun requesting the job status. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to query. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>attr</i> A set of client attributes to use to contact the job. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>register_callback</i> A pointer to a function to call when the status request has completed or failed.<br />
 <i>register_callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>register_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_register_job_status()</code> function returns <i>GLOBUS_SUCCESS</i> and begins to send a job state query to the job named by <i>job_contact</i> and registers the function pointed to by the <i>register_callback</i> parameter to be called once the status query terminates or fails. If an error occurs, <code>globus_gram_client_register_job_status()</code> returns an integer error code.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter</dl>
<h3>int globus_gram_client_register_job_status_with_info (const char *job_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_info_callback_func_t</code>info_callback, void *callback_arg)</h3>
<p> Send a status query to a GRAM job. The <code>globus_gram_client_register_job_status_with_info()</code> function initiates a query of the current status of the job associated with the <i>job</i> contact parameter. Job information is returned via the <i>job_info</i> parameter passed to the function pointed to by the <i>info_callback</i> parameter. This function returns as soon as it has begun requesting the job status. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string of the job to query. This is the same value returned from <code>globus_gram_client_job_request()</code>.<br />
 <i>attr</i> A set of client attributes to use to contact the job. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>info_callback</i> A pointer to a function to call when the status request has completed or failed.<br />
 <i>callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>info_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_gram_client_register_job_status_with_info()</code> function returns <i>GLOBUS_SUCCESS</i> and begins to send a job state query to the job named by <i>job_contact</i> and registers the function pointed to by the <i>info_callback</i> parameter to be called once the status query terminates or fails. If an error occurs, <code>globus_gram_client_register_job_status_with_info()</code> returns an integer error code.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter</dl>
<h3>int globus_gram_client_register_ping (const char *resource_manager_contact, <code>globus_gram_client_attr_t</code>attr, <code>globus_gram_client_nonblocking_func_t</code>register_callback, void *register_callback_arg)</h3>
<p> Send a ping request to a GRAM service. The <code>globus_gram_client_register_ping()</code> function sends a specially-formatted GRAM protocol message which checks to see if a Gatekeeper is running on a given PORT, and whether that Gatekeeper is configured to support the desired job manager service. This is used for diagnostic purposes. </p>
<p> If <code>globus_gram_client_register_ping()</code> determines that this request could not be processed before contacting the gatekeeper (for example, a malformed <i>resource_manager_contact</i>), it will return an error, and the <i>regiser_callback</i> function will not be called. Otherwise, the success or failure an be determined by the <i>operation_failure_code</i> parameter to the function pointed to by the <i>register_callback</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>resource_manager_contact</i> A NULL-terminated character string containing a <code>GRAM contact</code> that this function will contact.<br />
 <i>attr</i> A set of client attributes to use to contact the gatekeeper. If no custom attributes are needed, the caller should pass the value <i>GLOBUS_GRAM_CLIENT_NO_ATTR</i>.<br />
 <i>register_callback</i> A pointer to a function to call when the ping request has completed or failed.<br />
 <i>register_callback_arg</i> A pointer to application-specific data which will be passed to the function pointed to by <i>register_callback</i> as its <i>user_callback_arg</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_register_ping()</code> returns GLOBUS_SUCCESS and the <i>register_callback</i> function will be called once the ping operation completes. If an error occurs, this function returns an integer error code and the function pointed to by the <i>register_callback</i> parameter will not be called.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_PROTOCOL_FAILED</i> Protocol error<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_JOB_CONTACT</i> Invalid job contact<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_REQUEST</i> Invalid request<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NO_RESOURCES</i> No resources</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBB">Author</a></p>
<dd></dl>
