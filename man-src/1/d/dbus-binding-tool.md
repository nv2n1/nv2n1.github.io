---
title: "dbus-binding-tool(1)"
name: "dbus-binding-tool"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbus-binding-tool/"
description: "dbus-binding-tool – C language GLib bindings generation utility."
---

<h2>NAME</h2>
<p> dbus-binding-tool &#8211; C language GLib bindings generation utility.</p>
<h2>SYNOPSIS</h2>
<p> <code>dbus-binding-tool</code> [-<code>-force</code>] [-<code>-help</code>] [-<code>-ignore-unsupported</code>] [-<code>-mode=</code><i>pretty|glib-client|glib-server</i>] [-<code>-output=</code><i>file</i>] [-<code>-prefix=</code><i>symbol-prefix</i>] [-<code>-version</code>] [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dbus-binding-tool</code> is used to expose a GObject via D-Bus. As input, <code>dbus-binding-tool</code> uses a D-Bus Introspection XML file. As output, the client-side or server-side bindings is generated. This output is a header file which eases the use of a remote D-Bus object. Output is sent to standard out or to the filename specified with the &#8211;<code>-output</code> argument.</p>
<h2>EXTENDED DESCRIPTION</h2>
<h3></h3>
<p> The following is a sample D-Bus Introspection XML file which describes an object that exposes one method, named ManyArgs: </p>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; ?&gt;
&lt;node name=&quot;/com/example/MyObject&quot;&gt;
  &lt;interface name=&quot;com.example.MyObject&quot;&gt;
    &lt;method name=&quot;ManyArgs&quot;&gt;
      &lt;arg type=&quot;u&quot; name=&quot;x&quot; direction=&quot;in&quot; /&gt;
      &lt;arg type=&quot;s&quot; name=&quot;str&quot; direction=&quot;in&quot; /&gt;
      &lt;arg type=&quot;d&quot; name=&quot;trouble&quot; direction=&quot;in&quot; /&gt;
      &lt;arg type=&quot;d&quot; name=&quot;d_ret&quot; direction=&quot;out&quot; /&gt;
      &lt;arg type=&quot;s&quot; name=&quot;str_ret&quot; direction=&quot;out&quot; /&gt;
    &lt;/method&gt;
  &lt;/interface&gt;
&lt;/node&gt;
</pre>
<p> <code>dbus-binding-tool</code> supports annotations in the XML format to further control how the bindings are generated.</p>
<h3>client-side bindings</h3>
<p> When building client-side bindings, the &#8211;<code>-mode=glib-client</code> argument is used. The client-side bindings support the &quot;org.freedesktop.DBus.Glib.NoReply&quot; annotation. This is specified within the &lt;method&gt; tag to indicate that the client is not expecting a reply to the method call, so a reply should not be sent. This is often used to speed up rapid method calls where there are no &quot;out&quot; arguments, and not knowing if the method succeeded is an acceptable compromise to halve the traffic on the bus. For example: </p>
<pre><code>
&lt;method name "FooMethod"&gt;
  [...]
  &lt;annotation name="org.freedesktop.DBus.GLib.NoReply" value="yes"/&gt;
  [...]
&lt;/method&gt;
</code></pre>
<h3>server-side bindings</h3>
<p> When building server-side bindings, the &#8211;<code>-mode=glib-server</code> argument is used. Also the &#8211;<code>-prefix</code> argument must be used when building server-side bindings so that functions in the generated output are prefexed with the specified value. The server-side bindings support the following annotations: </p>
<p> &quot;org.freedesktop.DBus.GLib.CSymbol&quot; </p>
<p> This annotation is used to specify the C symbol names for the various types (interface, method, etc.), if it differs from the name D-Bus generates. </p>
<p>&lt;interface name=&#8221;com.example.MyObject&#8221;&gt;<br />
  &lt;annotation name=&#8221;org.freedesktop.DBus.GLib.CSymbol&#8221; value=&#8221;my_object&#8221;/&gt;<br />
  [&#8230;]<br />
  &lt;method name &#8220;ManyArgs&#8221;&gt;<br />
    &lt;annotation name=&#8221;org.freedesktop.DBus.GLib.CSymbol&#8221; value=&#8221;my_object_many_args&#8221;/&gt;<br />
    [&#8230;]<br />
  &lt;/method&gt;<br />
&lt;/interface&gt;</p>
<p> &quot;org.freedesktop.DBus.GLib.Async&quot; </p>
<p> This annotation marks the method implementation as an asynchronous function, which does not return a response straight away but will send the response at some later point to complete the call. This is used to implement non-blocking services where method calls can take time. </p>
<p> When a method is asynchronous, the function prototype is different. It is required that the function conform to the following rules: </p>
<p> &bull; The function must return a value of type gboolean; TRUE on success, and FALSE otherwise. &bull; The first parameter is a pointer to an instance of the object. &bull; Following the object instance pointer are the method input values. &bull; The final parameter must be a (DBusGMethodInvocation *). This is used when sending the response message back to the client, by calling dbus_g_method_return or dbus_g_method_return_error. </p>
<p> For example: </p>
<pre><code>
&lt;method name "FooMethod"&gt;
  [...]
  &lt;annotation name="org.freedesktop.DBus.GLib.Async" value="yes"/&gt;
  [...]
&lt;/method&gt;
</code></pre>
<p> &quot;org.freedesktop.DBus.GLib.Const&quot; </p>
<p> This attribute can only be applied to &quot;out&quot; &lt;arg&gt; nodes, and specifies that the parameter is not being copied when returned. For example, this turns a &#8216;s&#8217; argument from a (char **) to a (const char **), and results in the argument not being freed by D-Bus after the message is sent. For example: </p>
<pre>
  &lt;arg type=&quot;u&quot; name=&quot;x&quot; direction=&quot;out&quot;&gt;
    &lt;annotation name=&quot;org.freedesktop.DBus.GLib.Const&quot; value=&quot;&quot;/&gt;
  &lt;/arg&gt;
</pre>
<p> &quot;org.freedesktop.DBus.GLib.ReturnVal&quot; </p>
<p> This attribute can only be applied to &quot;out&quot; &lt;arg&gt; nodes, and alters the expected function signature. It currently can be set to two values: &quot;&quot; or &quot;error&quot;. The argument marked with this attribute is not returned via a pointer argument, but by the function&#8217;s return value. If the attribute&#8217;s value is the empty string, the (GError *) argument is also omitted so there is no standard way to return an error value. This is very useful for interfacing with existing code, as it is possible to match existing APIs. If the attribute&#8217;s value is &quot;error&quot;, then the final argument is a (GError *) as usual. For example: </p>
<pre>
  &lt;arg type=&quot;u&quot; name=&quot;x&quot; direction=&quot;out&quot;&gt;
    &lt;annotation name=&quot;org.freedesktop.DBus.GLib.ReturnVal&quot; value=&quot;&quot;/&gt;
  &lt;/arg&gt;
</pre>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>&#8211;force</code> </p>
<p> Overwrite the output file if it already exists with a newer timestamp than the source files. </p>
<p> <code>&#8211;help</code> </p>
<p> Display usage information. </p>
<p> <code>&#8211;ignore-unsupported</code> </p>
<p> If set, then unsupported signatures for &lt;method&gt; parameters are ignored. </p>
<p> <code>&#8211;mode=</code><i>pretty|glib-client|glib-server</i> </p>
<p> If the value is &quot;glib-client&quot;, then client bindings are generated. If the value is &quot;glib-server&quot;, then server bindings are generated. If the value is &quot;pretty&quot;, then the output is in a more human readable format. </p>
<p> <code>&#8211;output=</code><i>file</i> </p>
<p> Specify the output <i>file</i>. </p>
<p> <code>&#8211;prefix=</code><i>symbol-prefix</i> </p>
<p> Functions in the generated output are prefixed with the <i>symbol-prefix</i> value. </p>
<p> <code>&#8211;version</code> </p>
<p> Display the version number of the <code>dbus-binding-tool</code> command. </p>
<h2>OPERANDS</h2>
<p> The following operands are supported: </p>
<p> <i>file</i> A list of one or more input D-Bus Introspection XML files to include in the generated output. </p>
<h2>FILES</h2>
<p> The following files are used by this application: </p>
<p> <code>/usr/bin/dbus-binding-tool</code> Executable for the D-Bus Binding Tool application. </p>
<h2>ATTRIBUTES</h2>
<p> See <code><a href="/docs/linux/man/5-attributes/">attributes</a></code>(5) for descriptions of the following attributes: </p>
<table BORDER>
<tr VALIGN=top>
<td ALIGN=center>ATTRIBUTE TYPE</td>
<td ALIGN=center>ATTRIBUTE VALUE
</td>
</tr>
<tr VALIGN=top>
<td>Availability</td>
<td>SUNWdbus-bindings
</td>
</tr>
<tr VALIGN=top>
<td>Interface stability</td>
<td>Volatile
</td>
</tr>
</table>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dbus-cleanup-sockets/">dbus-cleanup-sockets</a></code>(1), <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), <code><a href="/docs/linux/man/1-dbus-monitor/">dbus-monitor</a></code>(1), <code><a href="/docs/linux/man/1-dbus-send/">dbus-send</a></code>(1), <code><a href="/docs/linux/man/1-dbus-uuidgen/">dbus-uuidgen</a></code>(1), <code><a href="/docs/linux/man/3-libdbus-glib-1/">libdbus-glib-1</a></code>(3), <code><a href="/docs/linux/man/5-attributes/">attributes</a></code>(5)</p>
<h2>NOTES</h2>
<p> Written by Brian Cameron, Sun Microsystems Inc., 2009. </p>
<h2>Index</h2>
<dt><a href="#lbAI">OPTIONS</a></p>
<dd>
<dt><a href="#lbAJ">OPERANDS</a></p>
<dd>
<dt><a href="#lbAK">FILES</a></p>
<dd>
<dt><a href="#lbAL">ATTRIBUTES</a></p>
<dd>
<dt><a href="#lbAM">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAN">NOTES</a></p>
<dd></dl>
