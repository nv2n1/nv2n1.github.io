---

title: "hx509_ca_tbs_set_notbefore(3)"
name: "hx509_ca_tbs_set_notbefore"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hx509_ca_tbs_set_notbefore/"
---

<p> hx509 CA functions &#8211; </p>
<h3>Functions</h3>
<p> <br/>
 int <code>hx509_ca_tbs_init</code> (hx509_context context, hx509_ca_tbs *tbs) <br/>
 <br/>
 void <code>hx509_ca_tbs_free</code> (hx509_ca_tbs *tbs) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_notBefore</code> (hx509_context context, hx509_ca_tbs tbs, time_t t) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_notAfter</code> (hx509_context context, hx509_ca_tbs tbs, time_t t) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_notAfter_lifetime</code> (hx509_context context, hx509_ca_tbs tbs, time_t delta) <br/>
 <br/>
 struct units * <code>hx509_ca_tbs_template_units</code> (void) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_template</code> (hx509_context context, hx509_ca_tbs tbs, int flags, hx509_cert cert) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_ca</code> (hx509_context context, hx509_ca_tbs tbs, int pathLenConstraint) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_proxy</code> (hx509_context context, hx509_ca_tbs tbs, int pathLenConstraint) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_domaincontroller</code> (hx509_context context, hx509_ca_tbs tbs) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_spki</code> (hx509_context context, hx509_ca_tbs tbs, const SubjectPublicKeyInfo *spki) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_serialnumber</code> (hx509_context context, hx509_ca_tbs tbs, const heim_integer *serialNumber) <br/>
 <br/>
 int <code>hx509_ca_tbs_add_eku</code> (hx509_context context, hx509_ca_tbs tbs, const heim_oid *oid) <br/>
 <br/>
 int <code>hx509_ca_tbs_add_crl_dp_uri</code> (hx509_context context, hx509_ca_tbs tbs, const char *uri, hx509_name issuername) <br/>
 <br/>
 int <code>hx509_ca_tbs_add_san_otherName</code> (hx509_context context, hx509_ca_tbs tbs, const heim_oid *oid, const heim_octet_string *os) <br/>
 <br/>
 int <code>hx509_ca_tbs_add_san_pkinit</code> (hx509_context context, hx509_ca_tbs tbs, const char *principal) <br/>
 <br/>
 int <code>hx509_ca_tbs_add_san_ms_upn</code> (hx509_context context, hx509_ca_tbs tbs, const char *principal) <br/>
 <br/>
 int <code>hx509_ca_tbs_add_san_jid</code> (hx509_context context, hx509_ca_tbs tbs, const char *jid) <br/>
 <br/>
 int <code>hx509_ca_tbs_add_san_hostname</code> (hx509_context context, hx509_ca_tbs tbs, const char *dnsname) <br/>
 <br/>
 int <code>hx509_ca_tbs_add_san_rfc822name</code> (hx509_context context, hx509_ca_tbs tbs, const char *rfc822Name) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_subject</code> (hx509_context context, hx509_ca_tbs tbs, hx509_name subject) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_unique</code> (hx509_context context, hx509_ca_tbs tbs, const heim_bit_string *subjectUniqueID, const heim_bit_string *issuerUniqueID) <br/>
 <br/>
 int <code>hx509_ca_tbs_subject_expand</code> (hx509_context context, hx509_ca_tbs tbs, hx509_env env) <br/>
 <br/>
 int <code>hx509_ca_tbs_set_signature_algorithm</code> (hx509_context context, hx509_ca_tbs tbs, const AlgorithmIdentifier *sigalg) <br/>
 <br/>
 int <code>hx509_ca_sign</code> (hx509_context context, hx509_ca_tbs tbs, hx509_cert signer, hx509_cert *certificate) <br/>
 <br/>
 int <code>hx509_ca_sign_self</code> (hx509_context context, hx509_ca_tbs tbs, hx509_private_key signer, hx509_cert *certificate) <br/>
  </p>
<h2>Detailed Description</h2>
<p> See the <code>Hx509 CA functions</code> for description and examples.  </p>
<h2>Function Documentation</h2>
<h3>int hx509_ca_sign (hx509_contextcontext, hx509_ca_tbstbs, hx509_certsigner, hx509_cert *certificate)</h3>
<p> Sign a to-be-signed certificate object with a issuer certificate. </p>
<p> The caller needs to at least have called the following functions on the to-be-signed certificate object: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>hx509_ca_tbs_init()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>hx509_ca_tbs_set_subject()</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>hx509_ca_tbs_set_spki()</code> </p>
 </dd></dl>
<p> When done the to-be-signed certificate object should be freed with <code>hx509_ca_tbs_free()</code>. </p>
<p> When creating self-signed certificate use <code>hx509_ca_sign_self()</code> instead. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>signer</i> the CA certificate object to sign with (need private key). <br/>
 <i>certificate</i> return cerificate, free with <code>hx509_cert_free()</code>. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_sign_self (hx509_contextcontext, hx509_ca_tbstbs, hx509_private_keysigner, hx509_cert *certificate)</h3>
<p> Work just like <code>hx509_ca_sign()</code> but signs it-self. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>signer</i> private key to sign with. <br/>
 <i>certificate</i> return cerificate, free with <code>hx509_cert_free()</code>. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_add_crl_dp_uri (hx509_contextcontext, hx509_ca_tbstbs, const char *uri, hx509_nameissuername)</h3>
<p> Add CRL distribution point URI to the to-be-signed certificate object. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>uri</i> uri to the CRL. <br/>
 <i>issuername</i> name of the issuer. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<p> issuername not supported  </p>
<h3>int hx509_ca_tbs_add_eku (hx509_contextcontext, hx509_ca_tbstbs, const heim_oid *oid)</h3>
<p> An an extended key usage to the to-be-signed certificate object. Duplicates will detected and not added. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>oid</i> extended key usage to add. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_add_san_hostname (hx509_contextcontext, hx509_ca_tbstbs, const char *dnsname)</h3>
<p> Add a Subject Alternative Name hostname to to-be-signed certificate object. A domain match starts with ., an exact match does not. </p>
<p> Example of a an domain match: .domain.se matches the hostname host.domain.se. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>dnsname</i> a hostame. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_add_san_jid (hx509_contextcontext, hx509_ca_tbstbs, const char *jid)</h3>
<p> Add a Jabber/XMPP jid Subject Alternative Name to the to-be-signed certificate object. The jid is an UTF8 string. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>jid</i> string of an a jabber id in UTF8. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_add_san_ms_upn (hx509_contextcontext, hx509_ca_tbstbs, const char *principal)</h3>
<p> Add Microsoft UPN Subject Alternative Name to the to-be-signed certificate object. The principal string is a UTF8 string. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>principal</i> Microsoft UPN string. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_add_san_otherName (hx509_contextcontext, hx509_ca_tbstbs, const heim_oid *oid, const heim_octet_string *os)</h3>
<p> Add Subject Alternative Name otherName to the to-be-signed certificate object. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>oid</i> the oid of the OtherName. <br/>
 <i>os</i> data in the other name. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_add_san_pkinit (hx509_contextcontext, hx509_ca_tbstbs, const char *principal)</h3>
<p> Add Kerberos Subject Alternative Name to the to-be-signed certificate object. The principal string is a UTF8 string. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>principal</i> Kerberos principal to add to the certificate. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_add_san_rfc822name (hx509_contextcontext, hx509_ca_tbstbs, const char *rfc822Name)</h3>
<p> Add a Subject Alternative Name rfc822 (email address) to to-be-signed certificate object. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>rfc822Name</i> a string to a email address. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>void hx509_ca_tbs_free (hx509_ca_tbs *tbs)</h3>
<p> Free an To Be Signed object. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>tbs</i> object to free. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_init (hx509_contextcontext, hx509_ca_tbs *tbs)</h3>
<p> Allocate an to-be-signed certificate object that will be converted into an certificate. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> returned to-be-signed certicate object, free with <code>hx509_ca_tbs_free()</code>. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_ca (hx509_contextcontext, hx509_ca_tbstbs, intpathLenConstraint)</h3>
<p> Make the to-be-signed certificate object a CA certificate. If the pathLenConstraint is negative path length constraint is used. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>pathLenConstraint</i> path length constraint, negative, no constraint. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_domaincontroller (hx509_contextcontext, hx509_ca_tbstbs)</h3>
<p> Make the to-be-signed certificate object a windows domain controller certificate. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_notAfter (hx509_contextcontext, hx509_ca_tbstbs, time_tt)</h3>
<p> Set the absolute time when the certificate is valid to. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>t</i> time when the certificate will expire </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_notAfter_lifetime (hx509_contextcontext, hx509_ca_tbstbs, time_tdelta)</h3>
<p> Set the relative time when the certificiate is going to expire. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>delta</i> seconds to the certificate is going to expire. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_notBefore (hx509_contextcontext, hx509_ca_tbstbs, time_tt)</h3>
<p> Set the absolute time when the certificate is valid from. If not set the current time will be used. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>t</i> time the certificated will start to be valid </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_proxy (hx509_contextcontext, hx509_ca_tbstbs, intpathLenConstraint)</h3>
<p> Make the to-be-signed certificate object a proxy certificate. If the pathLenConstraint is negative path length constraint is used. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>pathLenConstraint</i> path length constraint, negative, no constraint. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_serialnumber (hx509_contextcontext, hx509_ca_tbstbs, const heim_integer *serialNumber)</h3>
<p> Set the serial number to use for to-be-signed certificate object. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>serialNumber</i> serial number to use for the to-be-signed certificate object. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_signature_algorithm (hx509_contextcontext, hx509_ca_tbstbs, const AlgorithmIdentifier *sigalg)</h3>
<p> Set signature algorithm on the to be signed certificate </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>sigalg</i> signature algorithm to use </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_spki (hx509_contextcontext, hx509_ca_tbstbs, const SubjectPublicKeyInfo *spki)</h3>
<p> Set the subject public key info (SPKI) in the to-be-signed certificate object. SPKI is the public key and key related parameters in the certificate. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>spki</i> subject public key info to use for the to-be-signed certificate object. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_subject (hx509_contextcontext, hx509_ca_tbstbs, hx509_namesubject)</h3>
<p> Set the subject name of a to-be-signed certificate object. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>subject</i> the name to set a subject. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_template (hx509_contextcontext, hx509_ca_tbstbs, intflags, hx509_certcert)</h3>
<p> Initialize the to-be-signed certificate object from a template certifiate. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>flags</i> bit field selecting what to copy from the template certifiate. <br/>
 <i>cert</i> template certificate. </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_set_unique (hx509_contextcontext, hx509_ca_tbstbs, const heim_bit_string *subjectUniqueID, const heim_bit_string *issuerUniqueID)</h3>
<p> Set the issuerUniqueID and subjectUniqueID </p>
<p> These are only supposed to be used considered with version 2 certificates, replaced by the two extensions SubjectKeyIdentifier and IssuerKeyIdentifier. This function is to allow application using legacy protocol to issue them. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>issuerUniqueID</i> to be set <br/>
 <i>subjectUniqueID</i> to be set </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>int hx509_ca_tbs_subject_expand (hx509_contextcontext, hx509_ca_tbstbs, hx509_envenv)</h3>
<p> Expand the the subject name in the to-be-signed certificate object using <code>hx509_name_expand()</code>. </p>
<p> <code>Parameters:</code> </p>
<dl>
<dd> <p> <i>context</i> A hx509 context. <br/>
 <i>tbs</i> object to be signed. <br/>
 <i>env</i> enviroment variable to expand variables in the subject name, see hx509_env_init(). </p>
 </dd></dl>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> An hx509 error code, see <code>hx509_get_error_string()</code>. </p>
 </dd></dl>
<h3>struct units * hx509_ca_tbs_template_units (void)</h3>
<p> Make of template units, use to build flags argument to <code>hx509_ca_tbs_set_template()</code> with parse_units(). </p>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> an units structure. </p>
 </dd></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Heimdalx509library from the source code. </p>
