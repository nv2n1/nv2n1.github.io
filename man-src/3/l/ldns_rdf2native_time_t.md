---
title: "ldns_rdf2native_time_t(3)"
name: "ldns_rdf2native_time_t"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rdf2native_time_t/"
description: "ldns_native2rdf_int8, ldns_native2rdf_int16, ldns_native2rdf_int32, ldns_native2rdf_int16_data, ldns_rdf2native_int8, ldns_rdf2native_int16, ldns_rdf2native_int32, ldns_rdf2native_sockaddr_storage,..."
---

<h2>NAME</h2>
<p> ldns_native2rdf_int8, ldns_native2rdf_int16, ldns_native2rdf_int32, ldns_native2rdf_int16_data, ldns_rdf2native_int8, ldns_rdf2native_int16, ldns_rdf2native_int32, ldns_rdf2native_sockaddr_storage, ldns_rdf2native_time_t </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_native2rdf_int8(ldns_rdf_type type, uint8_t value); </p>
<p> ldns_rdf* ldns_native2rdf_int16(ldns_rdf_type type, uint16_t value); </p>
<p> ldns_rdf* ldns_native2rdf_int32(ldns_rdf_type type, uint32_t value); </p>
<p> ldns_rdf* ldns_native2rdf_int16_data(size_t size, uint8_t *data); </p>
<p> uint8_t ldns_rdf2native_int8(const ldns_rdf *rd); </p>
<p> uint16_t ldns_rdf2native_int16(const ldns_rdf *rd); </p>
<p> uint32_t ldns_rdf2native_int32(const ldns_rdf *rd); </p>
<p> struct sockaddr_storage * ldns_rdf2native_sockaddr_storage(const ldns_rdf *rd, uint16_t port, size_t *size); </p>
<p> time_t ldns_rdf2native_time_t(const ldns_rdf *rd); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_native2rdf_int8</i>()</p>
<dd>returns the rdf containing the native uint8_t repr. .br <code>type</code>: the ldns_rdf type to use .br <code>value</code>: the uint8_t to use .br Returns ldns_rdf* with the converted value</dl>
<dl>
<dt> <i>ldns_native2rdf_int16</i>()</p>
<dd>returns the rdf containing the native uint16_t representation. .br <code>type</code>: the ldns_rdf type to use .br <code>value</code>: the uint16_t to use .br Returns ldns_rdf* with the converted value</dl>
<dl>
<dt> <i>ldns_native2rdf_int32</i>()</p>
<dd>returns an rdf that contains the given int32 value. </p>
<p> Because multiple rdf types can contain an int32, the type must be specified .br <code>type</code>: the ldns_rdf type to use .br <code>value</code>: the uint32_t to use .br Returns ldns_rdf* with the converted value</dl>
<dl>
<dt> <i>ldns_native2rdf_int16_data</i>()</p>
<dd>returns an int16_data rdf that contains the data in the given array, preceded by an int16 specifying the length. </p>
<p> The memory is copied, and an LDNS_RDF_TYPE_INT16DATA is returned .br <code>size</code>: the size of the data .br <code>*data</code>: pointer to the actual data </p>
<p> .br Returns ldns_rd* the rdf with the data</dl>
<dl>
<dt> <i>ldns_rdf2native_int8</i>()</p>
<dd>returns the native uint8_t representation from the rdf. .br <code>rd</code>: the ldns_rdf to operate on .br Returns uint8_t the value extracted</dl>
<dl>
<dt> <i>ldns_rdf2native_int16</i>()</p>
<dd>returns the native uint16_t representation from the rdf. .br <code>rd</code>: the ldns_rdf to operate on .br Returns uint16_t the value extracted</dl>
<dl>
<dt> <i>ldns_rdf2native_int32</i>()</p>
<dd>returns the native uint32_t representation from the rdf. .br <code>rd</code>: the ldns_rdf to operate on .br Returns uint32_t the value extracted</dl>
<dl>
<dt> <i>ldns_rdf2native_sockaddr_storage</i>()</p>
<dd>returns the native sockaddr representation from the rdf. .br <code>rd</code>: the ldns_rdf to operate on .br <code>port</code>: what port to use. 0 means; use default (53) .br <code>size</code>: what is the size of the sockaddr_storage .br Returns struct sockaddr* the address in the format so other functions can use it (sendto)</dl>
<dl>
<dt> <i>ldns_rdf2native_time_t</i>()</p>
<dd>returns the native time_t representation from the rdf. .br <code>rd</code>: the ldns_rdf to operate on .br Returns time_t the value extracted (32 bits currently)</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rdf</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
