---
title: "vimtutor(1)"
name: "vimtutor"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vimtutor/"
description: "vimtutor – the Vim tutor"
---

<h2 class="name">NAME</h2>
<p> vimtutor &#8211; the Vim tutor </p>
<h2>SYNOPSIS</h2>
<p> <code>vimtutor [-g] [language]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Vimtutor</code> starts the <code>Vim</code> tutor. It copies the tutor file first, so that it can be modified without changing the original file. </p>
<p> The <code>Vimtutor</code> is useful for people that want to learn their first <code>Vim</code> commands. </p>
<p> The optional argument -g starts vimtutor with gvim rather than vim, if the GUI version of vim is available, or falls back to Vim if gvim is not found. </p>
<p> The optional [language] argument is the two-letter name of a language, like &quot;it&quot; or &quot;es&quot;. If the [language] argument is missing, the language of the current locale will be used. If a tutor in this language is available, it will be used. Otherwise the English version will be used. </p>
<p> <code>Vim</code> is always started in Vi compatible mode.</p>
<h2>FILES</h2>
<dl>
<dt>/usr/share/vim/vim81/tutor/tutor[.language]</p>
<dd> The <code>Vimtutor</code> text file(s).</p>
<dt>/usr/share/vim/vim81/tutor/tutor.vim</p>
<dd> The Vim script used to copy the <code>Vimtutor</code> text file.</dl>
<h2>AUTHOR</h2>
<p> The <code>Vimtutor</code> was originally written for Vi by Michael C. Pierce and Robert K. Ware, Colorado School of Mines using ideas supplied by Charles Smith, Colorado State University. E-mail: bware [at] mines.colorado.edu.<br />
 It was modified for <code>Vim</code> by Bram Moolenaar. For the names of the translators see the tutor files.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-vim/">vim</a>(1) </p>
<h2>Index</h2>
