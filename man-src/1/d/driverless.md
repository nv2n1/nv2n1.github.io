---
title: "driverless(1)"
name: "driverless"
section: "1"
letter: "d"
url: "/docs/linux/man/1-driverless/"
description: "driverless – PPD generator utility for driverless printing"
---

<h2 class="name">NAME</h2>
<p> <code>driverless </code>&#8211; PPD generator utility for driverless printing </p>
<h2>SYNOPSIS</h2>
<pre><code>
driverless[-h | --help | --version][-d | -v | --debug][list][_ipps._tcp][_ipp._tcp][--std - ipp - uris] | [cat driver URI] | [IPP printer URI]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>driverless</code> generates PPD files for printers which are designed for driverless IPP printing (currently IPP Everywhere, AirPrint, Mopria, and Wi-Fi-Direct printers, network printers and also IPP-over-USB printers with the help of <a href="/docs/linux/man/8-ippusbxd/">ippusbxd</a>(8)) by polling capability information from the printers via IPP. it can be either called for listing suitable printers in the network and for actually generating the PPD. It can also be called by CUPS when CUPS is listing available PPDs/drivers or creating print queues, making the setup of driverless printers with printer setup tools transparently working. </p>
<p> driverless is placed in /usr/lib/cups/driver/ for listing available driverless-capable printers and generating PPDs for them. It should also be put in /usr/lib/cups/backend/ (preferably by a symbolic link) to list IPP device URIs for suitable printers. Printer setup tools like system-config-printer, the CUPS web interface at <a rel="nofollow" href="http://localhost:631/,">http://localhost:631/,</a> and CUPS&#8217; command line utilities can use driverless with CUPS to list available driverless-capable printers, determine their IPP device URIs and generate PPDs for them. The printers will be automatically and correctly set up for driverless printing. Note that driverless printing requires IPP communication with the printer. </p>
<p> A second symbolic link to /usr/lib/cups/driver/driverless from /usr/bin/ allows driverless to be called directly by a user.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code>, <code>&#8211;version</code></p>
<dd> Show help page, including version number.</p>
<dt><code>-v</code>, <code>-d</code>, <code>&#8211;debug</code></p>
<dd> Debug mode, verbose logging to stderr.</p>
<dt><code>list</code></p>
<dd> List the driver URIs and metadata for all available IPP/IPPS printers suitable for driverless PPD file generation (to be used by CUPS).</p>
<dt><code>_ipps._tcp</code></p>
<dd> Check for only IPPS printers supporting driverless printing .</p>
<dt><code>_ipp._tcp</code></p>
<dd> Check for only IPP printers supporting driverless printing .</p>
<dt><code>&#8211;std-ipp-uris</code></p>
<dd> Show URIS in standard form</p>
<dt><code>cat</code> <i>driver URI</i></p>
<dd> Generate the PPD file for the supplied <i>driver URI</i> from the output of &quot;list&quot; (to be used by CUPS).</p>
<dt><i>IPP printer URI</i></p>
<dd> Generate the PPD file for the supplied <i>IPP printer URI</i> (suitable URIs are listed when calling driverless without options).</dl>
<p> When called without options, the IPP printer URIs of all available driverless-capable IPP printers will be listed. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-cups-browsed/">cups-browsed</a></code>(8), <code><a href="/docs/linux/man/1-ippfind/">ippfind</a></code>(1), <code><a href="/docs/linux/man/8-ippusbxd/">ippusbxd</a></code>(8) </p>
<h2>AUTHOR</h2>
<p> The authors of <code>driverless</code> are listed in /usr/share/doc/<code>cups-filters</code>/AUTHORS. </p>
<h2>Index</h2>
