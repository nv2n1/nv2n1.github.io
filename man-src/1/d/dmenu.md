---
title: "dmenu(1)"
name: "dmenu"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmenu/"
description: "dmenu – dynamic menu"
---

<h2>NAME</h2>
<p> dmenu &#8211; dynamic menu</p>
<h2>SYNOPSIS</h2>
<p> <code>dmenu</code> [<code>-bfiv</code>] [<code>-l</code> <i>lines</i>] [<code>-m</code> <i>monitor</i>] [<code>-p</code> <i>prompt</i>] [<code>-fn</code> <i>font</i>] [<code>-nb</code> <i>color</i>] [<code>-nf</code> <i>color</i>] [<code>-sb</code> <i>color</i>] [<code>-sf</code> <i>color</i>] [<code>-w</code> <i>windowid</i>] </p>
<p> <code>dmenu_run</code> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>dmenu</code> is a dynamic menu for X, which reads a list of newline-separated items from stdin. When the user selects an item and presses Return, their choice is printed to stdout and dmenu terminates. Entering text will narrow the items to those matching the tokens in the input. </p>
<p> <code>dmenu_run</code> is a script used by <i><a href="/docs/linux/man/1-dwm/">dwm</a></i>(1) which lists programs in the user&#8217;s $PATH and runs the result in their $SHELL.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> dmenu appears at the bottom of the screen.</p>
<dt><code>-f</code></p>
<dd> dmenu grabs the keyboard before reading stdin. This is faster, but will lock up X until stdin reaches end-of-file.</p>
<dt><code>-i</code></p>
<dd> dmenu matches menu items case insensitively.</p>
<dt><code>-l</code><i> lines</i></p>
<dd> dmenu lists items vertically, with the given number of lines.</p>
<dt><code>-m</code><i> monitor</i></p>
<dd> dmenu is displayed on the monitor number supplied. Monitor numbers are starting from 0.</p>
<dt><code>-p</code><i> prompt</i></p>
<dd> defines the prompt to be displayed to the left of the input field.</p>
<dt><code>-fn</code><i> font</i></p>
<dd> defines the font or font set used.</p>
<dt><code>-nb</code><i> color</i></p>
<dd> defines the normal background color. <i>#RGB</i>, <i>#RRGGBB</i>, and X color names are supported.</p>
<dt><code>-nf</code><i> color</i></p>
<dd> defines the normal foreground color.</p>
<dt><code>-sb</code><i> color</i></p>
<dd> defines the selected background color.</p>
<dt><code>-sf</code><i> color</i></p>
<dd> defines the selected foreground color.</p>
<dt><code>-v</code></p>
<dd> prints version information to stdout, then exits.</p>
<dt><code>-w</code><i> windowid</i></p>
<dd> embed into windowid.</dl>
<h2>USAGE</h2>
<p> dmenu is completely controlled by the keyboard. Items are selected using the arrow keys, page up, page down, home, and end.</p>
<dl>
<dt><code>Tab</code></p>
<dd> Copy the selected item to the input field.</p>
<dt><code>Return</code></p>
<dd> Confirm selection. Prints the selected item to stdout and exits, returning success.</p>
<dt><code>Ctrl-Return</code></p>
<dd> Confirm selection. Prints the selected item to stdout and continues.</p>
<dt><code>Shift-Return</code></p>
<dd> Confirm input. Prints the input text to stdout and exits, returning success.</p>
<dt><code>Escape</code></p>
<dd> Exit without selecting an item, returning failure.</p>
<dt>C-a</p>
<dd> Home</p>
<dt>C-b</p>
<dd> Left</p>
<dt>C-c</p>
<dd> Escape</p>
<dt>C-d</p>
<dd> Delete</p>
<dt>C-e</p>
<dd> End</p>
<dt>C-f</p>
<dd> Right</p>
<dt>C-g</p>
<dd> Escape</p>
<dt>C-h</p>
<dd> Backspace</p>
<dt>C-i</p>
<dd> Tab</p>
<dt>C-j</p>
<dd> Return</p>
<dt>C-J</p>
<dd> Shift-Return</p>
<dt>C-k</p>
<dd> Delete line right</p>
<dt>C-m</p>
<dd> Return</p>
<dt>C-M</p>
<dd> Shift-Return</p>
<dt>C-n</p>
<dd> Down</p>
<dt>C-p</p>
<dd> Up</p>
<dt>C-u</p>
<dd> Delete line left</p>
<dt>C-w</p>
<dd> Delete word left</p>
<dt>C-y</p>
<dd> Paste from primary X selection</p>
<dt>C-Y</p>
<dd> Paste from X clipboard</p>
<dt>M-g</p>
<dd> Home</p>
<dt>M-G</p>
<dd> End</p>
<dt>M-h</p>
<dd> Up</p>
<dt>M-j</p>
<dd> Page down</p>
<dt>M-k</p>
<dd> Page up</p>
<dt>M-l</p>
<dd> Down</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dwm/">dwm</a></i>(1), <i><a href="/docs/linux/man/1-stest/">stest</a></i>(1) </p>
<h2>Index</h2>
