---
title: "znc-buildmod(1)"
name: "znc-buildmod"
section: "1"
letter: "z"
url: "/docs/linux/man/1-znc-buildmod/"
description: "znc-buildmod – compile ZNC modules"
---

<h2>NAME</h2>
<p> znc-buildmod &#8211; compile ZNC modules</p>
<h2>SYNOPSIS</h2>
<p> <code>znc-buildmod</code> FILE&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>znc-buildmod</code> compiles a ZNC module for you. You just give it a list of source files and every single file is compiled into a module.</p>
<h2>EXIT STATUS</h2>
<p> Normally, exit status is 0 if everything went fine. In case the compiler errors when compiling some module, the exit status is 1.</p>
<h2>ENVIRONMENT</h2>
<p> Variables</p>
<h3>CXXFLAGS</h3>
<h3>LDFLAGS</h3>
<h3>MODLINK</h3>
<h3>INCLUDES</h3>
<h3>LIBS</h3>
<p> may be used. </p>
<h2>Index</h2>
