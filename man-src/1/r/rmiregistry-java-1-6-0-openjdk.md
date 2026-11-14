---
title: "rmiregistry-java-1-6-0-openjdk(1)"
name: "rmiregistry-java-1-6-0-openjdk"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rmiregistry-java-1-6-0-openjdk/"
description: "rmiregistry – The Java Remote Object Registry"
---

<p>rmiregistry &#8211; The Java Remote Object Registry </p>
<p> The <code>rmiregistry</code> command starts a remote object registry on the specified port on the current host.</p>
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
<dt>-J</p>
<dd>Used in conjunction with any <i>java</i> option, it passes the option following the <i>-J</i> (no spaces between the -J and the option) on to the <i>java</i> interpreter.</dl>
<h2>See Also</h2>
<p>java, <i>java.rmi.registry.LocateRegistry</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/api/java/rmi/registry/locateregistry.html">http://java.sun.com/javase/6/docs/api/java/rmi/registry/locateregistry.html</a> and <i>java.rmi.Naming</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/api/java/rmi/naming.html">http://java.sun.com/javase/6/docs/api/java/rmi/naming.html</a> </p>
<p>&nbsp;<wbr></p>
