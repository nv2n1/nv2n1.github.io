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
<dt><code>&#8211;recalc</code></dt>
<dd> Recalculate all cells before writing the result.</dd>
<dt><code>&#8211;list-exporters</code></dt>
<dd> List the available exporters (file formats that can be written).</dd>
<dt><code>-T, &#8211;export-type=</code><i>ID</i></dt>
<dd> Specify which exporter to use; see below for a list. This is only necessary when the right format does not follow from the output file name.</dd>
<dt><code>-O, &#8211;export-options=</code><i>optionsstring</i></dt>
<dd> Specify parameters for the chosen exporter. <i>optionsstring</i> is a list of <i>parameter</i>=<i>value</i> pairs, separated by spaces. The parameter names and values allowed are specific to the exporter and are documented below. Multiple parameters can be specified</dd>
<dt><code>&#8211;list-importers</code></dt>
<dd> List the available importers (file formats that can be read). <code>-I, &#8211;import-type=</code><i>ID</i> Specify which importer to use; see below for a list. This is only necessary when the right format does not follow from the input file name.</dd>
<dt><code>-E, &#8211;import-encoding=</code><i>STRING</i></dt>
<dd> Specify an encoding for imported content.</dd>
<dt><code>-M, &#8211;merge-to=</code><i>FILENAME</i></dt>
<dd> Merge a collection of workbooks into one. Sheet size will expand to the largest in all the workbooks. Names in the scope of individual workbooks will end up in the scope of the merged workbook. The merge will be aborted if there are name conflicts.</dd>
<dt><code>-S, &#8211;export-file-per-sheet</code></dt>
<dd> Export a file for each sheet if the exporter only supports one sheet at a time. The output filename is treated as a template in which sheet number is substituted for %n and/or sheet name is substituted for %s. If there are not substitutions, a default of &quot;.%s&quot; is added. </dd>
</dl>
<h3>Help options</h3>
<dl>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display ssconvert&#8217;s version.</dd>
<dt><code>-h, &#8211;help, &#8211;usage</code></dt>
<dd> Display a brief usage message.</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options.</dd>
<dt><code>&#8211;help-libspreadsheet</code></dt>
<dd> Show Gnumeric options. </dd>
</dl>
<h2>LIST OF IMPORTER/EXPORTER IDS</h2>
<p> The following IDs can be can be used both for import (reading) and export (writing).</p>
<dl>
<dt><code>Gnumeric_XmlIO:sax</code></dt>
<dd> Gnumeric&#8217;s XML file format (*.gnumeric)</dd>
<dt><code>Gnumeric_OpenCalc:openoffice</code></dt>
<dd> OpenDocument &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/OpenDocument">http://en.wikipedia.org/wiki/OpenDocument</a> &gt; or OpenOffice Calc &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/OpenOffice.org_Calc">http://en.wikipedia.org/wiki/OpenOffice.org_Calc</a> &gt; (*.sxc, *.ods) format. As an exporter, this is ODF/OpenOffice without foreign elements (*.ods).</dd>
<dt><code>Gnumeric_dif:dif</code></dt>
<dd> Data Interchange Format &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Data_Interchange_Format">http://en.wikipedia.org/wiki/Data_Interchange_Format</a> &gt; (*.dif)</dd>
<dt><code>Gnumeric_paradox:paradox</code></dt>
<dd> Paradox database &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Paradox_%28database%29">http://en.wikipedia.org/wiki/Paradox_%28database%29</a> &gt; or primary index file (*.db, *.px)</dd>
<dt><code>Gnumeric_stf:stf_assistant</code></dt>
<dd> Text (configurable)</dd>
<dt><code>Gnumeric_sylk:sylk</code></dt>
<dd> MultiPlan &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Multiplan">http://en.wikipedia.org/wiki/Multiplan</a> &gt; Symbolic Link (SYLK) &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/SYmbolic_LinK_%28SYLK%29">http://en.wikipedia.org/wiki/SYmbolic_LinK_%28SYLK%29</a> &gt; (*.slk)</dd>
<dt><code>Gnumeric_Excel:xlsx</code></dt>
<dd> Microsoft Excel &#8482; 2007 (&quot;Office Open XML&quot;, OOXML &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/XLSX">http://en.wikipedia.org/wiki/XLSX</a> &gt; ) format </dd>
</dl>
<h2>LIST OF IMPORTANT IMPORTER IDS</h2>
<dl>
<dt><code>Gnumeric_stf:stf_csvtab</code></dt>
<dd> Comma or tab separated values (CSV/TSV) (*.csv)</dd>
<dt><code>Gnumeric_html:html</code></dt>
<dd> HTML (*.html, *.htm)</dd>
<dt><code>Gnumeric_Excel:excel</code></dt>
<dd> Microsoft Excel &#8482; (*.xls)</dd>
<dt><code>Gnumeric_Excel:excel_xml</code></dt>
<dd> Microsoft Excel &#8482; 2003 SpreadsheetML </dd>
</dl>
<h2>LIST OF OTHER IMPORTER IDS</h2>
<dl>
<dt><code>Gnumeric_QPro:qpro</code></dt>
<dd> Quattro Pro &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Quattro_Pro">http://en.wikipedia.org/wiki/Quattro_Pro</a> &gt; (*.wb1, *.wb2, *.wb3)</dd>
<dt><code>Gnumeric_applix:applix</code></dt>
<dd> Applix (*.as)</dd>
<dt><code>Gnumeric_lotus:lotus</code></dt>
<dd> Lotus 1-2-3 &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Lotus_1-2-3">http://en.wikipedia.org/wiki/Lotus_1-2-3</a> &gt; (*.wk1, *.wks, *.123)</dd>
<dt><code>Gnumeric_mps:mps</code></dt>
<dd> MPS (Mathematical Programming System) format &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/MPS_%28format%29">http://en.wikipedia.org/wiki/MPS_%28format%29</a> &gt; Linear programming and mixed integer programming file format (*.mps)</dd>
<dt><code>Gnumeric_oleo:oleo</code></dt>
<dd> GNU Oleo &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/GNU_Oleo">http://en.wikipedia.org/wiki/GNU_Oleo</a> &gt; (*.oleo)</dd>
<dt><code>Gnumeric_plan_perfect:pln</code></dt>
<dd> PlanPerfect Format (PLN)</dd>
<dt><code>Gnumeric_psiconv:psiconv</code></dt>
<dd> Psion (*.psisheet)</dd>
<dt><code>Gnumeric_sc:sc</code></dt>
<dd> SC/xspread</dd>
<dt><code>Gnumeric_xbase:xbase</code></dt>
<dd> xBase &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/XBase">http://en.wikipedia.org/wiki/XBase</a> &gt; (*.dbf) file format </dd>
</dl>
<h2>LIST OF IMPORTANT EXPORTER IDS</h2>
<dl>
<dt><code>Gnumeric_OpenCalc:odf</code></dt>
<dd> ODF/OpenOffice with foreign elements (*.ods)</dd>
<dt><code>Gnumeric_glpk:glpk</code></dt>
<dd> GLPK Linear Program Solver</dd>
<dt><code>Gnumeric_html:html40</code></dt>
<dd> HTML 4.0 (*.html)</dd>
<dt><code>Gnumeric_html:html40frag</code></dt>
<dd> HTML (*.html) fragment</dd>
<dt><code>Gnumeric_html:xhtml</code></dt>
<dd> XHTML (*.html)</dd>
<dt><code>Gnumeric_html:xhtml_range</code></dt>
<dd> XHTML range &#8211; for export to clipboard</dd>
<dt><code>Gnumeric_pdf:pdf_assistant</code></dt>
<dd> Portable Document Format (*.PDF)</dd>
<dt><code>Gnumeric_stf:stf_csv</code></dt>
<dd> Comma separated values (CSV)</dd>
<dt><code>Gnumeric_Excel:excel_dsf</code></dt>
<dd> Microsoft Excel &#8482; 97/2000/XP &amp; 5.0/95 </dd>
</dl>
<h2>LIST OF OTHER EXPORTER IDS</h2>
<dl>
<dt><code>Gnumeric_Excel:excel_biff7</code></dt>
<dd> Microsoft Excel &#8482; 5.0/95</dd>
<dt><code>Gnumeric_Excel:excel_biff8</code></dt>
<dd> Microsoft S Excel &#8482; 97/2000/XP</dd>
<dt><code>Gnumeric_GnomeGlossary:po</code></dt>
<dd> Gnome Glossary PO file format</dd>
<dt><code>Gnumeric_html:html32</code></dt>
<dd> HTML 3.2 (*.html)</dd>
<dt><code>Gnumeric_html:latex</code></dt>
<dd> LaTeX 2e (*.tex)</dd>
<dt><code>Gnumeric_html:latex_table</code></dt>
<dd> LaTeX 2e (*.tex) table fragment</dd>
<dt><code>Gnumeric_html:roff</code></dt>
<dd> TROFF &lt;URL: <a rel="nofollow" href="http://en.wikipedia.org/wiki/Troff">http://en.wikipedia.org/wiki/Troff</a> &gt; (*.me) format.</dd>
<dt><code>Gnumeric_lpsolve:lpsolve</code></dt>
<dd> LPSolve &lt;URL: <a rel="nofollow" href="http://sourceforge.net/projects/lpsolve/">http://sourceforge.net/projects/lpsolve/</a> &gt; Mixed Integer Linear Programming (MILP) solver </dd>
</dl>
<h2>OPTIONS FOR THE PORTABLE DOCUMENT FORMAT (*.pdf) EXPORTER</h2>
<dl>
<dt><code>sheet</code></dt>
<dd> Name of the workbook sheet to operate on. You can specify several sheets by repeating this option. If this option is not given the active sheet (i. e. the sheet that was active when the file was saved) is used. This is ignored if the <code>object</code> option is given. </dd>
<dt><code>object</code></dt>
<dd> Name of the sheet object to print. If this option is given any <code>sheet</code> option is ignored. Only the first <code>object</code> given is exported. </dd>
<dt><code>paper</code></dt>
<dd> Paper size. Valid values include &quot;<code>A4</code>&quot; for ISO A4 and &quot;<code>na_letter_8.5x11in</code>&quot; for US Letter. If an individual graph is specified through the <code>object</code> option, then a paper size of &quot;<code>fit</code>&quot; reduces the size of the paper to the size of the graph. </dd>
</dl>
<h2>OPTIONS FOR THE CONFIGURABLE TEXT (*.txt) EXPORTER</h2>
<dl>
<dt><code>sheet</code></dt>
<dd> Name of the workbook sheet to operate on. You can specify several sheets by repeating this option. If this option is not given the active sheet (i. e. the sheet that was active when the file was saved) is used. </dd>
<dt><code>eol</code></dt>
<dd> End Of Line convention; how lines are terminated. &quot;<code>unix</code>&quot; for linefeed, &quot;<code>mac</code>&quot; for carriage return; &quot;<code>windows</code>&quot; for carriage return plus linefeed. </dd>
<dt><code>charset</code></dt>
<dd> The character encoding of the output. Defaults to UTF-8. </dd>
<dt><code>locale</code></dt>
<dd> The locale to use for number and date formatting. Defaults to the current locale as reported by <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1). Consult <code>locale -a</code> output for acceptable values. </dd>
<dt><code>quote</code></dt>
<dd> The character or string used for quoting fields. Defaults to &quot;<code>\&quot;</code>&quot; (quotation mark / double quote). </dd>
<dt><code>separator</code></dt>
<dd> The string used to separate fields. Defaults to space. </dd>
<dt><code>format</code></dt>
<dd> How cells should be formatted. Acceptable values: &quot;<code>automatic</code>&quot; (apply automatic formatting; default), &quot;<code>raw</code>&quot; (output data raw, unformatted), or &quot;<code>preserve</code>&quot; (preserve the formatting from the source document). </dd>
<p> This deals with the difference between a cell&#8217;s contents and the way those contents are formatted. </p>
<p> Consider a cell in a Gnumeric input document that was input as &quot;4/19/73&quot; in a US locale, with a format set to &quot;d-mmm-yyyy&quot; and thus formatted as &quot;19-Apr-1973&quot;. </p>
<p> With the default <code>format</code> setting of &quot;<code>automatic</code>&quot; it will be output as &quot;1973/04/19&quot;. With &quot;<code>preserve</code>&quot;, the formatting will be preserved and it will be output as &quot;19-Apr-1973&quot;. With &quot;<code>raw</code>&quot; it will be output as &quot;26773&quot; (Gnumeric&#8217;s internal representation: days since an epoch). </p>
<dt><code>transliterate-mode</code></dt>
<dd> How to handle unrepresentable characters (characters that cannot be represented in the chosen output character set). Acceptable values: &quot;<code>transliterate</code>&quot;, or &quot;<code>escape</code>&quot;. </dd>
<dt><code>quoting-mode</code></dt>
<dd> When does data need to be quoted? &quot;<code>never</code>&quot;, &quot;<code>auto</code>&quot; (puts quotes where needed), or &quot;<code>always</code>&quot;. Defaults to &quot;<code>never</code>&quot;. </dd>
<dt><code>quoting-on-whitespace</code></dt>
<dd> Controls whether initial or terminal whitespace forces quoting. Defaults to <code>TRUE</code>. </dd>
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
