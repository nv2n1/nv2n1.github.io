---
title: "wordview(1)"
name: "wordview"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wordview/"
description: "wordview – displays text contained in MS-Word file in X window"
---

<h2>NAME</h2>
<p> wordview &#8211; displays text contained in MS-Word file in X window </p>
<h2>SYNOPSIS</h2>
<p> <code>wordview</code> [ <i>filename</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>wordview</code> is simple GUI wrapper around <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1) which allows to browse through word file interactively. It doesn&#8217;t allow to edit file, but allows to save plain text representation (or version with some TeX commands) into the file. </p>
<p> If for some reason <code>catdoc</code> doesn&#8217;t recognize file encoding properly, <code>wordview</code> allows to specify encoding interactively. </p>
<h2>OPTIONS</h2>
<p> <code>wordview</code> supports standard X options, supported by <code><a href="/docs/linux/man/1-wish/">wish</a></code>(1) </p>
<h2>X RESOURCES</h2>
<p> Following X resources can be used to customize <code>wordview</code>look: </p>
<dl>
<dt><code>Wordview.Text.Background</code></dt>
<dd> background color for main window</dd>
<dt><code>Wordview.Text.Foreground</code></dt>
<dd> Foreground color for main window</dd>
<dt><code>Wordview.Text.selectBackground</code></dt>
<dd> Background color of selected text</dd>
<dt><code>Wordview.Text.selectForeground</code></dt>
<dd> Foreground color of selected text</dd>
<dt><code>Wordview.Text.Font</code></dt>
<dd> Font to display text. We recommend to use fixed-width font, such as Courier, becouse <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1) is intended to convert Word into text. Either XLFD font names or Tk-style font specifications like <code>{Courier 12pt} </code> can be used for specifying font. If you use XLFD font names, usage of unicode (iso10646-1) fonts is recommended.</dd>
<dt><code>Wordview.Text.findMode</code></dt>
<dd> How to search text. This option can have value either <code>exact</code> or <code>regexp</code> and specifis whether text is searched for exact match or for regular expression by default. This behavoir can be toggled interactively via checkbox in the search dialog.</dd>
<dt><code>Wordview.Text.findCase</code></dt>
<dd> This boolean option controls whether search is case-sensitive. Default is no.</dd>
<dt><code>Wordview.Menu.highlightBackground</code></dt>
<dd> Background color for highlighted menu item</dd>
<dt><code>Wordview.Menu.highlightThickness</code></dt>
<dd>
</dd><dt><code>Wordview.Menu.activeBackground</code></dt>
<dd> Background color of active menu item.</dd>
<dt><code>Wordview.Menu.activeBorderWidth</code></dt>
<dd> Width (in pixels) of border around highlighted menu item. Default is 0, which differs from Tk global default. See <code>options</code>(n) for more details.</dd></dl>
<p> A lot of other resource options which affect behavoir of standard Tk widgets can affect wordview. See Tcl/Tk manual pages for more information. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1),<code><a href="/docs/linux/man/1-wish/">wish</a></code>(1),<code>options</code>(n) </p>
<h2>AUTHOR</h2>
<p> Victor Wagner &lt;vitus [at] 45.free.net&gt;. </p>
