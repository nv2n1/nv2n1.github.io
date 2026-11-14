---
title: "tnameserv-java-1-6-0-openjdk(1)"
name: "tnameserv-java-1-6-0-openjdk"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tnameserv-java-1-6-0-openjdk/"
description: "Java IDL: Transient Naming Service – tnameserv"
---

<p>Java IDL: Transient Naming Service &#8211; <i>tnameserv</i> </p>
<p> This document discusses using the Java IDL Transient Naming Service, <i>tnameserv</i>. Java IDL also includes the Object Request Broker Daemon (ORBD). ORBD is a daemon process containing a Bootstrap Service, a Transient Naming Service, a <code>Persistent</code> Naming Service, and a Server Manager. The Java IDL tutorials all use ORBD, however, you can substitute <i>tnameserv</i> for <i>orbd</i> in any of the examples that use a Transient Naming Service. For documentation on the <i>orbd</i> tool, link to its man page or the <i>Java IDL Naming Service Included with ORBD</i> @ </p>
<p> <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/idl/jidlNaming.html">http://java.sun.com/javase/6/docs/technotes/guides/idl/jidlNaming.html</a> topic. </p>
<p> Topics in this section include: </p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>o</p>
<dd>Java IDL Transient Naming Service</p>
<dt>o</p>
<dd>Starting the Java IDL Transient Naming Service</p>
<dt>o</p>
<dd>Stopping the Java IDL Transient Naming Service</p>
<dt>o</p>
<dd>Sample Client: Adding Objects to the Namespace</p>
<dt>o</p>
<dd>Sample Client: Browsing the Namespace</dl>
</dl>
<h2>Java IDL Transient Naming Service</h2>
<p>The CORBA COS (Common Object Services) Naming Service provides a tree-like directory for object references much like a filesystem provides a directory structure for files. The Transient Naming Service provided with Java IDL, <i>tnameserv</i>, is a simple implementation of the COS Naming Service specification. </p>
<p> Object references are stored in the namespace by name and each object reference-name pair is called a name <i>binding</i>. Name bindings may be organized under <i>naming contexts</i>. Naming contexts are themselves name bindings and serve the same organizational function as a file system subdirectory. All bindings are stored under the <i>initial naming context</i>. The initial naming context is the only persistent binding in the namespace; the rest of the namespace is lost if the Java IDL naming service process halts and restarts. </p>
<p> For an applet or application to use COS naming, its ORB must know the port of a host running a naming service or have access to a stringified initial naming context for that naming service. The naming service can either be the Java IDL naming service or another COS-compliant naming service. </p>
<h2>Starting the Java IDL Transient Naming Service</h2>
<p>You must start the Java IDL naming service before an application or applet that uses its naming service. Installation of the Java IDL product creates a script (Solaris: <i>tnameserv</i>) or executable file (Windows NT: <i>tnameserv.exe</i>) that starts the Java IDL naming service. Start the naming service so it runs in the background. </p>
<p> If you do not specify otherwise, the Java IDL naming service listens on port 900 for the bootstrap protocol used to implement the ORB <i>resolve_initial_references()</i> and <i>list_initial_references()</i> methods, as follows: </p>
<pre><code> tnameserv -ORBInitialPort </code><tt>nameserverport</tt><code>&amp;</code></pre>
<p>If you do not specify the name server port, port 900 is used by default. When running Solaris software, you must become root to start a process on a port under 1024. For this reason, we recommend that you use a port number greater than or equal to 1024. To specify a different port, for example, 1050, and to run the naming service in the background, from a UNIX command shell, enter: </p>
<pre><code> tnameserv -ORBInitialPort 1050&amp;</code></pre>
<p>From an MS-DOS system prompt (Windows), enter: </p>
<pre><code> start tnameserv -ORBInitialPort 1050</code></pre>
<p>Clients of the name server must be made aware of the new port number. Do this by setting the <i>org.omg.CORBA.ORBInitialPort</i> property to the new port number when creating the ORB object. </p>
<h3>Running the server and client on different hosts</h3>
<p>In most of the Java IDL and RMI-IIOP tutorials, the Naming Service, Server, and Client are all running on the development machine. In real world deployment, it is likely that the client and server will run on different host machines than the Naming Service. </p>
<p> For the client and server to find the Naming Service, they must be made aware of the port number and host on which the naming service is running. Do this by setting the <i>org.omg.CORBA.ORBInitialPort</i> and <i>org.omg.CORBA.ORBInitialHost</i> properties in the client and server files to the machine name and port number on which the Naming Service is running. An example of this is shown in <i>The Hello World Example Using RMI-IIOP</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/rmi-iiop/rmiiiopexample.html.">http://java.sun.com/javase/6/docs/technotes/guides/rmi-iiop/rmiiiopexample.html.</a> You could also use the command line options <i>-ORBInitialPort</i> <i>nameserverport#</i> and <i>-ORBInitialHost</i> <i>nameserverhostname</i> to tell the client and server where to find the Naming Service. <i>Java IDL: Running the Hello World Example on TWO Machines</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/guides/idl/tutorial/jidl2machines.html">http://java.sun.com/javase/6/docs/technotes/guides/idl/tutorial/jidl2machines.html</a> shows one way of doing this using the command line option. </p>
<p> For example, suppose the Transient Naming Service, <i>tnameserv</i> is running on port 1050 on host <i>nameserverhost</i>. The client is running on host <i>clienthost</i> and the server is running on host <i>serverhost</i>. </p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>o</p>
<dd>Start <i>tnameserv</i> on the host <i>nameserverhost</i>, as follows: </p>
<pre><code> tnameserv -ORBInitialPort 1050</code></pre>
<dt>o</p>
<dd>Start the server on the <i>serverhost</i>, as follows: </p>
<pre><code> java Server -ORBInitialPort 1050 -ORBInitialHost nameserverhost</code></pre>
<dt>o</p>
<dd>Start the client on the <i>clienthost</i>, as follows: </p>
<pre><code> java Client -ORBInitialPort 1050 -ORBInitialHost nameserverhost</code></pre>
</dl>
</dl>
<h3>The -J option</h3>
<p>This command-line option is available for use with <i>tnameserve</i>:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>-Joption</p>
<dd>Pass <i>option</i> to the Java virtual machine, where <i>option</i> is one of the options described on the reference page for the <i>java application launcher</i> @ <a rel="nofollow" href="http://java.sun.com/javase/6/docs/technotes/tools/solaris/java.html.">http://java.sun.com/javase/6/docs/technotes/tools/solaris/java.html.</a> For example, <code>-J-Xms48m</code> sets the startup memory to 48 megabytes. It is a common convention for <code>-J</code> to pass options to the underlying virtual machine.</dl>
</dl>
<h2>Stopping the Java IDL Transient Naming Service</h2>
<p>To stop the Java IDL naming service, use the relevant operating system command, such as <i>kill</i> for a Unix process, or <i>Ctrl-C</i> for a Windows process. The naming service will continue to wait for invocations until it is explicitly shutdown. Note that names registered with the Java IDL naming service disappear when the service is terminated. </p>
<h2>Sample Client: Adding Objects to the Namespace</h2>
<p>The following sample program illustrates how to add names to the namespace. It is a self-contained Transient Naming Service client that creates the following simple tree. </p>
<pre><tt>Initial</tt><tt>Naming Context</tt><code>
 / \
 / \
 plans </code><tt>Personal</tt><code>
 / \
 / \
 calendar schedule</code></pre>
<p>In this example, <code>plans</code> is an object reference and <code>Personal</code> is a naming context that contains two object references: <code>calendar</code> and <code>schedule</code>. </p>
<pre><code>import java.util.Properties;
import org.omg.CORBA.*;
import org.omg.CosNaming.*;
public class NameClient
{
 public static void main(String args[])
 {
 try {</code></pre>
<p>In the above section, Starting the Java IDL Transient Naming Service, the nameserver was started on port 1050. The following code ensures that the client program is aware of this port number. </p>
<pre><code> Properties props = new Properties();
 props.put(&quot;org.omg.CORBA.ORBInitialPort&quot;, &quot;1050&quot;);
 ORB orb = ORB.init(args, props);</code></pre>
<p>This code obtains the initial naming context and assigns it to <code>ctx</code>. The second line copies <code>ctx</code> into a dummy object reference <code>objref</code> that we&#8217;ll attach to various names and add into the namespace. </p>
<pre><code> NamingContext ctx =
NamingContextHelper.narrow(orb.resolve_initial_references(&quot;NameService&quot;));
 NamingContext objref = ctx;</code></pre>
<p>This code creates a name &quot;plans&quot; of type &quot;text&quot; and binds it to our dummy object reference. &quot;plans&quot; is then added under the initial naming context using <i>rebind</i>. The <i>rebind</i> method allows us to run this program over and over again without getting the exceptions we&#8217;d get from using <i>bind</i>. </p>
<pre><code> NameComponent nc1 = new NameComponent(&quot;plans&quot;, &quot;text&quot;);
 NameComponent[] name1 = {nc1};
 ctx.rebind(name1, objref);
 System.out.println(&quot;plans rebind sucessful!&quot;);</code></pre>
<p>This code creates a naming context called &quot;Personal&quot; of type &quot;directory&quot;. The resulting object reference, <code>ctx2</code>, is bound to the name and added under the initial naming context. </p>
<pre><code> NameComponent nc2 = new NameComponent(&quot;Personal&quot;, &quot;directory&quot;);
 NameComponent[] name2 = {nc2};
 NamingContext ctx2 = ctx.bind_new_context(name2);
 System.out.println(&quot;new naming context added..&quot;);</code></pre>
<p>The remainder of the code binds the dummy object reference using the names &quot;schedule&quot; and &quot;calendar&quot; under the &quot;Personal&quot; naming context (<code>ctx2</code>). </p>
<pre><code> NameComponent nc3 = new NameComponent(&quot;schedule&quot;, &quot;text&quot;);
 NameComponent[] name3 = {nc3};
 ctx2.rebind(name3, objref);
 System.out.println(&quot;schedule rebind sucessful!&quot;);
 NameComponent nc4 = new NameComponent(&quot;calender&quot;, &quot;text&quot;);
 NameComponent[] name4 = {nc4};
 ctx2.rebind(name4, objref);
 System.out.println(&quot;calender rebind sucessful!&quot;);
 } catch (Exception e) {
 e.printStackTrace(System.err);
 }
 }
}</code></pre>
<h2>Sample Client: Browsing the Namespace</h2>
<p>The following sample program illustrates how to browse the namespace. </p>
<pre><code>import java.util.Properties;
import org.omg.CORBA.*;
import org.omg.CosNaming.*;
public class NameClientList
{
 public static void main(String args[])
 {
 try {</code></pre>
<p>In the above section, Starting the Java IDL Transient Naming Service, the nameserver was started on port 1050. The following code ensures that the client program is aware of this port number. </p>
<pre><code> Properties props = new Properties();
 props.put(&quot;org.omg.CORBA.ORBInitialPort&quot;, &quot;1050&quot;);
 ORB orb = ORB.init(args, props);</code></pre>
<p>The following code obtains the intial naming context. </p>
<pre><code> NamingContext nc =
NamingContextHelper.narrow(orb.resolve_initial_references(&quot;NameService&quot;));</code></pre>
<p>The <i>list</i> method lists the bindings in the naming context. In this case, up to 1000 bindings from the initial naming context will be returned in the BindingListHolder; any remaining bindings are returned in the BindingIteratorHolder. </p>
<pre><code> BindingListHolder bl = new BindingListHolder();
 BindingIteratorHolder blIt= new BindingIteratorHolder();
 nc.list(1000, bl, blIt);</code></pre>
<p>This code gets the array of bindings out of the returned BindingListHolder. If there are no bindings, the program ends. </p>
<pre><code> Binding bindings[] = bl.value;
 if (bindings.length == 0) return;</code></pre>
<p>The remainder of the code loops through the bindings and prints the names out. </p>
<pre><code> for (int i=0; i &lt; bindings.length; i++) {
 // get the object reference for each binding
 org.omg.CORBA.Object obj = nc.resolve(bindings[i].binding_name);
 String objStr = orb.object_to_string(obj);
 int lastIx = bindings[i].binding_name.length-1;
 // check to see if this is a naming context
 if (bindings[i].binding_type == BindingType.ncontext) {
 System.out.println( &quot;Context: &quot; +
bindings[i].binding_name[lastIx].id);
 } else {
 System.out.println(&quot;Object: &quot; +
bindings[i].binding_name[lastIx].id);
 }
 }
 } catch (Exception e) {
 e.printStackTrace(System.err);
 }
 }
}</code></pre>
<p>&nbsp;<wbr></p>
