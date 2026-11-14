---
title: "dex-syntax(7)"
name: "dex-syntax"
section: "7"
letter: "d"
url: "/docs/linux/man/7-dex-syntax/"
description: "Syntax of syntax highlighting files used by dex."
---

<p>Syntax of syntax highlighting files used by dex.</p>
<h2>Description</h2>
<p>Syntax file consists of states. A state consists of optional conditionals and one default action. The best way understand the syntax is to read /usr/share/dex/syntax/dex (a simple example) or /usr/share/dex/syntax/c (a more complete example using sub-syntaxes). </p>
<p> Basic syntax of the syntax files is the same used in the rc files, but the available commands are different. </p>
<p> Conditionals and default actions have destination state. The special destination state &quot;this&quot; can be used to jump to current state.</p>
<h2>Commands</h2>
<h3>Main commands</h3>
<p>syntax &lt;name&gt;</p>
<dl>
<dd>Begin a new syntax. One syntax file can contain multiple syntax definitions, but you should only define one real syntax in one syntax file.</dl>
<dl>
<dd>See also SUB-SYNTAXES.</dl>
<p> state &lt;name&gt; [emit-color]</p>
<dl>
<dd>Add new state. Conditionals (if any) and one default action must follow. First state is the start state.</dl>
<p> default &lt;color&gt; &lt;name&gt;&#8230;</p>
<dl>
<dd>Set default color for emitted name.</dl>
<dl>
<dd>Example:</p>
<dl>
<dd>default numeric oct dec hex</dl>
</dl>
<dl>
<dd>If there is no color defined for oct, dec or hex then color numeric is used instead.</dl>
<p> list [-i] &lt;name&gt; &lt;string&gt;&#8230;</p>
<dl>
<dd>Define a list of strings.</dl>
<dl>
<dd>Example:</p>
<dl>
<dd>list keyword if else for while do continue switch case</dl>
</dl>
<dl>
<dd>Use conditional <code>inlist</code> to test if a buffered string is in a list.</dl>
<dl>
<dd>&nbsp;<wbr>-i Make list case-insensitive.</dl>
<h3>Conditionals</h3>
<p>bufis [-i] &lt;string&gt; &lt;destination&gt; [emit-name]</p>
<dl>
<dd>Test if buffered bytes are same as <i>string</i>. If they are emit <i>emit-name</i> and jump to destination state.</dl>
<p> char [-bn] &lt;characters&gt; &lt;destination&gt; [emit-name]</p>
<dl>
<dd>Test if current byte is in the character list. If it is then emit <i>emit-color</i> and jump to destination state. If <i>emit-name</i> is not given then destination states emit name is used.</dl>
<dl>
<dd>Characters is a list of strings. Ranges are supported (a-d is same as abcd).</dl>
<dl>
<dd>-b Add byte to buffer.</dl>
<dl>
<dd>-n Invert character bitmap.</dl>
<p> heredocend &lt;destination&gt;</p>
<dl>
<dd>Compare following characters to heredoc end delimiter and go to destination state if comparison is true.</dl>
<p> inlist &lt;list&gt; &lt;destination&gt; [emit-name]</p>
<dl>
<dd>Test if buffered bytes are found in <i>list</i>. If found emit <i>emit-name</i> and jump to destination state.</dl>
<p> str [-i] &lt;string&gt; &lt;destination&gt; [emit-name]</p>
<dl>
<dd>See if following bytes are same as <i>string</i>. If they are emit <i>emit-name</i> and jump to destination state.</dl>
<dl>
<dd>-i case-insensitive.</dl>
<dl>
<dd>NOTE: This conditional can be slow, especially if string is longer than two bytes.</dl>
<h3>Default actions</h3>
<p>Last command of every state must be default action. It is an unconditional jump. </p>
<p> eat &lt;destination&gt; [emit-name]</p>
<dl>
<dd>Consume byte, emit <i>emit-name</i> color and continue to destination state.</dl>
<p> heredocbegin &lt;subsyntax&gt; &lt;return-state&gt;</p>
<dl>
<dd>Store buffered bytes as heredoc end delimiter and go to subsyntax. Subsyntax is like any other subsyntax but it must contain heredocend conditional.</dl>
<p> noeat [-b] &lt;destination&gt;</p>
<dl>
<dd>Continue to destination state without emitting color or consuming byte.</dl>
<dl>
<dd>-b Don&#8217;t stop buffering.</dl>
<h3>Other commands</h3>
<p>recolor &lt;color&gt; [count]</p>
<dl>
<dd>If count is given, recolor count previous bytes, otherwise recolor buffered bytes.</dl>
<h2>Sub-Syntaxes</h2>
<p>Sub-syntaxes are useful when same states are needed in many contexts. </p>
<p> Sub-syntax name must be prefixed with &quot;.&quot;. It is recommended to also use main syntax&#8217;s name in the prefix. For example &quot;.c-comment&quot; if &quot;c&quot; is the main syntax. </p>
<p> Sub-syntax is a syntax of which some destination state&#8217;s name is END. END is a special state name which is replaced by state given at another syntax. </p>
<p> Example: </p>
<dl>
<dd># sub-syntax<br />
 syntax .c-comment</dl>
<dl>
<dd>state comment</p>
<dl>
<dd>char &quot;*&quot; star<br />
 eat comment</dl>
</dl>
<dl>
<dd>state star comment</p>
<dl>
<dd># END is a special state name<br />
 char / END comment<br />
 noeat comment</dl>
</dl>
<dl>
<dd># main syntax<br />
 syntax c</dl>
<dl>
<dd>state c code</p>
<dl>
<dd>char &quot; 	
&quot; c<br />
 char -b a-zA-Z_ ident<br />
 char &quot;\&quot;&quot; string<br />
 char &quot;&#8217;&quot; char<br />
 # call sub-syntax<br />
 str &quot;/*&quot; .c-comment:c<br />
 eat c</dl>
</dl>
<dl>
<dd># other states removed</dl>
<p> In this example the destination state .c-comment:c is special syntax for calling a sub-syntax. &quot;.c-comment&quot; is name of the sub-syntax and &quot;c&quot; is the return state defined in the main syntax. Whole sub-syntax tree is copied into the main syntax and all destination states in the sub-syntax whose name is END are replaced with &quot;c&quot;.</p>
<h2>Authors</h2>
<p>Timo Hirvonen &lt;tihirvon [at] gmail.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-dex/">dex</a>(1) </p>
