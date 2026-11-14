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
<dt><code>Wordview.Text.Background</code></p>
<dd> background color for main window</p>
<dt><code>Wordview.Text.Foreground</code></p>
<dd> Foreground color for main window</p>
<dt><code>Wordview.Text.selectBackground</code></p>
<dd> Background color of selected text</p>
<dt><code>Wordview.Text.selectForeground</code></p>
<dd> Foreground color of selected text</p>
<dt><code>Wordview.Text.Font</code></p>
<dd> Font to display text. We recommend to use fixed-width font, such as Courier, becouse <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1) is intended to convert Word into text. Either XLFD font names or Tk-style font specifications like <code>{Courier 12pt} </code> can be used for specifying font. If you use XLFD font names, usage of unicode (iso10646-1) fonts is recommended.</p>
<dt><code>Wordview.Text.findMode</code></p>
<dd> How to search text. This option can have value either <code>exact</code> or <code>regexp</code> and specifis whether text is searched for exact match or for regular expression by default. This behavoir can be toggled interactively via checkbox in the search dialog.</p>
<dt><code>Wordview.Text.findCase</code></p>
<dd> This boolean option controls whether search is case-sensitive. Default is no.</p>
<dt><code>Wordview.Menu.highlightBackground</code></p>
<dd> Background color for highlighted menu item</p>
<dt><code>Wordview.Menu.highlightThickness</code></p>
<dd>
<dt><code>Wordview.Menu.activeBackground</code></p>
<dd> Background color of active menu item.</p>
<dt><code>Wordview.Menu.activeBorderWidth</code></p>
<dd> Width (in pixels) of border around highlighted menu item. Default is 0, which differs from Tk global default. See <code><a href="/docs/linux/man/n-options/">options</a></code>(n) for more details.</dl>
<p> A lot of other resource options which affect behavoir of standard Tk widgets can affect wordview. See Tcl/Tk manual pages for more information. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-catdoc/">catdoc</a></code>(1),<code><a href="/docs/linux/man/1-wish/">wish</a></code>(1),<code><a href="/docs/linux/man/n-options/">options</a></code>(n) </p>
<h2>AUTHOR</h2>
<p> Victor Wagner &lt;vitus [at] 45.free.net&gt;. </p>
<h2>Index</h2>
