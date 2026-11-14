---
title: "fvwmtaskbar(1)"
name: "fvwmtaskbar"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmtaskbar/"
description: "FvwmTaskBar – the fvwm taskbar module"
---

<p>FvwmTaskBar &#8211; the fvwm taskbar module </p>
<h2>Synopsis</h2>
<p><code>FvwmTaskBar</code> [<i>name</i>] </p>
<p> FvwmTaskBar is spawned by fvwm, so no command line invocation will work. </p>
<h2>Description</h2>
<p>The FvwmTaskBar module provides a taskbar made up of buttons arranged by rows, each corresponding to a window that fvwm is managing. Clicking on first button gives focus to the corresponding top level window; clicking on the middle button will hide a top level window; third mouse button is reserved for a future extension (context menu). Like the other modules, FvwmTaskBar only works when fvwm is used as the window manager. </p>
<p> When started, the taskbar shows up as a single row of buttons filling the full width of the screen, but during the work can be resized to accommodate up to 8 rows. In addition, if the AutoStick option is used, the taskbar will auto position itself at the top or bottom of the screen, and can be dragged from one position to another with a normal move operation. </p>
<p> The first button of the taskbar, labelled &quot;Start&quot; sends a &quot;Popup StartMenu&quot; command to the fvwm, which can be used to pop-up a general-purpose menu when the button is pressed. </p>
<p> The FvwmTaskBar also displays at the right side a window showing the current time and the built-in incoming mail indicator. </p>
<h2>Copyrights</h2>
<p>The FvwmTaskBar module is derived from Mike Finger&#8217;s FvwmWinList. </p>
<p> Copyright 1994, Mike Finger. The author makes no guarantees or warranties of any kind about the use of this module. Use this module at your own risk. You may freely use this module or any portion of it for any purpose as long as the copyright is kept intact. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmTaskBar</i> gets configuration information from fvwm to find the options that pertain to it. These options are discussed in a later section. </p>
<h2>Invocation</h2>
<p>FvwmTaskBar can be invoked by fvwm during initialization by inserting the line &#8216;Module FvwmTaskBar&#8217; in the .fvwm2rc file. </p>
<p> FvwmTaskBar must reside in a directory that is listed in the ModulePath option of fvwm for it to be executed by fvwm. </p>
<h2>Configuration Options</h2>
<p>The following options can be placed in the .fvwm2rc file </p>
<dl>
<dt>*FvwmTaskBar: Geometry <i>{+-}&lt;X&gt;{+-}&lt;Y&gt;</i></p>
<dd>Specifies the location and gravity of the FvwmTaskBar window. Currently, this option is scanned as a normal X geometry string. You can include the width and the height in addition to the &quot;x&quot; and &quot;y&quot; offset. However, only the &quot;x&quot; and &quot;y&quot; offset are used. To avoid possible future compatibility problems, only code the &quot;x&quot; and &quot;y&quot; offset. </p>
<p> The actual width of the taskbar is always the full width of the screen and the height is controlled by the *FvwmTaskBar: Rows option. </p>
<p> If the AutoStick option is specified, the taskbar automatically &quot;sticks&quot; to the top or the bottom of the screen, whichever is closest to the geometry specification. </p>
<p> To position the taskbar at the bottom of the screen, use a geometry of &quot;+0-0&quot;. </p>
<dt>*FvwmTaskBar: Rows r</p>
<dd>Specifies the initial number in rows of the FvwmTaskBar window. Default is 1 and the maximum is 8. </p>
<dt>*FvwmTaskBar: Font <i>font</i></p>
<dd>Specifies the default font to be used for labeling the buttons, when they are not depressed. If not specified, fixed font is assumed. </p>
<dt>*FvwmTaskBar: SelFont <i>font</i></p>
<dd>Specifies the font to be used for the depressed buttons. Note that the Start button will always use this font even if is not pressed. If this option is not specified, the default font is used instead. </p>
<dt>*FvwmTaskBar: StatusFont <i>font</i></p>
<dd>Specifies the font to be used for the clock and tip windows. If this option is not specified, fixed font is used. </p>
<dt>*FvwmTaskBar: Fore <i>color</i></p>
<dd>Specifies the color to use for the button names. </p>
<dt>*FvwmTaskBar: Back <i>color</i></p>
<dd>Specifies the background color for the bar and buttons. </p>
<dt>*FvwmTaskBar: Colorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for the window background and the foreground color of the buttons. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>*FvwmTaskBar: IconFore <i>color</i></p>
<dd>Specifies the color to use for the button names which represent iconified windows. </p>
<dt>*FvwmTaskBar: IconBack <i>color</i></p>
<dd>Specifies the color to use for the buttons which represent iconified windows. </p>
<dt>*FvwmTaskBar: IconColorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for the buttons of iconified windows. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>*FvwmTaskBar: FocusFore <i>color</i></p>
<dd>Specifies the color to use for the button which represents the window with the focus. If not specified the color specified by *FvwmTaskBar: Fore or *FvwmTaskBar: Colorset is used. </p>
<dt>*FvwmTaskBar: FocusBack <i>color</i></p>
<dd>Specifies the color to use for the button which represents the window with the focus. If not specified the color specified by *FvwmTaskBar: Back or *FvwmTaskBar: Colorset is used. Note that the button which represents the window with the focus is also highlighted. See &quot;*FvwmTaskBar: NoBrightFocus&quot;. </p>
<dt>*FvwmTaskBar: FocusColorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for the button which represents the window with the focus. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>*FvwmTaskBar: NoBrightFocus</p>
<dd>By default the button which represents the window with the focus is highlighted. This option disables this feature. <i>Note:</i> you will want this option if you use a pixmap (via FvwmTheme) for the background. </p>
<dt>*FvwmTaskBar: TipsFore <i>color</i></p>
<dd>Specifies the color to be used for the text in the tips windows. </p>
<dt>*FvwmTaskBar: TipsBack <i>color</i></p>
<dd>Specifies the background color for the tips windows. </p>
<dt>*FvwmTaskBar: TipsColorset <i>colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for the tips windows. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>*FvwmTaskBar: AutoStick</p>
<dd>This option causes the taskbar to &quot;stick&quot; either to the top or bottom of the screen, whichever is closest to the initial window placement. Any further move operation is also subject to that behavior. </p>
<dt>*FvwmTaskBar: AutoFocus</p>
<dd>This option causes the taskbar to raise a window if the cursor stays on a button in taskbar and its tip is open. </p>
<dt>*FvwmTaskBar: AutoHide [<i>pixels</i>]</p>
<dd>This option causes the taskbar to disappear leaving a narrow strip at the bottom of the screen, and reappear only when the mouse is moved to that strip. This option automatically enables AutoStick. The optional <i>pixels</i> parameter specifies thickness of a strip (3 pixels by default). </p>
<dt>*FvwmTaskBar: UseSkipList</p>
<dd>Tells FvwmTaskBar to not show the windows that are listed on a WindowListSkip line in the configuration file. </p>
<dt>*FvwmTaskBar: DeskOnly</p>
<dd>Tells FvwmTaskBar to show only windows that are on the current desktop. When desktops are switched, the list of windows changes accordingly. </p>
<dt>*FvwmTaskBar: PageOnly</p>
<dd>Tells FvwmTaskBar to show only windows that are on the same page as the task bar. When a window enters or leaves the page, the list of windows changes accordingly. </p>
<dt>*FvwmTaskBar: ScreenOnly</p>
<dd>Tells FvwmTaskBar to show only windows that are only on the same Xinerama screen as the task bar. When a window enters or leaves the screen, the list of windows changes accordingly. </p>
<dt>*FvwmTaskBar: UseIconNames</p>
<dd>Tells FvwmTaskBar to use the icon name of the window instead of the full window name. This is useful to keep the width of the buttons small. </p>
<dt>*FvwmTaskBar: ShowTransients</p>
<dd>Tells FvwmTaskBar to show the application transient windows also. By default they are not shown. </p>
<dt>*FvwmTaskBar: Action <i>action response</i></p>
<dd>Tells FvwmTaskBar to do <i>response</i> when <i>action</i> is done. The currently supported <i>action</i>s are: Click1, Click2, Click3 and so on. By default the module supports 5 mouse buttons, but it can be compiled to support more. The currently supported <i>response</i>s are any fvwm built-in commands, including modules and functions. Warning: Use of the former syntax that allowed to use comma separated lists of commands is strongly discouraged due to synchronization problems with fvwm. Please use complex fvwm functions instead (defined with the AddToFunc command of fvwm). </p>
<p> In the <i>response</i> part, you can use a number of predefined variables: <i>$left</i>, <i>$right</i>, <i>$top</i> and <i>$bottom</i> are substituted by the left, right, top and bottom coordinates of the button pressed. <i>$-left</i>, <i>$-right</i>, <i>$-top</i> and <i>$-bottom</i> are substituted likewise, but the coordinates are calculated from the bottom or the right edge of the screen instead (for a button that is 5 pixels away from the right screen border, $-right will be 5). <i>$width</i> and <i>$height</i> are replaced by the width or height of the button. All this is done regardless of any quoting characters. To get a literal &#8216;$&#8217; use the string &#8216;$$&#8217;. </p>
<dt>*FvwmTaskBar: Button Title <i>title</i>, Icon <i>icon</i>, Action <i>action</i></p>
<dd>Tells FvwmTaskBar to put a shortcut minibutton in the taskbar that does <i>action</i> when clicked. The icon can have a caption denoted by <i>title</i>, an icon denoted by <i>icon</i>, or a combination of the two. The icons will appear to the immediate right of the start button, and will appear in the order that they are declared in the .fvwm2rc file. </p>
<p> To invoke different commands for different mouse clicks, use this syntax: </p>
<pre>*FvwmTaskBar: Button Title <i>title</i>, Icon <i>icon</i>, \
 Action (Mouse 1) <i>action1</i>, Action (Mouse 2) <i>action2</i></pre>
<dt>*FvwmTaskBar: ButtonWidth <i>width</i></p>
<dd>Indicates the maximum width that window buttons should reach. (the minimum is hard coded at 32). </p>
<dt>*FvwmTaskBar: Pad <i>width</i></p>
<dd>Specifies the space (in pixels) between the window buttons. If this option is not specified, the default space is 3. </p>
<dt>*FvwmTaskBar: WindowButtonsLeftMargin <i>margin</i></p>
<dd>Specifies the space (in pixels) between the left side of the left-most window button and the right side of the start button or right-most shortcut minibutton. If this option is not specified, the default margin is 4. </p>
<dt>*FvwmTaskBar: WindowButtonsRightMargin <i>margin</i></p>
<dd>Specifies the space (in pixels) between the right side of the right-most window button and the left side of the clock and tip window. If this option is not specified, the default margin is 2. </p>
<dt>*FvwmTaskBar: StartButtonRightMargin <i>margin</i></p>
<dd>Specifies the space (in pixels) between the right side of the start button and the left side of the left-most shortcut minibutton. If this option is not specified, the default margin is 0. </p>
<dt>*FvwmTaskBar: 3DFvwm</p>
<dd>By default the buttons use a special (asymmetric) 3D look. This option enables a more classical 3D look (Ie., a la fvwm). </p>
<dt>*FvwmTaskBar: HighlightFocus</p>
<dd>If the mouse pointer is over the taskbar, the window under the current button is active. This behavior is like the TVTWM Icon Manager or FvwmIconMan. <i>Note:</i> If you use this option combined with FollowMouse focus style, you&#8217;ll want the taskbar to be ClickToFocus. </p>
<dt>*FvwmTaskBar: ShowTips</p>
<dd>Enables the tips windows (by default disabled). </p>
<dt>*FvwmTaskBar: NoIconAction <i>action</i></p>
<dd>Tells FvwmTaskBar to do <i>action</i> is when a NoIcon style window is iconified or de-iconified. Relevant coordinates are appended to <i>action</i> so that the icon can be traced to an FvwmTaskBar button. An example action is &quot;*FvwmTaskBar: NoIconAction SendToModule FvwmAnimate animate&quot;. A blank or null action turns this feature off. </p>
</dl>
<h2></h2>
<p>The following options deal more specifically with the status indicators displayed at the right of the taskbar. </p>
<dl>
<dt>*FvwmTaskBar: ClockFormat <i>format-string</i></p>
<dd>This option specifies the time format for the digital clock. It is a <i><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</i> compatible format string. By default it is &quot;%R&quot;. There is a 24 character limit for string expansion. The string depends of locale settings. </p>
<dt>*FvwmTaskBar: DateFormat <i>format-string</i></p>
<dd>This option specifies the date and/or time format for clock tip. It is a <i><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</i> compatible format string. By default it is &quot;%A, %B %d, %Y&quot;. There is 40 characters limit for string expansion. The string depends of locale settings now. </p>
<dt>*FvwmTaskBar: UpdateInterval <i>seconds</i></p>
<dd>Specifies how often the clock display should be refreshed, so that times of the form HH:MM:SS can be used. By default 60 seconds. </p>
<dt>*FvwmTaskBar: BellVolume <i>volume</i></p>
<dd>This sets the volume of the bell when mail is detected. It is a value between 0 (no bell) and 100 (maximum volume). By default it is set to 20. </p>
<dt>*FvwmTaskBar: MailBox <i>path</i></p>
<dd>This option instructs the module to look for mail at the specified place. It is a full pathname to the user&#8217;s mailbox. By default it is <i>/var/spool/mail/$USER_LOGIN</i>. A value of &#8216;None&#8217; instructs the module not to have a mail indicator. </p>
<dt>*FvwmTaskBar: MailDir</p>
<dd>By default format of the user&#8217;s mailbox is mbox. If this option is specified, the maildir format is used instead. </p>
<dt>*FvwmTaskBar: MailCommand <i>command</i></p>
<dd>Specifies a <i>fvwm</i> command to be executed when double-clicking on the mail icon. </p>
<dt>*FvwmTaskBar: MailCheck <i>seconds</i></p>
<dd>Specifies the interval between checks for new mail. The default is ten seconds. A value of zero or less switches mail checking off. </p>
<p> Note, this value is only relable when greater than the <i>UpdateInterval</i> value. The mail check is done either on any redraw (like a focus change) or every nearest factor of the <i>UpdateInterval</i> value. </p>
<dt>*FvwmTaskBar: IgnoreOldMail</p>
<dd>If set, draw no bitmap if there is no new mail. </p>
</dl>
<h2></h2>
<p>The following options deal with the Start button at the left of the taskbar: </p>
<dl>
<dt>*FvwmTaskBar: StartCommand <i>command</i></p>
<dd>This option specifies a command to run when the start button is pressed. Some strings are replaced in the command when it is executed like for the other buttons. See <code>Action</code> for details. If both, <code>StartCommand</code> and <code>StartMenu</code> have been defined, the command is executed first and the menu is opened afterwards. The <code>StartCommand</code> can be used to exactly place a menu atop a button. </p>
<pre>*FvwmTaskBar: StartCommand Popup StartMenu rectangle \
 $widthx$height+$left+$top 0 -100m</pre>
<p>To invoke different commands for different mouse clicks, use this syntax: </p>
<pre>*FvwmTaskBar: StartCommand (Mouse 1) Popup Mouse1Menu
*FvwmTaskBar: StartCommand (Mouse 3) Popup Mouse3Menu</pre>
<dt>*FvwmTaskBar: StartName <i>string</i></p>
<dd>This option specifies the string displayed in the Start button. (&#8216;Start&#8217; by default). If the string is omitted no string is displayed. </p>
<dt>*FvwmTaskBar: StartMenu <i>string</i></p>
<dd>This option specifies the pop up menu to invoke when the start button is pressed. (&#8216;StartMenu&#8217; by default). The module send a &#8216;Popup StartMenu&#8217; command to the fvwm window manager. </p>
<p> To invoke different menus for different mouse clicks, use this syntax: </p>
<pre>*FvwmTaskBar: StartMenu (Mouse 1) Mouse1Menu
*FvwmTaskBar: StartMenu (Mouse 3) Mouse3Menu</pre>
<dt>*FvwmTaskBar: StartIcon <i>icon-name</i></p>
<dd>This option specifies the name of the icon to display at the left of the Start button. </p>
<dt>*FvwmTaskBar: NoDefaultStartButton</p>
<dd>This option removes the default start button if no start button configuration options are given. It is useful to remove the start button. Note that this is the default if you use the Button configuration option. </p>
</dl>
<h2>Sample Configuration</h2>
<p>The following are excerpts from a .fvwm2rc file which describe FvwmTaskBar initialization commands: </p>
<pre>#
# Start the taskbar on fvwm startup and restart
#
AddToFunc &quot;StartFunction&quot; &quot;I&quot; Module FvwmTaskBar
#
# For Click 1 action
#
AddToFunc DeiconifyRaiseAndFocus
+ I Iconify off
+ I Raise
+ I Focus
#
# Set the style for the taskbar window, keep always on top of another
# windows
#
Style &quot;FvwmTaskBar&quot; NoTitle,BorderWidth 4, HandleWidth 4,Sticky,\
StaysOnTop,WindowListSkip,CirculateSkip
#------------------------------------ taskbar
*FvwmTaskBar: Back #c3c3c3
*FvwmTaskBar: Fore black
*FvwmTaskBar: TipsBack bisque
*FvwmTaskBar: TipsFore black
*FvwmTaskBar: Geometry +0-0
*FvwmTaskBar: Font -adobe-helvetica-medium-r-*-*-14-*-*-*-*-*-*-*
*FvwmTaskBar: SelFont -adobe-helvetica-bold-r-*-*-14-*-*-*-*-*-*-*
*FvwmTaskBar: StatusFont fixed
*FvwmTaskBar: Action Click1 DeiconifyRaiseAndFocus
*FvwmTaskBar: Action Click2 Iconify On
*FvwmTaskBar: Action Click3 Lower
*FvwmTaskBar: UseSkipList
*FvwmTaskBar: UseIconNames
*FvwmTaskBar: AutoStick
*FvwmTaskBar: ShowTips
*FvwmTaskBar: NoIconAction SendToModule FvwmAnimate animate
*FvwmTaskBar: ButtonWidth 180
*FvwmTaskBar: BellVolume 20
*FvwmTaskBar: MailBox /var/spool/mail/
*FvwmTaskBar: MailCommand Exec xterm -e mail
*FvwmTaskBar: ClockFormat %I:%M %p
*FvwmTaskBar: StartName Start
*FvwmTaskBar: StartMenu StartMenu
*FvwmTaskBar: StartIcon mini-exp.xpm
*FvwmTaskBar: Button Title Mozilla, Action exec exec /usr/local/mozilla/mozilla
*FvwmTaskBar: Button Icon mini.term.xpm, Action exec exec xterm
*FvwmTaskBar: Button Title Freeamp, Icon mini.cd.xpm, Action exec exec freeamp</pre>
<h2>Bugs</h2>
<p>There is a bug report that FvwmTaskBar doesn&#8217;t work well with auto hide turned on. </p>
<h2>Author</h2>
<dl>
<dt><i>David Barth</i> &lt;barth [at] di.epfl.ch&gt;</p>
<dd></dl>
<h2>Acknowledgments</h2>
<p>These people have contributed to <code>FvwmTaskBar</code>: </p>
<dl>
<dt><i>Danny Dulai</i> &lt;nirva [at] ishiboo.com&gt;</p>
<dd>
<dt><i>fvwm workers</i> &lt;fvwm-workers [at] fvwm.org&gt;</p>
<dd></dl>
