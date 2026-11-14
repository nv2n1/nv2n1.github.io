---
title: "pdfcrack(1)"
name: "pdfcrack"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfcrack/"
description: "pdfcrack – Password recovery tool for PDF-files"
---

<h2>NAME</h2>
<p> pdfcrack &#8211; Password recovery tool for PDF-files</p>
<h2>SYNOPSIS</h2>
<p> <code>pdfcrack </code> [ <code>-f</code> ] FILE [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>PDFCrack </code> is a tool for recovering passwords and content from PDF-files. </p>
<p> If aborted with Ctrl-C or by receiving a SIGINT signal, <code>pdfcrack</code> will automatically save current position. The position will be saved in a file called <code>savedstate.sav</code> in current working directory. </p>
<p> Mandatory arguments for long options are mandatory for short options too.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
&nbsp;<wbr><code>-b</code>,&nbsp;<wbr><code>&#8211;bench</code></p>
<dd> perform benchmark and exit</p>
<dt>
&nbsp;<wbr><code>-c</code>,&nbsp;<wbr><code>&#8211;charset=</code><i>STRING</i></p>
<dd> Use the characters in <i>STRING</i> as charset</p>
<dt><code>-w</code>, <code>&#8211;wordlist=</code><i>FILE</i></p>
<dd> Use <i>FILE</i> as source of passwords to try</p>
<dt><code>-n</code>, <code>&#8211;minpw=</code><i>INTEGER</i></p>
<dd> Skip trying passwords shorter than <i>INTEGER</p>
<dt></i><code>-m</code>, <code>&#8211;maxpw=</code><i>INTEGER</i></p>
<dd> Stop when reaching this <i>INTEGER</i> passwordlength</p>
<dt><code>-l</code>, <code>&#8211;loadstate=</code><i>FILE</i></p>
<dd>
&nbsp;<wbr>Continue from the state saved in&nbsp;<wbr><i>FILE</p>
<dt>
&nbsp;<wbr></i><code>-o</code>,&nbsp;<wbr><code>&#8211;owner</code></p>
<dd> Work with the ownerpassword</p>
<dt>
&nbsp;<wbr><code>-u</code>,&nbsp;<wbr><code>&#8211;user</code></p>
<dd> Work with the userpassword (default)</p>
<dt>
&nbsp;<wbr><code>-p</code>,&nbsp;<wbr><code>&#8211;password=</code><i>STRING</i></p>
<dd> Give userpassword to speed up breaking ownerpassword (implies <code>-o</code>)</p>
<dt>
&nbsp;<wbr><code>-q</code>,&nbsp;<wbr><code>&#8211;quiet</code></p>
<dd> Run quietly</p>
<dt><code>-s</code>, <code>&#8211;permutate</code></p>
<dd> Try permutating the passwords (currently only supports switching first character to uppercase)</p>
<dt>
&nbsp;<wbr><code>-v</code>,&nbsp;<wbr><code>&#8211;version</code></p>
<dd> Print version and exit</dl>
<h2>REPORTING BUGS</h2>
<p> Via e-mail to Henning Noren &lt;confusion42 [at] users.sourceforge.net&gt; or report on project page at <a rel="nofollow" href="http://pdfcrack.sourceforge.net/">http://pdfcrack.sourceforge.net/</a></p>
<h2>AUTHOR</h2>
<p> Henning Noren</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Henning Noren &lt;confusion42 [at] users.sourceforge.net&gt;<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law. </p>
<h2>Index</h2>
