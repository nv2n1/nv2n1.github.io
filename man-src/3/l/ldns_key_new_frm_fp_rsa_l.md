---
title: "ldns_key_new_frm_fp_rsa_l(3)"
name: "ldns_key_new_frm_fp_rsa_l"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_key_new_frm_fp_rsa_l/"
description: "ldns_key_new_frm_fp_rsa, ldns_key_new_frm_fp_rsa_l"
---

<h2>NAME</h2>
<p> ldns_key_new_frm_fp_rsa, ldns_key_new_frm_fp_rsa_l </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> RSA* ldns_key_new_frm_fp_rsa(FILE *fp); </p>
<p> RSA* ldns_key_new_frm_fp_rsa_l(FILE *fp, int *line_nr); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_key_new_frm_fp_rsa</i>()</p>
<dd>frm_fp helper function. This function parses the remainder of the (RSA) priv. key file generated from bind9 .br <code>fp</code>: the file to parse .br Returns NULL on failure otherwise a RSA structure</dl>
<dl>
<dt> <i>ldns_key_new_frm_fp_rsa_l</i>()</p>
<dd>frm_fp helper function. This function parses the remainder of the (RSA) priv. key file generated from bind9 .br <code>fp</code>: the file to parse .br <code>line_nr</code>: pointer to an integer containing the current line number (for debugging purposes) .br Returns NULL on failure otherwise a RSA structure</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_key_new_frm_fp</i>, <i>ldns_key</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
