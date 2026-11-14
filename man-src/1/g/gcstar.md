---
title: "gcstar(1)"
name: "gcstar"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcstar/"
description: "GCstar – Personal collection manager"
---

<h2>NAME</h2>
<p> GCstar &#8211; Personal collection manager</p>
<h2>SYNOPSIS</h2>
<p> <code>gcstar</code> [-u UPDATE-OPTIONS] [-x EXECUTE-OPTIONS] [FILENAME]</p>
<h2>DESCRIPTION</h2>
<p> <code>GCstar</code> is a Gtk2 program used to manage personal collections.</p>
<h2>OPTIONS</h2>
<p> Without any option, it will open FILENAME if specified or the previously opened file. There are also two groups of options. </p>
<h3>UPDATE-OPTIONS</h3>
<dl>
<dt><code>-u, &#8211;update</code></p>
<dd> Tell GCstar to look for available updates</p>
<dt><code>-a, &#8211;all</code></p>
<dd> Update all components</p>
<dt><code>-c, &#8211;collection</code></p>
<dd> Update collection models</p>
<dt><code>-w, &#8211;website</code></p>
<dd> Update plugins to download information</p>
<dt><code>-i, &#8211;import</code></p>
<dd> Update plugins to import data</p>
<dt><code>-e, &#8211;export</code></p>
<dd> Update plugins to export data</p>
<dt><code>-l, &#8211;lang</code></p>
<dd> Update translations</p>
<dt><code>-n, &#8211;noproxy</code></p>
<dd> Don&#8217;t ask for a proxy</dl>
<h3>EXECUTE-OPTIONS</h3>
<dl>
<dt><code>-x, &#8211;execute</code></p>
<dd> Enter non-interactive mode</p>
<dt><code>-c, &#8211;collection MODEL</code></p>
<dd> Specify the collection type</p>
<dt><code>-w, &#8211;website PLUGIN</code></p>
<dd> Specify the plugin to use to download information</p>
<dt><code>-i, &#8211;import PLUGIN</code></p>
<dd> Specify the plugin to use to import a collection</p>
<dt><code>-e, &#8211;export PLUGIN</code></p>
<dd> Specify the plugin to use to export the collection</p>
<dt><code>-f, &#8211;fields FILENAME</code></p>
<dd> File containing fields list to use for import/export</p>
<dt><code>-o, &#8211;output FILENAME</code></p>
<dd> Write output in FILENAME instead of standard output</p>
<dt><code>&#8211;download TITLE</code></p>
<dd> Search for the item with TITLE as name</p>
<dt><code>&#8211;importprefs PREFERENCES</code></p>
<dd> Preferences for the import plugin</p>
<dt><code>&#8211;exportprefs PREFERENCES</code></p>
<dd> Preferences for the export plugin</p>
<dt>Preferences for import/export plugins are specified using this schema</p>
<dd> Key1=&gt;Value1,Key2=&gt;Value2</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></p>
<dd> Used to define following variables if needed</p>
<dt><code>XDG_CONFIG_HOME</code></p>
<dd> Where configuration files should be stored. If not defined: $HOME/.config</p>
<dt><code>XDG_DATA_HOME</code></p>
<dd> Where some data will be stored. If not defined: $HOME/.local/share</dl>
<h2>BUGS REPORTING</h2>
<p> To report bugs, please use this forum: <a rel="nofollow" href="http://forums.gcstar.org/viewforum.php?id=4">http://forums.gcstar.org/viewforum.php?id=4</a></p>
<h2>AUTHORS</h2>
<dl>
<dt>Tian &lt;tian [at] c-sait.net&gt;</p>
<dd> <a rel="nofollow" href="http://www.gcstar.org/">http://www.gcstar.org/</a> </p>
</dl>
<h2>Index</h2>
