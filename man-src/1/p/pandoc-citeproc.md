---
title: "pandoc-citeproc(1)"
name: "pandoc-citeproc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pandoc-citeproc/"
---

<h2>NAME</h2>

 

 pandoc-citeproc - filter to resolve citations in a pandoc document.

<h2>SYNOPSIS</h2>

 

 pandoc-citeproc [options] [file..]

<h2>DESCRIPTION</h2>

 

 The pandoc-citeproc executable has two modes, filter mode and convert mode.

<h3>Filter mode</h3>

 

 Run without options, it acts as a filter that takes a JSON-encoded Pandoc document, formats citations and adds a bibliography, and returns a JSON-encoded pandoc document. 

 To process citations with pandoc, call pandoc-citeproc as a filter:
<dl>
<dt>
<dd> <pre>
pandoc --filter pandoc-citeproc input.md -s -o output.html
</pre></dl>
 

 The bibliography will be put into a pandoc Div container with class references. 

 pandoc-citeproc will look for the following metadata fields in the input: 

 bibliography: A path, or YAML list of paths, of bibliography files to use. These may be in any of the formats supported by bibutils.
<dl>
<dt>
<dd> <pre><code>
Format &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
File extension-- -- -- -- -- --&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
-- -- -- -- -- -- --MODS &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.mods
    BibLaTeX &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.bib
    BibTeX &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.bibtex
    RIS &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.ris
    EndNote &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.enl
    EndNote XML &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.xml
    ISI &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.wos
    MEDLINE &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.medline
    Copac &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.copac
    JSON citeproc &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
.json
</code></pre></dl>
 

 references: A YAML list of references. Each reference is a YAML object. The format is essentially CSL JSON format. Here is an example:
<dl>
<dt>
<dd> 
- id:doe2006
         &amp;nbsp;
&amp;nbsp;
author : &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
family : Doe
             &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
given : &amp;nbsp;
[ John, F.] &amp; nbsp;
&amp;nbsp;
title : Article
            &amp;nbsp;
&amp;nbsp;
page : 33 - 34 &amp; nbsp;
&amp;nbsp;
issued : &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
year : 2006 &amp; nbsp;
&amp;nbsp;
type : article - journal
                     &amp;nbsp;
&amp;nbsp;
volume : 6 &amp; nbsp;
&amp;nbsp;
container - title : Journal of Generic Studies
</dl>
 

 The contents of fields will be interpreted as markdown when appropriate: so, for example, emphasis and strong emphasis can be used in title fileds. Simple tex math will also be parsed and rendered appropriately. 

 csl or citation-style: Path to a CSL style file. If the file is not found relative to the working directory, pandoc-citeproc will look in the $HOME/.csl directory (or C:\Users\USERNAME\AppData\Roaming\csl in Windows 7). 

 citation-abbreviations: Path to a CSL abbreviations JSON file. The format is described here (<a rel="nofollow" HREF="http://citationstylist.org/2011/10/19/abbreviations-for-zotero-test-release">http://citationstylist.org/2011/10/19/abbreviations-for-zotero-test-release</a>). Here is a short example:
<dl>
<dt>
<dd> <pre><code>
{
    &amp;nbsp;
    "default" : &amp;nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        "container-title" : &amp;nbsp;
        {
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            "Lloyd's Law Reports" : &amp;nbsp;
            "Lloyd's Rep",
                &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            "Estates Gazette" : &amp;nbsp;
            "EG",
                &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            "Scots Law Times" : &amp;nbsp;
            "SLT" &amp; nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
        }
        &amp;nbsp;
        &amp;nbsp;
    }
}
</code></pre></dl>
 

 The metadata must contain either references or bibliography or both as a source of references. csl and citation-abbreviations are optional. If csl is not provided, chicago-author-date.csl will be used by default.

<h3>Convert mode</h3>

 

 If the option --bib2yaml or --bib2json is used, pandoc-citeproc will not process citations; instead, it will treat its input (from stdin or files) as a bibliography and convert it either to a pandoc YAML metadata section, suitable for inclusion in a pandoc document (--bib2yaml), or as a CSL JSON bibliography, suitable for import to zotero (--bib2json). 

 The --format option can be used to specify the bibliography format, though when files are used, pandoc-citeproc can generally guess this from the extension. 

 This mode supersedes the old biblio2yaml program.

<h2>OPTIONS</h2>

<dl>
<dt>-h, --help
<dd> Print usage information.
<dl>
<dt>
<dd></dl>

<dt>-V, --version
<dd> Print version.
<dl>
<dt>
<dd></dl>

<dt>-y, --bib2yaml
<dd> Convert bibliography to YAML suitable for inclusion in pandoc metadata.
<dl>
<dt>
<dd></dl>

<dt>-j, --bib2json
<dd> Convert bibliography to CSL JSON suitable for import into Zotero.
<dl>
<dt>
<dd></dl>

<dt>-f FORMAT, --format=FORMAT
<dd> Specify format of bibliography to be converted. Legal values are biblatex, bibtex, ris, endnote, endnotexml, isi, medline, copac, and json.
<dl>
<dt>
<dd></dl>
</dl>

<h2>AUTHORS</h2>

 

 Andrea Rossato and John MacFarlane.

<h2>SEE ALSO</h2>

 

 pandoc (1). 

 The pandoc-citeproc source code and all documentation may be downloaded from &lt;<a rel="nofollow" HREF="http://github.com/jgm/pandoc-citeproc/">http://github.com/jgm/pandoc-citeproc/</a>&gt;. 

<h2>Index</h2>


