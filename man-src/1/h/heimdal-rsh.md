---
title: "heimdal-rsh(1)"
name: "heimdal-rsh"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-rsh/"
description: "rsh – remote shell"
---

<h2 class="name">NAME</h2>
<p> <code>rsh</code> &#8211; remote shell </p>
<h2>SYNOPSIS</h2>
<p> [-<code>45FGKdefnuxz</code> ] [-<code>U string </code> ] [-<code>p </code><i>port</i> ] [-<code>l </code><i>username</i> ] [-<code>P </code><i>N|O</i> ] <i>host [command]</i></p>
<h2>DESCRIPTION</h2>
<p> authenticates to the <a href="/docs/linux/man/8-rshd/">rshd</a>(8) daemon on the remote <i>host</i> and then executes the specified <i>command</i> </p>
<p> copies its standard input to the remote command, and the standard output and error of the remote command to its own. </p>
<p> Valid options are:</p>
<dl>
<dt> &#8211;<code>4</code> &#8211;<code>-krb4</code></p>
<dd>
<dd>The &#8211;<code>4</code> option requests Kerberos 4 authentication. Normally all supported authentication mechanisms will be tried, but in some cases more explicit control is desired.</p>
<dt> &#8211;<code>5</code> &#8211;<code>-krb5</code></p>
<dd>
<dd>The &#8211;<code>5</code> option requests Kerberos 5 authentication. This is analogous to the &#8211;<code>4</code> option.</p>
<dt> &#8211;<code>K</code> &#8211;<code>-broken</code></p>
<dd>
<dd>The &#8211;<code>K</code> option turns off all Kerberos authentication. The security in this mode relies on reserved ports. The long name is an indication of how good this is.</p>
<dt> &#8211;<code>n</code> &#8211;<code>-no-input</code></p>
<dd>
<dd>The &#8211;<code>n</code> option directs the input from the /dev/null device (see the Sx BUGS section of this manual page).</p>
<dt><code>-d</code></p>
<dd> Enable <a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2) socket debugging.</p>
<dt> &#8211;<code>e</code> &#8211;<code>-no-stderr</code></p>
<dd>
<dd>Don&#8217;t use a separate socket for the stderr stream. This can be necessary if rsh-ing through a NAT bridge.</p>
<dt> &#8211;<code>x</code> &#8211;<code>-encrypt</code></p>
<dd>
<dd>The &#8211;<code>x</code> option enables encryption for all data exchange. This is only valid for Kerberos authenticated connections (see the Sx BUGS section for limitations).</p>
<dt> &#8211;<code>z</code></p>
<dd>
<dd>The opposite of &#8211;<code>x</code> This is the default, and is mainly useful if encryption has been enabled by default, for instance in the <code>appdefaults</code> section of /etc/krb5.conf when using Kerberos 5.</p>
<dt> &#8211;<code>f</code> &#8211;<code>-forward</code></p>
<dd>
<dd>Forward Kerberos 5 credentials to the remote host. Also settable via <code>appdefaults</code> (see krb5.conf).</p>
<dt> &#8211;<code>F</code> &#8211;<code>-forwardable</code></p>
<dd>
<dd>Make the forwarded credentials re-forwardable. Also settable via <code>appdefaults</code> (see krb5.conf).</p>
<dt> &#8211;<code>l </code><i>string</i> &#8211;<code>-user= </code><i>string</i></p>
<dd>
<dd>By default the remote username is the same as the local. The &#8211;<code>l</code> option or the username [at] host format allow the remote name to be specified.</p>
<dt> &#8211;<code>n</code> &#8211;<code>-no-input</code></p>
<dd>
<dd>Direct input from /dev/null (see the Sx BUGS section).</p>
<dt> &#8211;<code>p </code><i>number-or-service</i> &#8211;<code>-port= </code><i>number-or-service</i></p>
<dd>
<dd>Connect to this port instead of the default (which is 514 when using old port based authentication, 544 for Kerberos 5 and non-encrypted Kerberos 4, and 545 for encrytpted Kerberos 4; subject of course to the contents of /etc/services )</p>
<dt> &#8211;<code>P </code><i>N|O|1|2</i> &#8211;<code>-protocol= </code><i>N|O|1|2</i></p>
<dd>
<dd>Specifies the protocol version to use with Kerberos 5. <i>N</i> and <i>2</i> select protocol version 2, while <i>O</i> and <i>1</i> select version 1. Version 2 is believed to be more secure, and is the default. Unless asked for a specific version, will try both. This behaviour may change in the future.</p>
<dt> &#8211;<code>u</code> &#8211;<code>-unique</code></p>
<dd>
<dd>Make sure the remote credentials cache is unique, that is, don&#8217;t reuse any existing cache. Mutually exclusive to &#8211;<code>U</code></p>
<dt> &#8211;<code>U string </code> &#8211;<code>-tkfile= string </code></p>
<dd>
<dd>Name of the remote credentials cache. Mutually exclusive to &#8211;<code>u</code></p>
<dt> &#8211;<code>x</code> &#8211;<code>-encrypt</code></p>
<dd>
<dd>The &#8211;<code>x</code> option enables encryption for all data exchange. This is only valid for Kerberos authenticated connections (see the Sx BUGS section for limitations).</p>
<dt><code>-z</code></p>
<dd> The opposite of &#8211;<code>x</code> This is the default, but encryption can be enabled when using Kerberos 5, by setting the <code>libdefaults/encrypt</code> option in krb5.conf5.</dl>
<h2>EXAMPLES</h2>
<p> Care should be taken when issuing commands containing shell meta characters. Without quoting, these will be expanded on the local machine. </p>
<p> The following command: </p>
<blockquote><p><tt>rsh otherhost cat remotefile &gt; localfile</tt></p></blockquote>
<p> will write the contents of the remote remotefile to the local localfile but: </p>
<blockquote><p><tt>rsh otherhost 'cat remotefile &gt; remotefile2'</tt></p></blockquote>
<p> will write it to the remote remotefile2</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/hosts </code></p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rlogin/">rlogin</a>(1), krb_realmofhost3, krb_sendauth3, hosts.equiv5, krb5.conf5, <a href="/docs/linux/man/5-rhosts/">rhosts</a>(5), <a href="/docs/linux/man/8-kerberos/">kerberos</a>(8) <a href="/docs/linux/man/8-rshd/">rshd</a>(8)</p>
<h2>HISTORY</h2>
<p> The command appeared in BSD 4.2</p>
<h2>AUTHORS</h2>
<p> This implementation of was written as part of the Heimdal Kerberos 5 implementation.</p>
<h2>BUGS</h2>
<p> Some shells (notably <a href="/docs/linux/man/1-csh/">csh</a>(1)) will cause to block if run in the background, unless the standard input is directed away from the terminal. This is what the &#8211;<code>n</code> option is for. </p>
<p> The &#8211;<code>x</code> options enables encryption for the session, but for both Kerberos 4 and 5 the actual command is sent unencrypted, so you should not send any secret information in the command line (which is probably a bad idea anyway, since the command line can usually be read with tools like <a href="/docs/linux/man/1-ps/">ps</a>(1)). Forthermore in Kerberos 4 the command is not even integrity protected, so anyone with the right tools can modify the command. </p>
<h2>Index</h2>
