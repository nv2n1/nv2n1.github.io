---
title: "html2markdown(1)"
name: "html2markdown"
section: "1"
letter: "h"
url: "/docs/linux/man/1-html2markdown/"
description: "html2markdown – converts a page of HTML into markdown."
---

<h2 class="name">NAME</h2>
<p> html2markdown &#8211; converts a page of HTML into markdown. </p>
<h2>SYNOPSIS</h2>
<p> <code>html2markdown</code> [options&#8230;] [(<i>filename</i>|<i>url</i>) [<i>encoding</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>html2markdown</code> downloads the specified HTML page, and converts it to text marked up with markdown. The source HTML page may be a local file or remote URL. If not specified, it will be read from standard input. The output is printed to standard output. </p>
<p> If an <i>encoding</i> is specified, it will override any encoding information provided by the HTTP Server. When not specified, <code>python-feedparser</code> (if available) will be used to determine the source encoding. If not available, or when reading local files, the encoding is assumed to be UTF-8.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;no-wrap-links</code></p>
<dd> Don&#8217;t wrap long links.</p>
<dt><code>&#8211;ignore-emphasis</code></p>
<dd> Don&#8217;t include any formatting for emphasis.</p>
<dt><code>&#8211;reference-links</code></p>
<dd> Use reference style links instead of in-line links.</p>
<dt><code>&#8211;ignore-links</code></p>
<dd> Don&#8217;t include any formatting for links.</p>
<dt><code>&#8211;protect-links</code></p>
<dd> Protect links from line breaks surrounding them with angle brackets.</p>
<dt><code>&#8211;ignore-images</code></p>
<dd> Don&#8217;t include any formatting for images.</p>
<dt><code>&#8211;images-to-alt</code></p>
<dd> Discard image data, only keep alt text.</p>
<dt><code>&#8211;images-with-size</code></p>
<dd> Write image tags with height and width attrs as raw html to retain dimensions.</p>
<dt><code>-g</code>, <code>&#8211;google-doc</code></p>
<dd> Convert an html-exported Google Document.</p>
<dt><code>-d</code>, <code>&#8211;dash-unordered-list</code></p>
<dd> Use a dash rather than a star for unordered list items.</p>
<dt><code>-e</code>, <code>&#8211;asterisk-emphasis</code></p>
<dd> Use an asterisk rather than an underscore for emphasized text.</p>
<dt><code>-b</code> <i>BODY_WIDTH</i>, <code>&#8211;body-width</code>=<i>BODY_WIDTH</i></p>
<dd> Number of characters per output line, <code>0</code> for no wrap.</p>
<dt><code>-i</code> <i>LIST_INDENT</i>, <code>&#8211;google-list-indent</code>=<i>LIST_INDENT</i></p>
<dd> Number of pixels Google indents nested lists.</p>
<dt><code>-s</code>, <code>&#8211;hide-strikethrough</code></p>
<dd> Hide strike-through text. Only relevant when <code>-g</code> is specified as well.</p>
<dt><code>&#8211;escape-all</code></p>
<dd> Escape all special characters. Output is less readable, but avoids corner case formatting issues.</p>
<dt><code>&#8211;bypass-tables</code></p>
<dd> Format tables in HTML rather than Markdown syntax.</p>
<dt><code>&#8211;ignore-tables</code></p>
<dd> Ignore table-related tags (table, th, td, tr) while keeping rows.</p>
<dt><code>&#8211;single-line-break</code></p>
<dd> Use a single line break after a block element rather than two line breaks. <code>NOTE:</code> Requires <code>&#8211;body-width</code>=<code>0</code>.</p>
<dt><code>&#8211;unicode-snob</code></p>
<dd> Use unicode throughout document.</p>
<dt><code>&#8211;no-automatic-links</code></p>
<dd> Do not use automatic links wherever applicable.</p>
<dt><code>&#8211;no-skip-internal-links</code></p>
<dd> Do not skip internal links.</p>
<dt><code>&#8211;links-after-para</code></p>
<dd> Put links after each paragraph instead of document.</p>
<dt><code>&#8211;mark-code</code></p>
<dd> Mark program code blocks with <code>[code]</code><i>&#8230;</i><code>[/code]</code>.</p>
<dt><code>&#8211;default-image-alt</code>=<i>TEXT</i></p>
<dd> The default alt string for images with missing ones.</p>
<dt><code>&#8211;pad-tables</code></p>
<dd> Pad the cells to equal column width in tables.</p>
<dt><code>&#8211;decode-errors</code>=<i>DECODE_ERRORS</i></p>
<dd> What to do in case of decode errors. <code>ignore</code>, <code>strict</code>, and <code>replace</code> are acceptable values.</p>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show a help message and exit. </p>
</dl>
<h2>AUTHOR</h2>
<p> This manpage was written for Debian, by Stefano Rivera &lt;stefanor [at] debian.org&gt;. </p>
<h2>Index</h2>
