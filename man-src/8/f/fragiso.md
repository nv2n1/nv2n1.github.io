---
title: "fragiso(8)"
name: "fragiso"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fragiso/"
description: "fragiso – split rpm packages from an iso and reassemble the iso later on"
---

<p>fragiso &#8211; split rpm packages from an iso and reassemble the iso later on </p>
<h2>Synopsis</h2>
<p><code>fragiso</code> <code>make</code> <i>iso</i> <i>fiso</i><br />
 <code>fragiso</code> <code>list</code> <i>fiso</i><br />
 <code>fragiso</code> <code>fill</code> [<code>-m</code>] <i>fiso iso</i> </p>
<h2>Description</h2>
<p>fragiso can be used to convert an iso file into a fragment file, which is a list describing all of the rpms on the iso and a data chunk containing everything but the rpms. It is used by <code>drpmsync</code> when an iso needs to be transferred. The idea is that often the rpms on the iso are already available on the destination host, so it saves bandwidth to first transfer the fragmented iso, copy the locally available rpms, transfer the unavailable rpms and reassemble the iso file. <code>fragiso</code> <code>make</code> converts the iso into the fragment iso, <code>fragiso</code> <code>list</code> can be used to extract the rpm information. This information consists of the offset and length of all rpms and the lead/signature header md5sum plus the header/payload md5sum. To reassemble the iso one has to copy the rpms at the right offset into a new file and then use <code>fragiso</code> <code>fill</code> later on to provide all data not contained in the rpms. The <code>-m</code> option tells fragiso to print the resulting md5sum of the iso to stdout. It can be used for verification purposes. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-drpmsync/">drpmsync</a></code>(8) </p>
<h2>Author</h2>
<p>Michael Schroeder &lt;mls [at] suse.de&gt;</p>
