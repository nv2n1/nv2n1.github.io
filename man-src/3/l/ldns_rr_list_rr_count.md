---
title: "ldns_rr_list_rr_count(3)"
name: "ldns_rr_list_rr_count"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_list_rr_count/"
description: "ldns_rr_list_rr_count, ldns_rr_list_set_rr_count"
---

<h2>NAME</h2>
<p> ldns_rr_list_rr_count, ldns_rr_list_set_rr_count </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> size_t ldns_rr_list_rr_count(const ldns_rr_list *rr_list); </p>
<p> void ldns_rr_list_set_rr_count(ldns_rr_list *rr_list, size_t count); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_list_rr_count</i>()</p>
<dd>returns the number of rr&#8217;s in an rr_list. .br <code>rr_list</code>: the rr_list to read from .br Returns the number of rr&#8217;s</dl>
<dl>
<dt> <i>ldns_rr_list_set_rr_count</i>()</p>
<dd>sets the number of rr&#8217;s in an rr_list. .br <code>rr_list</code>: the rr_list to set the count on .br <code>count</code>: the number of rr in this list .br Returns void</dl>
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
