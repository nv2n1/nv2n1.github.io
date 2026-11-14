---
title: "ldns_get_rr_type_by_name(3)"
name: "ldns_get_rr_type_by_name"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_get_rr_type_by_name/"
description: "ldns_get_rr_class_by_name, ldns_get_rr_type_by_name"
---

<h2>NAME</h2>
<p> ldns_get_rr_class_by_name, ldns_get_rr_type_by_name </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rr_class ldns_get_rr_class_by_name(const char *name); </p>
<p> ldns_rr_type ldns_get_rr_type_by_name(const char *name); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_get_rr_class_by_name</i>()</p>
<dd>retrieves a class by looking up its name. .br <code>name</code>: string with the name .br Returns the cass which corresponds with the name</dl>
<dl>
<dt> <i>ldns_get_rr_type_by_name</i>()</p>
<dd>retrieves a rrtype by looking up its name. .br <code>name</code>: a string with the name .br Returns the type which corresponds with the name</dl>
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
