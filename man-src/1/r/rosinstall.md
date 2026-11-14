---
title: "rosinstall(1)"
name: "rosinstall"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rosinstall/"
description: "rosinstall – rosinstall command"
---

<h2>NAME</h2>
<p> rosinstall &#8211; rosinstall command</p>
<h2>SYNOPSIS</h2>
<p> <code>rosinstall</code> [<i>options</i>] &lt;<i>install-path</i>&gt; [<i>rosinstall files or directories</i>]&#8230;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show this help message and exit</p>
<dt><code>-n, &#8211;nobuild</code></p>
<dd> Skip the build step for the ROS stack</p>
<dt><code>&#8211;rosdep-yes</code></p>
<dd> Pass through &#8211;rosdep-yes to rosmake</p>
<dt><code>&#8211;continue-on-error</code></p>
<dd> Continue despite checkout errors </p>
<p> <code>&#8211;delete-changed-uris</code> Delete the local copy of a directory before changing URI. </p>
<p> <code>&#8211;abort-changed-uris</code> Abort if changed uri detected </p>
<p> <code>&#8211;backup-changed-uris=BACKUP_CHANGED</code> Backup the local copy of a directory before changing URI to this directory. </p>
<p> <code>&#8211;generate-versioned-rosinstall=GENERATE_VERSIONED</code> Generate a versioned rosinstall file</dl>
<h2>DESCRIPTION</h2>
<p> The <code>rosinstall</code> command can download source code trees from a variety of source control systems (e.g. Git, Mercurial, Bazaar, Subversion). The rosinstall file format lets you specify multiple source code trees, which simplifies the process of creating development workspaces. </p>
<p> rosinstall does the following:</p>
<dl>
<dt>1.</p>
<dd> Merges all URIs into new or existing .rosinstall file at PATH</p>
<dt>2.</p>
<dd> Checks out or updates all version controlled URIs</p>
<dt>3.</p>
<dd> Calls rosmake after checkout or updates</p>
<dt>4.</p>
<dd> Generates/overwrites updated setup files </p>
<p> Run &quot;rosinstall -h&quot; to access the built-in tool documentation. </p>
<p> See <i><a rel="nofollow" href="http://www.ros.org/wiki/rosinstall">http://www.ros.org/wiki/rosinstall</a></i> for more details</dl>
<h2>AUTHOR</h2>
<p> Tully Foote, Thibault Kruse, Morgan Quigley, Ken Conley, Brian Gerkey</p>
<h2>COPYRIGHT</h2>
<p> 2011, Willow Garage </p>
<h2>Index</h2>
