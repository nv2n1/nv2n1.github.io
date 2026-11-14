---
title: "globus_gass_transfer_request_get_denial_reason(3)"
name: "globus_gass_transfer_request_get_denial_reason"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_request_get_denial_reason/"
description: "Request Handles –"
---

<h2 class="name">NAME</h2>
<p> Request Handles &#8211; </p>
<p> Request Handles.</p>
<h3>Data Structures</h3>
<p> struct <code>globus_gass_transfer_request_t</code><br />
 <i>Request handle. </i></p>
<h3>Enumerations</h3>
<p> enum <code>globus_gass_transfer_request_type_t</code> { <code>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_INVALID</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_GET</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_PUT</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_APPEND</code> } </p>
<p> enum <code>globus_gass_transfer_request_status_t</code> { <code>GLOBUS_GASS_TRANSFER_REQUEST_INVALID</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_STARTING</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_PENDING</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_FAILED</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_DENIED</code>, <code>GLOBUS_GASS_TRANSFER_REQUEST_DONE</code> } </p>
<h3>Functions</h3>
<p> <code>globus_gass_transfer_request_type_t</code> <code>globus_gass_transfer_request_get_type</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<p> void * <code>globus_gass_transfer_request_get_user_pointer</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<p> int <code>globus_gass_transfer_request_set_user_pointer</code> (<code>globus_gass_transfer_request_t</code> request, void *user_pointer) </p>
<p> <code>globus_gass_transfer_request_status_t</code> <code>globus_gass_transfer_request_get_status</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<p> int <code>globus_gass_transfer_request_get_referral</code> (<code>globus_gass_transfer_request_t</code> request, globus_gass_transfer_referral_t *referral) </p>
<p> char * <code>globus_gass_transfer_request_get_url</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<p> globus_size_t <code>globus_gass_transfer_request_get_length</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<p> int <code>globus_gass_transfer_request_set_type</code> (<code>globus_gass_transfer_request_t</code> request, <code>globus_gass_transfer_request_type_t</code> type) </p>
<p> int <code>globus_gass_transfer_request_set_url</code> (<code>globus_gass_transfer_request_t</code> request, char *url) </p>
<p> void <code>globus_gass_transfer_request_set_length</code> (<code>globus_gass_transfer_request_t</code> request, globus_size_t length) </p>
<p> int <code>globus_gass_transfer_request_get_denial_reason</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<p> char * <code>globus_gass_transfer_request_get_denial_message</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<p> char * <code>globus_gass_transfer_request_get_subject</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<p> int <code>globus_gass_transfer_request_destroy</code> (<code>globus_gass_transfer_request_t</code> request) </p>
<h2>Detailed Description</h2>
<p> Request Handles. </p>
<p> Request handles are used by the GASS Transfer API to associate operations with a single file transfer request. Specifically, they are used to register multiple byte range buffers with a file transfer request, and to query the state of a transfer in-progress. </p>
<p> To implement a server, the request handle is populated by the protocol module implementation. The server may use the functions in this section to determine information about what the client is requesting. </p>
<p> To implement a client, the request handle should be queried after the blocking call or initial callback has been invoked to determine if the request has been authorized or referred, and after EOF, to determine whether the request has completed successfully. </p>
<p> A request handle contains a pointer which may be used by the handler of the request to store a pointer to arbitrary application-specific data.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gass_transfer_request_status_t</code></h3>
<p> Request Status </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_INVALID </i></p>
<dd> Handle is no longer valid</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_STARTING </i></p>
<dd> Initial connection and authorization is not yet completed</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_PENDING </i></p>
<dd> Request is authorized.</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_FAILED </i></p>
<dd> Request failed due to protocol error or client or server aborting the request</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED </i></p>
<dd> Request can not be processed by this server, referred to another URL or URLs</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_DENIED </i></p>
<dd> The server denied this request</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_DONE </i></p>
<dd> All callbacks have completed</dl>
<h3>enum <code>globus_gass_transfer_request_type_t</code></h3>
<p> Type of operation associated with a request handle. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_INVALID </i></p>
<dd> Handle no longer valid</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_GET </i></p>
<dd> A get request</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_PUT </i></p>
<dd> A put request</p>
<dt><i>GLOBUS_GASS_TRANSFER_REQUEST_TYPE_APPEND </i></p>
<dd> An append request</dl>
<h2>Function Documentation</h2>
<h3>int globus_gass_transfer_request_destroy (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Destroy a request handle. </p>
<p> This function destroys the caller&#8217;s reference to a request handle. It must be called for all request handles which are created by calling functions in the &#8216;@ref globus_gass_transfer_client&#8217; or &#8216;@ref globus_gass_transfer_server&#8217; sections of this manual. After calling the function, the caller must not attempt to use the request handle for any purpose. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request to destroy.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The request handle reference was successfully destroyed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> Either an invalid request handle or one which is actively being used was passed to this function as the <i>request</i> parameter.</dl>
<h3>char* globus_gass_transfer_request_get_denial_message (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Get an string describing why a request was denied. </p>
<p> This function queries a request which was denied by a server to determine why it was denied. The denial reason will be expressed as a response string. The string must be freed by the caller. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A handle to the request to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A string indicating why the request was denied. If the request handle is invalid or the request was not denied, then this function returns GLOBUS_NULL.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_request_get_denial_reason()</code></dl>
<h3>int globus_gass_transfer_request_get_denial_reason (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Get an integer code describing why the request was denied. </p>
<p> This function queries a request which was denied by a server to determine why it was denied. The denial reason will be expressed in a protocol-specific response code. Knowledge of the protocol is needed to understand this response. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A handle to the request to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A protocol-specific integer indicating why the request was denied. If the request handle is invalid or the request was not denied, then this function returns 0.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_request_get_denial_message()</code></dl>
<h3>globus_size_t globus_gass_transfer_request_get_length (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Get the length of a file to be transferred using GASS. </p>
<p> This function queries the request handle to determine the amount of data that will be transferred to copy the URL. The length may be <i>GLOBUS_GASS_TRANSFER_LENGTH_UNKNOWN</i> if the sender can not determine the length before making or authorizing the request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The length of the file located at the request&#8217;s URL, or <i>GLOBUS_GASS_TRANSFER_LENGTH_UNKNOWN</i> if that cannot be determined.</dl>
<h3>int globus_gass_transfer_request_get_referral (<code>globus_gass_transfer_request_t</code>request, globus_gass_transfer_referral_t *referral)</h3>
<p> Extract referral information from a request handle. </p>
<p> This function queries the request handle to determine any referral information that it contains. This function should only be called on request handles in the GLOBUS_GASS_TRANSFER_REQUEST_REFERRED state. If no referral information is stored in the request handle, then the referral will be initialized to an empty referral. The referral must be destroyed by calling <code>globus_gass_transfer_referral_destroy()</code> by the caller. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle to query.<br />
 <i>referral</i> A pointer to an uninitialized referral structure. It will be populated by calling this function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The referral was successfully extracted from the request handle.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> The referral pointer was GLOBUS_NULL;</dl>
<h3><code>globus_gass_transfer_request_status_t</code> globus_gass_transfer_request_get_status (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Check the status of a request. </p>
<p> This function queries a request to determine the status of the request. This function should be called after EOF has been reached, or after the initial get, put, or append has returned or had it&#8217;s callback function called to determine if it is possible to procede, or whether the file transfer was successfully processed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A <code>globus_gass_transfer_request_status_t</code> indicating the current status of the request.</dl>
<h3>char* globus_gass_transfer_request_get_subject (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Get the subject string associated with a request. </p>
<p> This function queries a request handle to determine the subject identity of the client who initiated the request. The string must not be freed by the caller. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A handle to the request to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A string containing the request initiator&#8217;s subject identity. If the request handle is invalid or a credential was not used to initiate the request, this value will be GLOBUS_NULL.</dl>
<h3><code>globus_gass_transfer_request_type_t</code> globus_gass_transfer_request_get_type (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Determine the type of a request. </p>
<p> This function is used by GASS server implementations to discover what type of operation the client is requesting for an URL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>type</code> of the request.</dl>
<h3>char* globus_gass_transfer_request_get_url (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Get the URL from a request handle. </p>
<p> This function queries the request handle to determine the URL associated with the request. This function is intended to be useful to GASS server implementors. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> A pointer to the URL, or GLOBUS_NULL if the request handle is invalid. The string which is returned must not be freed by the caller. It may not be accessed after the request has been destroyed.</dl>
<h3>void* globus_gass_transfer_request_get_user_pointer (<code>globus_gass_transfer_request_t</code>request)</h3>
<p> Get the user pointer associated with a request </p>
<p> This function extracts the user pointer from a request handle. The user-pointer may be used by the application which is generating or servicing the request to store a pointer to any application-specific piece of data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request to query.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The user pointer&#8217;s value.</dl>
<h3>void globus_gass_transfer_request_set_length (<code>globus_gass_transfer_request_t</code>request, globus_size_tlength)</h3>
<p> Set the length of a transfer associated request handle. </p>
<p> This function modifies the given request handle so that it&#8217;s length field is set to give length parameter. </p>
<p> This function must only be called by protocol modules when constructing a request handle when receiving the response to a get request. This function can only be called once per request handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A handle to the request to modify.<br />
 <i>length</i> The length of the file request.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The URL was set for the request handle.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> The request handle was invalid, or the URL had already been set.</dl>
<h3>int globus_gass_transfer_request_set_type (<code>globus_gass_transfer_request_t</code>request, <code>globus_gass_transfer_request_type_t</code>type)</h3>
<p> Set the type of a request. </p>
<p> This function modifies a request handle by setting the type of operation that it is being used for. This function may only be called once per handle, and only from a GASS protocol module implementation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request handle to modify.<br />
 <i>type</i> The type of operation that this request handle will be used for.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The request handle&#8217;s type has been set.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> The request handle was invalid or it&#8217;s type was already set. The request handle was not modified.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Only GASS Protocol modules may call this function.</dl>
<h3>int globus_gass_transfer_request_set_url (<code>globus_gass_transfer_request_t</code>request, char *url)</h3>
<p> Set the URL to which a request handle refers. </p>
<p> This function modifies the given request handle so that it&#8217;s URL field is set to string pointed to by <i>url</i>. </p>
<p> No copy is made of the string, so the caller must not free it. It must be allocated by calling one of the memory allocators in globus_libc, as it will be freed when the request handle is destroyed. </p>
<p> This function must only be called by protocol modules when constructing a request handle when accepting a new request. This function can only be called once per request handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A handle to the request to modify.<br />
 <i>url</i> A string containing the URL that this request will be associated with.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The URL was set for the request handle.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> The request handle was invalid, or the URL had already been set.</dl>
<h3>int globus_gass_transfer_request_set_user_pointer (<code>globus_gass_transfer_request_t</code>request, void *user_pointer)</h3>
<p> Set the user pointer associated with a request handle. </p>
<p> This function sets the user pointer from a request handle. The user-pointer may be used by the application which is generating or servicing the request to store a pointer to any application-specific piece of data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> The request to modify.<br />
 <i>user_pointer</i> The new value of the user pointer for the request.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCES</i> The user pointer&#8217;s value was set.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INVALID_USE</i> An invalid request handle was passed to this function</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Function Documentation</a></p>
<dd>
<dt><a href="#lbAY">Author</a></p>
<dd></dl>
