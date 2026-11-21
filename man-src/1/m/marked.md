---

title: "marked(1)"
name: "marked"
section: "1"
letter: "m"
url: "/docs/linux/man/1-marked/"
description: "marked – a javascript markdown parser"
---

<p> marked &#8211; a javascript markdown parser</p>
<h2>SYNOPSIS</h2>
<p> <code>marked</code> [-o <i>&lt;output&gt;</i>] [-i <i>&lt;input&gt;</i>] [&#8211;help] [&#8211;tokens] [&#8211;pedantic] [&#8211;gfm] [&#8211;breaks] [&#8211;tables] [&#8211;sanitize] [&#8211;smart-lists] [&#8211;lang-prefix <i>&lt;prefix&gt;</i>] [&#8211;no-etc&#8230;] [&#8211;silent] [<i>filename</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>marked</code> is a full-featured javascript markdown parser, built for speed. It also includes multiple GFM features. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>cat in.md | marked &gt; out.html</dt>
<dd>
</dd><dt>echo &quot;hello *world*&quot; | marked</dt>
<dd>
</dd><dt>marked -o out.html in.md &#8211;gfm</dt>
<dd>
</dd><dt>marked &#8211;output=&quot;hello world.html&quot; -i in.md &#8211;no-breaks</dt>
<dd>
</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o, &#8211;output&nbsp;<wbr>[</code><i>output</i>]</dt>
<dd> Specify file output. If none is specified, write to stdout.</dd>
<dt><code>-i, &#8211;input&nbsp;<wbr>[</code><i>input</i>]</dt>
<dd> Specify file input, otherwise use last argument as input file. If no input file is specified, read from stdin.</dd>
<dt><code>-t, &#8211;tokens</code></dt>
<dd> Output a token stream instead of html.</dd>
<dt><code>&#8211;pedantic</code></dt>
<dd> Conform to obscure parts of markdown.pl as much as possible. Don&#8217;t fix original markdown bugs.</dd>
<dt><code>&#8211;gfm</code></dt>
<dd> Enable github flavored markdown.</dd>
<dt><code>&#8211;breaks</code></dt>
<dd> Enable GFM line breaks. Only works with the gfm option.</dd>
<dt><code>&#8211;tables</code></dt>
<dd> Enable GFM tables. Only works with the gfm option.</dd>
<dt><code>&#8211;sanitize</code></dt>
<dd> Sanitize output. Ignore any HTML input.</dd>
<dt><code>&#8211;smart-lists</code></dt>
<dd> Use smarter list behavior than the original markdown.</dd>
<dt><code>&#8211;lang-prefix&nbsp;<wbr>[</code><i>prefix</i>]</dt>
<dd> Set the prefix for code block classes.</dd>
<dt><code>&#8211;no-sanitize, -no-etc&#8230;</code></dt>
<dd> The inverse of any of the marked options above.</dd>
<dt><code>&#8211;silent</code></dt>
<dd> Silence error output.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display help information. </dd>
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
<p> <code><a href="/docs/linux/man/1-markdown/">markdown</a>(1),</code> <code>node.js(1)</code> </p>
