---
title: "desktoptojson(8)"
name: "desktoptojson"
section: "8"
letter: "d"
url: "/docs/linux/man/8-desktoptojson/"
description: "desktoptojson – Converts a .desktop file to a .json file."
---

<p>desktoptojson &#8211; Converts a .desktop file to a .json file.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>desktoptojson</code> &#8211;input&nbsp;<wbr><i>DESKTOP-FILE</i> &#8211;output&nbsp;<wbr><i>JSON-FILE</i></p>
<dt> <code>desktoptojson</code> {&#8211;version | &#8211;help}</dl>
<h2>Description</h2>
<dd>The KService framework uses information contained in .desktop files to locate services, including plugins for Qt5-based applications and libraries. The Qt5 plugin system, however, uses JSON data embedded in the plugin itself. <code>desktoptojson</code> allows the information contained in a .desktop file to also be used as the embedded data for a Qt5 plugin by converting the .desktop file entries into JSON data. </p>
<p> The generated JSON data is a JSON object that maps the entries from the [Desktop Entry] group of the .desktop file. Any other groups are ignored. Most entries are just converted to JSON strings, but certain entries (such as Hidden and X-KDE-PluginInfo-EnabledByDefault) are known to be boolean values and converted as such, and similarly some (such as X-KDE-ServiceTypes and X-KDE-PluginInfo-Depends) are always converted to arrays of strings.</p>
<h2>Options</h2>
<p><code>&#8211;input </code><i>DESKTOP-FILE</i></p>
<dl>
<dd>The .desktop file to convert.</dl>
<p> <code>&#8211;output </code><i>JSON-FILE</i></p>
<dl>
<dd>The file to write the generated JSON data to.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show a brief help text.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Show version information.</dl>
<h2>Usage</h2>
<p>Most users of this utility will use the CMake macro <code>kservice_desktop_to_json</code> as part of the process of building a plugin. </p>
<dl>
<dd>
<pre>add_library(myplugin MODULE ${myplugin_SRCS})
kservice_desktop_to_json(myplugin myplugin.desktop)</pre>
</dl>
<p> This will produce the JSON file myplugin.json, which can be referenced from the <code>K_PLUGIN_FACTORY_WITH_JSON</code> or <code>Q_PLUGIN_METADATA</code> macros.</p>
<h2>Bugs</h2>
<p>Please use m[blue]<code>KDE&#8217;s bugtracker</code>m[]<font SIZE="-2">[1]</font> to report bugs.</p>
<h2>Authors</h2>
<p><code>Scarlett Clark</code> &lt;scarlett [at] scarlettgatelyclark.com&gt;</p>
<dl>
<dd>Wrote the original documentation.</dl>
<p> <code>Alex Merry</code> &lt;alexmerry [at] kde.org&gt;</p>
<dl>
<dd>Edited the documentation.</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>KDE&#8217;s bugtracker</p>
<dl>
<dd><a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dl>
