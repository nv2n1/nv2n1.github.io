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
<dt><code>&#8211;registry</code>, <code>-reg</code></dt>
<dd> Specify add-in registry path</dd>
<dt><code>&#8211;path</code>, <code>-p</code></dt>
<dd> Specify startup path</dd>
<dt><code>-v</code></dt>
<dd> Verbose output</dd></dl>
<h3>Add-in commands:</h3>
<dl>
<dt><code>install</code>, <code>i</code></dt>
<dd> Installs add-ins.</dd>
<dt><code>uninstall</code>, <code>u</code></dt>
<dd> Uninstalls add-ins.</dd>
<dt><code>check-install</code>, <code>ci</code></dt>
<dd> Checks installed add-ins.</dd>
<dt><code>update</code>, <code>up</code></dt>
<dd> Updates installed add-ins.</dd>
<dt><code>list</code>, <code>l</code></dt>
<dd> Lists installed add-ins.</dd>
<dt><code>list-av</code>, <code>la</code></dt>
<dd> Lists add-ins available in registered repositories.</dd>
<dt><code>list-update</code>, <code>lu</code></dt>
<dd> Lists available add-in updates.</dd></dl>
<h3>Repository Commands:</h3>
<dl>
<dt><code>rep-add</code>, <code>ra</code></dt>
<dd> Registers repositories.</dd>
<dt><code>rep-remove</code>, <code>rr</code></dt>
<dd> Unregisters repositories.</dd>
<dt><code>rep-update</code>, <code>ru</code></dt>
<dd> Updates the lists of available addins.</dd>
<dt><code>rep-list</code>, <code>rl</code></dt>
<dd> Lists registered repositories.</dd></dl>
<h3>Add-in Registry Commands:</h3>
<dl>
<dt><code>reg-update</code>, <code>rgu</code></dt>
<dd> Updates the add-in registry.</dd>
<dt><code>reg-build</code>, <code>rgb</code></dt>
<dd> Rebuilds the add-in registry.</dd>
<dt><code>info</code></dt>
<dd> Prints information about an add-in.</dd></dl>
<h3>Packaging Commands:</h3>
<dl>
<dt><code>rep-build</code>, <code>rb</code></dt>
<dd> Creates a repository index file for a directory structure.</dd>
<dt><code>pack</code>, <code>p</code></dt>
<dd> Creates a package from an add-in configuration file.</dd>
<dt><code>help</code>, <code>h</code></dt>
<dd> Shows help about a command.</dd></dl>
<h3>Debug Commands:</h3>
<dl>
<dt><code>dump-file</code></dt>
<dd> Prints the contents of a registry file.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a></code>(1). </p>
