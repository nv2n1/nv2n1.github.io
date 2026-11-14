---
title: "gentoo(1)"
name: "gentoo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gentoo/"
description: "gentoo – A highly configurable file manager for X"
---

<h2>NAME</h2>
<p> gentoo &#8211; A highly configurable file manager for X</p>
<h2>SYNOPSIS</h2>
<p> gentoo [&#8211;version] [&#8211;root-ok] [&#8211;no-rc] [&#8211;no-gtkrc] [&#8211;no-fam] [&#8211;left=path] [&#8211;right=path]</p>
<h2>DESCRIPTION</h2>
<p> gentoo is a file manager for Linux and compatible systems. It allows you to interactively navigate your file system using the mouse, and also to perform various fairly standard operations (such as copy, move, rename, &#8230;) on the files and directories contained therein. </p>
<p> gentoo always shows you the contents of two directories at once. Each of these is displayed in its own scrollable list, called a pane. At any time, exactly one pane is the <i>current</i> pane, and has a highlighted bar running across its top region. The current pane acts as the source for all file operations, while the other pane is the destination. You can select rows in panes using selection methods of varying complexity (from simply clicking a row, to selecting rows by name using a regular expression). Once you have a selection, you can click a button to perform some command on the selected files. </p>
<p> All file operations performed by gentoo are implemented natively. When you use gentoo to copy a file, for example, gentoo does <i>not</i> simply execute the system&#8217;s <code><a href="//www.systutorials.com/docs/linux/man/1L-cp/">cp</a></code>(1L) command. Rather, gentoo contains its own code for opening source and destination files, and then reading and writing the right amount of data between them. This way of doing things makes gentoo independent of the availability of shell commands to do things. </p>
<p> gentoo incorporates a fairly powerful, object-oriented file typing and styling system. It can use a variety of ways to determine the <code>type</code> of the files it is displaying. Each type is then linked to something called a <code>style,</code> which controls how rows of that type are rendered in panes. You can use this system to control icons, colors, and various operations on the rows. For example, it is easy to make gentoo display all PNG images in red, and to invoke <code>The <a href="/docs/linux/man/1-gimp/">GIMP</a></code>(1) on them when double-clicked. </p>
<p> A design goal with gentoo has been to provide full GUI configurability, removing the need to edit a configuration file by hand and restart the program to see the changes, as is otherwise common in many programs for Un*x. As a result of this, gentoo features a Configuration dialog window where you can configure most aspects of its operation directly, using the mouse and standard GUI widgets. </p>
<p> gentoo borrows its basic look&#8217;n&#8217;feel from the classic Amiga file manager Directory OPUS, but is not a &quot;clone&quot; of any kind.</p>
<h2>OPTIONS</h2>
<p> gentoo is not primarily driven by command line arguments, but the following are available:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Causes gentoo to print its version number (a string on the form MAJOR.MINOR.MICRO, like 0.15.6) to the standard output, and then exit successfully. Numbers having an odd MINOR component indicate development versions of the program.</p>
<dt><code>&#8211;locale-info</code></p>
<dd> Makes gentoo print a couple of localization settings, and then exit. This is mostly useful during development and debugging, and not of a lot of interest when just using the application.</p>
<dt><code>&#8211;root-ok</code></p>
<dd> Makes gentoo accept being run by the root user. Normally, this is not allowed since it is considered a big threat to system security. Note that gentoo has the ability to execute user-defined strings using the <code><a href="/docs/linux/man/3-execvp/">execvp</a></code>(3) function. This is generally considered harmful. However, if you <code>really</code> want to run gentoo while logged on as root, supplying this option allows you to. It is <code>not</code> recommended, though.</p>
<dt><code>&#8211;no-rc</code></p>
<dd> Starts up gentoo without loading any configuration file. This makes it run using the built-in defaults, which are <code>very</code> Spartan indeed. Seldom comfortable, but occasionally handy when trying to determine if a problem is with the configuration or with the core code.</p>
<dt><code>&#8211;no-gtkrc</code></p>
<dd> Avoids loading the GTK+ RC file, thus disabling any widget customizations, and forces all widgets to use the default GTK+ look.</p>
<dt><code>&#8211;no-fam</code></p>
<dd> Disables use of FAM (File Alteration Monitor) to detect when contents of a displayed pane change. Option only available if gentoo was built with FAM support to begin with.</p>
<dt><code>&#8211;left, &#8211;right (or -1, -2)</code></p>
<dd> Sets the initial path for the left and right pane, respectively. If present, the path specified with one of these options overrides any other path for the pane in question. See below (Initial Directory Paths) for details.</p>
<dt><code>&#8211;run ARG (or -rARG)</code></p>
<dd> Runs ARG, a gentoo command. Commands specified this way are executed before gentoo accepts any user input through the graphical interface, but after the configuration file has been read in. You can use it many times in order to make gentoo run a whole series of commands. Remember that gentoo&#8217;s command names are case-sensitive, and that built-in commands (like &quot;About&quot;) always begin with a capital letter.</dl>
<p> Any non-option command arguments will be silently ignored. If an argument &quot;-h&quot; or &quot;&#8211;help&quot; is given, gentoo will give a summary of its supported command line options and exit successfully. If an unknown option is given, or a option is missing a required argument, gentoo will whine and exit with a failure.</p>
<h2>BASIC USAGE</h2>
<p> When gentoo starts up, it will open up its single main window, which is split vertically (or horizontally; it&#8217;s configurable) down the middle, forming the two panes mentioned above. It also contains a bank of buttons along the bottom.</p>
<h3>Initial Directory Paths</h3>
<p> The actual paths shown in the two panes upon start-up can be controlled in various ways. There are four ways of getting a path to show up in pane. In order of decreasing priority, they are:</p>
<dl>
<dt>1. Command-line Argument</p>
<dd> Using the &#8211;left and &#8211;right (or their short forms, -1 and -2) command-line arguments overrides any other setting.</p>
<dt>2. Configured Default Directory</p>
<dd> If no command-line argument is present, and the &quot;Default Directory&quot; configuration option is set, that directory is used.</p>
<dt>3. Most Recently Visited Directory</p>
<dd> If no default directory exists, the most recently visited directory is taken from the directory history for each pane. This only works if a directory history file has been found and loaded.</p>
<dt>4. Current Directory</p>
<dd> If all else fails, gentoo uses the current directory (&quot;.&quot;).</dl>
<h3>Navigating</h3>
<p> Navigating around the file system using gentoo is very simple. The two panes act as independent views of the file system, and both are navigated in exactly the same way. </p>
<p> You can always see which directory a pane is showing by reading its path, shown in the entry box below (by default&#8211;you can change the position to above) the pane. </p>
<p> To enter a directory, locate it in the pane and double click it with the left mouse button. gentoo will read the directory&#8217;s contents, and update the display accordingly. </p>
<p> There are several ways of going <code>up</code> in the directory structure. To enter the directory containing the one currently shown (the current dir&#8217;s <code>parent</code>), you can: click the parent button (to the left of the path entry box); hit <code>Backspace</code> on your keyboard; click the middle mouse button; select &quot;Parent&quot; from the pop-up menu on the right mouse button, or click the downward arrow to the right of the path box (this pops up the directory history menu), then select the second row from the top.</p>
<h3>Selecting Files</h3>
<p> Before you can do anything to a file, you need to select it. All file-management commands in gentoo act upon the current selection (in the current pane). There are several ways of selecting files, but the most frequently used are mouse-based. Note that the word &quot;file&quot; used below really should be taken to mean &quot;file or directory&quot;, since selection doesn&#8217;t distinguish between the two. </p>
<p> To select a file (or directory), just point the mouse at the name (anywhere in the row is fine), and click the left mouse button. The colors of the clicked row will change, indicating that it is currently selected. To select more rows, keep the mouse button down, and drag the mouse vertically. gentoo extends the selection, including all rows touched. If you drag across the top or bottom border, the pane will scroll, trying to keep up. This is a very quick and convenient way of selecting multiple files, as long as they are listed in succession. </p>
<p> If you click again on an already selected file, you will unselect it. You can drag to unselect several files, just as when selecting. </p>
<p> To select a sequence of files without dragging, first click normally on the first file that you wish to select. Then release the mouse button, locate the last file in the sequence (it can be either above or below the first one), hold down <code>shift</code> on your keyboard, and click the wanted file. gentoo now adds all files between the first and the last to the current selection. </p>
<p> If you follow the instructions given above to select a sequence, but press <code>control</code> rather than <code>shift</code> before clicking the second time, gentoo will <i>unselect</i> the range of files indicated. </p>
<p> If you click on a file with the <code>meta</code> key held down (that&#8217;s actually a key labeled <code>Alt</code>, located to the immediate left of the space bar, on my PC keyboard), gentoo will do something cool: it will select (or unselect, it&#8217;s a toggle just like ordinary selection) all files, including the clicked one, that have the same <code>type</code> as the one you clicked. This can be used to select for example all PNG image files in a directory even if you can only see one. Occasionally very useful. </p>
<p> If you click on a file with both the <code>shift</code> and <code>control</code> keys held down, gentoo will toggle the selected state of all files having the same file name <i>extension</i> as the one you clicked. This can sometimes be useful to select files that you don&#8217;t have a proper <code>type</code> defined for, as long as those files do share an extension, that is.</p>
<h3>Changing Sort Order</h3>
<p> The files and directories listed in each of gentoo&#8217;s two panes are always sorted on some column: typically file name. You can chose to sort on some other field by clicking the appropriate column title once. If you click on the field that is already current, the sorting will be reversed (i.e., for names it will be Z-A rather than A-Z). </p>
<p> If your display includes icons, try sorting on that column: gentoo will then order each row according to its File Style, grouping the rows based on their parent styles, all the way up to the root of the Style tree. This means that, for example, JPEG and PNG pictures (both having an immediate parent style of Image) will be shown together, and before all Text files (HTML, man pages and so on). It&#8217;s quite cool, really. :)</p>
<h3>Executing Commands</h3>
<p> Commands are used to make gentoo <code>do</code> stuff. The typical command operates upon the set of selected files in the current pane, so it&#8217;s usually a good idea to first select some files. See the previous subsection for details on how to select files. Once you have a bunch of files selected, you need to tell gentoo which command to execute. There are several ways of doing this. </p>
<p> Most basic file operations (e.g. copy, move, rename, and so on) are found on the (cleverly labeled) buttons along the bottom of gentoo&#8217;s main window. To copy a file, just select it, then click the button labeled &quot;Copy&quot;. It&#8217;s really that simple. Most of these built-in (or <code>native</code>) commands automatically operate recursively on directories, so you could copy (or move) a whole directory of files by just selecting it and then clicking &quot;Copy&quot;. </p>
<p> If you can&#8217;t see a button that does what you want to do, there&#8217;s a chance that the command exists, but isn&#8217;t bound. Click the right mouse button in a pane, this opens up the &quot;pane pop-up menu&quot;. Select the &quot;Run&#8230;&quot; item. This opens up a dialog window showing all available commands. Select a command, and click &quot;OK&quot; to execute it.</p>
<h2>CONFIGURATION</h2>
<p> gentoo is a pretty complicated program; it has a rather large amount of configuration data that it needs in order to be really useful. For example, my current personal configuration file contains well over a thousand different configuration values. </p>
<p> To store this hefty amount of configuration data, gentoo uses a heavily structured configuration file. In fact, the file is (or at least it should be) legal XML! </p>
<p> When new features are added to gentoo, they will typically require some form of configuration data. This data is then simply added somewhere in the existing configuration file structure. Effort is made to assign reasonable built-in default values for all such new features, so older configuration files (that don&#8217;t contain the values required by the new features) should still work. The first time you hit &quot;Save&quot; in the configuration window after changing your version of gentoo, your personal configuration file will be updated to match the version of gentoo. </p>
<p> Describing how to go about configuring gentoo is too big a topic for a manual page to cover. I&#8217;ll just say that the command to open up the configuration window is called &quot;Configure&quot;. It is by default available on a button (typically the top-right one), in the pane pop-up menu, and also by pressing the <code>C</code> key on your keyboard. </p>
<h2>FILES</h2>
<dl>
<dt><i>~/.gentoorc</i></p>
<dd> A user&#8217;s personal configuration file. When gentoo starts up, it will try to load this file. If the file isn&#8217;t found, the site-wide configuration will be tried instead.</p>
<dt><i>/usr/local/etc/gentoorc</i></p>
<dd> This is the site-wide configuration file. If a user doesn&#8217;t have a configuration in his/her home directory, gentoo loads this file instead. The actual location of this file is slightly system-dependent, the above is the default. As an end user, you typically won&#8217;t need to access this file manually.</p>
<dt><i>~/.gentoo-history</i></p>
<dd> This file contains lists of the most recently visited directories, for both panes. These are the lists that appear in the drop-down menu when the arrow next to the path entry box is clicked. Can be disabled in the Dir Pane configuration.</p>
<dt><i>~/.gentoogtkrc</i></p>
<dd> This file allows you to control the look of the widgets used by gentoo, through the GTK+ style system. This file must be present in the user&#8217;s home directory &#8211; there is no site-wide GTK+ configuration file.</p>
<dt><i>/etc/passwd, /etc/group</i></p>
<dd> These two files normally hold the system&#8217;s password and group information. These are (probably) the ones gentoo uses to map user IDs to login names, to do tilde-expansion (mapping of user name to directory path), and to map group IDs to group names. That is <i>probably,</i> because gentoo doesn&#8217;t actually refer to these files by name. Instead, it uses the (BSD-style) API function calls <code><a href="/docs/linux/man/3-getpwent/">getpwent</a></code>(3) and <code><a href="/docs/linux/man/3-getgrent/">getgrent</a></code>(3) to access this information.</p>
<dt><i>/etc/fstab, /proc/mounts, (or /etc/mtab)</i></p>
<dd> These files contain data on available and mounted file systems. They are read by gentoo&#8217;s auto-mounting code. You can configure the exact file names used, on the &quot;Mounting&quot; tab in the main configuration window. Note that using <i>/proc/mounts</i> rather than <i>/etc/mtab</i> is recommended on Linux systems; they contain roughly the same data, but the one in /proc is always up to date, and faster to read!</dl>
<h2>BUGS</h2>
<p> All releases of gentoo numbered 0.x.y, where x (the so called <code>minor</code> version number) is odd, are to be considered <code>development</code> releases, as opposed to <code>stable</code> ones. This means that the software will probably suffer from bugs. If you find something that you suspect is indeed a bug, please don&#8217;t hesitate to contact the author! For details on how to do this, see below. </p>
<p> If you&#8217;re concerned about using potentially buggy and completely unwarranted software to manage your precious files, please feel free <code>not</code> to use gentoo. The world is full of alternatives. </p>
<p> The chances that a bug gets fixed increase greatly if you report it. When reporting a bug, you must describe how to reproduce it, and also try to be as detailed and precise as possible in your description of the actual bug. If possible, perhaps you should include the output of <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) (or whatever your system&#8217;s debugger is called). In some cases it might be helpful if you include the configuration file you were using when the problem occurred. Before reporting a bug, please make sure that you are running a reasonably recent version of the software, since otherwise &quot;your&quot; bug might already been fixed. See below for how to obtain new releases. </p>
<p> Also, you should locate and read through the <code>BUGS</code> file distributed with gentoo, so you don&#8217;t go through all this hassle just to report an already known bug, thereby wasting everybody&#8217;s time&#8230;</p>
<h2>AUTHOR</h2>
<p> gentoo was written, from scratch, by Emil Brink. The first line of code was written on May 15th, 1998. It is my first program to use the GTK+ GUI toolkit, my first program to be released under the GPL, and also my first really major Linux application. However, it is <code>not</code> my first program! ;^) I&#8217;ve been writing (increasingly complex) code for almost two decades now. I have recently finished my Master of Science degree in Computer Science and Engineering at the Royal Institute of Technology in Stockholm, Sweden. </p>
<p> The only efficient way to contact me (to report bugs, give praise, suggest features/fixes/extensions/whatever) is by Internet e-mail. My address is &lt;<code>emil [at] obsession.se</code>&gt;. <code>Please</code> try and include the word &quot;gentoo&quot; in the Subject part of your e-mail, to help me organize my inbox. Thanks.</p>
<h2>ACKNOWLEDGMENTS</h2>
<p> The author wishes to thank the following people for their various contributions to gentoo:</p>
<dl>
<dt>Johan Hanson (&lt;johan [at] tiq.com&gt;)</p>
<dd> Johan is the man behind all icon graphics in gentoo, and also the author of the custom widgets used in it. He also comes up with plenty of ideas for new features and changes to old ones, some of which are even implemented. Johan has stuff at &lt;<a rel="nofollow" href="http://www.bahnhof.se/~misagon/">http://www.bahnhof.se/~misagon/</a>&gt;.</p>
<dt>Jonas Minnberg (&lt;sasq [at] nightmode.org&gt;)</p>
<dd> Jonas did intensive testing of early versions of gentoo, and eventually persuaded me into releasing it (back around version 0.9.7 or so).</p>
<dt>Ulf Petterson (&lt;ulf [at] obsession.se&gt;)</p>
<dd> Ulf drew the main gentoo logo (the one shown in the About window), and also designed the main HTML documentation&#8217;s layout.</p>
<dt>Josip Rodin (&lt;jrodin [at] jagor.srce.hr&gt;)</p>
<dd> Maintainer of the gentoo package for Debian Linux, and also a source of suggestions for improvements, as well as a relay for bug reports from Debian Linux users.</p>
<dt>Ryan Weaver (&lt;ryanw [at] infohwy.com&gt;)</p>
<dd> Maintainer of the gentoo packages for Red Hat Linux, and probably one of the fastest package creators out there. :)</p>
<dt>Oliver Braun, Jim Geovedi and Pehr Johansson</p>
<dd> Maintainers of gentoo ports to FreeBSD, OpenBSD, and NetBSD, respectively.</dl>
<p> Thanks also to all people who have mailed me about gentoo, providing bug reports, feature requests, and the occasional kind word. :^) It&#8217;s because of people like yourselves that we have this wonderful computer platform to play with.</p>
<h2>COPYRIGHT</h2>
<p> gentoo is released as free, open-source software, under the terms of the GNU General Public License (GNU GPL), version 2. This license is included in the distribution under the traditional name of <code>COPYING,</code> and I suggest that you read it if you&#8217;re not familiar with it. If you can&#8217;t find the file, but have Internet access, you could take a look at <code>&lt;<a rel="nofollow" href="http://www.gnu.org/">http://www.gnu.org/</a>&gt;.</code> It is important to realize that the mentioned license means that there is <code>ABSOLUTELY NO WARRANTY</code> for this software.</p>
<h2>OTHER INFO</h2>
<p> Some unfinished, outdated, but still pretty informative documentation is available, in HTML format, in the <code>docs/</code> subdirectory in the distribution archive. If you haven&#8217;t installed gentoo from the original .tar.gz distribution archive, you might need to either inspect the distribution you <code>did</code> use (perhaps it came as some form of &quot;package&quot;), or contact a system administrator. </p>
<p> The GTK+ GUI toolkit that gentoo requires is available at <code>&lt;<a rel="nofollow" href="http://www.gtk.org/">http://www.gtk.org/</a>&gt;.</code> gentoo uses the slightly outdated stable series, called 1.2.x. The latest known release in that series is GTK+ 1.2.10. Because of severe performance problems, gentoo will probably not be ported to use the current (2.0.x) series of GTK+ any time soon. </p>
<p> The latest version of gentoo is always available on the official gentoo home page, at <code>&lt;<a rel="nofollow" href="http://www.obsession.se/gentoo/">http://www.obsession.se/gentoo/</a>&gt;.</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7), <code><a href="/docs/linux/man/1-file/">file</a></code>(1), <code><a href="/docs/linux/man/5-magic/">magic</a></code>(5), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) </p>
<p> Manual page section numbers in this page refer to sections on (some?) Linux systems, your mileage will most likely vary. Try the <code><a href="/docs/linux/man/1-apropos/">apropos</a></code>(1) command, it might help you out. </p>
<h2>Index</h2>
