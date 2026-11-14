---
title: "fvwmwinlist(1)"
name: "fvwmwinlist"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmwinlist/"
description: "FvwmWinList – the fvwm window list module"
---

<p>FvwmWinList &#8211; the fvwm window list module </p>
<h2>Synopsis</h2>
<p><code>FvwmWinList</code> [<i>name</i>] </p>
<p> FvwmWinList is spawned by fvwm, so no command line invocation will work. </p>
<h2>Description</h2>
<p>The FvwmWinList module provides a window list made up of buttons, each corresponding to a window that fvwm is managing. Clicking on the buttons with any of the three mouse buttons will either do a default action or can be user configured. Like the other modules, FvwmWinList only works when fvwm is used as the window manager. </p>
<h2>Copyrights</h2>
<p>The FvwmWinList module is the original work of Mike Finger. </p>
<p> Copyright 1994, Mike Finger. The author makes no guarantees or warranties of any kind about the use of this module. Use this modules at your own risk. You may freely use this module or any portion of it for any purpose as long as the copyright is kept intact. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmWinList</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>). Available options are discussed in a later section. </p>
<h2>Invocation</h2>
<p>FvwmWinList can be invoked by fvwm during initialization by inserting the line &#8216;Module FvwmWinList&#8217; in the .fvwm2rc file. </p>
<p> FvwmWinList can also be bound to a keystroke, mouse button, or menu option to be invoked later, in this case using &#8216;Transient&#8217; as an argument will cause FvwmWinList to resemble the built in window list. </p>
<h2>Configuration Options</h2>
<dl>
<dt>*FvwmWinList: Geometry <i>{+-}&lt;X&gt;{+-}&lt;Y&gt;</i></p>
<dd>Specifies the location and gravity of the FvwmWinList window. At the current time, size is not supported and FvwmWinList will resize itself as buttons are added. If the NoAnchor option is not specified then the windows gravity corner will be anchored, and the window will grow in the opposite direction. (i.e. If the geometry is specified -5-5, that is SoutEastGravity. This will cause the window to draw up and to the left as windows are added) </p>
<dt>*FvwmWinList: Font <i>font</i></p>
<dd>Specifies the font to be used for labeling the buttons. </p>
<dt>*FvwmWinList: Colorset <i>n</i></p>
<dd>Specifies the colorset to use for the buttons. See FvwmTheme. Defaults to 0. </p>
<dt>*FvwmWinList: Fore <i>color</i></p>
<dd>Specifies the color to use for the button names. Cancels *FvwmWinList: Colorset. </p>
<dt>*FvwmWinList: Back <i>color</i></p>
<dd>Specifies the color for the buttons. Cancels *FvwmWinList: Colorset. </p>
<dt>*FvwmWinList: FocusColorset <i>n</i></p>
<dd>Specifies the colorset to use for the button for the window that has the input focus. Defaults to 1. </p>
<dt>*FvwmWinList: FocusFore <i>color</i></p>
<dd>Specifies the color to use for the button names for the window that has the input focus. If omitted, the color from <code>*FvwmWinList: Fore</code> is used. Cancels *FvwmWinList: FocusColorset. </p>
<dt>*FvwmWinList: FocusBack <i>color</i></p>
<dd>Specifies the color to use for the button for the window that has the input focus. If omitted, the color from <code>*FvwmWinList: Back</code> is used. Cancels *FvwmWinList: FocusColorset. </p>
<dt>*FvwmWinList: IconColorset <i>n</i></p>
<dd>Specifies the colorset to use for buttons for windows that are iconified. Defaults to 0. </p>
<dt>*FvwmWinList: IconFore <i>color</i></p>
<dd>Specifies the color to use for the button names for windows that are iconified. If omitted, the color from <code>*FvwmWinList: Fore</code> is used. Cancels *FvwmWinList: IconColorset. </p>
<dt>*FvwmWinList: IconBack <i>color</i></p>
<dd>Specifies the color to use for the button for windows that are iconified. If omitted, the color from <code>*FvwmWinList: Back</code> is used. Cancels *FvwmWinList: IconColorset. </p>
<dt>*FvwmWinList: DontDepressFocus</p>
<dd>By default FvwmWinList will show the button for the window that has the input focus as pressed in. This option disables that feature. </p>
<dt>*FvwmWinList: ButtonFrameWidth <i>width</i></p>
<dd>Specify the width of the 3D borders around the buttons in FvwmWinList. </p>
<dt>*FvwmWinList: FollowWindowList</p>
<dd>Specifies that FvwmWinList will keep its list in the same order as fvwm. This is the order displayed by the &quot;WindowList NoDeskSort&quot; fvwm command. This is not the default as it is more visually disturbing when the focus changes. </p>
<dt>*FvwmWinList: UseSkipList</p>
<dd>Tells FvwmWinList to not show the windows that are listed on a WindowListSkip line in the configuration file. </p>
<dt>*FvwmWinList: ShowCurrentDesk</p>
<dd>Specifies that only windows on the current desk are displayed. </p>
<dt>*FvwmWinList: NoAnchor</p>
<dd>By default, FvwmWinList will anchor the gravity corner so the window will grow in the opposite direction. This undoes that option, i.e. the window will always grow down. Do not use this option if a negative geometry was specified. </p>
<dt>*FvwmWinList: UseIconNames</p>
<dd>Tells FvwmWinList to use the icon name of the window instead of the full window name. This is useful to keep the width of the window small. </p>
<dt>*FvwmWinList: LeftJustify</p>
<dd>By default, FvwmWinList will center the icon text in the icon. This option causes it to be justified flush with the left edge of the icon. This option is turned on when MiniIcons are used. </p>
<dt>*FvwmWinList: MinWidth <i>width</i></p>
<dd>
<dt>*FvwmWinList: MaxWidth <i>width</i></p>
<dd>Specify the minimum and maximum widths that the buttons will shrink or grow to. The buttons will normally size to fit the longest name, but certain applications produce icon titles that can easily fill the screen. Setting these parameters constrains the size of the buttons to be between the two values. Setting them identically will fix the size of the buttons. Setting Max &lt; Min will have unpredictable results. </p>
<dt>*FvwmWinList: TruncateLeft</p>
<dd>If names get truncated because of the setting of <code>FvwmWinList: MaxWidth</code>, they will normally get truncated on the right, so only the start of the names are visible. Setting this resource will cause them to get truncated on the left, so that the end of names are visible. This is useful when the window title contains a directory and file name, for example. </p>
<dt>*FvwmWinList: Action <i>action response</i></p>
<dd>Tells FvwmWinList to do <i>response</i> when <i>action</i> is done. The currently supported <i>action</i>s are: Click1, Click2, Click3 and so on. By default the module supports 3 mouse buttons, but it can be compiled to support more. The currently supported <i>response</i>s are any fvwm built-in commands, including modules and functions. Warning: The use of the former syntax that allowed to use comma separated lists of commands is strongly discouraged due to synchronization problems with fvwm. Please use complex fvwm functions instead (defined with the &#8216;AddToFunc&#8217; command of fvwm). </p>
<dt>*FvwmWinList: NoIconAction <i>action</i></p>
<dd>Tells FvwmWinList to do <i>action</i> is when a NoIcon style window is iconified or de-iconified. Relevant coordinates are appended to <i>action</i> so that the icon can be traced to an FvwmWinList button. An example action is &quot;*FvwmWinList: NoIconAction SendToModule FvwmAnimate animate&quot;. A blank or null action turns this feature off. </p>
</dl>
<h2>Sample Configuration</h2>
<p>The following are excepts from a .fvwm2rc file which describe FvwmWinList initialization commands: </p>
<pre>########
# Pop up the window list in transient mode on button 3 press &amp; hold
Mouse 3 R A Module FvwmWinList Transient
AddToFunc DeiconifyAndRaise
+ I Iconify off
+ I Raise
########################## Window-Lister ###############################
*FvwmWinList: Back DarkOliveGreen
*FvwmWinList: Fore PaleGoldenRod
*FvwmWinList: Font -*-new century schoolbook-bold-r-*-*-*-120-*-*-*-*-*-*
*FvwmWinList: Action Click1 Function DeiconifyAndRaise
*FvwmWinList: Action Click2 Iconify
*FvwmWinList: Action Click3 Module FvwmIdent
*FvwmWinList: UseSkipList
*FvwmWinList: UseIconNames
*FvwmWinList: Geometry -50-85
*FvwmWinList: MinWidth 70
*FvwmWinList: MaxWidth 120
# I prefer the text centered
#*FvwmWinList: LeftJustify
# I like it anchored
#*FvwmWinList: NoAnchor
# A flat list in most recently focused order
#*FvwmWinList: FollowWindowList
#*FvwmWinList: BorderReliefWidth 0
# pretend to be a taskbar
*FvwmWinList: NoIconAction SendToModule FvwmAnimate animate</pre>
<h2>Author</h2>
<p>Mike Finger (mfinger [at] mermaid.micro.umn.edu)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Mike_Finger [at] atk.com)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(doodman on IRC, check the&nbsp;<wbr>#linux channel) </p>
<p> Various Patches by<br />
John Heidemann&nbsp;<wbr>&lt;johnh [at] ficus.CS.UCLA.EDU&gt;&nbsp;<wbr>and<br />
Jason L Tibbitts&nbsp;<wbr>&lt;tibbs [at] tcamc.uh.edu&gt;.</p>
