---
title: "ddns-confgen(8)"
name: "ddns-confgen"
section: "8"
letter: "d"
url: "/docs/linux/man/8-ddns-confgen/"
description: "ddns-confgen – ddns key generation tool"
---

<p>ddns-confgen &#8211; ddns key generation tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ddns-confgen</code> [<code>-a&nbsp;<wbr></code><i>algorithm</i>] [<code>-h</code>] [<code>-k&nbsp;<wbr></code><i>keyname</i>] [<code>-r&nbsp;<wbr></code><i>randomfile</i>] [-s&nbsp;<wbr><i>name</i> | -z&nbsp;<wbr><i>zone</i>] [<code>-q</code>] [name]</dl>
<h2>Description</h2>
<p><code>ddns-confgen</code></p>
<dd>generates a key for use by <code>nsupdate</code> and <code>named</code>. It simplifies configuration of dynamic zones by generating a key and providing the <code>nsupdate</code> and <code>named.conf</code> syntax that will be needed to use it, including an example <code>update-policy</code> statement. </p>
<p> If a domain name is specified on the command line, it will be used in the name of the generated key and in the sample <code>named.conf</code> syntax. For example, <code>ddns-confgen example.com</code> would generate a key called &quot;ddns-key.example.com&quot;, and sample <code>named.conf</code> command that could be used in the zone definition for &quot;example.com&quot;. </p>
<p> Note that <code>named</code> itself can configure a local DDNS key for use with <code>nsupdate -l</code>. <code>ddns-confgen</code> is only needed when a more elaborate configuration is required: for instance, if <code>nsupdate</code> is to be used from a remote system.</p>
<h2>Options</h2>
<p>-a <i>algorithm</i></p>
<dl>
<dd>Specifies the algorithm to use for the TSIG key. Available choices are: hmac-md5, hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha384 and hmac-sha512. The default is hmac-sha256.</dl>
<p> -h</p>
<dl>
<dd>Prints a short summary of the options and arguments to <code>ddns-confgen</code>.</dl>
<p> -k <i>keyname</i></p>
<dl>
<dd>Specifies the key name of the DDNS authentication key. The default is <code>ddns-key</code> when neither the <code>-s</code> nor <code>-z</code> option is specified; otherwise, the default is <code>ddns-key</code> as a separate label followed by the argument of the option, e.g., <code>ddns-key.example.com.</code> The key name must have the format of a valid domain name, consisting of letters, digits, hyphens and periods.</dl>
<p> -q</p>
<dl>
<dd>Quiet mode: Print only the key, with no explanatory text or usage examples.</dl>
<p> -r <i>randomfile</i></p>
<dl>
<dd>Specifies a source of random data for generating the authorization. If the operating system does not provide a <i>/dev/random</i> or equivalent device, the default source of randomness is keyboard input. <i>randomdev</i> specifies the name of a character device or file containing random data to be used instead of the default. The special value <i>keyboard</i> indicates that keyboard input should be used.</dl>
<p> -s <i>name</i></p>
<dl>
<dd>Single host mode: The example <code>named.conf</code> text shows how to set an update policy for the specified <i>name</i> using the &quot;name&quot; nametype. The default key name is ddns-key.<i>name</i>. Note that the &quot;self&quot; nametype cannot be used, since the name to be updated may differ from the key name. This option cannot be used with the <code>-z</code> option.</dl>
<p> -z <i>zone</i></p>
<dl>
<dd>zone mode: The example <code>named.conf</code> text shows how to set an update policy for the specified <i>zone</i> using the &quot;zonesub&quot; nametype, allowing updates to all subdomain names within that <i>zone</i>. This option cannot be used with the <code>-s</code> option.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-nsupdate/">nsupdate</a></code>(1), <code><a href="/docs/linux/man/5-named-conf/">named.conf</a></code>(5), <code><a href="/docs/linux/man/8-named/">named</a></code>(8), BIND 9 Administrator Reference Manual.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
