---
title: "ldns_getaddrinfo(3)"
name: "ldns_getaddrinfo"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_getaddrinfo/"
description: "ldns_getaddrinfo"
---

<h2>NAME</h2>
<p> ldns_getaddrinfo </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> uint16_t ldns_getaddrinfo(ldns_resolver *res, ldns_rdf *node, ldns_rr_class c, ldns_rr_list **list); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_getaddrinfo</i>()</p>
<dd>This function is a wrapper function for ldns_get_rr_list_name_by_addr and ldns_get_rr_list_addr_by_name. It&#8217;s name is from the getaddrinfo() library call. It tries to mimic that call, but without the lowlevel stuff. .br <code>res</code>: The resolver. If this value is NULL then a resolver will be created by ldns_getaddrinfo. .br <code>node</code>: the name or ip address to look up .br <code>c</code>: the class to look in .br <code>list</code>: put the found RR&#8217;s in this list .br Returns the number of RR found.</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
