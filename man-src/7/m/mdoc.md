---
title: "mdoc(7)"
name: "mdoc"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mdoc/"
description: "mdoc – quick reference guide for the -mdoc macro package"
---

<p>Linux</p>
<h2>Name</h2>
<p><code>mdoc</code> &#8211; quick reference guide for the <code>-mdoc</code> macro package</p>
<h2>Synopsis</h2>
<p><code>groff</code> &#8211;<code>m </code><i>doc</i> <i>files &#8230;</i></p>
<h2>Description</h2>
<p>The <code>-mdoc</code> package is a set of content-based and domain-based macros used to format the BSD man pages. The macro names and their meanings are listed below for quick reference; for a detailed explanation on using the package, see groff_mdoc7 and the tutorial sampler mdoc.samples7. </p>
<p> Note that this is not the usual macro package for Linux documentation, although it is used for documentation of several widely used programs; see <a href="/docs/linux/man/7-man/">man</a>(7). </p>
<p> The macros are described in two groups, the first includes the structural and physical page layout macros. The second contains the manual and general text domain macros which differentiate the <code>-mdoc</code> package from other troff formatting packages.</p>
<h2>Page Structure Domain</h2>
<h3>Title Macros</h3>
<p>To create a valid manual page, these three macros, in this order, are required: </p>
<dl>
<dt><code>. </code><i>Month day, year</i></p>
<dd>Document date.</p>
<dt><code>. </code></p>
<dd>Title, in uppercase.</p>
<dt><code>. </code><i>OPERATING_SYSTEM [version/release]</i></p>
<dd>Operating system (<code>BSD</code> )</dl>
<h3>Page Layout Macros</h3>
<p>Section headers, paragraph breaks, lists and displays. </p>
<dl>
<dt><code>.</dl>
</dl>
<p> </code></p>
<h2>Section Headers.</h2>
<dd>Valid headers, in the order of presentation:</p>
<dl>
<dt><i>NAME</i></p>
<dd>Name section, should include the `.<code>groff</code> &#8216; or `.Fn and &#8216; the `. &#8211; macros. &#8216;</p>
<dt><i>SYNOPSIS</i></p>
<dd>Usage.</p>
<dt><i>DESCRIPTION</i></p>
<dd>General description, should include options and parameters.</p>
<dt><i>RETURN VALUE</i></p>
<dd>Sections two and three function calls.</p>
<dt><i>ENVIRONMENT</i></p>
<dd>Describe environment variables.</p>
<dt><i>FILES</i></p>
<dd>Files associated with the subject.</p>
<dt><i>EXAMPLES</i></p>
<dd>Examples and suggestions.</p>
<dt><i>DIAGNOSTICS</i></p>
<dd>Normally used for section four device interface diagnostics.</p>
<dt><i>ERRORS</i></p>
<dd>Sections two and three error and signal handling.</p>
<dt><i>SEE ALSO</i></p>
<dd>Cross references and citations.</p>
<dt><i>CONFORMING TO</i></p>
<dd>Conformance to standards if applicable.</p>
<dt><i>HISTORY</i></p>
<dd>If a standard is not applicable, the history of the subject should be given.</p>
<dt><i>BUGS</i></p>
<dd>Gotchas and caveats.</p>
<dt><i>other</i></p>
<dd>Customized headers may be added at the authors discretion.</dl>
<p> Li .Ss Subsection Headers. Li .Pp Paragraph Break. Vertical space (one line). Li .D1 (D-one) Display-one Indent and display one text line. Li .Dl (D-ell) Display-one literal. Indent and display one line of literal text. Li .Bd Begin-display block. Display options:</p>
<dl>
<dt><code>-ragged</code></p>
<dd>Unjustified (ragged edges).</p>
<dt><code>-filled</code></p>
<dd>Justified.</p>
<dt><code>-literal</code></p>
<dd>Literal text or code.</p>
<dt><code>-file </code><i>name</i></p>
<dd>Read in named <i>file</i> and display.</p>
<dt><code>-offset </code><i>string</i></p>
<dd>Offset display. Acceptable <i>string</i> values:</p>
<dl>
<dt><i>left</i></p>
<dd>Align block on left (default).</p>
<dt><i>center</i></p>
<dd>Approximate center margin.</p>
<dt><i>indent</i></p>
<dd>Six constant width spaces (a tab).</p>
<dt><i>indent-two</i></p>
<dd>Two tabs.</p>
<dt><i>right</i></p>
<dd>Left aligns block 2 inches from right.</p>
<dt><i>xx </i><code>n</code></p>
<dd>Where <i>xx</i> is a number from <code>4 n</code> to <code>99 n</code></p>
<dt><i>Aa </i>Where</p>
<dd><i>Aa </i>is a callable macro name.</p>
<dt><i>string</i></p>
<dd>The width of <i>string</i> is used.</dl>
</dl>
<p> Li .Ed End-display (matches .Bd). Li .Bl Begin-list. Create lists or columns. Options:</p>
<dl>
<dt><i>List-types</i></p>
<dd>
<dl>
<dt><code>-bullet Ta </code>Bullet Item List</p>
<dd>
<dt><code>-item Ta </code>Unlabeled List</p>
<dd>
<dt><code>-enum Ta </code>Enumerated List</p>
<dd>
<dt><code>-tag Ta </code>Tag Labeled List</p>
<dd>
<dt><code>-diag Ta </code>Diagnostic List</p>
<dd>
<dt><code>-hang Ta </code>Hanging Labeled List</p>
<dd>
<dt><code>-ohang Ta </code>Overhanging Labeled List</p>
<dd>
<dt><code>-inset Ta </code>Inset or Run-on Labeled List</p>
<dd></dl>
<dt><code>List-parameters</code></p>
<dd>
<dl>
<dt><code>-offset</code></p>
<dd>(All lists.) See `. &#8216; begin-display above.</p>
<dt><code>-width</code></p>
<dd>( &#8211;<code>tag</code> and &#8211;<code>hang</code> lists only.) See `. &#8216;</p>
<dt><code>-compact</code></p>
<dd>(All lists.) Suppresses blank lines.</dl>
</dl>
<p> Li .El End-list. Li .It List item.</p>
<h2>Manual And General Text Domain Macros</h2>
<p>The manual and general text domain macros are special in that most of them are parsed for callable macros for example:</p>
<dl>
<dt><code>.</code>[-<code>s </code><i>file</i> ]</p>
<dd>Produces [-<code>s </code><i>file</i> ]</dl>
<p> In this example, the option enclosure macro `.[is] &#8216; parsed, and calls the callable content macro `- &#8216; which operates on the argument `s&#8217; and then calls the callable content macro `<i>file &#8230;</i> &#8216; which operates on the argument `file&#8217; Some macros may be callable, but are not parsed and vice versa. These macros are indicated in the <i>parsed</i> and <i>callable</i> columns below. </p>
<p> Unless stated, manual domain macros share a common syntax: </p>
<blockquote><p><tt>.</tt><i>argument [&nbsp;. ,&nbsp;;&nbsp;:&nbsp;(&nbsp;)&nbsp;[&nbsp;]&nbsp;argument &#8230;]</i> </p></blockquote>
<p> <code>Note</code> Opening and closing punctuation characters are recognized as such only if they are presented one at a time. The string `),&#8217; is not recognized as punctuation and will be output with a leading white space and in what ever font the calling macro uses. The argument list `]&#8217; ) , is recognized as three sequential closing punctuation characters and a leading white space is not output between the characters and the previous argument (if any). The special meaning of a punctuation character may be escaped with the string `\&amp;&#8217; For example the following string,</p>
<dl>
<dt><code>.</code><i>file1 , file2 , file3&nbsp;)&nbsp;.</i></p>
<dd>Produces <i>file1 , file2 , file3 )</i></dl>
<h3>Manual Domain Macros</h3>
<dl>
<dt><i>Name<tt>&nbsp;<wbr>&nbsp;</tt>Parsed<tt>&nbsp;<wbr>&nbsp;</tt>Callable<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Description</i></p>
<dd>
<dt><i>Ta </i>Yes Ta Yes Ta Address. (This macro may be deprecated.)</p>
<dd>
<dt><code>An </code>Ta Yes Ta Yes Ta Author name.</p>
<dd>
<dt><i>Ta </i>Yes Ta Yes Ta Command-line argument.</p>
<dd>
<dt><code>Ta </code><code>Ta </code><code>Ta </code>Configuration declaration (section four only).</p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta Command-line argument modifier.</p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta Defined variable (source code).</p>
<dd>
<dt><code>Er </code>Ta Yes Ta Yes Ta Error number (source code).</p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta Environment variable.</p>
<dd>
<dt><code>Fa </code>Ta Yes Ta Yes Ta Function argument.</p>
<dd>
<dt><code>Fd </code>Ta Yes Ta Yes Ta Function declaration.</p>
<dd>
<dt><code>Fn </code>Ta Yes Ta Yes Ta Function call (also .Fo and .Fc).</p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta Interactive command.</p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta Literal text.</p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta Command name.</p>
<dd>
<dt>[Ta Yes Ta Yes Ta Option (also .[and .Oc). ]</p>
<dd>
<dt><code>Ot </code>Ta Yes Ta Yes Ta Old style function type (Fortran only).</p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta Pathname or filename.</p>
<dd>
<dt><code>St </code>Ta Yes Ta Yes Ta Standards (-p1003.2, -p1003.1 or -ansiC)</p>
<dd>
<dt><i>Ta </i>Yes Ta Yes Ta Variable name.</p>
<dd>
<dt><code>Vt </code>Ta Yes Ta Yes Ta Variable type (Fortran only).</p>
<dd>
<dt><code>TaYesTaYesTaManualPageCrossReference. </code></p>
<dd></dl>
<h3>General Text Domain Macros</h3>
<dl>
<dt><i>Name<tt>&nbsp;<wbr>&nbsp;</tt>Parsed<tt>&nbsp;<wbr>&nbsp;</tt>Callable<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Description</i></p>
<dd>
<dt><code>%A Ta </code>Yes Ta <code>Ta </code>Reference author.</p>
<dd>
<dt><code>%B Ta </code>Yes Ta Yes Ta Reference book title.</p>
<dd>
<dt><code>%C Ta </code><code>Ta </code><code>Ta </code>Reference place of publishing (city).</p>
<dd>
<dt><code>%D Ta </code><code>Ta </code><code>Ta </code>Reference date.</p>
<dd>
<dt><code>%J Ta </code>Yes Ta Yes Ta Reference journal title.</p>
<dd>
<dt><code>%N Ta </code><code>Ta </code><code>Ta </code>Reference issue number.</p>
<dd>
<dt><code>%O Ta </code><code>Ta </code><code>Ta </code>Reference optional information.</p>
<dd>
<dt><code>%P Ta </code><code>Ta </code><code>Ta </code>Reference page number(s).</p>
<dd>
<dt><code>%R Ta </code><code>Ta </code><code>Ta </code>Reference report Name.</p>
<dd>
<dt><code>%T Ta </code>Yes Ta Yes Ta Reference article title.</p>
<dd>
<dt><code>%V Ta </code><code>Ta </code><code>Ta </code>Reference volume.</p>
<dd>
<dt><code>Ac </code>Ta Yes Ta Yes Ta Angle close quote.</p>
<dd>
<dt><code>Ao </code>Ta Yes Ta Yes Ta Angle open quote.</p>
<dd>
<dt><code>Ap </code>Ta Yes Ta Yes Ta Apostrophe.</p>
<dd>
<dt><code>Aq </code>Ta Yes Ta Yes Ta Angle quote.</p>
<dd>
<dt><code>AT&amp;T System Ta </code><code>Ta </code><code>Ta </code><code>AT&amp;T UNIX</code></p>
<dd>
<dt><code>Bc </code>Ta Yes Ta Yes Ta Bracket close quote.</p>
<dd>
<dt><code>Bf </code>Ta <code>Ta </code><code>Ta </code>Begin font mode.</p>
<dd>
<dt><code>Bo </code>Ta Yes Ta Yes Ta Bracket open quote.</p>
<dd>
<dt><code>Bq </code>Ta Yes Ta Yes Ta Bracket quote.</p>
<dd>
<dt><code>BSD Ta </code>Yes Ta Yes Ta BSD</p>
<dd>
<dt><code>Db </code>Ta <code>Ta </code><code>Ta </code>Debug (default is &quot;off&quot;)</p>
<dd>
<dt><code>Dc </code>Ta Yes Ta Yes Ta Double close quote.</p>
<dd>
<dt><code>Do </code>Ta Yes Ta Yes Ta Double open quote.</p>
<dd>
<dt><code>&#8220;Ta </code>Yes Ta Yes Ta Double quote. &#8221;</p>
<dd>
<dt><code>Ec </code>Ta Yes Ta Yes Ta Enclose string close quote.</p>
<dd>
<dt><code>Ef </code>Ta <code>Ta </code><code>Ta </code>End font mode.</p>
<dd>
<dt><i>Ta </i>Yes Ta Yes Ta Emphasis (traditional English).</p>
<dd>
<dt><code>Eo </code>Ta Yes Ta Yes Ta Enclose string open quote.</p>
<dd>
<dt><code>Fx </code>Ta <code>Ta </code><code>Ta </code><code>FreeBSD operating system</code></p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta Normal text (no-op).</p>
<dd>
<dt><code>Ta </code>Yes Ta Yes Ta <code>space.</code></p>
<dd>
<dt><code>Pc </code>Ta Yes Ta Yes Ta Parenthesis close quote.</p>
<dd>
<dt><code>Ta </code>Yes Ta <code>Ta </code>Prefix string.</p>
<dd>
<dt><code>Po </code>Ta Yes Ta Yes Ta Parenthesis open quote.</p>
<dd>
<dt><code>(Ta </code>Yes Ta Yes Ta Parentheses quote. )</p>
<dd>
<dt><code>Qc </code>Ta Yes Ta Yes Ta Straight Double close quote.</p>
<dd>
<dt><code>`Ta </code>Yes &#8216;</p>
<dd>Ta Yes Ta Quoted literal.</p>
<dt><code>Qo </code>Ta Yes Ta Yes Ta Straight Double open quote.</p>
<dd>
<dt><code>Qq </code>Ta Yes Ta Yes Ta Straight Double quote.</p>
<dd>
<dt><code></dl>
</dl>
<p> </code></p>
<dd>Li Rs Ta No Ta No Ta &quot;Reference start.&quot; Li Rv Ta No Ta No Ta &quot;Return values (sections two and three only).&quot; Li Sc Ta Yes Ta Yes Ta &quot;Single close quote.&quot; Li So Ta Yes Ta Yes Ta &quot;Single open quote.&quot; Li Sq Ta Yes Ta Yes Ta &quot;Single quote.&quot; Li Sm Ta No Ta No Ta &quot;Space mode (default is \*qon\*q)&quot; Li Sx Ta Yes Ta Yes Ta &quot;Section Cross Reference.&quot; Li Sy Ta Yes Ta Yes Ta &quot;Symbolic (traditional English).&quot; Li Tn Ta Yes Ta Yes Ta &quot;Trade or type name (small Caps).&quot; Li Ux Ta Yes Ta Yes Ta Ux Li Xc Ta Yes Ta Yes Ta &quot;Extend argument list close.&quot; Li Xo Ta Yes Ta Yes Ta &quot;Extend argument list open.&quot; </p>
<p> Macro names ending in `q&#8217; quote remaining items on the argument list. Macro names ending in `o&#8217; begin a quote which may span more than one line of input and are close quoted with the matching macro name ending in `c&#8217; Enclosure macros may be nested and are limited to eight arguments. </p>
<p> Note: the extended argument list macros ( `. &#8216; `. &#8216; and the function enclosure macros ( `.Fo , &#8216; `.Fc ) &#8216; are irregular. The extended list macros are used when the number of macro arguments would exceed the troff limitation of nine arguments. </p>
<p> The macros UR (starting a URI/URL hypertext reference), UE (ending one), and UN (identifying a target for a reference) are also available. See <a href="/docs/linux/man/7-man/">man</a>(7) for more information on these macros.</p>
<h2>Files</h2>
<dl>
<dt><code>doc.tmac </code></p>
<dd>Manual and general text domain macros.</p>
<dt><code>tmac/doc-common </code></p>
<dd>Common structural macros and definitions.</p>
<dt><code>tmac/doc-nroff </code></p>
<dd>Site dependent nroff style file.</p>
<dt><code>tmac/doc-ditroff </code></p>
<dd>Site dependent troff style file.</p>
<dt><code>tmac/doc-syms </code></p>
<dd>Special defines (such as the standards macro).</dl>
<h2>See Also</h2>
<p>groff_mdoc7, <a href="/docs/linux/man/7-man/">man</a>(7), man-pages7, mdoc.samples7</p>
<h2>Colophon</h2>
<p>This page is part of release 4.15 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
