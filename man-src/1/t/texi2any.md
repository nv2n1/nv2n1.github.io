---
title: "texi2any(1)"
name: "texi2any"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texi2any/"
description: "texi2any – translate Texinfo documents"
---

<h2 class="name">NAME</h2>
<p> texi2any &#8211; translate Texinfo documents </p>
<h2>SYNOPSIS</h2>
<p> <code>makeinfo</code> [<i>,OPTION/</i>]&#8230; <i>,TEXINFO-FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Translate Texinfo source documentation to various other formats, by default Info files suitable for reading online with Emacs or standalone GNU Info. </p>
<p> This program is commonly installed as both `makeinfo&#8217; and `texi2any&#8217;; the behavior is identical, and does not depend on the installed name.</p>
<h3>General options:</h3>
<dl>
<dt><code>&#8211;document-language</code>=<i>,STR/</i> locale to use in translating Texinfo keywords</p>
<dd> for the output document (default C).</p>
<dt><code>&#8211;error-limit</code>=<i>,NUM/</i></p>
<dd> quit after NUM errors (default 100).</p>
<dt><code>&#8211;force</code></p>
<dd> preserve output even if errors.</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit.</p>
<dt><code>&#8211;no-validate</code></p>
<dd> suppress node cross-reference validation.</p>
<dt><code>&#8211;no-warn</code></p>
<dd> suppress warnings (but not errors).</p>
<dt><code>&#8211;conf-dir</code>=<i>,DIR/</i></p>
<dd> search also for initialization files in DIR.</p>
<dt><code>&#8211;init-file</code>=<i>,FILE/</i></p>
<dd> load FILE to modify the default behavior.</p>
<dt><code>-c</code>, <code>&#8211;set-customization-variable</code> VAR=VAL</p>
<dd> set customization variable VAR to value VAL.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> explain what is being done.</p>
<dt><code>&#8211;version</code></p>
<dd> display version information and exit.</dl>
<h3>Output format selection (default is to produce Info):</h3>
<dl>
<dt><code>&#8211;docbook</code></p>
<dd> output Docbook XML rather than Info.</p>
<dt><code>&#8211;html</code></p>
<dd> output HTML rather than Info.</p>
<dt><code>&#8211;plaintext</code></p>
<dd> output plain text rather than Info.</p>
<dt><code>&#8211;xml</code></p>
<dd> output Texinfo XML rather than Info.</p>
<dt><code>&#8211;dvi</code>, <code>&#8211;dvipdf</code>, <code>&#8211;ps</code>, <code>&#8211;pdf</code></p>
<dd> call texi2dvi to generate given output, after checking validity of TEXINFO-FILE.</dl>
<h3>General output options:</h3>
<dl>
<dt><code>-E</code>, <code>&#8211;macro-expand</code>=<i>,FILE/</i></p>
<dd> output macro-expanded source to FILE, ignoring any @setfilename.</p>
<dt><code>&#8211;no-headers</code></p>
<dd> suppress node separators, Node: lines, and menus from Info output (thus producing plain text) or from HTML (thus producing shorter output). Also, if producing Info, write to standard output by default.</p>
<dt><code>&#8211;no-split</code></p>
<dd> suppress any splitting of the output; generate only one output file.</p>
<dt><code>&#8211;[no-]number-sections</code></p>
<dd> output chapter and sectioning numbers; default is on.</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,DEST/</i></p>
<dd> output to DEST. With split output, create DEST as a directory</p>
<dt>and put the output files there.</p>
<dd> With non-split output, if DEST is already</p>
<dt>a directory or ends with a /,</p>
<dd> put the output file there.</p>
<dt>
<dd> Otherwise, DEST names the output file.</dl>
<h3>Options for Info and plain text:</h3>
<dl>
<dt><code>&#8211;disable-encoding</code></p>
<dd> do not output accented and special characters in Info output based on @documentencoding.</p>
<dt><code>&#8211;enable-encoding</code></p>
<dd> override <code>&#8211;disable-encoding</code> (default).</p>
<dt><code>&#8211;fill-column</code>=<i>,NUM/</i></p>
<dd> break Info lines at NUM characters (default 72).</p>
<dt><code>&#8211;footnote-style</code>=<i>,STYLE/</i></p>
<dd> output footnotes in Info according to STYLE: `separate&#8217; to put them in their own node; `end&#8217; to put them at the end of the node, in which they are defined (this is the default).</p>
<dt><code>&#8211;paragraph-indent</code>=<i>,VAL/</i></p>
<dd> indent Info paragraphs by VAL spaces (default 3). If VAL is `none&#8217;, do not indent; if VAL is `asis&#8217;, preserve existing indentation.</p>
<dt><code>&#8211;split-size</code>=<i>,NUM/</i></p>
<dd> split Info files at size NUM (default 300000).</dl>
<h3>Options for HTML:</h3>
<dl>
<dt><code>&#8211;css-include</code>=<i>,FILE/</i></p>
<dd> include FILE in HTML &lt;style&gt; output; read stdin if FILE is -.</p>
<dt><code>&#8211;css-ref</code>=<i>,URL/</i></p>
<dd> generate CSS reference to URL.</p>
<dt><code>&#8211;internal-links</code>=<i>,FILE/</i></p>
<dd> produce list of internal links in FILE.</p>
<dt><code>&#8211;split</code>=<i>,SPLIT/</i></p>
<dd> split at SPLIT, where SPLIT may be `chapter&#8217;, `section&#8217; or `node&#8217;.</p>
<dt><code>&#8211;transliterate-file-names</code></p>
<dd> use file names in ASCII transliteration.</p>
<dt><code>&#8211;node-files</code></p>
<dd> produce redirection files for nodes and anchors; default is set only if split.</dl>
<h3>Options for XML and Docbook:</h3>
<dl>
<dt><code>&#8211;output-indent</code>=<i>,VAL/</i></p>
<dd> does nothing, retained for compatibility.</dl>
<h3>Options for DVI/PS/PDF:</h3>
<dl>
<dt><code>&#8211;Xopt</code>=<i>,OPT/</i></p>
<dd> pass OPT to texi2dvi; can be repeated.</dl>
<h3>Input file options:</h3>
<dl>
<dt><code>&#8211;commands-in-node-names</code></p>
<dd> does nothing, retained for compatibility.</p>
<dt><code>-D</code> VAR</p>
<dd> define the variable VAR, as with @set.</p>
<dt><code>-D</code> &#8216;VAR VAL&#8217;</p>
<dd> define VAR to VAL (one shell argument).</p>
<dt><code>-I</code> DIR</p>
<dd> append DIR to the @include search path.</p>
<dt><code>-P</code> DIR</p>
<dd> prepend DIR to the @include search path.</p>
<dt><code>-U</code> VAR</p>
<dd> undefine the variable VAR, as with @clear.</dl>
<h3>Conditional processing in input:</h3>
<dl>
<dt><code>&#8211;ifdocbook</code></p>
<dd> process @ifdocbook and @docbook even if not generating Docbook.</p>
<dt><code>&#8211;ifhtml</code></p>
<dd> process @ifhtml and @html even if not generating HTML.</p>
<dt><code>&#8211;ifinfo</code></p>
<dd> process @ifinfo even if not generating Info.</p>
<dt><code>&#8211;ifplaintext</code></p>
<dd> process @ifplaintext even if not generating plain text.</p>
<dt><code>&#8211;iftex</code></p>
<dd> process @iftex and @tex.</p>
<dt><code>&#8211;ifxml</code></p>
<dd> process @ifxml and @xml.</p>
<dt><code>&#8211;no-ifdocbook</code></p>
<dd> do not process @ifdocbook and @docbook text.</p>
<dt><code>&#8211;no-ifhtml</code></p>
<dd> do not process @ifhtml and @html text.</p>
<dt><code>&#8211;no-ifinfo</code></p>
<dd> do not process @ifinfo text.</p>
<dt><code>&#8211;no-ifplaintext</code></p>
<dd> do not process @ifplaintext text.</p>
<dt><code>&#8211;no-iftex</code></p>
<dd> do not process @iftex and @tex text.</p>
<dt><code>&#8211;no-ifxml</code></p>
<dd> do not process @ifxml and @xml text.</dl>
<p> Also, for the <code>&#8211;no-ifFORMAT</code> options, do process @ifnotFORMAT text. </p>
<p> The defaults for the @if&#8230; conditionals depend on the output format: if generating Docbook, <code>&#8211;ifdocbook</code> is on and the others are off; if generating HTML, <code>&#8211;ifhtml</code> is on and the others are off; if generating Info, <code>&#8211;ifinfo</code> is on and the others are off; if generating plain text, <code>&#8211;ifplaintext</code> is on and the others are off; if generating XML, <code>&#8211;ifxml</code> is on and the others are off.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>makeinfo foo.texi</p>
<dd> write Info to foo&#8217;s @setfilename</p>
<dt>makeinfo &#8211;html foo.texi</p>
<dd> write HTML to @setfilename</p>
<dt>makeinfo &#8211;xml foo.texi</p>
<dd> write Texinfo XML to @setfilename</p>
<dt>makeinfo &#8211;docbook foo.texi</p>
<dd> write Docbook XML to @setfilename</p>
<dt>makeinfo &#8211;plaintext foo.texi</p>
<dd> write plain text to standard output</p>
<dt>makeinfo &#8211;pdf foo.texi</p>
<dd> write PDF using texi2dvi</p>
<dt>makeinfo &#8211;html &#8211;no-headers foo.texi</p>
<dd> write html without node lines, menus</p>
<dt>makeinfo &#8211;number-sections foo.texi</p>
<dd> write Info with numbered sections</p>
<dt>makeinfo &#8211;no-split foo.texi</p>
<dd> write one Info file however big</dl>
<h2>REPORTING BUGS</h2>
<p> Email bug reports to bug-texinfo [at] gnu.org, general questions and discussion to help-texinfo [at] gnu.org.<br />
 Texinfo home page: <a rel="nofollow" href="http://www.gnu.org/software/texinfo/">http://www.gnu.org/software/texinfo/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>texi2any</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>texi2any</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info texi2any</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
