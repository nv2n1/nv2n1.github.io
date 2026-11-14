---
title: "marked(1)"
name: "marked"
section: "1"
letter: "m"
url: "/docs/linux/man/1-marked/"
description: "marked – a javascript markdown parser"
---

<h2 class="name">NAME</h2>
<p> marked &#8211; a javascript markdown parser</p>
<h2>SYNOPSIS</h2>
<p> <code>marked</code> [-o <i>&lt;output&gt;</i>] [-i <i>&lt;input&gt;</i>] [&#8211;help] [&#8211;tokens] [&#8211;pedantic] [&#8211;gfm] [&#8211;breaks] [&#8211;tables] [&#8211;sanitize] [&#8211;smart-lists] [&#8211;lang-prefix <i>&lt;prefix&gt;</i>] [&#8211;no-etc&#8230;] [&#8211;silent] [<i>filename</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>marked</code> is a full-featured javascript markdown parser, built for speed. It also includes multiple GFM features. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>cat in.md | marked &gt; out.html</p>
<dd>
<dt>echo &quot;hello *world*&quot; | marked</p>
<dd>
<dt>marked -o out.html in.md &#8211;gfm</p>
<dd>
<dt>marked &#8211;output=&quot;hello world.html&quot; -i in.md &#8211;no-breaks</p>
<dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o, &#8211;output&nbsp;<wbr>[</code><i>output</i>]</p>
<dd> Specify file output. If none is specified, write to stdout.</p>
<dt><code>-i, &#8211;input&nbsp;<wbr>[</code><i>input</i>]</p>
<dd> Specify file input, otherwise use last argument as input file. If no input file is specified, read from stdin.</p>
<dt><code>-t, &#8211;tokens</code></p>
<dd> Output a token stream instead of html.</p>
<dt><code>&#8211;pedantic</code></p>
<dd> Conform to obscure parts of markdown.pl as much as possible. Don&#8217;t fix original markdown bugs.</p>
<dt><code>&#8211;gfm</code></p>
<dd> Enable github flavored markdown.</p>
<dt><code>&#8211;breaks</code></p>
<dd> Enable GFM line breaks. Only works with the gfm option.</p>
<dt><code>&#8211;tables</code></p>
<dd> Enable GFM tables. Only works with the gfm option.</p>
<dt><code>&#8211;sanitize</code></p>
<dd> Sanitize output. Ignore any HTML input.</p>
<dt><code>&#8211;smart-lists</code></p>
<dd> Use smarter list behavior than the original markdown.</p>
<dt><code>&#8211;lang-prefix&nbsp;<wbr>[</code><i>prefix</i>]</p>
<dd> Set the prefix for code block classes.</p>
<dt><code>&#8211;no-sanitize, -no-etc&#8230;</code></p>
<dd> The inverse of any of the marked options above.</p>
<dt><code>&#8211;silent</code></p>
<dd> Silence error output.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display help information. </p>
</dl>
<h2>CONFIGURATION</h2>
<p> For configuring and running programmatically. </p>
<p> <code>Example</code> </p>
<p>&nbsp;<wbr>require(&#8216;marked&#8217;)(&#8216;*foo*&#8217;,&nbsp;<wbr>{&nbsp;<wbr>gfm: true&nbsp;<wbr>}); </p>
<h2>BUGS</h2>
<p> Please report any bugs to <a rel="nofollow" href="https://github.com/chjj/marked.">https://github.com/chjj/marked.</a> </p>
<h2>LICENSE</h2>
<p> Copyright (c) 2011-2014, Christopher Jeffrey (MIT License). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-markdown/">markdown</a>(1),</code> <code><a href="/docs/linux/man/1-node-js/">node.js</a>(1)</code> </p>
<h2>Index</h2>
