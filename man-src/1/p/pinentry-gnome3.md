---
title: "pinentry-gnome3(1)"
name: "pinentry-gnome3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pinentry-gnome3/"
description: "pinentry-gnome3 – PIN or pass-phrase entry dialog for GnuPG"
---

<h2 class="name">NAME</h2>
<p> pinentry-gnome3 &#8211; PIN or pass-phrase entry dialog for GnuPG</p>
<h2>SYNOPSIS</h2>
<p> <code>pinentry-gnome3 [</code><i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pinentry-gnome3</code> is a program that allows for secure entry of PINs or pass phrases. That means it tries to take care that the entered information is not swapped to disk or temporarily stored anywhere. This functionality is particularly useful for entering pass phrases when using encryption software such as GnuPG or e-mail clients using the same. It uses an open protocol and is therefore not tied to particular software. </p>
<p> <code>pinentry-gnome3</code> implements a PIN entry dialog based on GNOME 3, which aims to follow the GNOME Human Interface Guidelines as closely as possible. If the X Window System is not active then an alternative text-mode dialog will be used. There are other flavors that implement PIN entry dialogs using other tool kits. </p>
<p> <code>pinentry-gnome3</code> is typically used internally by <code>gpg-agent</code>. Users don&#8217;t normally have a reason to call it directly.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the program version and licensing information.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a usage message summarizing the most useful command-line options.</p>
<dt><code>&#8211;debug</code>, <code>-d</code></p>
<dd> Turn on some debugging. Mostly useful for the maintainers. Note that this may reveal sensitive information like the entered pass phrase.</p>
<dt><code>&#8211;enhanced</code>, <code>-e</code></p>
<dd> Ask for timeouts and insurance, too. Note that this is currently not fully supported.</p>
<dt><code>&#8211;no-global-grab</code>, <code>-g</code></p>
<dd> Grab the keyboard only when the window is focused. Use this option if you are debugging software using <code>pinentry-gnome3</code>; otherwise you may not be able to to access your X session anymore (unless you have other means to connect to the machine to kill <code>pinentry-gnome3</code>).</p>
<dt><code>&#8211;parent-wid</code> <i>N</i></p>
<dd> Use window ID <i>N</i> as the parent window for positioning the window. Note, that this is not fully supported by all flavors of <code>pinentry</code>.</p>
<dt><code>&#8211;display</code> <i>STRING</i>, <code>&#8211;ttyname</code> <i>STRING</i>, <code>&#8211;ttytype</code> <i>STRING</i>, <code>&#8211;lc-type</code> <i>STRING</i>, <code>&#8211;lc-messages</code> <i>STRING</i></p>
<dd> These options are used to pass localization information to <code>pinentry-gnome3</code>. They are required because <code>pinentry-gnome3</code> is usually called by some background process which does not have any information on the locale and terminal to use. Assuan protocol options are an alternative way to pass these information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pinentry-curses/">pinentry-curses</a></code>(1), <code><a href="/docs/linux/man/1-pinentry-gtk-2/">pinentry-gtk-2</a></code>(1), <code><a href="/docs/linux/man/1-pinentry-fltk/">pinentry-fltk</a></code>(1), <code><a href="/docs/linux/man/1-pinentry-qt/">pinentry-qt</a></code>(1), <code><a href="/docs/linux/man/1-pinentry-tty/">pinentry-tty</a></code>(1), <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1) </p>
<p> The full documentation for <code>pinentry-gnome3</code> is maintained as a Texinfo manual. If the <code>pinentry-doc</code> package is installed, the command</p>
<dl>
<dt>
<dd> <code>info pinentry</code></dl>
<p> should give you access to the complete manual.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Daniel Kahn Gillmor for the Debian project, adapted from other pinentry manual pages written by Peter Eisentraut. </p>
<h2>Index</h2>
