---
title: "expand_number(3)"
name: "expand_number"
section: "3"
letter: "e"
url: "/docs/linux/man/3-expand_number/"
description: "expand_number – format a number from human readable form"
---

<h2 class="name">NAME</h2>
<p> <code>expand_number</code> &#8211; format a number from human readable form </p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In bsd/libutil.h Ft int Fo expand_number Fa const char *buf uint64_t *num Fc</p>
<h2>DESCRIPTION</h2>
<p> The Fn expand_number function unformats the Fa buf string and stores a unsigned 64-bit quantity at address pointed out by the Fa num argument. </p>
<p> The Fn expand_number function follows the SI power of two convention. </p>
<p> The prefixes are:</p>
<dl>
<dt><code>Prefix Ta </code><code>Description Ta </code><code>Multiplier</code></p>
<dd>
<dt><code>k Ta </code><code>kilo Ta </code>1024</p>
<dd>
<dt><code>M Ta </code><code>mega Ta </code>1048576</p>
<dd>
<dt><code>G Ta </code><code>giga Ta </code>1073741824</p>
<dd>
<dt><code>T Ta </code><code>tera Ta </code>1099511627776</p>
<dd>
<dt><code>P Ta </code><code>peta Ta </code>1125899906842624</p>
<dd>
<dt><code>E Ta </code><code>exa Ta </code>1152921504606846976</p>
<dd></dl>
<h2>RETURN VALUES</h2>
<p> Rv -std</p>
<h2>ERRORS</h2>
<p> The Fn expand_number function will fail if:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The given string contains no digits.</p>
<dt><code>Bq </code>Er EINVAL</p>
<dd> An unrecognized prefix was given.</p>
<dt><code>Bq </code>Er ERANGE</p>
<dd> Result doesn&#8217;t fit into 64 bits.</dl>
<h2>SEE ALSO</h2>
<p> humanize_number3</p>
<h2>HISTORY</h2>
<p> The Fn expand_number function first appeared in Fx 6.3 . </p>
<h2>Index</h2>
