---

title: "ykclient(1)"
name: "ykclient"
section: "1"
letter: "y"
url: "/docs/linux/man/1-ykclient/"
description: "ykclient – YubiCloud One-Time-Password Validation Client"
---

<p> ykclient &#8211; YubiCloud One-Time-Password Validation Client</p>
<h2>SYNOPSIS</h2>
<p> <code>ykclient</code> [<i>OPTION</i>]&#8230; <i>CLIENTID YUBIKEYOTP</i></p>
<h2>DESCRIPTION</h2>
<p> Validate the YUBIKEYOTP one-time-password against the YubiCloud using CLIENTID as the client identifier. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Display this help screen</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display version information</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Print debugging information</dd>
<dt><code>&#8211;url</code> URL</dt>
<dd> Validation service URL, for example, &quot;<a rel="nofollow" href="http://api.yubico.com/wsapi/verify">http://api.yubico.com/wsapi/verify</a>&quot;</dd>
<dt><code>&#8211;ca</code> CADIR</dt>
<dd> Path to directory containing Certificate Authoritity, e.g., &quot;/usr/local/etc/CERTS&quot;</dd>
<dt><code>&#8211;cai</code> CAFILE</dt>
<dd> Path to a file holding one or more certificated to verify the peer with</dd>
<dt><code>&#8211;apikey</code> Key</dt>
<dd> API key for HMAC validation of request/response</dd>
<dt><code>&#8211;proxy</code> ip:port</dt>
<dd> Connect to validation service through a proxy, e.g., &quot;socks5h://user:pass [at] 127.0.0.1:1080&quot;</dd></dl>
<p> Exit status is 0 on success, 1 if there is a hard failure, 2 if the OTP was replayed, 3 for other soft OTP-related failures.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs at &lt;<a rel="nofollow" href="https://github.com/Yubico/yubico-c-client">https://github.com/Yubico/yubico-c-client</a>&gt;. </p>
