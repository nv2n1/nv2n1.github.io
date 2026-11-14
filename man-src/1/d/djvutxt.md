---
title: "djvutxt(1)"
name: "djvutxt"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djvutxt/"
description: "djvutxt – Extract the hidden text from DjVu documents."
---

<h2 class="name">NAME</h2>
<p> djvutxt &#8211; Extract the hidden text from DjVu documents.</p>
<h2>SYNOPSIS</h2>
<p> <code>djvutxt [</code><i>options</i><code>] </code><i>inputdjvufile</i><code> [</code><i>outputtxtfile</i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> Program <code>djvutxt</code> decodes the hidden text layer of a DjVu document <i>inputdjvufile</i> and prints it into file <i>outputtxtfile</i> or on the standard output. The hidden text layer is usually generated with the help of an optical character recognition software. </p>
<p> Without options <code>-detail</code> and <code>-escape</code>, this program simply outputs the UTF-8 text. Option <code>-detail</code> cause the output of S-expressions describing the text and its location. Option <code>-escape</code> uses C-style escape sequences to represent nonprintable non-ASCII characters. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;page=</code><i>pagespec</i></p>
<dd> Specify which pages should be processed. When this option is not specified, the text of all pages of the documents is concatenated into the output file. The page specification <i>pagespec </i> contains one or more comma-separated page ranges. A page range is either a page number, or two page numbers separated by a dash. For instance, specification <code>1-10</code> outputs pages 1 to 10, and specification <code>1,3,99999-4</code> outputs pages 1 and 3, followed by all the document pages in reverse order up to page 4.</p>
<dt><code>&#8211;detail=</code><i>keyword</i></p>
<dd> This options causes <code>djvutxt</code> to output S-expressions specifying the position of the text in the page. See the manual page <code><a href="/docs/linux/man/1-djvused/">djvused</a></code>(1) for a description of the output format. Argument <i>keyword</i> specifies the maximum level of detail for which text location is reported. The recognized values are: <code>page</code>, <code>column</code>, <code>region</code>, <code>para</code>, <code>line</code>, <code>word</code>, and <code>char</code>. All other values are interpreted as <code>char</code>.</p>
<dt><code>&#8211;escape</code></p>
<dd> Output escape sequences of the form <code>&nbsp;<wbr>ooo</code> for all non ASCII or non printable UTF-8 characters and for the backslash character. </p>
</dl>
<h2>REMARKS</h2>
<p> Use program <code><a href="/docs/linux/man/1-djvused/">djvused</a></code>(1) for more control over the text layer. </p>
<h2>CREDITS</h2>
<p> This program was initially written by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt; and was then improved Bill Riemers &lt;docbill [at] sourceforge.net&gt; and many others. It was then rewritten to use the ddjvuapi by Leon Bottou &lt;leonb [at] sourceforge.net&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-djvused/">djvused</a></code>(1) </p>
<h2>Index</h2>
