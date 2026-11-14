---
title: "tsocks(5)"
name: "tsocks"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tsocks/"
description: "tsocks.conf – configuration file for"
---

<p><code>tsocks.conf</code> &#8211; configuration file for </p>
<p><a href="/docs/linux/man/8-tsocks/">tsocks</a>(8) </p>
<h2>Overview</h2>
<p>The configuration for tsocks can be anything from two lines to hundreds of lines based on the needs at any particular site. The basic idea is to define any networks the machine can access directly (i.e without the use of a SOCKS server) and define one or many SOCKS servers to be used to access other networks (including a &#8216;default&#8217; server). </p>
<p> Local networks are declared using the &#8216;local&#8217; keyword in the configuration file. When applications attempt to connect to machines in networks marked as local tsocks will not attempt to use a SOCKS server to negotiate the connection. </p>
<p> Obviously if a connection is not to a locally accessible network it will need to be proxied over a SOCKS server. However, many installations have several different SOCKS servers to be used to access different internal (and external) networks. For this reason the configuration file allows the definition of </p>
<p> Paths are declared as blocks in the configuration file. That is, they begin with a &#8216;path {&#8216; line in the configuration file and end with a &#8216;}&#8217; line. Inside this block directives should be used to declare a SOCKS server (as documented later in this manual page) and &#8216;reaches&#8217; directives should be used to declare networks and even destination ports in those networks that this server should be used to reach. N.B Each path MUST define a SOCKS server and contain one or more &#8216;reaches&#8217; directives. </p>
<p> SOCKS server declaration directives that are not contained within a &#8216;path&#8217; block define the default SOCKS server. If tsocks needs to connect to a machine via a SOCKS server (i.e it isn&#8217;t a network declared as &#8216;local&#8217;) and no &#8216;path&#8217; has declared it can reach that network via a &#8216;reaches&#8217; directive this server is used to negotiate the connection.</p>
<h2>Configuration Syntax</h2>
<p>The basic structure of all lines in the configuration file is: </p>
<dl>
<dd>&lt;directive&gt; = &lt;parameters&gt;</dl>
<p> The exception to this is &#8216;path&#8217; blocks which look like: </p>
<dl>
<dd>path {</p>
<dl>
<dd>&lt;directive&gt; = &lt;parameters&gt;</dl>
<p> }</dl>
<p> Empty lines are ignored and all input on a line after a &#8216;#&#8217; character is ignored.</p>
<h3>Directives</h3>
<p>The following directives are used in the tsocks configuration file: </p>
<dl>
<dt><i>server</i></p>
<dd>The IP address of the SOCKS server (e.g &quot;server = 10.1.4.253&quot;). Only one server may be specified per path block, or one outside a path block (to define the default server). Unless &#8211;disable-hostnames was specified to configure at compile time the server can be specified as a hostname (e.g &quot;server = socks.nec.com&quot;) </p>
<dt><i>server_port</i></p>
<dd>The port on which the SOCKS server receives requests. Only one server_port may be specified per path block, or one outside a path (for the default server). This directive is not required if the server is on the standard port (1080). </p>
<dt><i>server_type</i></p>
<dd>SOCKS version used by the server. Versions 4 and 5 are supported (but both for only the connect operation). The default is 4. Only one server_type may be specified per path block, or one outside a path (for the default server). </p>
<p> You can use the inspectsocks utility to determine the type of server, see the &#8216;UTILITIES&#8217; section later in this manual page. </p>
<dt><i>default_user</i></p>
<dd>This specifies the default username to be used for username and password authentication in SOCKS version 5. In order to determine the username to use (if the socks server requires username and password authentication) tsocks first looks for the environment variable TSOCKS_USERNAME, then looks for this configuration option, then tries to get the local username. This option is not valid for SOCKS version 4 servers. Only one default_user may be specified per path block, or one outside a path (for the default server) </p>
<dt><i>default_pass</i></p>
<dd>This specified the default password to be used for username and password authentication in SOCKS version 5. In order to determine the password to use (if the socks server requires username and password authentication) tsocks first looks for the environment variable TSOCKS_PASSWORD, then looks for this configuration option. This option is not valid for SOCKS version 4 servers. Onle one default_pass may be specified per path block, or one outside a path (for the default server) </p>
<dt><i>local</i></p>
<dd>An IP/Subnet pair specifying a network which may be accessed directly without proxying through a SOCKS server (e.g &quot;local = 10.0.0.0/255.0.0.0&quot;). Obviously all SOCKS server IP addresses must be in networks specified as local, otherwise tsocks would need a SOCKS server to reach SOCKS servers. </p>
<dt><i>reaches</i></p>
<dd>This directive is only valid inside a path block. Its parameter is formed as IP[:startport[-endport]]/Subnet and it specifies a network (and a range of ports on that network) that can be accessed by the SOCKS server specified in this path block. For example, in a path block &quot;reaches = 150.0.0.0:80-1024/255.0.0.0&quot; indicates to tsocks that the SOCKS server specified in the current path block should be used to access any IPs in the range 150.0.0.0 to 150.255.255.255 when the connection request is for ports 80-1024. </p>
</dl>
<h2>Utilities</h2>
<p>tsocks comes with two utilities that can be useful in creating and verifying the tsocks configuration file. </p>
<dl>
<dt>inspectsocks</p>
<dd>inspectsocks can be used to determine the SOCKS version that a server supports. Inspectsocks takes as its arguments the ip address/hostname of the SOCKS server and optionally the port number for socks (e.g &#8216;inspectsocks socks.nec.com 1080&#8217;). It then inspects that server to attempt to determine the version that server supports. </p>
<dt>validateconf</p>
<dd>validateconf can be used to verify the configuration file. It checks the format of the file and also the contents for errors. Having read the file it dumps the configuration to the screen in a formatted, readable manner. This can be extremely useful in debugging problems. </p>
<p> validateconf can read a configuration file from a location other than the location specified at compile time with the -f &lt;filename&gt; command line option. </p>
<p> Normally validateconf simply dumps the configuration read to the screen (in a nicely readable format), however it also has a useful &#8216;test&#8217; mode. When passed a hostname/ip on the command line like -t &lt;hostname/ip&gt;, validateconf determines which of the SOCKS servers specified in the configuration file would be used by tsocks to access the specified host. </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tsocks/">tsocks</a>(8) </p>
<h2>Author</h2>
<p>Shaun Clowes (delius [at] progsoc.uts.edu.au)</p>
<h2>Copyright</h2>
<p>Copyright 2000 Shaun Clowes </p>
<p> tsocks and its documentation may be freely copied under the terms and conditions of version 2 of the GNU General Public License, as published by the Free Software Foundation (Cambridge, Massachusetts, United States of America). </p>
<p> This documentation is based on the documentation for logwrites, another shared library interceptor. One line of code from it was used in tsocks and a lot of the documentation :) logwrites is by adam [at] yggdrasil.com (Adam J. Richter) and can be had from <a href="ftp://ftp.yggdrasil.com">ftp.yggdrasil.com</a> pub/dist/pkg</p>
