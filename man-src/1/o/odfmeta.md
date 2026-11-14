---
title: "odfmeta(1)"
name: "odfmeta"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odfmeta/"
description: "odfmeta – List or change the metadata of an ODF file"
---

<p>odfmeta &#8211; List or change the metadata of an ODF file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>odfmeta</code> [-l] [-v] [-V] [-c] [-d] [-x&nbsp;<wbr><i>metafield</i>&#8230;] [-X&nbsp;<wbr><i>metafield</i>&#8230;] [-a&nbsp;<wbr><i>metafield</i>&#8230;] [-A&nbsp;<wbr><i>metafield</i>&#8230;] [-I&nbsp;<wbr><i>metafield</i>&#8230;] [-o&nbsp;<wbr><i>path</i>] <i>path</i></dl>
<h2>Description</h2>
<p> <code>odfmeta</code></p>
<dd>is a program that will list or change the metadata in an OpenDocument file. This is useful for version control systems. You can change title, keywords, description etc. </p>
<p> &#8220;Path&#8221; is assumed to be an OpenDocument file of text, spreadsheet or presentation type.</p>
<h2>Options</h2>
<p> -l</p>
<dl>
<dt>
<dd> List (extract) all known metadata fields.</dl>
<p> -v or -V</p>
<dl>
<dt>
<dd> Print the version number of the ODF document <i>format</i>. If you use -V it will print &quot;version:&quot; before the number for compatibility with -X. The version number can&#8217;t be modified.</dl>
<p> -c</p>
<dl>
<dt>
<dd> Make field values continous by normalizing white space. Might be convenient when postprocessing with standard (line oriented) text utilities.</dl>
<p> -d</p>
<dl>
<dt>
<dd> Update the modification date to the current date and time.</dl>
<p> -x <i>metafield</i></p>
<dl>
<dt>
<dd> Extract the contents of this metafield from the file. Known field names are creation-date, creator, date, description, editing-cycles, editing-duration, generator, initial-creator, keyword, language, print-date, printed-by, subject, title, user-defined. All other names are assumed to be user defined.</dl>
<p> -X <i>metafield</i></p>
<dl>
<dt>
<dd> Same as -x, but also preserves/includes the field name.</dl>
<p> -a <i>metafield</i></p>
<dl>
<dt>
<dd> Append a custom metafield to the metadata; but only if a similar field does not exist yet.</dl>
<p> -A <i>metafield</i></p>
<dl>
<dt>
<dd> Append a custom metafield to the metadata in any case.</dl>
<p> -I <i>metafield</i></p>
<dl>
<dt>
<dd> Append a custom metafield to the metadata and remove any existing similar field.</dl>
<p> -o <i>path</i></p>
<dl>
<dt>
<dd> Filename to write modified ODT file to. If no <code>-o</code> option is provided, the ODT file will be written to stdout.</dl>
<h2>Examples</h2>
<dl>
<dt>
<dd> <font SIZE="-1"> </font></p>
<pre>
odfmeta -l odf-file.odt
odfmeta -I &quot;title:The Little Engine That Could&quot; -A subject:I-think-I-can -o newfile.odt source.odt
</pre>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-formail/">formail</a></code>(1), <code><a href="/docs/linux/man/1-id3tag/">id3tag</a></code>(1)</p>
<h2>Bugs</h2>
<p> All known versions of OpenOffice.org keep only four &lt;meta:user-defined&gt; elements. If you add more than those, you&#8217;ll loose them next time you save with OpenOffice.org. KOffice keeps only one &lt;meta:keyword&gt; element.</p>
<h2>Author</h2>
<p> <code>S&oslash;ren Roug</code></p>
<dl>
<dt>
<dd> Original author</dl>
<h2>Index</h2>
