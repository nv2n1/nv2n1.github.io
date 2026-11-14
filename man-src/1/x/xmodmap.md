---
title: "xmodmap(1)"
name: "xmodmap"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmodmap/"
description: "xmodmap – utility for modifying keymaps and pointer button mappings in X"
---

<h2 class="name">NAME</h2>
<p> xmodmap &#8211; utility for modifying keymaps and pointer button mappings in X </p>
<h2>SYNOPSIS</h2>
<p> <code>xmodmap</code> [-options &#8230;] [filename]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xmodmap</i> program is used to edit and display the keyboard <i>modifier map</i> and <i>keymap table</i> that are used by client applications to convert event keycodes into keysyms. It is usually run from the user&#8217;s session startup script to configure the keyboard according to personal tastes.</p>
<h2>OPTIONS</h2>
<p> The following options may be used with <i>xmodmap</i>:</p>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This option specifies the host and display to use.</p>
<dt><code>-help</code></p>
<dd> This option indicates that a brief description of the command line arguments should be printed on the standard error channel. This will be done whenever an unhandled argument is given to <i>xmodmap.</i></p>
<dt><code>-grammar</code></p>
<dd> This option indicates that a help message describing the expression grammar used in files and with -e expressions should be printed on the standard error.</p>
<dt><code>-version</code></p>
<dd> This option indicates that <i>xmodmap</i> should print its version information and exit.</p>
<dt><code>-verbose</code></p>
<dd> This option indicates that <i>xmodmap</i> should print logging information as it parses its input.</p>
<dt><code>-quiet</code></p>
<dd> This option turns off the verbose logging. This is the default.</p>
<dt><code>-n</code></p>
<dd> This option indicates that <i>xmodmap</i> should not change the mappings, but should display what it would do, like <i><a href="/docs/linux/man/1-make/">make</a>(1)</i> does when given this option.</p>
<dt><code>-e </code><i>expression</i></p>
<dd> This option specifies an expression to be executed. Any number of expressions may be specified from the command line.</p>
<dt><code>-pm</code></p>
<dd> This option indicates that the current modifier map should be printed on the standard output. This is the default mode of operation if no other mode options are specified.</p>
<dt><code>-pk</code></p>
<dd> This option indicates that the current keymap table should be printed on the standard output.</p>
<dt><code>-pke</code></p>
<dd> This option indicates that the current keymap table should be printed on the standard output in the form of expressions that can be fed back to <i>xmodmap</i>.</p>
<dt><code>-pp</code></p>
<dd> This option indicates that the current pointer map should be printed on the standard output.</p>
<dt><code>&#8211;</code></p>
<dd> A lone dash means that the standard input should be used as the input file.</dl>
<p> The <i>filename</i> specifies a file containing <i>xmodmap</i> expressions to be executed. This file is usually kept in the user&#8217;s home directory with a name like <i>.xmodmaprc</i>.</p>
<h2>EXPRESSION GRAMMAR</h2>
<p> The <i>xmodmap</i> program reads a list of expressions and parses them all before attempting to execute any of them. This makes it possible to refer to keysyms that are being redefined in a natural way without having to worry as much about name conflicts. </p>
<p> The list of keysym names may be found in the header file <i>&lt;X11/keysymdef.h&gt;</i> (without the <i>XK_</i> prefix). Keysyms matching Unicode characters may be specified as &quot;U0020&quot; to &quot;U007E&quot; and &quot;U00A0&quot; to &quot;U10FFFF&quot; for all possible Unicode characters.</p>
<dl>
<dt><code>keycode </code><i>NUMBER</i> = <i>KEYSYMNAME &#8230;</i></p>
<dd> The list of keysyms is assigned to the indicated keycode (which may be specified in decimal, hex or octal and can be determined by running the <i>xev</i> program). Up to eight keysyms may be attached to a key, however the last four are not used in any major X server implementation. The first keysym is used when no modifier key is pressed in conjunction with this key, the second with Shift, the third when the Mode_switch key is used with this key and the fourth when both the Mode_switch and Shift keys are used.</p>
<dt><code>keycode any = </code><i>KEYSYMNAME &#8230;</i></p>
<dd> If no existing key has the specified list of keysyms assigned to it, a spare key on the keyboard is selected and the keysyms are assigned to it. The list of keysyms may be specified in decimal, hex or octal.</p>
<dt><code>keysym </code><i>KEYSYMNAME</i> = <i>KEYSYMNAME &#8230;</i></p>
<dd> The <i>KEYSYMNAME</i> on the left hand side is translated into matching keycodes used to perform the corresponding set of <code>keycode</code> expressions. Note that if the same keysym is bound to multiple keys, the expression is executed for each matching keycode.</p>
<dt><code>clear </code><i>MODIFIERNAME</i></p>
<dd> This removes all entries in the modifier map for the given modifier, where valid name are: <code>Shift</code>, <code>Lock</code>, <code>Control</code>, <code>Mod1</code>, <code>Mod2</code>, <code>Mod3</code>, <code>Mod4</code>, and <code>Mod5</code> (case does not matter in modifier names, although it does matter for all other names). For example, &#8220;clear Lock&#8221; will remove all any keys that were bound to the shift lock modifier.</p>
<dt><code>add </code><i>MODIFIERNAME</i> = <i>KEYSYMNAME &#8230;</i></p>
<dd> This adds all keys containing the given keysyms to the indicated modifier map. The keysym names are evaluated after all input expressions are read to make it easy to write expressions to swap keys (see the EXAMPLES section).</p>
<dt><code>remove </code><i>MODIFIERNAME</i> = <i>KEYSYMNAME &#8230;</i></p>
<dd> This removes all keys containing the given keysyms from the indicated modifier map. Unlike <code>add,</code> the keysym names are evaluated as the line is read in. This allows you to remove keys from a modifier without having to worry about whether or not they have been reassigned.</p>
<dt><code>pointer = default</code></p>
<dd> This sets the pointer map back to its default settings (button 1 generates a code of 1, button 2 generates a 2, etc.).</p>
<dt><code>pointer = </code><i>NUMBER &#8230;</i></p>
<dd> This sets the pointer map to contain the indicated button codes. The list always starts with the first physical button. Setting a button code to 0 disables events from that button.</dl>
<p> Lines that begin with an exclamation point (!) are taken as comments. </p>
<p> If you want to change the binding of a modifier key, you must also remove it from the appropriate modifier map.</p>
<h2>EXAMPLES</h2>
<p> Many pointers are designed such that the first button is pressed using the index finger of the right hand. People who are left-handed frequently find that it is more comfortable to reverse the button codes that get generated so that the primary button is pressed using the index finger of the left hand. This could be done on a 3 button pointer as follows: </p>
<pre>
%  xmodmap -e &quot;pointer = 3 2 1&quot;
</pre>
<p> Many applications support the notion of Meta keys (similar to Control keys except that Meta is held down instead of Control). However, some servers do not have a Meta keysym in the default keymap table, so one needs to be added by hand. The following command will attach Meta to the Multi-language key (sometimes labeled Compose Character). It also takes advantage of the fact that applications that need a Meta key simply need to get the keycode and don&#8217;t require the keysym to be in the first column of the keymap table. This means that applications that are looking for a Multi_key (including the default modifier map) won&#8217;t notice any change. </p>
<pre>
%  xmodmap -e &quot;keysym Multi_key = Multi_key Meta_L&quot;
</pre>
<p> Similarly, some keyboards have an Alt key but no Meta key. In that case the following may be useful: </p>
<pre>
%  xmodmap -e &quot;keysym Alt_L = Meta_L Alt_L&quot;
</pre>
<p> One of the more simple, yet convenient, uses of <i>xmodmap</i> is to set the keyboard&#8217;s &quot;rubout&quot; key to generate an alternate keysym. This frequently involves exchanging Backspace with Delete to be more comfortable to the user. If the <i>ttyModes</i> resource in <i>xterm</i> is set as well, all terminal emulator windows will use the same key for erasing characters: </p>
<pre>
%  xmodmap -e &quot;keysym BackSpace = Delete&quot;
%  echo &quot;XTerm*ttyModes:  erase ^?&quot; | xrdb -merge
</pre>
<p> Some keyboards do not automatically generate less than and greater than characters when the comma and period keys are shifted. This can be remedied with <i>xmodmap</i> by resetting the bindings for the comma and period with the following scripts: </p>
<pre>
!
! make shift-, be &lt; and shift-. be &gt;
!
keysym comma = comma less
keysym period = period greater
</pre>
<p> One of the more irritating differences between keyboards is the location of the Control and CapsLock keys. A common use of <i>xmodmap</i> is to swap these two keys as follows: </p>
<pre>
!
! Swap Caps_Lock and Control_L
!
remove Lock = Caps_Lock
remove Control = Control_L
keysym Control_L = Caps_Lock
keysym Caps_Lock = Control_L
add Lock = Caps_Lock
add Control = Control_L
</pre>
<p> This example can be run again to swap the keys back to their previous assignments. </p>
<p> The <i>keycode</i> command is useful for assigning the same keysym to multiple keycodes. Although unportable, it also makes it possible to write scripts that can reset the keyboard to a known state. The following script sets the backspace key to generate Delete (as shown above), flushes all existing caps lock bindings, makes the CapsLock key be a control key, make F5 generate Escape, and makes Break/Reset be a shift lock. </p>
<pre>
!
! On the HP, the following keycodes have key caps as listed:
!
!     101  Backspace
!      55  Caps
!      14  Ctrl
!      15  Break/Reset
!      86  Stop
!      89  F5
!
keycode 101 = Delete
keycode 55 = Control_R
clear Lock
add Control = Control_R
keycode 89 = Escape
keycode 15 = Caps_Lock
add Lock = Caps_Lock
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get default host and display number.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xev/">xev</a>(1), <a href="/docs/linux/man/1-setxkbmap/">setxkbmap</a>(1), <a href="/docs/linux/man/3-xstringtokeysym/">XStringToKeysym</a>(3), <i>Xlib</i> documentation on key and pointer events</p>
<h2>BUGS</h2>
<p> Every time a <code>keycode</code> expression is evaluated, the server generates a <i>MappingNotify</i> event on every client. This can cause some thrashing. All of the changes should be batched together and done at once. Clients that receive keyboard input and ignore <i>MappingNotify</i> events will not notice any changes made to keyboard mappings. </p>
<p> <i>Xmodmap</i> should generate &quot;add&quot; and &quot;remove&quot; expressions automatically whenever a keycode that is already bound to a modifier is changed. </p>
<p> There should be a way to have the <i>remove</i> expression accept keycodes as well as keysyms for those times when you really mess up your mappings.</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium, rewritten from an earlier version by David Rosenthal of Sun Microsystems. </p>
<h2>Index</h2>
