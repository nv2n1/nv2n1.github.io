---
title: "gsettings-data-convert(1)"
name: "gsettings-data-convert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsettings-data-convert/"
description: "gsettings-data-convert – GConf to GSettings data migration"
---

<h2 class="name">NAME</h2>
<p> gsettings-data-convert &#8211; GConf to GSettings data migration </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gsettings-data-convert</code> [option&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gsettings-data-convert</code></p>
<dd>reads values out of the users GConf database and stores them in GSettings. </p>
<p> The information about the mapping from GConf keys to GSettings keys is taken from files in /usr/share/GConf/gsettings. Each file in that directory is read as a key file, with sections for each GSettings schema that is being converted. The entries in each section map GSettings keys to paths in the GConf database. Currently, <code>gsettings-data-convert</code> supports all basic GConf types as well as lists of strings and lists of integers. </p>
<p> A simple example might look like this: </p>
<dl>
<dt>
<dd>
<pre>
[org.gnome.fonts]
antialiasing = /desktop/gnome/font_rendering/antialiasing
dpi = /desktop/gnome/font_rendering/dpi
hinting = /desktop/gnome/font_rendering/hinting
rgba_order = /desktop/gnome/font_rendering/rgba_order
</pre>
</dl>
<p> If the GSettings schema does not have a fixed path, you must specify the path in the group name, separated by a colon character: </p>
<dl>
<dt>
<dd>
<pre>
[org.gnome.fonts:/desktop/gnome/font-rendering/]
</pre>
</dl>
<p> <code>gsettings-data-convert</code> keeps a list of the key files it has already converted, so it is safe to run it repeatedly to handle newly appeared key files. The expected use of this utility is to make each application install a key file for the GConf keys that it wants to be migrated, and run <code>gsettings-data-convert</code> every time a user logs in.</p>
<h3>Options</h3>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help and exit</dl>
<p> <code>&#8211;dry-run</code></p>
<dl>
<dt>
<dd> Do not make any changes, just report what would be done</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Show verbose messages</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gsettings-schema-convert/">gsettings-schema-convert</a></code>(1) is a related command that helps with the conversion of schemas from GConf to GSettings. </p>
<h2>Index</h2>
