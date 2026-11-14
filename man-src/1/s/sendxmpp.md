---
title: "sendxmpp(1)"
name: "sendxmpp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sendxmpp/"
description: "sendxmpp – send xmpp messages from the commandline."
---

<h2 class="name">NAME</h2>
<p> sendxmpp &#8211; send xmpp messages from the commandline. </p>
<h2>SYNOPSIS</h2>
<p> sendxmpp [options] &lt;recipient1&gt; [&lt;recipient2&gt; &#8230;] </p>
<p> sendxmpp &#8211;raw [options]</p>
<h2>DESCRIPTION</h2>
<p> sendxmpp is a program to send <font SIZE="-1">XMPP </font>(Jabber) messages from the commandline, not unlike <i><a href="/docs/linux/man/1-mail/">mail</a></i>(1). Messages can be sent both to individual recipients and chatrooms.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>,<code>&#8211;file</code> <i>file</i></p>
<dd> Use <i>file</i> configuration file instead of <i>~/.sendxmpprc</i></p>
<dt><code>-u</code>,<code>&#8211;username</code> <i>user</i></p>
<dd> Use <i>user</i> instead of the one in the configuration file</p>
<dt><code>-p</code>,<code>&#8211;password</code> <i>password</i></p>
<dd> Use <i>password</i> instead of the one in the configuration file</p>
<dt><code>&#8211;sso</code></p>
<dd> Instead of specifying username or password, attempt to use system level <font SIZE="-1">SSO </font>(e.g. kerberos) if supported.</p>
<dt><code>-j</code>,<code>&#8211;jserver</code> <i>server</i></p>
<dd> Use jabber <i>server</i> instead of the one in the configuration file.</p>
<dt><code>-o</code>,<code>&#8211;component</code> <i>componentname</i></p>
<dd> Use componentname in connect call. Seems needed for Google talk.</p>
<dt><code>-r</code>,<code>&#8211;resource</code> <i>res</i></p>
<dd> Use resource <i>res</i> for the sender [default: &#8216;sendxmpp&#8217;]; when sending to a chatroom, this determines the &#8216;alias&#8217;</p>
<dt><code>-t</code>,<code>&#8211;tls</code></p>
<dd> Connect securely, using <font SIZE="-1">TLS</font></p>
<dt><code>-e</code>,<code>&#8211;ssl</code></p>
<dd> Connect securely, using <font SIZE="-1">SSL</font></p>
<dt><code>-n</code>,<code>&#8211;no-tls-verify</code></p>
<dd> Deactivate the verification of <font SIZE="-1">SSL</font> certificates. Better way is to use parameter <code>&#8211;tls-ca-path</code> with the needed path to <font SIZE="-1">CA</font> certificates.</p>
<dt><code>-a</code>,<code>&#8211;tls-ca-path</code></p>
<dd> Path to your custom <font SIZE="-1">CA</font> certificates, so you can verificate <font SIZE="-1">SSL</font> certificates during connecting.</p>
<dt><code>-l</code>,<code>&#8211;headline</code></p>
<dd> Backward compatibility option. You should use <code>&#8211;message-type=headline</code> instead. Send a headline type message (not stored in offline messages)</p>
<dt><code>&#8211;messages-type</code></p>
<dd> Set type of message. Supported types are: <code>message chat headline</code>. Default message type is <code>message</code>. Headline type message can be set also with <code>&#8211;headline</code> option, see <code>&#8211;headline</code></p>
<dt><code>-c</code>,<code>&#8211;chatroom</code></p>
<dd> Send the message to a chatroom</p>
<dt><code>-s</code>,<code>&#8211;subject</code> <i>subject</i></p>
<dd> Set the subject for the message to <i>subject</i> [default: &#8221;]; when sending to a chatroom, this will set the subject for the chatroom</p>
<dt><code>-m</code>,<code>&#8211;message</code> <i>message</i></p>
<dd> Read the message from <i>message</i> (a file) instead of stdin</p>
<dt><code>-i</code>,<code>&#8211;interactive</code></p>
<dd> Work in interactive mode, reading lines from stdin and sending the one-at-time</p>
<dt><code>-w</code>,<code>&#8211;raw</code></p>
<dd> Send raw <font SIZE="-1">XML</font> message to jabber server</p>
<dt><code>-v</code>,<code>&#8211;verbose</code></p>
<dd> Give verbose output about what is happening</p>
<dt><code>-h</code>,<code>&#8211;help</code>,<code>&#8211;usage</code></p>
<dd> Show a &#8216;Usage&#8217; message</p>
<dt><code>-d</code>,<code>&#8211;debug</code></p>
<dd> Show debugging info while running. <font SIZE="-1"><code>WARNING</code></font>: This will include passwords etc. so be careful with the output! Specify multiple times to increase debug level.</dl>
<h2>CONFIGURATION FILE</h2>
<p> You may define a &#8216;<i>~/.sendxmpprc</i>&#8216; file with the necessary data for your xmpp-account. Since version 1.24 the following format is supported: </p>
<pre>
    username: I&lt;your_username&gt;
    jserver: I&lt;jabber_server&gt;
    port: I&lt;jabber_port&gt;
    password: I&lt;your_jabber_password&gt;
    component: I&lt;optional_component_name&gt;
</pre>
<p> Example for Google Talk servers: </p>
<pre>
    username: I&lt;lubomir.host&gt;
    jserver: I&lt;talk.google.com&gt;
    password: I&lt;my-secure-password&gt;
    component: I&lt;gmail.com&gt;
</pre>
<p> With version 1.23 and older only one-line format is supported: </p>
<dl>
<dt>
<dd> <i>user</i>@<i>server</i> <i>password</i> <i>componentname</i></dl>
<p> e.g.: </p>
<pre>
    # my account
    alice [at] jabber.org  secret
</pre>
<p> (&#8216;#&#8217; and newlines are allowed like in shellscripts). You can add a <i>host</i> (or <font SIZE="-1">IP</font> address) if it is different from the <i>server</i> part of your <font SIZE="-1">JID:</font> </p>
<pre>
    # account with specific connection host
    alice [at] myjabberserver.com;foo.com secret
</pre>
<p> You can also add a <i>port</i> if it is not the standard <font SIZE="-1">XMPP</font> port: </p>
<pre>
    # account with weird port number
    alice [at] myjabberserver.com:1234 secret
</pre>
<p> Of course, you may also mix the two: </p>
<pre>
    # account with a specific host and port
    alice [at] myjabberserver.com;foo.com:1234 secret
</pre>
<p> <font SIZE="-1"><code>NOTE</code></font>: for your security, sendxmpp demands that the configuration file is owned by you and readable only to you (permissions 600).</p>
<h2>EXAMPLE</h2>
<pre><code>
$ echo "hello bob!" | sendxmpp - s hello someone[at] jabber.org or to send to a chatroom : $ echo "Dinner Time" | sendxmpp - r TheCook-- chatroom test2[at] conference.jabber.org or to send your system logs somewhere, as new lines appear : $ tail - f / var / log / syslog | sendxmpp - i sysadmin[at] myjabberserver.com
                                                                                                                                                                                                                                                                                                NOTE : be careful not the overload public jabber services
</code></pre>
<h2>SEE ALSO</h2>
<p> Documentation for the Net::XMPP module </p>
<p> The jabber homepage: &lt;<a rel="nofollow" href="http://www.jabber.org/">http://www.jabber.org/</a>&gt; </p>
<p> The sendxmpp homepage: &lt;<a rel="nofollow" href="http://sendxmpp.hostname.sk">http://sendxmpp.hostname.sk</a>&gt;</p>
<h2>AUTHOR</h2>
<p> sendxmpp has been written by Dirk-Jan C. Binnema &lt;djcb [at] djcbsoftware.nl&gt;, and uses the Net::XMPP modules written by Ryan Eatmon. Current maintainer is Lubomir Host &lt;lubomir.host [at] gmail.com&gt;, &lt;<a rel="nofollow" href="http://blog.hostname.sk">http://blog.hostname.sk</a>&gt; </p>
<h2>Index</h2>
