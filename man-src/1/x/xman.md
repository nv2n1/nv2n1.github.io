---
title: "xman(1)"
name: "xman"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xman/"
description: "xman – Manual page display program for the X Window System"
---

<h2 class="name">NAME</h2>
<p> xman &#8211; Manual page display program for the X Window System </p>
<h2>SYNOPSIS</h2>
<p> <code>xman</code> [ <i>-options</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xman</i> is a manual page browser. The default size of the initial <i>xman</i> window is small so that you can leave it running throughout your entire login session. In the initial window there are three options: <i>Help</i> will pop up a window with on-line help, <i>Quit</i> will exit, and <i>Manual Page</i> will pop up a window with a manual page browser in it. Typing Control-S will pop up a window prompting for a specific manual page to display. You may display more than one manual page browser window at a time from a single execution of <i>xman</i>. </p>
<p> For further information on using <i>xman</i>, please read the on-line help information. Most of this manual will discuss customization of <i>xman</i>.</p>
<h2>OPTIONS</h2>
<p> Xman supports all standard Toolkit command line arguments (see <i><a href="/docs/linux/man/7-x/">X</a></i>(7)). The following additional arguments are supported. </p>
<dl>
<dt><code>-helpfile</code> <i>filename</i></p>
<dd> Specifies a helpfile to use other than the default.</p>
<dt><code>-bothshown</code></p>
<dd> Allows both the manual page and manual directory to be on the screen at the same time.</p>
<dt><code>-notopbox</code></p>
<dd> Starts without the Top Menu with the three buttons in it.</p>
<dt><code>-geometry</code> <i>WxH+X+Y</i></p>
<dd> Sets the size and location of the Top Menu with the three buttons in it.</p>
<dt><code>-pagesize</code> <i>WxH+X+Y</i></p>
<dd> Sets the size and location of all the Manual Pages.</dl>
<h2>CUSTOMIZING XMAN</h2>
<p> <i>Xman</i> allows customization of both the directories to be searched for manual pages, and the name that each directory will map to in the <i>Sections</i> menu. Xman determines which directories it will search by reading the <i>MANPATH</i> environment variable. If no <i>MANPATH</i> is found then the directory is /usr/man is searched on POSIX systems. This environment is expected to be a colon-separated list of directories for xman to search. </p>
<pre>
setenv MANPATH /mit/kit/man:/usr/man
</pre>
<p> By default, <i>xman</i> will search each of the following directories (in each of the directories specified in the users MANPATH) for manual pages. If manual pages exist in that directory then they are added to list of manual pages for the corresponding menu item. A menu item is only displayed for those sections that actually contain manual pages. </p>
<table>
<tr VALIGN=top>
<td>Directory</td>
<td>Section Name
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/1-man1/">man1</a></td>
<td>(1) User Commands
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/2-man2/">man2</a></td>
<td>(2) System Calls
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-man3/">man3</a></td>
<td>(3) Subroutines
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/4-man4/">man4</a></td>
<td>(4) Devices
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/5-man5/">man5</a></td>
<td>(5) File Formats
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/6-man6/">man6</a></td>
<td>(6) Games
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/7-man7/">man7</a></td>
<td>(7) Miscellaneous
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/8-man8/">man8</a></td>
<td>(8) Sys. Administration
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/l-manl/">manl</a></td>
<td>(l) Local
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/n-mann/">mann</a></td>
<td>(n) New
</td>
</tr>
<tr VALIGN=top>
<td>mano</td>
<td>(o) Old
</td>
</tr>
</table>
<p> For instance, a user has three directories in her manual path and each contain a directory called <i>man3</i>. All these manual pages will appear alphabetically sorted when the user selects the menu item called <i>(3) Subroutines</i>. If there is no directory called <i>mano</i> in any of the directories in her MANPATH, or there are no manual pages in any of the directories called <i>mano</i> then no menu item will be displayed for the section called <i>(o) Old</i>.</p>
<h2>BSD AND LINUX SYSTEMS</h2>
<p> In newer BSD and Linux systems, <i>Xman</i> will search for a file named <i>/etc/man.conf</i> which will contain the list of directories containing manual pages. See <i><a href="/docs/linux/man/5-man-conf/">man.conf</a></i>(5) for a complete description of the file format.</p>
<h2>THE MANDESC FILE</h2>
<p> By using the <i>mandesc</i> file a user or system manager is able to more closely control which manual pages will appear in each of the sections represented by menu items in the <i>Sections</i> menu. This functionality is only available on a section by section basis, and individual manual pages may not be handled in this manner. (Although generous use of symbolic links &#8212; see <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1) &#8212; will allow almost any configuration you can imagine.) </p>
<p> The format of the mandesc file is a character followed by a label. The character determines which of the sections will be added under this label. For instance suppose that you would like to create an extra menu item that contains all programmer subroutines. This label should contain all manual pages in both sections two and three. The <i>mandesc</i> file would look like this: </p>
<pre>
2Programmer Subroutines
3Programmer Subroutines
</pre>
<p> This will add a menu item to the <i>Sections</i> menu that would bring up a listing of all manual pages in sections two and three of the Programmers Manual. Since the label names are <i>exactly</i> the same they will be added to the same section. Note, however, that the original sections still exist. </p>
<p> If you want to completely ignore the default sections in a manual directory then add the line: </p>
<pre>
no default sections
</pre>
<p> anywhere in your mandesc file. This keeps xman from searching the default manual sections <i>In that directory only</i>. As an example, suppose you want to do the same thing as above, but you don&#8217;t think that it is useful to have the <i>System Calls</i> or <i>Subroutines</i> sections any longer. You would need to duplicate the default entries, as well as adding your new one. </p>
<pre>
no default sections
<a href="//www.systutorials.com/docs/linux/man/1-1/">1</a>(1) User Commands
2Programmer Subroutines
3Programmer Subroutines
<a href="//www.systutorials.com/docs/linux/man/4-4/">4</a>(4) Devices
<a href="//www.systutorials.com/docs/linux/man/5-5/">5</a>(5) File Formats
<a href="//www.systutorials.com/docs/linux/man/6-6/">6</a>(6) Games
<a href="//www.systutorials.com/docs/linux/man/7-7/">7</a>(7) Miscellaneous
<a href="//www.systutorials.com/docs/linux/man/8-8/">8</a>(8) Sys. Administration
<a href="//www.systutorials.com/docs/linux/man/l-l/">l</a>(l) Local
<a href="//www.systutorials.com/docs/linux/man/n-n/">n</a>(n) New
o(o) Old
</pre>
<p> Xman will read any section that is of the form <i>man&lt;character&gt;</i>, where &lt;character&gt; is an upper or lower case letter (they are treated distinctly) or a numeral (0-9). Be warned, however, that <a href="/docs/linux/man/1-man/">man</a>(1) and <a href="/docs/linux/man/8-catman/">catman</a>(8) will not search directories that are non-standard.</p>
<h2>WIDGETS</h2>
<p> In order to specify resources, it is useful to know the hierarchy of the widgets which compose <i>xman</i>. In the notation below, indentation indicates hierarchical structure. The widget class name is given first, followed by the widget instance name. </p>
<pre>
Xman xman       <i>(This widget is never used)</i>
        TopLevelShell  topBox
                Form  form
                        Label  topLabel
                        Command  helpButton
                        Command  quitButton
                        Command  manpageButton
                TransientShell  search
                        DialogWidgetClass  dialog
                                Label  label
                                Text  value
                                Command  manualPage
                                Command  apropos
                                Command  cancel
                TransientShell  pleaseStandBy
                        Label  label
        TopLevelShell  manualBrowser
                Paned  Manpage_Vpane
                        Paned  horizPane
                                MenuButton  options
                                MenuButton  sections
                                Label  manualBrowser
                        Viewport  directory
                                List  directory
                                List  directory
                                .
                                . (one for each section,
                                .  created on the fly)
                                .
                        ScrollByLine  manualPage
                SimpleMenu  optionMenu
                        SmeBSB  displayDirectory
                        SmeBSB  displayManualPage
                        SmeBSB  help
                        SmeBSB  search
                        SmeBSB  showBothScreens
                        SmeBSB  removeThisManpage
                        SmeBSB  openNewManpage
                        SmeBSB  showVersion
                        SmeBSB  quit
                SimpleMenu  sectionMenu
                        SmeBSB  &lt;name of section&gt;
                                .
                                . (one for each section)
                                .
                TransientShell  search
                        DialogWidgetClass  dialog
                                Label  label
                                Text  value
                                Command  manualPage
                                Command  apropos
                                Command  cancel
                TransientShell  pleaseStandBy
                        Label  label
                TransientShell  likeToSave
                        Dialog  dialog
                                Label  label
                                Text  value
                                Command  yes
                                Command  no
        TopLevelShell  help
                Paned  Manpage_Vpane
                        Paned  horizPane
                                MenuButton  options
                                MenuButton  sections
                                Label  manualBrowser
                        ScrollByLine  manualPage
                SimpleMenu  optionMenu
                        SmeBSB  displayDirectory
                        SmeBSB  displayManualPage
                        SmeBSB  help
                        SmeBSB  search
                        SmeBSB  showBothScreens
                        SmeBSB  removeThisManpage
                        SmeBSB  openNewManpage
                        SmeBSB  showVersion
                        SmeBSB  quit
</pre>
<h2>APPLICATION RESOURCES</h2>
<p> <i>xman</i> has the following application-specific resources which allow customizations unique to <i>xman</i>. </p>
<dl>
<dt><code>manualFontNormal</code> (Class <code>Font</code>)</p>
<dd> The font to use for normal text in the manual pages.</p>
<dt><code>manualFontBold</code> (Class <code>Font</code>)</p>
<dd> The font to use for bold text in the manual pages.</p>
<dt><code>manualFontItalic</code> (Class <code>Font</code>)</p>
<dd> The font to use for italic text in the manual pages.</p>
<dt><code>directoryFontNormal</code> (Class <code>Font</code>)</p>
<dd> The font to use for the directory text.</p>
<dt><code>bothShown</code> (Class <code>Boolean</code>)</p>
<dd> Either `true&#8217; or `false,&#8217; specifies whether or not you want both the directory and the manual page shown at start up.</p>
<dt><code>directoryHeight</code> (Class <code>DirectoryHeight</code>)</p>
<dd> The height in pixels of the directory, when the directory and the manual page are shown simultaneously.</p>
<dt><code>topCursor</code> (Class <code>Cursor</code>)</p>
<dd> The cursor to use in the top box.</p>
<dt><code>helpCursor</code> (Class <code>Cursor</code>)</p>
<dd> The cursor to use in the help window.</p>
<dt><code>manpageCursor</code> (Class <code>Cursor</code>)</p>
<dd> The cursor to use in the manual page window.</p>
<dt><code>searchEntryCursor</code> (Class <code>Cursor</code>)</p>
<dd> The cursor to use in the search entry text widget.</p>
<dt><code>pointerColor</code> (Class <code>Foreground</code>)</p>
<dd> This is the color of all the cursors (pointers) specified above. The name was chosen to be compatible with xterm.</p>
<dt><code>helpFile</code> (Class <code>File</code>)</p>
<dd> Use this rather than the system default helpfile.</p>
<dt><code>topBox</code> (Class <code>Boolean</code>)</p>
<dd> Either `true&#8217; or `false,&#8217; determines whether the top box (containing the help, quit and manual page buttons) or a manual page is put on the screen at start-up. The default is true.</p>
<dt><code>verticalList</code> (Class <code>Boolean</code>)</p>
<dd> Either `true&#8217; or `false,&#8217; determines whether the directory listing is vertically or horizontally organized. The default is horizontal (false).</dl>
<h2>GLOBAL ACTIONS</h2>
<p> <i>Xman</i> defines all user interaction through global actions. This allows the user to modify the translation table of any widget, and bind any event to the new user action. The list of actions supported by <i>xman</i> are:</p>
<dl>
<dt><code>GotoPage(</code><i>page</i><code>)</code></p>
<dd> When used in a manual page display window this will allow the user to move between a directory and manual page display. The <i>page</i> argument can be either <code>Directory</code> or <code>ManualPage</code>.</p>
<dt><code>Quit()</code></p>
<dd> This action may be used anywhere, and will exit xman.</p>
<dt><code>Search(</code><i>type</i><code>, </code><i>action</i><code>)</code></p>
<dd> Only useful when used in a search popup, this action will cause the search widget to perform the named search type on the string in the search popup&#8217;s value widget. This action will also pop down the search widget. The <i>type</i> argument can be either <code>Apropos</code>, <code>Manpage</code> or <code>Cancel</code>. If an <i>action</i> of <code>Open</code> is specified then xman will open a new manual page to display the results of the search, otherwise xman will attempt to display the results in the parent of the search popup.</p>
<dt><code>PopupHelp()</code></p>
<dd> This action may be used anywhere, and will popup the help widget.</p>
<dt><code>PopupSearch()</code></p>
<dd> This action may be used anywhere except in a help window. It will cause the search popup to become active and visible on the screen, allowing the user search for a manual page.</p>
<dt><code>CreateNewManpage()</code></p>
<dd> This action may be used anywhere, and will create a new manual page display window.</p>
<dt><code>RemoveThisManpage()</code></p>
<dd> This action may be used in any manual page or help display window. When called it will remove the window, and clean up all resources associated with it.</p>
<dt><code>SaveFormattedPage(</code><i>action</i>)</p>
<dd> This action can only be used in the <code>likeToSave</code> popup widget, and tells xman whether to <code>Save</code> or <code>Cancel</code> a save of the manual page that has just been formatted.</p>
<dt><code>ShowVersion()</code></p>
<dd> This action may be called from any manual page or help display window, and will cause the informational display line to show the current version of xman.</dl>
<h2>FILES</h2>
<dl>
<dt><i>&lt;manpath directory&gt;</i>/man&lt;<i>character</i>&gt;</p>
<dd>
<dt><i>&lt;manpath directory&gt;</i>/cat&lt;<i>character</i>&gt;</p>
<dd>
<dt><i>&lt;manpath directory&gt;</i>/mandesc</p>
<dd>
<dt>/etc/X11/app-defaults/Xman</p>
<dd> specifies required resources.</p>
<dt>/tmp</p>
<dd> <i>Xman</i> creates temporary files in /tmp for all unformatted man pages and all apropos searches.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-x/">X</a></i>(7), <i><a href="/docs/linux/man/1-man/">man</a></i>(1), <i><a href="/docs/linux/man/1-apropos/">apropos</a></i>(1), <i><a href="/docs/linux/man/8-catman/">catman</a></i>(8), <i>Athena Widget Set</i></p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> the default host and display to use.</p>
<dt><code>MANPATH</code></p>
<dd> the search path for manual pages. Directories are separated by colons (e.g. /usr/man:/mit/kit/man:/foo/bar/man).</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</p>
<dt><code>XAPPLRESDIR</code></p>
<dd> A string that will have &#8220;Xman&#8221; appended to it. This string will be the full path name of a user app-defaults file to be merged into the resource database after the system app-defaults file, and before the resources that are attached to the display.<br />
 See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</dl>
<h2>AUTHORS</h2>
<p> Chris Peterson, MIT X Consortium from the V10 version written by Barry Shein formerly of Boston University. Bug fixes and Linux support by Carlos A M dos Santos, for The XFree86 Project. </p>
<h2>Index</h2>
