---
title: "ident(1)"
name: "ident"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ident/"
description: "ident – identify RCS keyword strings in files"
---

<h2>NAME</h2>
<p> ident &#8211; identify RCS keyword strings in files</p>
<h2>SYNOPSIS</h2>
<p> <code>ident</code> [ <code>-q</code> ] [ <code>-V</code> ] [ <i>file</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ident</code> searches for all instances of the pattern <code>$</code><i>keyword</i><code>:</code><i>&nbsp;<wbr>text&nbsp;<wbr></i><code>$</code> in the named files or, if no files are named, the standard input. </p>
<p> These patterns are normally inserted automatically by the <font SIZE="-1">RCS</font> command <code><a href="/docs/linux/man/1-co/">co</a></code>(1), but can also be inserted manually. The option <code>-q</code> suppresses the warning given if there are no patterns in a file. The option <code>-V</code> prints <font SIZE="-1">RCS</font>&#8216;s version number. </p>
<p> <code>ident</code> works on text files as well as object files and dumps. For example, if the C program in <code>f.c</code> contains</p>
<dl>
<dt>
<dd> <code> #include &lt;stdio.h&gt;<br />
 static char const rcsid[] = </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;$Id: f.c,v 5.4 1993/11/09 17:40:15 eggert Exp&nbsp;<wbr>$&quot;;<br />
 int main() { return printf(&quot;%s
&quot;, rcsid) == EOF; } </code></dl>
<p> and <code>f.c</code> is compiled into <code>f.o</code>, then the command</p>
<dl>
<dt>
<dd> <code>ident f.c f.o</code></dl>
<p> will output </p>
<pre>
<dl>
<dt><dd><code>f.c:
    $Id: f.c,v 5.4 1993/11/09 17:40:15 eggert Exp $
f.o:
    $Id: f.c,v 5.4 1993/11/09 17:40:15 eggert Exp $
</code></pre>
</dl>
<p> If a C program defines a string like <code>rcsid</code> above but does not use it, <code><a href="/docs/linux/man/1-lint/">lint</a></code>(1) may complain, and some C compilers will optimize away the string. The most reliable solution is to have the program use the <code>rcsid</code> string, as shown in the example above. </p>
<p> <code>ident</code> finds all instances of the <code>$</code><i>keyword</i><code>:</code><i>&nbsp;<wbr>text&nbsp;<wbr></i><code>$</code> pattern, even if <i>keyword</i> is not actually an <font SIZE="-1">RCS</font>-supported keyword. This gives you information about nonstandard keywords like <code>$XConsortium$</code>. </p>
<p> The pattern normally requires a colon and a space immediately after the keyword and a space immediately before the terminating <code>$</code>, but for Subversion 1.2 (and later) compatability, <code>ident</code> will also recognize the pattern <code>$</code><i>keyword</i><code>::</code><i>&nbsp;<wbr>text&nbsp;<wbr></i><code>$</code> (i.e., two colons and a space) and the pattern <code>$</code><i>keyword</i><code>::</code><i>&nbsp;<wbr>text&nbsp;<wbr>#</i><code>$</code> (likewise, with a hash before the terminating <code>$</code>). These are the fixed-width keyword syntax. To summarize, the three recognized patterns are:</p>
<dl>
<dt>
<dd> <code>$</code><i>keyword</i><code>:</code><i>&nbsp;<wbr>text&nbsp;<wbr></i><code>$</code><br />
 <code>$</code><i>keyword</i><code>::</code><i>&nbsp;<wbr>text&nbsp;<wbr></i><code>$</code><br />
 <code>$</code><i>keyword</i><code>::</code><i>&nbsp;<wbr>text&nbsp;<wbr>#</i><code>$</code>
</dl>
<h2>KEYWORDS</h2>
<p> Here is the list of keywords currently maintained by <code><a href="/docs/linux/man/1-co/">co</a></code>(1). All times are given in Coordinated Universal Time (<font SIZE="-1">UTC</font>, sometimes called <font SIZE="-1">GMT</font>) by default, but if the files were checked out with <code>co</code>&#8216;s <code>-z</code><i>zone</i> option, times are given with a numeric time zone indication appended.</p>
<dl>
<dt><code>$Author$</code></p>
<dd> The login name of the user who checked in the revision.</p>
<dt><code>$Date$</code></p>
<dd> The date and time the revision was checked in.</p>
<dt><code>$Header$</code></p>
<dd> A standard header containing the full <font SIZE="-1">RCS</font> file name, the revision number, the date and time, the author, the state, and the locker (if locked).</p>
<dt><code>$Id$</code></p>
<dd> Same as <code>$Header$</code>, except that the <font SIZE="-1">RCS</font> file name is without directory components.</p>
<dt><code>$Locker$</code></p>
<dd> The login name of the user who locked the revision (empty if not locked).</p>
<dt><code>$Log$</code></p>
<dd> The log message supplied during checkin. For <code>ident</code>&#8216;s purposes, this is equivalent to <code>$RCSfile$</code>.</p>
<dt><code>$Name$</code></p>
<dd> The symbolic name used to check out the revision, if any.</p>
<dt><code>$RCSfile$</code></p>
<dd> The <font SIZE="-1">RCS</font> file name without directory components.</p>
<dt><code>$Revision$</code></p>
<dd> The revision number assigned to the revision.</p>
<dt><code>$Source$</code></p>
<dd> The full <font SIZE="-1">RCS</font> file name.</p>
<dt><code>$State$</code></p>
<dd> The state assigned to the revision with the <code>-s</code> option of <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1) or <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1).</dl>
<p> <code><a href="/docs/linux/man/1-co/">co</a></code>(1) represents the following characters in keyword values by escape sequences to keep keyword strings well-formed. </p>
<dl>
<dt>
<dd>
<pre>
<i>char     escape sequence</i>
tab      <code>	</code>
newline  <code>
</code>
space    <code> 
$        $
\        \</code>
</pre>
</dl>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1992, 1993 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ci/">ci</a></code>(1), <code><a href="/docs/linux/man/1-co/">co</a></code>(1), <code><a href="/docs/linux/man/1-rcs/">rcs</a></code>(1), <code><a href="/docs/linux/man/1-rcsdiff/">rcsdiff</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/1-rlog/">rlog</a></code>(1), <code><a href="/docs/linux/man/5-rcsfile/">rcsfile</a></code>(5). </p>
<p> Walter F. Tichy, <font SIZE="-1">RCS</font>&#8211;A System for Version Control, <i>Software&#8211;Practice &amp; Experience</i> <code>15</code>, 7 (July 1985), 637-654. </p>
<p> The full documentation for <font SIZE="-1">RCS</font> is maintained as a Texinfo manual. If the <code><a href="/docs/linux/man/1-info/">info</a></code>(1) and <font SIZE="-1">RCS</font> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info rcs</code></dl>
<p> should give you access to the complete manual. Additionally, the <font SIZE="-1">RCS</font> homepage:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://www.gnu.org/software/rcs/">http://www.gnu.org/software/rcs/</a></code></dl>
<p> has news and links to the latest release, development site, etc. </p>
<h2>Index</h2>
