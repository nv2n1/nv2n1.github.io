---
title: "rootd(1)"
name: "rootd"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rootd/"
description: "rootd – The ROOT file server daemon"
---

<h2 class="name">NAME</h2>
<p> rootd &#8211; The ROOT file server daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>rootd</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>rootd</code> program. </p>
<p> <code>rootd</code> is a <code>ROOT</code> remote file server daemon. </p>
<p> This small server is started either by <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8) (or <i><a href="/docs/linux/man/8-xinetd/">xinetd</a></i>(8)) when a client requests a connection to a <i>rootd</i> server or by hand (i.e. from the command line). The <i>rootd</i> server works with the <code>ROOT</code> <i>TNetFile</i>, <i>TFTP</i> and <i>TNetSystem</i> classes. It allows access to remote directories and <code>ROOT</code> files in either read or write mode from any <code>ROOT</code> interactive session. By default rootd listens on port 1094, assigned to it by IANA.</p>
<h2>STARTING VIA (X)INETD</h2>
<p> To run <i>rootd</i> via <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8) or <i><a href="/docs/linux/man/8-xinetd/">xinetd</a></i>(8) the port 1094 must be assigned to <i>rootd</i> in <i>/etc/services</i>; the following line should be added, if not present: </p>
<dl>
<dt>
<dd>
<pre>
rootd     1094/tcp
</pre>
</dl>
<p> If the system uses inetd, add the following line to <i>/etc/inetd.conf</i>: </p>
<dl>
<dt>
<dd>
<pre>
rootd stream tcp nowait root &lt;<i>bindir</i>&gt;/rootd rootd -i
</pre>
</dl>
<p> where &lt;<i>bindir</i>&gt; is the directory you have installed <i>rootd</i> in. </p>
<p> The <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8) daemon must re-read its configuration file to become aware of the new service. This can be done either by killing and restarting it manually </p>
<dl>
<dt>
<dd>
<pre>
kill -HUP &lt;pid inetd&gt;
</pre>
</dl>
<p> or, if <code>SYSV</code> <i><a href="/docs/linux/man/8-init/">init</a></i>(8) scripts are used, by restarting it, e.g. </p>
<dl>
<dt>
<dd>
<pre>
/etc/init.d/inetd restart
</pre>
</dl>
<p> If the system uses <i><a href="/docs/linux/man/8-xinetd/">xinetd</a></i>(8) instead, a file named &#8216;rootd&#8217; should be created under <i>/etc/xinetd.d</i> with content: </p>
<dl>
<dt>
<dd>
<pre>
# default: off
# description: The rootd daemon
#
service rootd
{
     disable         = no
     flags           = REUSE
     socket_type     = stream
     wait            = no
     user            = root
     server          = &lt;<i>bindir</i>&gt;/rootd
     server_args     = -i
}
</pre>
</dl>
<p> where, again, &lt;<i>bindir</i>&gt; is the directory you have installed <i>rootd</i> in. </p>
<p> The <i><a href="/docs/linux/man/8-xinetd/">xinetd</a></i>(8) daemon must be restarted: </p>
<dl>
<dt>
<dd>
<pre>
/sbin/service xinetd restart
</pre>
</dl>
<p> If you installed <code>ROOT</code> using some pre-compiled package (for example a <code>Redhat Linux</code> or a <code>Debian GNU/Linux</code> package), this may already be done for you. </p>
<p> The above configuration examples start the daemon with superuser privileges. Please refer to the <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8) or <i><a href="/docs/linux/man/8-xinetd/">xinetd</a></i>(8) documentation for ways of limiting the privileges.</p>
<h2>STARTING BY HAND</h2>
<p> You can also start <i>rootd</i> by hand running directly under your private account (no root system privileges needed). For example to start <i>rootd</i> listening on port 5151 just type: </p>
<dl>
<dt>
<dd>
<pre>
rootd -p 5151
</pre>
</dl>
<p> <code>Notice</code>: no &amp; is needed <i>rootd</i> will go in background by itself.</p>
<h2>ANONYMOUS LOGINS</h2>
<p> <i>rootd</i> can also be configured for anonymous usage (like anonymous ftp). To setup <i>rootd</i> to accept anonymous logins do the following (while being logged in as root):</p>
<dl>
<dt>1</p>
<dd> Add the following line to /etc/passwd: </p>
<dl>
<dt>
<dd>
<pre>
rootd:*:71:72:Anonymous rootd:/var/spool/rootd:/bin/false
</pre>
</dl>
<dt>
<dd> where you may modify the uid, gid (71, 72) and the home directory to suite your system.</p>
<dt>2</p>
<dd> Add the following line to /etc/group: </p>
<dl>
<dt>
<dd>
<pre>
rootd:*:72:rootd
</pre>
</dl>
<dt>
<dd> where the gid must match the gid in <i>/etc/passwd</i></p>
<dt>3</p>
<dd>
&nbsp;<wbr>Create the directories: </p>
<dl>
<dt>
<dd>
<pre>
/var/spool/rootd
mkdir /var/spool/rootd/tmp
chmod 777 /var/spool/rootd/tmp
</pre>
</dl>
<dt>
<dd> Where <i>/var/spool/rootd</i> must match the <code>rootd</code> home directory as specified in the <code>rootd</code> <i>/etc/passwd</i> entry.</p>
<dt>4</p>
<dd> To make writable directories for anonymous do, for example: </p>
<dl>
<dt>
<dd>
<pre>
mkdir /var/spool/rootd/pub
chown rootd:rootd /var/spool/rootd/pub
</pre>
</dl>
<dt>
<dd> That&#8217;s all.</dl>
<p> If you installed <code>ROOT</code> using some pre-compiled package (for example a <code>Redhat Linux</code> or a <code>Debian GNU/Linux</code> package), this may already be done for you. </p>
<p> Several remarks:</p>
<dl>
<dt><code>*</code></p>
<dd> You can login to an anonymous server either with the names <i>anonymous</i> or <i>rootd.</i></p>
<dt><code>*</code></p>
<dd> The passwd should be of type <i>user [at] host.domain</i> Only the @ is enforced for the time being.</p>
<dt><code>*</code></p>
<dd> In anonymous mode the top of the file tree is set to the <code>rootd</code> home directory, therefore only files below the home directory can be accessed.</p>
<dt><code>*</code></p>
<dd> Anonymous mode only works when the server is started via <a href="/docs/linux/man/8-inetd/">inetd</a>(8) or <a href="/docs/linux/man/8-xinetd/">xinetd</a>(8).</dl>
<h2>ABOUT PASSWORD AUTHENTICATION</h2>
<p> In system using shadow passwords, full access to the password field of the user information structure requires special privileges; this is typically granted if rootd is started by <i><a href="/docs/linux/man/8-inetd/">inetd</a>(8)</i> or <i><a href="/docs/linux/man/8-xinetd/">xinetd</a>(8)</i>, as the in above examples. If the daemon is started in unprivileged mode, either from a regular account or by (x)inetd with reduced privileges, password-based authentication require users to create a file $HOME/.rootdpass containing an encrypted password (using <i><a href="/docs/linux/man/3-crypt/">crypt</a></i>(3)). The system tests the existence of this file before checking the system password files. An encrypted password can be created in the following way: </p>
<dl>
<dt>
<dd>
<pre>
perl -e '$pw = crypt(&quot;&lt;secretpasswd&gt;&quot;,&quot;salt&quot;); print &quot;$pw'
</pre>
</dl>
<p> storing the output string in $HOME/.rootdpass . </p>
<p> If the $HOME/.rootdpass does not exists and the system password file cannot be accessed, rootd attempts to run the authentication via an <i><a href="/docs/linux/man/8-sshd/">sshd</a></i>(8) daemon.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code> &lt;<i>tcpwindowsize</i>&gt;</p>
<dd> specifies the tcp window size in bytes (e.g. see <a rel="nofollow" href="http://www.psc.edu/networking/perf_tune.html">http://www.psc.edu/networking/perf_tune.html</a>). Default is 65535. Only change default for pipes with a high bandwidth*delay product.</p>
<dt><code>-d</code> &lt;<i>level</i>&gt;</p>
<dd> level of debug info written to syslogd 0 = no debug (default), 1 = minimum, 2 = medium, 3 = maximum.</p>
<dt><code>-D</code> &lt;<i>rootdaemonrc</i>&gt;</p>
<dd> read access rules from file &lt;rootdaemonrc&gt;. By default &lt;root_etc_dir&gt;/system.rootdaemonrc is used for access rules; for privately started daemons $HOME/.rootdaemonrc (if present) is read first.</p>
<dt><code>-f</code></p>
<dd> run in the foreground (output on the window); useful for debugging purposes.</p>
<dt><code>-i</code></p>
<dd> indicates that <i>rootd</i> was started by <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8) or <i><a href="/docs/linux/man/8-xinetd/">xinetd</a></i>(8).</p>
<dt><code>-noauth</code></p>
<dd> do not require client authentication</p>
<dt><code>-p</code> &lt;<i>port#</i>&gt;[-&lt;<i>port2#</i>&gt;]</p>
<dd> specifies the port number to listen on. Use port-port2 to find the first available port in the indicated range. Use 0-N for range relative to default service port.</p>
<dt><code>-r</code></p>
<dd> files can only be opened in read-only mode</p>
<dt><code>-s</code> &lt;<i>sshd_port#</i>&gt;</p>
<dd> specifies the port number for the sshd daemon used for authentication (default is 22).</p>
<dt><code>-T</code> &lt;<i>tmpdir</i>&gt;</p>
<dd> specifies the directory path to be used to place temporary files; default is /usr/tmp. Useful when running with limited privileges.</p>
<dt><code>-w</code></p>
<dd> do not check /etc/hosts.equiv, $HOME/.rhosts for password-based authentication; by default these files are checked first by calling ruserok(&#8230;); if this option is specified a password is always required.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-root/">root</a></i>(1), <i><a href="/docs/linux/man/1-proofd/">proofd</a></i>(1), <i><a href="/docs/linux/man/1-system-rootdaemonrc/">system.rootdaemonrc</a></i>(1) </p>
<p> For more information on the <code>ROOT</code> system, please refer to <i><a rel="nofollow" href="http://root.cern.ch">http://root.cern.ch</a></i></p>
<h2>ORIGINAL AUTHORS</h2>
<p> The ROOT team (see web page above):</p>
<dl>
<dt>
<dd> <code>Rene Brun</code> and <code>Fons Rademakers</code></dl>
<h2>COPYRIGHT</h2>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Christian Holm Christensen &lt;cholm [at] nbi.dk&gt;, for the Debian GNU/Linux system and ROOT version 3. It has been modified by G. Ganis &lt;g.ganis [at] cern.ch&gt; to document new features included in ROOT version 4. </p>
<h2>Index</h2>
