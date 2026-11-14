---
title: "desktop-file-edit(1)"
name: "desktop-file-edit"
section: "1"
letter: "d"
url: "/docs/linux/man/1-desktop-file-edit/"
description: "desktop-file-install, desktop-file-edit – Installation and edition of desktop files"
---

<h2 class="name">NAME</h2>
<p> desktop-file-install, desktop-file-edit &#8211; Installation and edition of desktop files </p>
<h2>SYNOPSIS</h2>
<p> <code>desktop-file-install [&#8211;dir=DIR] [-m MODE|&#8211;mode=MODE]</code> <code>[&#8211;vendor=VENDOR] [&#8211;delete-original]</code> <code>[&#8211;rebuild-mime-info-cache]</code> <code>[EDITOPTION]&#8230; FILE&#8230;</code> </p>
<p> <code>desktop-file-edit [EDITOPTION]&#8230; FILE</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>desktop-file-install</i> program is a tool to install, and optionally edit, desktop files. The <i>desktop-file-edit</i> program is a tool to edit a desktop file. They are mostly useful for developers and packagers. </p>
<p> Various options are available to edit the desktop files. The edit options can be specified more than once and will be processed in the same order as the options passed to the program. </p>
<p> <i>desktop-file-install</i> and <i>desktop-file-edit</i> will always try to validate the resulting desktop file. A failure to validate might lead to the abortion of the installation of the desktop files. </p>
<p> The list of registered categories and desktop environments is defined in the Menu specification: <i><a rel="nofollow" href="http://freedesktop.org/wiki/Specifications/menu-spec">http://freedesktop.org/wiki/Specifications/menu-spec</a></i>.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;dir=DIR</i></p>
<dd> Install desktop files to the <i>DIR</i> directory.</p>
<dt><i>-m, &#8211;mode=MODE</i></p>
<dd> Set the permissions of the destination files to <i>MODE</i>.</p>
<dt><i>&#8211;vendor=VENDOR</i></p>
<dd> Add a vendor prefix to the desktop files. If a file already has this prefix, nothing happens; else, the file will be named <i>VENDOR</i>&#8211;<i>FILE</i>. For example: if <i>VENDOR</i> is <code>freedesktop.org</code> and <i>FILE</i> is <code>specification.desktop</code>, the result file will be <code>freedesktop.org-specification.desktop</code>.</p>
<dt><i>&#8211;delete-original</i></p>
<dd> Delete the source desktop files, leaving only the target files. Effectively &quot;renames&quot; the desktop files.</p>
<dt><i>&#8211;rebuild-mime-info-cache</i></p>
<dd> Rebuild the MIME types application database after installing the desktop files. See <i><a href="/docs/linux/man/1-update-desktop-database/">update-desktop-database</a>(1)</i> for information about this database.</dl>
<h2>EDIT OPTIONS</h2>
<p> The following edit options are supported:</p>
<dl>
<dt><i>&#8211;set-key=KEY</i></p>
<dd> Set the KEY key to the value passed to the next <i>&#8211;set-value</i> option. A matching <i>&#8211;set-value</i> option is mandatory.</p>
<dt><i>&#8211;set-value=VALUE</i></p>
<dd> Set the key specified with the previous <i>&#8211;set-key</i> option to VALUE. A matching <i>&#8211;set-key</i> option is mandatory.</p>
<dt><i>&#8211;set-name=NAME</i></p>
<dd> Set the name (key <code>Name</code>) to NAME. If a name was already set, it will be overridden. Localizations of the old name will be removed.</p>
<dt><i>&#8211;copy-name-to-generic-name</i></p>
<dd> Copy the value of the <code>Name</code> key to the <code>GenericName</code> key. Note that a desktop file requires a <code>Name</code> key to be valid, so this option will always have an effect.</p>
<dt><i>&#8211;set-generic-name=GENERIC-NAME</i></p>
<dd> Set the generic name (key <code>GenericName</code>) to GENERIC-NAME. If a generic name was already set, it will be overridden. Localizations of the old generic name will be removed.</p>
<dt><i>&#8211;copy-generic-name-to-name</i></p>
<dd> Copy the value of the <code>GenericName</code> key to the <code>Name</code> key, if the <code>GenericName</code> key is present.</p>
<dt><i>&#8211;set-comment=COMMENT</i></p>
<dd> Set the comment (key <code>Comment</code>) to COMMENT. If a comment was already set, it will be overridden. Localizations of the old comment will be removed.</p>
<dt><i>&#8211;set-icon=ICON</i></p>
<dd> Set the icon (key <code>Icon</code>) to ICON. If an icon was already set, it will be overridden. Localizations of the old icon will be removed.</p>
<dt><i>&#8211;add-category=CATEGORY</i></p>
<dd> Add <i>CATEGORY</i> to the list of categories (key <code>Categories</code>). If <i>CATEGORY</i> was already present in the list, this operation is a no-op. A non-registered category should be prefixed with <code>X-</code>.</p>
<dt><i>&#8211;remove-category=CATEGORY</i></p>
<dd> Remove <i>CATEGORY</i> from the list of categories (key <code>Categories</code>). If <i>CATEGORY</i> was not present in the list, this operation is a no-op.</p>
<dt><i>&#8211;add-mime-type=MIME-TYPE</i></p>
<dd> Add <i>MIME-TYPE</i> to the list of MIME types (key <code>MimeType</code>). If <i>MIME-TYPE</i> was already present in the list, this operation is a no-op.</p>
<dt><i>&#8211;remove-mime-type=MIME-TYPE</i></p>
<dd> Remove <i>MIME-TYPE</i> from the list of MIME types (key <code>MimeType</code>). If <i>MIME-TYPE</i> was not present in the list, this operation is a no-op.</p>
<dt><i>&#8211;add-only-show-in=ENVIRONMENT</i></p>
<dd> Add <i>ENVIRONMENT</i> to the list of desktop environments where the desktop files should be displayed (key <code>OnlyShowIn</code>). If <i>ENVIRONMENT</i> was already present in the list, this operation is a no-op. A non-registered desktop environment should be prefixed with <code>X-</code>. Note that an empty <code>OnlyShowIn</code> key in a desktop file means that the desktop file will be displayed in all environments.</p>
<dt><i>&#8211;remove-only-show-in=ENVIRONMENT</i></p>
<dd> Remove <i>ENVIRONMENT</i> from the list of desktop environments where the desktop files should be displayed (key <code>OnlyShowIn</code>). If <i>ENVIRONMENT</i> was not present in the list, this operation is a no-op.</p>
<dt><i>&#8211;add-not-show-in=ENVIRONMENT</i></p>
<dd> Add <i>ENVIRONMENT</i> to the list of desktop environments where the desktop files should not be displayed (key <code>NotShowIn</code>). If <i>ENVIRONMENT</i> was already present in the list, this operation is a no-op. A non-registered desktop environment should be prefixed with <code>X-</code>. Note that an empty <code>NotShowIn</code> key in a desktop file means that the desktop file will be displayed in all environments.</p>
<dt><i>&#8211;remove-not-show-in=ENVIRONMENT</i></p>
<dd> Remove <i>ENVIRONMENT</i> from the list of desktop environments where the desktop files should not be displayed (key <code>NotShowIn</code>). If <i>ENVIRONMENT</i> was not present in the list, this operation is a no-op.</p>
<dt><i>&#8211;remove-key=KEY</i></p>
<dd> Remove the <i>KEY</i> key from the desktop files, if present.</dl>
<h2>ENVIRONMENT</h2>
<p> Some environment variables change the behavior of <i>desktop-file-install</i>: </p>
<p> <code>DESKTOP_FILE_VENDOR</code></p>
<dl>
<dt>
<dd> This variable can be used as an alternative to the <i>&#8211;vendor</i> option. If the <i>&#8211;vendor</i> option is used, this environment variable will be ignored.</dl>
<p> <code>DESKTOP_FILE_INSTALL_DIR</code></p>
<dl>
<dt>
<dd> This variable can be used as an alternative to the <i>&#8211;dir</i> option. If the <i>&#8211;dir</i> option is used, this environment variable will be ignored.</dl>
<p> <code>RPM_BUILD_ROOT</code></p>
<dl>
<dt>
<dd> This variable is set when building RPM packages. If the <i>&#8211;dir</i> option and the <code>DESKTOP_FILE_INSTALL_DIR</code> environment variable are not used, it will automatically be prepended to the default install directory to install the desktop files appropriately when building packages.</dl>
<h2>BUGS</h2>
<p> If you find bugs in the <i>desktop-file-install</i> program, please report these on <a rel="nofollow" href="https://bugs.freedesktop.org.">https://bugs.freedesktop.org.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-desktop-file-validate/">desktop-file-validate</a>(1)</code> <code><a href="/docs/linux/man/1-update-desktop-database/">update-desktop-database</a>(1)</code> </p>
<h2>Index</h2>
