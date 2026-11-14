---
title: "xdg-icon-resource(1)"
name: "xdg-icon-resource"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-icon-resource/"
description: "xdg-icon-resource – command line tool for (un)installing icon resources"
---

<h2 class="name">NAME</h2>
<p> xdg-icon-resource &#8211; command line tool for (un)installing icon resources </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-icon-resource</code> install [<code>&#8211;noupdate</code>] [<code>&#8211;novendor</code>] [<code>&#8211;theme&nbsp;</code><i>theme</i>] [<code>&#8211;context&nbsp;</code><i>context</i>] [<code>&#8211;mode&nbsp;</code><i>mode</i>] <code>&#8211;size&nbsp;</code><i>size</i> <i>icon-file</i> [<i>icon-name</i>]</p>
<dt> <code>xdg-icon-resource</code> uninstall [<code>&#8211;noupdate</code>] [<code>&#8211;theme&nbsp;</code><i>theme</i>] [<code>&#8211;context&nbsp;</code><i>context</i>] [<code>&#8211;mode&nbsp;</code><i>mode</i>] <code>&#8211;size&nbsp;</code><i>size</i> <i>icon-name</i></p>
<dt> <code>xdg-icon-resource</code> forceupdate [<code>&#8211;theme&nbsp;</code><i>theme</i>] [<code>&#8211;mode&nbsp;</code><i>mode</i>]</p>
<dt> <code>xdg-icon-resource</code> {<code>&#8211;help</code> | <code>&#8211;manual</code> | <code>&#8211;version</code>}</dl>
<h2>DESCRIPTION</h2>
<dd>The xdg-icon-resource program can be used to install icon resources into the desktop icon system in order to illustrate menu entries, to depict desktop icons or to graphically represent file types. </p>
<p> The desktop icon system identifies icons by name. Depending on the required size, the choice of icon theme and the context in which the icon is used, the desktop icon system locates an appropriate icon resource to depict an icon. Icon resources can be XPM files or PNG files. </p>
<p> The desktop icon system works according to the XDG Icon Theme Specification at m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/icon-theme-spec">http://www.freedesktop.org/wiki/Specifications/icon-theme-spec</a></code>m[]</p>
<h2>COMMANDS</h2>
<p> install</p>
<dl>
<dt>
<dd> Installs the icon file indicated by <i>icon-file</i> to the desktop icon system under the name <i>icon-name</i>. Icon names do not have an extension. If <i>icon-name</i> is not provided the name is derived from <i>icon-file</i>. The icon file must have <i>.png</i> or <i>.xpm</i> as extension. If a corresponding <i>.icon</i> file exists in the same location as <i>icon-file</i> it will be installed as well.</dl>
<p> uninstall</p>
<dl>
<dt>
<dd> Removes the icon indicated by <i>icon-name</i> from the desktop icon system. Note that icon names do not have an extension.</dl>
<p> forceupdate</p>
<dl>
<dt>
<dd> Force an update of the desktop icon system. This is only useful if the last call to xdg-icon-resource included the <code>&#8211;noupdate</code> option.</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;noupdate</code></p>
<dl>
<dt>
<dd> Postpone updating the desktop icon system. If multiple icons are added in sequence this flag can be used to indicate that additional changes will follow and that it is not necessary to update the desktop icon system right away.</dl>
<p> <code>&#8211;novendor</code></p>
<dl>
<dt>
<dd> Normally, xdg-icon-resource checks to ensure that an icon file to be installed in the <i>apps</i> context has a proper vendor prefix. This option can be used to disable that check. </p>
<p> A vendor prefix consists of alpha characters ([a-zA-Z]) and is terminated with a dash (&quot;-&quot;). Companies and organizations are encouraged to use a word or phrase, preferably the organizations name, for which they hold a trademark as their vendor prefix. The purpose of the vendor prefix is to prevent name conflicts.</dl>
<p> <code>&#8211;theme</code> <i>theme</i></p>
<dl>
<dt>
<dd> Installs or removes the icon file as part of <i>theme</i>. If no theme is specified the icons will be installed as part of the default <i>hicolor</i> theme. Applications may install icons under multiple themes but should at least install icons for the default <i>hicolor</i> theme.</dl>
<p> <code>&#8211;context</code> <i>context</i></p>
<dl>
<dt>
<dd> Specifies the context for the icon. Icons to be used in the application menu and as desktop icon should use <i>apps</i> as context which is the default context. Icons to be used as file icons should use <i>mimetypes</i> as context. Other common contexts are <i>actions</i>, <i>devices</i>, <i>emblems</i>, <i>filesystems</i> and <i>stock</i>.</dl>
<p> <code>&#8211;size</code> <i>size</i></p>
<dl>
<dt>
<dd> Specifies the size of the icon. All icons must be square. Common sizes for icons in the apps context are: 16, 22, 32, 48, 64 and 128. Common sizes for icons in the mimetypes context are: 16, 22, 32, 48, 64 and 128</dl>
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
<h2>ENVIRONMENT VARIABLES</h2>
<p> xdg-icon-resource honours the following environment variables: </p>
<p> XDG_UTILS_DEBUG_LEVEL</p>
<dl>
<dt>
<dd> Setting this environment variable to a non-zero numerical value makes xdg-icon-resource do more verbose reporting on stderr. Setting a higher value increases the verbosity.</dl>
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
<p> <code><a href="/docs/linux/man/1-xdg-desktop-icon/">xdg-desktop-icon</a></code>(1), <code><a href="/docs/linux/man/1-xdg-desktop-menu/">xdg-desktop-menu</a></code>(1), <code><a href="/docs/linux/man/1-xdg-mime/">xdg-mime</a></code>(1), m[blue]<code>Icon theme specification</code>m[]<font SIZE="-2">[1]</font></p>
<h2>EXAMPLES</h2>
<p> To install an icon resource to depict a launcher for the application myfoobar, the company ShinyThings Inc. can use: </p>
<dl>
<dt>
<dd>
<pre>
xdg-icon-resource install --size 64 shinythings-myfoobar.png
</pre>
</dl>
<p> To install an icon for a new application/x-foobar file type one can use: </p>
<dl>
<dt>
<dd>
<pre><code>
xdg - icon - resource install-- context mimetypes-- size 48./ mime - foobar - 48.png application - x - foobar xdg - icon - resource install-- context mimetypes-- size 64./ mime - foobar - 64.png application - x - foobar
</code></pre>
</dl>
<p> This will install two icons with the name application-x-foobar but with different sizes.</p>
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
<dd> Icon theme specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/icon-theme-spec/">http://www.freedesktop.org/wiki/Specifications/icon-theme-spec/</a></dl>
</dl>
<h2>Index</h2>
