---
title: "update-manager(8)"
name: "update-manager"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-manager/"
description: "update-manager – graphical management of software packages updates"
---

<p>update-manager &#8211; graphical management of software packages updates</p>
<h2>Synopsis</h2>
<p><code>update-manager</code> [options]</p>
<h2>Description</h2>
<p>Update-manager is a frontend for the apt package management system. It allows you to perform some actions of the command line tool apt-get in a graphical environment. Update-manager is especially designed for upgrading your system, or migrating your system towards a more recent version. </p>
<h2>Options</h2>
<p>For a daily use, you may launch update-manager with no options so that your system is just upgraded. </p>
<p> For migration purposes, update-manager accepts some options: </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show a similar help message</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show version</p>
<dt><code>&#8211;data-dir=DATA_DIR</code></p>
<dd>Directory that contains the data files</p>
<dt><code>-c</code>, <code>&#8211;check-dist-upgrades</code></p>
<dd>Check if a new distribution release is available</p>
<dt><code>-d</code>, <code>&#8211;devel-release</code></p>
<dd>If using the latest supported release, upgrade to the development release</p>
<dt><code>-p</code>, <code>&#8211;proposed</code></p>
<dd>Upgrade using the latest proposed version of the release upgrader</p>
<dt><code>&#8211;no-focus-on-map</code></p>
<dd>Do not focus on map when starting </p>
</dl>
<h2>Actions Performed During An Upgrade To A New Version</h2>
<p>* eventually reinstall the package ubuntu-desktop </p>
<p> * switch to an updated sources.list entries </p>
<p> * adds the default user to new groups if needed</p>
<h2>See Also</h2>
<p><code>Synaptic</code>, <code>sources.list</code>, <code>aptitude</code> </p>
<h2>Authors</h2>
<p>update-manager was developed by Michael Vogt &lt;mvo [at] ubuntu.com&gt; with various contributors (see AUTHORS file) </p>
<p> This manual page was originally written by Bruno Mangin and Michael Vogt &lt;mvo [at] ubuntu.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2006-2007 Canonical </p>
<p> There is NO warranty. You may redistribute this software under the terms of the GNU General Public License. For more information about these matters, see the files named COPYING.</p>
