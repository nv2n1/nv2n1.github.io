---

title: "alsatplg(1)"
name: "alsatplg"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsatplg/"
description: "alsatplg – ALSA Topology Compiler"
---

<p> alsatplg &#8211; ALSA Topology Compiler </p>
<h2>SYNOPSIS</h2>
<p> <i>alsatplg</i> &lt;options&gt; [command]</p>
<h2>DESCRIPTION</h2>
<p> alsatplg (ALSA Topology compiler) is a program to compile topology configuration file to the binary file for the kernel drivers. </p>
<p> Current audio drivers typically hard code topology information in the driver sources: This tightly couples the audio driver to the development board making it time consuming to modify a driver to work on a different devices. The driver is also tightly coupled to the DSP firmware version meaning extra care is needed to keep the driver and firmware version in sync. New firmware features also mean driver updates. </p>
<p> The ALSA topology project removes the need for re-writing or porting audio drivers to different devices or different firmwares: Drivers have no hard coded topology data meaning a single driver can be used on different devices by updating the topology data from the file system. Firmware updates can be pushed without having to update the drivers. The new firmware just needs to include an updated topology file describing the update.</p>
<h2>OPTIONS</h2>
<p> Available options:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> this help</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> show the utility version and versions of used libraries</dd>
<dt><code>-c</code>, <code>&#8211;compile</code> <i>FILE</i></dt>
<dd> source configuration file for the compilation</dd>
<dt><code>-d</code>, <code>&#8211;decode</code> <i>FILE</i></dt>
<dd> source binary topology file for the decode</dd>
<dt><code>-n</code>, <code>&#8211;normalize</code> <i>FILE</i></dt>
<dd> parse and save the configuration file in the normalized format</dd>
<dt><code>-u</code>, <code>&#8211;dump</code> <i>FILE</i></dt>
<dd> parse and save the configuration file in the specified format</dd>
<dt><code>-o</code>, <code>&#8211;output</code> <i>FILE</i></dt>
<dd> output file</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code> <i>LEVEL</i></dt>
<dd> set verbose level</dd>
<dt><code>-s</code>, <code>&#8211;sort</code></dt>
<dd> sort the configuration identifiers (set for normalization)</dd>
<dt><code>-x</code>, <code>&#8211;nocheck</code></dt>
<dd> save the configuration without additional integrity check</dd>
<dt><code>-z</code>, <code>&#8211;dapm-nosort</code></dt>
<dd> do not sort DAPM graph items (like in version 1.2.1-)</dd></dl>
<h2>FILES</h2>
<p> The master topology files for each supported sound card are in <code>/usr/share/alsa/topology</code>. </p>
<p> For example, the master use case file for the <i>broadwell</i> card is in <code>/usr/share/alsa/topology/broadwell/broadwell.conf</code>, this file describes the audio hardware for the driver. </p>
<p> For more details on the syntax of UCM files, see the alsa-lib source code: <i><a rel="nofollow" href="http://git.alsa-project.org/?p=alsa-lib.git;a=blob;f=src/topology/parser.c">http://git.alsa-project.org/?p=alsa-lib.git;a=blob;f=src/topology/parser.c</a></i></p>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</dt>
<dd> Topology Interface: <i><a rel="nofollow" href="http://www.alsa-project.org/alsa-doc/alsa-lib/group__topology.html">http://www.alsa-project.org/alsa-doc/alsa-lib/group__topology.html</a></i></dd></dl>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Jaroslav Kysela &lt;perex [at] perex.cz&gt;</p>
<h2>COPYRIGHT</h2>
<p> GPLv2+ </p>
