---
title: "dselect(1)"
name: "dselect"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dselect/"
description: "dselect – Debian package management frontend"
---

<h2>NAME</h2>
<p> dselect &#8211; Debian package management frontend</p>
<h2>SYNOPSIS</h2>
<p> <code>dselect</code> [<i>option</i>&#8230;] [<i>action</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dselect</code> is one of the primary user interfaces for managing packages on a Debian system. At the <code>dselect</code> main menu, the system administrator can:<br />
&nbsp;<wbr>&#8211; Update the list of available package versions,<br />
&nbsp;<wbr>&#8211; View the status of installed and available packages,<br />
&nbsp;<wbr>&#8211; Alter package selections and manage dependencies,<br />
&nbsp;<wbr>&#8211; Install new packages or upgrade to newer versions. </p>
<p> <code>dselect</code> operates as a front-end to <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), the low-level debian package handling tool. It features a full-screen package selections manager with package depends and conflicts resolver. When run with administrator privileges, packages can be installed, upgraded and removed. Various access methods can be configured to retrieve available package version information and installable packages from package repositories. Depending on the used access method, these repositories can be public archive servers on the internet, local archive servers or cdroms. The recommended access method is <i>apt</i>, which is provided by the package <code>apt</code>. </p>
<p> Normally <code>dselect</code> is invoked without parameters. An interactive menu is presented, offering the user a list of actions. If an action is given as argument, then that action is started immediately. Several command line parameters are still available to modify the running behaviour of <code>dselect</code> or show additional information about the program.</p>
<h2>OPTIONS</h2>
<p> All options can be specified both on the command line and in the <code>dselect</code> configuration file <i>/etc/dpkg/dselect.cfg</i> or the files on the configuration directory <i>/etc/dpkg/dselect.cfg.d/</i>. Each line in the configuration file is either an option (exactly the same as the command line option but without leading hyphens) or a comment (if it starts with a <code>#</code>). </p>
<dl>
<dt><code>&#8211;admindir</code><i> directory</i></p>
<dd> Changes the directory where the dpkg `<i>status</i>&#8216;, `<i>available</i>&#8216; and similar files are located. This defaults to <i>/var/lib/dpkg</i> and normally there shouldn&#8217;t be any need to change it.</p>
<dt><code>&#8211;debug</code><i> file </i>| <code>-D</code><i>file</i></p>
<dd> Turn on debugging. Debugging information is sent to <i>file</i>.</p>
<dt><code>&#8211;expert</code></p>
<dd> Turns on expert mode, i.e. doesn&#8217;t display possibly annoying help messages.</p>
<dt><code>&#8211;colour</code>|<code>&#8211;color</code> <i>screenpart:</i>[<i>foreground</i>],[<i>background</i>][<i>:attr</i>[<i>+attr+&#8230;</i>]]</p>
<dd> Configures screen colors. This works only if your display supports colors. This option may be used multiple times (and is best used in <i>dselect.cfg</i>). Each use changes the color (and optionally, other attributes) of one part of the screen. The parts of the screen (from top to bottom) are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>title</code></p>
<dd> The screen title.</p>
<dt><code>listhead</code></p>
<dd> The header line above the list of packages.</p>
<dt><code>list</code></p>
<dd> The scrolling list of packages (and also some help text).</p>
<dt><code>listsel</code></p>
<dd> The selected item in the list.</p>
<dt><code>pkgstate</code></p>
<dd> In the list of packages, the text indicating the current state of each package.</p>
<dt><code>pkgstatesel</code></p>
<dd> In the list of packages, the text indicating the current state of the currently selected package.</p>
<dt><code>infohead</code></p>
<dd> The header line that displays the state of the currently selected package.</p>
<dt><code>infodesc</code></p>
<dd> The package&#8217;s short description.</p>
<dt><code>info</code></p>
<dd> Used to display package info such as the package&#8217;s description.</p>
<dt><code>infofoot</code></p>
<dd> The last line of the screen when selecting packages.</p>
<dt><code>query</code></p>
<dd> Used to display query lines</p>
<dt><code>helpscreen</code></p>
<dd> Color of help screens.</dl>
</dl>
<dt>
<dd> After the part of the screen comes a colon and the color specification. You can specify either the foreground color, the background color, or both, overriding the compiled-in colors. Use standard curses color names.</p>
<dt>
<dd> Optionally, after the color specification is another colon, and an attribute specification. This is a list of one or more attributes, separated by plus (&quot;+&quot;) characters. Available attributes include (not all of these will work on all terminals): normal, standout, underline, reverse, blink, bright, dim, bold</p>
<dt><code>&#8211;help</code></p>
<dd> Print a brief help text and exit successfully.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit successfully.</dl>
<h2>ACTIONS</h2>
<p> When <code>dselect</code> is started it can perform the following actions, either directly if it was specified on the command line or by prompting the user with a menu of available actions if running interactively:</p>
<h3>access</h3>
<p> Choose and configure an access method to access package repositories. </p>
<p> By default, <code>dselect</code> provides several methods such as <i>cdrom</i>, <i>multi_cd</i>, <i>nfs</i>, <i>multi_nfs</i>, <i>harddisk</i>, <i>mounted</i>, <i>multi_mount</i>, <i>floppy</i> or <i>ftp</i>, but other packages may provide additional methods, eg. the <i>apt</i> access method provided by the <code>apt</code> package. </p>
<p> The use of the <i>apt</i> access method is strongly recommended. </p>
<h3>update</h3>
<p> Refresh the available packages database. </p>
<p> Retrieves a list of available package versions from the package repository, configured for the current access method, and update the dpkg database. The package lists are commonly provided by the repository as files named <i>Packages</i> or <i>Packages.gz</i>. These files can be generated by repository maintainers, using the program <code><a href="/docs/linux/man/1-dpkg-scanpackages/">dpkg-scanpackages</a></code>(1). </p>
<p> Details of the update action depend on the access method&#8217;s implementation. Normally the process is straightforward and requires no user interaction. </p>
<h3>select</h3>
<p> View or manage package selections and dependencies. </p>
<p> This is the main function of <code>dselect</code>. In the select screen, the user can review a list of all available and installed packages. When run with administrator privileges, it is also possible to interactively change packages selection state. <code>dselect</code> tracks the implications of these changes to other depending or conflicting packages. </p>
<p> When a conflict or failed depends is detected, a dependency resolution subscreen is prompted to the user. In this screen, a list of conflicting or depending packages is shown, and for each package listed, the reason for its listing is shown. The user may apply the suggestions proposed by <code>dselect</code>, override them, or back out all the changes, including the ones that created the unresolved depends or conflicts. </p>
<p> The use of the interactive package selections management screen is explained in more detail below. </p>
<h3>install</h3>
<p> Installs selected packages. </p>
<p> The configured access method will fetch installable or upgradable packages from the relevant repositories and install these using <code>dpkg</code>. Depending on the implementation of the access method, all packages can be prefetched before installation, or fetched when needed. Some access methods may also remove packages that were marked for removal. </p>
<p> If an error occurred during install, it is usually advisable to run install again. In most cases, the problems will disappear or be solved. If problems persist or the installation performed was incorrect, please investigate into the causes and circumstances, and file a bug in the Debian bug tracking system. Instructions on how to do this can be found at <a rel="nofollow" href="https://bugs.debian.org/">https://bugs.debian.org/</a> or by reading the documentation for <code><a href="/docs/linux/man/1-bug/">bug</a></code>(1) or <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1), if these are installed. </p>
<p> Details of the install action depend on the access method&#8217;s implementation. The user&#8217;s attention and input may be required during installation, configuration or removal of packages. This depends on the maintainer scripts in the package. Some packages make use of the <code><a href="/docs/linux/man/1-debconf/">debconf</a></code>(1) library, allowing for more flexible or even automated installation setups. </p>
<h3>config</h3>
<p> Configures any previously installed, but not fully configured packages. </p>
<h3>remove</h3>
<p> Removes or purges installed packages, that are marked for removal. </p>
<h3>quit</h3>
<p> Quit <code>dselect</code> </p>
<p> Exits the program with zero (successful) errorcode. </p>
<h2>PACKAGE SELECTIONS MANAGEMENT</h2>
<h3>Introduction</h3>
<p> <code>dselect</code> directly exposes the administrator to some of the complexities involved with managing large sets of packages with many interdependencies. For a user who is unfamiliar with the concepts and the ways of the debian package management system, it can be quite overwhelming. Although <code>dselect</code> is aimed at easing package management and administration, it is only instrumental in doing so and can not be assumed to be a sufficient substitute for administrator skill and understanding. The user is required to be familiar with the concepts underlying the Debian packaging system. In case of doubt, consult the <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) manpage and the Debian Policy manual, contained in the <code>debian-policy</code> package. </p>
<p> Unless <code>dselect</code> is run in expert or immediate mode, a help screen is first displayed when choosing this action from the menu. The user is <i>strongly</i> advised to study all of the information presented in the online help screens, when one pops up. The online help screens can at any time be invoked with the <code>&#8216;?&#8217;</code> key. </p>
<h3>Screen layout</h3>
<p> The select screen is by default split in a top and a bottom half. The top half shows a list of packages. A cursor bar can select an individual package, or a group of packages, if applicable, by selecting the group header. The bottom half of the screen shows some details about the package currently selected in the top half of the screen. The type of detail that is displayed can be varied. </p>
<p> Pressing the <code>&#8216;I&#8217;</code> key toggles a full-screen display of the packages list, an enlarged view of the package details, or the equally split screen. </p>
<h3>Package details view</h3>
<p> The package details view by default shows the extended package description for the package that is currently selected in the packages status list. The type of detail can be toggled by pressing the <code>&#8216;i&#8217;</code> key. This alternates between:<br />
&nbsp;<wbr>&#8211; the extended description<br />
&nbsp;<wbr>&#8211; the control information for the installed version<br />
&nbsp;<wbr>&#8211; the control information for the available version </p>
<p> In a dependency resolution screen, there is also the possibility of viewing the specific unresolved depends or conflicts related to the package and causing it to be listed. </p>
<h3>Packages status list</h3>
<p> The main select screen displays a list of all packages known to the debian package management system. This includes packages installed on the system and packages known from the available packages database. </p>
<p> For every package, the list shows the package&#8217;s status, priority, section, installed and available architecture, installed and available versions, the package name and its short description, all in one line. By pressing the <code>&#8216;A&#8217;</code> key, the display of the installed and available architecture can be toggled between on an off. By pressing the <code>&#8216;V&#8217;</code> key, the display of the installed and available version can be toggled between on an off. By pressing the <code>&#8216;v&#8217;</code> key, the package status display is toggled between verbose and shorthand. Shorthand display is the default. </p>
<p> The shorthand status indication consists of four parts: an error flag, which should normally be clear, the current status, the last selection state and the current selection state. The first two relate to the actual state of the package, the second pair are about the selections set by the user. </p>
<p> These are the meanings of the shorthand package status indicator codes:<br />
&nbsp;<wbr>Error flag:<br />
&nbsp;<wbr>&nbsp;<wbr><i>empty</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>no error<br />
&nbsp;<wbr>&nbsp;<wbr><code>R</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>serious error, needs reinstallation;<br />
&nbsp;<wbr>Installed state:<br />
&nbsp;<wbr>&nbsp;<wbr><i>empty</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>not installed;<br />
&nbsp;<wbr>&nbsp;<wbr><code>*</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>fully installed and configured;<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>not installed but some config files may remain;<br />
&nbsp;<wbr>&nbsp;<wbr><code>U</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unpacked but not yet configured;<br />
&nbsp;<wbr>&nbsp;<wbr><code>C</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>half-configured&nbsp;<wbr>(an error happened);<br />
&nbsp;<wbr>&nbsp;<wbr><code>I</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>half-installed&nbsp;<wbr>(an error happened).<br />
&nbsp;<wbr>Current and requested selections:<br />
&nbsp;<wbr>&nbsp;<wbr><code>*</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>marked for installation or upgrade;<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>marked for removal, configuration files remain;<br />
&nbsp;<wbr>&nbsp;<wbr><code>=</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on hold: package will not be processed at all;<br />
&nbsp;<wbr>&nbsp;<wbr><code>_</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>marked for purge, also remove configuration;<br />
&nbsp;<wbr>&nbsp;<wbr><code>n</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>package is new and has yet to be marked. </p>
<h3>Cursor and screen movement</h3>
<p> The package selection list and the dependency conflict resolution screens can be navigated using motion commands mapped to the following keys: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>p, Up, k</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>move cursor bar up<br />
&nbsp;<wbr>&nbsp;<wbr><code>n, Down, j</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>move cursor bar down<br />
&nbsp;<wbr>&nbsp;<wbr><code>P, Pgup, Backspace</code>&nbsp;<wbr>scroll list 1 page up<br />
&nbsp;<wbr>&nbsp;<wbr><code>N, Pgdn, Space</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scroll list 1 page down<br />
&nbsp;<wbr>&nbsp;<wbr><code>^p</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scroll list 1 line up<br />
&nbsp;<wbr>&nbsp;<wbr><code>^n</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scroll list 1 line down<br />
&nbsp;<wbr>&nbsp;<wbr><code>t, Home</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>jump to top of list<br />
&nbsp;<wbr>&nbsp;<wbr><code>e, End</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>jump to end of list<br />
&nbsp;<wbr>&nbsp;<wbr><code>u</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scroll info 1 page up<br />
&nbsp;<wbr>&nbsp;<wbr><code>d</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scroll info 1 page down<br />
&nbsp;<wbr>&nbsp;<wbr><code>^u</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scroll info 1 line up<br />
&nbsp;<wbr>&nbsp;<wbr><code>^d</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>scroll info 1 line down<br />
&nbsp;<wbr>&nbsp;<wbr><code>B, Left-arrow</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pan display 1/3 screen left<br />
&nbsp;<wbr>&nbsp;<wbr><code>F, Right-arrow</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pan display 1/3 screen right<br />
&nbsp;<wbr>&nbsp;<wbr><code>^b</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pan display 1 character left<br />
&nbsp;<wbr>&nbsp;<wbr><code>^f</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pan display 1 character right </p>
<h3>Searching and sorting</h3>
<p> The list of packages can be searched by package name. This is done by pressing <code>&#8216;/&#8217;</code>, and typing a simple search string. The string is interpreted as a <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) regular expression. If you add <code>&#8216;/d&#8217;</code> to the search expression, dselect will also search in descriptions. If you add <code>&#8216;/i&#8217;</code> the search will be case insensitive. You may combine these two suffixes like this: <code>&#8216;/id&#8217;</code>. Repeated searching is accomplished by repeatedly pressing the <code>&#8216;n&#8217;</code> or <code>&#8216;\&#8217;</code> keys, until the wanted package is found. If the search reaches the bottom of the list, it wraps to the top and continues searching from there. </p>
<p> The list sort order can be varied by pressing the <code>&#8216;o&#8217;</code> and <code>&#8216;O&#8217;</code> keys repeatedly. The following nine sort orderings can be selected:<br />
&nbsp;<wbr>alphabet&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>available&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>status<br />
&nbsp;<wbr>priority+section&nbsp;<wbr>&nbsp;<wbr>available+priority&nbsp;<wbr>&nbsp;<wbr>status+priority<br />
&nbsp;<wbr>section+priority&nbsp;<wbr>&nbsp;<wbr>available+section&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>status+section<br />
 Where not listed above explicitly, alphabetic order is used as the final subordering sort key. </p>
<h3>Altering selections</h3>
<p> The requested selection state of individual packages may be altered with the following commands:<br />
&nbsp;<wbr>&nbsp;<wbr><code>+, Insert</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>install or upgrade<br />
&nbsp;<wbr>&nbsp;<wbr><code>=, H</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>hold in present state and version<br />
&nbsp;<wbr>&nbsp;<wbr><code>:, G</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>unhold: upgrade or leave uninstalled<br />
&nbsp;<wbr>&nbsp;<wbr><code>-, Delete</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>remove, but leave configuration<br />
&nbsp;<wbr>&nbsp;<wbr><code>_</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>remove&nbsp;<wbr>&amp;&nbsp;<wbr>purge configuration </p>
<p> When the change request results in one or more unsatisfied depends or conflicts, <code>dselect</code> prompts the user with a dependency resolution screen. This will be further explained below. </p>
<p> It is also possible to apply these commands to groups of package selections, by pointing the cursor bar onto a group header. The exact grouping of packages is dependent on the current list ordering settings. </p>
<p> Proper care should be taken when altering large groups of selections, because this can instantaneously create large numbers of unresolved depends or conflicts, all of which will be listed in one dependency resolution screen, making them very hard to handle. In practice, only hold and unhold operations are useful when applied to groups. </p>
<h3>Resolving depends and conflicts</h3>
<p> When the change request results in one or more unsatisfied depends or conflicts, <code>dselect</code> prompts the user with a dependency resolution screen. First however, an informative help screen is displayed. </p>
<p> The top half of this screen lists all the packages that will have unresolved depends or conflicts, as a result of the requested change, and all the packages whose installation can resolve any of these depends or whose removal can resolve any of the conflicts. The bottom half defaults to show the depends or conflicts that cause the currently selected package to be listed. </p>
<p> When the sublist of packages is displayed initially, <code>dselect</code> may have already set the requested selection status of some of the listed packages, in order to resolve the depends or conflicts that caused the dependency resolution screen to be displayed. Usually, it is best to follow up the suggestions made by <code>dselect</code>. </p>
<p> The listed packages&#8217; selection state may be reverted to the original settings, as they were before the unresolved depends or conflicts were created, by pressing the <code>&#8216;R&#8217;</code> key. By pressing the <code>&#8216;D&#8217;</code> key, the automatic suggestions are reset, but the change that caused the dependency resolution screen to be prompted is kept as requested. Finally, by pressing <code>&#8216;U&#8217;</code>, the selections are again set to the automatic suggestion values. </p>
<h3>Establishing the requested selections</h3>
<p> By pressing <code>enter</code>, the currently displayed set of selections is accepted. If <code>dselect</code> detects no unresolved depends as a result of the requested selections, the new selections will be set. However, if there are any unresolved depends, <code>dselect</code> will again prompt the user with a dependency resolution screen. </p>
<p> To alter a set of selections that creates unresolved depends or conflicts and forcing <code>dselect</code> to accept it, press the <code>&#8216;Q&#8217;</code> key. This sets the selections as specified by the user, unconditionally. Generally, don&#8217;t do this unless you&#8217;ve read the fine print. </p>
<p> The opposite effect, to back out any selections change requests and go back to the previous list of selections, is attained by pressing the <code>&#8216;X&#8217;</code> or <code>escape</code> keys. By repeatedly pressing these keys, any possibly detrimental changes to the requested package selections can be backed out completely to the last established settings. </p>
<p> If you mistakenly establish some settings and wish to revert all the selections to what is currently installed on the system, press the <code>&#8216;C&#8217;</code> key. This is somewhat similar to using the unhold command on all packages, but provides a more obvious panic button in cases where the user pressed <code>enter</code> by accident. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></p>
<dd> If set, <code>dselect</code> will use it as the directory from which to read the user specific configuration file.</dl>
<h2>BUGS</h2>
<p> The <code>dselect</code> package selection interface is confusing to some new users. Reportedly, it even makes seasoned kernel developers cry. </p>
<p> The documentation is lacking. </p>
<p> There is no help option in the main menu. </p>
<p> The visible list of available packages cannot be reduced. </p>
<p> The built in access methods can no longer stand up to current quality standards. Use the access method provided by apt, it is not only not broken, it is also much more flexible than the built in access methods.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), <code><a href="/docs/linux/man/8-apt-get/">apt-get</a></code>(8), <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5), <code><a href="/docs/linux/man/5-deb/">deb</a></code>(5). </p>
<h2>Index</h2>
