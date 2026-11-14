---
title: "globus_gsi_cred_handle_attrs_copy(3)"
name: "globus_gsi_cred_handle_attrs_copy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_cred_handle_attrs_copy/"
description: "Credential Handle Attributes –"
---

<h2 class="name">NAME</h2>
<p> Credential Handle Attributes &#8211; </p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_l_gsi_cred_handle_attrs_s * <code>globus_gsi_cred_handle_attrs_t</code>&quot; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_cred_handle_attrs_init</code> (<code>globus_gsi_cred_handle_attrs_t</code> *handle_attrs)<br />
 <i>Initialize credential handle attributes. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_destroy</code> (<code>globus_gsi_cred_handle_attrs_t</code> handle_attrs)<br />
 <i>Destroy credential handle attributes. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_copy</code> (<code>globus_gsi_cred_handle_attrs_t</code> source, <code>globus_gsi_cred_handle_attrs_t</code> *dest)<br />
 <i>Copy credential handle attributes. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_set_ca_cert_dir</code> (<code>globus_gsi_cred_handle_attrs_t</code> handle_attrs, const char *ca_cert_dir)<br />
 <i>Set the CA certificate directory. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_get_ca_cert_dir</code> (<code>globus_gsi_cred_handle_attrs_t</code> handle_attrs, char **ca_cert_dir)<br />
 <i>Get the CA certificate directory. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_set_search_order</code> (<code>globus_gsi_cred_handle_attrs_t</code> handle_attrs, <code>globus_gsi_cred_type_t</code> search_order[])<br />
 <i>Set the search order. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_attrs_get_search_order</code> (<code>globus_gsi_cred_handle_attrs_t</code> handle_attrs, <code>globus_gsi_cred_type_t</code> **search_order)<br />
 <i>Get the search order. </i></p>
<h2>Detailed Description</h2>
<p> Create/Destroy/Modify GSI Credential Handle Attributes. </p>
<p> Within the Globus GSI Credential Library, all credential handles contain a attribute structure, which in turn contains handle instance independent attributes. </p>
<p> This section defines operations to create, modify and destroy GSI Credential handle attributes.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_l_gsi_cred_handle_attrs_s* <code>globus_gsi_cred_handle_attrs_t</code></h3>
<p> Credential Handle Attributes. </p>
<p> Credential handle attributes provide a set of immutable parameters for a credential handle </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_cred_handle_init</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_cred_handle_attrs_copy (<code>globus_gsi_cred_handle_attrs_t</code>source, <code>globus_gsi_cred_handle_attrs_t</code> *dest)</h3>
<p> Copy credential handle attributes. Copy the Credential Handle Attributes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>source</i> The handle attribute to be copied<br />
 <i>dest</i> The copy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCESS unless there was an error, in which case an error object is returned.</dl>
<h3>globus_result_t globus_gsi_cred_handle_attrs_destroy (<code>globus_gsi_cred_handle_attrs_t</code>handle_attrs)</h3>
<p> Destroy credential handle attributes. Destroy the Credential Handle Attributes. This function does some cleanup and deallocation of the handle attributes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The handle attributes to destroy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_cred_handle_attrs_get_ca_cert_dir (<code>globus_gsi_cred_handle_attrs_t</code>handle_attrs, char **ca_cert_dir)</h3>
<p> Get the CA certificate directory. Get the trusted CA certificate directory </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> the credential handle attributes to get the trusted ca cert directory from<br />
 <i>ca_cert_dir</i> the trusted ca certificates directory</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no errors occurred. In case of a null handle_attrs or pointer to ca_cert_dir, an error object id is returned</dl>
<h3>globus_result_t globus_gsi_cred_handle_attrs_get_search_order (<code>globus_gsi_cred_handle_attrs_t</code>handle_attrs, <code>globus_gsi_cred_type_t</code> **search_order)</h3>
<p> Get the search order. Get the search order of the handle attributes </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The handle attributes to get the search order from<br />
 <i>search_order</i> The search_order of the handle attributes</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless handle_attrs is null</dl>
<h3>globus_result_t globus_gsi_cred_handle_attrs_init (<code>globus_gsi_cred_handle_attrs_t</code> *handle_attrs)</h3>
<p> Initialize credential handle attributes. Initializes the immutable Credential Handle Attributes The handle attributes are initialized as follows: </p>
<dl>
<dt>&bull;</p>
<dd> The search order is set to SERVICE, HOST, PROXY, USER</p>
<dt>&bull;</p>
<dd> All other attributes are set to 0/NULL</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> the attributes to be initialized</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if initialization was successful, otherwise an error is returned</dl>
<h3>globus_result_t globus_gsi_cred_handle_attrs_set_ca_cert_dir (<code>globus_gsi_cred_handle_attrs_t</code>handle_attrs, const char *ca_cert_dir)</h3>
<p> Set the CA certificate directory. Set the Trusted CA Certificate Directory Location </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> the credential handle attributes to set<br />
 <i>ca_cert_dir</i> the trusted ca certificates directory</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no errors occurred. In case of a null handle_attrs, an error object id is returned</dl>
<h3>globus_result_t globus_gsi_cred_handle_attrs_set_search_order (<code>globus_gsi_cred_handle_attrs_t</code>handle_attrs, <code>globus_gsi_cred_type_t</code>search_order[])</h3>
<p> Set the search order. Set the search order for finding a user certificate. The default value is {SERVICE, HOST, PROXY, USER} </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The handle attributes to set the search order of<br />
 <i>search_order</i> The search order. Should be a three element array containing in some order PROXY, USER, HOST, SERVICE. The array should be terminated by the value GLOBUS_SO_END.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless handle_attrs is null</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_credential from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAP">Author</a></p>
<dd></dl>
