---
title: "snmpkey(1)"
name: "snmpkey"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpkey/"
description: "snmpkey – Create SNMPv3 security keys for the Net::SNMP module"
---

<h2 class="name">NAME</h2>
<p> snmpkey &#8211; Create SNMPv3 security keys for the Net::SNMP module </p>
<h2>USAGE</h2>
<p> The <tt>&quot;snmpkey&quot;</tt> utility generates security keys based on a password and an authoritativeEngineID passed on the command line. This key can then be used by the Net::SNMP module instead of the plain text password when creating SNMPv3 objects. </p>
<pre><code>
snmpkey&lt;authProto&gt;&lt;password&gt;&lt;authEngineID&gt;[&lt;privProto&gt;[&lt;password&gt;]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The User-based Security Model used by SNMPv3 defines an algorithm which &#8220;localizes&#8221; a plain text password to a specific authoritativeEngineID using a one-way hash. This resulting key is used by the <font SIZE="-1">SNMP</font> application instead of the plain text password for security reasons. </p>
<p> The Net::SNMP module allows the user to either provide a plain text password or a localized key to the object constructor when configuring authentication or privacy. The <tt>&quot;snmpkey&quot;</tt> utility can be used to generate the key to be used by the <code>-authkey</code> or <code>-privkey</code> named arguments when they are passed to the Net::SNMP <tt>&quot;session()&quot;</tt> constructor.</p>
<h2>REQUIRED ARGUMENTS</h2>
<p> The <tt>&quot;snmpkey&quot;</tt> utility requires at least three command line arguments. The first argument defines which hash algorithm to use when creating the authKey. Either <font SIZE="-1">HMAC-MD5-96</font> or <font SIZE="-1">HMAC-SHA-96</font> can be specified with the string &#8216;md5&#8217; or &#8216;sha&#8217; respectively. This choice must match the algorithm passed to the <code>-authprotocol</code> argument when creating the Net::SNMP object. The second argument is the plain text password that is to be localized to create the authKey. The third required argument is the authoritativeEngineID of the remote <font SIZE="-1">SNMP</font> engine associated with the Net::SNMP argument <code>-hostname</code>. The authoritativeEngineID is to be entered as a hexadecimal string 10 to 64 characters (5 to 32 octets) long and can be prefixed with an optional &#8220;0x&#8221;. </p>
<p> The last two arguments are optional and can be used to determine how the privKey will be generated. By default, the fourth argument assumes a value of &#8216;des&#8217; corresponding to the default privacy protocol defined in the User-based Security Model. The Net::SNMP module supports <font SIZE="-1">CBC-3DES-EDE</font> and <font SIZE="-1">CFB128-AES-128</font> as alternatives to the default protocol CBC-DES. These protocols can be chosen by specifying the string &#8216;3des&#8217; or &#8216;aes&#8217; respectively. This choice must match the protocol passed to the <code>-privprotocol</code> argument when creating the Net::SNMP object. The last argument can be used to specify the plain text password that is to be localized to create the privKey. If this argument is not specified, the authKey password is used.</p>
<h2>AUTHOR</h2>
<p> David M. Town &lt;dtown [at] cpan.org&gt;</p>
<h2>LICENSE AND COPYRIGHT</h2>
<p> Copyright (c) 2001-2009 David M. Town. All rights reserved. </p>
<p> This program is free software; you may redistribute it and/or modify it under the same terms as the Perl 5 programming language system itself.</p>
<h2>SEE ALSO</h2>
<p> Net::SNMP </p>
<h2>Index</h2>
