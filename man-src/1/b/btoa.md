---
title: "btoa(1)"
name: "btoa"
section: "1"
letter: "b"
url: "/docs/linux/man/1-btoa/"
description: "BtoA – Convert binary base-64 encoded data to ASCII base-64 encoded data."
---

<p>BtoA &#8211; Convert binary base-64 encoded data to ASCII base-64 encoded data.</p>
<h2>Synopsis</h2>
<p><code>BtoA &lt;input_file&gt; &lt;output_file&gt;</code> </p>
<h2>Description</h2>
<p>The <code>BtoA</code> command provides a command-line utility used to convert binary base-64 encoded data to ASCII base-64 encoded data. </p>
<h2>Options</h2>
<p>The following parameters are mandatory:</p>
<dl>
<dt><code>&lt;input_file&gt;</code></p>
<dd>Specifies the path to the file which contains the base-64 encoded binary data. </p>
<dt><code>&lt;output_file&gt;</code></p>
<dd>Specifies the path to the file where the utility should write the ASCII output. </p>
</dl>
<h2>Examples</h2>
<p>This example command takes the base-64 binary data in the <code>binary_data.der</code> file and writes the ASCII equivalent of the data to the <code>ascii_data.pem</code> file:</p>
<dl>
<dd>
<pre> BtoA binary_data.der ascii_data.pem </p>
<h2>Copyright</h2>
<p>Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-atob/">AtoB</a>(1),</code><a href="/docs/linux/man/1-pki/">pki</a>(1)</p>
