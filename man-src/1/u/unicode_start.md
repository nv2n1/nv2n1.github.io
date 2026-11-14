---
title: "unicode_start(1)"
name: "unicode_start"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unicode_start/"
description: "unicode_start – put keyboard and console in unicode mode"
---

<h2 class="name">NAME</h2>
<p> unicode_start &#8211; put keyboard and console in unicode mode </p>
<h2>SYNOPSIS</h2>
<p> <code>unicode_start</code> [<i>font</i> [<i>umap</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>unicode_start</code> command will put the keyboard and console into Unicode (UTF-8) mode. </p>
<p> For the keyboard this means that one can attach 16-bit U+xxxx values to keyboard keys using <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), and have these appear as UTF-8 input to user programs. Also, that one can type hexadecimal Alt-xxxx using the numeric keypad, and again produce UTF-8. </p>
<p> For the console this means that the kernel expects UTF-8 output from user programs, and displays the output accordingly. </p>
<p> The parameter <i>font</i> is a font that is loaded. It should have a built-in Unicode map, or, if it hasn&#8217;t, such a map can be given explicitly as second parameter. When no font was specified, the current font is kept.</p>
<h2>NOTE</h2>
<p> Unicode mode is a parameter with a value per virtual console. However, usually the font and keymap is common to all consoles.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1), <code><a href="/docs/linux/man/1-kbd_mode/">kbd_mode</a></code>(1), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/1-unicode_stop/">unicode_stop</a></code>(1), <code><a href="/docs/linux/man/7-utf-8/">utf-8</a></code>(7), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8) </p>
<h2>Index</h2>
