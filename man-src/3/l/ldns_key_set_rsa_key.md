---
title: "ldns_key_set_rsa_key(3)"
name: "ldns_key_set_rsa_key"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_key_set_rsa_key/"
description: "ldns_key_set_algorithm, ldns_key_set_rsa_key, ldns_key_set_dsa_key, ldns_key_set_hmac_key, ldns_key_set_origttl, ldns_key_set_inception, ldns_key_set_expiration, ldns_key_set_pubkey_owner, ldns_key..."
---

<h2>NAME</h2>
<p> ldns_key_set_algorithm, ldns_key_set_rsa_key, ldns_key_set_dsa_key, ldns_key_set_hmac_key, ldns_key_set_origttl, ldns_key_set_inception, ldns_key_set_expiration, ldns_key_set_pubkey_owner, ldns_key_set_keytag, ldns_key_set_flags, ldns_key_list_set_key_count </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> void ldns_key_set_algorithm(ldns_key *k, ldns_signing_algorithm l); </p>
<p> void ldns_key_set_rsa_key(ldns_key *k, RSA *r); </p>
<p> void ldns_key_set_dsa_key(ldns_key *k, DSA *d); </p>
<p> void ldns_key_set_hmac_key(ldns_key *k, unsigned char *hmac); </p>
<p> void ldns_key_set_origttl(ldns_key *k, uint32_t t); </p>
<p> void ldns_key_set_inception(ldns_key *k, uint32_t i); </p>
<p> void ldns_key_set_expiration(ldns_key *k, uint32_t e); </p>
<p> void ldns_key_set_pubkey_owner(ldns_key *k, ldns_rdf *r); </p>
<p> void ldns_key_set_keytag(ldns_key *k, uint16_t tag); </p>
<p> void ldns_key_set_flags(ldns_key *k, uint16_t flags); </p>
<p> void ldns_key_list_set_key_count(ldns_key_list *key, size_t count); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_key_set_algorithm</i>()</p>
<dd>Set the key&#8217;s algorithm .br <code>k</code>: the key .br <code>l</code>: the algorithm</dl>
<dl>
<dt> <i>ldns_key_set_rsa_key</i>()</p>
<dd>Set the key&#8217;s rsa data. The rsa data should be freed by the user. .br <code>k</code>: the key .br <code>r</code>: the rsa data</dl>
<dl>
<dt> <i>ldns_key_set_dsa_key</i>()</p>
<dd>Set the key&#8217;s dsa data The dsa data should be freed by the user. .br <code>k</code>: the key .br <code>d</code>: the dsa data</dl>
<dl>
<dt> <i>ldns_key_set_hmac_key</i>()</p>
<dd>Set the key&#8217;s hmac data .br <code>k</code>: the key .br <code>hmac</code>: the raw key data</dl>
<dl>
<dt> <i>ldns_key_set_origttl</i>()</p>
<dd>Set the key&#8217;s original ttl .br <code>k</code>: the key .br <code>t</code>: the ttl</dl>
<dl>
<dt> <i>ldns_key_set_inception</i>()</p>
<dd>Set the key&#8217;s inception date (seconds after epoch) .br <code>k</code>: the key .br <code>i</code>: the inception</dl>
<dl>
<dt> <i>ldns_key_set_expiration</i>()</p>
<dd>Set the key&#8217;s expiration date (seconds after epoch) .br <code>k</code>: the key .br <code>e</code>: the expiration</dl>
<dl>
<dt> <i>ldns_key_set_pubkey_owner</i>()</p>
<dd>Set the key&#8217;s pubkey owner .br <code>k</code>: the key .br <code>r</code>: the owner</dl>
<dl>
<dt> <i>ldns_key_set_keytag</i>()</p>
<dd>Set the key&#8217;s key tag .br <code>k</code>: the key .br <code>tag</code>: the keytag</dl>
<dl>
<dt> <i>ldns_key_set_flags</i>()</p>
<dd>Set the key&#8217;s flags .br <code>k</code>: the key .br <code>flags</code>: the flags</dl>
<dl>
<dt> <i>ldns_key_list_set_key_count</i>()</p>
<dd>Set the keylist&#8217;s key count to count .br <code>key</code>: the key .br <code>count</code>: the cuont</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_key</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
