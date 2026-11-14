---
title: "globus_rls_client_connection(3)"
name: "globus_rls_client_connection"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_client_connection/"
description: "Connection Management –"
---

<h2 class="name">NAME</h2>
<p> Connection Management &#8211; </p>
<p> Functions to open and close connections to an RLS server.</p>
<h3>Defines</h3>
<p> #define <code>GLOBUS_RLS_URL_SCHEME</code> &#8216;rls&#8217; </p>
<p> #define <code>GLOBUS_RLS_URL_SCHEME_NOAUTH</code> &#8216;rlsn&#8217; </p>
<p> #define <code>GLOBUS_RLS_SERVER_DEFPORT</code> 39281 </p>
<p> #define <code>MAXERRMSG</code> 1024 </p>
<h3>Functions</h3>
<p> void <code>globus_rls_client_certificate</code> (char *certfile, char *keyfile) </p>
<p> void <code>globus_rls_client_proxy_certificate</code> (char *proxy) </p>
<p> globus_result_t <code>globus_rls_client_connect</code> (char *url, <code>globus_rls_handle_t</code> **h) </p>
<p> globus_result_t <code>globus_rls_client_close</code> (<code>globus_rls_handle_t</code> *h) </p>
<p> int <code>globus_rls_client_get_timeout</code> () </p>
<p> void <code>globus_rls_client_set_timeout</code> (int seconds) </p>
<h2>Detailed Description</h2>
<p> Functions to open and close connections to an RLS server.</p>
<h2>Define Documentation</h2>
<h3>#define GLOBUS_RLS_URL_SCHEME &#8216;rls&#8217;</h3>
<p> URL scheme to use when connecting to RLS server.</p>
<h3>#define GLOBUS_RLS_URL_SCHEME_NOAUTH &#8216;rlsn&#8217;</h3>
<p> URL scheme when connecting to RLS server without authentication.</p>
<h3>#define GLOBUS_RLS_SERVER_DEFPORT 39281</h3>
<p> Default port number that RLS server listens on.</p>
<h3>#define MAXERRMSG 1024</h3>
<p> Maximum length of error messages returned by server.</p>
<h2>Function Documentation</h2>
<h3>void globus_rls_client_certificate (char * certfile, char * keyfile)</h3>
<p> Set certificate used in authentication. Sets environment variables X509_USER_CERT, X509_USER_KEY, and clears X509_USER_PROXY. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>certfile</i> Name of X509 certificate file.<br />
 <i>keyfile</i> Name of X509 key file.</dl>
<h3>void globus_rls_client_proxy_certificate (char * proxy)</h3>
<p> Set X509_USER_PROXY environment variable to specified file. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>proxy</i> Name of X509 proxy certificate file. If NULL clears X509_USER_PROXY.</dl>
<h3>globus_result_t globus_rls_client_connect (char * url, <code>globus_rls_handle_t</code> ** h)</h3>
<p> Open connection to RLS server. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>url</i> URL of server to connect to. URL scheme should be <code>RLS</code> or <code>RLSN</code>, eg <code>RLS://my.host</code>. If the URL scheme is <code>RLSN</code> then no authentication is performed (the RLS server must be started with authentication disabled as well, this option is primarily intended for testing).<br />
 <i>h</i> If the connection is successful <i>*h</i> will be set to the connection handle. This handle is required by all other functions in the API.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Handle <i>h</i> now connected to RLS server identified by <i>url</i>.</dl>
<h3>globus_result_t globus_rls_client_close (<code>globus_rls_handle_t</code> * h)</h3>
<p> Close connection to RLS server. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Connection handle to be closed, previously allocated by <code>globus_rls_client_connect()</code>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Connection closed, <i>h</i> is no longer valid.</dl>
<h3>int globus_rls_client_get_timeout ()</h3>
<p> Get timeout for IO calls to RLS server. If 0 IO calls do not timeout. The default is 30 seconds. </p>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>timeout</i> Seconds to wait before timing out an IO operation.</dl>
<h3>void globus_rls_client_set_timeout (int seconds)</h3>
<p> Set timeout for IO calls to RLS server. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>seconds</i> Seconds to wait before timing out an IO operation. If 0 IO calls do not timeout. The default is 30 seconds.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAR">Author</a></p>
<dd></dl>
