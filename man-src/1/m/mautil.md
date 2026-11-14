---
title: "mautil(1)"
name: "mautil"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mautil/"
description: "mautil – Mono.Addins Setup Utility"
---

<h2>NAME</h2>
<p> mautil &#8211; Mono.Addins Setup Utility</p>
<h2>SYNOPSIS</h2>
<p> <code>mautil</code> [<i>options</i>] <i>&lt;command&gt; </i>[<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>mautil</code> tool works with Mono.Addins repositories and packages.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;registry</code>, <code>-reg</code></p>
<dd> Specify add-in registry path</p>
<dt><code>&#8211;path</code>, <code>-p</code></p>
<dd> Specify startup path</p>
<dt><code>-v</code></p>
<dd> Verbose output</dl>
<h3>Add-in commands:</h3>
<dl>
<dt><code>install</code>, <code>i</code></p>
<dd> Installs add-ins.</p>
<dt><code>uninstall</code>, <code>u</code></p>
<dd> Uninstalls add-ins.</p>
<dt><code>check-install</code>, <code>ci</code></p>
<dd> Checks installed add-ins.</p>
<dt><code>update</code>, <code>up</code></p>
<dd> Updates installed add-ins.</p>
<dt><code>list</code>, <code>l</code></p>
<dd> Lists installed add-ins.</p>
<dt><code>list-av</code>, <code>la</code></p>
<dd> Lists add-ins available in registered repositories.</p>
<dt><code>list-update</code>, <code>lu</code></p>
<dd> Lists available add-in updates.</dl>
<h3>Repository Commands:</h3>
<dl>
<dt><code>rep-add</code>, <code>ra</code></p>
<dd> Registers repositories.</p>
<dt><code>rep-remove</code>, <code>rr</code></p>
<dd> Unregisters repositories.</p>
<dt><code>rep-update</code>, <code>ru</code></p>
<dd> Updates the lists of available addins.</p>
<dt><code>rep-list</code>, <code>rl</code></p>
<dd> Lists registered repositories.</dl>
<h3>Add-in Registry Commands:</h3>
<dl>
<dt><code>reg-update</code>, <code>rgu</code></p>
<dd> Updates the add-in registry.</p>
<dt><code>reg-build</code>, <code>rgb</code></p>
<dd> Rebuilds the add-in registry.</p>
<dt><code>info</code></p>
<dd> Prints information about an add-in.</dl>
<h3>Packaging Commands:</h3>
<dl>
<dt><code>rep-build</code>, <code>rb</code></p>
<dd> Creates a repository index file for a directory structure.</p>
<dt><code>pack</code>, <code>p</code></p>
<dd> Creates a package from an add-in configuration file.</p>
<dt><code>help</code>, <code>h</code></p>
<dd> Shows help about a command.</dl>
<h3>Debug Commands:</h3>
<dl>
<dt><code>dump-file</code></p>
<dd> Prints the contents of a registry file.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a></code>(1). </p>
<h2>Index</h2>
