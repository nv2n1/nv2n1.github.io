---
title: "dzen2(1)"
name: "dzen2"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dzen2/"
description: "dzen2 – general-purpose messaging and notification for X11"
---

<h2>NAME</h2>
<p> dzen2 &#8211; general-purpose messaging and notification for X11</p>
<h2>SYNOPSIS</h2>
<p> <code>dzen2</code> [-v] [-p [seconds]] [-m [v|h]] [-ta &lt;l|c|r&gt;] [-sa &lt;l|c|r&gt;]<br />
[-x&nbsp;<wbr>&lt;pixel&gt;]&nbsp;<wbr>[-y&nbsp;<wbr>&lt;pixel&gt;]&nbsp;<wbr>[-w&nbsp;<wbr>&lt;pixel&gt;]&nbsp;<wbr>[-tw&nbsp;<wbr>&lt;pixel&gt;]&nbsp;<wbr>[-u]&nbsp;<wbr><br />
[-e&nbsp;<wbr>&lt;string&gt;]&nbsp;<wbr>[-l&nbsp;<wbr>&lt;lines&gt;]&nbsp;<wbr>&nbsp;<wbr>[-fn&nbsp;<wbr>&lt;font&gt;]&nbsp;<wbr>[-bg&nbsp;<wbr>&lt;color&gt;]<br />
[-fg&nbsp;<wbr>&lt;color&gt;]&nbsp;<wbr>[-xs&nbsp;<wbr>&lt;screen&gt;]</p>
<h2>DESCRIPTION</h2>
<p> <code>Dzen</code> is a general-purpose messaging and notification program for X11, desigend to be scriptable in any language and integrate well with window managers like dwm, wmii and xmonad though it will work with any windowmanger. </p>
<p> <code>Dzen</code> expects the status message on its standard input, and uses a custom formatting language for colors and several other features (like bar meters and such). See README for detailed usage and scripting instructions.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-fg &lt;color&gt;</code></p>
<dd> Set foreground color. The &lt;color&gt; can be specified either as symbolic name (e.g. red, darkgreen, etc.) or as #rrggbb hex-value (e.g. #ffffaa).</p>
<dt><code>-bg &lt;color&gt;</code></p>
<dd> Set background color (same format as -fg).</p>
<dt><code>-fn &lt;font&gt;</code></p>
<dd> Set font (using the format of xlsfonts and xfontsel).</p>
<dt><code>-ta &lt;l|c|r&gt;</code></p>
<dd> Set alignement of title window content: l(eft), c(center) or r(ight).</p>
<dt><code>-tw &lt;pixels&gt;</code></p>
<dd> Set title window width.</p>
<dt><code>-sa &lt;l|c|r&gt;</code></p>
<dd> Set alignment of slave window (see <code>-ta</code> ).</p>
<dt><code>-l &lt;lines&gt;</code></p>
<dd> Number of lines to display in slave window (see (1) in README).</p>
<dt><code>-e &lt;event1=action1:option1:&#8230;,action2;event2=&#8230;&gt;</code></p>
<dd> Set up events and actions, eg. responses to mouse clicks (see (2) in README).</p>
<dt><code>-m</code></p>
<dd> Start up in menu mode (see (3) in README).</p>
<dt><code>-u</code></p>
<dd> Update contents of title and slave window simultaneously, see (see (4) in README).</p>
<dt><code>-p [&lt;timeout&gt;]</code></p>
<dd> Persist EOF (optional timeout in seconds).</p>
<dt><code>-x &lt;pixels&gt;</code></p>
<dd> Set x position on the screen.</p>
<dt><code>-y &lt;pixels&gt;</code></p>
<dd> Set y position on the screen.</p>
<dt><code>-h &lt;pixels&gt;</code></p>
<dd> Set line height (defaults to fontheight + 2 pixels).</p>
<dt><code>-w &lt;pixels&gt;</code></p>
<dd> width</p>
<dt><code>-xs &lt;n&gt;</code></p>
<dd> Set the Xinerama screen number where dzen should appear.</p>
<dt><code>-v</code></p>
<dd> Display version information. </p>
</dl>
<h2>SEE ALSO</h2>
<p> More detailed documentation (especially on the formatting language of dzen2) is available in /usr/share/doc/dzen2/README.gz. </p>
<h2>AUTHOR</h2>
<p> <code>Dzen2</code> has been written by <code>Robert Manea.</code> This manpage has been written, based on dzen documentation, by Petr Ročkai, for Debian GNU/Linux, but may be used by others. This manpage falls under the same licence as Dzen2 itself, see /usr/share/doc/dzen2/copyright. </p>
<h2>Index</h2>
