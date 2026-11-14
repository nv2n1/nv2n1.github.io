---
title: "dlm_stonith(8)"
name: "dlm_stonith"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dlm_stonith/"
description: "dlm_stonith – a proxy for fencing via stonith/pacemaker"
---

<p>dlm_stonith &#8211; a proxy for fencing via stonith/pacemaker</p>
<h2>Synopsis</h2>
<p><code>dlm_stonith</code> </p>
<h2>Description</h2>
<p>dlm_controld can use dlm_stonith as a proxy fence agent when the stonith/pacemaker system performs actual fencing. dlm_stonith is run by dlm_controld, and is not meant to be run manually. dlm_controld provides the options on stdin as key=val; command line options are for testing. If fencing was successful, this program has a zero exit code. If fencing failed, this program has a non-zero exit code. </p>
<h2>Options</h2>
<p><code>-n</code><i> nodeid</i> </p>
<p> The nodeid of the target node. (stdin key is &quot;node&quot;) </p>
<p> <code>-t</code><i> fail_time</i> </p>
<p> The <a href="/docs/linux/man/2-time/">time</a>(2) at which the target node failed. If this option is provided, and the last fencing time is later, then a new fencing request is not made.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dlm_controld/">dlm_controld</a></code>(8), <code><a href="/docs/linux/man/5-dlm-conf/">dlm.conf</a></code>(5) </p>
