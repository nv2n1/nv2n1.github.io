---
title: "gconftool(1)"
name: "gconftool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gconftool/"
description: "gconftool-2 – GNOME configuration tool"
---

<h2 class="name">NAME</h2>
<p> gconftool-2 &#8211; GNOME configuration tool </p>
<h2>SYNOPSIS</h2>
<p> <code>gconftool-2</code> [-?] [-?|&#8211;help] [&#8211;usage] [-s|&#8211;set] [-g|&#8211;get] [&#8211;set-schema] [-u|&#8211;unset] [&#8211;recursive-unset] [-a|&#8211;all-entries] [&#8211;all-dirs] [&#8211;dump] [&#8211;load=STRING] [-R|&#8211;recursive-list] [&#8211;dir-exists=STRING] [&#8211;shutdown] [-p|&#8211;ping] [&#8211;spawn] [-t|&#8211;type int|bool|float|string|list|pair] [-T|&#8211;get-type] [&#8211;get-list-size] [&#8211;get-list-element] [&#8211;list-type=int|bool|float|string] [&#8211;car-type=int|bool|float|string] [&#8211;cdr-type=int|bool|float|string] [&#8211;short-desc=DESCRIPTION] [&#8211;long-desc=DESCRIPTION] [&#8211;owner=OWNER] [&#8211;install-schema-file=FILENAME] [&#8211;config-source=SOURCE] [&#8211;direct] [&#8211;makefile-install-rule] [&#8211;makefile-uninstall-rule] [&#8211;break-key] [&#8211;break-directory] [&#8211;short-docs] [&#8211;long-docs] [&#8211;get-schema-name] [&#8211;apply-schema] [&#8211;unapply-schema] [&#8211;get-default-source] [-v|&#8211;version]</p>
<h2>DESCRIPTION</h2>
<p> Each preference in the GConf repository is expressed as a key-value pair. A GConf preference key is an element in the GConf repository that corresponds to an application preference. Preference keys typically have simple values such as strings, integers, or lists of strings and integers. The default key-value pairs are installed on the system, and are known as schemas. gconftool-2 is the command-line interface tool that enables you to set the values of keys, display the values of keys, and install schemas from schema definition files when you install an application. The GConf preference keys are stored and managed by the GConf daemon (gconfd-2). These keys are cached in memory, and saved to disk in XML format when appropriate.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code>, <code>&#8211;set</code></p>
<dd> Set a key to a value and sync. Use with <code>&#8211;type</code>.</p>
<dt><code>-g</code>, <code>&#8211;get</code></p>
<dd> Print the value of a key to standard output.</p>
<dt><code>-u</code>, <code>&#8211;unset</code></p>
<dd> Unset the keys on the command line.</p>
<dt><code>&#8211;recursive-unset</code></p>
<dd> Recursively unset all keys at or below the key/directory names on the command line.</p>
<dt><code>-a</code>, <code>&#8211;all-entries</code></p>
<dd> Print all key/value pairs in a directory.</p>
<dt><code>&#8211;all-dirs</code></p>
<dd> Print all subdirectories in a directory.</p>
<dt><code>-R</code>, <code>&#8211;recursive-list</code></p>
<dd> Print all subdirectories and entries under a dir, recursively.</p>
<dt><code>&#8211;dir-exists</code>=<i>STRING</i></p>
<dd> Return 0 if the directory exists, 2 if it does not.</p>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>int</i>|bool|float|string|list|pair</p>
<dd> Specify the type of the value being set, or the type of the value a schema describes. Unique abbreviations are allowed.</p>
<dt><code>&#8211;list-type</code>=<i>int</i>|bool|float|string</p>
<dd> Specify the type of the list value being set, or the type of the value a schema describes. Unique abbreviations are allowed.</p>
<dt><code>&#8211;car-type</code>=<i>int</i>|bool|float|string</p>
<dd> Specify the type of the car pair value being set, or the type of the value a schema describes. Unique abbreviations are allowed.</p>
<dt><code>&#8211;cdr-type</code>=<i>int</i>|bool|float|string</p>
<dd> Specify the type of the cdr pair value being set, or the type of the value a schema describes. Unique abbreviations are allowed.</p>
<dt><code>&#8211;short-desc</code>=<i>DESCRIPTION</i></p>
<dd> Specify a short half-line description to go in a schema.</p>
<dt><code>&#8211;long-desc</code>=<i>DESCRIPTION</i></p>
<dd> Specify a several-line description to go in a schema.</p>
<dt><code>&#8211;owner</code>=<i>OWNER</i></p>
<dd> Specify the owner of a schema.</p>
<dt><code>&#8211;install-schema-file</code>=<i>FILENAME</i></p>
<dd> Specify a schema file to be installed</p>
<dt><code>&#8211;config-source</code>=<i>SOURCE</i></p>
<dd> Specify a configuration source to use rather than the default path</p>
<dt><code>&#8211;direct</code></p>
<dd> Access the config database directly, bypassing server. Requires that gconfd is not running.</p>
<dt><code>&#8211;set-schema</code></p>
<dd> Set a schema and sync. Use with <code>&#8211;short-desc</code>, <code>&#8211;long-desc</code>, <code>&#8211;owner</code>, and <code>&#8211;type</code>.</p>
<dt><code>&#8211;makefile-install-rule</code></p>
<dd> Properly installs schema files on the command line into the database. GCONF_CONFIG_SOURCE environment variable should be set to a non-default config source or set to the empty string to use the default.</p>
<dt><code>&#8211;break-key</code></p>
<dd> Torture-test an application by setting and unsetting a bunch of values of different types for keys on the command line.</p>
<dt><code>&#8211;break-directory</code></p>
<dd> Torture-test an application by setting and unsetting a bunch of keys inside the directories on the command line.</p>
<dt><code>&#8211;short-docs</code></p>
<dd> Get the short doc string for a key</p>
<dt><code>&#8211;long-docs</code></p>
<dd> Get the long doc string for a key</p>
<dt><code>&#8211;get-schema-name</code></p>
<dd> Get the name of the schema applied to this key</p>
<dt><code>&#8211;apply-schema</code></p>
<dd> Specify the schema name followed by the key to apply the schema name to</p>
<dt><code>&#8211;unapply-schema</code></p>
<dd> Remove any schema name applied to the given keys</p>
<dt><code>&#8211;get-default-source</code></p>
<dd> Get the name of the default source.</p>
<dt><code>&#8211;shutdown</code></p>
<dd> Shut down gconfd. <code>Don&#8217;t use this option without good reason.</code></p>
<dt><code>-p</code>, <code>&#8211;ping</code></p>
<dd> Return 0 if gconfd is running, 2 if not.</p>
<dt><code>&#8211;spawn</code></p>
<dd> Launch the config server (gconfd). (Normally happens automatically when needed.)</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print version</dl>
<p> Help options</p>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show the help message.</dl>
<h2>EXAMPLES</h2>
<p> Display the path to the current desktop wallpaper.</p>
<dl>
<dt>
<dd> gconftool-2 &#8211;get /desktop/gnome/background/picture_filename</dl>
<p> Change the widget font to &quot;Serif 12&quot;</p>
<dl>
<dt>
<dd> gconftool-2 &#8211;type string &#8211;set /desktop/gnome/interface/font_name &quot;Serif 12&quot;</dl>
<h2>AUTHOR</h2>
<p> <code>GConf</code> was written by Havoc Pennington &lt;hp [at] redhat.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> The GConf web site, <i><a rel="nofollow" href="http://www.gnome.org/projects/gconf/.">http://www.gnome.org/projects/gconf/.</a> </p>
<p> </i></p>
<h2>Index</h2>
