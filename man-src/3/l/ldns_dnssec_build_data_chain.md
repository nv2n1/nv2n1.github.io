---
title: "ldns_dnssec_build_data_chain(3)"
name: "ldns_dnssec_build_data_chain"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_build_data_chain/"
description: "ldns_dnssec_data_chain_new, ldns_dnssec_data_chain_free, ldns_dnssec_data_chain_deep_free, ldns_dnssec_build_data_chain, ldns_dnssec_data_chain_print"
---

<h2>NAME</h2>
<p> ldns_dnssec_data_chain_new, ldns_dnssec_data_chain_free, ldns_dnssec_data_chain_deep_free, ldns_dnssec_build_data_chain, ldns_dnssec_data_chain_print </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_dnssec_data_chain* ldns_dnssec_data_chain_new(); </p>
<p> void ldns_dnssec_data_chain_free(ldns_dnssec_data_chain *chain); </p>
<p> void ldns_dnssec_data_chain_deep_free(ldns_dnssec_data_chain *chain); </p>
<p> ldns_dnssec_data_chain* ldns_dnssec_build_data_chain(ldns_resolver *res, const uint16_t qflags, const ldns_rr_list *data_set, const ldns_pkt *pkt, ldns_rr *orig_rr); </p>
<p> void ldns_dnssec_data_chain_print(FILE *out, const ldns_dnssec_data_chain *chain); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_data_chain_new</i>()</p>
<dd>Creates a new dnssec_chain structure .br Returns ldns_dnssec_data_chain *</dl>
<dl>
<dt> <i>ldns_dnssec_data_chain_free</i>()</p>
<dd>Frees a dnssec_data_chain structure </p>
<p> .br <code>*chain</code>: The chain to free</dl>
<dl>
<dt> <i>ldns_dnssec_data_chain_deep_free</i>()</p>
<dd>Frees a dnssec_data_chain structure, and all data contained therein </p>
<p> .br <code>*chain</code>: The dnssec_data_chain to free</dl>
<dl>
<dt> <i>ldns_dnssec_build_data_chain</i>()</p>
<dd>Build an ldns_dnssec_data_chain, which contains all DNSSEC data that is needed to derive the trust tree later </p>
<p> The data_set will be cloned </p>
<p> .br <code>*res</code>: resolver structure for further needed queries .br <code>qflags</code>: resolution flags .br <code>*data_set</code>: The original rrset where the chain ends .br <code>*pkt</code>: optional, can contain the original packet (and hence the sigs and maybe the key) .br <code>*orig_rr</code>: The original Resource Record </p>
<p> .br Returns the DNSSEC data chain</dl>
<dl>
<dt> <i>ldns_dnssec_data_chain_print</i>()</p>
<dd>Prints the dnssec_data_chain to the given file stream </p>
<p> .br <code>*out</code>: The file stream to print to .br <code>*chain</code>: The dnssec_data_chain to print</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dnssec_data_chain</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
