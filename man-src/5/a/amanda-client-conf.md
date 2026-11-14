---
title: "amanda-client-conf(5)"
name: "amanda-client-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-amanda-client-conf/"
description: "amanda-client.conf – Client configuration file for Amanda, the Advanced Maryland Automatic Network Disk Archiver"
---

<p>amanda-client.conf &#8211; Client configuration file for Amanda, the Advanced Maryland Automatic Network Disk Archiver</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5) is the client configuration file for Amanda. This manpage lists the relevant sections and parameters of this file for quick reference. </p>
<p> The files <code>&lt;CONFIG_DIR&gt;/amanda-client.conf</code> and <code>&lt;CONFIG_DIR&gt;/&lt;config&gt;/amanda-client.conf</code> are loaded.</p>
<h2>Syntax</h2>
<p>The syntax of <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5) is identical to that for <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5).</p>
<h2>Global Parameters</h2>
<p><code>conf</code> <i>string</i></p>
<dl>
<dd>Default: <i>Set by configure</i>. The conf use by amrecover.</dl>
<p> <code>client-username</code> <i>string</i></p>
<dl>
<dd>Default: <i>CLIENT_LOGIN</i>. Similar to the parameter of the same name in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), this specifies the username that <code>amrecover</code> should send when connecting to the server. It should match the username specified in .amandahosts on the server.</dl>
<p> <code>client-port</code> [ <i>int</i> | <i>string</i> ]</p>
<dl>
<dd>Default: <i>&quot;amanda&quot;</i>. Similar to the parameter of the same name in <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), this specifies the port to connect on the server. It can be a service name or a numeric port number.</dl>
<p> <code>amdump-server</code> <i>string</i></p>
<dl>
<dd>No default: <i>Set by configure</i>. The amanda server to connect with the amdump_client program.</dl>
<p> <code>index-server</code> <i>string</i></p>
<dl>
<dd>Default: <i>Set by configure</i>. The amindexd server amrecover will connect to.</dl>
<p> <code>tape-server</code> <i>string</i></p>
<dl>
<dd>Default: <i>Set by configure</i>. The amidxtaped server amrecover will connect to.</dl>
<p> <code>tapedev</code> <i>string</i></p>
<dl>
<dd>Default: <i>Set by configure</i>. The tapedev amrecover will use.</dl>
<p> <code>auth</code> <i>string</i></p>
<dl>
<dd>Default: <code>&quot;bsdtcp&quot;</code>. Type of authorization to perform between tape server and backup client hosts. </p>
<p> <code>&quot;bsd&quot;</code>, bsd authorization with udp initial connection and one tcp connection by data stream. </p>
<p> <code>&quot;bsdtcp&quot;</code>, bsd authorization but use only one tcp connection. </p>
<p> <code>&quot;bsdudp&quot;</code>, like bsd, but will use only one tcp connection for all data stream. </p>
<p> <code>&quot;krb5&quot;</code> to use Kerberos-V authorization. </p>
<p> <code>&quot;local&quot;</code>, if the client is the server, it doesn&#8217;t require authencation setup. </p>
<p> <code>&quot;rsh&quot;</code> to use rsh authorization. </p>
<p> <code>&quot;ssh&quot;</code> to use OpenSSH authorization.</dl>
<p> <code>ssh-keys</code> <i>string</i></p>
<dl>
<dd>Default: <i>No default</i>. The key file the ssh auth will use, it must be the private key. If this parameter is not specified, then the default ssh key will be used.</dl>
<p> <code>gnutar-list-dir</code> <i>string</i></p>
<dl>
<dd>Default from configure <i>&#8211;with-gnutar-listdir=DIR</i>. The directory where gnutar keep its state file.</dl>
<p> <code>mailer</code> <i>string</i></p>
<dl>
<dd>Default found by configure. A mail program that can send mail with &#8216;<i>MAILER -s &quot;subject&quot; user &lt; message_file</i>&#8216;.</dl>
<p> <code>amandates</code> <i>string</i></p>
<dl>
<dd>Default: <i>/etc/amandates</i>. The file where amanda keep the last date of each dumplevel.</dl>
<p> <code>connect-tries</code> <i>int</i></p>
<dl>
<dd>Default: <i>3</i>. How many times the server will try a connection.</dl>
<p> <code>rep-tries</code> <i>int</i></p>
<dl>
<dd>Default: <i>5</i>. How many times amandad will resend a REP packet if it doesn&#8217;t get the ACK packet.</dl>
<p> <code>debug-days</code> <i>int</i></p>
<dl>
<dd>Default: <i>3</i>. The number of days the debug files are kept.</dl>
<p> <code>debug-amandad</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the amandad process</dl>
<p> <code>debug-amidxtaped</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the amidxtaped process</dl>
<p> <code>debug-amindexd</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the amindexd process</dl>
<p> <code>debug-amrecover</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the amrecover process</dl>
<p> <code>debug-auth</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the auth module</dl>
<p> <code>debug-event</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the event module</dl>
<p> <code>debug-holding</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the holdingdisk module</dl>
<p> <code>debug-protocol</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the protocol module</dl>
<p> <code>debug-selfcheck</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the selfcheck process</dl>
<p> <code>debug-sendsize</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the sendsize process</dl>
<p> <code>debug-sendbackup</code> <i>int</i></p>
<dl>
<dd>Default: <i>0</i>. Debug level of the sendbackup process</dl>
<p> <code>reserved-udp-port</code> <i>int</i>,<i>int</i></p>
<dl>
<dd>Default: &#8211;with-udpportrange or <i>512,1023</i>. Reserved udp port that will be used (amrecover with bsd or bsdudp)</dl>
<p> <code>reserved-tcp-port</code> <i>int</i>,<i>int</i></p>
<dl>
<dd>Default: &#8211;with-low-tcpportrange or <i>512,1023</i>. Reserved tcp port that will be used (amrecover with bsdtcp)</dl>
<p> <code>unreserved-tcp-port</code> <i>int</i>,<i>int</i></p>
<dl>
<dd>Default: &#8211;with-tcpportrange or <i>1025,65536</i>. Unreserved tcp port that will be used (bsd, bsdudp)</dl>
<p> <code>property</code> <i>string</i> <i>string</i>+</p>
<dl>
<dd>Adds a global property for this client host, useful for e.g., Application API plugins. The first string is the property name, the following strings are the property values</dl>
<h2>Application Section</h2>
<p>The <code>amanda-client.conf</code> file may define multiple types of application. The information is entered in a <code>application</code> section, which looks like this: </p>
<pre>define application &quot;<i>name</i>&quot; {
 <i>application-option</i> <i>application-value</i>
 ...
}</pre>
<p><i>name</i> is the name of this type of application. </p>
<p> The setting from an application is merged with the dle setting if the <i>name</i> is the same as the <code>client-application-name</code> from the dle or if the <code>client-application-name</code> from the dle is not set and the <i>name</i> is the same as the <code>plugin</code> from the dle. </p>
<p> The application options and values are: </p>
<p> <code>client-application-name</code> <i>string</i></p>
<dl>
<dd>Default: <i>none</i>. Not use on the client.</dl>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: <i>none</i>. A comment string describing this application.</dl>
<p> <code>plugin</code> <i>string</i></p>
<dl>
<dd>No default. Must be set to the name of the program. This program must be in the <i>$libexecdir/amanda/application</i> directory on the client. If set, it must be the same as the dle <code>plugin</code>.</dl>
<p> <code>property</code> [<code>append</code>] [<code>priority</code>] <i>string</i> <i>string</i>+</p>
<dl>
<dd>No default. You can set property for the application, each application have a different set of property. Both strings are quoted; the first string contains the name of the property to set, and the others contains its values. <code>append</code> keyword append the values to the list of values for that property. <code>priority</code> keyword disallow the setting of that property on the server.</dl>
<h2>Script Section</h2>
<p>The <code>amanda-client.conf</code> file may define multiple types of script. The information is entered in a <code>script</code> section, which looks like this: </p>
<pre>define script &quot;<i>name</i>&quot; {
 <i>script-option</i> <i>script-value</i>
 ...
}</pre>
<p><i>name</i> is the name of this type of script. </p>
<p> The setting from a script is merged with the dle setting if the <i>name</i> is the same as the <code>client-script-name</code> from the dle or if the <code>client-script-name</code> from the dle is not set and the <i>name</i> is the same as the <code>plugin</code> from the dle. </p>
<p> The script options and values are: </p>
<p> <code>client-script-name</code> <i>string</i></p>
<dl>
<dd>Default: <i>none</i>. Not used on the client.</dl>
<p> <code>comment</code> <i>string</i></p>
<dl>
<dd>Default: <i>none</i>. A comment string describing this script.</dl>
<p> <code>plugin</code> <i>string</i></p>
<dl>
<dd>No default. Must be set to the name of the program. This program must be in the <i>$libdir/amanda/application</i> directory on the client. If set, it must be the same as the dle <code>plugin</code>.</dl>
<p> <code>execute-where</code> <code>client</code></p>
<dl>
<dd>Default: <code>client</code>. Value can&#8217;t be changed.</dl>
<p> <code>execute-on</code> <i>execute_on</i>[,<i>execute_on</i>]*</p>
<dl>
<dd>No default. When the script must be executed, you can specify many of them: </p>
<p> <code>pre-dle-amcheck</code></p>
<dl>
<dd>Execute before the amcheck command for the dle.</dl>
<p> <code>pre-host-amcheck</code></p>
<dl>
<dd>Execute before the amcheck command for all dle for the client.</dl>
<p> <code>post-dle-amcheck</code></p>
<dl>
<dd>Execute after the amcheck command for the dle.</dl>
<p> <code>post-host-amcheck</code></p>
<dl>
<dd>Execute after the amcheck command for all dle for the client.</dl>
<p> <code>pre-dle-estimate</code></p>
<dl>
<dd>Execute before the estimate command for the dle.</dl>
<p> <code>pre-host-estimate</code></p>
<dl>
<dd>Execute before the estimate command for all dle for the client.</dl>
<p> <code>post-dle-estimate</code></p>
<dl>
<dd>Execute after the estimate command for the dle.</dl>
<p> <code>post-host-estimate</code></p>
<dl>
<dd>Execute after the estimate command for all dle for the client.</dl>
<p> <code>pre-dle-backup</code></p>
<dl>
<dd>Execute before the backup command for the dle.</dl>
<p> <code>post-dle-backup</code></p>
<dl>
<dd>Execute after the backup command for the dle.</dl>
<p> <code>pre-recover</code></p>
<dl>
<dd>Execute before any level is recovered.</dl>
<p> <code>post-recover</code></p>
<dl>
<dd>Execute after all levels are recovered.</dl>
<p> <code>pre-level-recover</code></p>
<dl>
<dd>Execute before each level recovery.</dl>
<p> <code>post-level-recover</code></p>
<dl>
<dd>Execute after each level recovery.</dl>
<p> <code>inter-level-recover</code></p>
<dl>
<dd>Execute between two levels of recovery.</dl>
</dl>
<p> <code>property</code> [<code>append</code>] [<code>priority</code>] <i>string</i> <i>string</i>+</p>
<dl>
<dd>No default. You can set property for the script, each script have a different set of property. Both strings are quoted; the first string contains the name of the property to set, and the others contains its values. <code>append</code> keyword append the values to the list of values for that property. <code>priority</code> keyword disallow the setting of that property on the server.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/8-amcrypt/">amcrypt</a></code>(8), <code><a href="/docs/linux/man/1-aespipe/">aespipe</a></code>(1) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
