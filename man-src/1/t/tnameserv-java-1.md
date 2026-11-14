---
title: "tnameserv-java-1(1)"
name: "tnameserv-java-1"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tnameserv-java-1/"
description: "tnameserv – Interface Definition Language (IDL)."
---

<h2>NAME</h2>
<p> tnameserv &#8211; Interface Definition Language (IDL).</p>
<h2>SYNOPSIS</h2>
<pre>
<code>tnameserve</code> <code>-ORBInitialPort</code> [ <i>nameserverport</i> ]
</pre>
<dl>
<dt>-ORBInitialPort <i>nameserverport</i></p>
<dd>
 The initial port where the naming service listens for the bootstrap protocol used to implement the ORB <code>resolve_initial_references</code> and <code>list_initial_references</code> methods.</dl>
<h2>DESCRIPTION</h2>
<p> Java IDL includes the Object Request Broker Daemon (ORBD). ORBD is a daemon process that contains a Bootstrap Service, a Transient Naming Service, a Persistent Naming Service, and a Server Manager. The Java IDL tutorials all use ORBD, but you can substitute the <code>tnameserv</code> command for the <code>orbd</code> command in any of the examples that use a Transient Naming Service. </p>
<p> See <a href="/docs/linux/man/1-orbd/">orbd</a>(1) or Naming Service at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlNaming.html">http://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlNaming.html</a> </p>
<p> The CORBA Common Object Services (COS) Naming Service provides a tree-structure directory for object references similar to a file system that provides a directory structure for files. The Transient Naming Service provided with Java IDL, <code>tnameserv</code>, is a simple implementation of the COS Naming Service specification. </p>
<p> Object references are stored in the name space by name and each object reference-name pair is called a name binding. Name bindings can be organized under naming contexts. Naming contexts are name bindings and serve the same organizational function as a file system subdirectory. All bindings are stored under the initial naming context. The initial naming context is the only persistent binding in the name space. The rest of the name space is lost when the Java IDL naming service process stops and restarts. </p>
<p> For an applet or application to use COS naming, its ORB must know the port of a host running a naming service or have access to an initial naming context string for that naming service. The naming service can either be the Java IDL naming service or another COS-compliant naming service.</p>
<h3>START THE NAMING SERVICE</h3>
<p> You must start the Java IDL naming service before an application or applet that uses its naming service. Installation of the Java IDL product creates a script (Oracle Solaris: <code>tnameserv</code>) or executable file (Windows: <code>tnameserv.exe</code>) that starts the Java IDL naming service. Start the naming service so it runs in the background. </p>
<p> If you do not specify otherwise, then the Java IDL naming service listens on port 900 for the bootstrap protocol used to implement the ORB <code>resolve_initial_references</code> and <code>list_initial_references methods</code>, as follows: </p>
<pre>
<code>tnameserv -ORBInitialPort nameserverport&amp;</code>
</pre>
<p> If you do not specify the name server port, then port 900 is used by default. When running Oracle Solaris software, you must become the root user to start a process on a port below 1024. For this reason, it is recommended that you use a port number greater than or equal to 1024. To specify a different port, for example, 1050, and to run the naming service in the background, from a UNIX command shell, enter: </p>
<pre>
<code>tnameserv -ORBInitialPort 1050&amp;</code>
</pre>
<p> From an MS-DOS system prompt (Windows), enter: </p>
<pre>
<code>start tnameserv -ORBInitialPort 1050</code>
</pre>
<p> Clients of the name server must be made aware of the new port number. Do this by setting the <code>org.omg.CORBA.ORBInitialPort</code> property to the new port number when you create the ORB object.</p>
<h3>RUN THE SERVER AND CLIENT ON DIFFERENT HOSTS</h3>
<p> In most of the Java IDL and RMI-IIOP tutorials, the naming service, server, and client are all running on the development machine. In real-world deployment, the client and server probably run on different host machines from the Naming Service. </p>
<p> For the client and server to find the Naming Service, they must be made aware of the port number and host on which the naming service is running. Do this by setting the <code>org.omg.CORBA.ORBInitialPort</code> and <code>org.omg.CORBA.ORBInitialHost</code> properties in the client and server files to the machine name and port number on which the Naming Service is running. An example of this is shown in Getting Started Using RMI-IIOP at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/rmi-iiop/rmiiiopexample.html">http://docs.oracle.com/javase/8/docs/technotes/guides/rmi-iiop/rmiiiopexample.html</a> </p>
<p> You could also use the command-line options <code>-ORBInitialPort nameserverport#</code> and <code>-ORBInitialHost nameserverhostname</code> to tell the client and server where to find the naming service. For one example of doing this using the command-line option, see Java IDL: The Hello World Example on Two Machines at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/idl/tutorial/jidl2machines.html">http://docs.oracle.com/javase/8/docs/technotes/guides/idl/tutorial/jidl2machines.html</a> </p>
<p> For example, suppose the Transient Naming Service, <code>tnameserv</code> is running on port 1050 on host <code>nameserverhost</code>. The client is running on host <code>clienthost,</code> and the server is running on host <code>serverhost</code>. </p>
<p> Start <code>tnameserv</code> on the host <code>nameserverhost</code>: </p>
<pre>
<code>tnameserv -ORBInitialPort 1050</code>
</pre>
<p> Start the server on the <code>serverhost</code>: </p>
<pre>
<code>java Server -ORBInitialPort 1050 -ORBInitialHost nameserverhost</code>
</pre>
<p> Start the client on the <code>clienthost</code>: </p>
<pre>
<code>java Client -ORBInitialPort 1050 -ORBInitialHost nameserverhost</code>
</pre>
<h3>STOP THE NAMING SERVICE</h3>
<p> To stop the Java IDL naming service, use the relevant operating system command, such as <code>kill</code> for a Unix process or <code>Ctrl+C</code> for a Windows process. The naming service continues to wait for invocations until it is explicitly shut down. Note that names registered with the Java IDL naming service disappear when the service is terminated.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-J<i>option</i></p>
<dd>
 Passes <code>option</code> to the Java Virtual Machine, where <code>option</code> is one of the options described on the reference page for the Java application launcher. For example, <code>-J-Xms48m</code> sets the startup memory to 48 MB. See <a href="/docs/linux/man/1-java/">java</a>(1).</dl>
<h2>EXAMPLES</h2>
<h3>ADD OBJECTS TO THE NAME SPACE</h3>
<p> The following example shows how to add names to the name space. It is a self-contained Transient Naming Service client that creates the following simple tree. </p>
<pre>
<code>Initial Naming Context</code>
</pre>
<pre>
<code>     plans</code>
</pre>
<pre>
<code>     Personal</code>
</pre>
<pre>
<code>          calendar</code>
</pre>
<pre>
<code>          schedule</code>
</pre>
<p> In this example, <code>plans</code> is an object reference and <code>Personal</code> is a naming context that contains two object references: <code>calendar</code> and <code>schedule</code>. </p>
<pre>
<code>import java.util.Properties;</code>
</pre>
<pre>
<code>import org.omg.CORBA.*;</code>
</pre>
<pre>
<code>import org.omg.CosNaming.*;</code>
</pre>
<pre>
<code>public class NameClient {</code>
</pre>
<pre><code>
public
static void main(String args[])
{
</code></pre>
<pre>
<code>        try {</code>
</pre>
<p> In Start the Naming Service, the <code>nameserver</code> was started on port 1050. The following code ensures that the client program is aware of this port number. </p>
<pre>
<code>            Properties props = new Properties();</code>
</pre>
<pre>
<code>            props.put(&quot;org.omg.CORBA.ORBInitialPort&quot;, &quot;1050&quot;);</code>
</pre>
<pre>
<code>            ORB orb = ORB.init(args, props);</code>
</pre>
<p> This code obtains the initial naming context and assigns it to <code>ctx</code>. The second line copies <code>ctx</code> into a dummy object reference <code>objref</code> that is attached to various names and added into the name space. </p>
<pre>
<code>            NamingContext ctx =</code>
</pre>
<pre>
<code>                NamingContextHelper.narrow(</code>
</pre>
<pre>
<code>                    orb.resolve_initial_references(&quot;NameService&quot;));</code>
</pre>
<pre>
<code>             NamingContext objref = ctx;</code>
</pre>
<p> This code creates a name <code>plans</code> of type <code>text</code> and binds it to the dummy object reference. <code>plans</code> is then added under the initial naming context using the <code>rebind</code> method. The <code>rebind</code> method enables you to run this program over and over again without getting the exceptions from using the <code>bind</code> method. </p>
<pre>
<code>            NameComponent nc1 = new NameComponent(&quot;plans&quot;, &quot;text&quot;);</code>
</pre>
<p>NameComponent[] name1 = {nc1};</p>
<pre>
<code>            ctx.rebind(name1, objref);</code>
</pre>
<pre>
<code>            System.out.println(&quot;plans rebind successful!&quot;);</code>
</pre>
<p> This code creates a naming context called <code>Personal</code> of type <code>directory</code>. The resulting object reference, <code>ctx2</code>, is bound to the <code>name</code> and added under the initial naming context. </p>
<pre>
<code>            NameComponent nc2 = new NameComponent(&quot;Personal&quot;, &quot;directory&quot;);</code>
</pre>
<p>NameComponent[] name2 = {nc2};</p>
<pre>
<code>            NamingContext ctx2 = ctx.bind_new_context(name2);</code>
</pre>
<pre>
<code>            System.out.println(&quot;new naming context added..&quot;);</code>
</pre>
<p> The remainder of the code binds the dummy object reference using the names <code>schedule</code> and <code>calendar</code> under the <code>Personal</code> naming context (<code>ctx2</code>). </p>
<pre>
<code>            NameComponent nc3 = new NameComponent(&quot;schedule&quot;, &quot;text&quot;);</code>
</pre>
<p>NameComponent[] name3 = {nc3};</p>
<pre>
<code>            ctx2.rebind(name3, objref);</code>
</pre>
<pre>
<code>            System.out.println(&quot;schedule rebind successful!&quot;);</code>
</pre>
<pre>
<code>            NameComponent nc4 = new NameComponent(&quot;calender&quot;, &quot;text&quot;);</code>
</pre>
<p>NameComponent[] name4 = {nc4};</p>
<pre>
<code>            ctx2.rebind(name4, objref);</code>
</pre>
<pre>
<code>            System.out.println(&quot;calender rebind successful!&quot;);</code>
</pre>
<pre>
<code>        } catch (Exception e) {</code>
</pre>
<pre>
<code>            e.printStackTrace(System.err);</code>
</pre>
<pre>
<code>        }</code>
</pre>
<pre>
<code>    }</code>
</pre>
<pre>
<code>}</code>
</pre>
<h3>BROWSING THE NAME SPACE</h3>
<p> The following sample program shoes how to browse the name space. </p>
<pre>
<code>import java.util.Properties;</code>
</pre>
<pre>
<code>import org.omg.CORBA.*;</code>
</pre>
<pre>
<code>import org.omg.CosNaming.*;</code>
</pre>
<pre>
<code>public class NameClientList {</code>
</pre>
<p>public<br />
static void main(String args[])<br />
{</p>
<pre>
<code>        try {</code>
</pre>
<p> In Start the Naming Service, the <code>nameserver</code> was started on port 1050. The following code ensures that the client program is aware of this port number. </p>
<pre>
<code>            Properties props = new Properties();</code>
</pre>
<pre>
<code>            props.put(&quot;org.omg.CORBA.ORBInitialPort&quot;, &quot;1050&quot;);</code>
</pre>
<pre>
<code>            ORB orb = ORB.init(args, props);</code>
</pre>
<p> The following code obtains the initial naming context. </p>
<pre>
<code>            NamingContext nc =</code>
</pre>
<pre>
<code>            NamingContextHelper.narrow(</code>
</pre>
<pre>
<code>                orb.resolve_initial_references(&quot;NameService&quot;));</code>
</pre>
<p> The <code>list</code> method lists the bindings in the naming context. In this case, up to 1000 bindings from the initial naming context will be returned in the <code>BindingListHolder</code>; any remaining bindings are returned in the <code>BindingIteratorHolder</code>. </p>
<pre>
<code>            BindingListHolder bl = new BindingListHolder();</code>
</pre>
<pre>
<code>            BindingIteratorHolder blIt= new BindingIteratorHolder();</code>
</pre>
<pre>
<code>            nc.list(1000, bl, blIt);</code>
</pre>
<p> This code gets the array of bindings out of the returned <code>BindingListHolder</code>. If there are no bindings, then the program ends. </p>
<pre>
<code>            Binding bindings[] = bl.value;</code>
</pre>
<p>if (bindings.length == 0)<br />
    return;</p>
<p> The remainder of the code loops through the bindings and prints outs the names. </p>
<p>for (int i = 0; i &lt; bindings.length; i++) {</p>
<pre>
<code>                // get the object reference for each binding</code>
</pre>
<pre>
<code>                org.omg.CORBA.Object obj = nc.resolve(bindings[i].binding_name);</code>
</pre>
<pre>
<code>                String objStr = orb.object_to_string(obj);</code>
</pre>
<p>int lastIx = bindings[i].binding_name.length &#8211; 1;</p>
<pre>
<code>                // check to see if this is a naming context</code>
</pre>
<p>if (bindings[i].binding_type == BindingType.ncontext) {</p>
<pre>
<code>                    System.out.println(&quot;Context: &quot; +</code>
</pre>
<p>                        bindings[i].binding_name[lastIx].id);</p>
<pre>
<code>                } else {</code>
</pre>
<pre>
<code>                    System.out.println(&quot;Object: &quot; +</code>
</pre>
<pre><code>
                        bindings[i].binding_name[lastIx].id);
</code></pre>
<pre>
<code>                }</code>
</pre>
<pre>
<code>            }</code>
</pre>
<pre>
<code>        } catch (Exception e) {</code>
</pre>
<pre>
<code>            e.printStackTrace(System.err)</code>
</pre>
<pre>
<code>        }</code>
</pre>
<pre>
<code>    }</code>
</pre>
<pre>
<code>}</code>
</pre>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <a href="/docs/linux/man/1-orbd/">orbd</a>(1) </p>
</dl>
<h2>Index</h2>
