---
title: "pmpause(1)"
name: "pmpause"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmpause/"
description: "pmpause, pmsleep – portable subsecond-capable sleep"
---

<h2>NAME</h2>
<p> <code>pmpause</code>, <code>pmsleep</code> &#8211; portable subsecond-capable sleep</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmpause</code><br />
 <code>$PCP_BINADM_DIR/pmsleep</code> <i>interval</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmpause</code> sleeps indefinitely, until interrupted by SIGKILL. </p>
<p> <code>pmsleep</code> sleeps for the specified <i>interval.</i> The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for <code>-t,</code> and in the simplest form may be an unsigned integer or floating point constant (the implied units in this case are seconds).</p>
<h2>DIAGNOSTICS</h2>
<p> The exit status is 0 for success, or 1 for a malformed command line. If the underlying <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2) system call fails, an errno is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sleep/">sleep</a></code>(1), <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2) and <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2). </p>
<h2>Index</h2>
