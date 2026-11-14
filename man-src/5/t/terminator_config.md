---
title: "terminator_config(5)"
name: "terminator_config"
section: "5"
letter: "t"
url: "/docs/linux/man/5-terminator_config/"
description: "~/.config/terminator/config – the config file for Terminator terminal emulator."
---

<p>~/.config/terminator/config &#8211; the config file for Terminator terminal emulator.</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>Terminator</code> config file. Terminator manages its configuration file via the ConfigObj library to combine flexibility with clear, human editable files. As of version 0.90, Terminator offers a full GUI preferences editor which automatically saves its config file so you don&#8217;t need to write a config file by hand. </p>
<h2>File Location</h2>
<p>Normally the config file will be ~/.config/terminator/config, but it may be overridden with $XDG_CONFIG_HOME (in which case it will be $XDG_CONFIG_HOME/terminator/config)</p>
<h2>File Format</h2>
<p>This is what a Terminator config file should look like: </p>
<p>&nbsp;<wbr>&nbsp;#&nbsp;This is a comment<br />
&nbsp;<wbr>&nbsp;[global_config]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;focus&nbsp;=&nbsp;system </p>
<p>&nbsp;<wbr>&nbsp;[keybindings]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;full_screen&nbsp;=&nbsp;&lt;Ctrl&gt;&lt;Shift&gt;F11 </p>
<p>&nbsp;<wbr>&nbsp;[profiles]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[[default]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;font&nbsp;=&nbsp;Fixed 10<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;background_color&nbsp;=&nbsp;&quot;#000000&quot;&nbsp;#&nbsp;A comment<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;foreground_color&nbsp;=&nbsp;&quot;#FFFFFF&quot;&nbsp;#&nbsp;Note that hex colour values must be quoted<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;scrollback_lines&nbsp;=&nbsp;&#8216;500&#8217;&nbsp;#More comment. Single quotes are valid too<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cursor_blink&nbsp;=&nbsp;True<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;custom_command&nbsp;=&nbsp;&quot;echo&nbsp;\&quot;foo#bar\&quot;&quot;&nbsp;#Final comment &#8211; this will work as expected. </p>
<p> Below are the individual sections that can exist in the config file:</p>
<h2>global_config</h2>
<p>These are the options Terminator currently supports in the global_config section:</p>
<dl>
<dt><code>dbus</code></p>
<dd>Control whether or not Terminator will load its DBus server. When this server is loaded, running Terminator multiple times will cause the first Terminator process to open additional windows. If this configuration item is set to False, or the python dbus module is unavailable, running Terminator multiple times will run a separate Terminator process for each invocation. Default value: <code>True</code></p>
<dt><code>focus</code></p>
<dd>Control how focus is given to terminals. &#8216;click&#8217; means the focus only moves to a terminal after you click in it. &#8216;sloppy&#8217; means the focus will follow the mouse pointer. &#8216;system&#8217; means the focus will match that used by a GNOME window manager. Default value: <code>click</code></p>
<dt><code>handle_size</code></p>
<dd>Controls the width of the separator between terminals. Anything outside the range 0-20 (inclusive) will be ignored and use your default theme value. Default value: <code>-1</code></p>
<dt><code>geometry_hinting</code></p>
<dd>If True the window will resize in step with font sizes, if False it will follow pixels Default value: <code>False</code></p>
<dt><code>window_state</code></p>
<dd>When set to &#8216;normal&#8217; the Terminator window opens normally. &#8216;maximise&#8217; opens the window in a maximised state, &#8216;fullscreen&#8217; in a fullscreen state and &#8216;hidden&#8217; will make it not shown by default. Default value: <code>normal</code></p>
<dt><code>borderless </code>(boolean)</p>
<dd>Controls whether the Terminator window will be started without window borders Default value: <code>False</code></p>
<dt><code>tab_position</code></p>
<dd>Defines where tabs are placed. Can be any of: top, left, right, bottom. If this is set to &quot;hidden&quot;, the tab bar will not be shown. Note that hiding the tab bar is very confusing and not recommended. Default value: <code>top</code></p>
<dt><code>broadcast_default</code></p>
<dd>Defines default broadcast behavior. Can be any of: all, group, off. Default value: <code>group</code></p>
<dt><code>close_button_on_tab </code>(boolean)</p>
<dd>If set to True, tabs will have a close button on them. Default value: <code>True</code></p>
<dt><code>hide_tabbar </code>(boolean)</p>
<dd>If set to True, the tab bar will be hidden. This means there will be no visual indication of either how many tabs there are, or which one you are on. Be warned that this can be very confusing and hard to use. <code>NOTE: THIS OPTION IS DEPRECATED, USE tab_position INSTEAD</code> Default value: <code>False</code></p>
<dt><code>scroll_tabbar </code>(boolean)</p>
<dd>If set to True, the tab bar will not fill the width of the window. The titlebars of the tabs will only take as much space as is necessary for the text they contain. Except, that is, if the tabs no longer fit the width of the window &#8211; in that case scroll buttons will appear to move through the tabs. Default value: <code>False</code></p>
<dt><code>try_posix_regexp </code>(boolean)</p>
<dd>If set to True, URL matching regexps will try to use POSIX style first, and fall back on GNU style on failure. If you are on Linux but URL matches don&#8217;t work, try setting this to True. If you are not on Linux, but you get VTE warnings on startup saying &quot;Error compiling regular expression&quot;, set this to False to silence them (they are otherwise harmless). Default value: <code>False</code> on Linux, <code>True</code> otherwise.</p>
<dt><code>use_custom_url_handler </code>(boolean)</p>
<dd>If set to True, URL handling will be given over entirely to the program specified by &#8216;custom_url_handler&#8217;. Default value: <code>False</code></p>
<dt><code>custom_url_handler </code>(string)</p>
<dd>Path to a program which accepts a URI as an argument and does something relevant with it. This option is ignored unless &#8216;use_custom_url_handler&#8217; is set to True. Default value: unset</p>
<dt><code>disable_real_transparency </code>(string)</p>
<dd>If this is set to True, Terminator will never try to use &#8216;real&#8217; transparency if your windowing environment supports it. Instead it will use &#8216;fake&#8217; transparency where a background image is shown, but other windows are not. Default value: False</p>
<dt><code>title_transmit_fg_color</code></p>
<dd>Sets the colour of the text shown in the titlebar of the active terminal. Default value: <code>&#8216;#FFFFFF&#8217;</code></p>
<dt><code>title_transmit_bg_color</code></p>
<dd>Sets the colour of the background of the titlebar in the active terminal. Default value: <code>&#8216;#C80003&#8217;</code></p>
<dt><code>title_receive_fg_color</code></p>
<dd>Sets the colour of the text shown in the titlebar of any terminal that <code>will</code> receive input from the active terminal. Default value: <code>&#8216;#FFFFFF&#8217;</code></p>
<dt><code>title_receive_bg_color</code></p>
<dd>Sets the colour of the background of the titlebar of any terminal that <code>will</code> receive input from the active terminal. Default value: <code>&#8216;#0076C9&#8217;</code></p>
<dt><code>title_inactive_fg_color</code></p>
<dd>Sets the colour of the text shown in the titlebar of any terminal that will <code>not</code> receive input from the active terminal. Default value: <code>&#8216;#000000&#8217;</code></p>
<dt><code>title_inactive_bg_color</code></p>
<dd>Sets the colour of the background of the titlebar of any terminal that will <code>not</code> receive input from the active terminal. Default value: <code>&#8216;#C0BEBF&#8217;</code></p>
<dt><code>title_use_system_font </code>(boolean)</p>
<dd>Whether or not to use the GNOME default proportional font for titlebars. Default value: <code>True</code></p>
<dt><code>title_font </code>(string)</p>
<dd>An Pango font name. Examples are &quot;Sans 12&quot; or &quot;Monospace Bold 14&quot;. Default value: <code>&quot;Sans 9&quot;</code></p>
<dt><code>inactive_color_offset</code></p>
<dd>Controls how much to reduce the colour values of fonts in terminals that do not have focus. It is a simple multiplication factor. A font colour that was RGB(200,200,200) with an inactive_color_offset of 0.5 would set inactive terminals to RGB(100,100,100).</p>
<dt><code>always_split_with_profile</code></p>
<dd>Controls whether splits/tabs will continue to use the profile of their peer terminal. If set to False, they will always use the default profile. Default value: <code>False</code></p>
<dt><code>putty_paste_style </code>(boolean)</p>
<dd>If set to True, right-click will paste the Primary selection, middle-click will popup the context menu. Default value: <code>False</code></p>
<dt><code>smart_copy </code>(boolean)</p>
<dd>If set to True, and there is no selection, the shortcut is allowed to pass through. This is useful for overloading Ctrl-C to copy a selection, or send the SIGINT to the current process if there is no selection. If False the shortcut does not pass through at all, and the SIGINT does not get sent. Default value: <code>True</code></p>
<dt><code>enabled_plugins</code></p>
<dd>A list of plugins which should be loaded by default. All other plugin classes will be ignored. The default value includes two plugins related to Launchpad, which are enabled by default to provide continuity with earlier releases where these were the only substantial plugins available, and all plugins were loaded by default. Default value: <code>&quot;LaunchpadBugURLHandler, LaunchpadCodeURLHandler&quot;</code> </p>
</dl>
<h2>keybindings</h2>
<p>These are the options Terminator currently supports in the keybindings section:</p>
<dl>
<dt><code>zoom_in</code></p>
<dd>Make font one unit larger. Default value: <code>&lt;Ctrl&gt;plus</code></p>
<dt><code>zoom_out</code></p>
<dd>Make font one unit smaller. Default value: <code>&lt;Ctrl&gt;minus</code></p>
<dt><code>zoom_normal</code></p>
<dd>Return font to pre-configured size. Default value: <code>&lt;Ctrl&gt;0</code></p>
<dt><code>new_tab</code></p>
<dd>Open a new tab. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;T</code></p>
<dt><code>cycle_next</code></p>
<dd>Cycle forwards through the tabs. Default value: <code>&lt;Ctrl&gt;Tab</code></p>
<dt><code>cycle_prev</code></p>
<dd>Cycle backwards through the tabs. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Tab</code> <code>go_next</code> Move cursor focus to the next tab. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;N</code></p>
<dt><code>go_prev</code></p>
<dd>Move cursor focus to the previous tab. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;P</code></p>
<dt><code>go_up</code></p>
<dd>Move cursor focus to the terminal above. Default value: <code>&lt;Alt&gt;Up</code></p>
<dt><code>go_down</code></p>
<dd>Move cursor focus to the terminal below. Default value: <code>&lt;Alt&gt;Down</code></p>
<dt><code>go_left</code></p>
<dd>Move cursor focus to the terminal to the left. Default value: <code>&lt;Alt&gt;Left</code></p>
<dt><code>go_right</code></p>
<dd>Move cursor focus to the terminal to the right. Default value: <code>&lt;Alt&gt;Right</code></p>
<dt><code>rotate_cw</code></p>
<dd>Rotate terminals clockwise. Default value: <code>&lt;Super&gt;R</code></p>
<dt><code>rotate_ccw</code></p>
<dd>Rotate terminals counter-clockwise. Default value: <code>&lt;Super&gt;&lt;Shift&gt;R</code></p>
<dt><code>split_horiz</code></p>
<dd>Split the current terminal horizontally. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;O</code></p>
<dt><code>split_vert</code></p>
<dd>Split the current terminal vertically. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;E</code></p>
<dt><code>close_term</code></p>
<dd>Close the current terminal. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;W</code></p>
<dt><code>copy</code></p>
<dd>Copy the currently selected text to the clipboard. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;C</code></p>
<dt><code>paste</code></p>
<dd>Paste the current contents of the clipboard. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;V</code></p>
<dt><code>toggle_scrollbar</code></p>
<dd>Show/Hide the scrollbar. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;S</code></p>
<dt><code>search</code></p>
<dd>Search for text in the terminal scrollback history. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;F</code></p>
<dt><code>close_window</code></p>
<dd>Quit Terminator. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Q</code></p>
<dt><code>resize_up</code></p>
<dd>Move the parent dragbar upwards. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Up</code></p>
<dt><code>resize_down</code></p>
<dd>Move the parent dragbar downwards. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Down</code></p>
<dt><code>resize_left</code></p>
<dd>Move the parent dragbar left. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Left</code></p>
<dt><code>resize_right</code></p>
<dd>Move the parent dragbar right. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Right</code></p>
<dt><code>move_tab_right</code></p>
<dd>Swap the current tab with the one to its right. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Page_Down</code></p>
<dt><code>move_tab_left</code></p>
<dd>Swap the current tab with the one to its left. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Page_Up</code></p>
<dt><code>toggle_zoom</code></p>
<dd>Zoom/Unzoom the current terminal to fill the window. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;X</code></p>
<dt><code>scaled_zoom</code></p>
<dd>Zoom/Unzoom the current terminal to fill the window, and scale its font. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;Z</code></p>
<dt><code>next_tab</code></p>
<dd>Move to the next tab. Default value: <code>&lt;Ctrl&gt;Page_Down</code></p>
<dt><code>prev_tab</code></p>
<dd>Move to the previous tab. Default value: <code>&lt;Ctrl&gt;Page_Up</code></p>
<dt><code>switch_to_tab_1 &#8211; switch_to_tab_10</code></p>
<dd>Keys to switch directly to the numbered tab. Note that &lt;Alt&gt;&lt;Shift&gt;1 may need to be provided as &lt;Alt&gt;! or similar, depending on your keyboard layout. Default value: <code>Unbound</code></p>
<dt><code>edit_window_title</code></p>
<dd>Edit the current active window&#8217;s title Default value: <code>&lt;Ctrl&gt;&lt;Alt&gt;W</code></p>
<dt><code>edit_tab_title</code></p>
<dd>Edit the currently active tab&#8217;s title Default value: <code>&lt;Ctrl&gt;&lt;Alt&gt;A</code></p>
<dt><code>edit_terminal_title</code></p>
<dd>Edit the currently active terminal&#8217;s title Default value: <code>&lt;Ctrl&gt;&lt;Alt&gt;X</code></p>
<dt><code>full_screen</code></p>
<dd>Toggle the window to a fullscreen window. Default value: <code>F11</code></p>
<dt><code>reset</code></p>
<dd>Reset the terminal state. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;R</code></p>
<dt><code>reset_clear</code></p>
<dd>Reset the terminal state and clear the terminal window. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;G</code></p>
<dt><code>hide_window</code></p>
<dd>Toggle visibility of the Terminator window. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;&lt;Alt&gt;a</code></p>
<dt><code>group_all</code></p>
<dd>Group all terminals together so input sent to one goes to all of them. Default value: <code>&lt;Super&gt;g</code></p>
<dt><code>ungroup_all</code></p>
<dd>Remove grouping from all terminals. Default value: <code>&lt;Super&gt;&lt;Shift&gt;G</code></p>
<dt><code>group_tab</code></p>
<dd>Group all terminals in the current tab together so input sent to one goes to all of them. Default value: <code>&lt;Super&gt;t</code></p>
<dt><code>ungroup_tab</code></p>
<dd>Remove grouping from all terminals in the current tab. Default value: <code>&lt;Super&gt;&lt;Shift&gt;T</code></p>
<dt><code>new_window</code></p>
<dd>Open a new Terminator window as part of the existing process. Default value: <code>&lt;Ctrl&gt;&lt;Shift&gt;I</code></p>
<dt><code>new_terminator</code></p>
<dd>Spawn a new instance of Terminator. Default value: <code>&lt;Super&gt;i</code> </p>
</dl>
<h2>profiles</h2>
<p>These are the options Terminator currently supports in the profiles section. Each profile should be its own subsection with a header in the format <code>[[name]]</code> </p>
<p> <code>allow_bold</code> (boolean) If true, allow applications in the terminal to make text boldface. Default value: <code>True</code></p>
<dl>
<dt><code>audible_bell</code> (boolean)</p>
<dd>If true, make a noise when applications send the escape sequence for the terminal bell. Default value: <code>False</code></p>
<dt><code>visible_bell</code> (boolean)</p>
<dd>If true, flash the terminal when applications send the escape sequence for the terminal bell. Default value: <code>False</code></p>
<dt><code>urgent_bell</code> (boolean)</p>
<dd>If true, set the window manager &quot;urgent&quot; hint when applications send the escale sequence for the terminal bell. Any keypress will cancel the urgent status. Default value: <code>False</code></p>
<dt><code>icon_bell</code> (boolean)</p>
<dd>If true, briefly show a small icon on the terminal title bar for the terminal bell. Default value: <code>True</code></p>
<dt><code>force_no_bell</code> (boolean)</p>
<dd>If true, don&#8217;t make a noise or flash. All terminal bells will be ignored. Default value: <code>False</code></p>
<dt><code>use_theme_colors</code></p>
<dd>If true, ignore the configured colours and use values from the theme instead. Default value: <code>False</code></p>
<dt><code>bold_is_bright</code></p>
<dd>If true, show bold text with increased brightness. If false, then text boldness can be controlled by applications independently from the text brightness. Default value: <code>False</code></p>
<dt><code>background_color</code></p>
<dd>Default colour of terminal background, as a colour specification (can be HTML-style hex digits, or a colour name such as &quot;red&quot;). <code>Note:</code> You may need to set <code>use_theme_colors=False</code> to force this setting to take effect. Default value: <code>&#8216;#000000&#8217;</code></p>
<dt><code>background_darkness</code></p>
<dd>A value between 0.0 and 1.0 indicating how much to darken the background image. 0.0 means no darkness, 1.0 means fully dark. If the terminal is set to transparent, this setting controls how transparent it is. 0.0 means fully transparent, 1.0 means fully opaque. Default value: <code>0.5</code></p>
<dt><code>background_type</code></p>
<dd>Type of terminal background. May be &quot;solid&quot; for a solid colour or &quot;transparent&quot; for full transparency in compositing window managers. Default value: <code>solid</code></p>
<dt><code>backspace_binding</code></p>
<dd>Sets what code the backspace key generates. Possible values are &quot;ascii-del&quot; for the ASCII DEL character, &quot;control-h&quot; for Control-H (AKA the ASCII BS character), &quot;escape-sequence&quot; for the escape sequence typically bound to backspace or delete. &quot;ascii-del&quot; is normally considered the correct setting for the Backspace key. Default value: <code>ascii-del</code></p>
<dt><code>delete_binding</code></p>
<dd>Sets what code the delete key generates. Possible values are &quot;ascii-del&quot; for the ASCII DEL character, &quot;control-h&quot; for Control-H (AKA the ASCII BS character), &quot;escape-sequence&quot; for the escape sequence typically bound to backspace or delete. &quot;escape-sequence&quot; is normally considered the correct setting for the Delete key. Default value: <code>escape-sequence</code></p>
<dt><code>color_scheme </code>(boolean)</p>
<dd>If specified this sets foreground_color and background_color to pre-set values. Possible options are &#8216;grey_on_black&#8217;, &#8216;black_on_yellow&#8217;, &#8216;black_on_white&#8217;, &#8216;white_on_black&#8217;, &#8216;green_on_black&#8217;, &#8216;orange_on_black&#8217;, &#8216;ambience&#8217;, &#8216;solarized_dark&#8217;, &#8216;solarized_light&#8217;. Default value: grey_on_black</p>
<dt><code>cursor_blink </code>(boolean)</p>
<dd>Controls if the cursor blinks. Default value: <code>True</code></p>
<dt><code>cursor_color</code></p>
<dd>Default colour of cursor, as a colour specification (can be HTML-style hex digits, or a colour name such as &quot;red&quot;). Default value: Current value of <code>foreground_color</code></p>
<dt><code>cursor_shape</code></p>
<dd>Default shape of cursor. Possibilities are &quot;block&quot;, &quot;ibeam&quot;, and &quot;underline&quot;. Default value: <code>block</code></p>
<dt><code>term</code></p>
<dd>This translates into the value that will be set for TERM in the environment of your terminals. Default value: <code>xterm-256color</code></p>
<dt><code>colorterm</code></p>
<dd>This translates into the value that will be set for COLORTERM in the environment of your terminals. Default value: <code>truecolor</code></p>
<dt><code>use_system_font</code></p>
<dd>Whether or not to use the GNOME default monospace font for terminals. Default value: <code>True</code></p>
<dt><code>font</code></p>
<dd>An Pango font name. Examples are &quot;Sans 12&quot; or &quot;Monospace Bold 14&quot;. Default value: <code>Mono 10</code></p>
<dt><code>foreground_color</code></p>
<dd>Default colour of text in the terminal, as a colour specification (can be HTML-style hex digits, or a colour name such as &quot;red&quot;). <code>Note:</code> You may need to set <code>use_theme_colors=False</code> to force this setting to take effect. Default value: <code>&#8216;#AAAAAA&#8217;</code></p>
<dt><code>scrollbar_position</code></p>
<dd>Where to put the terminal scrollbar. Possibilities are &quot;left&quot;, &quot;right&quot;, and &quot;disabled&quot;. Default value: <code>right</code></p>
<dt><code>show_titlebar</code></p>
<dd>If true, a titlebar will be drawn for each terminal which shows the current title of that terminal. Default value: <code>True</code></p>
<dt><code>scroll_background </code>(boolean)</p>
<dd>If true, scroll the background image with the foreground text; if false, keep the image in a fixed position and scroll the text above it. Default value: <code>True</code></p>
<dt><code>scroll_on_keystroke </code>(boolean)</p>
<dd>If true, pressing a key jumps the scrollbar to the bottom. Default value: <code>True</code></p>
<dt><code>scroll_on_output </code>(boolean)</p>
<dd>If true, whenever there&#8217;s new output the terminal will scroll to the bottom. Default value: <code>False</code></p>
<dt><code>scrollback_lines</code></p>
<dd>Number of scrollback lines to keep around. You can scroll back in the terminal by this number of lines; lines that don&#8217;t fit in the scrollback are discarded. Warning: with large values, rewrapping on resize might be slow. Default value: <code>500</code></p>
<dt><code>scrollback_infinite</code></p>
<dd>If this is set to True, scrollback_lines will be ignored and VTE will keep the entire scrollback history. Default value: <code>False</code></p>
<dt><code>focus_on_close</code></p>
<dd>Sets which terminal should get the focus when another terminal is closed. Values can be &quot;prev&quot;, &quot;next&quot; or &quot;auto&quot;. Using &quot;auto&quot;, if the closed terminal is within a split window, the focus will be on the sibling terminal rather than another tab. Default value: <code>auto</code></p>
<dt><code>exit_action</code></p>
<dd>Possible values are &quot;close&quot; to close the terminal, and &quot;restart&quot; to restart the command. Default value: <code>close</code></p>
<dt><code>palette</code></p>
<dd>Terminals have a 16-colour palette that applications inside the terminal can use. This is that palette, in the form of a colon-separated list of colour names. Colour names should be in hex format e.g. &quot;#FF00FF&quot;.</p>
<dt><code>word_chars</code></p>
<dd>When selecting text by word, sequences of these characters are also considered members of single words. The hyphen and alphanumerics do not need to be specified. Ranges can be given as &quot;A-Z&quot;. Default value: <code>&#8216;,./?%&amp;#:_&#8217;</code></p>
<dt><code>mouse_autohide </code>(boolean)</p>
<dd>Controls whether the mouse cursor should be hidden while typing. Default value: <code>True</code></p>
<dt><code>use_custom_command </code>(boolean)</p>
<dd>If True, the value of <code>custom_command</code> will be used instead of the default shell. Default value: <code>False</code></p>
<dt><code>custom_command</code></p>
<dd>Command to execute instead of the default shell, if <code>use_custom_command</code> is set to True. Default value: Nothing</p>
<dt><code>http_proxy</code></p>
<dd>URL of an HTTP proxy to use, e.g. <a rel="nofollow" href="http://proxy.lan:3128/">http://proxy.lan:3128/</a> Default value: Nothing</p>
<dt><code>encoding</code></p>
<dd>Character set to use for the terminal. Default value: <code>UTF-8</code></p>
<dt><code>copy_on_selection </code>(boolean)</p>
<dd>If set to True, text selections will be automatically copied to the clipboard, in addition to being made the Primary selection. Default value: <code>False</code></p>
<dd></dl>
<h2>layouts</h2>
<p>This describes the layouts section of the config file. Like with the profiles, each layout should be defined as a sub-section with a name formatted like: <code>[[name]]</code>. </p>
<p> Each object in a layout is a named sub-sub-section with various properties: </p>
<p> [layouts]<br />
&nbsp;<wbr>&nbsp;[[default]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[[window0]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type&nbsp;=&nbsp;Window<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[[child1]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;type&nbsp;=&nbsp;Terminal<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parent&nbsp;=&nbsp;window0 </p>
<p> Window objects may not have a parent attribute. <code>Every</code> other object must specify a parent. This is how the structure of the window is determined.</p>
<h2>plugins</h2>
<p>Terminator plugins can add their own configuration to the config file, and will appear as a sub-section. Please refer to the documentation of individual plugins for more information.</p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-terminator/">terminator</a></code>(1), <a rel="nofollow" href="http://www.voidspace.org.uk/python/configobj.html">http://www.voidspace.org.uk/python/configobj.html</a></p>
<dd>
