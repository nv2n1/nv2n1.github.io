---
title: "rcsfile(5)"
name: "rcsfile"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rcsfile/"
description: "rcsfile – RCS file format"
---

<p>rcsfile &#8211; <font SIZE="-1">RCS</font> file format</p>
<h2>Description</h2>
<p>An <font SIZE="-1">RCS</font> file&#8217;s contents are described by the grammar below. The text is free format: space, backspace, tab, newline, vertical tab, form feed, and carriage return (collectively, <i>white space)</i> have no significance except in strings. However, white space cannot appear within an id, num, or sym, and an <font SIZE="-1">RCS</font> file must end with a newline. Strings are enclosed by <code>@</code>. If a string contains a <code>@</code>, it must be doubled; otherwise, strings can contain arbitrary binary data. The meta syntax uses the following conventions: `|&#8217; (bar) separates alternatives; `{&#8216; and `}&#8217; enclose optional phrases; `{&#8216; and `}*&#8217; enclose phrases that can be repeated zero or more times; `{&#8216; and &#8216;}+&#8217; enclose phrases that must appear at least once and can be repeated; Terminal symbols are in <code>boldface</code>; nonterminal symbols are in <i>italics</i>. </p>
<pre><i>rcstext</i> ::= <i>admin</i> {<i>delta</i>}* <i>desc</i> {<i>deltatext</i>}*
<i>admin</i> ::= <code>head</code> {<i>num</i>}<code>;</code>
 { <code>branch</code> {<i>num</i>}<code>;</code> }
 <code>access</code> {<i>id</i>}*<code>;</code>
 <code>symbols</code> {<i>sym</i> <code>:</code> <i>num</i>}*<code>;</code>
 <code>locks</code> {<i>id</i> <code>:</code> <i>num</i>}*<code>;</code> {<code>strict ;</code>}
 { <code>integrity</code> {<i>intstring</i>}<code>;</code> }
 { <code>comment</code> {<i>string</i>}<code>;</code> }
 { <code>expand</code> {<i>string</i>}<code>;</code> }
<i>delta</i> ::= <i>num</i>
 <code>date</code> <i>num</i><code>;</code>
 <code>author</code> <i>id</i><code>;</code>
 <code>state</code> {<i>id</i>}<code>;</code>
 <code>branches</code> {<i>num</i>}*<code>;</code>
 <code>next</code> {<i>num</i>}<code>;</code>
 { <code>commitid</code> <i>sym</i><code>;</code> }
<i>desc</i> ::= <code>desc</code> <i>string</i>
<i>deltatext</i> ::= <i>num</i>
 <code>log</code> <i>string</i>
 <code>text</code> <i>string</i>
<i>num</i> ::= {<i>digit</i> | <code>.</code>}+
<i>digit</i> ::= <code>0</code> | <code>1</code> | <code>2</code> | <code>3</code> | <code>4</code> | <code>5</code> | <code>6</code> | <code>7</code> | <code>8</code> | <code>9</code>
<i>id</i> ::= {<i>idchar</i> | <code>.</code>}+
<i>sym</i> ::= {<i>idchar</i>}+
<i>idchar</i> ::= any visible graphic character except <i>special</i>
<i>special</i> ::= <code>$</code> | <code>,</code> | <code>.</code> | <code>:</code> | <code>;</code> | <code>@</code>
<i>string</i> ::= <code>@</code>{any character, with <code>@</code> doubled}*<code>@</code>
<i>word</i> ::= <i>id</i> | <i>num</i> | <i>string</i> | <code>:</code>
<i>intchar</i> ::= any character, except <code>@</code>
<i>thirdp</i> ::= <code>^L</code> {<i>intchar</i>}*
<i>intstring</i> ::= <code>@</code> {<i>intchar</i>}* {<i>thirdp</i>}* <code>@</code></pre>
<p>In releases prior to 5.8 (2011-08-30), the grammar included the <i>newphrase</i> production and used it in the <i>admin</i>, <i>delta</i> and <i>deltatext</i> productions. This allowed third-party programs to interoperate with <font SIZE="-1">RCS</font> by storing opaque (to <font SIZE="-1">RCS</font>) data in the file. As of 5.8, in the name of progress (towards more systematic file integrity support), the only area reserved for third-party interop is in the (string) value of the <i>integrity</i> field, specifically after the first <code>^L</code> (formfeed). A further restriction (for all programs) is that the <i>integrity</i> value must not contain <code>@</code>. Identifiers are case sensitive. Keywords are in lower case only. The sets of keywords and identifiers can overlap. In most environments <font SIZE="-1">RCS</font> uses the <font SIZE="-1">ISO</font> 8859/1 encoding: visible graphic characters are codes 041-176 and 240-377, and white space characters are codes 010-015 and 040. Dates, which appear after the <code>date</code> keyword, are of the form <i>Y</i><code>.</code><i>mm</i><code>.</code><i>dd</i><code>.</code><i>hh</i><code>.</code><i>mm</i><code>.</code><i>ss</i>, where <i>Y</i> is the year, <i>mm</i> the month (01-12), <i>dd</i> the day (01-31), <i>hh</i> the hour (00-23), <i>mm</i> the minute (00-59), and <i>ss</i> the second (00-60). <i>Y</i> contains just the last two digits of the year for years from 1900 through 1999, and all the digits of years thereafter. Dates use the Gregorian calendar; times use UTC. The <i>delta</i> nodes form a tree. All nodes whose numbers consist of a single pair (e.g., 2.3, 2.1, 1.3, etc.) are on the trunk, and are linked through the <code>next</code> field in order of decreasing numbers. The <code>head</code> field in the <i>admin</i> node points to the head of that sequence (i.e., contains the highest pair). The <code>branch</code> node in the admin node indicates the default branch (or revision) for most <font SIZE="-1">RCS</font> operations. If empty, the default branch is the highest branch on the trunk. All <i>delta</i> nodes whose numbers consist of 2<i>n</i> fields (<i>n</i>&ge;2) (e.g., 3.1.1.1, 2.1.2.2, etc.) are linked as follows. All nodes whose first 2<i>n</i>-1 number fields are identical are linked through the <code>next</code> field in order of increasing numbers. For each such sequence, the <i>delta</i> node whose number is identical to the first 2<i>n</i>-2 number fields of the deltas on that sequence is called the branchpoint. The <code>branches</code> field of a node contains a list of the numbers of the first nodes of all sequences for which it is a branchpoint. This list is ordered in increasing numbers. The following diagram shows an example of an <font SIZE="-1">RCS</font> file&#8217;s organization. </p>
<pre> Head
 |
 |
 v / \
 --------- / \
 / \ / \ | | / \ / \
 / \ / \ | 2.1 | / \ / \
 / \ / \ | | / \ / \
/1.2.1.3\ /1.3.1.1\ | | /1.2.2.2\ /1.2.2.1.1.1\
--------- --------- --------- --------- -------------
 ^ ^ | ^ ^
 | | | | |
 | | v | |
 / \ | --------- / \ |
 / \ | \ 1.3 / / \ |
 / \ ---------\ / / \-----------
/1.2.1.1\ 1.3.1 \ / /1.2.2.1\ 1.2.2.1.1
--------- \ / ---------
 ^ | ^
 | | |
 | v |
 | --------- |
 | \ 1.2 / |
 ----------------------\ /---------
 1.2.1 \ / 1.2.2
 \ /
 |
 |
 v
 ---------
 \ 1.1 /
 \ /
 \ /
 \ /</pre>
<h2>Identification</h2>
<p>Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1991, 1992, 1993, 1994, 1995 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-ident/">ident</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsclean/">rcsclean</a></code>(1), <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1). Walter F. Tichy, <font SIZE="-1">RCS</font>&#8211;A System for Version Control, <i>Software&#8211;Practice &amp; Experience</i> <code>15</code>, 7 (July 1985), 637-654. The full documentation for <font SIZE="-1">RCS</font> is maintained as a Texinfo manual. If the <code><a href="/docs/linux/man/1-info/">info</a></code>(1) and <font SIZE="-1">RCS</font> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info rcs</code></dl>
<p> should give you access to the complete manual. Additionally, the <font SIZE="-1">RCS</font> homepage:</p>
<dl>
<dd><code><a rel="nofollow" href="http://www.gnu.org/software/rcs/">http://www.gnu.org/software/rcs/</a></code></dl>
<p> has news and links to the latest release, development site, etc. </p>
