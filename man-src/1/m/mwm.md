---
title: "mwm(1)"
name: "mwm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mwm/"
description: "mwm — The Motif Window Manager"
---

<h2>NAME</h2>
<p> <code>mwm</code> &#8212; The Motif Window Manager</p>
<h2>SYNOPSIS</h2>
<p> <code>mwm</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>mwm</code> window manager provides functions that facilitate control (by the user and the programmer) of elements of window state such as placement, size, icon/normal display, and input-focus ownership. </p>
<p> The stand-alone window manager is not an integral part of CDE and does not support communication with other components in the CDE environment, such as the Style Manager and the Session Manager.</p>
<h3>Options</h3>
<dl>
<dt><i>-display</i>&nbsp;<wbr><code>display</code></p>
<dd> This option specifies the display to use; see <code><a href="/docs/linux/man/1-x/">X</a></code>(1).</p>
<dt><i>-xrm</i>&nbsp;<wbr><code>resourcestring</code></p>
<dd> This option specifies a resource string to use.</p>
<dt><i>-multiscreen</i></p>
<dd> This option causes <code>mwm</code> to manage all screens on the display. The default is to manage only a single screen.</p>
<dt><i>-name</i>&nbsp;<wbr><code>name</code></p>
<dd> This option causes <code>mwm</code> to retrieve its resources using the specified name, as in <code>name*resource</code>.</p>
<dt><i>-screens</i>&nbsp;<wbr><code>name&nbsp;<wbr>[name&nbsp;<wbr>[&#8230;]]</code></p>
<dd> This option specifies the resource names to use for the screens managed by <code>mwm</code>. If <code>mwm</code> is managing a single screen, only the first name in the list is used. If <code>mwm</code> is managing multiple screens, the names are assigned to the screens in order, starting with screen 0. Screen 0 gets the first name, screen 1 the second name, and so on.</dl>
<h3>Appearance</h3>
<p> The following sections describe the basic default behaviors of windows, icons, the icon box, input focus, and window stacking. The appearance and behavior of the window manager can be altered by changing the configuration of specific resources. Resources are defined under the heading &quot;X DEFAULTS.&quot;</p>
<h3>Screens</h3>
<p> By default, <code>mwm</code> manages only the single screen specified by the <i>-display</i> option or the <code>DISPLAY</code> environment variable (by default, screen 0). If the <i>-multiscreen</i> option is specified or if the <i>multiScreen</i> resource is True, <code>mwm</code> tries to manage all the screens on the display. </p>
<p> When <code>mwm</code> is managing multiple screens, the <i>-screens</i> option can be used to give each screen a unique resource name. The names are separated by blanks, for example, <i>-screens</i> scr0 scr1. If there are more screens than names, resources for the remaining screens will be retrieved using the first name. By default, the screen number is used for the screen name.</p>
<h3>Windows</h3>
<p> Default <code>mwm</code> window frames have distinct components with associated functions:</p>
<dl>
<dt><i>Title Area</i></p>
<dd> In addition to displaying the client&#8217;s title, the title area is used to move the window. To move the window, place the pointer over the title area, press button 1 and drag the window to a new location. By default, a wire frame is moved during the drag to indicate the new location. When the button is released, the window is moved to the new location.</p>
<dt><i>Title Bar</i></p>
<dd> The title bar includes the title area, the minimize button, the maximize button, and the window menu button. In shaped windows, such as round windows, the title bar floats above the window.</p>
<dt><i>Minimize Button</i></p>
<dd> To turn the window into an icon, click button 1 on the minimize button (the frame box with a <code>small</code> square in it).</p>
<dt><i>Maximize Button</i></p>
<dd> To make the window fill the screen (or enlarge to the largest size allowed by the configuration files), click button 1 on the maximize button (the frame box with a <code>large</code> square in it).</p>
<dt><i>Window Menu Button</i></p>
<dd> The window menu button is the frame box with a horizontal bar in it. To pull down the window menu, press button 1. While pressing, drag the pointer on the menu to your selection, then release the button when your selection is highlighted. Pressing button 3 in the title bar or resize border handles also posts the window menu. Alternately, you can click button 1 to pull down the menu and keep it posted; then position the pointer and select. You can also post the window menu by pressing &lt;Shift&gt; &lt;Esc&gt; or &lt;Alt&gt; &lt;Space&gt;. Double-clicking button 1 with the pointer on the window menu button closes the window.</dl>
<p> The following table lists the contents of the window menu.</p>
<h3>Default Window Menu</h3>
<table>
<tr VALIGN=top>
<td>Selection</td>
<td>Accelerator</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>Restore</td>
<td></td>
<td> Restores the window to its size before minimizing or maximizing.
</td>
</tr>
<tr VALIGN=top>
<td>Move</td>
<td></td>
<td> Allows the window to be moved with keys or mouse.
</td>
</tr>
<tr VALIGN=top>
<td>Size</td>
<td></td>
<td>Allows the window to be resized.
</td>
</tr>
<tr VALIGN=top>
<td>Minimize</td>
<td></td>
<td>Turns the window into an icon.
</td>
</tr>
<tr VALIGN=top>
<td>Maximize</td>
<td></td>
<td>Makes the window fill the screen.
</td>
</tr>
<tr VALIGN=top>
<td>Lower</td>
<td></td>
<td> Moves window to bottom of window stack.
</td>
</tr>
<tr VALIGN=top>
<td>Close</td>
<td>Alt+F4</td>
<td>Causes client to terminate.
</td>
</tr>
</table>
<dl>
<dt><i>Resize Border Handles</i></p>
<dd> To change the size of a window, move the pointer over a resize border handle (the cursor changes), press button 1, and drag the window to a new size. When the button is released, the window is resized. While dragging is being done, a rubber-band outline is displayed to indicate the new window size.</p>
<dt><i>Matte</i></p>
<dd> An optional matte decoration can be added between the client area and the window frame (see the <i>matteWidth</i> resource). A <i>matte</i> is not actually part of the window frame. There is no functionality associated with a matte.</dl>
<h3>Icons</h3>
<p> Icons are small graphic representations of windows. A window can be minimized (iconified) using the minimize button on the window frame. Icons provide a way to reduce clutter on the screen. </p>
<p> Pressing mouse button 1 when the pointer is over an icon causes the icon&#8217;s window menu to pop up. Releasing the button (press + release without moving mouse = click) causes the menu to stay posted. The menu contains the following selections:</p>
<h3>Icon Window Menu</h3>
<table>
<tr VALIGN=top>
<td>Selection</td>
<td>Accelerator</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>Restore</td>
<td></td>
<td>Opens the associated window.
</td>
</tr>
<tr VALIGN=top>
<td>Move</td>
<td></td>
<td> Allows the icon to be moved with keys.
</td>
</tr>
<tr VALIGN=top>
<td>Size</td>
<td></td>
<td>Inactive (not an option for icons).
</td>
</tr>
<tr VALIGN=top>
<td>Minimize</td>
<td></td>
<td>Inactive (not an option for icons).
</td>
</tr>
<tr VALIGN=top>
<td>Maximize</td>
<td></td>
<td> Opens the associated window and makes it fill the screen.
</td>
</tr>
<tr VALIGN=top>
<td>Lower</td>
<td></td>
<td>Moves icon to bottom of icon stack.
</td>
</tr>
<tr VALIGN=top>
<td>Close</td>
<td>Alt+F4</td>
<td> Removes client from <code>mwm</code> management.
</td>
</tr>
</table>
<p> Note that pressing button 3 over an icon also causes the icon&#8217;s window menu to pop up. To make a menu selection, drag the pointer over the menu and release button 3 when the desired item is highlighted. </p>
<p> Double-clicking button 1 on an icon invokes the <code>f.restore_and_raise</code> function and restores the icon&#8217;s associated window to its previous state. For example, if a maximized window is iconified, double-clicking button 1 restores it to its maximized state. Double-clicking button 1 on the icon box&#8217;s icon opens the icon box and allows access to the contained icons. (In general, double-clicking a mouse button is a quick way to perform a function.) Pressing &lt;Shift&gt; &lt;Esc&gt; or &lt;Menu&gt; (the pop-up menu key) causes the icon window menu of the currently selected icon to pop up.</p>
<h3>Icon Box</h3>
<p> When icons begin to clutter the screen, they can be packed into an icon box. (To use an icon box, <code>mwm</code> must be started with the icon box configuration already set.) The icon box is a <code>mwm</code> window that holds client icons. It includes one or more scroll bars when there are more window icons than the icon box can show at the same time. </p>
<p> Icons in the icon box can be manipulated with the mouse. The following table summarizes the behavior of this interface. Button actions apply whenever the pointer is on any part of the icon. Note that double-clicking an icon in the icon box invokes the <code>f.restore_and_raise</code> function. </p>
<table>
<tr VALIGN=top>
<td>Button</td>
<td>Action</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>Button 1</td>
<td>click</td>
<td>Selects the icon.
</td>
</tr>
<tr VALIGN=top>
<td>Button 1</td>
<td>double-click</td>
<td> Normalizes (opens) the associated window. Raises an already open window to the top of the stack.
</td>
</tr>
<tr VALIGN=top>
<td>Button 1</td>
<td>drag</td>
<td>Moves the icon.
</td>
</tr>
<tr VALIGN=top>
<td>Button 3</td>
<td>press</td>
<td> Causes the menu for that icon to pop up.
</td>
</tr>
<tr VALIGN=top>
<td>Button 3</td>
<td>drag</td>
<td> Highlights items as the pointer moves across the menu.
</td>
</tr>
</table>
<p> Pressing mouse button 3 when the pointer is over an icon causes the menu for that icon to pop up.</p>
<h3>Icon Menu for the Icon Box</h3>
<table>
<tr VALIGN=top>
<td>Selection</td>
<td>Accelerator</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>Restore</td>
<td></td>
<td> Opens the associated window (if not already open).
</td>
</tr>
<tr VALIGN=top>
<td>Move</td>
<td></td>
<td> Allows the icon to be moved with keys.
</td>
</tr>
<tr VALIGN=top>
<td>Size</td>
<td></td>
<td>Inactive.
</td>
</tr>
<tr VALIGN=top>
<td>Minimize</td>
<td></td>
<td>Inactive.
</td>
</tr>
<tr VALIGN=top>
<td>Maximize</td>
<td></td>
<td> Opens the associated window (if not already open) and maximizes its size.
</td>
</tr>
<tr VALIGN=top>
<td>Lower</td>
<td></td>
<td>Inactive.
</td>
</tr>
<tr VALIGN=top>
<td>Close</td>
<td>Alt+F4</td>
<td> Removes client from <code>mwm</code> management.
</td>
</tr>
</table>
<p> To pull down the window menu for the icon box itself, press button 1 with the pointer over the menu button for the icon box. The window menu of the icon box differs from the window menu of a client window: The &quot;Close&quot; selection is replaced with the &quot;PackIcons Shift+Alt+F7&quot; selection. When selected, PackIcons packs the icons in the box to achieve neat rows with no empty slots. </p>
<p> You can also post the window menu by pressing &lt;Shift&gt;, &lt;Esc&gt; or &lt;Alt&gt; &lt;Space&gt;. Pressing &lt;Menu&gt; (the pop-up menu key) causes the icon window menu of the currently selected icon to pop up.</p>
<h3>Input Focus</h3>
<p> The <code>mwm</code> window manager supports (by default) a keyboard input focus policy of explicit selection. This means when a window is selected to get keyboard input, it continues to get keyboard input until the window is withdrawn from window management, another window is explicitly selected to get keyboard input, or the window is iconified. Several resources control the input focus. The client window with the keyboard input focus has the active window appearance with a visually distinct window frame. </p>
<p> The following tables summarize the keyboard input focus selection behavior: </p>
<table>
<tr VALIGN=top>
<td>Button</td>
<td>Action</td>
<td>Object</td>
<td>Function Description
</td>
</tr>
<tr VALIGN=top>
<td>Button 1</td>
<td>press</td>
<td>Window / window frame</td>
<td>Keyboard focus selection.
</td>
</tr>
<tr VALIGN=top>
<td>Button 1</td>
<td>press</td>
<td>Icon</td>
<td>Keyboard focus selection.
</td>
</tr>
</table>
<table>
<tr VALIGN=top>
<td>Key Action</td>
<td>Function Description
</td>
</tr>
<tr VALIGN=top>
<td>[Alt][Tab]</td>
<td> Move input focus to next window in window stack (available only in explicit focus mode).
</td>
</tr>
<tr VALIGN=top>
<td>[Alt][Shift][Tab]</td>
<td> Move input focus to previous window in window stack (available only in explicit focus mode).
</td>
</tr>
</table>
<h3>Window Stacking</h3>
<p> There are two types of window stacks: global window stacks and an application&#8217;s local family window stack. </p>
<p> The global stacking order of windows may be changed as a result of setting the keyboard input focus, iconifying a window, or performing a window manager window stacking function. When keyboard focus policy is explicit the default value of the <i>focusAutoRaise</i> resource is True. This causes a window to be raised to the top of the stack when it receives input focus, for example, by pressing button 1 on the title bar. The key actions defined in the previous table will thus raise the window receiving focus to the top of the stack. </p>
<p> In pointer mode, the default value of <i>focusAutoRaise</i> is False, that is, the window stacking order is not changed when a window receives keyboard input focus. The following key actions can be used to cycle through the global window stack. </p>
<table>
<tr VALIGN=top>
<td>Key Action</td>
<td>Function Description
</td>
</tr>
<tr VALIGN=top>
<td>[Alt][ESC]</td>
<td> Place top window on bottom of stack.
</td>
</tr>
<tr VALIGN=top>
<td>[Alt][Shift][ESC]</td>
<td> Place bottom window on top of stack.
</td>
</tr>
</table>
<p> By default, a window&#8217;s icon is placed on the bottom of the stack when the window is iconified; however, the default can be changed by the <i>lowerOnIconify</i> resource. </p>
<p> Transient windows (secondary windows such a dialog boxes) stay above their parent windows by default; however, an application&#8217;s local family stacking order may be changed to allow a transient window to be placed below its parent top-level window. The following arguments show the modification of the stacking order for the <code>f.lower</code> function.</p>
<dl>
<dt><code>f.lower</code></p>
<dd> Lowers the transient window within the family (staying above the parent) and lowers the family in the global window stack.</p>
<dt><code>f.lower</code>&nbsp;<wbr>[ <i>within</i>]</p>
<dd> Lowers the transient window within the family (staying above the parent) but does not lower the family in the global window stack.</p>
<dt><code>f.lower</code>&nbsp;<wbr>[<i>freeFamily</i> ]</p>
<dd> Lowers the window free from its family stack (below the parent), but does not lower the family in the global window stack.</dl>
<p> The arguments <i>within</i> and <i>freeFamily</i> can also be used with <code>f.raise</code> and <code>f.raise_lower</code>.</p>
<h3>Session Management</h3>
<p> The window manager is an X Session Management Protocol aware client. It responds to SaveYourself (and other associated messages) by saving the geometries of its clients to a state file. <code>mwm</code> can then be restarted by the XSMP session manager. The default location for the state file is <code>$HOME/.mwmclientdb</code>. This location can be overriden with the resource <code>sessionClientDB</code>.</p>
<h3>X Resources</h3>
<p> The <code>mwm</code> command is configured from its resource database. This database is built from the following sources. They are listed in order of precedence, low to high: </p>
<p> <code>/usr/share/X11/app-defaults/Mwm</code> </p>
<p> <code>$HOME/Mwm</code> </p>
<p> <code>RESOURCE_MANAGER</code> root window property or <code>$HOME/.Xdefaults</code> </p>
<p> <code>XENVIRONMENT</code> variable or <code>$HOME/.Xdefaults-host</code> </p>
<p> <code>mwm</code> command line options </p>
<p> The file names <code>/usr/share/X11/app-defaults/Mwm</code> and <code>$HOME/Mwm</code> represent customary locations for these files. The actual location of the system-wide class resource file may depend on the <code>XFILESEARCHPATH</code> environment variable and the current language environment. The actual location of the user-specific class resource file may depend on the <code>XUSERFILESEARCHPATH</code> and <code>XAPPLRESDIR</code> environment variables and the current language environment. </p>
<p> Entries in the resource database may refer to other resource files for specific types of resources. These include files that contain bitmaps, fonts, and <code>mwm</code> specific resources such as menus and behavior specifications (for example, button and key bindings). </p>
<p> <i>Mwm</i> is the resource class name of <code>mwm</code> and <code>mwm</code> is the default resource name used by <code>mwm</code> to look up resources. the <i>-screens</i> command line option specifies resource names, such as &quot;mwm_b+w&quot; and &quot;mwm_color&quot;.) In the following discussion of resource specification, &quot;Mwm&quot; and &quot;mwm&quot; (and the aliased <code>mwm</code> resource names) can be used interchangeably, but &quot;mwm&quot; takes precedence over &quot;Mwm&quot;. </p>
<p> The <code>mwm</code> command uses the following types of resources:</p>
<dl>
<dt><code>Component Appearance Resources:</code></p>
<dd> These resources specify appearance attributes of window manager user interface components. They can be applied to the appearance of window manager menus, feedback windows (for example, the window reconfiguration feedback window), client window frames, and icons.</p>
<dt><code>General Appearance and Behavior Resources:</code></p>
<dd> These resources specify <code>mwm</code> appearance and behavior (for example, window management policies). They are not set separately for different <code>mwm</code> user interface components. They apply to all screens and workspaces.</p>
<dt><code>Screen Specific Appearance and Behavior Resources:</code></p>
<dd> These resources specify the appearance and behavior of <code>mwm</code> elements that are settable on a per-screen basis.</p>
<dt><code>Client Specific Resources:</code></p>
<dd> These <code>mwm</code> resources can be set for a particular client window or class of client windows. They specify client-specific icon and client window frame appearance and behavior.</dl>
<p> Resource identifiers can be either a resource name (for example, foreground) or a resource class (for example, Foreground). If the value of a resource is a filename and if the filename is prefixed by &quot;~/&quot;, then it is relative to the path contained in the <code>HOME</code> environment variable (generally the user&#8217;s home directory).</p>
<h3>Component Appearance Resources</h3>
<p> The syntax for specifying component appearance resources that apply to window manager icons, menus, and client window frames is <i>Mwm*</i> <code>resource_id</code> </p>
<p> For example, <i>Mwm*foreground</i> is used to specify the foreground color for <code>mwm</code> menus, icons, client window frames, and feedback dialogs. </p>
<p> The syntax for specifying component appearance resources that apply to a particular <code>mwm</code> component is <i>Mwm*</i>[<i>menu</i>|<i>icon</i>|<i>client</i>|<i>feedback</i>] <i>*</i><code>resource_id</code> </p>
<p> If <code>menu</code> is specified, the resource is applied only to <code>mwm</code> menus; if <code>icon</code> is specified, the resource is applied to icons; and if <code>client</code> is specified, the resource is applied to client window frames. For example, <i>Mwm*icon*foreground</i> is used to specify the foreground color for <code>mwm</code> icons, <i>Mwm*menu*foreground</i> specifies the foreground color for <code>mwm</code> menus, and <i>Mwm*client*foreground</i> is used to specify the foreground color for <code>mwm</code> client window frames. </p>
<p> The appearance of the title area of a client window frame (including window management buttons) can be separately configured. The syntax for configuring the title area of a client window frame is <i>Mwm*client*title*</i> <code>resource_id</code> </p>
<p> For example, <i>Mwm*client*title*foreground</i> specifies the foreground color for the title area. Defaults for title area resources are based on the values of the corresponding client window frame resources. </p>
<p> The appearance of menus can be configured based on the name of the menu. The syntax for specifying menu appearance by name is <i>Mwm*menu*</i> <code>menu_name</code><i>*</i><code>resource_id</code> </p>
<p> For example, <i>Mwm*menu*my_menu*foreground</i> specifies the foreground color for the menu named <i>my_menu</i>. The user can also specify resources for window manager menu components, that is, the gadgets that comprise the menu. These may include for example, a menu title, title separator, one or more buttons, and separators. If a menu contains more than one instance of a class, such as multiple PushButtonGadgets, the name of the first instance is &quot;PushButtonGadget1&quot;, the second is &quot;PushButtonGadget2&quot;, and so on. The following list identifies the naming convention used for window manager menu components:</p>
<dl>
<dt> &bull;</p>
<dd> Menu Title LabelGadget &#8211; &quot;TitleName&quot;</p>
<dt> &bull;</p>
<dd> Menu Title SeparatorGadget &#8211; &quot;TitleSeparator&quot;</p>
<dt> &bull;</p>
<dd> CascadeButtonGadget &#8211; &quot;CascadeButtonGadget&lt;n&gt;&quot;</p>
<dt> &bull;</p>
<dd> PushButtonGadget &#8211; &quot;PushButtonGadget&lt;n&gt;&quot;</p>
<dt> &bull;</p>
<dd> SeparatorGadget &#8211; &quot;SeparatorGadget&lt;n&gt;&quot;</dl>
<p> Refer to the man page for each class for a list of resources that can be specified. </p>
<p> The following component appearance resources that apply to all window manager parts can be specified:</p>
<h3>Component Appearance Resources &#8211; All Window Manager Parts</h3>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Class</td>
<td>Value Type</td>
<td>Default
</td>
</tr>
<tr VALIGN=top>
<td>background</td>
<td>Background</td>
<td>color</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>backgroundPixmap</td>
<td>BackgroundPixmap</td>
<td>string&#8211;</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>bottomShadowColor</td>
<td>Foreground</td>
<td>color</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>bottomShadowPixmap</td>
<td>Foreground</td>
<td>string&#8211;</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>fontList</td>
<td>FontList</td>
<td> string&#8212; </td>
<td>&quot;fixed&quot;
</td>
</tr>
<tr VALIGN=top>
<td>foreground</td>
<td>Foreground</td>
<td>color</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>saveUnder</td>
<td>SaveUnder</td>
<td>T/F</td>
<td>F
</td>
</tr>
<tr VALIGN=top>
<td>topShadowColor</td>
<td>Background</td>
<td>color</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>topShadowPixmap</td>
<td>TopShadowPixmap</td>
<td>string&#8211;</td>
<td>varies-
</td>
</tr>
</table>
<p> -The default is chosen based on the visual type of the screen. &#8211;Image name. See <code><a href="/docs/linux/man/3-xminstallimage/">XmInstallImage</a></code>(3). &#8212;X11 X Logical Font Description</p>
<dl>
<dt><i>background</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Background</i>)</p>
<dd> This resource specifies the background color. Any legal X color may be specified. The default value is chosen based on the visual type of the screen.</p>
<dt><i>backgroundPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>BackgroundPixmap</i>)</p>
<dd> This resource specifies the background Pixmap of the <code>mwm</code> decoration when the window is inactive (does not have the keyboard focus). The default value is chosen based on the visual type of the screen.</p>
<dt><i>bottomShadowColor</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Foreground</i>)</p>
<dd> This resource specifies the bottom shadow color. This color is used for the lower and right bevels of the window manager decoration. Any legal X color may be specified. The default value is chosen based on the visual type of the screen.</p>
<dt><i>bottomShadowPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>BottomShadowPixmap</i>)</p>
<dd> This resource specifies the bottom shadow Pixmap. This Pixmap is used for the lower and right bevels of the window manager decoration. The default is chosen based on the visual type of the screen.</p>
<dt><i>fontList</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>FontList</i>)</p>
<dd> This resource specifies the font used in the window manager decoration. The character encoding of the font should match the character encoding of the strings that are used. The default is &quot;fixed.&quot;</p>
<dt><i>foreground</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Foreground</i>)</p>
<dd> This resource specifies the foreground color. The default is chosen based on the visual type of the screen.</p>
<dt><i>saveUnder</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>SaveUnder</i>)</p>
<dd> This is used to indicate whether &quot;save unders&quot; are used for <code>mwm</code> components. For this to have any effect, save unders must be implemented by the X server. If save unders are implemented, the X server saves the contents of windows obscured by windows that have the save under attribute set. If the <i>saveUnder</i> resource is True, <code>mwm</code> will set the save under attribute on the window manager frame of any client that has it set. If <i>saveUnder</i> is False, save unders will not be used on any window manager frames. The default value is False.</p>
<dt><i>topShadowColor</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Background</i>)</p>
<dd> This resource specifies the top shadow color. This color is used for the upper and left bevels of the window manager decoration. The default is chosen based on the visual type of the screen.</p>
<dt>topShadowPixmap&nbsp;<wbr>(&nbsp;<wbr>class&nbsp;<wbr> <i>TopShadowPixmap)</i></p>
<dd> This resource specifies the top shadow Pixmap. This Pixmap is used for the upper and left bevels of the window manager decoration. The default is chosen based on the visual type of the screen.</dl>
<p> The following component appearance resources that apply to frame and icons can be specified:</p>
<h3>Frame and Icon Components</h3>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Class</td>
<td>Value Type</td>
<td>Default
</td>
</tr>
<tr VALIGN=top>
<td>activeBackground</td>
<td>Background</td>
<td>color</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>activeBackgroundPixmap</td>
<td>BackgroundPixmap</td>
<td>string&#8211;</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>activeBottomShadowColor</td>
<td>Foreground</td>
<td>color</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>activeBottomShadowPixmap</td>
<td>BottomShadowPixmap</td>
<td>string&#8211;</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>activeForeground</td>
<td>Foreground</td>
<td>color</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>activeTopShadowColor</td>
<td>Background</td>
<td>color</td>
<td>varies-
</td>
</tr>
<tr VALIGN=top>
<td>activeTopShadowPixmap</td>
<td>TopShadowPixmap</td>
<td>string&#8211;</td>
<td>varies-
</td>
</tr>
</table>
<p> -The default is chosen based on the visual type of the screen. &#8211;See <code><a href="/docs/linux/man/3-xminstallimage/">XmInstallImage</a></code>(3).</p>
<dl>
<dt><i>activeBackground</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Background</i>)</p>
<dd> This resource specifies the background color of the <code>mwm</code> decoration when the window is active (has the keyboard focus). The default is chosen based on the visual type of the screen.</p>
<dt><i>activeBackgroundPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ActiveBackgroundPixmap</i>)</p>
<dd> This resource specifies the background Pixmap of the <code>mwm</code> decoration when the window is active (has the keyboard focus). The default is chosen based on the visual type of the screen.</p>
<dt><i>activeBottomShadowColor</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Foreground</i>)</p>
<dd> This resource specifies the bottom shadow color of the <code>mwm</code> decoration when the window is active (has the keyboard focus). The default is chosen based on the visual type of the screen.</p>
<dt><i>activeBottomShadowPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>BottomShadowPixmap</i>)</p>
<dd> This resource specifies the bottom shadow Pixmap of the <code>mwm</code> decoration when the window is active (has the keyboard focus). The default is chosen based on the visual type of the screen.</p>
<dt><i>activeForeground</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Foreground</i>)</p>
<dd> This resource specifies the foreground color of the <code>mwm</code> decoration when the window is active (has the keyboard focus). The default is chosen based on the visual type of the screen.</p>
<dt><i>activeTopShadowColor</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Background</i>)</p>
<dd> This resource specifies the top shadow color of the <code>mwm</code> decoration when the window is active (has the keyboard focus). The default is chosen based on the visual type of the screen.</p>
<dt><i>activeTopShadowPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>TopShadowPixmap</i>)</p>
<dd> This resource specifies the top shadow Pixmap of the <code>mwm</code> decoration when the window is active (has the keyboard focus). The default is chosen based on the visual type of the screen.</dl>
<h3>General Appearance and Behavior Resources</h3>
<p> The syntax for specifying general appearance and behavior resources is <i>Mwm*</i><code>resource_id</code> </p>
<p> For example, <i>Mwm*keyboardFocusPolicy</i> specifies the window manager policy for setting the keyboard focus to a particular client window. </p>
<p> The following general appearance and behavior resources can be specified:</p>
<h3>General Appearance and Behavior Resources</h3>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Class</td>
<td>Value Type</td>
<td>Default
</td>
</tr>
<tr VALIGN=top>
<td>autoKeyFocus</td>
<td>AutoKeyFocus</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>autoRaiseDelay</td>
<td>AutoRaiseDelay</td>
<td>millisec</td>
<td>500
</td>
</tr>
<tr VALIGN=top>
<td>bitmap-</td>
<td>Bitmap-</td>
<td>directory</td>
<td>/usr/include-
</td>
</tr>
<tr VALIGN=top>
<td>Directory</td>
<td>Directory</td>
<td></td>
<td>/X11/bitmaps
</td>
</tr>
<tr VALIGN=top>
<td>clientAutoPlace</td>
<td>ClientAutoPlace</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>colormapFocus-</td>
<td>ColormapFocus-</td>
<td>string</td>
<td>keyboard
</td>
</tr>
<tr VALIGN=top>
<td>Policy</td>
<td>Policy</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>configFile</td>
<td>ConfigFile</td>
<td>file</td>
<td>$HOME/mwmrc
</td>
</tr>
<tr VALIGN=top>
<td>deiconifyKeyFocus</td>
<td>DeiconifyKeyFocus</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>doubleClick-</td>
<td>DoubleClick-</td>
<td>millisec.</td>
<td>multi-click
</td>
</tr>
<tr VALIGN=top>
<td>Time</td>
<td>Time</td>
<td></td>
<td>time-
</td>
</tr>
<tr VALIGN=top>
<td>enableWarp</td>
<td>enableWarp</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>enforceKeyFocus</td>
<td>EnforceKeyFocus</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>frameStyle</td>
<td>FrameStyle</td>
<td>string</td>
<td>recessed
</td>
</tr>
<tr VALIGN=top>
<td>iconAutoPlace</td>
<td>IconAutoPlace</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>iconClick</td>
<td>IconClick</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>interactivePlacement</td>
<td>InteractivePlacement</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>keyboardFocus-</td>
<td>KeyboardFocus-</td>
<td>string</td>
<td>explicit
</td>
</tr>
<tr VALIGN=top>
<td>Policy</td>
<td>Policy</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>lowerOnIconify</td>
<td>LowerOnIconify</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>moveThreshold</td>
<td>MoveThreshold</td>
<td>pixels</td>
<td>4
</td>
</tr>
<tr VALIGN=top>
<td>multiScreen</td>
<td>MultiScreen</td>
<td>T/F</td>
<td>F
</td>
</tr>
<tr VALIGN=top>
<td>passButtons</td>
<td>PassButtons</td>
<td>T/F</td>
<td>F
</td>
</tr>
<tr VALIGN=top>
<td>passSelectButton</td>
<td>PassSelectButton</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>positionIsFrame</td>
<td>PositionIsFrame</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>positionOnScreen</td>
<td>PositionOnScreen</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>quitTimeout</td>
<td>QuitTimeout</td>
<td>millisec.</td>
<td>1000
</td>
</tr>
<tr VALIGN=top>
<td>raiseKeyFocus</td>
<td>RaiseKeyFocus</td>
<td>T/F</td>
<td>F
</td>
</tr>
<tr VALIGN=top>
<td>refreshByClearing</td>
<td>RefreshByClearing</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>rootButtonClick</td>
<td>RootButtonClick</td>
<td>T/F</td>
<td>F
</td>
</tr>
<tr VALIGN=top>
<td>screens</td>
<td>Screens</td>
<td>string</td>
<td>varies
</td>
</tr>
<tr VALIGN=top>
<td>sessionClientDB</td>
<td>SessionClientDB</td>
<td>string</td>
<td>$HOME/.mwmclientdb
</td>
</tr>
<tr VALIGN=top>
<td>showFeedback</td>
<td>ShowFeedback</td>
<td>string</td>
<td>all
</td>
</tr>
<tr VALIGN=top>
<td>startupKeyFocus</td>
<td>StartupKeyFocus</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>wMenuButtonClick</td>
<td>WMenuButtonClick</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>wMenuButtonClick2</td>
<td>WMenuButtonClick2</td>
<td>T/F</td>
<td>T
</td>
</tr>
</table>
<p> -The resource doubleClickTime is included for backward compatibility. Use of the Xt resource multiClickTime is preferred.</p>
<dl>
<dt><i>autoKeyFocus</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>AutoKeyFocus</i>)</p>
<dd> This resource is available only when the keyboard input focus policy is explicit. If <i>autoKeyFocus</i> is given a value of True, then when a window with the keyboard input focus is withdrawn from window management or is iconified, the focus is set to the previous window that had the focus. If the value given is False, there is no automatic setting of the keyboard input focus. It is recommended that both <i>autoKeyFocus</i> and <i>startupKeyFocus</i> be True to work with tear off menus. The default value is True.</p>
<dt><i>autoRaiseDelay</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>AutoRaiseDelay</i>)</p>
<dd> This resource is available only when the <i>focusAutoRaise</i> resource is True and the keyboard focus policy is pointer. The <i>autoRaiseDelay</i> resource specifies the amount of time (in milliseconds) that <code>mwm</code> will wait before raising a window after it gets the keyboard focus. The default value of this resource is 500 (ms).</p>
<dt><i>bitmapDirectory</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>BitmapDirectory</i>)</p>
<dd> This resource identifies a directory to be searched for bitmaps referenced by <code>mwm</code> resources. This directory is searched if a bitmap is specified without an absolute pathname. The default value for this resource is <code>/usr/include/X11/bitmaps</code>. The directory <code>/usr/include/X11/bitmaps</code> represents the customary locations for this directory. The actual location of this directory may vary on some systems. If the bitmap is not found in the specified directory, <code>XBMLANGPATH</code> is searched.</p>
<dt><i>clientAutoPlace</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ClientAutoPlace</i>)</p>
<dd> This resource determines the position of a window when the window has not been given a program- or user-specified position. With a value of True, windows are positioned with the top left corners of the frames offset horizontally and vertically. A value of False causes the currently configured position of the window to be used. In either case, <code>mwm</code> will attempt to place the windows totally on-screen. The default value is True.</p>
<dt><i>colormapFocusPolicy</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ColormapFocusPolicy</i>)</p>
<dd> This resource indicates the colormap focus policy that is to be used. If the resource value is explicit, a colormap selection action is done on a client window to set the colormap focus to that window. If the value is pointer, the client window containing the pointer has the colormap focus. If the value is keyboard, the client window that has the keyboard input focus has the colormap focus. The default value for this resource is keyboard.</p>
<dt><i>configFile</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ConfigFile</i>)</p>
<dd> The resource value is the pathname for a <code>mwm</code> resource description file. If the pathname begins with &quot;~/&quot;, <code>mwm</code> considers it to be relative to the user&#8217;s home directory (as specified by the <code>HOME</code> environment variable). If the <code>LANG</code> environment variable is set, <code>mwm</code> looks for <i>$HOME/$LANG</i>/ <code>configFile</code>. If that file does not exist or if <code>LANG</code> is not set, <code>mwm</code> looks for <code>$HOME</code>/<code>configFile</code>. If the <i>configFile</i> pathname does not begin with &quot;~/&quot; or &quot;/&quot;, <code>mwm</code> considers it to be relative to the current working directory. If the <i>configFile</i> resource is not specified or if that file does not exist, <code>mwm</code> uses several default paths to find a configuration file. The order of the search is shown below: <code>/etc/X11/mwm/$LANG/system.mwmrc</code>&#8211; <code>/etc/X11/mwm/system.mwmrc</code>&#8211; Paths marked with &#8216;-&#8216; are implementation dependent.</p>
<dt><i>deiconifyKeyFocus</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>DeiconifyKeyFocus</i>)</p>
<dd> This resource applies only when the keyboard input focus policy is explicit. If a value of True is used, a window receives the keyboard input focus when it is normalized (deiconified). True is the default value.</p>
<dt><i>doubleClickTime</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>DoubleClickTime</i>)</p>
<dd> This resource is used to set the maximum time (in ms) between the clicks (button presses) that make up a double-click. The use of this resource is deprecated. Use the Xt resource <i>multiClickTime</i> instead. The value of <i>doubleClickTime</i> dynamically defaults to the value of <i>multiClickTime</i>.</p>
<dt><i>enableWarp</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>EnableWarp</i>)</p>
<dd> The default value of this resource, True, causes <code>mwm</code> to warp the pointer to the center of the selected window during keyboard-controlled resize and move operations. Setting the value to False causes <code>mwm</code> to leave the pointer at its original place on the screen, unless the user explicitly moves it with the cursor keys or pointing device.</p>
<dt><i>enforceKeyFocus</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>EnforceKeyFocus</i>)</p>
<dd> If this resource is given a value of True, the keyboard input focus is always explicitly set to selected windows even if there is an indication that they are &quot;globally active&quot; input windows. (An example of a globally active window is a scroll bar that can be operated without setting the focus to that client.) If the resource is False, the keyboard input focus is not explicitly set to globally active windows. The default value is True.</p>
<dt><i>frameStyle</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>frameStyle</i>)</p>
<dd> If this resource is given a value of &quot;slab&quot;, the the window manager frame is drawn such that the client area appears to be at the same height as the top of the window frame. If the resource is set to &quot;recessed&quot;, the window frame is drawn such that the client area appears lower than the top of the window frame. The default value is &quot;recessed&quot;.</p>
<dt><i>iconAutoPlace</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconAutoPlace</i>)</p>
<dd> This resource indicates whether the window manager arranges icons in a particular area of the screen or places each icon where the window was when it was iconified. The value True indicates that icons are arranged in a particular area of the screen, determined by the <i>iconPlacement</i> resource. The value False indicates that an icon is placed at the location of the window when it is iconified. The default is True.</p>
<dt><i>iconClick</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconClick</i>)</p>
<dd> When this resource is given the value of True, the system menu is posted and left posted when an icon is clicked. The default value is True.</p>
<dt><i>interactivePlacement</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>InteractivePlacement</i>)</p>
<dd> This resource controls the initial placement of new windows on the screen. If the value is True, the pointer shape changes before a new window is placed on the screen to indicate to the user that a position should be selected for the upper-left hand corner of the window. If the value is False, windows are placed according to the initial window configuration attributes. The default value of this resource is False.</p>
<dt><i>keyboardFocusPolicy</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>KeyboardFocusPolicy</i>)</p>
<dd> If set to pointer, the keyboard focus policy is to have the keyboard focus set to the client window that contains the pointer (the pointer could also be in the client window decoration that <code>mwm</code> adds). If set to explicit, the policy is to have the keyboard focus set to a client window when the user presses button 1 with the pointer on the client window or any part of the associated <code>mwm</code> decoration. The default value for this resource is explicit.</p>
<dt><i>lowerOnIconify</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>LowerOnIconify</i>)</p>
<dd> If this resource is given the default value of True, a window&#8217;s icon appears on the bottom of the window stack when the window is minimized (iconified). A value of False places the icon in the stacking order at the same place as its associated window. The default value of this resource is True.</p>
<dt><i>moveThreshold</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>MoveThreshold</i>)</p>
<dd> This resource is used to control the sensitivity of dragging operations that move windows and icons. The value of this resource is the number of pixels that the locator is moved with a button down before the move operation is initiated. This is used to prevent window/icon movement when you click or double-click and there is unintentional pointer movement with the button down. The default value of this resource is 4 (pixels).</p>
<dt><i>multiScreen</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>MultiScreen</i>)</p>
<dd> This resource, if True, causes <code>mwm</code> to manage all the screens on the display. If False, <code>mwm</code> manages only a single screen. The default value is False.</p>
<dt><i>passButtons</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>PassButtons</i>)</p>
<dd> This resource indicates whether or not button press events are passed to clients after they are used to do a window manager function in the client context. If the resource value is False, the button press is not passed to the client. If the value is True, the button press is passed to the client window. The window manager function is done in either case. The default value for this resource is False.</p>
<dt><i>passSelectButton</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>PassSelectButton</i>)</p>
<dd> This resource indicates whether or not to pass the select button press events to clients after they are used to do a window manager function in the client context. If the resource value is False, then the button press will not be passed to the client. If the value is True, the button press is passed to the client window. The window manager function is done in either case. The default value for this resource is True.</p>
<dt><i>positionIsFrame</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>PositionIsFrame</i>)</p>
<dd> This resource indicates how client window position information (from the <i>WM_NORMAL_HINTS</i> property and from configuration requests) is to be interpreted. If the resource value is True, the information is interpreted as the position of the <code>mwm</code> client window frame. If the value is False, it is interpreted as being the position of the client area of the window. The default value of this resource is True.</p>
<dt><i>positionOnScreen</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>PositionOnScreen</i>)</p>
<dd> This resource is used to indicate that windows should initially be placed (if possible) so that they are not clipped by the edge of the screen (if the resource value is True). If a window is larger than the size of the screen, at least the upper-left corner of the window is on-screen. If the resource value is False, windows are placed in the requested position even if totally off-screen. The default value of this resource is True.</p>
<dt><i>quitTimeout</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>QuitTimeout</i>)</p>
<dd> This resource specifies the amount of time (in milliseconds) that <code>mwm</code> will wait for a client to update the <i>WM_COMMAND</i> property after <code>mwm</code> has sent the <code>WM_SAVE_YOURSELF</code> message. The default value of this resource is 1000 (ms). (Refer to the <code>f.kill</code> function description for additional information.)</p>
<dt><i>raiseKeyFocus</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>RaiseKeyFocus</i>)</p>
<dd> This resource is available only when the keyboard input focus policy is explicit. When set to True, this resource specifies that a window raised by means of the <code>f.normalize_and_raise</code> function also receives the input focus. The default value of this resource is False.</p>
<dt><i>refreshByClearing</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>RefreshByClearing</i>)</p>
<dd> This resource determines the mechanism used to refresh a window (or the screen) when the <code>f.refresh_win</code> (<code>f.refresh</code>) function is executed. When set to True, an XClearArea is performed over the window for <code>f.refresh_win</code>. When set to False, a covering window is created and destroyed over the top of the window to be refreshed. If the function is <code>f.refresh</code> and this resource is set to True, then an XClearArea is performed over every window on the screen. If the resource is set to False, then one large window covering the entire screen is created and destroyed. The default value of this resource is True.</p>
<dt><i>rootButtonClick</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>RootButtonClick</i>)</p>
<dd> The <i>rootButtonClick</i> resource controls whether the a click on the root window will post the root menu in a &quot;sticky&quot; mode. If this resource is set to True, a button click on the root window will post the menu bound to the button down event for that button in a &quot;sticky&quot; fashion. If this resource is set to False, then the same button click would only cause the menu to flash as it would be unposted once the button up event is seen. The criterion used to determine if it is a button click is if the pointer doesn&#8217;t move between the button down and button up events. The default value for this resource is True.</p>
<dt><i>screens</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Screens</i>)</p>
<dd> This resource specifies the resource names to use for the screens managed by <code>mwm</code>. If <code>mwm</code> is managing a single screen, only the first name in the list is used. If <code>mwm</code> is managing multiple screens, the names are assigned to the screens in order, starting with screen 0. Screen 0 gets the first name, screen 1 the second name, and so on. The default screen names are 0, 1, and so on.</p>
<dt><i>sessionClientDB</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>SessionClientDB</i>)</p>
<dd> This resource identifies a file name to use as a root when saving state at the request of an XSMP session manager. When the session is saved, the window manager will then reuse the file name by automatically incrementing a suffix.</p>
<dt><i>showFeedback</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ShowFeedback</i>)</p>
<dd> This resource controls whether or not feedback windows or confirmation dialogs are displayed. A feedback window shows a client window&#8217;s initial placement and shows position and size during move and resize operations. Confirmation dialogs can be displayed for certain operations. The value for this resource is a list of names of the feedback options to be enabled or disabled; the names must be separated by a space. If an option is preceded by a minus sign, that option is excluded from the list. The <code>sign</code> of the first item in the list determines the initial set of options. If the sign of the first option is minus, <code>mwm</code> assumes all options are present and starts subtracting from that set. If the sign of the first decoration is plus (or not specified), <code>mwm</code> starts with no options and builds up a list from the resource.</dl>
<p> The names of the feedback options are shown below: </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>all</td>
<td>Show all feedback (Default value).
</td>
</tr>
<tr VALIGN=top>
<td>behavior</td>
<td>Confirm behavior switch.
</td>
</tr>
<tr VALIGN=top>
<td>kill</td>
<td>Confirm on receipt of KILL signal.
</td>
</tr>
<tr VALIGN=top>
<td>move</td>
<td>Show position during move.
</td>
</tr>
<tr VALIGN=top>
<td>none</td>
<td>Show no feedback.
</td>
</tr>
<tr VALIGN=top>
<td>placement</td>
<td> Show position and size during initial placement.
</td>
</tr>
<tr VALIGN=top>
<td>quit</td>
<td>Confirm quitting <code>mwm</code>.
</td>
</tr>
<tr VALIGN=top>
<td>resize</td>
<td>Show size during resize.
</td>
</tr>
<tr VALIGN=top>
<td>restart</td>
<td>Confirm <code>mwm</code> restart.
</td>
</tr>
</table>
<p> The following command line illustrates the syntax for showFeedback: </p>
<pre>
<tt></tt><i>Mwm*showFeedback: placement resize behavior restart</i>
</pre>
<p> This resource specification provides feedback for initial client placement and resize, and enables the dialog boxes to confirm the restart and set behavior functions. It disables feedback for the move function. The default value for this resource is all.</p>
<dl>
<dt><i>startupKeyFocus</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>StartupKeyFocus</i>)</p>
<dd> This resource is available only when the keyboard input focus policy is explicit. When given the default value of True, a window gets the keyboard input focus when the window is mapped (that is, initially managed by the window manager). It is recommended that both <i>autoKeyFocus</i> and <i>startupKeyFocus</i> be True to work with tear off menus. The default value is True.</p>
<dt><i>wMenuButtonClick</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>WMenuButtonClick</i>)</p>
<dd> This resource indicates whether a click of the mouse when the pointer is over the window menu button posts and leaves posted the window menu. If the value given this resource is True, the menu remains posted. True is the default value for this resource.</p>
<dt><i>wMenuButtonClick2</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>WMenuButtonClick2</i>)</p>
<dd> When this resource is given the default value of True, a double-click action on the window menu button does an <i>f.kill function</i>.</dl>
<h3>Screen Specific Appearance and Behavior Resources</h3>
<p> The syntax for specifying screen specific resources is <i>Mwm*</i> <code>screen_name</code><i>*</i><code>resource_id</code> For example, <i>Mwm*1*keyBindings</i> specifies the key bindings to use for screen &quot;1&quot;.</p>
<h3>Screen Specific Resources</h3>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Class</td>
<td>Value Type</td>
<td>Default
</td>
</tr>
<tr VALIGN=top>
<td>buttonBindings</td>
<td>ButtonBindings</td>
<td>string</td>
<td>DefaultButtonBindings
</td>
</tr>
<tr VALIGN=top>
<td>cleanText</td>
<td>CleanText</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>fadeNormalIcon</td>
<td>FadeNormalIcon</td>
<td>T/F</td>
<td>F
</td>
</tr>
<tr VALIGN=top>
<td>feedbackGeometry</td>
<td>FeedbackGeometry</td>
<td>string</td>
<td>center on screen
</td>
</tr>
<tr VALIGN=top>
<td>frameBorderWidth</td>
<td>FrameBorderWidth</td>
<td>pixels</td>
<td>varies
</td>
</tr>
<tr VALIGN=top>
<td>iconBoxGeometry</td>
<td>IconBoxGeometry</td>
<td>string</td>
<td>6&#215;1+0-0
</td>
</tr>
<tr VALIGN=top>
<td>iconBoxName</td>
<td>IconBoxName</td>
<td>string</td>
<td>iconbox
</td>
</tr>
<tr VALIGN=top>
<td>iconBoxSBDisplayPolicy</td>
<td>IconBoxSBDisplayPolicy</td>
<td>string</td>
<td>all
</td>
</tr>
<tr VALIGN=top>
<td>iconBoxTitle</td>
<td>IconBoxTitle</td>
<td>XmString</td>
<td>Icons
</td>
</tr>
<tr VALIGN=top>
<td>iconDecoration</td>
<td>IconDecoration</td>
<td>string</td>
<td>varies
</td>
</tr>
<tr VALIGN=top>
<td>iconImageMaximum</td>
<td>IconImageMaximum</td>
<td>wxh</td>
<td>48&#215;48
</td>
</tr>
<tr VALIGN=top>
<td>iconImageMinimum</td>
<td>IconImageMinimum</td>
<td>wxh</td>
<td>16&#215;16
</td>
</tr>
<tr VALIGN=top>
<td>iconPlacement</td>
<td>IconPlacement</td>
<td>string</td>
<td>left bottom
</td>
</tr>
<tr VALIGN=top>
<td>iconPlacementMargin</td>
<td>IconPlacementMargin</td>
<td>pixels</td>
<td>varies
</td>
</tr>
<tr VALIGN=top>
<td>keyBindings</td>
<td>KeyBindings</td>
<td>string</td>
<td>DefaultKeyBindings
</td>
</tr>
<tr VALIGN=top>
<td>limitResize</td>
<td>LimitResize</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>maximumMaximumSize</td>
<td>MaximumMaximumSize</td>
<td>wxh (pixels)</td>
<td>2X screen w&amp;h
</td>
</tr>
<tr VALIGN=top>
<td>moveOpaque</td>
<td>MoveOpaque</td>
<td>T/F</td>
<td>F
</td>
</tr>
<tr VALIGN=top>
<td>resizeBorderWidth</td>
<td>ResizeBorderWidth</td>
<td>pixels</td>
<td>varies
</td>
</tr>
<tr VALIGN=top>
<td>resizeCursors</td>
<td>ResizeCursors</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>transientDecoration</td>
<td>TransientDecoration</td>
<td>string</td>
<td>menu title
</td>
</tr>
<tr VALIGN=top>
<td>transientFunctions</td>
<td>TransientFunctions</td>
<td>string</td>
<td> -minimize-maximize
</td>
</tr>
<tr VALIGN=top>
<td>useIconBox</td>
<td>UseIconBox</td>
<td>T/F</td>
<td>F
</td>
</tr>
</table>
<dl>
<dt><i>buttonBindings</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ButtonBindings</i>)</p>
<dd> This resource identifies the set of button bindings for window management functions. The named set of button bindings is specified in the <code>mwm</code> resource description file. These button bindings are <code>merged</code> with the built-in default bindings. The default value for this resource is &quot;DefaultButtonBindings&quot;.</p>
<dt><i>cleanText</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>CleanText</i>)</p>
<dd> This resource controls the display of window manager text in the client title and feedback windows. If the default value of True is used, the text is drawn with a clear (no stipple) background. This makes text easier to read on monochrome systems where a backgroundPixmap is specified. Only the stippling in the area immediately around the text is cleared. If False, the text is drawn directly on top of the existing background.</p>
<dt><i>fadeNormalIcon</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>FadeNormalIcon</i>)</p>
<dd> If this resource is given a value of True, an icon is grayed out whenever it has been normalized (its window has been opened). The default value is False.</p>
<dt><i>feedbackGeometry</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>FeedbackGeometry</i>)</p>
<dd> This resource sets the position of the move and resize feedback window. If this resource is not specified, the default is to place the feedback window at the center of the screen. The value of the resource is a standard window geometry string with the following syntax: [<i>=</i>]{ <i>+-</i>}<code>xoffset</code>{<i>+-</i>} <code>yoffset</code>]</p>
<dt><i>frameBorderWidth</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>FrameBorderWidth</i>)</p>
<dd> This resource specifies the width (in pixels) of a client window frame border without resize handles. The border width includes the 3-D shadows. The default value is based on the size and resolution of the screen.</p>
<dt><i>iconBoxGeometry</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconBoxGeometry</i>)</p>
<dd> This resource indicates the initial position and size of the icon box. The value of the resource is a standard window geometry string with the following syntax: [<i>=</i>][<code>width</code> <i>x</i><code>height</code>][{<i>+-</i>}<code>xoffset</code> {<i>+-</i>}<code>yoffset</code>] If the offsets are not provided, the iconPlacement policy is used to determine the initial placement. The units for width and height are columns and rows. The actual screen size of the icon box window depends on the iconImageMaximum (size) and <i>iconDecoration</i> resources. The default value for size is (6 * iconWidth + padding) wide by (1 * iconHeight + padding) high. The default value of the location is +0 -0.</p>
<dt><i>iconBoxName</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconBoxName</i>)</p>
<dd> This resource specifies the name that is used to look up icon box resources. The default name is iconbox.</p>
<dt><i>iconBoxSBDisplayPolicy</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconBoxSBDisplayPolicy</i>)</p>
<dd> This resource specifies the scroll bar display policy of the window manager in the icon box. The resource has three possible values: all, vertical, and horizontal. The default value, &quot;all&quot;, causes both vertical and horizontal scroll bars always to appear. The value &quot;vertical&quot; causes a single vertical scroll bar to appear in the icon box and sets the orientation of the icon box to horizontal (regardless of the iconBoxGeometry specification). The value &quot;horizontal&quot; causes a single horizontal scroll bar to appear in the icon box and sets the orientation of the icon box to vertical (regardless of the iconBoxGeometry specification).</p>
<dt><i>iconBoxTitle</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconBoxTitle</i>)</p>
<dd> This resource specifies the name that is used in the title area of the icon box frame. The default value is Icons.</p>
<dt><i>iconDecoration</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconDecoration</i>)</p>
<dd> This resource specifies the general icon decoration. The resource value is label (only the label part is displayed) or image (only the image part is displayed) or label image (both the label and image parts are displayed). A value of activelabel can also be specified to get a label (not truncated to the width of the icon) when the icon is selected. The default icon decoration for icon box icons is that each icon has a label part and an image part (label image). The default icon decoration for stand alone icons is that each icon has an active label part, a label part, and an image part (activelabel label image).</p>
<dt><i>iconImageMaximum</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconImageMaximum</i>)</p>
<dd> This resource specifies the maximum size of the icon image. The resource value is <code>width</code><i>x</i> <code>height</code> (for example, 64&#215;64). The maximum supported size is 128&#215;128. The default value of this resource is 50&#215;50.</p>
<dt><i>iconImageMinimum</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconImageMinimum</i>)</p>
<dd> This resource specifies the minimum size of the icon image. The resource value is <code>width</code><i>x</i> <code>height</code> (for example, 32&#215;50). The minimum supported size is 16&#215;16. The default value of this resource is 16&#215;16.</p>
<dt><i>iconPlacement</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconPlacement</i>)</p>
<dd> This resource specifies the icon placement scheme to be used. The resource value has the following syntax:</p>
<dt>
<dd> <code>primary_layout secondary_layout [tight]</code></dl>
<p> The layout values are one of the following: </p>
<table>
<tr VALIGN=top>
<td>Value</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>top</td>
<td>Lay the icons out top to bottom.
</td>
</tr>
<tr VALIGN=top>
<td>bottom</td>
<td>Lay the icons out bottom to top.
</td>
</tr>
<tr VALIGN=top>
<td>left</td>
<td>Lay the icons out left to right.
</td>
</tr>
<tr VALIGN=top>
<td>right</td>
<td>Lay the icons out right to left.
</td>
</tr>
</table>
<p> A horizontal (vertical) layout value should not be used for both the <code>primary_layout</code> and the <code>secondary_layout</code> (for example, don&#8217;t use top for the <code>primary_layout</code> and bottom for the <code>secondary_layout</code>). </p>
<p> The <code>primary_layout</code> indicates whether, when an icon placement is done, the icon is placed in a row or a column and the direction of placement. The <code>secondary_layout</code> indicates where to place new rows or columns. For example, top right indicates that icons should be placed top to bottom on the screen and that columns should be added from right to left on the screen. </p>
<p> The default placement is left bottom (icons are placed left to right on the screen, with the first row on the bottom of the screen, and new rows added from the bottom of the screen to the top of the screen). A <code>tight</code> value places icons with zero spacing in between icons. This value is useful for aesthetic reasons, as well as X-terminals with small screens.</p>
<dl>
<dt><i>iconPlacementMargin</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconPlacementMargin</i>)</p>
<dd> This resource sets the distance between the edge of the screen and the icons that are placed along the edge of the screen. The value should be greater than or equal to 0. A default value (see below) is used if the value specified is invalid. The default value for this resource is equal to the space between icons as they are placed on the screen (this space is based on maximizing the number of icons in each row and column).</p>
<dt><i>keyBindings</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>KeyBindings</i>)</p>
<dd> This resource identifies the set of key bindings for window management functions. If specified, these key bindings <code>replace</code> the built-in default bindings. The named set of key bindings is specified in <code>mwm</code> resource description file. The default value for this resource is &quot;DefaultKeyBindings&quot;.</p>
<dt><i>limitResize</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>LimitResize</i>)</p>
<dd> If this resource is True, the user is not allowed to resize a window to greater than the maximum size. The default value for this resource is True.</p>
<dt><i>maximumMaximumSize</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>MaximumMaximumSize</i>)</p>
<dd> This resource is used to limit the maximum size of a client window as set by the user or client. The resource value is <code>width</code><i>x</i><code>height</code> (for example, 1024&#215;1024) where the width and height are in pixels. The default value of this resource is twice the screen width and height.</p>
<dt><i>moveOpaque</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>MoveOpaque</i>)</p>
<dd> This resource controls whether the actual window is moved or a rectangular outline of the window is moved. A default value of False displays a rectangular outline on moves.</p>
<dt><i>resizeBorderWidth</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ResizeBorderWidth</i>)</p>
<dd> This resource specifies the width (in pixels) of a client window frame border with resize handles. The specified border width includes the 3-D shadows. The default value is based on the size and resolution of the screen.</p>
<dt><i>resizeCursors</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ResizeCursors</i>)</p>
<dd> This is used to indicate whether the resize cursors are always displayed when the pointer is in the window size border. If True, the cursors are shown, otherwise the window manager cursor is shown. The default value is True.</p>
<dt><i>transientDecoration</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>TransientDecoration</i>)</p>
<dd> This controls the amount of decoration that <code>mwm</code> puts on transient windows. The decoration specification is exactly the same as for the <i>clientDecoration</i> (client specific) resource. Transient windows are identified by the <i>WM_TRANSIENT_FOR</i> property, which is added by the client to indicate a relatively temporary window. The default value for this resource is menu title (that is, transient windows have frame borders and a titlebar with a window menu button).</p>
<dt>
<dd> An application can also specify which decorations <code>mwm</code> should apply to its windows. If it does so, <code>mwm</code> applies only those decorations indicated by both the application and the <i>transientDecoration</i> resource. Otherwise, <code>mwm</code> applies the decorations indicated by the <i>transientDecoration</i> resource. For more information see the description of <code>XmNmwmDecorations</code> on the <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3) reference page.</p>
<dt><i>transientFunctions</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>TransientFunctions</i>)</p>
<dd> This resource is used to indicate which window management functions are applicable (or not applicable) to transient windows. The function specification is exactly the same as for the <i>clientFunctions</i> (client specific) resource. The default value for this resource is -minimize -maximize.</p>
<dt>
<dd> An application can also specify which functions <code>mwm</code> should apply to its windows. If it does so, <code>mwm</code> applies only those functions indicated by both the application and the <i>transientFunctions</i> resource. Otherwise, <code>mwm</code> applies the functions indicated by the <i>transientFunctions</i> resource. For more information see the description of <code>XmNmwmFunctions</code> on the <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3) reference page.</p>
<dt><i>useIconBox</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>UseIconBox</i>)</p>
<dd> If this resource is given a value of True, icons are placed in an icon box. When an icon box is not used, the icons are placed on the root window (default value).</dl>
<h3>Client Specific Resources</h3>
<p> The syntax for specifying client specific resources is </p>
<p> <i>Mwm*</i><code>client_name_or_class</code> <i>*</i><code>resource_id</code> </p>
<p> For example, <i>Mwm*mterm*windowMenu</i> is used to specify the window menu to be used with mterm clients. The syntax for specifying client specific resources for all classes of clients is </p>
<p> <i>Mwm*</i><code>resource_id</code> </p>
<p> Specific client specifications take precedence over the specifications for all clients. For example, <i>Mwm*windowMenu</i> is used to specify the window menu to be used for all classes of clients that don&#8217;t have a window menu specified. </p>
<p> The syntax for specifying resource values for windows that have an unknown name and class (that is, windows that do not have a <code>WM_CLASS</code> property associated with them) is </p>
<p> <i>Mwm*defaults*</i><code>resource_id</code> </p>
<p> For example, <i>Mwm*defaults*iconImage</i> is used to specify the icon image to be used for windows that have an unknown name and class. </p>
<p> The following client specific resources can be specified:</p>
<h3>Client Specific Resources</h3>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Class</td>
<td>Value Type</td>
<td>Default
</td>
</tr>
<tr VALIGN=top>
<td>clientDecoration</td>
<td>ClientDecoration</td>
<td>string</td>
<td>all.
</td>
</tr>
<tr VALIGN=top>
<td>clientFunctions</td>
<td>ClientFunctions</td>
<td>string</td>
<td>all.
</td>
</tr>
<tr VALIGN=top>
<td>focusAutoRaise</td>
<td>FocusAutoRaise</td>
<td>T/F</td>
<td>varies
</td>
</tr>
<tr VALIGN=top>
<td>iconImage</td>
<td>IconImage</td>
<td>pathname</td>
<td>(image)
</td>
</tr>
<tr VALIGN=top>
<td>iconImage-</td>
<td>Background</td>
<td>color</td>
<td>icon background
</td>
</tr>
<tr VALIGN=top>
<td>Background</td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>iconImageBottom-</td>
<td>Foreground</td>
<td>color</td>
<td>icon
</td>
</tr>
<tr VALIGN=top>
<td>ShadowColor</td>
<td></td>
<td></td>
<td>bottom shadow
</td>
</tr>
<tr VALIGN=top>
<td>iconImageBottom-</td>
<td>BottomShadow-</td>
<td>color</td>
<td>icon bottom
</td>
</tr>
<tr VALIGN=top>
<td>ShadowPixmap</td>
<td>Pixmap</td>
<td></td>
<td>shadow pixmap
</td>
</tr>
<tr VALIGN=top>
<td>iconImageForeground</td>
<td>Foreground</td>
<td>color</td>
<td>varies
</td>
</tr>
<tr VALIGN=top>
<td>iconImageTopShadowColor</td>
<td>Background</td>
<td>color</td>
<td>icon top
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>shadow color
</td>
</tr>
<tr VALIGN=top>
<td>iconImageTop-</td>
<td>TopShadowPixmap</td>
<td>color</td>
<td>icon top
</td>
</tr>
<tr VALIGN=top>
<td>ShadowPixmap</td>
<td></td>
<td></td>
<td>shadow pixmap
</td>
</tr>
<tr VALIGN=top>
<td>matteBackground</td>
<td>Background</td>
<td>color</td>
<td>background
</td>
</tr>
<tr VALIGN=top>
<td>matteBottom-</td>
<td>Foreground</td>
<td>color</td>
<td>bottom
</td>
</tr>
<tr VALIGN=top>
<td>ShadowColor</td>
<td></td>
<td></td>
<td>shadow color
</td>
</tr>
<tr VALIGN=top>
<td>matteBottom-</td>
<td>BottomShadow-</td>
<td>color</td>
<td>bottom
</td>
</tr>
<tr VALIGN=top>
<td>ShadowPixmap</td>
<td>Pixmap</td>
<td></td>
<td>shadow pixmap
</td>
</tr>
<tr VALIGN=top>
<td>matteForeground</td>
<td>Foreground</td>
<td>color</td>
<td>foreground
</td>
</tr>
<tr VALIGN=top>
<td>matteTopShadowColor</td>
<td>Background</td>
<td>color</td>
<td>top
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>shadow color
</td>
</tr>
<tr VALIGN=top>
<td>matteTopShadowPixmap</td>
<td>TopShadowPixmap</td>
<td>color</td>
<td>top
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>shadow pixmap
</td>
</tr>
<tr VALIGN=top>
<td>matteWidth</td>
<td>MatteWidth</td>
<td>pixels</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>maximumClientSize</td>
<td>MaximumClientSize</td>
<td>wxh</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>vertical horizontal</td>
<td>fill the screen
</td>
</tr>
<tr VALIGN=top>
<td>useClientIcon</td>
<td>UseClientIcon</td>
<td>T/F</td>
<td>T
</td>
</tr>
<tr VALIGN=top>
<td>usePPosition</td>
<td>UsePPosition</td>
<td>string</td>
<td>nonzero
</td>
</tr>
<tr VALIGN=top>
<td>windowMenu</td>
<td>WindowMenu</td>
<td>string</td>
<td>DefaultWindowMenu
</td>
</tr>
</table>
<dl>
<dt><i>clientDecoration</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ClientDecoration</i>)</p>
<dd> This resource controls the amount of window frame decoration. The resource is specified as a list of decorations to specify their inclusion in the frame. If a decoration is preceded by a minus sign, that decoration is excluded from the frame. The <code>sign</code> of the first item in the list determines the initial amount of decoration. If the sign of the first decoration is minus, <code>mwm</code> assumes all decorations are present and starts subtracting from that set. If the sign of the first decoration is plus (or not specified), then <code>mwm</code> starts with no decoration and builds up a list from the resource.</p>
<dt>
<dd> An application can also specify which decorations <code>mwm</code> should apply to its windows. If it does so, <code>mwm</code> applies only those decorations indicated by both the application and the <i>clientDecoration</i> resource. Otherwise, <code>mwm</code> applies the decorations indicated by the <i>clientDecoration</i> resource. For more information see the description of <code>XmNmwmDecorations</code> on the <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3) reference page. </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>all</td>
<td> Include all decorations (default value).
</td>
</tr>
<tr VALIGN=top>
<td>border</td>
<td>Window border.
</td>
</tr>
<tr VALIGN=top>
<td>maximize</td>
<td> Maximize button (includes title bar).
</td>
</tr>
<tr VALIGN=top>
<td>minimize</td>
<td> Minimize button (includes title bar).
</td>
</tr>
<tr VALIGN=top>
<td>none</td>
<td>No decorations.
</td>
</tr>
<tr VALIGN=top>
<td>resizeh</td>
<td> Border resize handles (includes border).
</td>
</tr>
<tr VALIGN=top>
<td>menu</td>
<td> Window menu button (includes title bar).
</td>
</tr>
<tr VALIGN=top>
<td>title</td>
<td>Title bar (includes border).
</td>
</tr>
</table>
</dl>
<p> Examples: <i>Mwm*XClock.clientDecoration: -resizeh -maximize</i> This removes the resize handles and maximize button from XClock windows. <i>Mwm*XClock.clientDecoration: menu minimize border</i> This does the same thing as above. Note that either <i>menu</i> or <i>minimize</i> implies <i>title</i>.</p>
<dl>
<dt><i>clientFunctions</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>ClientFunctions</i>)</p>
<dd> This resource is used to indicate which <code>mwm</code> functions are applicable (or not applicable) to the client window. The value for the resource is a list of functions. If the first function in the list has a minus sign in front of it, then <code>mwm</code> starts with all functions and subtracts from that set. If the first function in the list has a plus sign in front of it, then <code>mwm</code> starts with no functions and builds up a list. Each function in the list must be preceded by the appropriate plus or minus sign and separated from the next function by a space.</p>
<dt>
<dd> An application can also specify which functions <code>mwm</code> should apply to its windows. If it does so, <code>mwm</code> applies only those functions indicated by both the application and the <i>clientFunctions</i> resource. Otherwise, <code>mwm</code> applies the functions indicated by the <i>clientFunctions</i> resource. For more information see the description of <code>XmNmwmFunctions</code> on the <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3) reference page.</dl>
<p> The following table lists the functions available for this resource: </p>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td>all</td>
<td> Include all functions (default value).
</td>
</tr>
<tr VALIGN=top>
<td>none</td>
<td>No functions.
</td>
</tr>
<tr VALIGN=top>
<td>resize</td>
<td>f.resize-.
</td>
</tr>
<tr VALIGN=top>
<td>move</td>
<td>f.move-.
</td>
</tr>
<tr VALIGN=top>
<td>minimize</td>
<td>f.minimize-.
</td>
</tr>
<tr VALIGN=top>
<td>maximize</td>
<td>f.maximize-.
</td>
</tr>
<tr VALIGN=top>
<td>close</td>
<td>f.kill-.
</td>
</tr>
</table>
<p> -See <code><a href="/docs/linux/man/4-mwmrc/">mwmrc</a></code>(4).</p>
<dl>
<dt><i>focusAutoRaise</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>FocusAutoRaise</i>)</p>
<dd> When the value of this resource is True, clients are raised when they get the keyboard input focus. If the value is False, the stacking of windows on the display is not changed when a window gets the keyboard input focus. The default value is True when the keyboardFocusPolicy is explicit and False when the keyboardFocusPolicy is pointer.</p>
<dt><i>iconImage</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>IconImage</i>)</p>
<dd> This resource can be used to specify an icon image for a client (for example, &quot;Mwm*myclock*iconImage&quot;). The resource value is a pathname for a pixmap or bitmap file. The value of the (client specific) <i>useClientIcon</i> resource is used to determine whether or not user supplied icon images are used instead of client supplied icon images. The default value is to display a built-in window manager icon image.</p>
<dt><i>iconImageBackground</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Background</i>)</p>
<dd> This resource specifies the background color of the icon image that is displayed in the image part of an icon. The default value of this resource is the icon background color (that is, specified by &quot;Mwm*background or Mwm*icon*background).</p>
<dt><i>iconImageBottomShadowColor</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Foreground</i>)</p>
<dd> This resource specifies the bottom shadow color of the icon image that is displayed in the image part of an icon. The default value of this resource is the icon bottom shadow color (that is, specified by Mwm*icon*bottomShadowColor).</p>
<dt><i>iconImageBottomShadowPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>BottomShadowPixmap</i>)</p>
<dd> This resource specifies the bottom shadow Pixmap of the icon image that is displayed in the image part of an icon. The default value of this resource is the icon bottom shadow Pixmap (that is, specified by Mwm*icon*bottomShadowPixmap).</p>
<dt><i>iconImageForeground</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Foreground</i>)</p>
<dd> This resource specifies the foreground color of the icon image that is displayed in the image part of an icon. The default value of this resource varies depending on the icon background.</p>
<dt><i>iconImageTopShadowColor</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Background</i>)</p>
<dd> This resource specifies the top shadow color of the icon image that is displayed in the image part of an icon. The default value of this resource is the icon top shadow color (that is, specified by Mwm*icon*topShadowColor).</p>
<dt><i>iconImageTopShadowPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>TopShadowPixmap</i>)</p>
<dd> This resource specifies the top shadow Pixmap of the icon image that is displayed in the image part of an icon. The default value of this resource is the icon top shadow pixmap (that is, specified by Mwm*icon*topShadowPixmap).</p>
<dt><i>matteBackground</i>&nbsp;<wbr>&nbsp;<wbr>(class&nbsp;<wbr> <i>Background</i>)</p>
<dd> This resource specifies the background color of the matte, when <i>matteWidth</i> is positive. The default value of this resource is the client background color (that is, specified by &quot;Mwm*background or Mwm*client*background).</p>
<dt><i>matteBottomShadowColor</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Foreground</i>)</p>
<dd> This resource specifies the bottom shadow color of the matte, when <i>matteWidth</i> is positive. The default value of this resource is the client bottom shadow color (that is, specified by Mwm*bottomShadowColor or Mwm*client*bottomShadowColor).</p>
<dt><i>matteBottomShadowPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>BottomShadowPixmap</i>)</p>
<dd> This resource specifies the bottom shadow Pixmap of the matte, when <i>matteWidth</i> is positive. The default value of this resource is the client bottom shadow pixmap (that is, specified by Mwm*bottomShadowPixmap or Mwm*client*bottomShadowPixmap).</p>
<dt><i>matteForeground</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Foreground</i>)</p>
<dd> This resource specifies the foreground color of the matte, when <i>matteWidth</i> is positive. The default value of this resource is the client foreground color (that is, specified by Mwm*foreground or Mwm*client*foreground).</p>
<dt><i>matteTopShadowColor</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>Background</i>)</p>
<dd> This resource specifies the top shadow color of the matte, when <i>matteWidth</i> is positive. The default value of this resource is the client top shadow color (that is, specified by Mwm*topShadowColor or Mwm*client*topShadowColor).</p>
<dt><i>matteTopShadowPixmap</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>TopShadowPixmap</i>)</p>
<dd> This resource specifies the top shadow pixmap of the matte, when <i>matteWidth</i> is positive. The default value of this resource is the client top shadow pixmap (that is, specified by &quot;Mwm*topShadowPixmap or Mwm*client*topShadowPixmap).</p>
<dt><i>matteWidth</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>MatteWidth</i>)</p>
<dd> This resource specifies the width of the optional matte. The default value is 0, which effectively disables the matte.</p>
<dt><i>maximumClientSize</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>MaximumClientSize</i>)</p>
<dd> This resource is either a size specification or a direction that indicates how a client window is to be maximized. The resource value can be specified as a size specification <code>width</code><i>x</i><code>height</code>. The width and height are interpreted in the units that the client uses (for example, for terminal emulators this is generally characters). Alternately, &quot;vertical&quot; or &quot;horizontal&quot; can be specified to indicate the direction in which the client maximizes.</p>
<dt>
<dd> If this resource is not specified, the maximum size from the <i>WM_NORMAL_HINTS</i> property is used if set. Otherwise the default value is the size where the client window with window management borders fills the screen. When the maximum client size is not determined by the <i>maximumClientSize</i> resource, the <i>maximumMaximumSize</i> resource value is used as a constraint on the maximum size.</p>
<dt><i>useClientIcon</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>UseClientIcon</i>)</p>
<dd> If the value given for this resource is True, a client-supplied icon image takes precedence over a user-supplied icon image. The default value is True, giving the client-supplied icon image higher precedence than the user-supplied icon image.</p>
<dt><i>usePPosition</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>UsePPosition</i>)</p>
<dd> This resource specifies whether Mwm honors program specified position <code>PPosition</code> specified in the <i>WM_NORMAL_HINTS</i> property in the absence of an user specified position. Setting this resource to on, causes <code>mwm</code> to always honor program specified position. Setting this resource to off, causes <code>mwm</code> to always ignore program specified position. Setting this resource to the default value of nonzero cause <code>mwm</code> to honor program specified position other than (0,0).</p>
<dt><i>windowMenu</i>&nbsp;<wbr>(class&nbsp;<wbr> <i>WindowMenu</i>)</p>
<dd> This resource indicates the name of the menu pane that is posted when the window menu is popped up (usually by pressing button 1 on the window menu button on the client window frame). Menu panes are specified in the <code>mwm</code> resource description file. Window menus can be customized on a client class basis by creating custom menus in your <code>mwmrc</code> file (see <code><a href="/docs/linux/man/4-mwmrc/">mwmrc</a></code>(4) and specifying resources to activate the custom menus. The resources have the form <i>Mwm*</i> <code>client_name_or_class</code><i>*windowMenu</i>. The default value of this resource is DefaultWindowMenu.</dl>
<h3>Resource Description File</h3>
<p> The <code>mwm</code> resource description file is a supplementary resource file that contains resource descriptions that are referred to by entries in the resource manager property (see <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1) and the defaults files (<code>.Xdefaults</code>, <code>app-defaults/Mwm</code> ). It contains descriptions of resources that are to be used by <code>mwm</code>, and that cannot be easily encoded in the defaults files (a bitmap file is an analogous type of resource description file). A particular <code>mwm</code> resource description file can be selected using the <i>configFile</i> resource. </p>
<p> The following types of resources can be described in the <code>mwm</code> resource description file:</p>
<dl>
<dt><i>Buttons</i></p>
<dd> Window manager functions can be bound (associated) with button events.</p>
<dt><i>Keys</i></p>
<dd> Window manager functions can be bound (associated) with key press events.</p>
<dt><i>Menus</i></p>
<dd> Menu panes can be used for the window menu and other menus posted with key bindings and button bindings.</p>
<dt>
<dd> The <code>mwm</code> resource description file is described in <code><a href="/docs/linux/man/4-mwmrc/">mwmrc</a></code>(4).</dl>
<h3>Environment</h3>
<p> The <code>mwm</code> window manager uses the environment variable <code>HOME</code> specifying the user&#8217;s home directory. </p>
<p> The <code>mwm</code> window manager uses the environment variable <code>LANG</code> specifying the user&#8217;s choice of language for the <code>mwm</code> message catalog and the <code>mwm</code> resource description file. </p>
<p> The <code>mwm</code> window uses the environment variable <code>XFILESEARCHPATH</code>, <code>XUSERFILESEARCHPATH</code>, <code>XAPPLRESDIR</code>, <code>XENVIRONMENT</code>, <code>LANG</code>, and <code>HOME</code> in determining search paths for resource defaults files. The <code>mwm</code> window manager may also us <code>XBMLANGPATH</code> to search for bitmap files. </p>
<p> The <code>mwm</code> window manager reads the <code>$HOME/.motifbind</code> file if it exists to install a virtual key bindings property on the root window. For more information on the content of the <code>.motifbind</code> file, see </p>
<p> The <code>mwm</code> window manager uses the environment variable <code>MWMSHELL</code> (or <code>SHELL</code>, <i>if</i> <code>MWMSHELL</code> is not set), specifying the shell to use when executing commands via the <code>f.exec</code> function.</p>
<h3>Files</h3>
<p> <code>/etc/X11/mwm/$LANG/system.mwmrc</code> </p>
<p> <code>/etc/X11/mwm/system.mwmrc</code> </p>
<p> <code>/usr/share/X11/app-defaults/Mwm</code> </p>
<p> <code>$HOME/Mwm</code> </p>
<p> <code>$HOME/$LANG/.mwmrc</code> </p>
<p> <code>$HOME/.mwmrc</code></p>
<h3>RELATED INFORMATION</h3>
<p> <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3), <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3), <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/3-xminstallimage/">XmInstallImage</a></code>(3), <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1). </p>
<h2>Index</h2>
