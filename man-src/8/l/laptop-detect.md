---
title: "laptop-detect(8)"
name: "laptop-detect"
section: "8"
letter: "l"
url: "/docs/linux/man/8-laptop-detect/"
description: "laptop-detect – attempt to detect a laptop"
---

<p>laptop-detect &#8211; attempt to detect a laptop</p>
<h2>Synopsis</h2>
<p>laptop-detect [<i>-h</i>|<i>&#8211;help</i>|<i>-v</i>|<i>&#8211;verbose</i>|<i>-V</i>|<i>&#8211;version</i>]</p>
<h2>Description</h2>
<p>Laptop-detect attempts to determine whether it is being run on a laptop or a desktop and appraises its caller of this.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd>Output help information and exit.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd>be verbose (messages go to STDOUT)</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd>Output version information and exit.</dl>
<h2>Exit Status</h2>
<pre><code>0</code> most likely running on a laptop
<code>1</code> most likely NOT running on a laptop
<code>2</code> usage error (arguments supplied)</pre>
<h2>Files</h2>
<p><i>/proc/acpi/battery</i><br />
 <i>/proc/pmu/info</i></p>
<h2>Authors</h2>
<p>Franklin PIAT &lt;fpiat [at] bigfoot.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dmidecode/">dmidecode</a>(8) </p>
