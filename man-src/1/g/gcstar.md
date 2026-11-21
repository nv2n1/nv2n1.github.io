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
<dt><code>-u, &#8211;update</code></dt>
<dd> Tell GCstar to look for available updates</dd>
<dt><code>-a, &#8211;all</code></dt>
<dd> Update all components</dd>
<dt><code>-c, &#8211;collection</code></dt>
<dd> Update collection models</dd>
<dt><code>-w, &#8211;website</code></dt>
<dd> Update plugins to download information</dd>
<dt><code>-i, &#8211;import</code></dt>
<dd> Update plugins to import data</dd>
<dt><code>-e, &#8211;export</code></dt>
<dd> Update plugins to export data</dd>
<dt><code>-l, &#8211;lang</code></dt>
<dd> Update translations</dd>
<dt><code>-n, &#8211;noproxy</code></dt>
<dd> Don&#8217;t ask for a proxy</dd></dl>
<h3>EXECUTE-OPTIONS</h3>
<dl>
<dt><code>-x, &#8211;execute</code></dt>
<dd> Enter non-interactive mode</dd>
<dt><code>-c, &#8211;collection MODEL</code></dt>
<dd> Specify the collection type</dd>
<dt><code>-w, &#8211;website PLUGIN</code></dt>
<dd> Specify the plugin to use to download information</dd>
<dt><code>-i, &#8211;import PLUGIN</code></dt>
<dd> Specify the plugin to use to import a collection</dd>
<dt><code>-e, &#8211;export PLUGIN</code></dt>
<dd> Specify the plugin to use to export the collection</dd>
<dt><code>-f, &#8211;fields FILENAME</code></dt>
<dd> File containing fields list to use for import/export</dd>
<dt><code>-o, &#8211;output FILENAME</code></dt>
<dd> Write output in FILENAME instead of standard output</dd>
<dt><code>&#8211;download TITLE</code></dt>
<dd> Search for the item with TITLE as name</dd>
<dt><code>&#8211;importprefs PREFERENCES</code></dt>
<dd> Preferences for the import plugin</dd>
<dt><code>&#8211;exportprefs PREFERENCES</code></dt>
<dd> Preferences for the export plugin</dd>
<dt>Preferences for import/export plugins are specified using this schema</dt>
<dd> Key1=&gt;Value1,Key2=&gt;Value2</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></dt>
<dd> Used to define following variables if needed</dd>
<dt><code>XDG_CONFIG_HOME</code></dt>
<dd> Where configuration files should be stored. If not defined: $HOME/.config</dd>
<dt><code>XDG_DATA_HOME</code></dt>
<dd> Where some data will be stored. If not defined: $HOME/.local/share</dd></dl>
<h2>BUGS REPORTING</h2>
<p> To report bugs, please use this forum: <a rel="nofollow" href="http://forums.gcstar.org/viewforum.php?id=4">http://forums.gcstar.org/viewforum.php?id=4</a></p>
<h2>AUTHORS</h2>
<dl>
<dt>Tian &lt;tian [at] c-sait.net&gt;</dt>
<dd> <a rel="nofollow" href="http://www.gcstar.org/">http://www.gcstar.org/</a> </dd>
</dl>
