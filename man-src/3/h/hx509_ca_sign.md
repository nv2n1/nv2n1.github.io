---
title: "hx509_ca_sign(3)"
name: "hx509_ca_sign"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_ca_sign/"
description: "hx509 CA functions –"
---

<h2 class="name">NAME</h2>
<p> hx509 CA functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>hx509_ca_tbs_init</code> (hx509_context context, hx509_ca_tbs *tbs) </p>
<p> void <code>hx509_ca_tbs_free</code> (hx509_ca_tbs *tbs) </p>
<p> int <code>hx509_ca_tbs_set_notBefore</code> (hx509_context context, hx509_ca_tbs tbs, time_t t) </p>
<p> int <code>hx509_ca_tbs_set_notAfter</code> (hx509_context context, hx509_ca_tbs tbs, time_t t) </p>
<p> int <code>hx509_ca_tbs_set_notAfter_lifetime</code> (hx509_context context, hx509_ca_tbs tbs, time_t delta) </p>
<p> struct units * <code>hx509_ca_tbs_template_units</code> (void) </p>
<p> int <code>hx509_ca_tbs_set_template</code> (hx509_context context, hx509_ca_tbs tbs, int flags, hx509_cert cert) </p>
<p> int <code>hx509_ca_tbs_set_ca</code> (hx509_context context, hx509_ca_tbs tbs, int pathLenConstraint) </p>
<p> int <code>hx509_ca_tbs_set_proxy</code> (hx509_context context, hx509_ca_tbs tbs, int pathLenConstraint) </p>
<p> int <code>hx509_ca_tbs_set_domaincontroller</code> (hx509_context context, hx509_ca_tbs tbs) </p>
<p> int <code>hx509_ca_tbs_set_spki</code> (hx509_context context, hx509_ca_tbs tbs, const SubjectPublicKeyInfo *spki) </p>
<p> int <code>hx509_ca_tbs_set_serialnumber</code> (hx509_context context, hx509_ca_tbs tbs, const heim_integer *serialNumber) </p>
<p> int <code>hx509_ca_tbs_add_eku</code> (hx509_context context, hx509_ca_tbs tbs, const heim_oid *oid) </p>
<p> int <code>hx509_ca_tbs_add_crl_dp_uri</code> (hx509_context context, hx509_ca_tbs tbs, const char *uri, hx509_name issuername) </p>
<p> int <code>hx509_ca_tbs_add_san_otherName</code> (hx509_context context, hx509_ca_tbs tbs, const heim_oid *oid, const heim_octet_string *os) </p>
<p> int <code>hx509_ca_tbs_add_san_pkinit</code> (hx509_context context, hx509_ca_tbs tbs, const char *principal) </p>
<p> int <code>hx509_ca_tbs_add_san_ms_upn</code> (hx509_context context, hx509_ca_tbs tbs, const char *principal) </p>
<p> int <code>hx509_ca_tbs_add_san_jid</code> (hx509_context context, hx509_ca_tbs tbs, const char *jid) </p>
<p> int <code>hx509_ca_tbs_add_san_hostname</code> (hx509_context context, hx509_ca_tbs tbs, const char *dnsname) </p>
<p> int <code>hx509_ca_tbs_add_san_rfc822name</code> (hx509_context context, hx509_ca_tbs tbs, const char *rfc822Name) </p>
<p> int <code>hx509_ca_tbs_set_subject</code> (hx509_context context, hx509_ca_tbs tbs, hx509_name subject) </p>
<p> int <code>hx509_ca_tbs_set_unique</code> (hx509_context context, hx509_ca_tbs tbs, const heim_bit_string *subjectUniqueID, const heim_bit_string *issuerUniqueID) </p>
<p> int <code>hx509_ca_tbs_subject_expand</code> (hx509_context context, hx509_ca_tbs tbs, hx509_env env) </p>
<p> int <code>hx509_ca_tbs_set_signature_algorithm</code> (hx509_context context, hx509_ca_tbs tbs, const AlgorithmIdentifier *sigalg) </p>
<p> int <code>hx509_ca_sign</code> (hx509_context context, hx509_ca_tbs tbs, hx509_cert signer, hx509_cert *certificate) </p>
<p> int <code>hx509_ca_sign_self</code> (hx509_context context, hx509_ca_tbs tbs, hx509_private_key signer, hx509_cert *certificate) </p>
<h2>Detailed Description</h2>
<p> See the <code>Hx509 CA functions</code> for description and examples.</p>
<h2>Function Documentation</h2>
<h3>int hx509_ca_sign (hx509_contextcontext, hx509_ca_tbstbs, hx509_certsigner, hx509_cert *certificate)</h3>
<p> Sign a to-be-signed certificate object with a issuer certificate. </p>
<p> The caller needs to at least have called the following functions on the to-be-signed certificate object:</p>
<dl>
<dt>&bull;</p>
<dd> <code>hx509_ca_tbs_init()</code></p>
<dt>&bull;</p>
<dd> <code>hx509_ca_tbs_set_subject()</code></p>
<dt>&bull;</p>
<dd> <code>hx509_ca_tbs_set_spki()</code></dl>
<p> When done the to-be-signed certificate object should be freed with <code>hx509_ca_tbs_free()</code>. </p>
<p> When creating self-signed certificate use <code>hx509_ca_sign_self()</code> instead. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>signer</i> the CA certificate object to sign with (need private key).<br />
 <i>certificate</i> return cerificate, free with <code>hx509_cert_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_sign_self (hx509_contextcontext, hx509_ca_tbstbs, hx509_private_keysigner, hx509_cert *certificate)</h3>
<p> Work just like <code>hx509_ca_sign()</code> but signs it-self. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>signer</i> private key to sign with.<br />
 <i>certificate</i> return cerificate, free with <code>hx509_cert_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_add_crl_dp_uri (hx509_contextcontext, hx509_ca_tbstbs, const char *uri, hx509_nameissuername)</h3>
<p> Add CRL distribution point URI to the to-be-signed certificate object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>uri</i> uri to the CRL.<br />
 <i>issuername</i> name of the issuer.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<p> issuername not supported</p>
<h3>int hx509_ca_tbs_add_eku (hx509_contextcontext, hx509_ca_tbstbs, const heim_oid *oid)</h3>
<p> An an extended key usage to the to-be-signed certificate object. Duplicates will detected and not added. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>oid</i> extended key usage to add.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_add_san_hostname (hx509_contextcontext, hx509_ca_tbstbs, const char *dnsname)</h3>
<p> Add a Subject Alternative Name hostname to to-be-signed certificate object. A domain match starts with ., an exact match does not. </p>
<p> Example of a an domain match: .domain.se matches the hostname host.domain.se. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>dnsname</i> a hostame.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_add_san_jid (hx509_contextcontext, hx509_ca_tbstbs, const char *jid)</h3>
<p> Add a Jabber/XMPP jid Subject Alternative Name to the to-be-signed certificate object. The jid is an UTF8 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>jid</i> string of an a jabber id in UTF8.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_add_san_ms_upn (hx509_contextcontext, hx509_ca_tbstbs, const char *principal)</h3>
<p> Add Microsoft UPN Subject Alternative Name to the to-be-signed certificate object. The principal string is a UTF8 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>principal</i> Microsoft UPN string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_add_san_otherName (hx509_contextcontext, hx509_ca_tbstbs, const heim_oid *oid, const heim_octet_string *os)</h3>
<p> Add Subject Alternative Name otherName to the to-be-signed certificate object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>oid</i> the oid of the OtherName.<br />
 <i>os</i> data in the other name.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_add_san_pkinit (hx509_contextcontext, hx509_ca_tbstbs, const char *principal)</h3>
<p> Add Kerberos Subject Alternative Name to the to-be-signed certificate object. The principal string is a UTF8 string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>principal</i> Kerberos principal to add to the certificate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_add_san_rfc822name (hx509_contextcontext, hx509_ca_tbstbs, const char *rfc822Name)</h3>
<p> Add a Subject Alternative Name rfc822 (email address) to to-be-signed certificate object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>rfc822Name</i> a string to a email address.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>void hx509_ca_tbs_free (hx509_ca_tbs *tbs)</h3>
<p> Free an To Be Signed object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>tbs</i> object to free.</dl>
<h3>int hx509_ca_tbs_init (hx509_contextcontext, hx509_ca_tbs *tbs)</h3>
<p> Allocate an to-be-signed certificate object that will be converted into an certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> returned to-be-signed certicate object, free with <code>hx509_ca_tbs_free()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_ca (hx509_contextcontext, hx509_ca_tbstbs, intpathLenConstraint)</h3>
<p> Make the to-be-signed certificate object a CA certificate. If the pathLenConstraint is negative path length constraint is used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>pathLenConstraint</i> path length constraint, negative, no constraint.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_domaincontroller (hx509_contextcontext, hx509_ca_tbstbs)</h3>
<p> Make the to-be-signed certificate object a windows domain controller certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_notAfter (hx509_contextcontext, hx509_ca_tbstbs, time_tt)</h3>
<p> Set the absolute time when the certificate is valid to. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>t</i> time when the certificate will expire</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_notAfter_lifetime (hx509_contextcontext, hx509_ca_tbstbs, time_tdelta)</h3>
<p> Set the relative time when the certificiate is going to expire. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>delta</i> seconds to the certificate is going to expire.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_notBefore (hx509_contextcontext, hx509_ca_tbstbs, time_tt)</h3>
<p> Set the absolute time when the certificate is valid from. If not set the current time will be used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>t</i> time the certificated will start to be valid</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_proxy (hx509_contextcontext, hx509_ca_tbstbs, intpathLenConstraint)</h3>
<p> Make the to-be-signed certificate object a proxy certificate. If the pathLenConstraint is negative path length constraint is used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>pathLenConstraint</i> path length constraint, negative, no constraint.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_serialnumber (hx509_contextcontext, hx509_ca_tbstbs, const heim_integer *serialNumber)</h3>
<p> Set the serial number to use for to-be-signed certificate object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>serialNumber</i> serial number to use for the to-be-signed certificate object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_signature_algorithm (hx509_contextcontext, hx509_ca_tbstbs, const AlgorithmIdentifier *sigalg)</h3>
<p> Set signature algorithm on the to be signed certificate </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>sigalg</i> signature algorithm to use</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_spki (hx509_contextcontext, hx509_ca_tbstbs, const SubjectPublicKeyInfo *spki)</h3>
<p> Set the subject public key info (SPKI) in the to-be-signed certificate object. SPKI is the public key and key related parameters in the certificate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>spki</i> subject public key info to use for the to-be-signed certificate object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_subject (hx509_contextcontext, hx509_ca_tbstbs, hx509_namesubject)</h3>
<p> Set the subject name of a to-be-signed certificate object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>subject</i> the name to set a subject.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_template (hx509_contextcontext, hx509_ca_tbstbs, intflags, hx509_certcert)</h3>
<p> Initialize the to-be-signed certificate object from a template certifiate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>flags</i> bit field selecting what to copy from the template certifiate.<br />
 <i>cert</i> template certificate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_set_unique (hx509_contextcontext, hx509_ca_tbstbs, const heim_bit_string *subjectUniqueID, const heim_bit_string *issuerUniqueID)</h3>
<p> Set the issuerUniqueID and subjectUniqueID </p>
<p> These are only supposed to be used considered with version 2 certificates, replaced by the two extensions SubjectKeyIdentifier and IssuerKeyIdentifier. This function is to allow application using legacy protocol to issue them. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>issuerUniqueID</i> to be set<br />
 <i>subjectUniqueID</i> to be set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>int hx509_ca_tbs_subject_expand (hx509_contextcontext, hx509_ca_tbstbs, hx509_envenv)</h3>
<p> Expand the the subject name in the to-be-signed certificate object using <code>hx509_name_expand()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A hx509 context.<br />
 <i>tbs</i> object to be signed.<br />
 <i>env</i> enviroment variable to expand variables in the subject name, see hx509_env_init().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An hx509 error code, see <code>hx509_get_error_string()</code>.</dl>
<h3>struct units * hx509_ca_tbs_template_units (void)</h3>
<p> Make of template units, use to build flags argument to <code>hx509_ca_tbs_set_template()</code> with parse_units(). </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> an units structure.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
<h2>Index</h2>
