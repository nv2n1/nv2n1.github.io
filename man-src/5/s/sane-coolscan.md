---
title: "sane-coolscan(5)"
name: "sane-coolscan"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-coolscan/"
description: "sane-coolscan – SANE backend for Nikon film-scanners"
---

<p>sane-coolscan &#8211; SANE backend for Nikon film-scanners</p>
<h2>About This File</h2>
<p>This file is a short description of the coolscan backend for <code>SANE</code>.</p>
<h2>Description</h2>
<p>The <code>sane-coolscan</code> library implements a SANE backend that provides the interface to the following Nikon Coolscan Film scanners: Nikon LS20, LS30, LS1000, LS2000. <code>Even though the backend has worked for a number of people, there are still some</code> problems, especially in combination with some SCSI card/drivers (AHA-1505/aha152x.o) and the autofocus command. You should consider this backend &#8216;alpha&#8217; and be careful when using it the first time. </p>
<h2>Configuration</h2>
<p>The configuration file for this backend resides in <i>/etc/sane.d/coolscan.conf</i>. </p>
<p> Its content is a list of device names that correspond to Nikon Coolscan scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<pre> #scsi Vendor Model Type
 scsi Nikon * Scanner
 /dev/scanner</pre>
<p>The special device name must be a generic SCSI device or a symlink to such a device. To find out to which device your scanner is assigned and how you can set the permissions of that device, have a look at <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5).</p>
<h2>Scsi Adapter Tips</h2>
<p>Some SCSI-adapters and low-level SCSI drivers do not work correctly with this backend and the Coolscan scanners. These systems hang when the autofocus command is send to the Scanner. To see a list of which card/driver combinations work or don&#8217;t work have a look at: <i><a rel="nofollow" href="http://andreas.rick.free.fr/sane/autofocus.html.">http://andreas.rick.free.fr/sane/autofocus.html.</a></i></p>
<h2>Files</h2>
<dl>
<dt>The backend configuration file:</p>
<dd><i>/etc/sane.d/coolscan.conf</i></p>
<dt>The static library implementing this backend:</p>
<dd><i>/usr/lib/x86_64-linux-gnu/sane/libsane-coolscan.a</i></p>
<dt>The shared library implementing this backend:</p>
<dd><i>/usr/lib/x86_64-linux-gnu/sane/libsane-coolscan.so</i> (present on systems that support dynamic loading) </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_COOLSCAN</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
<p> Examples: </p>
<p> On bash:<br />
 export SANE_DEBUG_COOLSCAN=8 </p>
<p> On csh:<br />
 setenv SANE_DEBUG_COOLSCAN 8 </p>
</dl>
<h2>Bugs</h2>
<p>The autofocus command does not work with some SCSI card/driver combinations. The gamma table is not implemented for the LS1000 yet. The dust-removal is not working yet. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5)</p>
<dl>
<dt><i><a rel="nofollow" href="http://andreas.rick.free.fr/sane/">http://andreas.rick.free.fr/sane/</a></i></p>
<dd>The homepage of this backend.</p>
<dt><i><a rel="nofollow" href="http://www.sema.be/coolscan/">http://www.sema.be/coolscan/</a></i></p>
<dd>The original version of the coolscan backend by Didier. </p>
<h2>Thanks To</h2>
<p>Didier Carlier &#8211; For writing the original Coolscan backend (without it I would not have started this). </p>
<p> Oliver Rauch &#8211; For adapting xsane so quickly to the infrared stuff. </p>
<p> All the other people working on SANE.</p>
<h2>Author</h2>
<p>Andreas Rick</p>
<h2>Email-Contact</h2>
<p><i>andreas.rick [at] free.fr</i></p>
