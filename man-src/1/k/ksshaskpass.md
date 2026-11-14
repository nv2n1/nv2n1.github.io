---
title: "ksshaskpass(1)"
name: "ksshaskpass"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksshaskpass/"
description: "ksshaskpass – prompts a user for a passphrase using KDE"
---

<h2>NAME</h2>
<p> ksshaskpass &#8211; prompts a user for a passphrase using KDE</p>
<h2>SYNOPSIS</h2>
<p> <code>kdesshaskpass</code></p>
<h2>DESCRIPTION</h2>
<p> <code>kshaskpass</code> is a KDE-based passphrase dialog for use with OpenSSH. It is intended to be called by the <code><a href="/docs/linux/man/1-ssh-add/">ssh-add</a></code>(1) program and not invoked directly. It allows <code><a href="/docs/linux/man/1-ssh-add/">ssh-add</a></code>(1) to obtain a passphrase from a user, even if not connected to a terminal (assuming that an X display is available). This happens automatically in the case where <code>ssh-add</code> is invoked from one&#8217;s <code>~/.xsession</code> or as one of the KDE startup programs, for example. </p>
<p> In order to be called automatically by <code>ssh-add</code>, <code>ksshaskpass</code> should be installed as <i>/usr/bin/ssh-askpass</i>.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Armin Berres &lt;trigger [at] space-based.de&gt;. It was based on that for gnome-ssh-askpass by Colin Watson &lt;cjwatson [at] debian.org&gt;. </p>
<h2>Index</h2>
