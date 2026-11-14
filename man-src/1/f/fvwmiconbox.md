---
title: "fvwmiconbox(1)"
name: "fvwmiconbox"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmiconbox/"
description: "FvwmIconBox – the fvwm icon box module"
---

<p>FvwmIconBox &#8211; the fvwm icon box module </p>
<h2>Synopsis</h2>
<p><code>FvwmIconBox</code> [<i>name</i>] </p>
<p> FvwmIconBox is spawned by fvwm, so no command line invocation will work. </p>
<h2>Description</h2>
<p>The FvwmIconBox module provides an icon manager. The user can do operations, like iconify and de-iconify, for each icon shown in the module via mouse and keyboard. </p>
<h2>Copyrights</h2>
<p>The FvwmIconBox program is original work of Nobutaka Suzuki. </p>
<p> Copyright 1994, Nobutaka Suzuki. No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmIconBox</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>). </p>
<p> If the FvwmIconBox executable is linked to another name, i.e. ln -s FvwmIconBox MoreIconBox, then another module called MoreIconBox can be started, with a completely different configuration than FvwmIconBox, simply by changing the keyword FvwmIconBox to MoreIconBox. This way multiple clutter-reduction programs can be used. </p>
<h2>Invocation</h2>
<p>FvwmIconBox can be invoked by binding the action &#8216;Module FvwmIconBox&#8217; to a menu or key-stroke in the .fvwm2rc file. Fvwm will search directory specified in the ModulePath configuration option to attempt to locate FvwmIconBox. </p>
<h2>Configuration Options</h2>
<p>FvwmIconBox shows icons only if NoIcon is applied. Note that the NoIcon attribute should be set after the Icon attribute specification. Otherwise the icon-box module might become nothing but an empty-box module. The module reads the same .fvwm2rc file as fvwm reads when it starts up, and looks for lines as listed below: </p>
<dl>
<dt>*FvwmIconBox: Fore <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of white for the window foreground. This option affects only the foreground color of background_bitmap specified in *FvwmIconBox: Pixmap option described below. </p>
<dt>*FvwmIconBox: Colorset <i>colorset</i></p>
<dd>Tells the module to use colorset (See FvwmTheme) in place of Fore and Back. </p>
<dt>*FvwmIconBox: IconColorset <i>colorset</i></p>
<dd>Tells the module to use colorset (See FvwmTheme) in place of IconFore and IconBack. </p>
<dt>*FvwmIconBox: IconHiColorset <i>colorset</i></p>
<dd>Tells the module to use colorset (See FvwmTheme) in place of IconHiFore and IconHiBack. </p>
<dt>*FvwmIconBox: Back <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of black for the window background. </p>
<dt>*FvwmIconBox: IconFore <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of black for non-selected icon text. </p>
<dt>*FvwmIconBox: IconBack <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of white for the non-selected icon background. </p>
<dt>*FvwmIconBox: IconHiFore <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of black for selected icon text. </p>
<dt>*FvwmIconBox: IconHiBack <i>color</i></p>
<dd>Tells the module to use <i>color</i> instead of white for the selected icon background. </p>
<dt>*FvwmIconBox: Pixmap <i>pixmap</i></p>
<dd>Tells the module to use <i>pixmap</i> for the window background_pixmap. </p>
<dt>*FvwmIconBox: Font <i>fontname</i></p>
<dd>Tells the module to use <i>fontname</i> instead of fixed for text. </p>
<dt>*FvwmIconBox: SortIcons <i>option</i></p>
<dd>Tells the module to sort all icons in the icon box in alphabetical order. <i>option</i> can be <i>WindowName</i>, <i>IconName</i>, <i>ResClass</i>, and <i>ResName</i>. For example, specifying <i>ResClass</i> means that icons are sorted by using their resource-class strings. If <i>option</i> is <i>ResClass</i> or <i>ResName</i>, an icon having no XA_WM_CLASS property is considered to be the &quot;smallest&quot; element. </p>
<dt>*FvwmIconBox: Padding <i>number</i></p>
<dd>Specifies the number of pixels between icons. The default value is 5. </p>
<dt>*FvwmIconBox: SBWidth <i>number</i></p>
<dd>Specifies the width of horizontal and vertical scrollbars. The default value is 9. </p>
<dt>*FvwmIconBox: Placement <i>primary</i> <i>secondary</i></p>
<dd>Specifies icon placement policy. <i>primary</i> and <i>secondary</i> can be <i>Top</i>, <i>Bottom</i>, <i>Left</i> and <i>Right</i>. The following eight combinations are available: </p>
<pre><i>primary</i> <i>secondary</i>
 Left Top
 Left Bottom
 Right Top
 Right Bottom
 Top Left
 Top Right
 Bottom Left
 Bottom Right</pre>
<p><i>Top</i>: Icons are placed from top to bottom. </p>
<p> <i>Bottom</i>: Icons are placed from bottom to top. </p>
<p> <i>Left</i>: Icons are placed from left to right. </p>
<p> <i>Right</i>: Icons are placed from right to left. </p>
<p> For example, when the placement is &quot;Left Top&quot;, icons are placed from left to right, and new rows are added from top to bottom. The default vale is &quot;Left Bottom&quot;. </p>
<dt>*FvwmIconBox: UseSkipList</p>
<dd>Tells FvwmIconBox to not show the windows that are listed on a WindowListSkip line in the configuration file. </p>
<dt>*FvwmIconBox: Lines</p>
<dd>Specifies the number of icons placed in a line. If <i>primary</i> is Left or Right, this value specifies the number of columns. If <i>primary</i> is Top or Bottom, this value specifies the number of rows. For example, seven icons are placed in a row if *FvwmIconBox: Lines is 7 and *FvwmIconBox: Placement is &quot;Left Top&quot;. The default value is 6. </p>
<dt>*FvwmIconBox: HideSC <i>direction</i></p>
<dd>Specifies the un-displayed scroll bar . <i>Direction</i> can be either <i>Horizontal</i> or <i>Vertical</i>. </p>
<dt>*FvwmIconBox: Geometry <i>&lt;width&gt;x&lt;height&gt;{+-}&lt;X&gt;{+-}&lt;Y&gt;</i></p>
<dd>Specifies the location and/or size of FvwmIconBox. <i>width</i> and <i>height</i> are measured in icons, not pixels. The default value is 6&#215;1+0+0. </p>
<dt>*FvwmIconBox: MaxIconSize <i>&lt;width&gt;x&lt;height&gt;</i></p>
<dd>Specifies the maximum size of icon bitmap. A bitmap larger than this size is clipped to this size. The default value is 48&#215;48. In particular, if the height is 0, then icon bitmaps are not displayed and only icon labels are drawn. </p>
<dt>*FvwmIconBox: Mouse <i>Button</i> <i>Action</i> <i>Response[, Response]</i></p>
<dd>Tells the module to do <i>Response</i> when <i>Action</i> is done on button <i>Button</i>. Available <i>Response</i>s are built-in commands in Fvwm (e.g. Iconify, Delete, Focus) and available <i>Action</i>s are Click and DoubleClick. </p>
<dt>*FvwmIconBox: Key <i>Key</i> <i>Response[, Response]</i></p>
<dd>Tells the module to do <i>Response</i> when <i>Key</i> is pressed. Available <i>Response</i>s are, besides Fvwm built-in commands, the following six FvwmIconBox built-in commands: <i>Next</i>, <i>Prev</i>, <i>Left</i>, <i>Right</i>, <i>Up</i>, and <i>Down</i>. </p>
<p> <i>Next</i>: Change the hilighted icon to the next. </p>
<p> <i>Prev</i>: Change the hilighted icon to the previous. </p>
<p> <i>Left</i>: Move the slider of the horizontal scrollbar to left. Icons move to right accordingly. </p>
<p> <i>Right</i>: Move the slider of the horizontal scrollbar to right. Icons move to left accordingly. </p>
<p> <i>Up</i>: Move the slider of the vertical scrollbar to up. Icons move to down accordingly. </p>
<p> <i>Down</i>: Move the slider of the vertical scrollbar to down. Icons move to up accordingly. </p>
<dt>*FvwmIconBox: <i>windowname</i> <i>bitmap-file</i></p>
<dd>Specifies the bitmap to be displayed in the icon box for <i>windowname</i>. This option &quot;overrides&quot; bitmap files specified in Style command. <i>Windowname</i> can be window name, class name, or resource name. <i>Windowname</i> can contain &quot;*&quot; and &quot;?&quot; like Fvwm configuration file. The <i>bitmap-file</i> is either the full path name to a bitmap file, or a file in the ImagePath. If <i>bitmap-file</i> is specified to be &quot;-&quot;, the icon for a window corresponding to <i>windowname</i> is not shown in the icon box. </p>
<dt>*FvwmIconBox: SetWMIconSize</p>
<dd>Tells the module to set XA_WM_ICON_SIZE property of the root window at the size which the module want icon windows to have. If you show icon windows on not the root window but the module, it would be better to specify this option. </p>
<dt>*FvwmIconBox: HilightFocusWin</p>
<dd>Tells the module to hilight the icon of the window which has the keyboard focus. The fore/back colors of the hilighted icon are those specified in the *FvwmIconBox: IconHiFore and *FvwmIconBox: IconHiBack commands, respectively. </p>
<dt>*FvwmIconBox: Resolution <i>resolution</i></p>
<dd>If <i>resolution</i> is Desk, then the module shows only the icons on the current desk. Currently, Desk is the only value <i>resolution</i> can take :) </p>
<dt>*FvwmIconBox: FrameWidth <i>width1</i> <i>width2</i></p>
<dd>Specifies the frame-width of the module. <i>Width1</i> corresponds to the width from the outer-border to the scroll-bar, and, <i>width2</i> corresponds to the width from the scroll-bar to the internal-window displaying icons. The default values are 8 and 6, respectively. </p>
<dt>*FvwmIconBox: NoIconAction <i>action</i></p>
<dd>Tells FvwmIconBox to do <i>action</i> is when a NoIcon style window is iconified or de-iconified. Relevant coordinates are appended to <i>action</i> so that the icon can be traced to an FvwmIconBox button. An example action is &quot;*FvwmIconBox: NoIconAction SendToModule FvwmAnimate animate&quot;. A blank or null action turns this feature off. </p>
<dt>*FvwmIconBox: NoIconifiedParentheses</p>
<dd>Tells FvwmIconBox to not enclose the title of an iconified window within parantheses. </p>
<dt>*FvwmIconBox: NormalTitleRelief <i>num</i></p>
<dd>Sets the width in pixels of the relief that is put around icon titles for windows that are not iconified. The default if this option is not specified is 2 pixels. </p>
<dt>*FvwmIconBox: IconifiedTitleRelief <i>num</i></p>
<dd>Sets the width in pixels of the relief that is put around icon titles for windows that are iconified. The default if this option is not specified is 2 pixels. </p>
<dt>*FvwmIconBox: NormalTitleInvertedRelief</p>
<dd>This option makes the relief around titles of uniconified windows to appear pressed in. The default is a relief that makes the label look raised from the background (unless a relief width of 0 pixels is specified, see above). </p>
<dt>*FvwmIconBox: IconifiedTitleInvertedRelief</p>
<dd>This option makes the relief around titles of iconified windows to appear pressed in. </p>
</dl>
<h2>Sample Configuration</h2>
<p>The following are excepts from a .fvwm2rc file which describe FvwmIconBox initialization commands: </p>
<pre>############################################################
# Note that icons are shown in the module
# only if NoIcon attribute is applied.
Style &quot;*&quot; NoIcon
############################################################
*FvwmIconBox: IconBack #cfcfcf
*FvwmIconBox: IconHiFore black
*FvwmIconBox: IconHiBack LightSkyBlue
*FvwmIconBox: Back #5f9ea0
#*FvwmIconBox: Fore blue
*FvwmIconBox: Geometry 5x1+0+0
*FvwmIconBox: MaxIconSize 64x38
*FvwmIconBox: Font -adobe-helvetica-medium-r-*-*-12-*-*-*-*-*-*-*
*FvwmIconBox: SortIcons IconName
#*FvwmIconBox: SortIcons ResClass
*FvwmIconBox: Padding 4
*FvwmIconBox: FrameWidth 9 7
*FvwmIconBox: Lines 10
*FvwmIconBox: SBWidth 11
*FvwmIconBox: Placement Left Top
*FvwmIconBox: Pixmap fvwm.xpm
#*FvwmIconBox: HideSC Horizontal
*FvwmIconBox: SetWMIconSize
*FvwmIconBox: HilightFocusWin
#*FvwmIconBox: Resolution Desk
*FvwmIconBox: NoIconAction SendToModule FvwmAnimate animate
#
# mouse bindings
#
*FvwmIconBox: Mouse 1 Click RaiseLower
*FvwmIconBox: Mouse 1 DoubleClick Iconify
*FvwmIconBox: Mouse 2 Click Iconify -1, Focus
*FvwmIconBox: Mouse 3 Click Module FvwmIdent
#
# Key bindings
#
*FvwmIconBox: Key r RaiseLower
*FvwmIconBox: Key space Iconify
*FvwmIconBox: Key d Close
#
# FvwmIconBox built-in functions
#
*FvwmIconBox: Key n Next
*FvwmIconBox: Key p Prev
*FvwmIconBox: Key h Left
*FvwmIconBox: Key j Down
*FvwmIconBox: Key k Up
*FvwmIconBox: Key l Right
#
# Icon file specifications
#
# Mostly, you don't have to specify icon files, as FvwmIconBox now
# reads icon files specified in Style commands.
#
*FvwmIconBox: &quot;Fvwm*&quot; -</pre>
<h2>Author</h2>
<p>Nobutaka Suzuki (nobuta-s [at] is.aist-nara.ac.jp).</p>
