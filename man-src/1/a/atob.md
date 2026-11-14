---
title: "atob(1)"
name: "atob"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atob/"
description: "AtoB – Convert ASCII base-64 encoded data to binary base-64 encoded data."
---

<p>AtoB &#8211; Convert ASCII base-64 encoded data to binary base-64 encoded data.</p>
<h2>Synopsis</h2>
<p><code>AtoB &lt;input_file&gt; &lt;output_file&gt;</code> </p>
<h2>Description</h2>
<p>The <code>AtoB</code> command provides a command-line utility used to convert ASCII base-64 encoded data to binary base-64 encoded data. </p>
<h2>Options</h2>
<p>The following parameters are mandatory:</p>
<dl>
<dt><code>&lt;input_file&gt;</code></p>
<dd>Specifies the path to the file containing the base-64 encoded ASCII data. </p>
<dt><code>&lt;output_file&gt;</code></p>
<dd>Specifies the path to the file where the utility should write the binary output. </p>
</dl>
<h2>Examples</h2>
<p>This example command takes the base-64 ASCII data in the <code>ascii_data.pem</code> file and writes the binary equivalent of the data to the <code>binary_data.der</code> file:</p>
<dl>
<dd>
<pre> AtoB ascii_data.pem binary_data.der </p>
<h2>Copyright</h2>
<p>Copyright (c) 2016 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-btoa/">BtoA</a>(1),</code><a href="/docs/linux/man/1-pki/">pki</a>(1)</p>
