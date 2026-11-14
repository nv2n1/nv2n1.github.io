---
title: "fluxbox-keys(5)"
name: "fluxbox-keys"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fluxbox-keys/"
description: "fluxbox-keys – keyboard shortcuts configuration for"
---

<p>fluxbox-keys &#8211; keyboard shortcuts configuration for </p>
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</p>
<h2>Synopsis</h2>
<p>~/.fluxbox/keys</p>
<h2>Syntax</h2>
<p>Variable parameters are shown in emphasis: <i>argument</i> </p>
<p> Optional parameters are shown in square brackets: [<i>argument</i>] </p>
<p> All other characters shown are required verbatim. Whitespace is required where shown, but it is fine to add more whitespace.</p>
<h2>Description</h2>
<p>The keys file defines the keyboard shortcuts for <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i>. </p>
<p> You can customize fluxbox&#8217;s key handling through the ~/.fluxbox/keys file. The file consists of lines of the basic format: </p>
<p> <code>[</code><i>modifiers</i><code>] </code><i>key</i><code> :&#8217;command&#8217; [</code><i>arguments</i><i>&#8230;</i><code>]</code> </p>
<p> The space between the <i>key</i> and the <code>:</code> before the <i>command</i> is mandatory. </p>
<p> All modifiers and commands are case-insensitive. Some command arguments (especially those that will be passed to the shell) are case-sensitive. Some key names are case-sensitive. </p>
<p> Lines beginning with a <i>#</i> or <i>!</i> are considered comments and are unread by fluxbox. </p>
<p> You will need to &#8220;reload&#8221; fluxbox after editing the keys file so it picks up your change.</p>
<h2>Modifiers</h2>
<p>You can get a list of possible modifiers by calling &#8216;xmodmap -pm&#8217;. This also shows you to which keys the modifiers are mapped, but the following modifiers are most commonly used: </p>
<p> <code>Shift Control Mod1 Mod4</code> </p>
<p> where <code>Mod1</code> is the Alt key on the PC keyboard and <code>Mod4</code> is usually a key branded with a familiar company logo. </p>
<p> There are also some special modifiers that refer to mouse button events</p>
<dl>
<dd><code>OnDesktop</code></p>
<dl>
<dd>The mouse cursor is over the desktop (root window), and not any window.</dl>
<p> <code>OnToolbar</code></p>
<dl>
<dd>The mouse cursor is over the toolbar (which is normally at the bottom of the screen).</dl>
<p> <code>OnWindow</code></p>
<dl>
<dd>The mouse cursor is over a window.</dl>
<p> <code>OnTitlebar</code></p>
<dl>
<dd>The mouse cursor is over a window&#8217;s titlebar.</dl>
<p> <code>OnTab</code></p>
<dl>
<dd>The mouse cursor is over a tab.</dl>
<p> <code>Double</code></p>
<dl>
<dd>Limits this action to double-clicks only.</dl>
</dl>
<h3>Combining Modifiers</h3>
<p>To combine two or more modifiers, just list them (space-delimited) in any order.</p>
<h2>Keys</h2>
<p>You may specify a key by its key name (for example, <code>a</code> or <code>space</code>) or by its numeric keycode (for example, <code>38</code> or <code>0xf3</code>). </p>
<p> If you don&#8217;t know the name of a key, you can run <code><a href="/docs/linux/man/1-xev/">xev</a>(1)</code> in a terminal, push the key, and see the name in the output. If you have some &quot;special&quot; keys that do not produce a key name in the output of <code><a href="/docs/linux/man/1-xev/">xev</a>(1)</code>, you can just use the keycode (NOT the keysym!) in your keys file. </p>
<p> Commands can also be bound to mouse events (<i>N</i> denotes the number of the button, eg. <i>1</i> is the primary button, <i>4</i>/<i>5</i> are the wheel buttons): </p>
<p> <code>MouseN</code></p>
<dl>
<dd>The mouse button <i>N</i> is pressed down and held.</dl>
<p> <code>ClickN</code></p>
<dl>
<dd>The mouse button <i>N</i> is clicked (pressed and released with no movement in between)</dl>
<p> <code>MoveN</code></p>
<dl>
<dd>The mouse button <i>N</i> is currently held, the bound action is triggered as often as the mouse moves.</dl>
<p> There are some special &quot;keys&quot; that let you bind events to non-keyboard events: </p>
<p> <code>ChangeWorkspace</code></p>
<dl>
<dd>Fires when the workspace changes. This can be used to change backgrounds or do anything else you like when you switch to a new workspace. See the <code>EXAMPLES</code> below for one idea.</dl>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font> </p>
<p> Use caution with this event! For example, do NOT bind this to any action that changes your current workspace. If you break your fluxbox with this feature, you get to keep the pieces. </p>
</dl>
<h2>Chaining</h2>
<p>Key bindings can be chained in a fashion similar to Emacs key bindings using the syntax: </p>
<p> <i>modifiers-1</i> <i>key-1</i> <i>modifiers-2</i> <i>key-2</i> :&#8217;command&#8217; [<i>arguments &#8230;</i>]* </p>
<p> To abort a chained command part-way through typing it, press the &lt;ESC&gt; key. </p>
<p> <code>To Bind CTRL+C CTRL+X (Which means, press CTRL+C then CTRL+X) to quit fluxbox</code>. </p>
<dl>
<dd>
<pre>Control c Control x :Quit</pre>
</dl>
<h2>Keymodes</h2>
<p>A specific set of key mappings can be activated and de-activated on-the-fly using what are called keymodes. The syntax to define a mapping in a keymode is: </p>
<p> <i>keymode</i><code>: </code><i>modifiers</i><i>key</i><code> :&#8217;command&#8217; [</code><i>arguments</i><i>&#8230;</i><code>]</code> </p>
<p> Where <i>keymode</i> is any alpha-numeric string name. </p>
<p> When this keymode is activated (see the <code>KeyMode</code> command below), all bindings prefaced by that keymode name become active (and all other keybindings will be deactivated) until the keymode changes again.</p>
<h2>Commands</h2>
<p>Some commands have multiple names which are shown below as</p>
<dl>
<dd>CMD1 | CMD2</dl>
<p> Related commands have been grouped below as</p>
<dl>
<dd>CMD1 / CMD2</dl>
<p> The commands are broken up into sections as follows</p>
<dl>
<dd>
<dl>
<dd>&bull; Mouse Commands</dl>
<dl>
<dd>&bull; Window Commands</dl>
<dl>
<dd>&bull; Workspace Commands</dl>
<dl>
<dd>&bull; Menu Commands</dl>
<dl>
<dd>&bull; Window Manager Commands</dl>
<dl>
<dd>&bull; Special Commands</dl>
</dl>
<h3>Mouse Commands</h3>
<p>These commands may only be bound to mouse buttons (plus modifiers), not keystrokes. In all cases, the action finishes when the mouse button is released. </p>
<p> <code>StartMoving</code></p>
<dl>
<dd>Start dragging to move the window.</dl>
<p> <code>StartResizing</code> [<i>corner</i>]</p>
<dl>
<dd>Start dragging to resize the window as if you had grabbed the window at the specified <i>corner</i>. </p>
<p> By default <i>corner</i> is <code>BottomRight</code>, but may be overridden with one of:</p>
<dl>
<dd><code>NearestCorner NearestEdge NearestCornerOrEdge Center TopLeft Top TopRight Left Right BottomLeft Bottom BottomRight</code></dl>
<p> If <code>NearestCornerOrEdge</code> is specified the size of the corner can also be specified to be the larger of one or two following numbers: [<i>pixel-size</i> [<i>percent-size</i>]] or <i>percent-size</i>%, where <i>percent-size</i> is the percentage of half the window width or height. If no size is given, it defaults to 50 pixels and 30%.</dl>
<p> <code>StartTabbing</code></p>
<dl>
<dd>Start dragging to add this window to another&#8217;s tabgroup.</dl>
<p> <code>ActivateTab</code></p>
<dl>
<dd>Activates the tab underneath the mouse.</dl>
<h3>Window Commands</h3>
<p>These commands ordinarily affect only the currently focused window. The <code>OnWindow</code> modifier and <code>ForEach</code> command may affect the window that is used. </p>
<p> <code>Minimize</code> | <code>MinimizeWindow</code> | <code>Iconify</code></p>
<dl>
<dd>Minimize the current window, equivalent to the window button.</dl>
<p> <code>Maximize</code> | <code>MaximizeWindow</code></p>
<dl>
<dd>Maximize the current window, equivalent to the window button.</dl>
<p> <code>MaximizeHorizontal</code> / <code>MaximizeVertical</code></p>
<dl>
<dd>Maximize the current window in one direction only, leaving the other dimension unchanged.</dl>
<p> <code>Fullscreen</code></p>
<dl>
<dd>Resize the window&#8217;s content to fit the whole screen, without any window decoration.</dl>
<p> <code>Raise</code> / <code>Lower</code></p>
<dl>
<dd>Reorder this window to the top or bottom of the window stack, within its current layer. See <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i> for a discussion of layers.</dl>
<p> <code>RaiseLayer</code> / <code>LowerLayer</code> [<i>offset</i>]</p>
<dl>
<dd>Raise the window up to the layer above, or lower it to the layer below. See <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i> for a discussion of layers.</dl>
<p> <code>SetLayer</code> <i>layer</i></p>
<dl>
<dd>Move the window to the specified layer. <i>layer</i> should be one of <code>AboveDock</code>, <code>Dock</code>, <code>Top</code>, <code>Normal</code>, <code>Bottom</code>, <code>Desktop</code>. See <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i> for a discussion of layers.</dl>
<p> <code>Close</code></p>
<dl>
<dd>Close the current window, equivalent to the window button.</dl>
<p> <code>Kill</code> | <code>KillWindow</code></p>
<dl>
<dd>Close a window that&#8217;s not responding to <code>Close</code>, like using <code><a href="/docs/linux/man/1-xkill/">xkill</a>(1)</code>.</dl>
<p> <code>Shade</code> | <code>ShadeWindow</code></p>
<dl>
<dd>Toggle the <code>shaded</code> state of the current window, equivalent to the window button. A <code>shaded</code> window appears as only the title bar.</dl>
<p> <code>ShadeOn</code> / <code>ShadeOff</code></p>
<dl>
<dd>Set the <code>shaded</code> state of the window to On / Off.</dl>
<p> <code>Stick</code> | <code>StickWindow</code></p>
<dl>
<dd>Toggle the <code>sticky</code> state of the current window, equivalent to the window button. A <code>sticky</code> window is visible on all workspaces.</dl>
<p> <code>SetDecor</code> <i>decor</i></p>
<dl>
<dd>Sets which window decorations will be shown. <i>decor</i> has the same format as the &#8216;[Deco]&#8217; parameter in the apps file. See <i><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</i> for more info.</dl>
<p> <code>ToggleDecor</code></p>
<dl>
<dd>Toggles the presence of the window decorations (title bar, window buttons, and resize bar).</dl>
<p> <code>NextTab</code> / <code>PrevTab</code></p>
<dl>
<dd>Cycle to the next / previous tab in the current tab group.</dl>
<p> <code>Tab</code> <i>number</i></p>
<dl>
<dd>Cycle to the given tab in the current tab group, where <code>1</code> is the first tab. A negative <i>number</i> counts from the end of the tab group (<code>-1</code> is the last tab, <code>-2</code> is the next-to-last, etc.).</dl>
<p> <code>MoveTabRight</code> / <code>MoveTabLeft</code></p>
<dl>
<dd>Reorder the tabs in the current tab group, swapping the current tab with the one to the right / left.</dl>
<p> <code>DetachClient</code></p>
<dl>
<dd>Remove the current tab from the tab group, placing it in its own window.</dl>
<p> <code>ResizeTo</code> <i>width[%]</i> <i>height[%]</i></p>
<dl>
<dd>Resizes the window to the given width and height. If the value is given in percent, then the window size will be based on the current screen&#8217;s size.</dl>
<p> <code>Resize</code> <i>delta-width[%]</i> <i>delta-height[%]</i></p>
<dl>
<dd>Resizes the window relative to the current width and height. If the value is given in percent, then the window size will be based on the current window&#8217;s size.</dl>
<p> <code>ResizeHorizontal</code> <i>delta-width[%]</i> / <code>ResizeVertical</code> <i>delta-height[%]</i></p>
<dl>
<dd>Resizes the window in one dimension only. If the value is given in percent, then the window size will be based on the current window&#8217;s size.</dl>
<p> <code>MoveTo</code> <i>x[%]</i> <i>y[%]</i> [<i>anchor</i>]</p>
<dl>
<dd>Moves the window to the given coordinates, given in pixels or relatively to the current screen size if % is specified after the value. </p>
<p> If either <i>x</i> or <i>y</i> is set to <code>\</code>*, that coordinate will be ignored, and the movement will only take place in one dimension. </p>
<p> The default <i>anchor</i> is the upper left corner, but this may be overridden with one of:</p>
<dl>
<dd><code>TopLeft Left BottomLeft Top Center Bottom TopRight Right BottomRight</code></dl>
</dl>
<p> <code>Move</code> <i>delta-x</i> <i>delta-y</i></p>
<dl>
<dd>Moves the window relative to its current position. Positive numbers refer to right and down, and negative to left and up, respectively.</dl>
<p> <code>MoveRight</code> <i>d</i> / <code>MoveLeft</code> <i>d</i> / <code>MoveUp</code> <i>d</i> / <code>MoveDown</code> <i>d</i></p>
<dl>
<dd>Moves the window relative to its current position by the number of pixels specified in <i>d</i>. If the number is negative, it moves in the opposite direction.</dl>
<p> <code>TakeToWorkspace</code> <i>workspace</i> / <code>SendToWorkspace</code> <i>workspace</i></p>
<dl>
<dd>Sends you along with the current window to the selected workspace. SendToWorkspace just sends the window. The first workspace is number <code>1</code>, not 0.</dl>
<p> <code>TakeToNextWorkspace</code> [<i>offset</i>] / <code>TakeToPrevWorkspace</code> [<i>offset</i>]</p>
<dl>
<dd>Sends you along with the current window to the next or previous workspace. If you set <i>offset</i> to a value greater than the default of <code>1</code>, it will move you that number of workspaces ahead or behind. If you go beyond the end of the currently defined workspaces, it will wrap around to the other end automatically.</dl>
<p> <code>SendToNextWorkspace</code> [<i>offset</i>] / <code>SendToPrevWorkspace</code> [<i>offset</i>]</p>
<dl>
<dd>Identical to the &quot;TakeTo&#8230;&quot; commands, but again this sends only the window, and does not move you away from your current workspace.</dl>
<p> <code>SetAlpha</code> [<i>alpha</i> [<i>unfocused-alpha</i>]]</p>
<dl>
<dd>Sets the alpha value of a window. </p>
<p> Putting a <code>+</code> or <code>&#8211;</code> in front of the value adds or subtracts from the current value. A plain integer sets the value explicitly. </p>
<p> no arguments</p>
<dl>
<dd>Resets both focused and unfocused settings to default opacity.</dl>
<p> one argument</p>
<dl>
<dd>Changes both focused and unfocused alpha settings.</dl>
<p> two arguments</p>
<dl>
<dd>First value becomes the focused alpha, second becomes the unfocused alpha value.</dl>
</dl>
<p> <code>SetHead</code> <i>number</i></p>
<dl>
<dd>Moves the window to the given display head. Only available when fluxbox has been compiled with Xinerama support.</dl>
<p> <code>SendToNextHead</code> [<i>offset</i>] / <code>SendToPrevHead</code> [<i>offset</i>]</p>
<dl>
<dd>Sends the current window to the next/previous display head. If you specify an <i>offset</i> greater than <code>1</code>, it will move the window that many heads. If this takes the window beyond the total number of heads, it will wrap around to the beginning.</dl>
<p> <code>SetXProp</code> <i>PROP=value</i></p>
<dl>
<dd>Sets the xproperty <i>PROP</i> of the current window to <i>value</i>. Delete the content of <i>PROP</i> by using <i>PROP=</i>.</dl>
<h3>Workspace Commands</h3>
<p>These commands affect the entire workspace (or &quot;desktop&quot; as it is sometimes called). </p>
<p> <code>AddWorkspace</code> / <code>RemoveLastWorkspace</code></p>
<dl>
<dd>Adds or removes a workspace from the end of the list of workspaces.</dl>
<p> <code>NextWorkspace</code> [<i>n</i>] / <code>PrevWorkspace</code> [<i>n</i>] / <code>RightWorkspace</code> [<i>n</i>] / <code>LeftWorkspace</code> [<i>n</i>]</p>
<dl>
<dd>Switch to the Next / Previous workspace. All versions accept an offset value <i>n</i>, which defaults to <code>1</code> and refers to the number of workspaces to move at one time. {Next,Prev}Workspace wrap around when going past the last workspace, whereas {Right,Left}Workspace do not.</dl>
<p> <code>Workspace</code> <i>number</i></p>
<dl>
<dd>Jumps to the given workspace <i>number</i>. The first workspace is <code>1</code>.</dl>
<p> <code>NextWindow</code> [{<i>options</i>}] [<i>pattern</i>] / <code>PrevWindow</code> [{<i>options</i>}] [<i>pattern</i>]</p>
<dl>
<dd>Focuses the next / previous window in the focus list. </p>
<p> <i>options</i> is one or more of the following, space delimited:</p>
<dl>
<dd><code>static</code></p>
<dl>
<dd>Instead of moving in order of most-recent focus, move in order of when the window was opened (or, the order shown in the iconbar).</dl>
<p> <code>groups</code></p>
<dl>
<dd>Only include the current tab in windows with multiple tabs.</dl>
<p> If <i>pattern</i> arguments are supplied, only windows that match all the patterns are considered &#8211; all others are skipped. See the section <code>CLIENT PATTERNS</code> below for more information. </p>
<p> This pair of commands has a special side-effect when the keybinding used has a modifier &#8211; It will temporarily raise the cycled window to the front so you can see it, but if you continue holding down the modifier and press the key again (For example, keep holding &quot;Alt&quot; while you tap the &quot;Tab&quot; key a few times), fluxbox will lower the window again when you move on to the next one. This allows you to preview the windows in order, but does not change the order in doing so.</dl>
</dl>
<p> <code>NextGroup</code> [{<i>options</i>}] [<i>pattern</i>] / <code>PrevGroup</code> [{<i>options</i>}] [<i>pattern</i>]</p>
<dl>
<dd>Equivalent to NextWindow / PrevWindow above, but with the <code>groups</code> option forced on.</dl>
<p> <code>GotoWindow</code> <i>number</i> [{<i>options</i>}] [<i>pattern</i>]</p>
<dl>
<dd>Focuses and activates the window at position <i>number</i> in the focus list. The <i>options</i> and <i>pattern</i> arguments have the same meaning as <code>NextWindow</code> above.</dl>
<p> <code>Activate</code> [<i>pattern</i>] | <code>Focus</code> [<i>pattern</i>]</p>
<dl>
<dd>With <i>pattern</i>, this is an alias for <code>GoToWindow</code> 1 <i>pattern</i>. Without, this behaves like a window command, so that OnWindow events can change the focused window.</dl>
<p> <code>Attach</code> <i>pattern</i></p>
<dl>
<dd>Combines all windows that match the <i>pattern</i> into a single tab group. See <code>CLIENT PATTERNS</code> for more about the <i>pattern</i> arguments.</dl>
<p> <code>FocusLeft</code> / <code>FocusRight</code> / <code>FocusUp</code> / <code>FocusDown</code></p>
<dl>
<dd>Focus to the next window which is located in the direction specified.</dl>
<p> <code>ArrangeWindows</code> <i>pattern</i> / <code>ArrangeWindowsVertical</code> <i>pattern</i> / <code>ArrangeWindowsHorizontal</code> <i>pattern</i></p>
<dl>
<dd>Tries to arrange all windows on the current workspace so that they overlap the least amount possible. <code>ArrangeWindowsVertical</code> prefers vertical splits (windows side by side), whereas <code>ArrangeWindowsHorizontal</code> prefers horizontal splits (windows on top of eachother). See <code>CLIENT PATTERNS</code> for more about the <i>pattern</i> arguments.</dl>
<p> <code>ArrangeWindowsStackLeft</code> <i>pattern</i> / <code>ArrangeWindowsStackRight</code> <i>pattern</i></p>
<dl>
<dd>Similar to <code>ArrangeWindows</code>, these commands arrange windows on the current workspace. The currently focussed window is used as the <i>main</i> window, and will fill half the screen, while the other windows are tiled on the other half of the screen as if they were tiled with ArrangeWindows. <code>ArrangeWindowsStackLeft</code> puts the main window on the RIGHT hand side of the screen, and the tiled windows are on the LEFT hand side of the screen. <code>ArrangeWindowsStackRight</code> puts the main window on the LEFT hand side of the screen, and the tiled windows are on the RIGHT hand side of the screen.</dl>
<p> <code>ArrangeWindowsStackTop</code> <i>pattern</i> / *ArrangeWindowsStackBottom <i>pattern</i></p>
<dl>
<dd>Behaves just like <code>ArrangeWindowsStackLeft</code> and <code>ArrangeWindowsStackRight</code>. <code>ArrangeWindowsStackBottom</code> places the main window on the TOP half of the screen, and the tiled windows on the bottom half of the screen. <code>ArrangeWindowsStackTop</code> places the main window on the BOTTOM half of the screen and the tiled windows on the top half of the screen.</dl>
<p> <code>ShowDesktop</code></p>
<dl>
<dd>Minimizes all windows on the current workspace. If they are already all minimized, then it restores them.</dl>
<p> <code>Deiconify</code> <i>mode</i> <i>destination</i></p>
<dl>
<dd>Deiconifies windows (or, restores from a minimized state). </p>
<p> Where <i>mode</i> may be one of:</p>
<dl>
<dd><code>All</code></p>
<dl>
<dd>All icons across all workspaces.</dl>
<p> <code>AllWorkspace</code></p>
<dl>
<dd>All icons on the current workspace.</dl>
<p> <code>Last</code></p>
<dl>
<dd>The last icon across all workspaces.</dl>
<p> <code>LastWorkspace</code> (default)</p>
<dl>
<dd>The last icon on the current workspace.</dl>
</dl>
<p> And <i>destination</i> may be one of:</p>
<dl>
<dd><code>Current</code> (default)</p>
<dl>
<dd>Deiconify to the current workspace.</dl>
<p> <code>OriginQuiet</code></p>
<dl>
<dd>Deiconify to the window&#8217;s original workspace, but does so in the background, without moving you there.</dl>
</dl>
</dl>
<p> <code>SetWorkspaceName</code> <i>name</i> / <code>SetWorkspaceNameDialog</code></p>
<dl>
<dd>Sets the name of the current workspace.</dl>
<p> <code>CloseAllWindows</code></p>
<dl>
<dd>Closes all windows on all desktops.</dl>
<h3>Menu Commands</h3>
<p>These commands open or close fluxbox popup menus. For more information on what these menus contain or how to configure them, see <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i>. </p>
<p> <code>RootMenu</code></p>
<dl>
<dd>Opens the root menu. See <code>ROOT MENU</code> in <code><a href="/docs/linux/man/5-fluxbox-menu/">fluxbox-menu</a>(5)</code> for details.</dl>
<p> <code>WorkspaceMenu</code></p>
<dl>
<dd>Opens a menu showing all workspaces and windows. See <code>Workspace Menu</code> in <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> for details.</dl>
<p> <code>WindowMenu</code></p>
<dl>
<dd>Opens a menu containing actions for the current window. See <code>WINDOW MENU</code> in <code><a href="/docs/linux/man/5-fluxbox-menu/">fluxbox-menu</a>(5)</code> for details. </p>
<p> <code>ClientMenu</code> [<i>pattern</i>]</p>
<dl>
<dd>Opens a menu that contains all windows. If you specify a <i>pattern</i>, only matching windows will be in the menu. Selecting a window will jump to that workspace and raise the window. See <code>CLIENT PATTERNS</code> below for more details on the <i>pattern</i> argument.</dl>
<p> <code>CustomMenu</code> <i>path</i></p>
<dl>
<dd>Opens a custom menu file. This <i>path</i> must be a valid menu file in the same format as detailed by the <code>ROOT MENU</code> section of <code><a href="/docs/linux/man/5-fluxbox-menu/">fluxbox-menu</a>(5)</code>.</dl>
<p> <code>HideMenus</code></p>
<dl>
<dd>Hide all fluxbox popup menus.</dl>
</dl>
<h3>Window Manager Commands</h3>
<p>These commands affect the Window Manager, or more than one window. </p>
<p> <code>Restart</code> [<i>path</i>]</p>
<dl>
<dd>Restarts fluxbox. This does not close any running applications. If the optional <i>path</i> is a path to an executable window manager, that manager is started in place of fluxbox.</dl>
<p> <code>Quit</code> | <code>Exit</code></p>
<dl>
<dd>Exits fluxbox. This will normally cause X to stop as well and terminate all existing applications, returning you to the login manager or console.</dl>
<p> <code>Reconfig</code> | <code>Reconfigure</code></p>
<dl>
<dd>Reloads all fluxbox configuration files including the keys file, apps file, and init file, if they have changed.</dl>
<p> <code>SetStyle</code> <i>path</i></p>
<dl>
<dd>Sets the current style to that given in <i>path</i>, which must be the full path to a fluxbox style.</dl>
<p> <code>ReloadStyle</code></p>
<dl>
<dd>Reloads only the current style. Useful after editing a style which is currently in use.</dl>
<p> <code>ExecCommand</code> <i>args &#8230;</i> | <code>Exec</code> <i>args &#8230;</i> | <code>Execute</code> <i>args &#8230;</i></p>
<dl>
<dd>Probably the most-used binding of all. Passes all the arguments to your <code>$SHELL</code> (or /bin/sh if $SHELL is not set). You can use this to launch applications, run shell scripts, etc. Since all arguments are passed verbatim to the shell, you can use environment variables, pipes, or anything else the shell can do. Note that processes only see environment variables that were set before fluxbox started (such as in <code>~/.fluxbox/startup</code>), or any that are set via the <code>Export</code> or <code>SetEnv</code> commands, below. See <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> for more details on the <code>ENVIRONMENT</code> and <code>\~/.fluxbox/startup</code> file.</dl>
<p> <code>CommandDialog</code></p>
<dl>
<dd>Pops up a dialog box that lets you type in any of these commands manually.</dl>
<p> <code>SetEnv</code> <i>name</i> <i>value</i> | <code>Export</code> <i>name</i>=<i>value</i></p>
<dl>
<dd>Sets an environment variable in Fluxbox. It will be passed to any applications spawned by any future ExecCommand commands.</dl>
<p> <code>SetResourceValue</code> <i>resourcename</i> <i>resourcevalue</i> | <code>SetResourceValueDialog</code></p>
<dl>
<dd>Sets a fluxbox resource value, which are normally stored in the init file. See <i><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</i> for more details on available resources and allowed values.</dl>
<h3>Special Commands</h3>
<p>These commands have special meanings or behaviors. </p>
<p> <code>MacroCmd</code> {<i>command1</i>} {<i>command2</i>} {<i>command3</i>} <i>&#8230;</i></p>
<dl>
<dd>Allows you to execute more than one command with one keybinding. The commands will be executed in series. The <code>{</code><code>}</code> brackets are literally required, as in the following example: </p>
<dl>
<dd>
<pre>MacroCmd {MoveTo 0 0} {ResizeTo 1280 800}</pre>
</dl>
</dl>
<p> <code>Delay</code> {<i>command</i>} [<i>microseconds</i>]</p>
<dl>
<dd>Delays running <i>command</i> for the given amount of time. If the same key binding is activated again, the timer will be restarted.</dl>
<p> <code>ToggleCmd</code> {<i>command1</i>} {<i>command2</i>} <i>&#8230;</i></p>
<dl>
<dd>Alternates between the commands. On the first press of the bound key, runs <i>command1</i>. On the next press, runs <i>command2</i>.</dl>
<p> <code>BindKey</code> <i>keybinding</i></p>
<dl>
<dd>Adds the given <i>keybinding</i> (which must be a valid key binding as defined in the DESCRIPTION section above) to your keys file.</dl>
<p> <code>KeyMode</code> <i>keymode</i> [<i>return-keybinding</i>]</p>
<dl>
<dd>Activates the named <i>keymode</i> (or, all key binding lines prefaced with the same <i>keymode</i>:) and deactivates all others until the <i>return-keybinding</i> (by default <code>Escape</code>) is pressed. The default keymode is named <i>default</i>.</dl>
<p> <code>ForEach</code> {<i>command</i>} [{<i>condition</i>}] | <code>Map</code> {<i>command</i>} [{<i>condition</i>}]</p>
<dl>
<dd>Runs the given <i>command</i> (normally one from the <code>Window Commands</code> section above) on each window. If you specify a <i>condition</i> (See <code>Conditions</code>, below) the action will be limited to matching windows.</dl>
<p> <code>If</code> {<i>condition</i>} {<i>then-command</i>} [{<i>else-command</i>}] | <code>Cond</code> {<i>condition</i>} {<i>then-command</i>} [{<i>else-command</i>}]</p>
<dl>
<dd>If the <i>condition</i> command returns <code>true</code>, then run the <i>then-command</i>, otherwise run the optional <i>else-command</i>. See <code>Conditions</code> below for more information on the <i>condition</i> argument.</dl>
<h3>Conditions</h3>
<p>These special commands are used to match windows conditionally. They are commonly used by the <code>If</code> and <code>ForEach</code> command. </p>
<p> <code>Matches</code> <i>pattern</i></p>
<dl>
<dd>Returns <code>true</code> if the current window matches the given <i>pattern</i>. See <code>CLIENT PATTERNS</code> below for details on the <i>pattern</i> syntax. </p>
<p> If your key binding uses the <code>OnWindow</code> modifier, it matches against the window you clicked, not the currently focused window. </p>
<p> To check other windows besides the currently focused one, see the <code>Every</code> and <code>Some</code> conditions below.</dl>
<p> <code>Some</code> <i>condition</i></p>
<dl>
<dd>Returns <code>true</code> if any window on any workspace (not just the currently focused one) matches the <i>condition</i>.</dl>
<p> <code>Every</code> <i>condition</i></p>
<dl>
<dd>Returns <code>true</code> if every window on every workspace (not just the current one) matches the <i>condition</i>.</dl>
<p> <code>Not</code> <i>condition</i></p>
<dl>
<dd>Returns <code>true</code> if <i>condition</i> returns <code>false</code>, and vice-versa.</dl>
<p> <code>And</code> {<i>condition1</i>} {<i>condition2</i>} [{<i>condition3</i>} &#8230;]</p>
<dl>
<dd>Returns <code>true</code> if and only if all given conditions return <code>true</code>.</dl>
<p> <code>Or</code> {<i>condition1</i>} {<i>condition2</i>} [{<i>condition3</i>} &#8230;]</p>
<dl>
<dd>Returns <code>true</code> if any of the listed conditions return <code>true</code>.</dl>
<p> <code>Xor</code> {<i>condition1</i>} {<i>condition2</i>} [{<i>condition3</i>} &#8230;]</p>
<dl>
<dd>Returns the boolean <code>xor</code> of the truth values for all conditions listed.</dl>
<h2>Client Patterns</h2>
<p>Many of the more advanced commands take a <i>pattern</i> argument, which allows you to direct the action at a specific window or set of windows which match the properties specified in the <i>pattern</i>. </p>
<p> A <i>pattern</i> looks like this</p>
<dl>
<dd><code>(</code>[<i>propertyname</i>[!]=]<i>regexp</i><code>)</code> &#8230;</dl>
<p> Match definitions are enclosed in parentheses <code>(</code>&#8230;<code>)</code>, and if no <i>propertyname</i> is given then <code>Name</code> is assumed. The <i>regexp</i> can contain any regular expression, or the special value <code>[current]</code>, which matches the corresponding value of the currently focused window. See <i><a href="/docs/linux/man/7-regex/">regex</a>(7)</i> for more information on acceptable regular expressions. </p>
<p> <i>propertyname</i> is not case sensitive, whereas the <i>regexp</i> is. </p>
<p> If you specify multiple <code>(</code><i>pattern</i>) arguments, this implies an AND condition &#8211; All specified patterns must match. </p>
<p> You can use <code>=</code> to test for equality or <code>!=</code> to test for inequality. </p>
<p> The following values are accepted for <i>propertyname</i></p>
<dl>
<dd><code>Name</code></p>
<dl>
<dd>A string, corresponding to the CLASSNAME property (The first field of WM_CLASS from the output of the <code><a href="/docs/linux/man/1-xprop/">xprop</a>(1)</code> utility).</dl>
<p> <code>Class</code></p>
<dl>
<dd>A string, corresponding to the CLASSCLASS property (The second field of WM_CLASS from the output of the <code><a href="/docs/linux/man/1-xprop/">xprop</a>(1)</code> utility).</dl>
<p> <code>Title</code></p>
<dl>
<dd>A string, corresponding to the window title (WM_NAME from <code><a href="/docs/linux/man/1-xprop/">xprop</a>(1)</code>).</dl>
<p> <code>Role</code></p>
<dl>
<dd>A string, corresponding to the ROLE property (WM_WINDOW_ROLE from <code><a href="/docs/linux/man/1-xprop/">xprop</a>(1)</code>).</dl>
<p> <code>Transient</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window is transient (typically, a popup dialog) or not.</dl>
<p> <code>Maximized</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window is maximized or not.</dl>
<p> <code>MaximizedHorizontal</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window is maximized horizontally or not.</dl>
<p> <code>MaximizedVertical</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window is maximized vertically or not.</dl>
<p> <code>Minimized</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window is minimized (iconified) or not.</dl>
<p> <code>Fullscreen</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window is fullscreen or not.</dl>
<p> <code>Shaded</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window is shaded or not.</dl>
<p> <code>Stuck</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window is sticky (on all workspaces) or not.</dl>
<p> <code>FocusHidden</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window has asked to be left off the focus list (or, the alt-tab list), or not.</dl>
<p> <code>IconHidden</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window has asked to be left off the icon list (or, the taskbar), or not.</dl>
<p> <code>Urgent</code></p>
<dl>
<dd>Either <code>yes</code> or <code>no</code>, depending on whether the window has the urgent hint set.</dl>
<p> <code>Workspace</code></p>
<dl>
<dd>A number corresponding to the workspace number to which the window is attached. The first workspace here is <code>0</code>. You may also use <code>[current]</code> to match the currently visible workspace.</dl>
<p> <code>WorkspaceName</code></p>
<dl>
<dd>A string corresponding to the name of the workspace to which the window is attached.</dl>
<p> <code>Head</code></p>
<dl>
<dd>The number of the display head to which the window is attached. You may match this against the special value <code>[mouse]</code> which refers to the head where the mouse pointer currently resides.</dl>
<p> <code>Layer</code></p>
<dl>
<dd>The string name of the window&#8217;s layer, which is one of <code>AboveDock</code>, <code>Dock</code>, <code>Top</code>, <code>Normal</code>, <code>Bottom</code>, <code>Desktop</code></dl>
<p> <code>Screen</code></p>
<dl>
<dd>The number of the currently used <i>screen</i>. If the setup of the running xserver involves independent screens (<i>not Xinerama</i>), the $DISPLAY environment contains something like <i>:0.1</i> or <i>:1.0</i>. The part after the dot (<i>.</i>) is the number of the screen.</dl>
<p> <code>@XPROP</code></p>
<dl>
<dd>A string, corresponding to any xproperty (Use either the <code><a href="/docs/linux/man/1-xprop/">xprop</a>(1)</code> utility or the <i>SetXProp</i> command to set a xproperty to a window)</dl>
</dl>
<p> <code>Matches any windows with the CLASSNAME of &quot;xterm&quot;</code>. </p>
<dl>
<dd>
<pre>(xterm)</pre>
</dl>
<p> <code>Matches any windows with the same CLASSNAME as the currently focused window</code>. </p>
<dl>
<dd>
<pre>(Name=[current])</pre>
</dl>
<p> <code>Matches any windows on the same head as the mouse but on a different layer than the currently focused window</code>. </p>
<dl>
<dd>
<pre>(Head=[mouse]) (Layer!=[current])</pre>
</dl>
<p> <code>Matches any windows having a xproperty named FOO with &quot;bar&quot; in it</code>. </p>
<dl>
<dd>
<pre>(@FOO=.*bar.*)</pre>
</dl>
<h2>Files</h2>
<p><code>~/.fluxbox/keys</code></p>
<dl>
<dd>This is the default location for the keybinding definitions.</dl>
<p> <code>/usr/X11R6/include/X11/keysymdef.h</code></p>
<dl>
<dd>X key names are in this file.</dl>
<p> <code>/usr/X11R6/lib/X11/XKeysymDB</code></p>
<dl>
<dd>X key names are also in this file.</dl>
<h2>Resources</h2>
<p><code>session.keyFile:</code> <i>location</i></p>
<dl>
<dd>This may be set to override the location of the keybinding definitions.</dl>
<h2>Environment</h2>
<p>Remember that <code>ExecCommand</code> command can take advantage of other environment variables if they are set before fluxbox is started, or via the <code>Export</code> or <code>SetEnv</code> commands. For example, if <code>$TERM</code> is set, it could be use like this: </p>
<dl>
<dd>
<pre>Mod1 x :ExecCommand $TERM</pre>
</dl>
<p> For more information about environment variables, see your shell&#8217;s manual.</p>
<h2>Examples</h2>
<p>Here are some interesting and/or useful examples you can do with your keys file. </p>
<dl>
<dd>
<pre># Mod4+drag moves a window
OnWindow Mod4 Mouse1 :StartMoving
# If any xterm windows are open, cycle through them. If none are open, open
# one:
Mod4 t :If {Some Matches (xterm)} {NextWindow (xterm)} {Exec xterm}
# Set a different wallpaper on every workspace:
ChangeWorkspace :Exec fbsetbg ~/.fluxbox/bg$(xprop -root _NET_CURRENT_DESKTOP | awk '{print $3}').png
# Focusses the next window with it's xproperty 'PROP' set to 'foo'
Mod4 p Mod4 Tab :NextWindow (@PROP=foo)</pre>
</dl>
<h2>Authors</h2>
<dl>
<dd>&bull; Jim Ramsay &lt;i.am at jimramsay com&gt; (&gt;fluxbox-1.0.0)</dl>
<dl>
<dd>&bull; Curt Micol &lt;asenchi at asenchi com&gt; (&gt;fluxbox-0.9.11)</dl>
<dl>
<dd>&bull; Tobias Klausmann &lt;klausman at users sourceforge net&gt; (&lt;fluxbox-0.9.11)</dl>
<dl>
<dd>&bull; Grubert &lt;grubert at users sourceforge net&gt; (fluxbox)</dl>
<dl>
<dd>&bull; Matthew Hawkins &lt;matt at mh dropbear id au&gt; (blackbox)</dl>
<dl>
<dd>&bull; Wilbert Berendsen &lt;wbsoft at xs4all nl&gt; (blackbox)</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) <a href="/docs/linux/man/1-xprop/">xprop</a>(1) <a href="/docs/linux/man/1-xev/">xev</a>(1) <a href="/docs/linux/man/1-xkill/">xkill</a>(1) <a href="/docs/linux/man/7-regex/">regex</a>(7)</p>
<h2>Author</h2>
<p><code>Jim Ramsay</code> &lt;i.am [at] jimramsay.com&gt;</p>
<dl>
<dd>Author.</dl>
