---
title: "kdc(8)"
name: "kdc"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kdc/"
description: "kdc – Kerberos 5 server"
---

<p><code>kdc</code> &#8211; Kerberos 5 server</p>
<h2>Synopsis</h2>
<p>-words [-<code>c </code><i>file | </i> &#8211;<code>-config-file= </code><i>file</i> ] [-<code>p | &#8211;no-require-preauth</code> ] [-<code>-max-request= </code><i>size</i> ] [-<code>H | &#8211;enable-http</code> ] [-<code>-no-524</code> ] [-<code>-kerberos4</code> ] [-<code>-kerberos4-cross-realm</code> ] [-<code>r </code><i>string | </i> &#8211;<code>-v4-realm= </code><i>string</i> ] [-<code>P </code><i>portspec | </i> &#8211;<code>-ports= </code><i>portspec</i> ] [-<code>-detach</code> ] [-<code>-disable-des</code> ] [-<code>-addresses= </code><i>list of addresses</i> ]</p>
<h2>Description</h2>
<p>serves requests for tickets. When it starts, it first checks the flags passed, any options that are not specified with a command line flag are taken from a config file, or from a default compiled-in value. </p>
<p> Options supported:</p>
<dl>
<dt><code>-c </code><i>file , &#8211;</i><code>-config-file= </code><i>file</i></p>
<dd>Specifies the location of the config file, the default is /var/heimdal/kdc.conf This is the only value that can&#8217;t be specified in the config file.</p>
<dt><code>-p , &#8211;no-require-preauth</code></p>
<dd>Turn off the requirement for pre-autentication in the initial AS-REQ for all principals. The use of pre-authentication makes it more difficult to do offline password attacks. You might want to turn it off if you have clients that don&#8217;t support pre-authentication. Since the version 4 protocol doesn&#8217;t support any pre-authentication, serving version 4 clients is just about the same as not requiring pre-athentication. The default is to require pre-authentication. Adding the require-preauth per principal is a more flexible way of handling this.</p>
<dt><code>&#8211;max-request= </code><i>size</i></p>
<dd>Gives an upper limit on the size of the requests that the kdc is willing to handle.</p>
<dt><code>-H , &#8211;enable-http</code></p>
<dd>Makes the kdc listen on port 80 and handle requests encapsulated in HTTP.</p>
<dt><code>&#8211;no-524</code></p>
<dd>don&#8217;t respond to 524 requests</p>
<dt><code>&#8211;kerberos4</code></p>
<dd>respond to Kerberos 4 requests</p>
<dt><code>&#8211;kerberos4-cross-realm</code></p>
<dd>respond to Kerberos 4 requests from foreign realms. This is a known security hole and should not be enabled unless you understand the consequences and are willing to live with them.</p>
<dt><code>-r </code><i>string , &#8211;</i><code>-v4-realm= </code><i>string</i></p>
<dd>What realm this server should act as when dealing with version 4 requests. The database can contain any number of realms, but since the version 4 protocol doesn&#8217;t contain a realm for the server, it must be explicitly specified. The default is whatever is returned by Fn krb_get_lrealm . This option is only available if the KDC has been compiled with version 4 support.</p>
<dt><code>-P </code><i>portspec , &#8211;</i><code>-ports= </code><i>portspec</i></p>
<dd>Specifies the set of ports the KDC should listen on. It is given as a white-space separated list of services or port numbers.</p>
<dt><code>&#8211;addresses= </code><i>list of addresses</i></p>
<dd>The list of addresses to listen for requests on. By default, the kdc will listen on all the locally configured addresses. If only a subset is desired, or the automatic detection fails, this option might be used.</p>
<dt><code>&#8211;detach</code></p>
<dd>detach from pty and run as a daemon.</p>
<dt><code>&#8211;disable-des</code></p>
<dd>disable all des encryption types, makes the kdc not use them.</dl>
<p> All activities are logged to one or more destinations, see krb5.conf5, and krb5_openlog3. The entity used for logging is <code>kdc</code></p>
<h2>Configuration File</h2>
<p>The configuration file has the same syntax as krb5.conf5, but will be read before /etc/krb5.conf so it may override settings found there. Options specific to the KDC only are found in the &#8220;[kdc]&#8221; section. All the command-line options can preferably be added in the configuration file. The only difference is the pre-authentication flag, which has to be specified as: </p>
<blockquote><p><tt>require-preauth = no</tt></p></blockquote>
<p> (in fact you can specify the option as &#8211;<code>-require-preauth=no</code> </p>
<p> And there are some configuration options which do not have command-line equivalents:</p>
<dl>
<dt><code>enable-digest = </code><i>boolean</i></p>
<dd>turn on support for digest processing in the KDC. The default is FALSE.</p>
<dt><code>check-ticket-addresses = </code><i>boolean</i></p>
<dd>Check the addresses in the ticket when processing TGS requests. The default is TRUE.</p>
<dt><code>allow-null-ticket-addresses = </code><i>boolean</i></p>
<dd>Permit tickets with no addresses. This option is only relevant when check-ticket-addresses is TRUE.</p>
<dt><code>allow-anonymous = </code><i>boolean</i></p>
<dd>Permit anonymous tickets with no addresses.</p>
<dt><code>max-kdc-datagram-reply-length = </code><i>number</i></p>
<dd>Maximum packet size the UDP rely that the KDC will transmit, instead the KDC sends back a reply telling the client to use TCP instead.</p>
<dt><code>transited-policy = always-check |</code></p>
<dd>Li allow-per-principal | Li always-honour-request This controls how KDC requests with the <code>disable-transited-check</code> flag are handled. It can be one of:</p>
<dl>
<dt><code>always-check</code></p>
<dd>Always check transited encoding, this is the default.</p>
<dt><code>allow-per-principal</code></p>
<dd>Currently this is identical to <code>always-check</code> In a future release, it will be possible to mark a principal as able to handle unchecked requests.</p>
<dt><code>always-honour-request</code></p>
<dd>Always do what the client asked. In a future release, it will be possible to force a check per principal.</dl>
<dt><code>encode_as_rep_as_tgs_rep = </code><i>boolean</i></p>
<dd>Encode AS-Rep as TGS-Rep to be bug-compatible with old DCE code. The Heimdal clients allow both.</p>
<dt><code>kdc_warn_pwexpire = </code><i>time</i></p>
<dd>How long before password/principal expiration the KDC should start sending out warning messages.</dl>
<p> The configuration file is only read when the is started. If changes made to the configuration file are to take effect, the needs to be restarted. </p>
<p> An example of a config file: </p>
<blockquote>
<pre>[kdc]
 require-preauth = no
 v4-realm = FOO.SE</pre>
</blockquote>
<h2>Bugs</h2>
<p>If the machine running the KDC has new addresses added to it, the KDC will have to be restarted to listen to them. The reason it doesn&#8217;t just listen to wildcarded (like INADDR_ANY) addresses, is that the replies has to come from the same address they were sent to, and most OS:es doesn&#8217;t pass this information to the application. If your normal mode of operation require that you add and remove addresses, the best option is probably to listen to a wildcarded TCP socket, and make sure your clients use TCP to connect. For instance, this will listen to IPv4 TCP port 88 only: </p>
<blockquote>
<pre>kdc --addresses=0.0.0.0 --ports=&quot;88/tcp&quot;</pre>
</blockquote>
<p> There should be a way to specify protocol, port, and address triplets, not just addresses and protocol, port tuples.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-kinit/">kinit</a>(1), krb5.conf5 </p>
