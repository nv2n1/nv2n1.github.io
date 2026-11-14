---
title: "ldns_dnssec_trust_tree_print(3)"
name: "ldns_dnssec_trust_tree_print"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_trust_tree_print/"
description: "ldns_dnssec_trust_tree_new, ldns_dnssec_trust_tree_free, ldns_dnssec_trust_tree_depth, ldns_dnssec_derive_trust_tree, ldns_dnssec_trust_tree_contains_keys, ldns_dnssec_trust_tree_print, ldns_dnssec..."
---

<h2>NAME</h2>
<p> ldns_dnssec_trust_tree_new, ldns_dnssec_trust_tree_free, ldns_dnssec_trust_tree_depth, ldns_dnssec_derive_trust_tree, ldns_dnssec_trust_tree_contains_keys, ldns_dnssec_trust_tree_print, ldns_dnssec_trust_tree_print_sm, ldns_dnssec_trust_tree_add_parent, ldns_dnssec_derive_trust_tree_normal_rrset, ldns_dnssec_derive_trust_tree_dnskey_rrset, ldns_dnssec_derive_trust_tree_ds_rrset, ldns_dnssec_derive_trust_tree_no_sig </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_dnssec_trust_tree* ldns_dnssec_trust_tree_new(); </p>
<p> void ldns_dnssec_trust_tree_free(ldns_dnssec_trust_tree *tree); </p>
<p> size_t ldns_dnssec_trust_tree_depth(ldns_dnssec_trust_tree *tree); </p>
<p> ldns_dnssec_trust_tree* ldns_dnssec_derive_trust_tree( ldns_dnssec_data_chain *data_chain, ldns_rr *rr); </p>
<p> ldns_status ldns_dnssec_trust_tree_contains_keys( ldns_dnssec_trust_tree *tree, ldns_rr_list *keys); </p>
<p> void ldns_dnssec_trust_tree_print(FILE *out, ldns_dnssec_trust_tree *tree, size_t tabs, bool extended); </p>
<p>&nbsp;<wbr>ldns_dnssec_trust_tree_print_sm(); </p>
<p> ldns_status ldns_dnssec_trust_tree_add_parent(ldns_dnssec_trust_tree *tree, const ldns_dnssec_trust_tree *parent, const ldns_rr *parent_signature, const ldns_status parent_status); </p>
<p> void ldns_dnssec_derive_trust_tree_normal_rrset( ldns_dnssec_trust_tree *new_tree, ldns_dnssec_data_chain *data_chain, ldns_rr *cur_sig_rr); </p>
<p> void ldns_dnssec_derive_trust_tree_dnskey_rrset( ldns_dnssec_trust_tree *new_tree, ldns_dnssec_data_chain *data_chain, ldns_rr *cur_rr, ldns_rr *cur_sig_rr); </p>
<p> void ldns_dnssec_derive_trust_tree_ds_rrset( ldns_dnssec_trust_tree *new_tree, ldns_dnssec_data_chain *data_chain, ldns_rr *cur_rr); </p>
<p> void ldns_dnssec_derive_trust_tree_no_sig( ldns_dnssec_trust_tree *new_tree, ldns_dnssec_data_chain *data_chain); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_trust_tree_new</i>()</p>
<dd>Creates a new (empty) dnssec_trust_tree structure </p>
<p> .br Returns ldns_dnssec_trust_tree *</dl>
<dl>
<dt> <i>ldns_dnssec_trust_tree_free</i>()</p>
<dd>Frees the dnssec_trust_tree recursively </p>
<p> There is no deep free; all data in the trust tree consists of pointers to a data_chain </p>
<p> .br <code>tree</code>: The tree to free</dl>
<dl>
<dt> <i>ldns_dnssec_trust_tree_depth</i>()</p>
<dd>returns the depth of the trust tree </p>
<p> .br <code>tree</code>: tree to calculate the depth of .br Returns The depth of the tree</dl>
<dl>
<dt> <i>ldns_dnssec_derive_trust_tree</i>()</p>
<dd>Generates a dnssec_trust_tree for the given rr from the given data_chain </p>
<p> This does not clone the actual data; Don&#8217;t free the data_chain before you are done with this tree </p>
<p> .br <code>*data_chain</code>: The chain to derive the trust tree from .br <code>*rr</code>: The RR this tree will be about .br Returns ldns_dnssec_trust_tree *</dl>
<dl>
<dt> <i>ldns_dnssec_trust_tree_contains_keys</i>()</p>
<dd>Returns OK if there is a trusted path in the tree to one of the DNSKEY or DS RRs in the given list </p>
<p> \param *tree The trust tree so search \param *keys A ldns_rr_list of DNSKEY and DS rrs to look for </p>
<p> .br Returns LDNS_STATUS_OK if there is a trusted path to one of the keys, or the *first* error encountered if there were no paths</dl>
<dl>
<dt> <i>ldns_dnssec_trust_tree_print</i>()</p>
<dd>Prints the dnssec_trust_tree structure to the given file stream. </p>
<p> If a link status is not LDNS_STATUS_OK; the status and relevant signatures are printed too </p>
<p> .br <code>*out</code>: The file stream to print to .br <code>tree</code>: The trust tree to print .br <code>tabs</code>: Prepend each line with tabs*2 spaces .br <code>extended</code>: If true, add little explanation lines to the output</dl>
<dl>
<dt> <i>ldns_dnssec_trust_tree_print_sm</i>()</dl>
<dl>
<dt> <i>ldns_dnssec_trust_tree_add_parent</i>()</p>
<dd>Adds a trust tree as a parent for the given trust tree </p>
<p> .br <code>*tree</code>: The tree to add the parent to .br <code>*parent</code>: The parent tree to add .br <code>*parent_signature</code>: The RRSIG relevant to this parent/child connection .br <code>parent_status</code>: The DNSSEC status for this parent, child and RRSIG .br Returns LDNS_STATUS_OK if the addition succeeds, error otherwise</dl>
<dl>
<dt> <i>ldns_dnssec_derive_trust_tree_normal_rrset</i>()</p>
<dd>Sub function for derive_trust_tree that is used for a &#8216;normal&#8217; rrset </p>
<p> .br <code>new_tree</code>: The trust tree that we are building .br <code>data_chain</code>: The data chain containing the data for the trust tree .br <code>cur_sig_rr</code>: The currently relevant signature</dl>
<dl>
<dt> <i>ldns_dnssec_derive_trust_tree_dnskey_rrset</i>()</p>
<dd>Sub function for derive_trust_tree that is used for DNSKEY rrsets </p>
<p> .br <code>new_tree</code>: The trust tree that we are building .br <code>data_chain</code>: The data chain containing the data for the trust tree .br <code>cur_rr</code>: The currently relevant DNSKEY RR .br <code>cur_sig_rr</code>: The currently relevant signature</dl>
<dl>
<dt> <i>ldns_dnssec_derive_trust_tree_ds_rrset</i>()</p>
<dd>Sub function for derive_trust_tree that is used for DS rrsets </p>
<p> .br <code>new_tree</code>: The trust tree that we are building .br <code>data_chain</code>: The data chain containing the data for the trust tree .br <code>cur_rr</code>: The currently relevant DS RR</dl>
<dl>
<dt> <i>ldns_dnssec_derive_trust_tree_no_sig</i>()</p>
<dd>Sub function for derive_trust_tree that is used when there are no signatures </p>
<p> .br <code>new_tree</code>: The trust tree that we are building .br <code>data_chain</code>: The data chain containing the data for the trust tree</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dnssec_data_chain</i>, <i>ldns_dnssec_trust_tree</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
