---
title: "setprogname(3)"
name: "setprogname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setprogname/"
description: "getprogname setprogname – get or set the program name"
---

<p><code>getprogname</code> <code>setprogname</code> &#8211; get or set the program name</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/stdlib.h Ft const char * Fn getprogname void Ft void Fn setprogname const char *progname</p>
<h2>Description</h2>
<p>The Fn getprogname and Fn setprogname functions manipulate the name of the current program. They are used by error-reporting routines to produce consistent output. </p>
<p> The Fn getprogname function returns the name of the program. If the name has not been set yet, it will return <code>NULL</code> </p>
<p> The Fn setprogname function sets the name of the program to be the last component of the Fa progname argument. Since a pointer to the given string is kept as the program name, it should not be modified for the rest of the program&#8217;s lifetime. </p>
<p> In Fx , the name of the program is set by the start-up code that is run before Fn main ; thus, running Fn setprogname is not necessary. Programs that desire maximum portability should still call it; on another operating system, these functions may be implemented in a portability library. Calling Fn setprogname allows the aforementioned library to learn the program name without modifications to the start-up code.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-err/">err</a>(3), <a href="/docs/linux/man/3-setproctitle/">setproctitle</a>(3)</p>
<h2>History</h2>
<p>These functions first appeared in Nx 1.6 , and made their way into Fx 4.4 .</p>
