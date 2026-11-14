---
title: "fluxbox-apps(5)"
name: "fluxbox-apps"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fluxbox-apps/"
description: "fluxbox-apps – per-window attribute configuration for"
---

<p>fluxbox-apps &#8211; per-window attribute configuration for </p>
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</p>
<h2>Synopsis</h2>
<p>~/.fluxbox/apps</p>
<h2>Syntax</h2>
<p>Variable parameters are shown in emphasis: <i>argument</i> </p>
<p> All other characters shown are required verbatim. Whitespace is only required to delimit words, but it is fine to add more whitespace.</p>
<h2>Description</h2>
<p>It is possible to force an application to always have the same dimensions, position, and other settings when it is first launched. These settings are saved in the &#8216;apps&#8217; file. </p>
<p> Most simple settings can be saved using the &#8220;Remember&#8230;&#8221; submenu of the window menu, which can usually be opened with a right-click on the titlebar. More advanced features require manually editing the &#8216;apps&#8217; file. This may include using <code>GROUP SECTIONS</code> to set up automatic window tab groups. </p>
<p> You do not need to &#8220;reload&#8221; fluxbox after editing the apps file, the changes should be rescanned when the next window is opened. </p>
<p> The file is made up of two main types of sections, apps and groups, detailed below.</p>
<h2>App Sections</h2>
<p><code>[app]</code> sections provide settings for individual application windows. </p>
<p> These sections begin with a line of the format</p>
<dl>
<dd><code>[app]</code><code>(</code><i>pattern</i><code>)</code><code>{</code><i>count</i><code>}</code></dl>
<p> The <i>pattern</i> can be one or more patterns which match windows. For more details, see <code>CLIENT PATTERNS</code>. If you specify more than one <i>pattern</i>, they must ALL match for the settings to be applied. </p>
<p> The <code>{</code><i>count</i><code>}</code> is optional. If specified, then the entry will only match at most that many windows at any time. If omitted, the default is to apply the settings to all matching windows. </p>
<p> This opening <code>[apps]</code> line is followed by any number of settings for the application. See <code>SETTINGS</code> for more details. </p>
<p> Each of these sections ends with the single line</p>
<dl>
<dd><code>[end]</code></dl>
<h2>Group Sections</h2>
<p>The primary purpose of <code>[group]</code> sections is to group windows together. All windows in a group will be tabbed together automatically. </p>
<p> These sections begin with a line of the format</p>
<dl>
<dd><code>[group]</code><code>(</code><i>pattern</i><code>)</code></dl>
<p> Where the <i>pattern</i> item is optional. If specified, this pattern must match for the group to take effect. It is common to use non-window-specific patterns such as <code>(workspace)</code> here. See <code>CLIENT PATTERNS</code> for more details. </p>
<p> This is followed by any number of <code>[app]</code> lines. These have a similar format to the <code>[app]</code> section detailed above in <code>APP SECTIONS</code>, but do not contain any settings and do not have an associated <code>[end]</code> line. </p>
<p> Like this</p>
<dl>
<dd><code>[app]</code><code>(</code><i>pattern</i><code>)</code></dl>
<p> This section may also contain settings that are applied to every window in the group. See the <code>SETTINGS</code> section for details. </p>
<p> As with <code>[app]</code> sections, each of these sections ends with the single line</p>
<dl>
<dd><code>[end]</code></dl>
<h2>Settings</h2>
<p>These settings may be stored in the &#8216;apps&#8217; file. A settings line must appear inside either an <code>[app]</code> or <code>[group]</code> section. </p>
<p> The general format is</p>
<dl>
<dd><code>[</code><i>setting</i><code>]</code><code>{</code><i>value</i><code>}</code></dl>
<p> All allowed values are described below, except for <i>bool</i> which can simply have the value <code>yes</code> or <code>no</code>, which enables or disables the associated setting, respectively. </p>
<p> <code>[Workspace]</code> {<i>number</i>}</p>
<dl>
<dd>Forces the application to open on the <i>number</i> workspace specified. Workspaces are set by number, beginning with 0.</dl>
<p> <code>[Jump]</code> {<i>bool</i>}</p>
<dl>
<dd>Changes the active workspace to the remembered one when the application is opened. This is only useful when used in conjunction with <i>[Workspace]</i>. See <code>EXAMPLES</code>.</dl>
<p> <code>[Head]</code> {<i>number</i>}</p>
<dl>
<dd>Forces the application to open on the <i>number</i> head specified (Xinerama only).</dl>
<p> <code>[Layer]</code> {<i>number</i>}</p>
<dl>
<dd>Specify the layer to open the window on (by number). Each layer has a number. The named ones are: 2-AboveDock, 4-Dock, 6-Top, 8-Normal, 10-Bottom, 12-Desktop.</dl>
<p> <code>[Dimensions]</code> {<i>width[%]</i> <i>height[%]</i>}</p>
<dl>
<dd>Opens the application with the specified <i>width</i> and <i>height</i>, in pixels. If the value is given in percent, then the window size will be based on the current screen&#8217;s size.</dl>
<p> <code>[Position]</code> (<i>anchor</i>) {<i>X[%]</i> <i>Y[%]</i>}</p>
<dl>
<dd>Position the application at a particular spot. By default the upper-left corner is placed at screen coordinates (<i>X</i>,<i>Y</i>). If you specify an <i>anchor</i>, say BottomRight, then the lower-right corner of the window is positioned (<i>X</i>,<i>Y</i>) pixels from the lower-right corner of the screen. If the value is given in percent, then the coordinates will be based on the current screen&#8217;s size. </p>
<p> <i>anchor</i> may be set to one of:</p>
<dl>
<dd><code>TopLeft Left BottomLeft Top Center Bottom TopRight Right BottomRight</code></dl>
</dl>
<p> <code>[Deco]</code> {<i>value</i>}</p>
<dl>
<dd>Specify the decoration state. There are several predefined <i>value</i> sets:</p>
<dl>
<dd><code>NORMAL</code></p>
<dl>
<dd>Standard decorations</dl>
<p> <code>NONE</code></p>
<dl>
<dd>No decorations</dl>
<p> <code>BORDER</code></p>
<dl>
<dd>Like NONE except keep the X window border</dl>
<p> <code>TAB</code></p>
<dl>
<dd>Like BORDER except keep external tabs (if enabled)</dl>
<p> <code>TINY</code></p>
<dl>
<dd>Titlebar with only an iconify button</dl>
<p> <code>TOOL</code></p>
<dl>
<dd>Titlebar only</dl>
<p> The <i>value</i> may also be a bitmask for finer-grained control. The bits are, from (1&lt;&lt;0) to (1&lt;&lt;10): Titlebar, Handle/Grips, Border, Iconify Button, Maximize Button, Close Button, Menu Button, Sticky Button, Shade Button, External Tabs, Focus Enabled.</dl>
</dl>
<p> <code>[Shaded]</code> {<i>bool</i>}</p>
<dl>
<dd>Whether the window is Shaded (rolled-up) or not.</dl>
<p> <code>[Tab]</code> {<i>bool</i>}</p>
<dl>
<dd>Whether the window has tabs enabled.</dl>
<p> <code>[FocusNewWindow]</code> {<i>bool</i>}</p>
<dl>
<dd>If enabled, a new window will grab X focus as soon as it is opened. If disabled, a new window will not grab X focus as soon as it is opened.</dl>
<p> <code>[FocusHidden]</code> {<i>bool</i>}</p>
<dl>
<dd>If enabled, the window will not appear in <i>NextWindow</i>/<i>PrevWindow</i> lists.</dl>
<p> <code>[IconHidden]</code> {<i>bool</i>}</p>
<dl>
<dd>If enabled, the window will not appear in the icon area of the toolbar.</dl>
<p> <code>[Hidden]</code> {<i>bool</i>}</p>
<dl>
<dd>A shortcut for setting both <code>FocusHidden</code> and <code>IconHidden</code> at the same time.</dl>
<p> <code>[Sticky]</code> {<i>bool</i>}</p>
<dl>
<dd>Specify if an application should be sticky (shown on all workspaces) or not.</dl>
<p> <code>[Minimized]</code> {<i>bool</i>}</p>
<dl>
<dd>Application should start minimized</dl>
<p> <code>[Maximized]</code> {<i>value</i>}</p>
<dl>
<dd>Application should start maximized. <i>value</i> may be:</p>
<dl>
<dd><code>yes</code></p>
<dl>
<dd>Fully maximized</dl>
<p> <code>horz</code></p>
<dl>
<dd>Horizontally maximized</dl>
<p> <code>vert</code></p>
<dl>
<dd>Vertically maximized</dl>
<p> <code>no</code></p>
<dl>
<dd>Not maximized</dl>
</dl>
</dl>
<p> <code>[Fullscreen]</code> {<i>bool</i>}</p>
<dl>
<dd>Application should start in fullscreen mode (fully maximized without any decorations).</dl>
<p> <code>[Close]</code> {<i>bool</i>}</p>
<dl>
<dd>Save settings on close. By default, application settings are not updated when a window is closed.</dl>
<p> <code>[Alpha]</code> {<i>value</i> [<i>value</i>]}</p>
<dl>
<dd>Set the alpha value for this window. If two values are given, they correspond to the focused and unfocused transparency, respectively. One number only will be used for both values. <i>value</i> is an integer between 0 and 255.</dl>
<h2>Client Patterns</h2>
<p>A <i>pattern</i> looks like this</p>
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
<p><code>~/.fluxbox/apps</code></p>
<dl>
<dd>This is the default location for the application settings.</dl>
<h2>Resources</h2>
<p><code>session.appsFile:</code> <i>location</i></p>
<dl>
<dd>This may be set to override the location of the application settings.</dl>
<h2>Examples</h2>
<p>Here are some interesting and/or useful examples you can do with your apps file. </p>
<dl>
<dd>
<pre># Put the first two windows which end with 'term' on workspace 1
[app] (name=.*[tT]erm) {2}
 [Workspace] {1}
[end]
# Center kate with a specific size, and update these values when the window is
# closed.
[app] (name=kate)
 [Dimensions] {1022 747}
 [Position] (CENTER) {0 0}
 [Close] {yes}
[end]
# When starting konqueror, jump to workspace 1 first and start it there.
[app] (name=konqueror)
 [Workspace] {1}
 [Jump] {yes}
[end]
# start all aterm without decorations
[app] (name=aterm)
 [Deco] {NONE}
[end]
# a group with the gimp dock and toolbox
# appears on layer 4 (bottom)
[group]
 [app] (name=gimp) (role=gimp-dock)
 [app] (name=gimp) (role=gimp-toolbox)
 [Layer] {4}
[end]</pre>
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
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) <a href="/docs/linux/man/1-xprop/">xprop</a>(1) <a href="/docs/linux/man/7-regex/">regex</a>(7)</p>
<h2>Author</h2>
<p><code>Jim Ramsay</code> &lt;i.am [at] jimramsay.com&gt;</p>
<dl>
<dd>Author.</dl>
