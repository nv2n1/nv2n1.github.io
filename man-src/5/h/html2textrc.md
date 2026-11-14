---
title: "html2textrc(5)"
name: "html2textrc"
section: "5"
letter: "h"
url: "/docs/linux/man/5-html2textrc/"
description: "html2textrc – formatting properties file for"
---

<p>html2textrc &#8211; formatting properties file for </p>
<p> <a href="/docs/linux/man/1-html2text/">html2text</a>(1)</p>
<h2>Synopsis</h2>
<p><i>Key</i> [ <code>=</code> | <code>:</code> ] <i>Value</i></p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/5-html2textrc/">html2textrc</a></code>(5) file defines a set of formatting properties used by the <code><a href="/docs/linux/man/1-html2text/">html2text</a></code>(1) utility, that overrides the program&#8217;s built-in formatting defaults. Each line of the <code><a href="/docs/linux/man/5-html2textrc/">html2textrc</a></code>(5) file is either a formatting property or a comment. </p>
<p> Lines with a leading &quot;#&quot; or &quot;!&quot; (i.e. the first non-space character is a &quot;#&quot; or a &quot;!&quot;) and blank lines (i.e. a line consisting only of white-space characters), are considered comments and ignored. Everything else is literary interpreted by the parser as a formatting property, where a string-type property value may also be empty (unsets default value). Both, the property key and the property value, may contain C-style escape sequences to mask meta characters. </p>
<p> <code>A property definition line consists of:</code></p>
<dl>
<dt>(1)</p>
<dd>Optional leading space,</p>
<dt>(2)</p>
<dd>the property key (a sequence of non-space characters except &quot;=&quot; and &quot;:&quot;) as described below,</p>
<dt>(3)</p>
<dd>an optional space,</p>
<dt>(4)</p>
<dd>an optional &quot;=&quot; or &quot;:&quot;,</p>
<dt>(5)</p>
<dd>optional space,</p>
<dt>(6)</p>
<dd>the property value as described below.<br />
 Everything up to the next newline is interpreted <i>literary</i> as the value of the specified element. Literary meant leading white-space must be quoted with backslashes (i.e. &quot;\ &quot;). Be aware not to include unwanted trailing white-space characters.</dl>
<h2>Options</h2>
<p>The following is the list of valid formatting properties, together with their default values. If the <code>-style</code> command line option of <code><a href="/docs/linux/man/1-html2text/">html2text</a></code>(1) is used, different default values apply. </p>
<p> Curly braces indicate alternatives, e.g. <code>{A B}C</code> stands for <code>AC</code> or <code>BC</code>.</p>
<dl>
<dt><code>DOCUMENT.{vspace.{before after} indent.{left right}} = 0</code></p>
<dd>Specifies how many blank lines are inserted before and after, and how many blank columns are inserted to the left and to the right of the formatted document. (Numeric.)</p>
<dt><code>BODY.{vspace.{before after} indent.{left right}} = 0</code></p>
<dd>Same for the document body. (Since the document body is currently the only document part that is rendered, it is virtually the same whether you specify <code>DOCUMENT</code> or <code>BODY</code>). (Numeric.)</p>
<dt><code>{OL UL DIR MENU DL}.vspace.{before between after} = 0</code></p>
<dd>Specifies how many blank lines are inserted before a list, between the individual list items, and after the list. (Numeric.)</p>
<dt><code>{OL UL DIR MENU}.indents = 6</code></p>
<dd>Specifies by how deep list items are indented. If an item bullet would not fit into the space created by the indentation, then the indentation is automatically increased such that the bullet fits in (relevant for relatively wide bullets, e.g. roman numbers). If <i>N</i> blank-separated integers are specified instead of one, then the first <i>N-1</i> integers specify indentation for the first <i>N-1</i> list nesting levels, while the last integer specifies the indentation for nesting levels <i>N</i> and higher. (Numeric.)</p>
<dt><code>{UL DIR}.default_types = DISC CIRCLE SQUARE</code></p>
<dd>Specifies the default list type (i.e. the bullet style), if the HTML list tag does not specify an explicit type. Legal values are <code>NO_BULLET</code>, <code>DISC</code>, <code>SQUARE</code>, <code>CIRCLE</code>, <code>CUSTOM1</code>, <code>CUSTOM2</code> and <code>CUSTOM3</code>. If more than one value is specified, then the values apply for the respective list nesting levels (see <code>indents</code>). (Option.)</p>
<dt><code>MENU.default_types = NO_BULLET</code></p>
<dd>Same for &lt;MENU&gt;, but here the default is <code>NO_BULLET</code>. (Option.)</p>
<dt><code>LI.{disc square circle custom1 custom2 custom3}_bullet = {* # o + &#8211; ~}</code></p>
<dd>Specifies the strings used as list item bullets. (String.)</p>
<dt><code>{DT DD}.{vspace.{before after} indent.{left right}} = 0</code></p>
<dd>Specifies how many blank lines are inserted before and after, and how many blank columns are inserted to the left and to the right of each &lt;DT&gt; or &lt;DD&gt; element. (Numeric.)</p>
<dt><code>HR.marker = =</code></p>
<dd>Specifies the character to use for horizontal rules. (String.)</p>
<dt><code>HR.{vspace.{before after} indent.{left right}} = 0</code></p>
<dd>Specifies how many blank lines are inserted before and after, and how many blank columns are inserted to the left and to the right of the horizontal rule. (Numeric.)</p>
<dt><code>{H1 H2 H3 H4 H5 H6}.prefix = {****** ***** **** *** ** *}</code></p>
<dd>Specifies how headings are decorated with a prefix. (The default values have a trailing blank, e.g. &quot;******&nbsp;&quot;.) (String.)</p>
<dt><code>{H1 H2 H3 H4 H5 H6}.suffix = {****** ***** **** *** ** *}</code></p>
<dd>Specifies how headings are decorated with a suffix. (The default values have a leading blank, e.g. &quot;\&nbsp;******&quot;.) (String.)</p>
<dt><code>{H1 H2 H3 H4 H5 H6}.vspace.{before after} = 0</code></p>
<dd>Specifies how many blank lines are inserted before and after headings. (Numeric.)</p>
<dt><code>{PRE P}.{vspace.{before after} indent.{left right}} = 0</code></p>
<dd>Specifies how many blank lines are inserted before and after, and how many blank columns are inserted to the left and to the right of these items. (Numeric.)</p>
<dt><code>{BLOCKQUOTE ADDRESS}.{vspace.{before after} indent.{left right}} = {0 0 5 5}</code></p>
<dd>Specifies how many blank lines are inserted before and after, and how many blank columns are inserted to the left and to the right of these items. (Numeric.)</p>
<dt><code>TABLE.vspace.{before after} = 0</code></p>
<dd>Specifies how many blank lines are inserted before and after tables. (Numeric.)</p>
<dt><code>{H1 H2 H3 H4 H5 H6}.attributes = BOLD</code></p>
<dd>Specifies the cell attributes for headings. The value is a sequence of <code>NONE</code>, <code>BOLD</code>, <code>UNDERLINE</code> and <code>STRIKETHROUGH</code>. (Option.)</p>
<dt><code>{TT I BIG SMALL SUB SUP DFN CODE SAMP KBD CITE}.attributes = NONE</code></p>
<dd>Specifies the cell attributes for these text items. Legal values are: <code>NONE</code>, <code>BOLD</code>, <code>UNDERLINE</code> or <code>STRIKETHROUGH</code>. (Option.)</p>
<dt><code>U.attributes = UNDERLINE</code></p>
<dd>Same for &lt;U&gt; elements, but with a different default value. (Option.)</p>
<dt><code>{B EM STRONG}.attributes = BOLD</code></p>
<dd>Same for these elements, but with a different default value. (Option.)</p>
<dt><code>STRIKE.attributes = STRIKETHROUGH</code></p>
<dd>Same for &lt;STRIKE&gt; elements, but with a different default value. (Option.)</p>
<dt><code>A.attributes.{internal_link external_link} = UNDERLINE</code></p>
<dd>Specifies the cell attributes for links. A link is an &lt;A&gt; element that has an &quot;href&quot; attribute. An internal link is a link whose &quot;href&quot; attribute starts with a hash character (e.g. &quot;&lt;A href=&quot;#42&quot;&gt;&quot;). Legal values are again <code>NONE</code>, <code>BOLD</code>, <code>UNDERLINE</code> and <code>STRIKETHROUGH</code>. (Option.)</p>
<dt><code>IMG.replace.{all noalt} = unset</code></p>
<dd>Specifies the string used to replace all &lt;IMG&gt; elements, or those without an &quot;ALT&quot; attribute set. (String.)</p>
<dt><code>IMG.alt.{prefix suffix} = {[ ]}</code></p>
<dd>Specifies how the values (if any) of IMG elements&#8217; &quot;ALT&quot; attributes are marked. (String.)</dl>
<h2>Author</h2>
<p>Current maintainer and primary download location for <code>html2text</code> is:<br />
 Martin Bayer &lt;mbayer [at] zedat.fu-berlin.de&gt;<br />
 <a rel="nofollow" href="http://userpage.fu-berlin.de/~mbayer/tools/">http://userpage.fu-berlin.de/~mbayer/tools/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-html2text/">html2text</a></code>(1) </p>
