---
title: "fvwmbuttons(1)"
name: "fvwmbuttons"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmbuttons/"
description: "FvwmButtons – the fvwm buttonbox module"
---

<p>FvwmButtons &#8211; the fvwm buttonbox module </p>
<h2>Synopsis</h2>
<pre>Module FvwmButtons [-g geometry] [-transient | -transientpanel] [name[configfile]]</pre>
<p><i>FvwmButtons</i> can only be invoked by fvwm. Command line invocation of the <i>FvwmButtons</i> module will not work. </p>
<h2>Description</h2>
<p>The FvwmButtons module provides a window of buttons which sits on the X terminal&#8217;s root window. The user can press the buttons at any time, and trigger invocation of a user-specified command by the window manager. FvwmButtons only works when fvwm is used as the window manager. </p>
<p> The buttonbox can be of any configuration or geometry, and can have monochrome or color icons to represent the actions which would be invoked. Even other applications can be &#8216;swallowed&#8217; by the button bar. </p>
<p> Panels that are opened on a button press are available too. See <i>CREATING PANELS</i> section for details. </p>
<h2>Options</h2>
<p>The <i>-g</i> option specifies the geometry of the main window. The command line option takes precedence over any other geometry settings in the configuration file. </p>
<p> The <i>-transient</i> option tells FvwmButtons to terminate itself after the first key or button press has been received (presses to open a sub panel do not count) or a sub panel has been closed or respawned. This is especially useful for sub panels where you want to select a single button and have it closed automatically. It could be used to create two-dimensional graphical menus. Since <i>-transient</i> is an option, not a configuration setting you can use the same configuration for transient and non transient button bars. </p>
<p> The <i>-transientpanel</i> option does roughly the same as the <i>-transient</i> option, but instead of closing the whole button bar, the window is merely hidden. This is very useful if the button bar is started as a subpanel of another button bar because it avoids that it must be started again when something is selected. </p>
<h2>Invocation</h2>
<p>FvwmButtons is spawned by fvwm, so command line invocation will not work. </p>
<p> FvwmButtons can be invoked by inserting the line &#8216;Module FvwmButtons OptionalName&#8217; in the .fvwm2rc file. This should be placed in the StartFunction if FvwmButtons is to be spawned during fvwm&#8217;s initialization. This can be bound to a menu or mouse button or keystroke to invoke it later. </p>
<p> When invoked with the <i>OptionalName</i> argument, the <i>OptionalName</i> is used to find configuration commands. For example: </p>
<pre>AddToFunc StartFunction Module FvwmButtons MyButtonBox</pre>
<p>FvwmButtons will then use only the lines starting with &quot;*MyButtonBox&quot;, instead of the default &quot;*FvwmButtons&quot;. </p>
<h2>Configuration Options</h2>
<p>The following commands are understood by FvwmButtons: </p>
<dl>
<dt>*FvwmButtons: Back <i>color</i></p>
<dd>Specifies the background color for the buttons. The relief and shadow color are calculated from the background color. </p>
<dt>*FvwmButtons: BoxSize <i>algorithm</i></p>
<dd>This option specifies how serious FvwmButtons takes the Rows and Columns options (see below). It can be one of <i>dumb</i>, <i>fixed</i> or <i>smart</i>. </p>
<p> If <i>fixed</i> is used and both Rows and Columns are specified and non-zero, FvwmButtons uses exactly the number of rows and columns specified. If the box is too small to accommodate all buttons the module will fail. </p>
<p> If <i>smart</i> is used FvwmButtons enlarges the box so all buttons have a chance to fit. The number of columns is increased to at least the width of the widest button and new rows are added until all buttons are placed. For the best tolerance of configuration errors use the smart option. </p>
<p> <i>dumb</i> is neither <i>fixed</i> nor <i>smart.</i> This is the default. </p>
<dt>*FvwmButtons: Colorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for the window background. Refer to the FvwmTheme man page for details about colorsets. </p>
<dt>*FvwmButtons: ActiveColorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for the background color/image and/or title color of a button when the mouse is hovering above a button. </p>
<dt>*FvwmButtons: PressColorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for the background color/image and/or title color of a button when it is pressed. </p>
<dt>*FvwmButtons: Columns <i>columns</i></p>
<dd>Specifies the number of columns of buttons to be created. If unspecified, the number of columns is set to the number of buttons requested, divided by the number of rows. If both the rows and columns are specified, but the number of buttons is more than the rows and columns allow for, the columns specification is ignored unless the <i>BoxSize</i> option is <i>fixed</i>. </p>
<dt>*FvwmButtons: File <i>filename</i></p>
<dd>Specifies that the configuration for this button is found in the file <i>filename</i>. <i>Filename</i> can be a full pathname, or is assumed to be in fvwm&#8217;s startup directory. The configuration file is in the same format as fvwm&#8217;s configuration file, but each line is read as if prefixed by &quot;*FvwmButtons&quot;. Comments are given by starting a line with &quot;#&quot;. Line continuation is done by ending a line with a &quot;\&quot;. </p>
<dt>*FvwmButtons: Font <i>font</i></p>
<dd>Specifies the font to be used for labeling the buttons, or <i>None</i>. </p>
<dt>*FvwmButtons: Fore <i>color</i></p>
<dd>Specifies the color used for button label text and monochrome icons. </p>
<dt>*FvwmButtons: Frame <i>width</i></p>
<dd>Specifies the width of the relief around each button. If this is a negative number, the relief is inverted. This makes the button sunken normally and raised when activated. </p>
<dt>*FvwmButtons: Geometry <i>geometry</i></p>
<dd>Specifies the FvwmButtons window location and size. The geometry is a standard X11 window geometry specification. </p>
<dt>*FvwmButtons: ButtonGeometry <i>geometry</i></p>
<dd>This option works like the <i>Geometry</i> option except that the size is the size of a single button. The size of the whole FvwmButtons window is calculated by multiplying the button dimension by the number of rows and columns. </p>
<dt>*FvwmButtons: Padding <i>width height</i></p>
<dd>This option specifies the default horizontal padding to be <i>width</i> pixels, and the vertical padding to be <i>height</i> pixels. The amount of free space between the relief of the button and its contents is normally 2 pixels on the sides and 4 pixels above and below, except for swallowed windows and containers, which are not padded at all, unless this option is used. </p>
<dt>*FvwmButtons: Pixmap <i>pixmapfile</i></p>
<dd>Specifies a background pixmap to use. Specify &quot;none&quot; (without the double quotes) for a transparent background. </p>
<dt>*FvwmButtons: Rows <i>rows</i></p>
<dd>Specifies the number of rows of buttons to be created. The default is 2 rows. </p>
<dt>*FvwmButtons: (<i>options</i>) [<i>title icon command</i>]</p>
<dd>Specifies the contents of a button in the buttonbox. The following <i>options</i>, separated by commas or whitespace, can be given a button:</p>
<dl>
<dd>
<dl>
<dt><i>geometry</i></p>
<dd>Specifies the size and position of the button within the FvwmButtons window or container. The geometry is a standard X11 window geometry specification. The button is <i>width</i> times the normal button width and <i>height</i> times the normal button height. If values for <i>x</i> and <i>y</i> are given, the button is placed x (y) button units from the left (top) of the container if x (y) is positive and x (y) units from the right (bottom) if x (y) is negative. Buttons with position arguments (x and y) are placed before those without them. If two or more buttons are forced to overlap by this, FvwmButtons exits with an error message. </p>
<dt>Action [(<i>options</i>)] <i>command</i></p>
<dd>Specifies an fvwm command to be executed when the button is activated by pressing return or a mouse button. The <i>command</i> needs to be quoted if it contains a comma or a closing parenthesis. </p>
<p> The current options of the <i>Action</i> are: Mouse <i>n</i> &#8211; this action is only executed for mouse button <i>n</i>. One action can be defined for each mouse button, in addition to the general action. </p>
<p> In the <i>command</i> part, you can use a number of predefined variables: <i>$left</i>, <i>$right</i>, <i>$top</i> and <i>$bottom</i> are substituted by the left, right, top and bottom coordinates of the button pressed. <i>$-left</i>, <i>$-right</i>, <i>$-top</i> and <i>$-bottom</i> are substituted likewise, but the coordinates are calculated from the bottom or the right edge of the screen instead (for a button that is 5 pixels away from the right screen border, $-right will be 5). <i>$width</i> and <i>$height</i> are replaced by the width or height of the button. The variables <i>$fg</i> and <i>$bg</i> are replaced with the name of the foreground or background color set with the <i>Back</i> or <i>Fore</i> option (see below). All this is done regardless of any quoting characters. To get a literal &#8216;$&#8217; use the string &#8216;$$&#8217;. </p>
<p> Example: </p>
<pre> *FvwmButtons: (Title xload, Action (Mouse 1) \
 `Exec exec xload -fg $fg -bg $bg -geometry -3000-3000`)</pre>
<p>Note: With fvwm versions prior to 2.5.0, actions could not be assigned to a button that swallowed an application window (see <i>Swallow</i> option). Such actions worked only when the border around the button was clicked. This is now possible, but to get back the old behavior, the <i>ActionIgnoresClientWindow</i> can be used on the button: </p>
<pre> *FvwmButtons: (Action beep, ActionIgnoresClientWindow, \
 Swallow xeyes &quot;Exec exec xeyes&quot;)</pre>
<p>In this example, the action is only executed when you click on the border of the button or the transparent part of the xeyes window, but not on the xeyes window itself. </p>
<dt>ActionIgnoresClientWindow</p>
<dd>See the note in the description of <i>Action</i> above. </p>
<dt>ActionOnPress</p>
<dd>Usually the action is executed on the button release except for the <code>Popup</code> action. This option changes this behavior, the action is executed on the button press. This may be good, for example, with <code>Menu</code> or <code>SendToModule</code> that generates popups, or when <code>Frame</code> is 0 and the button would look unresponsive otherwise. </p>
<dt>Back <i>color</i></p>
<dd>Specifies the background color to be used drawing this box. A relief color and a shadow color are calculated from this. </p>
<dt>Center</p>
<dd>The contents of the button is centered on the button. This is the default but may be changed by <i>Left</i> or <i>Right</i>. </p>
<dt>Top</p>
<dd>The contents of the button is vertically aligned at the top of the button. The default is to vertically center it. </p>
<dt>Colorset <i>colorset</i></p>
<dd>The given colorset can be applied to a container, a swallowed application and a simple button. To apply it to a button or container, simply put the option in a line with a button or container description. Drawing backgrounds for individual buttons and containers with colorsets requires a lot of communication with the X server. So if you are not content with the drawing speed of dozens of buttons with colorset backgrounds, do not use colorsets here. Setting colorsets as the background of swallowed applications does not have this restriction but depends entirely on the swallowed application. It may work as you wish, but since it involves fiddling with other applications&#8217; windows there is no guarantee for anything. I have tested three applications: xosview works nicely with a colorset background, xload works only with a VGradient or solid background and an analog xclock leaves a trail painted in the background color after its hands. </p>
<p> If the swallowed window is an fvwm module (see the (No)FvwmModule option to Swallow), then the <i>colorset</i> is not applied to the swallowed module. You should use the <i>colorset</i> in the module configuration. If the swallowed module has a transparent colorset background, then the FvwmButtons background (and not the button colorset) is seen by transparency of the background of the swallowed module. Refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>ActiveColorset <i>colorset</i></p>
<dd>Use colorset <i>colorset</i> for the background color/image and/or title color of the button when the mouse is hovering above it. </p>
<dt>PressColorset <i>colorset</i></p>
<dd>Use colorset <i>colorset</i> for the background color/image and/or title color of the button when it is pressed. </p>
<dt>Container [(<i>options</i>)]</p>
<dd>Specifies that this button will contain a miniature buttonbox, equivalent to swallowing another FvwmButtons module. The options are the same as can be given for a single button, but they affect all the contained buttons. Options available for this use are <i>Back, Font, Fore, Frame</i> and <i>Padding</i>. Flags for Title and Swallow options can be set with <i>Title(flags)</i> and <i>Swallow(flags)</i>. You should also specify either &quot;Columns <i>width</i>&quot; or &quot;Rows <i>height</i>&quot;, or &quot;Rows 2&quot; will be assumed. For an example, see the <i>Sample configuration</i> section. </p>
<p> The container button itself (separate from the contents) can take format options like <i>Frame</i> and <i>Padding</i>, and commands can be bound to it. This means you can make a sensitive relief around a container, like </p>
<pre> *FvwmButtons: (2x2, Frame 5, Padding 2 2, Action Beep,\
 Container(Frame 1))</pre>
<p>Typically you will want to at least give the container a size setting <i>width</i>x<i>height</i>. </p>
<dt>End</p>
<dd>Specifies that no more buttons are defined for the current container, and further buttons will be put in the container&#8217;s parent. This option should be given on a line by itself, i.e </p>
<pre> *FvwmButtons: (End)</pre>
<dt>Font <i>fontname</i></p>
<dd>Specifies that the font <i>fontname</i> is to be used for labeling this button. </p>
<dt>Fore <i>color</i></p>
<dd>Specifies the foregound color of the title and monochrome icons in this button. </p>
<dt>Frame <i>width</i></p>
<dd>The relief of the button will be <i>width</i> pixels wide. If <i>width</i> is given as a negative number, the relief is inverted. This makes the button sunken normally and raised when activated. </p>
<dt>Icon <i>filename</i></p>
<dd>The name of an image file, containing the icon to display on the button. FvwmButtons searches through the path specified in the fvwm ImagePath configuration item to find the icon file. </p>
<dt>ActiveIcon <i>filename</i></p>
<dd>The name of an image file, containing an alternative icon to display on the button when the mouse is hovering above the button. If no ActiveIcon is specified, the image specified by Icon is displayed (if there is one). </p>
<dt>PressIcon <i>filename</i></p>
<dd>The name of an image file, containing an alternative icon to display on the button when the button is pressed. If no PressIcon is specified, the image specified by Icon is displayed (if there is one). </p>
<dt>Id <i>id</i></p>
<dd>The id to be used to identify this button. The first character of the id should be alphabetic. See also the &quot;DYNAMICAL ACTIONS&quot; section. </p>
<dt>Left</p>
<dd>The contents of the button are aligned to the left. The default is to center the contents on the button. </p>
<dt>NoSize</p>
<dd>This option specifies that this button will not be considered at all when making the initial calculations of button sizes. Useful for the odd button that gets just a couple of pixels too large to keep in line, and therefor blows up your whole buttonbox. &quot;NoSize&quot; is equivalent to &quot;Size 0 0&quot;. </p>
<dt>Padding <i>width height</i></p>
<dd>The amount of free space between the relief of the button and its contents is normally 2 pixels to the sides and 4 pixels above and below, except for swallowed windows and containers, which are by default not padded at all. This option sets the horizontal padding to <i>width</i> and the vertical padding to <i>height</i>. </p>
<dt>Panel [ (<i>options</i>) ] <i>hangon</i> <i>command</i></p>
<dd>Panels can be swallowed exactly like windows are swallowed by buttons with the <i>Swallow</i> command below, but they are not displayed within the button. Instead they are hidden until the user presses the panel&#8217;s button. Then the panel (the window of the swallowed application) opens with a sliding animation. The <i>options</i> can be any of the <i>flags</i> described for the Swallow command. In addition a direction &#8216;left&#8217;, &#8216;right&#8217;, &#8216;up&#8217; or &#8216;down&#8217; can be used to specify the sliding direction. </p>
<p> The <i>steps animation-steps</i> option defines the number of animation steps. </p>
<p> The <i>delay ms</i> option sets the delay between the steps of the animation in milliseconds. Use zero for no delay. The maximum delay is 10 seconds (10000). It doesn&#8217;t make any sense to use the delay option unless you also use the smooth option. </p>
<p> The <i>smooth</i> option causes the panel to redraw between the steps of the animation. The sliding animation may be smoother this way, it depends on the application, and display speed. The application may appear to grow instead of sliding out. The animation may be slower. </p>
<p> The <i>Hints</i> option causes FvwmButtons to use the applications size hints to calculate the size of the animation steps. <i>Hints</i> is the default. If the number of steps is not what you want, try using <i>NoHints.</i> </p>
<p> The <i>noborder</i> option tells FvwmButtons to ignore the borders of the window when calculating positions for the animation (equivalent to set noplr and noptb in the position option). </p>
<p> With the <i>indicator</i> option set, FvwmButtons will draw a small triangle in the button that will open a panel. The triangle points in the direction where the panel will pop up. The <i>indicator</i> keyword may be followed by a positive integer that specifies the maximum width and height of the indicator. Without this size FvwmButtons will make the indicator fit the button. You will probably want to use the <i>Padding</i> option to leave a few pixels between the indicator and the frame of the button. </p>
<p> The <i>position</i> option allows one to place the panel. The syntax is: </p>
<pre>position [<i>context-window</i>] [<i>pos</i>] [<i>x</i> <i>y</i>] [<i>border-opts</i>]</pre>
<p>The argument <i>context-window</i> can be one of: Button, Module or Root. The <i>context-window</i> is the window from which panel percentage offsets are calculated. Button specifies the panel&#8217;s button, Module specifies FvwmButtons itself, and Root specifies a virtual screen. The context-window together with the sliding direction define a line segment which is one of the borders of the context-window: the top/bottom/left/right border for sliding up/down/left/right. </p>
<p> The <i>pos</i> argument can be one of: center, left or right (for sliding up or a down) or top or bottom (for sliding left or right). It defines the vertical (sliding up and down) or the horizontal (sliding left and right) position of the Panel on the line segment. For example, for a sliding up if you use a left pos, then the left borders of the panel and of the context-window will be aligned. </p>
<p> The offset values <i>x</i> and <i>y</i> specify how far the panel is moved from it&#8217;s default position. By default, the numeric value given is interpreted as a percentage of the context window&#8217;s width (height). A trailing &quot;p&quot; changes the interpretation to mean &quot;pixels&quot;. All offset calculations are relative to the buttons location, even when using a root context. </p>
<p> The <i>border-opts</i> are: mlr, mtb, noplr and noptb. They define which border widths are taken in account. By default, the borders of FvwmButtons are not taken in account. mlr reverses this default for the left and the right border and mtb reverses this default for the top and the bottom border. Conversely, by default the borders of the Panel are taken in account. noplr reverses this default for the left and the right border and noptb reverses this default for the top and the bottom border. </p>
<p> The defaults are sliding up with a delay of five milliseconds and twelve animation steps. To post the panel without any animation, set the number of steps to zero. The default position is &#8216;Button center&#8217;. </p>
<p> Please refer to the <i>CREATING PANELS</i> section for further information on panels. </p>
<p> Example: </p>
<pre> # To include the panel in a button
 *FvwmButtons: (Panel(down, delay 0, steps 16) \
 SubPanel &quot;Module FvwmButtons SubPanel&quot;)
 # To define the panel as an instance of
 # FvwmButtons with a different name:
 *SubPanel: (Icon my_lock.xpm, Action Exec xlock)
 *SubPanel: (Icon my_move.xpm, Action Move)
 ...</pre>
<dt>Right</p>
<dd>The contents of the button are aligned to the right. The default is to center the contents on the button. </p>
<dt>Size <i>width height</i></p>
<dd>Specifies that the contents of this button require <i>width</i> by <i>height</i> pixels, regardless of what size FvwmButtons calculates from the icon and the title. A button bar with only swallowed windows will not get very large without this option specified, as FvwmButtons does not consider sizes for swallowing buttons. Note that this option gives the minimum space assured; other buttons might require the buttonbox to use larger sizes. </p>
<dt>Swallow [(<i>flags</i>)] <i>hangon</i> <i>command</i></p>
<dd>Causes FvwmButtons to execute <i>command</i>, and when a window with a name, class or resource matching <i>hangon</i> appears, it is captured and swallowed into this button. The <i>hangon</i> string may contain wildcard characters (&#8216;*&#8217;) that match any substring. Swallow replaces the variables <i>$fg</i> and <i>$bg</i> as described above for the <i>Action</i> option (but if you use the UseOld and NoClose options the application is not be restarted when FvwmButtons is restarted and thus does not get the new colors &#8211; if you changed them). An example: </p>
<pre> *FvwmButtons: (Swallow XClock 'Exec xclock -geometry -3000-3000 &amp;')</pre>
<p>takes the first window whose name, class, or resource is &quot;XClock&quot; and displays it in the button. If no matching window is found, the &quot;Exec&quot; command creates one. The argument &quot;-geometry -3000-3000&quot; is used so that the window is first drawn out of sight before its swallowed into FvwmButtons. </p>
<p> Modules can be swallowed by specifying the module instead of &#8216;Exec whatever&#8217;, like: </p>
<pre> *FvwmButtons: (Swallow &quot;FvwmPager&quot; &quot;FvwmPager 0 0&quot;)</pre>
<p>The flags that can be given to swallow are: </p>
<p> NoClose / Close &#8211; Specifies whether the swallowed program in this button will be un-swallowed or closed when FvwmButtons exits cleanly. &quot;NoClose&quot; can be combined with &quot;UseOld&quot; to have windows survive a restart of the window manager. The default setting is &quot;Close&quot;. </p>
<p> NoHints / Hints &#8211; Specifies whether hints from the swallowed program in this button will be ignored or not, useful in forcing a window to resize itself to fit its button. The default value is &quot;Hints&quot;. </p>
<p> NoKill / Kill &#8211; Specifies whether the swallowed program will be closed by killing it or by sending a message to it. This can be useful in ending programs that doesn&#8217;t accept window manager protocol. The default value is &quot;NoKill&quot;. This has no effect if &quot;NoClose&quot; is specified. </p>
<p> NoRespawn / Respawn / SwallowNew &#8211; Specifies whether the swallowed program is to be respawned (restarted) if it dies. If &quot;Respawn&quot; is specified, the program is respawned using the original <i>command</i>. Use this option with care, the program might have a legitimate reason to die. If &quot;SwallowNew&quot; is given, the program is not respawned, but if a new window with the specified name appears, it is swallowed. </p>
<p> NoOld / UseOld &#8211; Specifies whether the button will try to swallow an existing window matching the <i>hangon</i> name before spawning one itself with <i>command</i>. The <i>hangon</i> string may contain wildcard characters (&#8216;*&#8217;) that match any substring.The default value is &quot;NoOld&quot;. &quot;UseOld&quot; can be combined with &quot;NoKill&quot; to have windows survive a restart of the window manager. If you want FvwmButtons to swallow an old window, and not spawn one itself if failing, let the <i>command</i> be &quot;Nop&quot;: </p>
<pre> *FvwmButtons: (Swallow (UseOld) &quot;Console&quot; Nop)</pre>
<p>If you want to be able to start it yourself, combine it with an action: </p>
<pre> *FvwmButtons: (Swallow (UseOld) &quot;Console&quot; Nop, \
 Action `Exec &quot;Console&quot; console &amp;`)</pre>
<p>NoTitle / UseTitle &#8211; Specifies whether the title of the button will be taken from the swallowed window&#8217;s title or not. If &quot;UseTitle&quot; is given, the title on the button changes dynamically to reflect the window name. The default is &quot;NoTitle&quot;. </p>
<p> NoFvwmModule / FvwmModule &#8211; By default, FvwmButtons treats the swallowed window as an fvwm module window if the 4 first letters of the <i>command</i> is &quot;Fvwm&quot; or the 6 first letters of the <i>command</i> is &quot;Module&quot;. NoFvwmModule and FvwmModule override this logic. </p>
<dt>Title [(<i>options</i>)] <i>name</i></p>
<dd>Specifies the title to be written on the button. Whitespace can be included in the title by quoting it. If a title at any time is too long for its buttons, characters are chopped of one at a time until it fits. If <i>justify</i> is &quot;Right&quot;, the head is removed, otherwise its tail is removed. These <i>options</i> can be given to Title: </p>
<p> Center &#8211; The title is centered horizontally. This is the default. </p>
<p> Left &#8211; The title is justified to the left side. </p>
<p> Right &#8211; The title is justified to the right side. </p>
<p> Side &#8211; Causes the title to appear on the right hand side of any icon or swallowed window, instead of below which is the default. If you use small icons, and combine this with the &quot;Left&quot; or &quot;Right&quot; option, you can get a look similar to fvwm&#8217;s menus. </p>
<dt>ActiveTitle <i>name</i></p>
<dd>Specifies the title to be written on the button when the mouse is hovering above the button. If no ActiveTitle is specified, the text specified by Title is displayed (if there is any). </p>
<dt>PressTitle <i>name</i></p>
<dd>Specifies the title to be written on the button when the button is pressed. If no PressTitle is specified, the text specified by Title is displayed (if there is any). </p>
<dt>Legacy fields [<i>title icon command</i>]</p>
<dd>These fields are kept for compatibility with previous versions of FvwmButtons, and their use is discouraged. The <i>title</i> field is similar to the option Title <i>name</i>. If the title field is &quot;-&quot;, no title is displayed. The <i>icon</i> field is similar to the option Icon <i>filename</i>. If the icon field is &quot;-&quot; no icon is displayed. The <i>command</i> field is similar to the option Action <i>command</i> or alternatively Swallow &quot;<i>hangon</i>&quot; <i>command</i>.</p>
<dt>The <i>command</i></p>
<dd>Any fvwm command is recognized by FvwmButtons. See <a href="/docs/linux/man/1-fvwm/">fvwm</a>(1) for more information. </p>
<p> The Exec command has a small extension when used in Actions, its syntax is: </p>
<pre> Exec [&quot;hangon&quot;] command</pre>
<p>Example: </p>
<pre> *FvwmButtons: (Action Exec &quot;xload&quot; xload)</pre>
<p>The hangon string must be enclosed in double quotes. When FvwmButtons finds such an Exec command, the button remains pushed in until a window whose name, class or resource matches the quoted portion of the command is encountered. This is intended to provide visual feedback to the user that the action he has requested will be performed. The hangon string may contain wildcard characters (&#8216;*&#8217;) that match any substring. If the quoted portion contains no characters, then the button will pop out immediately. Note that users can continue pressing the button, and re-executing the command, even when it looks pressed in. </p>
<dt>Quoting</p>
<dd>Any string which contains whitespace must be quoted. Contrary to earlier versions commands no longer need to be quoted. In this case any quoting character will be passed on to the application untouched. Only commas &#8216;,&#8217; and closing parentheses &#8216;)&#8217; have to be quoted inside a command. Quoting can be done with any of the three quotation characters; single quote: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8216;This is a&nbsp;<wbr>&quot;quote&quot;&#8217;, </p>
<p> double quote: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;It&#8217;s another&nbsp;<wbr>`quote&#8217;&quot;, </p>
<p> and back quote: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>`This is a strange quote`. </p>
<p> The back quoting is unusual but used on purpose, if you use a preprocessor like FvwmCpp and want it to get into your commands, like this: </p>
<pre> #define BG gray60
 *FvwmButtons: (Swallow &quot;xload&quot; `Exec xload -bg BG &amp;`)</pre>
<p>Any single character can be quoted with a preceding backslash &#8216;\&#8217;.</dl>
</dl>
</dl>
<h2>Creating Panels</h2>
<p>Former versions of FvwmButtons (fvwm 2.0.46 to 2.3.6) had a different way of handling panels. You can not use your old panel configuration with the new panel feature. Read &quot;CONVERTING OLD PANEL CONFIGURATIONS&quot; for more information. </p>
<h3>How To Create New Panels</h3>
<p>Any program that can be launched from within fvwm and that has a window can be used as a panel. A terminal window could be your panel, or some application like xload or xosview or another fvwm module, including FvwmButtons itself. All you need to know is how to start your application from fvwm. </p>
<p> The button that invokes the panel is as easily configured as any other button. Essentially you need nothing more than the <i>Panel</i> option: </p>
<pre>*FvwmButtons: (Panel my_first_panel \
 &quot;Module FvwmButtons -g -30000-30000 my_first_panel&quot;)
*FvwmButtons: (Panel my_second_panel \
 &quot;Exec exec xterm -g -30000-30000 -n my_second_panel&quot;)</pre>
<p>This works like the <i>Swallow</i> option. The difference is that the application is not put into the button when it starts up but instead hidden from view. When you press the button for the panel the window slides into view. The &#8216;-g -30000-30000&#8217; option tells the application that it should be created somewhere very far to the top and left of your visible screen. Otherwise you would see it flashing for a moment when FvwmButtons starts up. Some applications do not work well with this kind of syntax so you may have to live with the short flashing of the window. If you want to make a panel from another instance of FvwmButtons you can do so, but you must give it a different name (&#8216;my_first_panel&#8217; in above example). If you run FvwmButtons under the same name, new panels are created recursively until your system runs out of resources and FvwmButtons crashes! To configure a second button bar with a different name, simply put &#8216;*new_name&#8217; in place of &#8216;*FvwmButtons&#8217; in your configuration file. If you are not familiar with the <i>Swallow</i> option or if you want to learn more about how &#8216;swallowing&#8217; panels works, refer to the description of the <i>Swallow</i> option. </p>
<p> Now that your panel basically works you will want to tune it a bit. You may not want a window title on the panel. To disable the title use the fvwm <i>Style</i> command. If your button bar is &#8216;sticky&#8217; you may want to make the panel sticky too. And probably the panel window should have no icon in case it is iconified. </p>
<pre>Style name_of_panel_window NoTitle, Sitcky, NoIcon</pre>
<p>You may want your panel to stay open only until you select something in it. You can give FvwmButtons the <i>-transientpanel</i> option after the -g option in the command. FvwmPager has a similar option &#8216;-transient&#8217;. </p>
<p> Last, but not least, you can now put an icon, a title or a small arrow in the button so that you can see what it is for. A title or icon can be specified as usual. To activate the arrow, just add &#8216;(indicator)&#8217; after the &#8216;Panel&#8217; keyword in the example above and the <i>Padding</i> option to leave a few pixels between the arrow and the border of the button. An optional direction in which the panel is opened can be given too: </p>
<pre>*FvwmButtons: (Padding 2, Panel(down, indicator) my_first_panel \
 &quot;Module FvwmButtons -g -30000-30000 -transientpanel my_first_panel&quot;)</pre>
<p>There are several more options to configure how your panel works, for example the speed and smoothness of the sliding animation. Please refer to the description of the <i>Panel</i> option for further details. </p>
<h3>Converting Old Panel Configurations</h3>
<p>This section describes how to convert a pretty old syntax used in 2.2.x versions. You may skip it if your syntax is more recent. </p>
<p> With the old panel feature you first had one or more lines defining panels in your main FvwmButtons configuration: </p>
<pre>...
*FvwmButtons(Title WinOps,Panel WinOps)
*FvwmButtons(Title Tools ,Panel Tools)
...</pre>
<p>After the last configuration line for the main panel the configuration of the first panel followed, introduced with a line beginning with *FvwmButtonsPanel: </p>
<pre>*FvwmButtonsPanel WinOps
*FvwmButtonsBack bisque2
...
*FvwmButtonsPanel Tools
*FvwmButtonsBack bisque2
...</pre>
<p>And perhaps you had style commands for you panels: </p>
<pre>Style FvwmButtonsPanel Title, NoHandles, BorderWidth 0
Style FvwmButtonsPanel NoButton 2, NoButton 4, Sticky</pre>
<p>The new configuration looks much the same, but now the configuration of the main panel is independent of the configuration of the sub panels. The lines invoking the panels use the same syntax as the Swallow option, so you simply add the name of the window to use as a panel and the command to execute instead of the panel name. Note that you give the new instance of FvwmButtons a different name. </p>
<pre>*FvwmButtons: (Title WinOps, Panel WinOps \
 &quot;Module FvwmButtons WinOps&quot;)
*FvwmButtons: (Title Tools , Panel Tools \
 &quot;Module FvwmButtons Tools&quot;)</pre>
<p>If you used something like &#8216;Panel-d&#8217; you now have to use &#8216;Panel(down)&#8217; instead. To make the new panel vanish as soon as a button was selected start FvwmButtons with the &#8216;-transientpanel&#8217; option: </p>
<pre>*FvwmButtons: (Title Tools , Panel(down) Tools \
 &quot;Module FvwmButtons -transientpanel Tools&quot;)</pre>
<p>The rest of the configuration is very easy to change. Delete the lines &#8216;*FvwmButtonsPanel &lt;name&gt;&#8217; and add &lt;name&gt; to all of the following configuration lines for the panel instead. Use the same name in your Style commands: </p>
<pre>*WinOps: Back bisque2
...
*Tools: Back bisque2
...
Style &quot;WinOps&quot; Title, NoHandles, BorderWidth 0
Style &quot;WinOps&quot; NoButton 2, NoButton 4, Sticky
Style &quot;Tools&quot; Title, NoHandles, BorderWidth 0
Style &quot;Tools&quot; NoButton 2, NoButton 4, Sticky</pre>
<p>That&#8217;s it. The new panels are much more flexible. Please refer to other parts of this documentation for details. </p>
<h3>Why Was The Panel Feature Rewritten?</h3>
<p>There are several reasons. The most important one is that the program code implementing the panels was very disruptive and caused a lot of problems. At the same time it made writing new features for FvwmButtons difficult at best. The second reason is that most users were simply unable to make it work &#8211; it was way too complicated. Even I (the author of the new code) had to spend several hours before I got it working the first time. The third reason is that the new panels are more versatile. Any application can be a panel in FvwmButtons, not just other instances of FvwmButtons itself. So I sincerely hope that nobody is angry about the change. Yes &#8211; you have to change your configuration, but the new feature is much easier to configure, especially if you already know how the Swallow option works. </p>
<h2>Arrangement Algorithm</h2>
<p>FvwmButtons tries to arrange its buttons as best it can, by using recursively, on each container including the buttonbox itself, the following algorithm.</p>
<dl>
<dt>Getting the size right</p>
<dd>First it calculates the number of button unit areas it will need, by adding the width times the height in buttons of each button. Containers are for the moment considered a normal button. Then it considers the given <i>rows</i> and <i>columns</i> arguments. If the number of rows is given, it will calculate how many columns are needed, and stick to that, unless <i>columns</i> is larger, in which case you will get some empty space at the bottom of the buttonbox. If the number of columns is given, it calculates how many rows it needs to fit all the buttons. If neither is given, it assumes you want two rows, and finds the number of columns from that. If the BoxSize option is set to <i>smart</i> at least the height/width of the tallest/widest button is used while the <i>fixed</i> value prevents the box from getting resized if both <i>rows</i> and <i>columns</i> have been set to non-zero.</p>
<dt>Shuffling buttons</p>
<dd>Now it has a large enough area to place the buttons in, all that is left is to place them right. There are two kinds of buttons: fixed and floating buttons. A fixed button is forced to a specific slot in the button box by a x/y geometry argument. All other buttons are considered floating. Fixed buttons are placed first. Should a fixed button overlap another one or shall be place outside the buttons window, FvwmButtons exits with an error message. After that the floating buttons are placed. The algorithm tries to place the buttons in a left to right, top to bottom western fashion. If a button fits at the suggested position it is placed there, if not the current slot stays empty and the slot to the right will be considered. After the button has been placed, the next button is tried to be placed in the next slot and so on until all buttons are placed. Additional rows are added below the bottom line of buttons until all buttons are placed if necessary if the BoxSize option <i>smart</i> is used.</p>
<dt>Containers</p>
<dd>Containers are arranged by the same algorithm, in fact they are shuffled recursively as the algorithm finds them.</p>
<dt>Clarifying example</p>
<dd>An example might be useful here: Suppose you have 6 buttons, all unit sized except number two, which is 2&#215;2. This makes for 5 times 1 plus 1 times 4 equals 9 unit buttons total area. Assume you have requested 3 columns. </p>
<pre>1) +---+---+---+ 2) +---+---+---+ 3) +---+---+---+
 | 1 | | | 1 | | | 1 | |
 +---+ + +---+ 2 + +---+ 2 +
 | | | | | | 3 | |
 + + + +---+---+ +---+---+---+
 | | | | | | | |
 +-----------+ +---+-------+ +---+---+---+
4) +---+---+---+ 5) +---+-------+ 6) +---+-------+
 | 1 | | | 1 | | | 1 | |
 +---+ 2 + +---+ 2 | +---+ 2 |
 | 3 | | | 3 | | | 3 | |
 +---+---+---+ +---+---+---+ +---+-------+
 | 4 | | | 4 | 5 | | | 4 | 5 | 6 |
 +---+---+---+ +---+---+---+ +---+---+---+</pre>
<dt>What size will the buttons be?</p>
<dd>When FvwmButtons has read the icons and fonts that are required by its configuration, it can find out which size is needed for every non-swallowing button. The unit button size of a container is set to be large enough to hold the largest button in it without squeezing it. Swallowed windows are simply expected to be comfortable with the button size they get from this scheme. If a particular configuration requires more space for a swallowed window, it can be set in that button&#8217;s configuration line using the option &quot;Size <i>width height</i>&quot;. This will tell FvwmButtons to give this button at least <i>width</i> by <i>height</i> pixels inside the relief and padding. </p>
</dl>
<h2>Dynamical Actions</h2>
<p>A running FvwmButtons instance may receive some commands at run time. This is achived using the fvwm command </p>
<pre>SendToModule FvwmButtons-Alias &lt;action&gt; &lt;params&gt;</pre>
<p>Supported actions: </p>
<dl>
<dt>ChangeButton <i>button_id</i> options</p>
<dd>can be used to change the title or icon of a button at run time. <i>button_id</i> is the id of the button to change as specified using the <code>Id</code> button option. It may also be a number, in this case the button with the given number is assumed. And finally, <i>button_id</i> may be in the form +x+y, where x and y are a column number and a row number of the button to be changed. It is possible to specify multiple option pairs (name with value) by delimiting them using comma. Currently options include <code>Title</code>, <code>ActiveTitle</code>, <code>PressTitle</code>, <code>Icon</code>, <code>ActiveIcon</code> and <code>PressIcon</code>. These options work like the configuration options of the same name. </p>
<dt>ExpandButtonVars <i>button_id</i> command</p>
<dd>replaces variables present in the <i>command</i> exactly like in the <code>Action</code> button option and then sends the command back to fvwm. <i>button_id</i> has the same syntax as described in <code>ChangeButton</code> above. </p>
<dt>PressButton <i>button_id</i> [<i>mouse_button</i>]</p>
<dd>simulates a mouse click on a button. <i>button_id</i> is the id of the button to press as specified using the <code>Id</code> button option and <i>mouse_button</i> is the number of mouse button used to click on the button e.g &quot;1&quot; for the left mouse button etc. Quotes around the number are not necessary. If <i>mouse_button</i> option is omitted, mouse button 1 is assumed. This command behaves exactly as if the mouse button was pressed and released on the button on in question. </p>
<dt>Silent</p>
<dd>This prefix may be specified before other actions. It disables all possible error and warning messages. </p>
<dt>Example:</p>
<dd>
<pre>*FvwmButtons: (Id note1, Title &quot;13:30 - Dinner&quot;, Icon clock1.xpm)
SendToModule FvwmButtons Silent \
 ChangeButton note1 Icon clock2.xpm, Title &quot;18:00 - Go Home&quot;</pre>
</dl>
<h2>Sample Configuration</h2>
<p>The following are excerpts from a .fvwm2rc file which describe FvwmButtons initialization commands: </p>
<pre>##########################################################
# Load any modules which should be started during fvwm
# initialization
# Make sure FvwmButtons is always there.
AddToFunc StartFunction &quot;I&quot; Module FvwmButtons
# Make it titlebar-less, sticky, and give it an icon
Style &quot;FvwmButtons&quot; Icon toolbox.xpm, NoTitle, Sticky
# Make the menu/panel look like CDE
Style &quot;WinOps&quot; Title, NoHandles, BorderWidth 0
Style &quot;WinOps&quot; NoButton 2, NoButton 4, Sticky
Style &quot;Tools&quot; Title, NoHandles, BorderWidth 0
Style &quot;Tools&quot; NoButton 2, NoButton 4, Sticky
##########################################################
DestroyModuleConfig FvwmButtons: *
*FvwmButtons: Fore Black
*FvwmButtons: Back rgb:90/80/90
*FvwmButtons: Geometry -135-5
*FvwmButtons: Rows 1
*FvwmButtons: BoxSize smart
*FvwmButtons: Font -*-helvetica-medium-r-*-*-12-*
*FvwmButtons: Padding 2 2
*FvwmButtons: (Title WinOps, Panel WinOps \
 &quot;Module FvwmButtons -transientpanel WinOps&quot;)
*FvwmButtons: (Title Tools, Panel Tools \
 &quot;Module FvwmButtons -transientpanel Tools&quot;)
*FvwmButtons: (Title Resize, Icon resize.xpm, Action Resize)
*FvwmButtons: (Title Move, Icon arrows2.xpm, Action Move )
*FvwmButtons: (Title Lower, Icon Down, Action Lower )
*FvwmButtons: (Title Raise, Icon Up, Action Raise )
*FvwmButtons: (Title Kill, Icon bomb.xpm, Action Destroy)
*FvwmButtons: (1x1,Container(Rows 3,Frame 1))
*FvwmButtons: (Title Dopey ,Action \
 `Exec &quot;big_win&quot; xterm -T big_win -geometry 80x50 &amp;`)
*FvwmButtons: (Title Snoopy, Font fixed, Action \
 `Exec &quot;small_win&quot; xterm -T small_win &amp;`)
*FvwmButtons: (Title Smokin')
*FvwmButtons: (End)
*FvwmButtons: (Title Xcalc, Icon rcalc.xpm, \
 Action `Exec &quot;Calculator&quot; xcalc &amp;`)
*FvwmButtons: (Title XMag, Icon magnifying_glass2.xpm, \
 Action `Exec &quot;xmag&quot; xmag &amp;`)
*FvwmButtons: (Title Mail, Icon mail2.xpm, \
 Action `Exec &quot;xmh&quot; xmh &amp;`)
*FvwmButtons: (4x1, Swallow &quot;FvwmPager&quot; `FvwmPager 0 3` \
 Frame 3)
*FvwmButtons: (Swallow(UseOld,NoKill) &quot;xload15&quot; `Exec xload \
 -title xload15 -nolabel -bg rgb:90/80/90 -update 15 \
 -geometry -3000-3000 &amp;`)</pre>
<p>The last lines are a little tricky &#8211; one spawns an FvwmPager module, and captures it to display in a quadruple width button. is used, the Pager will be as big as possible within the button&#8217;s relief. </p>
<p> The final line is even more magic. Note the combination of <i>UseOld</i> and <i>NoKill</i>, which will try to swallow an existing window with the name &quot;xload15&quot; when starting up (if failing: starting one with the specified command), which is un-swallowed when ending FvwmButtons. The swallowed application is started with &quot;-geometry -3000-3000&quot; so that it will not be visible until its swallowed. </p>
<p> The other panels are specified after the root panel: </p>
<pre>########## PANEL WinOps
DestroyModuleConfig WinOps: *
*WinOps: Back bisque2
*WinOps: Geometry -3-3
*WinOps: Columns 1
*WinOps: (Title Resize, Icon resize.xpm, Action Resize)
*WinOps: (Title Move, Icon arrows2.xpm, Action Move )
*WinOps: (Title Lower, Icon Down, Action Lower )
*WinOps: (Title Raise, Icon Up, Action Raise )
########## PANEL Tools
DestroyModuleConfig Tools: *
*Tools: Back bisque2
*Tools: Geometry -1-1
*Tools: Columns 1
*Tools: (Title Kill, Icon bomb.xpm, Action Destroy)</pre>
<p>The color specification <i>rgb:90/80/90</i> is actually the most correct way of specifying independent colors in X, and should be used instead of the older <i>#908090</i>. If the latter specification is used in your configuration file, you should be sure to escape the hash in any of the <i>command</i>s which will be executed, or fvwm will consider the rest of the line a comment. </p>
<p> Note that with the x/y geometry specs you can easily build button windows with gaps. Here is another example. You can not accomplish this without geometry specs for the buttons: </p>
<pre>##########################################################
# Another example
##########################################################
# Make it titlebar-less, sticky, and give it an icon
Style &quot;FvwmButtons&quot; Icon toolbox.xpm, NoTitle, Sticky
DestroyModuleConfig FvwmButtons: *
*FvwmButtons: Font 5x7
*FvwmButtons: Back rgb:90/80/90
*FvwmButtons: Fore black
*FvwmButtons: Frame 1
# 9x11 pixels per button, 4x4 pixels for the frame
*FvwmButtons: Geometry 580x59+0-0
*FvwmButtons: Rows 5
*FvwmButtons: Columns 64
*FvwmButtons: BoxSize fixed
*FvwmButtons: Padding 1 1
# Pop up a module menu directly above the button.
*FvwmButtons: (9x1+3+0, Padding 0, Title &quot;Modules&quot;, \
 Action `Menu Modulepopup rectangle \
 $widthx$height+$lleft+$top o+50 -100m`)
# first row of buttons from left to right:
*FvwmButtons: (3x2+0+1, Icon my_lock.xpm, Action `Exec xlock`)
*FvwmButtons: (3x2+3+1, Icon my_recapture.xpm, Action Recapture)
*FvwmButtons: (3x2+6+1, Icon my_resize.xpm, Action Resize)
*FvwmButtons: (3x2+9+1, Icon my_move.xpm, Action Move)
*FvwmButtons: (3x2+12+1, Icon my_fvwmconsole.xpm, \
 Action 'Module FvwmConsole')
# second row of buttons from left to right:
*FvwmButtons: (3x2+0+3, Icon my_exit.xpm, Action QuitSave)
*FvwmButtons: (3x2+3+3, Icon my_restart.xpm, Action Restart)
*FvwmButtons: (3x2+6+3, Icon my_kill.xpm, Action Destroy)
*FvwmButtons: (3x2+9+3, Icon my_shell.xpm, Action 'Exec rxvt')
# big items
*FvwmButtons: (10x5, Swallow (NoKill, NoCLose) \
 &quot;FvwmPager&quot; 'FvwmPager * * -geometry 40x40-1024-1024')
*FvwmButtons: (6x5, Swallow &quot;FvwmXclock&quot; `Exec xclock \
 -name FvwmXclock -geometry 40x40+0-3000 -padding 1 \
 -analog -chime -bg rgb:90/80/90`)
*FvwmButtons: (13x5, Swallow (NoClose) \
&quot;FvwmIconMan&quot; 'Module FvwmIconMan')
*FvwmButtons: (20x5, Padding 0, Swallow &quot;xosview&quot; \
 `Exec /usr/X11R6/bin/xosview -cpu -int -page -net \
 -geometry 100x50+0-3000 -font 5x7`)</pre>
<h2>Bugs</h2>
<p>The action part of the Swallow option must be quoted if it contains any whitespace character. </p>
<h2>Copyrights</h2>
<p>The FvwmButtons program, and the concept for interfacing this module to the Window Manager, are all original work by Robert Nation. </p>
<p> Copyright 1993, Robert Nation. No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact. </p>
<p> Further modifications and patching by Jarl Totland, copyright 1996. The statement above still applies. </p>
<h2>Author</h2>
<p>Robert Nation. Somewhat enhanced by Jarl Totland, Jui-Hsuan Joshua Feng, Scott Smedley.</p>
