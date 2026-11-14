---
title: "net-server(1)"
name: "net-server"
section: "1"
letter: "n"
url: "/docs/linux/man/1-net-server/"
---

<h2 class="name">NAME</h2>
 

 net-server - Base Net::Server starting module 

<h2>SYNOPSIS</h2>

 <pre><code>
net - server[base type][net server arguments] net - server PreFork ipv '*' net - server HTTP net - server HTTP app foo.cgi net - server HTTP app foo.cgi app /= bar.cgi
                                                                                                                                                                    net -
                                                                                                                                                                server HTTP port 8080 port 8443 / ssl ipv '*' server_type PreFork-- SSL_key_file = my.key-- SSL_cert_file = my.crt access_log_file STDERR
</code></pre>

<h2>DESCRIPTION</h2>

 The net-server program gives a simple way to test out code and try port connection parameters. Though the running server can be robust enough for full tim use, it is anticipated that this binary will just be used for basic testing of net-server ports, acting as a simple echo server, or for running development scripts as <font SIZE="-1">CGI.</font>

<h2>OPTIONS</h2>

<dl>
<dt>&quot;base type&quot;
<dd> The very first argument may be a Net::Server flavor. This is given as shorthand for writing out server_type ``ServerFlavor''. Additionally, this allows types such as <font SIZE="-1">HTTP</font> and <font SIZE="-1">PSGI,</font> which are not true Net::Server base types, to subclass other server types via an additional server_type argument. 

 <pre>
    net-server PreFork
    net-server HTTP  # becomes a HTTP server in the Fork flavor
    net-server HTTP server_type PreFork  # preforking HTTP server
</pre>
<dt>&quot;port&quot;
<dd> Port to bind upon. Default is 80 if running a <font SIZE="-1">HTTP</font> server as root, 8080 if running a <font SIZE="-1">HTTP</font> server as non-root, or 20203 otherwise. 

 Multiple value can be given for binding to multiple ports. All of the methods for specifying port attributes enumerated in Net::Server and Net::Server::Proto are available here. 

 <pre>
    net-server port 20201
    net-server port 20202
    net-server port 20203/IPv6
</pre>
<dt>&quot;host&quot;
<dd> Host to bind to. Default is *. Will bind to an IPv4 socket if an IPv4 address is given. Will bind to an IPv6 socket if an IPv6 address is given (requires installation of IO::Socket::INET6). 

 If a hostname is given and <tt>&quot;ipv&quot;</tt> is still set to 4, an IPv4 socket will be created. If a hostname is given and <tt>&quot;ipv&quot;</tt> is set to 6, an IPv6 socket will be created. If a hostname is given and <tt>&quot;ipv&quot;</tt> is set to * (default), a lookup will be performed and any available IPv4 or IPv6 addresses will be bound. The <tt>&quot;ipv&quot;</tt> parameter can be set directly, or passed along in the port, or additionally can be passed as part of the hostname. 

 <pre>
    net-server host localhost
    net-server host localhost/IPv4
</pre></dl>
 

 There are many more options available. Please see the Net::Server documentation.

<h2>AUTHOR</h2>

 <pre>
    Paul Seamons &lt;paul at seamons.com&gt;
</pre>

<h2>LICENSE</h2>

 This package may be distributed under the terms of either the 

 <pre>
  GNU General Public License
    or the
  Perl Artistic License
</pre> 

<h2>Index</h2>


