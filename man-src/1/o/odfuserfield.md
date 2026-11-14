---
title: "odfuserfield(1)"
name: "odfuserfield"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odfuserfield/"
description: "odfuserfield – List or change the user-field declarations in an ODF file"
---

<p>odfuserfield &#8211; List or change the user-field declarations in an ODF file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>odfuserfield</code> [-l] [-L] [-x&nbsp;<wbr><i>field</i>&#8230;] [-X&nbsp;<wbr><i>field</i>&#8230;] [-s&nbsp;<wbr><i>field:value</i>&#8230;] [-o&nbsp;<wbr><i>path</i>] <i>path</i></dl>
<h2>Description</h2>
<p> <code>Odfuserfield</code></p>
<dd>is a program that will list or change the user variable declarations in an OpenDocument file. There are two kinds of variables in OpenDocument. Simple variables can take different values at different positions, throughout a document. User variables have the same value throughout a document. Due to the latter&#8217;s global nature it is safe to change them with an external application. </p>
<p> Use <code>odfuserfield</code> to fill out form letters before printing or giving to the user. </p>
<p> &#8220;Path&#8221; is assumed to be an OpenDocument file of text, spreadsheet or presentation type.</p>
<h2>Options</h2>
<p> -l</p>
<dl>
<dt>
<dd> List (extract) all known user-fields.</dl>
<p> -L</p>
<dl>
<dt>
<dd> List (extract) all known user-fields with type and value.</dl>
<p> -x <i>field</i></p>
<dl>
<dt>
<dd> Extract the contents of this field from the file.</dl>
<p> -X <i>field</i></p>
<dl>
<dt>
<dd> Same as -x, but also preserves/includes the field name and type.</dl>
<p> -s <i>field:value</i></p>
<dl>
<dt>
<dd> Set the value of an existing user field. The field type will be the same.</dl>
<p> -o <i>path</i></p>
<dl>
<dt>
<dd> Filename to write modified ODT file to. If no <code>-o</code> option is provided, the ODT file will be written to stdout.</dl>
<h2>Example</h2>
<dl>
<dt>
<dd> <font SIZE="-1"> </font></p>
<pre>
odfuserfield -L odf-file
</pre>
<p> <font SIZE="+1"></dl>
<p> </font></p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-formail/">formail</a></code>(1), <code><a href="/docs/linux/man/1-id3tag/">id3tag</a></code>(1)</p>
<h2>Todo</h2>
<p> Implement formulas. See OpenDocument v1.0 specification section 6.3.5. This requires a different syntax for -s arguments.</p>
<h2>Authors</h2>
<p> <code>S&oslash;ren Roug</code></p>
<dl>
<dt>
<dd> Original author</dl>
<p> <code>Michael Howitz</code><br />
 gocept gmbh &amp; co. kg</p>
<dl>
<dt>
<dd> Refactoring</dl>
<h2>Index</h2>
