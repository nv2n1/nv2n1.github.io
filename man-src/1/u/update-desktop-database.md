---
title: "update-desktop-database(1)"
name: "update-desktop-database"
section: "1"
letter: "u"
url: "/docs/linux/man/1-update-desktop-database/"
description: "update-desktop-database – Build cache database of MIME types handled by desktop files"
---

<h2 class="name">NAME</h2>
<p> update-desktop-database &#8211; Build cache database of MIME types handled by desktop files </p>
<h2>SYNOPSIS</h2>
<p> <code>update-desktop-database [-q|&#8211;quiet] [-v|&#8211;verbose] [DIRECTORY&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>update-desktop-database</i> program is a tool to build a cache database of the MIME types handled by desktop files. </p>
<p> The cache database contains the list of MIME types that can be handled by desktop files, as well as, for each MIME type, a list of desktop files that can handle this MIME type. This cache database ease the work of applications that need to find an application that can open a document of a specific MIME type: those applications will not have to parse all the desktop files existing on the system, and can instead parse this cache database. </p>
<p> If no <i>DIRECTORY</i> is specified as argument, the desktop files that will be processed are the ones installed in <code>$XDG_DATA_DIRS/applications</code>. </p>
<p> If both the <i>&#8211;quiet</i> and <i>&#8211;verbose</i> options are used, then <i>&#8211;verbose</i> will be ignored.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>-q, &#8211;quiet</i></p>
<dd> Do not display any information about processing and updating progress.</p>
<dt><i>-v, &#8211;verbose</i></p>
<dd> Display more information about processing and updating progress.</dl>
<h2>NOTES</h2>
<p> If an invalid MIME type is met, it will be ignored and the creation of the cache database will continue. </p>
<p> The format of the cache database is a simple desktop entry format, with a <code>MIME Cache</code> group, containing one key per MIME type. The key name is the MIME type, and the key value is the list of desktop file that can handle this MIME type. </p>
<p> The order of the desktop files found for a MIME type is not significant. Therefore, an external mechanism must be used to determine what is the preferred desktop file for a MIME type.</p>
<h2>EXAMPLE</h2>
<p> Here is a simple example of a cache database:</p>
<dl>
<dt>
<dd>
&nbsp;[MIME Cache]<br />
&nbsp;application/x-shellscript=gedit.desktop;<br />
&nbsp;text/plain=gedit.desktop;gvim.desktop;<br />
&nbsp;video/webm=totem.desktop;</dl>
<p> This cache database is created with three desktop files, each containing a <code>MimeType</code> key:</p>
<dl>
<dt>
<dd>
&nbsp;<code>gedit.desktop</code>: MimeType=text/plain;application/x-shellscript;<br />
&nbsp;<code>gvim.desktop</code>: MimeType=text/plain;<br />
&nbsp;<code>totem.desktop</code>: MimeType=video/webm;</dl>
<h2>FILES</h2>
<p> <code>$XDG_DATA_DIRS/applications/mimeinfo.cache</code></p>
<dl>
<dt>
<dd> This file is the cache database created by <i>update-desktop-database</i>.</dl>
<h2>BUGS</h2>
<p> If you find bugs in the <i>update-desktop-database</i> program, please report these on <a rel="nofollow" href="https://bugs.freedesktop.org.">https://bugs.freedesktop.org.</a> </p>
<h2>Index</h2>
