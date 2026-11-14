---
title: "conserver-cf(5)"
name: "conserver-cf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-conserver-cf/"
description: "conserver.cf – console configuration file for conserver(8)"
---

<p>conserver.cf &#8211; console configuration file for <code><a href="/docs/linux/man/8-conserver/">conserver</a></code>(8)</p>
<h2>Description</h2>
<p>The format of the conserver.cf file is made up of named blocks of keyword/value pairs, comments, and optional whitespace for formatting flexibility. The block types as well as the keywords are pre-defined and explained in the <font SIZE="-1"><code>BLOCKS</code></font> section. A comment is an unquoted pound-sign to a newline. See the <font SIZE="-1"><code>PARSER</code></font> section for full details on whitespace and quoting. </p>
<p> Let me first show you a sample block with a couple of keyword/value pairs to make the description a bit simpler to understand.</p>
<dl>
<dd>
<pre>console simple { master localhost; type exec; rw *; }</pre>
</dl>
<p> This is actually a fully functional conserver.cf file (if certain conditions are met&#8230;and if you can list those conditions, you can probably can skip to the <font SIZE="-1"><code>BLOCKS</code></font> section). </p>
<p> Our example is made of up of a console-block named &#8220;simple&#8221; with three keyword/value pairs. What this does is define a console named &#8220;simple&#8221;, makes the master of that console the host &#8220;localhost&#8221;, makes the type an exec-style console, and gives every user read/write permission. This is the generic format of the file:</p>
<dl>
<dd>
<pre>block-type block-name { keyword value; ... }</pre>
</dl>
<p> To show the addition of comments and whitespace, here is the example reformatted (but functionally equivalent):</p>
<dl>
<dd>
<pre># define a console named &quot;simple&quot;
console simple {
 # setting all required values...
 master localhost;
 type exec; # exec-style console
 rw *; # allow any username
}</pre>
</dl>
<h2>Parser</h2>
<p>The parser has six characters that it considers special. These are: &#8220;{&#8221;, &#8220;}&#8221;, &#8220;;&#8221;, &#8220;#&#8221;, &#8220;\&#8221;, and &#8220;&quot;&#8221;. The first three (hereby called tokens) define the format of the configuration blocks and are used as word separators, the next is the comment character, and the last two are quoting characters. </p>
<p> Word separation occurs when the parser encounters an unquoted token and, in certain cases, whitespace. Whitespace is only used as a word separator when the parser is looking for a block-type or keyword. When it&#8217;s looking for a block-name or value, whitespace is like any other character, which allows you to embed whitespace in a block-name or value without having to quote it. Here is an example:</p>
<dl>
<dd>
<pre>default my defs { rw *; include other defs ; }</pre>
</dl>
<p> The block-type is &#8220;default&#8221;, the block-name is &#8220;my defs&#8221;, and the value for the keyword &#8220;include&#8221; is &#8220;other defs&#8221;. Whitespace around tokens are ignored so you get &#8220;other defs&#8221; instead of &#8220;other defs &#8221; as the value. </p>
<p> The only way to use one of the special characters as part of a block-name or value is to quote it. </p>
<p> Quoting is a simple matter of prefixing a character with a backslash or surrounding a group of characters with double-quotes. If a character is prefixed by a backslash, the next character is a literal (so &#8220;\&#8221; produces a &#8220;\&#8221;, &#8220;\&quot;&#8221; produces &#8220;&quot;&#8221;, &#8220;\{&#8221; produces a &#8220;{&#8221;, etc.). For double-quoted strings, all characters are literal except for &#8220;\&quot;&#8221;, which embeds a double-quote. </p>
<p> Adding a variety of quotes to our example without changing the meaning of things, we have:</p>
<dl>
<dd>
<pre>&quot;defa&quot;ult my\ defs { rw *; in
