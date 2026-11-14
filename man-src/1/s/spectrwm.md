---
title: "spectrwm(1)"
name: "spectrwm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spectrwm/"
description: "spectrwm – window manager for X11"
---

<h2>NAME</h2>
<p> <code>spectrwm</code> &#8211; window manager for X11</p>
<h2>SYNOPSIS</h2>
<p> <code>spectrwm</code></p>
<h2>DESCRIPTION</h2>
<p> <code>spectrwm</code> is a minimalistic window manager that tries to stay out of the way so that valuable screen real estate can be used for much more important stuff. It has sane defaults and does not require one to learn a language to do any configuration. It was written by hackers for hackers and it strives to be small, compact and fast. </p>
<p> When <code>spectrwm</code> starts up, it reads settings from its configuration file, spectrwm.conf See the Sx CONFIGURATION FILES section below. </p>
<p> The following notation is used throughout this page: </p>
<dl>
<dt><code>M</code></p>
<dd> Meta</p>
<dt><code>S</code></p>
<dd> Shift</p>
<dt><code>Aq </code><code>Name</code></p>
<dd> Named key</p>
<dt><code>M1</code></p>
<dd> Mouse button 1</p>
<dt><code>M3</code></p>
<dd> Mouse button 3</dl>
<p> <code>spectrwm</code> is very simple in its use. Most of the actions are initiated via key or mouse bindings. See the Sx BINDINGS section below for defaults and customizations.</p>
<h2>CONFIGURATION FILES</h2>
<p> <code>spectrwm</code> first tries to open the user specific file, ~/.spectrwm.conf If that file is unavailable, it then tries to open the global configuration file /etc/spectrwm.conf </p>
<p> The format of the file is </p>
<blockquote><p><tt></tt><i>keyword </i><code>= </code><i>setting</i> </p></blockquote>
<p> For example: </p>
<blockquote><p><tt>color_focus = red</tt></p></blockquote>
<p> Enabling or disabling an option is done by using 1 or 0 respectively. </p>
<p> Colors need to be specified per the <a href="/docs/linux/man/3-xquerycolor/">XQueryColor</a>(3) specification. </p>
<p> Comments begin with a #. When a literal `#&#8217; is desired in an option, then it must be escaped with a backslash, i.e. \# </p>
<p> The file supports the following keywords:</p>
<dl>
<dt><code>autorun</code></p>
<dd> Launch an application in a specified workspace at start-of-day. Defined in the format <code>ws Bo </code><i>idx Bc </i>: <i>application</i> e.g. ws[2]:xterm launches an <a href="/docs/linux/man/1-xterm/">xterm</a>(1) in workspace 2. </p>
<p> Note that workspace mapping is handled via libswmhack.so When <code>autorun</code> spawns windows via a daemon, ensure the daemon is started with the correct LD_PRELOAD in its environment. </p>
<p> For example, starting <a href="/docs/linux/man/1-urxvtd/">urxvtd</a>(1) via <a href="/docs/linux/man/1-xinit/">xinit</a>(1): </p>
<blockquote>
<pre>
LD_PRELOAD=/usr/lib/libswmhack.so.0.0 urxvtd -q -o -f
</pre>
</blockquote>
<p> Spawned programs automatically have LD_PRELOAD set when executed.</p>
<dt><code>bar_action</code></p>
<dd> External script that populates additional information in the status bar, such as battery life.</p>
<dt><code>bar_at_bottom</code></p>
<dd> Place the statusbar at the bottom of each region instead of the top.</p>
<dt><code>bar_border Bq </code><i>x</i></p>
<dd> Border color of the status bar(s) in screen <i>x</i></p>
<dt><code>bar_border_unfocus Bq </code><i>x</i></p>
<dd> Border color of the status bar(s) on unfocused region(s) in screen <i>x</i></p>
<dt><code>bar_border_width</code></p>
<dd> Set status bar border thickness in pixels. Disable border by setting to 0.</p>
<dt><code>bar_color Bq </code><i>x</i></p>
<dd> Background color of the status bar(s) in screen <i>x</i></p>
<dt><code>bar_enabled</code></p>
<dd> Set default <code>bar_toggle</code> state; default is 1.</p>
<dt><code>bar_enabled_ws Bq </code><i>x</i></p>
<dd> Set default <code>bar_toggle_ws</code> state on workspace <i>x</i> default is 1.</p>
<dt><code>bar_font</code></p>
<dd> Font used in the status bar. Either Xft or X Logical Font Description (XLFD) may be used to specify fonts. Fallback fonts may be specified by separating each font with a comma. If all entries are in XLFD syntax, font set will be used. If at least one entry is Xft, Xft will be used. Note that if Xft is in use, only the first font that successfully loads will be used regardless of missing glyphs. The default is to use font set. Also note that <a href="/docs/linux/man/1-dmenu/">dmenu</a>(1) does not support Xft fonts. </p>
<p> Xft examples: </p>
<blockquote>
<pre>
bar_font = Terminus:style=Regular:pixelsize=14:antialias=true
bar_font = -*-profont-medium-*-*-*-11-*-*-*-*-*-*-*,Terminus:pixelsize=14,-*-clean-medium-*-*-*-12-*-*-*-*-*-*-*
</pre>
</blockquote>
<p> Font set examples: </p>
<blockquote>
<pre>
bar_font = -*-terminus-medium-*-*-*-14-*-*-*-*-*-*-*
bar_font = -*-profont-medium-*-*-*-11-*-*-*-*-*-*-*,-*-terminus-medium-*-*-*-14-*-*-*-*-*-*-*,-*-clean-medium-*-*-*-12-*-*-*-*-*-*-*
</pre>
</blockquote>
<p> To list the available fonts in your system see fc-list1 or <a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a>(1) manpages. The <a href="/docs/linux/man/1-xfontsel/">xfontsel</a>(1) application can help with the XLFD setting.</p>
<dt><code>bar_font_color Bq </code><i>x</i></p>
<dd> Color of the font in status bar in screen <i>x</i></p>
<dt><code>bar_format</code></p>
<dd> Set the bar format string, overriding <code>clock_format</code> and all of the <code>enabled</code> options. The format is passed through <a href="/docs/linux/man/3-strftime/">strftime</a>(3) before being used. It may contain the following character sequences:</p>
<dl>
<dt><code>Character sequence Ta </code><code>Replaced with</code></p>
<dd>
<dt><code>+&lt; Ta </code>Pad with a space</p>
<dd>
<dt><code>+A Ta </code>Output of the external script</p>
<dd>
<dt><code>+C Ta </code>Window class (from WM_CLASS)</p>
<dd>
<dt><code>+D Ta </code>Workspace name</p>
<dd>
<dt><code>+F Ta </code>Floating indicator</p>
<dd>
<dt><code>+I Ta </code>Workspace index</p>
<dd>
<dt><code>+M Ta </code>Number of iconic (minimized) windows in workspace</p>
<dd>
<dt><code>+N Ta </code>Screen number</p>
<dd>
<dt><code>+P Ta </code>Window class and instance separated by a colon</p>
<dd>
<dt><code>+S Ta </code>Stacking algorithm</p>
<dd>
<dt><code>+T Ta </code>Window instance (from WM_CLASS)</p>
<dd>
<dt><code>+U Ta </code>Urgency hint</p>
<dd>
<dt><code>+V Ta </code>Program version</p>
<dd>
<dt><code>+W Ta </code>Window name (from _NET_WM_NAME/WM_NAME)</p>
<dd>
<dt><code>++ Ta </code>A literal `+&#8217;</p>
<dd></dl>
<p> All character sequences may limit its output to a specific length, for example +64A. Any characters that don&#8217;t match the specification are copied as-is.</p>
<dt><code>bar_justify</code></p>
<dd> Justify the status bar text. Possible values are <i>left</i> <i>center</i> and <i>right</i> </p>
<p> Note that if the output is not left justified, it may not be properly aligned in some circumstances, due to the white-spaces in the default static format. See the <code>bar_format</code> option for more details.</p>
<dt><code>bind Bq </code><i>x</i></p>
<dd> Bind key combo to action <i>x</i> See the Sx BINDINGS section below.</p>
<dt><code>border_width</code></p>
<dd> Set window border thickness in pixels. Disable all borders by setting to 0.</p>
<dt><code>boundary_width</code></p>
<dd> Set region containment boundary width in pixels. This is how far a window must be dragged/resized beyond the region edge before it is allowed outside the region. This has no effect when manipulating the window with key bindings. Disable the window containment effect by setting to 0.</p>
<dt><code>clock_enabled</code></p>
<dd> Enable or disable displaying the clock in the status bar. Disable by setting to 0 so a custom clock could be used in the <code>bar_action</code> script.</p>
<dt><code>iconic_enabled</code></p>
<dd> Display the number of iconic (minimized) windows in the status bar. Enable by setting to 1.</p>
<dt><code>color_focus</code></p>
<dd> Border color of the currently focused window. Default is red.</p>
<dt><code>color_focus_maximized</code></p>
<dd> Border color of the currently focused, maximized window. Defaults to the value of <code>color_focus</code></p>
<dt><code>color_unfocus</code></p>
<dd> Border color of unfocused windows, default is rgb:88/88/88.</p>
<dt><code>color_unfocus_maximized</code></p>
<dd> Border color of unfocused, maximized windows. Defaults to the value of <code>color_unfocus</code></p>
<dt><code>dialog_ratio</code></p>
<dd> Some applications have dialogue windows that are too small to be useful. This ratio is the screen size to what they will be resized. For example, 0.6 is 60% of the physical screen size.</p>
<dt><code>disable_border</code></p>
<dd> Remove border when bar is disabled and there is only one window on the region.</p>
<dt><code>focus_close</code></p>
<dd> Window to put focus when the focused window is closed. Possible values are <i>first</i> <i>next</i> <i>previous</i> (default) and <i>last</i> <i>next</i> and <i>previous</i> are relative to the window that is closed.</p>
<dt><code>focus_close_wrap</code></p>
<dd> Whether to allow the focus to jump to the last window when the first window is closed or vice versa. Disable by setting to 0.</p>
<dt><code>focus_default</code></p>
<dd> Window to put focus when no window has been focused. Possible values are <i>first</i> and <i>last</i> (default).</p>
<dt><code>focus_mode</code></p>
<dd> Window focus behavior with respect to the mouse cursor. Possible values: </p>
<dl>
<dt><i>default</i></p>
<dd> Set window focus on border crossings caused by cursor motion and window interaction.</p>
<dt><i>follow</i></p>
<dd> Set window focus on all cursor border crossings, including workspace switches and changes to layout.</p>
<dt><i>manual</i></p>
<dd> Set window focus on window interaction only.</dl>
<dt><code>java_workaround</code></p>
<dd> Workaround a Java GUI rendering issue on non-reparenting window managers by impersonating the LG3D window manager, written by Sun. Default is 1.</p>
<dt><code>keyboard_mapping</code></p>
<dd> Clear all key bindings and load new key bindings from the specified file. This allows you to load pre-defined key bindings for your keyboard layout. See the Sx KEYBOARD MAPPING FILES section below for a list of keyboard mapping files that have been provided for several keyboard layouts.</p>
<dt><code>layout</code></p>
<dd> Select layout to use at start-of-day. Defined in the format <code>ws Bo </code><i>idx Bc </i>: <i>master_grow : </i><i>master_add : </i><i>stack_inc : </i><i>always_raise : </i><i>stack_mode</i> e.g. ws[2]:-4:0:1:0:horizontal sets worskspace 2 to the horizontal stack mode, shrinks the master area by 4 ticks and adds one window to the stack, while maintaining default floating window behavior. Possible <i>stack_mode</i> values are <i>vertical</i> <i>vertical_flip</i> <i>horizontal</i> <i>horizontal_flip</i> and <i>fullscreen</i> </p>
<p> See <code>master_grow</code> <code>master_shrink</code> <code>master_add</code> <code>master_del</code> <code>stack_inc</code> <code>stack_dec</code> and <code>always_raise</code> for more information. Note that the stacking options are complicated and have side-effects. One should familiarize oneself with these commands before experimenting with the <code>layout</code> option. </p>
<p> This setting is not retained at restart.</p>
<dt><code>modkey</code></p>
<dd> Change mod key. Mod1 is generally the ALT key and Mod4 is the windows key on a PC.</p>
<dt><code>name</code></p>
<dd> Set the name of a workspace at start-of-day. Defined in the format <code>ws Bo </code><i>idx Bc </i>: <i>name</i> e.g. ws[1]:Console sets the name of workspace 1 to &#8220;Console&#8221;</p>
<dt><code>program Bq </code><i>p</i></p>
<dd> Define new action to spawn a program <i>p</i> See the Sx PROGRAMS section below.</p>
<dt><code>quirk Bq </code><i>c </i><code>: </code><i>i </i><code>: </code><i>n</i></p>
<dd> Add &quot;quirk&quot; for windows with class <i>c</i> instance <i>i</i> and name <i>n</i> See the Sx QUIRKS section below.</p>
<dt><code>region</code></p>
<dd> Allocates a custom region, removing any autodetected regions which occupy the same space on the screen. Defined in the format <code>screen Bo </code><i>idx </i><code>Bc </code>: <i>width </i><code>x </code><i>height </i><code>+ </code><i>x </i><code>+ </code><i>y</i> e.g. screen[1]:800&#215;1200+0+0. </p>
<p> To make a region span multiple monitors, create a region big enough to cover them all, e.g. screen[1]:2048&#215;768+0+0 makes the region span two monitors with 1024&#215;768 resolution sitting one next to the other.</p>
<dt><code>region_padding</code></p>
<dd> Pixel width of empty space within region borders. Disable by setting to 0.</p>
<dt><code>spawn_position</code></p>
<dd> Position in stack to place newly spawned windows. Possible values are <i>first</i> <i>next</i> <i>previous</i> and <i>last</i> (default). <i>next</i> and <i>previous</i> are relative to the focused window.</p>
<dt><code>stack_enabled</code></p>
<dd> Enable or disable displaying the current stacking algorithm in the status bar.</p>
<dt><code>term_width</code></p>
<dd> Set a preferred minimum width for the terminal. If this value is greater than 0, <code>spectrwm</code> will attempt to adjust the font sizes in the terminal to keep the terminal width above this number as the window is resized. Only <a href="/docs/linux/man/1-xterm/">xterm</a>(1) is currently supported. The <a href="/docs/linux/man/1-xterm/">xterm</a>(1) binary must not be setuid or setgid, which it is by default on most systems. Users may need to set program[term] (see the Sx PROGRAMS section) to use an alternate copy of the <a href="/docs/linux/man/1-xterm/">xterm</a>(1) binary without the setgid bit set.</p>
<dt><code>tile_gap</code></p>
<dd> Pixel width of empty space between tiled windows. Negative values cause overlap. Set this to the opposite of <code>border_width</code> to collapse the border between tiles. Disable by setting to 0.</p>
<dt><code>urgent_collapse</code></p>
<dd> Enables hiding of placeholders in the urgency hint indicator for workspaces that do not have any urgent windows. Enable by setting to 1.</p>
<dt><code>urgent_enabled</code></p>
<dd> Enable or disable the urgency hint indicator in the status bar. Note that many terminal emulators require an explicit setting for the bell character to trigger urgency on the window. In <a href="/docs/linux/man/1-xterm/">xterm</a>(1), for example, one needs to add the following line to .Xdefaults </p>
<blockquote>
<pre>
xterm.bellIsUrgent: true
</pre>
</blockquote>
<dt><code>verbose_layout</code></p>
<dd> Enable or disable displaying the current master window count and stack column/row count in the status bar. Enable by setting to 1. See <i>master_add</i> <i>master_del</i> <i>stack_inc</i> and <i>stack_dec</i> for more information.</p>
<dt><code>window_class_enabled</code></p>
<dd> Enable or disable displaying the window class name (from WM_CLASS) in the status bar. Enable by setting to 1.</p>
<dt><code>window_instance_enabled</code></p>
<dd> Enable or disable displaying the window instance name (from WM_CLASS) in the status bar. Enable by setting to 1.</p>
<dt><code>window_name_enabled</code></p>
<dd> Enable or disable displaying the window display name (from _NET_WM_NAME/WM_NAME) in the status bar. Enable by setting to 1. </p>
<p> To prevent excessively large window names from pushing the remaining text off the bar, it&#8217;s limited to 64 characters, by default. See the <code>bar_format</code> option for more details.</p>
<dt><code>warp_pointer</code></p>
<dd> Centers the mouse pointer on the focused window when using key bindings to change focus, switch workspaces, change regions, etc. Enable by setting to 1.</p>
<dt><code>workspace_limit</code></p>
<dd> Set the total number of workspaces available. Minimum is 1, maximum is 22, default is 10.</dl>
<h2>PROGRAMS</h2>
<p> <code>spectrwm</code> allows you to define custom actions to launch programs of your choice and then bind them the same as with built-in actions. See the Sx BINDINGS section below. </p>
<p> Custom programs in the configuration file are specified as follows: </p>
<blockquote><p><tt>program </tt><code>Bo </code><i>action Bc </i>= <i>progpath </i>[<i>arg </i>[<i>arg &#8230;</i> ] ] </p></blockquote>
<p> <i>action</i> is any identifier that does not conflict with a built-in action or keyword, <i>progpath</i> is the desired program, and <i>arg</i> is zero or more arguments to the program. </p>
<p> Remember that when using `#&#8217; in your program call, it must be escaped with a backslash, i.e. \# </p>
<p> The following argument variables will be substituted for values at the time the program is spawned: </p>
<dl>
<dt><code>$bar_border</code></p>
<dd>
<dt><code>$bar_color</code></p>
<dd>
<dt><code>$bar_font</code></p>
<dd>
<dt><code>$bar_font_color</code></p>
<dd>
<dt><code>$color_focus</code></p>
<dd>
<dt><code>$color_unfocus</code></p>
<dd>
<dt><code>$dmenu_bottom</code></p>
<dd> -b if <code>bar_at_bottom</code> is enabled.</p>
<dt><code>$region_index</code></p>
<dd>
<dt><code>$workspace_index</code></p>
<dd></dl>
<p> Example: </p>
<blockquote>
<pre><code>
program[ff] = / usr / local / bin / firefox http : // spectrwm.org/
                                                   bind[ff] = MOD + Shift + b #Now M - S - b launches firefox
</code></pre>
</blockquote>
<p> To cancel the previous, unbind it: </p>
<blockquote>
<pre>
bind[] = MOD+Shift+b
</pre>
</blockquote>
<p> Default programs:</p>
<dl>
<dt><code>lock</code></p>
<dd> xlock</p>
<dt><code>menu</code></p>
<dd> dmenu_run $dmenu_bottom -fn $bar_font -nb $bar_color -nf $bar_font_color -sb $bar_border -sf $bar_color</p>
<dt><code>term</code></p>
<dd> xterm</p>
<dt><code>initscr</code></p>
<dd> initscreen.sh # optional</p>
<dt><code>screenshot_all</code></p>
<dd> screenshot.sh full # optional</p>
<dt><code>screenshot_wind</code></p>
<dd> screenshot.sh window # optional</dl>
<p> Note that optional default programs will not be validated unless overridden. If a default program fails validation, you can resolve the exception by installing the program, modifying the program call or disabling the program by freeing the respective key binding. </p>
<p> For example, to override <code>lock</code> </p>
<blockquote>
<pre>
program[lock] = xscreensaver-command -lock
</pre>
</blockquote>
<p> To unbind <code>lock</code> and prevent it from being validated: </p>
<blockquote>
<pre>
bind[] = MOD+Shift+Delete
</pre>
</blockquote>
<h2>BINDINGS</h2>
<p> <code>spectrwm</code> provides many functions (or actions) accessed via key or mouse bindings. </p>
<p> The current mouse bindings are described below: </p>
<dl>
<dt><code>M1</code></p>
<dd> Focus window</p>
<dt><code>M-M1</code></p>
<dd> Move window</p>
<dt><code>M-M3</code></p>
<dd> Resize window</p>
<dt><code>M-S-M3</code></p>
<dd> Resize window while maintaining it centered</dl>
<p> The default key bindings are described below: </p>
<dl>
<dt><code>M-S- Aq </code><code>Return</code></p>
<dd> term</p>
<dt><code>M-p</code></p>
<dd> menu</p>
<dt><code>M-S-q</code></p>
<dd> quit</p>
<dt><code>M-q</code></p>
<dd> restart</p>
<dt><code>M- Aq </code><code>Space</code></p>
<dd> cycle_layout</p>
<dt><code>M-S-\</code></p>
<dd> flip_layout</p>
<dt><code>M-S- Aq </code><code>Space</code></p>
<dd> stack_reset</p>
<dt><code>M-h</code></p>
<dd> master_shrink</p>
<dt><code>M-l</code></p>
<dd> master_grow</p>
<dt><code>M-,</code></p>
<dd> master_add</p>
<dt><code>M-.</code></p>
<dd> master_del</p>
<dt><code>M-S-,</code></p>
<dd> stack_inc</p>
<dt><code>M-S-.</code></p>
<dd> stack_dec</p>
<dt><code>M- Aq </code><code>Return</code></p>
<dd> swap_main</p>
<dt> <code>M-j</code> <code>M- Aq </code><code>TAB</code></p>
<dd>
<dd>focus_next</p>
<dt> <code>M-k</code> <code>M-S- Aq </code><code>TAB</code></p>
<dd>
<dd>focus_prev</p>
<dt><code>M-m</code></p>
<dd> focus_main</p>
<dt><code>M-u</code></p>
<dd> focus_urgent</p>
<dt><code>M-S-j</code></p>
<dd> swap_next</p>
<dt><code>M-S-k</code></p>
<dd> swap_prev</p>
<dt><code>M-b</code></p>
<dd> bar_toggle</p>
<dt><code>M-S-b</code></p>
<dd> bar_toggle_ws</p>
<dt><code>M-x</code></p>
<dd> wind_del</p>
<dt><code>M-S-x</code></p>
<dd> wind_kill</p>
<dt><code>M- Aq </code><i>1-9,0,F1-F12</i></p>
<dd> ws_ Aq <i>1-22</i></p>
<dt><code>M-S- Aq </code><i>1-9,0,F1-F12</i></p>
<dd> mvws_ <code>Aq </code><i>1-22</i></p>
<dt><code>M- Aq </code><i>Keypad 1-9</i></p>
<dd> rg_ Aq <i>1-9</i></p>
<dt><code>M-S- Aq </code><i>Keypad 1-9</i></p>
<dd> mvrg_ Aq <i>1-9</i></p>
<dt><code>M- Aq </code><code>Right</code></p>
<dd> ws_next</p>
<dt><code>M- Aq </code><code>Left</code></p>
<dd> ws_prev</p>
<dt><code>M- Aq </code><code>Up </code>ws_next_all</p>
<dd>
<dt><code>M- Aq </code><code>Down</code></p>
<dd> ws_prev_all</p>
<dt><code>M-a</code></p>
<dd> ws_next_move</p>
<dt><code>M-S- Aq </code><code>Left</code></p>
<dd> ws_prev_move</p>
<dt><code>M-S- Aq </code><code>Up </code>ws_prior</p>
<dd>
<dt><code>M-S- Aq </code><code>Right</code></p>
<dd> rg_next</p>
<dt><code>M-S- Aq </code><code>Left</code></p>
<dd> rg_prev</p>
<dt><code>M-s</code></p>
<dd> screenshot_all</p>
<dt><code>M-S-s</code></p>
<dd> screenshot_wind</p>
<dt><code>M-S-v</code></p>
<dd> version</p>
<dt><code>M-t</code></p>
<dd> float_toggle</p>
<dt><code>M-S- Aq </code><code>Delete</code></p>
<dd> lock</p>
<dt><code>M-S-i</code></p>
<dd> initscr</p>
<dt><code>M-w</code></p>
<dd> iconify</p>
<dt><code>M-S-w</code></p>
<dd> uniconify</p>
<dt><code>M-e</code></p>
<dd> maximize_toggle</p>
<dt><code>M-S-r</code></p>
<dd> always_raise</p>
<dt><code>M-v</code></p>
<dd> button2</p>
<dt><code>M&#8211;</code></p>
<dd> width_shrink</p>
<dt><code>M-=</code></p>
<dd> width_grow</p>
<dt><code>M-S&#8211;</code></p>
<dd> height_shrink</p>
<dt><code>M-S-=</code></p>
<dd> height_grow</p>
<dt><code>M-[</code></p>
<dd> move_left</p>
<dt><code>M-]</code></p>
<dd> move_right</p>
<dt><code>M-S-[</code></p>
<dd> move_up</p>
<dt><code>M-S-]</code></p>
<dd> move_down</p>
<dt><code>M-S-/</code></p>
<dd> name_workspace</p>
<dt><code>M-/</code></p>
<dd> search_workspace</p>
<dt><code>M-f</code></p>
<dd> search_win</dl>
<p> The action names and descriptions are listed below: </p>
<dl>
<dt><code>term</code></p>
<dd> Spawn a new terminal (see Sx PROGRAMS above).</p>
<dt><code>menu</code></p>
<dd> Menu (see Sx PROGRAMS above).</p>
<dt><code>quit</code></p>
<dd> Quit <code>.</code></p>
<dt><code>restart</code></p>
<dd> Restart <code>.</code></p>
<dt><code>cycle_layout</code></p>
<dd> Cycle layout.</p>
<dt><code>flip_layout</code></p>
<dd> Swap the master and stacking areas.</p>
<dt><code>stack_reset</code></p>
<dd> Reset layout.</p>
<dt><code>master_shrink</code></p>
<dd> Shrink master area.</p>
<dt><code>master_grow</code></p>
<dd> Grow master area.</p>
<dt><code>master_add</code></p>
<dd> Add windows to master area.</p>
<dt><code>master_del</code></p>
<dd> Remove windows from master area.</p>
<dt><code>stack_inc</code></p>
<dd> Add columns/rows to stacking area.</p>
<dt><code>stack_dec</code></p>
<dd> Remove columns/rows from stacking area.</p>
<dt><code>swap_main</code></p>
<dd> Move current window to master area.</p>
<dt><code>focus_next</code></p>
<dd> Focus next window in workspace.</p>
<dt><code>focus_prev</code></p>
<dd> Focus previous window in workspace.</p>
<dt><code>focus_main</code></p>
<dd> Focus on main window in workspace.</p>
<dt><code>focus_urgent</code></p>
<dd> Focus on next window with the urgency hint flag set. The workspace is switched if needed.</p>
<dt><code>swap_next</code></p>
<dd> Swap with next window in workspace.</p>
<dt><code>swap_prev</code></p>
<dd> Swap with previous window in workspace.</p>
<dt><code>bar_toggle</code></p>
<dd> Toggle overall visibility of status bars.</p>
<dt><code>bar_toggle_ws</code></p>
<dd> Toggle status bar on current workspace.</p>
<dt><code>wind_del</code></p>
<dd> Delete current window in workspace.</p>
<dt><code>wind_kill</code></p>
<dd> Destroy current window in workspace.</p>
<dt><code>ws_ </code><i>n</i></p>
<dd> Switch to workspace <i>n</i> where <i>n</i> is 1 through <code>workspace_limit</code></p>
<dt><code>mvws_ </code><i>n</i></p>
<dd> Move current window to workspace <i>n</i> where <i>n</i> is 1 through <code>workspace_limit</code></p>
<dt><code>rg_ </code><i>n</i></p>
<dd> Focus on region <i>n</i> where <i>n</i> is 1 through 9.</p>
<dt><code>mvrg_ </code><i>n</i></p>
<dd> Move current window to region <i>n</i> where <i>n</i> is 1 through 9.</p>
<dt><code>ws_next</code></p>
<dd> Switch to next workspace with a window in it.</p>
<dt><code>ws_prev</code></p>
<dd> Switch to previous workspace with a window in it.</p>
<dt><code>ws_next_all</code></p>
<dd> Switch to next workspace.</p>
<dt><code>ws_prev_all</code></p>
<dd> Switch to previous workspace.</p>
<dt><code>ws_next_move</code></p>
<dd> Switch to next workspace with the current window.</p>
<dt><code>ws_prev_move</code></p>
<dd> Switch to previous workspace with the current window.</p>
<dt><code>ws_prior</code></p>
<dd> Switch to last visited workspace.</p>
<dt><code>rg_next</code></p>
<dd> Switch to next region.</p>
<dt><code>rg_prev</code></p>
<dd> Switch to previous region.</p>
<dt><code>screenshot_all</code></p>
<dd> Take screenshot of entire screen (if enabled) (see Sx PROGRAMS above).</p>
<dt><code>screenshot_wind</code></p>
<dd> Take screenshot of selected window (if enabled) (see Sx PROGRAMS above).</p>
<dt><code>version</code></p>
<dd> Toggle version in status bar.</p>
<dt><code>float_toggle</code></p>
<dd> Toggle focused window between tiled and floating.</p>
<dt><code>lock</code></p>
<dd> Lock screen (see Sx PROGRAMS above).</p>
<dt><code>initscr</code></p>
<dd> Reinitialize physical screens (see Sx PROGRAMS above).</p>
<dt><code>iconify</code></p>
<dd> Minimize (unmap) currently focused window.</p>
<dt><code>uniconify</code></p>
<dd> Restore (map) window returned by <a href="/docs/linux/man/1-dmenu/">dmenu</a>(1) selection.</p>
<dt><code>maximize_toggle</code></p>
<dd> Toggle maximization of focused window.</p>
<dt><code>always_raise</code></p>
<dd> When set tiled windows are allowed to obscure floating windows.</p>
<dt><code>button2</code></p>
<dd> Fake a middle mouse button click (mouse button 2).</p>
<dt><code>width_shrink</code></p>
<dd> Shrink the width of a floating window.</p>
<dt><code>width_grow</code></p>
<dd> Grow the width of a floating window.</p>
<dt><code>height_shrink</code></p>
<dd> Shrink the height of a floating window.</p>
<dt><code>height_grow</code></p>
<dd> Grow the height of a floating window.</p>
<dt><code>move_left</code></p>
<dd> Move a floating window a step to the left.</p>
<dt><code>move_right</code></p>
<dd> Move a floating window a step to the right.</p>
<dt><code>move_up</code></p>
<dd> Move a floating window a step upwards.</p>
<dt><code>move_down</code></p>
<dd> Move a floating window a step downwards.</p>
<dt><code>name_workspace</code></p>
<dd> Name the current workspace.</p>
<dt><code>search_workspace</code></p>
<dd> Search for a workspace.</p>
<dt><code>search_win</code></p>
<dd> Search the windows in the current workspace.</dl>
<p> Custom bindings in the configuration file are specified as follows: </p>
<blockquote><p><tt>bind </tt><code>Bo </code><i>action Bc </i>= <i>keys</i> </p></blockquote>
<p> <i>action</i> is one of the actions listed above (or empty to unbind) and <i>keys</i> is in the form of zero or more modifier keys (MOD, Mod1, Shift, etc.) and one or more normal keys (b, Space, etc.), separated by `+&#8217; </p>
<p> Example: </p>
<blockquote><p>
bind[reset] = Mod4 + q #bind Windows &#8211; key + q to reset bind[] = Mod1 + q #unbind Alt + q
 </p></blockquote>
<p> To use the currently defined <code>modkey</code> specify MOD as the modifier key. </p>
<p> Multiple key combinations may be bound to the same action. </p>
<p> To bind non-latin characters such as &aring; or &pi; you must enter the xkb character name instead of the character itself. Run <a href="/docs/linux/man/1-xev/">xev</a>(1), focus the window and press the specific key and in the terminal output read the symbol name. In the following example for &aring;: </p>
<blockquote><p>
KeyPress event, serial 41, synthetic NO, window 0x2600001,<br />
    root 0x15a, subw 0x0, time 106213808, (11, 5), root : (359, 823),<br />
                                                          state 0x0,<br />
                                                          keycode 24(keysym 0xe5, aring),<br />
                                                          same_screen YES,<br />
                                                          XLookupString gives 2 bytes : (c3 a5) &#8220;&amp;aring;&#8221; XmbLookupString gives 2 bytes : (c3 a5) &#8220;&amp;aring;&#8221; XFilterEvent returns : False
 </p></blockquote>
<p> The xkb name is aring. In other words, in spectrwm.conf add: </p>
<blockquote>
<pre>
bind[program] = MOD+aring
</pre>
</blockquote>
<h2>KEYBOARD MAPPING FILES</h2>
<p> Keyboard mapping files for several keyboard layouts are listed below. These files can be used with the <code>keyboard_mapping</code> setting to load pre-defined key bindings for the specified keyboard layout. </p>
<dl>
<dt><code>spectrwm_cz.conf</code></p>
<dd> Czech Republic keyboard layout</p>
<dt><code>spectrwm_es.conf</code></p>
<dd> Spanish keyboard layout</p>
<dt><code>spectrwm_fr.conf</code></p>
<dd> French keyboard layout</p>
<dt><code>spectrwm_fr_ch.conf</code></p>
<dd> Swiss French keyboard layout</p>
<dt><code>spectrwm_se.conf</code></p>
<dd> Swedish keyboard layout</p>
<dt><code>spectrwm_us.conf</code></p>
<dd> United States keyboard layout</dl>
<h2>QUIRKS</h2>
<p> <code>spectrwm</code> provides &quot;quirks&quot; which handle windows that must be treated specially in a tiling window manager, such as some dialogs and fullscreen apps. </p>
<p> The default quirks are described below: </p>
<dl>
<dt><code>Firefox-bin:firefox-bin</code></p>
<dd> TRANSSZ</p>
<dt><code>Firefox:Dialog</code></p>
<dd> FLOAT</p>
<dt><code>Gimp:gimp</code></p>
<dd> FLOAT + ANYWHERE</p>
<dt><code>MPlayer:xv</code></p>
<dd> FLOAT + FULLSCREEN + FOCUSPREV</p>
<dt><code>OpenOffice.org 2.4:VCLSalFrame</code></p>
<dd> FLOAT</p>
<dt><code>OpenOffice.org 3.1:VCLSalFrame</code></p>
<dd> FLOAT</p>
<dt><code>pcb:pcb</code></p>
<dd> FLOAT</p>
<dt><code>xine:Xine Window</code></p>
<dd> FLOAT + ANYWHERE</p>
<dt><code>xine:xine Panel</code></p>
<dd> FLOAT + ANYWHERE</p>
<dt><code>xine:xine Video Fullscreen Window</code></p>
<dd> FULLSCREEN + FLOAT</p>
<dt><code>Xitk:Xitk Combo</code></p>
<dd> FLOAT + ANYWHERE</p>
<dt><code>Xitk:Xine Window</code></p>
<dd> FLOAT + ANYWHERE</p>
<dt><code>XTerm:xterm</code></p>
<dd> XTERM_FONTADJ</dl>
<p> The quirks themselves are described below: </p>
<dl>
<dt><code>FLOAT</code></p>
<dd> This window should not be tiled, but allowed to float freely.</p>
<dt><code>TRANSSZ</code></p>
<dd> Adjusts size on transient windows that are too small using <code>dialog_ratio</code> (see Sx CONFIGURATION FILES ) .</p>
<dt><code>ANYWHERE</code></p>
<dd> Allow window to position itself, uncentered.</p>
<dt><code>XTERM_FONTADJ</code></p>
<dd> Adjust <a href="/docs/linux/man/1-xterm/">xterm</a>(1) fonts when resizing.</p>
<dt><code>FULLSCREEN</code></p>
<dd> Remove border to allow window to use full region size.</p>
<dt><code>FOCUSPREV</code></p>
<dd> On exit force focus on previously focused application not previous application in the stack.</p>
<dt><code>NOFOCUSONMAP</code></p>
<dd> Don&#8217;t change focus to the window when it first appears on the screen. Has no effect when <code>focus_mode</code> is set to <i>follow</i></p>
<dt><code>FOCUSONMAP_SINGLE</code></p>
<dd> When the window first appears on the screen, change focus to the window if there are no other windows on the workspace with the same WM_CLASS class/instance value. Has no effect when <code>focus_mode</code> is set to <i>follow</i></p>
<dt><code>OBEYAPPFOCUSREQ</code></p>
<dd> When an application requests focus on the window via a _NET_ACTIVE_WINDOW client message (source indication of 1), comply with the request. Note that a source indication of 0 (unspecified) or 2 (pager) are always obeyed.</p>
<dt><code>IGNOREPID</code></p>
<dd> Ignore the PID when determining the initial workspace for a new window. Especially useful for terminal windows that share a process.</p>
<dt><code>IGNORESPAWNWS</code></p>
<dd> Ignore the spawn workspace when determining the initial workspace for a new window.</p>
<dt><code>WS Bq </code><i>n</i></p>
<dd> Force a new window to appear on workspace <i>n</i></dl>
<p> Custom quirks in the configuration file are specified as follows: </p>
<blockquote><p><tt>quirk </tt><code>Bo </code><i>class </i><code>Bo </code>: <i>instance </i><code>Bo </code>: <i>name Bc </i>Bc Bc = <i>quirk </i>[+ <i>quirk &#8230;</i> ] </p></blockquote>
<p> <i>class</i> <i>instance</i> (optional) and <i>name</i> (optional) are patterns used to determine which window(s) the quirk(s) apply to and <i>quirk</i> is one of the quirks from the list above. </p>
<p> Note that patterns are interpreted as POSIX Extended Regular Expressions. Any &#8216;:&#8217;, &#8216;[&#8216; or &#8216;]&#8217; must be escaped with &#8216;\&#8217;. See <a href="/docs/linux/man/7-regex/">regex</a>(7) for more information on POSIX Extended Regular Expressions. </p>
<p> For example: </p>
<blockquote>
<pre><code>
quirk[MPlayer] = FLOAT + FULLSCREEN + FOCUSPREV #Float all windows having a class of 'MPlayer' quirk[.*] = FLOAT #Float all windows by default.quirk [.*:.*:.*] = FLOAT #Same as above.quirk [Firefox:Navigator] = FLOAT #Float all Firefox browser windows.quirk[::Console] = FLOAT #Float windows with WM_CLASS not set and a window name of 'Console'.quirk [\[0 - 9\].*:.*:\[\[\:alnum \:\]\] * ] = FLOAT #Float windows with WM_CLASS class beginning with a number, any WM_CLASS instance and a _NET_WM_NAME / WM_NAME either blank or containing alphanumeric characters without spaces.quirk [pcb:pcb] = NONE #remove existing quirk
</code></pre>
</blockquote>
<p> You can obtain <i>class</i> <i>instance</i> and <i>name</i> by running <a href="/docs/linux/man/1-xprop/">xprop</a>(1) and then clicking on the desired window. In the following example the main window of Firefox was clicked: </p>
<blockquote>
<pre>
$ xprop | grep -E &quot;^(WM_CLASS|_NET_WM_NAME|WM_NAME)&quot;
WM_CLASS(STRING) = &quot;Navigator&quot;, &quot;Firefox&quot;
WM_NAME(STRING) = &quot;spectrwm - ConformalOpenSource&quot;
_NET_WM_NAME(UTF8_STRING) = &quot;spectrwm - ConformalOpenSource&quot;
</pre>
</blockquote>
<p> Note that <a href="/docs/linux/man/1-xprop/">xprop</a>(1) displays WM_CLASS as: </p>
<blockquote>
<pre>
WM_CLASS(STRING) = &quot;&lt;instance&gt;&quot;, &quot;&lt;class&gt;&quot;
</pre>
</blockquote>
<p> In the example above the quirk entry would be: </p>
<blockquote>
<pre>
quirk[Firefox:Navigator] = FLOAT
</pre>
</blockquote>
<p> <code>spectrwm</code> also automatically assigns quirks to windows based on the value of the window&#8217;s _NET_WM_WINDOW_TYPE property as follows: </p>
<dl>
<dt><code>_NET_WM_WINDOW_TYPE_DOCK</code></p>
<dd> FLOAT + ANYWHERE</p>
<dt><code>_NET_WM_WINDOW_TYPE_TOOLBAR</code></p>
<dd> FLOAT + ANYWHERE</p>
<dt><code>_NET_WM_WINDOW_TYPE_UTILITY</code></p>
<dd> FLOAT + ANYWHERE</p>
<dt><code>_NET_WM_WINDOW_TYPE_SPLASH</code></p>
<dd> FLOAT</p>
<dt><code>_NET_WM_WINDOW_TYPE_DIALOG</code></p>
<dd> FLOAT</dl>
<p> In all other cases, no automatic quirks are assigned to the window. Quirks specified in the configuration file override the automatic quirks.</p>
<h2>EWMH</h2>
<p> <code>spectrwm</code> partially implements the Extended Window Manager Hints (EWMH) specification. This enables controlling windows as well as <code>spectrwm</code> itself from external scripts and programs. This is achieved by <code>spectrwm</code> responding to certain ClientMessage events. From the terminal these events can be conveniently sent using tools such as <a href="/docs/linux/man/1-wmctrl/">wmctrl</a>(1) and <a href="/docs/linux/man/1-xdotool/">xdotool</a>(1). For the actual format of these ClientMessage events, see the EWMH specification. </p>
<p> The id of the currently focused window is stored in the _NET_ACTIVE_WINDOW property of the root window. This can be used for example to retrieve the title of the currently active window with <a href="/docs/linux/man/1-xprop/">xprop</a>(1) and <a href="/docs/linux/man/1-grep/">grep</a>(1): </p>
<blockquote>
<pre>
$ WINDOWID=`xprop -root _NET_ACTIVE_WINDOW | grep -o &quot;0x.*&quot;`
$ xprop -id $WINDOWID _NET_WM_NAME | grep -o &quot;\&quot;.*\&quot;&quot;
</pre>
</blockquote>
<p> A window can be focused by sending a _NET_ACTIVE_WINDOW client message to the root window. For example, using <a href="/docs/linux/man/1-wmctrl/">wmctrl</a>(1) to send the message (assuming 0x4a0000b is the id of the window to be focused): </p>
<blockquote>
<pre>
$ wmctrl -i -a 0x4a0000b
</pre>
</blockquote>
<p> Windows can be closed by sending a _NET_CLOSE_WINDOW client message to the root window. For example, using <a href="/docs/linux/man/1-wmctrl/">wmctrl</a>(1) to send the message (assuming 0x4a0000b is the id of the window to be closed): </p>
<blockquote>
<pre>
$ wmctrl -i -c 0x4a0000b
</pre>
</blockquote>
<p> Windows can be floated and un-floated by adding or removing the _NET_WM_STATE_ABOVE atom from the _NET_WM_STATE property of the window. This can be achieved by sending a _NET_WM_STATE client message to the root window. For example, the following toggles the floating state of a window using <a href="/docs/linux/man/1-wmctrl/">wmctrl</a>(1) to send the message (assuming 0x4a0000b is the id of the window to be floated or un-floated): </p>
<blockquote>
<pre>
$ wmctrl -i -r 0x4a0000b -b toggle,_NET_WM_STATE_ABOVE
</pre>
</blockquote>
<p> Windows can also be iconified and un-iconified by substituting _NET_WM_STATE_HIDDEN for _NET_WM_STATE_ABOVE in the previous example: </p>
<blockquote>
<pre>
$ wmctrl -i -r 0x4a0000b -b toggle,_NET_WM_STATE_HIDDEN
</pre>
</blockquote>
<p> Floating windows can also be resized and moved by sending a _NET_MOVERESIZE_WINDOW client message to the root window. For example, using <a href="/docs/linux/man/1-wmctrl/">wmctrl</a>(1) to send the message (assuming 0x4a0000b is the id of the window to be resize/moved): </p>
<blockquote>
<pre>
$ wmctrl -i -r 0x4a0000b -e 0,100,50,640,480
</pre>
</blockquote>
<p> This moves the window to (100,50) and resizes it to 640&#215;480. </p>
<p> Any _NET_MOVERESIZE_WINDOW events received for stacked windows are ignored.</p>
<h2>SIGNALS</h2>
<p> Sending <code>spectrwm</code> a HUP signal will restart it.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.spectrwm.conf </code></p>
<dd> <code>spectrwm</code> user specific settings.</p>
<dt><code>/etc/spectrwm.conf </code></p>
<dd> <code>spectrwm</code> global settings.</dl>
<h2>HISTORY</h2>
<p> <code>spectrwm</code> was inspired by xmonad &amp; dwm.</p>
<h2>AUTHORS</h2>
<p> An -nosplit <code>spectrwm</code> was written by: </p>
<dl>
<dt><code>Marco Peereboom Aq </code>marco [at] peereboom.us</p>
<dd>
<dt><code>Ryan Thomas McBride Aq </code>mcbride [at] countersiege.com</p>
<dd>
<dt><code>Darrin Chandler Aq </code>dwchandler [at] stilyagin.com</p>
<dd>
<dt><code>Pierre-Yves Ritschard Aq </code>pyr [at] spootnik.org</p>
<dd>
<dt><code>Tuukka Kataja Aq </code>stuge [at] xor.fi</p>
<dd>
<dt><code>Jason L. Wright Aq </code>jason [at] thought.net</p>
<dd>
<dt><code>Reginald Kennedy Aq </code>rk [at] rejii.com</p>
<dd>
<dt><code>Lawrence Teo Aq </code>lteo [at] lteo.net</p>
<dd>
<dt><code>Tiago Cunha Aq </code>tcunha [at] gmx.com</p>
<dd>
<dt><code>David Hill Aq </code>dhill [at] mindcry.org</p>
<dd></dl>
<h2>Index</h2>
