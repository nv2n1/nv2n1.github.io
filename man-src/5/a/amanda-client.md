---
title: "amanda-client(5)"
name: "amanda-client"
section: "5"
letter: "a"
url: "/docs/linux/man/5-amanda-client/"
description: "amanda-client.conf – Client configuration file for Amanda, the Advanced Maryland Automatic Network Disk Archiver"
---

<p>amanda-client.conf &#8211; Client configuration file for Amanda, the Advanced Maryland Automatic Network Disk Archiver</p>
<h2>Description</h2>
<p><i>amanda-client.conf</i> is the client configuration file for <i>Amanda</i>. This manpage lists the relevant sections and parameters of this file for quick reference. </p>
<p> The files <code>&lt;CONFIG_DIR&gt;/amanda-client.conf</code> and <code>&lt;CONFIG_DIR&gt;/&lt;config&gt;/amanda-client.conf</code> are loaded.</p>
<h2>Parameters</h2>
<p>There are a number of configuration parameters that control the behavior of the <i>Amanda</i> programs. All have default values, so you need not specify the parameter in <code>amanda-client.conf</code> if the default is suitable. </p>
<p> Lines starting with # are ignored, as are blank lines. Comments may be placed on a line with a directive by starting the comment with a #. The remainder of the line is ignored. </p>
<p> Keywords are case insensitive, i.e. <code>auth</code> and <code>Auth</code> are treated the same. </p>
<p> Integer arguments may have one of the following (case insensitive) suffixes, some of which have a multiplier effect:</p>
<h3>Possible Suffixes</h3>
<p><code>b byte bytes</code></p>
<dl>
<dd>Some number of bytes.</dl>
<p> <code>bps</code></p>
<dl>
<dd>Some number of bytes per second.</dl>
<p> <code>k kb kbyte kbytes kilobyte kilobytes</code></p>
<dl>
<dd>Some number of kilobytes (bytes*1024).</dl>
<p> <code>kps kbps</code></p>
<dl>
<dd>Some number of kilobytes per second (bytes*1024).</dl>
<p> <code>m mb meg mbyte mbytes megabyte megabytes</code></p>
<dl>
<dd>Some number of megabytes (bytes*1024*1024).</dl>
<p> <code>mps mbps</code></p>
<dl>
<dd>Some number of megabytes per second (bytes*1024*1024).</dl>
<p> <code>g gb gbyte gbytes gigabyte gigabytes</code></p>
<dl>
<dd>Some number of gigabytes (bytes*1024*1024*1024).</dl>
<p> <code>tape tapes</code></p>
<dl>
<dd>Some number of tapes.</dl>
<p> <code>day days</code></p>
<dl>
<dd>Some number of days.</dl>
<p> <code>week weeks</code></p>
<dl>
<dd>Some number of weeks (days*7). </p>
<p> Note The value <code>inf</code> may be used in most places where an integer is expected to mean an infinite amount. </p>
<p> Boolean arguments may have any of the values <code>y</code>, <code>yes</code>, <code>t</code>, <code>true</code> or <code>on</code> to indicate a true state, or <code>n</code>, <code>no</code>, <code>f</code>, <code>false</code> or <code>off</code> to indicate a false state. If no argument is given, <code>true</code> is assumed.</dl>
<h3>Parameters</h3>
<p><code>conf</code> <i> string</i></p>
<dl>
<dd>Default: <i>Set by configure</i>. The conf use by amrecover.</dl>
<p> <code>index_server</code> <i> string</i></p>
<dl>
<dd>Default: <i>Set by configure</i>. The amindexd server amrecover will connect to.</dl>
<p> <code>tape_server</code> <i> string</i></p>
<dl>
<dd>Default: <i>Set by configure</i>. The amidxtaped server amrecover will connect to.</dl>
<p> <code>tapedev</code> <i> string</i></p>
<dl>
<dd>Default: <i>Set by configure</i>. The tapedev amrecover will use.</dl>
<p> <code>auth</code> <i> string</i></p>
<dl>
<dd>Default: <i>bsd</i>. Type of authorization to perform between tape server and backup client hosts. </p>
<p> <code>bsd</code>, bsd authorization with udp initial connection and one tcp connection by data stream. </p>
<p> <code>bsdtcp</code>, bsd authorization but use only one tcp connection. </p>
<p> <code>bsdudp</code>, like bsd, but will use only one tcp connection for all data stream. </p>
<p> <code>krb4</code> to use Kerberos-IV authorization. </p>
<p> <code>krb5</code> to use Kerberos-V authorization. </p>
<p> <code>local</code>, if the client is the server, it doesn&#8217;t require authencation setup. </p>
<p> <code>rsh</code> to use rsh authorization. </p>
<p> <code>ssh</code> to use OpenSSH authorization.</dl>
<p> <code>ssh_keys</code> <i> string</i></p>
<dl>
<dd>Default: <i>No default</i>. The key file the ssh auth will use, it must be the private key. If this parameter is not specified, then the deafult ssh key will be used.</dl>
<p> <code>gnutar_list_dir</code> <i> string</i></p>
<dl>
<dd>Default from configure <i>&#8211;with-gnutar-listdir=DIR</i>. The directory where gnutar keep its state file.</dl>
<p> <code>amandates</code> <i> string</i></p>
<dl>
<dd>Default: <i>/etc/amandates</i>. The file where amanda keep the last date of each dumplevel.</dl>
<p> <code>connect_tries</code> int</p>
<dl>
<dd>Default: <i>3</i>. How many times the server will try a connection.</dl>
<p> <code>rep_tries</code> int</p>
<dl>
<dd>Default: <i>5</i>. How many times amandad will resend a REP packet if it doesn&#8217;t get the ACK packet.</dl>
<p> <code>debug_amandad</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the amandad process</dl>
<p> <code>debug_amidxtaped</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the amidxtaped process</dl>
<p> <code>debug_amindexd</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the amindexd process</dl>
<p> <code>debug_amrecover</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the amrecover process</dl>
<p> <code>debug_auth</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the auth module</dl>
<p> <code>debug_event</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the event module</dl>
<p> <code>debug_holding</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the holdingdisk module</dl>
<p> <code>debug_protocol</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the protocol module</dl>
<p> <code>debug_selfcheck</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the selfcheck process</dl>
<p> <code>debug_sendsize</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the sendsize process</dl>
<p> <code>debug_sendbackup</code> int</p>
<dl>
<dd>Default: <i>0</i>. Debug level of the sendbackup process</dl>
<p> <code>reserved-udp-port</code> int,int</p>
<dl>
<dd>Default: &#8211;with-udpportrange or <i>512,1023</i>. Reserved udp port that will be used (amrecover with bsd or bsdudp)</dl>
<p> <code>reserved-tcp-port</code> int,int</p>
<dl>
<dd>Default: &#8211;with-low-tcpportrange or <i>512,1023</i>. Reserved tcp port that will be used (amrecover with bsdtcp)</dl>
<p> <code>unreserved-tcp-port</code> int,int</p>
<dl>
<dd>Default: &#8211;with-tcpportrange or <i>1025,65536</i>. Unreserved tcp port that will be used (bsd, bsdudp)</dl>
<h2>Author</h2>
<p>James da Silva, &lt;jds [at] amanda.org&gt;: Original text </p>
<p> Stefan G. Weichinger, &lt;sgw [at] amanda.org&gt;, maintainer of the <i>Amanda</i>-documentation: XML-conversion, major update, splitting</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/8-amcrypt/">amcrypt</a></code>(8), <code><a href="/docs/linux/man/1-aespipe/">aespipe</a></code>(1), : <a rel="nofollow" href="http://wiki.zmanda.com">http://wiki.zmanda.com</a> </p>
