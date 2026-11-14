---
title: "fvwmpager(1)"
name: "fvwmpager"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmpager/"
description: "FvwmPager – the Fvwm Pager module"
---

<p>FvwmPager &#8211; the Fvwm Pager module </p>
<h2>Synopsis</h2>
<p><code>FvwmPager</code> [ <i>-transient</i> ] [ <i>name</i> ] [ <i>first desk</i> [ <i>last desk</i> ] ] FvwmPager is spawned by fvwm, so no command line invocation will work. </p>
<p> All desks with desk numbers between <i>first desk</i> and <i>last desk</i> are displayed. If <i>last desk</i> is omitted only the <i>first desk</i> is shown. If both desk numbers are omitted, the current desk is used instead. If you use an asterisk &#8216;*&#8217; in place of <i>first desk</i> the pager will always show the current desktop, even when you switch desks. </p>
<p> Example lines to put in your .fvwm2rc: </p>
<pre>Module FvwmPager 0 3</pre>
<p>or </p>
<pre>Module FvwmPager *</pre>
<p>or from within an fvwm pop-up menu: </p>
<pre>AddToMenu Module-Popup Modules Title
+ Audio Module FvwmAudio
+ Auto Module FvwmAuto 200
+ Buttons Module FvwmButtons
+ Console Module FvwmConsole
+ Ident Module FvwmIdent
+ Banner Module FvwmBanner
+ Pager Module FvwmPager 0 3</pre>
<p>or </p>
<pre>+ Pager Module FvwmPager *</pre>
<p>If the pager is started with the <i>-transient</i> option, the next time a button is released the pager is closed. Note that this option does only work if the window style of the pager window is &#8216;sticky&#8217; (see the fvwm man page). You should use the &#8216;StaysOnTop&#8217; style too. </p>
<p> Example: </p>
<pre>Style FvwmPager Sticky, StaysOnTop
*FvwmPager: Rows 1
*FvwmPager: Columns 1
Mouse 3 R C Module FvwmPager -transient</pre>
<p>With this in your .fvwm2rc, if you press control and button 3 in the root window the pager pops up under the mouse and while the viewport moves with the mouse. </p>
<h2>Description</h2>
<p>The FvwmPager module shows a miniature view of the Fvwm desktops which are specified in the command line. This is a useful reminder of where your active windows are. Windows in the pager are shown in the same color as their fvwm decorations. </p>
<p> The pager can be used to change your viewport into the current desktop, to change desktops, or to move windows around. </p>
<p> Pressing mouse button 1 in the pager will cause you viewport to change to the selected page of the selected desk. If you click with button 1 in the desk-label area, you will switch desks but not pages within the desk. </p>
<p> Dragging mouse button 2 on a miniature view of a window will cause that window to be move to the location where you release the mouse button, but your viewport will not change. If you drag the window out of the pager and onto your desktop, a full size image of the window will appear for you to place. There is no way to pick up a full size image of the window and move it into the pager, however. Since some mice do not have button 2, I have made provisions to drag windows in the pager by using pressing modifier-1 (usually Alt) and dragging with button 3. </p>
<p> Clicking mouse button 3 on a location will cause the viewport to move to the selected location and switch desks if necessary, but will not align the viewport to a page boundary. Dragging button 3 will cause the viewport to move as you drag but not switch desktops, even if the pointer moves to another desktop. </p>
<p> With the <i>*FvwmPager: SloppyFocus</i> option the focus is transferred to the window pointed at with the mouse when the pointer is inside the pager. </p>
<p> When iconified, the pager will work as a fully functional current desk only pager. Windows and viewports can be moved within the icon of the pager. Users will want to make sure that they have no lines similar to </p>
<pre>Icon &quot;Fvwm Pager&quot; whatever</pre>
<p>in their .fvwm2rc files. </p>
<h2>Copyrights</h2>
<p>The FvwmPager program, and the concept for interfacing this module to the Window Manager, are all original work by Robert Nation. </p>
<p> Copyright 1994, Robert Nation. No guarantees or warranties or anything are provided or implied in any way whatsoever. Use this program at your own risk. Permission to use this program for any purpose is given, as long as the copyright is kept intact. </p>
<h2>Initialization</h2>
<p>During initialization, <i>FvwmPager</i> gets config info from <code>fvwm</code>&#8216;s module configuration database (see <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1), section <code>MODULE COMMANDS</code>). </p>
<p> To use FvwmPager with several different configurations, you can invoke FvwmPager with an optional parameter, which it will use as its <i>name</i> instead (e.g &quot;Module FvwmPager OtherPager&quot;). OtherPager will then read only the lines in the configuration file starting with &quot;*OtherPager&quot;, and not the lines belonging to FvwmPager. This way multiple pager instances may be used. </p>
<p> Note: the old way to use the FvwmPager with several different configurations is to link the executable to another name, i.e. </p>
<pre>ln -s FvwmPager OtherPager</pre>
<p>This may work, but this method is not supported. </p>
<h2>Keyboard Focus Control</h2>
<p>You can direct the keyboard focus to any window on the current desktop by clicking with button 2 on its image in the pager. The window does not need to be visible, but it does need to be on the current page. </p>
<h2>Invocation</h2>
<p>The invocation method was shown in the synopsis section </p>
<h2>Configuration Options</h2>
<dl>
<dt>*FvwmPager: Geometry <i>geometry</i></p>
<dd>Completely or partially specifies the pager windows location and geometry, in standard X11 notation. In order to maintain an undistorted aspect ratio, you might want to leave out either the width or height dimension of the geometry specification. </p>
<dt>*FvwmPager: Rows <i>rows</i></p>
<dd>Tells fvwm how many rows of desks to use when laying out the pager window. </p>
<dt>*FvwmPager: Columns <i>columns</i></p>
<dd>Tells fvwm how many columns of desks to use when laying out the pager window. </p>
<dt>*FvwmPager: IconGeometry <i>geometry</i></p>
<dd>Specifies a size (optional) and location (optional) for the pager&#8217;s icon window. Since there is no easy way for FvwmPager to determine the height of the icon&#8217;s label, you will have to make an allowance for the icon label height when using negative y-coordinates in the icon location specification (used to specify a location relative to the bottom instead of the top of the screen). </p>
<dt>*FvwmPager: StartIconic</p>
<dd>Causes the pager to start iconified. </p>
<dt>*FvwmPager: NoStartIconic</p>
<dd>Causes the pager to start normally. Useful for canceling the effect of the <i>StartIconic</i> option. </p>
<dt>*FvwmPager: LabelsBelow</p>
<dd>Causes the pager to draw desk labels below the corresponding desk. </p>
<dt>*FvwmPager: LabelsAbove</p>
<dd>Causes the pager to draw desk labels above the corresponding desk. Useful for canceling the effect of the <i>LabelsBelow</i> option. </p>
<dt>*FvwmPager: ShapeLabels</p>
<dd>Causes the pager to hide the labels of all but the current desk. This turns off label hilighting. </p>
<dt>*FvwmPager: NoShapeLabels</p>
<dd>Causes the pager to show the labels of all visible desks. Useful for canceling the effect of the <i>ShapeLabels</i> option. </p>
<dt>*FvwmPager: Font <i>font-name</i></p>
<dd>Specified a font to use to label the desktops. If <i>font_name</i> is &quot;none&quot; then no desktop labels will be displayed. </p>
<dt>*FvwmPager: SmallFont <i>font-name</i></p>
<dd>Specified a font to use to label the window names in the pager. If not specified, the window labels will be omitted. Window labels seem to be fairly useless for desktop scales of 32 or greater. If <i>font_name</i> is &quot;none&quot; then no window names will be displayed. </p>
<dt>*FvwmPager: Fore <i>color</i></p>
<dd>Specifies the color to use to write the desktop labels, and to draw the page-grid lines. </p>
<dt>*FvwmPager: Back <i>color</i></p>
<dd>Specifies the background color for the window. </p>
<dt>*FvwmPager: Hilight <i>color</i></p>
<dd>The active page and desk label will be highlighted by using this background pattern instead of the normal background. </p>
<dt>*FvwmPager: HilightPixmap <i>pixmap</i></p>
<dd>The active page will be highlighted by using this background pattern instead of the normal background. </p>
<dt>*FvwmPager: DeskHilight</p>
<dd>Hilight the active page with the current hilight color/pixmap. Useful for canceling the effect of the <i>NoDeskHilight</i> option. </p>
<dt>*FvwmPager: NoDeskHilight</p>
<dd>Don&#8217;t hilight the active page. </p>
<dt>*FvwmPager: WindowColors <i>fore back hiFore hiBack</i></p>
<dd>Change the normal/highlight colors of the windows. <i>fore</i> and <i>hiFore</i> specify the colors as used for the font inside the windows. <i>back</i> and <i>hiBack</i> are used to fill the windows with. </p>
<dt>*FvwmPager: WindowLabelFormat <i>format</i></p>
<dd>This specifies a printf() like format for the labels in the mini window. Possible flags are: %t, %i, %c, and %r for the window&#8217;s title, icon title, class, or resource name, respectively. The default is &quot;%i&quot;. </p>
<dt>*FvwmPager: Label <i>desk label</i></p>
<dd>Assigns the text <i>label</i> to desk <i>desk</i> (or the current desk if desk is &quot;*&quot;) in the pager window. Useful for assigning symbolic names to desktops, i.e. </p>
<pre>*FvwmPager: Label 1 Mail
*FvwmPager: Label 2 Maker
*FvwmPager: Label * Matlab</pre>
<p><code>Note</code>: There is currently a much better way to specify desk names globally (and not just in FvwmPager) using <code>DesktopName</code> command, so you should not use this option anymore. </p>
<dt>*FvwmPager: DeskColor <i>desk color</i></p>
<dd>Assigns the color <i>color</i> to desk <i>desk</i> (or the current desk if desk is &quot;*&quot;) in the pager window. This replaces the background color for the particular <i>desk</i>. This only works when the pager is full sized. When Iconified, the pager uses the color specified by *FvwmPager: Back. </p>
<p> <code>TIP:</code> Try using *FvwmPager: DeskColor in conjunction with FvwmCpp (or FvwmM4) and FvwmBacker to assign identical colors to your various desktops and the pager representations. </p>
<dt>*FvwmPager: Pixmap <i>pixmap</i></p>
<dd>Use <i>pixmap</i> as background for the pager. </p>
<dt>*FvwmPager: DeskPixmap <i>desk pixmap</i></p>
<dd>Assigns the pixmap <i>color</i> to desk <i>desk</i> (or the current desk if desk is &quot;*&quot;) in the pager window. This replaces the background pixmap for the particular <i>desk</i>. </p>
<p> <code>TIP:</code> Try using *FvwmPager: DeskPixmap in conjunction with FvwmCpp (or FvwmM4) and FvwmBacker to assign identical pixmaps to your various desktops and the pager representations. </p>
<dt>*FvwmPager: DeskTopScale <i>number</i></p>
<dd>If the geometry is not specified, then a desktop reduction factor is used to calculate the pager&#8217;s size. Things in the pager window are shown at 1/<i>number</i> of the actual size. </p>
<dt>*FvwmPager: MiniIcons</p>
<dd>Allow the pager to display a window&#8217;s mini icon in the pager, if it has one, instead of showing the window&#8217;s name. </p>
<dt>*FvwmPager: MoveThreshold <i>pixels</i></p>
<dd>Defines the distance the pointer has to be moved before a window being dragged with button 2 is actually moved. The default value is three pixels. If the pointer moved less that this amount the window snaps back to its original position when the button is released. If <i>pixels</i> is less than zero the default value is used. The value set with the <i>MoveThreshold</i> command in fvwm is inherited by FvwmPager but can be overridden with this option. </p>
<dt>*FvwmPager: SloppyFocus</p>
<dd>If the SloppyFocus option is used, you do not need to click into the mini window in the pager to give the real window the focus. Simply putting the pointer over the window inside the pager is enough. </p>
<p> Note: This option interferes slightly with the MouseFocus and SloppyFocus styles of fvwm. Sometimes, if you click into the pager window to change pages or desks and then move the pointer<tt>&nbsp;<wbr></tt>to<br />
 a place on the screen where a window of the new page will appear, this new window does not get the input focus. This may happen if you drag the pointer over one of the mini windows in the pager. There is nothing that can be done about this &#8211; except not using SloppyFocus in the pager. </p>
<dt>*FvwmPager: SolidSeparators</p>
<dd>By default the pages of the virtual desktop are separated by dashed lines in the pager window. This option causes FvwmPager to use solid lines instead. </p>
<dt>*FvwmPager: NoSeparators</p>
<dd>Turns off the lines separating the pages of the virtual desktop. </p>
<dt>*FvwmPager: Balloons [<i>type</i>]</p>
<dd>Show a balloon describing the window when the pointer is moved into a window in the pager. The default format (the window&#8217;s icon name) can be changed using BalloonStringFormat. If <i>type</i> is <i>Pager</i> balloons are just shown for an un-iconified pager; if <i>type</i> is <i>Icon</i> balloons are just shown for an iconified pager. If <i>type</i> is anything else (or null) balloons are always shown. </p>
<dt>*FvwmPager: BalloonFore <i>color</i></p>
<dd>Specifies the color for text in the balloon window. If omitted it defaults to the foreground color for the window being described. </p>
<dt>*FvwmPager: BalloonBack <i>color</i></p>
<dd>Specifies the background color for the balloon window. If omitted it defaults to the background color for the window being described. </p>
<dt>*FvwmPager: BalloonFont <i>font-name</i></p>
<dd>Specifies a font to use for the balloon text. Defaults to <i>fixed</i>. </p>
<dt>*FvwmPager: BalloonBorderWidth <i>number</i></p>
<dd>Sets the width of the balloon window&#8217;s border. Defaults to 1. </p>
<dt>*FvwmPager: BalloonBorderColor <i>color</i></p>
<dd>Sets the color of the balloon window&#8217;s border. Defaults to black. </p>
<dt>*FvwmPager: BalloonYOffset <i>number</i></p>
<dd>The balloon window is positioned to be horizontally centered against the pager window it is describing. The vertical position may be set as an offset. Negative offsets of <i>-n</i> are placed <i>n</i> pixels above the pager window, positive offsets of <i>+n</i> are placed <i>n</i> pixels below. Offsets of -1 and 1 represent the balloon window close to the original window without a gap. Offsets of 0 are not permitted, as this would permit direct transit from pager window to balloon window, causing an event loop. Defaults to +3. The offset will change sign automatically, as needed, to keep the balloon on the screen. </p>
<dt>*FvwmPager: BalloonStringFormat format</p>
<dd>The same as <i>*FvwmPager: WindowLabelFormat</i>, it just specifies the string to display in the balloons. The default is &quot;%i&quot;. </p>
<dt>*FvwmPager: Colorset <i>desk colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for <i>desk</i>. If you use an asterisk &#8216;*&#8217; in place of <i>desk</i>, the colorset is used on all desks. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>*FvwmPager: BalloonColorset <i>desk colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for balloons on <i>desk</i>. If you use an asterisk &#8216;*&#8217; in place of <i>desk</i>, the colorset is used on all desks. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>*FvwmPager: HilightColorset <i>desk colorset</i></p>
<dd>Tells the module to use colorset <i>colorset</i> for hilighting on <i>desk</i>. If you use an asterisk &#8216;*&#8217; in place of <i>desk</i>, the colorset is used on all desks. Please refer to the man page of the FvwmTheme module for details about colorsets. </p>
<dt>*FvwmPager: WindowColorsets <i>colorset activecolorset</i></p>
<dd>Uses colorsets in the same way as *FvwmPager: WindowColors. Please refer to the man page of the FvwmTheme module for details about colorsets. The shadow and hilight colors of the colorset are only used for the window borders if the *FvwmPager: Window3DBorders is specified too. </p>
<dt>*FvwmPager: WindowBorderWidth <i>n</i></p>
<dd>Specifies the width of the border drawn around the mini windows. This also sets the minimum size of the mini windows to (2 * <i>n</i> + 1). The default is 1. </p>
<dt>*FvwmPager: Window3DBorders</p>
<dd>Specifies that the mini windows should have a 3d borders based on the mini window background. This option only works if *FvwmPager: WindowColorsets is specified. </p>
<dt>*FvwmPager: UseSkipList</p>
<dd>Tells FvwmPager to not show the windows that are using the WindowListSkip style. </p>
</dl>
<h2>Author</h2>
<p>Robert Nation<br />
 DeskColor patch contributed by Alan Wild<br />
 MiniIcons &amp; WindowColors patch contributed by Rob Whapham<br />
 Balloons patch by Ric Lister &lt;ric [at] giccs.georgetown.edu&gt;<br />
 fvwm-workers: Dominik, Olivier, Hippo and others.</p>
