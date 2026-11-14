---
title: "fvwmiconman(1)"
name: "fvwmiconman"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmiconman/"
description: "FvwmIconMan – an fvwm icon manager"
---

<p>FvwmIconMan &#8211; an fvwm icon manager </p>
<h2>Synopsis</h2>
<p>FvwmIconMan is spawned by fvwm, so no command line invocation will work. </p>
<h2>Description</h2>
<p>FvwmIconMan is an icon manager modeled after the TWM icon manager. The user may have multiple icon managers, each of which armed with a list of window types which it manages. For example, the user may have one manager which lists only emacs windows, and another which lists everything else. You may also specify what resolution each icon manager uses, for example, one icon manager may manage windows on all desks, and another may manage only those on the current desk, page or screen. FvwmIconMan can display the miniature icons provided by fvwm for its managed windows. The managers may have a maximum number of columns (and so grows vertically), a maximum number of rows (and then grows horizontally), or stay at a fixed size, and adjust the size of the window buttons to fit (think win95&#8217;s Taskbar). And when support is compiled in for the X Shape extension, then the manager windows may be shaped. </p>
<p> You can specify actions to be run when mouse, or key events are received. For example, you could bind the first mouse button to iconify the selected window, and make bindings for the arrow keys to navigate the manager window without the mouse. </p>
<p> FvwmIconMan can be set to display which window currently has the keyboard focus, and by binding the select event (see below) to the fvwm Focus function, you can emulate the TWM icon manager&#8217;s behavior. </p>
<h2>Initialization</h2>
<p>During initialization, FvwmIconMan searches though the fvwm configuration file for the options which are described below. It is highly recommended that you make FvwmIconMan be a sticky window. And if you want to make use of the followfocus option, and/or binding an action to Focus, then you should make FvwmIconMan clicktofocus. Also, when using the Shape option, it&#8217;s recommended that the FvwmIconMan window not be decorated at all by fvwm. </p>
<h2>Invocation</h2>
<p>FvwmIconMan can be invoked by inserting the line &#8216;Module FvwmIconMan&#8217; in the .fvwm2rc file. If FvwmIconMan is to be spawned during fvwm&#8217;s initialization, then this line should be placed in the StartFunction declarations, or it can be bound to a menu, mouse button, or keystroke to invoke it later. </p>
<p> If you wish to run FvwmIconMan in a transient mode, such as with the built in window list, then pass &quot;-Transient&quot; as an argument. The invocation &quot;Module FvwmIconMan -Transient&quot; will do nicely. In this mode, FvwmIconMan will pop up one manager window directly under the cursor. When the mouse button is released, it will execute the appropriate action, and then exit. Things are somewhat complicated by the fact that you can specify that FvwmIconMan creates multiple manager windows, behavior which is unsuitable when running transiently. So, when running transiently, FvwmIconMan will only create one manager window. Use the manager id &#8216;transient&#8217; to specify options for this manager window. </p>
<p> FvwmIconMan may accept an alias name as an argument. For example, &quot;Module FvwmIconMan FvwmIconMan-Variant2&quot;. </p>
<h2>Configuration Options Reference Chart</h2>
<p>FvwmIconMan has acquired quite a few options. I assume others share my dislike of paging though a long man page, so here is a terse reference chart describing the available options. They are described in more detail in the next section. </p>
<pre>Name Description Default
NumManagers number of managers 1
Action binds command to event Mouse 0 N sendcommand Iconify
Background default background gray
ButtonGeometry size of button in pixels
Colorset default colorset
DontShow list of windows to ignore
DrawIcons use mini icons false
FocusAndSelectButton flat grey black
FocusAndSelectColorset
FocusButton style for focused buttons up grey black
FocusColorset
FollowFocus show which win has focus false
Font 8x13
Foreground default text color white
Format describes button label &quot;%c: %i&quot;
IconName manager icon name FvwmIconMan
IconAndSelectButton up black grey
IconAndSelectColorset
IconButton style for icon buttons up black grey
IconColorset
ManagerGeometry size of manager in buttons 0x1
MaxButtonWidth max width of a button
MaxButtonWidthByColumns
NoIconAction animate iconification NOP
PlainButton style for normal buttons up black grey
PlainColorset
ReliefThickness size of button relief 2
Resolution global/desk/page/screen page
Reverse normal, icon or none none
SelectButton style for selected buttons flat black grey
SelectColorset
Shape use shape extension false
Show list of windows to show
ShowOnlyIcons only icons visible false
ShowNoIcons icons are not displayed false
ShowTransient transient windows visible false
ShowOnlyFocused only focused visible false
Sort keep managers sorted name
SortWeight weight for sorting
Tips Tool Tips mode none
TipsDelays Tool Tips mapping delays 1000 300
TipsFont Font for Tool Tips default fvwm font
TipsColorset Tool Tips Colorset 0
TipsFormat describes Tips label the Format value
TipsBorderWidth Tool Tips border size 1
TipsPlacement Tips placement vs button updown
TipsJustification Tips Just vs button leftup
TipsOffsets Tips placement Offsets 3 2
Title manager title FvwmIconMan
TitleButton style for title button raisededge black grey
TitleColorset
UseWinList honor WinListSkip? true</pre>
<h2>Configuration Options</h2>
<p>With the exception of the nummanagers option, all of the options may be defined on a per-manager basis. So, for example, the user may have his emacs manager with a red foreground, and his xterm manager with a blue one. A configuration line may therefore have one of two forms: </p>
<dl>
<dt>*FvwmIconMan: OptionName OptionValue</p>
<dd>To specify that the <i>OptionName</i> takes the value <i>OptionValue</i> for all managers.</p>
<dt>*FvwmIconMan: ManagerId OptionName OptionValue</p>
<dd>To specify that the option <i>OptionName</i> takes the value <i>OptionValue</i> for manager <i>ManagerId</i>. <i>ManagerId</i> may either be a positive integer, or the string &quot;transient&quot;. An integer id refers to managers which FvwmIconMan creates when running normally, and an id of &quot;transient&quot; refers to the single manager which FvwmIconMan creates when running transiently. </p>
<p> The old syntax, that uses an asterisk instead of white spaces before <i>ManagerId</i> and <i>OptionName</i>, is supported too, but it is obsolete now. </p>
</dl>
<p> The following options may be specified: </p>
<dl>
<dt>*FvwmIconMan: NumManagers <i>num</i></p>
<dd><i>num</i> is a positive integer specifying the total number of icon managers. Since FvwmIconMan would like to know how many managers there are before handling any manager specific options, this should come first. The default is 1. </p>
<dt>*FvwmIconMan: [id] Action <i>type</i> <i>binding</i></p>
<dd>Binds an FvwmIconMan command to an event. <i>Type</i> may be one of the values: Key, Mouse, or Select. Actions are described in the following section ACTIONS. </p>
<dt>*FvwmIconMan: [id] Background <i>background</i></p>
<dd>Specifies the default background color. </p>
<dt>*FvwmIconMan: [id] ButtonGeometry <i>geometry</i></p>
<dd>Specifies the initial geometry of an individual button in pixels. If the specified height is 0, then the button height is determined from the font size. X and Y coordinates are ignored. </p>
<dt>*FvwmIconMan: [id] Colorset <i>colorset</i></p>
<dd>The default colorset used. Overrides background and foreground. See FvwmTheme. </p>
<dt>*FvwmIconMan: [id] DrawIcons <i>value</i></p>
<dd>If your version of fvwm is capable of using mini icons, then this option determines if FvwmIconMan displays the mini icons. Otherwise, it generates an error message. &quot;true&quot; means that mini icons are shown for iconified windows, &quot;false&quot; that mini icons are never shown, and &quot;always&quot; that mini icons are shown for all windows. </p>
<dt>*FvwmIconMan: [id] FocusAndSelectButton <i>style</i> [<i>forecolor</i> <i>backcolor</i>]</p>
<dd>Same as the plainbutton option, but specifies the look of buttons which are both selected, and have the keyboard focus. </p>
<dt>*FvwmIconMan: [id] FocusAndSelectColorset <i>colorset</i></p>
<dd>Works like focusandselectbutton but uses colorsets instead. The style setting can still only be applied with focusandselectbutton. See FvwmTheme. </p>
<dt>*FvwmIconMan: [id] FocusButton <i>style</i> [<i>forecolor</i> <i>backcolor</i>]</p>
<dd>Same as the plainbutton option, but specifies the look of buttons whose windows have the keyboard focus. </p>
<dt>*FvwmIconMan: [id] FocusColorset <i>colorset</i></p>
<dd>Works like focusbutton but uses colorsets instead. The style setting can still only be applied with focusbutton. See FvwmTheme. </p>
<dt>*FvwmIconMan: [id] FollowFocus <i>boolean</i></p>
<dd>If <i>true</i>, then the button appearance reflects which window currently has focus. Default is false. </p>
<dt>*FvwmIconMan: [id] Font <i>font</i></p>
<dd>Specifies the font to be used for labeling the buttons. The default is 8&#215;13. </p>
<dt>*FvwmIconMan: [id] Foreground <i>foreground</i></p>
<dd>Specifies the default foreground color. </p>
<dt>*FvwmIconMan: [id] Format <i>formatstring</i></p>
<dd>A printf like format string which describes the string to be printed in the manager window for each managed window. Possible flags are: %t, %i, %c, and %r for the window&#8217;s title, icon title, class, or resource name, respectively. The default is &quot;%c: %i&quot;. <code>Warning</code>: m4 reserves the word <i>format</i>, so if you use m4, take appropriate action. </p>
<dt>*FvwmIconMan: [id] IconName <i>iconstring</i></p>
<dd>Specifies the window icon name for that manager window. <i>Iconstring</i> may either be a single word, or a string enclosed in quotes. The default is &quot;FvwmIconMan&quot;. </p>
<dt>*FvwmIconMan: [id] IconAndSelectButton <i>style</i> [<i>forecolor</i> <i>backcolor</i>]</p>
<dd>Same as the plainbutton option, but specifies the look of buttons whose windows are iconified and the button is selected. </p>
<dt>*FvwmIconMan: [id] IconButton <i>style</i> [<i>forecolor</i> <i>backcolor</i>]</p>
<dd>Same as the plainbutton option, but specifies the look of buttons whose windows are iconified. </p>
<dt>*FvwmIconMan: [id] IconAndSelectColorset <i>colorset</i></p>
<dd>Works like IconAndSelectButton but uses colorsets instead. The style setting can still only be applied with iconbutton. See FvwmTheme. </p>
<dt>*FvwmIconMan: [id] IconColorset <i>colorset</i></p>
<dd>Works like iconbutton but uses colorsets instead. The style setting can still only be applied with iconbutton. See FvwmTheme. </p>
<dt>*FvwmIconMan: [id] ManagerGeometry <i>geometry</i></p>
<dd>Specifies the initial geometry of the manager, in units of buttons. If <i>height</i> is 0, then the manager will use <i>width</i> columns, and will grow vertically once it has more than <i>width</i> windows. Likewise, if <i>width</i> is 0, it will use <i>height</i> rows, and grow horizontally. If both are nonzero, then the manager window will be exactly that size, and stay that way. As columns are created, the buttons will narrow to accommodate. If the geometry is specified with a negative y coordinate, then the window manager will grow upwards. Otherwise, it will grow downwards. </p>
<dt>*FvwmIconMan: [id] MaxButtonWidth <i>width</i></p>
<dd>Defines a maximum for the width of a button (in pixels). By default there is no maximum. A value of 0 resets the default. The maximum is only used with a non growing manager (the ManagerGeometry option specifies non zero width and height). </p>
<dt>*FvwmIconMan: [id] MaxButtonWidthByColumns <i>col</i></p>
<dd>This is another way to set the button width. col is the number of columns of icons. The button width is determined by dividing the total width of FvwmIconMan by the number of columns. For example if the width of FvwmIconMan manager is 1024, MaxButtonWidthByColumns is 4 then MaxButtonWidth is 256. This is useful when you do not know, at config time, the width of the manager, for example, for a swallowed FvwmIconMan. </p>
<dt>*FvwmIconMan: [id] NoIconAction <i>action</i></p>
<dd>Tells FvwmIconMan to do <i>action</i> when a NoIcon style window is iconified or de-iconified. Relevant coordinates are appended to <i>action</i> so that the icon can be traced to an FvwmIconMan button. An example action is &quot;*FvwwmIconMan: NoIconAction SendToModule FvwmAnimate animate&quot;. A blank or null action turns this feature off. </p>
<dt>*FvwmIconMan: [id] PlainButton <i>style</i> [<i>forecolor</i> <i>backcolor</i>]</p>
<dd>Specifies how normal buttons look. <i>style</i> may be one of <i>flat</i>, <i>up</i>, <i>down</i>, <i>raisededge</i>, or <i>sunkedge</i>, and describes how the button is drawn. The color options are both optional, and if not set, then the default colors are used. If on a monochrome screen, then the <i>style</i> option is ignored, but must still be set. </p>
<dt>*FvwmIconMan: [id] PlainColorset <i>colorset</i></p>
<dd>Works like plainbutton but uses colorsets instead. The style setting can still only be applied with plainbutton. See FvwmTheme. </p>
<dt>*FvwmIconMan: [id] ReliefThickness <i>num</i></p>
<dd><i>num</i> is an integer specifying the number of pixels thick that the relief at the edge of non-flat buttons should be. Setting this to 0 will produce flat buttons, as if the values for <i>FocusAndSelectButton</i>, <i>FocusButton</i>, <i>IconAndSelectButton</i>, <i>IconButton</i>, <i>PlainButton</i>, <i>SelectButton</i>, and <i>TitleButton</i> were all set to <i>flat</i>. If <i>num</i> is negative, the button will be inverted as if you had used <i>Reverse</i> for all classes. </p>
<dt>*FvwmIconMan: [id] Resolution <i>resolution</i></p>
<dd>Specifies when the manager will display an entry for a certain window. <i>resolution</i> may take one of the following values: global, desk, page, screen, !desk, !page, or !screen. If global, then all windows of the appropriate type (see the show and dontshow options below) will be shown. If desk, then only those windows on the current desk are shown. If page, then only those windows on the current page are shown. If screen, then only those windows on the current Xinerama screen are shown. !desk reverses the sense of desk, displaying only those windows not on the current desk. Likewise, !page shows only those windows not on the current page and !screen shows only those windows not on the current Xinerama screen. The default is page. If Xinerama is not active or only a single screen is used, page and screen are equivalent. </p>
<p> This configuration line is respected when FvwmIconMan is running as well, the resolution is changed dynamically. </p>
<dt>*FvwmIconMan: [id] Reverse <i>class</i></p>
<dd>Causes certain classes of buttons to have their relief lines reversed so that up and down styles are reversed. This has no affect on flat buttons. The class can be icon, normal or none. The default is none. </p>
<dt>*FvwmIconMan: [id] SelectButton <i>style</i> [<i>forecolor</i> <i>backcolor</i>]</p>
<dd>Same as the plainbutton option, but specifies the look of buttons when the mouse is over them. </p>
<dt>*FvwmIconMan: [id] SelectColorset <i>colorset</i></p>
<dd>Works like selectbutton but uses colorsets instead. The style setting can still only be applied with selectbutton. See FvwmTheme. </p>
<dt>*FvwmIconMan: [id] Shape <i>boolean</i></p>
<dd>If <i>True</i>, then use make the window shaped. Probably only useful if you have multiple columns or rows. If FvwmIconMan wasn&#8217;t compiled to support the Shape extension, this generates an error message. When using shaped windows, it&#8217;s recommended that a fvwm style is made for FvwmIconMan that has no borders. Otherwise, fvwm will get confused. </p>
<dt>*FvwmIconMan: [id] Sort <i>value</i></p>
<dd>If <i>name</i>, then the manager list is sorted by name. If <i>namewithcase</i>, then it is sorted by name sensitive to case. If <i>id</i>, then the manager list is sorted by the window id, which never changes after the window is created. If <i>weighted</i>, then the manager list is sorted by weight (see the description of <i>sortweight</i> below). Or it can be set to <i>none</i>, which results in no sorting. Default is <i>name</i>. </p>
<dt>*FvwmIconMan: [id] SortWeight <i>weight</i> <i>pattern-list</i></p>
<dd>Assigns the specified <i>weight</i> to windows that match <i>pattern-list</i>. The list is made up of patterns of the form <i>type=pattern</i>, where type is one of <i>class</i>, <i>resource</i>, <i>title</i>, or <i>icon</i>, and pattern is an expression of the same format used in the fvwm style command (minimalistic shell pattern matching). Multiple sort weights can be given. Each window is matched against the list of sort weights, in order, and is given the weight from the first match. Lower-weighted windows are placed first in the manager list. For example: </p>
<pre>*FvwmIconMan: Sort weighted
*FvwmIconMan: SortWeight 1 class=XTerm title=special*
*FvwmIconMan: SortWeight 10 class=XTerm
*FvwmIconMan: SortWeight 5</pre>
<p>In this example, xterm windows whose titles start with &quot;special&quot; (weight 1) are listed first, followed by everything but other xterms (weight 5), and the other xterms (weight 10) are listed last. If no default weight (empty pattern list) is given, the default weight is 0. Only relevant if the sort type is set to <i>weighted</i>. </p>
<dt>*FvwmIconMan: [id] Title <i>title-string</i></p>
<dd>Specifies the window title string for that manager window. <i>Titlestring</i> may either be a single word, or a string enclosed in quotes. The default is &quot;FvwmIconMan&quot;. This will be drawn in the title bar of the manager window, if any, and in the title button, which is the button drawn when the manager is empty. </p>
<dt>*FvwmIconMan: [id] TitleButton <i>style</i> [<i>forecolor</i> <i>backcolor</i>]</p>
<dd>Same as the plainbutton option, but specifies the look of the title button (the button drawn when the manager is empty). The manager&#8217;s title is drawn in the title button. </p>
<dt>*FvwmIconMan: [id] UseWinList <i>boolean</i></p>
<dd>If <i>true</i>, then honor the WinListSkip style flag. Otherwise, all windows are subject to possible management according to the show and dontshow lists. </p>
</dl>
<p> The two following options control which windows get handled by which managers. A manager can get two lists, one of windows to show, and one of windows to ignore. If only the <i>show</i> list is given, then that manager will show only the windows in the list. If only the <i>DontShow</i> list is given, then the manager will show all windows except those in the list. If both lists are given, then a window will be shown if it is not in the <i>DontShow</i> list, and in the <i>Show</i> list. And finally, if neither list is given, then the manager will handle all windows. Each list is made up of patterns of the form <i>type=pattern</i>, where type is one of <i>class</i>, <i>resource</i>, <i>title</i>, or <i>icon</i>, and pattern is an expression of the same format used in the fvwm style command (minimalistic shell pattern matching). Quotes around the pattern will be taken as part of the expression. If a window could be handled by more than one manager, then the manager with the lowest id gets it. </p>
<dl>
<dt>*FvwmIconMan: [id] Show <i>pattern list</i></p>
<dd>If a window matches one of the patterns in the list, then it may be handled by this manager. </p>
<dt>*FvwmIconMan: [id] DontShow <i>pattern list</i></p>
<dd>If a window matches one of the patterns in the list, then it may not be handled by this manager. </p>
<dt>*FvwmIconMan: [id] ShowTransient <i>boolean</i></p>
<dd>Show transient windows in the list (default false). </p>
<dt>*FvwmIconMan: [id] ShowOnlyIcons <i>boolean</i></p>
<dd>Only iconified windows are shown if <i>boolean</i> is true. </p>
<dt>*FvwmIconMan: [id] ShowNoIcons <i>boolean</i></p>
<dd>Only windows that are not iconified are shown if <i>boolean</i> is true. </p>
<dt>*FvwmIconMan: [id] ShowOnlyFocused <i>boolean</i></p>
<dd>Only window with the focus is shown if <i>boolean</i> is true. </p>
</dl>
<p> The following two options control tips. </p>
<dl>
<dt>*FvwmIconMan: [id] Tips <i>value</i></p>
<dd>where <i>value</i> can be always, needed or false. Default is false, no tips are displayed. With always, tips are enabled. With needed, a tip is displayed only if either the button string is truncated or the tip string is not equal to the button string. This configuration line is respected when FvwmIconMan is running as well. </p>
<dt>*FvwmIconMan: [id] TipsDelays <i>delay</i> [<i>mappeddelay</i>]</p>
<dd>where <i>delay</i> and <i>mappeddelay</i> are time out values in milliseconds. If no <i>mappeddelay</i> is given <i>delay</i> is assumed. Default is 1000 300. When the cursor is on a button, FvwmIconMan wait <i>delay</i> milliseconds before displaying the tip. In the case where a tip is already mapped and the cursor goes to another button, FvwmIconMan waits <i>mappeddelay</i> milliseconds before displaying the new tip. </p>
<dt>*FvwmIconMan: [id] TipsFont <i>fontname</i></p>
<dd>Specifies the font to be used for tips. Default is the default fvwm font. </p>
<dt>*FvwmIconMan: [id] TipsColorset <i>colorset</i></p>
<dd>Specifies the colors for tips window. Default is colorset 0. See FvwmTheme. </p>
<dt>*FvwmIconMan: [id] TipsFormat <i>formatstring</i></p>
<dd>Similar to the Format option but for the tips window. The default is the format string from the Format option. </p>
<dt>*FvwmIconMan: [id] TipsBorderWidth <i>pixels</i></p>
<dd>Specifies the border width (in pixels) of the tips window. Default is 1. </p>
<dt>*FvwmIconMan: [id] TipsPlacement <i>value</i></p>
<dd>where <i>value</i> can be up, down, right, left, updown or leftright. This value specifies the position of the tips window relative to its button. Default is updown where buttons on the top half of the screen get tips below the button, otherwise the tips are above the button. </p>
<dt>*FvwmIconMan: [id] TipsJustification <i>value</i></p>
<dd>where <i>value</i> can be leftup, rightdown or center. Specifies the justification (direction) of the tips window relative to its button after the tips window has been placed. Default is leftup which means that if a tip is placed above or below its button, then the left border of the tip and of the button are aligned. If the tip is placed on the left or on the right of its button, leftup aligns the top borders. rightdown and center work like leftup but in different directions. The alignment is adjusted by the TipsOffset option. See next option. </p>
<dt>*FvwmIconMan: [id] TipsOffsets <i>placementoffset</i> <i>justoffset</i></p>
<dd>where <i>placementoffset</i> and <i>justoffset</i> are offsets in pixels for the TipsPlacement and TipsJustification configuration option. Default is 3 2. </p>
</dl>
<h2>Actions</h2>
<p>Actions are commands which may be bound to an event of the type: a key press, a mouse click, or the mouse entering a window manager button &#8211; denoted by the action types <i>Key</i>, <i>Mouse</i>, and <i>Select</i>. </p>
<p> Normally, actions bound to a mouse click are executed when the button is pressed. In transient mode, the action is executed when the button is released, since it is assumed that FvwmIconMan was bound to some mouse event. A tip/warning: FvwmIconMan still keeps track of the mouse button and any modifier keys in this case, so if you bind FvwmIconMan to say, meta-button3, then it would be wise to ensure that the action you want to execute will be executed when the meta-button3 event occurs (which would be the button release, assuming you kept your finger on the meta key). </p>
<p> The syntax for actions are: </p>
<dl>
<dt><code>Key actions</code>: Key <i>Keysym</i> <i>Modifiers</i> <i>FunctionList</i></p>
<dd><i>Keysym</i> and <i>Modifiers</i> are exactly the same as for the fvwm <i>Key</i> command. </p>
<dt><code>Mouse actions</code>: Mouse <i>Button</i> <i>Modifiers</i> <i>FunctionList</i></p>
<dd><i>Button</i> and <i>Modifiers</i> are exactly the same as for the fvwm <i>Mouse</i> command. </p>
<dt><code>Select actions</code>: Select <i>FunctionList</i></p>
<dd></dl>
<p> A <i>FunctionList</i> is a sequence of commands separated by commas. They are executed in left to right order, in one shared context &#8211; which currently only contains a pointer to the &quot;current&quot; button. If a button is selected (typically by the mouse pointer sitting on it) when the action is executed, then the current button is initialized to that button. Otherwise, it points to nothing. </p>
<p> Most of the available commands then modify this &quot;current&quot; button, either by moving it around, making it become the selected button, or sending commands to fvwm acting on the window represented by that button. Note that while this current button is initialized to be the selected button, the selected button does not implicitly follow it around. This way, the user can send commands to various windows, without changing which button is selected. </p>
<p> Commands take five types of arguments: <i>Integer</i>, <i>Manager</i>, <i>Window</i>, <i>Button</i>, and <i>String</i>. A <i>String</i> is a string specified exactly as for fvwm &#8211; either in quotes or as a single word not in quotes. Again, you may bind a sequence of commands to an event, by listing them separated by commas. </p>
<p> <i>Window</i> and <i>Button</i> types look exactly the same in the .fvwm2rc file, but are interpreted as either specifying a managed window, or a FvwmIconMan button representing a window. They can either be an integer (which is interpreted module N where N is the number of buttons &#8211; so 0 is the first and -1 is the last), or one of the strings: <i>Select</i>, <i>Focus</i>, <i>Up</i>, <i>Down</i>, <i>Right</i>, <i>Left</i>, <i>Next</i>, <i>Prev</i>. <i>Select</i> and <i>Focus</i> refer to the currently selected or focused button or window. <i>Up</i>, <i>Down</i>, <i>Right</i>, and <i>Left</i> refer to the button or window above, below, to the right of, or to the left of the current button in the manager window, allowing navigation around the manager window. <i>Next</i> and <i>Prev</i> designates the window, button, or manager after or before the current button, allowing navigation of the one dimensional list of windows which is drawn in the manager window. If the manager is sorted, <i>Next</i> and <i>Prev</i> move through the windows in the sorted order. </p>
<p> The <i>Manager</i> type can either be an integer, <i>Next</i>, or <i>Prev</i>. The meaning is analogous to that of the <i>Button</i> type, but in terms of the integral index of the managers, restricted to managers which are nonempty. </p>
<p> The following functions are currently defined:</p>
<dl>
<dt>bif <i>Button</i> <i>Integer/String</i></p>
<dd>A relative branch instruction. If <i>Button</i> is <i>Select</i> or <i>Focus</i>, then take the branch if there is a selected button or a focused button. If <i>Button</i> is an integer, then branch if nonzero. If it is one of <i>Up</i>, <i>Down</i>, <i>Right</i>, <i>Left</i>, <i>Next</i>, <i>Prev</i>, then the branch is taken when the current button can move in that direction. If the branch is taken, then <i>Integer</i> commands are skipped. No backwards branches are allowed. </p>
<dt>bifn <i>Button</i> <i>Integer/String</i></p>
<dd>The complement of bif. The branch is taken if <i>Button</i> evaluates to false, by the criteria listed for bif. </p>
<dt>gotobutton <i>Button</i></p>
<dd>Sets current button to <i>Button</i>. If <i>Button</i> is an integer, then the current button is set to <i>Button</i> modulo the number of buttons, in the whichever manager contains the selected button, if any. </p>
<dt>gotomanager <i>Manager</i></p>
<dd>Sets button to button 0 of <i>Manager</i>. This will only go to a visible, nonempty manager. So an integral argument is taken modulo the number of such managers. </p>
<dt>jmp <i>Integer/String</i></p>
<dd>Executes a relative jump of <i>Integer</i> instructions. Backwards jumps are not allowed. The jump is computed relative to the instruction following the jmp. </p>
<dt>label <i>String</i></p>
<dd>Provides a label that previous instructions can jump to. It will not be visible to subsequent jump instructions, and the same label can be used multiple times in the same instruction list (though it would be perverse to do so.) </p>
<dt>print <i>String</i></p>
<dd>Prints <i>String</i> to the console. Useful for debugging actions. </p>
<dt>printdebug</p>
<dd>Prints defined actions to the console. Should only be used by developers. To enable this command, set CONFIG and FUNCTIONS variables to &#8216;1&#8217; in the modules/FvwmIconMan/debug.h and recompile this module. </p>
<dt>quit</p>
<dd>Quits FvwmIconMan. </p>
<dt>refresh</p>
<dd>Causes all manager windows to redraw themselves. </p>
<dt>ret</p>
<dd>Stop executing the entire action. </p>
<dt>searchback <i>String</i></p>
<dd>Sets button to button before the current one whose printed string in the manager window matches specified <i>String</i>, which may contain wildcards. </p>
<dt>searchforward <i>String</i></p>
<dd>Sets button to button after the current one whose printed string in the manager window matches specified <i>String</i>, which may contain wildcards. </p>
<dt>select</p>
<dd>Selects the current button, if any. If a select action has been specified, it will then be run. Therefore, it is considered unwise to set the select button in the select action. </p>
<dt>sendcommand <i>Command</i></p>
<dd>Sends the fvwm command <i>Command</i> to the window represented by the current button, if any. </p>
<dt>warp</p>
<dd>Warps cursor to current button, if any. </p>
</dl>
<p> <code>Examples:</code> </p>
<pre>gotobutton select, gotobutton Down, select</pre>
<p>Selects the button below the currently selected button. Since the current button is already initialized to the selected button, this may be shortened to &quot;gotobutton Down, select&quot;. </p>
<pre>gotobutton Up, select</pre>
<p>Selects the button above the currently selected button. </p>
<pre>gotobutton 0, select</pre>
<p>Selects the first button of the current manager. If there is no current manager, which is the case when no button is selected, then this does nothing. </p>
<pre>gotobutton -1, select</pre>
<p>Selects the last button of the current manager. </p>
<pre>gotobutton focus, select</pre>
<p>Selects the button corresponding to the focused window. </p>
<pre>gotobutton focus, Iconify</pre>
<p>Sends the fvwm command Iconify to the focused window. Note that this does not change the selected button. </p>
<pre>bif Next 3, gotobutton 0, select, ret, gotobutton Next, select</pre>
<p>If a button is selected, and it&#8217;s the last button, go to button 0. If it&#8217;s not the last button, go to the next button. Otherwise, do nothing. Basically, this action cycles through all buttons in the current manager. </p>
<pre>bif select 7, bif focus 3, gotomanager 0, select, ret, gotobutton focus, \
 select, ret, gotobutton down, select</pre>
<p>This is good for sending to FvwmIconMan with a SendToModule command. If there is a selected button, it moves down. Otherwise, if there is a focused button, it is selected. Otherwise, button 0 of manager 0 gets selected. </p>
<pre>bif select Select, bif focus Focus, gotomanager 0, select, ret, label Focus, \
 gotobutton focus, select, ret, label Select, gotobutton down, select</pre>
<p>Same as previous, but using the label instruction. </p>
<p> In addition to being bound to keys and mice, actions can be sent from fvwm to FvwmIconMan via the SendToModule command. Don&#8217;t quote the command when using SendToModule. Also, due to a bug in the current version of fvwm, don&#8217;t quote FvwmIconMan either. </p>
<h2>Sample Configurations</h2>
<p>This first example is of a the simplest invocation of FvwmIconMan, which only has one manager, and handles all windows: </p>
<pre>##############################################################
# Load any modules which should be started during
# fvwm initialization
ModulePath /usr/lib/X11/fvwm:/usr/bin/X11
Module FvwmIconMan
# Make FvwmIconMan title-bar-less, sticky, and give it an icon
Style &quot;Fvwm*&quot; Icon toolbox.xpm,NoTitle,NoHandles,Sticky
Style &quot;FvwmIconMan&quot; HandleWidth 5, Handles, BorderWidth 5
##############################################################
##############################################################
#Definitions used by the modules
*FvwmIconMan: NumManagers 1
*FvwmIconMan: Resolution global
*FvwmIconMan: Background slategrey
*FvwmIconMan: Foreground white
*FvwmIconMan: Font 7x13
*FvwmIconMan: ButtonGeometry 100x0
*FvwmIconMan: ManagerGeometry 1x0-0+0</pre>
<p>This example is the Reader&#8217;s Digest version of my personal configuration. It has two managers, one for emacs and one for everything else, minus things with no icon title. Only windows on the current page are displayed. The use of the <i>drawicons</i> and <i>shape</i> options requires that fvwm and FvwmIconMan are compiled with the correct options. Note how the geometry and show options are specified per manager, and the others are common to all: </p>
<pre>Style &quot;FvwmIconMan&quot; NoTitle, Sticky, WindowListSkip, BorderWidth 0
Style &quot;FvwmIconMan&quot; HandleWidth 0
Key F8 A N SendToModule FvwmIconMan bif select Select, bif focus Focus, \
 gotomanager 0, select, sendcommand WarpToWindow, ret, label Focus, \
 gotobutton focus, select, sendcommand WarpToWindow, ret, label Select, \
 gotobutton prev, select, sendcommand WarpToWindow
Key F9 A N SendToModule FvwmIconMan bif select Select, bif focus Focus, \
 gotomanager 0, select, sendcommand WarpToWindow, ret, label Focus, \
 gotobutton focus, select, sendcommand WarpToWindow, ret, label Select, \
 gotobutton next, select, sendcommand WarpToWindow
*FvwmIconMan: NumManagers 2
*FvwmIconMan: Resolution page
*FvwmIconMan: Background steelblue
*FvwmIconMan: Foreground white
*FvwmIconMan: Font 7x13
*FvwmIconMan: UseWinList true
*FvwmIconMan: DrawIcons true
*FvwmIconMan: Shape true
*FvwmIconMan: FollowFocus true
*FvwmIconMan: Sort name
*FvwmIconMan: PlainButton up white steelblue
*FvwmIconMan: SelectButton down white steelblue
*FvwmIconMan: FocusButton up white brown
*FvwmIconMan: FocusAndSelectButton down white brown
*FvwmIconMan: TitleButton raisededge white steelblue
*FvwmIconMan: NoIconAction &quot;SendToModule FvwmAnimate animate&quot;
*FvwmIconMan: 1 Title &quot;Emacs windows&quot;
*FvwmIconMan: 1 IconName &quot;FvwmIconMan: Emacs&quot;
*FvwmIconMan: 1 Format &quot;%i&quot;
*FvwmIconMan: 1 Show resource=emacs resource=gemacs
*FvwmIconMan: 1 ManagerGeometry 1x0-400+0
*FvwmIconMan: 1 ButtonGeometry 200x0
*FvwmIconMan: 2 Title &quot;All windows&quot;
*FvwmIconMan: 2 IconName &quot;FvwmIconMan: all&quot;
*FvwmIconMan: 2 Format &quot;%c: %i&quot;
*FvwmIconMan: 2 DontShow icon=Untitled
*FvwmIconMan: 2 ManagerGeometry 2x4-0+0
*FvwmIconMan: 2 ButtonGeometry 200x0
*FvwmIconMan: transient Geometry 194x100
*FvwmIconMan: transient DontShow icon=Untitled
*FvwmIconMan: transient Action Mouse 0 A sendcommand select select Iconify
*FvwmIconMan: Action Mouse 1 N sendcommand Iconify
*FvwmIconMan: Action Mouse 2 N sendcommand WarpToWindow
*FvwmIconMan: Action Mouse 3 N sendcommand &quot;Module FvwmIdent FvwmIdent&quot;
*FvwmIconMan: Action Key Left N gotobutton Left, select
*FvwmIconMan: Action Key Right N gotobutton Right, select
*FvwmIconMan: Action Key Up N gotobutton Up, select
*FvwmIconMan: Action Key Down N gotobutton Down, select
*FvwmIconMan: Action Key q N quit</pre>
<h2>Unfinished Business</h2>
<p>There is one bug that I know of. A honest to goodness solution to this would be appreciated. When an icon manager is set to grow upwards or leftwards, on some machines it may wander occasionally. </p>
<p> It doesn&#8217;t handle windows without resource names as gracefully as it should. </p>
<h2>Author</h2>
<p>Brady Montz (bradym [at] cs.arizona.edu). </p>
<h2>Thanks</h2>
<pre>Thanks to:
 David Berson &lt;berson [at] cs.pitt.edu&gt;,
 Gren Klanderman &lt;greg [at] alphatech.com&gt;,
 David Goldberg &lt;dsg [at] mitre.org&gt;,
 Pete Forman &lt;gsez020 [at] compo.bedford.waii.com&gt;,
 Neil Moore &lt;amethyst [at] maxwell.ml.org&gt;,
 Josh M. Osborne &lt;stripes [at] va.pubnix.com,
 Adam Rice &lt;wysiwyg [at] glympton.airtime.co.uk&gt;,
 Chris Siebenmann &lt;cks [at] hawkwind.utcs.toronto.edu&gt;,
 Bjorn Victor &lt;victor [at] delial.docs.uu.se&gt;.
for contributing either code or truly keen ideas.</pre>
