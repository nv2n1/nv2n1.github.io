---
title: "pcscd(8)"
name: "pcscd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pcscd/"
description: "pcscd – PC/SC Smart Card Daemon"
---

<p>pcscd &#8211; PC/SC Smart Card Daemon</p>
<h2>Synopsis</h2>
<p><code>pcscd</code> [<i>options</i>]</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;apdu</code></p>
<dd>log APDUs and SW using the debug method (see <code>&#8211;debug</code>).</p>
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></p>
<dd>Specifies the file <i>file</i> as an alternate location for <i>/etc/reader.conf.d/reader.conf</i>.</p>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd>Runs pcscd in the foreground and sends log messages to stderr instead of <a href="/docs/linux/man/3-syslog/">syslog</a>(3).</p>
<dt><code>-T</code>, <code>&#8211;color</code></p>
<dd>use colored logs.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>use the lowest log level. Any log message of this level or above will be sent to stderr or <a href="/docs/linux/man/3-syslog/">syslog</a>(3) depending on the use of <code>&#8211;foreground</code>.</p>
<dt><code>&#8211;info</code></p>
<dd>use info log level. This is the default log level.</p>
<dt><code>-e</code>, <code>&#8211;error</code></p>
<dd>use error log level.</p>
<dt><code>-C</code>, <code>&#8211;critical</code></p>
<dd>use critical log level.</dl>
<p> The log levels are ordered as: debug &lt; info &lt; error &lt; critical. Use a log level l will log this level and all the levels above it.</p>
<dl>
<dt><code>&#8211;force-reader-polling </code></p>
<dd>Ignore the IFD_GENERATE_HOTPLUG reader capability</p>
<dt><code>-t</code>, <code>&#8211;max-thread</code></p>
<dd>Set the maximum number of threads (default 200)</p>
<dt><code>-s</code>, <code>&#8211;max-card-handle-per-thread</code></p>
<dd>Set the maximum number of card handle per thread (default: 200)</p>
<dt><code>-r</code>, <code>&#8211;max-card-handle-per-reader</code></p>
<dd>Set the maximum number of card handle per reader (default: 200)</p>
<dt><code>-x</code>, <code>&#8211;auto-exit</code></p>
<dd>Cause pcscd to quit after 60 seconds of inactivity</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Displays information about the pcscd command line</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Displays the program version number</p>
<dt><code>-H</code>, <code>&#8211;hotplug</code></p>
<dd>Ask pcscd to rescan the USB buses for added or removed readers and re-read the <i>/etc/reader.conf.d/reader.conf</i> file to detect added or removed non-USB readers (serial or PCMCIA).</dl>
<h2>Description</h2>
<p>pcscd is the daemon program for pcsc-lite. It is a resource manager that coordinates communications with smart card readers and smart cards and cryptographic tokens that are connected to the system. </p>
<p> It allows applications to access smart cards and readers using the winscard API but without knowing details of the card or reader. </p>
<p> pcscd coordinates the loading of drivers for card readers.</p>
<h2>Serial Smart Card Reader Drivers</h2>
<p>Smart card reader drivers are placed in the <i>/usr/lib64/pcsc/drivers</i> directory. Each driver is simply an <i>.so</i> file. pcscd locates the driver using the <i>/etc/reader.conf.d/reader.conf</i> file. See the <code><a href="/docs/linux/man/5-reader-conf/">reader.conf</a></code>(5) manual page for more information. Drivers are available at <i><a rel="nofollow" href="http://www.musclecard.com/drivers.html">http://www.musclecard.com/drivers.html</a></i>.</p>
<h2>Usb Smart Card Reader Drivers</h2>
<p>USB smart card reader drivers are located in <i>/usr/lib64/pcsc/drivers</i> directory as a bundle. You shall not add a USB driver in <i>/etc/reader.conf.d/reader.conf</i> file.</p>
<h2>Files</h2>
<p><i>/etc/reader.conf.d/reader.conf</i> : Reader configuration file </p>
<p> <i>/var/run/pcscd/pcscd.pid</i> : process id of the running pcscd </p>
<p> <i>/usr/lib64/pcsc/drivers</i> : directory containing bundles for USB drivers</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-bundletool/">bundleTool</a></code>(8), <code><a href="/docs/linux/man/5-reader-conf/">reader.conf</a></code>(5), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)</p>
<h2>Authors</h2>
<p>David Corcoran &lt;corcoran [at] musclecard.com&gt; and Ludovic Rousseau &lt;ludovic.rousseau [at] free.fr&gt;</p>
