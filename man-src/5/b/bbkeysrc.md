---
title: "bbkeysrc(5)"
name: "bbkeysrc"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bbkeysrc/"
description: "bbkeysrc – bbkeys configuration file"
---

<p>bbkeysrc &#8211; bbkeys configuration file </p>
<h2>Synopsis</h2>
<p><code>$HOME/.bbkeysrc</code> </p>
<h2>Description</h2>
<p><code>bbkeys</code> picks up its configuration settings from $HOME/.bbkeysrc unless overridden on the command line. There are several avenues open to the user to set any key-grabs that the user wishes:</p>
<h3>Using <i>bbconf</i>:</h3>
<p>This is a Qt-based application available at <a rel="nofollow" href="http://bbconf.sourceforge.net/.">http://bbconf.sourceforge.net/.</a></p>
<h3>Manually editing <i>$HOME/.bbkeysrc</i>:</h3>
<p>The format is very easy, and it follows the same format as blackbox&#8217;s menu files. It must begin with a &quot;[begin]&quot; tag. It may contain a &quot;[config]&quot; tag, containing a configuration section, ending with a &quot;[end]&quot; tag. In fact, all opening section tags must end with an &quot;[end]&quot; tag. It should also contain a &quot;[keybindings]&quot; section. </p>
<p> For more information, see the man page for blackbox&#8217;s menu. </p>
<h2>List Of Config Options</h2>
<dl>
<dt><i>stylefile</i>:</p>
<dd>filename of blackbox style to use (string) </p>
<dt><i>honorModifiers</i>:</p>
<dd>whether or not to break if NumLock or ScrollLock is pressed. (hint: for bbkeys to ignore your keybindings if NumLock or ScrollLock are pressed, set this to true) (true or false) </p>
<dt><i>raiseWhileCycling</i>:</p>
<dd>should bbkeys raise the windows you&#8217;re cycling through while cycling through them? (true or false) </p>
<dt><i>showCycleMenu</i></p>
<dd>show the window-cycling menu or cycle without it? (true or false) </p>
<dt><i>cycleMenuTitle</i></p>
<dd>show the given string as the title of the window-cycling menu. if an empty string is passed as the parameter to this config option(&quot;{}&quot;), then the title will not be drawn. (string value) </p>
<dt><i>menuTextJustify</i></p>
<dd>how should the window-cycling menu be justified? (left, center, right) </p>
<dt><i>menuTitleJustify</i></p>
<dd>how should the window-cycling title be justified? (left, center, right) </p>
<dt><i>autoConfig</i></p>
<dd>should bbkeys watch for changes to its config file? (true or false) Note: if you decide to not do this (though it should be VERY light on system resources), you can always force bbkeys to reconfigure itself by sending it a SIGHUP (killall -HUP bbkeys). </p>
<dt><i>autoConfigCheckTimeout</i></p>
<dd>how often should bbkeys check for changes made to its config file? (numeric number of seconds) </p>
<dt><i>workspaceColumns</i></p>
<dd>number of columns that you have your workspaces laid out in your pager (numeric) </p>
<dt><i>workspaceRows</i></p>
<dd>number of rows that you have your workspaces/desktops laid out in (numeric). As way of an example, if you have your pager laid out in a 4&#215;2 grid (4 wide, 2 high), then you would set workspaceColumns to 4 and workspaceRows to 2. </p>
<dt><i>cycleMenuX</i></p>
<dd>horizontal position that you want the window cycling menu to show up at. (numeric) </p>
<dt><i>cycleMenuY</i></p>
<dd>vertical position that you want the window cycling menu to show up at. (numeric) NOTE. The cycleMenuX and cycleMenuY config options allow you to place your window-cycling window exactly where you want to put it on screen. We at the Bbkeys Foundation For Better Software (TM) call this a feature, though some crazy nuts might call it a bug caused by the fact that blackbox&#8217;s Menu class doesn&#8217;t have anything in it to center it on-screen, etc. It also doesn&#8217;t have any methods available to figure out how big the menu will be on-screen. This can be worked around by bbkeys, but I&#8217;ve not the time to do it now. Patch anyone? Or, you can just consider it a really neat feature that you can place the popup window-cycling window anywhere you want. =:D</dl>
<h2>Keybindings</h2>
<p>The format of this section is similar to the config section, and blackbox&#8217;s menu structure. Each line will look like this:</p>
<dl>
<dd>[command] (keys) {parameters} </p>
</dl>
<p> <code>Parameters:</code><br />
 Not all directives need to have parameters provided, and within the [keybindings] section, the only sub-group allowed (a group that will have an [end] tag) is the [chain] tag. The chain tag is special and allows the user to give emacs-style keybindings, where a certain keystroke is given, released, and then another keystroke is given to complete the action. A good example would be the following: </p>
<dl>
<dd>&nbsp;<wbr>[chain]&nbsp;<wbr>(Control-Mod1-W)<br />
[sendToWorkspace]&nbsp;<wbr>(1)&nbsp;<wbr>{1}<br />
[sendToWorkspace]&nbsp;<wbr>(2)&nbsp;<wbr>{2}<br />
[sendToWorkspace]&nbsp;<wbr>(3)&nbsp;<wbr>{3}<br />
[sendToWorkspace]&nbsp;<wbr>(4)&nbsp;<wbr>{4}<br />
&nbsp;<wbr>[end] </p>
</dl>
<p> Note that both the beginning [chain] and the ending [end] tags must be provided. In this example, the chain is begun by the user pressing (and holding) the Control modifier, the Mod1 (Alt) modifier, and the &quot;W&quot; key on his keyboard. The user then releases these keys and bbkeys enters the chain. Bbkeys will then wait for the user to press one of the keybindings from within that chain to execute the next action. In this case, if bbkeys sees either the 1, 2, 3 or 4 key pressed on the keyboard, it will execute the given action for that key. Again, in this case, bbkeys will send the currently-focused window to the workspace specified in the {}-enclosed parameter (workspace 1, 2, 3, or 4 as the case may be here. </p>
<p> So, the parameters provided in a keybinding directive can be seen as additional information to provide to the &quot;command&quot;. In some cases, it will be a number (what workspace to send a window to, how many pixels to move the window, how many pixels to resize a window, etc.). In other cases, it will be a string (&quot;xterm -fn nexus&quot;, for example, as an argument to the Execute command. And for many directives, it is not needed at all. </p>
<p> <code>Keys:</code><br />
 The format for the keybindings are using 0 or more modifiers, separated with the &quot;-&quot; character, finally followed by the key name as known to X. The &quot;left&quot; key, for example, is known to X as &quot;Left&quot;. The &quot;j&quot; key is known as &quot;J&quot;. You get the idea. The modifiers are typically, &quot;Shift&quot;, &quot;Control&quot;, and &quot;Mod1&quot;. An example would be Mod1-Control-K. This would be listed as the second element in a keybinding directive. </p>
<p> <code>Commands:</code><br />
 The following commands are understood by bbkeys. Bbkeys is not case-sensitive with regards to its commands, so the case may be mixed accidentally or on purpose. =:) </p>
<dl>
<dt><i>execute</i></p>
<dd>Executes a command. An string argument/parameter is expected for this directive that lists the command to be executed. </p>
<dt><i>iconify</i></p>
<dd>
<dt><i>raise</i></p>
<dd>
<dt><i>lower</i></p>
<dd>
<dt><i>close</i></p>
<dd>
<dt><i>toggleShade</i></p>
<dd>
<dt><i>toggleOmnipresent</i></p>
<dd>Sets a window to be &quot;sticky&quot;&#8211;on all workspaces. </p>
<dt><i>toggleDecorations</i></p>
<dd>Either strips a window of all decorations or causes it to be decorated regularly. </p>
<dt><i>moveWindowUp</i></p>
<dd>A numeric parameter may be provided which tells bbkeys how many pixels in the given direction to move the currently-selected window. </p>
<dt><i>moveWindowDown</i></p>
<dd>A numeric parameter may be provided which tells bbkeys how many pixels in the given direction to move the currently-selected window. </p>
<dt><i>moveWindowLeft</i></p>
<dd>A numeric parameter may be provided which tells bbkeys how many pixels in the given direction to move the currently-selected window. </p>
<dt><i>moveWindowRight</i></p>
<dd>A numeric parameter may be provided which tells bbkeys how many pixels in the given direction to move the currently-selected window. </p>
<dt><i>resizeWindowWidth</i></p>
<dd>A numeric parameter may be provided which tells bbkeys how many pixels in the given direction to resize the currently-selected window. This may be a positive or negative number, allowing bbkeys to grow or shrink the window. </p>
<dt><i>resizeWindowHeight</i></p>
<dd>A numeric parameter may be provided which tells bbkeys how many pixels in the given direction to resize the currently-selected window. This may be a positive or negative number, allowing bbkeys to grow or shrink the window. </p>
<dt><i>toggleMaximizeFull</i></p>
<dd>
<dt><i>toggleMaximizeVertical</i></p>
<dd>
<dt><i>toggleMaximizeHorizontal</i></p>
<dd>
<dt><i>sendToWorkspace</i></p>
<dd>A numeric parameter must be provided which tells bbkeys which workspace (1-based index) to send the current window to. </p>
<dt><i>nextWindow</i></p>
<dd>Used for window cycling (alt-tabbing, most often). Selects the next window according to the window stack. </p>
<dt><i>prevWindow</i></p>
<dd>Used for window cycling (alt-tabbing, most often). Selects the previous window according to the window stack. </p>
<dt><i>nextWindowOnAllWorkspaces</i></p>
<dd>
<dt><i>prevWindowOnAllWorkspaces</i></p>
<dd>
<dt><i>nextWindowOnAllScreens</i></p>
<dd>
<dt><i>prevWindowOnAllScreens</i></p>
<dd>
<dt><i>nextWindowOfClass</i></p>
<dd>
<dt><i>prevWindowOfClass</i></p>
<dd>
<dt><i>nextWindowOfClassOnAllWorkspaces</i></p>
<dd>
<dt><i>prevWindowOfClassOnAllWorkspaces</i></p>
<dd>
<dt><i>changeWorkspace</i></p>
<dd>A numeric parameter must be given to tell bbkeys which 1-based workspace to switch to. </p>
<dt><i>nextWorkspace</i></p>
<dd>
<dt><i>prevWorkspace</i></p>
<dd>
<dt><i>upWorkspace</i></p>
<dd>
<dt><i>downWorkspace</i></p>
<dd>
<dt><i>leftWorkspace</i></p>
<dd>
<dt><i>rightWorkspace</i></p>
<dd>
<dt><i>nextScreen</i></p>
<dd>
<dt><i>prevScreen</i></p>
<dd>
<dt><i>chain</i></p>
<dd>No parameter is needed for this directive. </p>
</dl>
<h2>Example</h2>
<p>Example config file below&#8230;<br />
 [begin] (bbkeys configuration file)<br />
&nbsp;<wbr>&nbsp;<wbr>[config]<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(stylefile)&nbsp;<wbr>{~/local/blackbox-CVS/share/blackbox/styles/Cthulhain}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(honorModifiers)&nbsp;<wbr>{false}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(raiseWhileCycling)&nbsp;<wbr>{false}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(showCycleMenu)&nbsp;<wbr>&nbsp;<wbr>{true}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(menuTextJustify)&nbsp;<wbr>{right}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(autoConfig)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>{true}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(autoConfigCheckTimeout)&nbsp;<wbr>{2}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(workspaceColumns)&nbsp;<wbr>{4}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(workspaceRows)&nbsp;<wbr>{2}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(cycleMenuX)&nbsp;<wbr>{20}<br />
&nbsp;<wbr>[option]&nbsp;<wbr>(cycleMenuY)&nbsp;<wbr>{20}<br />
&nbsp;<wbr>&nbsp;<wbr>[end] </p>
<pre><code>[keybindings] (begin keybindings)

[chain] (Control-Mod1-W)

[sendToWorkspace] (1) {1}

[sendToWorkspace] (2) {2}

[sendToWorkspace] (3) {3}

[sendToWorkspace] (4) {4}

[sendToWorkspace] (5) {5}

[sendToWorkspace] (6) {6}

[sendToWorkspace] (7) {7}

[sendToWorkspace] (8) {8}

[end]

[chain] (Mod1-Y)

[execute] (1) {xmms}

[execute] (2) {aumix -v +5}

[execute] (3) {aumix -v -5}

[end]

[Lower]  (Mod1-Down)

[Raise]  (Mod1-Up)

[toggleShade]  (Mod1-F9)

[Close]  (Mod1-F4)

[Iconify]  (Mod1-m)

[toggleMaximizeFull]  (Mod1-F12)

[toggleMaximizeHorizontal]  (Mod1-F11)

[toggleMaximizeVertical]  (Mod1-F10)

[toggleOmnipresent]  (Mod1-Control-S)

[resizeWindowWidth]  (Mod1-Control-Shift-Left) {-5}

[resizeWindowWidth]  (Mod1-Control-Shift-Right) {5}

[resizeWindowHeight]  (Mod1-Control-Shift-Up) {-5}

[resizeWindowHeight]  (Mod1-Control-Shift-Down) {5}

[moveWindowUp]  (Mod1-Control-Up) {1}

[moveWindowDown]  (Mod1-Control-Down) {1}

[moveWindowLeft]  (Mod1-Control-Left) {1}

[moveWindowRight]  (Mod1-Control-Right) {1}

[NextWindow]  (Mod1-Tab)

[NextWindowOnAllWorkspaces]  (Mod1-Control-Tab)

[PrevWindow]  (Mod1-Shift-Tab)

[changeWorkspace]  (Mod1-1) {1}

[changeWorkspace]  (Mod1-2) {2}

[changeWorkspace]  (Mod1-3) {3}

[changeWorkspace]  (Mod1-4) {4}

[changeWorkspace]  (Mod1-5) {5}

[changeWorkspace]  (Mod1-6) {6}

[changeWorkspace]  (Mod1-7) {7}

[changeWorkspace]  (Mod1-8) {8}</code></pre>
<p>&nbsp;<wbr>[upWorkspace]&nbsp;<wbr>(Mod1-Control-K)<br />
&nbsp;<wbr>[downWorkspace]&nbsp;<wbr>(Mod1-Control-J)<br />
&nbsp;<wbr>[leftWorkspace]&nbsp;<wbr>(Mod1-Control-H)<br />
&nbsp;<wbr>[rightWorkspace]&nbsp;<wbr>(Mod1-Control-L)<br />
&nbsp;<wbr>[showRootMenu]&nbsp;<wbr>(Mod1-Control-Escape)<br />
&nbsp;<wbr>[Execute]&nbsp;<wbr>&nbsp;<wbr>(Mod1-F5)&nbsp;<wbr>{xrefresh}<br />
&nbsp;<wbr>[Execute]&nbsp;<wbr>&nbsp;<wbr>(Mod1-F1)&nbsp;<wbr>{gnome-terminal}<br />
&nbsp;<wbr>#[Execute]&nbsp;<wbr>&nbsp;<wbr>(Mod4-E)&nbsp;<wbr>{kfmclient openProfile filemanagement}<br />
&nbsp;<wbr>#[Execute]&nbsp;<wbr>&nbsp;<wbr>(F20)&nbsp;<wbr>{kfmclient openProfile filemanagement}<br />
&nbsp;<wbr>[Execute]&nbsp;<wbr>&nbsp;<wbr>(Mod4-E)&nbsp;<wbr>{nautilus&nbsp;<wbr>/home/gideon}<br />
&nbsp;<wbr>[Execute]&nbsp;<wbr>&nbsp;<wbr>(F20)&nbsp;<wbr>{nautilus&nbsp;<wbr>/home/gideon}<br />
&nbsp;<wbr>&nbsp;<wbr>[end]&nbsp;<wbr>(end keybindings) [end] (end bbkeys configuration)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bbkeys/">bbkeys</a>(1),</code> <code><a href="/docs/linux/man/1-blackbox/">blackbox</a>(1)</code> </p>
<h2>Author</h2>
