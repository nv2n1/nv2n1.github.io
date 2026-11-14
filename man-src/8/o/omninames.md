---
title: "omninames(8)"
name: "omninames"
section: "8"
letter: "o"
url: "/docs/linux/man/8-omninames/"
description: "omniNames – omniORB Naming Service"
---

<p>omniNames &#8211; omniORB Naming Service</p>
<h2>Synopsis</h2>
<p><code>omniNames</code> [-start &lt;port&gt;] </p>
<h2>Description</h2>
<p>omniNames is omniORB&#8217;s implementation of the OMG&#8217;s COS Naming Service Specification. When started for the first time, omniNames needs to be told which port it should listen on. This is specified with the -start option. Subsequently, omniNames will always determine its port from the log file which it writes. When omniNames starts up successfully it writes the stringified object reference for its root context on standard error. </p>
<h2>Environment Variables</h2>
<dl>
<dt><code>OMNINAMES_LOGDIR</code></p>
<dd>the directory in which log files are kept.</p>
<dt><code>OMNINAMES_ITBC</code></p>
<dd>the idle time between checkpoints in seconds. It defaults to 15 minutes. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-nameclt/">nameclt</a>(1) </p>
<h2>Author</h2>
<p>Tristan Richardson, ORL (Olivetti &amp; Oracle Research Laboratory)</p>
