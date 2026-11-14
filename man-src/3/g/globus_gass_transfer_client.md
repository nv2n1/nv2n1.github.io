---
title: "globus_gass_transfer_client(3)"
name: "globus_gass_transfer_client"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_client/"
description: "Client-Initiated Operations –"
---

<h2 class="name">NAME</h2>
<p> Client-Initiated Operations &#8211; </p>
<p> GASS Transfer Client Operations.</p>
<h3>Functions</h3>
<p> int <code>globus_gass_transfer_register_get</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_gass_transfer_callback_t callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_get</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url) </p>
<p> int <code>globus_gass_transfer_register_put</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_t length, globus_gass_transfer_callback_t callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_put</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_t length) </p>
<p> int <code>globus_gass_transfer_register_append</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_t length, globus_gass_transfer_callback_t callback, void *user_arg) </p>
<p> int <code>globus_gass_transfer_append</code> (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_t length) </p>
<h2>Detailed Description</h2>
<p> GASS Transfer Client Operations. </p>
<p> One mode of using the GASS Transfer API is to initiate file transfers. The operations supported by the GASS Transfer API are file get, put, and append. These operations are provided for HTTP, and HTTPS file servers. The <code>protocol module interface</code> allows support for additional protocols to be added easily. </p>
<p> The GASS transfer library provides both blocking and non-blocking versions of all its client functions. When a blocking function completes, or the non-blocking function&#8217;s callback is called, the user should check the request&#8217;s status to discover whether the transfer was completed successfully, denied, or referred.</p>
<h2>Function Documentation</h2>
<h3>int globus_gass_transfer_append (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_tlength)</h3>
<p> Blocking file append. </p>
<p> This function initiates a new &#8216;append&#8217; request of the file named by <i>url</i>. The entire file will be transferred to the server if the user is authorized to do so. This function blocks until the GASS library has determined whether the file may be retrieved by the caller, may not because it is a referral to another URL or URLs, or the server has denied the request. </p>
<p> Upon returning from this function, the request handle is initialized to refer to the <i>append</i> request&#8217;s state. </p>
<p> If the server can&#8217;t store the file at <i>url</i>, but has an alternative location for the user to store to, then this function return with request&#8217;s status set to <i>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A pointer to an uninitialized request handle.<br />
 <i>attr</i> Request attributes.<br />
 <i>url</i> URL to append to.<br />
 <i>length</i> The length of the data to append to the url, if known. If this parameter is set to <i>GLOBUS_GASS_LENGTH_UNKNOWN</i>, then the append may fail if the protocol does not support arbitrarily-length files.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The put was successfully initiated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> One of request, attr, or callback was GLOBUS_NULL. The put could not be processed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR</i> An internal resource was not available to process the put.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> No protocol handler for doing a append on this URL type is implemented.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_BAD_URL</i> The URL could not be parsed.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_register_append()</code></dl>
<h3>int globus_gass_transfer_get (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url)</h3>
<p> Blocking file get. </p>
<p> This function initiates a new &#8216;get&#8217; request of the file named by <i>url</i>. The entire file will be transferred from the server if the file exists and user is authorized to do so. This function blocks until the GASS library has determined whether the file may be retrievied by the caller, may not because it is a referral to another URL or URLs, or the server has denied the request. </p>
<p> Upon returning from this function, the request handle is initialized to refer to the <i>get</i> request&#8217;s state. This request handle must be destroyed after the user has finished processing the data associated with the callback. </p>
<p> If the file doesn&#8217;t exist at <i>url</i>, but a referral does, then this function will return with the request&#8217;s status set to <i>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A pointer to an uninitialized request handle.<br />
 <i>attr</i> Request attributes.<br />
 <i>url</i> URL to get</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The get was successfully initiated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> One of request or attr was GLOBUS_NULL. The get could not be processed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR</i> An internal resource was not available to process the get.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> No protocol handler for doing a get on this URL type is implemented.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_BAD_URL</i> The URL could not be parsed.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_register_get()</code></dl>
<h3>int globus_gass_transfer_put (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_tlength)</h3>
<p> Blocking file put. </p>
<p> This function initiates a new &#8216;put&#8217; request of the file named by <i>url</i>. The entire file will be transferred to the server if the user is authorized to do so. This function blocks until the GASS library has determined whether the file may be retrieved by the caller, may not because it is a referral to another URL or URLs, or the server has denied the request. </p>
<p> Upon returning from this function, the request handle is initialized to refer to the <i>put</i> request&#8217;s state. </p>
<p> If the server can&#8217;t store the file at <i>url</i>, but has an alternative location for the user to store to, then this function return with request&#8217;s status set to <i>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A pointer to an uninitialized request handle.<br />
 <i>attr</i> Request attributes.<br />
 <i>url</i> URL to put.<br />
 <i>length</i> The length of the data to put to the url, if known. If this parameter is set to <i>GLOBUS_GASS_LENGTH_UNKNOWN</i>, then the put may fail if the protocol does not support arbitrarily-length files.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The get was successfully initiated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> One of request or attr was GLOBUS_NULL. The get could not be processed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR</i> An internal resource was not available to process the get.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> No protocol handler for doing a put on this URL type is implemented.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_BAD_URL</i> The URL could not be parsed.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_register_put()</code></dl>
<h3>int globus_gass_transfer_register_append (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_tlength, globus_gass_transfer_callback_tcallback, void *user_arg)</h3>
<p> Nonblocking file append. </p>
<p> This function initiates a new &#8216;append&#8217; request of the file named by <i>url</i>. The entire file will be transferred to the server if the user is authorized to do so. This function does not block; instead, the user&#8217;s callback function will be called once the GASS library has determined whether the file may be stored or not. </p>
<p> Upon returning from this function, the request handle is initialized to refer to the <i>append</i> request&#8217;s state. </p>
<p> If the server can&#8217;t store the file at <i>url</i>, but has an alternative location for the user to store to, then the callback function will be called with the request&#8217;s status set to <i>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A pointer to an uninitialized request handle.<br />
 <i>attr</i> Request attributes.<br />
 <i>url</i> URL to append to.<br />
 <i>length</i> The length of the data to append to the url, if known. If this parameter is set to <i>GLOBUS_GASS_LENGTH_UNKNOWN</i>, then the append may fail if the protocol does not support arbitrarily-length files.<br />
 <i>callback</i> Function to call once the URL has been accepted, referred, or denied by the server.<br />
 <i>user_arg</i> User-supplied argument to the callback function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The put was successfully initiated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> One of request, attr, or callback was GLOBUS_NULL. The put could not be processed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR</i> An internal resource was not available to process the put.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> No protocol handler for doing a append on this URL type is implemented.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_BAD_URL</i> The URL could not be parsed.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_append()</code></dl>
<h3>int globus_gass_transfer_register_get (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_gass_transfer_callback_tcallback, void *user_arg)</h3>
<p> Nonblocking file get. </p>
<p> This function initiates a new &#8216;get&#8217; request of the file named by <i>url</i>. The entire file will be transferred from the server if the file exists and user is authorized to do so. This function does not block; instead, the user&#8217;s callback function will be called once the GASS library has determined whether the file can be retrieved or not. </p>
<p> Upon returning from this function, the request handle is initialized to refer to the <i>get</i> request&#8217;s state. </p>
<p> If the server can&#8217;t store the file at <i>url</i>, but has an alternative location for the user to store to, then the callback function will be called with the request&#8217;s status set to <i>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A pointer to an uninitialized request handle.<br />
 <i>attr</i> Request attributes.<br />
 <i>url</i> URL to get<br />
 <i>callback</i> Function to call once the URL has been accepted, referred, or denied by the server.<br />
 <i>user_arg</i> User-supplied argument to the callback function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The get was successfully initiated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> One of request, attr, or callback was GLOBUS_NULL. The get could not be processed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR</i> An internal resource was not available to process the get.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> No protocol handler for doing a get on this URL type is implemented.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_BAD_URL</i> The URL could not be parsed.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_get()</code></dl>
<h3>int globus_gass_transfer_register_put (<code>globus_gass_transfer_request_t</code> *request, globus_gass_transfer_requestattr_t *attr, char *url, globus_size_tlength, globus_gass_transfer_callback_tcallback, void *user_arg)</h3>
<p> Nonblocking file put. </p>
<p> This function initiates a new &#8216;put&#8217; request of the file named by <i>url</i>. The entire file will be transferred to the server if the user is authorized to do so. This function does not block; instead, the user&#8217;s callback function will be called once the GASS library has determined whether the file may be stored or not. </p>
<p> Upon returning from this function, the request handle is initialized to refer to the <i>put</i> request&#8217;s state. </p>
<p> If the server can&#8217;t store the file at <i>url</i>, but has an alternative location for the user to store to, then the callback function will be called with the request&#8217;s status set to <i>GLOBUS_GASS_TRANSFER_REQUEST_REFERRED</i>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>request</i> A pointer to an uninitialized request handle.<br />
 <i>attr</i> Request attributes.<br />
 <i>url</i> URL to put.<br />
 <i>length</i> The length of the data to put to the url, if known. If this parameter is set to <i>GLOBUS_GASS_LENGTH_UNKNOWN</i>, then the put may fail if the protocol does not support arbitrarily-length files.<br />
 <i>callback</i> Function to call once the URL has been accepted, referred, or denied by the server.<br />
 <i>user_arg</i> User-supplied argument to the callback function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> The put was successfully initiated.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NULL_POINTER</i> One of request, attr, or callback was GLOBUS_NULL. The put could not be processed.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_INTERNAL_ERROR</i> An internal resource was not available to process the put.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_NOT_IMPLEMENTED</i> No protocol handler for doing a put on this URL type is implemented.<br />
 <i>GLOBUS_GASS_TRANSFER_ERROR_BAD_URL</i> The URL could not be parsed.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gass_transfer_put()</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
