---
title: "setxkbmap(1)"
name: "setxkbmap"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setxkbmap/"
description: "setxkbmap – set the keyboard using the X Keyboard Extension"
---

<h2 class="name">NAME</h2>
<p> setxkbmap &#8211; set the keyboard using the X Keyboard Extension </p>
<h2>SYNOPSIS</h2>
<p> <code>setxkbmap [</code> <i>args</i> <code>] [</code> <i>layout</i> <code>[</code> <i>variant</i> <code>[</code> <i>option &#8230;</i> <code>] ] ]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>setxkbmap</code> command maps the keyboard to use the layout determined by the options specified on the command line. </p>
<p> An XKB keymap is constructed from a number of components which are compiled only as needed. The source for all of the components can be found in <i>/usr/share/X11/xkb</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-compat </code><i>name</i></p>
<dd> Specifies the name of the compatibility map component used to construct a keyboard layout.</p>
<dt><code>-config </code><i>file</i></p>
<dd> Specifies the name of an XKB configuration file which describes the keyboard to be used.</p>
<dt><code>-device </code><i>device</i></p>
<dd> Specifies the numeric device id of the input device to be updated with the new keyboard layout. If not specified, the core keyboard device of the X server is updated.</p>
<dt><code>-display </code><i>display</i></p>
<dd> Specifies the display to be updated with the new keyboard layout.</p>
<dt><code>-geometry </code><i>name</i></p>
<dd> Specifies the name of the geometry component used to construct a keyboard layout.</p>
<dt><code>-help</code></p>
<dd> Prints a message describing the valid input to <i>setxkbmap</i>.</p>
<dt><code>-I </code><i>directory</i></p>
<dd> Adds a directory to the list of directories to be used to search for specified layout or rules files.</p>
<dt><code>-keycodes </code><i>name</i></p>
<dd> Specifies the name of the keycodes component used to construct a keyboard layout.</p>
<dt><code>-keymap </code><i>name</i></p>
<dd> Specifies the name of the keymap description used to construct a keyboard layout.</p>
<dt><code>-layout </code><i>name</i></p>
<dd> Specifies the name of the layout used to determine the components which make up the keyboard description. The <i>-layout</i> option may only be used once. Multiple layouts can be specified as a comma-separated list.</p>
<dt><code>-model </code><i>name</i></p>
<dd> Specifies the name of the keyboard model used to determine the components which make up the keyboard description. Only one model may be specified on the command line.</p>
<dt><code>-option </code><i>name</i></p>
<dd> Specifies the name of an option to determine the components which make up the keyboard description; multiple options may be specified, one per <i>-option</i> flag. Note that <code>setxkbmap</code> adds options specified in the command line to the options that were set before (as saved in root window properties). If you want to replace all previously specified options, use the <i>-option</i> flag with an empty argument first.</p>
<dt><code>-print</code></p>
<dd> With this option <code>setxkbmap</code> just prints component names in a format acceptable by <code>xkbcomp</code> (an XKB keymap compiler) and exits. The option can be used for tests instead of a verbose option and in cases when one needs to run both the <code>setxkbmap</code> and the <code>xkbcomp</code> in chain (see below).</p>
<dt><code>-query</code></p>
<dd> With this option <code>setxkbmap</code> just prints the current rules, model, layout, variant, and options, then exits.</p>
<dt><code>-rules </code><i>file</i></p>
<dd> Specifies the name of the rules file used to resolve the requested layout and model to a set of component names.</p>
<dt><code>-symbols </code><i>name</i></p>
<dd> Specifies the name of the symbols component used to construct a keyboard layout.</p>
<dt><code>-synch</code></p>
<dd> Force synchronization for X requests.</p>
<dt><code>-types </code><i>name</i></p>
<dd> Specifies the name of the types component used to construct a keyboard layout.</p>
<dt><code>-variant </code><i>name</i></p>
<dd> Specifies which variant of the keyboard layout should be used to determine the components which make up the keyboard description. The <i>-variant</i> option may only be used once. Multiple variants can be specified as a comma-separated list and will be matched with the layouts specified with <i>-layout</i>.</p>
<dt><code>-verbose|-v [</code><i>level</i>]</p>
<dd> Specifies level of verbosity in output messages. Valid levels range from 0 (least verbose) to 10 (most verbose). The default verbosity level is 5. If no level is specified, each <i>-v</i> or <i>-verbose</i> flag raises the level by 1.</p>
<dt><code>-version</code></p>
<dd> Prints the program&#8217;s version number.</dl>
<h2>USING WITH xkbcomp</h2>
<p> If you have an Xserver and a client shell running on different computers and some XKB configuration files on those machines are different, you can get problems specifying a keyboard map by model, layout, and options names. This is because <code>setxkbmap</code> converts its arguments to names of XKB configuration files according to files that are on the client-side computer, then sends these file names to the server where <code>xkbcomp</code> has to compose a complete keyboard map using files which the server has. Thus if the sets of files differ in some way, the names that <code>setxkbmap</code> generates can be unacceptable on the server side. You can solve this problem by running the <code>xkbcomp</code> on the client side too. With the <i>-print</i> option <code>setxkbmap</code> just prints the file names in an appropriate format to its stdout and this output can be piped directly to the <code>xkbcomp</code> input. For example, the command </p>
<p> <code>setxkbmap us -print | xkbcomp &#8211; $DISPLAY</code> </p>
<p> makes both steps run on the same (client) machine and loads a keyboard map into the server.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xkbcomp/">xkbcomp</a>(1), <a href="/docs/linux/man/7-xkeyboard-config/">xkeyboard-config</a>(7)</p>
<h2>FILES</h2>
<p> <i>/usr/share/X11/xkb</i> </p>
<h2>Index</h2>
