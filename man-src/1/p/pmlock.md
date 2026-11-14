---
title: "pmlock(1)"
name: "pmlock"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlock/"
description: "pmlock – simple file-based mutex"
---

<h2>NAME</h2>
<p> <code>pmlock</code> &#8211; simple file-based mutex</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmlock</code> [ <code>-v</code> ] <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmlock</code> attempts to acquire an exclusive lock by creating <i>file</i> with a mode of 0. </p>
<p> The exit status is 0 for success, 1 for failure. </p>
<p> To release the lock, unlink <i>file</i>. </p>
<p> In the event of a failure, the <code>-v</code> option produces an explanatory message on <i>stdout</i>. </p>
<h2>Index</h2>
