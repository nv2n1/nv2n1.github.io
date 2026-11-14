---
title: "gnome-ssh-askpass(1)"
name: "gnome-ssh-askpass"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-ssh-askpass/"
description: "gnome-ssh-askpass – prompts a user for a passphrase using GNOME"
---

<h2 class="name">NAME</h2>
<p> gnome-ssh-askpass &#8211; prompts a user for a passphrase using GNOME </p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-ssh-askpass</code></p>
<h2>DESCRIPTION</h2>
<p> <code>gnome-ssh-askpass</code> is a GNOME-based passphrase dialog for use with OpenSSH. It is intended to be called by the <code><a href="/docs/linux/man/1-ssh-add/">ssh-add</a></code>(1) program and not invoked directly. It allows <code><a href="/docs/linux/man/1-ssh-add/">ssh-add</a></code>(1) to obtain a passphrase from a user, even if not connected to a terminal (assuming that an X display is available). This happens automatically in the case where <code>ssh-add</code> is invoked from one&#8217;s <code>~/.xsession</code> or as one of the GNOME startup programs, for example. </p>
<p> In order to be called automatically by <code>ssh-add</code>, <code>gnome-ssh-askpass</code> should be installed as <i>/usr/bin/ssh-askpass</i>.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables are recognized:</p>
<dl>
<dt><i>GNOME_SSH_ASKPASS_GRAB_SERVER</i></p>
<dd> Causes <code>gnome-ssh-askpass</code> to grab the X server before asking for a passphrase.</p>
<dt><i>GNOME_SSH_ASKPASS_GRAB_POINTER</i></p>
<dd> Causes <code>gnome-ssh-askpass</code> to grab the mouse pointer using <i>gdk_pointer_grab</i>() before asking for a passphrase.</dl>
<p> Regardless of whether either of these environment variables is set, <code>gnome-ssh-askpass</code> will grab the keyboard using <i>gdk_keyboard_grab</i>().</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Colin Watson &lt;cjwatson [at] debian.org&gt; for the Debian system (but may be used by others). It was based on that for <code>x11-ssh-askpass</code> by Philip Hands. </p>
<h2>Index</h2>
