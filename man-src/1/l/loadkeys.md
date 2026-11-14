---
title: "loadkeys(1)"
name: "loadkeys"
section: "1"
letter: "l"
url: "/docs/linux/man/1-loadkeys/"
description: "loadkeys – load keyboard translation tables"
---

<h2 class="name">NAME</h2>
<p> loadkeys &#8211; load keyboard translation tables </p>
<h2>SYNOPSIS</h2>
<p> <code>loadkeys</code> [ <i>-a &#8211;ascii</i> ] [ <i>-b &#8211;bkeymap</i> ] [ <i>-c &#8211;clearcompose</i> ] [ <i>-C &#8216;&lt;FILE&gt;&#8217;</i> | <i>&#8211;console=&lt;FILE&gt;</i> ] [ <i>-d &#8211;default</i> ] [ <i>-h &#8211;help</i> ] [ <i>-m &#8211;mktable</i> ] [ <i>-p &#8211;parse</i> ] [ <i>-q &#8211;quiet</i> ] [ <i>-s &#8211;clearstrings</i> ] [ <i>-u &#8211;unicode</i> ] [ <i>-v &#8211;verbose</i> ] [ <i>-V &#8211;version</i> ] [ <i>filename&#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The program <code>loadkeys</code> reads the file or files specified by <i>filename&#8230;</i>. Its main purpose is to load the kernel keymap for the console. You can specify console device by the <i>-C</i> (or <i>&#8211;console</i> ) option.</p>
<h2>RESET TO DEFAULT</h2>
<p> If the <i>-d</i> (or <i>&#8211;default</i> ) option is given, <code>loadkeys</code> loads a default keymap, probably the file <i>defkeymap.map</i> either in <i>/usr/share/keymaps</i> or in <i>/usr/src/linux/drivers/char</i>. (Probably the former was user-defined, while the latter is a qwerty keyboard map for PCs &#8211; maybe not what was desired.) Sometimes, with a strange keymap loaded (with the minus on some obscure unknown modifier combination) it is easier to type `loadkeys defkeymap&#8217;.</p>
<h2>LOAD KERNEL KEYMAP</h2>
<p> The main function of <code>loadkeys</code> is to load or modify the keyboard driver&#8217;s translation tables. When specifying the file names, standard input can be denoted by dash (-). If no file is specified, the data is read from the standard input. </p>
<p> For many countries and keyboard types appropriate keymaps are available already, and a command like `loadkeys uk&#8217; might do what you want. On the other hand, it is easy to construct one&#8217;s own keymap. The user has to tell what symbols belong to each key. She can find the keycode for a key by use of <code><a href="/docs/linux/man/1-showkey/">showkey</a></code>(1), while the keymap format is given in <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5) and can also be seen from the output of <code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1).</p>
<h2>LOAD KERNEL ACCENT TABLE</h2>
<p> If the input file does not contain any compose key definitions, the kernel accent table is left unchanged, unless the <i>-c</i> (or <i>&#8211;clearcompose</i> ) option is given, in which case the kernel accent table is emptied. If the input file does contain compose key definitions, then all old definitions are removed, and replaced by the specified new entries. The kernel accent table is a sequence of (by default 68) entries describing how dead diacritical signs and compose keys behave. For example, a line </p>
<dl>
<dt>
<dd> compose &#8216;,&#8217; &#8216;c&#8217; to ccedilla</dl>
<p> means that &lt;ComposeKey&gt;&lt;,&gt;&lt;c&gt; must be combined to &lt;ccedilla&gt;. The current content of this table can be see using `dumpkeys &#8211;compose-only&#8217;.</p>
<h2>LOAD KERNEL STRING TABLE</h2>
<p> The option <i>-s</i> (or <i>&#8211;clearstrings</i> ) clears the kernel string table. If this option is not given, <code>loadkeys</code> will only add or replace strings, not remove them. (Thus, the option -s is required to reach a well-defined state.) The kernel string table is a sequence of strings with names like F31. One can make function key F5 (on an ordinary PC keyboard) produce the text `Hello!&#8217;, and Shift+F5 `Goodbye!&#8217; using lines </p>
<dl>
<dt>
<dd> keycode 63 = F70 F71<br />
 string F70 = &quot;Hello!&quot;<br />
 string F71 = &quot;Goodbye!&quot;</dl>
<p> in the keymap. The default bindings for the function keys are certain escape sequences mostly inspired by the VT100 terminal.</p>
<h2>CREATE KERNEL SOURCE TABLE</h2>
<p> If the <i>-m</i> (or <i>&#8211;mktable</i> ) option is given <code>loadkeys</code> prints to the standard output a file that may be used as <i>/usr/src/linux/drivers/char/defkeymap.c,</i> specifying the default key bindings for a kernel (and does not modify the current keymap).</p>
<h2>CREATE BINARY KEYMAP</h2>
<p> If the <i>-b</i> (or <i>&#8211;bkeymap</i> ) option is given <code>loadkeys</code> prints to the standard output a file that may be used as a binary keymap as expected by Busybox <code>loadkmap</code> command (and does not modify the current keymap).</p>
<h2>UNICODE MODE</h2>
<p> <code>loadkeys</code> automatically detects whether the console is in Unicode or ASCII (XLATE) mode. When a keymap is loaded, literal keysyms (such as <code>section</code>) are resolved accordingly; numerical keysyms are converted to fit the current console mode, regardless of the way they are specified (decimal, octal, hexadecimal or Unicode). </p>
<p> The <i>-u</i> (or <i>&#8211;unicode</i>) switch forces <code>loadkeys</code> to convert all keymaps to Unicode. If the keyboard is in a non-Unicode mode, such as XLATE, <code>loadkeys</code> will change it to Unicode for the time of its execution. A warning message will be printed in this case. </p>
<p> It is recommended to run <code><a href="/docs/linux/man/1-kbd_mode/">kbd_mode</a></code>(1) before <code>loadkeys</code> instead of using the <i>-u</i> option.</p>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>-a &#8211;ascii</code></p>
<dd> Force conversion to ASCII.</p>
<dt><code>-h &#8211;help</code></p>
<dd> <code>loadkeys</code> prints its version number and a short usage message to the programs standard error output and exits.</p>
<dt><code>-p &#8211;parse</code></p>
<dd> <code>loadkeys</code> searches and parses keymap without action.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> <code>loadkeys</code> suppresses all normal output.</p>
<dt><code>-V &#8211;version</code></p>
<dd> <code>loadkeys</code> prints version number and exits.</dl>
<h2>WARNING</h2>
<p> Note that anyone having read access to <code>/dev/console</code> can run <code>loadkeys</code> and thus change the keyboard layout, possibly making it unusable. Note that the keyboard translation table is common for all the virtual consoles, so any changes to the keyboard bindings affect all the virtual consoles simultaneously. </p>
<p> Note that because the changes affect all the virtual consoles, they also outlive your session. This means that even at the login prompt the key bindings may not be what the user expects.</p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/keymaps</i></p>
<dd> default directory for keymaps.</dl>
<dl>
<dt><i>/usr/src/linux/drivers/char/defkeymap.map</i></p>
<dd> default kernel keymap.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1), <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5) </p>
<h2>Index</h2>
