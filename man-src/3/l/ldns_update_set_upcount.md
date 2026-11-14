---
title: "ldns_update_set_upcount(3)"
name: "ldns_update_set_upcount"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_update_set_upcount/"
description: "ldns_update_set_zocount, ldns_update_set_prcount, ldns_update_set_upcount, ldns_update_set_adcount"
---

<h2>NAME</h2>
<p> ldns_update_set_zocount, ldns_update_set_prcount, ldns_update_set_upcount, ldns_update_set_adcount </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p>&nbsp;<wbr>ldns_update_set_zocount(); </p>
<p> void ldns_update_set_prcount(ldns_pkt *p, uint16_t c); </p>
<p> void ldns_update_set_upcount(ldns_pkt *p, uint16_t c); </p>
<p> void ldns_update_set_adcount(ldns_pkt *p, uint16_t c); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_update_set_zocount</i>()</dl>
<dl>
<dt> <i>ldns_update_set_prcount</i>()</p>
<dd>Set the pr count .br <code>p</code>: the packet .br <code>c</code>: the pr count to set</dl>
<dl>
<dt> <i>ldns_update_set_upcount</i>()</p>
<dd>Set the up count .br <code>p</code>: the packet .br <code>c</code>: the up count to set</dl>
<dl>
<dt> <i>ldns_update_set_adcount</i>()</p>
<dd>Set the ad count .br <code>p</code>: the packet .br <code>c</code>: the ad count to set</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_update_pkt_new</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
