---
title: "desktop-file-validate(1)"
name: "desktop-file-validate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-desktop-file-validate/"
description: "desktop-file-validate – Validate desktop entry files"
---

<h2 class="name">NAME</h2>
<p> desktop-file-validate &#8211; Validate desktop entry files </p>
<h2>SYNOPSIS</h2>
<p> <code>desktop-file-validate [&#8211;no-hints] [&#8211;no-warn-deprecated] [&#8211;warn-kde] FILE&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>desktop-file-validate</i> program is a tool to validate desktop entry files according to the Desktop Entry specification 1.4. </p>
<p> The specification describes a file format to provide information such as name, icon and description for an application. Such a file can then be used as an application launcher and to display the application in the applications menu. </p>
<p> For information about the Desktop Entry specification, see <i><a rel="nofollow" href="http://freedesktop.org/wiki/Specifications/desktop-entry-spec">http://freedesktop.org/wiki/Specifications/desktop-entry-spec</a></i>. </p>
<p> The desktop entry files are commonly called <code>desktop files</code>.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;no-hints</i></p>
<dd> Do not output hints about things that might be improved in the desktop file.</p>
<dt><i>&#8211;no-warn-deprecated</i></p>
<dd> Do not warn about usage of deprecated items that were defined in previous versions of the specification.</p>
<dt><i>&#8211;warn-kde</i></p>
<dd> Warn about usage of KDE extensions to the specification. This includes the use of the <code>KDE Desktop Entry</code> group, of the <code>ServiceTypes</code>, <code>DocPath</code>, <code>Keywords</code>, <code>InitialPreference</code>, <code>Dev</code>, <code>FSType</code>, <code>MountPoint</code>, <code>ReadOnly</code>, <code>UnmountIcon</code> keys, or of the <code>Service</code>, <code>ServiceType</code> and <code>FSDevice</code> types.</dl>
<h2>BUGS</h2>
<p> If you find bugs in the <i>desktop-file-validate</i> program, please report these on <a rel="nofollow" href="https://bugs.freedesktop.org.">https://bugs.freedesktop.org.</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-desktop-file-edit/">desktop-file-edit</a>(1)</code> <code><a href="/docs/linux/man/1-desktop-file-install/">desktop-file-install</a>(1)</code> </p>
<h2>Index</h2>
