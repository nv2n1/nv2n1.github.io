---

title: "euare-userresyncmfadevice(1)"
name: "euare-userresyncmfadevice"
section: "1"
letter: "e"
url: "/docs/linux/man/1-euare-userresyncmfadevice/"
description: "euare-userresyncmfadevice – Re-synchronize an MFA device with the server"
---

<h2>NAME</h2>
<p> euare-userresyncmfadevice &#8211; Re-synchronize an MFA device with the server</p>
<p> euare-userresyncmfadevice <code>-s</code> SERIAL <code>-c1</code> CODE <code>-c2</code> CODE</p>
<dl>
<dt>[&#8211;as-account ACCOUNT] [-U URL]</dt>
<dd> [&#8211;region USER [at] REGION] [-I KEY_ID] [-S KEY] [&#8211;security-token TOKEN] [&#8211;debug] [&#8211;debugger] [&#8211;version] [-h] USER</dd></dl>
<p> Re-synchronize an MFA device with the server</p>
<h3>positional arguments:</h3>
<dl>
<dt>USER</dt>
<dd> user owning the MFA device to re-synchronize (required)</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-s</code> SERIAL, <code>&#8211;serial-number</code> SERIAL</dt>
<dd> serial number of the MFA device (required)</dd>
<dt><code>-c1</code> CODE</dt>
<dd> an authentication code emitted by the MFA device (required)</dd>
<dt><code>-c2</code> CODE</dt>
<dd> a subsequent authentication code emitted by the MFA device (required)</dd>
<dt><code>&#8211;as-account</code> ACCOUNT</dt>
<dd> [Eucalyptus cloud admin only] run this command as the administrator of another account</dd>
<dt><code>-U</code> URL, <code>&#8211;url</code> URL</dt>
<dd> identity service endpoint URL</dd>
<dt><code>&#8211;region</code> USER [at] REGION</dt>
<dd> region and/or user names to search when looking up config file data</dd>
<dt> <code>-I</code> KEY_ID, <code>&#8211;access-key-id</code> KEY_ID</dt>
<dt> <code>-S</code> KEY, <code>&#8211;secret-key</code> KEY</dt>
<dt> <code>&#8211;security-token</code> TOKEN</dt>
<dt><code>&#8211;debug</code></dt>
<dd>
</dd><dd>show debugging output</dd>
<dt><code>&#8211;debugger</code></dt>
<dd> launch interactive debugger on error</dd>
<dt><code>&#8211;version</code></dt>
<dd> show the program&#8217;s version and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit </dd>
</dl>
