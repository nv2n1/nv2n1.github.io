---
title: "stapvirt(1)"
name: "stapvirt"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stapvirt/"
description: "stapvirt – prepare libvirt domains for systemtap probing"
---

<h2>NAME</h2>
<p> stapvirt &#8211; prepare libvirt domains for systemtap probing </p>
<h2>SYNOPSIS</h2>
<p> <code>stapvirt</code> [<code>-c</code> <i>URI</i>] [<code>-d</code> <i>PATH</i>] [<code>-v</code>] <i>COMMAND</i> <i>ARGUMENTS</i> </p>
<h2>DESCRIPTION</h2>
<p> The <i>stapvirt</i> program can be used to add ports to domains managed by libvirt (see &lt;<a rel="nofollow" href="http://libvirt.org/">http://libvirt.org/</a>&gt;). These ports can then be used by <i>stap</i> to run scripts inside the domains (see the &#8216;&#8211;remote&#8217; option in <i><a href="/docs/linux/man/1-stap/">stap</a></i>(1) for more information). </p>
<p> Ports are added to the definition of the domain using the <code>port-add</code> command. These ports can later be removed using the <code>port-remove</code> command. Note that there can only be as many simultaneous <i>stap</i> sessions as there are ports. </p>
<p> Starting from libvirt v1.1.1 and QEMU v0.10.0, SystemTap ports can be hotplugged and thus do not need to be added first using the <code>port-add</code> command. However, you need to ensure that there is a virtio-serial controller in place so that hotplugged ports can be connected. If creating a domain using virt-install, you can do this by adding this option: </p>
<dl>
<dt>
<dd>
<pre>
<code>$</code> virt-install [...] --controller=virtio-serial
</pre>
</dl>
<p> If the domain has already been created, you can simply do <code>port-add</code> followed immediately by <code>port-remove</code>, and then power off and restart the domain. The port will be removed, but the controller will remain. </p>
<h2>OPTIONS</h2>
<p> The following options are supported. Any other option prints a short help message. </p>
<dl>
<dt><code>-c</code> <i>URI</i></p>
<dd> Specify the libvirt driver URI to which to connect (e.g. &#8216;<a href="qemu:///system'">qemu:///system&#8217;</a>). The default value is NULL, which indicates to libvirt to connect to the default driver. See the page at &lt;<a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a>&gt; for supported values. </p>
<dt><code>-d</code> <i>PATH</i></p>
<dd> Specify the directory in which UNIX sockets should be created when SystemTap ports are added. The default directory is &#8216;/var/lib/libvirt/qemu&#8217;. </p>
<dt><code>-v</code></p>
<dd> Increase verbosity. This option may be repeated for more verbosity. </p>
</dl>
<h2>COMMANDS</h2>
<p> The following commands are recognized by stapvirt. Any other command prints a short help message. </p>
<dl>
<dt><code>help</code></p>
<dd> Display the help message. </p>
<dt><code>list</code></p>
<dd> List available domains. </p>
<dt><code>port-add</code> <i>DOMAIN</i></p>
<dd> Add a permanent SystemTap port to the domain&#8217;s definition. If the domain is currently running, it must be powered off before changes take effect. </p>
<dt><code>port-list</code> <i>DOMAIN</i></p>
<dd> List the UNIX socket paths of the permanent SystemTap ports in the domain&#8217;s definition. </p>
<dt><code>port-remove</code> <i>DOMAIN</i></p>
<dd> Remove a permanent SystemTap port from the domain&#8217;s definition. If the domain is currently running, it must be powered off before changes take effect. </p>
<dt><code>query</code> <i>DOMAIN</i></p>
<dd> Display the following information about the domain: its name, its UUID, its state, the number of permanent SystemTap ports installed, and whether hotplugging is supported. </p>
</dl>
<h2>TUTORIAL</h2>
<p> This tutorial will help you get started with stapvirt. Let&#8217;s start by listing all the privileged domains on the machine with the <code>list</code> command: </p>
<dl>
<dt>
<dd>
<pre>
<code>$</code> stapvirt -c '<a href="qemu:///system'">qemu:///system'</a> list
Available domains on URI '<a href="qemu:///system':">qemu:///system':</a>
ID      State     Type        Name
2       running   persistent  TestVM
</pre>
</dl>
<p> Note that we specified the libvirt URI using the -c switch. Otherwise libvirt might have defaulted to e.g. &#8216;<a href="qemu:///session'.">qemu:///session&#8217;.</a> </p>
<p> Rather than typing the URI everytime, it might be easier to instead set the LIBVIRT_DEFAULT_URI environment variable and omit the -c switch. Note that this is a libvirt functionality (see &lt;libvirt.org/uri.html&gt; for more details). </p>
<p> The <code>list</code> command indicates that we have a running domain named &#8216;TestVM&#8217; with ID 2. Let&#8217;s use the <code>query</code> command to retrieve more information: </p>
<dl>
<dt>
<dd>
<pre>
<code>$</code> stapvirt query TestVM # by name
<code>$</code> stapvirt query 2      # by ID
              Name:  TestVM
              UUID:  905951c0-fa4f-409b-079c-c91ddda27028
             State:  running
                ID:  2
              Type:  persistent
   Permanent Ports:  0
       Hotplugging:  not supported
</pre>
</dl>
<p> The <code>query</code> command gives us some basic information about the domain, such as its name, UUID, and state. More importantly, it gives us two pieces of information: the number of permanent ports installed, and whether hotplugging is supported. Technically, hotplugging support depends on libvirt and qemu, and is not related to the domain in itself. </p>
<p> If hotplugging were supported, we could stop here and run <i>stap</i> directly (assuming we have a virtio-serial controller already in place, see <code>DESCRIPTION</code>). Since in our case hotplugging is not supported, we need to add SystemTap ports. To do this, we use the <code>port-add</code> command: </p>
<dl>
<dt>
<dd>
<pre>
<code>$</code> stapvirt port-add TestVM
Added new port org.systemtap.stapsh.0
The domain must be powered off before changes take effect.
</pre>
</dl>
<p> We can confirm that a port was added by running the <code>query</code> command again: </p>
<dl>
<dt>
<dd>
<pre>
<code>$</code> stapvirt query TestVM
<code>...</code>
   Permanent Ports:  1
       Hotplugging:  not supported
</pre>
</dl>
<p> It now indicates that there is 1 permanent port. We can also use the <code>port-list</code> command to know exactly where the port will be created: </p>
<dl>
<dt>
<dd>
<pre>
<code>$</code> stapvirt port-list TestVM
/var/lib/libvirt/qemu/TestVM.org.systemtap.stapsh.0.sock
</pre>
</dl>
<p> After powering off and restarting the domain, we are now ready to use the port with <i>stap</i>: </p>
<dl>
<dt>
<dd>
<pre><code>
$ stap - e 'probe begin { printf("Hello from TestVM!
"); exit() }' --remote = libvirt : // TestVM
                                                                                         Hello from TestVM !
</code></pre>
</dl>
<p> Finally, if we&#8217;d like to remove the port, we can use the <code>port-remove</code> command: </p>
<dl>
<dt>
<dd>
<pre>
<code>$</code> stapvirt port-remove TestVM
Removed port org.systemtap.stapsh.0
The domain must be powered off before changes take effect.
</pre>
</dl>
<p> And that&#8217;s all there is to it! </p>
<h2>SEE ALSO</h2>
<pre>
<i><a href="//www.systutorials.com/docs/linux/man/1-stap/">stap</a></i>(1),
<i><a href="//www.systutorials.com/docs/linux/man/1-virt-install/">virt-install</a></i>(1)
</pre>
<h2>BUGS</h2>
<p> Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>,<code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
<h2>Index</h2>
