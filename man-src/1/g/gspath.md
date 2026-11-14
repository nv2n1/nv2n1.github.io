---
title: "gspath(1)"
name: "gspath"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gspath/"
description: "gspath – Utility to display standard directory/path information"
---

<h2>NAME</h2>
<p> gspath &#8211; Utility to display standard directory/path information</p>
<h2>SYNOPSIS</h2>
<p> <code>gspath</code> </p>
<h2>DESCRIPTION</h2>
<p> This utility can be used to print out a single directory or path in order for external applications to know what paths the GNUstep system is using. It was written to provide information for the GNUstep make package. </p>
<p> The <code>gspath</code> usility is called with exactly one argument, which determines what it prints. </p>
<h2>Arguments</h2>
<p> To display the path to the defaults directory for the current user, use the <code>defaults</code> argument. </p>
<p> To display the directory search path needed to locate dynamic libraries, use the <code>libpath</code> argument. </p>
<p> To display the directory search path needed to locate commmand-line programs, use the <code>path</code> argument. </p>
<p> To display the GNUstep home directory of the current user, use the <code>user</code> argument. </p>
<h2>HISTORY</h2>
<p> Work on <code>gspath</code> started July 2005. </p>
<p> This manual page first appeared in gnustep-base 1.11.1 (July 2005). </p>
<h2>AUTHORS</h2>
<p> <code>gspath </code> was written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt;. </p>
<p> This man page was written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt;. </p>
<h2>Index</h2>
