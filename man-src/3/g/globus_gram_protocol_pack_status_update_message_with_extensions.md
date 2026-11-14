---
title: "globus_gram_protocol_pack_status_update_message_with_extensions(3)"
name: "globus_gram_protocol_pack_status_update_message_with_extensions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol_pack_status_update_message_with_extensions/"
description: "Message Packing –"
---

<h2 class="name">NAME</h2>
<p> Message Packing &#8211; </p>
<p> Message Packing.</p>
<h3>Functions</h3>
<p> int <code>globus_gram_protocol_pack_job_request</code> (int job_state_mask, const char *callback_url, const char *rsl, globus_byte_t **query, globus_size_t *querysize)<br />
 <i>Pack a GRAM Job Request. </i><br />
 int <code>globus_gram_protocol_pack_job_request_reply</code> (int status, const char *job_contact, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM reply message. </i><br />
 int <code>globus_gram_protocol_pack_job_request_reply_with_extensions</code> (int status, const char *job_contact, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM reply message with extension attributes. </i><br />
 int <code>globus_gram_protocol_pack_status_request</code> (const char *status_request, globus_byte_t **query, globus_size_t *querysize)<br />
 <i>Pack a GRAM query message. </i><br />
 int <code>globus_gram_protocol_pack_status_reply</code> (int job_status, int failure_code, int job_failure_code, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM query reply message. </i><br />
 int <code>globus_gram_protocol_pack_status_reply_with_extensions</code> (int job_status, int failure_code, int job_failure_code, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM query reply message with extensions. </i><br />
 int <code>globus_gram_protocol_pack_status_update_message</code> (char *job_contact, int status, int failure_code, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM status update message. </i><br />
 int <code>globus_gram_protocol_pack_status_update_message_with_extensions</code> (char *job_contact, int status, int failure_code, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)<br />
 <i>Pack a GRAM status update message with extensions. </i><br />
 int <code>globus_gram_protocol_pack_version_request</code> (char **request, size_t *requestsize)<br />
 <i>Pack a GRAM version request message. </i></p>
<h2>Detailed Description</h2>
<p> Message Packing. </p>
<h2>Function Documentation</h2>
<h3>int globus_gram_protocol_pack_job_request (intjob_state_mask, const char *callback_url, const char *rsl, globus_byte_t **query, globus_size_t *querysize)</h3>
<p> Pack a GRAM Job Request. The <code>globus_gram_protocol_pack_job_request()</code> function combines its parameters into a GRAM job request message body. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_post()</code> or just frame it by calling <code>globus_gram_protocol_frame_request()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_job_request()</code> function returns the packed message by modifying the <i>query</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_state_mask</i> The bitwise-or of the GRAM job states which the client would like to register for job state change callbacks.<br />
 <i>callback_url</i> A callback contact string which will be contacted when a job state change which matches the <i>job_state_mask</i> occurs. This may be NULL, if the client does not wish to register a callback contact with this job request. Typically, this value is returned in the <i>url</i> parameter to <code>globus_gram_protocol_allow_attach()</code>.<br />
 <i>rsl</i> An RSL string which contains the job request. This will be processed on the server side.<br />
 <i>query</i> An output parameter which will be set to a new string containing the packed job request message. The caller must free this memory by calling free()<br />
 <i>querysize</i> An output parameter which will be populated with the length of the job request message returned in <i>query</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_job_request()</code> returns GLOBUS_SUCCESS and modifies the <i>query</i> and <i>querysize</i> parameters to point to the values described above.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter</dl>
<h3>int globus_gram_protocol_pack_job_request_reply (intstatus, const char *job_contact, globus_byte_t **reply, globus_size_t *replysize)</h3>
<p> Pack a GRAM reply message. The <code>globus_gram_protocol_pack_job_request_reply()</code> function combines its parameters into a GRAM reply message body. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_reply()</code> or just frame it by calling <code>globus_gram_protocol_frame_reply()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_job_request_reply()</code> function returns the packed message by modifying the <i>reply</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>status</i> The job&#8217;s failure code if the job failed, or 0, if the job request was processed successfully.<br />
 <i>job_contact</i> A string containing the job contact string. This may be NULL, if the job request was not successful.<br />
 <i>reply</i> A pointer which will be set to the packed reply string The caller must free this string by calling free().<br />
 <i>replysize</i> A pointer which will be set to the length of the reply string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_job_request_reply()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>reply</i> and <i>replysize</i> parameters to point to the values described above. If an error occurs, an integer error code is returned and the values pointed to by <i>reply</i> and <i>replysize</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_MALLOC_FAILED</i> Out of memory</dl>
<h3>int globus_gram_protocol_pack_job_request_reply_with_extensions (intstatus, const char *job_contact, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)</h3>
<p> Pack a GRAM reply message with extension attributes. The <code>globus_gram_protocol_pack_job_request_reply_with_extensions()</code> function combines its parameters into a GRAM reply message body. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_reply()</code> or just frame it by calling <code>globus_gram_protocol_frame_reply()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_job_request_reply_with_extensions()</code> function returns the packed message by modifying the <i>reply</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>status</i> The job&#8217;s failure code if the job failed, or 0, if the job request was processed successfully.<br />
 <i>job_contact</i> A string containing the job contact string. This may be NULL, if the job request was not successful.<br />
 <i>extensions</i> A pointer to a hash table keyed on a string attribute name with the hash values being pointers to <i>globus_gram_protocol_extension_t</i> structures. These will be encoded in the reply message after the standard attributes.<br />
 <i>reply</i> A pointer which will be set to the packed reply string The caller must free this string by calling free().<br />
 <i>replysize</i> A pointer which will be set to the length of the reply string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_job_request_reply_with_extensions()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>reply</i> and <i>replysize</i> parameters to point to the values described above. If an error occurs, an integer error code is returned and the values pointed to by <i>reply</i> and <i>replysize</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_MALLOC_FAILED</i> Out of memory</dl>
<h3>int globus_gram_protocol_pack_status_reply (intjob_status, intfailure_code, intjob_failure_code, globus_byte_t **reply, globus_size_t *replysize)</h3>
<p> Pack a GRAM query reply message. The <code>globus_gram_protocol_pack_status_reply()</code> function combines its parameters into a GRAM status reply message body. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_reply()</code> or just frame it by calling <code>globus_gram_protocol_frame_reply()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_status_reply()</code> function returns the packed message by modifying the <i>reply</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_status</i> The job&#8217;s current <code>job state</code>.<br />
 <i>failure_code</i> The error code generated by the query. This may be GLOBUS_SUCCESS if the query succeeded.<br />
 <i>job_failure_code</i> The error code associated with the job if it has failed. This may be GLOBUS_SUCCESS if the job has not failed.<br />
 <i>reply</i> An output parameter which will be set to a new string containing the packed reply message.<br />
 <i>replysize</i> An output parameter which will be set to the length of the reply message returned in <i>reply</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_status_reply()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>reply</i> and <i>replysize</i> parameters to point to the values described above. If an error occurs, an integer error code is returned and the values pointed to by <i>reply</i> and <i>replysize</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_MALLOC_FAILED</i> Out of memory</dl>
<h3>int globus_gram_protocol_pack_status_reply_with_extensions (intjob_status, intfailure_code, intjob_failure_code, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)</h3>
<p> Pack a GRAM query reply message with extensions. The <code>globus_gram_protocol_pack_status_reply_with_extensions()</code> function combines its parameters into a GRAM status reply message body. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_reply()</code> or just frame it by calling <code>globus_gram_protocol_frame_reply()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_status_reply_with_extensions()</code> function returns the packed message by modifying the <i>reply</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_status</i> The job&#8217;s current <code>job state</code>.<br />
 <i>failure_code</i> The error code generated by the query. This may be GLOBUS_SUCCESS if the query succeeded.<br />
 <i>job_failure_code</i> The error code associated with the job if it has failed. This may be GLOBUS_SUCCESS if the job has not failed.<br />
 <i>extensions</i> A pointer to a hash table containing the names and values of the protocol extensions to add to this message.<br />
 <i>reply</i> An output parameter which will be set to a new string containing the packed reply message.<br />
 <i>replysize</i> An output parameter which will be set to the length of the reply message returned in <i>reply</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_status_reply_with_extensions()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>reply</i> and <i>replysize</i> parameters to point to the values described above. If an error occurs, an integer error code is returned and the values pointed to by <i>reply</i> and <i>replysize</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_MALLOC_FAILED</i> Out of memory</dl>
<h3>int globus_gram_protocol_pack_status_request (const char *status_request, globus_byte_t **query, globus_size_t *querysize)</h3>
<p> Pack a GRAM query message. The <code>globus_gram_protocol_pack_status_request()</code> function combines its parameters into a GRAM status query message body. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_post()</code> or just frame it by calling <code>globus_gram_protocol_frame_request()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_status_request()</code> function returns the packed message by modifying the <i>query</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>status_request</i> A string containing the type of query message to send, including any query parameters. The valid strings supported by GRAM in GT5 are:</p>
<dl>
<dt>&bull;</p>
<dd> status</p>
<dt>&bull;</p>
<dd> register</p>
<dt>&bull;</p>
<dd> unregister</p>
<dt>&bull;</p>
<dd> signal</p>
<dt>&bull;</p>
<dd> renew</p>
<dt>&bull;</p>
<dd> cancel</dl>
<p> <i>query</i> An output parameter which will be set to a new string containing the packed job query message.<br />
 <i>querysize</i> An output parameter which will be set to the length of the job query message returned in <i>query</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_status_request()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>query</i> and <i>querysize</i> parameters to point to the values described above. If an error occurs, an integer error code is returned and the values pointed to by <i>query</i> and <i>querysize</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_MALLOC_FAILED</i> Out of memory</dl>
<h3>int globus_gram_protocol_pack_status_update_message (char *job_contact, intstatus, intfailure_code, globus_byte_t **reply, globus_size_t *replysize)</h3>
<p> Pack a GRAM status update message. The <code>globus_gram_protocol_pack_status_update_message()</code> function combines its parameters into a GRAM status update message body. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_post()</code> or just frame it by calling <code>globus_gram_protocol_frame_request()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_status_update_message()</code> function returns the packed message by modifying the <i>reply</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string associated with the job.<br />
 <i>status</i> The job&#8217;s current <code>job state</code>.<br />
 <i>failure_code</i> The error associated with this job request if the <i>status</i> value is GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED.<br />
 <i>reply</i> An output parameter which will be set to a new string containing the packed status message. The caller must free this memory by calling free()<br />
 <i>replysize</i> An output parameter which will be set to the length of the status message returned in <i>reply</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_status_update_message()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>reply</i> and <i>replysize</i> parameters as described above. If an error occurs, an integer error code is returned and the values pointed to by <i>reply</i> and <i>replysize</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory</dl>
<h3>int globus_gram_protocol_pack_status_update_message_with_extensions (char *job_contact, intstatus, intfailure_code, globus_hashtable_t *extensions, globus_byte_t **reply, globus_size_t *replysize)</h3>
<p> Pack a GRAM status update message with extensions. The <code>globus_gram_protocol_pack_status_update_message_with_extensions()</code> function combines its parameters into a GRAM status update message body. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_post()</code> or just frame it by calling <code>globus_gram_protocol_frame_request()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_status_update_message_with_extensions()</code> function returns the packed message by modifying the <i>reply</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>job_contact</i> The job contact string associated with the job.<br />
 <i>status</i> The job&#8217;s current <code>job state</code>.<br />
 <i>failure_code</i> The error associated with this job request if the <i>status</i> value is GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED.<br />
 <i>extensions</i> A pointer to a hash table keyed by extension attribute names with the values being pointers to globus_gram_protocol_extension_t structures.<br />
 <i>reply</i> An output parameter which will be set to a new string containing the packed status message. The caller must free this memory by calling free()<br />
 <i>replysize</i> An output parameter which will be set to the length of the status message returned in <i>reply</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_status_update_message_with_extensions()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>reply</i> and <i>replysize</i> parameters as described above. If an error occurs, an integer error code is returned and the values pointed to by <i>reply</i> and <i>replysize</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory</dl>
<h3>int globus_gram_protocol_pack_version_request (char **request, size_t *requestsize)</h3>
<p> Pack a GRAM version request message. The <code>globus_gram_protocol_pack_job_request()</code> function creates a copy of the GRAM version request. The caller may frame and send the resulting message by calling <code>globus_gram_protocol_post()</code> or just frame it by calling <code>globus_gram_protocol_frame_request()</code> and send it by some other mechanism. The <code>globus_gram_protocol_pack_version_request()</code> function returns the packed message by modifying the <i>request</i> parameter to point to a new string containing the message. The caller is responsible for freeing that string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> An output parameter which will be set to a new string containing the packed version request message. The caller must free this memory by calling free().<br />
 <i>requestsize</i> An output parameter which will be populated with the length of the version request message returned in <i>query</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_pack_job_request()</code> returns GLOBUS_SUCCESS and modifies the <i>request</i> and <i>requestsize</i> parameters to point to the values described above. If an error occurs, <code>globus_gram_protocol_pack_version_request()</code> returns an integer error code and the values pointed to by <i>request</i> and <i>requestsize</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_protocol from the source code. </p>
<h2>Index</h2>
