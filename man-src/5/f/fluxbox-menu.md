---
title: "fluxbox-menu(5)"
name: "fluxbox-menu"
section: "5"
letter: "f"
url: "/docs/linux/man/5-fluxbox-menu/"
description: "fluxbox-menu –"
---

<p>fluxbox-menu &#8211; </p>
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) menu syntax</p>
<h2>Synopsis</h2>
<p>/usr/local/share/fluxbox/menu </p>
<p> ~/.fluxbox/menu </p>
<p> ~/.fluxbox/windowmenu</p>
<h2>Syntax</h2>
<p>Variable parameters are shown in emphasis: <i>argument</i> </p>
<p> All other characters shown are required verbatim. Whitespace is only required to delimit words, but it is fine to add more whitespace.</p>
<h2>Description</h2>
<p>There are two types of menus in fluxbox which can be configured. </p>
<p> The first is the root menu, which normally appears when you right-click on the desktop. </p>
<p> The first is the <code>ROOT MENU</code> (Or right-click menu), is usually bound to a right-click on the desktop, though this binding can be changed in the &#8216;keys&#8217; file (<code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code>). This same syntax is used for the <code>CustomMenu</code> command, also mentioned in <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code>. </p>
<p> Fluxbox installs a default root menu file in <code>/usr/local/share/fluxbox/menu</code>. You can also use fluxbox -i to confirm this location. Of course this system-wide menu can be customized for all users at once, but it is also possible to create an individual menu file for each user. By convention, users create a menu file in <code>~/.fluxbox/menu</code>. Once you&#8217;ve created your own menu file, you&#8217;ll want to make sure that you properly declare this location in your &#8216;init&#8217; file so that fluxbox knows where to look. See <code>RESOURCES</code>, below for details. </p>
<p> The second type is the <code>WINDOW MENU</code>, which defines the contents of the menu which appears when you right-click on a window&#8217;s titlebar or iconbar. This opens a menu file as defined by <code>~/.fluxbox/windowmenu</code>. If this file does not exist, fluxbox will copy in the default from <code>/usr/local/share/fluxbox/windowmenu</code>. </p>
<p> You do not need to &#8220;reload&#8221; fluxbox after editing the apps file, the changes should be taken into account the next time you open the menu.</p>
<h2>Root Menu</h2>
<p>The root menu must begin with a <code>[begin]</code> tag and end with an <code>[end]</code> tag, and every tag must be on its own line. </p>
<p> There are up to four fields in a menu line. They are of the form</p>
<dl>
<dd>[<i>tag</i>] (<i>label</i>) {<i>command</i>} &lt;&#8216;icon&#8217;&gt;</dl>
<p> The &lt;&#8216;icon&#8217;&gt; field is always optional when shown below. If specified, the <i>icon</i> will be scaled down and displayed in the menu alongside the text label of the item. It must be in .xpm or .png format. </p>
<p> Any line that starts with a <i>#</i> or <i>!</i> is considered a comment and ignored by fluxbox. Also, in the label/command/filename fields you can escape any character. Using <i>\</i> inserts a literal back-slash into the label/command/filename field. </p>
<p> You may enter labels, commands, and icons using characters from any <code><a href="/docs/linux/man/1-iconv/">iconv</a>(1)</code> language/locale by specifying the encoding used via the <code>[encoding]</code> tag, detailed below.</p>
<h3>Structural Tags</h3>
<p><code>[begin]</code> (<i>title</i>)</p>
<dl>
<dd>This tells fluxbox to start parsing the menu file. This tag is required for fluxbox to read your menu file. If it cannot find it, the system default menu is used in its place. The <i>title</i> appears at the top of the menu. And <code>[end]</code> tag is required to end the menu.</dl>
<p> <code>[submenu]</code> (<i>label</i>) {<i>title</i>} &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>This tells fluxbox to create and parse a new menu, which is inserted as a submenu into the parent menu. These menus are parsed recursively, so there is no limit to the number of levels or nested submenus you can have. The <i>label</i> is the text that will appear in the parent menu, and the <i>title</i> is shown at the top of the submenu. If omitted, the <i>title</i> will be the same as the <i>label</i>. An <code>[end]</code> tag is required to end the submenu.</dl>
<p> <code>[end]</code></p>
<dl>
<dd>This tells fluxbox that it is at the end of a menu. This can either be a <code>[submenu]</code> or the <code>[begin]</code> tag of the main root menu. There must be at least one of these tags in your menu to correspond to the required <code>[begin]</code> tag, and one for each <code>[submenu]</code>.</dl>
<p> <code>[encoding]</code> {<i>encoding</i>}</p>
<dl>
<dd>This begins an <code>[encoding]</code> section and specifies the string encoding of all strings until the matching <code>[endencoding]</code> tag. For a list of available encodings on your system, run <code>iconv -l</code>.</dl>
<p> <code>[endencoding]</code></p>
<dl>
<dd>This ends an <code>[encoding]</code> section.</dl>
<p> <code>[include]</code> (<i>path</i>)</p>
<dl>
<dd>Parses the file specified by filename inline with the current menu. The <i>path</i> can be the full path to a file or it can begin with <code>~/</code>, which will be expanded into your home directory. If <i>path</i> is a directory, then all files in that directory are included.</dl>
<p> <code>[separator]</code></p>
<dl>
<dd>This will create a nice separation line. Useful for splitting up sections in a &#8220;pretty&#8221; way. The optional <i>comment</i> is not displayed, but can be useful for internal documentation or script parsing of menu files.</dl>
<p> <code>[nop]</code> (<i>label</i>) &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>Insert a non-operational item into the current menu. This is much like <code>[separator]</code>, but instead of a line, it inserts a <i>label</i>. This can be used to help format the menu into blocks or sections if so desired. The <i>label</i> is optional, and if omitted a blank item will be inserted.</dl>
<h3>Applications</h3>
<p><code>[exec]</code> (<i>label</i>) {<i>command&#8230;</i>} &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>Inserts a command item into the menu. When you select the menu item from the menu, fluxbox runs <i>command&#8230;</i> in your <code>$SHELL</code> (or /bin/sh if $SHELL is not set). You can use this to launch applications, run shell scripts, etc. Since all arguments are passed verbatim to the shell, you can use environment variables, pipes, or anything else the shell can do. Note that processes only see environment variables that were set before fluxbox started (such as in ~/.fluxbox/startup).</dl>
<h3>Fluxbox Functions</h3>
<p><code>[config]</code> (<i>label</i>) &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>Inserts a fluxbox native submenu item, containing numerous configuration options concerning window placement, focus style, window moving style, etc. See <code>Configuration Menu</code> in <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> for details.</dl>
<p> <code>[reconfig]</code> (<i>label</i>) &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>When selected this item re-reads the current style and menu files and applies any changes. This is useful for creating a new style or theme, as you don&#8217;t have to constantly restart fluxbox every time you save your style. However, fluxbox automatically rereads the menu whenever it changes.</dl>
<p> <code>[restart]</code> (<i>label</i>) {<i>command</i>} &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>This tells fluxbox to restart. If <i>command</i> is supplied, it shuts down and runs the command (which is commonly the name of another window manager). If <i>command</i> is omitted, fluxbox restarts itself.</dl>
<p> <code>[exit]</code> (<i>label</i>) &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>Inserts an item that shuts down and exits fluxbox. Any open windows are reparented to the root window before fluxbox exits.</dl>
<p> <code>[style]</code> (<i>label</i>) {<i>filename</i>} &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>This tells fluxbox to insert an item that, when selected, reads style file named filename and apply the new textures, colors and fonts to the current running session.</dl>
<p> <code>[stylesmenu]</code> (<i>directory</i>) &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>Reads all filenames from the specified directory, assuming that they are all valid style files, and creates inline menu items in the current menu for every filename, that, when selected by the user will apply the selected style file to the current session. The labels that are created in the menu are the filenames of the style files.</dl>
<p> <code>[stylesdir]</code> (<i>label</i>) {<i>directory</i>} &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>Creates a submenu entry with <i>label</i> (that is also the title of the new submenu), and inserts in that submenu all filenames in the specified <i>directory</i>, assuming that they are all valid style files (directories are ignored) in the same way as the <code>[stylesdir]</code> command does. Both <code>[stylesdir]</code> and <code>[stylesmenu]</code> commands make it possible to install style files without editing your init file.</dl>
<p> <code>[wallpapers]</code> (<i>directory</i>) {<i>command</i>} &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>This inserts a menu item to set the wallpaper for each file in the given directory. The <i>command</i> is optional, and defaults to <code>fbsetbg</code>.</dl>
<p> <code>[workspaces]</code> (<i>label</i>) &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>This tells fluxbox to insert a link to the workspaces menu directly into your menu. See <code>Workspace Menu</code> in <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> for details.</dl>
<p> <code>[</code><i>command</i><code>]</code> (<i>label</i>) &lt;&#8216;icon&#8217;&gt;</p>
<dl>
<dd>In addition to the commands above, any legal keys file <i>command</i> may be used as a menu item. See <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code> for more information.</dl>
<h2>Window Menu</h2>
<p>Like the <code>ROOT MENU</code>, this menu file must start with <code>[begin]</code> and end with <code>[end]</code>. However, this file consists of only one <code>[</code><i>tag</i><code>]</code> per line with no labels, commands, or icons. </p>
<p> The available tags in this menu are: </p>
<p> <code>[shade]</code></p>
<dl>
<dd>Provides a menu item to shade or unshade (or, roll-up) the window. This is equivalent to the shade titlebar button.</dl>
<p> <code>[stick]</code></p>
<dl>
<dd>Provides a menu item to stick or unstick the window. Stuck windows are displayed on all workspaces. This is equivalent to the stick titlebar button.</dl>
<p> <code>[maximize]</code></p>
<dl>
<dd>Provides a menu item to maximize or unmaximize the window, equivalent to the maximize titlebar button. The button with which you click alters the behaviour of this item as follows: </p>
<dl>
<dd>&bull; Button 1 (Un)Maximize as normal.</dl>
<dl>
<dd>&bull; Button 2 (Un)Maximize window vertically.</dl>
<dl>
<dd>&bull; Button 3 (Un)Maximize window horizontally.</dl>
</dl>
<p> <code>[iconify]</code></p>
<dl>
<dd>Provides a menu item to iconify (or, minimize) the window, equivalent to the iconify titlebar button.</dl>
<p> <code>[close]</code></p>
<dl>
<dd>Closes the window gracefully, equivalent to the titlebar button.</dl>
<p> <code>[kill]</code></p>
<dl>
<dd>Kills the window&#8217;s process, like <code><a href="/docs/linux/man/1-xkill/">xkill</a>(1)</code>.</dl>
<p> <code>[raise]</code></p>
<dl>
<dd>Raise the window to the top of the stack within its layer.</dl>
<p> <code>[lower]</code></p>
<dl>
<dd>Lower the window to the bottom of the stack within its layer.</dl>
<p> <code>[settitledialog]</code></p>
<dl>
<dd>Opens a dialog which can be used to set the window&#8217;s title. Some applications may re-set their own title from time-to-time, wiping out your setting.</dl>
<p> <code>[sendto]</code></p>
<dl>
<dd>Sends the window to a different workspace. When you select the workspace with a middle-click, fluxbox will also change to the new workspace. A regular click only sends the window.</dl>
<p> <code>[layer]</code></p>
<dl>
<dd>Adds a &#8220;Layer&#8230;&#8221; submenu which lets you change the layer of this window.</dl>
<p> <code>[alpha]</code></p>
<dl>
<dd>Adds a &#8220;Transparency&#8230;&#8221; submenu which lets you change the focused and unfocused transparency of this window.</dl>
<p> <code>[extramenus]</code></p>
<dl>
<dd>Adds the &#8220;Remember&#8230;&#8221; menu item, which allows you to specify which settings should be stored in the &#8216;apps&#8217; file (See <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code> for more details).</dl>
<p> <code>[separator]</code></p>
<dl>
<dd>Adds a horizontal line to the menu</dl>
<h2>Files</h2>
<p><code>~/.fluxbox/menu</code></p>
<dl>
<dd>This is the default location for the user&#8217;s root menu.</dl>
<p> <code>/usr/local/share/fluxbox/menu</code></p>
<dl>
<dd>This is the system-wide root menu file. It will be used if the user&#8217;s root menu is missing or unparseable.</dl>
<p> <code>~/.fluxbox/windowmenu</code></p>
<dl>
<dd>This is the user&#8217;s window menu definition file</dl>
<p> <code>/usr/local/share/fluxbox/menu</code></p>
<dl>
<dd>This is the default window menu. If the user does not have this file, it will be copied to <code>~/.fluxbox/windowmenu</code> on fluxbox startup.</dl>
<h2>Resources</h2>
<p><code>session.menuFile:</code> <i>location</i></p>
<dl>
<dd>This may be set to override the location of the user&#8217;s root menu.</dl>
<h2>Environment</h2>
<p>The <i>comand&#8230;</i> field of the <code>[exec]</code> tag can take advantage of other environment variables if they are set before fluxbox is started.</p>
<h2>Examples</h2>
<p><code>Root Menu</code>.</p>
<dl>
<dd>
<pre># fluxbox menu file
[begin] (fluxbox)
 [exec] (rxvt) {rxvt -ls} &lt;/usr/X11R6/share/icons/terminal.xpm&gt;
 [exec] (netscape) {netscape -install}
 [exec] (The GIMP) {gimp}
 [exec] (XV) {xv}
 [exec] (Vim) {rxvt -geometry 132x60 -name VIM -e screen vim}
 [exec] (Mutt) {rxvt -name mutt -e mutt}
 [submenu] (mozilla)
 [exec] (browser) {mozilla -browser}
 [exec] (news) {mozilla -news}
 [exec] (mail) {mozilla -mail}
 [exec] (edit) {mozilla -edit}
 [exec] (compose) {mozilla -compose}
 [end]
 [submenu] (Window Manager)
 [exec] (Edit Menus) {nedit ~/.fluxbox/menu}
 [submenu] (Style) {Which Style?}
 [stylesdir] (~/.fluxbox/styles)
 [stylesmenu] (fluxbox Styles) {/usr/local/share/fluxbox/styles}
 [end]
 [config] (Config Options)
 [reconfig] (Reconfigure)
 [restart] (Restart)
 [end]
 [exit] (Log Out)
[end]</pre>
</dl>
<p> <code>Default Window Menu</code>.</p>
<dl>
<dd>
<pre>[begin]
 [shade]
 [stick]
 [maximize]
 [iconify]
 [raise]
 [lower]
 [settitledialog]
 [sendto]
 [layer]
 [alpha]
 [extramenus]
 [separator]
 [close]
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
<p><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1) <a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5) <a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5) <a href="/docs/linux/man/1-xkill/">xkill</a>(1) <a href="/docs/linux/man/1-iconv/">iconv</a>(1)</p>
<h2>Author</h2>
<p><code>Jim Ramsay</code> &lt;i.am [at] jimramsay.com&gt;</p>
<dl>
<dd>Author.</dl>
