---
title: "install-mh(1)"
name: "install-mh"
section: "1"
letter: "i"
url: "/docs/linux/man/1-install-mh/"
description: "install-mh – initialize the nmh environment"
---

<h2 class="name">NAME</h2>
<p> install-mh &#8211; initialize the nmh environment </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/libexec/nmh/install-mh</code> [<code>-auto</code>] [<code>-check</code>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Install-mh</code></p>
<dd>is the <code>nmh</code> program to create the initial setup for a first-time <code>nmh</code> user. <code>Install-mh</code> lives in two places for historical reasons. </p>
<p> The <code>-auto</code> option does things as automatically as possible and makes <code>install-mh</code> less chatty. </p>
<p> The user is asked for the name of the directory that will be designated as the user&#8217;s <code>nmh</code> directory. If this directory does not exist, the user is asked if it should be created. Normally, this directory should be under the user&#8217;s home directory, and has the default name of <i>&#8220;Mail&#8221;</i>. <code>Install-mh</code> writes an initial <i>.mh_profile</i> for the user. </p>
<p> As with all <code>nmh</code> commands, <code>install-mh</code> first checks for the existence of the <code>$MH</code> environment variable since that gives the profile path if set. If it isn&#8217;t set, the <code>$HOME</code> environment variable is consulted to determine the user&#8217;s home directory. If <code>$HOME</code> is not set, then the <i>/etc/passwd</i> file is consulted. </p>
<p> When creating the users initial <i>.mh_profile</i>, <code>install-mh</code> will check for the existence of a global profile <i>/etc/nmh/mh.profile</i>. If found, this will be used to initialize the new <i>.mh_profile</i>. </p>
<p> The <code>-check</code> option can be used to check whether or not nmh has been installed. This can be used by other programs to determine whether or not nmh has been installed without their having to know the internals of nmh.</p>
<h2>FILES</h2>
<dl>
<dt>$HOME/.mh_profile</p>
<dd> The user&#8217;s profile.</p>
<dt>/etc/nmh/mh.profile</p>
<dd> Used to initialize user&#8217;s profile.</dl>
<h2>PROFILE COMPONENTS</h2>
<dl>
<dt>Path:</p>
<dd> To set the user&#8217;s nmh directory.</dl>
<h2>CONTEXT</h2>
<p> With <code>-auto</code>, the current folder is changed to &#8220;<i>inbox</i>&#8221;. </p>
<h2>Index</h2>
