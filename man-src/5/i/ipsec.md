---
title: "ipsec(5)"
name: "ipsec"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec/"
description: "ipsec.secrets – secrets for IKE/IPsec authentication"
---

<p>ipsec.secrets &#8211; secrets for IKE/IPsec authentication</p>
<h2>Description</h2>
<p>The file ipsec.secrets contains a list of secrets. Currently supported secrets are preshared secrets (PSKs), RSA keys and XAUTH passwords. These secrets are used by <code><a href="/docs/linux/man/8-pluto/">pluto</a></code>(8) , the Libreswan Internet Key Exchange daemon, to authenticate other hosts. </p>
<p> RSA private keys are stored in the NSS database. The secrets file only contains a reference to these private RSA keys. For RSA keys belonging to imported X.509 certificates, the certificate &quot;friendly name&quot; is used. For raw RSA keys, the CKAID is used. </p>
<p> XAUTH passwords are stored in plaintext in this file. The secrets file should be owned by root, and permissions should be set to block all access by others. (eg: chmod 600) </p>
<p> The file is a sequence of entries and include directives. Here is an example &#8211; each entry or directive must start at the left margin, but if it continues beyond a single line, each continuation line must be indented. </p>
<dl>
<dd>
<pre># sample /etc/ipsec.secrets file for 10.1.0.1
10.1.0.1 10.2.0.1 : PSK &quot;secret shared by two hosts&quot;
# sample roadwarrior
%any gateway.corp.com : PSK &quot;shared secret with many roadwarriors&quot;
# sample server for roadwarriors
myip %any : PSK &quot;shared secret with many roadwarriors&quot;
# an entry may be split across lines,
# but indentation matters
<a rel="nofollow" href="http://www.xs4all.nl">www.xs4all.nl</a> @<a href="http://www.kremvax.ru">www.kremvax.ru</a>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>10.6.0.1 10.7.0.1 1.8.0.1 : PSK &quot;secret shared by 5 systems&quot;
# a raw RSA private key in NSS. All but the public exponent now point
# to the NSS CKAIDNSS
# note that the lines are too wide for a
# man page, so ... has been substituted for
# the truncated part
@my.com : RSA {
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#pubkey=0sAQPaGwWbUSK...
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PublicExponent: 0x03
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>PrivateExponent: 0x316e6593...
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Prime1: 0x316e6593...
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Prime2: 0x316e6593...
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Exponent1: 0x316e6593...
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Exponent2: 0x316e6593...
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Coefficient: 0x316e6593...
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CKAIDNSS: 0x316e6593...
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>}
# an imported X.509 certificate in NSS
: RSA &quot;&lt;friendly name&gt;&quot;
# XAUTH password, used with leftxauthusername=username
@username : XAUTH &quot;password&quot;
include ipsec.*.secrets # get secrets from other files</pre>
</dl>
<p> Each entry in the file is a list of indices, followed by a secret. The two parts are separated by a colon (<code>:</code>) that is followed by whitespace or a newline. </p>
<p> An index is an IP address, or a Fully Qualified Domain Name, user [at] FQDN, <code>%any</code> or <code>%any6</code> (other kinds may come). An IP address may be written in the familiar dotted quad form or as a domain name to be looked up when the file is loaded (or in any of the forms supported by the Libreswan <code><a href="/docs/linux/man/3-ipsec_ttoaddr/">ipsec_ttoaddr</a></code>(3) routine). Be aware that using domain names requires DNS to be functional before the IPsec tunnel comes up. To denote a Fully Qualified Domain Name (as opposed to an IP address denoted by its domain name), precede the name with an at sign (<code>@</code>). </p>
<p> Matching IDs with indices is fairly straightforward: they have to be equal. In the case of a &#8220;Road Warrior&#8221; connection, if an equal match is not found for the Peer&#8217;s ID, and it is in the form of an IP address, an index of <code>%any</code> will match the peer&#8217;s IP address if IPV4 and <code>%any6</code> will match a the peer&#8217;s IP address if IPV6. </p>
<p> This file is only read at startup time. If any changes are made to this file, the pluto daemon should be told to re-read this file using the command <code>ipsec secrets</code> or <code>ipsec auto &#8211;rereadsecrets</code>. Note that currently there is no way to add a specific new entry &#8211; it&#8217;s all or nothing. </p>
<p> Smartcard support has been moved from Libreswan to NSS. Please see the NSS documentation on how to configure smartcards. </p>
<p> An additional complexity arises in the case of authentication by preshared secret: the responder will need to look up the secret before the Peer&#8217;s ID payload has been decoded, so the ID used will be the IP address. </p>
<p> To authenticate a connection between two hosts, the entry that most specifically matches the host and peer IDs is used. An entry with no index will match any host and peer. More specifically, an entry with one index will match a host and peer if the index matches the host&#8217;s ID (the peer isn&#8217;t considered). Still more specifically, an entry with multiple indices will match a host and peer if the host ID and peer ID each match one of the indices. If the key is for an asymmetric authentication technique (i.e. a public key system such as RSA), an entry with multiple indices will match a host and peer even if only the host ID matches an index (it is presumed that the multiple indices are all identities of the host). It is acceptable for two entries to be the best match as long as they agree about the secret or private key. </p>
<p> Authentication by preshared secret requires that both systems find the identical secret (the secret is not actually transmitted by the IKE protocol). If both the host and peer appear in the index list, the same entry will be suitable for both systems so verbatim copying between systems can be used. This naturally extends to larger groups sharing the same secret. Thus multiple-index entries are best for PSK authentication. </p>
<p> Authentication by raw RSA Signatures requires that each host have its own private key. A host could reasonably use a different private keys for different interfaces and for different peers. But it would not be normal to share entries between systems. Thus no-index and one-index forms of entry often make sense for RSA Signature authentication. </p>
<p> The key part of an entry may start with a token indicating the kind of key. &#8220;RSA&#8221; signifies RSA private key and &#8220;PSK&#8221; signifies PreShared Key (case is ignored). </p>
<p> The token &#8220;XAUTH&#8221; indicates a eXtended Authentication password. There should be one indice, and it should be in the @FQDN format. The file will be searched with the XAUTH username, which is usually provided in the configuration file. XAUTH is otherwise identical to PSK in syntax. </p>
<p> A preshared secret is most conveniently represented as a sequence of characters, delimited by the double-quote character (<code>&quot;</code>). The sequence cannot contain a newline or double-quote. Strictly speaking, the secret is actually the sequence of bytes that is used in the file to represent the sequence of characters (excluding the delimiters). A preshared secret may also be represented, without quotes, in any form supported by <code><a href="/docs/linux/man/3-ipsec_ttodata/">ipsec_ttodata</a></code>(3). </p>
<p> A raw RSA private key is a composite of eight generally large numbers. The notation used is a brace-enclosed list of field name and value pairs (see the example above). A suitable key, in a suitable format, may be generated by <code><a href="/docs/linux/man/8-ipsec_rsasigkey/">ipsec_rsasigkey</a></code>(8). The structure is very similar to that used by BIND 8.2.2 or later, but note that the numbers must have a &#8220;0s&#8221; prefix if they are in base 64. The order of the fields is fixed. Note that most fields are now unused and filled in with the CKAID, which is a reference to the location within the NSS database. </p>
<p> The first token of an entry must start in the first column of its line. Subsequent tokens must be separated by whitespace, except for a colon token, which only needs to be followed by whitespace. A newline is taken as whitespace, but every line of an entry after the first must be indented. </p>
<p> Whitespace at the end of a line is ignored (except in the 0t notation for a key). At the start of line or after whitespace, <code>#</code> and the following text up to the end of the line is treated as a comment. Within entries, all lines must be indented (except for lines with no tokens). Outside entries, no line may be indented (this is to make sure that the file layout reflects its structure). </p>
<p> An include directive causes the contents of the named file to be processed before continuing with the current file. The filename is subject to &#8220;globbing&#8221; as in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), so every file with a matching name is processed. Includes may be nested to a modest depth (10, currently). If the filename doesn&#8217;t start with a <code>/</code>, the directory containing the current file is prepended to the name. The include directive is a line that starts with the word <code>include</code>, followed by whitespace, followed by the filename (which must not contain whitespace).</p>
<h2>Files</h2>
<p>/etc/ipsec.secrets</p>
<h2>See Also</h2>
<p>The rest of the Libreswan distribution, in particular <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5), <code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_newhostkey/">ipsec_newhostkey</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_rsasigkey/">ipsec_rsasigkey</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_showhostkey/">ipsec_showhostkey</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8) <code>&#8211;rereadsecrets</code>, and <code><a href="/docs/linux/man/8-pluto/">pluto</a></code>(8) <code>&#8211;listen</code>.</p>
<h2>History</h2>
<p>Originally designed for the FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by D. Hugh Redelmeier. Updated for Openswan by Ken Bantoft. Updated for Libreswan by Paul Wouters </p>
<p> This file originally stored the private part of RSA keys. All private key material is now stored in the NSS database. The fields of the raw RSA key currently filled with the CKAID might be ignored and removed in future versions.</p>
<h2>Bugs</h2>
<p>If an ID is 0.0.0.0, it will match <code>%any</code>; if it is <code>0::0</code>, it will match <code>%any6</code>.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
