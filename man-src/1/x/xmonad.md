---
title: "xmonad(1)"
name: "xmonad"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmonad/"
description: "xmonad – a tiling window manager"
---

<h2>Name</h2>
<p> xmonad &#8211; a tiling window manager</p>
<h2>Description</h2>
<p> xmonad is a minimalist tiling window manager for X, written in Haskell. Windows are managed using automatic layout algorithms, which can be dynamically reconfigured. At any time windows are arranged so as to maximize the use of screen real estate. All features of the window manager are accessible purely from the keyboard: a mouse is entirely optional. xmonad is configured in Haskell, and custom layout algorithms may be implemented by the user in config files. A principle of xmonad is predictability: the user should know in advance precisely the window arrangement that will result from any action. </p>
<p> By default, xmonad provides three layout algorithms: tall, wide and fullscreen. In tall or wide mode, windows are tiled and arranged to prevent overlap and maximize screen use. Sets of windows are grouped together on virtual screens, and each screen retains its own layout, which may be reconfigured dynamically. Multiple physical monitors are supported via Xinerama, allowing simultaneous display of a number of screens. </p>
<p> By utilizing the expressivity of a modern functional language with a rich static type system, xmonad provides a complete, featureful window manager in less than 1200 lines of code, with an emphasis on correctness and robustness. Internal properties of the window manager are checked using a combination of static guarantees provided by the type system, and type-based automated testing. A benefit of this is that the code is simple to understand, and easy to modify.</p>
<h2>Usage</h2>
<p> xmonad places each window into a &quot;workspace&quot;. Each workspace can have any number of windows, which you can cycle though with mod-j and mod-k. Windows are either displayed full screen, tiled horizontally, or tiled vertically. You can toggle the layout mode with mod-space, which will cycle through the available modes. </p>
<p> You can switch to workspace N with mod-N. For example, to switch to workspace 5, you would press mod-5. Similarly, you can move the current window to another workspace with mod-shift-N. </p>
<p> When running with multiple monitors (Xinerama), each screen has exactly 1 workspace visible. mod-{w,e,r} switch the focus between screens, while shift-mod-{w,e,r} move the current window to that screen. When xmonad starts, workspace 1 is on screen 1, workspace 2 is on screen 2, etc. When switching workspaces to one that is already visible, the current and visible workspaces are swapped.</p>
<h3>Flags</h3>
<p> xmonad has several flags which you may pass to the executable. These flags are:</p>
<dl>
<dt><code>&#8211;recompile</code></p>
<dd> Recompiles your configuration in ~/.xmonad/xmonad.hs</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;restart</code></p>
<dd> Causes the currently running xmonad process to restart</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;replace</code></p>
<dd> Replace the current window manager with xmonad</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;version</code></p>
<dd> Display version of xmonad</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;verbose-version</code></p>
<dd> Display detailed version of xmonad</p>
<dl>
<dt>
<dd></dl>
</dl>
<h3>Default keyboard bindings</h3>
<dl>
<dt><code>mod-shift-return</code></p>
<dd> Launch terminal</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-p</code></p>
<dd> Launch dmenu</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-p</code></p>
<dd> Launch gmrun</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-c</code></p>
<dd> Close the focused window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-space</code></p>
<dd> Rotate through the available layout algorithms</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-space</code></p>
<dd> Reset the layouts on the current workspace to default</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-n</code></p>
<dd> Resize viewed windows to the correct size</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-tab</code></p>
<dd> Move focus to the next window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-tab</code></p>
<dd> Move focus to the previous window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-j</code></p>
<dd> Move focus to the next window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-k</code></p>
<dd> Move focus to the previous window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-m</code></p>
<dd> Move focus to the master window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-return</code></p>
<dd> Swap the focused window and the master window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-j</code></p>
<dd> Swap the focused window with the next window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-k</code></p>
<dd> Swap the focused window with the previous window</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-h</code></p>
<dd> Shrink the master area</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-l</code></p>
<dd> Expand the master area</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-t</code></p>
<dd> Push window back into tiling</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-comma</code></p>
<dd> Increment the number of windows in the master area</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-period</code></p>
<dd> Deincrement the number of windows in the master area</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-q</code></p>
<dd> Quit xmonad</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-q</code></p>
<dd> Restart xmonad</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-slash</code></p>
<dd> Run xmessage with a summary of the default keybindings (useful for beginners)</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-[1..9]</code></p>
<dd> Switch to workspace N</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-[1..9]</code></p>
<dd> Move client to workspace N</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-{w,e,r}</code></p>
<dd> Switch to physical/Xinerama screens 1, 2, or 3</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-shift-{w,e,r}</code></p>
<dd> Move client to screen 1, 2, or 3</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-button1</code></p>
<dd> Set the window to floating mode and move by dragging</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-button2</code></p>
<dd> Raise the window to the top of the stack</p>
<dl>
<dt>
<dd></dl>
<dt><code>mod-button3</code></p>
<dd> Set the window to floating mode and resize by dragging</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Examples</h2>
<p> To use xmonad as your window manager add to your ~/.xinitrc file:</p>
<dl>
<dt>
<dd>
<pre>
exec xmonad
</pre>
</dl>
<h2>Customization</h2>
<p> xmonad is customized in ~/.xmonad/xmonad.hs, and then restarting with mod-q. </p>
<p> You can find many extensions to the core feature set in the xmonad- contrib package, available through your package manager or from xmonad.org (<a rel="nofollow" href="http://xmonad.org">http://xmonad.org</a>).</p>
<h3>Modular Configuration</h3>
<p> As of xmonad-0.9, any additional Haskell modules may be placed in ~/.xmonad/lib/ are available in GHC&#8217;s searchpath. Hierarchical modules are supported: for example, the file ~/.xmonad/lib/XMonad/Stack/MyAdditions.hs could contain:</p>
<dl>
<dt>
<dd>
<pre><code>
module XMonad.Stack.MyAdditions &amp;nbsp;
(function1) &amp; nbsp;
where
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
function1 &amp;nbsp;
= &amp;nbsp;
error &amp;nbsp;
"function1: Not implemented yet!"
</code></pre>
</dl>
<p> Your xmonad.hs may then import XMonad.Stack.MyAdditions as if that module was contained within xmonad or xmonad-contrib.</p>
<h2>Bugs</h2>
<p> Probably. If you find any, please report them to the bugtracker (<a rel="nofollow" href="http://code.google.com/p/xmonad/issues/list)">http://code.google.com/p/xmonad/issues/list)</a> </p>
<h2>Index</h2>
