---
title: "lbzless(1)"
name: "lbzless"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lbzless/"
description: "lbzless – file perusal filter for crt viewing of compressed text"
---

<h2>NAME</h2>
<p> lbzless &#8211; file perusal filter for crt viewing of compressed text</p>
<h2>SYNOPSIS</h2>
<p> <code>lbzless</code> [ name &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Zless</i> is a filter which allows examination of compressed or plain text files one screenful at a time on a soft-copy terminal. It is the equivalent of setting the environment variable LESSOPEN to &#8216;|lbzip2 -cdq &#8212; %s&#8217;, and the environment variable LESSMETACHARS to &#8216;&lt;space&gt;&lt;tab&gt;&lt;newline&gt;;*?&quot;()&lt;&gt;[|&amp;^`#\$%=~&#8217;, and then running <i>less</i>. However, enough people seem to think that having the command <i>lbzless</i> available is important to be worth providing it.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-lbzmore/">lbzmore</a>(1), <a href="/docs/linux/man/1-less/">less</a>(1)</p>
<h2>BUGS</h2>
<p> <i>Zless</i> does not work with compressed data that is piped to it via standard input; it requires that input files be specified as arguments. To read compressed data from a pipe, you can use &#8230;<code>|bunzip2|less</code> instead of &#8230;<code>|lbzless</code>.</p>
<h2>COPYRIGHT NOTICE</h2>
<p> Copyright &#169; 2006, 2007 Free Software Foundation, Inc.<br />
 Copyright &#169; 1992, 1993 Jean-loup Gailly </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Foundation. </p>
<h2>Index</h2>
