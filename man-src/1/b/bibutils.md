---
title: "bibutils(1)"
name: "bibutils"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bibutils/"
description: "bibutils – bibliography conversion utilities"
---

<h2 class="name">NAME</h2>
<p> bibutils &#8211; bibliography conversion utilities </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <i>format</i><code>2xml</code> [<i>OPTIONS</i>] [<i>file.format</i>]</p>
<dt> <code>xml2</code><i>format</i> [<i>OPTIONS</i>] [<i>file.xml</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>The bibutils program set inter-converts between various bibliography formats using m[blue]<code>Library of Congress</code>m[]<font SIZE="-2">[1]</font>&#8216;s m[blue]<code>Metadata Object Description Schema (MODS)</code>m[]<font SIZE="-2">[2]</font>version 3.1. For example, one can convert RIS-format files to Bibtex by doing two transformations: RIS-&gt;MODS-&gt;Bibtex.</p>
<h2>CONVERTING TO MODS</h2>
<h3>Overview</h3>
<table>
<tr VALIGN=top>
<td><i>Command</i></td>
<td><i>Description</i>
</td>
</tr>
<tr VALIGN=top>
<td> bib2xml </td>
<td> convert bibtex to MODS
</td>
</tr>
<tr VALIGN=top>
<td> biblatex2xml </td>
<td> convert biblatex to MODS
</td>
</tr>
<tr VALIGN=top>
<td> copac2xml </td>
<td> convert m[blue]<code>COPAC</code>m[]<font SIZE="-2">[3]</font>format references to MODS
</td>
</tr>
<tr VALIGN=top>
<td> ebi2xml </td>
<td> convert EBI XML to MODS
</td>
</tr>
<tr VALIGN=top>
<td> end2xml </td>
<td> convert EndNote (Refer format) to MODS
</td>
</tr>
<tr VALIGN=top>
<td> endx2xml </td>
<td> convert EndNote XML to MODS
</td>
</tr>
<tr VALIGN=top>
<td> isi2xml </td>
<td> convert ISI web of science to MODS
</td>
</tr>
<tr VALIGN=top>
<td> med2xml </td>
<td> convert Pubmed XML references to MODS
</td>
</tr>
<tr VALIGN=top>
<td> modsclean </td>
<td> a MODS to MODS converter
</td>
</tr>
<tr VALIGN=top>
<td> ris2xml </td>
<td> convert RIS format to MODS
</td>
</tr>
<tr VALIGN=top>
<td> wordbib2xml </td>
<td> convert Word2007 bibliography XML to MODS
</td>
</tr>
</table>
<h3>Common Options Converting to MODS</h3>
<p> Several flags available for the end2xml, endx2xml, bib2xml, ris2xml, med2xml, and copac2xml programs. Most options have both a short and a long version. </p>
<table>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> -h </td>
<td> &#8211;help </td>
<td> display help
</td>
</tr>
<tr VALIGN=top>
<td> -v </td>
<td> &#8211;version </td>
<td> display version
</td>
</tr>
<tr VALIGN=top>
<td> -a </td>
<td> &#8211;add-refcount </td>
<td> add &quot;_#&quot;, where # is reference count to reference id
</td>
</tr>
<tr VALIGN=top>
<td> -s </td>
<td> &#8211;single-refperfile </td>
<td> put one reference per file name by the reference number
</td>
</tr>
<tr VALIGN=top>
<td> -i </td>
<td> &#8211;input-encoding </td>
<td> interpret the input file as using the requested character set (use w/o argument for current list derived from character sets at m[blue]<code><a rel="nofollow" href="http://www.kostis.net">www.kostis.net</a></code>m[]<font SIZE="-2">[4]</font>) unicode is now a character set option
</td>
</tr>
<tr VALIGN=top>
<td> -u </td>
<td> &#8211;unicode-characters </td>
<td> encode unicode characters directly in the file rather than as XML entities
</td>
</tr>
<tr VALIGN=top>
<td> -un </td>
<td> &#8211;unicode-no-bom </td>
<td> as -u, but don&#8217;t include a byte order mark
</td>
</tr>
<tr VALIGN=top>
<td> -x </td>
<td> &#8211;xml-entities </td>
<td> encode unicode characters as XML entities (opposite of -u)
</td>
</tr>
<tr VALIGN=top>
<td> -nl </td>
<td> &#8211;no-latex </td>
<td> do not convert latex-style character combinations
</td>
</tr>
<tr VALIGN=top>
<td> -s </td>
<td> &#8211;single-refperfile </td>
<td> one reference per output file
</td>
</tr>
<tr VALIGN=top>
<td> -d </td>
<td> &#8211;drop-key </td>
<td> don&#8217;t put citation key in the mods id field
</td>
</tr>
<tr VALIGN=top>
<td> -c </td>
<td> &#8211;corporation-file </td>
<td> with argument specifying a file containing a list of corporation names to be placed in &lt;name type=&quot;corporate&quot;&gt;&lt;/name&gt; instead of type=&quot;personal&quot; and eliminate name mangling
</td>
</tr>
<tr VALIGN=top>
<td> -a </td>
<td> &#8211;asis </td>
<td> with argument specifying a file containing a list of names to be treated verbatim
</td>
</tr>
<tr VALIGN=top>
<td> -nt </td>
<td> &#8211;nosplit-title </td>
<td> don&#8217;t split titles into TITLE/SUBTITLE pairs
</td>
</tr>
<tr VALIGN=top>
<td>
</td>
<td> &#8211;verbose </td>
<td> verbose output
</td>
</tr>
<tr VALIGN=top>
<td>
</td>
<td> &#8211;debug </td>
<td> very verbose output (mostly for debugging)
</td>
</tr>
</table>
<h3>bib2xml</h3>
<p> <code>bib2xml</code> converts a bibtex-formatted reference file to an XML-intermediate bibliography file. Specify file(s) to be converted on the command line. Files containing bibtex substitutions strings should be specified before the files where substitutions are specified (or in the same file before their use). If no files are specified, then bibtex information will be read from standard input. </p>
<dl>
<dt>
<dd>
<pre>
bib2xml bibtex_file.bib &gt; output_file.xml
</pre>
</dl>
<h3>biblatex2xml</h3>
<p> <code>biblatex2xml</code> converts a biblatex (not to be confused with bibtex) formatted reference file to an MODS XML-intermediate bibliography file. </p>
<dl>
<dt>
<dd>
<pre>
biblatex2xml biblatex_file.bib &gt; outputfile.xml
</pre>
</dl>
<h3>copac2xml</h3>
<p> <code>copac2xml</code>converts a COPAC formatted reference file to a MODS XML-intermediate bibliography file.</p>
<h3>end2xml</h3>
<p> <code>end2xml</code> converts a text endnote-formatted reference file to an XML-intermediate bibliography file. This program will not work on the binary library; the file needs to be exported first. Endnote tagged formats (&quot;Refer&quot; format export) look like Example 1, &#8220;Example refer format file&#8221;. There are very nice instructions for making sure that you are properly exporting this at m[blue]<code><a rel="nofollow" href="http://www.sonnysoftware.com/endnoteimport.html">http://www.sonnysoftware.com/endnoteimport.html</a></code>m[]<font SIZE="-2">[5]</font> </p>
<p> Usage for <code>end2xml</code> is the same as <code>bib2xml</code>. </p>
<dl>
<dt>
<dd>
<pre>
end2xml endnote_file.end &gt; output_file.xml
</pre>
</dl>
<h3>ebi2xml</h3>
<p> <code>ebi2xml</code> converts a EBI XML file to a MODS XML-intermediate bibliography file.</p>
<h3>endx2xml</h3>
<p> <code>endx2xml</code> converts a EndNote-XML exported reference file to a MODS XML-intermediate bibliography file. This program will not work on the binary library; the file needs to be exported first.</p>
<h3>isi2xml</h3>
<p> <code>isi2xml</code> converts an ISI-web-of-science-formatted reference file to an XML-intermediate bibliography file. </p>
<p> Usage for <code>isi2xml</code> is the same as <code>bib2xml</code>. </p>
<dl>
<dt>
<dd>
<pre>
isi2xml input_file.isi &gt; output_file.xml
</pre>
</dl>
<h3>ris2xml</h3>
<p> <code>ris2xml</code> converts a RIS-formatted reference file to an XML-intermediate bibliography file. <code>ris2xml</code> usage is as <code>end2xml</code> and <code>bib2xml</code> </p>
<dl>
<dt>
<dd>
<pre>
ris2xml ris_file.ris &gt;  output_file.xml
</pre>
</dl>
<h3>wordbib2xml</h3>
<p> <code>wordbib2xml</code> convert a Word2007-formatted reference file to an XML-intermediate bibliogrpahy file.</p>
<h2>CONVERTING FROM MODS</h2>
<h3>Overview</h3>
<table>
<tr VALIGN=top>
<td><i>Command</i></td>
<td><i>Description</i>
</td>
</tr>
<tr VALIGN=top>
<td> xml2ads </td>
<td> convert MODS into the SAO/NASA ADS format
</td>
</tr>
<tr VALIGN=top>
<td> xml2bib </td>
<td> convert MODS into bibtex
</td>
</tr>
<tr VALIGN=top>
<td> xml2end </td>
<td> convert MODS into format for EndNote
</td>
</tr>
<tr VALIGN=top>
<td> xml2isi </td>
<td> convert MODS to ISI format
</td>
</tr>
<tr VALIGN=top>
<td> xml2ris </td>
<td> convert MODS into RIS format
</td>
</tr>
<tr VALIGN=top>
<td> xml2wordbib </td>
<td> convert MODS into Word 2007 bibliography format
</td>
</tr>
</table>
<h3>Common Options Converting from MODS</h3>
<p> Note that <i>&#8211;output-encoding</i> refers to the input file </p>
<table>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> -h </td>
<td> &#8211;help </td>
<td> display help
</td>
</tr>
<tr VALIGN=top>
<td> -v </td>
<td> &#8211;version </td>
<td> display version
</td>
</tr>
<tr VALIGN=top>
<td> -o </td>
<td> &#8211;output-encoding </td>
<td> interpret the input file as using the requested character set (use w/o argument for current list derived from character sets at m[blue]<code><a rel="nofollow" href="http://www.kostis.net">www.kostis.net</a></code>m[]<font SIZE="-2">[4]</font>) unicode is now a character set option
</td>
</tr>
<tr VALIGN=top>
<td> -s </td>
<td> &#8211;single-refperfile </td>
<td> put one reference per file name by the reference number
</td>
</tr>
<tr VALIGN=top>
<td> -nb </td>
<td> &#8211;no-bom </td>
<td> do not write Byte Order Mark if writing UTF8
</td>
</tr>
</table>
<h3>xml2bib</h3>
<p> <code>xml2bib</code> converts the MODS XML bibliography into a bibtex-formatted reference file. <code>xml2bib</code> usage is as for other tools </p>
<dl>
<dt>
<dd>
<pre>
xml2bib xml_file.xml &gt; output_file.bib
</pre>
</dl>
<p> Since the BibTeX reference format is fairly flexible and seems to have the greatest number of personal preferences, it has also accumulated a number of specific options that are not available for other formats. </p>
<p> Starting with 3.24, xml2bib output uses lowercase tags and mixed case reference types for better interaction with other software. The older behavior with all uppercase tags/reference types can still be generated using the command-line switch -U/&#8211;uppercase. </p>
<p> <font SIZE="+1"> <code>xml2bib-specific Options:</code></p>
<dl>
<dt>
<dd> </font></p>
<table>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> -fc </td>
<td> &#8211;finalcomma </td>
<td> add final comma in the bibtex output for those that want it
</td>
</tr>
<tr VALIGN=top>
<td> -sd </td>
<td> &#8211;singledash </td>
<td> use one dash instead of two (longer dash in latex) between numbers in page output
</td>
</tr>
<tr VALIGN=top>
<td> -b </td>
<td> &#8211;brackets </td>
<td> use brackets instead of quotation marks around field data
</td>
</tr>
<tr VALIGN=top>
<td> -w </td>
<td> &#8211;whitespace </td>
<td> add beautifying whitespace to output
</td>
</tr>
<tr VALIGN=top>
<td> -U </td>
<td> &#8211;uppercase </td>
<td> use all uppercase for tags (field names) and reference types (pre-3.24 behavior)
</td>
</tr>
<tr VALIGN=top>
<td> -sk </td>
<td> &#8211;strictkey </td>
<td> only use alphanumeric characters for bibtex citation keys
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
</dl>
<p> </font></p>
<h3>xml2ads</h3>
<p> <code>xml2ads</code> converts the MODS XML bibliography to the Smithsonian Astrophysical Observatory (SAO)/National Aeronautics and Space Administration (NASA) Astrophyics Data System or m[blue]<code>ADS reference format</code>m[]<font SIZE="-2">[6]</font> (which is very similar to the tagged Endnote style). <code>xml2ads</code> usage is as for other tools </p>
<dl>
<dt>
<dd>
<pre>
xml2ads xml_file.xml &gt; output_file.ads
</pre>
</dl>
<h3>xml2ris</h3>
<p> <code>xml2ris</code> converts the MODS XML bibliography to RIS-formatted bibliography file. <code>xml2ris</code> usage is as for other tools </p>
<dl>
<dt>
<dd>
<pre>
xml2ris xml_file.xml &gt; output_file.ris
</pre>
</dl>
<h3>xml2end</h3>
<p> <code>xml2end</code> converts the MODS XML bibliography to tagged Endnote (refer-format) bibliography file. <code>xml2end</code> usage is as for other tools </p>
<dl>
<dt>
<dd>
<pre>
xml2end xml_file.xml &gt;  output_file.end
</pre>
</dl>
<h3>xml2wordbib</h3>
<p> <code>xml2wordbib</code> converts the MODS XML bibliography to Word 2007-formatted XML bibliography file. <code>xml2wordbib</code> usage is as for other tools </p>
<dl>
<dt>
<dd>
<pre>
xml2wordbib xml_file.xml &gt;  output_file.word.xml
</pre>
</dl>
<p> <code>xml2wordbib</code> was called xml2word in versions of bibutils prior to 3.40. It was renamed to avoid confusion with other tools. Hopefully this will not break too many scripts already in use.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Example refer format file</code> </p>
<dl>
<dt>
<dd>
<pre>
%0 Journal Article 
%A C. D. Putnam
%A C. S. Pikaard 
%D 1992 
%T Cooperative binding of the Xenopus RNA polymerase I 
   transcription factor xUBF to repetitive ribosomal gene enhancers 
%J Mol Cell Biol 
%V 12 
%P 4970-4980 
%F Putnam1992
        
</pre>
</dl>
<h3>xml2bib Output Variations</h3>
<p> <code>Example 2. Default</code> </p>
<dl>
<dt>
<dd>
<pre>
              @Article{Putnam1992, 
              author=&quot;C. D. Putnam
              and C. S. Pikaard&quot;,
              year=&quot;1992&quot;,
              month=&quot;Nov&quot;,
              title=&quot;Cooperative binding of the 
              Xenopus RNA polymerase I transcription 
              factor xUBF to repetitive ribosomal 
              gene enhancers&quot;,
              journal=&quot;Mol Cell Biol&quot;,
              volume=&quot;12&quot;,
              pages=&quot;4970--4980&quot;,
              number=&quot;11&quot;}
            
</pre>
</dl>
<p> <code>Example 3. Final Comma</code> </p>
<dl>
<dt>
<dd>
<pre>
              @Article{Putnam1992,
              author=&quot;C. D. Putnam
              and C. S. Pikaard&quot;,
              year=&quot;1992&quot;,
              month=&quot;Nov&quot;,
              title=&quot;Cooperative binding of the 
              Xenopus RNA polymerase I transcription 
              factor xUBF to repetitive ribosomal 
              gene enhancers&quot;,
              journal=&quot;Mol Cell Biol&quot;,
              volume=&quot;12&quot;,
              pages=&quot;4970--4980&quot;,
              number=&quot;11&quot;,}
            
</pre>
</dl>
<p> <code>Example 4. Single Dash</code> </p>
<dl>
<dt>
<dd>
<pre>
              @Article{Putnam1992,
              author=&quot;C. D. Putnam
              and C. S. Pikaard&quot;,
              year=&quot;1992&quot;,
              month=&quot;Nov&quot;,
              title=&quot;Cooperative binding of the 
              Xenopus RNA polymerase I transcription 
              factor xUBF to repetitive ribosomal 
              gene enhancers&quot;,
              journal=&quot;Mol Cell Biol&quot;,
              volume=&quot;12&quot;,
              pages=&quot;4970-4980&quot;,
              number=&quot;11&quot;}
            
</pre>
</dl>
<p> <code>Example 5. Whitespace</code> </p>
<dl>
<dt>
<dd>
<pre>
@Article{Putnam1992,
  author =      &quot;C. D. Putnam
                and C. S. Pikaard&quot;,
  year =        &quot;1992&quot;,
  month =       &quot;Jan&quot;,
  title =       &quot;Cooperative binding of 
the Xenopus RNA polymerase I transcription 
factor xUBF to repetitive ribosomal gene 
enhancers&quot;,
  journal =     &quot;Mol Cell Biol&quot;,
  volume =      &quot;12&quot;,
  pages =       &quot;4970--4980&quot;
}
</pre>
</dl>
<p> <code>Example 6. Brackets</code> </p>
<dl>
<dt>
<dd>
<pre><code>
@Article
{
    Putnam1992,
        author = {Putnam, C.D.and Pikaard, C.S.},
        title = {Cooperative binding of the Xenopus
                     RNA polymerase I transcription factor xUBF
                         to repetitive ribosomal gene enhancers},
        journal = {Mol Cell Biol},
        year = {1992},
        month = {Nov},
        volume = {12},
        number = {11},
        pages = { 4970 --4980 }
}
</code></pre>
</dl>
<p> <code>Example 7. Uppercase</code> </p>
<dl>
<dt>
<dd>
<pre>
              @ARTICLE{Putnam1992,
              AUTHOR=&quot;Putnam, C. D.
              and Pikaard, C. S.&quot;,
              TITLE=&quot;Cooperative binding of the Xenopus
              RNA polymerase I transcription factor xUBF
              to repetitive ribosomal gene enhancers&quot;,
              JOURNAL=&quot;Mol Cell Biol&quot;,
              YEAR=&quot;1992&quot;,
              MONTH=&quot;Nov&quot;,
              VOLUME=&quot;12&quot;,
              NUMBER=&quot;11&quot;,
              PAGES=&quot;4970--4980&quot;
              }
            
</pre>
</dl>
<h2>LICENSE</h2>
<p> All versions of bibutils are relased under the GNU Public License (GPL). In a nutshell, feel free to download, run, and modify these programs as required. If you re-release these, you need to release the modified version of the source. (And I&#8217;d appreciate patches as well&#8230;if you care enough to make the change, then I&#8217;d like to see what you&#8217;re adding or fixing.) </p>
<p> m[blue]<code>Chris Putnam, Ludwig Institute for Cancer Research</code>m[]<font SIZE="-2">[7]</font></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2010 David Bremner (Manual)<br />
 Copyright &#169; 2008 Christopher Putnam (Software and Manual) </p>
<p> This manual page is distributed under the terms of version 2 of the GNU General Public License. </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Library of Congress</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.loc.gov">http://www.loc.gov</a></dl>
<dt> 2.</p>
<dd> Metadata Object Description Schema (MODS)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.loc.gov/standards/mods/">http://www.loc.gov/standards/mods/</a></dl>
<dt> 3.</p>
<dd> COPAC</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://copac.ac.uk/">http://copac.ac.uk/</a></dl>
<dt> 4.</p>
<dd> <a rel="nofollow" href="http://www.kostis.net">www.kostis.net</a></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.kostis.net/">http://www.kostis.net/</a></dl>
<dt> 5.</p>
<dd> <a rel="nofollow" href="http://www.sonnysoftware.com/endnoteimport.html">http://www.sonnysoftware.com/endnoteimport.html</a></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.sonnysoftware.com/endnoteimport.html">http://www.sonnysoftware.com/endnoteimport.html</a></dl>
<dt> 6.</p>
<dd> ADS reference format</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://doc.adsabs.harvard.edu/abs_doc/help_pages/taggedformat.html">http://doc.adsabs.harvard.edu/abs_doc/help_pages/taggedformat.html</a></dl>
<dt> 7.</p>
<dd> Chris Putnam, Ludwig Institute for Cancer Research</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.sourceforge.net/p/bibutils/home/Bibutils">http://www.sourceforge.net/p/bibutils/home/Bibutils</a></dl>
</dl>
<h2>Index</h2>
