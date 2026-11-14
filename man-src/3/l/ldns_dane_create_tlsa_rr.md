---
title: "ldns_dane_create_tlsa_rr(3)"
name: "ldns_dane_create_tlsa_rr"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dane_create_tlsa_rr/"
description: "ldns_dane_create_tlsa_owner, ldns_dane_cert2rdf, ldns_dane_select_certificate, ldns_dane_create_tlsa_rr"
---

<h2>NAME</h2>
<p> ldns_dane_create_tlsa_owner, ldns_dane_cert2rdf, ldns_dane_select_certificate, ldns_dane_create_tlsa_rr </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_dane_create_tlsa_owner(ldns_rdf** tlsa_owner, const ldns_rdf* name, uint16_t port, ldns_dane_transport transport); </p>
<p> ldns_status ldns_dane_cert2rdf(ldns_rdf** rdf, X509* cert, ldns_tlsa_selector selector, ldns_tlsa_matching_type matching_type); </p>
<p> ldns_status ldns_dane_select_certificate(X509** selected_cert, X509* cert, STACK_OF(X509)* extra_certs, X509_STORE* pkix_validation_store, ldns_tlsa_certificate_usage cert_usage, int index); </p>
<p> ldns_status ldns_dane_create_tlsa_rr(ldns_rr** tlsa, ldns_tlsa_certificate_usage certificate_usage, ldns_tlsa_selector selector, ldns_tlsa_matching_type matching_type, X509* cert); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dane_create_tlsa_owner</i>()</p>
<dd>Creates a dname consisting of the given name, prefixed by the service port and type of transport: _&lt;EM&gt;port&lt;/EM&gt;._&lt;EM&gt;transport&lt;/EM&gt;.&lt;EM&gt;name&lt;/EM&gt;. </p>
<p> .br <code>tlsa_owner</code>: The created dname. .br <code>name</code>: The dname that should be prefixed. .br <code>port</code>: The service port number for wich the name should be created. .br <code>transport</code>: The transport for wich the name should be created. .br Returns LDNS_STATUS_OK on success or an error code otherwise.</dl>
<dl>
<dt> <i>ldns_dane_cert2rdf</i>()</p>
<dd>Creates a LDNS_RDF_TYPE_HEX type rdf based on the binary data choosen by the selector and encoded using matching_type. </p>
<p> .br <code>rdf</code>: The created created rdf of type LDNS_RDF_TYPE_HEX. .br <code>cert</code>: The certificate from which the data is selected .br <code>selector</code>: The full certificate or the public key .br <code>matching_type</code>: The full data or the SHA256 or SHA512 hash of the selected data .br Returns LDNS_STATUS_OK on success or an error code otherwise.</dl>
<dl>
<dt> <i>ldns_dane_select_certificate</i>()</p>
<dd>Selects the certificate from cert, extra_certs or the pkix_validation_store based on the value of cert_usage and index. </p>
<p> .br <code>selected_cert</code>: The selected cert. .br <code>cert</code>: The certificate to validate (or not) .br <code>extra_certs</code>: Intermediate certificates that might be necessary during validation. May be NULL, except when the certificate usage is &quot;Trust Anchor Assertion&quot; because the trust anchor has to be provided.(otherwise choose a &quot;Domain issued certificate!&quot; .br <code>pkix_validation_store</code>: Used when the certificate usage is &quot;CA constraint&quot; or &quot;Service Certificate Constraint&quot; to validate the certificate and, in case of &quot;CA constraint&quot;, select the CA. When pkix_validation_store is NULL, validation is explicitely turned off and the behaviour is then the same as for &quot;Trust anchor assertion&quot; and &quot;Domain issued certificate&quot; respectively. .br <code>cert_usage</code>: Which certificate to use and how to validate. .br <code>index</code>: Used to select the trust anchor when certificate usage is &quot;Trust Anchor Assertion&quot;. 0 is the last certificate in the validation chain. 1 the one but last, etc. When index is -1, the last certificate is used that MUST be self-signed. This can help to make sure that the intended (self signed) trust anchor is actually present in extra_certs (which is a DANE requirement). </p>
<p> .br Returns LDNS_STATUS_OK on success or an error code otherwise.</dl>
<dl>
<dt> <i>ldns_dane_create_tlsa_rr</i>()</p>
<dd>Creates a TLSA resource record from the certificate. No PKIX validation is performed! The given certificate is used as data regardless the value of certificate_usage. </p>
<p> .br <code>tlsa</code>: The created TLSA resource record. .br <code>certificate_usage</code>: The value for the Certificate Usage field .br <code>selector</code>: The value for the Selector field .br <code>matching_type</code>: The value for the Matching Type field .br <code>cert</code>: The certificate which data will be represented </p>
<p> .br Returns LDNS_STATUS_OK on success or an error code otherwise.</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dane_verify</i>, <i>ldns_dane_verify_rr</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
