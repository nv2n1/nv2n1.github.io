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
<p> <code>dmenu</code> [<code>-bfiv</code>] [<code>-l</code> <i>lines</i>] [<code>-m</code> <i>monitor</i>] [<code>-p</code> <i>prompt</i>] [<code>-fn</code> <i>font</i>] [<code>-nb</code> <i>color</i>] [<code>-nf</code> <i>color</i>] [<code>-sb</code> <i>color</i>] [<code>-sf</code> <i>color</i>] [<code>-w</code> <i>windowid</i>] </p>
<p> <code>dmenu_run</code> &#8230;</p>
<p> <code>dmenu</code> is a dynamic menu for X, which reads a list of newline-separated items from stdin. When the user selects an item and presses Return, their choice is printed to stdout and dmenu terminates. Entering text will narrow the items to those matching the tokens in the input. </p>
<p> <code>dmenu_run</code> is a script used by <i>dwm</i>(1) which lists programs in the user&#8217;s $PATH and runs the result in their $SHELL.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> dmenu appears at the bottom of the screen.</dd>
<dt><code>-f</code></dt>
<dd> dmenu grabs the keyboard before reading stdin. This is faster, but will lock up X until stdin reaches end-of-file.</dd>
<dt><code>-i</code></dt>
<dd> dmenu matches menu items case insensitively.</dd>
<dt><code>-l</code><i> lines</i></dt>
<dd> dmenu lists items vertically, with the given number of lines.</dd>
<dt><code>-m</code><i> monitor</i></dt>
<dd> dmenu is displayed on the monitor number supplied. Monitor numbers are starting from 0.</dd>
<dt><code>-p</code><i> prompt</i></dt>
<dd> defines the prompt to be displayed to the left of the input field.</dd>
<dt><code>-fn</code><i> font</i></dt>
<dd> defines the font or font set used.</dd>
<dt><code>-nb</code><i> color</i></dt>
<dd> defines the normal background color. <i>#RGB</i>, <i>#RRGGBB</i>, and X color names are supported.</dd>
<dt><code>-nf</code><i> color</i></dt>
<dd> defines the normal foreground color.</dd>
<dt><code>-sb</code><i> color</i></dt>
<dd> defines the selected background color.</dd>
<dt><code>-sf</code><i> color</i></dt>
<dd> defines the selected foreground color.</dd>
<dt><code>-v</code></dt>
<dd> prints version information to stdout, then exits.</dd>
<dt><code>-w</code><i> windowid</i></dt>
<dd> embed into windowid.</dd></dl>
<h2>USAGE</h2>
<p> dmenu is completely controlled by the keyboard. Items are selected using the arrow keys, page up, page down, home, and end.</p>
<dl>
<dt><code>Tab</code></dt>
<dd> Copy the selected item to the input field.</dd>
<dt><code>Return</code></dt>
<dd> Confirm selection. Prints the selected item to stdout and exits, returning success.</dd>
<dt><code>Ctrl-Return</code></dt>
<dd> Confirm selection. Prints the selected item to stdout and continues.</dd>
<dt><code>Shift-Return</code></dt>
<dd> Confirm input. Prints the input text to stdout and exits, returning success.</dd>
<dt><code>Escape</code></dt>
<dd> Exit without selecting an item, returning failure.</dd>
<dt>C-a</dt>
<dd> Home</dd>
<dt>C-b</dt>
<dd> Left</dd>
<dt>C-c</dt>
<dd> Escape</dd>
<dt>C-d</dt>
<dd> Delete</dd>
<dt>C-e</dt>
<dd> End</dd>
<dt>C-f</dt>
<dd> Right</dd>
<dt>C-g</dt>
<dd> Escape</dd>
<dt>C-h</dt>
<dd> Backspace</dd>
<dt>C-i</dt>
<dd> Tab</dd>
<dt>C-j</dt>
<dd> Return</dd>
<dt>C-J</dt>
<dd> Shift-Return</dd>
<dt>C-k</dt>
<dd> Delete line right</dd>
<dt>C-m</dt>
<dd> Return</dd>
<dt>C-M</dt>
<dd> Shift-Return</dd>
<dt>C-n</dt>
<dd> Down</dd>
<dt>C-p</dt>
<dd> Up</dd>
<dt>C-u</dt>
<dd> Delete line left</dd>
<dt>C-w</dt>
<dd> Delete word left</dd>
<dt>C-y</dt>
<dd> Paste from primary X selection</dd>
<dt>C-Y</dt>
<dd> Paste from X clipboard</dd>
<dt>M-g</dt>
<dd> Home</dd>
<dt>M-G</dt>
<dd> End</dd>
<dt>M-h</dt>
<dd> Up</dd>
<dt>M-j</dt>
<dd> Page down</dd>
<dt>M-k</dt>
<dd> Page up</dd>
<dt>M-l</dt>
<dd> Down</dd></dl>
<h2>SEE ALSO</h2>
<p> <i>dwm</i>(1), <i><a href="/docs/linux/man/1-stest/">stest</a></i>(1) </p>
