---
title: "ibus-emoji(7)"
name: "ibus-emoji"
section: "7"
letter: "i"
url: "/docs/linux/man/7-ibus-emoji/"
description: "ibus-emoji – Call the IBus emoji utility by IBus Emojier"
---

<p><code>ibus-emoji</code> &#8211; Call the IBus emoji utility by <code>IBus Emojier</code></p>
<h2>Synopsis</h2>
<p><code>/usr/libexec/ibus-ui-emojier</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>IBus Emojier provides a GUI to select an emoji by typing an emoji annotation or choosing a character with mouse click and it&#8217;s designed to work as an extended IBus lookup window using Space, Enter, and Arrow keys. The text entry accepts an emoji annotation or Unicode points. If IBus panel is launched, IBus panel calls IBus Emojier with a shortcut key or the right click menu and output the selected emoji on the previous focused text on an application. If IBus panel is not available likes GNOME desktop, You can still use <code>ibus emoji</code> command to launch IBus Emojier and it saves the selected emoji in your clipboard and you can paste the emoji by a paste key likes Control-v. Refer <code>emoji</code> section in <code>ibus (1)</code> for the command line options. Homepage: <a rel="nofollow" href="https://github.com/ibus/ibus/wiki">https://github.com/ibus/ibus/wiki</a> </p>
<h2>Settings</h2>
<dl>
<dt><code>ANNOTATION LANGUAGE</code></p>
<dd>You can choose a language of emoji annotations with <code>ibus-setup (1).</code></p>
<dt><code>FONT</code></p>
<dd>You can choose an emoji font with <code>ibus-setup (1).</code> E.g. &quot;Noto Color Emoji&quot;, &quot;Android Emoji&quot; font. </p>
</dl>
<h2>Keyboard Operations</h2>
<dl>
<dt><code>Control-Period or Control-Semicolon</code></p>
<dd>Launch IBus Emojier. The shortcut key can be customized by <code>ibus-setup (1).</code></p>
<dt><code>Left, Right arrow, Control-b or Control-f</code></p>
<dd>Select the next left or right category or emoji on the list if an annotation is not typed. Otherwise move the cursor to the immdediate left or right in the typed annotation.</p>
<dt><code>Down, Up arrow, Control-n or Control-p</code></p>
<dd>Select the next top or down category or emoji on the list</p>
<dt><code>Enter</code></p>
<dd>Commit the selected emoji.</p>
<dt><code>Escape</code></p>
<dd>Go back to the category list from emoji list, erase the typed annotation, and close IBus Emojier.</p>
<dt><code>Space</code></p>
<dd>Select the next left category or emoji on the list. If Shift-Space is typed, a space chararacter can be inserted between words in an annotation or Unicode points. E.g. 1f466 Shift-Space 1f3fb</p>
<dt><code>PageDown, PageUp, Control-Shift-n or Control-Shift-p</code></p>
<dd>Move to the next or previous page in the category or emoji list.</p>
<dt><code>Head, End, Control-h or Control-e</code></p>
<dd>Select the first or last emoji on the list if an annotation is not typed. Otherwise move the cursor to the head or end in the typed annotation.</p>
<dt><code>Control-u</code></p>
<dd>Erase the typed annotation.</p>
<dt><code>Control-x or Control-v or Control-c</code></p>
<dd>Cut the selected annotation to the clipboard with Control-x. Paste the contents of the clipboard into the annotation entry with Control-v. Copy the selected annotation to the clipboard with Control-c.</p>
<dt><code>Control-Shift-c</code></p>
<dd>Copy the selected emoji to the clipboard. </p>
</dl>
<h2>Bugs</h2>
<p>If you find a bug, please report it at <a rel="nofollow" href="https://github.com/ibus/ibus/issues">https://github.com/ibus/ibus/issues</a> </p>
