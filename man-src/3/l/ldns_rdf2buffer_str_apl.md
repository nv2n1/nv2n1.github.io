---
title: "ldns_rdf2buffer_str_apl(3)"
name: "ldns_rdf2buffer_str_apl"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rdf2buffer_str_apl/"
description: "ldns_rdf2buffer_str_a, ldns_rdf2buffer_str_aaaa, ldns_rdf2buffer_str_str, ldns_rdf2buffer_str_b64, ldns_rdf2buffer_str_hex, ldns_rdf2buffer_str_type, ldns_rdf2buffer_str_class, ldns_rdf2buffer_str_..."
---

<h2>NAME</h2>
<p> ldns_rdf2buffer_str_a, ldns_rdf2buffer_str_aaaa, ldns_rdf2buffer_str_str, ldns_rdf2buffer_str_b64, ldns_rdf2buffer_str_hex, ldns_rdf2buffer_str_type, ldns_rdf2buffer_str_class, ldns_rdf2buffer_str_alg, ldns_rdf2buffer_str_loc, ldns_rdf2buffer_str_unknown, ldns_rdf2buffer_str_nsap, ldns_rdf2buffer_str_wks, ldns_rdf2buffer_str_nsec, ldns_rdf2buffer_str_period, ldns_rdf2buffer_str_tsigtime, ldns_rdf2buffer_str_apl, ldns_rdf2buffer_str_int16_data, ldns_rdf2buffer_str_int16, ldns_rdf2buffer_str_ipseckey </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_rdf2buffer_str_a(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_aaaa(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_str(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_b64(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_hex(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_type(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_class(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_alg(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_loc(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_unknown(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_nsap(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_wks(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_nsec(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_period(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_tsigtime(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_apl(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_int16_data(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_int16(ldns_buffer *output, const ldns_rdf *rdf); </p>
<p> ldns_status ldns_rdf2buffer_str_ipseckey(ldns_buffer *output, const ldns_rdf *rdf); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rdf2buffer_str_a</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_A rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_aaaa</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_AAAA rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_str</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_STR rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_b64</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_B64 rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_hex</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_HEX rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_type</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_TYPE rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_class</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_CLASS rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_alg</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_ALG rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_loc</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_LOC rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_unknown</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_UNKNOWN rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_nsap</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_NSAP rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_wks</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_WKS rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_nsec</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_NSEC rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_period</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_PERIOD rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_tsigtime</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_TSIGTIME rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_apl</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_APL rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_int16_data</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_INT16_DATA rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_int16</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_INT16 rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<dl>
<dt> <i>ldns_rdf2buffer_str_ipseckey</i>()</p>
<dd>Converts an LDNS_RDF_TYPE_IPSECKEY rdata element to string format and adds it to the output buffer .br <code>*rdf</code>: The rdata to convert .br <code>*output</code>: The buffer to add the data to .br Returns LDNS_STATUS_OK on success, and error status on failure</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
