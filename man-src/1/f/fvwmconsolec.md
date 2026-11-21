---
title: "fvwmconsolec(1)"
name: "fvwmconsolec"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmconsolec/"
description: "FvwmConsoleC.pl – Command editor for fvwm command input interface"
---
<h2>SYNOPSIS</h2>
<p> FvwmConsole -e /usr/X11/lib/fvwm/FvwmConsoleC.pl </p>
<h2>COPYRIGHT</h2>
<p> Copyright 1996, Toshi Isogai. No guarantees or warranties are provided. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact. </p>
<h2>DESCRIPTION</h2>
<p> FvwmConsoleC.pl offers editing capabilities while the user is entering the line. By default, the line editing commands are similar to those of emacs. It also offers <code>substitution</code> , which replaces a pattern to a string before it sends the command. </p>
<h2>FUNCTIONS</h2>
<p> Functions are bound to a key or key combination to be invoked. The followings are functions available and their default key bindings. </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>bind</code></dt>
<dd> <p> <i>Meta-k, Ctrl-x Ctrl-b</i> <br />
 List up key bindings and substitutions. </p>
 </dd>
<dt><code>boh</code></dt>
<dd> <p> <br />
 Move to the beginning of history. </p>
 </dd>
<dt><code>boh_ign_mode</code><i>Esc-&lt;</i></dt>
<dd> <p> <br />
 Move to the beginning of history. If it is in search mode, continue. </p>
 </dd>
<dt><code>bol</code></dt>
<dd> <p> <i>Home, Ctrl-a</i> <br />
 Move cursor to the beginning of the line. </p>
 </dd>
<dt><code>bs[(n)]</code><i>BackSpace, Ctrl-h</i></dt>
<dd> <p> <br />
 Backspace n times. default of n is 1. </p>
 </dd>
<dt><code>cancel</code></dt>
<dd> <p> <i>Ctrl-x Ctrl-k</i> <br />
 Cancel the current input. </p>
 </dd>
<dt><code>del_back_line</code></dt>
<dd> <p> <br />
 Delete the line from the beginning to the cursor. </p>
 </dd>
<dt><code>del_back_word</code><i>Ctrl-w</i></dt>
<dd> <p> <br />
 Delete the word from the beginning to the cursor. </p>
 </dd>
<dt><code>del_char [(n)]</code><i>Delete, Ctrl-d</i></dt>
<dd> <p> Delete n characters from the cursor to the right. Default of n is 1. </p>
 </dd>
<dt><code>del_forw_line</code><i>Ctrl-k</i></dt>
<dd> <p> <br />
 Delete the line from the cursor to the end. </p>
 </dd>
<dt><code>del_forw_word</code><i>Meta-d</i></dt>
<dd> <p> <br />
 Delete the word from the cursor to the end. </p>
 </dd>
<dt><code>del_line</code><i>Ctrl-u</i></dt>
<dd> <p> <br />
 Delete the entire line. </p>
 </dd>
<dt><code>enter</code></dt>
<dd> <p> <i>Enter, Ctrl-j, Ctrl-m</i> <br />
 Perform substitution if applicable and send the line to fvwm. </p>
 </dd>
<dt><code>enter_wo_subst</code><i>Meta-Enter</i></dt>
<dd> <p> <br />
 Send the line to fvwm without any substitution. </p>
 </dd>
<dt><code>eoh</code></dt>
<dd> <p> <br />
 Move to the end of history. </p>
 </dd>
<dt><code>eoh_ign_mode</code><i>Esc-&gt;</i></dt>
<dd> <p> <br />
 Move to the end of history. If it is in search mode, continue. </p>
 </dd>
<dt><code>eol</code></dt>
<dd> <p> <i>End, Ctrl-e</i> <br />
 Move the cursor to the end of line. </p>
 </dd>
<dt><code>ins_char (str)</code></dt>
<dd> <p> <br />
 Insert string at the cursor. </p>
 </dd>
<dt><code>ins_last_word</code><i>Esc-.</i></dt>
<dd> <p> <br />
 Insert the last argument of the previous command at the cursor. </p>
 </dd>
<dt><code>ins_nth_word</code><i>Meta-[1..9]</i></dt>
<dd> <p> <br />
 Insert the n-th argument of the previous command at the cursor. </p>
 </dd>
<dt><code>list_func</code><i>Meta-l</i></dt>
<dd> <p> <br />
 List up available editing functions. </p>
 </dd>
<dt><code>next_char</code><i>Right, Ctrl-f</i></dt>
<dd> <p> <br />
 Move the cursor to the next character. </p>
 </dd>
<dt><code>next_line</code><i>Down, Ctrl-n</i></dt>
<dd> <p> <br />
 Move to the next line in history. </p>
 </dd>
<dt><code>next_word</code><i>Meta-f</i></dt>
<dd> <p> <br />
 Move the cursor to the next word. </p>
 </dd>
<dt><code>prefix</code></dt>
<dd> <p> <br />
 Wait for the next character typed in for multi-key binding. </p>
 </dd>
<dt><code>prev_char</code><i>Left, Ctrl-b</i></dt>
<dd> <p> <br />
 Move the cursor to the previous character. </p>
 </dd>
<dt><code>prev_line</code><i>Up, Ctrl-p</i></dt>
<dd> <p> <br />
 Move to the previous line in history. </p>
 </dd>
<dt><code>prev_word</code><i>Meta-b</i></dt>
<dd> <p> <br />
 Move the cursor to the previous word. </p>
 </dd>
<dt><code>quote</code></dt>
<dd> <p> <i>Ctrl-q</i> <br />
 Insert the next character typed into the buffer literally. </p>
 </dd>
<dt><code>search</code></dt>
<dd> <p> <i>Ctrl-s</i> <br />
 Search pattern in history. </p>
 </dd>
<dt><code>search_rev</code><i>Ctrl-r</i></dt>
<dd> <p> <br />
 Search pattern in history in reverse order. </p>
 </dd>
<dt><code>subst</code></dt>
<dd> <p> <i>Meta-s</i> <br />
 Substitute all patterns to strings and reprint the line. The substitutions are not nested and performed in the order that they are defined. </p>
 </dd></dl>
</dl>
<h2>CONFIGURATION</h2>
<p> The key binding can be overridden or defined in fvwm module configuration. </p>
<dl>
<dd> <p> *FvwmConsole: Key \ck prev_line </p>
 </dd></dl>
<p>Non-space character sequence need not be quoted. In order to undefine, omit the last argument. </p>
<dl>
<dd> <p> *FvwmConsole: Key \ck </p>
 </dd></dl>
<p>Note that non-meta character is case sensitive. \c means control key, \e means escape, and \m is alt key. <br />
 It also accepts Subst configuration. Users often input long fvwm command repeatedly. Subst will replace particular input sequence to user defined string. Example: </p>
<dl>
<dd> <p> *FvwmConsole: Subst &#8216;^bigx&#8217; &#8216;Exec xterm -g 120x60+0+0 -fn 10x20 -fg black -bg lemonchiffon&#8217; </p>
 </dd></dl>
<p>Typing &#8216;bigx&lt;return&gt;&#8216; in FvwmConsole will launch xterm. &#8216;^&#8216; denotes the beginning of line in <code>regular expression.</code> &#8216;pl&#8217; in the middle of the command will not be replaced. Although the format looks different, it takes Perl regular expression. It just uses single or double quote as the delimiter. Single or double quotes have no difference, although they have to match, and cannot include itself in the string. </p>
<dl>
<dd> <p> *FvwmConsole: Subst &#8216;^g\s*(\d+)&#8216; &#8216;Desk 0 0\nGotoPage 0 $1\nFocus&#8217; </p>
 </dd></dl>
<p>Entering &#8216;g4&#8217; or &#8216;g 4&#8217; will jump to desk 0 page 0 4 and focus. </p>
<h2>INVOCATION</h2>
<p> FvwmConsoleC.pl should be invoked by FvwmConsole. </p>
<h2>SEE ALSO</h2>
<p> FvwmConsole(1x), <a href="/docs/linux/man/1-perlre/">perlre</a>(1) </p>
<h2>AUTHOR</h2>
<p> Toshi Isogai </p>
