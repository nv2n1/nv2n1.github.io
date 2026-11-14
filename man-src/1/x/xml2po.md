---
title: "xml2po(1)"
name: "xml2po"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2po/"
description: "xml2po – program to create a PO-template file from a DocBook XML file and merge it back into a (translated) XML file"
---

<h2 class="name">NAME</h2>
<p> xml2po &#8211; program to create a PO-template file from a DocBook XML file and merge it back into a (translated) XML file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xml2po</code> [<code>OPTIONS</code>] [<i>XMLFILE</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>xml2po</code> command. </p>
<p> <code>xml2po</code> is a simple Python program which extracts translatable content from free-form XML documents and outputs gettext compatible POT files. Translated PO files can be turned into XML output again. </p>
<p> It can work it&#8217;s magic with most &quot;simple&quot; tags, and for complicated tags one has to provide a list of all tags which are &quot;final&quot; (that will be put into one &quot;message&quot; in PO file), &quot;ignored&quot; (skipped over) and &quot;space preserving&quot;.</p>
<h2>OPTIONS</h2>
<p> The program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<p> <code>-a</code>, <code>&#8211;automatic-tags</code></p>
<dl>
<dt>
<dd> Automatically decide if tags are to be considered &quot;final&quot; or not.</dl>
<p> <code>-k</code>, <code>&#8211;keep-entities</code></p>
<dl>
<dt>
<dd> Don&#8217;t expand entities (default). See also the <code>-e</code> option.</dl>
<p> <code>-e</code>, <code>&#8211;expand-all-entities</code></p>
<dl>
<dt>
<dd> Expand all entities (including SYSTEM ones).</dl>
<p> <code>-m</code>, <code>&#8211;mode=</code><i>TYPE</i></p>
<dl>
<dt>
<dd> Treat tags as type <i>TYPE</i> (default: docbook).</dl>
<p> <code>-o</code>, <code>&#8211;output=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Print resulting text (XML while merging translations with &quot;-p&quot; or &quot;-t&quot; options, POT template file while extracting strings, and translated PO file with &quot;-r&quot; option) to the given FILE.</dl>
<p> <code>-p</code>, <code>&#8211;po-file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Specify a PO FILE containing translation and output XML document with translations merged in.</dl>
<p> <code>-r</code>, <code>&#8211;reuse=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Specify a translated XML document in FILE with the same structure to generate translated PO file for XML document given on command line.</dl>
<p> <code>-t</code>, <code>&#8211;translation=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Specify a MO file containing translation and output XML document with translations merged in.</dl>
<p> <code>-u</code>, <code>&#8211;update-translation=</code><i>LANG.po</i></p>
<dl>
<dt>
<dd> Update a PO file using <code>msgmerge</code>.</dl>
<p> <code>-l</code>, <code>&#8211;language=</code><i>LANG</i></p>
<dl>
<dt>
<dd> Explicitly set language of the translation.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show summary of options.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version of program.</dl>
<h2>EXAMPLES</h2>
<h3>Creating POT template files</h3>
<p> To create a POT template book.pot from an input file book.xml, which consists of chapter1.xml and chapter2.xml (external entities), run: </p>
<dl>
<dt>
<dd>
<pre>
                                <code>/usr/bin/xml2po</code> <code>-o</code> book.pot book.xml chapter1.xml chapter2.xml
                        
</pre>
</dl>
<p> To expand entities use the <code>-e</code> option: </p>
<dl>
<dt>
<dd>
<pre>
                                <code>/usr/bin/xml2po</code> <code>-e -o</code> book.pot book.xml
                        
</pre>
</dl>
<h3>Creating translated XML files (merging back PO files)</h3>
<p> After translating book.pot into LANG.po, merge the translations back by using <code>-p</code> option for each XML file: </p>
<dl>
<dt>
<dd>
<pre>
                                <code>/usr/bin/xml2po</code> <code>-p</code> LANG.po <code>-o</code> book.LANG.xml book.xml
                                <code>/usr/bin/xml2po</code> <code>-p</code> LANG.po <code>-o</code> chapter1.LANG.xml chapter1.xml
                                <code>/usr/bin/xml2po</code> <code>-p</code> LANG.po <code>-o</code> chapter2.LANG.xml chapter2.xml
                        
</pre>
</dl>
<p> If you used the <code>-e</code> option to expand entities, you should use it again to merge back the translation into an XML file: </p>
<dl>
<dt>
<dd>
<pre>
                                <code>/usr/bin/xml2po</code> <code>-e -p</code> LANG.po <code>-o</code> book.LANG.xml book.xml
                        
</pre>
</dl>
<h3>Updating PO files</h3>
<p> When base XML file changes, the real advantages of PO files come to surface. There are 2 ways to merge the translation. The first is to produce a new POT template file (additionally use the <code>-e</code> if you decided earlier to expand entities). Afterwards run <code>msgmerge</code> to merge the translation with the new POT file: </p>
<dl>
<dt>
<dd>
<pre>
                                <code>/usr/bin/msgmerge</code> <code>-o</code> tmp.po LANG.po book.pot
                        
</pre>
</dl>
<p> Now rename tmp.po to LANG.po and update your translation. Alternatively, <code>xml2po</code> provides the <code>-u</code> option, which does exactly these two steps for you. The advantage is, that it also runs <code>msgfmt</code> to give you a statistical output of translation status (count of translated, untranslated and fuzzy messages). Additionally use the <code>-e</code> if you decided earlier to expand entities: </p>
<dl>
<dt>
<dd>
<pre>
                                <code>/usr/bin/xml2po</code> <code>-u</code> LANG.po book.xml
                        
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code>msgmerge</code> (1), <code>msgfmt</code> (1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Daniel Leidert daniel.leidert [at] wgdd.de for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Daniel Leidert </p>
<h2>Index</h2>
