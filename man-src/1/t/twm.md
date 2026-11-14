---
title: "twm(1)"
name: "twm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-twm/"
description: "twm – Tab Window Manager for the X Window System"
---

<h2>NAME</h2>
<p> twm &#8211; Tab Window Manager for the X Window System</p>
<h2>SYNTAX</h2>
<p> <code>twm </code>[ <code>-display</code> <i>dpy</i> ] [ <code>-s</code> ] [ <code>-f</code> <i>initfile</i> ] [ <code>-v</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Twm</i> is a window manager for the X Window System. It provides titlebars, shaped windows, several forms of icon management, user-defined macro functions, click-to-type and pointer-driven keyboard focus, and user-specified key and pointer button bindings. </p>
<p> This program is usually started by the user&#8217;s session manager or startup script. When used from <i><a href="/docs/linux/man/1-xdm/">xdm</a>(1)</i> or <i><a href="/docs/linux/man/1-xinit/">xinit</a>(1)</i> without a session manager, <i>twm</i> is frequently executed in the foreground as the last client. When run this way, exiting <i>twm</i> causes the session to be terminated (i.e., logged out). </p>
<p> By default, application windows are surrounded by a &#8220;frame&#8221; with a titlebar at the top and a special border around the window. The titlebar contains the window&#8217;s name, a rectangle that is lit when the window is receiving keyboard input, and function boxes known as &#8220;titlebuttons&#8221; at the left and right edges of the titlebar. </p>
<p> Pressing pointer Button1 (usually the left-most button unless it has been changed with <i>xmodmap</i>) on a titlebutton will invoke the function associated with the button. In the default interface, windows are iconified by clicking (pressing and then immediately releasing) the left titlebutton (which looks like a Dot). Conversely, windows are deiconified by clicking in the associated icon or entry in the icon manager (see description of the variable <code>ShowIconManager</code> and of the function <code>f.showiconmgr</code>). </p>
<p> Windows are resized by pressing the right titlebutton (which resembles a group of nested squares), dragging the pointer over edge that is to be moved, and releasing the pointer when the outline of the window is the desired size. Similarly, windows are moved by pressing in the title or highlight region, dragging a window outline to the new location, and then releasing when the outline is in the desired position. Just clicking in the title or highlight region raises the window without moving it. </p>
<p> When new windows are created, <i>twm</i> will honor any size and location information requested by the user (usually through <i>-geometry</i> command line argument or resources for the individual applications). Otherwise, an outline of the window&#8217;s default size, its titlebar, and lines dividing the window into a 3&#215;3 grid that track the pointer are displayed. Clicking pointer Button1 will position the window at the current position and give it the default size. Pressing pointer Button2 (usually the middle pointer button) and dragging the outline will give the window its current position but allow the sides to be resized as described above. Clicking pointer Button3 (usually the right pointer button) will give the window its current position but attempt to make it long enough to touch the bottom the screen.</p>
<h2>OPTIONS</h2>
<p> <i>Twm</i> accepts the following command line options: </p>
<dl>
<dt><code>-display </code><i>dpy</i></p>
<dd> This option specifies the X server to use.</p>
<dt><code>-s</code></p>
<dd> This option indicates that only the default screen (as specified by <code>-display</code> or by the <code>DISPLAY</code> environment variable) should be managed. By default, <i>twm</i> will attempt to manage all screens on the display.</p>
<dt><code>-f </code><i>filename</i></p>
<dd> This option specifies the name of the startup file to use. By default, <i>twm</i> will look in the user&#8217;s home directory for files named <i>.twmrc.num</i> (where <i>num</i> is a screen number) or <i>.twmrc</i>.</p>
<dt><code>-v</code></p>
<dd> This option indicates that <i>twm</i> should print error messages whenever an unexpected X Error event is received. This can be useful when debugging applications but can be distracting in regular use.</dl>
<h2>CUSTOMIZATION</h2>
<p> Much of <i>twm</i>&#8216;s appearance and behavior can be controlled by providing a startup file in one of the following locations (searched in order for each screen being managed when <i>twm</i> begins):</p>
<dl>
<dt><code>$HOME/.twmrc.</code><i>screennumber</i></p>
<dd> The <i>screennumber</i> is a small positive number (e.g. 0, 1, etc.) representing the screen number (e.g. the last number in the DISPLAY environment variable <i>host:displaynum.screennum</i>) that would be used to contact that screen of the display. This is intended for displays with multiple screens of differing visual types.</p>
<dt><code>$HOME/.twmrc</code></p>
<dd> This is the usual name for an individual user&#8217;s startup file.</p>
<dt><code>/usr/lib/X11/twm/system.twmrc</code></p>
<dd> If neither of the preceding files are found, <i>twm</i> will look in this file for a default configuration. This is often tailored by the site administrator to provide convenient menus or familiar bindings for novice users.</dl>
<p> If no startup files are found, <i>twm</i> will use the built-in defaults described above. The only resource used by <i>twm</i> is <i>bitmapFilePath</i> for a colon-separated list of directories to search when looking for bitmap files (for more information, see the <i>Athena Widgets</i> manual and <i><a href="/docs/linux/man/1-xrdb/">xrdb</a>(1)</i>). </p>
<p> <i>Twm</i> startup files are logically broken up into three types of specifications: <i>Variables</i>, <i>Bindings</i>, <i>Menus</i>. The <i>Variables</i> section must come first and is used to describe the fonts, colors, cursors, border widths, icon and window placement, highlighting, autoraising, layout of titles, warping, use of the icon manager. The <i>Bindings</i> section usually comes second and is used to specify the functions that should be to be invoked when keyboard and pointer buttons are pressed in windows, icons, titles, and frames. The <i>Menus</i> section gives any user-defined menus (containing functions to be invoked or commands to be executed). </p>
<p> Variable names and keywords are case-insensitive. Strings must be surrounded by double quote characters (e.g. &quot;blue&quot;) and are case-sensitive. A pound sign (#) outside of a string causes the remainder of the line in which the character appears to be treated as a comment.</p>
<h2>VARIABLES</h2>
<p> Many of the aspects of <i>twm</i>&#8216;s user interface are controlled by variables that may be set in the user&#8217;s startup file. Some of the options are enabled or disabled simply by the presence of a particular keyword. Other options require keywords, numbers, strings, or lists of all of these. </p>
<p> Lists are surrounded by braces and are usually separated by whitespace or a newline. For example: </p>
<pre>
<code>AutoRaise</code> { &quot;emacs&quot; &quot;XTerm&quot; &quot;Xmh&quot; }
</pre>
<p> or </p>
<pre>
<code>AutoRaise</code>
{
   &quot;emacs&quot;
   &quot;XTerm&quot;
   &quot;Xmh&quot;
}
</pre>
<p> When a variable containing a list of strings representing windows is searched (e.g. to determine whether or not to enable autoraise as shown above), a string must be an exact, case-sensitive match to the window&#8217;s name (given by the WM_NAME window property), resource name or class name (both given by the WM_CLASS window property). The preceding example would enable autoraise on windows named &#8220;emacs&#8221; as well as any <i>xterm</i> (since they are of class &#8220;XTerm&#8221;) or xmh windows (which are of class &#8220;Xmh&#8221;). </p>
<p> String arguments that are interpreted as filenames (see the <code>Pixmaps</code>, <code>Cursors</code>, and <code>IconDirectory</code> below) will prepend the user&#8217;s directory (specified by the <code>HOME</code> environment variable) if the first character is a tilde (~). If, instead, the first character is a colon (:), the name is assumed to refer to one of the internal bitmaps that are used to create the default titlebars symbols: <code>:xlogo</code> or <code>:delete</code> (both refer to the X logo), <code>:dot</code> or <code>:iconify</code> (both refer to the dot), <code>:resize</code> (the nested squares used by the resize button), <code>:menu</code> (a page with lines), and <code>:question</code> (the question mark used for non-existent bitmap files). </p>
<p> The following variables may be specified at the top of a <i>twm</i> startup file. Lists of Window name prefix strings are indicated by <i>win-list</i>. Optional arguments are shown in square brackets:</p>
<dl>
<dt><code>AutoRaise</code> { <i>win-list</i> }</p>
<dd> This variable specifies a list of windows that should automatically be raised whenever the pointer enters the window. This action can be interactively enabled or disabled on individual windows using the function <code>f.autoraise</code>.</p>
<dt><code>AutoRelativeResize</code></p>
<dd> This variable indicates that dragging out a window size (either when initially sizing the window with pointer Button2 or when resizing it) should not wait until the pointer has crossed the window edges. Instead, moving the pointer automatically causes the nearest edge or edges to move by the same amount. This allows the resizing of windows that extend off the edge of the screen. If the pointer is in the center of the window, or if the resize is begun by pressing a titlebutton, <i>twm</i> will still wait for the pointer to cross a window edge (to prevent accidents). This option is particularly useful for people who like the press-drag-release method of sweeping out window sizes.</p>
<dt><code>BorderColor</code> <i>string</i> [{ <i>wincolorlist</i> }]</p>
<dd> This variable specifies the default color of the border to be placed around all non-iconified windows, and may only be given within a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>wincolorlist</i> specifies a list of window and color name pairs for specifying particular border colors for different types of windows. For example: </p>
<pre>
<code>BorderColor</code> &quot;gray50&quot;
{
   &quot;XTerm&quot;  &quot;red&quot;
   &quot;xmh&quot; &quot;green&quot;
}
</pre>
<p> The default is &quot;black&quot;.</p>
<dt><code>BorderTileBackground</code> <i>string</i> [{ <i>wincolorlist</i> }]</p>
<dd> This variable specifies the default background color in the gray pattern used in unhighlighted borders (only if <code>NoHighlight</code> hasn&#8217;t been set), and may only be given within a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>wincolorlist</i> allows per-window colors to be specified. The default is &quot;white&quot;.</p>
<dt><code>BorderTileForeground</code> <i>string</i> [{ <i>wincolorlist</i> }]</p>
<dd> This variable specifies the default foreground color in the gray pattern used in unhighlighted borders (only if <code>NoHighlight</code> hasn&#8217;t been set), and may only be given within a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>wincolorlist</i> allows per-window colors to be specified. The default is &quot;black&quot;.</p>
<dt><code>BorderWidth</code> <i>pixels</i></p>
<dd> This variable specifies the width in pixels of the border surrounding all client window frames if <code>ClientBorderWidth</code> has not been specified. This value is also used to set the border size of windows created by <i>twm</i> (such as the icon manager). The default is 2.</p>
<dt><code>ButtonIndent</code> <i>pixels</i></p>
<dd> This variable specifies the amount by which titlebuttons should be indented on all sides. Positive values cause the buttons to be smaller than the window text and highlight area so that they stand out. Setting this and the <code>TitleButtonBorderWidth</code> variables to 0 makes titlebuttons be as tall and wide as possible. The default is 1.</p>
<dt><code>ClientBorderWidth</code></p>
<dd> This variable indicates that border width of a window&#8217;s frame should be set to the initial border width of the window, rather than to the value of <code>BorderWidth</code>.</p>
<dt><code>Color</code> { <i>colors-list</i> }</p>
<dd> This variable specifies a list of color assignments to be made if the default display is capable of displaying more than simple black and white. The <i>colors-list</i> is made up of the following color variables and their values: <code>DefaultBackground</code>, <code>DefaultForeground</code>, <code>MenuBackground</code>, <code>MenuForeground</code>, <code>MenuTitleBackground</code>, <code>MenuTitleForeground</code>, <code>MenuShadowColor</code>, <code>MenuBorderColor</code>, <code>PointerForeground</code>, and <code>PointerBackground</code>. The following color variables may also be given a list of window and color name pairs to allow per-window colors to be specified (see <code>BorderColor</code> for details): <code>BorderColor</code>, <code>IconManagerHighlight</code>, <code>BorderTitleBackground</code>, <code>BorderTitleForeground</code>, <code>TitleBackground</code>, <code>TitleForeground</code>, <code>IconBackground</code>, <code>IconForeground</code>, <code>IconBorderColor</code>, <code>IconManagerBackground</code>, and <code>IconManagerForeground</code>. For example: </p>
<pre><code>
Color
{
    MenuBackground "gray50" MenuForeground "blue" BorderColor "red" {"XTerm"
                                                                     "yellow"} TitleForeground "yellow" TitleBackground "blue"
}
</code></pre>
<p> All of these color variables may also be specified for the <code>Monochrome</code> variable, allowing the same initialization file to be used on both color and monochrome displays.</p>
<dt><code>ConstrainedMoveTime</code> <i>milliseconds</i></p>
<dd> This variable specifies the length of time between button clicks needed to begin a constrained move operation. Double clicking within this amount of time when invoking <code>f.move</code> will cause the window to be moved only in a horizontal or vertical direction. Setting this value to 0 will disable constrained moves. The default is 400 milliseconds.</p>
<dt><code>Cursors</code> { <i>cursor-list</i> }</p>
<dd> This variable specifies the glyphs that <i>twm</i> should use for various pointer cursors. Each cursor may be defined either from the <code>cursor</code> font or from two bitmap files. Shapes from the <code>cursor</code> font may be specified directly as: </p>
<pre>
   <i>cursorname</i>  &quot;<i>string</i>&quot;
</pre>
<p> where <i>cursorname</i> is one of the cursor names listed below, and <i>string</i> is the name of a glyph as found in the file <i>/usr/include/X11/cursorfont.h</i> (without the &#8220;XC_&#8221; prefix). If the cursor is to be defined from bitmap files, the following syntax is used instead: </p>
<pre>
   <i>cursorname</i>  &quot;<i>image</i>&quot;&quot;<i>mask</i>&quot;
</pre>
<p> The <i>image</i> and <i>mask</i> strings specify the names of files containing the glyph image and mask in <i><a href="/docs/linux/man/1-bitmap/">bitmap</a>(1)</i> form. The bitmap files are located in the same manner as icon bitmap files. The following example shows the default cursor definitions: </p>
<pre>
<code>Cursors</code>
{
   Frame    &quot;top_left_arrow&quot;
   Title    &quot;top_left_arrow&quot;
   Icon     &quot;top_left_arrow&quot;
   IconMgr  &quot;top_left_arrow&quot;
   Move     &quot;fleur&quot;
   Resize      &quot;fleur&quot;
   Menu     &quot;sb_left_arrow&quot;
   Button      &quot;hand2&quot;
   Wait     &quot;watch&quot;
   Select      &quot;dot&quot;
   Destroy  &quot;pirate&quot;
}
</pre>
<dt><code>DecorateTransients</code></p>
<dd> This variable indicates that transient windows (those containing a WM_TRANSIENT_FOR property) should have titlebars. By default, transients are not reparented.</p>
<dt><code>DefaultBackground</code> <i>string</i></p>
<dd> This variable specifies the background color to be used for sizing and information windows. The default is &quot;white&quot;.</p>
<dt><code>DefaultForeground</code> <i>string</i></p>
<dd> This variable specifies the foreground color to be used for sizing and information windows. The default is &quot;black&quot;.</p>
<dt><code>DontIconifyByUnmapping</code> { <i>win-list</i> }</p>
<dd> This variable specifies a list of windows that should not be iconified by simply unmapping the window (as would be the case if <code>IconifyByUnmapping</code> had been set). This is frequently used to force some windows to be treated as icons while other windows are handled by the icon manager.</p>
<dt><code>DontMoveOff</code></p>
<dd> This variable indicates that windows should not be allowed to be moved off the screen. It can be overridden by the <code>f.forcemove</code> function.</p>
<dt><code>DontSqueezeTitle</code> [{ <i>win-list</i> }]</p>
<dd> This variable indicates that titlebars should not be squeezed to their minimum size as described under <code>SqueezeTitle</code> below. If the optional window list is supplied, only those windows will be prevented from being squeezed.</p>
<dt><code>ForceIcons</code></p>
<dd> This variable indicates that icon pixmaps specified in the <code>Icons</code> variable should override any client-supplied pixmaps.</p>
<dt><code>FramePadding</code> <i>pixels</i></p>
<dd> This variable specifies the distance between the titlebar decorations (the button and text) and the window frame. The default is 2 pixels.</p>
<dt><code>Grayscale</code> { <i>colors</i> }</p>
<dd> This variable specifies a list of color assignments that should be made if the screen has a GrayScale default visual. See the description of <code>Colors</code>.</p>
<dt><code>IconBackground</code> <i>string</i> [{ <i>win-list</i> }]</p>
<dd> This variable specifies the background color of icons, and may only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>win-list</i> is a list of window names and colors so that per-window colors may be specified. See the <code>BorderColor</code> variable for a complete description of the <i>win-list</i>. The default is &quot;white&quot;.</p>
<dt><code>IconBorderColor</code> <i>string</i> [{ <i>win-list</i> }]</p>
<dd> This variable specifies the color of the border used for icon windows, and may only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>win-list</i> is a list of window names and colors so that per-window colors may be specified. See the <code>BorderColor</code> variable for a complete description of the <i>win-list</i>. The default is &quot;black&quot;.</p>
<dt><code>IconBorderWidth</code> <i>pixels</i></p>
<dd> This variable specifies the width in pixels of the border surrounding icon windows. The default is 2.</p>
<dt><code>IconDirectory</code> <i>string</i></p>
<dd> This variable specifies the directory that should be searched if if a bitmap file cannot be found in any of the directories in the <code>bitmapFilePath</code> resource.</p>
<dt><code>IconFont</code> <i>string</i></p>
<dd> This variable specifies the font to be used to display icon names within icons. The default is &quot;variable&quot;.</p>
<dt><code>IconForeground</code> <i>string</i> [{ <i>win-list</i> }]</p>
<dd> This variable specifies the foreground color to be used when displaying icons, and may only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>win-list</i> is a list of window names and colors so that per-window colors may be specified. See the <code>BorderColor</code> variable for a complete description of the <i>win-list</i>. The default is &quot;black&quot;.</p>
<dt><code>IconifyByUnmapping [{ </code><i>win-list</i> }]</p>
<dd> This variable indicates that windows should be iconified by being unmapped without trying to map any icons. This assumes that the user will remap the window through the icon manager, the <code>f.warpto</code> function, or the <i>TwmWindows</i> menu. If the optional <i>win-list</i> is provided, only those windows will be iconified by simply unmapping. Windows that have both this and the <code>IconManagerDontShow</code> options set may not be accessible if no binding to the <i>TwmWindows</i> menu is set in the user&#8217;s startup file.</p>
<dt><code>IconManagerBackground</code> <i>string</i> [{ <i>win-list</i> }]</p>
<dd> This variable specifies the background color to use for icon manager entries, and may only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>win-list</i> is a list of window names and colors so that per-window colors may be specified. See the <code>BorderColor</code> variable for a complete description of the <i>win-list</i>. The default is &quot;white&quot;.</p>
<dt><code>IconManagerDontShow</code> [{ <i>win-list</i> }]</p>
<dd> This variable indicates that the icon manager should not display any windows. If the optional <i>win-list</i> is given, only those windows will not be displayed. This variable is used to prevent windows that are rarely iconified (such as <i>xclock</i> or <i>xload</i>) from taking up space in the icon manager.</p>
<dt><code>IconManagerFont</code> <i>string</i></p>
<dd> This variable specifies the font to be used when displaying icon manager entries. The default is &quot;variable&quot;.</p>
<dt><code>IconManagerForeground</code> <i>string</i> [{ <i>win-list</i> }]</p>
<dd> This variable specifies the foreground color to be used when displaying icon manager entries, and may only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>win-list</i> is a list of window names and colors so that per-window colors may be specified. See the <code>BorderColor</code> variable for a complete description of the <i>win-list</i>. The default is &quot;black&quot;.</p>
<dt><code>IconManagerGeometry</code> <i>string</i> [ <i>columns</i> ]</p>
<dd> This variable specifies the geometry of the icon manager window. The <i>string</i> argument is standard geometry specification that indicates the initial full size of the icon manager. The icon manager window is then broken into <i>columns</i> pieces and scaled according to the number of entries in the icon manager. Extra entries are wrapped to form additional rows. The default number of columns is 1.</p>
<dt><code>IconManagerHighlight</code> <i>string</i> [{ <i>win-list</i> }]</p>
<dd> This variable specifies the border color to be used when highlighting the icon manager entry that currently has the focus, and can only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>win-list</i> is a list of window names and colors so that per-window colors may be specified. See the <code>BorderColor</code> variable for a complete description of the <i>win-list</i>. The default is &quot;black&quot;.</p>
<dt><code>IconManagers</code> { <i>iconmgr-list</i> }</p>
<dd> This variable specifies a list of icon managers to create. Each item in the <i>iconmgr-list</i> has the following format: </p>
<pre>
   &quot;<i>winname</i>&quot; [&quot;<i>iconname</i>&quot;]&quot;<i>geometry</i>&quot; <i>columns</i>
</pre>
<p> where <i>winname</i> is the name of the windows that should be put into this icon manager, <i>iconname</i> is the name of that icon manager window&#8217;s icon, <i>geometry</i> is a standard geometry specification, and <i>columns</i> is the number of columns in this icon manager as described in <code>IconManagerGeometry</code>. For example: </p>
<pre>
<code>IconManagers</code>
{
   &quot;XTerm&quot;  &quot;=300x5+800+5&quot;5
   &quot;myhost&quot; &quot;=400x5+100+5&quot;2
}
</pre>
<p> Clients whose name or class is &#8220;XTerm&#8221; will have an entry created in the &#8220;XTerm&#8221; icon manager. Clients whose name was &#8220;myhost&#8221; would be put into the &#8220;myhost&#8221; icon manager.</p>
<dt><code>IconManagerShow</code> { <i>win-list</i> }</p>
<dd> This variable specifies a list of windows that should appear in the icon manager. When used in conjunction with the <code>IconManagerDontShow</code> variable, only the windows in this list will be shown in the icon manager.</p>
<dt><code>IconRegion</code> <i>geomstring</i> <i>vgrav hgrav gridwidth gridheight</i></p>
<dd> This variable specifies an area on the root window in which icons are placed if no specific icon location is provided by the client. The <i>geomstring</i> is a quoted string containing a standard geometry specification. If more than one <code>IconRegion</code> lines are given, icons will be put into the succeeding icon regions when the first is full. The <i>vgrav</i> argument should be either <code>North</code> or <code>South</code> and control and is used to control whether icons are first filled in from the top or bottom of the icon region. Similarly, the <i>hgrav</i> argument should be either <code>East</code> or <code>West</code> and is used to control whether icons should be filled in from left from the right. Icons are laid out within the region in a grid with cells <i>gridwidth</i> pixels wide and <i>gridheight</i> pixels high.</p>
<dt><code>Icons</code> { <i>win-list</i> }</p>
<dd> This variable specifies a list of window names and the bitmap filenames that should be used as their icons. For example: </p>
<pre>
<code>Icons</code>
{
   &quot;XTerm&quot;  &quot;xterm.icon&quot;
   &quot;xfd&quot;    &quot;xfd_icon&quot;
}
</pre>
<p> Windows that match &#8220;XTerm&#8221; and would not be iconified by unmapping, and would try to use the icon bitmap in the file &#8220;xterm.icon&#8221;. If <code>ForceIcons</code> is specified, this bitmap will be used even if the client has requested its own icon pixmap.</p>
<dt><code>InterpolateMenuColors</code></p>
<dd> This variable indicates that menu entry colors should be interpolated between entry specified colors. In the example below: </p>
<pre>
<code>Menu</code> &quot;mymenu&quot;
{
   &quot;Title&quot;     (&quot;black&quot;:&quot;red&quot;)f.title
   &quot;entry1&quot;       f.nop
   &quot;entry2&quot;       f.nop
   &quot;entry3&quot; (&quot;white&quot;:&quot;green&quot;)f.nop
   &quot;entry4&quot;       f.nop
   &quot;entry5&quot; (&quot;red&quot;:&quot;white&quot;)f.nop
}
</pre>
<p> the foreground colors for &#8220;entry1&#8221; and &#8220;entry2&#8221; will be interpolated between black and white, and the background colors between red and green. Similarly, the foreground for &#8220;entry4&#8221; will be half-way between white and red, and the background will be half-way between green and white.</p>
<dt><code>MakeTitle</code> { <i>win-list</i> }</p>
<dd> This variable specifies a list of windows on which a titlebar should be placed and is used to request titles on specific windows when <code>NoTitle</code> has been set.</p>
<dt><code>MaxWindowSize</code> <i>string</i></p>
<dd> This variable specifies a geometry in which the width and height give the maximum size for a given window. This is typically used to restrict windows to the size of the screen. The default width is 32767 &#8211; screen width. The default height is 32767 &#8211; screen height.</p>
<dt><code>MenuBackground</code> <i>string</i></p>
<dd> This variable specifies the background color used for menus, and can only be specified inside of a <code>Color</code> or <code>Monochrome</code> list. The default is &quot;white&quot;.</p>
<dt><code>MenuBorderColor</code> <i>string</i></p>
<dd> This variable specifies the color of the menu border and can only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The default is &quot;black&quot;.</p>
<dt><code>MenuBorderWidth</code> <i>pixels</i></p>
<dd> This variable specifies the width in pixels of the border surrounding menu windows. The default is 2.</p>
<dt><code>MenuFont</code> <i>string</i></p>
<dd> This variable specifies the font to use when displaying menus. The default is &quot;variable&quot;.</p>
<dt><code>MenuForeground</code> <i>string</i></p>
<dd> This variable specifies the foreground color used for menus, and can only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The default is &quot;black&quot;.</p>
<dt><code>MenuShadowColor</code> <i>string</i></p>
<dd> This variable specifies the color of the shadow behind pull-down menus and can only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The default is &quot;black&quot;.</p>
<dt><code>MenuTitleBackground</code> <i>string</i></p>
<dd> This variable specifies the background color for <code>f.title</code> entries in menus, and can only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The default is &quot;white&quot;.</p>
<dt><code>MenuTitleForeground</code> <i>string</i></p>
<dd> This variable specifies the foreground color for <code>f.title</code> entries in menus and can only be specified inside of a <code>Color</code> or <code>Monochrome</code> list. The default is &quot;black&quot;.</p>
<dt><code>Monochrome</code> { <i>colors</i> }</p>
<dd> This variable specifies a list of color assignments that should be made if the screen has a depth of 1. See the description of <code>Colors</code>.</p>
<dt><code>MoveDelta</code> <i>pixels</i></p>
<dd> This variable specifies the number of pixels the pointer must move before the <code>f.move</code> function starts working. Also see the <code>f.deltastop</code> function. The default is zero pixels.</p>
<dt><code>NoBackingStore</code></p>
<dd> This variable indicates that <i>twm</i>&#8216;s menus should not request backing store to minimize repainting of menus. This is typically used with servers that can repaint faster than they can handle backing store.</p>
<dt><code>NoCaseSensitive</code></p>
<dd> This variable indicates that case should be ignored when sorting icon names in an icon manager. This option is typically used with applications that capitalize the first letter of their icon name.</p>
<dt><code>NoDefaults</code></p>
<dd> This variable indicates that <i>twm</i> should not supply the default titlebuttons and bindings. This option should only be used if the startup file contains a completely new set of bindings and definitions.</p>
<dt><code>NoGrabServer</code></p>
<dd> This variable indicates that <i>twm</i> should not grab the server when popping up menus and moving opaque windows.</p>
<dt><code>NoHighlight</code> [{ <i>win-list</i> }]</p>
<dd> This variable indicates that borders should not be highlighted to track the location of the pointer. If the optional <i>win-list</i> is given, highlighting will only be disabled for those windows. When the border is highlighted, it will be drawn in the current <code>BorderColor</code>. When the border is not highlighted, it will be stippled with a gray pattern using the current <code>BorderTileForeground</code> and <code>BorderTileBackground</code> colors.</p>
<dt><code>NoIconManagers</code></p>
<dd> This variable indicates that no icon manager should be created.</p>
<dt><code>NoMenuShadows</code></p>
<dd> This variable indicates that menus should not have drop shadows drawn behind them. This is typically used with slower servers since it speeds up menu drawing at the expense of making the menu slightly harder to read.</p>
<dt><code>NoRaiseOnDeiconify</code></p>
<dd> This variable indicates that windows that are deiconified should not be raised.</p>
<dt><code>NoRaiseOnMove</code></p>
<dd> This variable indicates that windows should not be raised when moved. This is typically used to allow windows to slide underneath each other.</p>
<dt><code>NoRaiseOnResize</code></p>
<dd> This variable indicates that windows should not be raised when resized. This is typically used to allow windows to be resized underneath each other.</p>
<dt><code>NoRaiseOnWarp</code></p>
<dd> This variable indicates that windows should not be raised when the pointer is warped into them with the <code>f.warpto</code> function. If this option is set, warping to an occluded window may result in the pointer ending up in the occluding window instead the desired window (which causes unexpected behavior with <code>f.warpring</code>).</p>
<dt><code>NoSaveUnders</code></p>
<dd> This variable indicates that menus should not request save-unders to minimize window repainting following menu selection. It is typically used with displays that can repaint faster than they can handle save-unders.</p>
<dt><code>NoStackMode</code> [{ <i>win-list</i> }]</p>
<dd> This variable indicates that client window requests to change stacking order should be ignored. If the optional <i>win-list</i> is given, only requests on those windows will be ignored. This is typically used to prevent applications from relentlessly popping themselves to the front of the window stack.</p>
<dt><code>NoTitle</code> [{ <i>win-list</i> }]</p>
<dd> This variable indicates that windows should not have titlebars. If the optional <i>win-list</i> is given, only those windows will not have titlebars. <code>MakeTitle</code> may be used with this option to force titlebars to be put on specific windows.</p>
<dt><code>NoTitleFocus</code></p>
<dd> This variable indicates that <i>twm</i> should not set keyboard input focus to each window as it is entered. Normally, <i>twm</i> sets the focus so that focus and key events from the titlebar and icon managers are delivered to the application. If the pointer is moved quickly and <i>twm</i> is slow to respond, input can be directed to the old window instead of the new. This option is typically used to prevent this &#8220;input lag&#8221; and to work around bugs in older applications that have problems with focus events.</p>
<dt><code>NoTitleHighlight</code> [{ <i>win-list</i> }]</p>
<dd> This variable indicates that the highlight area of the titlebar, which is used to indicate the window that currently has the input focus, should not be displayed. If the optional <i>win-list</i> is given, only those windows will not have highlight areas. This and the <code>SqueezeTitle</code> options can be set to substantially reduce the amount of screen space required by titlebars.</p>
<dt><code>OpaqueMove</code></p>
<dd> This variable indicates that the <code>f.move</code> function should actually move the window instead of just an outline so that the user can immediately see what the window will look like in the new position. This option is typically used on fast displays (particularly if <code>NoGrabServer</code> is set).</p>
<dt><code>Pixmaps</code> { <i>pixmaps</i> }</p>
<dd> This variable specifies a list of pixmaps that define the appearance of various images. Each entry is a keyword indicating the pixmap to set, followed by a string giving the name of the bitmap file. The following pixmaps may be specified: </p>
<pre>
<code>Pixmaps</code>
{
   TitleHighlight &quot;gray1&quot;
}
</pre>
<p> The default for <i>TitleHighlight</i> is to use an even stipple pattern.</p>
<dt><code>Priority</code> <i>priority</i></p>
<dd> This variable sets <i>twm</i>&#8216;s priority. <i>priority</i> should be an unquoted, signed number (e.g. 999). This variable has an effect only if the server supports the SYNC extension.</p>
<dt><code>RandomPlacement</code></p>
<dd> This variable indicates that windows with no specified geometry should be placed in a pseudo-random location instead of having the user drag out an outline.</p>
<dt><code>ResizeFont</code> <i>string</i></p>
<dd> This variable specifies the font to be used for in the dimensions window when resizing windows. The default is &quot;fixed&quot;.</p>
<dt><code>RestartPreviousState</code></p>
<dd> This variable indicates that <i>twm</i> should attempt to use the WM_STATE property on client windows to tell which windows should be iconified and which should be left visible. This is typically used to try to regenerate the state that the screen was in before the previous window manager was shutdown.</p>
<dt><code>SaveColor</code> { <i>colors-list</i> }</p>
<dd> This variable indicates a list of color assignments to be stored as pixel values in the root window property _MIT_PRIORITY_COLORS. Clients may elect to preserve these values when installing their own colormap. Note that use of this mechanism is a way an for application to avoid the &quot;technicolor&quot; problem, whereby useful screen objects such as window borders and titlebars disappear when a programs custom colors are installed by the window manager. For example: </p>
<pre>
<code>SaveColor</code>
{
        BorderColor
        TitleBackground
        TitleForeground
        &quot;red&quot;
        &quot;green&quot;
        &quot;blue&quot;
}
</pre>
<p> This would place on the root window 3 pixel values for borders and titlebars, as well as the three color strings, all taken from the default colormap.</p>
<dt><code>ShowIconManager</code></p>
<dd> This variable indicates that the icon manager window should be displayed when <i>twm</i> is started. It can always be brought up using the <code>f.showiconmgr</code> function.</p>
<dt><code>SortIconManager</code></p>
<dd> This variable indicates that entries in the icon manager should be sorted alphabetically rather than by simply appending new windows to the end.</p>
<dt><code>SqueezeTitle</code> [{ <i>squeeze-list</i> }]</p>
<dd> This variable indicates that <i>twm</i> should attempt to use the SHAPE extension to make titlebars occupy only as much screen space as they need, rather than extending all the way across the top of the window. The optional <i>squeeze-list</i> may be used to control the location of the squeezed titlebar along the top of the window. It contains entries of the form: </p>
<pre>
   &quot;<i>name</i>&quot;      <i>justification</i><i>num</i><i>denom</i>
</pre>
<p> where <i>name</i> is a window name, <i>justification</i> is either <code>left</code>, <code>center</code>, or <code>right</code>, and <i>num</i> and <i>denom</i> are numbers specifying a ratio giving the relative position about which the titlebar is justified. The ratio is measured from left to right if the numerator is positive, and right to left if negative. A denominator of 0 indicates that the numerator should be measured in pixels. For convenience, the ratio 0/0 is the same as 1/2 for <code>center</code> and -1/1 for <code>right</code>. For example: </p>
<pre>
<code>SqueezeTitle</code>
{
   &quot;XTerm&quot;  left  00
   &quot;xterm1&quot; left  13
   &quot;xterm2&quot; left  23
   &quot;oclock&quot; center00
   &quot;emacs&quot;  right 00
}
</pre>
<p> The <code>DontSqueezeTitle</code> list can be used to turn off squeezing on certain titles.</p>
<dt><code>StartIconified</code> [{ <i>win-list</i> }]</p>
<dd> This variable indicates that client windows should initially be left as icons until explicitly deiconified by the user. If the optional <i>win-list</i> is given, only those windows will be started iconic. This is useful for programs that do not support an <i>-iconic</i> command line option or resource.</p>
<dt><code>TitleBackground</code> <i>string</i> [{ <i>win-list</i> }]</p>
<dd> This variable specifies the background color used in titlebars, and may only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>win-list</i> is a list of window names and colors so that per-window colors may be specified. The default is &quot;white&quot;.</p>
<dt><code>TitleButtonBorderWidth</code> <i>pixels</i></p>
<dd> This variable specifies the width in pixels of the border surrounding titlebuttons. This is typically set to 0 to allow titlebuttons to take up as much space as possible and to not have a border. The default is 1.</p>
<dt><code>TitleFont</code> <i>string</i></p>
<dd> This variable specifies the font to be used for displaying window names in titlebars. The default is &quot;variable&quot;.</p>
<dt><code>TitleForeground</code> <i>string</i> [{ <i>win-list</i> }]</p>
<dd> This variable specifies the foreground color used in titlebars, and may only be specified inside of a <code>Color</code>, <code>Grayscale</code> or <code>Monochrome</code> list. The optional <i>win-list</i> is a list of window names and colors so that per-window colors may be specified. The default is &quot;black&quot;.</p>
<dt><code>TitlePadding</code> <i>pixels</i></p>
<dd> This variable specifies the distance between the various buttons, text, and highlight areas in the titlebar. The default is 8 pixels.</p>
<dt><code>UnknownIcon</code> <i>string</i></p>
<dd> This variable specifies the filename of a bitmap file to be used as the default icon. This bitmap will be used as the icon of all clients which do not provide an icon bitmap and are not listed in the <code>Icons</code> list.</p>
<dt><code>UsePPosition</code> <i>string</i></p>
<dd> This variable specifies whether or not <i>twm</i> should honor program-requested locations (given by the <code>PPosition</code> flag in the WM_NORMAL_HINTS property) in the absence of a user-specified position. The argument <i>string</i> may have one of three values: <code>&quot;off&quot;</code> (the default) indicating that <i>twm</i> should ignore the program-supplied position, <code>&quot;on&quot;</code> indicating that the position should be used, and <code>&quot;non-zero&quot;</code> indicating that the position should used if it is other than (0,0). The latter option is for working around a bug in older toolkits.</p>
<dt><code>WarpCursor</code> [{ <i>win-list</i> }]</p>
<dd> This variable indicates that the pointer should be warped into windows when they are deiconified. If the optional <i>win-list</i> is given, the pointer will only be warped when those windows are deiconified.</p>
<dt><code>WindowRing</code> { <i>win-list</i> }</p>
<dd> This variable specifies a list of windows along which the <code>f.warpring</code> function cycles.</p>
<dt><code>WarpUnmapped</code></p>
<dd> This variable indicates that the <code>f.warpto</code> function should deiconify any iconified windows it encounters. This is typically used to make a key binding that will pop a particular window (such as <i>xmh</i>), no matter where it is. The default is for <code>f.warpto</code> to ignore iconified windows.</p>
<dt><code>XorValue</code> <i>number</i></p>
<dd> This variable specifies the value to use when drawing window outlines for moving and resizing. This should be set to a value that will result in a variety of of distinguishable colors when exclusive-or&#8217;ed with the contents of the user&#8217;s typical screen. Setting this variable to 1 often gives nice results if adjacent colors in the default colormap are distinct. By default, <i>twm</i> will attempt to cause temporary lines to appear at the opposite end of the colormap from the graphics.</p>
<dt><code>Zoom</code> [ <i>count</i> ]</p>
<dd> This variable indicates that outlines suggesting movement of a window to and from its iconified state should be displayed whenever a window is iconified or deiconified. The optional <i>count</i> argument specifies the number of outlines to be drawn. The default count is 8.</dl>
<p> The following variables must be set after the fonts have been assigned, so it is usually best to put them at the end of the variables or beginning of the bindings sections:</p>
<dl>
<dt><code>DefaultFunction</code> <i>function</i></p>
<dd> This variable specifies the function to be executed when a key or button event is received for which no binding is provided. This is typically bound to <code>f.nop</code>, <code>f.beep</code>, or a menu containing window operations.</p>
<dt><code>WindowFunction</code> <i>function</i></p>
<dd> This variable specifies the function to execute when a window is selected from the <code>TwmWindows</code> menu. If this variable is not set, the window will be deiconified and raised.</dl>
<h2>BINDINGS</h2>
<p> After the desired variables have been set, functions may be attached titlebuttons and key and pointer buttons. Titlebuttons may be added from the left or right side and appear in the titlebar from left-to-right according to the order in which they are specified. Key and pointer button bindings may be given in any order. </p>
<p> Titlebuttons specifications must include the name of the pixmap to use in the button box and the function to be invoked when a pointer button is pressed within them: </p>
<pre>
<code>LeftTitleButton</code> &quot;<i>bitmapname</i>&quot;= <i>function</i>
</pre>
<p> or </p>
<pre>
<code>RightTitleButton</code> &quot;<i>bitmapname</i>&quot;= <i>function</i>
</pre>
<p> The <i>bitmapname</i> may refer to one of the built-in bitmaps (which are scaled to match <code>TitleFont</code>) by using the appropriate colon-prefixed name described above. </p>
<p> Key and pointer button specifications must give the modifiers that must be pressed, over which parts of the screen the pointer must be, and what function is to be invoked. Keys are given as strings containing the appropriate keysym name; buttons are given as the keywords <code>Button1</code>&#8211;<code>Button5</code>: </p>
<pre>
&quot;FP1&quot;    = <i>modlist</i> : <i>context</i> : <i>function</i>
<code>Button1</code>  = <i>modlist</i> : <i>context</i> : <i>function</i>
</pre>
<p> The <i>modlist</i> is any combination of the modifier names <code>shift</code>, <code>control</code>, <code>lock</code>, <code>meta</code>, <code>mod1</code>, <code>mod2</code>, <code>mod3</code>, <code>mod4</code>, or <code>mod5</code> (which may be abbreviated as <code>s</code>, <code>c</code>, <code>l</code>, <code>m</code>, <code>m1</code>, <code>m2</code>, <code>m3</code>, <code>m4</code>, <code>m5</code>, respectively) separated by a vertical bar (|). Similarly, the <i>context</i> is any combination of <code>window</code>, <code>title</code>, <code>icon</code>, <code>root</code>, <code>frame</code>, <code>iconmgr</code>, their first letters (<code>iconmgr</code> abbreviation is <code>m</code>), or <code>all</code>, separated by a vertical bar. The <i>function</i> is any of the <code>f.</code> keywords described below. For example, the default startup file contains the following bindings: </p>
<pre>
Button1  =  : root: f.menu &quot;TwmWindows&quot;
Button1  = m   : window | icon: f.function &quot;move-or-lower&quot;
Button2  = m   : window | icon: f.iconify
Button3  = m   : window | icon: f.function &quot;move-or-raise&quot;
Button1  =  : title: f.function &quot;move-or-raise&quot;
Button2  =  : title: f.raiselower
Button1  =  : icon: f.function &quot;move-or-iconify&quot;
Button2  =  : icon: f.iconify
Button1  =  : iconmgr: f.iconify
Button2  =  : iconmgr: f.iconify
</pre>
<p> A user who wanted to be able to manipulate windows from the keyboard could use the following bindings: </p>
<pre>
&quot;F1&quot;  =  : all    : f.iconify
&quot;F2&quot;  =  : all    : f.raiselower
&quot;F3&quot;  =  : all    : f.warpring &quot;next&quot;
&quot;F4&quot;  =  : all    : f.warpto &quot;xmh&quot;
&quot;F5&quot;  =  : all    : f.warpto &quot;emacs&quot;
&quot;F6&quot;  =  : all    : f.colormap &quot;next&quot;
&quot;F7&quot;  =  : all    : f.colormap &quot;default&quot;
&quot;F20&quot; =  : all    : f.warptoscreen &quot;next&quot;
&quot;Left&quot;   = m   : all: f.backiconmgr
&quot;Right&quot;  = m | s  : all: f.forwiconmgr
&quot;Up&quot;  = m   : all : f.upiconmgr
&quot;Down&quot;   = m | s  : all: f.downiconmgr
</pre>
<p> <i>Twm</i> provides many more window manipulation primitives than can be conveniently stored in a titlebar, menu, or set of key bindings. Although a small set of defaults are supplied (unless the <code>NoDefaults</code> is specified), most users will want to have their most common operations bound to key and button strokes. To do this, <i>twm</i> associates names with each of the primitives and provides <i>user-defined functions</i> for building higher level primitives and <i>menus</i> for interactively selecting among groups of functions. </p>
<p> User-defined functions contain the name by which they are referenced in calls to <code>f.function</code> and a list of other functions to execute. For example: </p>
<p>Function &#8220;move-or-lower&#8221; {f.move f.deltastop f.lower} Function &#8220;move-or-raise&#8221; {f.move f.deltastop f.raise} Function &#8220;move-or-iconify&#8221; {f.move f.deltastop f.iconify} Function &#8220;restore-colormap&#8221;<br />
{<br />
    f.colormap &#8220;default&#8221; f.lower<br />
}</p>
<p> The function name must be used in <code>f.function</code> exactly as it appears in the function specification. </p>
<p> In the descriptions below, if the function is said to operate on the selected window, but is invoked from a root menu, the cursor will be changed to the <code>Select</code> cursor and the next window to receive a button press will be chosen:</p>
<dl>
<dt><code>!</code> <i>string</i></p>
<dd> This is an abbreviation for <code>f.exec</code> <i>string</i>.</p>
<dt><code>f.autoraise</code></p>
<dd> This function toggles whether or not the selected window is raised whenever entered by the pointer. See the description of the variable <code>AutoRaise</code>.</p>
<dt><code>f.backiconmgr</code><i></p>
<dd> This function warps the pointer to the previous column in the current icon manager, wrapping back to the previous row if necessary.</p>
<dt></i><code>f.beep</code></p>
<dd> This function sounds the keyboard bell.</p>
<dt><code>f.bottomzoom</code></p>
<dd> This function is similar to the <code>f.fullzoom</code> function, but resizes the window to fill only the bottom half of the screen.</p>
<dt><code>f.circledown</code></p>
<dd> This function lowers the top-most window that occludes another window.</p>
<dt><code>f.circleup</code></p>
<dd> This function raises the bottom-most window that is occluded by another window.</p>
<dt><code>f.colormap</code> <i>string</i></p>
<dd> This function rotates the colormaps (obtained from the WM_COLORMAP_WINDOWS property on the window) that <i>twm</i> will display when the pointer is in this window. The argument <i>string</i> may have one of the following values: <code>&quot;next&quot;</code>, <code>&quot;prev&quot;</code>, and <code>&quot;default&quot;</code>. It should be noted here that in general, the installed colormap is determined by keyboard focus. A pointer driven keyboard focus will install a private colormap upon entry of the window owning the colormap. Using the click to type model, private colormaps will not be installed until the user presses a mouse button on the target window.</p>
<dt><code>f.deiconify</code></p>
<dd> This function deiconifies the selected window. If the window is not an icon, this function does nothing.</p>
<dt><code>f.delete</code></p>
<dd> This function sends the WM_DELETE_WINDOW message to the selected window if the client application has requested it through the WM_PROTOCOLS window property. The application is supposed to respond to the message by removing the indicated window. If the window has not requested WM_DELETE_WINDOW messages, the keyboard bell will be rung indicating that the user should choose an alternative method. Note this is very different from f.destroy. The intent here is to delete a single window, not necessarily the entire application.</p>
<dt><code>f.deltastop</code></p>
<dd> This function allows a user-defined function to be aborted if the pointer has been moved more than <i>MoveDelta</i> pixels. See the example definition given for <code>Function &quot;move-or-raise&quot;</code> at the beginning of the section.</p>
<dt><code>f.destroy</code></p>
<dd> This function instructs the X server to close the display connection of the client that created the selected window. This should only be used as a last resort for shutting down runaway clients. See also f.delete.</p>
<dt><code>f.downiconmgr</code><i></p>
<dd> This function warps the pointer to the next row in the current icon manger, wrapping to the beginning of the next column if necessary.</p>
<dt></i><code>f.exec</code> <i>string</i></p>
<dd> This function passes the argument <i>string</i> to /bin/sh for execution. In multiscreen mode, if <i>string</i> starts a new X client without giving a display argument, the client will appear on the screen from which this function was invoked.</p>
<dt><code>f.focus</code></p>
<dd> This function toggles the keyboard focus of the server to the selected window, changing the focus rule from pointer-driven if necessary. If the selected window already was focused, this function executes an <code>f.unfocus</code>.</p>
<dt><code>f.forcemove</code></p>
<dd> This function is like <code>f.move</code> except that it ignores the <code>DontMoveOff</code> variable.</p>
<dt><code>f.forwiconmgr</code><i></p>
<dd> This function warps the pointer to the next column in the current icon manager, wrapping to the beginning of the next row if necessary.</p>
<dt></i><code>f.fullzoom</code></p>
<dd> This function resizes the selected window to the full size of the display or else restores the original size if the window was already zoomed.</p>
<dt><code>f.function</code> <i>string</i></p>
<dd> This function executes the user-defined function whose name is specified by the argument <i>string</i>.</p>
<dt><code>f.hbzoom</code></p>
<dd> This function is a synonym for <code>f.bottomzoom</code>.</p>
<dt><code>f.hideiconmgr</code></p>
<dd> This function unmaps the current icon manager.</p>
<dt><code>f.horizoom</code></p>
<dd> This variable is similar to the <code>f.zoom</code> function except that the selected window is resized to the full width of the display.</p>
<dt><code>f.htzoom</code></p>
<dd> This function is a synonym for <code>f.topzoom</code>.</p>
<dt><code>f.hzoom</code></p>
<dd> This function is a synonym for <code>f.horizoom</code>.</p>
<dt><code>f.iconify</code></p>
<dd> This function iconifies or deiconifies the selected window or icon, respectively.</p>
<dt><code>f.identify</code></p>
<dd> This function displays a summary of the name and geometry of the selected window. If the server supports the SYNC extension, the priority of the client owning the window is also displayed. Clicking the pointer or pressing a key in the window will dismiss it.</p>
<dt><code>f.lefticonmgr</code><i></p>
<dd> This function similar to </i><code>f.backiconmgr</code> except that wrapping does not change rows.</p>
<dt><code>f.leftzoom</code></p>
<dd> This variable is similar to the <code>f.bottomzoom</code> function but causes the selected window is only resized to the left half of the display.</p>
<dt><code>f.lower</code></p>
<dd> This function lowers the selected window.</p>
<dt><code>f.menu</code> <i>string</i></p>
<dd> This function invokes the menu specified by the argument <i>string</i>. Cascaded menus may be built by nesting calls to <code>f.menu</code>.</p>
<dt><code>f.move</code></p>
<dd> This function drags an outline of the selected window (or the window itself if the <code>OpaqueMove</code> variable is set) until the invoking pointer button is released. Double clicking within the number of milliseconds given by <code>ConstrainedMoveTime</code> warps the pointer to the center of the window and constrains the move to be either horizontal or vertical depending on which grid line is crossed. To abort a move, press another button before releasing the first button.</p>
<dt><code>f.nexticonmgr</code><i></p>
<dd> This function warps the pointer to the next icon manager containing any windows on the current or any succeeding screen.</p>
<dt></i><code>f.nop</code></p>
<dd> This function does nothing and is typically used with the <code>DefaultFunction</code> or <code>WindowFunction</code> variables or to introduce blank lines in menus.</p>
<dt><code>f.previconmgr</code><i></p>
<dd> This function warps the pointer to the previous icon manager containing any windows on the current or preceding screens.</p>
<dt></i><code>f.priority</code> <i>string</i></p>
<dd> This function sets the priority of the client owning the selected window to the numeric value of the argument <i>string</i>, which should be a signed integer in double quotes (e.g. &quot;999&quot; ). This function has an effect only if the server supports the SYNC extension.</p>
<dt><code>f.quit</code></p>
<dd> This function causes <i>twm</i> to restore the window&#8217;s borders and exit. If <i>twm</i> is the first client invoked from <i>xdm</i>, this will result in a server reset.</p>
<dt><code>f.raise</code></p>
<dd> This function raises the selected window.</p>
<dt><code>f.raiselower</code></p>
<dd> This function raises the selected window to the top of the stacking order if it is occluded by any windows, otherwise the window will be lowered.</p>
<dt><code>f.refresh</code></p>
<dd> This function causes all windows to be refreshed.</p>
<dt><code>f.resize</code></p>
<dd> This function displays an outline of the selected window. Crossing a border (or setting <code>AutoRelativeResize</code>) will cause the outline to begin to rubber band until the invoking button is released. To abort a resize, press another button before releasing the first button.</p>
<dt><code>f.restart</code></p>
<dd> This function kills and restarts <i>twm</i>.</p>
<dt><code>f.startwm</code> <i>string</i></p>
<dd> This function kills <i>twm</i> and starts another window manager, as specified by <i>string</i>.</p>
<dt><code>f.righticonmgr</code><i></p>
<dd> This function is similar to </i><code>f.nexticonmgr</code> except that wrapping does not change rows.</p>
<dt><code>f.rightzoom</code></p>
<dd> This variable is similar to the <code>f.bottomzoom</code> function except that the selected window is only resized to the right half of the display.</p>
<dt><code>f.saveyourself</code></p>
<dd> This function sends a WM_SAVEYOURSELF message to the selected window if it has requested the message in its WM_PROTOCOLS window property. Clients that accept this message are supposed to checkpoint all state associated with the window and update the WM_COMMAND property as specified in the ICCCM. If the selected window has not selected for this message, the keyboard bell will be rung.</p>
<dt><code>f.showiconmgr</code></p>
<dd> This function maps the current icon manager.</p>
<dt><code>f.sorticonmgr</code></p>
<dd> This function sorts the entries in the current icon manager alphabetically. See the variable <code>SortIconManager</code>.</p>
<dt><code>f.title</code></p>
<dd> This function provides a centered, unselectable item in a menu definition. It should not be used in any other context.</p>
<dt><code>f.topzoom</code></p>
<dd> This variable is similar to the <code>f.bottomzoom</code> function except that the selected window is only resized to the top half of the display.</p>
<dt><code>f.unfocus</code></p>
<dd> This function resets the focus back to pointer-driven. This should be used when a focused window is no longer desired.</p>
<dt><code>f.upiconmgr</code><i></p>
<dd> This function warps the pointer to the previous row in the current icon manager, wrapping to the last row in the same column if necessary.</p>
<dt></i><code>f.vlzoom</code></p>
<dd> This function is a synonym for <code>f.leftzoom</code>.</p>
<dt><code>f.vrzoom</code></p>
<dd> This function is a synonym for <code>f.rightzoom</code>.</p>
<dt><code>f.warpring</code> <i>string</i></p>
<dd> This function warps the pointer to the next or previous window (as indicated by the argument <i>string</i>, which may be <code>&quot;next&quot;</code> or <code>&quot;prev&quot;</code>) specified in the <code>WindowRing</code> variable.</p>
<dt><code>f.warpto</code> <i>string</i></p>
<dd> This function warps the pointer to the window which has a name or class that matches <i>string</i>. If the window is iconified, it will be deiconified if the variable <code>WarpUnmapped</code> is set or else ignored.</p>
<dt><code>f.warptoiconmgr</code> <i>string</i></p>
<dd> This function warps the pointer to the icon manager entry associated with the window containing the pointer in the icon manager specified by the argument <i>string</i>. If <i>string</i> is empty (i.e. &quot;&quot;), the current icon manager is chosen.</p>
<dt><code>f.warptoscreen</code> <i>string</i></p>
<dd> This function warps the pointer to the screen specified by the argument <i>string</i>. <i>String</i> may be a number (e.g. <code>&quot;0&quot;</code> or <code>&quot;1&quot;</code>), the word <code>&quot;next&quot;</code> (indicating the current screen plus 1, skipping over any unmanaged screens), the word <code>&quot;back&quot;</code> (indicating the current screen minus 1, skipping over any unmanaged screens), or the word <code>&quot;prev&quot;</code> (indicating the last screen visited.</p>
<dt><code>f.winrefresh</code></p>
<dd> This function is similar to the <code>f.refresh</code> function except that only the selected window is refreshed.</p>
<dt><code>f.zoom</code></p>
<dd> This function is similar to the <code>f.fullzoom</code> function, except that the only the height of the selected window is changed.</dl>
<h2>MENUS</h2>
<p> Functions may be grouped and interactively selected using pop-up (when bound to a pointer button) or pull-down (when associated with a titlebutton) menus. Each menu specification contains the name of the menu as it will be referred to by <code>f.menu</code>, optional default foreground and background colors, the list of item names and the functions they should invoke, and optional foreground and background colors for individual items: </p>
<pre><code>
Menu "menuname" [("deffore"
                  : "defback")] {
    string1[("fore1"
             : "backn")] function1
        string2[("fore2"
                 : "backn")] function2
            .
            .
            .stringN[("foreN"
                      : "backN")] functionN
}
</code></pre>
<p> The <i>menuname</i> is case-sensitive. The optional <i>deffore</i> and <i>defback</i> arguments specify the foreground and background colors used on a color display to highlight menu entries. The <i>string</i> portion of each menu entry will be the text which will appear in the menu. The optional <i>fore</i> and <i>back</i> arguments specify the foreground and background colors of the menu entry when the pointer is not in the entry. These colors will only be used on a color display. The default is to use the colors specified by the <code>MenuForeground</code> and <code>MenuBackground</code> variables. The <i>function</i> portion of the menu entry is one of the functions, including any user-defined functions, or additional menus. </p>
<p> There is a special menu named <code>TwmWindows</code> which contains the names of all of the client and <i>twm</i>-supplied windows. Selecting an entry will cause the <code>WindowFunction</code> to be executed on that window. If <code>WindowFunction</code> hasn&#8217;t been set, the window will be deiconified and raised.</p>
<h2>ICONS</h2>
<p> <i>Twm</i> supports several different ways of manipulating iconified windows. The common pixmap-and-text style may be laid out by hand or automatically arranged as described by the <code>IconRegion</code> variable. In addition, a terse grid of icon names, called an icon manager, provides a more efficient use of screen space as well as the ability to navigate among windows from the keyboard. </p>
<p> An icon manager is a window that contains names of selected or all windows currently on the display. In addition to the window name, a small button using the default iconify symbol will be displayed to the left of the name when the window is iconified. By default, clicking on an entry in the icon manager performs <code>f.iconify</code>. To change the actions taken in the icon manager, use the the <code>iconmgr</code> context when specifying button and keyboard bindings. </p>
<p> Moving the pointer into the icon manager also directs keyboard focus to the indicated window (setting the focus explicitly or else sending synthetic events <code>NoTitleFocus</code> is set). Using the <code>f.upiconmgr</code>, <code>f.downiconmgr</code> <code>f.lefticonmgr</code>, and <code>f.righticonmgr</code> functions, the input focus can be changed between windows directly from the keyboard.</p>
<h2>BUGS</h2>
<p> The resource manager should have been used instead of all of the window lists. </p>
<p> The <code>IconRegion</code> variable should take a list. </p>
<p> Double clicking very fast to get the constrained move function will sometimes cause the window to move, even though the pointer is not moved. </p>
<p> If <code>IconifyByUnmapping</code> is on and windows are listed in <code>IconManagerDontShow</code> but not in <code>DontIconifyByUnmapping</code>, they may be lost if they are iconified and no bindings to <code>f.menu &quot;TwmWindows&quot;</code> or <code>f.warpto</code> are setup.</p>
<h2>FILES</h2>
<pre>
<i>$HOME/.twmrc.&lt;screen number&gt;</i>
<i>$HOME/.twmrc</i>
<i>/usr/lib/X11/twm/system.twmrc</i>
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>DISPLAY</p>
<dd> This variable is used to determine which X server to use. It is also set during <code>f.exec</code> so that programs come up on the proper screen.</p>
<dt>HOME</p>
<dd> This variable is used as the prefix for files that begin with a tilde and for locating the <i>twm</i> startup file.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/1-xdm/">xdm</a>(1), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1)</p>
<h2>AUTHORS</h2>
<p> Tom LaStrange, Solbourne Computer; Jim Fulton, MIT X Consortium; Steve Pitschke, Stardent Computer; Keith Packard, MIT X Consortium; Dave Sternlicht, MIT X Consortium; Dave Payne, Apple Computer. </p>
<h2>Index</h2>
