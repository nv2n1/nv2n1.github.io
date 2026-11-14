---
title: "globus_gsi_proxy_handle_attrs_init(3)"
name: "globus_gsi_proxy_handle_attrs_init"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_proxy_handle_attrs_init/"
description: "Handle Attributes –"
---

<h2 class="name">NAME</h2>
<p> Handle Attributes &#8211; </p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_l_gsi_proxy_handle_attrs_s * <code>globus_gsi_proxy_handle_attrs_t</code>&quot;<br />
 <i>Handle Attributes. </i></p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_proxy_handle_attrs_init</code> (<code>globus_gsi_proxy_handle_attrs_t</code> *handle_attrs)<br />
 <i>Initialize Attributes. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_destroy</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs)<br />
 <i>Destroy attributes. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_keybits</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int bits)<br />
 <i>Set Key Bits. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_keybits</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int *bits)<br />
 <i>Get Key Bits. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_init_prime</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int prime)<br />
 <i>Set Initial Prime Number. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_init_prime</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int *prime)<br />
 <i>Get Initial Prime Number. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_signing_algorithm</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, const EVP_MD *algorithm)<br />
 <i>Set Signing Algorithm. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_signing_algorithm</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, const EVP_MD **algorithm)<br />
 <i>Get Signing Algorithm. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_clock_skew_allowable</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int skew)<br />
 <i>Set Clock Skew Allowable. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_clock_skew_allowable</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, int *skew)<br />
 <i>Get Clock Skew Allowable. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_get_key_gen_callback</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, void(**callback)(int, int, void *))<br />
 <i>Get Key Gen Callback. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_set_key_gen_callback</code> (<code>globus_gsi_proxy_handle_attrs_t</code> handle_attrs, void(*callback)(int, int, void *))<br />
 <i>Set Key Gen Callback. </i><br />
 globus_result_t <code>globus_gsi_proxy_handle_attrs_copy</code> (<code>globus_gsi_proxy_handle_attrs_t</code> a, <code>globus_gsi_proxy_handle_attrs_t</code> *b)<br />
 <i>Copy Attributes. </i></p>
<h2>Detailed Description</h2>
<p> Handle attributes are used to control additional features of the GSI Proxy handle. These features are operation independent. </p>
<p> Currently there are no attributes. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_t</code></dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_l_gsi_proxy_handle_attrs_s* <code>globus_gsi_proxy_handle_attrs_t</code></h3>
<p> Handle Attributes. A GSI Proxy handle attributes type is used to associate immutable parameter values with a <code>Handle Management</code> handle. A handle attributes object should be created with immutable parameters and then passed to the proxy handle init function <code>globus_gsi_proxy_handle_init()</code>. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>Handle Management</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_copy (<code>globus_gsi_proxy_handle_attrs_t</code>a, <code>globus_gsi_proxy_handle_attrs_t</code> *b)</h3>
<p> Copy Attributes. Make a copy of GSI Proxy handle attributes </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>a</i> The handle attributes to copy<br />
 <i>b</i> The copy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_destroy (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs)</h3>
<p> Destroy attributes. Destroy the GSI Proxy handle attributes </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The handle attributes to be destroyed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_attrs_init()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_get_clock_skew_allowable (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, int *skew)</h3>
<p> Get Clock Skew Allowable. Get the allowable clock skew for the proxy certificate </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The handle_attrs to get the clock skew from<br />
 <i>skew</i> The allowable clock skew (in seconds) to get from the proxy certificate request. This value gets set by the function, so it needs to be a pointer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle_attrs is valid, otherwise an error is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_get_init_prime (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, int *prime)</h3>
<p> Get Initial Prime Number. Get the initial prime number used for generating the public key pair in the RSA algorithm </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The attributes to get the initial prime number from<br />
 <i>prime</i> The initial prime number taken from the attributes</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_get_key_gen_callback (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, void(**)(int, int, void *)callback)</h3>
<p> Get Key Gen Callback. Get the public/private key generation callback that provides status during the generation of the keys </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The handle_attrs to get the callback from<br />
 <i>callback</i> The callback from the handle attributes</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle_attrs is valid, otherwise an error is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_get_keybits (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, int *bits)</h3>
<p> Get Key Bits. Gets the length of the public key pair used by the proxy certificate </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> the attributes to get the key length from<br />
 <i>bits</i> the length of the key pair in bits</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_get_signing_algorithm (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, const EVP_MD **algorithm)</h3>
<p> Get Signing Algorithm. Gets the Signing Algorithm to used to sign the certificate request. In most cases, the signing party will ignore this value, and sign with an algorithm of its choice. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The proxy handle_attrs to get the signing algorithm of<br />
 <i>algorithm</i> Parameter used to return the signing algorithm used</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns GLOBUS_SUCCESS if the handle is valid, otherwise an error object is returned.</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_init (<code>globus_gsi_proxy_handle_attrs_t</code> *handle_attrs)</h3>
<p> Initialize Attributes. Initialize GSI Proxy Handle Attributes. </p>
<p> Initialize proxy handle attributes, which can (and should) be associated with a proxy handle. For most purposes, these attributes should primarily be used by the proxy handle. </p>
<p> Currently, no attribute values are initialized. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The handle attributes structure to be initialized</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS unless an error occurred, in which case, a globus error object ID is returned</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_proxy_handle_attrs_destroy()</code></dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_set_clock_skew_allowable (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, intskew)</h3>
<p> Set Clock Skew Allowable. Sets the clock skew in minutes of the proxy cert request so that time differences between hosts won&#8217;t cause problems. This value defaults to 5 minutes. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> the handle_attrs containing the clock skew to be set<br />
 <i>skew</i> the amount to skew by (in seconds)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle_attrs is valid &#8211; otherwise an error is returned.</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_set_init_prime (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, intprime)</h3>
<p> Set Initial Prime Number. Set the initial prime number used for generating public key pairs in the RSA algorithm </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The attributes to set<br />
 <i>prime</i> The prime number to set it to This value needs to be a prime number</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_set_key_gen_callback (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, void(*)(int, int, void *)callback)</h3>
<p> Set Key Gen Callback. Set the public/private key generation callback that provides status during the generation of the keys </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The handle_attrs to get the callback from<br />
 <i>callback</i> The callback from the handle attributes</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if the handle_attrs is valid, otherwise an error is returned</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_set_keybits (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, intbits)</h3>
<p> Set Key Bits. Set the length of the public key pair used by the proxy certificate </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> the attributes to set<br />
 <i>bits</i> the length to set it to (usually 1024)</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_proxy_handle_attrs_set_signing_algorithm (<code>globus_gsi_proxy_handle_attrs_t</code>handle_attrs, const EVP_MD *algorithm)</h3>
<p> Set Signing Algorithm. Sets the Signing Algorithm to be used to sign the certificate request. In most cases, the signing party will ignore this value, and sign with an algorithm of its choice. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle_attrs</i> The proxy handle to set the signing algorithm of<br />
 <i>algorithm</i> The signing algorithm to set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Returns GLOBUS_SUCCESS if the handle is valid, otherwise an error object is returned.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_proxy_core from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAV">Author</a></p>
<dd></dl>
