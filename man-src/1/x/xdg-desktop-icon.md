---
title: "xdg-desktop-icon(1)"
name: "xdg-desktop-icon"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-desktop-icon/"
description: "xdg-desktop-icon – command line tool for (un)installing icons to the desktop"
---

<h2 class="name">NAME</h2>
<p> xdg-desktop-icon &#8211; command line tool for (un)installing icons to the desktop </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-desktop-icon</code> install [<code>&#8211;novendor</code>] <i>FILE</i></p>
<dt> <code>xdg-desktop-icon</code> uninstall <i>FILE</i></p>
<dt> <code>xdg-desktop-icon</code> {<code>&#8211;help</code> | <code>&#8211;manual</code> | <code>&#8211;version</code>}</dl>
<h2>DESCRIPTION</h2>
<dd>The xdg-desktop-icon program can be used to install an application launcher or other file on the desktop of the current user. </p>
<p> An application launcher is represented by a *.desktop file. Desktop files are defined by the freedesktop.org Desktop Entry Specification. The most important aspects of *.desktop files are summarized below.</p>
<h2>COMMANDS</h2>
<p> install</p>
<dl>
<dt>
<dd> Installs <i>FILE</i> to the desktop of the current user. <i>FILE</i> can be a *.desktop file or any other type of file.</dl>
<p> uninstall</p>
<dl>
<dt>
<dd> Removes <i>FILE</i> from the desktop of the current user.</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;novendor</code></p>
<dl>
<dt>
<dd> Normally, xdg-desktop-icon checks to ensure that a *.desktop file to be installed has a vendor prefix. This option can be used to disable that check. </p>
<p> A vendor prefix consists of alpha characters ([a-zA-Z]) and is terminated with a dash (&quot;-&quot;). Companies and organizations are encouraged to use a word or phrase, preferably the organizations name, for which they hold a trademark as their vendor prefix. The purpose of the vendor prefix is to prevent name conflicts.</dl>
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
<p> An application launcher can be added to the desktop by installing a *.desktop file. A *.desktop file consists of a <i>[Desktop Entry]</i> header followed by several <i>Key</i>=<i>Value</i> lines. </p>
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
<p> For a complete overview of the *.desktop file format please visit m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/desktop-entry-spec">http://www.freedesktop.org/wiki/Specifications/desktop-entry-spec</a></code>m[]</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> xdg-desktop-icon honours the following environment variables: </p>
<p> XDG_UTILS_DEBUG_LEVEL</p>
<dl>
<dt>
<dd> Setting this environment variable to a non-zero numerical value makes xdg-desktop-icon do more verbose reporting on stderr. Setting a higher value increases the verbosity.</dl>
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
<p> <code><a href="/docs/linux/man/1-xdg-icon-resource/">xdg-icon-resource</a></code>(1)</p>
<h2>EXAMPLES</h2>
<p> The company ShinyThings Inc. has developed an application named &quot;WebMirror&quot; and would like to add a launcher for for on the desktop. The company will use &quot;shinythings&quot; as its vendor id. In order to add the application to the desktop there needs to be a .desktop file for the application: </p>
<dl>
<dt>
<dd>
<pre><code>
shinythings - webmirror.desktop : [Desktop Entry] Encoding = UTF - 8 Type = Application
                                                                 Exec = webmirror
                                                                     Icon = shinythings - webmirror
                                                                                              Name = WebMirror
                                                                                Name[nl] = WebSpiegel
</code></pre>
</dl>
<p> Now the xdg-desktop-icon tool can be used to add the webmirror.desktop file to the desktop: </p>
<dl>
<dt>
<dd>
<pre>
xdg-desktop-icon install ./shinythings-webmirror.desktop
</pre>
</dl>
<p> To add a README file to the desktop as well, the following command can be used: </p>
<dl>
<dt>
<dd>
<pre>
xdg-desktop-icon install ./shinythings-README
</pre>
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
<h2>Index</h2>
