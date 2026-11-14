---
title: "ssconvert(1)"
name: "ssconvert"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssconvert/"
description: "ssconvert – a command line spreadsheet format converter"
---

<h2 class="name">NAME</h2>
<p> ssconvert &#8211; a command line spreadsheet format converter</p>
<h2>SYNOPSIS</h2>
<p> <code>ssconvert</code> [<i>OPTIONS</i>] <i>infile</i> <i>outfile</i> </p>
<p> <code>ssconvert</code> [<i>OPTIONS</i>] <code>&#8211;merge-to</code> <i>outfile</i> <i>infile1</i> <i>infile2</i> <code>&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ssconvert</code> is a command line utility to convert spreadsheet files between various spreadsheet file formats. It is a companion utility to <code>Gnumeric</code>, the powerful spreadsheet program created by the GNOME project. </p>
<p> <code>ssconvert</code> accepts either file names or URIs as <i>infile</i> <i>outfile</i>. The special URIs <i>fd://0</i> and <i>fd://1</i> can be used for standard input and standard output respectively. </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with single letter options starting with a single dash (`-&#8216;) and longer options starting with two dashes (`&#8211;&#8216;). </p>
<h3>Main options</h3>
<dl>
<dt><code>&#8211;recalc</code></p>
<dd> Recalculate all cells before writing the result.</p>
<dt><code>&#8211;list-exporters</code></p>
<dd> List the available exporters (file formats that can be written).</p>
<dt><code>-T, &#8211;export-type=</code><i>ID</i></p>
<dd> Specify which exporter to use; see below for a list. This is only necessary when the right format does not follow from the output file name.</p>
<dt><code>-O, &#8211;export-options=</code><i>optionsstring</i></p>
<dd> Specify parameters for the chosen exporter. <i>optionsstring</i> is a list of <i>parameter</i>=<i>value</i> pairs, separated by spaces. The parameter names and values allowed are specific to the exporter and are documented below. Multiple parameters can be specified</p>
<dt><code>&#8211;list-importers</code></p>
<dd> List the available importers (file formats that can be read). <code>-I, &#8211;import-type=</code><i>ID</i> Specify which importer to use; see below for a list. This is only necessary when the right format does not follow from the input file name.</p>
<dt><code>-E, &#8211;import-encoding=</code><i>STRING</i></p>
<dd> Specify an encoding for imported content.</p>
<dt><code>-M, &#8211;merge-to=</code><i>FILENAME</i></p>
<dd> Merge a collection of workbooks into one. Sheet size will expand to the largest in all the workbooks. Names in the scope of individual workbooks will end up in the scope of the merged workbook. The merge will be aborted if there are name conflicts.</p>
<dt><code>-S, &#8211;export-file-per-sheet</code></p>
<dd> Export a file for each sheet if the exporter only supports one sheet at a time. The output filename is treated as a template in which sheet number is substituted for %n and/or sheet name is substituted for %s. If there are not substitutions, a default of &quot;.%s&quot; is added. </p>
</dl>
<h3>Help options</h3>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Display ssconvert&#8217;s version.</p>
<dt><code>-h, &#8211;help, &#8211;usage</code></p>
<dd> Display a brief usage message.</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options.</p>
<dt><code>&#8211;help-libspreadsheet</code></p>
<dd> Show Gnumeric options. </p>
</dl>
<h2>LIST OF IMPORTER/EXPORTER IDS</h2>
<p> The following IDs can be can be used both for import (reading) and export (writing).</p>
<dl>
<dt><code>Gnumeric_XmlIO:sax</code></p>
<dd> Gnumeric&#8217;s XML file format (*.gnumeric)</p>
<dt><code>Gnumeric_OpenCalc:openoffice</code></p>
<dd> OpenDocument &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/OpenDocument">http://en.wikipedia.org/wiki/OpenDocument</a> &gt; or OpenOffice Calc &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/OpenOffice.org_Calc">http://en.wikipedia.org/wiki/OpenOffice.org_Calc</a> &gt; (*.sxc, *.ods) format. As an exporter, this is ODF/OpenOffice without foreign elements (*.ods).</p>
<dt><code>Gnumeric_dif:dif</code></p>
<dd> Data Interchange Format &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Data_Interchange_Format">http://en.wikipedia.org/wiki/Data_Interchange_Format</a> &gt; (*.dif)</p>
<dt><code>Gnumeric_paradox:paradox</code></p>
<dd> Paradox database &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Paradox_%28database%29">http://en.wikipedia.org/wiki/Paradox_%28database%29</a> &gt; or primary index file (*.db, *.px)</p>
<dt><code>Gnumeric_stf:stf_assistant</code></p>
<dd> Text (configurable)</p>
<dt><code>Gnumeric_sylk:sylk</code></p>
<dd> MultiPlan &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Multiplan">http://en.wikipedia.org/wiki/Multiplan</a> &gt; Symbolic Link (SYLK) &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/SYmbolic_LinK_%28SYLK%29">http://en.wikipedia.org/wiki/SYmbolic_LinK_%28SYLK%29</a> &gt; (*.slk)</p>
<dt><code>Gnumeric_Excel:xlsx</code></p>
<dd> Microsoft Excel &#8482; 2007 (&quot;Office Open XML&quot;, OOXML &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/XLSX">http://en.wikipedia.org/wiki/XLSX</a> &gt; ) format </p>
</dl>
<h2>LIST OF IMPORTANT IMPORTER IDS</h2>
<dl>
<dt><code>Gnumeric_stf:stf_csvtab</code></p>
<dd> Comma or tab separated values (CSV/TSV) (*.csv)</p>
<dt><code>Gnumeric_html:html</code></p>
<dd> HTML (*.html, *.htm)</p>
<dt><code>Gnumeric_Excel:excel</code></p>
<dd> Microsoft Excel &#8482; (*.xls)</p>
<dt><code>Gnumeric_Excel:excel_xml</code></p>
<dd> Microsoft Excel &#8482; 2003 SpreadsheetML </p>
</dl>
<h2>LIST OF OTHER IMPORTER IDS</h2>
<dl>
<dt><code>Gnumeric_QPro:qpro</code></p>
<dd> Quattro Pro &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Quattro_Pro">http://en.wikipedia.org/wiki/Quattro_Pro</a> &gt; (*.wb1, *.wb2, *.wb3)</p>
<dt><code>Gnumeric_applix:applix</code></p>
<dd> Applix (*.as)</p>
<dt><code>Gnumeric_lotus:lotus</code></p>
<dd> Lotus 1-2-3 &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Lotus_1-2-3">http://en.wikipedia.org/wiki/Lotus_1-2-3</a> &gt; (*.wk1, *.wks, *.123)</p>
<dt><code>Gnumeric_mps:mps</code></p>
<dd> MPS (Mathematical Programming System) format &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/MPS_%28format%29">http://en.wikipedia.org/wiki/MPS_%28format%29</a> &gt; Linear programming and mixed integer programming file format (*.mps)</p>
<dt><code>Gnumeric_oleo:oleo</code></p>
<dd> GNU Oleo &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/GNU_Oleo">http://en.wikipedia.org/wiki/GNU_Oleo</a> &gt; (*.oleo)</p>
<dt><code>Gnumeric_plan_perfect:pln</code></p>
<dd> PlanPerfect Format (PLN)</p>
<dt><code>Gnumeric_psiconv:psiconv</code></p>
<dd> Psion (*.psisheet)</p>
<dt><code>Gnumeric_sc:sc</code></p>
<dd> SC/xspread</p>
<dt><code>Gnumeric_xbase:xbase</code></p>
<dd> xBase &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/XBase">http://en.wikipedia.org/wiki/XBase</a> &gt; (*.dbf) file format </p>
</dl>
<h2>LIST OF IMPORTANT EXPORTER IDS</h2>
<dl>
<dt><code>Gnumeric_OpenCalc:odf</code></p>
<dd> ODF/OpenOffice with foreign elements (*.ods)</p>
<dt><code>Gnumeric_glpk:glpk</code></p>
<dd> GLPK Linear Program Solver</p>
<dt><code>Gnumeric_html:html40</code></p>
<dd> HTML 4.0 (*.html)</p>
<dt><code>Gnumeric_html:html40frag</code></p>
<dd> HTML (*.html) fragment</p>
<dt><code>Gnumeric_html:xhtml</code></p>
<dd> XHTML (*.html)</p>
<dt><code>Gnumeric_html:xhtml_range</code></p>
<dd> XHTML range &#8211; for export to clipboard</p>
<dt><code>Gnumeric_pdf:pdf_assistant</code></p>
<dd> Portable Document Format (*.PDF)</p>
<dt><code>Gnumeric_stf:stf_csv</code></p>
<dd> Comma separated values (CSV)</p>
<dt><code>Gnumeric_Excel:excel_dsf</code></p>
<dd> Microsoft Excel &#8482; 97/2000/XP &amp; 5.0/95 </p>
</dl>
<h2>LIST OF OTHER EXPORTER IDS</h2>
<dl>
<dt><code>Gnumeric_Excel:excel_biff7</code></p>
<dd> Microsoft Excel &#8482; 5.0/95</p>
<dt><code>Gnumeric_Excel:excel_biff8</code></p>
<dd> Microsoft S Excel &#8482; 97/2000/XP</p>
<dt><code>Gnumeric_GnomeGlossary:po</code></p>
<dd> Gnome Glossary PO file format</p>
<dt><code>Gnumeric_html:html32</code></p>
<dd> HTML 3.2 (*.html)</p>
<dt><code>Gnumeric_html:latex</code></p>
<dd> LaTeX 2e (*.tex)</p>
<dt><code>Gnumeric_html:latex_table</code></p>
<dd> LaTeX 2e (*.tex) table fragment</p>
<dt><code>Gnumeric_html:roff</code></p>
<dd> TROFF &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Troff">http://en.wikipedia.org/wiki/Troff</a> &gt; (*.me) format.</p>
<dt><code>Gnumeric_lpsolve:lpsolve</code></p>
<dd> LPSolve &lt;URL: <a rel="nofollow" href="http://sourceforge.net/projects/lpsolve/">http://sourceforge.net/projects/lpsolve/</a> &gt; Mixed Integer Linear Programming (MILP) solver </p>
</dl>
<h2>OPTIONS FOR THE PORTABLE DOCUMENT FORMAT (*.pdf) EXPORTER</h2>
<dl>
<dt><code>sheet</code></p>
<dd> Name of the workbook sheet to operate on. You can specify several sheets by repeating this option. If this option is not given the active sheet (i. e. the sheet that was active when the file was saved) is used. This is ignored if the <code>object</code> option is given. </p>
<dt><code>object</code></p>
<dd> Name of the sheet object to print. If this option is given any <code>sheet</code> option is ignored. Only the first <code>object</code> given is exported. </p>
<dt><code>paper</code></p>
<dd> Paper size. Valid values include &quot;<code>A4</code>&quot; for ISO A4 and &quot;<code>na_letter_8.5x11in</code>&quot; for US Letter. If an individual graph is specified through the <code>object</code> option, then a paper size of &quot;<code>fit</code>&quot; reduces the size of the paper to the size of the graph. </p>
</dl>
<h2>OPTIONS FOR THE CONFIGURABLE TEXT (*.txt) EXPORTER</h2>
<dl>
<dt><code>sheet</code></p>
<dd> Name of the workbook sheet to operate on. You can specify several sheets by repeating this option. If this option is not given the active sheet (i. e. the sheet that was active when the file was saved) is used. </p>
<dt><code>eol</code></p>
<dd> End Of Line convention; how lines are terminated. &quot;<code>unix</code>&quot; for linefeed, &quot;<code>mac</code>&quot; for carriage return; &quot;<code>windows</code>&quot; for carriage return plus linefeed. </p>
<dt><code>charset</code></p>
<dd> The character encoding of the output. Defaults to UTF-8. </p>
<dt><code>locale</code></p>
<dd> The locale to use for number and date formatting. Defaults to the current locale as reported by <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1). Consult <code>locale -a</code> output for acceptable values. </p>
<dt><code>quote</code></p>
<dd> The character or string used for quoting fields. Defaults to &quot;<code>\&quot;</code>&quot; (quotation mark / double quote). </p>
<dt><code>separator</code></p>
<dd> The string used to separate fields. Defaults to space. </p>
<dt><code>format</code></p>
<dd> How cells should be formatted. Acceptable values: &quot;<code>automatic</code>&quot; (apply automatic formatting; default), &quot;<code>raw</code>&quot; (output data raw, unformatted), or &quot;<code>preserve</code>&quot; (preserve the formatting from the source document). </p>
<p> This deals with the difference between a cell&#8217;s contents and the way those contents are formatted. </p>
<p> Consider a cell in a Gnumeric input document that was input as &quot;4/19/73&quot; in a US locale, with a format set to &quot;d-mmm-yyyy&quot; and thus formatted as &quot;19-Apr-1973&quot;. </p>
<p> With the default <code>format</code> setting of &quot;<code>automatic</code>&quot; it will be output as &quot;1973/04/19&quot;. With &quot;<code>preserve</code>&quot;, the formatting will be preserved and it will be output as &quot;19-Apr-1973&quot;. With &quot;<code>raw</code>&quot; it will be output as &quot;26773&quot; (Gnumeric&#8217;s internal representation: days since an epoch). </p>
<dt><code>transliterate-mode</code></p>
<dd> How to handle unrepresentable characters (characters that cannot be represented in the chosen output character set). Acceptable values: &quot;<code>transliterate</code>&quot;, or &quot;<code>escape</code>&quot;. </p>
<dt><code>quoting-mode</code></p>
<dd> When does data need to be quoted? &quot;<code>never</code>&quot;, &quot;<code>auto</code>&quot; (puts quotes where needed), or &quot;<code>always</code>&quot;. Defaults to &quot;<code>never</code>&quot;. </p>
<dt><code>quoting-on-whitespace</code></p>
<dd> Controls whether initial or terminal whitespace forces quoting. Defaults to <code>TRUE</code>. </p>
</dl>
<h2>EXAMPLE</h2>
<p> To convert the Gnumeric file <i>foo.gnumeric</i> to a Microsoft Excel(TM) format file <i>foo.xls</i>: </p>
<p> <code>ssconvert</code> <i>foo.gnumeric</i> <i>foo.xls</i> </p>
<p> The export format can be specified explicitly, to override the default (which is based on the file extension): </p>
<p> <code>ssconvert</code> <code>&#8211;export-type=</code>Gnumeric_stf:stf_csv <i>foo.xls</i> <i>foo.txt</i> </p>
<p> To convert an Excel format file <i>statfuns.xls</i> to a text file, specifying the semicolon as the separator character: </p>
<p> <code>ssconvert</code> <code>-O &#8216;separator=; format=raw&#8217;</code> <i>samples/excel/statfuns.xls</i> <i>statfuns.txt</i> </p>
<h2>LICENSE</h2>
<p> <code>ssconvert</code> is licensed under the terms of the General Public License (GPL), version 2 or 3. For information on this license look at the source code that came with the software or see the GNU project page &lt;URL: <a rel="nofollow" href="http://www.gnu.org">http://www.gnu.org</a> &gt;. </p>
<h2>COPYRIGHT</h2>
<p> The copyright on the <code>Gnumeric</code> software and source code is held by the individual authors as is documented in the source code. </p>
<h2>AUTHOR</h2>
<p> <code>ssconvert</code>&#8216;s primary author is Jody Goldberg &lt;jody [at] gnome.org&gt;; <code>ssconvert</code> builds on the <code>Gnumeric</code> codebase. </p>
<p> The initial version of this manpage was written by J.H.M. Dassen (Ray) &lt;jdassen [at] debian.org&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnumeric/">gnumeric</a>(1),</code> <code><a href="/docs/linux/man/1-ssdiff/">ssdiff</a>(1),</code> <code><a href="/docs/linux/man/1-ssgrep/">ssgrep</a>(1),</code> <code><a href="/docs/linux/man/1-ssindex/">ssindex</a>(1)</code> </p>
<p> The Gnumeric Homepage &lt;URL: <a rel="nofollow" href="http://www.gnome.org/projects/gnumeric/">http://www.gnome.org/projects/gnumeric/</a> &gt;. </p>
<p> The GNOME project page &lt;URL: <a rel="nofollow" href="http://www.gnome.org/">http://www.gnome.org/</a> &gt;. </p>
<h2>Index</h2>
