---
title: "ldns_dname_cat_clone(3)"
name: "ldns_dname_cat_clone"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dname_cat_clone/"
description: "ldns_dname_cat_clone, ldns_dname_cat"
---

<h2>NAME</h2>
<p> ldns_dname_cat_clone, ldns_dname_cat </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_dname_cat_clone(const ldns_rdf *rd1, const ldns_rdf *rd2); </p>
<p> ldns_status ldns_dname_cat(ldns_rdf *rd1, ldns_rdf *rd2); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dname_cat_clone</i>()</p>
<dd>concatenates two dnames together .br <code>rd1</code>: the leftside .br <code>rd2</code>: the rightside .br Returns a new rdf with leftside/rightside</dl>
<dl>
<dt> <i>ldns_dname_cat</i>()</p>
<dd>concatenates rd2 after rd1 (rd2 is copied, rd1 is modified) .br <code>rd1</code>: the leftside .br <code>rd2</code>: the rightside .br Returns LDNS_STATUS_OK on success</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dname</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
