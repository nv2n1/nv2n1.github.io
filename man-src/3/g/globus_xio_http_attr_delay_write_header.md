---
title: "globus_xio_http_attr_delay_write_header(3)"
name: "globus_xio_http_attr_delay_write_header"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_http_attr_delay_write_header/"
description: "Attributes and Cntls –"
---

<p>Attributes and Cntls &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_http_handle_cmd_t</code> { <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HEADER</code>, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_STATUS_CODE</code>, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_REASON_PHRASE</code>, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HTTP_VERSION</code>, <code>GLOBUS_XIO_HTTP_HANDLE_SET_END_OF_ENTITY</code> } </p>
<p> enum <code>globus_xio_http_attr_cmd_t</code> { <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_METHOD</code>, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HTTP_VERSION</code>, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HEADER</code>, <code>GLOBUS_XIO_HTTP_ATTR_DELAY_WRITE_HEADER</code>, <code>GLOBUS_XIO_HTTP_GET_REQUEST</code>, <code>GLOBUS_XIO_HTTP_GET_RESPONSE</code> } </p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HEADER</code>, const char *header_name, const char *header_value) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_STATUS_CODE</code>, int status) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_REASON_PHRASE</code>, const char *reason) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HTTP_VERSION</code>, <code>globus_xio_http_version_t</code> version) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_END_OF_ENTITY</code>) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_METHOD</code>, const char *method) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HTTP_VERSION</code>, <code>globus_xio_http_version_t</code> version) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HEADER</code>, const char *header_name, const char *header_value) </p>
<h2>Detailed Description</h2>
<p>HTTP driver specific attrs and cntls. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>globus_xio_attr_cntl()</code> </p>
<p> <code>globus_xio_handle_cntl()</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_http_attr_cmd_t</code></h3>
<p>HTTP driver specific attribute and data descriptor cntls </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_METHOD </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HTTP_VERSION </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HEADER </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_ATTR_DELAY_WRITE_HEADER </i></p>
<dd>See usage for: <code>globus_xio_attr_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_GET_REQUEST </i></p>
<dd>See usage for: <code>globus_xio_data_descriptor_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_GET_RESPONSE </i></p>
<dd>See usage for: <code>globus_xio_data_descriptor_cntl </code></dl>
<h3>enum <code>globus_xio_http_handle_cmd_t</code></h3>
<p>HTTP driver specific cntls </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HEADER </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_STATUS_CODE </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_REASON_PHRASE </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HTTP_VERSION </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code></p>
<dt><i>GLOBUS_XIO_HTTP_HANDLE_SET_END_OF_ENTITY </i></p>
<dd>See usage for: <code>globus_xio_handle_cntl </code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_METHOD</code>, const char *method)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the HTTP method to use for a client request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>method</i> The request method string (&#8216;GET&#8217;, &#8216;PUT&#8217;, &#8216;POST&#8217;, etc) that will be used in the HTTP request.</dl>
<p> If this is not set on the target before it is opened, it will default to GET. </p>
<p> This attribute is ignored when opening the server side of an HTTP connection. </p>
<p> Setting this attribute may fail with</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_MEMORY</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_PARAMETER</dl>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HTTP_VERSION</code>, <code>globus_xio_http_version_t</code>version)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the HTTP version to use for a client request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>version</i> The HTTP version to use for the client request.</dl>
<p> If the client is using HTTP/1.0 in a request which will send a request message body (such as a POST or PUT), then the client MUST set the &#8216;Content-Length&#8217; HTTP header to be the length of the message. If this attribute is not present, then the default of GLOBUS_XIO_HTTP_VERSION_1_1 will be used. </p>
<p> This attribute is ignored when opening the server side of an HTTP connection.</p>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HEADER</code>, const char *header_name, const char *header_value)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the value of an HTTP request header. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>header_name</i> Name of the HTTP header to set.<br />
 <i>header_value</i> Value of the HTTP header</dl>
<p> Certain headers will cause the HTTP driver to behave differently than normal. This must be called before </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Transfer-Encoding: {identity|chunked} Override the default transfer encoding. If a server knows the exact length of the message body, or does not intend to support persistent connections, it may set this header to be &#8216;identity&#8217;. </p>
<p>&nbsp;<wbr>If this is set to&nbsp;<wbr>&#8216;identity&#8217;&nbsp;<wbr>and any of the following are true, then the connection will be closed after the end of the message is sent:&nbsp;<wbr> </p>
<dt> &bull;</p>
<dd>A Content-Length header is not present</p>
<dt> &bull;</p>
<dd>The HTTP version is set to &#8216;HTTP/1.0&#8217;</p>
<dt> &bull;</p>
<dd>The Connection header is set to &#8216;close&#8217; Attempts to set this to &#8216;chunked&#8217; with an &#8216;HTTP/1.0&#8217; client will fail with a GLOBUS_XIO_ERROR_HTTP_INVALID_HEADER error.</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Content-Length: 1*Digit</p>
<dt> &bull;</p>
<dd>Provide a content length for the response message. If the &#8216;chunked&#8217; transfer encoding is being used, then this header will be silently ignored by the HTTP driver.</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Connection: close</p>
<dt> &bull;</p>
<dd>If present in the server response, the connection will be closed after the end of the data response is written. Otherwise, when persistent connections are enabled, the connection <i>may</i> be left open by the driver. Persistent connections are not yet implemented.</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HEADER</code>, const char *header_name, const char *header_value)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the value of a response HTTP header. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>header_name</i> Name of the HTTP header to set.<br />
 <i>header_value</i> Value of the HTTP header</dl>
<p> Certain headers will cause changes in how the HTTP protocol will be handled. These include:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Transfer-Encoding: {identity|chunked} Override the default transfer encoding. If a server knows the exact length of the message body, or does not intend to support persistent connections, it may set this header to be &#8216;identity&#8217;. </p>
<p>&nbsp;<wbr>If this is set to&nbsp;<wbr>&#8216;identity&#8217;&nbsp;<wbr>and any of the following are true, then the connection will be closed after the end of the response is sent:&nbsp;<wbr> </p>
<dt> &bull;</p>
<dd>A Content-Length header is not present</p>
<dt> &bull;</p>
<dd>The HTTP version is set to &#8216;HTTP/1.0&#8217;</p>
<dt> &bull;</p>
<dd>The Connection header is set to &#8216;close&#8217; Attempts to set this to &#8216;chunked&#8217; with an &#8216;HTTP/1.0&#8217; client will fail with a GLOBUS_XIO_ERROR_HTTP_INVALID_HEADER error.</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Content-Length: 1*Digit</p>
<dt> &bull;</p>
<dd>Provide a content length for the response message. If the &#8216;chunked&#8217; transfer encoding is being used, then this header will be silently ignored by the HTTP driver.</dl>
<dl COMPACT>
<dt>&bull;</p>
<dd>Connection: close</p>
<dt> &bull;</p>
<dd>The HTTP connection will be closed after the end of the data response is written.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This handle control function can fail with</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_MEMORY</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_PARAMETER</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_HTTP_INVALID_HEADER</dl>
</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_STATUS_CODE</code>, intstatus)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the response status code. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>status</i> Value in the range 100-599 which will be used as the HTTP response code, as per RFC 2616.</dl>
<p> If this cntl is not called by a server, then the default value of 200 (&#8216;Ok&#8217;) will be used. If this is called on the client-side of an HTTP connection, the handle control will fail with a GLOBUS_XIO_ERROR_PARAMETER error. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This handle control function can fail with</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_PARAMETER</dl>
</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_REASON_PHRASE</code>, const char *reason)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the response reason phrase. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>reason</i> The value of the HTTP response string, as per RFC 2616.</dl>
<p> If this cntl is not called by a server, then a default value based on the handle&#8217;s response status code will be generated. If this is called on the client-side of an HTTP connection, the handle control will fail with a GLOBUS_XIO_ERROR_PARAMETER error. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This handle control function can fail with</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_MEMORY</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_PARAMETER</dl>
</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HTTP_VERSION</code>, <code>globus_xio_http_version_t</code>version)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Set the response HTTP version. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>version</i> The HTTP version to be used in the server response line.</dl>
<p> If this cntl is not called by a server, then the default of GLOBUS_XIO_HTTP_VERSION_1_1 will be used, though no HTTP/1.1 features (chunking, persistent connections, etc) will be assumed if the client request was an HTTP/1.0 request. If this is called on the client-side of an HTTP connection, the handle control will fail with GLOBUS_XIO_ERROR_PARAMETER. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>This handle control function can fail with</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_MEMORY</p>
<dt>&bull;</p>
<dd>GLOBUS_XIO_ERROR_PARAMETER</dl>
</dl>
<h3>globus_result_t globus_xio_handle_cntl (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_END_OF_ENTITY</code>)</h3>
<p>This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Indicate end-of-entity for an HTTP body. </p>
<p> HTTP clients and servers must call this command to indicate to the driver that the entity-body which is being sent is completed. Subsequent attempts to write data on the handle will fail. </p>
<p> This handle command MUST be called on the client side of an HTTP connection when the HTTP method is OPTIONS, POST, or PUT, or when the open attributes indicate that an entity will be sent. This handle command MUST be called on the server side of an HTTP request connection when the HTTP method was OPTIONS, GET, POST, or TRACE.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
