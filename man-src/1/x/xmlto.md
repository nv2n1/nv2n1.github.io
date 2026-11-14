---
title: "xmlto(1)"
name: "xmlto"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmlto/"
description: "xmlto – apply an XSL stylesheet to an XML document"
---

<h2 class="name">NAME</h2>
<p> xmlto &#8211; apply an XSL stylesheet to an XML document </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xmlto</code> [<code>-o</code>&nbsp;<wbr><i>output_dir</i>] [<code>-x</code>&nbsp;<wbr><i>custom_xsl</i>] [<code>-m</code>&nbsp;<wbr><i>xsl_fragment</i>] [<code>-v</code>] [<code>-p</code>&nbsp;<wbr><i>postprocessor_opts</i>] [<code>&#8211;extensions</code>] [<code>&#8211;searchpath</code>&nbsp;<wbr><i>path</i>] [<code>&#8211;skip-validation</code>] [<code>&#8211;stringparam</code>&nbsp;<wbr><i>paramname</i>=<i>paramvalue</i>] [<code>&#8211;noclean</code>] [<code>&#8211;noautosize</code>] [<code>&#8211;noextensions</code>] [<code>&#8211;with-fop</code>] [<code>&#8211;with-dblatex</code>] {<i>format</i>} {<i>file</i>}</p>
<dt> <code>xmlto</code> {[&#8211;help] | [&#8211;version]}</dl>
<h2>DESCRIPTION</h2>
<dd>The purpose of <code>xmlto</code> is to convert an XML <i>file</i> to the desired <i>format</i> using whatever means necessary. This may involve two steps: </p>
<dl>
<dt>
<dd> 1. The application of an appropriate XSL stylesheet using an XSL-T processor.</dl>
<dl>
<dt>
<dd> 2. Further processing with other tools. This step may not be necessary.</dl>
<p> To decide which stylesheet to use and what, if any, needs to be done to post-process the output, <code>xmlto</code> makes use of format scripts, which are simple shell scripts that <code>xmlto</code> calls during the conversion. </p>
<p> The appropriate format script is selected based on the type of XML file and the desired output format. <code>xmlto</code> comes with some format scripts for converting DocBook XML files to a variety of formats. You may specify your own format script by using an absolute filename for <i>format</i> on the command line. </p>
<p> Firstly, if <code>xmlto</code> has not been told explicitly which stylesheet to use (with the <code>-x</code> option), the format script will be called with <code>$1</code> set to stylesheet. The environment variable <code>XSLT_PROCESSOR</code> contains the base name of the executable that will be used to perform the XSL-T transformation (for example xsltproc). The format script should write the name of the stylesheet to use to standard output and exit successfully, or exit with a non-zero return code if there is no appropriate stylesheet to use (for example, if the only available stylesheet is known not to work with the XSL-T processor that will be used). If nothing is written to standard output but the script exits successfully, no XSL-T transformation will be performed. </p>
<p> Secondly, after an XSL-T processor has been run using the stylesheet, the format script will be called again, this time with <code>$1</code> set to post-process. The format script should perform any necessary steps to translate the XSL-T processed output into the desired output format, including copying the output to the desired output directory. For post-processing, the format script is run in a temporary directory containing just the processed output (whose name is stored in <code>XSLT_PROCESSED</code> and whose basename is that of the original XML file with any filename extension replaced with .proc). <code>INPUT_FILE</code> is set to the name of the original XML file, <code>OUTPUT_DIR</code> is set to the name of the directory that the output (and only the output) must end up in, and <code>SEARCHPATH</code> is set to a colon-separate list of fallback directories in which to look for input (for images, for example). If this step is unsuccessful the format script should exit with a non-zero return code.</p>
<h2>OPTIONS</h2>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Be verbose (<code>-vv</code> for very verbose).</dl>
<p> <code>-x</code> <i>stylesheet</i></p>
<dl>
<dt>
<dd> Use <i>stylesheet</i> instead of asking the format script to choose one.</dl>
<p> <code>-m</code> <i>fragment</i></p>
<dl>
<dt>
<dd> Use the provided XSL <i>fragment</i> to modify the stylesheet.</dl>
<p> <code>-o</code> <i>directory</i></p>
<dl>
<dt>
<dd> Put output in the specified <i>directory</i> instead of the current working directory.</dl>
<p> <code>-p</code> <i>postprocessor_opts</i></p>
<dl>
<dt>
<dd> Pass <i>postprocessor_opts</i> to processing stages after stylesheet application (e.g. lynx or links when going through HTML to text, or xmltex when going from through TeX to DVI). If <code>-p</code> is specified a second time, the options specified will be passed to second-stage postprocessing; presently this is only applicable when going through xmltex and dvips to PostScript.</dl>
<p> <code>&#8211;extensions</code></p>
<dl>
<dt>
<dd> Turn on stylesheet extensions for the tool chain in use (<i>use.extensions</i> is turned on). The variables turned on are the ones used by Norman Walsh&#8217;s DocBook XSL stylesheets.</dl>
<p> <code>&#8211;searchpath</code> <i>path</i></p>
<dl>
<dt>
<dd> Add the colon-separated list of directories in <i>path</i> as fallback directories for including input.</dl>
<p> <code>&#8211;skip-validation</code></p>
<dl>
<dt>
<dd> Skip the validation step that is normally performed.</dl>
<p> <code>&#8211;stringparam</code> <i>paramname</i>=<i>paramvalue</i></p>
<dl>
<dt>
<dd> Pass a named parameter <i>paramname</i> with value <i>paramvalue</i> to stylesheet from the command line.</dl>
<p> <code>&#8211;noclean</code></p>
<dl>
<dt>
<dd> Temporary files are not deleted(their names are shown and kept in tmp directory). It could help with analyzing problems.</dl>
<p> <code>&#8211;noautosize</code></p>
<dl>
<dt>
<dd> By default, some XSL variables are overriden by autodetection (<i>page.width</i> and <i>page.height</i> for paperconf (libpaper) use, <i>paper.type</i> for locale-based (<code>LC_PAPER</code>) selection). With this option, <code>xmlto</code> doesn&#8217;t use this autodetection and user is able to modify defaults himself (either via default param.xsl modification or by user-defined XSL fragment).</dl>
<p> <code>&#8211;noextensions</code></p>
<dl>
<dt>
<dd> By default, <code>xmlto</code> enables XSL params <i>passivetex.extensions</i> for passivetex backend and <i>fop.extensions</i> and <i>fop1.extensions</i> for fop backend. This usually produces better results. If you for some reason don&#8217;t want to use these parameters, just disable them using this option.</dl>
<p> <code>&#8211;with-fop</code></p>
<dl>
<dt>
<dd> Use fop for formatting. It is an experimental option, expects fop in specific location(detected at configured time), could be changed manually in <code>xmlto</code> script by modification of <i>FOP_PATH</i></dl>
<p> <code>&#8211;with-dblatex</code></p>
<dl>
<dt>
<dd> Use dblatex for formatting. It is an experimental option, expects dblatex in specific location(detected at configured time), could be changed manually in <code>xmlto</code> script by modification of <i>DBLATEX_PATH</i></dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message. It will describe xmlto&#8217;s options, and the available output formats.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of xmlto.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>XSLT_PROCESSOR</code></p>
<dl>
<dt>
<dd> Base name of the executable that will be used to perform the XSL-T transformation (default: <code><a href="/docs/linux/man/1-xsltproc/">xsltproc</a></code>(1)).</dl>
<p> <code>TMPDIR</code></p>
<dl>
<dt>
<dd> Directory, where to create temporary stylesheets (default: /tmp).</dl>
<h2>DIAGNOSTICS</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Everything went fine. This is the expected exit code.</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> <code>xmlto</code> was called with insufficient arguments.</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-mktemp/">mktemp</a></code>(1) failed to create a file/directory. Make sure /tmp or <code>TMPDIR</code> is writable.</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> <code>xmlto</code> failed to find some binary on configured location. Make sure that all required packages are installed and paths in xmlto script are set properly.</dl>
<p> <code>10+(Validation non-zero error code)</code></p>
<dl>
<dt>
<dd> <code>xmlto</code> tried to validate a xml document, but validation failed. For better diagnostic, validation output and xmllint exit code is provided. Consider either fixing your document or using <code>&#8211;skip-validation</code>.</dl>
<h2>EXAMPLES</h2>
<p> To convert a DocBook XML document to PDF, use: </p>
<dl>
<dt>
<dd>
<pre>
<code>xmlto pdf mydoc.xml</code>
</pre>
</dl>
<p> To convert a DocBook XML document to HTML and store the resulting HTML files in a separate directory use: </p>
<dl>
<dt>
<dd>
<pre>
<code>xmlto -o html-dir html mydoc.xml</code>
</pre>
</dl>
<p> To convert a DocBook XML document to a single HTML file use: </p>
<dl>
<dt>
<dd>
<pre>
<code>xmlto html-nochunks mydoc.xml</code>
</pre>
</dl>
<p> To modify the output using an XSL fragment use: </p>
<dl>
<dt>
<dd>
<pre>
<code>xmlto -m ulink.xsl pdf mydoc.xml</code>
</pre>
</dl>
<p> To specify which stylesheet to use (overriding the one that the format script would choose) use: </p>
<dl>
<dt>
<dd>
<pre>
<code>xmlto -x mystylesheet.xsl pdf mydoc.xml</code>
</pre>
</dl>
<h2>AUTHORS</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Original author, maintainer until 0.0.18</dl>
<p> <code>Ondřej Vavs&iacute;k</code> &lt;ovasik [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Maintainer since 0.0.19</dl>
<h2>COPYRIGHT</h2>
<h2>Index</h2>
