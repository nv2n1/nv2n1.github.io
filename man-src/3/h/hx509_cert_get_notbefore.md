---
title: "hx509_cert_get_notbefore(3)"
name: "hx509_cert_get_notbefore"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_cert_get_notbefore/"
description: "hx509 certificate functions –"
---

<p>hx509 certificate functions &#8211; </p>
<h3>Functions</h3>
<p>hx509_cert <code>hx509_cert_init</code> (hx509_context context, const Certificate *c, heim_error_t *error) </p>
<p> hx509_cert <code>hx509_cert_init_data</code> (hx509_context context, const void *ptr, size_t len, heim_error_t *error) </p>
<p> void <code>hx509_cert_free</code> (hx509_cert cert) </p>
<p> hx509_cert <code>hx509_cert_ref</code> (hx509_cert cert) </p>
<p> void <code>hx509_verify_ctx_f_allow_default_trustanchors</code> (hx509_verify_ctx ctx, int boolean) </p>
<p> int <code>hx509_cert_find_subjectAltName_otherName</code> (hx509_context context, hx509_cert cert, const heim_oid *oid, hx509_octet_string_list *list) </p>
<p> int <code>hx509_cert_cmp</code> (hx509_cert p, hx509_cert q) </p>
<p> int <code>hx509_cert_get_issuer</code> (hx509_cert p, hx509_name *name) </p>
<p> int <code>hx509_cert_get_subject</code> (hx509_cert p, hx509_name *name) </p>
<p> int <code>hx509_cert_get_base_subject</code> (hx509_context context, hx509_cert c, hx509_name *name) </p>
<p> int <code>hx509_cert_get_serialnumber</code> (hx509_cert p, heim_integer *i) </p>
<p> time_t <code>hx509_cert_get_notBefore</code> (hx509_cert p) </p>
<p> time_t <code>hx509_cert_get_notAfter</code> (hx509_cert p) </p>
<p> int <code>hx509_cert_get_SPKI</code> (hx509_context context, hx509_cert p, SubjectPublicKeyInfo *spki) </p>
<p> int <code>hx509_cert_get_SPKI_AlgorithmIdentifier</code> (hx509_context context, hx509_cert p, AlgorithmIdentifier *alg) </p>
<p> int <code>hx509_cert_get_issuer_unique_id</code> (hx509_context context, hx509_cert p, heim_bit_string *issuer) </p>
<p> int <code>hx509_cert_get_subject_unique_id</code> (hx509_context context, hx509_cert p, heim_bit_string *subject) </p>
<p> int <code>hx509_verify_hostname</code> (hx509_context context, const hx509_cert cert, int flags, hx509_hostname_type type, const char *hostname, const struct sockaddr *sa, int sa_size) </p>
<p> hx509_cert_attribute <code>hx509_cert_get_attribute</code> (hx509_cert cert, const heim_oid *oid) </p>
<p> int <code>hx509_cert_set_friendly_name</code> (hx509_cert cert, const char *name) </p>
<p> const char * <code>hx509_cert_get_friendly_name</code> (hx509_cert cert) </p>
<p> int <code>hx509_query_alloc</code> (hx509_context context, hx509_query **q) </p>
<p> void <code>hx509_query_match_option</code> (hx509_query *q, hx509_query_option option) </p>
<p> int <code>hx509_query_match_issuer_serial</code> (hx509_query *q, const Name *issuer, const heim_integer *serialNumber) </p>
<p> int <code>hx509_query_match_friendly_name</code> (hx509_query *q, const char *name) </p>
<p> int <code>hx509_query_match_eku</code> (hx509_query *q, const heim_oid *eku) </p>
<p> int <code>hx509_query_match_cmp_func</code> (hx509_query *q, int(*func)(hx509_context, hx509_cert, void *), void *ctx) </p>
<p> void <code>hx509_query_free</code> (hx509_context context, hx509_query *q) </p>
<p> void <code>hx509_query_statistic_file</code> (hx509_context context, const char *fn) </p>
<p> void <code>hx509_query_unparse_stats</code> (hx509_context context, int printtype, FILE *out) </p>
<p> int <code>hx509_cert_check_eku</code> (hx509_context context, hx509_cert cert, const heim_oid *eku, int allow_any_eku) </p>
<p> int <code>hx509_cert_binary</code> (hx509_context context, hx509_cert c, heim_octet_string *os) </p>
<p> int <code>hx509_print_cert</code> (hx509_context context, hx509_cert cert, FILE *out) </p>
<h2>Detailed Description</h2>
<p>See the <code>The basic certificate</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>int hx509_cert_binary (hx509_contextcontext, hx509_certc, heim_octet_string *os)</h3>
<p>Encodes the hx509 certificate as a DER encode binary. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>c</i> the certificate to encode.<br />
 <i>os</i> the encode certificate, set to NULL, 0 on case of error. Free the os-&gt;data with <code>hx509_xfree()</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_cert_check_eku (hx509_contextcontext, hx509_certcert, const heim_oid *eku, intallow_any_eku)</h3>
<p>Check the extended key usage on the hx509 certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>cert</i> A hx509 context.<br />
 <i>eku</i> the EKU to check for<br />
 <i>allow_any_eku</i> if the any EKU is set, allow that to be a substitute.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_cert_cmp (hx509_certp, hx509_certq)</h3>
<p>Compare to hx509 certificate object, useful for sorting. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> a hx509 certificate object.<br />
 <i>q</i> a hx509 certificate object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 the objects are the same, returns &gt; 0 is p is &#8216;larger&#8217; then q, &lt; 0 if p is &#8216;smaller&#8217; then q.</dl>
<h3>int hx509_cert_find_subjectAltName_otherName (hx509_contextcontext, hx509_certcert, const heim_oid *oid, hx509_octet_string_list *list)</h3>
<p>Return a list of subjectAltNames specified by oid in the certificate. On error the </p>
<p> The returned list of octet string should be freed with <code>hx509_free_octet_string_list()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>cert</i> a hx509 certificate object.<br />
 <i>oid</i> an oid to for SubjectAltName.<br />
 <i>list</i> list of matching SubjectAltName.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_cert_free (hx509_certcert)</h3>
<p>Free reference to the hx509 certificate object, if the refcounter reaches 0, the object if freed. Its allowed to pass in NULL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cert</i> the cert to free.</dl>
<h3>hx509_cert_attribute hx509_cert_get_attribute (hx509_certcert, const heim_oid *oid)</h3>
<p>Get an external attribute for the certificate, examples are friendly name and id. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cert</i> hx509 certificate object to search<br />
 <i>oid</i> an oid to search for.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>an hx509_cert_attribute, only valid as long as the certificate is referenced.</dl>
<h3>int hx509_cert_get_base_subject (hx509_contextcontext, hx509_certc, hx509_name *name)</h3>
<p>Return the name of the base subject of the hx509 certificate. If the certiicate is a verified proxy certificate, the this function return the base certificate (root of the proxy chain). If the proxy certificate is not verified with the base certificate HX509_PROXY_CERTIFICATE_NOT_CANONICALIZED is returned. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> a hx509 context.<br />
 <i>c</i> a hx509 certificate object.<br />
 <i>name</i> a pointer to a hx509 name, should be freed by <code>hx509_name_free()</code>. See also <code>hx509_cert_get_subject()</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>const char * hx509_cert_get_friendly_name (hx509_certcert)</h3>
<p>Get friendly name of the certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cert</i> cert to get the friendly name from.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>an friendly name or NULL if there is. The friendly name is only valid as long as the certificate is referenced.</dl>
<h3>int hx509_cert_get_issuer (hx509_certp, hx509_name *name)</h3>
<p>Return the name of the issuer of the hx509 certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> a hx509 certificate object.<br />
 <i>name</i> a pointer to a hx509 name, should be freed by <code>hx509_name_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_cert_get_issuer_unique_id (hx509_contextcontext, hx509_certp, heim_bit_string *issuer)</h3>
<p>Get a copy of the Issuer Unique ID </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> a hx509_context<br />
 <i>p</i> a hx509 certificate<br />
 <i>issuer</i> the issuer id returned, free with der_free_bit_string()</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>. The error code HX509_EXTENSION_NOT_FOUND is returned if the certificate doesn&#8217;t have a issuerUniqueID</dl>
<h3>time_t hx509_cert_get_notAfter (hx509_certp)</h3>
<p>Get notAfter time of the certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> a hx509 certificate object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>return not after time.</dl>
<h3>time_t hx509_cert_get_notBefore (hx509_certp)</h3>
<p>Get notBefore time of the certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> a hx509 certificate object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>return not before time</dl>
<h3>int hx509_cert_get_serialnumber (hx509_certp, heim_integer *i)</h3>
<p>Get serial number of the certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> a hx509 certificate object.<br />
 <i>i</i> serial number, should be freed ith der_free_heim_integer().</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_cert_get_SPKI (hx509_contextcontext, hx509_certp, SubjectPublicKeyInfo *spki)</h3>
<p>Get the SubjectPublicKeyInfo structure from the hx509 certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> a hx509 context.<br />
 <i>p</i> a hx509 certificate object.<br />
 <i>spki</i> SubjectPublicKeyInfo, should be freed with free_SubjectPublicKeyInfo().</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_cert_get_SPKI_AlgorithmIdentifier (hx509_contextcontext, hx509_certp, AlgorithmIdentifier *alg)</h3>
<p>Get the AlgorithmIdentifier from the hx509 certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> a hx509 context.<br />
 <i>p</i> a hx509 certificate object.<br />
 <i>alg</i> AlgorithmIdentifier, should be freed with free_AlgorithmIdentifier(). The algorithmidentifier is typicly rsaEncryption, or id-ecPublicKey, or some other public key mechanism.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_cert_get_subject (hx509_certp, hx509_name *name)</h3>
<p>Return the name of the subject of the hx509 certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>p</i> a hx509 certificate object.<br />
 <i>name</i> a pointer to a hx509 name, should be freed by <code>hx509_name_free()</code>. See also <code>hx509_cert_get_base_subject()</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_cert_get_subject_unique_id (hx509_contextcontext, hx509_certp, heim_bit_string *subject)</h3>
<p>Get a copy of the Subect Unique ID </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> a hx509_context<br />
 <i>p</i> a hx509 certificate<br />
 <i>subject</i> the subject id returned, free with der_free_bit_string()</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>. The error code HX509_EXTENSION_NOT_FOUND is returned if the certificate doesn&#8217;t have a subjectUniqueID</dl>
<h3>hx509_cert hx509_cert_init (hx509_contextcontext, const Certificate *c, heim_error_t *error)</h3>
<p>Allocate and init an hx509 certificate object from the decoded certificate `c´. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>c</i><br />
 <i>error</i></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Returns an hx509 certificate</dl>
<h3>hx509_cert hx509_cert_init_data (hx509_contextcontext, const void *ptr, size_tlen, heim_error_t *error)</h3>
<p>Just like <code>hx509_cert_init()</code>, but instead of a decode certificate takes an pointer and length to a memory region that contains a DER/BER encoded certificate. </p>
<p> If the memory region doesn&#8217;t contain just the certificate and nothing more the function will fail with HX509_EXTRA_DATA_AFTER_STRUCTURE. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>ptr</i> pointer to memory region containing encoded certificate.<br />
 <i>len</i> length of memory region.<br />
 <i>error</i> possibly returns an error</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 certificate</dl>
<h3>hx509_cert hx509_cert_ref (hx509_certcert)</h3>
<p>Add a reference to a hx509 certificate object. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cert</i> a pointer to an hx509 certificate object.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>the same object as is passed in.</dl>
<h3>int hx509_cert_set_friendly_name (hx509_certcert, const char *name)</h3>
<p>Set the friendly name on the certificate. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>cert</i> The certificate to set the friendly name on<br />
 <i>name</i> Friendly name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_print_cert (hx509_contextcontext, hx509_certcert, FILE *out)</h3>
<p>Print a simple representation of a certificate </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context, can be NULL<br />
 <i>cert</i> certificate to print<br />
 <i>out</i> the stdio output stream, if NULL, stdout is used</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code</dl>
<h3>int hx509_query_alloc (hx509_contextcontext, hx509_query **q)</h3>
<p>Allocate an query controller. Free using <code>hx509_query_free()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>q</i> return pointer to a hx509_query.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_query_free (hx509_contextcontext, hx509_query *q)</h3>
<p>Free the query controller. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>q</i> a pointer to the query controller.</dl>
<h3>int hx509_query_match_cmp_func (hx509_query *q, int(*)(hx509_context, hx509_cert, void *)func, void *ctx)</h3>
<p>Set the query controller to match using a specific match function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>q</i> a hx509 query controller.<br />
 <i>func</i> function to use for matching, if the argument is NULL, the match function is removed.<br />
 <i>ctx</i> context passed to the function.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_query_match_eku (hx509_query *q, const heim_oid *eku)</h3>
<p>Set the query controller to require an one specific EKU (extended key usage). Any previous EKU matching is overwitten. If NULL is passed in as the eku, the EKU requirement is reset. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>q</i> a hx509 query controller.<br />
 <i>eku</i> an EKU to match on.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_query_match_friendly_name (hx509_query *q, const char *name)</h3>
<p>Set the query controller to match on a friendly name </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>q</i> a hx509 query controller.<br />
 <i>name</i> a friendly name to match on</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_query_match_issuer_serial (hx509_query *q, const Name *issuer, const heim_integer *serialNumber)</h3>
<p>Set the issuer and serial number of match in the query controller. The function make copies of the isser and serial number. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>q</i> a hx509 query controller<br />
 <i>issuer</i> issuer to search for<br />
 <i>serialNumber</i> the serialNumber of the issuer.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_query_match_option (hx509_query *q, hx509_query_optionoption)</h3>
<p>Set match options for the hx509 query controller. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>q</i> query controller.<br />
 <i>option</i> options to control the query controller.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_query_statistic_file (hx509_contextcontext, const char *fn)</h3>
<p>Set a statistic file for the query statistics. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>fn</i> statistics file name</dl>
<h3>void hx509_query_unparse_stats (hx509_contextcontext, intprinttype, FILE *out)</h3>
<p>Unparse the statistics file and print the result on a FILE descriptor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>printtype</i> tyep to print<br />
 <i>out</i> the FILE to write the data on.</dl>
<h3>void hx509_verify_ctx_f_allow_default_trustanchors (hx509_verify_ctxctx, intboolean)</h3>
<p>Allow using the operating system builtin trust anchors if no other trust anchors are configured. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> a verification context<br />
 <i>boolean</i> if non zero, useing the operating systems builtin trust anchors.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_verify_hostname (hx509_contextcontext, const hx509_certcert, intflags, hx509_hostname_typetype, const char *hostname, const struct sockaddr *sa, intsa_size)</h3>
<p>Verify that the certificate is allowed to be used for the hostname and address. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> A hx509 context.<br />
 <i>cert</i> the certificate to match with<br />
 <i>flags</i> Flags to modify the behavior:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>HX509_VHN_F_ALLOW_NO_MATCH no match is ok</dl>
<p> <i>type</i> type of hostname:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>HX509_HN_HOSTNAME for plain hostname.</p>
<dt>&bull;</p>
<dd>HX509_HN_DNSSRV for DNS SRV names.</dl>
<p> <i>hostname</i> the hostname to check<br />
 <i>sa</i> address of the host<br />
 <i>sa_size</i> length of address</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Heimdalx509library from the source code.</p>
