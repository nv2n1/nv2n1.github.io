---
title: "globus_gsi_cert_utils_error_success(3)"
name: "globus_gsi_cert_utils_error_success"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_cert_utils_error_success/"
description: "Cert Utils Constants –"
---

<p>Cert Utils Constants &#8211; </p>
<h3>Typedefs</h3>
<p>typedef enum<br />
 <code>globus_gsi_cert_utils_cert_type_e</code> <code>globus_gsi_cert_utils_cert_type_t</code>&quot; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_gsi_cert_utils_error_t</code> { <code>GLOBUS_GSI_CERT_UTILS_ERROR_SUCCESS</code> = 0, <code>GLOBUS_GSI_CERT_UTILS_ERROR_GETTING_NAME_ENTRY_OF_SUBJECT</code> = 1, <code>GLOBUS_GSI_CERT_UTILS_ERROR_COPYING_SUBJECT</code> = 2, <code>GLOBUS_GSI_CERT_UTILS_ERROR_GETTING_CN_ENTRY</code> = 3, <code>GLOBUS_GSI_CERT_UTILS_ERROR_ADDING_CN_TO_SUBJECT</code> = 4, <code>GLOBUS_GSI_CERT_UTILS_ERROR_OUT_OF_MEMORY</code> = 5, <code>GLOBUS_GSI_CERT_UTILS_ERROR_UNEXPECTED_FORMAT</code> = 6, <code>GLOBUS_GSI_CERT_UTILS_ERROR_NON_COMPLIANT_PROXY</code> = 7, <code>GLOBUS_GSI_CERT_UTILS_ERROR_DETERMINING_CERT_TYPE</code> = 8, <code>GLOBUS_GSI_CERT_UTILS_ERROR_LAST</code> = 9 } </p>
<p> enum <code>globus_gsi_cert_utils_cert_type_e</code> { <code>GLOBUS_GSI_CERT_UTILS_TYPE_DEFAULT</code> = 0, <code>GLOBUS_GSI_CERT_UTILS_TYPE_EEC</code> = (1 &lt;&lt; 0), <code>GLOBUS_GSI_CERT_UTILS_TYPE_CA</code> = (1 &lt;&lt; 1), <code>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_2</code> = (1 &lt;&lt; 2), <code>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3</code> = (1 &lt;&lt; 3), <code>GLOBUS_GSI_CERT_UTILS_TYPE_RFC</code> = (1 &lt;&lt; 4), <code>GLOBUS_GSI_CERT_UTILS_TYPE_FORMAT_MASK</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_IMPERSONATION_PROXY</code> = (1 &lt;&lt; 5), <code>GLOBUS_GSI_CERT_UTILS_TYPE_LIMITED_PROXY</code> = (1 &lt;&lt; 6), <code>GLOBUS_GSI_CERT_UTILS_TYPE_RESTRICTED_PROXY</code> = (1 &lt;&lt; 7), <code>GLOBUS_GSI_CERT_UTILS_TYPE_INDEPENDENT_PROXY</code> = (1 &lt;&lt; 8), <code>GLOBUS_GSI_CERT_UTILS_TYPE_PROXY_MASK</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3_IMPERSONATION_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3_INDEPENDENT_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3_LIMITED_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3_RESTRICTED_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_2_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_2_LIMITED_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_RFC_IMPERSONATION_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_RFC_INDEPENDENT_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_RFC_LIMITED_PROXY</code>, <code>GLOBUS_GSI_CERT_UTILS_TYPE_RFC_RESTRICTED_PROXY</code> } </p>
<h2>Detailed Description</h2>
<h2>Typedef Documentation</h2>
<h3>typedef enum <code>globus_gsi_cert_utils_cert_type_e</code> <code>globus_gsi_cert_utils_cert_type_t</code></h3>
<p>Certificate Types. </p>
<p> These certificate types are used to describe some properties of a certificate and to specify what type of proxy should be generated in the proxy core code. There are two non-proxy types of certificates understood by Globus: EEC (End-Entity Certificate) and CA (Certificate Authority Certificates), three proxy formats (GSI 2 &#8216;legacy&#8217; proxies, GSI 3 &#8216;Draft&#8217; proxies, and RFC 3820-compliant proxies), and four types of proxy (limited, impersonation &#8216;full&#8217;, restricted, and independent). The latter two types are not expressible in the GSI 2 format. </p>
<p> In addition to enumerations for the concrete renderings of certificate format and type combined, there are default, formats-without-types and types-without-formats so that application logic which uses the proxy library can request default proxy formats which are compatible with the issuing certificate.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_gsi_cert_utils_cert_type_e</code></h3>
<p>Certificate Types. </p>
<p> These certificate types are used to describe some properties of a certificate and to specify what type of proxy should be generated in the proxy core code. There are two non-proxy types of certificates understood by Globus: EEC (End-Entity Certificate) and CA (Certificate Authority Certificates), three proxy formats (GSI 2 &#8216;legacy&#8217; proxies, GSI 3 &#8216;Draft&#8217; proxies, and RFC 3820-compliant proxies), and four types of proxy (limited, impersonation &#8216;full&#8217;, restricted, and independent). The latter two types are not expressible in the GSI 2 format. </p>
<p> In addition to enumerations for the concrete renderings of certificate format and type combined, there are default, formats-without-types and types-without-formats so that application logic which uses the proxy library can request default proxy formats which are compatible with the issuing certificate. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_DEFAULT </i></p>
<dd>Default proxy type</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_EEC </i></p>
<dd>A end entity certificate</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_CA </i></p>
<dd>A CA certificate</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_2 </i></p>
<dd>Legacy Proxy Format</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3 </i></p>
<dd>X.509 Proxy Certificate Profile (draft) Proxy Format</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_RFC </i></p>
<dd>X.509 Proxy Certificate Profile Compliant Proxy Format</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_FORMAT_MASK </i></p>
<dd>Proxy certificate formats mask</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_IMPERSONATION_PROXY </i></p>
<dd>Impersonation proxy type</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_LIMITED_PROXY </i></p>
<dd>Limited proxy type</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_RESTRICTED_PROXY </i></p>
<dd>Restricted proxy type</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_INDEPENDENT_PROXY </i></p>
<dd>Independent proxy type</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_PROXY_MASK </i></p>
<dd>Proxy types mask</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3_IMPERSONATION_PROXY </i></p>
<dd>A X.509 Proxy Certificate Profile (pre-RFC) compliant impersonation proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3_INDEPENDENT_PROXY </i></p>
<dd>A X.509 Proxy Certificate Profile (pre-RFC) compliant independent proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3_LIMITED_PROXY </i></p>
<dd>A X.509 Proxy Certificate Profile (pre-RFC) compliant limited proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_3_RESTRICTED_PROXY </i></p>
<dd>A X.509 Proxy Certificate Profile (pre-RFC) compliant restricted proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_2_PROXY </i></p>
<dd>A legacy Globus impersonation proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_GSI_2_LIMITED_PROXY </i></p>
<dd>A legacy Globus limited impersonation proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_RFC_IMPERSONATION_PROXY </i></p>
<dd>A X.509 Proxy Certificate Profile RFC compliant impersonation proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_RFC_INDEPENDENT_PROXY </i></p>
<dd>A X.509 Proxy Certificate Profile RFC compliant independent proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_RFC_LIMITED_PROXY </i></p>
<dd>A X.509 Proxy Certificate Profile RFC compliant limited proxy</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_TYPE_RFC_RESTRICTED_PROXY </i></p>
<dd>A X.509 Proxy Certificate Profile RFC compliant restricted proxy</dl>
<h3>enum <code>globus_gsi_cert_utils_error_t</code></h3>
<p>Cert Utils Error Codes </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_SUCCESS </i></p>
<dd>Success &#8211; never used</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_GETTING_NAME_ENTRY_OF_SUBJECT </i></p>
<dd>Failed to retrieve a subcomponent of the subject</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_COPYING_SUBJECT </i></p>
<dd>A error occured while trying to copy a X.509 subject</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_GETTING_CN_ENTRY </i></p>
<dd>Failed to retrieve a CN subcomponent of the subject</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_ADDING_CN_TO_SUBJECT </i></p>
<dd>Failed to add a CN component to a X.509 subject name</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_OUT_OF_MEMORY </i></p>
<dd>Out of memory</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_UNEXPECTED_FORMAT </i></p>
<dd>Something unexpected happen while converting a string subject to a X509_NAME structure</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_NON_COMPLIANT_PROXY </i></p>
<dd>Proxy does not comply with the expected format</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_DETERMINING_CERT_TYPE </i></p>
<dd>Couldn&#8217;t dtermine the certificate type</p>
<dt><i>GLOBUS_GSI_CERT_UTILS_ERROR_LAST </i></p>
<dd>Last marker &#8211; never used</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_cert_utils from the source code.</p>
