---
title: "fvwmconsolec-pl(1)"
name: "fvwmconsolec-pl"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmconsolec-pl/"
description: "FvwmConsoleC.pl – Command editor for fvwm command input interface"
---

<p>FvwmConsoleC.pl &#8211; Command editor for fvwm command input interface </p>
<h2>Synopsis</h2>
<p>FvwmConsole -e /usr/X11/lib/fvwm/FvwmConsoleC.pl </p>
<h2>Copyright</h2>
<p>Copyright 1996, Toshi Isogai. No guarantees or warranties are provided. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact. </p>
<h2>Description</h2>
<p>FvwmConsoleC.pl offers editing capabilities while the user is entering the line. By default, the line editing commands are similar to those of emacs. It also offers <code>substitution</code> , which replaces a pattern to a string before it sends the command. </p>
<h2>Functions</h2>
<p>Functions are bound to a key or key combination to be invoked. The followings are functions available and their default key bindings.</p>
<dl>
<dd>
<dl>
<dt><code>bind</code></p>
<dd><i>Meta-k, Ctrl-x Ctrl-b</i><br />
 List up key bindings and substitutions.</p>
<dt><code>boh</code></p>
<dd>Move to the beginning of history.</p>
<dt><code>boh_ign_mode</code> <i>Esc-&lt;</i></p>
<dd>Move to the beginning of history. If it is in search mode, continue.</p>
<dt><code>bol</code></p>
<dd><i>Home, Ctrl-a</i><br />
 Move cursor to the beginning of the line.</p>
<dt><code>bs[(n)]</code> <i>BackSpace, Ctrl-h</i></p>
<dd>Backspace n times. default of n is 1.</p>
<dt><code>cancel</code></p>
<dd><i>Ctrl-x Ctrl-k</i><br />
 Cancel the current input.</p>
<dt><code>del_back_line</code></p>
<dd>Delete the line from the beginning to the cursor.</p>
<dt><code>del_back_word</code> <i>Ctrl-w</i></p>
<dd>Delete the word from the beginning to the cursor.</p>
<dt><code>del_char [(n)]</code> <i>Delete, Ctrl-d</i></p>
<dd>Delete n characters from the cursor to the right. Default of n is 1.</p>
<dt><code>del_forw_line</code> <i>Ctrl-k</i></p>
<dd>Delete the line from the cursor to the end.</p>
<dt><code>del_forw_word</code> <i>Meta-d</i></p>
<dd>Delete the word from the cursor to the end.</p>
<dt><code>del_line</code> <i>Ctrl-u</i></p>
<dd>Delete the entire line.</p>
<dt><code>enter</code></p>
<dd><i>Enter, Ctrl-j, Ctrl-m</i><br />
 Perform substitution if applicable and send the line to fvwm.</p>
<dt><code>enter_wo_subst</code> <i>Meta-Enter</i></p>
<dd>Send the line to fvwm without any substitution.</p>
<dt><code>eoh</code></p>
<dd>Move to the end of history.</p>
<dt><code>eoh_ign_mode</code> <i>Esc-&gt;</i></p>
<dd>Move to the end of history. If it is in search mode, continue.</p>
<dt><code>eol</code></p>
<dd><i>End, Ctrl-e</i><br />
 Move the cursor to the end of line.</p>
<dt><code>ins_char (str)</code></p>
<dd>Insert string at the cursor.</p>
<dt><code>ins_last_word</code> <i>Esc-.</i></p>
<dd>Insert the last argument of the previous command at the cursor.</p>
<dt><code>ins_nth_word</code> <i>Meta-[1..9]</i></p>
<dd>Insert the n-th argument of the previous command at the cursor.</p>
<dt><code>list_func</code> <i>Meta-l</i></p>
<dd>List up available editing functions.</p>
<dt><code>next_char</code> <i>Right, Ctrl-f</i></p>
<dd>Move the cursor to the next character.</p>
<dt><code>next_line</code> <i>Down, Ctrl-n</i></p>
<dd>Move to the next line in history.</p>
<dt><code>next_word</code> <i>Meta-f</i></p>
<dd>Move the cursor to the next word.</p>
<dt><code>prefix</code></p>
<dd>Wait for the next character typed in for multi-key binding.</p>
<dt><code>prev_char</code> <i>Left, Ctrl-b</i></p>
<dd>Move the cursor to the previous character.</p>
<dt><code>prev_line</code> <i>Up, Ctrl-p</i></p>
<dd>Move to the previous line in history.</p>
<dt><code>prev_word</code> <i>Meta-b</i></p>
<dd>Move the cursor to the previous word.</p>
<dt><code>quote</code></p>
<dd><i>Ctrl-q</i><br />
 Insert the next character typed into the buffer literally.</p>
<dt><code>search</code></p>
<dd><i>Ctrl-s</i><br />
 Search pattern in history.</p>
<dt><code>search_rev</code> <i>Ctrl-r</i></p>
<dd>Search pattern in history in reverse order.</p>
<dt><code>subst</code></p>
<dd><i>Meta-s</i><br />
 Substitute all patterns to strings and reprint the line. The substitutions are not nested and performed in the order that they are defined.</dl>
</dl>
<h2>Configuration</h2>
<p>The key binding can be overridden or defined in fvwm module configuration. </p>
<dl>
<dd>*FvwmConsole: Key 
