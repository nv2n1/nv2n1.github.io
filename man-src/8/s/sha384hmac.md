---
title: "sha384hmac(8)"
name: "sha384hmac"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sha384hmac/"
description: "sha512hmac – compute and check HMAC values"
---

<p>sha512hmac &#8211; compute and check HMAC values</p>
<h2>Synopsis</h2>
<p>sha512hmac [OPTIONS] [-u | -k keyfile | -K key] [-c file [-q] | file [&#8230;] ] </p>
<h2>Description</h2>
<p>The <i>sha512hmac</i> command can compute and/or verify HMAC and unkeyed checksum values for the contents of files. Variations such as <i>sha384hmac</i>, <i>sha256hmac</i>, and <i>sha1hmac</i> all operate similarly except that they use different digest algorithms. </p>
<h2>Self-Test</h2>
<p>As a safety measure, the tool will always attempt to verify a previously- computed HMAC over itself with the contents of a second file (<i>sha512hmac.hmac</i> for <i>sha512hmac</i>, and a similarly-named file for each variation) before processing any other files, and will exit with an error if the second file either cannot be read or does not match the computed value.</p>
<h2>Options</h2>
<dl>
<dt>-c</p>
<dd>Check that the HMAC values and names listed in the specified file(s) are correct for the files which are available. The format of the files should match the output which the tool produces when computing the values: a hex-encoded HMAC value and then a filename, separated by whitespace.</p>
<dt>-q</p>
<dd>Suppress any output when checking values.</p>
<dt>-d <i>cfgdir</i></p>
<dd>Specify the configuration directory to be used by the NSS library. The default location is <code>/etc/pki/nssdb</code>.</p>
<dt>-h <i>algorithm</i></p>
<dd>Generate the HMAC value using a non-default hashing algorithm. The default is determined by the name used to invoke the tool (sha1hmac, sha256hmac, etc.). If no default can be derived this way, the default setting will be <code>sha512</code>. Specify <i>help</i> or another invalid value to obtain a list of recognized algorithms.</p>
<dt>-u</p>
<dd>Generate an unkeyed checksum instead of an HMAC. The output produced by the tool should then be comparable to that of <i>sha1sum</i> and related tools.</p>
<dt>-k <i>filename</i></p>
<dd>Use the contents of the specified file as the secret key used in computing the HMAC values. <i>If no key file or text is specified, a hard-coded default value is used.</i> This option should <i>always</i> be used.</p>
<dt>-K <i>text</i></p>
<dd>Use the text of the argument as the secret key used in computing the HMAC values. <i>If no key file or text is specified, a hard-coded default value is used.</i></p>
<dt>-b</p>
<dd>Process file contents in binary mode, marking output as such by prefixing filenames with <i>*</i>. This option is not expected to have any other meaningful effect.</p>
<dt>-t <i>bits</i></p>
<dd>Truncate HMAC values to a given length when computing or verifying them.</p>
<dt>-S</p>
<dd>Generate an HMAC over the tool itself and output it on standard out. This is a bootstrapping option which is not expected to be used.</p>
<dt>-P</p>
<dd>Attempt to pass all input files through <i>prelink -y</i> before processing their contents. The tool always attempts to do so when computing or performing a self-check. </p>
</dl>
<h2>Examples</h2>
<p>Example output from <i>sha1hmac</i>, for files on the developer&#8217;s system:<br />
&nbsp;<wbr>&nbsp;<wbr>e64db5e8a9b8a40091e5302fa4de0bfc6c5d19d0&nbsp;<wbr>&nbsp;<wbr>/etc/passwd<br />
&nbsp;<wbr>&nbsp;<wbr>e7d93a2c70ec4d7720c6f2b033c1e5ea19f2d677&nbsp;<wbr>&nbsp;<wbr>/etc/group<br />
&nbsp;<wbr>&nbsp;<wbr>d732d6df77114ea6b81a43d64655f86b1e5ee925&nbsp;<wbr>&nbsp;<wbr>/etc/services<br />
&nbsp;<wbr>&nbsp;<wbr>ad92162bef979054a75d1f3510e6b05902bec641&nbsp;<wbr>&nbsp;<wbr>/etc/hosts </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fipshmac/">fipshmac</a></code>(1), <code><a href="/docs/linux/man/1-fipscheck/">fipscheck</a></code>(1), <code><a href="/docs/linux/man/8-prelink/">prelink</a></code>(8) </p>
<h2>Bugs</h2>
<p>Probably, but let&#8217;s hope not. If you find any, please either report them in the bug database at <a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a> against the &quot;hmaccalc&quot; component, or in the trac instance at <a rel="nofollow" href="https://fedorahosted.org/hmaccalc/.">https://fedorahosted.org/hmaccalc/.</a> </p>
<h2>Author</h2>
<p>Nalin Dahyabhai &lt;nalin [at] redhat.com&gt;</p>
