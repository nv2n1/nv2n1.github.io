---
title: "key-mon(1)"
name: "key-mon"
section: "1"
letter: "k"
url: "/docs/linux/man/1-key-mon/"
description: "Keymon – Keyboard and mouse monitor window for GTK."
---

<h2>NAME</h2>
<p> Keymon &#8211; Keyboard and mouse monitor window for GTK.</p>
<h2>SYNOPSIS</h2>
<p> <code>key-mon [options]</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-s</code>, <code>&#8211;smaller</code></p>
<dd> Make the dialog 25% smaller than normal.</p>
<dt><code>-l</code>, <code>&#8211;larger</code></p>
<dd> Make the dialog 25% larger than normal.</p>
<dt><code>-m</code>, <code>&#8211;meta</code></p>
<dd> Show the meta (windows) key.</p>
<dt><code>&#8211;nometa</code></p>
<dd> Opposite of <code>&#8211;meta</code></p>
<dt><code>&#8211;mouse</code></p>
<dd> Show the mouse.</p>
<dt><code>&#8211;nomouse</code></p>
<dd> Opposite of <code>&#8211;mouse</code></p>
<dt><code>&#8211;shift</code></p>
<dd> Show shift key.</p>
<dt><code>&#8211;noshift</code></p>
<dd> Opposite of <code>&#8211;shift</code></p>
<dt><code>&#8211;ctrl</code></p>
<dd> Show the ctrl key.</p>
<dt><code>&#8211;noctrl</code></p>
<dd> Opposite of <code>&#8211;ctrl</code></p>
<dt><code>&#8211;alt</code></p>
<dd> Show the alt key.</p>
<dt><code>&#8211;noalt</code></p>
<dd> Opposite of <code>&#8211;alt</code></p>
<dt><code>&#8211;scale</code>=<i>SCALE</i></p>
<dd> Scale the dialog. ex. 2.0 is 2 times larger, 0.5 is half the size. Defaults to 1.0</p>
<dt><code>&#8211;key-timeout</code>=<i>KEY_TIMEOUT</i></p>
<dd> Timeout before key returns to unpressed image. Defaults to 0.5</p>
<dt><code>&#8211;mouse-timeout</code>=<i>MOUSE_TIMEOUT</i></p>
<dd> Timeout before mouse returns to unpressed image. Defaults to 0.2</p>
<dt><code>&#8211;visible-click-timeout</code>=<i>VISIBLE_CLICK_TIMEOUT</i></p>
<dd> Timeout before highly visible click disappears. Defaults to 0.2</p>
<dt><code>&#8211;decorated</code></p>
<dd> Show decoration</p>
<dt><code>&#8211;nodecorated</code></p>
<dd> Opposite of <code>&#8211;decorated</code></p>
<dt><code>&#8211;backgroundless</code></p>
<dd> Show only buttons</p>
<dt><code>&#8211;nobackgroundless</code></p>
<dd> Opposite of <code>&#8211;backgroundless</code></p>
<dt><code>&#8211;no-press-fadeout</code>=<i>NO_PRESS_FADEOUT</i></p>
<dd> Fadeout the window after a period with no key press. Defaults to 0.0 seconds (Experimental)</p>
<dt><code>&#8211;only_combo</code></p>
<dd> Show only key combos (ex. Control-A)</p>
<dt><code>&#8211;noonly_combo</code></p>
<dd> Opposite of <code>&#8211;only_combo</code></p>
<dt><code>&#8211;sticky</code></p>
<dd> Sticky mode</p>
<dt><code>&#8211;nosticky</code></p>
<dd> Opposite of <code>&#8211;sticky</code></p>
<dt><code>&#8211;visible_click</code></p>
<dd> Show where you clicked</p>
<dt><code>&#8211;novisible_click</code></p>
<dd> Opposite of <code>&#8211;visible_click</code></p>
<dt><code>&#8211;follow_mouse</code></p>
<dd> Show the mouse more visibly</p>
<dt><code>&#8211;nofollow_mouse</code></p>
<dd> Opposite of <code>&#8211;follow_mouse</code></p>
<dt><code>&#8211;kbdfile</code>=<i>KBD_FILE</i></p>
<dd> Use this kbd filename.</p>
<dt><code>&#8211;swap</code></p>
<dd> Swap the mouse buttons.</p>
<dt><code>&#8211;noswap</code></p>
<dd> Opposite of <code>&#8211;swap</code></p>
<dt><code>&#8211;emulate-middle</code></p>
<dd> When you press the left, and right mouse buttons at the same time, it displays as a middle mouse button click.</p>
<dt><code>&#8211;noemulate-middle</code></p>
<dd> Opposite of <code>&#8211;emulate-middle</code></p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Show version information and exit.</p>
<dt><code>-t</code> THEME, <code>&#8211;theme</code>=<i>THEME</i></p>
<dd> The theme to use when drawing status images (ex. &quot;-t apple&quot;).</p>
<dt><code>&#8211;list-themes</code></p>
<dd> List available themes</p>
<dt><code>&#8211;old-keys</code>=<i>OLD_KEYS</i></p>
<dd> How many historical keypresses to show (defaults to 0)</p>
<dt><code>&#8211;reset</code></p>
<dd> Reset all options to their defaults.</p>
<dt><code>&#8211;opacity</code>=<i>OPACITY</i></p>
<dd> Opacity of window</p>
<dt><code>&#8211;loglevel</code>=<i>LOGLEVEL</i></p>
<dd> Logging level</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Output debugging information. Shorthand for <code>&#8211;loglevel</code>=<i>debug</i></p>
<dt><code>&#8211;screenshot</code>=<i>SCREENSHOT</i></p>
<dd> Create a &quot;screenshot.png&quot; and exit. Pass a comma separated list of keys to simulate(ex. &quot;KEY_A,KEY_LEFTCTRL&quot;).</dl>
<h2>DESCRIPTON</h2>
<p> <code>Keymon</code> is a program to help in teaching or podcasting by showing the current status of the mouse buttons and keyboard. </p>
<p> <code>Keymon</code> creates a small, borderless window which always stays topmost and monitors the keystrokes and mouse buttons used at any time in any program. </p>
<p> Configuration files are saved in ~/.config/key-mon/.</p>
<h2>AUTHOR</h2>
<p> Written by Scott Kirkwood (scott+keymon [at] forusers.com)</p>
<h2>SEE ALSO</h2>
<p> Full documentation for <code>keymon</code> is available at</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://code.google.com/p/key-mon">http://code.google.com/p/key-mon</a></code></dl>
<p> Send bugs to</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://code.google.com/p/key-mon/issues/list">http://code.google.com/p/key-mon/issues/list</a></code></dl>
<h2>Index</h2>
