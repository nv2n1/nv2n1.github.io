---
title: "html2text-2-7(1)"
name: "html2text-2-7"
section: "1"
letter: "h"
url: "/docs/linux/man/1-html2text-2-7/"
description: "html2text-2.7 – manual page for html2text-2.7 2016.9.19"
---

<p>html2text-2.7 &#8211; manual page for html2text-2.7 2016.9.19</p>
<h2>Synopsis</h2>
<p><code>html2text-2.7</code> [<i>(filename|url) </i>[<i>encoding</i>]]</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>&#8211;default-image-alt</code>=<i>DEFAULT_IMAGE_ALT</i></p>
<dd>The default alt string for images with missing ones</p>
<dt><code>&#8211;pad-tables</code></p>
<dd>pad the cells to equal column width in tables</p>
<dt><code>&#8211;no-wrap-links</code></p>
<dd>wrap links during conversion</p>
<dt><code>&#8211;ignore-emphasis</code></p>
<dd>don&#8217;t include any formatting for emphasis</p>
<dt><code>&#8211;reference-links</code></p>
<dd>use reference style links instead of inline links</p>
<dt><code>&#8211;ignore-links</code></p>
<dd>don&#8217;t include any formatting for links</p>
<dt><code>&#8211;protect-links</code></p>
<dd>protect links from line breaks surrounding them with angle brackets</p>
<dt><code>&#8211;ignore-images</code></p>
<dd>don&#8217;t include any formatting for images</p>
<dt><code>&#8211;images-to-alt</code></p>
<dd>Discard image data, only keep alt text</p>
<dt><code>&#8211;images-with-size</code></p>
<dd>Write image tags with height and width attrs as raw html to retain dimensions</p>
<dt><code>-g</code>, <code>&#8211;google-doc</code></p>
<dd>convert an html-exported Google Document</p>
<dt><code>-d</code>, <code>&#8211;dash-unordered-list</code></p>
<dd>use a dash rather than a star for unordered list items</p>
<dt><code>-e</code>, <code>&#8211;asterisk-emphasis</code></p>
<dd>use an asterisk rather than an underscore for emphasized text</p>
<dt><code>-b</code> BODY_WIDTH, <code>&#8211;body-width</code>=<i>BODY_WIDTH</i></p>
<dd>number of characters per output line, 0 for no wrap</p>
<dt><code>-i</code> LIST_INDENT, <code>&#8211;google-list-indent</code>=<i>LIST_INDENT</i></p>
<dd>number of pixels Google indents nested lists</p>
<dt><code>-s</code>, <code>&#8211;hide-strikethrough</code></p>
<dd>hide strike-through text. only relevant when <code>-g</code> is specified as well</p>
<dt><code>&#8211;escape-all</code></p>
<dd>Escape all special characters. Output is less readable, but avoids corner case formatting issues.</p>
<dt><code>&#8211;bypass-tables</code></p>
<dd>Format tables in HTML rather than Markdown syntax.</p>
<dt><code>&#8211;ignore-tables</code></p>
<dd>Ignore table-related tags (table, th, td, tr) while keeping rows.</p>
<dt><code>&#8211;single-line-break</code></p>
<dd>Use a single line break after a block element rather than two line breaks. NOTE: Requires <code>&#8211;body-width</code>=<i>0</i></p>
<dt><code>&#8211;unicode-snob</code></p>
<dd>Use unicode throughout document</p>
<dt><code>&#8211;no-automatic-links</code></p>
<dd>Do not use automatic links wherever applicable</p>
<dt><code>&#8211;no-skip-internal-links</code></p>
<dd>Do not skip internal links</p>
<dt><code>&#8211;links-after-para</code></p>
<dd>Put links after each paragraph instead of document</p>
<dt><code>&#8211;mark-code</code></p>
<dd>Mark program code blocks with [code]&#8230;[/code]</p>
<dt><code>&#8211;decode-errors</code>=<i>DECODE_ERRORS</i></p>
<dd>What to do in case of decode errors.&#8217;ignore&#8217;, &#8216;strict&#8217; and &#8216;replace&#8217; are acceptable values </p>
</dl>
