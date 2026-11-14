---
title: "amanda-auth(7)"
name: "amanda-auth"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-auth/"
description: "amanda-auth – Communication/Authentication methods between Amanda server and client"
---

<p>amanda-auth &#8211; Communication/Authentication methods between Amanda server and client</p>
<h2>Description</h2>
<p>Amanda offers 7 methods of communication between Amanda server (sometimes also called the tape server) and clients, each with its own authentication method. The desired communication method is specified by the <i>auth</i> parameter in the amanda.conf file (<code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5)) commonly as a dumptype. Valid values to the <i>auth</i> parameter are <code>bsd</code>, <code>bsdudp</code>, <code>bsdtcp</code>, <code>krb5</code>, <code>local</code>, <code>rsh</code>, and <code>ssh</code>. The authentication and communication method is used during the backup process <code>amdump</code> (<a href="/docs/linux/man/8-amdump/">amdump</a>(8)) as well as the recovery process <code>amrecover</code> (<a href="/docs/linux/man/8-amrecover/">amrecover</a>(8)).</p>
<h2>Compilation And General Information</h2>
<p>The communication method and thus type of authentication that will be used by the Amanda server is specified by the <i>auth</i> parameter in the dumptype for each disklist entry (DLE). The <i>auth</i> parameter thus may be easily and globally specified in the &quot;global&quot; dumptype. If <i>auth</i> is not specified, the <code>bsdtcp</code> communication method is used. See <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) for more information on Amanda configuration and dumptypes, and <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5) for more information on disklists. </p>
<p> On the client side, the Amanda daemon <code>amandad</code> validates the connection depending on the value of the <code>auth</code> argument passed to it (see <a href="/docs/linux/man/8-amanda/">Amanda</a>(8)). Also, when it comes to recovery, the <code>auth</code> parameter can be specified in the <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5) file to specify the communication method to be used by the client to the server. </p>
<p> When Amanda is being built from source code, desired communication and thus authentication methods (shown as &quot;Authentication&quot;) must be specified as configure options at compilation time. </p>
<pre>Authentication Configure option(s)
 bsd --with-bsd-security --with-amandahosts (pre-2.6)
 bsdtcp --with-bsdtcp-security --with-amandahosts (pre-2.6)
 bsdudp --with-bsdudp-security --with-amandahosts (pre-2.6)
 krb5 --with-krb5-security
 local (always included)
 rsh --with-rsh-security
 ssh --with-ssh-security</pre>
<p>There are additional configure options for <code>bsd</code>, <code>bsdudp</code>, and <code>bsdtcp</code> to allow for specifying explicit UDP and TCP port ranges. </p>
<pre> --with-udpportrange
 --with-tcpportrange
 --with-low-tcpportrange</pre>
<p>See <code>PORT USAGE</code> below for more information. </p>
<p> There are additional configure options for Kerberos if you so desire. All but the last option are for Kerberos 4. Defaults shown in square brackets. </p>
<pre> --with-server-principal=ARG server host principal [amanda]
 --with-server-instance=ARG server host instance []
 --with-server-keyfile=ARG server host key file [/.amanda]
 --with-client-principal=ARG client host principal [rcmd]
 --with-client-instance=ARG client host instance [HOSTNAME_INSTANCE]
 --with-client-keyfile=ARG client host key file [KEYFILE]
 --with-ticket-lifetime=ARG ticket lifetime [128]
 --with-krb5-security=DIR where libkrb.a lives [see below]</pre>
<p>If configuring with &#8211;with-krb5-security, the configure script will search under /usr/kerberos/lib, /usr/cygnus/lib, /usr/lib, and /opt/kerberos/lib for the kerberos bits, libkrb.a, in this order. Kerberos support will not be added if it does not find them. If the kerberos bits are found under some other hierarchy, you can specify this via &#8211;with-krb5-security=DIR where DIR is where the kerberos bits live. The configure script will then look in the &#8216;lib&#8217; directory under this hierarchy for libkrb.a. </p>
<p> The <code>auth</code> parameter selects a communication/authentication method to use between the client and the backup server. These methods are described each in their own section below.</p>
<h3>Usernames</h3>
<p>When Amanda is built, a username is specified with the <code>&#8211;with-user</code> option. Most Amanda processes run under this user&#8217;s identity, to minimize security risks. In binary distributions, this username is usually one of &#8216;amanda&#8217;, &#8216;amandabackup&#8217;, or &#8216;backup&#8217;. The examples below use &#8216;amandabackup&#8217; since it is unambiguous. You may need to adjust accordingly for your system.</p>
<h3>Authenticated Peer Hostnames</h3>
<p>Amanda&#8217;s authentication mechanisms provide an authenticated hostname of the system on the other end of the connection, which is used to restrict access to only particular hosts. The degree of &quot;authentication&quot; performed on this hostname varies with the authentication mechanism, and is discussed below.</p>
<h2>Bsd, Bsdudp, And Bsdtcp Communication And Authentication</h2>
<p>For additional information including example configurations, see <a rel="nofollow" href="http://wiki.zmanda.com/index.php/Configuring_bsd/bsdudp/bsdtcp_authentication.">http://wiki.zmanda.com/index.php/Configuring_bsd/bsdudp/bsdtcp_authentication.</a> </p>
<p> The <code>bsd</code>, <code>bsdudp</code>, and <code>bsdtcp</code> communication methods use either UDP, TCP, or both protocols operating as a network service to authenticate and exchange data between server and clients. </p>
<p> The authentication proceeds as follows: for a new, incoming connection, Amanda verifies that the source port is in the reserved range (less than 1024), which for UNIX hosts suggests that the remote user has root privileges. Amanda then verifies that the reverse DNS for the remote address matches the forward DNS; that is, that the address maps to a hostname which maps back to the same address. Finally, the remote system must provide a username that matches the username in .amandahosts. </p>
<p> In addition to compilation and general configuration (see <code>COMPILATION AND GENERAL INFORMATION</code> above), the authentication method that the client is configured to receive is specified by the <code>auth</code> parameter in the network service configuration for Amanda. The authentication method used by an Amanda client to reach the server during recovery is the authentication method specified by the <i>auth</i> parameter in the client&#8217;s Amanda network service configuration or in its amanda-client.conf file (see <a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a>(5)). </p>
<p> By default, Amanda use the &quot;amanda&quot; service name and associated port set in /etc/services. It can be changed by setting the dumptype <i>client-port</i> option to a different port number or a different service name. All examples are for the service name &quot;amanda&quot; that uses the default port 10080.</p>
<h3>.amandahosts file</h3>
<p>Servers and clients using the bsd, bsdudp, and bsdtcp authentication methods refer to the .amandahosts file to control access. Amanda should be compiled for this access control if one of these methods will be used and is the default compilation option for Amanda 2.6 (use &#8211;with-amandahosts when compiling pre-2.6 versions of Amanda). </p>
<p> Amanda looks for the .amandahosts file in the Amanda user&#8217;s home directory, commonly /var/lib/amanda. </p>
<p> Each authorization is on its own line in the following format </p>
<p> <i>hostname</i> [ <i>username</i> [ <i>service&#8230;</i> ] ] </p>
<p> If <i>username</i> is ommitted, it defaults to the user running <code>amandad</code>, i.e. the user listed in the <code>inetd</code> or <code>xinetd</code> configuration file. </p>
<p> <i>service&#8230;</i> is a space-delimited list of services the client is authorized to execute: <code>noop</code>, <code>selfcheck</code>, <code>sendsize</code>, <code>sendbackup</code>, <code>amdump</code> (a shortcut for the previous four services which are required on clients), <code>amindexd</code>, and <code>amidxtaped</code>. The last two services are required on a server for clients to connect to it using <code>amrecover</code>. </p>
<p> If service is omitted, it defaults to <code>noop selfcheck sendsize sendbackup</code> (which is equivalent to <code>amdump</code>). </p>
<p> Example of the .amandahosts file on an Amanda client, where &#8216;amandabackup&#8217; is the Amanda dumpuser. </p>
<pre> <code>amandaserver.example.com amandabackup amdump</code></pre>
<p>Example of the .amandahosts file on an Amanda server </p>
<pre> <code>amandaclient1.example.com root amindexd amidxtaped</code></pre>
<h3>bsd communication and authentication</h3>
<p>The authentication is done using .amandahosts file in the Amanda user&#8217;s home directory. The protocol between Amanda server and client is UDP. The number of disk list entries (DLEs)&#8211;number of Amanda clients&#8211;is limited by the UDP packet size. This authentication protocol will use a different port for each data stream (see PORT USAGE below)</p>
<h3>bsdudp communication and authentication</h3>
<p>The authentication is done using .amandahosts files in the Amanda user&#8217;s home directory. It uses UDP protocol between Amanda server and client for data and hence the number of DLEs is limited by the UDP packet size. It uses one TCP port to establish the connection and multiplexes all data streams using one port on the server (see PORT USAGE below).</p>
<h3>bsdtcp communication and authentication</h3>
<p>The authentication is done using .amandahosts files in the backup user&#8217;s (for example: amandabackup) home directory. It uses TCP protocol between Amanda server and client. On the client, two reserved ports are used. On the server, all data streams are multiplexed to one port (see PORT USAGE below).</p>
<h3>Using Inetd Server</h3>
<p>Template for Amanda client inetd service entry </p>
<pre><i> service_name</i> <i>socket_type</i> <i>protocol</i> <i>wait/nowait</i> <i>amanda_backup_user</i> <i>absolute_path_to_amandad</i> amandad <i>server_args</i></pre>
<p>Client example of using <code>bsd</code> authorization for inetd server given Amanda user is &quot;amandabackup&quot;: </p>
<pre><code> amanda dgram udp wait amandabackup /path/to/amandad amandad -auth=bsd amdump</code></pre>
<p>The same could be used for <code>bsdudp</code> if specifying -auth=bsdudp instead of -auth=bsd. </p>
<p> Client example of using <code>bsdtcp</code> authorization for inetd server given Amanda user is &quot;amandabackup&quot;: </p>
<pre><code> amanda stream tcp nowait amandabackup /path/to/amandad amandad -auth=bsdtcp amdump</code></pre>
<p><code>amindexd</code> and <code>amidxtaped</code> would typically be added at the end of the line as <code>amandad</code> server arguments for an Amanda server. </p>
<p> Server example of using <code>bsdtcp</code> authorization for inetd server given Amanda user is &quot;amandabackup&quot;: </p>
<pre><code> amanda stream tcp nowait amandabackup /path/to/amandad amandad -auth=bsdtcp amdump amindexd amidxtaped</code></pre>
<p>For Amanda version 2.5.0 and earlier, remember that neither <code>bsdudp</code> nor <code>bsdtcp</code> are supported and the Amanda daemon <code>amandad</code> accepts no arguments. Because of the latter, <code>amrecover</code> as of Amanda version 2.5.1 is not compatible with 2.5.0 and earlier servers. Thus, servers that are 2.5.0 or earlier must, in addition to the <i>amanda</i> service, run <i>amindexd</i> and <i>amidxtaped</i> Amanda services as their own network services, amandaidx and amidxtape, respectively (see below). </p>
<p> There are no compatibility issues if server and clients are all 2.5.0 or earlier. If your server is 2.5.1 or later, you can still have clients that are 2.5.0 and earlier although you must then use <code>bsd</code> communication/authentication with these clients and must also run <i>amindexd</i> and <i>amidxtaped</i> Amanda services on the server as their own network services, amandaidx and amidxtape, respectively (see below). If you have a server that is 2.5.0 and earlier, clients of a later version on which you wish to run <code>amrecover</code> must use <code>amoldrecover</code> instead and, again, the server must be running the amandaidx and amidxtape network services. </p>
<p> Example of amindexd and amidxtaped Amanda daemon services configured as their own network services for a 2.5.0 or earlier server or a newer server having 2.5.0 or earlier clients </p>
<pre><code> amandaidx stream tcp nowait amandabackup /usr/local/libexec/amanda/current/amindexd amindexd</code>
<code> amidxtape stream tcp nowait amandabackup /usr/local/libexec/amanda/current/amidxtaped amidxtaped</code></pre>
<h3>Using Xinetd Server</h3>
<p>Template for Amanda client xinetd service file </p>
<pre>service amanda
{
 only_from = <i>Amanda server</i>
 socket_type = <i>socket type</i>
 protocol = <i>protocol</i>
 wait = <i>yes/no</i>
 user = <i>amanda backup user</i>
 group = <i>amanda backup user group id</i>
 groups = yes
 server = <i>absolute path to amandad</i>
 server_args = <i>amandad server arguments</i>
 disable = no
}</pre>
<p>The <i>only_from</i> parameter can be used with xinetd but is usually in addition to the primary form of access control via the .amandahosts file. </p>
<p> Client example of using <code>bsd</code> authorization for xinetd server and for Amanda user &quot;amandabackup&quot;: </p>
<pre>service amanda
{
 only_from = amandaserver.example.com
 socket_type = dgram
 protocol = udp
 wait = yes
 user = amandabackup
 group = disk
 groups = yes
 server = /path/to/amandad
 server_args = -auth=bsd amdump
 disable = no 
}</pre>
<p>The same could be used for <code>bsdudp</code> if specifying -auth=bsdudp instead of -auth=bsd. </p>
<p> Client example of using <code>bsdtcp</code> authorization for xinetd server and for Amanda user &quot;amandabackup&quot;: </p>
<pre>service amanda
{
 only_from = amandaserver.example.com amandaclient.example.com
 socket_type = stream
 protocol = tcp
 wait = no
 user = amandabackup
 group = disk
 groups = yes
 server = /path/to/amandad
 server_args = -auth=bsdtcp amdump
 disable = no 
}</pre>
<p><code>amindexd</code> and <code>amidxtaped</code> would typically be added as additional <code>amandad</code> <i>server_args</i> for an Amanda server. </p>
<p> For Amanda version 2.5.0 and earlier, remember that neither <code>bsdudp</code> nor <code>bsdtcp</code> are supported and the Amanda daemon <code>amandad</code> accepts no arguments. Because of the latter, <code>amrecover</code> as of Amanda version 2.5.1 is not compatible with 2.5.0 and earlier servers. Thus, servers that are 2.5.0 or earlier must, in addition to the <i>amanda</i> service, run <i>amindexd</i> and <i>amidxtaped</i> Amanda services as their own network services, amandaidx and amidxtape, respectively (see below). </p>
<p> There are no compatibility issues if server and clients are all 2.5.0 or earlier. If your server is 2.5.1 or later, you can still have clients that are 2.5.0 and earlier although you must then use <code>bsd</code> communication/authentication with these clients and must also run <i>amindexd</i> and <i>amidxtaped</i> Amanda services on the server as their own network services, amandaidx and amidxtape, respectively (see below). If you have a server that is 2.5.0 and earlier, clients of a later version on which you wish to run <code>amrecover</code> must use <code>amoldrecover</code> instead and, again, the server must be running the amandaidx and amidxtape network services. </p>
<p> Example of amindexd and amidxtaped Amanda daemon services configured as their own network services for a 2.5.0 or earlier server or a newer server having 2.5.0 or earlier clients </p>
<pre>service amandaidx
{
 socket_type = stream
 protocol = tcp
 wait = no
 user = amanda
 group = disk
 server = /usr/local/libexec/amanda/amindexd 
 disable = no
}
service amidxtape
{
 socket_type = stream
 protocol = tcp
 wait = no
 user = amanda
 group = disk
 server = /usr/local/libexec/amanda/amidxtaped
 disable = no
}</pre>
<h3>Port Usage</h3>
<p>List of TCP/UDP ports used by network service communication methods for Amanda server and client. </p>
<pre> Key:
 UP = Unreserved Port
 RPpAP = Reserved Port per Amanda Process
 UPpDLE = Unreserved Port per DLE
 [..] = Configure options that can be used at compile time to define port ranges
Authentication Protocol Amanda server Amanda client
bsd udp 1 RPpAP [--with-udpportrange] 10080
 tcp 1 UP [--with-tcpportrange] 3 UPpDLE [--with-tcpportrange]
bsdudp udp 1 RPpAP [--with-udpportrange] 10080
 tcp 1 UP [-with-tcpportrange] 1 UPpDLE [--with-tcpportrange]
bsdtcp tcp 1 RPpAP [--with-low-tcpportrange] 10080</pre>
<p>Amanda server also uses two ports (dumper process) to communicate with the chunker/taper processes. These ports are in the range set by &#8211;with-tcpportrange. </p>
<p> You can override the default port ranges that Amanda was compiled with in each configuration using the <i>reserved-udp-port</i>, <i>reserved-tcp-port</i>, and <i>unreserved-tcp-port</i> parameters in amanda.conf and amanda-client.conf configuration files (see <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5) and <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5)).</p>
<h3>Authenticated Peer Hostnames with BSD Authentications</h3>
<p>The BSD authentication mechanisms only verify that the remote host&#8217;s DNS is configured correctly and that the remote user has access to reserved ports. As such, the peer hostname should only be trusted to the extent that the local DNS service is trusted.</p>
<h2>Kerberos Communication And Authentication</h2>
<p>For more detail, see <a rel="nofollow" href="http://wiki.zmanda.com/index.php/Kerberos_authentication.">http://wiki.zmanda.com/index.php/Kerberos_authentication.</a> </p>
<p> Amanda supports Kerberos 5 communication methods between Amanda server and client. </p>
<p> General information including compilation are given above (see <code>COMPILATION AND GENERAL INFORMATION</code> above). </p>
<p> Kerberos 5 uses TCP and the server uses only one TCP port and data streams are multiplexed to this port. </p>
<p> The <code>krb5</code> driver script defaults to: </p>
<pre>/*
 * The lifetime of our tickets in minutes.
 */
#define AMANDA_TKT_LIFETIME (12*60)
/*
 * The name of the service in /etc/services.
 */
#define AMANDA_KRB5_SERVICE_NAME &quot;k5amanda&quot;</pre>
<p>You can currently only override these by editing the source code. </p>
<p> The kerberized AMANDA service uses a different port on the client hosts. The /etc/services line is: </p>
<pre> k5amanda 10082/tcp</pre>
<p>And the /etc/inetd.conf line is: </p>
<pre> k5amanda stream tcp nowait root /usr/local/libexec/amanda/amandad amandad -auth=krb5</pre>
<p>Note that you&#8217;re running this as root, rather than as your dump user. AMANDA will set its UID down to the dump user at times it doesn&#8217;t need to read the keytab file, and give up root permissions entirely before it goes off and runs dump. Alternately you can change your keytab files to be readable by user amanda. You should understand the security implications of this before changing the permissions on the keytab. </p>
<p> The following dumptype options apply to <code>krb5</code>: </p>
<pre> auth &quot;krb5&quot; # use krb5 auth for this host
 # (you can mingle krb hosts and bsd .rhosts in one conf)</pre>
<p>The principal and keytab files that Amanda uses must be set in the amanda.conf file for kerberos 5 dumps to work. You can hardcode this in the source code if you really want to (common-src/krb5-security.c) </p>
<pre> krb5keytab
 krb5principal</pre>
<p>For example: </p>
<pre> krb5keytab &quot;/etc/krb5.keytab-amanda&quot;
 krb5principal &quot;amanda/saidin.omniscient.com&quot;</pre>
<p>The principal in the second option must be contained in the first. The keytab should be readable by the amanda user (and definitely not world readable!) and is (obviously) on the server. In MIT&#8217;s kadmin, the following: </p>
<pre> addprinc -randkey amanda/saidin.omniscient.com
 ktadd -k /etc/krb5.keytab-amanda amanda/saidin.omniscient.com</pre>
<p>will do the trick. You will obviously want to change the principal name to reflect something appropriate for the conventions at your site. </p>
<p> You must also configure each client to allow the amanda principal in for dumps. </p>
<p> There are several ways to go about authorizing a server to connect to a client. </p>
<p> The normal way is via a .k5amandausers file or a .k5login file in the client user&#8217;s home directory. The determination of which file to use is based on the way you ran configure on AMANDA. By default, AMANDA will use .k5amandahosts, but if you configured with &#8211;without-amandahosts, AMANDA will use .k5login. (similar to the default for .rhosts/.amandahosts-style security). The .k5login file syntax is a superset of the default <code>krb5</code> .k5login. The routines to check it are implemented in amanda rather than using krb5_kuserok because the connections are actually gssapi based. </p>
<p> This .k5amandahosts/.k5login is a hybrid of the .amandahosts and a .k5login file. You can just list principal names, as in a .k5login file and the principal will be permitted in from any host. If you do NOT specify a realm, then there is no attempt to validate the realm (this is only really a concern if you have cross-realm authentication set up with another realm or something else that allows you multiple realms in your kdc. If you do specify a realm, only that principal [at] realm will be permitted to connect. </p>
<p> You may prepend this with a hostname and whitespace, and only that principal (with optional realm as above) will be permitted to access from that hostname. </p>
<p> Here are examples of valid entries in the .k5amandahosts: </p>
<pre> service/amanda
 service/amanda [at] TEST.COM
 dumpmaster.test.com service/amanda
 dumpmaster.test.com service/amanda [at] TEST.COM</pre>
<p>Rather than using a .k5amandahosts or .k5login file, the easiest way is to use a principal named after the destination user, (such as amanda [at] TEST.COM in our example) and not have either a .k5amandahosts or .k5login file in the destination user&#8217;s home directory. </p>
<p> There is no attempt to verify the realm in this case (only a concern if you have cross-realm authentication setup).</p>
<h3>Authenticated Peer Hostnames with Kerberos Authentication</h3>
<p>When accepting a new incoming connection, the Kerberos authentication mechanism performs a similar check to that done by the BSD authentications: the forward and reverse DNS entries for the remote host must match. As such, while Kerberos authentication can cryptographically ensure that the remote system is recognized (since it has a ticket), its assurances about the remote host&#8217;s identity are weaker and depend on the integrity of the DNS.</p>
<h2>Local Communication</h2>
<p>The Amanda server communicates with the client internally versus over the network, ie. the client is also the server. </p>
<p> This is the only method that requires no authentication as it is clearly not needed. </p>
<p> The authenticated peer hostname for this authentication is always &quot;localhost&quot;.</p>
<h2>Rsh Communication And Authentication</h2>
<p>For more detail, see <a rel="nofollow" href="http://wiki.zmanda.com/index.php/Configuring_rsh_authentication.">http://wiki.zmanda.com/index.php/Configuring_rsh_authentication.</a> </p>
<p> The Amanda server communicates with its client as the Amanda user via the RSH protocol. </p>
<p> Please note that RSH protocol itself is insecure and should be used with caution especially on any servers and clients with public IPs. </p>
<p> Each Amanda client communicates with the server using one TCP port and all data streams from the client are multiplexed over one port. The number of Amanda clients is limited by the number of reserved ports available on the Amanda server. Some versions of RSH do not use reserved ports and, thus, this restriction is not valid. </p>
<p> General information including compilation is given above (see <code>COMPILATION AND GENERAL INFORMATION</code> above). </p>
<p> In addition to specifying the <i>auth</i> field in dumptype definition, it might be required to specify <i>client-username</i> and <code>amandad</code> fields. If the backup user name is different on the Amanda client, the user name is specified as <code>client-username</code>. If the location of the Amanda daemon <code>amandad</code> is different on the Amanda client, the location is specified as <i>amandad-path</i> field value. </p>
<pre>For example:
define dumptype rsh_example {
 ...
 auth &quot;rsh&quot;
 client-username &quot;amandabackup&quot;
 amandad-path &quot;/usr/lib/exec/amandad&quot;
 ...
}</pre>
<h3>Authenticated Peer Hostnames with RSH Authentication</h3>
<p>The RSH authentication mechanism does not provide an authenticated peer hostname.</p>
<h2>Ssh Communication And Authentication</h2>
<p>For more detail, see <a rel="nofollow" href="http://wiki.zmanda.com/index.php/How_To:Set_up_transport_encryption_with_SSH.">http://wiki.zmanda.com/index.php/How_To:Set_up_transport_encryption_with_SSH.</a> </p>
<p> Amanda client sends data to the server using SSH. SSH keys have to be set up so that Amanda server can communicate with its clients using SSH. </p>
<p> General information including compilation is given above (see <code>COMPILATION AND GENERAL INFORMATION</code> above). </p>
<p> SSH provides transport encryption and authentication. To set up an SSH authentication session, Amanda will run the equivalent of the following to start the backup process. </p>
<p> <code> /path/to/ssh -l </code><i>user_name</i><code> client.zmanda.com $libexecdir/amandad</code> </p>
<p> To use SSH, you need to set up SSH keys either by storing the passphrase in cleartext, using ssh-agent, or using no passphrase at all. All of these options have security implications which should be carefully considered before adoption. </p>
<p> When you use a public key on the client to do data encryption (see <a rel="nofollow" href="http://wiki.zmanda.com/index.php/How_To:Set_up_data_encryption">http://wiki.zmanda.com/index.php/How_To:Set_up_data_encryption</a>), you can lock away the private key in a secure place. Both, transport and storage will be encrypted with such a setup. See <a href="http://wiki.zmanda.com/index.php/Encryption">http://wiki.zmanda.com/index.php/Encryption</a> for an overview of encryption options. </p>
<p> Enable SSH authentication and set the <code>ssh-keys</code> option in all DLEs for that host by adding the following to the DLE itself or to the corresponding dumptype in amanda.conf: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>auth&nbsp;<wbr>&quot;ssh&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>ssh-keys&nbsp;<wbr>&quot;/home/amandabackup/.ssh/id_rsa_amdump&quot; </p>
<p> <code>ssh-keys</code> is the path to the private key on the client. If the username to which Amanda should connect is different from the default, then you should also add </p>
<p>&nbsp;<wbr>&nbsp;<wbr>client-username&nbsp;<wbr>&quot;otherusername&quot; </p>
<p> If your server <code>amandad</code> path and client <code>amandad</code> path are different, you should also add </p>
<p>&nbsp;<wbr>&nbsp;<wbr>amandad-path&nbsp;<wbr>&quot;/client/amandad/path&quot; </p>
<p> For a marginal increase in security, prepend the keys used for AMANDA in the clients&#8217; authorized_keys file with the following: </p>
<pre> from=&quot;amanda_server.your.domain.com&quot;,no-port-forwarding,no-X11-forwarding,no-agent-forwarding,command=&quot;/absolute/path/to/amandad -auth=ssh amdump&quot;</pre>
<p>This will limit that key to connect only from Amanda server and only be able to execute <code><a href="/docs/linux/man/8-amandad/">amandad</a></code>(8). </p>
<p> In the same way, prepend the key used for AMANDA in the server&#8217;s authorized_keys file with: </p>
<pre> from=&quot;amanda_client.your.domain.com&quot;,no-port-forwarding,no-X11-forwarding,no-agent-forwarding,command=&quot;/absolute/path/to/amandad -auth=ssh amindexd amidxtaped&quot;</pre>
<p>You can omit the from=.. option if you have too many clients to list, although this has obvious security implications. </p>
<p> Set <code>ssh-keys</code> and any other necessary options in /etc/amanda/amanda_client.conf: </p>
<pre> auth &quot;ssh&quot;
 ssh-keys &quot;/root/.ssh/id_rsa_amrecover&quot;
 client-username &quot;amanda&quot;
 amandad-path &quot;/server/amandad/path&quot;</pre>
<p>Besides user keys, SSH uses host keys to uniquely identify each host, to prevent one host from impersonating another. Unfortunately, the only easy way to set up these host keys is to make a connection and tell SSH that you trust the identity: </p>
<pre> $ ssh client1.zmanda.com
 The authenticity of host 'client1.zmanda.com (192.168.10.1)' can't be established.
 RSA key fingerprint is 26:4e:df:a2:be:c8:cb:20:1c:68:8b:cc:c0:3b:8e:9d.
 Are you sure you want to continue connecting (yes/no)?yes</pre>
<p>As Amanda will not answer this question itself, you must manually make every connection (server to client and client to server) that you expect Amanda to make. Note that you must use the same username that Amanda will use (that is, ssh client and ssh client.domain.com are distinct).</p>
<h3>Authenticated Peer Hostnames with SSH Authentication</h3>
<p>When accepting an incoming conneciton, the SSH daemon gives Amanda information about the remote system in the $SSH_CONNECTION environment variable. Amanda parses this information to determine the remote address, and then performs a similar check to that done by the BSD authentications: the forward and reverse DNS entries for the remote host must match. As such, while SSH authentication can cryptographically ensure that the remote system is recognized (since it had a recognized secret key), its assurances about the remote host&#8217;s identity are weaker and depend on the integrity of the DNS.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5), <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/8-amrecover/">amrecover</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Paul Yeatman</code> &lt;pyeatman [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
