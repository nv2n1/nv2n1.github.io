---
title: "ltx2crossrefxml(1)"
name: "ltx2crossrefxml"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ltx2crossrefxml/"
description: "ltx2crossrefxml.pl – create XML files for submitting to crossref.org"
---

<h2 class="name">NAME</h2>
<p> ltx2crossrefxml.pl &#8211; create XML files for submitting to crossref.org </p>
<h2>SYNOPSIS</h2>
<p> ltx2crossrefxml [<code>-c</code> <i>config_file</i>] [<code>-o</code> <i>output_file</i>] [<code>-input-is-xml</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>latex_file1</i>&nbsp;<i>latex_file2</i>&nbsp;&#8230;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>config_file</i></p>
<dd> Configuration file. If this file is absent, defaults are used. See below for its format.</p>
<dt><code>-o</code> <i>output_file</i></p>
<dd> Output file. If this option is not used, the <font SIZE="-1">XML</font> is output to stdout.</p>
<dt><code>-rpi-is-xml</code></p>
<dd> Do not transform author and title input strings, assume they are valid <font SIZE="-1">XML.</font></dl>
<p> The usual <tt>&quot;--help&quot;</tt> and <tt>&quot;--version&quot;</tt> options are also supported. Options can begin with either <tt>&quot;-&quot;</tt> or <tt>&quot;--&quot;</tt>, and ordered arbitrarily.</p>
<h2>DESCRIPTION</h2>
<p> For each given <i>latex_file</i>, this script reads <tt>&quot;.rpi&quot;</tt> and (if they exist) <tt>&quot;.bbl&quot;</tt> files and outputs corresponding <font SIZE="-1">XML</font> that can be uploaded to Crossref (&lt;<a rel="nofollow" href="https://crossref.org">https://crossref.org</a>&gt;). Any extension of <i>latex_file</i> is ignored, and <i>latex_file</i> itself is not read (and need not even exist). </p>
<p> Each <tt>&quot;.rpi&quot;</tt> file specifies the metadata for a single article to be uploaded to Crossref (a <tt>&quot;journal_article&quot;</tt> element in their schema); an example is below. These files are output by the <tt>&quot;resphilosophica&quot;</tt> package (&lt;<a rel="nofollow" href="https://ctan.org/pkg/resphilosophica">https://ctan.org/pkg/resphilosophica</a>&gt;), but (as always) can also be created by hand or by whatever other method you implement. </p>
<p> Any <tt>&quot;.bbl&quot;</tt> files present are used for the citation information in the output <font SIZE="-1">XML.</font> See the <font SIZE="-1">CITATIONS</font> section below. </p>
<p> Unless <tt>&quot;--rpi-is-xml&quot;</tt> is specified, for all text (authors, title, citations), standard TeX control sequences are replaced with plain text or <font SIZE="-1">UTF-8</font> or eliminated, as appropriate. The <tt>&quot;LaTeX::ToUnicode::convert&quot;</tt> routine is used for this (&lt;<a rel="nofollow" href="https://ctan.org/pkg/bibtexperllibs">https://ctan.org/pkg/bibtexperllibs</a>&gt;). Tricky TeX control sequences will almost surely not be handled correctly. If <tt>&quot;--rpi-is-xml&quot;</tt> is given, the author and title strings from the rpi files are output as-is, assuming they are valid <font SIZE="-1">XML</font>; no checking is done. Citation text from <tt>&quot;.bbl&quot;</tt> files is always converted from LaTeX to plain text. </p>
<p> This script just writes an <font SIZE="-1">XML</font> file. It&#8217;s up to you to actually do the uploading to Crossref; for example, you can use their Java tool <tt>&quot;crossref-upload-tool.jar&quot;</tt> (&lt;<a rel="nofollow" href="https://www.crossref.org/education/member-setup/direct-deposit-xml/https-post">https://www.crossref.org/education/member-setup/direct-deposit-xml/https-post</a>&gt;). For the definition of their schema, see &lt;<a rel="nofollow" href="https://data.crossref.org/reports/help/schema_doc/4.4.2/index.html">https://data.crossref.org/reports/help/schema_doc/4.4.2/index.html</a>&gt; (this is the schema version currently followed by this script).</p>
<h2>CONFIGURATION FILE FORMAT</h2>
<p> The configuration file is read as Perl code. Thus, comment lines starting with <tt>&quot;#&quot;</tt> and blank lines are ignored. The other lines are typically assignments in the form (spaces are optional): </p>
<pre>
    $variable = value ;
</pre>
<p> Usually the value is a <tt>&quot;string&quot;</tt> enclosed in <font SIZE="-1">ASCII</font> double-quote or single-quote characters, per Perl syntax. The idea is to specify the user-specific and journal-specific values needed for the Crossref upload. The variables which are used are these: </p>
<pre><code>
$depositorName = "Depositor Name";
$depositorEmail = 'depositor [at] example.org';
$registrant = 'Registrant';
#organization name
    $fullTitle = "FULL TITLE";
#journal name
    $issn = "1234-5678";
#required $abbrevTitle = "ABBR. TTL.";
#optional $coden = "CODEN";
#optional
</code></pre>
<p> For a given run, all <tt>&quot;.rpi&quot;</tt> data read is assumed to belong to the journal that is specified in the configuration file. More precisely, the configuration data is written as a <tt>&quot;journal_metadata&quot;</tt> element, with given <tt>&quot;full_title&quot;</tt>, <tt>&quot;issn&quot;</tt>, etc., and then each <tt>&quot;.rpi&quot;</tt> is written as <tt>&quot;journal_issue&quot;</tt> plus <tt>&quot;journal_article&quot;</tt> elements. </p>
<p> The configuration file can also define one Perl function: <tt>&quot;LaTeX_ToUnicode_convert_hook&quot;</tt>. If it is defined, it is called at the beginning of the procedure that converts LaTeX text to Unicode, which is done with the LaTeX::ToUnicode module, from the <tt>&quot;bibtexperllibs&quot;</tt> package (&lt;<a rel="nofollow" href="https://ctan.org/pkg/bibtexperllibs">https://ctan.org/pkg/bibtexperllibs</a>&gt;). The function must accept one string (the LaTeX text), and return one string (presumably the transformed string). The standard conversions are then applied to the returned string, so the configured function need only handle special cases, such as control sequences particular to the journal at hand.</p>
<h2>RPI FILE FORMAT</h2>
<p> Here&#8217;s the (relevant part of the) <tt>&quot;.rpi&quot;</tt> file corresponding to the <tt>&quot;rpsample.tex&quot;</tt> example in the <tt>&quot;resphilosophica&quot;</tt> package (&lt;<a rel="nofollow" href="https://ctan.org/pkg/resphilosophica">https://ctan.org/pkg/resphilosophica</a>&gt;): </p>
<pre><code>
% authors = Boris Veytsmannd A.U.Th{\o} rnd C.O.R\"espondent
                                   % title = A Sample Paper :\ mph{A Template} % year = 2012 % volume = 90 % issue = 1 --2 % startpage = 1 % endpage = 1 % doi = 10.11612 / resphil.A31245 % paperUrl = http : // borisv.lk.net/paper12
                                                                                                                                                                                                                  %
                                                                                                                                                                                                                  publicationType = full_text
</code></pre>
<p> Other lines, some not beginning with %, are ignored (and not shown). For more details on processing, see the code. </p>
<p> The <tt>%paperUrl</tt> value is what will be associated with the given <tt>%doi</tt> (output as the <tt>&quot;resource&quot;</tt> element). Crossref strongly recommends that the url be for a so-called landing page, and not directly for a pdf (&lt;<a rel="nofollow" href="https://www.crossref.org/education/member-setup/creating-a-landing-page/">https://www.crossref.org/education/member-setup/creating-a-landing-page/</a>&gt;). Special case: if the url is not specified, and the journal is <i>Res Philosophica</i>, a special-purpose search url using pdcnet.org is returned. Any other journal must always specify this. </p>
<p> The <tt>%authors</tt> field is split at <tt>&quot;nd&quot;</tt> (ignoring whitespace before and after), and output as the <tt>&quot;contributors&quot;</tt> element, using <tt>&quot;sequence=&quot;first&quot;&quot;</tt> for the first listed, <tt>&quot;sequence=&quot;additional&quot;&quot;</tt> for the remainder. </p>
<p> If the <tt>%publicationType</tt> is not specified, it defaults to <tt>&quot;full_text&quot;</tt>, since that has historically been the case; <tt>&quot;full_text&quot;</tt> can also be given explicitly. The other values allowed by the Crossref schema are <tt>&quot;abstract_only&quot;</tt> and <tt>&quot;bibliographic_record&quot;</tt>. Finally, if the value is <tt>&quot;omit&quot;</tt>, the <tt>&quot;publication_type&quot;</tt> attribute is omitted entirely from the given <tt>&quot;journal_article&quot;</tt> element. </p>
<p> Each <tt>&quot;.rpi&quot;</tt> must contain information for only one article, but multiple files can be read in a single run. It would not be difficult to support multiple articles in a single <tt>&quot;.rpi&quot;</tt> file, but it makes debugging and error correction easier when each uploaded <font SIZE="-1">XML</font> contains a single article.</p>
<h3><font SIZE="-1">MORE ABOUT AUTHOR NAMES</font></h3>
<p> The three formats for names recognized are (not coincidentally) the same as BibTeX: </p>
<pre>
   First von Last
   von Last, First
   von Last, Jr., First
</pre>
<p> The forms can be freely intermixed within a single <tt>%authors</tt> line, separated with <tt>&quot;nd&quot;</tt> (including the backslash). Commas as name separators are not supported, unlike BibTeX. </p>
<p> In short, you may almost always use the first form; you shouldn&#8217;t if either there&#8217;s a Jr part, or the Last part has multiple tokens but there&#8217;s no von part. See the <tt>&quot;btxdoc&quot;</tt> (&#8220;BibTeXing&#8221; by Oren Patashnik) document for details. </p>
<p> In the <tt>%authors</tt> line of a <tt>&quot;.rpi&quot;</tt> file, some secondary directives are recognized, indicated by <tt>&quot;|&quot;</tt> characters. Easiest to explain with an example: </p>
<pre>
  %authors=|organization|\LaTeX\ Project Team nd Alex Brown|orcid=123
</pre>
<p> Thus: 1) if <tt>&quot;|organization|&quot;</tt> is specified, the author name will be output as an <tt>&quot;organization&quot;</tt> contributor, instead of the usual <tt>&quot;person_name&quot;</tt>, as the Crossref schema requires. </p>
<p> 2) If <tt>&quot;|orcid=</tt>value<tt>|&quot;</tt> is specified, the <i>value</i> is output as an <tt>&quot;ORCID&quot;</tt> element for that <tt>&quot;person_name&quot;</tt>. </p>
<p> These two directives, <tt>&quot;|organization&quot;</tt>| and <tt>&quot;|orcid|&quot;</tt> are mutually exclusive, because that&#8217;s how the Crossref schema defines them. The <tt>&quot;=&quot;</tt> sign after <tt>&quot;orcid&quot;</tt> is required, while all spaces after the <tt>&quot;orcid&quot;</tt> keyword are ignored. Other than that, the <font SIZE="-1">ORCID</font> value is output literally. (E.g., the <font SIZE="-1">ORCID</font> value of <tt>123</tt> above is clearly invalid, but it would be output anyway, with no warning.) </p>
<p> Extra <tt>&quot;|&quot;</tt> characters, at the beginning or end of the entire <tt>%authors</tt> string, or doubled in the middle, are accepted and ignored. Whitespace is ignored around all <tt>&quot;|&quot;</tt> characters.</p>
<h2>CITATIONS</h2>
<p> Each <tt>&quot;.bbl&quot;</tt> file corresponding to an input <tt>&quot;.rpi&quot;</tt> file is read and used to output a <tt>&quot;citation_list&quot;</tt> element for that <tt>&quot;journal_article&quot;</tt> in the output <font SIZE="-1">XML.</font> If no <tt>&quot;.bbl&quot;</tt> file exists for a given <tt>&quot;.rpi&quot;</tt>, no <tt>&quot;citation_list&quot;</tt> is output for that article. </p>
<p> The <tt>&quot;.bbl&quot;</tt> processing is rudimentary: only so-called <tt>&quot;unstructured_citation&quot;</tt> references are produced for Crossref, that is, the contents of the citation (each paragraph in the <tt>&quot;.bbl&quot;</tt>) is dumped as a single flat string without markup. </p>
<p> Bibliography text is unconditionally converted from TeX to <font SIZE="-1">XML,</font> via the method described above. It is not unusual for the conversion to be incomplete or incorrect. It is up to you to check for this; e.g., if any backslashes remain in the output, it is most likely an error. </p>
<p> Furthermore, it is assumed that the <tt>&quot;.bbl&quot;</tt> file contains a sequence of references, each starting with <tt>&quot;ibitem{</tt>KEY<tt>}&quot;</tt> (which itself must be at the beginning of a line, preceded only by whitespace), and the whole bibliography ending with <tt>&quot;nd{thebibliography}&quot;</tt> (similarly at the beginning of a line). A bibliography not following this format will not produce useful results. Bibliographies can be created by hand, or with BibTeX, or any other method. </p>
<p> The <tt>&quot;key&quot;</tt> attribute for the <tt>&quot;citation&quot;</tt> element is taken as the <i></i><font SIZE="-1"><i>KEY</i></font><i></i> argument to the <tt>&quot;ibitem&quot;</tt> command. The sequential number of the citation (1, 2, &#8230;) is appended. The argument to <tt>&quot;ibitem&quot;</tt> can be empty (<tt>&quot;ibitem{}&quot;</tt>, and the sequence number will be used on its own. Although TeX will not handle empty <tt>&quot;ibitem&quot;</tt> keys, it can be convenient when creating a <tt>&quot;.bbl&quot;</tt> purely for Crossref. </p>
<p> The <tt>&quot;.rpi&quot;</tt> file is also checked for the bibliography information, in this same format. </p>
<p> Feature request: if anyone is interested in figuring out how to generate structured citations (&lt;<a rel="nofollow" href="https://data.crossref.org/reports/help/schema_doc/4.4.2/schema_4_4_2.html#citation">https://data.crossref.org/reports/help/schema_doc/4.4.2/schema_4_4_2.html#citation</a>&gt;) instead of these flat text dumps, that would be great.</p>
<h2>EXAMPLES</h2>
<pre>
  ltx2crossrefxml.pl ../paper1/paper1.tex ../paper2/paper2.tex \
                      -o result.xml
  ltx2crossrefxml.pl -c myconfig.cfg paper.tex -o paper.xml
</pre>
<h2>AUTHOR</h2>
<p> Boris Veytsman &lt;<a rel="nofollow" href="https://github.com/borisveytsman/crossrefware">https://github.com/borisveytsman/crossrefware</a>&gt;</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright (C) 2012-2021 Boris Veytsman </p>
<p> This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License &lt;<a rel="nofollow" href="https://www.gnu.org/licenses/gpl.html">https://www.gnu.org/licenses/gpl.html</a>&gt;. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law. </p>
<h2>Index</h2>
<dt><a href="#lbAI">CITATIONS</a></p>
<dd>
<dt><a href="#lbAJ">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAK">AUTHOR</a></p>
<dd>
<dt><a href="#lbAL">COPYRIGHT AND LICENSE</a></p>
<dd></dl>
