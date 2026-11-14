---
title: "ldns_rr_set_pop_rr(3)"
name: "ldns_rr_set_pop_rr"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_set_pop_rr/"
description: "ldns_rr_set_push_rr, ldns_rr_set_pop_rr"
---

<h2>NAME</h2>
<p> ldns_rr_set_push_rr, ldns_rr_set_pop_rr </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> bool ldns_rr_set_push_rr(ldns_rr_list *rr_list, ldns_rr *rr); </p>
<p> ldns_rr* ldns_rr_set_pop_rr(ldns_rr_list *rr_list); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_set_push_rr</i>()</p>
<dd>pushes an rr to an rrset (which really are rr_list&#8217;s). .br <code>*rr_list</code>: the rrset to push the rr to .br <code>*rr</code>: the rr to push .br Returns true if the push succeeded otherwise false</dl>
<dl>
<dt> <i>ldns_rr_set_pop_rr</i>()</p>
<dd>pops the last rr from an rrset. This function is there only for the symmetry. .br <code>rr_list</code>: the rr_list to pop from .br Returns NULL if nothing to pop. Otherwise the popped RR </p>
</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr</i>, <i>ldns_rr_list</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
