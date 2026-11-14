---
title: "clipit(1)"
name: "clipit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clipit/"
description: "ClipIt – Lightweight GTK+ Clipboard Manager"
---

<h2>NAME</h2>
<p> ClipIt &#8211; Lightweight GTK+ Clipboard Manager</p>
<h2>SYNOPSIS</h2>
<p> <code>clipit</code> [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ClipIt</code> is a lightweight GTK+ clipboard manager. </p>
<p> <code>ClipIt</code> features a clipboard CLI. Unrecognized options and the contents of your standard input get copied to your clipboard. See <code>CLI EXAMPLES</code>.</p>
<h2><code>OPTIONS</code></h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show help options.</p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd> Run as daemon. Use this mode if you just want <code>ClipIt</code> to keep your clipboard and primary contents safe.</p>
<dt><code>-n</code>, <code>&#8211;no-icon</code></p>
<dd> Do not use status icon.</p>
<dt><code>-c</code>, <code>&#8211;clipboard</code></p>
<dd> Print clipboard contents.</p>
<dt><code>-p</code>, <code>&#8211;primary</code></p>
<dd> Print primary contents.</dl>
<h2>NOTES</h2>
<h3>ACTIONS</h3>
<p> <code>ClipIt&#8217;s</code> actions perform commands using the contents of your clipboard. &quot;<code>%s</code>&quot; in the command is replaced with the clipboard contents.</p>
<h3>CLI EXAMPLES</h3>
<dl>
<dt>Put text in the clipboard</p>
<dd>
&nbsp;<wbr>echo&nbsp;<wbr>&quot;copied to clipboard&quot;&nbsp;<wbr>| clipit<br />
&nbsp;<wbr>clipit&nbsp;<wbr>&quot;copied to clipboard&quot;</p>
<dt>Put text in the clipboard and print the clipboard contents</p>
<dd>
&nbsp;<wbr>echo&nbsp;<wbr>&quot;copied to clipboard&quot;&nbsp;<wbr>| clipit -c</dl>
<h3>Hotkeys</h3>
<p>&nbsp;<wbr>The available hotkey modifiers are&nbsp;<wbr>&lt;Ctrl&gt;,&nbsp;<wbr>&lt;Alt&gt;&nbsp;<wbr>&lt;Shift&gt;,&nbsp;<wbr>&lt;Release&gt;,&nbsp;<wbr>&lt;Meta&gt;,&nbsp;<wbr>&lt;Super&gt;,&nbsp;<wbr>&lt;Hyper&gt;,&nbsp;<wbr>&lt;Mod[1-5]&gt;</p>
<h2>SEE ALSO</h2>
<p> Website: <a rel="nofollow" href="http://sourceforge.net/projects/gtkclipit/">http://sourceforge.net/projects/gtkclipit/</a></p>
<h2>AUTHOR</h2>
<p> Maintained by Cristian Henzel &lt;oss [at] rspwn.com&gt;. Forked from parcellite, which was written by Gilberto &quot;Xyhthyx&quot; Miralla &lt;xyhthyx [at] gmail.com&gt;. </p>
<h2>Index</h2>
