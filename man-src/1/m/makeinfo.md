---

title: "makeinfo(1)"
name: "makeinfo"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makeinfo/"
description: "texi2any – translate Texinfo documents"
---

<p> texi2any &#8211; translate Texinfo documents </p>
<h2>SYNOPSIS</h2>
<p> <code>makeinfo</code> [<i>,OPTION/</i>]&#8230; <i>,TEXINFO-FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Translate Texinfo source documentation to various other formats, by default Info files suitable for reading online with Emacs or standalone GNU Info. </p>
<p> This program is commonly installed as both `makeinfo&#8217; and `texi2any&#8217;; the behavior is identical, and does not depend on the installed name.</p>
<h3>General options:</h3>
<dl>
<dt><code>&#8211;document-language</code>=<i>,STR/</i> locale to use in translating Texinfo keywords</dt>
<dd> for the output document (default C).</dd>
<dt><code>&#8211;error-limit</code>=<i>,NUM/</i></dt>
<dd> quit after NUM errors (default 100).</dd>
<dt><code>&#8211;force</code></dt>
<dd> preserve output even if errors.</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit.</dd>
<dt><code>&#8211;no-validate</code></dt>
<dd> suppress node cross-reference validation.</dd>
<dt><code>&#8211;no-warn</code></dt>
<dd> suppress warnings (but not errors).</dd>
<dt><code>&#8211;conf-dir</code>=<i>,DIR/</i></dt>
<dd> search also for initialization files in DIR.</dd>
<dt><code>&#8211;init-file</code>=<i>,FILE/</i></dt>
<dd> load FILE to modify the default behavior.</dd>
<dt><code>-c</code>, <code>&#8211;set-customization-variable</code> VAR=VAL</dt>
<dd> set customization variable VAR to value VAL.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> explain what is being done.</dd>
<dt><code>&#8211;version</code></dt>
<dd> display version information and exit.</dd></dl>
<h3>Output format selection (default is to produce Info):</h3>
<dl>
<dt><code>&#8211;docbook</code></dt>
<dd> output Docbook XML rather than Info.</dd>
<dt><code>&#8211;html</code></dt>
<dd> output HTML rather than Info.</dd>
<dt><code>&#8211;plaintext</code></dt>
<dd> output plain text rather than Info.</dd>
<dt><code>&#8211;xml</code></dt>
<dd> output Texinfo XML rather than Info.</dd>
<dt><code>&#8211;dvi</code>, <code>&#8211;dvipdf</code>, <code>&#8211;ps</code>, <code>&#8211;pdf</code></dt>
<dd> call texi2dvi to generate given output, after checking validity of TEXINFO-FILE.</dd></dl>
<h3>General output options:</h3>
<dl>
<dt><code>-E</code>, <code>&#8211;macro-expand</code>=<i>,FILE/</i></dt>
<dd> output macro-expanded source to FILE, ignoring any @setfilename.</dd>
<dt><code>&#8211;no-headers</code></dt>
<dd> suppress node separators, Node: lines, and menus from Info output (thus producing plain text) or from HTML (thus producing shorter output). Also, if producing Info, write to standard output by default.</dd>
<dt><code>&#8211;no-split</code></dt>
<dd> suppress any splitting of the output; generate only one output file.</dd>
<dt><code>&#8211;[no-]number-sections</code></dt>
<dd> output chapter and sectioning numbers; default is on.</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,DEST/</i></dt>
<dd> output to DEST. With split output, create DEST as a directory</dd>
<dt>and put the output files there.</dt>
<dd> With non-split output, if DEST is already</dd>
<dt>a directory or ends with a /,</dt>
<dd> put the output file there.</dd>
<dt>
</dt><dd> Otherwise, DEST names the output file.</dd></dl>
<h3>Options for Info and plain text:</h3>
<dl>
<dt><code>&#8211;disable-encoding</code></dt>
<dd> do not output accented and special characters in Info output based on @documentencoding.</dd>
<dt><code>&#8211;enable-encoding</code></dt>
<dd> override <code>&#8211;disable-encoding</code> (default).</dd>
<dt><code>&#8211;fill-column</code>=<i>,NUM/</i></dt>
<dd> break Info lines at NUM characters (default 72).</dd>
<dt><code>&#8211;footnote-style</code>=<i>,STYLE/</i></dt>
<dd> output footnotes in Info according to STYLE: `separate&#8217; to put them in their own node; `end&#8217; to put them at the end of the node, in which they are defined (this is the default).</dd>
<dt><code>&#8211;paragraph-indent</code>=<i>,VAL/</i></dt>
<dd> indent Info paragraphs by VAL spaces (default 3). If VAL is `none&#8217;, do not indent; if VAL is `asis&#8217;, preserve existing indentation.</dd>
<dt><code>&#8211;split-size</code>=<i>,NUM/</i></dt>
<dd> split Info files at size NUM (default 300000).</dd></dl>
<h3>Options for HTML:</h3>
<dl>
<dt><code>&#8211;css-include</code>=<i>,FILE/</i></dt>
<dd> include FILE in HTML &lt;style&gt; output; read stdin if FILE is -.</dd>
<dt><code>&#8211;css-ref</code>=<i>,URL/</i></dt>
<dd> generate CSS reference to URL.</dd>
<dt><code>&#8211;internal-links</code>=<i>,FILE/</i></dt>
<dd> produce list of internal links in FILE.</dd>
<dt><code>&#8211;split</code>=<i>,SPLIT/</i></dt>
<dd> split at SPLIT, where SPLIT may be `chapter&#8217;, `section&#8217; or `node&#8217;.</dd>
<dt><code>&#8211;transliterate-file-names</code></dt>
<dd> use file names in ASCII transliteration.</dd>
<dt><code>&#8211;node-files</code></dt>
<dd> produce redirection files for nodes and anchors; default is set only if split.</dd></dl>
<h3>Options for XML and Docbook:</h3>
<dl>
<dt><code>&#8211;output-indent</code>=<i>,VAL/</i></dt>
<dd> does nothing, retained for compatibility.</dd></dl>
<h3>Options for DVI/PS/PDF:</h3>
<dl>
<dt><code>&#8211;Xopt</code>=<i>,OPT/</i></dt>
<dd> pass OPT to texi2dvi; can be repeated.</dd></dl>
<h3>Input file options:</h3>
<dl>
<dt><code>&#8211;commands-in-node-names</code></dt>
<dd> does nothing, retained for compatibility.</dd>
<dt><code>-D</code> VAR</dt>
<dd> define the variable VAR, as with @set.</dd>
<dt><code>-D</code> &#8216;VAR VAL&#8217;</dt>
<dd> define VAR to VAL (one shell argument).</dd>
<dt><code>-I</code> DIR</dt>
<dd> append DIR to the @include search path.</dd>
<dt><code>-P</code> DIR</dt>
<dd> prepend DIR to the @include search path.</dd>
<dt><code>-U</code> VAR</dt>
<dd> undefine the variable VAR, as with @clear.</dd></dl>
<h3>Conditional processing in input:</h3>
<dl>
<dt><code>&#8211;ifdocbook</code></dt>
<dd> process @ifdocbook and @docbook even if not generating Docbook.</dd>
<dt><code>&#8211;ifhtml</code></dt>
<dd> process @ifhtml and @html even if not generating HTML.</dd>
<dt><code>&#8211;ifinfo</code></dt>
<dd> process @ifinfo even if not generating Info.</dd>
<dt><code>&#8211;ifplaintext</code></dt>
<dd> process @ifplaintext even if not generating plain text.</dd>
<dt><code>&#8211;iftex</code></dt>
<dd> process @iftex and @tex.</dd>
<dt><code>&#8211;ifxml</code></dt>
<dd> process @ifxml and @xml.</dd>
<dt><code>&#8211;no-ifdocbook</code></dt>
<dd> do not process @ifdocbook and @docbook text.</dd>
<dt><code>&#8211;no-ifhtml</code></dt>
<dd> do not process @ifhtml and @html text.</dd>
<dt><code>&#8211;no-ifinfo</code></dt>
<dd> do not process @ifinfo text.</dd>
<dt><code>&#8211;no-ifplaintext</code></dt>
<dd> do not process @ifplaintext text.</dd>
<dt><code>&#8211;no-iftex</code></dt>
<dd> do not process @iftex and @tex text.</dd>
<dt><code>&#8211;no-ifxml</code></dt>
<dd> do not process @ifxml and @xml text.</dd></dl>
<p> Also, for the <code>&#8211;no-ifFORMAT</code> options, do process @ifnotFORMAT text. </p>
<p> The defaults for the @if&#8230; conditionals depend on the output format: if generating Docbook, <code>&#8211;ifdocbook</code> is on and the others are off; if generating HTML, <code>&#8211;ifhtml</code> is on and the others are off; if generating Info, <code>&#8211;ifinfo</code> is on and the others are off; if generating plain text, <code>&#8211;ifplaintext</code> is on and the others are off; if generating XML, <code>&#8211;ifxml</code> is on and the others are off.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>makeinfo foo.texi</dt>
<dd> write Info to foo&#8217;s @setfilename</dd>
<dt>makeinfo &#8211;html foo.texi</dt>
<dd> write HTML to @setfilename</dd>
<dt>makeinfo &#8211;xml foo.texi</dt>
<dd> write Texinfo XML to @setfilename</dd>
<dt>makeinfo &#8211;docbook foo.texi</dt>
<dd> write Docbook XML to @setfilename</dd>
<dt>makeinfo &#8211;plaintext foo.texi</dt>
<dd> write plain text to standard output</dd>
<dt>makeinfo &#8211;pdf foo.texi</dt>
<dd> write PDF using texi2dvi</dd>
<dt>makeinfo &#8211;html &#8211;no-headers foo.texi</dt>
<dd> write html without node lines, menus</dd>
<dt>makeinfo &#8211;number-sections foo.texi</dt>
<dd> write Info with numbered sections</dd>
<dt>makeinfo &#8211;no-split foo.texi</dt>
<dd> write one Info file however big</dd></dl>
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
</dt><dd> <code>info texi2any</code></dd></dl>
<p> should give you access to the complete manual. </p>
