---
title: "pcp-verify(1)"
name: "pcp-verify"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-verify/"
description: "pcp-verify – verify aspects of a PCP installation"
---

<h2>NAME</h2>
<p> <code>pcp-verify</code> &#8211; verify aspects of a PCP installation</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp</code> [<i>pcp options</i>] <code>verify</code> [<code>-c</code>/<code>&#8211;containers</code>] [<code>-s</code>/<code>&#8211;secure</code>] [<code>-v</code>/<code>&#8211;verbose</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-verify</code> inspects various aspects of a PCP collector installation and reports on whether it is configured correctly for certain modes of operation. </p>
<p> By default, <code>pcp-verify</code> checks that PMCD is running and no agents are in a failed state. These checks can be extended and refined using the command line.</p>
<h2>OPTIONS</h2>
<p> Additional options are available for changing the verification performed by <code>pcp-verify</code>. </p>
<p> <code>-c</code>/<code>&#8211;containers</code> verifies the collector installation for monitoring containers. </p>
<p> <code>-s</code>/<code>&#8211;secure</code> verifies that the required components for encrypted communication are in place. </p>
<p> <code>-v</code>/<code>&#8211;verbose</code> increase the verbosity, and report on each check as it is made. In the absence of any issues found, <code>pcp-verify</code> operates silently.</p>
<h2>DIAGNOSTICS</h2>
<p> <code>pcp-verify</code> will exit with a non-zero status if it finds anything worth reporting, otherwise it is silent and returns zero.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) and <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). </p>
<h2>Index</h2>
