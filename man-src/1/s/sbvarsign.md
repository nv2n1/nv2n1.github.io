---

title: "sbvarsign(1)"
name: "sbvarsign"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sbvarsign/"
description: "sbvarsign – UEFI authenticated variable signing tool"
---

<p> <code>sbvarsign</code> [<i>,options/</i>] <i>,&#8211;key &lt;keyfile&gt; &#8211;cert &lt;certfile&gt; &lt;var-name&gt; &lt;var-data-file&gt;/</i></p>
<p> Sign a blob of data for use in SetVariable().</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;engine</code> &lt;eng&gt;</dt>
<dd> use the specified engine to load the key</dd>
<dt><code>&#8211;key</code> &lt;keyfile&gt;</dt>
<dd> signing key (PEM-encoded RSA private key)</dd>
<dt><code>&#8211;cert</code> &lt;certfile&gt;</dt>
<dd> certificate (x509 certificate)</dd>
<dt><code>&#8211;include-attrs</code></dt>
<dd> include attrs at beginning of output file</dd>
<dt><code>&#8211;guid</code> &lt;GUID&gt;</dt>
<dd> EFI GUID for the variable. If omitted, EFI_IMAGE_SECURITY_DATABASE or EFI_GLOBAL_VARIABLE (depending on &lt;var-name&gt;) will be used.</dd>
<dt><code>&#8211;attr</code> &lt;attrs&gt;</dt>
<dd> variable attributes. One or more of: NON_VOLATILE BOOTSERVICE_ACCESS RUNTIME_ACCESS TIME_BASED_AUTHENTICATED_WRITE_ACCESS APPEND_WRITE</dd>
<dt>Separate multiple attrs with a comma,</dt>
<dd> default is all attributes, TIME_BASED_AUTH&#8230; is always included.</dd>
<dt><code>&#8211;output</code> &lt;file&gt;</dt>
<dd> write signed data to &lt;file&gt; (default &lt;var-data-file&gt;.signed) </dd>
</dl>
