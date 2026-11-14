---
title: "cups-exec(8)"
name: "cups-exec"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cups-exec/"
description: "cupsd-helper – cupsd helper programs (deprecated)"
---

<p>cupsd-helper &#8211; cupsd helper programs (deprecated)</p>
<h2>Synopsis</h2>
<p><code>cups-deviced</code> <i>request-id</i> <i>limit</i> <i>user-id</i> <i>options</i><br />
 <code>cups-driverd</code> <code>cat</code> <i>ppd-name</i><br />
 <code>cups-driverd</code> <code>list</code> <i>request_id</i> <i>limit</i> <i>options</i><br />
 <code>cups-exec</code> <i>sandbox-profile</i> [ <i>-g</i> <i>group-id</i> ] [ <i>-n</i> <i>nice-value</i> ] [ <i>-u</i> <i>user-id</i> ] <i>/path/to/program</i> <i>argv0</i> <i>&#8230;</i> <i>argvN</i></p>
<h2>Description</h2>
<p>The <code>cupsd-helper</code> programs perform long-running operations on behalf of the scheduler, <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8). The <code>cups-deviced</code> helper program runs each CUPS <code><a href="/docs/linux/man/7-backend/">backend</a></code>(7) with no arguments in order to discover the available printers. </p>
<p> The <code>cups-driverd</code> helper program lists all available printer drivers, a subset of &quot;matching&quot; printer drivers, or a copy of a specific driver PPD file. </p>
<p> The <code>cups-exec</code> helper program runs backends, filters, and other programs. On macOS these programs are run in a secure sandbox.</p>
<h2>Files</h2>
<p>The <code>cups-driverd</code> program looks for PPD and driver information files in the following directories: </p>
<pre> <i>/Library/Printers</i>
 <i>/opt/share/ppd</i>
 <i>/System/Library/Printers</i>
 <i>/usr/local/share/ppd</i>
 <i>/usr/share/cups/drv</i>
 <i>/usr/share/cups/model</i>
 <i>/usr/share/ppd</i></pre>
<p>PPD files can be compressed using the <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) program or placed in compressed <code><a href="/docs/linux/man/1-tar/">tar</a></code>(1) archives to further reduce their size. </p>
<p> Driver information files must conform to the format defined in <code><a href="/docs/linux/man/5-ppdcfile/">ppdcfile</a></code>(5).</p>
<h2>Notes</h2>
<p>CUPS printer drivers, backends, and PPD files are deprecated and will no longer be supported in a future feature release of CUPS. Printers that do not support IPP can be supported using applications such as <code><a href="/docs/linux/man/1-ippeveprinter/">ippeveprinter</a></code>(1).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-backend/">backend</a></code>(7), <code><a href="/docs/linux/man/1-cups/">cups</a></code>(1), <code><a href="/docs/linux/man/8-cupsd/">cupsd</a></code>(8), <code><a href="/docs/linux/man/5-cupsd-conf/">cupsd.conf</a></code>(5), <code><a href="/docs/linux/man/7-filter/">filter</a></code>(7), <code><a href="/docs/linux/man/5-ppdcfile/">ppdcfile</a></code>(5), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2021-2022 by OpenPrinting.</p>
