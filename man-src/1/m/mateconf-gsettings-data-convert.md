---
title: "mateconf-gsettings-data-convert(1)"
name: "mateconf-gsettings-data-convert"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mateconf-gsettings-data-convert/"
description: "mateconf-gsettings-data-convert – MateConf to GSettings data migration"
---

<h2 class="name">NAME</h2>
<p> mateconf-gsettings-data-convert &#8211; MateConf to GSettings data migration </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mateconf-gsettings-data-convert</code> [option&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>mateconf-gsettings-data-convert</code></p>
<dd>reads values out of the users MateConf database and stores them in GSettings. </p>
<p> The information about the mapping from MateConf keys to GSettings keys is taken from files in <i>/usr/share/MateConf/gsettings</i>. Each file in that directory is read as a key file, with sections for each GSettings schema that is being converted. The entries in each section map GSettings keys to paths in the MateConf database. Currently, <code>mateconf-gsettings-data-convert</code> supports all basic MateConf types as well as lists of strings and lists of integers. </p>
<p> A simple example might look like this: </p>
<dl>
<dt>
<dd>
<pre>
[org.mate.fonts]
antialiasing = /desktop/mate/font_rendering/antialiasing
dpi = /desktop/mate/font_rendering/dpi
hinting = /desktop/mate/font_rendering/hinting
rgba_order = /desktop/mate/font_rendering/rgba_order
</pre>
</dl>
<p> If the GSettings schema does not have a fixed path, you must specify the path in the group name, separated by a colon character: </p>
<dl>
<dt>
<dd>
<pre>
[org.mate.fonts:/desktop/mate/font-rendering/]
</pre>
</dl>
<p> <code>mateconf-gsettings-data-convert</code> keeps a list of the key files it has already converted, so it is safe to run it repeatedly to handle newly appeared key files. The expected use of this utility is to make each application install a key file for the MateConf keys that it wants to be migrated, and run <code>mateconf-gsettings-data-convert</code> every time a user logs in.</p>
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
<p> <code><a href="/docs/linux/man/1-mateconf-gsettings-schema-convert/">mateconf-gsettings-schema-convert</a></code>(1) is a related command that helps with the conversion of schemas from MateConf to GSettings. </p>
<h2>Index</h2>
