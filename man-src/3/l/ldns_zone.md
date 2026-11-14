---
title: "ldns_zone(3)"
name: "ldns_zone"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_zone/"
description: "ldns_zone"
---

<h2>NAME</h2>
<p> ldns_zone </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_zone</i></p>
<dd>
<dd>DNS Zone </p>
<p> A list of RR&#8217;s with some<br />
 extra information which comes from the SOA RR<br />
 Note: nothing has been done to make this efficient (yet).<br />
 struct ldns_struct_zone<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>the soa defines a zone:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*_soa;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/* basicly a zone is a list of rr&#8217;s */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_list <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*_rrs;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/* we could change this to be a b-tree etc etc todo */</p>
<p> };<br />
 typedef struct ldns_struct_zone ldns_zone;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>
</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_zone_new</i>, <i>ldns_zone_deep_free</i>, <i>ldns_zone_new_frm_fp</i>, <i>ldns_zone_new_frm_fp_l</i>, <i>ldns_zone_sort</i>, <i>ldns_zone_glue_rr_list</i>, <i>ldns_zone_push_rr</i>, <i>ldns_zone_push_rr_list</i>, <i>ldns_zone_set_rrs</i>, <i>ldns_zone_set_soa</i>, <i>ldns_zone_rrs</i>, <i>ldns_zone_soa</i>, <i>ldns_zone_rr_count</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
