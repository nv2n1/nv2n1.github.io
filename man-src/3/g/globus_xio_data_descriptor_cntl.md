---
title: "globus_xio_data_descriptor_cntl(3)"
name: "globus_xio_data_descriptor_cntl"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_data_descriptor_cntl/"
description: "builtins/http/globus_xio_http.h –"
---

<h2 class="name">NAME</h2>
<p> builtins/http/globus_xio_http.h &#8211; </p>
<p> Globus XIO HTTP Driver Header.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_xio.h&#8217; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_xio_http_header_t</code><br />
 <i>HTTP Header. </i></p>
<h3>Enumerations</h3>
<p> enum <code>globus_xio_http_handle_cmd_t</code> { <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HEADER</code>, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_STATUS_CODE</code>, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_REASON_PHRASE</code>, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HTTP_VERSION</code>, <code>GLOBUS_XIO_HTTP_HANDLE_SET_END_OF_ENTITY</code> } </p>
<p> enum <code>globus_xio_http_attr_cmd_t</code> { <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_METHOD</code>, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HTTP_VERSION</code>, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HEADER</code>, <code>GLOBUS_XIO_HTTP_ATTR_DELAY_WRITE_HEADER</code>, <code>GLOBUS_XIO_HTTP_GET_REQUEST</code>, <code>GLOBUS_XIO_HTTP_GET_RESPONSE</code> } </p>
<p> enum <code>globus_xio_http_errors_t</code> { <code>GLOBUS_XIO_HTTP_ERROR_INVALID_HEADER</code>, <code>GLOBUS_XIO_HTTP_ERROR_PARSE</code>, <code>GLOBUS_XIO_HTTP_ERROR_NO_ENTITY</code>, <code>GLOBUS_XIO_HTTP_ERROR_EOF</code>, <code>GLOBUS_XIO_HTTP_ERROR_PERSISTENT_CONNECTION_DROPPED</code> } </p>
<p> enum <code>globus_xio_http_version_t</code> { , <code>GLOBUS_XIO_HTTP_VERSION_1_0</code>, <code>GLOBUS_XIO_HTTP_VERSION_1_1</code> } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HEADER</code>, const char *header_name, const char *header_value) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_STATUS_CODE</code>, int status) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_REASON_PHRASE</code>, const char *reason) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_RESPONSE_HTTP_VERSION</code>, <code>globus_xio_http_version_t</code> version) </p>
<p> globus_result_t <code>globus_xio_handle_cntl</code> (handle, driver, <code>GLOBUS_XIO_HTTP_HANDLE_SET_END_OF_ENTITY</code>) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_METHOD</code>, const char *method) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HTTP_VERSION</code>, <code>globus_xio_http_version_t</code> version) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_SET_REQUEST_HEADER</code>, const char *header_name, const char *header_value) </p>
<p> globus_result_t <code>globus_xio_attr_cntl</code> (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_DELAY_WRITE_HEADER</code>) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_HTTP_GET_REQUEST</code>, char **method, char **uri, <code>globus_xio_http_version_t</code> *http_version, globus_hashtable_t *headers) </p>
<p> globus_result_t <code>globus_xio_data_descriptor_cntl</code> (dd, driver, <code>GLOBUS_XIO_HTTP_GET_RESPONSE</code>, int *status_code, char **reason_phrase, <code>globus_xio_http_version_t</code> *http_version, globus_hashtable_t *headers) </p>
<h2>Detailed Description</h2>
<p> Globus XIO HTTP Driver Header. </p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_xio_attr_cntl (attr, driver, <code>GLOBUS_XIO_HTTP_ATTR_DELAY_WRITE_HEADER</code>)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Delay writing HTTP request until first data write. </p>
<p> If this attribute is present when opening an HTTP handle, the HTTP request will not be sent immediately upon opening the handle. Instead, it will be delayed until the first data write is done. This allows other HTTP headers to be sent after the handle is opened. </p>
<p> This attribute cntl takes no arguments.</p>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, <code>GLOBUS_XIO_HTTP_GET_REQUEST</code>, char **method, char **uri, <code>globus_xio_http_version_t</code> *http_version, globus_hashtable_t *headers)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get HTTP Request Information. </p>
<p> Returns in the passed parameters values concerning the HTTP request. Any of the parameters may be NULL if the application is not interested in that part of the information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>method</i> Pointer to be set to the HTTP request method (typically GET, PUT, or POST). The caller must not access this value outside of the lifetime of the data descriptor nor free it.<br />
 <i>uri</i> Pointer to be set to the requested HTTP path. The caller must not access this value outside of the lifetime of the data descriptor nor free it.<br />
 <i>http_version</i> Pointer to be set to the HTTP version used for this request.<br />
 <i>headers</i> Pointer to be set to point to a hashtable of <code>globus_xio_http_header_t</code> values, keyed by the HTTP header names. The caller must not access this value outside of the lifetime of the data descriptor nor free it or any values in it.</dl>
<h3>globus_result_t globus_xio_data_descriptor_cntl (dd, driver, <code>GLOBUS_XIO_HTTP_GET_RESPONSE</code>, int *status_code, char **reason_phrase, <code>globus_xio_http_version_t</code> *http_version, globus_hashtable_t *headers)</h3>
<p> This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts. Get HTTP Response Information </p>
<p> Returns in the passed parameters values concerning the HTTP response. Any of the parameters may be NULL if the application is not interested in that part of the information. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>status_code</i> Pointer to be set to the HTTP response status code (such as 404), as per RFC 2616. The caller must not access this value outside of the lifetime of the data descriptor nor free it or any values in it.<br />
 <i>reason_phrase</i> Pointer to be set to the HTTP response reason phrase (such as Not Found). The caller must not access this value outside of the lifetime of the data descriptor nor free it or any values in it.<br />
 <i>http_version</i> Pointer to be set to the HTTP version used for this request.<br />
 <i>headers</i> Pointer to be set to point to a hashtable of <code>globus_xio_http_header_t</code> values, keyed by the HTTP header names. The caller must not access this value outside of the lifetime of the data descriptor nor free it or any values in it.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
