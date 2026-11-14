---
title: "ldns_dane_verify(3)"
name: "ldns_dane_verify"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dane_verify/"
description: "ldns_dane_verify, ldns_dane_verify_rr"
---

<h2>NAME</h2>
<p> ldns_dane_verify, ldns_dane_verify_rr </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_dane_verify(ldns_rr_list* tlsas, X509* cert, STACK_OF(X509)* extra_certs, X509_STORE* pkix_validation_store); </p>
<p> ldns_status ldns_dane_verify_rr(const ldns_rr* tlsa_rr, X509* cert, STACK_OF(X509)* extra_certs, X509_STORE* pkix_validation_store); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dane_verify</i>()</p>
<dd>Verify if any of the given TLSA resource records matches the given certificate. </p>
<p> .br <code>tlsas</code>: The resource records that specify what and how to match the certificate. One must match for this function to succeed. With tlsas == NULL or the number of TLSA records in tlsas == 0, regular PKIX validation is performed. .br <code>cert</code>: The certificate to match (and validate) .br <code>extra_certs</code>: Intermediate certificates that might be necessary creating the validation chain. .br <code>pkix_validation_store</code>: Used when the certificate usage is &quot;CA constraint&quot; or &quot;Service Certificate Constraint&quot; to validate the certificate. </p>
<p> .br Returns LDNS_STATUS_OK on success, LDNS_STATUS_DANE_PKIX_DID_NOT_VALIDATE when one of the TLSA&#8217;s matched but the PKIX validation failed, LDNS_STATUS_DANE_TLSA_DID_NOT_MATCH when none of the TLSA&#8217;s matched, or other ldns_status errors.</dl>
<dl>
<dt> <i>ldns_dane_verify_rr</i>()</p>
<dd>Verify if the given TLSA resource record matches the given certificate. Reporting on a TLSA rr mismatch (LDNS_STATUS_DANE_TLSA_DID_NOT_MATCH) is preferred over PKIX failure (LDNS_STATUS_DANE_PKIX_DID_NOT_VALIDATE). So when PKIX validation is required by the TLSA Certificate usage, but the TLSA data does not match, LDNS_STATUS_DANE_TLSA_DID_NOT_MATCH is returned whether the PKIX validated or not. </p>
<p> .br <code>tlsa_rr</code>: The resource record that specifies what and how to match the certificate. With tlsa_rr == NULL, regular PKIX validation is performed. .br <code>cert</code>: The certificate to match (and validate) .br <code>extra_certs</code>: Intermediate certificates that might be necessary creating the validation chain. .br <code>pkix_validation_store</code>: Used when the certificate usage is &quot;CA constraint&quot; or &quot;Service Certificate Constraint&quot; to validate the certificate. </p>
<p> .br Returns LDNS_STATUS_OK on success, LDNS_STATUS_DANE_TLSA_DID_NOT_MATCH on TLSA data mismatch, LDNS_STATUS_DANE_PKIX_DID_NOT_VALIDATE when TLSA matched, but the PKIX validation failed, or other ldns_status errors.</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dane_create_tlsa_owner</i>, <i>ldns_dane_cert2rdf</i>, <i>ldns_dane_select_certificate</i>, <i>ldns_dane_create_tlsa_rr</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
