---
title: "guake(1)"
name: "guake"
section: "1"
letter: "g"
url: "/docs/linux/man/1-guake/"
description: "guake — A drop-down terminal for GNOME environment."
---

<h2>NAME</h2>
<p> guake &#8212; A drop-down terminal for GNOME environment.</p>
<h2>SYNOPSIS</h2>
<p> <code>guake</code> [<code>-h, &#8211;help</code>] [<code>-p, &#8211;preferences</code>] [<code>-a, &#8211;about</code>] [<code>-q, &#8211;quit</code>] [<code>-f, &#8211;fullscreen</code>] [<code>-t, &#8211;toggle-visiblity</code>] [<code>&#8211;show</code>] [<code>&#8211;hide</code>] [<code>-s, &#8211;select-tab</code>] [<code>-g, &#8211;selected-tab</code>] [<code>-e, &#8211;execute-command</code>] [<code>-t, &#8211;tab-index</code>] [<code>&#8211;bgcolor</code>] [<code>&#8211;fgcolor</code>] [<code>-r, &#8211;rename-current-tab</code>]</p>
<h2>DESCRIPTION</h2>
<p> Guake is a drop-down terminal for GNOME and any other desktop. It aims to provide a quick-access terminal, that show/hide on screen with a simple key pressing. </p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code> Show summary of options.</p>
<dl>
<dt><code>-t, &#8211;toggle-visibility</code></dt>
<dd> Toggle the visibility of guake</dd>
<dt><code>&#8211;show</code></dt>
<dd> Display the main window</dd>
<dt><code>&#8211;hide</code></dt>
<dd> Hide the main window</dd>
<dt><code>-p, &#8211;preferences</code></dt>
<dd> Shows the preferences window of guake</dd>
<dt><code>-a, &#8211;about</code></dt>
<dd> Shows the about window of guake</dd>
<dt><code>-n, &#8211;new-tab</code></dt>
<dd> Create a new tab in Guake</dd>
<dt><code>-s, &#8211;select-tab</code></dt>
<dd> Select a tab given its 0-based index</dd>
<dt><code>-g, &#8211;selected-tab</code></dt>
<dd> Return the index of the current tab</dd>
<dt><code>-e, &#8211;execute-command</code></dt>
<dd> Execute a command in the selected tab</dd>
<dt><code>-i, &#8211;tab-index</code></dt>
<dd> Specify which tab to rename. Default is 0.</dd>
<dt><code>&#8211;bgcolor</code></dt>
<dd> Set the hexadecimal (#rrggbb) background color of the selected tab.</dd>
<dt><code>&#8211;fgcolor</code></dt>
<dd> Set the hexadecimal (#rrggbb) foreground color of the selected tab</dd>
<dt><code>&#8211;rename-tab</code></dt>
<dd> Rename the specified tab. Reset to default if TITLE is a single dash &quot;-&quot;.</dd>
<dt><code>-r, &#8211;rename-current-tab</code></dt>
<dd> Rename the current tab. Reset to default if TITLE is a single dash &quot;-&quot;.</dd>
<dt><code>-q, &#8211;quit</code></dt>
<dd> Closes the current running guake</dd></dl>
<h2>AUTHOR</h2>
<p> guake was originally written by &lt;gabriel [at] guake-terminal.org&gt; </p>
<p> This manual page was written by Gabriel Falcao Goncalves de Moura &lt;gabriel [at] guake-terminal.org&gt;, for the Debian project (but may be used by others). </p>
