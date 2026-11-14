---
title: "hx509_ca_tbs_add_eku(3)"
name: "hx509_ca_tbs_add_eku"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_ca_tbs_add_eku/"
---

<h2 class="name">NAME</h2>
 

 hx509 CA functions - 

<h3>Functions</h3>

 

 
 int <b>hx509_ca_tbs_init</b> (hx509_context context, hx509_ca_tbs *tbs) 
 
 void <b>hx509_ca_tbs_free</b> (hx509_ca_tbs *tbs) 
 
 int <b>hx509_ca_tbs_set_notBefore</b> (hx509_context context, hx509_ca_tbs tbs, time_t t) 
 
 int <b>hx509_ca_tbs_set_notAfter</b> (hx509_context context, hx509_ca_tbs tbs, time_t t) 
 
 int <b>hx509_ca_tbs_set_notAfter_lifetime</b> (hx509_context context, hx509_ca_tbs tbs, time_t delta) 
 
 struct units * <b>hx509_ca_tbs_template_units</b> (void) 
 
 int <b>hx509_ca_tbs_set_template</b> (hx509_context context, hx509_ca_tbs tbs, int flags, hx509_cert cert) 
 
 int <b>hx509_ca_tbs_set_ca</b> (hx509_context context, hx509_ca_tbs tbs, int pathLenConstraint) 
 
 int <b>hx509_ca_tbs_set_proxy</b> (hx509_context context, hx509_ca_tbs tbs, int pathLenConstraint) 
 
 int <b>hx509_ca_tbs_set_domaincontroller</b> (hx509_context context, hx509_ca_tbs tbs) 
 
 int <b>hx509_ca_tbs_set_spki</b> (hx509_context context, hx509_ca_tbs tbs, const SubjectPublicKeyInfo *spki) 
 
 int <b>hx509_ca_tbs_set_serialnumber</b> (hx509_context context, hx509_ca_tbs tbs, const heim_integer *serialNumber) 
 
 int <b>hx509_ca_tbs_add_eku</b> (hx509_context context, hx509_ca_tbs tbs, const heim_oid *oid) 
 
 int <b>hx509_ca_tbs_add_crl_dp_uri</b> (hx509_context context, hx509_ca_tbs tbs, const char *uri, hx509_name issuername) 
 
 int <b>hx509_ca_tbs_add_san_otherName</b> (hx509_context context, hx509_ca_tbs tbs, const heim_oid *oid, const heim_octet_string *os) 
 
 int <b>hx509_ca_tbs_add_san_pkinit</b> (hx509_context context, hx509_ca_tbs tbs, const char *principal) 
 
 int <b>hx509_ca_tbs_add_san_ms_upn</b> (hx509_context context, hx509_ca_tbs tbs, const char *principal) 
 
 int <b>hx509_ca_tbs_add_san_jid</b> (hx509_context context, hx509_ca_tbs tbs, const char *jid) 
 
 int <b>hx509_ca_tbs_add_san_hostname</b> (hx509_context context, hx509_ca_tbs tbs, const char *dnsname) 
 
 int <b>hx509_ca_tbs_add_san_rfc822name</b> (hx509_context context, hx509_ca_tbs tbs, const char *rfc822Name) 
 
 int <b>hx509_ca_tbs_set_subject</b> (hx509_context context, hx509_ca_tbs tbs, hx509_name subject) 
 
 int <b>hx509_ca_tbs_set_unique</b> (hx509_context context, hx509_ca_tbs tbs, const heim_bit_string *subjectUniqueID, const heim_bit_string *issuerUniqueID) 
 
 int <b>hx509_ca_tbs_subject_expand</b> (hx509_context context, hx509_ca_tbs tbs, hx509_env env) 
 
 int <b>hx509_ca_tbs_set_signature_algorithm</b> (hx509_context context, hx509_ca_tbs tbs, const AlgorithmIdentifier *sigalg) 
 
 int <b>hx509_ca_sign</b> (hx509_context context, hx509_ca_tbs tbs, hx509_cert signer, hx509_cert *certificate) 
 
 int <b>hx509_ca_sign_self</b> (hx509_context context, hx509_ca_tbs tbs, hx509_private_key signer, hx509_cert *certificate) 

<h2>Detailed Description</h2>

 

 See the <b>Hx509 CA functions</b> for description and examples.

<h2>Function Documentation</h2>

 

<h3>int hx509_ca_sign (hx509_contextcontext, hx509_ca_tbstbs, hx509_certsigner, hx509_cert *certificate)</h3>

 Sign a to-be-signed certificate object with a issuer certificate. 

 The caller needs to at least have called the following functions on the to-be-signed certificate object:
<dl>
<dt>&bull;
<dd> <b>hx509_ca_tbs_init()</b>
<dt>&bull;
<dd> <b>hx509_ca_tbs_set_subject()</b>
<dt>&bull;
<dd> <b>hx509_ca_tbs_set_spki()</b></dl>
 

 

 When done the to-be-signed certificate object should be freed with <b>hx509_ca_tbs_free()</b>. 

 When creating self-signed certificate use <b>hx509_ca_sign_self()</b> instead. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>signer</i> the CA certificate object to sign with (need private key). 
 <i>certificate</i> return cerificate, free with <b>hx509_cert_free()</b>.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_sign_self (hx509_contextcontext, hx509_ca_tbstbs, hx509_private_keysigner, hx509_cert *certificate)</h3>

 Work just like <b>hx509_ca_sign()</b> but signs it-self. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>signer</i> private key to sign with. 
 <i>certificate</i> return cerificate, free with <b>hx509_cert_free()</b>.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_add_crl_dp_uri (hx509_contextcontext, hx509_ca_tbstbs, const char *uri, hx509_nameissuername)</h3>

 Add CRL distribution point URI to the to-be-signed certificate object. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>uri</i> uri to the CRL. 
 <i>issuername</i> name of the issuer.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 issuername not supported

<h3>int hx509_ca_tbs_add_eku (hx509_contextcontext, hx509_ca_tbstbs, const heim_oid *oid)</h3>

 An an extended key usage to the to-be-signed certificate object. Duplicates will detected and not added. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>oid</i> extended key usage to add.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_add_san_hostname (hx509_contextcontext, hx509_ca_tbstbs, const char *dnsname)</h3>

 Add a Subject Alternative Name hostname to to-be-signed certificate object. A domain match starts with ., an exact match does not. 

 Example of a an domain match: .domain.se matches the hostname host.domain.se. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>dnsname</i> a hostame.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_add_san_jid (hx509_contextcontext, hx509_ca_tbstbs, const char *jid)</h3>

 Add a Jabber/XMPP jid Subject Alternative Name to the to-be-signed certificate object. The jid is an UTF8 string. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>jid</i> string of an a jabber id in UTF8.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_add_san_ms_upn (hx509_contextcontext, hx509_ca_tbstbs, const char *principal)</h3>

 Add Microsoft UPN Subject Alternative Name to the to-be-signed certificate object. The principal string is a UTF8 string. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>principal</i> Microsoft UPN string.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_add_san_otherName (hx509_contextcontext, hx509_ca_tbstbs, const heim_oid *oid, const heim_octet_string *os)</h3>

 Add Subject Alternative Name otherName to the to-be-signed certificate object. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>oid</i> the oid of the OtherName. 
 <i>os</i> data in the other name.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_add_san_pkinit (hx509_contextcontext, hx509_ca_tbstbs, const char *principal)</h3>

 Add Kerberos Subject Alternative Name to the to-be-signed certificate object. The principal string is a UTF8 string. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>principal</i> Kerberos principal to add to the certificate.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_add_san_rfc822name (hx509_contextcontext, hx509_ca_tbstbs, const char *rfc822Name)</h3>

 Add a Subject Alternative Name rfc822 (email address) to to-be-signed certificate object. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>rfc822Name</i> a string to a email address.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>void hx509_ca_tbs_free (hx509_ca_tbs *tbs)</h3>

 Free an To Be Signed object. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>tbs</i> object to free.</dl>
 

 

<h3>int hx509_ca_tbs_init (hx509_contextcontext, hx509_ca_tbs *tbs)</h3>

 Allocate an to-be-signed certificate object that will be converted into an certificate. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> returned to-be-signed certicate object, free with <b>hx509_ca_tbs_free()</b>.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_ca (hx509_contextcontext, hx509_ca_tbstbs, intpathLenConstraint)</h3>

 Make the to-be-signed certificate object a CA certificate. If the pathLenConstraint is negative path length constraint is used. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>pathLenConstraint</i> path length constraint, negative, no constraint.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_domaincontroller (hx509_contextcontext, hx509_ca_tbstbs)</h3>

 Make the to-be-signed certificate object a windows domain controller certificate. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_notAfter (hx509_contextcontext, hx509_ca_tbstbs, time_tt)</h3>

 Set the absolute time when the certificate is valid to. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>t</i> time when the certificate will expire</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_notAfter_lifetime (hx509_contextcontext, hx509_ca_tbstbs, time_tdelta)</h3>

 Set the relative time when the certificiate is going to expire. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>delta</i> seconds to the certificate is going to expire.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_notBefore (hx509_contextcontext, hx509_ca_tbstbs, time_tt)</h3>

 Set the absolute time when the certificate is valid from. If not set the current time will be used. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>t</i> time the certificated will start to be valid</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_proxy (hx509_contextcontext, hx509_ca_tbstbs, intpathLenConstraint)</h3>

 Make the to-be-signed certificate object a proxy certificate. If the pathLenConstraint is negative path length constraint is used. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>pathLenConstraint</i> path length constraint, negative, no constraint.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_serialnumber (hx509_contextcontext, hx509_ca_tbstbs, const heim_integer *serialNumber)</h3>

 Set the serial number to use for to-be-signed certificate object. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>serialNumber</i> serial number to use for the to-be-signed certificate object.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_signature_algorithm (hx509_contextcontext, hx509_ca_tbstbs, const AlgorithmIdentifier *sigalg)</h3>

 Set signature algorithm on the to be signed certificate 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>sigalg</i> signature algorithm to use</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_spki (hx509_contextcontext, hx509_ca_tbstbs, const SubjectPublicKeyInfo *spki)</h3>

 Set the subject public key info (SPKI) in the to-be-signed certificate object. SPKI is the public key and key related parameters in the certificate. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>spki</i> subject public key info to use for the to-be-signed certificate object.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_subject (hx509_contextcontext, hx509_ca_tbstbs, hx509_namesubject)</h3>

 Set the subject name of a to-be-signed certificate object. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>subject</i> the name to set a subject.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_template (hx509_contextcontext, hx509_ca_tbstbs, intflags, hx509_certcert)</h3>

 Initialize the to-be-signed certificate object from a template certifiate. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>flags</i> bit field selecting what to copy from the template certifiate. 
 <i>cert</i> template certificate.</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_set_unique (hx509_contextcontext, hx509_ca_tbstbs, const heim_bit_string *subjectUniqueID, const heim_bit_string *issuerUniqueID)</h3>

 Set the issuerUniqueID and subjectUniqueID 

 These are only supposed to be used considered with version 2 certificates, replaced by the two extensions SubjectKeyIdentifier and IssuerKeyIdentifier. This function is to allow application using legacy protocol to issue them. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>issuerUniqueID</i> to be set 
 <i>subjectUniqueID</i> to be set</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>int hx509_ca_tbs_subject_expand (hx509_contextcontext, hx509_ca_tbstbs, hx509_envenv)</h3>

 Expand the the subject name in the to-be-signed certificate object using <b>hx509_name_expand()</b>. 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>context</i> A hx509 context. 
 <i>tbs</i> object to be signed. 
 <i>env</i> enviroment variable to expand variables in the subject name, see hx509_env_init().</dl>
 

 <b>Returns:</b>
<dl>
<dt>
<dd> An hx509 error code, see <b>hx509_get_error_string()</b>.</dl>
 

 

<h3>struct units * hx509_ca_tbs_template_units (void)</h3>

 Make of template units, use to build flags argument to <b>hx509_ca_tbs_set_template()</b> with parse_units(). 

 <b>Returns:</b>
<dl>
<dt>
<dd> an units structure.</dl>
 

 

<h2>Author</h2>

 

 Generated automatically by Doxygen for Heimdalx509library from the source code. 

<h2>Index</h2>


