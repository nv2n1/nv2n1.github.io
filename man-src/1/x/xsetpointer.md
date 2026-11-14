---
title: "xsetpointer(1)"
name: "xsetpointer"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsetpointer/"
description: "xsetpointer – set an X Input device as the main pointer"
---

<h2 class="name">NAME</h2>
<p> xsetpointer &#8211; set an X Input device as the main pointer </p>
<h2>SYNOPSIS</h2>
<p> <code>xsetpointer -l</code> | <i>device-name</i></p>
<h2>DESCRIPTION</h2>
<p> Xsetpointer sets an XInput device as the main pointer. When called with the -l flag it lists the available devices. When called with the -c/+c flag, it toggles the sending of core input events, for servers which implement a virtual core pointer; -c disables core events, and +c enables.</p>
<h2>AUTHOR</h2>
<p> Frederic Lepied </p>
<h2>Index</h2>
