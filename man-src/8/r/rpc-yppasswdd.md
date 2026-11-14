---
title: "rpc-yppasswdd(8)"
name: "rpc-yppasswdd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpc-yppasswdd/"
description: "rpc.yppasswdd – NIS password update daemon"
---

<p>rpc.yppasswdd &#8211; NIS password update daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>rpc.yppasswdd</code> [-D&nbsp;<wbr><i>directory</i>] -e&nbsp;<wbr><i>chsh</i>|<i>chfn</i> [&#8211;port&nbsp;<wbr><i>number</i>] [-f|&#8211;foreground]</p>
<dt> <code>rpc.yppasswdd</code> [-s&nbsp;<wbr><i>shadow</i>] [-p&nbsp;<wbr><i>passwd</i>] -e&nbsp;<wbr><i>chsh</i>|<i>chfn</i> [&#8211;port&nbsp;<wbr><i>number</i>] [-f|&#8211;foreground]</p>
<dt> <code>rpc.yppasswdd</code> -x&nbsp;<wbr><i>program</i> | -E&nbsp;<wbr><i>program</i> -e&nbsp;<wbr><i>chsh</i>|<i>chfn</i> [&#8211;port&nbsp;<wbr><i>number</i>] [-f|&#8211;foreground]</dl>
<h2>Description</h2>
<p><code>rpc.yppasswdd</code></p>
<dd>is the RPC server that lets users change their passwords in the presence of NIS (a.k.a. YP). It must be run on the NIS master server for that NIS domain. </p>
<p> When a <code><a href="/docs/linux/man/1-yppasswd/">yppasswd</a></code>(1) client contacts the server, it sends the old user password along with the new one. <code>rpc.yppasswdd</code> will search the system&#8217;s <code>passwd</code> file for the specified user name, verify that the given (old) password matches, and update the entry. If the user specified does not exist, or if the password, UID or GID doesn&#8217;t match the information in the password file, the update request is rejected, and an error returned to the client. </p>
<p> If this version of the server is compiled with the CHECKROOT=1 option, the password given is also checked against the systems root password. </p>
<p> After updating the <code>passwd</code> file and returning a success notification to the client, <code>rpc.yppasswdd</code> executes the <code>pwupdate</code> script that updates the NIS server&#8217;s <code>passwd.*</code> and <code>shadow.byname</code> maps. This script assumes all NIS maps are kept in directories named <i>/var/yp/</i><i>nisdomain</i> that each contain a <code>Makefile</code> customized for that NIS domain. If no such <code>Makefile</code> is found, the scripts uses the generic one in <i>/var/yp</i>. </p>
<p> It is possible to pass <code>OPTIONS</code> to <code>rpc.yppasswdd</code> using the environment variable YPPASSWDD_ARGS and this variable can be set in <code>/etc/sysconfig/yppasswdd</code>.</p>
<h2>Options</h2>
<p>The following options are available: </p>
<p> <code>-D</code><i> directory</i></p>
<dl>
<dd>The <code>passwd</code> and <code>shadow</code> files are located under the specified directory path. <code>rpc.yppasswdd</code> will use this files, not <i>/etc/passwd</i> and <i>/etc/shadow.</i> This is useful if you do not want to give all users in the NIS database automatic access to your NIS server.</dl>
<p> <code>-E</code><i> program</i></p>
<dl>
<dd>Instead of rpc.yppasswdd editing the passwd &amp; shadow files, the specified program will be run to do the editing. The following environment variables will be set for the program: YP_PASSWD_OLD, YP_PASSWD_NEW, YP_USER, YP_GECOS, YP_SHELL. The program should return an exit status of 0 if the change completes successfully, 1 if the change completes successfully but pwupdate should not be run, and otherwise if the change fails.</dl>
<p> <code>-p</code><i> passwdfile</i></p>
<dl>
<dd>This options tells <code>rpc.yppasswdd</code> to use a different source file instead of <i>/etc/passwd</i> This is useful if you do not want to give all users in the NIS database automatic access to your NIS server.</dl>
<p> <code>-s</code><i> shadowfile</i></p>
<dl>
<dd>This options tells <code>rpc.yppasswdd</code> to use a different source file instead of <i>/etc/passwd</i>. See below for a brief discussion of shadow support.</dl>
<p> <code>-e [chsh|chfn]</code></p>
<dl>
<dd>By default, <code>rpc.yppasswdd</code> will not allow users to change the shell or GECOS field of their <code>passwd</code> entry. Using the <code>-e</code> option, you can enable either of these. Note that when enabling support for <code><a href="/docs/linux/man/1-ypchsh/">ypchsh</a></code>(1), you have to list all shells users are allowed to select in <i>/etc/shells</i>.</dl>
<p> <code>-x program</code></p>
<dl>
<dd>When the -x option is used, rpc.yppasswdd will not attempt to modify any files itself, but will instead run the specified program, passing to its stdin information about the requested operation(s). There is a defined protocol used to communicate with this external program, which has total freedom in how it propagates the change request. See below for more details on this.</dl>
<p> <code>-m</code></p>
<dl>
<dd>Will be ignored, for compatibility with Solaris only.</dl>
<p> <code>&#8211;port number</code></p>
<dl>
<dd>rpc.yppasswdd will try to register itself to this port. This makes it possible to have a router filter packets to the NIS ports.</dl>
<p> <code>-v &#8211;version</code></p>
<dl>
<dd>Prints the version number and if this package is compiled with the CHECKROOT option.</dl>
<p> <code>-f</code>, <code>&#8211;foreground</code></p>
<dl>
<dd>will not put itself into background.</dl>
<h2>Miscellaneous</h2>
<h3>Shadow Passwords</h3>
<p>Using Shadow passwords alongside NIS does not make too much sense, because the supposedly inaccesible passwords now become readable through a simple invocation of <code><a href="/docs/linux/man/1-ypcat/">ypcat</a></code>(1). </p>
<p> Shadow support in <code>rpc.yppasswdd</code> does not mean that it offers a very clever solution to this problem, it simply means that it can read and write password entries in the system&#8217;s <code>shadow</code> file. You have to produce a <code>shadow.byname</code> NIS map to distribute password information to your NIS clients. <code>rpc.yppasswdd</code> will search at first in the <i>/etc/passwd</i> file for the user and password. If it find&#8217;s the user, but the password is &quot;x&quot; and a <i>/etc/shadow</i> file exists, it will update the password in the shadow map.</p>
<h3>Use of the -x option</h3>
<p>The program should expect to read a single line from stdin, which is formatted as follows: </p>
<p> &lt;username&gt; o:&lt;oldpass&gt; p:&lt;password&gt; s:&lt;shell&gt; g:&lt;gcos&gt;
 </p>
<p> where any of the three fields [p, s, g] may or may not be present. </p>
<p> This program should write &quot;OK
&quot; to stdout if the operation succeeded. On any other result, rpc.yppasswdd will report failure to the client. </p>
<p> Note that the program specified by the -x option is responsible for doing any NIS make and build, and for doing any necessary validation on the shell and gcos field information supplied. The password passed to the client will be in UNIX crypt() format.</p>
<h3>Logging</h3>
<p><code>rpc.yppasswdd</code> logs all password update requests to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a>(8)</code>&#8216;s auth facility. The logging information includes the originating host&#8217;s IP address and the user name and UID contained in the request. The user-supplied password itself is not logged.</p>
<h3>Security</h3>
<p><code>rpc.yppasswdd</code> should be as secure or insecure as any program relying on simple password authentication. If you feel that this is not enough, you may want to protect <code>rpc.yppasswdd</code> from outside access by using the `securenets&#8217; feature of the new <code><a href="/docs/linux/man/8-portmap/">portmap</a></code>(8) version 3. Better still, look at <code><a href="/docs/linux/man/8-rpasswdd/">rpasswdd</a></code>(8).</p>
<h2>Files</h2>
<p><i>/usr/sbin/rpc.yppasswdd</i> </p>
<p> <i>/usr/lib/yp/pwupdate</i> </p>
<p> <i>/etc/passwd</i> </p>
<p> <i>/etc/shadow</i> </p>
<p> <i>/etc/sysconfig/yppasswdd</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5), <code><a href="/docs/linux/man/5-shadow/">shadow</a></code>(5), <code><a href="/docs/linux/man/1-passwd/">passwd</a></code>(1), <code><a href="/docs/linux/man/8-rpasswdd/">rpasswdd</a></code>(8), <code><a href="/docs/linux/man/1-yppasswd/">yppasswd</a></code>(1), <code><a href="/docs/linux/man/1-ypchsh/">ypchsh</a></code>(1), <code><a href="/docs/linux/man/1-ypchfn/">ypchfn</a></code>(1), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/1-ypcat/">ypcat</a></code>(1)</p>
<h2>Author</h2>
<p>Olaf Kirch &lt;okir [at] monad.swb.de&gt; and Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;</p>
