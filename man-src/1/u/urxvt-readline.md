---
title: "urxvt-readline(1)"
name: "urxvt-readline"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt-readline/"
---

<h2 class="name">NAME</h2>
 

 readline - improve readline editing (enabled by default) 

<h2>DESCRIPTION</h2>

 A support package that tries to make editing with readline easier. At the moment, it reacts to clicking shift-left mouse button by trying to move the text cursor to this position. It does so by generating as many cursor-left or cursor-right keypresses as required (this only works for programs that correctly support wide characters). 

 To avoid too many false positives, this is only done when:
<dl>
<dt>- the tty is in <font SIZE="-1">ICANON</font> state.
<dd>
<dt>- the text cursor is visible.
<dd>
<dt>- the primary screen is currently being displayed.
<dd>
<dt>- the mouse is on the same (multi-row-) line as the text cursor.
<dd></dl>
 

 The normal selection mechanism isn't disabled, so quick successive clicks might interfere with selection creation in harmless ways. 

<h2>Index</h2>


