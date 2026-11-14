---
title: "ldns-dane(1)"
name: "ldns-dane"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-dane/"
description: "ldns-dane – verify or create TLS authentication with DANE (RFC6698)"
---

<h2>NAME</h2>
<p> ldns-dane &#8211; verify or create TLS authentication with DANE (RFC6698)</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-dane</code> <i>[OPTIONS]</i> <i>verify</i> <i>name</i> <i>port</i> </p>
<p> <code>ldns-dane</code> <i>[OPTIONS]</i> <i>-t</i> <i>tlsafile</i> <i>verify</i> </p>
<p> <code>ldns-dane</code> <i>[OPTIONS]</i> <i>name</i> <i>port</i> <i>create</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <i>Certificate-usage</i> [ <i>Selector</i> [ <i>Matching-type</i> ] ] ] </p>
<p> <code>ldns-dane</code> <i>-h</i> </p>
<p> <code>ldns-dane</code> <i>-v</i> </p>
<h2>DESCRIPTION</h2>
<p> In the first form: A TLS connection to <i>name</i>:<i>port</i> is established. The TLSA resource record(s) for <i>name</i> are used to authenticate the connection. </p>
<p> In the second form: The TLSA record(s) are read from <i>tlsafile</i> and used to authenticate the TLS service they reference. </p>
<p> In the third form: A TLS connection to <i>name</i>:<i>port</i> is established and used to create the TLSA resource record(s) that would authenticate the connection. The parameters for TLSA rr creation are: </p>
<p> <i>Certificate-usage</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> CA constraint</p>
<dt>1</p>
<dd> Service certificate constraint</p>
<dt>2</p>
<dd> Trust anchor assertion</p>
<dt>3</p>
<dd> Domain-issued certificate (default)</dl>
</dl>
<p> <i>Selector</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Full certificate (default)</p>
<dt>1</p>
<dd> SubjectPublicKeyInfo</dl>
</dl>
<p> <i>Matching-type</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> No hash used</p>
<dt>1</p>
<dd> SHA-256 (default)</p>
<dt>2</p>
<dd> SHA-512</dl>
</dl>
<p> In stead of numbers the first few letters of the value may be used. Except for the hash algorithm name, where the full name must be specified. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-4</p>
<dd> TLS connect IPv4 only</p>
<dt>-6</p>
<dd> TLS connect IPv6 only</p>
<dt>-a <i>address</i></p>
<dd> Don&#8217;t try to resolve <i>name</i>, but connect to <i>address</i> instead. </p>
<p> This option may be given more than once.</p>
<dt>-b</p>
<dd> print &quot;<i>name</i>. TYPE52 \# <i>size</i> <i>hexdata</i>&quot; form instead of TLSA presentation format.</p>
<dt>-c <i>certfile</i></p>
<dd> Do not TLS connect to <i>name</i>:<i>port</i>, but authenticate (or make TLSA records) for the certificate (chain) in <i>certfile</i> instead.</p>
<dt>-d</p>
<dd> Assume DNSSEC validity even when the TLSA records were acquired insecure or were bogus.</p>
<dt>-f <i>CAfile</i></p>
<dd> Use CAfile to validate. Default is /etc/pki/tls/certs/ca-bundle.trust.crt</p>
<dt>-h</p>
<dd> Print short usage help</p>
<dt>-i</p>
<dd> Interact after connecting.</p>
<dt>-k <i>keyfile</i></p>
<dd> Specify a file that contains a trusted DNSKEY or DS rr. Key(s) are used when chasing signatures (i.e. <i>-S</i> is given). </p>
<p> This option may be given more than once. </p>
<p> Alternatively, if <code>-k</code> is not specified, and a default trust anchor (/var/lib/unbound/root.key) exists and contains a valid DNSKEY or DS record, it will be used as the trust anchor.</p>
<dt>-n</p>
<dd> Do <code>not</code> verify server name in certificate.</p>
<dt>-o <i>offset</i></p>
<dd> When creating a &quot;Trust anchor assertion&quot; TLSA resource record, select the <i>offset</i>th certificate offset from the end of the validation chain. 0 means the last certificate, 1 the one but last, 2 the second but last, etc. </p>
<p> When <i>offset</i> is -1 (the default), the last certificate is used (like with 0) that MUST be self-signed. This can help to make sure that the intended (self signed) trust anchor is actually present in the server certificate chain (which is a DANE requirement).</p>
<dt>-p <i>CApath</i></p>
<dd> Use certificates in the <i>CApath</i> directory to validate. Default is /etc/pki/tls/certs/</p>
<dt>-s</p>
<dd> When creating TLSA resource records with the &quot;CA Constraint&quot; and the &quot;Service Certificate Constraint&quot; certificate usage, do not validate and assume PKIX is valid. </p>
<p> For &quot;CA Constraint&quot; this means that verification should end with a self-signed certificate.</p>
<dt>-S</p>
<dd> Chase signature(s) to a known key. </p>
<p> Without this option, the local network is trusted to provide a DNSSEC resolver (i.e. AD bit is checked).</p>
<dt>-t <i>tlsafile</i></p>
<dd> Read TLSA record(s) from <i>tlsafile</i>. When <i>name</i> and <i>port</i> are also given, only TLSA records that match the <i>name</i>, <i>port</i> and <i>transport</i> are used. Otherwise the owner name of the TLSA record(s) will be used to determine <i>name</i>, <i>port</i> and <i>transport</i>.</p>
<dt>-u</p>
<dd> Use UDP transport instead of TCP.</p>
<dt>-v</p>
<dd> Show version and exit. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>/var/lib/unbound/root.key</p>
<dd> The file from which trusted keys are loaded for signature chasing, when no <code>-k</code> option is given. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-unbound-anchor/">unbound-anchor</a>(8) </p>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <i>ldns-team [at] nlnetlabs.nl</i>. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2012 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
