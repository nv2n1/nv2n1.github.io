---
title: "evim(1)"
name: "evim"
section: "1"
letter: "e"
url: "/docs/linux/man/1-evim/"
description: "evim – easy Vim, edit a file with Vim and setup for modeless editing"
---

<h2 class="name">NAME</h2>
<p> evim &#8211; easy Vim, edit a file with Vim and setup for modeless editing </p>
<h2>SYNOPSIS</h2>
<p> <code>evim</code> [options] [file ..]<br />
 <code>eview</code></p>
<h2>DESCRIPTION</h2>
<p> <code>eVim</code> starts <code>Vim</code> and sets options to make it behave like a modeless editor. This is still Vim but used as a point-and-click editor. This feels a lot like using Notepad on MS-Windows. <code>eVim</code> will always run in the GUI, to enable the use of menus and toolbar. </p>
<p> Only to be used for people who really can&#8217;t work with Vim in the normal way. Editing will be much less efficient. </p>
<p> <code>eview</code> is the same, but starts in read-only mode. It works just like evim -R. </p>
<p> See <a href="/docs/linux/man/1-vim/">vim</a>(1) for details about Vim, options, etc. </p>
<p> The &#8216;insertmode&#8217; option is set to be able to type text directly.<br />
 Mappings are setup to make Copy and Paste work with the MS-Windows keys. CTRL-X cuts text, CTRL-C copies text and CTRL-V pastes text. Use CTRL-Q to obtain the original meaning of CTRL-V.</p>
<h2>OPTIONS</h2>
<p> See <a href="/docs/linux/man/1-vim/">vim</a>(1).</p>
<h2>FILES</h2>
<dl>
<dt>/usr/share/vim/vim81/evim.vim</p>
<dd> The script loaded to initialize eVim.</dl>
<h2>AKA</h2>
<p> Also Known As &quot;Vim for gumbies&quot;. When using evim you are expected to take a handkerchief, make a knot in each corner and wear it on your head.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-vim/">vim</a>(1)</p>
<h2>AUTHOR</h2>
<p> Most of <code>Vim</code> was made by Bram Moolenaar, with a lot of help from others. See the Help/Credits menu. </p>
<h2>Index</h2>
