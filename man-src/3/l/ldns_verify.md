---
title: "ldns_verify(3)"
name: "ldns_verify"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_verify/"
description: "ldns_verify, ldns_verify_rrsig, ldns_verify_rrsig_keylist, ldns_verify_rrsig_keylist_notime, ldns_verify_notime"
---

<h2>NAME</h2>
<p> ldns_verify, ldns_verify_rrsig, ldns_verify_rrsig_keylist, ldns_verify_rrsig_keylist_notime, ldns_verify_notime </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_verify(ldns_rr_list *rrset, ldns_rr_list *rrsig, const ldns_rr_list *keys, ldns_rr_list *good_keys); </p>
<p> ldns_status ldns_verify_rrsig(ldns_rr_list *rrset, ldns_rr *rrsig, ldns_rr *key); </p>
<p> ldns_status ldns_verify_rrsig_keylist(ldns_rr_list *rrset, ldns_rr *rrsig, const ldns_rr_list *keys, ldns_rr_list *good_keys); </p>
<p> ldns_status ldns_verify_rrsig_keylist_notime(ldns_rr_list *rrset, ldns_rr *rrsig, const ldns_rr_list *keys, ldns_rr_list *good_keys); </p>
<p> ldns_status ldns_verify_notime(ldns_rr_list *rrset, ldns_rr_list *rrsig, const ldns_rr_list *keys, ldns_rr_list *good_keys); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_verify</i>()</p>
<dd>Verifies a list of signatures for one rrset. </p>
<p> .br <code>rrset</code>: the rrset to verify .br <code>rrsig</code>: a list of signatures to check .br <code>keys</code>: a list of keys to check with .br <code>good_keys</code>: if this is a (initialized) list, the pointer to keys from keys that validate one of the signatures are added to it .br Returns status LDNS_STATUS_OK if there is at least one correct key</dl>
<dl>
<dt> <i>ldns_verify_rrsig</i>()</p>
<dd>verify an rrsig with 1 key .br <code>rrset</code>: the rrset .br <code>rrsig</code>: the rrsig to verify .br <code>key</code>: the key to use .br Returns status message wether verification succeeded.</dl>
<dl>
<dt> <i>ldns_verify_rrsig_keylist</i>()</p>
<dd>Verifies an rrsig. All keys in the keyset are tried. .br <code>rrset</code>: the rrset to check .br <code>rrsig</code>: the signature of the rrset .br <code>keys</code>: the keys to try .br <code>good_keys</code>: if this is a (initialized) list, the pointer to keys from keys that validate one of the signatures are added to it .br Returns a list of keys which validate the rrsig + rrset. Returns status LDNS_STATUS_OK if at least one key matched. Else an error.</dl>
<dl>
<dt> <i>ldns_verify_rrsig_keylist_notime</i>()</p>
<dd>Verifies an rrsig. All keys in the keyset are tried. Time is not checked. .br <code>rrset</code>: the rrset to check .br <code>rrsig</code>: the signature of the rrset .br <code>keys</code>: the keys to try .br <code>good_keys</code>: if this is a (initialized) list, the pointer to keys from keys that validate one of the signatures are added to it .br Returns a list of keys which validate the rrsig + rrset. Returns status LDNS_STATUS_OK if at least one key matched. Else an error.</dl>
<dl>
<dt> <i>ldns_verify_notime</i>()</p>
<dd>Verifies a list of signatures for one rrset, but disregard the time. Inception and Expiration are not checked. </p>
<p> .br <code>rrset</code>: the rrset to verify .br <code>rrsig</code>: a list of signatures to check .br <code>keys</code>: a list of keys to check with .br <code>good_keys</code>: if this is a (initialized) list, the pointer to keys from keys that validate one of the signatures are added to it .br Returns status LDNS_STATUS_OK if there is at least one correct key</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_verify_rrsig_evp</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
