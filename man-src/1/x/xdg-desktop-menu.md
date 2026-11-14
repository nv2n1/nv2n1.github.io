---
title: "xdg-desktop-menu(1)"
name: "xdg-desktop-menu"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-desktop-menu/"
description: "xdg-desktop-menu – command line tool for (un)installing desktop menu items"
---

<h2 class="name">NAME</h2>
<p> xdg-desktop-menu &#8211; command line tool for (un)installing desktop menu items </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-desktop-menu</code> install [<code>&#8211;noupdate</code>] [<code>&#8211;novendor</code>] [<code>&#8211;mode&nbsp;</code><i>mode</i>] <i>directory-file(s)</i> <i>desktop-file(s)</i></p>
<dt> <code>xdg-desktop-menu</code> uninstall [<code>&#8211;noupdate</code>] [<code>&#8211;mode&nbsp;</code><i>mode</i>] <i>directory-file(s)</i> <i>desktop-file(s)</i></p>
<dt> <code>xdg-desktop-menu</code> forceupdate [<code>&#8211;mode&nbsp;</code><i>mode</i>]</p>
<dt> <code>xdg-desktop-menu</code> {<code>&#8211;help</code> | <code>&#8211;manual</code> | <code>&#8211;version</code>}</dl>
<h2>DESCRIPTION</h2>
<dd>The xdg-desktop-menu program can be used to install new menu entries to the desktop&#8217;s application menu. </p>
<p> The application menu works according to the XDG Desktop Menu Specification at m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/menu-spec">http://www.freedesktop.org/wiki/Specifications/menu-spec</a></code>m[]</p>
<h2>COMMANDS</h2>
<p> install</p>
<dl>
<dt>
<dd> Install one or more applications in a submenu of the desktop menu system. </p>
<p> <i>desktop-file</i>: A desktop file represents a single menu entry in the menu. Desktop files are defined by the freedesktop.org Desktop Entry Specification. The most important aspects of *.desktop files are summarized below. </p>
<p> Menu entries can be added to the menu system in two different ways. They can either be added to a predefined submenu in the menu system based on one or more category keywords, or they can be added to a new submenu. </p>
<p> To add a menu entry to a predefined submenu the desktop file that represents the menu entry must have a Categories= entry that lists one or more keywords. The menu item will be included in an appropriate submenu based on the included keywords. </p>
<p> To add menu items to a new submenu the desktop-files must be preceded by a directory-file that describes the submenu. If multiple desktop-files are specified, all entries will be added to the same menu. If entries are installed to a menu that has been created with a previous call to <code>xdg-desktop-menu</code> the entries will be installed in addition to any already existing entries. </p>
<p> <i>directory-file</i>: The *.directory file indicated by <i>directory-file</i> represents a submenu. The directory file provides the name and icon for a submenu. The name of the directory file is used to identify the submenu. </p>
<p> If multiple directory files are provided each file will represent a submenu within the menu that precedes it, creating a nested menu hierarchy (sub-sub-menus). The menu entries themselves will be added to the last submenu. </p>
<p> Directory files follow the syntax defined by the freedesktop.org Desktop Entry Specification.</dl>
<p> uninstall</p>
<dl>
<dt>
<dd> Remove applications or submenus from the desktop menu system previously installed with <code>xdg-desktop-menu install</code>. </p>
<p> A submenu and the associated directory file is only removed when the submenu no longer contains any menu entries.</dl>
<p> forceupdate</p>
<dl>
<dt>
<dd> Force an update of the menu system. </p>
<p> This command is only useful if the last call to xdg-desktop-menu included the <code>&#8211;noupdate</code> option.</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;noupdate</code></p>
<dl>
<dt>
<dd> Postpone updating the menu system. If multiple updates to the menu system are made in sequence this flag can be used to indicate that additional changes will follow and that it is not necessary to update the menu system right away.</dl>
<p> <code>&#8211;novendor</code></p>
<dl>
<dt>
<dd> Normally, xdg-desktop-menu checks to ensure that any *.directory and *.desktop files to be installed has a vendor prefix. This option can be used to disable that check. </p>
<p> A vendor prefix consists of alpha characters ([a-zA-Z]) and is terminated with a dash (&quot;-&quot;). Companies and organizations are encouraged to use a word or phrase, preferably the organizations name, for which they hold a trademark as their vendor prefix. The purpose of the vendor prefix is to prevent name conflicts.</dl>
<p> <code>&#8211;mode</code> <i>mode</i></p>
<dl>
<dt>
<dd> <i>mode</i> can be <i>user</i> or <i>system</i>. In user mode the file is (un)installed for the current user only. In system mode the file is (un)installed for all users on the system. Usually only root is allowed to install in system mode. </p>
<p> The default is to use system mode when called by root and to use user mode when called by a non-root user.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show command synopsis.</dl>
<p> <code>&#8211;manual</code></p>
<dl>
<dt>
<dd> Show this manual page.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show the xdg-utils version information.</dl>
<h2>DESKTOP FILES</h2>
<p> An application item in the application menu is represented by a *.desktop file. A *.desktop file consists of a <i>[Desktop Entry]</i> header followed by several <i>Key</i>=<i>Value</i> lines. </p>
<p> A *.desktop file can provide a name and description for an application in several different languages. This is done by adding a language code as used by LC_MESSAGES in square brackets behind the <i>Key</i>. This way one can specify different values for the same <i>Key</i> depending on the currently selected language. </p>
<p> The following keys are often used: </p>
<p> Type=Application</p>
<dl>
<dt>
<dd> This is a mandatory field that indicates that the *.desktop file describes an application launcher.</dl>
<p> Name=<i>Application Name</i></p>
<dl>
<dt>
<dd> The name of the application. For example <i>Mozilla</i></dl>
<p> GenericName=<i>Generic Name</i></p>
<dl>
<dt>
<dd> A generic description of the application. For example <i>Web Browser</i></dl>
<p> Comment=<i>Comment</i></p>
<dl>
<dt>
<dd> Optional field to specify a tooltip for the application. For example <i>Visit websites on the Internet</i></dl>
<p> Icon=<i>Icon File</i></p>
<dl>
<dt>
<dd> The icon to use for the application. This can either be an absolute path to an image file or an icon-name. If an icon-name is provided an image lookup by name is done in the user&#8217;s current icon theme. The <code>xdg-icon-resource</code> command can be used to install image files into icon themes. The advantage of using an icon-name instead of an absolute path is that with an icon-name the application icon can be provided in several different sizes as well as in several differently themed styles.</dl>
<p> Exec=<i>Command Line</i></p>
<dl>
<dt>
<dd> The command line to start the application. If the application can open files the %f placeholder should be specified. When a file is dropped on the application launcher the %f is replaced with the file path of the dropped file. If multiple files can be specified on the command line the %F placeholder should be used instead of %f. If the application is able to open URLs in addition to local files then %u or %U can be used instead of %f or %F.</dl>
<p> Categories=<i>Categories</i></p>
<dl>
<dt>
<dd> A list of categories separated by semi-colons. A category is a keyword that describes and classifies the application. By default applications are organized in the application menu based on category. When menu entries are explicitly assigned to a new submenu it is not necessary to list any categories. </p>
<p> When using categories it is recommended to include one of the following categories: AudioVideo, Development, Education, Game, Graphics, Network, Office, Settings, System, Utility. </p>
<p> See Appendix A of the XDG Desktop Menu Specification for information about additional categories: m[blue]<code><a rel="nofollow" href="http://standards.freedesktop.org/menu-spec/menu-spec-1.0.html#category-registry">http://standards.freedesktop.org/menu-spec/menu-spec-1.0.html#category-registry</a></code>m[]</dl>
<p> MimeType=<i>Mimetypes</i></p>
<dl>
<dt>
<dd> A list of mimetypes separated by semi-colons. This field is used to indicate which file types the application is able to open.</dl>
<p> For a complete overview of the *.desktop file format please visit m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/desktop-entry-spec">http://www.freedesktop.org/wiki/Specifications/desktop-entry-spec</a></code>m[]</p>
<h2>DIRECTORY FILES</h2>
<p> The appearance of submenu in the application menu is provided by a *.directory file. In particular it provides the title of the submenu and a possible icon. A *.directory file consists of a <i>[Desktop Entry]</i> header followed by several <i>Key</i>=<i>Value</i> lines. </p>
<p> A *.directory file can provide a title (name) for the submenu in several different languages. This is done by adding a language code as used by LC_MESSAGES in square brackets behind the <i>Key</i>. This way one can specify different values for the same <i>Key</i> depending on the currently selected language. </p>
<p> The following keys are relevant for submenus: </p>
<p> Type=Directory</p>
<dl>
<dt>
<dd> This is a mandatory field that indicates that the *.directory file describes a submenu.</dl>
<p> Name=<i>Menu Name</i></p>
<dl>
<dt>
<dd> The title of submenu. For example <i>Mozilla</i></dl>
<p> Comment=<i>Comment</i></p>
<dl>
<dt>
<dd> Optional field to specify a tooltip for the submenu.</dl>
<p> Icon=<i>Icon File</i></p>
<dl>
<dt>
<dd> The icon to use for the submenu. This can either be an absolute path to an image file or an icon-name. If an icon-name is provided an image lookup by name is done in the user&#8217;s current icon theme. The <code>xdg-icon-resource</code> command can be used to install image files into icon themes. The advantage of using an icon-name instead of an absolute path is that with an icon-name the submenu icon can be provided in several different sizes as well as in several differently themed styles.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> xdg-desktop-menu honours the following environment variables: </p>
<p> XDG_UTILS_DEBUG_LEVEL</p>
<dl>
<dt>
<dd> Setting this environment variable to a non-zero numerical value makes xdg-desktop-menu do more verbose reporting on stderr. Setting a higher value increases the verbosity.</dl>
<p> XDG_UTILS_INSTALL_MODE</p>
<dl>
<dt>
<dd> This environment variable can be used by the user or administrator to override the installation mode. Valid values are <i>user</i> and <i>system</i>.</dl>
<h2>EXIT CODES</h2>
<p> An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned: </p>
<p> <code>1</code></p>
<dl>
<dt>
<dd> Error in command line syntax.</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> One of the files passed on the command line did not exist.</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> A required tool could not be found.</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> The action failed.</dl>
<p> <code>5</code></p>
<dl>
<dt>
<dd> No permission to read one of the files passed on the command line.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdg-desktop-icon/">xdg-desktop-icon</a></code>(1), <code><a href="/docs/linux/man/1-xdg-icon-resource/">xdg-icon-resource</a></code>(1), <code><a href="/docs/linux/man/1-xdg-mime/">xdg-mime</a></code>(1), m[blue]<code>Desktop entry specification</code>m[]<font SIZE="-2">[1]</font>, m[blue]<code>Desktop menu specification</code>m[]<font SIZE="-2">[2]</font></p>
<h2>EXAMPLES</h2>
<p> The company ShinyThings Inc. has developed an application named &quot;WebMirror&quot; and would like to add it to the application menu. The company will use &quot;shinythings&quot; as its vendor id. In order to add the application to the menu there needs to be a .desktop file with a suitable <i>Categories</i> entry: </p>
<dl>
<dt>
<dd>
<pre><code>
shinythings - webmirror.desktop : [Desktop Entry] Encoding = UTF - 8 Type = Application
                                                                 Exec = webmirror
                                                                     Icon = webmirror
                                                                         Name = WebMirror
                                                                             Name[nl] = WebSpiegel
                                                                                 Categories = Network;
WebDevelopment;
</code></pre>
</dl>
<p> Now the xdg-desktop-menu tool can be used to add the shinythings-webmirror.desktop file to the desktop application menu: </p>
<dl>
<dt>
<dd>
<pre>
xdg-desktop-menu install ./shinythings-webmirror.desktop
</pre>
</dl>
<p> Note that for the purpose of this example the menu items are available in two languages, English and Dutch. The language code for Dutch is nl. </p>
<p> In the next example the company ShinyThings Inc. will add its own submenu to the desktop application menu consisting of a &quot;WebMirror&quot; menu item and a &quot;WebMirror Admin Tool&quot; menu item. </p>
<p> First the company needs to create two .desktop files that describe the two menu items. Since the items are to be added to a new submenu it is not necessary to include a Categories= line: </p>
<dl>
<dt>
<dd>
shinythings &#8211; webmirror.desktop : [Desktop Entry] Encoding = UTF &#8211; 8 Type = Application<br />
                                                                 Exec = webmirror<br />
                                                                     Icon = shinythings &#8211; webmirror<br />
                                                                                              Name = WebMirror<br />
                                                                                Name[nl] = WebSpiegel<br />
                                                                                               shinythings &#8211;<br />
                                                                                           webmirror &#8211; admin.desktop : [Desktop Entry] Encoding = UTF &#8211; 8 Type = Application<br />
                                                                                                                                                      Exec = webmirror &#8211; admintool<br />
                                                                                                                                                                             Icon = shinythings &#8211; webmirror &#8211; admintool Name = WebMirror Admin Tool<br />
                                                                                                                                                                                        Name[nl] = WebSpiegel Administratie Tool
</dl>
<p> In addition a .directory file needs to be created to provide a title and icon for the sub-menu itself: </p>
<dl>
<dt>
<dd>
shinythings &#8211; webmirror.directory : [Desktop Entry] Encoding = UTF &#8211; 8 Icon = shinythings &#8211; webmirror &#8211; menu Name = WebMirror<br />
                                                                                  Name[nl] = WebSpiegel
</dl>
<p> These file can now be installed with: </p>
<dl>
<dt>
<dd>
<pre>
xdg-desktop-menu install ./shinythings-webmirror.directory \
      ./shinythings-webmirror.desktop ./shinythings-webmirror-admin.desktop
</pre>
</dl>
<p> The menu entries could also be installed one by one: </p>
<dl>
<dt>
<dd>
<pre>
xdg-desktop-menu install --noupdate ./shinythings-webmirror.directory \
      ./shinythings-webmirror.desktop
xdg-desktop-menu install --noupdate ./shinythings-webmirror.directory \
      ./shinythings-webmirror-admin.desktop
xdg-desktop-menu forceupdate
</pre>
</dl>
<p> Although the result is the same it is slightly more efficient to install all files at the same time. </p>
<p> The *.desktop and *.directory files reference icons with the names webmirror, webmirror-admin and webmirror-menu which should also be installed. In this example the icons are installed in two different sizes, once with a size of 22&#215;22 pixels and once with a size of 64&#215;64 pixels: </p>
<dl>
<dt>
<dd>
<pre><code>
xdg - icon - resource install-- size 22./ wmicon - 22.png shinythings - webmirror xdg - icon - resource install-- size 22./ wmicon - menu - 22.png shinythings - webmirror - menu xdg - icon - resource install-- size 22./ wmicon - admin - 22.png shinythings - webmirror - admin xdg - icon - resource install-- size 64./ wmicon - 64.png shinythings - webmirror xdg - icon - resource install-- size 64./ wmicon - menu - 64.png shinythings - webmirror - menu xdg - icon - resource install-- size 64./ wmicon - admin - 64.png shinythings - webmirror - admin
</code></pre>
</dl>
<h2>AUTHORS</h2>
<p> <code>Kevin Krammer</code></p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Jeremy White</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Desktop entry specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/desktop-entry-spec/">http://www.freedesktop.org/wiki/Specifications/desktop-entry-spec/</a></dl>
<dt> 2.</p>
<dd> Desktop menu specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/menu-spec/">http://www.freedesktop.org/wiki/Specifications/menu-spec/</a></dl>
</dl>
<h2>Index</h2>
