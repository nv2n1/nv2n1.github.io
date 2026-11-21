---

title: "html2markdown(1)"
name: "html2markdown"
section: "1"
letter: "h"
url: "/docs/linux/man/1-html2markdown/"
description: "html2markdown – converts a page of HTML into markdown."
---

<p> html2markdown &#8211; converts a page of HTML into markdown. </p>
<h2>SYNOPSIS</h2>
<p> <code>html2markdown</code> [options&#8230;] [(<i>filename</i>|<i>url</i>) [<i>encoding</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>html2markdown</code> downloads the specified HTML page, and converts it to text marked up with markdown. The source HTML page may be a local file or remote URL. If not specified, it will be read from standard input. The output is printed to standard output. </p>
<p> If an <i>encoding</i> is specified, it will override any encoding information provided by the HTTP Server. When not specified, <code>python-feedparser</code> (if available) will be used to determine the source encoding. If not available, or when reading local files, the encoding is assumed to be UTF-8.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;no-wrap-links</code></dt>
<dd> Don&#8217;t wrap long links.</dd>
<dt><code>&#8211;ignore-emphasis</code></dt>
<dd> Don&#8217;t include any formatting for emphasis.</dd>
<dt><code>&#8211;reference-links</code></dt>
<dd> Use reference style links instead of in-line links.</dd>
<dt><code>&#8211;ignore-links</code></dt>
<dd> Don&#8217;t include any formatting for links.</dd>
<dt><code>&#8211;protect-links</code></dt>
<dd> Protect links from line breaks surrounding them with angle brackets.</dd>
<dt><code>&#8211;ignore-images</code></dt>
<dd> Don&#8217;t include any formatting for images.</dd>
<dt><code>&#8211;images-to-alt</code></dt>
<dd> Discard image data, only keep alt text.</dd>
<dt><code>&#8211;images-with-size</code></dt>
<dd> Write image tags with height and width attrs as raw html to retain dimensions.</dd>
<dt><code>-g</code>, <code>&#8211;google-doc</code></dt>
<dd> Convert an html-exported Google Document.</dd>
<dt><code>-d</code>, <code>&#8211;dash-unordered-list</code></dt>
<dd> Use a dash rather than a star for unordered list items.</dd>
<dt><code>-e</code>, <code>&#8211;asterisk-emphasis</code></dt>
<dd> Use an asterisk rather than an underscore for emphasized text.</dd>
<dt><code>-b</code> <i>BODY_WIDTH</i>, <code>&#8211;body-width</code>=<i>BODY_WIDTH</i></dt>
<dd> Number of characters per output line, <code>0</code> for no wrap.</dd>
<dt><code>-i</code> <i>LIST_INDENT</i>, <code>&#8211;google-list-indent</code>=<i>LIST_INDENT</i></dt>
<dd> Number of pixels Google indents nested lists.</dd>
<dt><code>-s</code>, <code>&#8211;hide-strikethrough</code></dt>
<dd> Hide strike-through text. Only relevant when <code>-g</code> is specified as well.</dd>
<dt><code>&#8211;escape-all</code></dt>
<dd> Escape all special characters. Output is less readable, but avoids corner case formatting issues.</dd>
<dt><code>&#8211;bypass-tables</code></dt>
<dd> Format tables in HTML rather than Markdown syntax.</dd>
<dt><code>&#8211;ignore-tables</code></dt>
<dd> Ignore table-related tags (table, th, td, tr) while keeping rows.</dd>
<dt><code>&#8211;single-line-break</code></dt>
<dd> Use a single line break after a block element rather than two line breaks. <code>NOTE:</code> Requires <code>&#8211;body-width</code>=<code>0</code>.</dd>
<dt><code>&#8211;unicode-snob</code></dt>
<dd> Use unicode throughout document.</dd>
<dt><code>&#8211;no-automatic-links</code></dt>
<dd> Do not use automatic links wherever applicable.</dd>
<dt><code>&#8211;no-skip-internal-links</code></dt>
<dd> Do not skip internal links.</dd>
<dt><code>&#8211;links-after-para</code></dt>
<dd> Put links after each paragraph instead of document.</dd>
<dt><code>&#8211;mark-code</code></dt>
<dd> Mark program code blocks with <code>[code]</code><i>&#8230;</i><code>[/code]</code>.</dd>
<dt><code>&#8211;default-image-alt</code>=<i>TEXT</i></dt>
<dd> The default alt string for images with missing ones.</dd>
<dt><code>&#8211;pad-tables</code></dt>
<dd> Pad the cells to equal column width in tables.</dd>
<dt><code>&#8211;decode-errors</code>=<i>DECODE_ERRORS</i></dt>
<dd> What to do in case of decode errors. <code>ignore</code>, <code>strict</code>, and <code>replace</code> are acceptable values.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show program&#8217;s version number and exit.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show a help message and exit. </dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage was written for Debian, by Stefano Rivera &lt;stefanor [at] debian.org&gt;. </p>
