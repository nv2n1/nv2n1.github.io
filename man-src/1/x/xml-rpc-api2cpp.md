---
title: "xml-rpc-api2cpp(1)"
name: "xml-rpc-api2cpp"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml-rpc-api2cpp/"
description: "xml-rpc-api2cpp – Make a C++ wrapper class for an XML-RPC API"
---

<h2 class="name">NAME</h2>
<p> xml-rpc-api2cpp &#8211; Make a C++ wrapper class for an XML-RPC API </p>
<h2>SYNOPSIS</h2>
<p> <code>xml-rpc-api2cpp</code> <i>server-url</i> <i>remote-method-prefix</i> <i>c++-class-name</i></p>
<h2>DESCRIPTION</h2>
<p> xml-rpc-api2cpp queries an XML-RPC server using the XML-RPC Instrospection API designed by Edd Dumbill. It then prints a C++ wrapper class to standard output. This class can be used with xmlrpc-c&#8217;s C++ API. </p>
<p> You can find a list of supported XML-RPC server libraries (and patches for many others) at <code><a rel="nofollow" href="http://xmlrpc-c.sourceforge.net/hacks.php">http://xmlrpc-c.sourceforge.net/hacks.php</a></code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>server-url</i></p>
<dd> The name of the server to query. Try <code><a rel="nofollow" href="http://xmlrpc-c.sourceforge.net/cgi-bin/interop.cgi">http://xmlrpc-c.sourceforge.net/cgi-bin/interop.cgi</a></code>.</p>
<dt><i>remote-method-prefix</i></p>
<dd> The prefix of the methods to wrap. For example, to wrap all the system.* calls, you could specify &quot;system&quot;.</p>
<dt><i>c++-class-name</i></p>
<dd> The name of the C++ class to generate. Try &quot;SystemProxy&quot;.</dl>
<h2>BUGS</h2>
<p> xml-rpc-api2cpp can&#8217;t talk to certain PHP servers based on Edd Dumbill&#8217;s PHP library, because the trailing bytes of the XML-RPC message get truncated in HTTP pipelining mode. It&#8217;s not clear whether this is a PHP, Apache or w3c-libwww bug. </p>
<p> xml-rpc-api2cpp assumes that method descriptions are ASCII text, not HTML as specified in the standard. (In practice, both conventions are often seen.) It may also get unhappy if method descriptions contain &quot;*/&quot;. </p>
<p> In general, error messages and diagnostics are still fairly poor.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-xmlrpc-c/">xmlrpc-c</a></code>(7), <code><a href="/docs/linux/man/1-xml-rpc-api2txt/">xml-rpc-api2txt</a></code>(1). </p>
<p> This program is part of xmlrpc-c.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Eric Kidd &lt;eric.kidd [at] pobox.com&gt;. It may be distributed under the same terms as the rest of xmlrpc-c. </p>
<h2>Index</h2>
