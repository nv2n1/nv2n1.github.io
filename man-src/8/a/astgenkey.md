---
title: "astgenkey(8)"
name: "astgenkey"
section: "8"
letter: "a"
url: "/docs/linux/man/8-astgenkey/"
description: "astgenkey — generates keys for for Asterisk IAX2 RSA authentication"
---

<p><code>astgenkey</code> &#8212; generates keys for for Asterisk IAX2 RSA authentication</p>
<h2>Synopsis</h2>
<p><code>astgenkey</code> [ -q ] [ -n ] [ <i>keyname</i> ] </p>
<h2>Description</h2>
<p><code>astgenkey </code> This script generates an RSA private and public key pair in PEM format for use by Asterisk. The private key should be kept a secret, as it can be used to fake your system&#8217;s identity. Thus by default (without the option <i>-n</i> ) the script will create a passphrase-encrypted copy of your secret key: without entering the passphrase you won&#8217;t be able to use it. However if you want to use such a key with Asterisk, you&#8217;ll have to start it interactively, because the scripts that start asterisk can&#8217;t use that encrypted key. The key is identified by a name. If you don&#8217;t write the name on the command-line you&#8217;ll be prompted for one. The outputs of the script are: <i>name</i><code>.pub</code></p>
<dl>
<dd>The public key: not secret. Send this to the other side.</dl>
<p> <i>name</i><code>.key</code></p>
<dl>
<dd>The private key: secret.</dl>
<p> Those files should be copied to <i>/usr/share/asterisk/keys</i> (The private key: on your system. The public key: on other systems) To see the currently-installed keys from the asterisk CLI, use the command</p>
<dl>
<dd>show keys</dl>
<h2>Options</h2>
<p><code>-q</code></p>
<dl>
<dd>Run quietly.</dl>
<p> <code>-n</code></p>
<dl>
<dd>Don&#8217;t encrypt the private key.</dl>
<h2>Security</h2>
<p>The keys are created, using the umask of the user running the command. To create the keys in a secure manner, you should check to ensure that your umask is first set to disallow the private key from being world- readable, such as with the following commands: </p>
<p> <i>umask 0066</i> </p>
<p> <i>astgenkey yourkey</i> </p>
<p> And then make the key accessible to Asterisk (assuming you run it as user &quot;asterisk&quot;). </p>
<p>&nbsp;<wbr>&nbsp;<wbr>chown asterisk&nbsp;<wbr>/usr/share/asterisk/keys/yourname.*</p>
<h2>Files</h2>
<p><i>/usr/share/asterisk/keys</i></p>
<dl>
<dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-asterisk/">asterisk</a>(8), <a href="/docs/linux/man/1-genrsa/">genrsa</a>(1), <a href="/docs/linux/man/1-rsa/">rsa</a>(1), <a rel="nofollow" href="http://www.voip-info.org/wiki-Asterisk+iax+rsa+auth">http://www.voip-info.org/wiki-Asterisk+iax+rsa+auth</a> </p>
<h2>Author</h2>
<p>This manual page was written by Tzafrir Cohen &lt;tzafrir.cohen [at] xorcom.com&gt; Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
