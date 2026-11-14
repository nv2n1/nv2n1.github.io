---
title: "ttmkfdir(1)"
name: "ttmkfdir"
section: "1"
letter: "t"
url: "/docs/linux/man/1-ttmkfdir/"
description: "ttmkfdir – Utility to create fonts.scale files for truetype fonts"
---

<h2>NAME</h2>
<p> <code>ttmkfdir</code>&nbsp;<wbr>&#8211; Utility to create fonts.scale files for truetype fonts</p>
<h2>SYNOPSIS</h2>
<p> <code>ttmkfdir</code> [OPTION]</p>
<h2>DESCRIPTION</h2>
<p>&nbsp;<wbr>Originally written by Joerg Pommnitz, ttmkfdir is a tool to create valid and complete fonts.scale file from TrueType fonts. It is very useful when you plan to use a TrueType enabled font server that is based on the X11R6 sample implementation&nbsp;<wbr>(xfsft for instance). Great care has been taken to correctly identify the encodings that a given TrueType font supports. </p>
<p> The ttmkfdir comes with Red Hat Linux has experienced quite some modifications or improvements, include: </p>
<p> &#8211; migration to FreeType 2 library</p>
<dl>
<dt>&#8211; more accurate checking for big font files</p>
<dd>
<dt>&#8211; support for both two X core font backends, Freetype and XTT</p>
<dd>
<dt>&#8211; Truetype collection(ttc) font file support</p>
<dd>
<dt>&#8211; additional CJK friendly features</p>
<dd>
<dt>&#8211; bug fixes</p>
<dd>
<p>&nbsp;<wbr></dl>
<h2>OPTIONS</h2>
<p> Here is the detailed usage of Red Hat version of ttmkfdir.</p>
<dl>
<dt><code>-h, &#8211;help </code></p>
<dd> It shows the menus and combo box in iok UI</p>
<dt><code>-e, &#8211;encoding &lt;encodings.dir&gt;</code></p>
<dd> ttmkfdir is doing its job by checking each TrueType font file against fontenc layer, please refer <a rel="nofollow" href="http://www.xfree86.org">www.xfree86.org</a>/current/fonts.html for details. Default encodings.dir file is /usr/X11R6/lib/X11/fonts/encodings/encodings.dir</p>
<dt><code>-o, &#8211;output</code></p>
<dd> Specify output, default is fonts.scale in the current directory</p>
<dt><code>-d, &#8211;font-dir</code></p>
<dd> Specify TrueType font directory, default is the current directory</p>
<dt><code>-f, &#8211;default-foundry</code></p>
<dd> Specify name of the default font foundry, default is &quot;misc&quot;</p>
<dt><code>-m, &#8211;max-missing</code></p>
<dd> Specify the maximum number of missing characters per encoding, default is 5. This option applies to the encoding that has less than 256 codepoint definitions.</p>
<dt><code>-a, &#8211;max-missing-percentage</code></p>
<dd> Specify the maximum percentage of missing characters per encoding, default is 2. This option applies to the encoding that has more than 256 codepoint definitions.</p>
<dt><code>-b, &#8211;font-backend</code></p>
<dd> For X FreeType backend, use value &quot;1&quot;, for XTT backend use value &quot;2&quot;, default value is 1. When you have TrueType Collection font(.ttc), you need to use this option.</p>
<dt><code>-x, &#8211;additional-entries</code></p>
<dd> Additional entries mean those extra TTCaps stuff for XTT backend, mainly for bold and italic font support. Or for FreeType backend, because FreeType still doesn&#8217;t support bold and italic font, ttmkfdir can generate extra &quot;dummy&quot; XLFDs, so applications who asking those fonts won&#8217;t complain. </p>
<p> Default value is &quot;0&quot; means off,otherwise use &quot;1&quot; to switch it on.</p>
<dt><code>-c, &#8211;completeness</code></p>
<dd> use less strict completeness tests for encoding tables</p>
<dt><code>-p, &#8211;panose</code></p>
<dd> use panose information </p>
</dl>
<h2>AUTHOR</h2>
<p> Yu Shao &lt;yshao [at] redhat.com&gt; and Pravin Satpute &lt;psatpute [at] redhat.com&gt; </p>
<h2>LICENSE</h2>
<p> GNU Library General Public License </p>
<h2>Index</h2>
