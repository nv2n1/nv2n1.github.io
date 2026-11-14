---
title: "globus_gsi_cred_get_key_bits(3)"
name: "globus_gsi_cred_get_key_bits"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_cred_get_key_bits/"
description: "Credential Handle Management –"
---

<h2 class="name">NAME</h2>
<p> Credential Handle Management &#8211; </p>
<h3>Typedefs</h3>
<p> typedef struct<br />
 globus_l_gsi_cred_handle_s * <code>globus_gsi_cred_handle_t</code>&quot; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_cred_handle_init</code> (<code>globus_gsi_cred_handle_t</code> *handle, <code>globus_gsi_cred_handle_attrs_t</code> handle_attrs)<br />
 <i>Initialize a Handle. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_destroy</code> (<code>globus_gsi_cred_handle_t</code> handle)<br />
 <i>Destroy the credential handle. </i><br />
 globus_result_t <code>globus_gsi_cred_handle_copy</code> (<code>globus_gsi_cred_handle_t</code> source, <code>globus_gsi_cred_handle_t</code> *dest)<br />
 <i>Copy a handle. </i><br />
 globus_result_t <code>globus_gsi_cred_get_handle_attrs</code> (<code>globus_gsi_cred_handle_t</code> handle, <code>globus_gsi_cred_handle_attrs_t</code> *attrs)<br />
 <i>Get the handle attributes. </i><br />
 globus_result_t <code>globus_gsi_cred_get_goodtill</code> (<code>globus_gsi_cred_handle_t</code> cred_handle, time_t *goodtill)<br />
 <i>Get credential expiration. </i><br />
 globus_result_t <code>globus_gsi_cred_get_lifetime</code> (<code>globus_gsi_cred_handle_t</code> cred_handle, time_t *lifetime)<br />
 <i>Get credential lifetime. </i><br />
 globus_result_t <code>globus_gsi_cred_get_key_bits</code> (<code>globus_gsi_cred_handle_t</code> cred_handle, int *key_bits)<br />
 <i>Get credential strength. </i><br />
 globus_result_t <code>globus_gsi_cred_set_cert</code> (<code>globus_gsi_cred_handle_t</code> handle, X509 *cert)<br />
 <i>Set the credential&#8217;s certificate. </i><br />
 globus_result_t <code>globus_gsi_cred_get_cert</code> (<code>globus_gsi_cred_handle_t</code> handle, X509 **cert)<br />
 <i>Get the credential&#8217;s certificate. </i><br />
 globus_result_t <code>globus_gsi_cred_set_key</code> (<code>globus_gsi_cred_handle_t</code> handle, EVP_PKEY *key)<br />
 <i>Set the credential&#8217;s private key. </i><br />
 globus_result_t <code>globus_gsi_cred_get_key</code> (<code>globus_gsi_cred_handle_t</code> handle, EVP_PKEY **key)<br />
 <i>Get the credential&#8217;s private key. </i><br />
 globus_result_t <code>globus_gsi_cred_set_cert_chain</code> (<code>globus_gsi_cred_handle_t</code> handle, STACK_OF(X509)*cert_chain)<br />
 <i>Set the certificate chain. </i><br />
 globus_result_t <code>globus_gsi_cred_get_cert_chain</code> (<code>globus_gsi_cred_handle_t</code> handle, STACK_OF(X509)**cert_chain)<br />
 <i>Get the certificate chain. </i><br />
 globus_result_t <code>globus_gsi_cred_get_X509_subject_name</code> (<code>globus_gsi_cred_handle_t</code> handle, X509_NAME **subject_name)<br />
 <i>Get credential subject name. </i><br />
 globus_result_t <code>globus_gsi_cred_get_X509_identity_name</code> (<code>globus_gsi_cred_handle_t</code> handle, X509_NAME **identity_name)<br />
 <i>Get X.509 identity. </i><br />
 globus_result_t <code>globus_gsi_cred_get_subject_name</code> (<code>globus_gsi_cred_handle_t</code> handle, char **subject_name)<br />
 <i>Get credential subject name. </i><br />
 globus_result_t <code>globus_gsi_cred_get_policies</code> (<code>globus_gsi_cred_handle_t</code> handle, STACK **policies)<br />
 <i>Get certificate chain policies. </i><br />
 globus_result_t <code>globus_gsi_cred_get_policy_languages</code> (<code>globus_gsi_cred_handle_t</code> handle, STACK_OF(ASN1_OBJECT)**policy_languages)<br />
 <i>Get certificate chain policy languages. </i><br />
 globus_result_t <code>globus_gsi_cred_get_X509_issuer_name</code> (<code>globus_gsi_cred_handle_t</code> handle, X509_NAME **issuer_name)<br />
 <i>Get credential issuer name object. </i><br />
 globus_result_t <code>globus_gsi_cred_get_issuer_name</code> (<code>globus_gsi_cred_handle_t</code> handle, char **issuer_name)<br />
 <i>Get issuer name. </i><br />
 globus_result_t <code>globus_gsi_cred_get_identity_name</code> (<code>globus_gsi_cred_handle_t</code> handle, char **identity_name)<br />
 <i>Get identity name. </i><br />
 globus_result_t <code>globus_gsi_cred_verify_cert_chain</code> (<code>globus_gsi_cred_handle_t</code> cred_handle, globus_gsi_callback_data_t callback_data)<br />
 <i>Verify credential. </i><br />
 globus_result_t <code>globus_gsi_cred_verify_cert_chain_when</code> (<code>globus_gsi_cred_handle_t</code> cred_handle, globus_gsi_callback_data_t callback_data_in, time_t check_time)<br />
 <i>Verify credential at a specific time. </i><br />
 globus_result_t <code>globus_gsi_cred_verify</code> (<code>globus_gsi_cred_handle_t</code> handle)<br />
 <i>Verify a credential. </i></p>
<h2>Detailed Description</h2>
<p> Create/Destroy/Modify a GSI Credential Handle. </p>
<p> Within the Globus GSI Credential Library, all credential operations require a handle parameter. Currently only one operation may be in progress at once per credential handle. </p>
<p> This section defines operations to create, modify and destroy GSI Credential handles.</p>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_l_gsi_cred_handle_s* <code>globus_gsi_cred_handle_t</code></h3>
<p> GSI Credential Handle. </p>
<p> A GSI Credential handle keeps track of state relating to a credential. Handles can have immutable <code>attributes</code> associated with them. All credential <code>operations </code> take a credential handle pointer as a parameter. </p>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>globus_gsi_cred_handle_init()</code>, <code>globus_gsi_cred_handle_destroy()</code>, <code>globus_gsi_cred_handle_attrs_t</code></dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_cred_get_cert (<code>globus_gsi_cred_handle_t</code>handle, X509 **cert)</h3>
<p> Get the credential&#8217;s certificate. Get the certificate of a credential </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle to get the certificate from<br />
 <i>cert</i> The resulting X509 certificate, a duplicate of the certificate in the credential handle. This variable should be freed when the user is finished with it using the function X509_free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object id is returned</dl>
<h3>globus_result_t globus_gsi_cred_get_cert_chain (<code>globus_gsi_cred_handle_t</code>handle, STACK_OF(X509)**cert_chain)</h3>
<p> Get the certificate chain. Get the certificate chain of the credential handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate chain to get<br />
 <i>cert_chain</i> The certificate chain to set as a duplicate of the cert chain in the credential handle. This variable (or the variable it points to) needs to be freed when the user is finished with it using sk_X509_free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object id is returned</dl>
<h3>globus_result_t globus_gsi_cred_get_goodtill (<code>globus_gsi_cred_handle_t</code>cred_handle, time_t *goodtill)</h3>
<p> Get credential expiration. This function retrieves the expiration time of the credential contained in the handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cred_handle</i> The credential handle to retrieve the expiration time from<br />
 <i>goodtill</i> Contains the expiration time on return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h3>globus_result_t globus_gsi_cred_get_handle_attrs (<code>globus_gsi_cred_handle_t</code>handle, <code>globus_gsi_cred_handle_attrs_t</code> *attrs)</h3>
<p> Get the handle attributes. This function retrieves a copy of the credential handle attributes </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle to retrieve the attributes from<br />
 <i>attrs</i> Contains the credential attributes on return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h3>globus_result_t globus_gsi_cred_get_identity_name (<code>globus_gsi_cred_handle_t</code>handle, char **identity_name)</h3>
<p> Get identity name. Get the identity&#8217;s subject name from the credential handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate to get the identity of<br />
 <i>identity_name</i> The identity certificate&#8217;s subject name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object identifier is returned</dl>
<h3>globus_result_t globus_gsi_cred_get_issuer_name (<code>globus_gsi_cred_handle_t</code>handle, char **issuer_name)</h3>
<p> Get issuer name. Get the issuer&#8217;s subject name from the credential handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate to get the issuer of<br />
 <i>issuer_name</i> The issuer certificate&#8217;s subject name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object identifier is returned</dl>
<h3>globus_result_t globus_gsi_cred_get_key (<code>globus_gsi_cred_handle_t</code>handle, EVP_PKEY **key)</h3>
<p> Get the credential&#8217;s private key. Get the credential handle&#8217;s private key </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the private key to get<br />
 <i>key</i> The private key which after this function returns is set to a duplicate of the private key of the credential handle. This variable needs to be freed by the user when it is no longer used via the function EVP_PKEY_free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h3>globus_result_t globus_gsi_cred_get_key_bits (<code>globus_gsi_cred_handle_t</code>cred_handle, int *key_bits)</h3>
<p> Get credential strength. This function retrieves the key strength of the credential contained in a handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cred_handle</i> The credential handle to retrieve the strength from<br />
 <i>key_bits</i> Contains the number of bits in the key on return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h3>globus_result_t globus_gsi_cred_get_lifetime (<code>globus_gsi_cred_handle_t</code>cred_handle, time_t *lifetime)</h3>
<p> Get credential lifetime. This function retrieves the lifetime of the credential contained in a handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cred_handle</i> The credential handle to retrieve the lifetime from<br />
 <i>lifetime</i> Contains the lifetime on return</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h3>globus_result_t globus_gsi_cred_get_policies (<code>globus_gsi_cred_handle_t</code>handle, STACK **policies)</h3>
<p> Get certificate chain policies. Get the Policies from the Cert Chain in the handle. The policies will be null-terminated as they are added to the handle. If a policy for a cert in the chain doesn&#8217;t exist, the string in the stack will be set to the static string GLOBUS_NULL_POLICIES </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the handle to get the cert chain containing the policies<br />
 <i>policies</i> the stack of policies retrieved from the handle&#8217;s cert chain</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object if an error occurred</dl>
<h3>globus_result_t globus_gsi_cred_get_policy_languages (<code>globus_gsi_cred_handle_t</code>handle, STACK_OF(ASN1_OBJECT)**policy_languages)</h3>
<p> Get certificate chain policy languages. Get the policy languages from the cert chain in the handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> the handle to get the cert chain containing the policies<br />
 <i>policy_languages</i> the stack of policies retrieved from the handle&#8217;s cert chain</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object if an error occurred</dl>
<h3>globus_result_t globus_gsi_cred_get_subject_name (<code>globus_gsi_cred_handle_t</code>handle, char **subject_name)</h3>
<p> Get credential subject name. Get the credential handle&#8217;s certificate subject name </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate to get the subject name of<br />
 <i>subject_name</i> The subject name as a string. This should be freed using OPENSSL_free() when the user is finished with it</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, a error object id otherwise</dl>
<h3>globus_result_t globus_gsi_cred_get_X509_identity_name (<code>globus_gsi_cred_handle_t</code>handle, X509_NAME **identity_name)</h3>
<p> Get X.509 identity. Get the identity&#8217;s X.509 subject name from the credential handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate to get the identity from<br />
 <i>identity_name</i> The identity certificate&#8217;s X509 subject name</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object identifier is returned</dl>
<h3>globus_result_t globus_gsi_cred_get_X509_issuer_name (<code>globus_gsi_cred_handle_t</code>handle, X509_NAME **issuer_name)</h3>
<p> Get credential issuer name object. Get the credential handle&#8217;s certificate issuer name </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate to get the issuer name of<br />
 <i>issuer_name</i> The issuer name as an X509_NAME object. This should be freed using X509_NAME_free when the user is finished with it</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, a error object id otherwise</dl>
<h3>globus_result_t globus_gsi_cred_get_X509_subject_name (<code>globus_gsi_cred_handle_t</code>handle, X509_NAME **subject_name)</h3>
<p> Get credential subject name. Get the credential handle&#8217;s certificate subject name </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate to get the subject name of<br />
 <i>subject_name</i> The subject name as an X509_NAME object. This should be freed using X509_NAME_free when the user is finished with it</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, a error object id otherwise</dl>
<h3>globus_result_t globus_gsi_cred_handle_copy (<code>globus_gsi_cred_handle_t</code>source, <code>globus_gsi_cred_handle_t</code> *dest)</h3>
<p> Copy a handle. Copies a credential handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>source</i> The handle to be copied<br />
 <i>dest</i> The destination of the copy</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h3>globus_result_t globus_gsi_cred_handle_destroy (<code>globus_gsi_cred_handle_t</code>handle)</h3>
<p> Destroy the credential handle. Destroys the credential handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle to be destroyed</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS</dl>
<h3>globus_result_t globus_gsi_cred_handle_init (<code>globus_gsi_cred_handle_t</code> *handle, <code>globus_gsi_cred_handle_attrs_t</code>handle_attrs)</h3>
<p> Initialize a Handle. Initializes a credential handle to be used credential handling functions. Takes a set of handle attributes that are immutable to the handle. The handle attributes are only pointed to by the handle, so the lifetime of the attributes needs to be as long as that of the handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle to be initialized<br />
 <i>handle_attrs</i> The immutable attributes of the handle</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error captured in a globus_result_t</dl>
<h3>globus_result_t globus_gsi_cred_set_cert (<code>globus_gsi_cred_handle_t</code>handle, X509 *cert)</h3>
<p> Set the credential&#8217;s certificate. Set the Credential&#8217;s Certificate. The X509 cert that is passed in should be a valid X509 certificate object </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle to set the certificate on<br />
 <i>cert</i> The X509 cert to set in the cred handle. The cert passed in can be NULL which will set the cert in the handle to NULL, freeing the current cert in the handle.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object id if an error</dl>
<h3>globus_result_t globus_gsi_cred_set_cert_chain (<code>globus_gsi_cred_handle_t</code>handle, STACK_OF(X509)*cert_chain)</h3>
<p> Set the certificate chain. Set the certificate chain of the credential handle </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle containing the certificate chain field to set<br />
 <i>cert_chain</i> The certificate chain to set the handle&#8217;s certificate chain to</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object id is returned</dl>
<h3>globus_result_t globus_gsi_cred_set_key (<code>globus_gsi_cred_handle_t</code>handle, EVP_PKEY *key)</h3>
<p> Set the credential&#8217;s private key. Set the private key of the credential handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The handle on which to set the key.<br />
 <i>key</i> The private key to set the handle&#8217;s key to. This value can be NULL, in which case the current handle&#8217;s key is freed.</dl>
<h3>globus_result_t globus_gsi_cred_verify (<code>globus_gsi_cred_handle_t</code>handle)</h3>
<p> Verify a credential. This function checks that the certificate is signed by the public key of the issuer cert (the first cert in the chain). Note that this function DOES NOT check the private key or the public of the certificate, as stated in a previous version of the documentation. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>handle</i> The credential handle containing the certificate and key to be validated</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object identifier is returned</dl>
<h3>globus_result_t globus_gsi_cred_verify_cert_chain (<code>globus_gsi_cred_handle_t</code>cred_handle, globus_gsi_callback_data_tcallback_data)</h3>
<p> Verify credential. This function performs path validation on the certificate chain contained in the credential handle. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cred_handle</i> The credential handle containing the certificate chain to be validated<br />
 <i>callback_data</i> A initialized callback data structure</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object identifier is returned</dl>
<h3>globus_result_t globus_gsi_cred_verify_cert_chain_when (<code>globus_gsi_cred_handle_t</code>cred_handle, globus_gsi_callback_data_tcallback_data_in, time_tcheck_time)</h3>
<p> Verify credential at a specific time. This function performs path validation on the certificate chain contained in the credential handle. Expiration checks are done at the time given. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>cred_handle</i> The credential handle containing the certificate chain to be validated<br />
 <i>callback_data_in</i> A callback data structure. If NULL, one will be initialized with only the default cert dir set.<br />
 <i>check_time</i> Check if the cert chain was valid at this time. Set to 0 to use a time that the cert is valid, essentially bypassing the expiration check.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS if no error, otherwise an error object identifier is returned</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_credential from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbBG">Author</a></p>
<dd></dl>
