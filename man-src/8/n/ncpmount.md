---
title: "ncpmount(8)"
name: "ncpmount"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ncpmount/"
description: "ncpmount, mount.ncp, mount.ncpfs – mount volume(s) from a specified NetWare fileserver."
---

<p>ncpmount, mount.ncp, mount.ncpfs &#8211; mount volume(s) from a specified NetWare fileserver.</p>
<h2>Synopsis</h2>
<p><code>ncpmount</code> [ <code>-h</code> ] [ <code>-S</code> <i>server</i> ] [ <code>-U</code> <i>user name</i> ] [ <code>-P</code> <i>password</i> | <code>-n</code> ] [ <code>-C</code> ] [ <code>-c</code> <i>client name</i> ] [ <code>-u</code> <i>uid</i> ] [ <code>-g</code> <i>gid</i> ] [ <code>-f</code> <i>file mode</i> ] [ <code>-d</code> <i>dir mode</i> ] [ <code>-V</code> <i>volume</i> ] [ <code>-t</code> <i>time_out</i> ] [ <code>-r</code> <i>retry_count</i> ] [ <code>-b</code> ] [ <code>-i</code> <i>level</i> ] [ <code>-v</code> ] [ <code>-m</code> ] [ <code>-y</code> <i>iocharset</i> ] [ <code>-p</code> <i>codepage</i> ] [ <code>-N</code> <i>ignored namespace</i> ] [ <code>-2</code> | <code>-3</code> | <code>-4</code> ] [ <code>-s</code> ] [ <code>-A</code> <i>dns name</i> ] mount-point <code>mount.ncp</code> remote-server-and-user mount-point [ <code>-n</code> ] [ <code>-v</code> ] [ <code>-o</code> <i>mount_options</i> ] </p>
<h2>Description</h2>
<p>This program is used to mount volumes of the specified NetWare Fileserver under the specified mount point. <code>ncpfs</code> is a linux filesystem which understands the NCP protocol. This is the protocol Novell NetWare clients use to talk to NetWare servers. ncpfs was inspired by <code>lwared</code>, a free NetWare emulator for Linux written by Ales Dryak. See <a href="ftp://klokan.sh.cvut.cz/pub/linux">ftp://klokan.sh.cvut.cz/pub/linux</a> for this very interesting program. <code>ncpmount</code>, when invoked with all appropriate arguments, attaches and logs into specified server and mounts all volumes (or one volume or subtree) from server under the specified mount point. <code>ncpmount</code> when invoked without any arguments specifying the fileserver, user id and password checks the file <i>$HOME/.nwclient</i> to find a file server, a user name and possibly a password to use for the specified mount point. See <a href="/docs/linux/man/5-nwclient/">nwclient</a>(5) for more information. Please note that the access permissions of .nwclient MUST be 600, for security reasons. </p>
<h2>Options</h2>
<p><code>mount-point</code></p>
<dl>
<dd><code>mount-point</code> is the directory you want to mount the filesystem over. Its function is the the same as for a normal mount command. </p>
<p> If the real uid of the caller is not root, <code>ncpmount</code> checks whether the user is allowed to mount a filesystem on the mount-point. So it should be safe to make <code>ncpmount</code> setuid root. The filesystem stores the uid of the user who called ncpmount. So <code>ncpumount</code> can check whether the caller is allowed to unmount the filesystem.</dl>
<p> <code>-S</code> <i>server</i> (mount option <code>server=</code> or part before <code>/</code> in <i>remote-server-and-user</i>)</p>
<dl>
<dd><code>server</code> is the name of the server you want to use.</dl>
<p> <code>-h</code></p>
<dl>
<dd><code>-h</code> is used to print out a short help text.</dl>
<p> <code>-C</code> (mount option <code>noupcasepasswd</code>)</p>
<dl>
<dd>By default passwords are converted to uppercase before they are sent to the server because most servers require this. This option disables this feature ensuring that passwords are sent without any case conversion.</dl>
<p> <code>-n</code> (mount option <code>nopasswd</code>)</p>
<dl>
<dd><code>-n</code> must be specified for logins that do not have a password configured. This option means do not update /etc/mtab if there is option <code>-o</code> on command line. You must use <code>-o nopasswd</code> in this case.</dl>
<p> <code>passwdfile=file</code> (only mount option)</p>
<dl>
<dd>If you want specify password and you do not want store it into world readable /etc/fstab, you can use this option. <i>file</i> then contains lines in form SERVER/USER:PASSWORD:other_data (other_data are currently unused)</dl>
<p> <code>pass-fd=fd</code> (only mount option)</p>
<dl>
<dd>If you want to pass password in secure way to ncpmount, you can pass it through specified <i>fd</i>.</dl>
<p> <code>-P</code> <i>password</i> (mount option <code>passwd=</code>)</p>
<dl>
<dd>specifies the password to use for the Netware user id. </p>
<p> If neither <code>-n</code> nor the <code>-P</code> nor the <code>passwdfile=</code> nor the <code>pass-fd=</code> arguments are specified ncpmount will prompt for a password. This makes it difficult to use in scripts such as /etc/rc. If you want to have ncpmount work automatically from a script you must include the appropriate option and be very careful to ensure that appopriate file permissions are set for the script that includes your password to ensure that others can not read it.</dl>
<p> <code>-U</code> <i>user name</i> (mount option <code>user=</code> or rest of <i>remote-server-and-user</i> after <code>/</code>)</p>
<dl>
<dd>Specifies the Netware user id to use when logging in to the fileserver. If this option is not specified then ncpmount will attempt to login to the fileserver using the Linux login id of the user invoking ncpmount.</dl>
<p> <code>-m</code> (mount option <code>multiple</code>)</p>
<dl>
<dd>Normally, <code>ncpmount</code> limits number of connections from client to server to one per unique user name. If you want mount more than one connection with same username and server, you must specify <code>-m</code>.</dl>
<p> <code>-u</code> <i>uid,</i> <code>-g</code> <i>gid</i> (mount option <code>uid=</code> and <code>gid=</code>)</p>
<dl>
<dd>ncpmount does not yet implement a scheme for mapping NetWare users/groups to Linux users/groups. Linux requires that each file has an owner and group id. With <code>-u</code> and <code>-g</code> you can tell ncpmount which id&#8217;s it should assign to the files in the mounted directory. </p>
<p> The defaults for these values are the current uid and gid.</dl>
<p> <code>-c</code> <i>user name</i> (mount option <code>owner=</code>)</p>
<dl>
<dd><code>-c</code> names the user who is the <i>owner</i> of the connection, where owner does not refer to file ownership (that &quot;owner&quot; is set by the -u argument), but the owner of the mount, ie: who is allowed to call ncpumount on this mount. The default owner of the connection and the mount is the user who called ncpmount. This option allows you to specify that some other user should be set as the owner. </p>
<p> In this this way it is possible to mount a public read-only directory, but to allow the lp daemon to print on NetWare queues. This is possible because only users who have write permissions on a directory may issue ncp requests over a connection. The exception to this rule is the &#8216;mount owner&#8217;, who is also granted &#8216;request permission&#8217;.</dl>
<p> <code>-f</code> <i>file mode,</i> <code>-d</code> <i>dir mode</i> (mount option <code>mode=</code> (or <code>filemode=</code>) and <code>dirmode=</code>)</p>
<dl>
<dd>Like <code>-u</code> and <code>-g</code>, these options are used to determine what permissions should be assigned files and directories of the mounted volumes. The values must be specified as octal numbers. The default values are taken from the current umask, where the file mode is the current umask, and the dir mode adds execute permissions where the file mode gives read permissions. </p>
<p> Note that these permissions can differ from the rights the server gives to us. If you do not have write permissions on the server, you can very well choose a file mode that tells that you have. This certainly cannot override the restrictions imposed by the server.</dl>
<p> <code>-V</code> <i>volume</i> (mount option <code>volume=</code>)</p>
<dl>
<dd>There are 2 general ways you can mount a NetWare server&#8217;s disk space: Either you can mount all volumes under one directory, or you can mount only a single volume. </p>
<p> When you choose to mount the complete disk space at once, you have the advantage that only one Linux mount point and only one NetWare connection is used for all the volumes of this server. Both of these are limited resources. (Although raising the number of Linux mount points is significantly cheaper than raising the number of available NetWare connections ;-)) </p>
<p> When you specify to mount a single volume by using the option <code>-V</code> <i>volume,</i> you have the big advantage that nfsd is able to re-export this mounted directory. You must invoke <code>nfsd</code> and <code>mountd</code> with the option <i>&#8211;re-export</i> to make nfsd re-export ncpfs mounted directories. This uses one Linux mount point and one NetWare connection per mounted volume. Maybe sometime in the future I will make it possible to mount all volumes on different mount points, using only one connection.</dl>
<p> <code>-t</code> <i>time_out</i> (mount option <code>timeo=</code> or <code>timeout=</code>)</p>
<dl>
<dd>With <code>-t</code> you can adjust the time ncpfs waits for the server to answer a request it sent. Use the option to raise the timeout value when your ncpfs connections seem to be unstable although your servers are well up. This can happen when you have very busy servers, or servers that are very far away. </p>
<p> <i>time_out</i> is specified in 1/100s, the current default value is 60.</dl>
<p> <code>-r</code> <i>retry_count</i> (mount option <code>retry=</code>)</p>
<dl>
<dd>As <code>-t</code>, <code>-r</code> can be used to tune the ncpfs connection to the server. With <i>retry_count</i> you can specify how many times ncpfs will attempt to send a packet to the server before it decides the connection is dead. The current default value is 5. </p>
<p> Currently ncpfs is not too clever when trying to find out that connections are dead. If anybody knows how to do that correctly, as it is done by commercial workstations, please tell me.</dl>
<p> <code>-y</code> <i>iocharset</i> (mount option <code>iocharset=</code>)</p>
<dl>
<dd>You can specify character translation rules for converting names from unicode to your desktop (it works together with <code>-p</code>). <i>iocharset</i> is charset name, for example <i>iso-8859-1</i>.</dl>
<p> <code>-p</code> <i>codepage</i> (mount option <code>codepage=</code>)</p>
<dl>
<dd>You can specify character translation rules for converting names from Netware encoding to unicode (it works together with <code>-y</code>). <i>codepage</i> is codepage name, for example <i>cp437</i>.</dl>
<p> <code>-b</code> (mount option <code>bindery</code>)</p>
<dl>
<dd>If you are connecting to NetWare 4 or NetWare 5 through bindery emulation instead of NDS, you must specify this option.</dl>
<p> <code>-i</code> <i>level</i> (mount option <code>signature=</code><i>level</i>)</p>
<dl>
<dd>Enables packet signing. <i>level</i> is from 0 to 3: 0 means disable, 1 means sign if server needs it, 2 means sign if server allows it and 3 means sign packets always.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Print ncpfs version number. It has another meaning (<i>verbose</i>) if you specify <code>-o</code> on command line. If you are interested in version, type <code>ncpmount -v</code> without another options.</dl>
<p> <code>-A</code> <i>dns name</i> (mount option <code>ipserver=</code><i>dns name</i>)</p>
<dl>
<dd>When you are mounting volumes from NetWare 5 server over UDP, you must specify <i>dns name</i> of server here and <i>logical server name</i> in <code>-S</code> (or in <code>server=</code>). This name is used to switch <code>ncpmount</code> into UDP mode and to specify server to connect. Currently, <code>DNS</code> is only supported <code>IP</code> name resolution protocol. There is currently no support for <code>SLP</code>.</dl>
<p> <code>-N</code> <i>ignored namespace</i> (mount option <code>nonfs</code> and <code>nolong</code>)</p>
<dl>
<dd><code>ncpfs</code> supports <i>NFS</i>, <i>LONG</i> (<i>OS/2</i>) and <i>DOS</i> namespace on NetWare volumes. If you do not want to use <i>NFS</i> or <i>LONG</i> namespace (because of bugs in (server) code or for backward compatibility), you must specify these ignored namespaces in mount parameters.</dl>
<p> <code>-2</code></p>
<dl>
<dd>If you have unusual <code>ncpfs</code> code in kernel and <code>ncpmount</code> is not able to autodetect it, use this option. It switches <code>ncpmount</code> to <code>ncpfs</code> interface version 2. This interface was used in 2.0.x kernels, does not support NCP/UDP, does not have NDS authentication info storage and uses only 16bit uid/gid.</dl>
<p> <code>-3</code></p>
<dl>
<dd>If you have unusual <code>ncpfs</code> code in kernel and <code>ncpmount</code> is not able to autodetect it, use this option. It switches <code>ncpmount</code> to <code>ncpfs</code> interface version 3. This interface was used in kernels from 2.1.30 to 2.3.40 (laters 2.3.x and 2.4.x still supports this interface to make transition easier). This interface supports NCP/UDP, does have NDS authentication info storage (if you uncomment it in kernel sources) and uses 16bit uid/gid.</dl>
<p> <code>-4</code></p>
<dl>
<dd>If you have unusual <code>ncpfs</code> code in kernel and <code>ncpmount</code> is not able to autodetect it, use this option. It switches <code>ncpmount</code> to <code>ncpfs</code> interface version 4. This interface is used in kernels after 2.3.40. This interface supports NCP/UDP, does have NDS authentication info storage and uses 32bit uid/gid.</dl>
<p> <code>-s</code> (mount option <code>strong</code>)</p>
<dl>
<dd>Normally, files marked <i>read-only</i> cannot be removed from NetWare volume because of they are marked <i>Delete Inhibit</i> and <i>Rename Inhibit</i>. If you want to remove these files by simple <i>unlink</i>, you should mount volume with this option.</dl>
<p> mount option <code>nostrong</code></p>
<dl>
<dd>Refuse to remove <i>read-only</i> files. If you want remove such file, you must first remove <i>read-only</i> attribute. It is standard behavior of <code>ncpfs</code>.</dl>
<p> mount option <code>symlinks</code></p>
<dl>
<dd>Use special, normally unused, attributes combinations to express symlinks, executable attributes and files readable by world.</dl>
<p> mount option <code>nosymlinks</code></p>
<dl>
<dd>Do not allow special meaning of &#8216;shareable&#8217; attribute. This is a default.</dl>
<p> mount option <code>ipx</code></p>
<dl>
<dd>Use <i>IPX</i> for connection to server. Default if no <code>ipserver</code> option specified on cmdline.</dl>
<p> mount option <code>udp</code></p>
<dl>
<dd>Use <i>UDP</i> for connection to server. Not available in 2.0.x kernels. Default if <code>ipserver</code> is used.</dl>
<p> mount option <code>tcp</code></p>
<dl>
<dd>Use <i>TCP</i> for connection to server. Available only with 2.4.0 and later kernels.</dl>
<p> mount option <code>nfsextras</code></p>
<dl>
<dd>Use the meta-data provided by the NFS namespace to allow files&#8217; modes to be changed, and to allow the creation of symlinks and named pipes. This adds significant overhead to fetching file information.</dl>
<p> mount option <code>nonfsextras</code></p>
<dl>
<dd>Do not make use of meta-data provided by the NFS namespace. This is the default.</dl>
<h2>Environment Variables</h2>
<p><code>USER / LOGNAME</code></p>
<dl>
<dd>The variables USER or LOGNAME may contain the username of the person using the client. USER is tried first. If it&#8217;s empty, LOGNAME is tried.</dl>
<h2>Diagnostics</h2>
<p>Most diagnostics issued by ncpfs are logged by syslogd. Normally nothing is printed, only error situations are logged there.</p>
<h2>Examples</h2>
<p>If you want to mount volume SYS as user DOWNLOAD from server MIRROR into directory /home/pub/mirror, with files owner mirror.mirror and file mode -rw-r&#8211;r&#8211;, you can add <code>MIRROR/DOWNLOAD /home/pub/mirror ncp defaults,mode=644,uid=mirror,gid=mirror,owner=root,volume=SYS,nopasswd,multiple</code> into <i>/etc/fstab</i>. You should always specify <code>multiple</code> in mount options, otherwise there can be only one connection to server with same name. </p>
<h2>Notes</h2>
<p><code>IPX</code></p>
<dl>
<dd>You must configure the IPX subsystem before ncpmount will work. It is especially important that there is a route to the internal network of your server.</dl>
<p> <code>IP</code></p>
<dl>
<dd>You must specify both <code>-S</code> <i>logical_name</i> and <code>-A</code> <i>dns_name</i>. <i>logical_name</i> is used for searching <i>.nwclient</i>, other configuration files and is logged into <i>/etc/mtab</i>, <i>dns_name</i> is used for connecting to server. In future, logical_name will be read from server.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-syslogd/">syslogd</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8), <a href="/docs/linux/man/8-nfsd/">nfsd</a>(8), <a href="/docs/linux/man/8-mountd/">mountd</a>(8), <a href="/docs/linux/man/8-mount/">mount</a>(8)</code> </p>
<h2>Credits</h2>
<p>ncpfs would not have been possible without lwared, written by Ales Dryak (A.Dryak [at] sh.cvut.cz). </p>
<p> The encryption code was taken from Dr. Dobbs&#8217;s Journal 11/93. There Pawel Szczerbina described it in an article on NCP. </p>
<p> The ncpfs code was initially hacked from smbfs by Volker Lendecke (lendecke [at] math.uni-goettingen.de). smbfs was put together by Paal-Kr. Engstad (pke [at] engstad.ingok.hitos.no) and later polished by Volker. </p>
<p> Code is currently maintained by Petr Vandrovec (vandrove [at] vc.cvut.cz).</p>
