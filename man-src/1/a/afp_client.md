---
title: "afp_client(1)"
name: "afp_client"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afp_client/"
description: "afp_client- Mount, unmount and control Apple Filing Protocol (AFP) sessions using the FUSE infrastructure."
---

<h2>NAME</h2>
<p> afp_client- Mount, unmount and control Apple Filing Protocol (AFP) sessions using the FUSE infrastructure.</p>
<h2>SYNOPSIS</h2>
<p> <code>afp_client mount|status|unmount|suspend|resume|exit [options]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>afp_client</code> command allows you to perform some basic functions to access AFP volumes, such as mount, unmount, get status, suspend and resume. </p>
<p> Do not confuse this with afpcmd; afp_client is to be used only for the FUSE client, in conjunction with <a href="/docs/linux/man/1-afpfsd/">afpfsd</a>(1). afpcmd is a batch-mode file transferring client. Both of them use the afpfs-ng libraries. </p>
<p> <a href="/docs/linux/man/1-afp_mount/">afp_mount</a>(1) is normally a symlink to afp_client. It only handles mounting commands with a fully formed AFP URL. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>mount</code></p>
<dd> The name of the interface. This is usually a driver name followed by a unit number, for example <code>eth0</code> for the first Ethernet interface.</p>
<dt><code>mount [mount options] node</code></p>
<dd> Using the authentication and server information provided with the mount options, mount the remove filesystem on node. For more information, see the &quot;mount options&quot; later in this man page. If you would prefer to use the AFP URL syntax, see <a href="/docs/linux/man/1-mount_afp/">mount_afp</a>(1) for more information.</p>
<dt><code>unmount node</code></p>
<dd> Remove the AFP mount that is currently connected to <code>node</code></p>
<dt><code>status</code></p>
<dd> Show status information of all connected servers. This will provide information on connected servers&#8217; IP address, server descriptions (machine type, machine name, signature, login message) and available volumes. It also provides statistics and other details. This is crtical for debugging.</p>
<dt><code>suspend</code></p>
<dd> Suspends but does not unmount the current connections to all currently connected server. Currently unsupported.</p>
<dt><code>resume</code></p>
<dd> Resumes all suspended server connections. Currently unsupported. Enable or disable the <code>promiscuous</code> mode of the interface. If selected, all packets on the network will be received by the interface.</dl>
<h2>MOUNT FLAGS</h2>
<dl>
<dt><code>-u, &#8211;user &lt;username&gt;</code></p>
<dd> Log in using &lt;username&gt;</p>
<dt><code>-p, &#8211;pass &lt;password&gt;</code></p>
<dd> If you specify a &#8216;-&#8216; as the password, you will be prompted for it. This allows you to use a password without having to expose it on the command line.</p>
<dt><code>-o, &#8211;port &lt;portnum&gt;</code></p>
<dd> Use TCP portnum instead of the default, 548.</p>
<dt><code>-V, &#8211;volumepassword &lt;volumepassword&gt;</code></p>
<dd> Use this if the volume you&#8217;re accessing uses a volume password (a very weak form of protection as it is transferred as clear text). If you specify a &#8216;-&#8216; as the password, you will be prompted for it. This allows you to use a password without having to expose it on the command line. </p>
<p> If you specify a &#8216;-&#8216; as the password, you will be prompted for it. This allows you to use a password without having to expose it on the command line.</p>
<dt><code>-v, &#8211;version &lt;afp version&gt;</code></p>
<dd> Specify the AFP version that will be used for a mount. For AFP 2.2, use &#8217;22&#8217;, for 3.2, use &#8217;32&#8217;, etc. By default afpfs-ng will choose the highest AFP version shared between the client and server. afpfs-ng supports AFP 2.0 up to 3.2. <code>-a, &#8211;uam &lt;uam&gt;</code> Set the authentication method, to one of:</p>
<dl>
<dt>
<dd>
<p> <i>No User Authent</i> </p>
<p> <i>Cleartxt Passwrd</i> </p>
<p> <i>Randnum Exchange</i> </p>
<p> <i>2-Way Randnum Exchange</i> </p>
<p> <i>DHCAST128</i> </p>
<p> <i>Client Krb v2</i> </p>
<p> <i>DHX2</i></dl>
<p> If you do not specify a UAM, the most secure one common to both the server and client (afpfs-ng) will be chosen.</p>
<dt><code>-m, &#8211;map &lt;uam&gt;</code></p>
<dd> Set the method used to map local to server UID and GIDs. Posible values are:</p>
<dl>
<dt>
<dd>
<p> <i>Common user directory</i> This should be used in an environment where the UID and GID of the client and server are expected to match perfectly. An example of this is where there is an NIS or open directory server. </p>
<p> <i>Login ids</i> Use this when you want all files to appear to be owned by the uid and gid of the userid that you used for your authentication information.</p>
<dl>
<dt></dl>
</dl>
</dl>
<h2>HISTORY</h2>
<dd> afp_client is part of the FUSE implementation of afpfs-ng. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-afpfsd/">afpfsd</a>(1), <a href="/docs/linux/man/1-mount_afp/">mount_afp</a>(1)</p>
<h2>AUTHORS</h2>
<p> Alex deVries, alexthepuffin [at] gmail.com </p>
<h2>Index</h2>
