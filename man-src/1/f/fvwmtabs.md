---
title: "fvwmtabs(1)"
name: "fvwmtabs"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmtabs/"
description: "FvwmTabs – a generic tabbing module for the fvwm window manager."
---

<p><code>FvwmTabs</code> &#8211; a generic tabbing module for the fvwm window manager. </p>
<h2>Synopsis</h2>
<p><code>FvwmTabs</code> is spawned by fvwm, so no command line invocation is possible.</p>
<h2>Description</h2>
<p>The <code>FvwmTabs</code> module is capable of swallowing any fvwm window &amp; treating it as a tab in a <i>tab-manager</i> window. A tab-manager is sometimes called a <i>tabber</i>. </p>
<p> Each tab-manager can store any number of windows, each in its own <i>tab</i>. The number of tab-managers is limited only by system resources. Tab-managers can even be nested/swallowed within other tab-managers. (ie. a tab-manager can be added as an individual tab to another tab-manager.)</p>
<h2>Invocation</h2>
<p><code>FvwmTabs</code> can be invoked by inserting the line <tt>&quot;Module FvwmTabs&quot;</tt> in your .fvwmrc file. This can be placed on a line by itself, if <code>FvwmTabs</code> is to be spawned during fvwm&#8217;s initialization, or can be bound to a menu or mouse button or keystroke to invoke it later.</p>
<h2>Installing Dependencies</h2>
<p><code>FvwmTabs</code> requires 2 <font SIZE="-1">CPAN</font> modules (that are <font SIZE="-1">NOT</font> distributed with fvwm) to be installed on your system. They are <i>Tk</i> and <i>X11::Protocol</i>. </p>
<p> They are available at: &lt;<a rel="nofollow" href="http://search.cpan.org/CPAN/authors/id/N/NI/NI-S/Tk-804.027.tar.gz">http://search.cpan.org/CPAN/authors/id/N/NI/NI-S/Tk-804.027.tar.gz</a>&gt; and &lt;<a href="http://search.cpan.org/~smccam/X11-Protocol-0.56/">http://search.cpan.org/~smccam/X11-Protocol-0.56/</a>&gt;. </p>
<p> To install either package: </p>
<p> tar zxvf <tt>$name</tt>.tar.gz ; cd <tt>$name</tt> ; perl Makefile.PL ; make install </p>
<p> <code>FvwmTabs</code> will tell you if you do not have these packages installed when you (try to) start it.</p>
<h2>Configuration Options</h2>
<p><code>FvwmTabs</code> reads the same config file as fvwm when it starts up. </p>
<p> The following options are recognised by <code>FvwmTabs</code>:</p>
<dl>
<dt>*FvwmTabs: activeFG <i>color</i></p>
<dd>The text color of the button for the visible tab. The default color is yellow.</p>
<dt>*FvwmTabs: activeBG <i>color</i></p>
<dd>The backgound color of the button for the visible tab. The default color is MidnightBlue.</p>
<dt>*FvwmTabs: inactiveFG <i>color</i></p>
<dd>The text color of the buttons for the invisible tabs. The default color is antiquewhite.</p>
<dt>*FvwmTabs: inactiveBG <i>color</i>&gt;</p>
<dd>The backgound color of the buttons for the invisible tabs. The default color is royalblue.</p>
<dt>*FvwmTabs: titleFG <i>color</i></p>
<dd>The text color used in the titlebar. The default color is black.</p>
<dt>*FvwmTabs: titleBG <i>color</i></p>
<dd>The background color used in the titlebar. The default color is antiquewhite.</p>
<dt>*FvwmTabs: activeRelief <i>style</i></p>
<dd>The relief style to use for active buttons. <i>style</i> can be either <i>raised</i>, <i>flat</i> or <i>sunken</i>. The default style is <i>sunken</i>.</p>
<dt>*FvwmTabs: inactiveRelief <i>style</i></p>
<dd>The relief style to use for inactive buttons. <i>style</i> can be either <i>raised</i>, <i>flat</i> or <i>sunken</i>. The default style is <i>flat</i>.</p>
<dt>*FvwmTabs: buttonYPadding <i>pixels</i></p>
<dd>How much padding to use around top and bottom of tab buttons. The default value is <i>3</i> pixels.</p>
<dt>*FvwmTabs: pollRate <i>ms</i></p>
<dd>Specifies how often to check for X events. <i>ms</i> is time in milliseconds. The default value, <i>250</i>, should be fine for most users. If you are on a very slow machine you may wish to increase this.</p>
<dt>*FvwmTabs: buttonFont <i>font</i></p>
<dd>The font to use on the tab buttons. The default font is <i>Helvetica -12 bold</i>.</p>
<dt>*FvwmTabs: titleFont <i>font</i></p>
<dd>The font to use on the titlebar. The default font is <i>Helvetica -12</i>.</p>
<dt>*FvwmTabs: menuFont <i>font</i></p>
<dd>The font to use on the menus. The default font is <i>Helvetica -12</i>.</p>
<dt>*FvwmTabs: fontSelector <i>fontProgram</i></p>
<dd>The external font chooser program to launch when dynamically changing fonts. The default <i>fontProgram</i> is <i>gfontsel &#8211;print -f &#8220;%f&#8221;</i>. Anti-gnome users might try <i>xfontsel -print -pattern &#8220;%f&#8221;</i>. If set to <i>none</i>, no font menu options will appear.</p>
<dt>*FvwmTabs: autoSwallowClass <i>className</i> [<i>tabManagerId</i>], &#8230;</p>
<dd>
<dt>*FvwmTabs: autoSwallowResource <i>resourceName</i> [<i>tabManagerId</i>], &#8230;</p>
<dd>
<dt>*FvwmTabs: autoSwallowName <i>name</i> [<i>tabManagerId</i>], &#8230;</p>
<dd>Specify windows to swallow automatically. These are comma-separated lists that specify the class/resource/name of a window &amp; an optional tab-manager id into which the window should be swallowed. By default, the tab-manager id increments from zero &#8211; ie. 0 is the first tab-manager created, 1 the second, etc, but it may be overridden by specifying an argument to the <i>NewTabber</i> function. (No whitespace is allowed in tabber ids.) You can alternatively specify &#8216;any&#8217; or &#8216;lastFocus&#8217; which will put the window in the tab-manager with the least number of tabs or the last focused tab-manager, respectively. If no tab-manager number is specified, an implicit default value of &#8216;any&#8217; is used. Note that <i>className</i>/<i>resourceName</i>/<i>name</i> can be a (Perl) regular expression.</p>
<dt>*FvwmTabs: balloonBG <i>color</i></p>
<dd>The backgound color of the balloon popups that appear over the tab buttons. The default color is <i>#C0C080</i>.</p>
<dt>*FvwmTabs: balloonFont <i>font</i></p>
<dd>The font to use on the balloon popups. The default font is <i>Helvetica -12</i>.</p>
<dt>*FvwmTabs: balloonWait <i>ms</i></p>
<dd>How long the mouse cursor must pause (in milliseconds) over a tab button before the balloon pops up. The default value is <i>250</i>.</p>
<dt>*FvwmTabs: balloonMsg <i>msg</i></p>
<dd>Message to display in balloon popups. The default value is <i></i>%tabNo:<i>
%iconText
%title</i>.</p>
<dt>*FvwmTabs: autoResize <i>bool</i></p>
<dd><i>bool</i> can be either <i>true</i> or <i>false</i>. If true, windows in the tab-manager automatically resize to the dimensions of the largest window in the tab-manager. The default value is <i>false</i>. If the user performs an explicit resize of a tab-manager window, all windows in the tab-manager are resized to the new window size.</p>
<dt>*FvwmTabs: stateFile <i>file</i></p>
<dd><code>FvwmTabs</code> has the ability to preserve its state (ie. remember the windows it has swallowed as tabs) b/w fvwm restarts. <i>file</i> specifies the name of a temporary file to record the state in, so it can be reconstructed when <code>FvwmTabs</code> restarts. The default file is <tt>&quot;$FVWM_USERDIR/.fvwmtabs.state&quot;</tt>.</p>
<dt>*FvwmTabs: fixedSizeTabs <i>bool</i></p>
<dd><i>bool</i> can be either <i>true</i> or <i>false</i>. If true, the tab-manager will ensure each tab-button has the same dimensions. If false, the selected tab is expanded so that it is fully visible. The default value is <i>false</i>.</p>
<dt>*FvwmTabs: showTitlebar <i>bool</i></p>
<dd>Show internal titlebar. If set to <i>true</i> a titlebar appears below the row of tab-buttons &amp; displays the title associated with the current window. This titlebar is capable of displaying long or multi-line titles. The default value is <i>true</i>.</p>
<dt>*FvwmTabs: useTMTitlebar <i>bool</i></p>
<dd>Add the title associated with the selected tab to the tab-manager titlebar. (ie. the titlebar at the top of the window, distinct from the titlebar below the tab-buttons.) Default value is <i>true</i>.</p>
<dt>*FvwmTabs: dragDropIcon <i>imageFile</i></p>
<dd>Specify the icon to display when performing a drag-&amp;-drop operation to reorder the tab-buttons. FvwmTabs will search the ImagePath for this image unless an absolute filename (ie. filename begins with &#8216;/&#8217;) is specified. The default value is <i>none</i>. If <i>none</i> (or an invalid file) is specified a * is used.</p>
<dt>*FvwmTabs: bBuggyFocus <i>bool</i></p>
<dd>FvwmTabs tries to work around a limitation in Perl/Tk (there is no way to access the timestamp associated with <font SIZE="-1">WM_TAKE_FOCUS</font> events). On some systems this doesn&#8217;t work and sometimes tab-managers have trouble acquiring the focus. If this happens to you, try setting this option to <i>true</i>. This can lead to focussing race-conditions (tab-managers temporarily &#8220;steal&#8221; focus in some situations) but this is less annoying than not being able to focus at all.</p>
<dt>*FvwmTabs: enableSwallowDND <i>bool</i></p>
<dd>Swallow windows that (are moved to) overlap a tabber. Note: drag-&amp;-drop can be enabled for individual tabbers via the menu. The default value is <i>true</i>.</p>
<dt>*FvwmTabs: swallowDNDTolerance <i>tol</i></p>
<dd>Determines how much a window must overlap a tabber for it to be swallowed when drag-&amp;-drop is enabled. If the value has a %-sign appended to it, windows must overlap by the specified percentage of the current size of the tabber. If no %-sign is present, the value is treated in units of pixels. The default value is <i>10</i> (pixels).</p>
<dt>*FvwmTabs: useIconsOnTabs <i>bool</i></p>
<dd>Show the mini icon associated with each window on its tab button. Note: mini icons for apps that use <font SIZE="-1">EWMH</font> icons look a bit distorted. This is because of the poor image resizing algorithm used in Tk. This should be rectified in the near future. The default value is <i>true</i>.</p>
<dt>*FvwmTabs: killIcon <i>image</i></p>
<dd>Image to use on kill toolbar button. Default is <i>none</i>.</p>
<dt>*FvwmTabs: addIcon <i>image</i></p>
<dd>Image to use on add toolbar button. Default is <i>none</i>.</p>
<dt>*FvwmTabs: swallowIcon <i>image</i></p>
<dd>Image to use on add toolbar button when tabber will swallow next window to popup. Default is <i>none</i>. By using a separate icon to <i>addIcon</i>, this option provides visual feedback on when a tabber will unconditionally swallow the next window to popup.</p>
<dt>*FvwmTabs: releaseIcon <i>image</i></p>
<dd>Image to use on release toolbar button. Default is <i>none</i>.</p>
<dt>*FvwmTabs: menuIcon <i>image</i></p>
<dd>Image to use on menu toolbar button. Default is <i>none</i>.</dl>
<h2>Fvwm Functions For Key Bindings</h2>
<p>A number of fvwm functions are available once the <code>FvwmTabs</code> module is started.</p>
<dl>
<dt>NewTabber</p>
<dd>Create a new tabber. Optional argument is tabber name. No whitespace is allowed in the tabber name. Can also prefix &#8211;geometry argument. </p>
<p> Example: NewTabber &#8211;geometry=+200+400 scottie</p>
<dt>Tabize</p>
<dd>Add a window (as a tab) to a tabber.</p>
<dt>NextTab</p>
<dd>Show/select the next tab.</p>
<dt>PrevTab</p>
<dd>Show/select the previous tab.</p>
<dt>LastTab</p>
<dd>Show/select the last selected tab (if there was one).</p>
<dt>ReleaseTab</p>
<dd>Release a tabbed window back to fvwm.</p>
<dt>ReleaseIconifyTab</p>
<dd>Release a tabbed window back to fvwm &amp; iconify it.</p>
<dt>ReleaseAllTabs</p>
<dd>Release all windows in a tab-manager back to fvwm.</p>
<dt>ReleaseIconifyAllTabs</p>
<dd>Release all windows in a tab-manager back to fvwm &amp; iconify them.</p>
<dt>CloseTabber</p>
<dd>Destroy a tab-manager. All windows in the tab-manager are released back to fvwm.</p>
<dt>AddTab</p>
<dd>Pick a new window to add to a tab-manager. Selecting this option &amp; clicking on a window will add the selected window to the tab-manager.</p>
<dt>MultiAddTab</p>
<dd>Pick &amp; add new windows to a tab-manager until <font SIZE="-1">ESC</font> is pressed.</p>
<dt>ShowTab <i>tabNo</i></p>
<dd>Show/select tab <i>tabNo</i> in the tab-manager. <i>tabNo</i> is zero-based. ie. 0 is the first tab, 1 is the second, etc.</p>
<dt>AddToTabber</p>
<dd>Add a window (as a tab) to a tab-manager.</p>
<dt>SwapLeft</p>
<dd>Swap the selected window with the window on its immediate left.</p>
<dt>SwapRight</p>
<dd>Swap the selected window with the window on its immediate right.</p>
<dt>SelectTabber</p>
<dd>Select a tab-manager for a new window to be added to.</p>
<dt>EnableDND</p>
<dd>Swallow windows that (are moved to) overlap a tabber.</dl>
<h2>Key Bindings</h2>
<p>By default, <code>FvwmTabs</code> reads a default user configuration file <i>FvwmTabs-DefaultSetup</i> which defines several useful key-bindings for <code>FvwmTabs</code>. You can tell <code>FvwmTabs</code> <font SIZE="-1">NOT</font> to read this file with <tt>&quot;SetEnv FvwmTabs_NoDefaultSetup&quot;</tt> &#8211; this environment variable must be set <i>before</i> starting the module. </p>
<p> All of the key bindings can be changed using the standard fvwm <i>Key</i> command &amp; making use of the aforementioned fvwm functions. ie. </p>
<p> Key (FvwmTabs*) A A <font SIZE="-1">CM</font> Function AddTab </p>
<p> Then, pressing Ctrl-Alt-a (when the focus is in a tab-manager) will allow you to click on a window to add to the tab-manager. </p>
<p> The default key bindings (set in the <i>FvwmTabs-DefaultSetup</i> file) are:</p>
<dl>
<dt>Ctrl-Alt-a</p>
<dd>AddTab</p>
<dt>Ctrl-Alt-c</p>
<dd>CloseTabber</p>
<dt>Ctrl-Alt-i</p>
<dd>ReleaseIconifyTab</p>
<dt>Ctrl-Alt-Shift-I</p>
<dd>ReleaseIconifyAllTabs</p>
<dt>Ctrl-Alt-l</p>
<dd>LastTab</p>
<dt>Ctrl-Alt-m</p>
<dd>MultiAddTab</p>
<dt>Ctrl-Alt-n &amp; Ctrl-Alt-Tab</p>
<dd>NextTab</p>
<dt>Ctrl-Alt-p</p>
<dd>PrevTab</p>
<dt>Ctrl-Alt-r</p>
<dd>ReleaseTab</p>
<dt>Ctrl-Alt-Shift-R</p>
<dd>ReleaseAllTabs</p>
<dt>Ctrl-Alt-t</p>
<dd>NewTabber</p>
<dt>Ctrl-Alt-<i>num</i></p>
<dd>ShowTab <i>num</i>.</p>
<dt>Ctrl-Alt-Left</p>
<dd>SwapLeft</p>
<dt>Ctrl-Alt-Right</p>
<dd>SwapRight</dl>
<h2>Mouse Bindings</h2>
<p><code>Mouse bindings on Tab Buttons</code> </p>
<p> <i>Mouse-1</i> on a tab-button displays the window associated with the tab. </p>
<p> <i>Mouse-2</i> on a tab-button releases the window associated with the tab back to the window manager as a standalone window. </p>
<p> <i>Mouse-3</i> on a tab-button releases the window associated with the tab back to the window manager &amp; iconifies it. </p>
<p> The tab-buttons can be reordered with a drag-&amp;-drop operation initiated with <i>Ctrl-Mouse-2</i>. A dragged tab is inserted before the tab-button onto which it is dropped. </p>
<p> <code>Mouse bindings on Toolbar Icons</code> </p>
<p> <i>Mouse-1</i> on the &#8220;menu&#8221; button will bring up a menu of options. See <font SIZE="-1">MENU</font> <font SIZE="-1">BINDINGS</font>. </p>
<p> <i>Mouse-1</i> on the &#8220;release&#8221; button will release the selected window from the tabber. </p>
<p> <i>Mouse-2</i> on the &#8220;release&#8221; button will release all windows from the tabber, and iconify them. </p>
<p> <i>Mouse-3</i> on the &#8220;release&#8221; button will release all windows from the tabber. </p>
<p> <i>Mouse-1</i> on the &#8220;add&#8221; button will add the next window you click on to the tabber. </p>
<p> <i>Mouse-2</i> on the &#8220;add&#8221; button will add the next window to popup to the tabber. </p>
<p> <i>Mouse-3</i> on the &#8220;add&#8221; button will add every window you click on (until you press Esc) to the tabber. </p>
<p> <i>Mouse-1</i> on the &#8220;kill&#8221; button will <i>Close</i> the selected window. </p>
<p> <i>Mouse-2</i> on the &#8220;kill&#8221; button causes <i>FvwmTabs</i> to try to kill the selected window itself. </p>
<p> <i>Mouse-3</i> on the &#8220;kill&#8221; button will <i>Kill</i> the selected window.</p>
<h2>Menu Bindings</h2>
<p><i>Mouse-1</i> on the &#8220;menu&#8221; button will bring up a menu of options: </p>
<p> <i>Release All</i> will release all tabbed programs back to the window manager as standalone windows. </p>
<p> <i>Release All (Iconify)</i> will release all tabbed programs back to the window manager as iconised standalone windows. </p>
<p> <i>Add</i> will add the next mouse-clicked window to the tab-manager. </p>
<p> <i>Add Next</i> will add the next window that is created to the tab-manager. </p>
<p> <i>Multi Add</i> keeps adding mouse-clicked windows to a tab-manager until the escape key is pressed. Useful for adding multiple windows to a tab-manager at once. </p>
<p> <i>Font</i> shows a sub-menu enabling you to dynamically configure the button/title/menu fonts, using the external program identified by the <i>fontSelector</i> option. </p>
<p> <i>Show Titlebar</i> toggles the display of the titlebar below the tab-buttons. </p>
<p> <i>Window Tabizer Dialog</i> will popup a dialog box for specifying windows to swallow. Windows can be specified explicitly (by name) or by using a (Perl) regular expression matcher. (Note: / character is automatically escaped.) </p>
<p> The menu options between the separators will display the window/tab associated with the text. (The menu text is actually the title associated with the window. The text on each tab-button is the icon name.) </p>
<p> <i>About</i> pops up a dialog with version/developer information. </p>
<p> <i>Close</i> will close the <code>FvwmTabs</code> window, invoking Release All in the process.</p>
<h2>Bugs</h2>
<dl>
<dt>&bull;</p>
<dd>Tab-managers don&#8217;t take focus when iconified.</p>
<dt>&bull;</p>
<dd>FvwmTabs doesn&#8217;t obey <tt>&quot;ClickToFocus&quot;</tt> mode.</p>
<dt>&bull;</p>
<dd>FvwmTabs has a problem swallowing shaded windows.</p>
<dt>&bull;</p>
<dd>Using <tt>&quot;Maximise&quot;</tt> to resize tab-manager windows prevents dynamic resizing from working.</dl>
<p> Please send bug reports, feature requests &amp; queries about <code>FvwmTabs</code> to the fvwm mailing list: <i>fvwm [at] fvwm.org</i>. Be sure to include the word &#8220;FvwmTabs&#8221; somewhere in the subject line.</p>
<h2>Todo</h2>
<p>Features to be added to <code>FvwmTabs</code> in the future (in no particular order):</p>
<dl>
<dt>&bull;</p>
<dd>Colorset support. (use Colorset tracker from fvwm-perllib)</p>
<dt>&bull;</p>
<dd>Use Ctrl-Mouse-1 instead of Ctrl-Mouse-2 to reorder (drag-&amp;-drop) windows.</p>
<dt>&bull;</p>
<dd>option: menu item to sort tabs by name, file extension, etc.</p>
<dt>&bull;</p>
<dd>For autoSwallow options that specify a tab-manager, create the tab-manager if it doesn&#8217;t already exist. (default behaviour is not to swallow it)</dl>
<h2>Fvwmtabs Homepage</h2>
<p>There is some useful information about FvwmTabs, including a short tutorial, on the authors website: </p>
<p> &lt;<a rel="nofollow" href="http://members.optusnet.com.au/~scottsmedley/fvwmtabs/">http://members.optusnet.com.au/~scottsmedley/fvwmtabs/</a>&gt;.</p>
<h2>Licensing</h2>
<p><code>FvwmTabs</code> is <font SIZE="-1">GPL</font> software. </p>
<p> See &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;</p>
<h2>Author</h2>
<p>Scott Smedley &lt;ss [at] aao.gov.au&gt;</p>
