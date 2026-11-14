---
title: "ras-mc-ctl(8)"
name: "ras-mc-ctl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-ras-mc-ctl/"
description: "ras-mc-ctl – RAS memory controller admin utility"
---

<p>ras-mc-ctl &#8211; RAS memory controller admin utility</p>
<h2>Synopsis</h2>
<p><code>ras-mc-ctl</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p>The <code>ras-mc-ctl</code> program is a <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) script which performs some useful RAS administration tasks on EDAC (Error Detection and Correction) drivers. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Display a brief usage message.</p>
<dt><code>&#8211;mainboard</code></p>
<dd>Print mainboard vendor and model for this hardware, if available. The method used by <code>ras-mc-ctl</code> to obtain the mainboard vendor and model information for the current system is described below in the <i>MAINBOARD CONFIGURATION</i> section.</p>
<dt><code>&#8211;status</code></p>
<dd>Print the status of EDAC drivers (loaded or unloaded).</p>
<dt><code>&#8211;quiet</code></p>
<dd>Be less verbose when executing an operation.</p>
<dt><code>&#8211;register-labels</code></p>
<dd>Register motherboard DIMM labels into EDAC driver sysfs files. This option uses the detected mainboard manufacturer and model number in combination with a &quot;labels database&quot; found in any of the files under /etc/ras/dimm_labels.d/* or in the labels.db file at /etc/ras/dimm_labels.db. An entry for the current hardware must exist in the labels database for this option to do anything.</p>
<dt><code>&#8211;print-labels</code></p>
<dd>Display the configured labels for the current hardware, as well as the current labels registered with EDAC.</p>
<dt><code>&#8211;guess-labels</code></p>
<dd>Print DMI labels, when bank locator is available in the DMI table. It helps to fill the labels database at /etc/ras/dimm_labels.d/.</p>
<dt><code>&#8211;labeldb=DB</code></p>
<dd>Specify an alternate location for the labels database.</p>
<dt><code>&#8211;delay=time</code></p>
<dd>Specify a delay of <code>time</code> seconds before registering DIMM labels. Only meaninful if used together with &#8211;register-labels.</p>
<dt><code>&#8211;layout</code></p>
<dd>Prints the memory layout as detected by the EDAC driver. Useful to check if the EDAC driver is properly detecting the memory controller architecture. </p>
</dl>
<h2>Mainboard Configuration</h2>
<p>The <code>ras-mc-ctl</code> script uses the following method to determine the current system&#8217;s mainboard vendor and model information: </p>
<dl>
<dt>1.</p>
<dd>If the config file /etc/edac/mainboard exists, then it is parsed by <code>ras-mc-ctl</code>. The mainboard config file has the following simple syntax: </p>
<pre> vendor = &lt;mainboard vendor string&gt;
 model = &lt;mainboard model string&gt;
 script = &lt;script to gather mainboard information&gt;</pre>
<p>Where anything after a &#8216;#&#8217; character on a line is considered a comment. If the keyword <code>script</code> is specified, then that script or executable is run by <code>ras-mc-ctl</code> to gather the mainboard vendor and model information. The script should write the resulting information on stdout in the same format as the mainboard config file. </p>
<dt>2.</p>
<dd>If no mainboard config file exists, then <code>ras-mc-ctl</code> will attempt to read DMI information from the sysfs files </p>
<pre> /sys/class/dmi/id/board_vendor
 /sys/class/dmi/id/board_name</pre>
<dt>3.</p>
<dd>If the sysfs files above do not exist, then <code>ras-mc-ctl</code> will fall back to parsing output of the <code><a href="/docs/linux/man/8-dmidecode/">dmidecode</a></code>(8) utility. Use of this utility will most often require that <code>ras-mc-ctl</code> be run as root. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rasdaemon/">rasdaemon</a></code>(1) </p>
