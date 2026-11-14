---
title: "jw(1)"
name: "jw"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jw/"
description: "jw, docbook2dvi, docbook2html, docbook2man, docbook2pdf, docbook2ps, docbook2rtf, docbook2tex, docbook2texi, docbook2txt – (Jade Wrapper) converts SGML files to other formats"
---

<h2 class="name">NAME</h2>
<p> jw, docbook2dvi, docbook2html, docbook2man, docbook2pdf, docbook2ps, docbook2rtf, docbook2tex, docbook2texi, docbook2txt &#8211; (Jade Wrapper) converts SGML files to other formats </p>
<h2>SYNOPSIS</h2>
<p> <code>jw</code> [ <code>-f </code><i>frontend</i> | <code>&#8211;frontend </code><i>frontend</i> ]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-b </code><i>backend</i> | <code>&#8211;backend </code><i>backend</i> ]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-c&nbsp;<wbr></code><i>file</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;cat&nbsp;<wbr></code><i>file</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-n</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;nostd</code>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-d </code><i>file</i><code>|default|none</code> | <code>&#8211;dsl </code><i>file</i><code>|default|none</code> ]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-l&nbsp;<wbr></code><i>file</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;dcl&nbsp;<wbr></code><i>file</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-s&nbsp;<wbr></code><i>path</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;sgmlbase&nbsp;<wbr></code><i>path</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-p&nbsp;<wbr></code><i>program</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;parser&nbsp;<wbr></code><i>program</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-o&nbsp;<wbr></code><i>directory</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;output&nbsp;<wbr></code><i>directory</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-V </code><i>variable</i><code>[=</code><i>value</i><code>]</code> ]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-u</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;nochunks</code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>-i&nbsp;<wbr></code><i>section</i>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;include&nbsp;<wbr></code><i>section</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-w&nbsp;<wbr></code><i>type</i><code>|list</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;warning&nbsp;<wbr></code><i>type</i><code>|list</code>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-e&nbsp;<wbr></code><i>type</i><code>|list</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;error&nbsp;<wbr></code><i>type</i><code>|list</code>&nbsp;<wbr>]<br />
&nbsp;<wbr>[&nbsp;<wbr><code>-h</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;help</code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>-v</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;version</code>&nbsp;<wbr>]<br />
&nbsp;<wbr><i>SGML-file</i> </p>
<p> <code>docbook2dvi</code> <i>SGML-file</i> </p>
<p> <code>docbook2html</code> <i>SGML-file</i> </p>
<p> <code>docbook2man</code> <i>SGML-file</i> </p>
<p> <code>docbook2pdf</code> <i>SGML-file</i> </p>
<p> <code>docbook2ps</code> <i>SGML-file</i> </p>
<p> <code>docbook2rtf</code> <i>SGML-file</i> </p>
<p> <code>docbook2tex</code> <i>SGML-file</i> </p>
<p> <code>docbook2texi</code> <i>SGML-file</i> </p>
<p> <code>docbook2txt</code> <i>SGML-file</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>jw</code> shell script allows to convert a DocBook file (or some other SGML-based format) to other formats (including HTML, RTF, PS and PDF) with an easy-to-understand syntax. It hides most of Jade&#8217;s or OpenJade complexity and adds comfortable features. </p>
<p> Other scripts like <code>docbook2html</code>, <code>docbook2rtf</code> or <code>docbook2ps</code> provide different ways of calling <code>jw</code> that might be easier to remember. </p>
<p> For the moment, jw does not handle XML, but only SGML. </p>
<p> This utility assumes that several other components are installed. The list includes:</p>
<dl>
<dt>&bull;</p>
<dd> the ISO character entities for SGML</p>
<dt>&bull;</p>
<dd> James Clark&#8217;s DSSSL engine, jade, or an equivalent parser like OpenJade</p>
<dt>&bull;</p>
<dd> the DocBook DTD from the OASIS consortium</p>
<dt>&bull;</p>
<dd> Norman Walsh&#8217;s DocBook modular style sheets (or some other set of DSSSL style sheets)</p>
<dt>&bull;</p>
<dd> Sebastian Rahtz&#8217;s jadetex set of TeX macros for jade (for backends intended to &quot;printing&quot; formats like PDF, RTF or PostScript)</p>
<dt>&bull;</p>
<dd> A perl interpreter (for backends that use perl)</p>
<dt>&bull;</p>
<dd> SGMLSpm from CPAN (for backends that use sgmls)</p>
<dt>&bull;</p>
<dd> Lynx HTML browser (for the <i>txt</i> backend)</dl>
<p> The jw script is basically called like this: </p>
<pre>
jw mydoc.sgml
</pre>
<p> where <i>mydoc.sgml</i> is a SGML file. </p>
<p> The command line above uses default options: it converts from DocBook (the default frontend) to HTML (the default backend), does not put the result in a subdirectory (unless specified otherwise in the style sheets), etc. </p>
<p> In this example, the &quot;mydoc&quot; file name as well as the &quot;.sgml&quot; extension can be replaced by anything else. Current extensions for SGML DocBook files include &quot;.sgml&quot;, &quot;.sgm&quot;, &quot;.docbook&quot;, and &quot;.db&quot;. The processed file <i>mydoc.sgml</i> can be in any other directory than the current one. </p>
<p> Here we have chosen to generate HTML output. In fact we can use any of the backends stored in the <i>backends/</i> subdirectory of the DocBook-utils distribution directory (usually <i>/usr/share/sgml/docbook/utils-0.6.14</i>). Similarly, you can use any frontend defined in the <i>frontends/</i> subdirectory to convert from another input format. </p>
<p> This sample command creates one or many HTML files with arbitrary file names in the current directory. This default behavior can be changed through command line options and/or customization style sheets.</p>
<h2>OPTIONS</h2>
<p> The following options apply to the conversion script:</p>
<dl>
<dt><code> -f </code><i>frontend</i><code> | &#8211;frontend </code><i>frontend</i></p>
<dd> Allows to specify another frontend than default <i>docbook</i>. The list of currently available frontends is:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>docbook</i></p>
<dd> Converts docbook with Norman Walsh&#8217;s style sheets. This frontend searches in the subdirectories of the base SGML directory for a file named <i>html/docbook.dsl</i> or <i>print/docbook.dsl</i> (depending on the backend&#8217;s type: html or print).</dl>
</dl>
<dt><code> -b </code><i>backend</i><code> | &#8211;backend </code><i>backend</i></p>
<dd> Allows to specify another backend than default <i>HTML</i>. The list of currently available backends is:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>dvi</i></p>
<dd> Converts to DVI (DeVice Independant files) by calling <code>Jade</code> or <code>OpenJade</code>.</p>
<dt><i>html</i></p>
<dd> Converts to HTML (HyperText Markup Language) by calling <code>Jade</code> or <code>OpenJade</code>.</p>
<dt><i>man</i></p>
<dd> Converts a refentry to a Unix manual page by calling docbook2man. Does not work with other SGML document types than DocBook.</p>
<dt><i>pdf</i></p>
<dd> Converts to PDF (Portable Document Format) by calling <code>Jade</code> or <code>OpenJade</code>.</p>
<dt><i>ps</i></p>
<dd> Converts to PostScript by calling <code>Jade</code> or <code>OpenJade</code>.</p>
<dt><i>rtf</i></p>
<dd> Converts to RTF (Rich Text Format) by calling <code>Jade</code> or <code>OpenJade</code>. The resulting file can then be inported into <code>MS Word</code> or one of its Linux replacement programs. </p>
<p> <code>Note</code> &#8211; The original picture must be present when RTF document is viewed, because the RTF documents created by <code>OpenJade</code> includes pictures by reference.</p>
<dt><i>tex</i></p>
<dd> Converts to TeX by calling <code>Jade</code> or <code>OpenJade</code>.</p>
<dt><i>texi</i></p>
<dd> Converts to GNU TeXinfo pages by calling docbook2texi. Does not work with other SGML document types than DocBook.</p>
<dt><i>txt</i></p>
<dd> Converts to a bare text file by calling <code>Jade</code> or <code>OpenJade</code>, then <code>Lynx</code>.</dl>
</dl>
<dt><code> -c </code><i>file</i><code> | &#8211;cat </code><i>file</i></p>
<dd> Allows to use an extra SGML Open Catalog that will list other files like customization style sheets, adaptations to the DocBook Document Type Definition, special character entities, etc. This catalog is added to the list of catalogs determined by the script (see option <code>&#8211;nostd</code> below)</p>
<dt><code> -n | &#8211;nostd </code></p>
<dd> Do not use the standard SGML Open Catalogs. Normally, the standard catalogs list is determined like this:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> if the centralized catalog exists, then use it. The centralized catalog is a list of all catalogs that might be necessary that usually resides in <i>/etc/sgml</i>. Its name is provided by the frontend, for example the <i>docbook</i> frontend returns <i>/etc/sgml/sgml-docbook.cat</i>.</p>
<dt>&bull;</p>
<dd> Otherwise, take all the files named <i>catalog</i> from the subdirectories of the SGML base directory (usually <i>/usr/share/sgml</i>).</dl>
</dl>
<p> This option is useful in conjunction with the <code>&#8211;cat</code> option to use only the catalogs that are specified on the command line.</p>
<dt><code> -d </code><i>file</i><code>|default|none | &#8211;dsl </code><i>file</i><code>|default|none </code></p>
<dd> Allows to use a customized style sheet instead of the default one. </p>
<p> A &quot;target&quot; starting with a hash mark &quot;#&quot; can be appended to the file name. As a result, only the corresponding part of the style sheet is executed (the &quot;style specification&quot; whose &quot;identificator&quot; is equal to the target&#8217;s name). A common use of this mechanism is to define &quot;#html&quot; and &quot;#print&quot; targets to trigger the corresponding part of a replacement style sheet which is common for both HTML and printout conversion. </p>
<p> By replacing the file name with &quot;default&quot;, the default style sheet provided with the frontend is used. For example, the <i>docbook</i> frontend returns <i>./docbook.dsl#html</i> (or <i>./docbook.dsl#print</i>) in the SGML base directory. </p>
<p> By replacing the file name with &quot;none&quot;, no replacement style sheet is used, not even the default style sheet. The style sheet which is used is also determined by the frontend. For example, the <i>docbook</i> frontend returns Norman Walsh&#8217;s <i>html/docbook.dsl</i> (or <i>print/docbook.dsl</i>) found somewhere below the SGML base directory. </p>
<p> If no &#8211;dsl option is specified, then &quot;&#8211;dsl default&quot; is used.</p>
<dt><code> -l </code><i>file</i><code> | &#8211;dcl </code><i>file</i></p>
<dd> Allows to use a customized SGML declaration instead of the default one. The file name of the default SGML declaration is not set for SGML files, and is set to <i>xml.dcl</i> in the SGML base directory for XML files.</p>
<dt><code> -s </code><i>path</i><code> | &#8211;sgmlbase </code><i>path</i></p>
<dd> Allows to use another location for the SGML base directory. This is the directory below which all SGML DTDs, style sheets, entities, etc are installed. The default value is <i>/usr/share/sgml</i>.</p>
<dt><code> -p </code><i>program</i><code> | &#8211;parser </code><i>program</i></p>
<dd> Specify the parser to use (<code>Jade</code> or <code>OpenJade</code>) if several are installed. If this option is not specified, the script first tries to use Jade, then it tries <code>OpenJade</code>.</p>
<dt><code> -o </code><i>directory</i><code> | &#8211;output </code><i>directory</i></p>
<dd> Set output directory where all the resulting files will be stored. If the style sheets define a subdirectory where to store the resulting files too, the subdirectory defined by the style sheets will be placed below the subdirectory defined by this option.</p>
<dt><code> -V </code><i>variable</i><code>=[</code><i>value</i><code>] </code></p>
<dd> Set a variable (to a value, if one is specified).</p>
<dt><code> -u | &#8211;nochunks </code></p>
<dd> Output only one big file. This option is useful only when generating HTML, because the output can be split into several files. This option overrides the setting that may be done in the style sheets.</p>
<dt><code> -i </code><i>section</i><code> | &#8211;include </code><i>section</i></p>
<dd> Declare a SGML marked section as &quot;include&quot;. A SGML marked section is a kind of conditional part of a document. If it is declared &quot;ignore&quot;, it will be left ignored, otherwise it will be processed. An example of such a marked section would be:</dl>
<pre><code>
            &lt;DOCTYPE mydoc [
              &lt;!ENTITY % confidential "ignore"&gt;
            ]&gt;
            &lt;mydoc&gt;
              ...
              &lt;![ %confidential [ Some confidential text... ]]&gt;
              ...
            &lt;/mydoc&gt;
            
</code></pre>
<dl>
<dt><code> -w </code><i>type</i><code>|list | &#8211;warning </code><i>type</i><code>|list </code></p>
<dd> Enables or disables the display of given types of warnings. Several -w options might be entered on the command line. Warning types that start with &quot;no-&quot; disable the corresponding warnings, the other types enable them. </p>
<p> If the warning type is replaced with &quot;list&quot;, then a list of allowed warning types is displayed.</p>
<dt><code> -e </code><i>type</i><code>|list | &#8211;error </code><i>type</i><code>|list </code></p>
<dd> Disables given types of errors. Several -e options might be entered on the command line. All error types start with &quot;no-&quot;. </p>
<p> If the error type is replaced with &quot;list&quot;, then a list of allowed error types is displayed.</p>
<dt><code> -h | &#8211;help </code></p>
<dd> Print a short help message and exit</p>
<dt><code> -v | &#8211;version </code></p>
<dd> Print the version identifier and exit</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/sgml/sgml-docbook.cat</i></p>
<dd> Centralized SGML open catalog. This file name might vary if another frontend than <i>docbook</i> is used.</p>
<dt><i>/usr/share/sgml/docbook/utils-0.6.14/backends</i></p>
<dd> The various backends</p>
<dt><i>/usr/share/sgml/docbook/utils-0.6.14/frontends</i></p>
<dd> The various frontends</p>
<dt><i>/usr/share/sgml/docbook/utils-0.6.14/helpers</i></p>
<dd> The various helper scripts like docbook2man or docbook2texi</dl>
<h2>AUTHORS</h2>
<p> Eric Bischoff (jw shell script and a few backends), Jochem Huhmann (the <i>man</i> and <i>texi</i> backends)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docbook2man-spec-pl/">docbook2man-spec.pl</a></code>(1), <code><a href="/docs/linux/man/1-docbook2texi-spec-pl/">docbook2texi-spec.pl</a></code>(1), <code><a href="/docs/linux/man/8-install-catalog/">install-catalog</a></code>(8), <code><a href="/docs/linux/man/1-nsgmls/">nsgmls</a></code>(1), docbook-utils homepage &lt;URL:<a rel="nofollow" href="http://sources.redhat.com/docbook-tools/">http://sources.redhat.com/docbook-tools/</a>&gt;. </p>
<h2>Index</h2>
