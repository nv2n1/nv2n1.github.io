---
title: "globus_gram_client-h(3)"
name: "globus_gram_client-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_client-h/"
description: "globus_gram_client.h – GRAM Client API."
---

<p>globus_gram_client.h &#8211; GRAM Client API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_io.h&#8217;<br />
 #include &#8216;globus_gram_protocol_constants.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>globus_gram_client_job_info_s</code><br />
 <i>Extensible job information structure. </i></p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GRAM_CLIENT_NO_ATTR</code><br />
 <i>Default GRAM client operation attribute. </i></p>
<h3>Typedefs</h3>
<p>typedef void(* <code>globus_gram_client_callback_func_t</code> )(void *user_callback_arg, char *job_contact, int state, int errorcode)<br />
 <i>Signature for GRAM state notification callback functions. </i><br />
 typedef struct<br />
 <code>globus_gram_client_job_info_s</code> <code>globus_gram_client_job_info_t</code>&quot;<br />
 <i>Extensible job information structure. </i><br />
 typedef void(* <code>globus_gram_client_info_callback_func_t</code> )(void *user_callback_arg, const char *job_contact, <code>globus_gram_client_job_info_t</code> *job_info)<br />
 <i>Signature for GRAM state notification callback functions with extension support. </i><br />
 typedef void * <code>globus_gram_client_attr_t</code><br />
 <i>GRAM client operation attribute. </i><br />
 typedef void(* <code>globus_gram_client_nonblocking_func_t</code> )(void *user_callback_arg, globus_gram_protocol_error_t operation_failure_code, const char *job_contact, globus_gram_protocol_job_state_t job_state, globus_gram_protocol_error_t job_failure_code)<br />
 <i>Signature for callbacks signalling completion of non-blocking GRAM requests. </i></p>
<h3>Functions</h3>
<p>int <code>globus_gram_client_callback_allow</code> (<code>globus_gram_client_callback_func_t</code> callback_func, void *user_callback_arg, char **callback_contact)<br />
 <i>Begin listening for job state change callbacks. </i><br />
 int <code>globus_gram_client_info_callback_allow</code> (<code>globus_gram_client_info_callback_func_t</code> callback_func, void *user_callback_arg, char **callback_contact)<br />
 <i>Begin listening for job state change callbacks. </i><br />
 int <code>globus_gram_client_register_job_request</code> (const char *resource_manager_contact, const char *description, int job_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Send a job request to a GRAM service. </i><br />
 int <code>globus_gram_client_job_request</code> (const char *resource_manager_contact, const char *description, int job_state_mask, const char *callback_contact, char **job_contact)<br />
 <i>Send a job request to a GRAM service. </i><br />
 int <code>globus_gram_client_register_job_request_with_info</code> (const char *resource_manager_contact, const char *description, int job_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_info_callback_func_t</code> callback, void *callback_arg)<br />
 <i>Send a job request to a GRAM service with extensions-aware callback. </i><br />
 int <code>globus_gram_client_job_request_with_info</code> (const char *resource_manager_contact, const char *description, int job_state_mask, const char *callback_contact, char **job_contact, <code>globus_gram_client_job_info_t</code> *info)<br />
 <i>Send a job request to a GRAM service and parse extensions in the response. </i><br />
 int <code>globus_gram_client_register_job_cancel</code> (const char *job_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Cancel a GRAM job. </i><br />
 int <code>globus_gram_client_job_cancel</code> (const char *job_contact)<br />
 <i>Cancel a GRAM job. </i><br />
 int <code>globus_gram_client_register_job_status</code> (const char *job_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Send a status query to a GRAM job. </i><br />
 int <code>globus_gram_client_register_job_status_with_info</code> (const char *job_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_info_callback_func_t</code> info_callback, void *callback_arg)<br />
 <i>Send a status query to a GRAM job. </i><br />
 int <code>globus_gram_client_job_refresh_credentials</code> (char *job_contact, gss_cred_id_t creds)<br />
 <i>Delegate a new credential to a job. </i><br />
 int <code>globus_gram_client_register_job_refresh_credentials</code> (char *job_contact, gss_cred_id_t creds, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Delegate a new credential to a job. </i><br />
 int <code>globus_gram_client_job_status</code> (const char *job_contact, int *job_status, int *failure_code)<br />
 <i>Send a status query to a GRAM job. </i><br />
 int <code>globus_gram_client_job_status_with_info</code> (const char *job_contact, <code>globus_gram_client_job_info_t</code> *job_info)<br />
 <i>Send a status query to a GRAM job. </i><br />
 int <code>globus_gram_client_register_job_signal</code> (const char *job_contact, globus_gram_protocol_job_signal_t signal, const char *signal_arg, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Send a signal a GRAM job. </i><br />
 int <code>globus_gram_client_job_signal</code> (const char *job_contact, globus_gram_protocol_job_signal_t signal, const char *signal_arg, int *job_status, int *failure_code)<br />
 <i>Send a signal a GRAM job. </i><br />
 int <code>globus_gram_client_register_job_callback_registration</code> (const char *job_contact, int job_state_mask, const char *callback_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Register a new callback contact to be notified for job state changes. </i><br />
 int <code>globus_gram_client_job_callback_register</code> (const char *job_contact, int job_state_mask, const char *callback_contact, int *job_status, int *failure_code)<br />
 <i>Register a new callback contact to be notified for job state changes. </i><br />
 int <code>globus_gram_client_register_job_callback_unregistration</code> (const char *job_contact, const char *callback_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Unregister a callback contact to stop job state change notifications. </i><br />
 int <code>globus_gram_client_job_callback_unregister</code> (const char *job_contact, const char *callback_contact, int *job_status, int *failure_code)<br />
 <i>Unregister a callback contact to stop job state change notifications. </i><br />
 int <code>globus_gram_client_callback_disallow</code> (char *callback_contact)<br />
 <i>Stop listening for job state change callbacks. </i><br />
 int <code>globus_gram_client_job_contact_free</code> (char *job_contact)<br />
 <i>Free a job contact string. </i><br />
 const char * <code>globus_gram_client_error_string</code> (int error_code)<br />
 <i>Get a description of a a GRAM error code. </i><br />
 int <code>globus_gram_client_version</code> (void)<br />
 <i>Return GRAM protocol version. </i><br />
 int <code>globus_gram_client_set_credentials</code> (gss_cred_id_t new_credentials)<br />
 <i>Set the default GRAM credential. </i><br />
 int <code>globus_gram_client_ping</code> (const char *resource_manager_contact)<br />
 <i>Send a ping request to a GRAM service. </i><br />
 int <code>globus_gram_client_register_ping</code> (const char *resource_manager_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_nonblocking_func_t</code> register_callback, void *register_callback_arg)<br />
 <i>Send a ping request to a GRAM service. </i><br />
 int <code>globus_gram_client_get_jobmanager_version</code> (const char *resource_manager_contact, globus_hashtable_t *extensions)<br />
 <i>Get version information from a job manager. </i><br />
 int <code>globus_gram_client_register_get_jobmanager_version</code> (const char *resource_manager_contact, <code>globus_gram_client_attr_t</code> attr, <code>globus_gram_client_info_callback_func_t</code> info_callback, void *callback_arg)<br />
 <i>Get version information from a job manager without blocking. </i><br />
 void <code>globus_gram_client_debug</code> (void)<br />
 <i>Enable GRAM debugging. </i><br />
 int <code>globus_gram_client_attr_init</code> (<code>globus_gram_client_attr_t</code> *attr)<br />
 <i>Initialize a GRAM client attribute. </i><br />
 int <code>globus_gram_client_attr_destroy</code> (<code>globus_gram_client_attr_t</code> *attr)<br />
 <i>Destroy a GRAM client attribute. </i><br />
 int <code>globus_gram_client_attr_set_credential</code> (<code>globus_gram_client_attr_t</code> attr, gss_cred_id_t credential)<br />
 <i>Set a GRAM client attribute&#8217;s security credential. </i><br />
 int <code>globus_gram_client_attr_get_credential</code> (<code>globus_gram_client_attr_t</code> attr, gss_cred_id_t *credential)<br />
 <i>Get a GRAM client attribute&#8217;s security credential. </i><br />
 int <code>globus_gram_client_attr_set_delegation_mode</code> (<code>globus_gram_client_attr_t</code> attr, globus_io_secure_delegation_mode_t mode)<br />
 <i>Set a GRAM client attribute&#8217;s delegation mode. </i><br />
 int <code>globus_gram_client_attr_get_delegation_mode</code> (<code>globus_gram_client_attr_t</code> attr, globus_io_secure_delegation_mode_t *mode)<br />
 <i>Get a GRAM client attribute&#8217;s security credential. </i><br />
 void <code>globus_gram_client_job_info_destroy</code> (<code>globus_gram_client_job_info_t</code> *info)<br />
 <i>Free memory associated with a globus_gram_client_job_info_t structure. </i></p>
<h2>Detailed Description</h2>
<p>GRAM Client API. </p>
<p> This header file contains the exported client interface of the Resource Allocation Management System.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gram_client from the source code.</p>
