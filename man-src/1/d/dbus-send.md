---
title: "dbus-send(1)"
name: "dbus-send"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbus-send/"
description: "dbus-send – Send a message to a message bus"
---

<h2 class="name">NAME</h2>
<p> dbus-send &#8211; Send a message to a message bus </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dbus-send</code> [&#8211;system | &#8211;session | &#8211;bus=<i>ADDRESS</i> | &#8211;peer=<i>ADDRESS</i>] [&#8211;dest=<i>NAME</i>] [&#8211;print-reply&nbsp;[<i>=literal</i>]] [&#8211;reply-timeout=<i>MSEC</i>] [&#8211;type=<i>TYPE</i>] <i>OBJECT_PATH</i> <i>INTERFACE.MEMBER</i> [<i>CONTENTS</i>&#8230;]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dbus-send</code> command is used to send a message to a D-Bus message bus. See m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] for more information about the big picture. </p>
<p> There are two well-known message buses: the systemwide message bus (installed on many systems as the &quot;messagebus&quot; service) and the per-user-login-session message bus (started each time a user logs in). The <code>&#8211;system</code> and <code>&#8211;session</code> options direct <code>dbus-send</code> to send messages to the system or session buses respectively. If neither is specified, <code>dbus-send</code> sends to the session bus. </p>
<p> Nearly all uses of <code>dbus-send</code> must provide the <code>&#8211;dest</code> argument which is the name of a connection on the bus to send the message to. If <code>&#8211;dest</code> is omitted, no destination is set. </p>
<p> The object path and the name of the message to send must always be specified. Following arguments, if any, are the message contents (message arguments). These are given as type-specified values and may include containers (arrays, dicts, and variants) as described below. </p>
<dl>
<dt>
<dd>
<pre><code>
&lt;contents&gt;   ::= &lt;item&gt; | &lt;container&gt; [ &lt;item&gt; | &lt;container&gt;...]
&lt;item&gt;       ::= &lt;type&gt;:&lt;value&gt;
&lt;container&gt;  ::= &lt;array&gt; | &lt;dict&gt; | &lt;variant&gt;
&lt;array&gt;      ::= array:&lt;type&gt;:&lt;value&gt;[,&lt;value&gt;...]
&lt;dict&gt;       ::= dict:&lt;type&gt;:&lt;type&gt;:&lt;key&gt;,&lt;value&gt;[,&lt;key&gt;,&lt;value&gt;...]
&lt;variant&gt;    ::= variant:&lt;type&gt;:&lt;value&gt;
&lt;type&gt;       ::= string | int16 | uint16 | int32 | uint32 | int64 | uint64 | double | byte | boolean | objpath
</code></pre>
</dl>
<p> D-Bus supports more types than these, but <code>dbus-send</code> currently does not. Also, <code>dbus-send</code> does not permit empty containers or nested containers (e.g. arrays of variants). </p>
<p> Here is an example invocation: </p>
<dl>
<dt>
<dd>
<pre>
  dbus-send --dest=org.freedesktop.ExampleName               \
            /org/freedesktop/sample/object/name              \
            org.freedesktop.ExampleInterface.ExampleMethod   \
            int32:47 string:'hello world' double:65.32       \
            array:string:&quot;1st item&quot;,&quot;next item&quot;,&quot;last item&quot;  \
            dict:string:int32:&quot;one&quot;,1,&quot;two&quot;,2,&quot;three&quot;,3      \
            variant:int32:-8                                 \
            objpath:/org/freedesktop/sample/object/name
</pre>
</dl>
<p> Note that the interface is separated from a method or signal name by a dot, though in the actual protocol the interface and the interface member are separate fields.</p>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>&#8211;dest=</code><i>NAME</i></p>
<dl>
<dt>
<dd> Specify the name of the connection to receive the message.</dl>
<p> <code>&#8211;print-reply</code></p>
<dl>
<dt>
<dd> Block for a reply to the message sent, and print any reply received in a human-readable form. It also means the message type (<code>&#8211;type=</code>) is <code>method_call</code>.</dl>
<p> <code>&#8211;print-reply=literal</code></p>
<dl>
<dt>
<dd> Block for a reply to the message sent, and print the body of the reply. If the reply is an object path or a string, it is printed literally, with no punctuation, escape characters etc.</dl>
<p> <code>&#8211;reply-timeout=</code><i>MSEC</i></p>
<dl>
<dt>
<dd> Wait for a reply for up to <i>MSEC</i> milliseconds. The default is implementation-defined, typically 25 seconds.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Send to the system message bus.</dl>
<p> <code>&#8211;session</code></p>
<dl>
<dt>
<dd> Send to the session message bus. (This is the default.)</dl>
<p> <code>&#8211;bus=</code><i>ADDRESS</i></p>
<dl>
<dt>
<dd> Register on a message bus at <i>ADDRESS</i>, typically a <code>dbus-daemon</code>.</dl>
<p> <code>&#8211;peer=</code><i>ADDRESS</i></p>
<dl>
<dt>
<dd> Send to a non-message-bus D-Bus server at <i>ADDRESS</i>. In this case <code>dbus-send</code> will not call the Hello method.</dl>
<p> <code>&#8211;type=</code><i>TYPE</i></p>
<dl>
<dt>
<dd> Specify <code>method_call</code> or <code>signal</code> (defaults to &quot;<code>signal</code>&quot;).</dl>
<h2>AUTHOR</h2>
<p> dbus-send was written by Philip Blundell.</p>
<h2>BUGS</h2>
<p> Please send bug reports to the D-Bus mailing list or bug tracker, see m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] </p>
<h2>Index</h2>
