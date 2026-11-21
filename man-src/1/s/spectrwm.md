---

title: "spectrwm(1)"
name: "spectrwm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spectrwm/"
description: "spectrwm – window manager for X11"
---

<p> <code>spectrwm</code> &#8211; window manager for X11</p>
<h2>SYNOPSIS</h2>
<p> <code>spectrwm</code></p>
<h2>DESCRIPTION</h2>
<p> <code>spectrwm</code> is a minimalistic window manager that tries to stay out of the way so that valuable screen real estate can be used for much more important stuff. It has sane defaults and does not require one to learn a language to do any configuration. It was written by hackers for hackers and it strives to be small, compact and fast. </p>
<p> When <code>spectrwm</code> starts up, it reads settings from its configuration file, spectrwm.conf See the Sx CONFIGURATION FILES section below. </p>
<p> The following notation is used throughout this page: </p>
<dl>
<dt><code>M</code></dt>
<dd> Meta</dd>
<dt><code>S</code></dt>
<dd> Shift</dd>
<dt><code>Aq </code><code>Name</code></dt>
<dd> Named key</dd>
<dt><code>M1</code></dt>
<dd> Mouse button 1</dd>
<dt><code>M3</code></dt>
<dd> Mouse button 3</dd></dl>
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
<dt><code>autorun</code></dt>
<dd> Launch an application in a specified workspace at start-of-day. Defined in the format <code>ws Bo </code><i>idx Bc </i>: <i>application</i> e.g. ws[2]:xterm launches an <a href="/docs/linux/man/1-xterm/">xterm</a>(1) in workspace 2. </dd>
<p> Note that workspace mapping is handled via libswmhack.so When <code>autorun</code> spawns windows via a daemon, ensure the daemon is started with the correct LD_PRELOAD in its environment. </p>
<p> For example, starting <a href="/docs/linux/man/1-urxvtd/">urxvtd</a>(1) via <a href="/docs/linux/man/1-xinit/">xinit</a>(1): </p>
<blockquote>
<pre>
LD_PRELOAD=/usr/lib/libswmhack.so.0.0 urxvtd -q -o -f
</pre>
</blockquote>
<p> Spawned programs automatically have LD_PRELOAD set when executed.</p>
<dt><code>bar_action</code></dt>
<dd> External script that populates additional information in the status bar, such as battery life.</dd>
<dt><code>bar_at_bottom</code></dt>
<dd> Place the statusbar at the bottom of each region instead of the top.</dd>
<dt><code>bar_border Bq </code><i>x</i></dt>
<dd> Border color of the status bar(s) in screen <i>x</i></dd>
<dt><code>bar_border_unfocus Bq </code><i>x</i></dt>
<dd> Border color of the status bar(s) on unfocused region(s) in screen <i>x</i></dd>
<dt><code>bar_border_width</code></dt>
<dd> Set status bar border thickness in pixels. Disable border by setting to 0.</dd>
<dt><code>bar_color Bq </code><i>x</i></dt>
<dd> Background color of the status bar(s) in screen <i>x</i></dd>
<dt><code>bar_enabled</code></dt>
<dd> Set default <code>bar_toggle</code> state; default is 1.</dd>
<dt><code>bar_enabled_ws Bq </code><i>x</i></dt>
<dd> Set default <code>bar_toggle_ws</code> state on workspace <i>x</i> default is 1.</dd>
<dt><code>bar_font</code></dt>
<dd> Font used in the status bar. Either Xft or X Logical Font Description (XLFD) may be used to specify fonts. Fallback fonts may be specified by separating each font with a comma. If all entries are in XLFD syntax, font set will be used. If at least one entry is Xft, Xft will be used. Note that if Xft is in use, only the first font that successfully loads will be used regardless of missing glyphs. The default is to use font set. Also note that <a href="/docs/linux/man/1-dmenu/">dmenu</a>(1) does not support Xft fonts. </dd>
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
<dt><code>bar_font_color Bq </code><i>x</i></dt>
<dd> Color of the font in status bar in screen <i>x</i></dd>
<dt><code>bar_format</code></dt>
<dd> Set the bar format string, overriding <code>clock_format</code> and all of the <code>enabled</code> options. The format is passed through <a href="/docs/linux/man/3-strftime/">strftime</a>(3) before being used. It may contain the following character sequences:</dd>
<dl>
<dt><code>Character sequence Ta </code><code>Replaced with</code></dt>
<dd>
</dd><dt><code>+&lt; Ta </code>Pad with a space</dt>
<dd>
</dd><dt><code>+A Ta </code>Output of the external script</dt>
<dd>
</dd><dt><code>+C Ta </code>Window class (from WM_CLASS)</dt>
<dd>
</dd><dt><code>+D Ta </code>Workspace name</dt>
<dd>
</dd><dt><code>+F Ta </code>Floating indicator</dt>
<dd>
</dd><dt><code>+I Ta </code>Workspace index</dt>
<dd>
</dd><dt><code>+M Ta </code>Number of iconic (minimized) windows in workspace</dt>
<dd>
</dd><dt><code>+N Ta </code>Screen number</dt>
<dd>
</dd><dt><code>+P Ta </code>Window class and instance separated by a colon</dt>
<dd>
</dd><dt><code>+S Ta </code>Stacking algorithm</dt>
<dd>
</dd><dt><code>+T Ta </code>Window instance (from WM_CLASS)</dt>
<dd>
</dd><dt><code>+U Ta </code>Urgency hint</dt>
<dd>
</dd><dt><code>+V Ta </code>Program version</dt>
<dd>
</dd><dt><code>+W Ta </code>Window name (from _NET_WM_NAME/WM_NAME)</dt>
<dd>
</dd><dt><code>++ Ta </code>A literal `+&#8217;</dt>
<dd></dd></dl>
<p> All character sequences may limit its output to a specific length, for example +64A. Any characters that don&#8217;t match the specification are copied as-is.</p>
<dt><code>bar_justify</code></dt>
<dd> Justify the status bar text. Possible values are <i>left</i> <i>center</i> and <i>right</i> </dd>
<p> Note that if the output is not left justified, it may not be properly aligned in some circumstances, due to the white-spaces in the default static format. See the <code>bar_format</code> option for more details.</p>
<dt><code>bind Bq </code><i>x</i></dt>
<dd> Bind key combo to action <i>x</i> See the Sx BINDINGS section below.</dd>
<dt><code>border_width</code></dt>
<dd> Set window border thickness in pixels. Disable all borders by setting to 0.</dd>
<dt><code>boundary_width</code></dt>
<dd> Set region containment boundary width in pixels. This is how far a window must be dragged/resized beyond the region edge before it is allowed outside the region. This has no effect when manipulating the window with key bindings. Disable the window containment effect by setting to 0.</dd>
<dt><code>clock_enabled</code></dt>
<dd> Enable or disable displaying the clock in the status bar. Disable by setting to 0 so a custom clock could be used in the <code>bar_action</code> script.</dd>
<dt><code>iconic_enabled</code></dt>
<dd> Display the number of iconic (minimized) windows in the status bar. Enable by setting to 1.</dd>
<dt><code>color_focus</code></dt>
<dd> Border color of the currently focused window. Default is red.</dd>
<dt><code>color_focus_maximized</code></dt>
<dd> Border color of the currently focused, maximized window. Defaults to the value of <code>color_focus</code></dd>
<dt><code>color_unfocus</code></dt>
<dd> Border color of unfocused windows, default is rgb:88/88/88.</dd>
<dt><code>color_unfocus_maximized</code></dt>
<dd> Border color of unfocused, maximized windows. Defaults to the value of <code>color_unfocus</code></dd>
<dt><code>dialog_ratio</code></dt>
<dd> Some applications have dialogue windows that are too small to be useful. This ratio is the screen size to what they will be resized. For example, 0.6 is 60% of the physical screen size.</dd>
<dt><code>disable_border</code></dt>
<dd> Remove border when bar is disabled and there is only one window on the region.</dd>
<dt><code>focus_close</code></dt>
<dd> Window to put focus when the focused window is closed. Possible values are <i>first</i> <i>next</i> <i>previous</i> (default) and <i>last</i> <i>next</i> and <i>previous</i> are relative to the window that is closed.</dd>
<dt><code>focus_close_wrap</code></dt>
<dd> Whether to allow the focus to jump to the last window when the first window is closed or vice versa. Disable by setting to 0.</dd>
<dt><code>focus_default</code></dt>
<dd> Window to put focus when no window has been focused. Possible values are <i>first</i> and <i>last</i> (default).</dd>
<dt><code>focus_mode</code></dt>
<dd> Window focus behavior with respect to the mouse cursor. Possible values: </dd>
<dl>
<dt><i>default</i></dt>
<dd> Set window focus on border crossings caused by cursor motion and window interaction.</dd>
<dt><i>follow</i></dt>
<dd> Set window focus on all cursor border crossings, including workspace switches and changes to layout.</dd>
<dt><i>manual</i></dt>
<dd> Set window focus on window interaction only.</dd></dl>
<dt><code>java_workaround</code></dt>
<dd> Workaround a Java GUI rendering issue on non-reparenting window managers by impersonating the LG3D window manager, written by Sun. Default is 1.</dd>
<dt><code>keyboard_mapping</code></dt>
<dd> Clear all key bindings and load new key bindings from the specified file. This allows you to load pre-defined key bindings for your keyboard layout. See the Sx KEYBOARD MAPPING FILES section below for a list of keyboard mapping files that have been provided for several keyboard layouts.</dd>
<dt><code>layout</code></dt>
<dd> Select layout to use at start-of-day. Defined in the format <code>ws Bo </code><i>idx Bc </i>: <i>master_grow : </i><i>master_add : </i><i>stack_inc : </i><i>always_raise : </i><i>stack_mode</i> e.g. ws[2]:-4:0:1:0:horizontal sets worskspace 2 to the horizontal stack mode, shrinks the master area by 4 ticks and adds one window to the stack, while maintaining default floating window behavior. Possible <i>stack_mode</i> values are <i>vertical</i> <i>vertical_flip</i> <i>horizontal</i> <i>horizontal_flip</i> and <i>fullscreen</i> </dd>
<p> See <code>master_grow</code> <code>master_shrink</code> <code>master_add</code> <code>master_del</code> <code>stack_inc</code> <code>stack_dec</code> and <code>always_raise</code> for more information. Note that the stacking options are complicated and have side-effects. One should familiarize oneself with these commands before experimenting with the <code>layout</code> option. </p>
<p> This setting is not retained at restart.</p>
<dt><code>modkey</code></dt>
<dd> Change mod key. Mod1 is generally the ALT key and Mod4 is the windows key on a PC.</dd>
<dt><code>name</code></dt>
<dd> Set the name of a workspace at start-of-day. Defined in the format <code>ws Bo </code><i>idx Bc </i>: <i>name</i> e.g. ws[1]:Console sets the name of workspace 1 to &#8220;Console&#8221;</dd>
<dt><code>program Bq </code><i>p</i></dt>
<dd> Define new action to spawn a program <i>p</i> See the Sx PROGRAMS section below.</dd>
<dt><code>quirk Bq </code><i>c </i><code>: </code><i>i </i><code>: </code><i>n</i></dt>
<dd> Add &quot;quirk&quot; for windows with class <i>c</i> instance <i>i</i> and name <i>n</i> See the Sx QUIRKS section below.</dd>
<dt><code>region</code></dt>
<dd> Allocates a custom region, removing any autodetected regions which occupy the same space on the screen. Defined in the format <code>screen Bo </code><i>idx </i><code>Bc </code>: <i>width </i><code>x </code><i>height </i><code>+ </code><i>x </i><code>+ </code><i>y</i> e.g. screen[1]:800&#215;1200+0+0. </dd>
<p> To make a region span multiple monitors, create a region big enough to cover them all, e.g. screen[1]:2048&#215;768+0+0 makes the region span two monitors with 1024&#215;768 resolution sitting one next to the other.</p>
<dt><code>region_padding</code></dt>
<dd> Pixel width of empty space within region borders. Disable by setting to 0.</dd>
<dt><code>spawn_position</code></dt>
<dd> Position in stack to place newly spawned windows. Possible values are <i>first</i> <i>next</i> <i>previous</i> and <i>last</i> (default). <i>next</i> and <i>previous</i> are relative to the focused window.</dd>
<dt><code>stack_enabled</code></dt>
<dd> Enable or disable displaying the current stacking algorithm in the status bar.</dd>
<dt><code>term_width</code></dt>
<dd> Set a preferred minimum width for the terminal. If this value is greater than 0, <code>spectrwm</code> will attempt to adjust the font sizes in the terminal to keep the terminal width above this number as the window is resized. Only <a href="/docs/linux/man/1-xterm/">xterm</a>(1) is currently supported. The <a href="/docs/linux/man/1-xterm/">xterm</a>(1) binary must not be setuid or setgid, which it is by default on most systems. Users may need to set program[term] (see the Sx PROGRAMS section) to use an alternate copy of the <a href="/docs/linux/man/1-xterm/">xterm</a>(1) binary without the setgid bit set.</dd>
<dt><code>tile_gap</code></dt>
<dd> Pixel width of empty space between tiled windows. Negative values cause overlap. Set this to the opposite of <code>border_width</code> to collapse the border between tiles. Disable by setting to 0.</dd>
<dt><code>urgent_collapse</code></dt>
<dd> Enables hiding of placeholders in the urgency hint indicator for workspaces that do not have any urgent windows. Enable by setting to 1.</dd>
<dt><code>urgent_enabled</code></dt>
<dd> Enable or disable the urgency hint indicator in the status bar. Note that many terminal emulators require an explicit setting for the bell character to trigger urgency on the window. In <a href="/docs/linux/man/1-xterm/">xterm</a>(1), for example, one needs to add the following line to .Xdefaults </dd>
<blockquote>
<pre>
xterm.bellIsUrgent: true
</pre>
</blockquote>
<dt><code>verbose_layout</code></dt>
<dd> Enable or disable displaying the current master window count and stack column/row count in the status bar. Enable by setting to 1. See <i>master_add</i> <i>master_del</i> <i>stack_inc</i> and <i>stack_dec</i> for more information.</dd>
<dt><code>window_class_enabled</code></dt>
<dd> Enable or disable displaying the window class name (from WM_CLASS) in the status bar. Enable by setting to 1.</dd>
<dt><code>window_instance_enabled</code></dt>
<dd> Enable or disable displaying the window instance name (from WM_CLASS) in the status bar. Enable by setting to 1.</dd>
<dt><code>window_name_enabled</code></dt>
<dd> Enable or disable displaying the window display name (from _NET_WM_NAME/WM_NAME) in the status bar. Enable by setting to 1. </dd>
<p> To prevent excessively large window names from pushing the remaining text off the bar, it&#8217;s limited to 64 characters, by default. See the <code>bar_format</code> option for more details.</p>
<dt><code>warp_pointer</code></dt>
<dd> Centers the mouse pointer on the focused window when using key bindings to change focus, switch workspaces, change regions, etc. Enable by setting to 1.</dd>
<dt><code>workspace_limit</code></dt>
<dd> Set the total number of workspaces available. Minimum is 1, maximum is 22, default is 10.</dd></dl>
<h2>PROGRAMS</h2>
<p> <code>spectrwm</code> allows you to define custom actions to launch programs of your choice and then bind them the same as with built-in actions. See the Sx BINDINGS section below. </p>
<p> Custom programs in the configuration file are specified as follows: </p>
<blockquote><p><tt>program </tt><code>Bo </code><i>action Bc </i>= <i>progpath </i>[<i>arg </i>[<i>arg &#8230;</i> ] ] </p></blockquote>
<p> <i>action</i> is any identifier that does not conflict with a built-in action or keyword, <i>progpath</i> is the desired program, and <i>arg</i> is zero or more arguments to the program. </p>
<p> Remember that when using `#&#8217; in your program call, it must be escaped with a backslash, i.e. \# </p>
<p> The following argument variables will be substituted for values at the time the program is spawned: </p>
<dl>
<dt><code>$bar_border</code></dt>
<dd>
</dd><dt><code>$bar_color</code></dt>
<dd>
</dd><dt><code>$bar_font</code></dt>
<dd>
</dd><dt><code>$bar_font_color</code></dt>
<dd>
</dd><dt><code>$color_focus</code></dt>
<dd>
</dd><dt><code>$color_unfocus</code></dt>
<dd>
</dd><dt><code>$dmenu_bottom</code></dt>
<dd> -b if <code>bar_at_bottom</code> is enabled.</dd>
<dt><code>$region_index</code></dt>
<dd>
</dd><dt><code>$workspace_index</code></dt>
<dd></dd></dl>
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
<dt><code>lock</code></dt>
<dd> xlock</dd>
<dt><code>menu</code></dt>
<dd> dmenu_run $dmenu_bottom -fn $bar_font -nb $bar_color -nf $bar_font_color -sb $bar_border -sf $bar_color</dd>
<dt><code>term</code></dt>
<dd> xterm</dd>
<dt><code>initscr</code></dt>
<dd> initscreen.sh # optional</dd>
<dt><code>screenshot_all</code></dt>
<dd> screenshot.sh full # optional</dd>
<dt><code>screenshot_wind</code></dt>
<dd> screenshot.sh window # optional</dd></dl>
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
<dt><code>M1</code></dt>
<dd> Focus window</dd>
<dt><code>M-M1</code></dt>
<dd> Move window</dd>
<dt><code>M-M3</code></dt>
<dd> Resize window</dd>
<dt><code>M-S-M3</code></dt>
<dd> Resize window while maintaining it centered</dd></dl>
<p> The default key bindings are described below: </p>
<dl>
<dt><code>M-S- Aq </code><code>Return</code></dt>
<dd> term</dd>
<dt><code>M-p</code></dt>
<dd> menu</dd>
<dt><code>M-S-q</code></dt>
<dd> quit</dd>
<dt><code>M-q</code></dt>
<dd> restart</dd>
<dt><code>M- Aq </code><code>Space</code></dt>
<dd> cycle_layout</dd>
<dt><code>M-S-\</code></dt>
<dd> flip_layout</dd>
<dt><code>M-S- Aq </code><code>Space</code></dt>
<dd> stack_reset</dd>
<dt><code>M-h</code></dt>
<dd> master_shrink</dd>
<dt><code>M-l</code></dt>
<dd> master_grow</dd>
<dt><code>M-,</code></dt>
<dd> master_add</dd>
<dt><code>M-.</code></dt>
<dd> master_del</dd>
<dt><code>M-S-,</code></dt>
<dd> stack_inc</dd>
<dt><code>M-S-.</code></dt>
<dd> stack_dec</dd>
<dt><code>M- Aq </code><code>Return</code></dt>
<dd> swap_main</dd>
<dt> <code>M-j</code> <code>M- Aq </code><code>TAB</code></dt>
<dd>
</dd><dd>focus_next</dd>
<dt> <code>M-k</code> <code>M-S- Aq </code><code>TAB</code></dt>
<dd>
</dd><dd>focus_prev</dd>
<dt><code>M-m</code></dt>
<dd> focus_main</dd>
<dt><code>M-u</code></dt>
<dd> focus_urgent</dd>
<dt><code>M-S-j</code></dt>
<dd> swap_next</dd>
<dt><code>M-S-k</code></dt>
<dd> swap_prev</dd>
<dt><code>M-b</code></dt>
<dd> bar_toggle</dd>
<dt><code>M-S-b</code></dt>
<dd> bar_toggle_ws</dd>
<dt><code>M-x</code></dt>
<dd> wind_del</dd>
<dt><code>M-S-x</code></dt>
<dd> wind_kill</dd>
<dt><code>M- Aq </code><i>1-9,0,F1-F12</i></dt>
<dd> ws_ Aq <i>1-22</i></dd>
<dt><code>M-S- Aq </code><i>1-9,0,F1-F12</i></dt>
<dd> mvws_ <code>Aq </code><i>1-22</i></dd>
<dt><code>M- Aq </code><i>Keypad 1-9</i></dt>
<dd> rg_ Aq <i>1-9</i></dd>
<dt><code>M-S- Aq </code><i>Keypad 1-9</i></dt>
<dd> mvrg_ Aq <i>1-9</i></dd>
<dt><code>M- Aq </code><code>Right</code></dt>
<dd> ws_next</dd>
<dt><code>M- Aq </code><code>Left</code></dt>
<dd> ws_prev</dd>
<dt><code>M- Aq </code><code>Up </code>ws_next_all</dt>
<dd>
</dd><dt><code>M- Aq </code><code>Down</code></dt>
<dd> ws_prev_all</dd>
<dt><code>M-a</code></dt>
<dd> ws_next_move</dd>
<dt><code>M-S- Aq </code><code>Left</code></dt>
<dd> ws_prev_move</dd>
<dt><code>M-S- Aq </code><code>Up </code>ws_prior</dt>
<dd>
</dd><dt><code>M-S- Aq </code><code>Right</code></dt>
<dd> rg_next</dd>
<dt><code>M-S- Aq </code><code>Left</code></dt>
<dd> rg_prev</dd>
<dt><code>M-s</code></dt>
<dd> screenshot_all</dd>
<dt><code>M-S-s</code></dt>
<dd> screenshot_wind</dd>
<dt><code>M-S-v</code></dt>
<dd> version</dd>
<dt><code>M-t</code></dt>
<dd> float_toggle</dd>
<dt><code>M-S- Aq </code><code>Delete</code></dt>
<dd> lock</dd>
<dt><code>M-S-i</code></dt>
<dd> initscr</dd>
<dt><code>M-w</code></dt>
<dd> iconify</dd>
<dt><code>M-S-w</code></dt>
<dd> uniconify</dd>
<dt><code>M-e</code></dt>
<dd> maximize_toggle</dd>
<dt><code>M-S-r</code></dt>
<dd> always_raise</dd>
<dt><code>M-v</code></dt>
<dd> button2</dd>
<dt><code>M&#8211;</code></dt>
<dd> width_shrink</dd>
<dt><code>M-=</code></dt>
<dd> width_grow</dd>
<dt><code>M-S&#8211;</code></dt>
<dd> height_shrink</dd>
<dt><code>M-S-=</code></dt>
<dd> height_grow</dd>
<dt><code>M-[</code></dt>
<dd> move_left</dd>
<dt><code>M-]</code></dt>
<dd> move_right</dd>
<dt><code>M-S-[</code></dt>
<dd> move_up</dd>
<dt><code>M-S-]</code></dt>
<dd> move_down</dd>
<dt><code>M-S-/</code></dt>
<dd> name_workspace</dd>
<dt><code>M-/</code></dt>
<dd> search_workspace</dd>
<dt><code>M-f</code></dt>
<dd> search_win</dd></dl>
<p> The action names and descriptions are listed below: </p>
<dl>
<dt><code>term</code></dt>
<dd> Spawn a new terminal (see Sx PROGRAMS above).</dd>
<dt><code>menu</code></dt>
<dd> Menu (see Sx PROGRAMS above).</dd>
<dt><code>quit</code></dt>
<dd> Quit <code>.</code></dd>
<dt><code>restart</code></dt>
<dd> Restart <code>.</code></dd>
<dt><code>cycle_layout</code></dt>
<dd> Cycle layout.</dd>
<dt><code>flip_layout</code></dt>
<dd> Swap the master and stacking areas.</dd>
<dt><code>stack_reset</code></dt>
<dd> Reset layout.</dd>
<dt><code>master_shrink</code></dt>
<dd> Shrink master area.</dd>
<dt><code>master_grow</code></dt>
<dd> Grow master area.</dd>
<dt><code>master_add</code></dt>
<dd> Add windows to master area.</dd>
<dt><code>master_del</code></dt>
<dd> Remove windows from master area.</dd>
<dt><code>stack_inc</code></dt>
<dd> Add columns/rows to stacking area.</dd>
<dt><code>stack_dec</code></dt>
<dd> Remove columns/rows from stacking area.</dd>
<dt><code>swap_main</code></dt>
<dd> Move current window to master area.</dd>
<dt><code>focus_next</code></dt>
<dd> Focus next window in workspace.</dd>
<dt><code>focus_prev</code></dt>
<dd> Focus previous window in workspace.</dd>
<dt><code>focus_main</code></dt>
<dd> Focus on main window in workspace.</dd>
<dt><code>focus_urgent</code></dt>
<dd> Focus on next window with the urgency hint flag set. The workspace is switched if needed.</dd>
<dt><code>swap_next</code></dt>
<dd> Swap with next window in workspace.</dd>
<dt><code>swap_prev</code></dt>
<dd> Swap with previous window in workspace.</dd>
<dt><code>bar_toggle</code></dt>
<dd> Toggle overall visibility of status bars.</dd>
<dt><code>bar_toggle_ws</code></dt>
<dd> Toggle status bar on current workspace.</dd>
<dt><code>wind_del</code></dt>
<dd> Delete current window in workspace.</dd>
<dt><code>wind_kill</code></dt>
<dd> Destroy current window in workspace.</dd>
<dt><code>ws_ </code><i>n</i></dt>
<dd> Switch to workspace <i>n</i> where <i>n</i> is 1 through <code>workspace_limit</code></dd>
<dt><code>mvws_ </code><i>n</i></dt>
<dd> Move current window to workspace <i>n</i> where <i>n</i> is 1 through <code>workspace_limit</code></dd>
<dt><code>rg_ </code><i>n</i></dt>
<dd> Focus on region <i>n</i> where <i>n</i> is 1 through 9.</dd>
<dt><code>mvrg_ </code><i>n</i></dt>
<dd> Move current window to region <i>n</i> where <i>n</i> is 1 through 9.</dd>
<dt><code>ws_next</code></dt>
<dd> Switch to next workspace with a window in it.</dd>
<dt><code>ws_prev</code></dt>
<dd> Switch to previous workspace with a window in it.</dd>
<dt><code>ws_next_all</code></dt>
<dd> Switch to next workspace.</dd>
<dt><code>ws_prev_all</code></dt>
<dd> Switch to previous workspace.</dd>
<dt><code>ws_next_move</code></dt>
<dd> Switch to next workspace with the current window.</dd>
<dt><code>ws_prev_move</code></dt>
<dd> Switch to previous workspace with the current window.</dd>
<dt><code>ws_prior</code></dt>
<dd> Switch to last visited workspace.</dd>
<dt><code>rg_next</code></dt>
<dd> Switch to next region.</dd>
<dt><code>rg_prev</code></dt>
<dd> Switch to previous region.</dd>
<dt><code>screenshot_all</code></dt>
<dd> Take screenshot of entire screen (if enabled) (see Sx PROGRAMS above).</dd>
<dt><code>screenshot_wind</code></dt>
<dd> Take screenshot of selected window (if enabled) (see Sx PROGRAMS above).</dd>
<dt><code>version</code></dt>
<dd> Toggle version in status bar.</dd>
<dt><code>float_toggle</code></dt>
<dd> Toggle focused window between tiled and floating.</dd>
<dt><code>lock</code></dt>
<dd> Lock screen (see Sx PROGRAMS above).</dd>
<dt><code>initscr</code></dt>
<dd> Reinitialize physical screens (see Sx PROGRAMS above).</dd>
<dt><code>iconify</code></dt>
<dd> Minimize (unmap) currently focused window.</dd>
<dt><code>uniconify</code></dt>
<dd> Restore (map) window returned by <a href="/docs/linux/man/1-dmenu/">dmenu</a>(1) selection.</dd>
<dt><code>maximize_toggle</code></dt>
<dd> Toggle maximization of focused window.</dd>
<dt><code>always_raise</code></dt>
<dd> When set tiled windows are allowed to obscure floating windows.</dd>
<dt><code>button2</code></dt>
<dd> Fake a middle mouse button click (mouse button 2).</dd>
<dt><code>width_shrink</code></dt>
<dd> Shrink the width of a floating window.</dd>
<dt><code>width_grow</code></dt>
<dd> Grow the width of a floating window.</dd>
<dt><code>height_shrink</code></dt>
<dd> Shrink the height of a floating window.</dd>
<dt><code>height_grow</code></dt>
<dd> Grow the height of a floating window.</dd>
<dt><code>move_left</code></dt>
<dd> Move a floating window a step to the left.</dd>
<dt><code>move_right</code></dt>
<dd> Move a floating window a step to the right.</dd>
<dt><code>move_up</code></dt>
<dd> Move a floating window a step upwards.</dd>
<dt><code>move_down</code></dt>
<dd> Move a floating window a step downwards.</dd>
<dt><code>name_workspace</code></dt>
<dd> Name the current workspace.</dd>
<dt><code>search_workspace</code></dt>
<dd> Search for a workspace.</dd>
<dt><code>search_win</code></dt>
<dd> Search the windows in the current workspace.</dd></dl>
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
<dt><code>spectrwm_cz.conf</code></dt>
<dd> Czech Republic keyboard layout</dd>
<dt><code>spectrwm_es.conf</code></dt>
<dd> Spanish keyboard layout</dd>
<dt><code>spectrwm_fr.conf</code></dt>
<dd> French keyboard layout</dd>
<dt><code>spectrwm_fr_ch.conf</code></dt>
<dd> Swiss French keyboard layout</dd>
<dt><code>spectrwm_se.conf</code></dt>
<dd> Swedish keyboard layout</dd>
<dt><code>spectrwm_us.conf</code></dt>
<dd> United States keyboard layout</dd></dl>
<h2>QUIRKS</h2>
<p> <code>spectrwm</code> provides &quot;quirks&quot; which handle windows that must be treated specially in a tiling window manager, such as some dialogs and fullscreen apps. </p>
<p> The default quirks are described below: </p>
<dl>
<dt><code>Firefox-bin:firefox-bin</code></dt>
<dd> TRANSSZ</dd>
<dt><code>Firefox:Dialog</code></dt>
<dd> FLOAT</dd>
<dt><code>Gimp:gimp</code></dt>
<dd> FLOAT + ANYWHERE</dd>
<dt><code>MPlayer:xv</code></dt>
<dd> FLOAT + FULLSCREEN + FOCUSPREV</dd>
<dt><code>OpenOffice.org 2.4:VCLSalFrame</code></dt>
<dd> FLOAT</dd>
<dt><code>OpenOffice.org 3.1:VCLSalFrame</code></dt>
<dd> FLOAT</dd>
<dt><code>pcb:pcb</code></dt>
<dd> FLOAT</dd>
<dt><code>xine:Xine Window</code></dt>
<dd> FLOAT + ANYWHERE</dd>
<dt><code>xine:xine Panel</code></dt>
<dd> FLOAT + ANYWHERE</dd>
<dt><code>xine:xine Video Fullscreen Window</code></dt>
<dd> FULLSCREEN + FLOAT</dd>
<dt><code>Xitk:Xitk Combo</code></dt>
<dd> FLOAT + ANYWHERE</dd>
<dt><code>Xitk:Xine Window</code></dt>
<dd> FLOAT + ANYWHERE</dd>
<dt><code>XTerm:xterm</code></dt>
<dd> XTERM_FONTADJ</dd></dl>
<p> The quirks themselves are described below: </p>
<dl>
<dt><code>FLOAT</code></dt>
<dd> This window should not be tiled, but allowed to float freely.</dd>
<dt><code>TRANSSZ</code></dt>
<dd> Adjusts size on transient windows that are too small using <code>dialog_ratio</code> (see Sx CONFIGURATION FILES ) .</dd>
<dt><code>ANYWHERE</code></dt>
<dd> Allow window to position itself, uncentered.</dd>
<dt><code>XTERM_FONTADJ</code></dt>
<dd> Adjust <a href="/docs/linux/man/1-xterm/">xterm</a>(1) fonts when resizing.</dd>
<dt><code>FULLSCREEN</code></dt>
<dd> Remove border to allow window to use full region size.</dd>
<dt><code>FOCUSPREV</code></dt>
<dd> On exit force focus on previously focused application not previous application in the stack.</dd>
<dt><code>NOFOCUSONMAP</code></dt>
<dd> Don&#8217;t change focus to the window when it first appears on the screen. Has no effect when <code>focus_mode</code> is set to <i>follow</i></dd>
<dt><code>FOCUSONMAP_SINGLE</code></dt>
<dd> When the window first appears on the screen, change focus to the window if there are no other windows on the workspace with the same WM_CLASS class/instance value. Has no effect when <code>focus_mode</code> is set to <i>follow</i></dd>
<dt><code>OBEYAPPFOCUSREQ</code></dt>
<dd> When an application requests focus on the window via a _NET_ACTIVE_WINDOW client message (source indication of 1), comply with the request. Note that a source indication of 0 (unspecified) or 2 (pager) are always obeyed.</dd>
<dt><code>IGNOREPID</code></dt>
<dd> Ignore the PID when determining the initial workspace for a new window. Especially useful for terminal windows that share a process.</dd>
<dt><code>IGNORESPAWNWS</code></dt>
<dd> Ignore the spawn workspace when determining the initial workspace for a new window.</dd>
<dt><code>WS Bq </code><i>n</i></dt>
<dd> Force a new window to appear on workspace <i>n</i></dd></dl>
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
<dt><code>_NET_WM_WINDOW_TYPE_DOCK</code></dt>
<dd> FLOAT + ANYWHERE</dd>
<dt><code>_NET_WM_WINDOW_TYPE_TOOLBAR</code></dt>
<dd> FLOAT + ANYWHERE</dd>
<dt><code>_NET_WM_WINDOW_TYPE_UTILITY</code></dt>
<dd> FLOAT + ANYWHERE</dd>
<dt><code>_NET_WM_WINDOW_TYPE_SPLASH</code></dt>
<dd> FLOAT</dd>
<dt><code>_NET_WM_WINDOW_TYPE_DIALOG</code></dt>
<dd> FLOAT</dd></dl>
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
<dt><code>~/.spectrwm.conf </code></dt>
<dd> <code>spectrwm</code> user specific settings.</dd>
<dt><code>/etc/spectrwm.conf </code></dt>
<dd> <code>spectrwm</code> global settings.</dd></dl>
<h2>HISTORY</h2>
<p> <code>spectrwm</code> was inspired by xmonad &amp; dwm.</p>
<h2>AUTHORS</h2>
<p> An -nosplit <code>spectrwm</code> was written by: </p>
<dl>
<dt><code>Marco Peereboom Aq </code>marco [at] peereboom.us</dt>
<dd>
</dd><dt><code>Ryan Thomas McBride Aq </code>mcbride [at] countersiege.com</dt>
<dd>
</dd><dt><code>Darrin Chandler Aq </code>dwchandler [at] stilyagin.com</dt>
<dd>
</dd><dt><code>Pierre-Yves Ritschard Aq </code>pyr [at] spootnik.org</dt>
<dd>
</dd><dt><code>Tuukka Kataja Aq </code>stuge [at] xor.fi</dt>
<dd>
</dd><dt><code>Jason L. Wright Aq </code>jason [at] thought.net</dt>
<dd>
</dd><dt><code>Reginald Kennedy Aq </code>rk [at] rejii.com</dt>
<dd>
</dd><dt><code>Lawrence Teo Aq </code>lteo [at] lteo.net</dt>
<dd>
</dd><dt><code>Tiago Cunha Aq </code>tcunha [at] gmx.com</dt>
<dd>
</dd><dt><code>David Hill Aq </code>dhill [at] mindcry.org</dt>
<dd></dd></dl>
