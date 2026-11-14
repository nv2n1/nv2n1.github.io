---
title: "xml-rpc-api2txt(1)"
name: "xml-rpc-api2txt"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml-rpc-api2txt/"
description: "xml-rpc-api2txt – Print out a description of an XML-RPC API as text"
---

<h2 class="name">NAME</h2>
<p> xml-rpc-api2txt &#8211; Print out a description of an XML-RPC API as text </p>
<h2>SYNOPSIS</h2>
<p> <code>xml-rpc-api2txt</code> <i>server-url</i></p>
<h2>DESCRIPTION</h2>
<p> xml-rpc-api2txt queries an XML-RPC server using the XML-RPC Instrospection API designed by Edd Dumbill. It then prints the results to standard output in a nicely formatted form, suitable for sending via e-mail. </p>
<p> You can find a list of supported XML-RPC server libraries (and patches for many others) at <code><a rel="nofollow" href="http://xmlrpc-c.sourceforge.net/hacks.php">http://xmlrpc-c.sourceforge.net/hacks.php</a></code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>server-url</i></p>
<dd> The name of the server to query. Try <code><a rel="nofollow" href="http://xmlrpc-c.sourceforge.net/cgi-bin/interop.cgi">http://xmlrpc-c.sourceforge.net/cgi-bin/interop.cgi</a></code>.</dl>
<h2>BUGS</h2>
<p> xml-rpc-api2txt assumes that method descriptions are ASCII text, not HTML as specified in the standard. (In practice, both conventions are often seen.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-xmlrpc-c/">xmlrpc-c</a></code>(7), <code><a href="/docs/linux/man/1-xml-rpc-api2cpp/">xml-rpc-api2cpp</a></code>(1). </p>
<p> This program is part of xmlrpc-c.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Eric Kidd &lt;eric.kidd [at] pobox.com&gt;. It may be distributed under the same terms as the rest of xmlrpc-c. </p>
<h2>Index</h2>
