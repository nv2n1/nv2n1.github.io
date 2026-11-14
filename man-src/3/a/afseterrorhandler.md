---
title: "afseterrorhandler(3)"
name: "afseterrorhandler"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afseterrorhandler/"
---

afSetErrorHandler - install a custom error handling routine 

<h2>Synopsis</h2><pre>#include &lt;audiofile.h&gt;</pre><pre>AFerrfunc afSetErrorHandler (AFerrfunc errorFunction);</pre><h2>Parameters</h2><i>errorFunction</i> is a pointer to an error handling function.
<h2>Description</h2>afSetErrorHandler allows the user to install an error handling function overriding the default function.
<h2>Return Value</h2>The value returned from afSetErrorHandler is a pointer to the previous error handling function.
<h2>Author</h2>Michael Pruett &lt;michael [at] 68k.org&gt;
