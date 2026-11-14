---
title: "globus_gram_client_attr_get_delegation_mode(3)"
name: "globus_gram_client_attr_get_delegation_mode"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gram_client_attr_get_delegation_mode/"
description: "GRAM Client Attribute Functions –"
---

<h2 class="name">NAME</h2>
<p> GRAM Client Attribute Functions &#8211; </p>
<h3>Macros</h3>
<p> #define <code>GLOBUS_GRAM_CLIENT_NO_ATTR</code><br />
 <i>Default GRAM client operation attribute. </i></p>
<h3>Typedefs</h3>
<p> typedef void * <code>globus_gram_client_attr_t</code><br />
 <i>GRAM client operation attribute. </i></p>
<h3>Functions</h3>
<p> int <code>globus_gram_client_attr_init</code> (<code>globus_gram_client_attr_t</code> *attr)<br />
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
 <i>Get a GRAM client attribute&#8217;s security credential. </i></p>
<h2>Detailed Description</h2>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_GRAM_CLIENT_NO_ATTR</h3>
<p> Default GRAM client operation attribute. The GLOBUS_GRAM_CLIENT_NO_ATTR macro defines a constant for use when a user of the GRAM client API does not want to specify any non-default GRAM attributes.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void* <code>globus_gram_client_attr_t</code></h3>
<p> GRAM client operation attribute. The <code>globus_gram_client_attr_t</code> type is an opaque type describing GRAM attributes. It can be accessed or modified by functions in the <code>GRAM Client Attribute Functions</code> documentation.</p>
<h2>Function Documentation</h2>
<h3>int globus_gram_client_attr_destroy (<code>globus_gram_client_attr_t</code> *attr)</h3>
<p> Destroy a GRAM client attribute. The <code>globus_gram_client_attr_destroy()</code> function destroys and frees a GRAM client attribute. After this function returns, the value pointed to by <i>attr</i> is no longer valid and must not be used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> A pointer to the attribute to destroy. All data associated with the attribute will be freed and it will be an invalid attribute.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_attr_destroy()</code> destroys the attribute pointed to by the <i>attr</i> parameter and sets it to an invalid state. If an error occurs, <code>globus_gram_client_attr_destroy()</code> returns an integer error code and value of <i>attr</i> is unchanged.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_ATTR</i> Invalid attribute</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_attr_init()</code></dl>
<h3>int globus_gram_client_attr_get_credential (<code>globus_gram_client_attr_t</code>attr, gss_cred_id_t *credential)</h3>
<p> Get a GRAM client attribute&#8217;s security credential. The <code>globus_gram_client_attr_get_credential()</code> function gets the value of the <code>credential</code> in an attribute and modifies the <i>credential</i> parameter to point to it. This is a shallow copy. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query for its <i>credential</i>.<br />
 <i>credential</i> An output parameter that will be initialized to point to the GSSAPI credential which the <i>attr</i> is currently using.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_attr_get_credential()</code> modifies the the value pointed to by the <i>credential</i> parameter to be the same credential as that being used by the attribute named by the <i>attr</i> parameter and returns <i>GLOBUS_SUCCESS</i>. If an error occurs, <code>globus_gram_client_attr_get_credential()</code> returns an integer error code and the value pointed to by the <i>credential</i> parameter is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_ATTR</i> Invalid attribute<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_attr_set_credential()</code></dl>
<h3>int globus_gram_client_attr_get_delegation_mode (<code>globus_gram_client_attr_t</code>attr, globus_io_secure_delegation_mode_t *mode)</h3>
<p> Get a GRAM client attribute&#8217;s security credential. The <code>globus_gram_client_attr_get_delegation_mode()</code> function gets the value of the <code>delegation_mode</code> in an attribute and modifies the <i>mode</i> parameter to point to its value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to query for its <i>delegation_mode</i>.<br />
 <i>mode</i> An output parameter that will be set to point to the delegation mode which the <i>attr</i> is currently using.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_attr_get_delegation_mode()</code> modifies the the value pointed to by the <i>mode</i> parameter as described above and returns <i>GLOBUS_SUCCESS</i>. If an error occurs, <code>globus_gram_client_attr_get_delegation_mode()</code> returns an integer error code and the value pointed to by the <i>mode</i> parameter is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_ATTR</i> Invalid attribute<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_NULL_PARAMETER</i> Null parameter</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_attr_get_delegation_mode()</code></dl>
<h3>int globus_gram_client_attr_init (<code>globus_gram_client_attr_t</code> *attr)</h3>
<p> Initialize a GRAM client attribute. The <code>globus_gram_client_attr_init()</code> function creates a new opaque structure that can be used to specify custom attributes for performing GRAM client operations. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> An output parameter which will be set to the newly initialized attribute.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_attr_init()</code> modifies the <i>attr</i> parameter to point to a new GRAM client attribute and returns <i>GLOBUS_SUCCESS</i>. If an error occurs, <code>globus_gram_client_attr_init()</code> returns an integer error code and value of <i>attr</i> is undefined.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_ATTR</i> Invalid attribute<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_MALLOC_FAILED</i> Out of memory</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_attr_destroy()</code></dl>
<h3>int globus_gram_client_attr_set_credential (<code>globus_gram_client_attr_t</code>attr, gss_cred_id_tcredential)</h3>
<p> Set a GRAM client attribute&#8217;s security credential. The <code>globus_gram_client_attr_set_credential()</code> function sets the value of the <code>credential</code> in an attribute to the GSSAPI credential named by the <i>credential</i> parameter. This is done as a shallow copy, so the value of <i>credential</i> must not be freed until the attribute will no longer be used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to modify to use the credential named by the <i>credential</i> parameter.<br />
 <i>credential</i> The GSSAPI credential to use with the attribute named by the <i>attr</i> parameter. This may be <i>GSS_C_NO_CREDENTIAL</i> to set the attribute to use the default security credential.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_attr_set_credential()</code> modifies the the attribute pointed to by the <i>attr</i> parameter to use the credential specified by the <i>credential</i> parameter and returns <i>GLOBUS_SUCCESS</i>. If an error occurs, <code>globus_gram_client_attr_set_credential()</code> returns an integer error code and the attribute named by <i>attr</i> is unchanged.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_ATTR</i> An invalid attribute set was passed to this function.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_attr_get_credential()</code></dl>
<h3>int globus_gram_client_attr_set_delegation_mode (<code>globus_gram_client_attr_t</code>attr, globus_io_secure_delegation_mode_tmode)</h3>
<p> Set a GRAM client attribute&#8217;s delegation mode. The <code>globus_gram_client_attr_set_delegation_mode()</code> function sets the value of the <code>delegation_mode</code> in an attribute to the delegation mode in the <i>mode</i> parameter. </p>
<p> The GRAM client supports the following delegation modes:</p>
<dl>
<dt>&bull;</p>
<dd> <code>GLOBUS_IO_SECURE_DELEGATION_MODE_LIMITED_PROXY</code></p>
<dt>&bull;</p>
<dd> <code>GLOBUS_IO_SECURE_DELEGATION_MODE_FULL_PROXY</code></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> The attribute set to modify to use the delegation mode in the <i>mode</i> parameter.<br />
 <i>mode</i> The new value of the delegation mode.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_gram_client_attr_set_delegation_mode()</code> modifies the the attribute named by the <i>attr</i> parameter to use the delegation mode in the <i>mode</i> parameter and returns GLOBUS_SUCCESS. If an error occurs, <code>globus_gram_client_attr_set_delegation_mode()</code> returns an integer error code and the <i>delegation_mode</i> attribute value is unchanged.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_GRAM_PROTOCOL_ERROR_INVALID_ATTR</i> Invalid attribute</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gram_client_attr_get_delegation_mode()</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gram_client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Function Documentation</a></p>
<dd>
<dt><a href="#lbAR">Author</a></p>
<dd></dl>
