---
title: "ldns_fskipcs(3)"
name: "ldns_fskipcs"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_fskipcs/"
description: "ldns_fget_token, ldns_fskipcs"
---

<h2>NAME</h2>
<p> ldns_fget_token, ldns_fskipcs </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ssize_t ldns_fget_token(FILE *f, char *token, const char *delim, size_t limit); </p>
<p> void ldns_fskipcs(FILE *fp, const char *s); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_fget_token</i>()</p>
<dd>returns a token/char from the stream F. This function deals with ( and ) in the stream, and ignores them when encountered .br <code>*f</code>: the file to read from .br <code>*token</code>: the read token is put here .br <code>*delim</code>: chars at which the parsing should stop .br <code>*limit</code>: how much to read. If 0 the builtin maximum is used .br Returns 0 on error of EOF of the stream F. Otherwise return the length of what is read</dl>
<dl>
<dt> <i>ldns_fskipcs</i>()</p>
<dd>skips all of the characters in the given string in the fp, moving the position to the first character that is not in *s. .br <code>*fp</code>: file to use .br <code>*s</code>: characters to skip .br Returns void</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_buffer</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
