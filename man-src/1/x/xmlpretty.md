---
title: "xmlpretty(1)"
name: "xmlpretty"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmlpretty/"
description: "xmlpretty – XML pretty printer"
---

<h2 class="name">NAME</h2>
<p> xmlpretty &#8211; XML pretty printer </p>
<h2>SYNOPSIS</h2>
<pre><code>
xmlpretty[--options][filename]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>xmlpretty</code> is the commandline interface to XML::Handler::YAWriter, acting as a tool to add and remove pretty printing to <font SIZE="-1">XML</font> files. </p>
<p> <code>xmlpretty</code> has several methods to add human readablitiy. </p>
<p> If you want to add readablity without adding so-called <i>ignorable whitespace</i>, use it in the following way : </p>
<pre>
  $ xmlpretty --AddHiddenNewline \
              --AddHiddenAttrTab \
          --CatchEmptyElement \
          uglyfile.xml &gt; prettyfile.xml
</pre>
<p> If you do <code>not</code> want to process the file further, but only want it human readable, add visible whitespace to the file as follows : </p>
<pre>
  $ xmlpretty --PrettyWhiteNewline \
              --PrettyWhiteIndent \
          --CatchEmptyElement \
          uglyfile.xml &gt; prettyfile.xml
</pre>
<p> You may use YAWriter to clean whitespace from <font SIZE="-1">XML</font> documents. This may work in 99% of the cases where you want to get rid of ignorable whitespace caused by the various forms of pretty printing. </p>
<pre><code>
$ xmlpretty-- NoWhiteSpace-- NoComments-- AddHiddenNewline-- AddHiddenAttrTab-- CatchEmptyElement
        prettyfile.xml &gt; cleanfile.xml
</code></pre>
<h3>Options</h3>
<p> Options are given in a gnu like &#8211;option idiom.</p>
<dl>
<dt>AddHiddenNewline boolean</p>
<dd> Add hidden newline before &#8220;&gt;&#8221;</p>
<dt>AddHiddenAttrTab boolean</p>
<dd> Add hidden tabulation for attributes</p>
<dt>CatchEmptyElement boolean</p>
<dd> Catch empty Elements, apply &#8220;/&gt;&#8221; compression</p>
<dt>CatchWhiteSpace boolean</p>
<dd> Catch whitespace with comments</p>
<dt>IsSGML boolean</p>
<dd> This option will cause start_document, processing_instruction and doctype_decl to appear as <font SIZE="-1">SGML.</font> The <font SIZE="-1">SGML</font> is still well-formed of course, if your <font SIZE="-1">SAX</font> events are well-formed.</p>
<dt>NoComments boolean</p>
<dd> Supress Comments</p>
<dt>NoDTD boolean</p>
<dd> Supress <font SIZE="-1">DTD</font></p>
<dt>NoPI boolean</p>
<dd> Supress Processing Instructions</p>
<dt>NoProlog boolean</p>
<dd> Supress &lt;?xml &#8230; ?&gt; Prolog</p>
<dt>NoWhiteSpace boolean</p>
<dd> Supress WhiteSpace to clean documents from prior pretty printing.</p>
<dt>PrettyWhiteIndent boolean</p>
<dd> Add visible indent before any eventstring</p>
<dt>PrettyWhiteNewline boolean</p>
<dd> Add visible newlines before any eventstring</p>
<dt><font SIZE="-1">SAX1</font> boolean (not yet implemented)</p>
<dd> Output only <font SIZE="-1">SAX1</font> compilant eventstrings</dl>
<h3>Bugs:</h3>
<p> Automatic recoding between 8bit and 16bit does not yet work correctly ! </p>
<p> I have Perl-5.6 at home and here I can specify &#8220;use utf8;&#8221; in the right places to make recoding work. But I dislike saying &#8220;use 5.00555;&#8221; because many systems run 5.00503.</p>
<h2>AUTHOR</h2>
<p> Michael Koehne, Kraehe [at] Copyleft.De</p>
<h2>Thanks</h2>
<p> &#8220;Derksen, Eduard (Enno), <font SIZE="-1">CSCIO&#8221;</font> &lt;enno [at] att.com&gt; helped me with the Escape hash and gave quite a lot of usefull comments.</p>
<h2>SEE ALSO</h2>
<p> perl and XML::Parser::PerlSAX </p>
<h2>Index</h2>
