---
title: "rmiregistry-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64(1)"
name: "rmiregistry-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmiregistry-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64/"
description: "rmiregistry – The Java Remote Object Registry"
---

<p>rmiregistry &#8211; The Java Remote Object Registry </p>
<dl COMPACT>
<dd>The <code>rmiregistry</code> command starts a remote object registry on the specified port on the current host.</dl>
<h2>Synopsis</h2>
<pre><code>rmiregistry [</code><tt>port</tt><code>]</code></pre>
<h2>Description</h2>
<p>The <code>rmiregistry</code> command creates and starts a remote object registry on the specified <i>port</i> on the current host. If <i>port</i> is omitted, the registry is started on port 1099. The <code>rmiregistry</code> command produces no output and is typically run in the background. For example: </p>
<p> <i>rmiregistry &amp;</i> </p>
<p> A remote object registry is a bootstrap naming service that is used by RMI servers on the same host to bind remote objects to names. Clients on local and remote hosts can then look up remote objects and make remote method invocations. </p>
<p> The registry is typically used to locate the first remote object on which an application needs to invoke methods. That object in turn will provide application-specific support for finding other objects. </p>
<p> The methods of the <i>java.rmi.registry.LocateRegistry</i> class are used to get a registry operating on the local host or local host and port. </p>
<p> The URL-based methods of the <i>java.rmi.Naming</i> class operate on a registry and can be used to look up a remote object on any host, and on the local host: bind a simple (string) name to a remote object, rebind a new name to a remote object (overriding the old binding), unbind a remote object, and list the URLs bound in the registry. </p>
<h2>Options</h2>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>-J</p>
<dd>Used in conjunction with any <i>java</i> option, it passes the option following the <i>-J</i> (no spaces between the -J and the option) on to the <i>java</i> interpreter.</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-java/">java</a>(1), <i>java.rmi.registry.LocateRegistry</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/java/rmi/registry/LocateRegistry.html">http://docs.oracle.com/javase/7/docs/api/java/rmi/registry/LocateRegistry.html</a> and <i>java.rmi.Naming</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/api/java/rmi/Naming.html">http://docs.oracle.com/javase/7/docs/api/java/rmi/Naming.html</a></p>
