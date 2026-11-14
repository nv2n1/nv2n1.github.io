---
title: "gtkwaverc(5)"
name: "gtkwaverc"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gtkwaverc/"
description: "gtkwaverc – GTKWave Configuration File"
---

<p>gtkwaverc &#8211; GTKWave Configuration File</p>
<h2>Syntax</h2>
<p>option &lt;<i>value</i>&gt;</p>
<dl>
<dt>The configuration file is a series of option and value pairs. Comment lines marked with an initial &#8216;#&#8217; character are permissible. Blank lines are ignored.</p>
<dd></dl>
<h2>Description</h2>
<p>Configuration file for <i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1). The search path for the configuration file (if unspecified) is the current working directory followed by the user&#8217;s home directory.</p>
<h2>Options</h2>
<dl>
<dt><code>accel</code> &lt;<i>&quot;pathvalue&quot; accelerator</i>&gt;</p>
<dd>This allows replacement of menu accelerator keys. See the .gtkwaverc file in the source distribution for examples on pathvalue and accelerator syntax. The special accelerator value of <i>(null)</i> means that no accelerator is bound to the menu item.</p>
<dt><code>alt_hier_delimeter</code> &lt;<i>value</i>&gt;</p>
<dd>This allows another character in addition to the hier_delimeter to be used to delimit levels in the hierarchy for VCD. Only the first character in the value is significant. Note that this is normally off. The intended use is to resolve the hierarchies of netlist based models that often contain slashes to delimit hierarchy inside of $var statements.</p>
<dt><code>alt_wheel_mode</code> &lt;<i>value</i>&gt;</p>
<dd>Default is on. Scrollwheel alone pans along a quarter at a time rather than a full page, so you don&#8217;t get lost. Ctrl+wheel zooms in/out around the mouse cursor position, not the marker position. Alt+wheel edges left/right based on the currently selected signal. This makes measuring deltas easier.</p>
<dt><code>analog_redraw_skip_count</code> &lt;<i>value</i>&gt;</p>
<dd>Specifies how many overlapping analog segments can be drawn for a given X position onscreen. (Default: 20) If there are gaps in analog traces, this value is too low.</p>
<dt><code>append_vcd_hier</code> &lt;<i>value</i>&gt;</p>
<dd>Allows the specification of a prefix hierarchy for VCD files. This can be done in &quot;pieces,&quot; so that multiple layers of hierarchy are prepended to symbol names with the most significant addition occurring first (see .gtkwaverc in the examples/vcd directory). The intended use of this is to have the ability to add &quot;project&quot; prefixes which allow easier selection of everything from the tree hierarchy.</p>
<dt><code>atomic_vectors</code> &lt;<i>value</i>&gt;</p>
<dd>Speeds up vcd loading and takes up less memory. This option is deprecated; it is currently the default.</p>
<dt><code>autocoalesce</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value enables autocoalescing of VCD vectors when applicable. This may be toggled dynamically during wave viewer usage.</p>
<dt><code>autocoalesce_reversal</code> &lt;<i>value</i>&gt;</p>
<dd>causes split vectors to be reconstructed in reverse order (only if autocoalesce is also active).</p>
<dt><code>autoname_bundles</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that GTKWave will create its own bundle names rather than prompting the user for them.</p>
<dt><code>color_0</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when 0.</p>
<dt><code>color_1</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when 1.</p>
<dt><code>color_back</code> &lt;<i>value</i>&gt;</p>
<dd>background color.</p>
<dt><code>color_baseline</code> &lt;<i>value</i>&gt;</p>
<dd>middle mouse button marker color.</p>
<dt><code>color_black</code> &lt;<i>value</i>&gt;</p>
<dd>color value for &quot;black&quot; in signal window.</p>
<dt><code>color_brkred</code> &lt;<i>value</i>&gt;</p>
<dd>brick red color for comments.</p>
<dt><code>color_dash</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when don&#8217;t care (&quot;-&quot;).</p>
<dt><code>color_dashfill</code> &lt;<i>value</i>&gt;</p>
<dd>trace color (inside of box) when don&#8217;t care (&quot;-&quot;).</p>
<dt><code>color_dkblue</code> &lt;<i>value</i>&gt;</p>
<dd>color value for &quot;dark blue&quot; in signal window.</p>
<dt><code>color_dkgray</code> &lt;<i>value</i>&gt;</p>
<dd>color value for &quot;dark gray&quot; in signal window.</p>
<dt><code>color_gmstrd</code> &lt;<i>value</i>&gt;</p>
<dd>color value for trace groupings.</p>
<dt><code>color_grid</code> &lt;<i>value</i>&gt;</p>
<dd>grid color (use Alt-G/Shift-Alt-G to show/hide grid). This is also the color used for <code>highlight_wavewindow</code> when enabled.</p>
<dt><code>color_grid2</code> &lt;<i>value</i>&gt;</p>
<dd>grid color for secondary pattern search.</p>
<dt><code>color_high</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when high (&quot;H&quot;).</p>
<dt><code>color_low</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when low (&quot;L&quot;).</p>
<dt><code>color_ltblue</code> &lt;<i>value</i>&gt;</p>
<dd>color for shadowed traces.</p>
<dt><code>color_ltgray</code> &lt;<i>value</i>&gt;</p>
<dd>color value for &quot;light gray&quot; in signal window.</p>
<dt><code>color_mark</code> &lt;<i>value</i>&gt;</p>
<dd>color of the named markers.</p>
<dt><code>color_mdgray</code> &lt;<i>value</i>&gt;</p>
<dd>color value for &quot;medium gray&quot; in signal window.</p>
<dt><code>color_mid</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when floating (&quot;Z&quot;).</p>
<dt><code>color_normal</code> &lt;<i>value</i>&gt;</p>
<dd>color value for &quot;normal&quot; GTK state in signal window.</p>
<dt><code>color_time</code> &lt;<i>value</i>&gt;</p>
<dd>text color for timebar.</p>
<dt><code>color_timeb</code> &lt;<i>value</i>&gt;</p>
<dd>text color for timebar&#8217;s background.</p>
<dt><code>color_trans</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when transitioning.</p>
<dt><code>color_u</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when undefined (&quot;U&quot;).</p>
<dt><code>color_ufill</code> &lt;<i>value</i>&gt;</p>
<dd>trace color (inside of box) when undefined (&quot;U&quot;).</p>
<dt><code>color_umark</code> &lt;<i>value</i>&gt;</p>
<dd>color of the unnamed (primary) marker.</p>
<dt><code>color_value</code> &lt;<i>value</i>&gt;</p>
<dd>text color for vector values.</p>
<dt><code>color_vbox</code> &lt;<i>value</i>&gt;</p>
<dd>vector color (horizontal).</p>
<dt><code>color_vtrans</code> &lt;<i>value</i>&gt;</p>
<dd>vector color (verticals/transitions).</p>
<dt><code>color_w</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when weak (&quot;W&quot;).</p>
<dt><code>color_wfill</code> &lt;<i>value</i>&gt;</p>
<dd>trace color (inside of box) when weak (&quot;W&quot;).</p>
<dt><code>color_white</code> &lt;<i>value</i>&gt;</p>
<dd>color value for &quot;white&quot; in signal window.</p>
<dt><code>color_x</code> &lt;<i>value</i>&gt;</p>
<dd>trace color when undefined (&quot;X&quot;) (collision for VHDL).</p>
<dt><code>color_xfill</code> &lt;<i>value</i>&gt;</p>
<dd>trace color (inside of box) when undefined (&quot;X&quot;) (collision for VHDL).</p>
<dt><code>constant_marker_update</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that the values for traces listed in the signal window are to be updated constantly when the left mouse button is being held down rather than only when it is first pressed then when released (which is the default).</p>
<dt><code>context_tabposition</code> &lt;<i>value</i>&gt;</p>
<dd>Use zero for tabbed viewing with named tabs at the top. Nonzero places numerically indexed tabs at the left.</p>
<dt><code>convert_to_reals</code> &lt;<i>value</i>&gt;</p>
<dd>Converts all integer and parameter VCD declarations to real-valued ones when set to a nonzero/yes value. The positive aspect of this is that integers and parameters will take up less space in memory and will automatically display in decimal format. The negative aspect of this is that integers and parameters will only be displayable as decimals and can&#8217;t be bit reversed, inverted, etc.</p>
<dt><code>cursor_snap</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates the number of pixels the marker should snap to for the nearest signal transition.</p>
<dt><code>disable_ae2_alias</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that the AE2 loader is to ignore the aliasdb keyword and is not to construct facility aliases.</p>
<dt><code>disable_empty_gui</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that if gtkwave is invoked without a dumpfile name, then an empty gtkwave session is to be suppressed. Default is a zero value: to bring up an empty session which needs a file loaded or dragged into it.</p>
<dt><code>disable_mouseover</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that signal/value tooltip pop up bubbles on mouse button presses should be disabled in the value window. A zero value indicates that value tooltips should be active (default is disabled).</p>
<dt><code>disable_tooltips</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that tooltip pop up bubbles should be disabled. A zero value indicates that tooltips should be active (default).</p>
<dt><code>do_initial_zoom_fit</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that the trace should initially be crunched to fit the screen. A zero value indicates that the initial zoom should be zero (default).</p>
<dt><code>dynamic_resizing</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that dynamic resizing should be initially enabled (default). A zero value indicates that dynamic resizing should be initially disabled. </p>
<dt><code>editor</code> &lt;<i>&quot;value&quot;</i>&gt;</p>
<dd>This is used to specify a string (quotes mandatory) for when gtkwave invokes a text editor (e.g., Open Source Definition). Examples are: editor &quot;vimx -g +%d %s&quot;, editor &quot;gedit +%d %s&quot;, editor &quot;emacs +%d %s&quot;, and for OSX, editor &quot;mate -l %d %s&quot;. The %d may be combined with other characters in a string such as +, etc. The %s argument must stand by itself. Note that if this rc variable is not set, then the environment variable GTKWAVE_EDITOR will be consulted next, then finally gedit will be used (if found).</p>
<dt><code>enable_fast_exit</code> &lt;<i>value</i>&gt;</p>
<dd>Allows exit without bringing up a confirmation requester. The default is nonzero/yes.</p>
<dt><code>enable_ghost_marker</code> &lt;<i>value</i>&gt;</p>
<dd>lets the user turn on/off the ghost marker during primary marker dragging. Default is enabled.</p>
<dt><code>enable_horiz_grid</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that when grid drawing is enabled, horizontal lines are to be drawn. This is the default.</p>
<dt><code>enable_vcd_autosave</code> &lt;<i>value</i>&gt;</p>
<dd>causes the vcd loader to automatically generate a .sav file (vcd_autosave.sav ) in the cwd if a save file is not specified on the command line. Note that this mirrors the VCD $var defs and no attempt is made to coalesce split bitvectors back together.</p>
<dt><code>enable_vert_grid</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that when grid drawing is enabled, vertical lines are to be drawn. This is the default. Note that all possible combinations of enable_horiz_grid and enable_vert_grid values are acceptable.</p>
<dt><code>fontname_logfile</code> &lt;<i>value</i>&gt;</p>
<dd>When followed by an argument, this indicates the name of the X11 font that you wish to use for the logfile browser. You may generate appropriate fontnames using the xfontsel program.</p>
<dt><code>fontname_signals</code> &lt;<i>value</i>&gt;</p>
<dd>When followed by an argument, this indicates the name of the X11 font that you wish to use for signals. You may generate appropriate fontnames using the xfontsel program.</p>
<dt><code>fontname_waves</code> &lt;<i>value</i>&gt;</p>
<dd>When followed by an argument, this indicates the name of the X11 font that you wish to use for waves. You may generate appropriate fontnames using the xfontsel program. Note that the signal font must be taller than the wave font or the viewer will complain then terminate.</p>
<dt><code>force_toolbars</code> &lt;<i>value</i>&gt;</p>
<dd>When enabled, this forces everything above the signal and wave windows to be rendered as toolbars. This allows for them to be detached which allows for more usable wave viewer space. By default this is off.</p>
<dt><code>hide_sst</code> &lt;<i>value</i>&gt;</p>
<dd>Hides the Signal Search Tree widget for GTK2.4 and greater such that it is not embedded into the main viewer window. It is still reachable as an external widget through the menus.</p>
<dt><code>hier_delimeter</code> &lt;<i>value</i>&gt;</p>
<dd>This allows characters other than &#8216;/&#8217; to be used to delimit levels in the hierarchy. Only the first character in the value is significant.</p>
<dt><code>hier_grouping</code> &lt;<i>value</i>&gt;</p>
<dd>For the tree widgets, this allows the hierarchies to be grouped in a single place rather than spread among the netnames.</p>
<dt><code>hier_max_level</code> &lt;<i>value</i>&gt;</p>
<dd>Sets the maximum hierarchy depth (from the right side) to display for trace names. Note that a value of zero displays the full hierarchy name.</p>
<dt><code>highlight_wavewindow</code> &lt;<i>value</i>&gt;</p>
<dd>When enabled, this causes traces highlighted in the signal window also to be highlighted in the wave window.</p>
<dt><code>hpane_pack</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that the horizontal pane should be constructed using the gtk_paned_pack functions (default and recommended). A zero value indicates that gtk_paned_add will be used instead.</p>
<dt><code>ignore_savefile_pane_pos</code> &lt;<i>value</i>&gt;</p>
<dd>If nonzero, specifies that the pane position attributes (i.e., signal window width size, SST is expanded, etc.) are to be ignored during savefile loading and is to be skipped during saving. Default is that the attribute is used.</p>
<dt><code>ignore_savefile_pos</code> &lt;<i>value</i>&gt;</p>
<dd>If nonzero, specifies that the window position attribute is to be ignored during savefile loading and is to be skipped during saving. Default is that the position attribute is used. </p>
<dt><code>ignore_savefile_size</code> &lt;<i>value</i>&gt;</p>
<dd>If nonzero, specifies that the window size attribute is to be ignored during savefile loading and is to be skipped during saving. Default is that the size attribute is used.</p>
<dt><code>initial_signal_window_width</code> &lt;<i>value</i>&gt;</p>
<dd>Sets the creation width for the signal pane on GUI initialization. Also sets another potential minimum value for dynamic resizing.</p>
<dt><code>initial_window_x</code> &lt;<i>value</i>&gt;</p>
<dd>Sets the size of the initial width of the wave viewer window. Values less than or equal to zero will set the initial width equal to -1 which will let GTK determine the minimum size.</p>
<dt><code>initial_window_xpos</code> &lt;<i>value</i>&gt;</p>
<dd>Sets the size of the initial x coordinate of the wave viewer window. -1 will let the window manager determine the position.</p>
<dt><code>initial_window_y</code> &lt;<i>value</i>&gt;</p>
<dd>Sets the size of the initial height of the wave viewer window. Values less than or equal to zero will set the initial width equal to -1 which will let GTK determine the minimum size.</p>
<dt><code>initial_window_ypos</code> &lt;<i>value</i>&gt;</p>
<dd>Sets the size of the initial y coordinate of the wave viewer window. -1 will let the window manager determine the position.</p>
<dt><code>keep_xz_colors</code> &lt;<i>value</i>&gt;</p>
<dd>When nonzero, indicates that the original color scheme for non 0/1 signal values is to be used when Color Format overrides are in effect. Default is off.</p>
<dt><code>left_justify_sigs</code> &lt;<i>value</i>&gt;</p>
<dd>When nonzero, indicates that the signal window signal name justification should default to left, else the justification is to the right (default).</p>
<dt><code>lxt_clock_compress_to_z</code> &lt;<i>value</i>&gt;</p>
<dd>For LXT (not LXT2) allows clocks to compress to a &#8216;z&#8217; value so that regular/periodic value changes may be noted.</p>
<dt><code>page_divisor</code> &lt;<i>value</i>&gt;</p>
<dd>Sets the scroll amount for page left and right operations. (The buttons, not the hscrollbar.) Values over 1.0 are taken as 1/x and values equal to and less than 1.0 are taken literally. (i.e., 2 gives a half-page scroll and .67 gives 2/3). The default is 1.0.</p>
<dt><code>ps_maxveclen</code> &lt;<i>value</i>&gt;</p>
<dd>sets the maximum number of characters that can be printed for a value in the signal window portion of a postscript file (not including the net name itself). Legal values are 4 through 66 (default).</p>
<dt><code>ruler_origin</code> &lt;<i>value</i>&gt;</p>
<dd>sets the zero origin for alternate time tick marks.</p>
<dt><code>ruler_step</code> &lt;<i>value</i>&gt;</p>
<dd>sets the left/right step value for the alternate time tick marks from the origin. When this value is zero, alternate time tick marks are disabled.</p>
<dt><code>scale_to_time_dimension</code> &lt;<i>value</i>&gt;</p>
<dd>The value can be any of the characters m, u, n, f, p, or s, which indicates which time dimension to convert the time values to. The default for this is * which means that time dimension conversion is disabled.</p>
<dt><code>show_base_symbols</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value (default) indicates that the numeric base symbols for hexadecimal (&#8216;$&#8217;), binary (&#8216;%&#8217;), and octal (&#8216;#&#8217;) should be rendered. Otherwise they will be omitted.</p>
<dt><code>show_grid</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value (default) indicates that a grid should be drawn behind the traces. A zero indicates that no grid should be drawn.</p>
<dt><code>splash_disable</code> &lt;<i>value</i>&gt;</p>
<dd>Turning this off enables the splash screen with the GTKWave mascot when loading a trace. Default is on.</p>
<dt><code>sst_dynamic_filter</code> &lt;<i>value</i>&gt;</p>
<dd>When true (default) allows the SST dialog signal filter to filter signals while keys are being pressed, otherwise enter must be pressed to cause the filter to go active.</p>
<dt><code>sst_expanded</code> &lt;<i>value</i>&gt;</p>
<dd>When true allows the SST dialog (when not hidden) to come up already expanded.</p>
<dt><code>strace_repeat_count</code> &lt;<i>value</i>&gt;</p>
<dd>Determines how many times that edge search and pattern search will iterate on a search. This allows, for example, skipping ahead 10 clock edges instead of 1.</p>
<dt><code>use_big_fonts</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that any text rendered into the wave window will use fonts that are four points larger in size than normal. This can enhance readability. A zero value indicates that normal font sizes should be used.</p>
<dt><code>use_frequency_delta</code> &lt;<i>value</i>&gt;</p>
<dd>allows you to switch between the delta time and frequency display in the upper right corner of the main window when measuring distances between markers. Default behavior is that the delta time is displayed (off).</p>
<dt><code>use_full_precision</code> &lt;<i>value</i>&gt;</p>
<dd>does not round time values when the number of ticks per pixel onscreen is greater than 10 when active. The default is that this feature is disabled.</p>
<dt><code>use_maxtime_display</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that the maximum time will be displayed in the upper right corner of the screen. Otherwise, the current primary (unnamed) marker time will be displayed. This can be toggled at any time with the Toggle Max-Marker menu option.</p>
<dt><code>use_nonprop_fonts</code> &lt;<i>value</i>&gt;</p>
<dd>Allows accelerated redraws of the signalwindow that can be done because the font width is constant. Default is off.</p>
<dt><code>use_pango_fonts</code> &lt;<i>value</i>&gt;</p>
<dd>Uses anti-aliased pango fonts (GTK2) rather than bitmapped X11 ones. Default is on.</p>
<dt><code>use_roundcaps</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that vector traces should be drawn with rounded caps rather than perpendicular ones. The default for this is zero.</p>
<dt><code>use_scrollbar_only</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that the page, shift, fetch, and discard buttons should not be drawn (i.e., time manipulations should be through the scrollbar only rather than front panel buttons). The default for this is zero.</p>
<dt><code>use_scrollwheel_as_y</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that the scroll wheel on the mouse should be used to scroll the signals up and down rather than scrolling the time value from left to right.</p>
<dt><code>use_standard_clicking</code> &lt;<i>value</i>&gt;</p>
<dd>This option no longer has any effect in gtkwave: normal GTK click semantics are used in the signalwindow.</p>
<dt><code>use_standard_trace_select</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value keeps the currently selected traces from deselecting on mouse button press. This allows drag and drop to function more smoothly. As this behavior is not how GTK normally functions, it is by default disabled.</p>
<dt><code>use_toolbutton_interface</code> &lt;<i>value</i>&gt;</p>
<dd>A nonzero value indicates that a toolbar with buttons should be at the top of the screen instead of the traditional style gtkwave button groups. Default is on.</p>
<dt><code>vcd_explicit_zero_subscripts</code> &lt;<i>value</i>&gt;</p>
<dd>indicates that signal names should be stored internally as name.bitnumber when enabled. When disabled, a more &quot;normal&quot; ordering of name[bitnumber] is used. Note that when disabled, the Bundle Up and Bundle Down options are disabled in the Signal Search Regexp, Signal Search Hierarchy, and Signal Search Tree options. This is necessary as the internal data structures for signals are represented with one &quot;less&quot; level of hierarchy than when enabled and those functions would not work properly. This should not be an issue if atomic_vectors are enabled. Default for vcd_explicit_zero_subscripts is disabled.</p>
<dt><code>vcd_preserve_glitches</code> &lt;<i>value</i>&gt;</p>
<dd>indicates that any repeat equal values for a net spanning different time values in the VCD/FST file are not to be compressed into a single value change but should remain in order to allow glitches to be present for this case. Default for vcd_preserve_glitches is disabled.</p>
<dt><code>vcd_preserve_glitches_real</code> &lt;<i>value</i>&gt;</p>
<dd>indicates that any repeat equal values for a real net spanning different time values in the VCD/FST file are not to be compressed into a single value change but should remain for this case. Default for vcd_preserve_glitches is disabled. The intended use is for when viewing analog interpolated data such that removing duplicate values would incorrectly deform the interpolation.</p>
<dt><code>vcd_warning_filesize</code> &lt;<i>value</i>&gt;</p>
<dd>produces a warning message if the VCD filesize is greater than the argument&#8217;s size in MB. Set to zero to disable this.</p>
<dt><code>vector_padding</code> &lt;<i>value</i>&gt;</p>
<dd>indicates the number of pixels of extra whitespace that should be added to any strings for the purpose of calculating text in vectors. Permissible values are 0 to 16 with the default being 4.</p>
<dd><code>vlist_compression</code> &lt;<i>value</i>&gt; indicates the value to pass to zlib during vlist processing (which is used in the VCD recoder). -1 disables compression, 0-9 correspond to the value zlib expects. 4 is default.</p>
<dt><code>vlist_prepack</code> &lt;<i>value</i>&gt;</p>
<dd>indicates that the VCD recoder should pre-compress data going into the value change vlists in order to reduce memory usage. This is done before potential zlib packing. Default is off.</p>
<dt><code>vlist_spill</code> &lt;<i>value</i>&gt;</p>
<dd>indicates that the VCD recoder should spill all generated vlists to a tempfile on disk in order to reduce memory usage. Default is off.</p>
<dt><code>wave_scrolling</code> &lt;<i>value</i>&gt;</p>
<dd>a nonzero value enables scrolling by dragging the marker off the left or right sides of the wave window. A zero value disables it.</p>
<dt><code>zoom_base</code> &lt;<i>value</i>&gt;</p>
<dd>allows setting of the zoom base with a value between 1.5 and 10.0. Default is 2.0.</p>
<dt><code>zoom_center</code> &lt;<i>value</i>&gt;</p>
<dd>a nonzero value enables center zooming, a zero value disables it.</p>
<dt><code>zoom_dynamic</code> &lt;<i>value</i>&gt;</p>
<dd>a nonzero value enables dynamic full zooming when using the partial VCD (incremental) loader, a zero value disables it.</p>
<dt><code>zoom_dynamic_end</code> &lt;<i>value</i>&gt;</p>
<dd>a nonzero value enables dynamic zoom to the end when using the partial VCD (incremental) loader, a zero value disables it.</p>
<dt><code>zoom_pow10_snap</code> &lt;<i>value</i>&gt;</p>
<dd>corresponds to the Zoom Pow10 Snap menu option. Default for this is disabled (zero).</dl>
<h2>Authors</h2>
<p>Anthony Bybell &lt;bybell [at] rocketmail.com&gt;</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-gtkwave/">gtkwave</a></i>(1) </p>
