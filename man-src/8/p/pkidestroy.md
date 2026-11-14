---
title: "pkidestroy(8)"
name: "pkidestroy"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkidestroy/"
description: "pkidestroy – Removes a subsystem from an instance of Certificate Server."
---

<p>pkidestroy &#8211; Removes a subsystem from an instance of Certificate Server.</p>
<h2>Synopsis</h2>
<p>pkidestroy -s &lt;subsystem&gt; -i &lt;instance&gt; [-u &lt;secutiry domain username&gt;] [-W &lt;security domain password file&gt;] [-h] [-v] [-p &lt;prefix&gt;] </p>
<h2>Description</h2>
<p>Removes a subsystem from an instance of Certificate Server. This utility removes any of the Java-based Certificate Server subsystems (CA, KRA, OCSP, and TKS). An instance can contain multiple subsystems, although it may contain at most one of each type of subsystem. So, for example, an instance could contain CA and KRA subsystems, but not two CA subsystems. If <code>pkidestroy</code> is invoked on the last subsystem in the instance, then that instance is removed. Typically, as subsystems need to contact the CA to update the security domain, the CA instance should be the last instance to be removed. </p>
<h2>Options</h2>
<dl>
<dt><code>-s &lt;subsystem&gt;</code></p>
<dd>Specifies the subsystem to be removed, where &lt;subsystem&gt; is CA, KRA, OCSP, or TKS. If this option is not specified, <code>pkidestroy</code> will prompt for its value.</p>
<dt><code>-i &lt;instance&gt;</code></p>
<dd>Specifies the name of the instance from which the subsystem should be removed. The instance is located at /var/log/pki/&lt;instance&gt;. If this option is not specified, <code>pkidestroy</code> will prompt for its value.</p>
<dt><code>-u &lt;security domain username&gt; </code></p>
<dd>Specifies the username of the security domain of the subsystem. This is an <code>optional</code> parameter.</p>
<dt><code>-W &lt;security domain password file&gt; </code></p>
<dd>Specifies the file containing the password of the security domain of the subsystem. This is an <code>optional</code> parameter.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Prints additional help information.</p>
<dt><code>-v</code></p>
<dd>Displays verbose information about the installation. This flag can be provided multiple times to increase verbosity. See <code>pkidestroy -h </code> for details. </p>
</dl>
<h2>Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a> </p>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;. <code>pkidestroy</code> was written by the Certificate Server project.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2012 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pkispawn/">pkispawn</a>(8)</code> </p>
