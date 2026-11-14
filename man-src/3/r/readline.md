---
title: "readline(3)"
name: "readline"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readline/"
description: "readline – get a line from a user with editing"
---

<p>readline &#8211; get a line from a user with editing</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;readline/history.h&gt;
#include &lt;readline/readline.h&gt;
#include &lt;stdio.h&gt;
char *

readline(const char *prompt);</code></pre>
<h2>Copyright</h2>
<p>Readline is Copyright (C) 1989-2011 Free Software Foundation, Inc.</p>
<h2>Description</h2>
<p><code>readline</code> will read a line from the terminal and return it, using <code>prompt</code> as a prompt. If <code>prompt</code> is <code>NULL</code> or the empty string, no prompt is issued. The line returned is allocated with <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3); the caller must free it when finished. The line returned has the final newline removed, so only the text of the line remains. </p>
<p> <code>readline</code> offers editing capabilities while the user is entering the line. By default, the line editing commands are similar to those of emacs. A vi-style line editing interface is also available. </p>
<p> This manual page describes only the most basic use of <code>readline</code>. Much more functionality is available; see <i>The GNU Readline Library</i> and <i>The GNU History Library</i> for additional information.</p>
<h2>Return Value</h2>
<p><code>readline</code> returns the text of the line read. A blank line returns the empty string. If <code>EOF</code> is encountered while reading a line, and the line is empty, <code>NULL</code> is returned. If an <code>EOF</code> is read with a non-empty line, it is treated as a newline.</p>
<h2>Notation</h2>
<p>An Emacs-style notation is used to denote keystrokes. Control keys are denoted by C-<i>key</i>, e.g., C-n means Control-N. Similarly, <i>meta</i> keys are denoted by M-<i>key</i>, so M-x means Meta-X. (On keyboards without a <i>meta</i> key, M-<i>x</i> means ESC <i>x</i>, i.e., press the Escape key then the <i>x</i> key. This makes ESC the <i>meta prefix</i>. The combination M-C-<i>x</i> means ESC-Control-<i>x</i>, or press the Escape key then hold the Control key while pressing the <i>x</i> key.) </p>
<p> Readline commands may be given numeric <i>arguments</i>, which normally act as a repeat count. Sometimes, however, it is the sign of the argument that is significant. Passing a negative argument to a command that acts in the forward direction (e.g., <code>kill-line</code>) causes that command to act in a backward direction. Commands whose behavior with arguments deviates from this are noted. </p>
<p> When a command is described as <i>killing</i> text, the text deleted is saved for possible future retrieval (<i>yanking</i>). The killed text is saved in a <i>kill ring</i>. Consecutive kills cause the text to be accumulated into one unit, which can be yanked all at once. Commands which do not kill text separate the chunks of text on the kill ring.</p>
<h2>Initialization File</h2>
<p>Readline is customized by putting commands in an initialization file (the <i>inputrc</i> file). The name of this file is taken from the value of the <code>INPUTRC</code> environment variable. If that variable is unset, the default is <i>~/.inputrc</i>. If that file does not exist or cannot be read, the ultimate default is <i>/etc/inputrc</i>. When a program which uses the readline library starts up, the init file is read, and the key bindings and variables are set. There are only a few basic constructs allowed in the readline init file. Blank lines are ignored. Lines beginning with a <code>#</code> are comments. Lines beginning with a <code>$</code> indicate conditional constructs. Other lines denote key bindings and variable settings. Each program using this library may add its own commands and bindings. </p>
<p> For example, placing</p>
<dl>
<dd>M-Control-u: universal-argument</dl>
<p> or</p>
<dl>
<dd>C-Meta-u: universal-argument</dl>
<p> into the <i>inputrc</i> would make M-C-u execute the readline command <i>universal-argument</i>. </p>
<p> The following symbolic character names are recognized while processing key bindings: <i>DEL</i>, <i>ESC</i>, <i>ESCAPE</i>, <i>LFD</i>, <i>NEWLINE</i>, <i>RET</i>, <i>RETURN</i>, <i>RUBOUT</i>, <i>SPACE</i>, <i>SPC</i>, and <i>TAB</i>. </p>
<p> In addition to command names, readline allows keys to be bound to a string that is inserted when the key is pressed (a <i>macro</i>).</p>
<h3>Key Bindings</h3>
<p>The syntax for controlling key bindings in the <i>inputrc</i> file is simple. All that is required is the name of the command or the text of a macro and a key sequence to which it should be bound. The name may be specified in one of two ways: as a symbolic key name, possibly with <i>Meta-</i> or <i>Control-</i> prefixes, or as a key sequence. The name and key sequence are separated by a colon. There can be no whitespace between the name and the colon. </p>
<p> When using the form <code>keyname</code>:<i>function-name</i> or <i>macro</i>, <i>keyname</i> is the name of a key spelled out in English. For example: </p>
<dl>
<dd>Control-u: universal-argument<br />
 Meta-Rubout: backward-kill-word<br />
 Control-o: &quot;&gt; output&quot;</dl>
<p> In the above example, <i>C-u</i> is bound to the function <code>universal-argument</code>, <i>M-DEL</i> is bound to the function <code>backward-kill-word</code>, and <i>C-o</i> is bound to run the macro expressed on the right hand side (that is, to insert the text &#8220;&gt; output&#8221; into the line). </p>
<p> In the second form, <code>&quot;keyseq&quot;</code>:<i>function-name</i> or <i>macro</i>, <code>keyseq</code> differs from <code>keyname</code> above in that strings denoting an entire key sequence may be specified by placing the sequence within double quotes. Some GNU Emacs style key escapes can be used, as in the following example, but the symbolic character names are not recognized. </p>
<dl>
<dd>&quot;\C-u&quot;: universal-argument<br />
 &quot;\C-x\C-r&quot;: re-read-init-file<br />
 &quot;[11~&quot;: &quot;Function Key 1&quot;</dl>
<p> In this example, <i>C-u</i> is again bound to the function <code>universal-argument</code>. <i>C-x C-r</i> is bound to the function <code>re-read-init-file</code>, and <i>ESC [ 1 1 ~</i> is bound to insert the text &#8220;Function Key 1&#8221;. </p>
<p> The full set of GNU Emacs style escape sequences available when specifying key sequences is</p>
<dl>
<dd>
<dl>
<dt><code>\C-</code></p>
<dd>control prefix</p>
<dt><code>\M-</code></p>
<dd>meta prefix</p>
<dt><code></code></p>
<dd>an escape character</p>
<dt><code>\</code></p>
<dd>backslash</p>
<dt><code>\</code></p>
<dd>literal &quot;, a double quote</p>
<dt><code>\&#8217;</code></p>
<dd>literal &#8216;, a single quote</dl>
</dl>
<p> In addition to the GNU Emacs style escape sequences, a second set of backslash escapes is available:</p>
<dl>
<dd>
<dl>
<dt><code></code></p>
<dd>alert (bell)</p>
<dt><code></code></p>
<dd>backspace</p>
<dt><code>\d</code></p>
<dd>delete</p>
<dt><code></code></p>
<dd>form feed</p>
<dt><code>
</code></p>
<dd>newline</p>
<dt><code></code></p>
<dd>carriage return</p>
<dt><code>	</code></p>
<dd>horizontal tab</p>
<dt><code></code></p>
<dd>vertical tab</p>
<dt><code>\</code><i>nnn</i></p>
<dd>the eight-bit character whose value is the octal value <i>nnn</i> (one to three digits)</p>
<dt><code>
