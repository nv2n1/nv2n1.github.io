---
title: "rmiregistry-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64(1)"
name: "rmiregistry-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmiregistry-java-1-8-0-openjdk-1-8-0-151-1-b12-el7_4-x86_64/"
description: "rmiregistry – Starts a remote object registry on the specified port on the current host."
---

<p>rmiregistry &#8211; Starts a remote object registry on the specified port on the current host.</p>
<h2>Synopsis</h2>
<pre><code>rmiregistry</code> [ <i>port</i> ]</pre>
<dl COMPACT>
<dt><i>port</i></p>
<dd>The number of a <code>port</code> on the current host at which to start the remote object registry.</dl>
<h2>Description</h2>
<p>The <code>rmiregistry</code> command creates and starts a remote object registry on the specified port on the current host. If the port is omitted, then the registry is started on port 1099. The <code>rmiregistry</code> command produces no output and is typically run in the background, for example: </p>
<pre><code>rmiregistry &amp;</code></pre>
<p>A remote object registry is a bootstrap naming service that is used by RMI servers on the same host to bind remote objects to names. Clients on local and remote hosts can then look up remote objects and make remote method invocations. </p>
<p> The registry is typically used to locate the first remote object on which an application needs to call methods. That object then provides application-specific support for finding other objects. </p>
<p> The methods of the <code>java.rmi.registry.LocateRegistry</code> class are used to get a registry operating on the local host or local host and port. </p>
<p> The URL-based methods of the <code>java.rmi.Naming</code> class operate on a registry and can be used to look up a remote object on any host and on the local host. Bind a simple name (string) to a remote object, rebind a new name to a remote object (overriding the old binding), unbind a remote object, and list the URL bound in the registry.</p>
<h2>Options</h2>
<dl COMPACT>
<dt>-J</p>
<dd>Used with any Java option to pass the option following the <code>-J</code> (no spaces between the <code>-J</code> and the option) to the Java interpreter.</dl>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-java/">java</a>(1)</p>
<dt>&bull;</p>
<dd><code>java.rmi.registry.LocateRegistry</code> class description at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/java/rmi/registry/LocateRegistry.html">http://docs.oracle.com/javase/8/docs/api/java/rmi/registry/LocateRegistry.html</a></p>
<dt>&bull;</p>
<dd><code>java.rmi.Naming class description</code> at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/api/java/rmi/Naming.html">http://docs.oracle.com/javase/8/docs/api/java/rmi/Naming.html</a> </p>
</dl>
