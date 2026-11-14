---
title: "look(1)"
name: "look"
section: "1"
letter: "l"
url: "/docs/linux/man/1-look/"
description: "look – display lines beginning with a given string"
---

<h2 class="name">NAME</h2>
<p> look &#8211; display lines beginning with a given string </p>
<h2>SYNOPSIS</h2>
<p> <code>look</code> [options] <i>string</i> [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>look</code> utility displays any lines in <i>file</i> which contain <i>string</i>. As <code>look</code> performs a binary search, the lines in <i>file</i> must be sorted (where <code><a href="/docs/linux/man/1-sort/">sort</a></code>(1) was given the same options <code>-d</code> and/or <code>-f</code> that <code>look</code> is invoked with). </p>
<p> If <i>file</i> is not specified, the file <i>/usr/share/dict/words</i> is used, only alphanumeric characters are compared and the case of alphabetic characters is ignored.</p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;alternative</code></p>
<dl>
<dt>
<dd> Use the alternative dictionary file.</dl>
<p> <code>-d</code>, <code>&#8211;alphanum</code></p>
<dl>
<dt>
<dd> Use normal dictionary character set and order, i.e., only blanks and alphanumeric characters are compared. This is on by default if no file is specified. </p>
<p> Note that blanks have been added to dictionary character set for compatibility with <code>sort -d</code> command since version 2.28.</dl>
<p> <code>-f</code>, <code>&#8211;ignore-case</code></p>
<dl>
<dt>
<dd> Ignore the case of alphabetic characters. This is on by default if no file is specified.</dl>
<p> <code>-t</code>, <code>&#8211;terminate</code> <i>character</i></p>
<dl>
<dt>
<dd> Specify a string termination character, i.e., only the characters in <i>string</i> up to and including the first occurrence of <i>character</i> are compared.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> The <code>look</code> utility exits 0 if one or more lines were found and displayed, 1 if no lines were found, and &gt;1 if an error occurred.</p>
<h2>ENVIRONMENT</h2>
<p> <code>WORDLIST</code></p>
<dl>
<dt>
<dd> Path to a dictionary file. The environment variable has greater priority than the dictionary path defined in FILES segment.</dl>
<h2>FILES</h2>
<p> <i>/usr/share/dict/words</i></p>
<dl>
<dt>
<dd> the dictionary</dl>
<p> <i>/usr/share/dict/web2</i></p>
<dl>
<dt>
<dd> the alternative dictionary</dl>
<h2>HISTORY</h2>
<p> The <code>look</code> utility appeared in Version 7 AT&amp;T Unix.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
sort -d /etc/passwd -o /tmp/look.dict
look -t: root:foobar /tmp/look.dict
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1), <code><a href="/docs/linux/man/1-sort/">sort</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>look</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
