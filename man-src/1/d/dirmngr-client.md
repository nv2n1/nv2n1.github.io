---
title: "dirmngr-client(1)"
name: "dirmngr-client"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dirmngr-client/"
description: "dirmngr-client – Tool to access the Dirmngr services"
---

<h2 class="name">NAME</h2>
<p> <code>dirmngr-client</code> &#8211; Tool to access the Dirmngr services </p>
<h2>SYNOPSIS</h2>
<p> <code>dirmngr-client</code> [<i>options</i>] [<i>certfile</i>|<i>pattern</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>dirmngr-client</code> is a simple tool to contact a running dirmngr and test whether a certificate has been revoked &#8212; either by being listed in the corresponding CRL or by running the OCSP protocol. If no dirmngr is running, a new instances will be started but this is in general not a good idea due to the huge performance overhead. </p>
<p> The usual way to run this tool is either: </p>
<dl>
<dt>
</dt><dd>
<pre>
dirmngr-client <i>acert</i>
</pre>
</dd></dl>
<p> or </p>
<dl>
<dt>
</dt><dd>
<pre>
dirmngr-client &lt;<i>acert</i>
</pre>
</dd></dl>
<p> Where <i>acert</i> is one DER encoded (binary) X.509 certificates to be tested. </p>
<h2>RETURN VALUE</h2>
<p> <code>dirmngr-client</code> returns these values: </p>
<dl>
<dt><code>0</code></dt>
<dd> The certificate under question is valid; i.e. there is a valid CRL available and it is not listed there or the OCSP request returned that that certificate is valid. </dd>
<dt><code>1</code></dt>
<dd> The certificate has been revoked </dd>
<dt><code>2 (and other values)</code></dt>
<dd> There was a problem checking the revocation state of the certificate. A message to stderr has given more detailed information. Most likely this is due to a missing or expired CRL or due to a network problem. </dd>
</dl>
<h2>OPTIONS</h2>
<p> <code>dirmngr-client</code> may be called with the following options: </p>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Print the program version and licensing information. Note that you cannot abbreviate this command. </dd>
<dt><code>&#8211;help, -h</code></dt>
<dd> Print a usage message summarizing the most useful command-line options. Note that you cannot abbreviate this command. </dd>
<dt><code>&#8211;quiet, -q</code></dt>
<dd> Make the output extra brief by suppressing any informational messages. </dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;verbose</code></dt>
<dd> Outputs additional information while running. You can increase the verbosity by giving several verbose commands to <code>dirmngr</code>, such as &#8216;-vv&#8217;. </dd>
<dt><code>&#8211;pem</code></dt>
<dd> Assume that the given certificate is in PEM (armored) format. </dd>
<dt><code>&#8211;ocsp</code></dt>
<dd> Do the check using the OCSP protocol and ignore any CRLs. </dd>
<dt><code>&#8211;force-default-responder</code></dt>
<dd> When checking using the OCSP protocol, force the use of the default OCSP responder. That is not to use the Reponder as given by the certificate. </dd>
<dt><code>&#8211;ping</code></dt>
<dd> Check whether the dirmngr daemon is up and running. </dd>
<dt><code>&#8211;cache-cert</code></dt>
<dd> Put the given certificate into the cache of a running dirmngr. This is mainly useful for debugging. </dd>
<dt><code>&#8211;validate</code></dt>
<dd> Validate the given certificate using dirmngr&#8217;s internal validation code. This is mainly useful for debugging. </dd>
<dt><code>&#8211;load-crl</code></dt>
<dd> This command expects a list of filenames with DER encoded CRL files. With the option <code>&#8211;url</code> URLs are expected in place of filenames and they are loaded directly from the given location. All CRLs will be validated and then loaded into dirmngr&#8217;s cache. </dd>
<dt><code>&#8211;lookup</code></dt>
<dd> Take the remaining arguments and run a lookup command on each of them. The results are Base-64 encoded outputs (without header lines). This may be used to retrieve certificates from a server. However the output format is not very well suited if more than one certificate is returned. </dd>
<dt><code>&#8211;url</code></dt>
<dd> <code>-u</code> Modify the <code>lookup</code> and <code>load-crl</code> commands to take an URL. </dd>
<dt><code>&#8211;local</code></dt>
<dd> <code>-l</code> Let the <code>lookup</code> command only search the local cache. </dd>
<dt><code>&#8211;squid-mode</code></dt>
<dd> Run <code>dirmngr-client</code> in a mode suitable as a helper program for Squid&#8217;s <code>external_acl_type</code> option. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-dirmngr/">dirmngr</a></code>(8), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
</dt><dd>
<pre>
info gnupg
</pre>
</dd></dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
