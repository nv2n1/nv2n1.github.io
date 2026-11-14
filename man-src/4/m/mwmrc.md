---
title: "mwmrc(4)"
name: "mwmrc"
section: "4"
letter: "m"
url: "/docs/linux/man/4-mwmrc/"
description: "mwmrc — the Motif Window Manager Resource Description File"
---

<p><code>mwmrc</code> &#8212; the Motif Window Manager Resource Description File</p>
<h2>Description</h2>
<p>The <code>mwmrc</code> file is a supplementary resource file that controls much of the behavior of the Motif window manager <code>mwm</code>. It contains descriptions of resources that cannot easily be written using standard X Window System, Version 11 resource syntax. The resource description file contains entries that are referred to by X resources in defaults files (for example, <code>/usr/share/X11/app-defaults/Mwm</code>) or in the <code>RESOURCE_MANAGER</code> property on the root window. For example, the resource description file enables you to specify different types of window menus; however, an X resource is used to specify which of these window menus <code>mwm</code> should use for a particular window.</p>
<h3>Location</h3>
<p>The window manager searches for one of the following resource description files, where <i>$LANG</i> is the value of the language environment on a per-user basis: </p>
<pre><tt>$HOME/$LANG/.mwmrc
$HOME/.mwmrc
/etc/X11/mwm/$LANG/system.mwmrc
/etc/X11/mwm/system.mwmrc</tt></pre>
<p>The first file found is the first used. If no file is found, a set of built-in specifications is used. A particular resource description file can be selected using the <i>configFile</i> resource. The following shows how a different resource description file can be specified from the command line: </p>
<pre><tt>/usr/bin/mwm -xrm &quot;mwm*configFile: mymwmrc&quot;</tt></pre>
<h3>Resource Types</h3>
<p>The following types of resources can be described in the mwm resource description file:</p>
<dl>
<dt><code>Buttons</code></p>
<dd>Window manager functions can be bound (associated) with button events.</p>
<dt><code>Keys</code></p>
<dd>Window manager functions can be bound (associated) with key press events.</p>
<dt><code>Menus</code></p>
<dd>Menu panes can be used for the window menu and other menus posted with key bindings and button bindings.</dl>
<h2>Mwm Resource Description File Syntax</h2>
<p>The <code>mwm</code> resource description file is a standard text file that contains items of information separated by blanks, tabs, and new lines characters. Blank lines are ignored. Items or characters can be quoted to avoid special interpretation (for example, the comment character can be quoted to prevent it from being interpreted as the comment character). A quoted item can be contained in double quotes (<code>&quot; &quot;</code>). Single characters can be quoted by preceding them by the back-slash character (<code>\</code>). If a line ends with a back-slash, the next line is considered a continuation of that line. All text from an unquoted <code>#</code> to the end of the line is regarded as a comment and is not interpreted as part of a resource description. If <code>!</code> is the first character in a line, the line is regarded as a comment.</p>
<h3>Window Manager Functions</h3>
<p>Window manager functions can be accessed with button and key bindings, and with window manager menus. Functions are indicated as part of the specifications for button and key binding sets, and menu panes. The function specification has the following syntax: </p>
<pre><tt></tt><code>function</code> = <code>function_name</code> [<code>function_args</code>]
<code>function_name</code> = <code>window manager function</code>
<code>function_args</code> = {<code>quoted_item</code> | <code>unquoted_item</code>}</pre>
<p>The following functions are supported. If a function is specified that isn&#8217;t one of the supported functions then it is interpreted by <code>mwm</code> as <code>f.nop</code>.</p>
<dl>
<dt><code>f.beep</code></p>
<dd>This function causes a beep.</p>
<dt><code>f.circle_down</code> [ <i>icon</i> | <i>window</i>]</p>
<dd>This function causes the window or icon that is on the top of the window stack to be put on the bottom of the window stack (so that it is no longer obscuring any other window or icon). This function affects only those windows and icons that are obscuring other windows and icons, or that are obscured by other windows and icons. Secondary windows (that is, transient windows) are restacked with their associated primary window. Secondary windows always stay on top of the associated primary window and there can be no other primary windows between the secondary windows and their primary window. If an <i>icon</i> function argument is specified, then the function applies only to icons. If a <i>window</i> function argument is specified then the function applies only to windows.</p>
<dt><code>f.circle_up</code> [ <i>icon</i> | <i>window</i>]</p>
<dd>This function raises the window or icon on the bottom of the window stack (so that it is not obscured by any other windows). This function affects only those windows and icons that are obscuring other windows and icons, or that are obscured by other windows and icons. Secondary windows (that is, transient windows) are restacked with their associated primary window. If an <i>icon</i> function argument is specified then the function applies only to icons. If an <i>window</i> function argument is specified then the function applies only to windows.</p>
<dt><code>f.exec</code> <code>command</code> (or <i>!</i> <code>command</code>)</p>
<dd>This function causes <i>command</i> to be executed (using the value of the <i>$MWMSHELL</i> or <i>$SHELL</i> environment variable if set; otherwise, <code>/bin/sh</code> ). The <i>!</i> notation can be used in place of the <code>f.exec</code> function name.</p>
<dt><code>f.focus_color</code></p>
<dd>This function sets the colormap focus to a client window. If this function is done in a root context, then the default colormap (setup by the X Window System for the screen where <code>mwm</code> is running) is installed and there is no specific client window colormap focus. This function is treated as <code>f.nop</code> if <i>colormapFocusPolicy</i> is not explicit.</p>
<dt><code>f.focus_key</code></p>
<dd>This function sets the keyboard input focus to a client window or icon. This function is treated as <code>f.nop</code> if <i>keyboardFocusPolicy</i> is not explicit or the function is executed in a root context.</p>
<dt><code>f.kill</code></p>
<dd>This function is used to close application windows. The actual processing that occurs depends on the protocols that the application observes. The application lists the protocols it observes in the <code>WM_PROTOCOLS</code> property on its top level window. If the application observes the <code>WM_DELETE_WINDOW</code> protocol, it is sent a message that requests the window be deleted. If the application observes both <code>WM_DELETE_WINDOW</code> and <code>WM_SAVE_YOURSELF</code>, it is sent one message requesting the window be deleted and another message advising it to save its state. If the application observes only the <code>WM_SAVE_YOURSELF</code>protocol <i>,</i> it is sent a message advising it to save its state. After a delay (specified by the resource <i>quitTimeout</i>), the application&#8217;s connection to the X server is terminated. If the application observes neither of these protocols, its connection to the X server is terminated.</p>
<dt><code>f.lower</code>&nbsp;<wbr>[<i>&#8211;</i> <code>client</code> | <i>within</i>&nbsp;<wbr>| <i>freeFamily</i>]</p>
<dd>This function lowers a primary window to the bottom of the global window stack (where it obscures no other window) and lowers the secondary window (transient window or dialog box) within the client family. The arguments to this function are mutually exclusive. The <i>client</i> argument indicates the name or class of a client to lower. The name or class of a client appears in the <code>WM_CLASS</code> property on the client&#8217;s top-level window. If the <i>client</i> argument is not specified, the context that the function was invoked in indicates the window or icon to lower. Specifying <i>within</i> lowers the secondary window within the family (staying above the parent) but does not lower the client family in the global window stack. Specifying <i>freeFamily</i> lowers the window to the bottom of the global windows stack from its local family stack.</p>
<dt><code>f.maximize</code></p>
<dd>This function causes a client window to be displayed with its maximum size. Refer to the <i>maximumClientSize</i>, <i>maximumMaximumSize</i>, and <i>limitResize</i> resources in <code><a href="/docs/linux/man/1-mwm/">mwm</a></code>(1).</p>
<dt><code>f.menu</code> <i>menu_name</i></p>
<dd>This function associates a cascading (pull-right) menu with a menu pane entry or a menu with a button or key binding. The <i>menu_name</i> function argument identifies the menu to be used.</p>
<dt><code>f.minimize</code></p>
<dd>This function causes a client window to be minimized (iconified). When a window is minimized with no icon box in use, and if the <i>lowerOnIconify</i> resource has the value True (the default), the icon is placed on the bottom of the window stack (such that it obscures no other window). If an icon box is used, then the client&#8217;s icon changes to its iconified form inside the icon box. Secondary windows (that is, transient windows) are minimized with their associated primary window. There is only one icon for a primary window and all its secondary windows.</p>
<dt><code>f.move</code></p>
<dd>This function initiates an interactive move of a client window.</p>
<dt><code>f.next_cmap</code></p>
<dd>This function installs the next colormap in the list of colormaps for the window with the colormap focus.</p>
<dt><code>f.next_key</code> [ <i>icon</i> | <i>window</i> | <i>transient</i>]</p>
<dd>This function sets the keyboard input focus to the next window/icon in the set of windows/icons managed by the window manager (the ordering of this set is based on the stacking of windows on the screen). This function is treated as <code>f.nop</code> if <code>keyboardFocusPolicy</code> is not explicit. The keyboard input focus is only moved to windows that do not have an associated secondary window that is application modal. If the <i>transient</i> argument is specified, then transient (secondary) windows are traversed (otherwise, if only <i>window</i> is specified, traversal is done only to the last focused window in a transient group). If an <i>icon</i> function argument is specified, then the function applies only to icons. If a <i>window</i> function argument is specified, then the function applies only to windows.</p>
<dt><code>f.nop</code></p>
<dd>This function does nothing.</p>
<dt><code>f.normalize</code></p>
<dd>This function causes a client window to be displayed with its normal size. Secondary windows (that is, transient windows) are placed in their normal state along with their associated primary window.</p>
<dt><code>f.normalize_and_raise</code></p>
<dd>This function causes a client window to be displayed with its normal size and raised to the top of the window stack. Secondary windows (that is, transient windows) are placed in their normal state along with their associated primary window.</p>
<dt><code>f.pack_icons</code></p>
<dd>This function is used to relayout icons (based on the layout policy being used) on the root window or in the icon box. In general this causes icons to be &quot;packed&quot; into the icon grid.</p>
<dt><code>f.pass_keys</code></p>
<dd>This function is used to enable/disable (toggle) processing of key bindings for window manager functions. When it disables key binding processing all keys are passed on to the window with the keyboard input focus and no window manager functions are invoked. If the <code>f.pass_keys</code> function is invoked with a key binding to disable key binding processing the same key binding can be used to enable key binding processing.</p>
<dt><code>f.post_wmenu</code></p>
<dd>This function is used to post the window menu. If a key is used to post the window menu and a window menu button is present, the window menu is automatically placed with its top-left corner at the bottom-left corner of the window menu button for the client window. If no window menu button is present, the window menu is placed at the top-left corner of the client window.</p>
<dt><code>f.prev_cmap</code></p>
<dd>This function installs the previous colormap in the list of colormaps for the window with the colormap focus.</p>
<dt><code>f.prev_key</code> [ <i>icon</i> | <i>window</i> | <i>transient</i>]</p>
<dd>This function sets the keyboard input focus to the previous window/icon in the set of windows/icons managed by the window manager (the ordering of this set is based on the stacking of windows on the screen). This function is treated as <code>f.nop</code> if <i>keyboardFocusPolicy</i> is not explicit. The keyboard input focus is only moved to windows that do not have an associated secondary window that is application modal. If the <i>transient</i> argument is specified, then transient (secondary) windows are traversed (otherwise, if only <i>window</i> is specified, traversal is done only to the last focused window in a transient group). If an <i>icon</i> function argument is specified then the function applies only to icons. If an <i>window</i> function argument is specified then the function applies only to windows.</p>
<dt><code>f.quit_mwm</code></p>
<dd>This function terminates mwm (but NOT the X window system).</p>
<dt><code>f.raise</code>&nbsp;<wbr>[<i>&#8211;</i><i>client</i> | <i>within</i> | <i>freeFamily</i>]</p>
<dd>This function raises a primary window to the top of the global window stack (where it is obscured by no other window) and raises the secondary window (transient window or dialog box) within the client family. The arguments to this function are mutually exclusive. The <i>client</i> argument indicates the name or class of a client to lower. If the <i>client</i> is not specified, the context that the function was invoked in indicates the window or icon to lower. Specifying <i>within</i> raises the secondary window within the family but does not raise the client family in the global window stack. Specifying <i>freeFamily</i> raises the window to the top of its local family stack and raises the family to the top of the global window stack.</p>
<dt><code>f.raise_lower</code>&nbsp;<wbr>[ <i>within</i> | <i>freeFamily</i>]</p>
<dd>This function raises a primary window to the top of the global window stack if it is partially obscured by another window; otherwise, it lowers the window to the bottom of the window stack. The arguments to this function are mutually exclusive. Specifying <i>within</i> raises a secondary window within the family (staying above the parent window), if it is partially obscured by another window in the application&#8217;s family; otherwise, it lowers the window to the bottom of the family stack. It has no effect on the global window stacking order. Specifying <i>freeFamily</i> raises the window to the top of its local family stack, if obscured by another window, and raises the family to the top of the global window stack; otherwise, it lowers the window to the bottom of its local family stack and lowers the family to the bottom of the global window stack.</p>
<dt><code>f.refresh</code></p>
<dd>This function causes all windows to be redrawn.</p>
<dt><code>f.refresh_win</code></p>
<dd>This function causes a client window to be redrawn.</p>
<dt><code>f.resize</code></p>
<dd>This function initiates an interactive resize of a client window.</p>
<dt><code>f.restore</code></p>
<dd>This function restores the previous state of an icon&#8217;s associated window. If a maximized window is iconified, then <code>f.restore</code> restores it to its maximized state. If a normal window is iconified, then <code>f.restore</code> restores it to its normalized state.</p>
<dt><code>f.restore_and_raise</code></p>
<dd>This function restores the previous state of an icon&#8217;s associated window and raises the window to the top of the window stack. If a maximized window is iconified, then <code>f.restore_and_raise</code> restores it to its maximized state and raises it to the top of the window stack. If a normal window is iconified, then <code>f.restore_and_raise</code> restores it to its normalized state and raises it to the top of the window stack.</p>
<dt><code>f.restart</code></p>
<dd>This function causes mwm to be restarted (effectively terminated and re-executed). Restart is necessary for <code>mwm</code> to incorporate changes in both the <code>mwmrc</code> file and X resources.</p>
<dt><code>f.screen</code>&nbsp;<wbr>[ <i>next</i> | <i>prev</i> | <i>back</i> | <i>screen_number</i>]</p>
<dd>This function causes the pointer to be warp to a specific screen number or to the <i>next</i>, <i>previous</i>, or last visited (<i>back</i>) screen. The arguments to this function are mutually exclusive. The <i>screen_number</i> argument indicates the screen number that the pointer is to be warped. Screens are numbered starting from screen 0. Specifying <i>next</i> cause the pointer to warp to the next managed screen (skipping over any unmanaged screens). Specifying <i>prev</i> cause the pointer to warp to the previous managed screen (skipping over any unmanaged screens). Specifying <i>back</i> cause the pointer to warp to the last visited screen.</p>
<dt><code>f.send_msg</code> <i>message_number</i></p>
<dd>This function sends an <code>XClientMessageEvent</code> of type <code>_MOTIF_WM_MESSAGES</code> with <i>message_type</i> set to <i>message_number</i>. The client message is sent only if <i>message_number</i> is included in the client&#8217;s <code>_MOTIF_WM_MESSAGES</code> property. A menu item label is grayed out if the menu item is used to do <code>f.send_msg</code> of a message that is not included in the client&#8217;s <code>_MOTIF_WM_MESSAGES</code> property.</p>
<dt><code>f.separator</code></p>
<dd>This function causes a menu separator to be put in the menu pane at the specified location (the label is ignored).</p>
<dt><code>f.set_behavior</code></p>
<dd>This function causes the window manager to restart with the default behavior (if a custom behavior is configured) or a custom behavior (if a default behavior is configured). By default this is bound to <i>Shift Ctrl Alt&nbsp;<wbr>&lt;Key&gt;!</i>.</p>
<dt><code>f.title</code></p>
<dd>This function inserts a title in the menu pane at the specified location.</p>
<dt><code>f.version</code></p>
<dd>This function causes the window manager to display its release version in a dialog box.</dl>
<h3>Function Constraints</h3>
<p>Each function may be constrained as to which resource types can specify the function (for example, menu pane) and also what context the function can be used in (for example, the function is done to the selected client window). Function contexts are:</p>
<dl>
<dt><i>root</i></p>
<dd>No client window or icon has been selected as an object for the function.</p>
<dt><i>window</i></p>
<dd>A client window has been selected as an object for the function. This includes the window&#8217;s title bar and frame. Some functions are applied only when the window is in its normalized state (for example, <code>f.maximize</code>) or its maximized state (for example, <code>f.normalize</code>).</p>
<dt><i>icon</i></p>
<dd>An icon has been selected as an object for the function.</dl>
<p> If a function is specified in a type of resource where it is not supported or is invoked in a context that does not apply then the function is treated as <code>f.nop</code>. The following table indicates the resource types and function contexts in which window manager functions apply. </p>
<table>
<tr VALIGN=top>
<td>Function</td>
<td>Contexts</td>
<td>Resources
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>f.beep</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.circle_down</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.circle_up</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.exec</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.focus_color</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.focus_key</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.kill</code></td>
<td>icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.lower</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.maximize</code></td>
<td>icon,window(normal)</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.menu</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.minimize</code></td>
<td>window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.move</code></td>
<td>icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.next_cmap</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.next_key</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.nop</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.normalize</code></td>
<td>icon,window(maximized)</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.normalize_and_raise</code></td>
<td>icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.pack_icons</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.pass_keys</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.post_wmenu</code></td>
<td>root,icon,window</td>
<td>button,key
</td>
</tr>
<tr VALIGN=top>
<td><code>f.prev_cmap</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.prev_key</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.quit_mwm</code></td>
<td>root</td>
<td>button,key,menu (root only)
</td>
</tr>
<tr VALIGN=top>
<td><code>f.raise</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.raise_lower</code></td>
<td>icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.refresh</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.refresh_win</code></td>
<td>window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.resize</code></td>
<td>window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.restart</code></td>
<td>root</td>
<td>button,key,menu (root only)
</td>
</tr>
<tr VALIGN=top>
<td><code>f.restore</code></td>
<td>icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.restore_and_raise</code></td>
<td>icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.screen</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.send_msg</code></td>
<td>icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.separator</code></td>
<td>root,icon,window</td>
<td>menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.set_behavior</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.title</code></td>
<td>root,icon,window</td>
<td>menu
</td>
</tr>
<tr VALIGN=top>
<td><code>f.version</code></td>
<td>root,icon,window</td>
<td>button,key,menu
</td>
</tr>
</table>
<h2>Window Manager Event Specification</h2>
<p>Events are indicated as part of the specifications for button and key binding sets, and menu panes. Button events have the following syntax: </p>
<pre><tt></tt><code>button</code> =~[<code>modifier_list</code> ]<i>&lt;</i><code>button_event_name</code> <i>&gt;</i>
<code>modifier_list</code> =~<code>modifier_name</code> { <code>modifier_name</code>}</pre>
<p>The following table indicates the values that can be used for <code>modifier_name</code>. Note that [Alt] and [Meta] can be used interchangably on some hardware. </p>
<table>
<tr VALIGN=top>
<td>Modifier</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Ctrl</td>
<td>Control Key
</td>
</tr>
<tr VALIGN=top>
<td>Shift</td>
<td>Shift Key
</td>
</tr>
<tr VALIGN=top>
<td>Alt</td>
<td>Alt Key
</td>
</tr>
<tr VALIGN=top>
<td>Meta</td>
<td>Meta Key
</td>
</tr>
<tr VALIGN=top>
<td>Mod1</td>
<td>Modifier1
</td>
</tr>
<tr VALIGN=top>
<td>Mod2</td>
<td>Modifier2
</td>
</tr>
<tr VALIGN=top>
<td>Mod3</td>
<td>Modifier3
</td>
</tr>
<tr VALIGN=top>
<td>Mod4</td>
<td>Modifier4
</td>
</tr>
<tr VALIGN=top>
<td>Mod5</td>
<td>Modifier5
</td>
</tr>
</table>
<p> Locking modifiers are ignored when processing button and key bindings. The following table lists keys that are interpreted as locking modifiers. The X server may map some of these symbols to the Mod1 &#8211; Mod5 modifier keys. These keys may or may not be available on your hardware: Key Symbol Caps Lock Shift Lock Kana Lock Num Lock Scroll Lock The following table indicates the values that can be used for <code>button_event_name</code>. </p>
<table>
<tr VALIGN=top>
<td>Button</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Btn1Down</td>
<td>Button 1 Press
</td>
</tr>
<tr VALIGN=top>
<td>Btn1Up</td>
<td>Button 1 Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn1Click</td>
<td>Button 1 Press and Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn1Click2</td>
<td>Button 1 Double Click
</td>
</tr>
<tr VALIGN=top>
<td>Btn2Down</td>
<td>Button 2 Press
</td>
</tr>
<tr VALIGN=top>
<td>Btn2Up</td>
<td>Button 2 Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn2Click</td>
<td>Button 2 Press and Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn2Click2</td>
<td>Button 2 Double Click
</td>
</tr>
<tr VALIGN=top>
<td>Btn3Down</td>
<td>Button 3 Press
</td>
</tr>
<tr VALIGN=top>
<td>Btn3Up</td>
<td>Button 3 Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn3Click</td>
<td>Button 3 Press and Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn3Click2</td>
<td>Button 3 Double Click
</td>
</tr>
<tr VALIGN=top>
<td>Btn4Down</td>
<td>Button 4 Press
</td>
</tr>
<tr VALIGN=top>
<td>Btn4Up</td>
<td>Button 4 Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn4Click</td>
<td>Button 4 Press and Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn4Click2</td>
<td>Button 4 Double Click
</td>
</tr>
<tr VALIGN=top>
<td>Btn5Down</td>
<td>Button 5 Press
</td>
</tr>
<tr VALIGN=top>
<td>Btn5Up</td>
<td>Button 5 Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn5Click</td>
<td>Button 5 Press and Release
</td>
</tr>
<tr VALIGN=top>
<td>Btn5Click2</td>
<td>Button 5 Double Click
</td>
</tr>
</table>
<p> Key events that are used by the window manager for menu mnemonics and for binding to window manager functions are single key presses; key releases are ignored. Key events have the following syntax: </p>
<pre><tt></tt><code>key</code> =~[<code>modifier_list</code>] <code>&lt;Key&gt;</code><code>key_name</code>
<code>modifier_list</code> =~<code>modifier_name</code> { <code>modifier_name</code>}</pre>
<p>All modifiers specified are interpreted as being exclusive (this means that only the specified modifiers can be present when the key event occurs). Modifiers for keys are the same as those that apply to buttons. The <code>key_name</code> is an X11 keysym name. Keysym names can be found in the <code>keysymdef.h</code> file (remove the <code>XK_</code> prefix).</p>
<h2>Button Bindings</h2>
<p>The <code>buttonBindings</code> resource value is the name of a set of button bindings that are used to configure window manager behavior. A window manager function can be done when a button press occurs with the pointer over a framed client window, an icon or the root window. The context for indicating where the button press applies is also the context for invoking the window manager function when the button press is done (significant for functions that are context sensitive). The button binding syntax is </p>
<pre><tt></tt><i>Buttons</i> <code>bindings_set_name</code>
<i>{</i>
 <code>button</code> <code>context</code> <code>function</code>
 <code>button</code> <code>context</code> <code>function</code>
 ...
 <code>button</code> <code>context</code> <code>function</code>
<i>}</i></pre>
<p>The syntax for the <code>context</code> specification is: <code>context</code> = <code>object</code>[<i>|</i> <code>context</code>] <code>object</code> = <i>root</i> | <i>icon</i> | <i>window</i> | <i>title</i> | <i>frame</i> | <i>border</i> | <i>app</i> The context specification indicates where the pointer must be for the button binding to be effective. For example, a context of <i>window</i> indicates that the pointer must be over a client window or window management frame for the button binding to be effective. The <i>frame</i> context is for the window management frame around a client window (including the border and titlebar), the <i>border</i> context is for the border part of the window management frame (not including the titlebar), the <i>title</i> context is for the title area of the window management frame, and the <i>app</i> context is for the application window (not including the window management frame). If an <code>f.nop</code> function is specified for a button binding, the button binding is not done.</p>
<h2>Key Bindings</h2>
<p>The <code>keyBindings</code> resource value is the name of a set of key bindings that are used to configure window manager behavior. A window manager function can be done when a particular key is pressed. The context in which the key binding applies is indicated in the key binding specification. The valid contexts are the same as those that apply to button bindings. The key binding syntax is: </p>
<pre><tt></tt><i>Keys</i> <code>bindings_set_name</code>
<i>{</i>
 <code>key</code> <code>context</code> <code>function</code>
 <code>key</code> <code>context</code> <code>function</code>
 ...
 <code>key</code> <code>context</code> <code>function</code>
<i>}</i></pre>
<p>If an <code>f.nop</code> function is specified for a key binding, the key binding is not done. If an <code>f.post_wmenu</code> or <code>f.menu</code> function is bound to a key, <code>mwm</code> automatically uses the same key for removing the menu from the screen after it has been popped up. The <code>context</code> specification syntax is the same as for button bindings with one addition. The context <i>ifkey</i> may be specified for binding keys that may not be available on all displays. If the key is not available and if <i>ifkey</i> is in the context, then reporting of the error message to the error log is suppressed. This feature is useful for networked, heterogeneous environments. For key bindings, the <i>frame</i>, <i>title</i>, <i>border</i>, and <i>app</i> contexts are equivalent to the <i>window</i> context. The context for a key event is the window or icon that has the keyboard input focus (<i>root</i> if no window or icon has the keyboard input focus).</p>
<h2>Menu Panes</h2>
<p>Menus can be popped up using the <code>f.post_wmenu</code> and <code>f.menu</code> window manager functions. The context for window manager functions that are done from a menu is <i>root</i>, <i>icon</i> or <i>window</i> depending on how the menu was popped up. In the case of the <i>window</i> menu or menus popped up with a key binding, the location of the keyboard input focus indicates the context. For menus popped up using a button binding, the context of the button binding is the context of the menu. The menu pane specification syntax is: </p>
<pre><tt></tt><i>Menu</i> <code>menu_name</code>
<i>{</i>
 <code>label</code> [<code>mnemonic</code>] [<code>accelerator</code> ] <code>function</code>
 <code>label</code> [<code>mnemonic</code>] [<code>accelerator</code> ] <code>function</code>
 ...
 <code>label</code> [<code>mnemonic</code>] [<code>accelerator</code> ] <code>function</code>
<i>}</i></pre>
<p>Each line in the <i>Menu</i> specification identifies the label for a menu item and the function to be done if the menu item is selected. Optionally a menu button mnemonic and a menu button keyboard accelerator may be specified. Mnemonics are functional only when the menu is posted and keyboard traversal applies. The <code>label</code> may be a string or a bitmap file. The label specification has the following syntax: </p>
<pre><tt></tt><code>label</code> = <code>text</code> | <code>bitmap_file</code>
<code>bitmap_file</code> = <i>@</i><code>file_name</code>
<code>text</code> = <code>quoted_item</code> | <code>unquoted_item</code></pre>
<p>The string encoding for labels must be compatible with the menu font that is used. Labels are greyed out for menu items that do the <code>f.nop</code> function or an invalid function or a function that doesn&#8217;t apply in the current context. A <code>mnemonic</code> specification has the following syntax: </p>
<pre><tt></tt><code>mnemonic</code> = <i>_</i> <code>character</code></pre>
<p>The first matching <code>character</code> in the label is underlined. If there is no matching <code>character</code> in the label, no mnemonic is registered with the window manager for that label. Although the <code>character</code> must exactly match a character in the label, the mnemonic does not execute if any modifier (such as Shift) is pressed with the character key. The <code>accelerator</code> specification is a key event specification with the same syntax as is used for key bindings to window manager functions.</p>
<h2>Including Files</h2>
<p>You may include other files into your mwmrc file by using the <i>include</i> construct. For example, </p>
<pre><tt>INCLUDE
{
 /usr/local/shared/mwm.menus
 /home/kmt/personal/my.bindings
}</tt></pre>
<p>causes the files named to be read in and interpreted in order as an additional part of the mwmrc file. <i>Include</i> is a top-level construct. It cannot be nested inside another construct.</p>
<h2>Warnings</h2>
<p>Errors that occur during the processing of the resource description file are recorded in: <code>$HOME/.mwm/errorlog</code>. Be sure to check this file if the appearance or behavior of <code>mwm</code> is not what you expect.</p>
<h2>Files</h2>
<pre><code>$HOME/$LANG/.mwmrc
$HOME/.mwmrc
/etc/X11/mwm/$LANG/system.mwmrc
/etc/X11/mwm/system.mwmrc</code></pre>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/1-mwm/">mwm</a></code>(1), <code><a href="/docs/linux/man/1-x/">X</a></code>(1).</p>
