---
title: "bpluginfo(8)"
name: "bpluginfo"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bpluginfo/"
description: "bpluginfo – Bacula Plugin information utility"
---

<p>bpluginfo &#8211; Bacula Plugin information utility</p>
<h2>Synopsis</h2>
<p><code>bplufinfo</code> [<i>options</i>] <i>plugin_filename.so</i></p>
<h2>Description</h2>
<p>The main purpose of <code>bpluginfo</code> is to display different information about Bacula plugin. You can use it to check a plugin name, author, license and short description. You can use additional &#8216;-a&#8217; option for validating a Bacula Daemons API. In most cases it is not required. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-h</code></p>
<dd>Show usage of the program.</p>
<dt><code>-v</code></p>
<dd>Verbose information printing all available data from the plugin, including plugin header and implemented API.</p>
<dt><code>-i</code></p>
<dd>Display short information from plugin header only. This is a default option. Option incompatible with <code>-f</code> option.</p>
<dt><code>-f</code></p>
<dd>Display information about implemented API functions.</p>
<dt><code>-a&nbsp;<wbr>&lt;api&gt;</code></p>
<dd>You can supply the plugin initialization function with a particular Bacula API number. Without this option a default API number is &#8216;1&#8217;. Option require a numeric argument.</dl>
<h2>Return Code</h2>
<p><code>bpluginfo</code> returns 0 on success, and non-zero on error.</p>
<dl>
<dt>You can check return code to find what was a cause of the error.</p>
<dd>&nbsp;<wbr>*&nbsp;<wbr>0 &#8211; success<br />
&nbsp;<wbr>*&nbsp;<wbr>1 &#8211; cannot load a plugin<br />
&nbsp;<wbr>*&nbsp;<wbr>2 &#8211; cannot find a loadPlugin function<br />
&nbsp;<wbr>*&nbsp;<wbr>3 &#8211; cannot find an unloadPlugin function<br />
&nbsp;<wbr>*&nbsp;<wbr>10 &#8211; not enough memory</dl>
<h2>Example Usage</h2>
<p>This is an example of bplufinfo usage with verbose option (-v) and default plugin. </p>
<dl>
<dd>
<pre><code>$ bpluginfo -v bpipe-fd.so 
Plugin type: File Daemon plugin
Plugin magic: *FDPluginData*
Plugin version: 1
Plugin release date: January 2008
Plugin author: Kern Sibbald
Plugin license: Bacula AGPLv3
Plugin description: Bacula Pipe File Daemon Plugin
Plugin API version: 6
Plugin functions:
 newPlugin()
 freePlugin()
 getPluginValue()
 setPluginValue()
 handlePluginEvent()
 startBackupFile()
 endBackupFile()
 startRestoreFile()
 endRestoreFile()
 pluginIO()
 createFile()
 setFileAttributes()
</code></pre>
</dl>
<h2>Author</h2>
<p>Written by Radoslaw Korzeniewski (c) Inteos Sp. z o.o.</p>
<h2>Bugs</h2>
<p>Does not handle all required bacula functions callbacks which can lead to utility crash. </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;support [at] inteos.pl&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2012 Free Software Foundation Europe e.V.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>bacula-dir,</code> <code>bacula-sd,</code> <code>bacula-fd,</code> <code>Bacula Plugins API</code> </p>
