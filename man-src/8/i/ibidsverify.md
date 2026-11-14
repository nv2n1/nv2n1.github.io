---
title: "ibidsverify(8)"
name: "ibidsverify"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibidsverify/"
description: "IBIDSVERIFY –"
---

<p>IBIDSVERIFY &#8211;</p>
<h2>Validate Ib Identifiers In Subnet And Report Errors</h2>
<h3>Synopsis</h3>
<p>ibidsverify.pl [-h] [-R]</p>
<h3>Description</h3>
<p>ibidsverify.pl is a perl script which uses a full topology file that was created by ibnetdiscover, scans the network to validate the LIDs and GUIDs in the subnet. The validation consists of checking that there are no zero or duplicate identifiers. </p>
<p> Finally, ibidsverify.pl will also reuse the cached ibnetdiscover output from some of the other diag tools which makes it a bit faster than running ibnetdiscover from scratch.</p>
<h3>Options</h3>
<p><code>-R</code> Recalculate the ibnetdiscover information, ie do not use the cached information. This option is slower but should be used if the diag tools have not been used for some time or if there are other reasons to believe the fabric has changed. </p>
<p> <code>-C &lt;ca_name&gt;</code> use the specified ca_name. </p>
<p> <code>-P &lt;ca_port&gt;</code> use the specified ca_port.</p>
<h3>Exit Status</h3>
<p>Exit status is 1 if errors are found, 0 otherwise.</p>
<h3>Files</h3>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h3>See Also</h3>
<p><code><a href="/docs/linux/man/8-ibnetdiscover/">ibnetdiscover</a>(8)</code></p>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] voltaire.com</i> &gt; </p>
</dl>
