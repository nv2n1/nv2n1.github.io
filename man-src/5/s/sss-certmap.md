---
title: "sss-certmap(5)"
name: "sss-certmap"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sss-certmap/"
description: "sss-certmap – SSSD Certificate Matching and Mapping Rules"
---

<p>sss-certmap &#8211; SSSD Certificate Matching and Mapping Rules</p>
<h2>Description</h2>
<p>The manual page describes the rules which can be used by SSSD and other components to match X.509 certificates and map them to accounts. </p>
<p> Each rule has four components, a &#8220;priority&#8221;, a &#8220;matching rule&#8221;, a &#8220;mapping rule&#8221; and a &#8220;domain list&#8221;. All components are optional. A missing &#8220;priority&#8221; will add the rule with the lowest priority. The default &#8220;matching rule&#8221; will match certificates with the digitalSignature key usage and clientAuth extended key usage. If the &#8220;mapping rule&#8221; is empty the certificates will be searched in the userCertificate attribute as DER encoded binary. If no domains are given only the local domain will be searched.</p>
<h2>Rule Components</h2>
<h3>Priority</h3>
<p>The rules are process by priority while the number &#8216;0&#8217; (zero) indicates the highest priority. The higher the number the lower is the priority. A missing value indicates the lowest priority. </p>
<p> Internally the priority is treated as unsigned 32bit integer, using a priority value larger than 4294967295 will cause an error.</p>
<h3>Matching Rule</h3>
<p>The matching rule is used to select a certificate to which the mapping rule should be applied. It uses a system similar to the one used by &#8220;pkinit_cert_match&#8221; option of MIT Kerberos. It consists of a keyword enclosed by &#8216;&lt;&#8216; and &#8216;&gt;&#8217; which identified a certain part of the certificate and a pattern which should be found for the rule to match. Multiple keyword pattern pairs can be either joined with &#8216;&amp;&amp;&#8217; (and) or &#8216;||&#8217; (or). </p>
<p> The available options are: </p>
<p> &lt;SUBJECT&gt;regular-expression</p>
<dl>
<dd>With this a part or the whole subject name of the certificate can be matched. For the matching POSIX Extended Regular Expression syntax is used, see <a href="/docs/linux/man/7-regex/">regex</a>(7) for details. </p>
<p> For the matching the subject name stored in the certificate in DER encoded ASN.1 is converted into a string according to RFC 4514. This means the most specific name component comes first. Please note that not all possible attribute names are covered by RFC 4514. The names included are &#8216;CN&#8217;, &#8216;L&#8217;, &#8216;ST&#8217;, &#8216;O&#8217;, &#8216;OU&#8217;, &#8216;C&#8217;, &#8216;STREET&#8217;, &#8216;DC&#8217; and &#8216;UID&#8217;. Other attribute names might be shown differently on different platform and by different tools. To avoid confusion those attribute names are best not used or covered by a suitable regular-expression. </p>
<p> Example: &lt;SUBJECT&gt;.*,DC=MY,DC=DOMAIN</dl>
<p> &lt;ISSUER&gt;regular-expression</p>
<dl>
<dd>With this a part or the whole issuer name of the certificate can be matched. All comments for &lt;SUBJECT&gt; apply her as well. </p>
<p> Example: &lt;ISSUER&gt;^CN=My-CA,DC=MY,DC=DOMAIN$</dl>
<p> &lt;KU&gt;key-usage</p>
<dl>
<dd>This option can be used to specify which key usage values the certificate should have. The following value can be used in a comma separate list: </p>
<dl>
<dd>&bull; digitalSignature</dl>
<dl>
<dd>&bull; nonRepudiation</dl>
<dl>
<dd>&bull; keyEncipherment</dl>
<dl>
<dd>&bull; dataEncipherment</dl>
<dl>
<dd>&bull; keyAgreement</dl>
<dl>
<dd>&bull; keyCertSign</dl>
<dl>
<dd>&bull; cRLSign</dl>
<dl>
<dd>&bull; encipherOnly</dl>
<dl>
<dd>&bull; decipherOnly</dl>
<p> A numerical value in the range of a 32bit unsigned integer can be used as well to cover special use cases. </p>
<p> Example: &lt;KU&gt;digitalSignature,keyEncipherment</dl>
<p> &lt;EKU&gt;extended-key-usage</p>
<dl>
<dd>This option can be used to specify which extended key usage the certificate should have. The following value can be used in a comma separated list: </p>
<dl>
<dd>&bull; serverAuth</dl>
<dl>
<dd>&bull; clientAuth</dl>
<dl>
<dd>&bull; codeSigning</dl>
<dl>
<dd>&bull; emailProtection</dl>
<dl>
<dd>&bull; timeStamping</dl>
<dl>
<dd>&bull; OCSPSigning</dl>
<dl>
<dd>&bull; KPClientAuth</dl>
<dl>
<dd>&bull; pkinit</dl>
<dl>
<dd>&bull; msScLogin</dl>
<p> Extended key usages which are not listed above can be specified with their OID in dotted-decimal notation. </p>
<p> Example: &lt;EKU&gt;clientAuth,1.3.6.1.5.2.3.4</dl>
<p> &lt;SAN&gt;regular-expression</p>
<dl>
<dd>To be compatible with the usage of MIT Kerberos this option will match the Kerberos principals in the PKINIT or AD NT Principal SAN as &lt;SAN:Principal&gt; does. </p>
<p> Example: &lt;SAN&gt;.*@MY\.REALM</dl>
<p> &lt;SAN:Principal&gt;regular-expression</p>
<dl>
<dd>Match the Kerberos principals in the PKINIT or AD NT Principal SAN. </p>
<p> Example: &lt;SAN:Principal&gt;.*@MY\.REALM</dl>
<p> &lt;SAN:ntPrincipalName&gt;regular-expression</p>
<dl>
<dd>Match the Kerberos principals from the AD NT Principal SAN. </p>
<p> Example: &lt;SAN:ntPrincipalName&gt;.*@MY.AD.REALM</dl>
<p> &lt;SAN:pkinit&gt;regular-expression</p>
<dl>
<dd>Match the Kerberos principals from the PKINIT SAN. </p>
<p> Example: &lt;SAN:ntPrincipalName&gt;.*@MY\.PKINIT\.REALM</dl>
<p> &lt;SAN:dotted-decimal-oid&gt;regular-expression</p>
<dl>
<dd>Take the value of the otherName SAN component given by the OID in dotted-decimal notation, interpret it as string and try to match it against the regular expression. </p>
<p> Example: &lt;SAN:1.2.3.4&gt;test</dl>
<p> &lt;SAN:otherName&gt;base64-string</p>
<dl>
<dd>Do a binary match with the base64 encoded blob against all otherName SAN components. With this option it is possible to match against custom otherName components with special encodings which could not be treated as strings. </p>
<p> Example: &lt;SAN:otherName&gt;MTIz</dl>
<p> &lt;SAN:rfc822Name&gt;regular-expression</p>
<dl>
<dd>Match the value of the rfc822Name SAN. </p>
<p> Example: &lt;SAN:rfc822Name&gt;.*@email\.domain</dl>
<p> &lt;SAN:dNSName&gt;regular-expression</p>
<dl>
<dd>Match the value of the dNSName SAN. </p>
<p> Example: &lt;SAN:dNSName&gt;.*\.my\.dns\.domain</dl>
<p> &lt;SAN:x400Address&gt;base64-string</p>
<dl>
<dd>Binary match the value of the x400Address SAN. </p>
<p> Example: &lt;SAN:x400Address&gt;MTIz</dl>
<p> &lt;SAN:directoryName&gt;regular-expression</p>
<dl>
<dd>Match the value of the directoryName SAN. The same comments as given for &lt;ISSUER&gt; and &lt;SUBJECT&gt; apply here as well. </p>
<p> Example: &lt;SAN:directoryName&gt;.*,DC=com</dl>
<p> &lt;SAN:ediPartyName&gt;base64-string</p>
<dl>
<dd>Binary match the value of the ediPartyName SAN. </p>
<p> Example: &lt;SAN:ediPartyName&gt;MTIz</dl>
<p> &lt;SAN:uniformResourceIdentifier&gt;regular-expression</p>
<dl>
<dd>Match the value of the uniformResourceIdentifier SAN. </p>
<p> Example: &lt;SAN:uniformResourceIdentifier&gt;URN:.*</dl>
<p> &lt;SAN:iPAddress&gt;regular-expression</p>
<dl>
<dd>Match the value of the iPAddress SAN. </p>
<p> Example: &lt;SAN:iPAddress&gt;192\.168\..*</dl>
<p> &lt;SAN:registeredID&gt;regular-expression</p>
<dl>
<dd>Match the value of the registeredID SAN as dotted-decimal string. </p>
<p> Example: &lt;SAN:registeredID&gt;1\.2\.3\..*</dl>
<h3>Mapping Rule</h3>
<p>The mapping rule is used to associate a certificate with one or more accounts. A Smartcard with the certificate and the matching private key can then be used to authenticate as one of those accounts. </p>
<p> Currently SSSD basically only supports LDAP to lookup user information (the exception is the proxy provider which is not of relevance here). Because of this the mapping rule is based on LDAP search filter syntax with templates to add certificate content to the filter. It is expected that the filter will only contain the specific data needed for the mapping an that the caller will embed it in another filter to do the actual search. Because of this the filter string should start and stop with &#8216;(&#8216; and &#8216;)&#8217; respectively. </p>
<p> In general it is recommended to use attributes from the certificate and add them to special attributes to the LDAP user object. E.g. the &#8216;altSecurityIdentities&#8217; attribute in AD or the &#8216;ipaCertMapData&#8217; attribute for IPA can be used. </p>
<p> This should be preferred to read user specific data from the certificate like e.g. an email address and search for it in the LDAP server. The reason is that the user specific data in LDAP might change for various reasons would would break the mapping. On the other hand it would be hard to break the mapping on purpose for a specific user. </p>
<p> The templates to add certificate data to the search filter are based on Python-style formatting strings. They consists of a keyword in curly braces with an optional sub-component specifier separated by a &#8216;.&#8217; or an optional conversion/formatting option separated by a &#8216;!&#8217;. Allowed values are: </p>
<p> {issuer_dn[!((ad|ad_x500)|ad_ldap|nss_x500|(nss|nss_ldap))]}</p>
<dl>
<dd>This template will add the full issuer DN converted to a string according to RFC 4514. If X.500 ordering (most specific RDN comes last) an option with the &#8216;_x500&#8217; prefix should be used. </p>
<p> The conversion options starting with &#8216;ad_&#8217; will use attribute names as used by AD, e.g. &#8216;S&#8217; instead of &#8216;ST&#8217;. </p>
<p> The conversion options starting with &#8216;nss_&#8217; will use attribute names as used by NSS. </p>
<p> The default conversion option is &#8216;nss&#8217;, i.e. attribute names according to NSS and LDAP/RFC 4514 ordering. </p>
<p> Example: (ipacertmapdata=X509:&lt;I&gt;{issuer_dn!ad}&lt;S&gt;{subject_dn!ad})</dl>
<p> {subject_dn[!((ad|ad_x500)|ad_ldap|nss_x500|(nss|nss_ldap))]}</p>
<dl>
<dd>This template will add the full subject DN converted to string according to RFC 4514. If X.500 ordering (most specific RDN comes last) an option with the &#8216;_x500&#8217; prefix should be used. </p>
<p> The conversion options starting with &#8216;ad_&#8217; will use attribute names as used by AD, e.g. &#8216;S&#8217; instead of &#8216;ST&#8217;. </p>
<p> The conversion options starting with &#8216;nss_&#8217; will use attribute names as used by NSS. </p>
<p> The default conversion option is &#8216;nss&#8217;, i.e. attribute names according to NSS and LDAP/RFC 4514 ordering. </p>
<p> Example: (ipacertmapdata=X509:&lt;I&gt;{issuer_dn!nss_x500}&lt;S&gt;{subject_dn!nss_x500})</dl>
<p> {cert[!(bin|base64)]}</p>
<dl>
<dd>This template will add the whole DER encoded certificate as a string to the search filter. Depending on the conversion option the binary certificate is either converted to an escaped hex sequence &#8216;
