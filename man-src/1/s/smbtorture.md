---
title: "smbtorture(1)"
name: "smbtorture"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbtorture/"
description: "smbtorture – Run a series of tests against a SMB server"
---

<h2 class="name">NAME</h2>
<p> smbtorture &#8211; Run a series of tests against a SMB server </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>smbtorture</code> {//server/share} [-d debuglevel] [-U user%pass] [-k] [-N numprocs] [-n netbios_name] [-W workgroup] [-o num_operations] [-e num files(entries)] [-O socket_options] [-m maximum_protocol] [-L] [-c CLIENT.TXT] [-t timelimit] [-C filename] [-A] [-p port] [-s seed] [-f max_failures] [-X] {BINDING-STRING|UNC} {TEST1} [TEST2] [&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>smbtorture is a testsuite that runs several tests against a SMB server. All tests are known to succeed against a Windows 2003 server (?). Smbtorture&#8217;s primary goal is finding differences in implementations of the SMB protocol and testing SMB servers. </p>
<p> Any number of tests can be specified on the command-line. If no tests are specified, all tests are run. </p>
<p> If no arguments are specified at all, all available options and tests are listed.</p>
<h3>Binding string format</h3>
<p> The binding string format is: </p>
<p> TRANSPORT:host[flags] </p>
<p> Where TRANSPORT is either ncacn_np for SMB, ncacn_ip_tcp for RPC/TCP or ncalrpc for local connections. </p>
<p> &#8216;host&#8217; is an IP or hostname or netbios name. If the binding string identifies the server side of an endpoint, &#8216;host&#8217; may be an empty string. </p>
<p> &#8216;flags&#8217; can include a SMB pipe name if using the ncacn_np transport or a TCP port number if using the ncacn_ip_tcp transport, otherwise they will be auto-determined. </p>
<p> other recognised flags are: </p>
<p> sign</p>
<dl>
<dt>
<dd> enable ntlmssp signing</dl>
<p> seal</p>
<dl>
<dt>
<dd> enable ntlmssp sealing</dl>
<p> connect</p>
<dl>
<dt>
<dd> enable rpc connect level auth (auth, but no sign or seal)</dl>
<p> validate</p>
<dl>
<dt>
<dd> enable the NDR validator</dl>
<p> print</p>
<dl>
<dt>
<dd> enable debugging of the packets</dl>
<p> bigendian</p>
<dl>
<dt>
<dd> use bigendian RPC</dl>
<p> padcheck</p>
<dl>
<dt>
<dd> check reply data for non-zero pad bytes</dl>
<p> For example, these all connect to the samr pipe: </p>
<dl>
<dt>
<dd> &bull; ncacn_np:myserver</dl>
<dl>
<dt>
<dd> &bull; ncacn_np:myserver[samr]</dl>
<dl>
<dt>
<dd> &bull; ncacn_np:myserver[\pipe\samr]</dl>
<dl>
<dt>
<dd> &bull; ncacn_np:myserver[/pipe/samr]</dl>
<dl>
<dt>
<dd> &bull; ncacn_np:myserver[samr,sign,print]</dl>
<dl>
<dt>
<dd> &bull; ncacn_np:myserver[\pipe\samr,sign,seal,bigendian]</dl>
<dl>
<dt>
<dd> &bull; ncacn_np:myserver[/pipe/samr,seal,validate]</dl>
<dl>
<dt>
<dd> &bull; ncacn_np:</dl>
<dl>
<dt>
<dd> &bull; ncacn_np:[/pipe/samr]</dl>
<dl>
<dt>
<dd> &bull; ncacn_ip_tcp:myserver</dl>
<dl>
<dt>
<dd> &bull; ncacn_ip_tcp:myserver[1024]</dl>
<dl>
<dt>
<dd> &bull; ncacn_ip_tcp:myserver[1024,sign,seal]</dl>
<dl>
<dt>
<dd> &bull; ncalrpc:</dl>
<h3>UNC Format</h3>
<p> The UNC format is: </p>
<p> //server/share</p>
<h2>OPTIONS</h2>
<p> -d debuglevel</p>
<dl>
<dt>
<dd> Use the specified Samba debug level. A higher debug level means more output.</dl>
<p> -U user%pass</p>
<dl>
<dt>
<dd> Use the specified username/password combination when logging in to a remote server.</dl>
<p> -k</p>
<dl>
<dt>
<dd> Use kerberos when authenticating.</dl>
<p> -W workgroup</p>
<dl>
<dt>
<dd> Use specified name as our workgroup name.</dl>
<p> -n netbios_name</p>
<dl>
<dt>
<dd> Use specified name as our NetBIOS name.</dl>
<p> -O socket_options</p>
<dl>
<dt>
<dd> Use specified socket options, equivalent of the smb.conf option &#8220;socket options&#8221;. See the <a href="/docs/linux/man/5-smb-conf/">smb.conf</a>(5) manpage for details.</dl>
<p> -m max_protocol</p>
<dl>
<dt>
<dd> Specify the maximum SMB dialect that should be used. Possible values are: CORE, COREPLUS, LANMAN1, LANMAN2, NT1</dl>
<p> -s seed</p>
<dl>
<dt>
<dd> Initialize the randomizer using <i>seed</i> as seed.</dl>
<p> -L</p>
<dl>
<dt>
<dd> Use oplocks.</dl>
<p> -X</p>
<dl>
<dt>
<dd> Enable dangerous tests. Use with care! This might crash your server&#8230;</dl>
<p> -t timelimit</p>
<dl>
<dt>
<dd> Specify the NBENCH time limit in seconds. Defaults to 600.</dl>
<p> -p ports</p>
<dl>
<dt>
<dd> Specify ports to connect to.</dl>
<p> -c file</p>
<dl>
<dt>
<dd> Read NBENCH commands from <i>file</i> instead of from CLIENT.TXT.</dl>
<p> -A</p>
<dl>
<dt>
<dd> Show not just OK or FAILED but more detailed output. Used only by DENY test at the moment.</dl>
<p> -C filename</p>
<dl>
<dt>
<dd> Load a list of UNC names from the specified filename. Smbtorture instances will connect to a random host from this list.</dl>
<p> -N numprocs</p>
<dl>
<dt>
<dd> Specify number of smbtorture processes to launch.</dl>
<p> -o num_operations</p>
<dl>
<dt>
<dd> Number of times some operations should be tried before assuming they&#8217;re output is consistent (default:100).</dl>
<p> -e num_files</p>
<dl>
<dt>
<dd> Number of entries to use in certain tests (such as creating X files) (default: 1000).</dl>
<p> -f max_failures</p>
<dl>
<dt>
<dd> Number of failures before aborting a test (default: 1).</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 4.0 of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> Samba</p>
<h2>AUTHOR</h2>
<p> This utility is part of the m[blue]<code>Samba</code>m[]<font SIZE="-2">[1]</font> suite, which is developed by the global m[blue]<code>Samba Team</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> smbtorture was written by Andrew Tridgell. </p>
<p> This manpage was written by Jelmer Vernooij.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Samba</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.samba.org/">http://www.samba.org/</a></dl>
<dt> 2.</p>
<dd> Samba Team</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.samba.org/samba/team/">http://www.samba.org/samba/team/</a></dl>
</dl>
<h2>Index</h2>
