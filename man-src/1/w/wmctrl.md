---
title: "wmctrl(1)"
name: "wmctrl"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmctrl/"
description: "wmctrl – interact with a EWMH/NetWM compatible X Window Manager."
---

<h2 class="name">NAME</h2>
<p> wmctrl &#8211; interact with a EWMH/NetWM compatible X Window Manager. </p>
<h2>SYNOPSIS</h2>
<p> <code>wmctrl</code> [<i> options </i>|<i> actions </i>]<i>&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>wmctrl</code> is a command that can be used to interact with an X Window manager that is compatible with the EWMH/NetWM specification. <code>wmctrl</code> can query the window manager for information, and it can request that certain window management actions be taken. </p>
<p> <code>wmctrl</code> is controlled entirely by its command line arguments. The command line arguments are used to specify the action to be performed (with options that modify behavior) and any arguments that might be needed to perform the actions. </p>
<p> The following sections define the supported actions and options. Arguments to the actions and options are written in the form <i>&lt;ARGNAME&gt;</i> in the descriptions below. The detailed syntax for writing arguments are in a single section dedicated to that purpose. </p>
<h2>ACTIONS</h2>
<p> The following command line arguments can be specified to invoke a <code>wmctrl</code> action. Only one action can be executed with the invocation of the <code>wmctrl</code> command. </p>
<dl>
<dt><code>-a</code><i> &lt;WIN&gt;</i></p>
<dd> Switch to the desktop containing the window <i>&lt;WIN&gt;</i>, raise the window, and give it focus. </p>
<dt><code>-b ( add | remove | toggle),</code><i>prop1</i><code> [,</code><i>prop2</i><code> ]</code></p>
<dd> Add, remove, or toggle up to two window properties simultaneously. The window that is being modified must be identified with a <code>-r </code> action. The property change is achived by using the EWMH _NET_WM_STATE request. The supported property names (for <i>prop1</i> and <i>prop2</i>) are <code>modal</code>, <code>sticky</code>, <code>maximized_vert</code>, <code>maximized_horz</code>, <code>shaded</code>, <code>skip_taskbar</code>, <code>skip_pager</code>, <code>hidden</code>, <code>fullscreen</code>, <code>above</code> and <code>below</code>. Two properties are supported to allow operations like maximizing a window to full screen mode. Note that this action is made up of exactly two shell command line arguments. </p>
<dt><code>-c</code><i> &lt;WIN&gt;</i></p>
<dd> Close the window <i>&lt;WIN&gt;</i> gracefully. </p>
<dt><code>-d</code></p>
<dd> List all desktops managed by the window manager. One line is output for each desktop, with the line broken up into space separated columns. The first column contains an integer desktop number. The second column contains a &#8216;*&#8217; character for the current desktop, otherwise it contains a &#8216;-&#8216; character. The next two columns contain the fixed string <code>DG:</code> and then the desktop geometry as &#8216;<i>&lt;width&gt;</i>x<i>&lt;height&gt;</i>&#8216; (<i>e.g.</i> &#8216;1280&#215;1024&#8217;). The following two columns contain the fixed string <code>VP:</code> and then the viewport position in the format &#8216;<i>&lt;y&gt;</i>,<i>&lt;y&gt;</i>&#8216; (<i>e.g.</i> &#8216;0,0&#8217;). The next three columns after this contains the fixed string <code>WA:</code> and then two columns with the workarea geometry as &#8216;<i>X</i>,<i>Y</i> and <i>W</i>x<i>H</i>&#8216; (<i>e.g.</i> &#8216;0,0 1280&#215;998&#8217;). The rest of the line contains the name of the desktop (possibly containing multiple spaces). </p>
<dt><code>-e</code><i> &lt;MVARG&gt;</i></p>
<dd> Resize and move a window that has been specified with a <code>-r</code> action according to the <i>&lt;MVARG&gt;</i> argument. </p>
<dt><code>-g</code><i> w</i><code>,</code><i>h</i></p>
<dd> Change the geometry (common size) of all desktops so they are <i>w</i> pixels wide and <i>h</i> pixels high. <i>w</i> and <i>h</i> must be positive integers. A window manager may ignore this request. </p>
<dt><code>-h</code></p>
<dd> Print help text about program usage. </p>
<dt><code>-I</code><i> name</i></p>
<dd> Set the icon name (short title) of the window specified by a <code>-r</code> action to <i>name</i>. </p>
<dt><code>-k ( on | off )</code></p>
<dd> Turn on or off the window manager&#8217;s &quot;show the desktop&quot; mode (if the window manager implements this feature). </p>
<dt><code>-l</code></p>
<dd> List the windows being managed by the window manager. One line is output for each window, with the line broken up into space separated columns. The first column always contains the window identity as a hexadecimal integer, and the second column always contains the desktop number (a -1 is used to identify a sticky window). If the <code>-p</code> option is specified the next column will contain the PID for the window as a decimal integer. If the <code>-G</code> option is specified then four integer columns will follow: x-offset, y-offset, width and height. The next column always contains the client machine name. The remainder of the line contains the window title (possibly with multiple spaces in the title). </p>
<dt><code>-m</code></p>
<dd> Display information about the window manager and the environment. </p>
<dt><code>-n</code><i> N</i></p>
<dd> Change the number of desktops to <i>N</i> (a non-negative integer). </p>
<dt><code>-N</code><i> name</i></p>
<dd> Set the name (long title) of the window specified by a <code>-r</code> action to <i>name</i>. </p>
<dt><code>-o</code><i> x</i><code>,</code><i>y</i></p>
<dd> Change the viewport for the current desktop. The values <i>x</i> and <i>y</i> are numeric offsets that specify the position of the top left corner of the viewport. A window manager may ignore this request. </p>
<dt><code>-r</code><i> &lt;WIN&gt;</i></p>
<dd> Specify a target window for an action. </p>
<dt><code>-R</code><i> &lt;WIN&gt;</i></p>
<dd> Move the window <i>&lt;WIN&gt;</i> to the current desktop, raise the window, and give it focus. </p>
<dt><code>-s</code><i> &lt;DESK&gt;</i></p>
<dd> Switch to the desktop <i>&lt;DESK&gt;</i>. </p>
<dt><code>-t</code><i> &lt;DESK&gt;</i></p>
<dd> Move a window that has been specified with the <code>-r</code> action to the desktop <i>&lt;DESK&gt;</i>. </p>
<dt><code>-T</code><i> name</i></p>
<dd> Set the both the name (long title) and icon name (short title) of the window specified by a <code>-r</code> action to <i>name</i>. This action is like using the <code>-N</code> and <code>-I</code> actions at the same time (which would otherwise be impossible since <code>wmctrl</code> can execute only one action at a time). </p>
</dl>
<h2>OPTIONS</h2>
<p> The following options modify the default actions, or they modify the interpretation of arguments. </p>
<dl>
<dt><code>-F</code></p>
<dd> Window name arguments (<i>&lt;WIN&gt;</i>) are to be treated as exact window titles that are case sensitive. Without this options window titles are considered to be case insensitive substrings of the full window title. </p>
<dt><code>-G</code></p>
<dd> Include geometry information in the output of the <code>-l</code> action. </p>
<dt><code>-i</code></p>
<dd> Interpret window arguments (<i>&lt;WIN&gt;</i>) as a numeric value rather than a string name for the window. If the numeric value starts with the prefix &#8216;0x&#8217; it is assumed to be a hexadecimal number. </p>
<dt><code>-p</code></p>
<dd> Include PIDs in the window list printed by the <code>-l</code> action. Prints a PID of &#8216;0&#8217; if the application owning the window does not support it. </p>
<dt><code>-u</code></p>
<dd> Override auto-detection and force UTF-8 mode. </p>
<dt><code>-v</code></p>
<dd> Provide verbose output. This is really useful when debugging <code>wmctrl</code> itself. </p>
<dt><code>-w</code><i> [ &lt;WORKAROUND&gt;[,&lt;WORKAROUND&gt;]&#8230; ]</i></p>
<dd> Use workarounds specified in the argument. </p>
<dt><code>-x </code></p>
<dd> Include WM_CLASS in the window list or interpret &lt;WIN&gt; as the WM_CLASS name. </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>&lt;DESK&gt;</i></p>
<dd> A Desktop is always specified by an integer which represents the desktop numbers. Desktop numbers start at 0. Use -1 to pin to all desktops. </p>
<dt><i>&lt;MVARG&gt;</i></p>
<dd> A move and resize argument has the format <code>&#8216;</code><i>g</i><code>,</code><i>x</i><code>,</code><i>y,</i><code>w</code><i>,</i><code>h</code><i>&#8216;.</i> All five components are integers. The first value, <i>g</i>, is the gravity of the window, with 0 being the most common value (the default value for the window). Please see the EWMH specification for other values.</p>
<dt>
<dd> The four remaining values are a standard geometry specification: <i>x</i><code>,</code><i>y</i> is the position of the top left corner of the window, and <i>w</i><code>,</code><i>h</i> is the width and height of the window, with the exception that the value of -1 in any position is interpreted to mean that the current geometry value should not be modified. </p>
<dt><i>&lt;WIN&gt;</i></p>
<dd> This argument specifies a window that is the target of an action. By default the argument is treated as if were a string, and windows are examined until one is found with a title the contains the specified string as a substring. The substring matching is done in a case insensitive manner. The <code>-F</code> option may be used to force exact, case sensitive title matching. The option <code>-i</code> may be used to interpret the window target as a numeric window identity instead of a string.</p>
<dt>
<dd> The window name string <code>:SELECT:</code> is treated specially. If this window name is used then <code>wmctrl</code> waits for the user to select the target window by clicking on it.</p>
<dt>
<dd> The window name string <code>:ACTIVE:</code> may be used to instruct <code>wmctrl </code> to use the currently active window for the action. </p>
<dt><i>&lt;WORKAROUND&gt;</i></p>
<dd> There is only one work around currently implemeted. It is specified by using the string <code>DESKTOP_TITLES_INVALID_UTF8</code> and it causes the printing of non-ASCII desktop tiles correctly when using Window Maker. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Getting a list of windows managed by the window manager</p>
<dl>
<dt>
<dd> wmctrl -l</dl>
<p> Getting a list of windows with PID and geometry information.</p>
<dl>
<dt>
<dd> wmctrl -p -G -l</dl>
<p> Going to the window with a name containing &#8217;emacs&#8217; in it</p>
<dl>
<dt>
<dd> wmctrl -a emacs</dl>
<p> Shade a window with a title that contains the word &#8216;mozilla&#8217;</p>
<dl>
<dt>
<dd> wmctrl -r mozilla -b add,shaded</dl>
<p> Close a very specifically titled window sticky</p>
<dl>
<dt>
<dd> wmctrl -F -c &#8216;Debian bug tracking system &#8211; Mozilla&#8217;</dl>
<p> Toggle the &#8216;stickiness&#8217; of a window with a specific window identity</p>
<dl>
<dt>
<dd> wmctrl -i -r 0x0120002 -b add,sticky</dl>
<p> Change the title of window to a specified string but choose the window by clicking on it</p>
<dl>
<dt>
<dd> wmctrl -r :SELECT: -T &quot;Selected Window&quot;</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zenity/">zenity</a></code>(1) is a useful dialog program for building scripts with <code>wmctrl</code>. </p>
<p> Some examples of EWMH/NetWM compatible window managers include recent versions of Enlightenment, Icewm, Kwin, Sawfish and Xfce.</p>
<h2>AUTHOR</h2>
<p> wmctrl was written by Tomas Styblo &lt;tripie [at] cpan.org&gt;. </p>
<p> This manual page was written by Shyamal Prasad &lt;shyamal [at] member.fsf.org&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
