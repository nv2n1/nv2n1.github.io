---
title: "pcp-dmcache(1)"
name: "pcp-dmcache"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-dmcache/"
description: "pcp-dmcache, pcp-lvmcache – report on logical storage device caches"
---

<h2>NAME</h2>
<p> <code>pcp-dmcache</code>, <code>pcp-lvmcache</code> &#8211; report on logical storage device caches</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp</code> [<i>pcp options</i>] <code>dmcache</code> [<code>-i</code>/<code>&#8211;iops</code>] [<code>-R</code>/<code>&#8211;repeat</code> <i>N</i>] [<i>device</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-dmcache</code> reports on the activity of any configured Device Mapper Cache targets. The reported information includes device IOPs, cache and metadata device utilization, as well as hit and miss rates and ratios for both reads and writes for each cache device. </p>
<p> <code>pcp-lvmcache</code> (Logical Volume Manager cache) is an exact synonym for <code>pcp-dmcache</code> (Device Mapper cache). </p>
<p> When invoked via the <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) command, the <code>-h</code>/<code>&#8211;host</code>, <code>-a</code>/<code>&#8211;archive</code>, <code>-O</code>/<code>&#8211;origin</code>, <code>-s</code>/<code>&#8211;samples</code>, <code>-t</code>/<code>&#8211;interval</code>, <code>-Z</code>/<code>&#8211;timezone</code> and several other <i>pcp options</i> become indirectly available. </p>
<p> By default, <code>pcp-dmcache</code> reports on all available cache target devices (one line each, per sample), but this can be restricted to specific devices on the command line.</p>
<h2>OPTIONS</h2>
<p> Additional options are available for changing the output displayed by <code>pcp-dmcache</code>. </p>
<p> <code>-i</code>/<code>&#8211;iops</code> displays total read and write operations instead of the default cache hit ratio. </p>
<p> <code>-R</code>/<code>&#8211;repeat</code> changes the frequency at which the column heading is displayed. By default, a header is displayed after every tenth sample.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-pmdadm/">pmdadm</a></code>(1), <code><a href="/docs/linux/man/1-dmsetup/">dmsetup</a></code>(1), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) and <code><a href="/docs/linux/man/7-lvmcache/">lvmcache</a></code>(7). </p>
<h2>Index</h2>
