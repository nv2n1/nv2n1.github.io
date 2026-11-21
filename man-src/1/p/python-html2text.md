---

title: "python-html2text(1)"
name: "python-html2text"
section: "1"
letter: "p"
url: "/docs/linux/man/1-python-html2text/"
description: "python-html2text – manual page for python-html2text 2016.9.19"
---

<p> python-html2text &#8211; manual page for python-html2text 2016.9.19</p>
<h2>SYNOPSIS</h2>
<p> <code>python-html2text</code> [<i>(filename|url) </i>[<i>encoding</i>]]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>&#8211;default-image-alt</code>=<i>DEFAULT_IMAGE_ALT</i></dt>
<dd> The default alt string for images with missing ones</dd>
<dt><code>&#8211;pad-tables</code></dt>
<dd> pad the cells to equal column width in tables</dd>
<dt><code>&#8211;no-wrap-links</code></dt>
<dd> wrap links during conversion</dd>
<dt><code>&#8211;ignore-emphasis</code></dt>
<dd> don&#8217;t include any formatting for emphasis</dd>
<dt><code>&#8211;reference-links</code></dt>
<dd> use reference style links instead of inline links</dd>
<dt><code>&#8211;ignore-links</code></dt>
<dd> don&#8217;t include any formatting for links</dd>
<dt><code>&#8211;protect-links</code></dt>
<dd> protect links from line breaks surrounding them with angle brackets</dd>
<dt><code>&#8211;ignore-images</code></dt>
<dd> don&#8217;t include any formatting for images</dd>
<dt><code>&#8211;images-to-alt</code></dt>
<dd> Discard image data, only keep alt text</dd>
<dt><code>&#8211;images-with-size</code></dt>
<dd> Write image tags with height and width attrs as raw html to retain dimensions</dd>
<dt><code>-g</code>, <code>&#8211;google-doc</code></dt>
<dd> convert an html-exported Google Document</dd>
<dt><code>-d</code>, <code>&#8211;dash-unordered-list</code></dt>
<dd> use a dash rather than a star for unordered list items</dd>
<dt><code>-e</code>, <code>&#8211;asterisk-emphasis</code></dt>
<dd> use an asterisk rather than an underscore for emphasized text</dd>
<dt><code>-b</code> BODY_WIDTH, <code>&#8211;body-width</code>=<i>BODY_WIDTH</i></dt>
<dd> number of characters per output line, 0 for no wrap</dd>
<dt><code>-i</code> LIST_INDENT, <code>&#8211;google-list-indent</code>=<i>LIST_INDENT</i></dt>
<dd> number of pixels Google indents nested lists</dd>
<dt><code>-s</code>, <code>&#8211;hide-strikethrough</code></dt>
<dd> hide strike-through text. only relevant when <code>-g</code> is specified as well</dd>
<dt><code>&#8211;escape-all</code></dt>
<dd> Escape all special characters. Output is less readable, but avoids corner case formatting issues.</dd>
<dt><code>&#8211;bypass-tables</code></dt>
<dd> Format tables in HTML rather than Markdown syntax.</dd>
<dt><code>&#8211;ignore-tables</code></dt>
<dd> Ignore table-related tags (table, th, td, tr) while keeping rows.</dd>
<dt><code>&#8211;single-line-break</code></dt>
<dd> Use a single line break after a block element rather than two line breaks. NOTE: Requires <code>&#8211;body-width</code>=<i>0</i></dd>
<dt><code>&#8211;unicode-snob</code></dt>
<dd> Use unicode throughout document</dd>
<dt><code>&#8211;no-automatic-links</code></dt>
<dd> Do not use automatic links wherever applicable</dd>
<dt><code>&#8211;no-skip-internal-links</code></dt>
<dd> Do not skip internal links</dd>
<dt><code>&#8211;links-after-para</code></dt>
<dd> Put links after each paragraph instead of document</dd>
<dt><code>&#8211;mark-code</code></dt>
<dd> Mark program code blocks with [code]&#8230;[/code]</dd>
<dt><code>&#8211;decode-errors</code>=<i>DECODE_ERRORS</i></dt>
<dd> What to do in case of decode errors.&#8217;ignore&#8217;, &#8216;strict&#8217; and &#8216;replace&#8217; are acceptable values </dd>
</dl>
