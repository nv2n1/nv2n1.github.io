---
title: "edac-ctl(8)"
name: "edac-ctl"
section: "8"
letter: "e"
url: "/docs/linux/man/8-edac-ctl/"
description: "edac-ctl – EDAC admin utility"
---

<p>edac-ctl &#8211; EDAC admin utility</p>
<h2>Synopsis</h2>
<p><code>edac-ctl </code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>The <code>edac-ctl</code> program is a <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) script which performs some useful administration tasks for EDAC (Error Detection and Correction) drivers. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Display a brief usage message.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Quiet operation.</p>
<dt><code>&#8211;mainboard</code></p>
<dd>Print mainboard vendor and model for this hardware, if available. This option requires that the <code><a href="/docs/linux/man/8-dmidecode/">dmidecode</a></code>(8) utility be installed, and must be run as root.</p>
<dt><code>&#8211;status</code></p>
<dd>Print the status of EDAC drivers (loaded or unloaded).</p>
<dt><code>&#8211;register-labels</code></p>
<dd>Register motherboard DIMM labels into EDAC driver sysfs files. This option uses the detected mainboard manufacturer and model number in combination with a &quot;labels database&quot; found in any of the files under /etc/edac/labels.d/* or in the labels.db file at /etc/edac/labels.db. An entry for the current hardware must exist in the labels database for this option to do anything.</p>
<dt><code>&#8211;print-labels</code></p>
<dd>Display the configured labels for the current hardware, as well as the current labels registered with EDAC.</p>
<dt><code>&#8211;delay=N</code></p>
<dd>Delay N seconds before writing DIMM labels.</p>
<dt><code>&#8211;labeldb=DB</code></p>
<dd>Specify an alternate location for the labels database. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-edac/">edac</a></code>(3), <code><a href="/docs/linux/man/1-edac-util/">edac-util</a></code>(1) </p>
