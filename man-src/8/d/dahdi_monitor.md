---
title: "dahdi_monitor(8)"
name: "dahdi_monitor"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dahdi_monitor/"
description: "dahdi_monitor – checks the rx/tx levels of DAHDI channels"
---

<p>dahdi_monitor &#8211; checks the rx/tx levels of DAHDI channels</p>
<h2>Synopsis</h2>
<p><code>dahdi_monitor </code><i>channel number</i><code> [-v] [-f </code><i>FILE</i><code>]</code> </p>
<h2>Description</h2>
<p>dahdi_monitor monitors a DAHDI channel. It gives you a visual representation of the sound strengths and makes it easy to see if the received or transmitted signals are too high or out of balance </p>
<h2>Options</h2>
<p>The first (mandatory) parameter is the number of the channel to monitor. </p>
<p> <code>-v</code></p>
<dl>
<dd>Display visual audio levels.</dl>
<p> <code>-f </code><i>FILE</i></p>
<dl>
<dd>Write output to FILE</dl>
<p> Some extra, yet undocumented, options.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dahdi_tool/">dahdi_tool</a>(8), <a href="/docs/linux/man/8-dahdi_cfg/">dahdi_cfg</a>(8), <a href="/docs/linux/man/8-asterisk/">asterisk</a>(8). </p>
<h2>Author</h2>
<p>This manual page was written by Santiago Ruano Rinc[&#8216;o]n &lt;santiago [at] unicauca.edu.co&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation.</p>
