---
title: "remote_startup(5)"
name: "remote_startup"
section: "5"
letter: "r"
url: "/docs/linux/man/5-remote_startup/"
description: "remote_startup – the xxQS_NAMExx remote startup mechanism"
---

<p>remote_startup &#8211; the xxQS_NAMExx remote startup mechanism</p>
<h2>Description</h2>
<p>xxQS_NAMExx supports several commands to facilitate interactive commands or remote startup of a tightly integrated parallel job. Each command can be set up with (option <code>-sconf</code>) to use different daemons and commands to start the final session. Different startup methods can therefore contain different daemons and commands, and are not related to other startup methods in any way, although it is often desirable to have the same communication method for all startup methods. </p>
<p> Each method requires a separate instance of the communication daemon to be started by for each job, which thus must use a randomly-chosen port, to which the client will try to connect. This is necessary to support tight integration, ensuring that everything for a given job stays in the same process tree and can be properly controlled and accounted by xxQS_NAMExx.</p>
<h2>Qlogin</h2>
<p>An interactive <code>qlogin</code> session invoked by will show up in <code>qstat</code> with the default name <code>QLOGIN</code> unless changed by the <code>-N </code><i>name</i> option. The two entries <code>qlogin_daemon</code> and <code>qlogin_command</code> are responsible for establishing the communication to start such a session. </p>
<p> The default is the value <code>builtin</code>, which will trigger an xxQS_NAME_Sxx internal communication method: </p>
<dl>
<dd>
<dl>
<dt><code>qlogin_command</code></p>
<dd>builtin</p>
<dt><code>qlogin_daemon</code></p>
<dd>builtin</dl>
</dl>
<p> In cases where you want a different communication method, it can also be set up for the formerly-used communication method based on <code>telnet</code>. Despite the fact that <code>telnet</code> is used, there is no need to have <code>telnetd</code> running all the time &#8211; xxQS_NAME_Sxx will start a unique one for each job, even when it&#8217;s from the same user, and telnet can stay disabled as a system service (whether under init or inetd). Only the file /etc/hosts.equiv needs to contain the name of the machines from where a should be allowed. This is often the head node of a cluster, or particular submit machines. Using telnet, the traffic is not encrypted, but that may be reasonable on a private subnet for the cluster, especially if xxQS_NAME_Sxx&#8217;s CSP security isn&#8217;t used to secure the system generally. </p>
<p> To achieve this: </p>
<dl>
<dd>
<dl>
<dt><code>qlogin_command</code></p>
<dd>/usr/bin/telnet</p>
<dt><code>qlogin_daemon</code></p>
<dd>/usr/sbin/in.telnetd</dl>
</dl>
<p> must be defined in The defined <code>qlogin_command</code> will then be called with two additional parameters: &#8216;HOST&#8217;, and &#8216;PORT&#8217; in exactly that order, which refer to the machine the <code>qlogin_command</code> should address and the port to be used. </p>
<p> This can also be used to set up secure communication using <code>SSH</code> (which can also provide X and credential forwarding, as well as compression). In this case a small wrapper must be implemented, whose sole purpose is to swap the two given arguments and prepend <code>-p</code> to the port argument. A suitable one is installed as <i>$SGE_ROOT/util/resources/wrappers/qlogin_wrapper</i>: </p>
<dl>
<dd>
<dl>
<dt><code>qlogin_command</code></p>
<dd>/opt/sge/util/resources/wrappers/qlogin_wrapper</p>
<dt><code>qlogin_daemon</code></p>
<dd>/usr/sbin/sshd -i</dl>
</dl>
<h2>Qrlogin</h2>
<p>An interactive <code>qrlogin</code> session invoked by <code>without</code> a command will show up in <code>qstat</code> having the default name <code>QRLOGIN</code> unless changed by the <code>-N </code><i>name</i> option. The two entries <code>rlogin_daemon</code> and <code>rlogin_command</code> are responsible for establishing the command to start such a session. </p>
<p> The default is the value <code>builtin</code>, which will trigger an xxQS_NAME_Sxx internal communication method: </p>
<dl>
<dd>
<dl>
<dt><code>rlogin_command</code></p>
<dd>builtin</p>
<dt><code>rlogin_daemon</code></p>
<dd>builtin</dl>
</dl>
<p> In cases where you want a different communication method, it can follow the formerly-used communication method based on <code>rlogin</code>. As for telnet, rlogin can stay disabled as a system service (whether under init or inetd). Only the file /etc/hosts.equiv needs to contain the name of the machines from where a should be allowed. This is often the head node of a cluster, or particular submit machines. Using <code>rlogin</code>, the traffic is not encrypted, but that may be reasonable on a private subnet for the cluster, especially if xxQS_NAME_Sxx&#8217;s CSP security isn&#8217;t used to secure the system generally. </p>
<p> To achieve this: </p>
<dl>
<dd>
<dl>
<dt><code>rlogin_command</code></p>
<dd>$SGE_ROOT/utilbin/<i>$ARC</i>/rlogin</p>
<dt><code>rlogin_daemon</code></p>
<dd>/usr/sbin/in.rlogind</dl>
</dl>
<p> must be defined in The value of <i>$SGE_ROOT</i> must be replaced by the root of the installation, and <i>$ARC</i> must be replaced by the particular platform architecture, as use of environment variables is not implemented for these entries. When the cluster is homogeneous, it can be set to e.g. &#8216;lx-amd64&#8217; or &#8216;lx-x86&#8217;. In a heterogeneous cluster local configurations need to be defined, where preferably the minority of machines will get local configurations. </p>
<p> The defined <code>rlogin_command</code> will then be called with three additional parameters: &#8216;-p&#8217;,&#8217;PORT&#8217;, and &#8216;HOST&#8217; in exactly that order, which refer to the machine the <code>rlogin_command</code> should address, and the port to be used. </p>
<p> This can also be used to set up a secure communication using <code>SSH</code>: </p>
<dl>
<dd>
<dl>
<dt><code>rlogin_command</code></p>
<dd>/usr/bin/ssh</p>
<dt><code>rlogin_daemon</code></p>
<dd>/usr/sbin/sshd -i</dl>
</dl>
<h2>Qrsh</h2>
<p>An interactive session for a remote command invoked by <code>with</code> a command will show up in <code>qstat</code> by default with name of the command issued, unless changed by the <code>-N </code><i>name</i> option. The two entries <code>rsh_daemon</code> and <code>rsh_command</code> are responsible for establishing the communication to start such a session. This startup method will also be used by the master task of a tightly integrated parallel job to start slave processes on other granted exechosts. </p>
<p> The default is the value <code>builtin</code>, which will trigger an xxQS_NAME_Sxx internal communication method: </p>
<dl>
<dd>
<dl>
<dt><code>rsh_command</code></p>
<dd>builtin</p>
<dt><code>rsh_daemon</code></p>
<dd>builtin</dl>
</dl>
<p> In cases where you want a different communication method, it can also be set up for the formerly-used communication method based on <code>rsh</code>. As for telnet, rsh can stay disabled as a system service (whether under init or inetd). Only the file /etc/hosts.equiv needs to contain the name of the machines from where a should be allowed. This is often the head node of a cluster, or particular submit machines. Using <code>rsh</code>, the traffic is not encrypted, but that may be reasonable on a private subnet for the cluster, especially if xxQS_NAME_Sxx&#8217;s CSP security isn&#8217;t used to secure the system generally. </p>
<p> To achieve this: </p>
<dl>
<dd>
<dl>
<dt><code>rsh_command</code></p>
<dd>$SGE_ROOT/utilbin/<i>$ARC</i>/rsh</p>
<dt><code>rsh_daemon</code></p>
<dd>$SGE_ROOT/utilbin/<i>$ARC</i>/rshd -l</dl>
</dl>
<p> must be defined in The value of <i>$SGE_ROOT</i> must be replaced by the root of the installation, and <i>$ARC</i> must be replaced by the particular platform architecture, as use of environment variables is not implemented for these entries. When the cluster is homogeneous, it can be set to e.g. &#8216;lx-amd64&#8217; or &#8216;lx-x86&#8217;. In a heterogeneous cluster local configurations need to be defined, where preferably the minority of machines will get local configurations. </p>
<p> The defined <code>rsh_command</code> will then be called with four additional parameters: &#8216;-n&#8217;, &#8216;-p&#8217;, &#8216;PORT&#8217;, and &#8216;HOST&#8217; in exactly that order, which refer to the machine the <code>rsh_command</code> should address and the port to be used. </p>
<p> This can also be used to set up a secure communication using <code>SSH</code>: </p>
<dl>
<dd>
<dl>
<dt><code>rsh_command</code></p>
<dd>/usr/bin/ssh</p>
<dt><code>rsh_daemon</code></p>
<dd>/usr/sbin/sshd -i</dl>
</dl>
<p> Again, this is independent of SSH as a system service, which can remain disabled.</p>
<h2>Local Configurations Of Exechosts</h2>
<p>It is important to note that the communication method set up for one particular startup method must match at each end. This can either be achieved by using only a global configuration, or carefully setting up local configurations for the exechosts involved. Whether or not local configurations exist, which must be taken care of, can be checked with <code>qconf -sconfl</code>. </p>
<p> As a general rule, for setting up a communication method between a machine A (where the <code>command</code> is issued) and a machine B (where the <code>daemon</code> is started) it must be guaranteed that the: </p>
<dl>
<dd>setup communication method for the <code>command</code> on machine A<br />
 (either global configuration from or local configuration <code>qconf -sconf </code><code>A</code> of machine A)</dl>
<p> matches </p>
<dl>
<dd>setup communication method for the <code>daemon</code> for machine B<br />
 (either global configuration from or local configuration <code>qconf -sconf </code><code>B</code> of machine B)</dl>
<p> This way it is also possible to use different communication methods, depending whether a connection from A to B is invoked, or from B to A.</p>
<h2>Restrictions</h2>
<p>For all three communication methods, a direct connection between the target and the source machine where the particular command was issued must exist. This can also be implemented using TCP/IP forwarding, but will usually fail if one machine is behind NAT which will mangle the machines&#8217; addresses. The communication methods won&#8217;t work with simple firewalling of the exec hosts since the methods use a random port. It may be possible to set up application-specific firewalling, if necessary, or to wrap the methods and start an SSH tunnel on the port specified for each communication instance. </p>
<p> The <code>builtin</code> method does not support forwarding of X graphics from the compute nodes, or GSSAPI tokens to them. If you need that for any of the remote methods, you will want to set up SSH communication instead.</p>
<h2>Ssh Authentication</h2>
<p>To allow the <code>SSH</code> setup explained above to work, the user must be authenticated without the use of a <i>passphrase</i>. While entering a <i>passphrase</i> would still work for interactive commands, it will fail in case of a tightly integrated parallel job, where the master process tries to start a slave process on another exechost. </p>
<p> You can set up <i>passphraseless</i> <code>SSH keys</code>, although this is discouraged. A simpler and global working setup is to use host-based authentication &lt;URL: <a rel="nofollow" href="https://gridengine.sourceforge.io/SGE/howto/hostbased-ssh.html">https://gridengine.sourceforge.io/SGE/howto/hostbased-ssh.html</a> &gt; for the machines inside the cluster.</p>
<h2>Ssh Tight Integration</h2>
<p>To have a tight integration of <code>SSH</code> into xxQS_NAME_Sxx, the started <code>sshd</code> needs an additional group ID to be attached. With this additional group ID, xxQS_NAME_Sxx is able to record the resource consumption and computing time in a correct way. Also a <code>qdel</code> of such a job will be able to succeed. </p>
<p> Such a tight SSH integration can be achieved by two means:</p>
<dl>
<dt><code>Use of PAM</code></p>
<dd>The easiest way on supported platforms (at least GNU/Linux): a <i><a href="/docs/linux/man/7-pam/">pam</a></i>(7) module is available for use with the system ssh; it attaches the necessary additional group ID to the started process to provide tight integration. See also the workshop paper &lt;URL: <a rel="nofollow" href="http://gridengine.org/assets/static/ws2007/K5SGE.pdf">http://gridengine.org/assets/static/ws2007/K5SGE.pdf</a> &gt;.</p>
<dt><code>Recompile xxQS_NAMExx with ./aimk -tight-ssh &#8230;</code></p>
<dd>The source of xxQS_NAMExx contains the necessary additions to compile a modified <i>sshd</i>, which will honor the additional group ID and attach it also to the started process. It&#8217;s necessary to provide the source of <i>OpenSSH</i> in the directory <i>3rd_party</i> inside <i>$SGE_ROOT</i> having a plain name &#8216;openssh&#8217;. Inside this directory the file <i>sshd.c</i> needs to be patched: </p>
<dl>
<dd>in main():</p>
<dl>
<dd>init_rng();<br />
 #ifdef SGESSH_INTEGRATION<br />
 sgessh_readconfig();<br />
 #endif</dl>
<p> in privsep_postauth():</p>
<dl>
<dd>/* Drop privileges */<br />
 #ifdef SGESSH_INTEGRATION<br />
 sgessh_do_setusercontext(authctxt-&gt;pw);<br />
 #else<br />
 do_setusercontext(authctxt-&gt;pw);<br />
 #endif</dl>
<p> See the original documentation &lt;URL: <a rel="nofollow" href="http://gridengine.org/assets/static/ws2007/SGE-openSSHTightIntegration.RonChen.pdf">http://gridengine.org/assets/static/ws2007/SGE-openSSHTightIntegration.RonChen.pdf</a> &gt;.</dl>
</dl>
<h2>Restricting Access</h2>
<p>With the builtin method in use, there is no need to allow direct access for normal users to compute nodes with ssh etc. However, you may want to allow users to access the nodes for debugging. If you don&#8217;t want to over-subscribe the nodes, so that qrsh etc. can be used for access, you can use PAM to restrict access for a user only to the nodes on which they have a running job, so as to minimize interference with other others. </p>
<p> There are two possible ways. The cleanest uses Otherwise you can use generic PAM modules, such as <i><a href="/docs/linux/man/8-pam_limits/">pam_limits</a></i>(8) or <i><a href="/docs/linux/man/8-pam_access/">pam_access</a></i>(8), with modifications to their configuration set up and taken down in the job prolog and epilog respectively. See, for instance, a user list message &lt;URL: <a rel="nofollow" href="http://gridengine.markmail.org/message/mu3i7haeshlevu6q?q=282211">http://gridengine.markmail.org/message/mu3i7haeshlevu6q?q=282211</a> &gt;, and other examples of similar prolog/epilog scripts provided with locking in the pam_authuser contribution in the Torque distribution.</p>
<h2>Security</h2>
<p>See the notes above concerning security of the communication channel.</p>
<h2>Examples</h2>
<p>Using SSH with the PAM module, forcing tty allocation, and preventing the delegation of GSSAPI credentials to the compute nodes:</p>
<dl>
<dd>rsh_daemon /opt/sge/util/rshdwrapper<br />
 rsh_command ssh -tt -o GSSAPIDelegateCredentials=no<br />
 qlogin_daemon /opt/sge/util/rshdwrapper<br />
 qlogin_command ssh -tt -o GSSAPIDelegateCredentials=no<br />
 rlogin_daemon /opt/sge/util/rshdwrapper<br />
 rlogin_command ssh -tt -o GSSAPIDelegateCredentials=no</dl>
<p> Old-style method, using telnet and rlogin:</p>
<dl>
<dd>qlogin_command /usr/bin/telnet<br />
 qlogin_daemon /usr/sbin/in.telnetd<br />
 rlogin_command /opt/sge/utilbin/lx-x86/rlogin<br />
 rlogin_daemon /usr/sbin/in.rlogind<br />
 rsh_command /opt/sge/utilbin/lx-x86/rsh<br />
 rsh_daemon /opt/sge/utilbin/lx-x86/rshd -l</dl>
<h2>Files</h2>
<dl>
<dt><i>$SGE_ROOT/util/resources/wrappers/qlogin_wrapper</i></p>
<dd>SSH-based wrapper for qlogin (see above)</dl>
<h2>See Also</h2>
<p>xxQS_NAMExx-specific remote programs. &lt;URL: <a rel="nofollow" href="https://sourceforge.net/p/gridengine/sge/sge.git/ci/master/tree/source/3rdparty/remote/remote.html">https://sourceforge.net/p/gridengine/sge/sge.git/ci/master/tree/source/3rdparty/remote/remote.html</a> &gt;</p>
<h2>Author</h2>
<p>Man page written by Reuti, partly based on Sun material. Some additions by Dave Love.</p>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
