---
title: "xcompose(3)"
name: "xcompose"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcompose/"
description: "Compose – X client mappings for multi-key input sequences"
---

<p>Compose &#8211; X client mappings for multi-key input sequences </p>
<h2>Description</h2>
<p>The X library, libX11, provides a simple input method for characters beyond those represented on typical keyboards using sequences of key strokes that are combined to enter a single character. </p>
<p> The compose file is searched for in the following order:</p>
<dl COMPACT>
<dt>&#8211;</p>
<dd>If the environment variable <code>$XCOMPOSEFILE</code> is set, its value is used as the name of the Compose file.</p>
<dt>&#8211;</p>
<dd>If the user&#8217;s home directory has a file named <i>.XCompose</i>, it is used as the Compose file.</p>
<dt>&#8211;</p>
<dd>The system provided compose file is used by mapping the locale to a compose file from the list in <i>/usr/share/X11/locale/compose.dir</i>.</dl>
<p> Compose files can use an &#34;<code>include</code>&#34; instruction. This allows local modifications to be made to existing compose files without including all of the content directly. For example, the system&#8217;s iso8859-1 compose file can be included with a line like this:</p>
<dl COMPACT>
<dd><code>include &#34;</code><i>%S/iso8859-1/Compose</i><code>&#34;</code></dl>
<p> There are several substitutions that can be made in the file name of the include instruction:</p>
<dl COMPACT>
<dt><i>%H</i></p>
<dd>expands to the user&#8217;s home directory (the <code>$HOME</code> environment variable)</p>
<dt><i>%L</i></p>
<dd>expands to the name of the locale specific Compose file (i.e., &#34;<i>/usr/share/X11/locale/&lt;localename&gt;/Compose</i>&#34;)</p>
<dt><i>%S</i></p>
<dd>expands to the name of the system directory for Compose files (i.e., &#34;<i>/usr/share/X11/locale</i>&#34;)</dl>
<p> For example, you can include in your compose file the default Compose file by using:</p>
<dl COMPACT>
<dd><code>include &#34;%L&#34;</code></dl>
<p> and then rewrite only the few rules that you need to change. New compose rules can be added, and previous ones replaced.</p>
<h2>File Format</h2>
<p>Compose files are plain text files, with a separate line for each compose sequence. Comments begin with <code>#</code> characters. Each compose sequence specifies one or more events and a resulting input sequence, with an optional comment at the end of the line:</p>
<dl COMPACT>
<dd><i>EVENT</i> [<i>EVENT</i>&#8230;] <code>:</code> <i>RESULT</i> [<code>#</code> <i>COMMENT</i>]</dl>
<p> Each event consists of a specified input keysym, and optional modifier states:</p>
<dl COMPACT>
<dd>[([<code>!</code>] ([<code>~</code>] <i>MODIFIER</i>)&#8230;) | <code>None</code>] <code>&lt;</code><i>keysym</i><code>&gt;</code></dl>
<p> If the modifier list is preceded by &#34;<code>!</code>&#34; it must match exactly. MODIFIER may be one of Ctrl, Lock, Caps, Shift, Alt or Meta. Each modifier may be preceded by a &#34;<code>~</code>&#34; character to indicate that the modifier must not be present. If &#34;<code>None</code>&#34; is specified, no modifier may be present. </p>
<p> The result specifies a string, keysym, or both, that the X client receives as input when the sequence of events is input:</p>
<dl COMPACT>
<dd><code>&#34;</code><i>STRING</i><code>&#34;</code> | <i>keysym</i> | <code>&#34;</code><i>STRING</i><code>&#34;</code> <i>keysym</i></dl>
<p> Keysyms are specified without the <code>XK_</code> prefix. </p>
<p> Strings may be direct text encoded in the locale for which the compose file is to be used, or an escaped octal or hexadecimal character code. Octal codes are specified as <code>&#34;\123&#34;</code> and hexadecimal codes as <code>&#34;:&#34;</code>. It is not necessary to specify in the right part of a rule a locale encoded string in addition to the keysym name. If the string is omitted, Xlib figures it out from the keysym according to the current locale. I.e., if a rule looks like:</p>
<dl COMPACT>
<dd><code>&lt;dead_grave&gt; &lt;A&gt; : &#34;\300&#34; Agrave</code></dl>
<p> the result of the composition is always the letter with the &quot;\300&quot; code. But if the rule is:</p>
<dl COMPACT>
<dd><code>&lt;dead_grave&gt; &lt;A&gt; : Agrave</code></dl>
<p> the result depends on how Agrave is mapped in the current locale.</p>
<h2>Environment</h2>
<dl COMPACT>
<dt><code>XCOMPOSEFILE</code></p>
<dd>File to use for compose sequences.</p>
<dt><code>XCOMPOSECACHE</code></p>
<dd>Directory to use for caching compiled compose files.</dl>
<h2>Files</h2>
<dl COMPACT>
<dt><i>$HOME/.XCompose</i></p>
<dd>User default compose file if XCOMPOSEFILE is not set.</p>
<dt><i>/usr/share/X11/locale/compose.dir</i></p>
<dd>File listing the compose file path to use for each locale.</p>
<dt><i>/usr/share/X11/locale/&lt;localemapping&gt;/Compose</i></p>
<dd>System default compose file for the locale, mapped via compose.dir.</p>
<dt><i>/var/cache/libx11/compose/</i></p>
<dd>System-wide cache directory for compiled compose files.</p>
<dt><i>$HOME/.compose-cache/</i></p>
<dd>Per-user cache directory for compiled compose files.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xlookupstring/">XLookupString</a></code>(3), <code><a href="/docs/linux/man/3-xmblookupstring/">XmbLookupString</a></code>(3), <code><a href="/docs/linux/man/3-xwclookupstring/">XwcLookupString</a></code>(3), <code><a href="/docs/linux/man/3-xutf8lookupstring/">Xutf8LookupString</a></code>(3), <code><a href="/docs/linux/man/1-mkcomposecache/">mkcomposecache</a></code>(1), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7).<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
