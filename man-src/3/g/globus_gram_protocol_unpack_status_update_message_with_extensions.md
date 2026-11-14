---
title: "globus_gram_protocol_unpack_status_update_message_with_extensions(3)"
name: "globus_gram_protocol_unpack_status_update_message_with_extensions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_protocol_unpack_status_update_message_with_extensions/"
description: "Message Unpacking –"
---

<h2 class="name">NAME</h2>
<p> Message Unpacking &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_gram_protocol_unpack_job_request</code> (const globus_byte_t *query, globus_size_t querysize, int *job_state_mask, char **callback_url, char **description)<br />
 <i>Unpack a GRAM Job Request. </i><br />
 int <code>globus_gram_protocol_unpack_job_request_reply</code> (const globus_byte_t *reply, globus_size_t replysize, int *status, char **job_contact)<br />
 <i>Unpack a GRAM reply message. </i><br />
 int <code>globus_gram_protocol_unpack_job_request_reply_with_extensions</code> (const globus_byte_t *reply, globus_size_t replysize, int *status, char **job_contact, globus_hashtable_t *extensions)<br />
 <i>Unpack a GRAM reply message, parsing all extensions. </i><br />
 int <code>globus_gram_protocol_unpack_status_request</code> (const globus_byte_t *query, globus_size_t querysize, char **status_request)<br />
 <i>Unpack a GRAM query message. </i><br />
 int <code>globus_gram_protocol_unpack_status_reply</code> (const globus_byte_t *reply, globus_size_t replysize, int *job_status, int *failure_code, int *job_failure_code)<br />
 <i>Unpack a GRAM query reply. </i><br />
 int <code>globus_gram_protocol_unpack_status_reply_with_extensions</code> (const globus_byte_t *reply, globus_size_t replysize, globus_hashtable_t *extensions)<br />
 <i>Unpack a GRAM query reply with extensions. </i><br />
 int <code>globus_gram_protocol_unpack_status_update_message</code> (const globus_byte_t *reply, globus_size_t replysize, char **job_contact, int *status, int *failure_code)<br />
 <i>Unpack a GRAM status update message. </i><br />
 int <code>globus_gram_protocol_unpack_status_update_message_with_extensions</code> (const globus_byte_t *reply, globus_size_t replysize, globus_hashtable_t *extensions)<br />
 <i>Unpack a GRAM status update message with extensions. </i><br />
 void <code>globus_gram_protocol_hash_destroy</code> (globus_hashtable_t *message_hash) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>void globus_gram_protocol_hash_destroy (globus_hashtable_t *message_hash)</h3>
<p> Destroy message attribute hash </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>message_hash</i> Hashtable of globus_gram_protocol_extension_t * values to destroy</dl>
<h3>int globus_gram_protocol_unpack_job_request (const globus_byte_t *query, globus_size_tquerysize, int *job_state_mask, char **callback_url, char **description)</h3>
<p> Unpack a GRAM Job Request. The <code>globus_gram_protocol_unpack_job_request()</code> function parses the job request message packed in the <i>query</i> message and returns copies of the standard message attributes in the <i>job_state_mask</i>, <i>callback_url</i>, and <i>description</i> parameters. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>query</i> The unframed job request message to parse.<br />
 <i>querysize</i> The length of the job request message string.<br />
 <i>job_state_mask</i> A pointer to an integer to be set to the job state mask from the job request.<br />
 <i>callback_url</i> A pointer to be set with a copy of the URL of the callback contact to be registered for this job request. The caller must free this memory by calling free().<br />
 <i>description</i> A pointer to be set to a copy of the job description RSL string for this job request. The caller must free this memory by calling free().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_unpack_job_request()</code> will return <i>GLOBUS_SUCCESS</i> and modify the <i>job_state_mask</i>, <i>callback_url</i>, and <i>description</i> parameters to values extracted from the message in <i>query</i>. If an error occurs, an integer error code will be returned and the values of <i>job_state_mask</i>, <i>callback_url</i>, and <i>description</i> will be undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED</i> Unpack failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_VERSION_MISMATCH</i> Version mismatch</dl>
<h3>int globus_gram_protocol_unpack_job_request_reply (const globus_byte_t *reply, globus_size_treplysize, int *status, char **job_contact)</h3>
<p> Unpack a GRAM reply message. The <code>globus_gram_protocol_unpack_job_request_reply()</code> function parses the reply message packed in the <i>reply</i> message and returns copies of the standard message attributes in the <i>status</i> and <i>job_contact</i> parameters. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>reply</i> The unframed job reply message to parse.<br />
 <i>replysize</i> The length of the reply string.<br />
 <i>status</i> A pointer to an integer to be set to the failure code associated with the job request. This may be GLOBUS_SUCCESS, if the job request was successful.<br />
 <i>job_contact</i> A pointer to a string to be set to the job contact string. This may set to NULL if the job request failed. If <code>globus_gram_protocol_unpack_job_request_reply()</code> returns GLOBUS_SUCCESS, then the caller must free this string using free().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_unpack_job_request_reply()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>status</i> and <i>job_contact</i> parameters to point to the values described above. If an error occurs, an integer error code is returned and the values pointed to by <i>status</i> and <i>job_contact</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAN_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED</i> Unpack failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_VERSION_MISMATCH</i> Version mismatch</dl>
<h3>int globus_gram_protocol_unpack_job_request_reply_with_extensions (const globus_byte_t *reply, globus_size_treplysize, int *status, char **job_contact, globus_hashtable_t *extensions)</h3>
<p> Unpack a GRAM reply message, parsing all extensions. The <code>globus_gram_protocol_unpack_job_request_reply_with_extensions()</code> function parses the reply message packed in the <i>reply</i> message parameter and returns copies of the standard message attributes in the <i>status</i> and <i>job_contact</i> parameters, and all other extension attributes in the hashtable pointed to by <i>extensions</i>. Each entry in the hashtable will be keyed by the attribute name and the value will be a pointer to a <i>globus_gram_protocol_extension_t</i> structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>status</i> A pointer to an integer to be set to the failure code associated with the job request. This may be GLOBUS_SUCCESS, if the job request was successful.<br />
 <i>job_contact</i> A pointer to a string to be set to the job contact string. This may set to NULL if the job request failed. If <code>globus_gram_protocol_unpack_job_request_reply_with_extensions()</code> returns GLOBUS_SUCCESS, then the caller must free this string using free().<br />
 <i>extensions</i> A pointer to be set to a hash table containing the names and values of all protocol extensions present in the response message. If <code>globus_gram_protocol_unpack_job_request_reply_with_extensions()</code> returns GLOBUS_SUCCESS, the caller must free this hash table and its values by calling <code>globus_gram_protocol_hash_destroy()</code>.<br />
 <i>reply</i> The unframed job reply message to parse.<br />
 <i>replysize</i> The length of the reply string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_unpack_job_request_reply_with_extensions()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>status</i>, <i>job_contact</i>, and <i>extensions</i> to point to the values described above. If an error occurs, an integer error code is returned and the values pointed to by <i>status</i>, <i>job_contact</i>, and <i>extensions</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAN_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED</i> Unpack failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_VERSION_MISMATCH</i> Version mismatch</dl>
<h3>int globus_gram_protocol_unpack_status_reply (const globus_byte_t *reply, globus_size_treplysize, int *job_status, int *failure_code, int *job_failure_code)</h3>
<p> Unpack a GRAM query reply. The <code>globus_gram_protocol_unpack_status_reply()</code> function parses the message packed in the <i>reply</i> parameter and sets the current job state, protocol failure code, and job failure code values in its output parameters. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>reply</i> The unframed reply message to parse.<br />
 <i>replysize</i> The length of the reply message.<br />
 <i>job_status</i> A pointer to an integer to be set to the job&#8217;s current <code>job state</code>.<br />
 <i>failure_code</i> A pointer to an integer to be set to the failure code associated with the query request. This may be GLOBUS_SUCCESS, if the request was successful.<br />
 <i>job_failure_code</i> A pointer to an integer to be set to the failure code for the job, if the <i>job_status</i> is GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_unpack_status_reply()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>job_status</i>, <i>failure_code</i>, and <i>job_failure_code</i> parameters to point to the value described above. If an error occurs, an integer error code is returned and the values pointed to by <i>job_status</i>, <i>failure_code</i>, and <i>job_failure_code</i> are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED</i> Unpack failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_VERSION_MISMATCH</i> Version mismatch<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter</dl>
<h3>int globus_gram_protocol_unpack_status_reply_with_extensions (const globus_byte_t *reply, globus_size_treplysize, globus_hashtable_t *extensions)</h3>
<p> Unpack a GRAM query reply with extensions. The <code>globus_gram_protocol_unpack_status_reply_with_extensions()</code> function parses the message packed in the <i>reply</i> parameter, storing all attributes and values in a hash table. The <i>extensions</i> parameter is modified to point to that hash table. The caller of <code>globus_gram_protocol_unpack_status_reply_with_extensions()</code> must free that hash table by calling <code>globus_gram_protocol_hash_destroy()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>reply</i> The unframed reply message to parse.<br />
 <i>replysize</i> The length of the reply message.<br />
 <i>extensions</i> A pointer to be set to a hash table containing the names and values of all protocol attributes present in the reply message. If <code>globus_gram_protocol_unpack_status_reply_with_extensions()</code> returns GLOBUS_SUCCESS, the caller must free this hash table and its values by calling <code>globus_gram_protocol_hash_destroy()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_unpack_status_reply_with_extensions()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>extensions</i> parameter to point to the value described above. If an error occurs, an integer error code is returned and the value pointed to by <i>extensions</i> is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED</i> Unpack failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_VERSION_MISMATCH</i> Version mismatch</dl>
<h3>int globus_gram_protocol_unpack_status_request (const globus_byte_t *query, globus_size_tquerysize, char **status_request)</h3>
<p> Unpack a GRAM query message. The <code>globus_gram_protocol_unpack_status_request()</code> function parses the message packed in the <i>query</i> parameter and returns a copy of the message in the <i>status_request</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>query</i> The unframed query message to parse.<br />
 <i>querysize</i> The length of the query string.<br />
 <i>status_request</i> A pointer to a string to be set to the query value. The caller must free this string using free().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_unpack_status_request()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>status_request</i> parameter to point to the value described above. If an error occurs, an integer error code is returned and the value pointed to by <i>status_request</i> is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED</i> Unpack failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_VERSION_MISMATCH</i> Version mismatch</dl>
<h3>int globus_gram_protocol_unpack_status_update_message (const globus_byte_t *reply, globus_size_treplysize, char **job_contact, int *status, int *failure_code)</h3>
<p> Unpack a GRAM status update message. The <code>globus_gram_protocol_unpack_status_update_message()</code> function parses the message packed in the <i>reply</i> parameter, storing the standard message attribute values in its return parameters <i>job_contact</i>, <i>status</i>, and <i>failure_code</i>. The caller is responsible for freeing the <i>job_contact</i> value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>reply</i> The unframed reply message to parse.<br />
 <i>replysize</i> The length of the reply message.<br />
 <i>job_contact</i> An output parameter to be set to the job contact string. If <code>globus_gram_protocol_unpack_status_update_message()</code> returns GLOBUS_SUCCESS, then the caller must free this string using free().<br />
 <i>status</i> An output parameter to be set to the integer value of the job&#8217;s current <code>job state</code>.<br />
 <i>failure_code</i> An output parameter to be set to the integer failure code for the job if the <i>job_status</i> is GLOBUS_GRAM_PROTOCOL_JOB_STATE_FAILED.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_unpack_status_update_message()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>job_contact</i>, <i>status</i>, and <i>failure_code</i> parameters as described above. If an error occurs, an integer error code is returned and the values pointed to by the <i>job_contact</i>, <i>status</i>, and <i>failure_code</i> parameters are undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Sucess<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED</i> Unpack failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_VERSION_MISMATCH</i> Version mismatch</dl>
<h3>int globus_gram_protocol_unpack_status_update_message_with_extensions (const globus_byte_t *reply, globus_size_treplysize, globus_hashtable_t *extensions)</h3>
<p> Unpack a GRAM status update message with extensions. The <code>globus_gram_protocol_unpack_status_update_message_with_extensions()</code> function parses the message packed in the <i>reply</i> parameter, storing the message attribute values in its return parameter <i>extensions</i>. The caller is responsible for freeing the <i>extensions</i> hash table by calling <code>globus_gram_protocol_hash_destroy()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>reply</i> The unframed reply message to parse.<br />
 <i>replysize</i> The length of the reply message.<br />
 <i>extensions</i> An output parameter which will be initialized to a hashtable containing the message attributes. The caller must destroy this hashtable calling <code>globus_gram_protocol_hash_destroy()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_protocol_unpack_status_update_message_with_extensions()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the <i>extensions</i> parameter as described above. If an error occurs, an integer error code is returned and the value pointed to by the <i>extensions</i> parameters is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Sucess<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_HTTP_UNPACK_FAILED</i> Unpack failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Malloc failed<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_VERSION_MISMATCH</i> Version mismatch</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_protocol from the source code. </p>
<h2>Index</h2>
