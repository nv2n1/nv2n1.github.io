---
title: "ldns_dnssec_zone_mark_glue(3)"
name: "ldns_dnssec_zone_mark_glue"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_zone_mark_glue/"
description: "ldns_dnssec_zone_sign, ldns_dnssec_zone_sign_nsec3, ldns_dnssec_zone_mark_glue, ldns_dnssec_name_node_next_nonglue, ldns_dnssec_zone_create_nsecs, ldns_dnssec_remove_signatures, ldns_dnssec_zone_cr..."
---

<h2>NAME</h2>
<p> ldns_dnssec_zone_sign, ldns_dnssec_zone_sign_nsec3, ldns_dnssec_zone_mark_glue, ldns_dnssec_name_node_next_nonglue, ldns_dnssec_zone_create_nsecs, ldns_dnssec_remove_signatures, ldns_dnssec_zone_create_rrsigs </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_dnssec_zone_sign(ldns_dnssec_zone *zone, ldns_rr_list *new_rrs, ldns_key_list *key_list, int (*func)(ldns_rr *, void *), void *arg); </p>
<p> ldns_status ldns_dnssec_zone_sign_nsec3(ldns_dnssec_zone *zone, ldns_rr_list *new_rrs, ldns_key_list *key_list, int (*func)(ldns_rr *, void *), void *arg, uint8_t algorithm, uint8_t flags, uint16_t iterations, uint8_t salt_length, uint8_t *salt); </p>
<p>&nbsp;<wbr>ldns_dnssec_zone_mark_glue(); </p>
<p> ldns_rbnode_t* ldns_dnssec_name_node_next_nonglue(ldns_rbnode_t *node); </p>
<p> ldns_status ldns_dnssec_zone_create_nsecs(ldns_dnssec_zone *zone, ldns_rr_list *new_rrs); </p>
<p> ldns_dnssec_rrs* ldns_dnssec_remove_signatures(ldns_dnssec_rrs *signatures, ldns_key_list *key_list, int (*func)(ldns_rr *, void *), void *arg); </p>
<p> ldns_status ldns_dnssec_zone_create_rrsigs(ldns_dnssec_zone *zone, ldns_rr_list *new_rrs, ldns_key_list *key_list, int (*func)(ldns_rr *, void*), void *arg); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_zone_sign</i>()</p>
<dd>signs the given zone with the given keys </p>
<p> .br <code>zone</code>: the zone to sign .br <code>key_list</code>: the list of keys to sign the zone with .br <code>new_rrs</code>: newly created resource records are added to this list, to free them later .br <code>func</code>: callback function that decides what to do with old signatures This function takes an ldns_rr* and an optional void *arg argument, and returns one of four values: LDNS_SIGNATURE_LEAVE_ADD_NEW: leave the signature and add a new one for the corresponding key LDNS_SIGNATURE_REMOVE_ADD_NEW: remove the signature and replace is with a new one from the same key LDNS_SIGNATURE_LEAVE_NO_ADD: leave the signature and do not add a new one with the corresponding key LDNS_SIGNATURE_REMOVE_NO_ADD: remove the signature and do not replace </p>
<p> .br <code>arg</code>: optional argument for the callback function .br Returns LDNS_STATUS_OK on success, an error code otherwise</dl>
<dl>
<dt> <i>ldns_dnssec_zone_sign_nsec3</i>()</p>
<dd>signs the given zone with the given new zone, with NSEC3 </p>
<p> .br <code>zone</code>: the zone to sign .br <code>key_list</code>: the list of keys to sign the zone with .br <code>new_rrs</code>: newly created resource records are added to this list, to free them later .br <code>func</code>: callback function that decides what to do with old signatures .br <code>arg</code>: optional argument for the callback function .br <code>algorithm</code>: the NSEC3 hashing algorithm to use .br <code>flags</code>: NSEC3 flags .br <code>iterations</code>: the number of NSEC3 hash iterations to use .br <code>salt_length</code>: the length (in octets) of the NSEC3 salt .br <code>salt</code>: the NSEC3 salt data .br Returns LDNS_STATUS_OK on success, an error code otherwise</dl>
<dl>
<dt> <i>ldns_dnssec_zone_mark_glue</i>()</dl>
<dl>
<dt> <i>ldns_dnssec_name_node_next_nonglue</i>()</p>
<dd>Finds the first dnssec_name node in the rbtree that is not occluded. It *does* return names that are partially occluded. </p>
<p> .br <code>node</code>: the first node to check .br Returns the first node that has not been marked as glue, or NULL if not found (TODO: make that LDNS_RBTREE_NULL?)</dl>
<dl>
<dt> <i>ldns_dnssec_zone_create_nsecs</i>()</p>
<dd>Adds NSEC records to the given dnssec_zone </p>
<p> .br <code>zone</code>: the zone to add the records to .br <code>new_rrs</code>: ldns_rr&#8217;s created by this function are added to this rr list, so the caller can free them later .br Returns LDNS_STATUS_OK on success, an error code otherwise</dl>
<dl>
<dt> <i>ldns_dnssec_remove_signatures</i>()</p>
<dd>remove signatures if callback function tells to </p>
<p> .br <code>signatures</code>: list of signatures to check, and possibly remove, depending on the value of the callback .br <code>key_list</code>: these are marked to be used or not, on the return value of the callback .br <code>func</code>: this function is called to specify what to do with each signature (and corresponding key) .br <code>arg</code>: Optional argument for the callback function .br Returns s pointer to the new signatures rrs (the original passed to this function may have been removed)</dl>
<dl>
<dt> <i>ldns_dnssec_zone_create_rrsigs</i>()</p>
<dd>Adds signatures to the zone </p>
<p> .br <code>zone</code>: the zone to add RRSIG Resource Records to .br <code>new_rrs</code>: the RRSIG RRs that are created are also added to this list, so the caller can free them later .br <code>key_list</code>: list of keys to sign with. .br <code>func</code>: Callback function to decide what keys to use and what to do with old signatures .br <code>arg</code>: Optional argument for the callback function .br Returns LDNS_STATUS_OK on success, error otherwise</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dnssec_zone</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
