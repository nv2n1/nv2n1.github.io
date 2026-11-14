---
title: "pssh(1)"
name: "pssh"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pssh/"
description: "pssh — parallel ssh program"
---

<h2 class="name">NAME</h2>
<p> pssh &#8212; parallel ssh program </p>
<h2>SYNOPSIS</h2>
<p> <code>pssh</code> [<code>-vAiIP</code>] [<code>-h</code> <i>hosts_file</i>] [<code>-H</code> [<i>user</i>@]<i>host</i>[:<i>port</i>]] [<code>-l</code> <i>user</i>] [<code>-p</code> <i>par</i>] [<code>-o</code> <i>outdir</i>] [<code>-e</code> <i>errdir</i>] [<code>-t</code> <i>timeout</i>] [<code>-O</code> <i>options</i>] [<code>-x</code> <i>args</i>] [<code>-X</code> <i>arg</i>] <i>command &#8230;</i> </p>
<p> <code>pssh -I</code> [<code>-vAiIP</code>] [<code>-h</code> <i>hosts_file</i>] [<code>-H</code> [<i>user</i>@]<i>host</i>[:<i>port</i>]] [<code>-l</code> <i>user</i>] [<code>-p</code> <i>par</i>] [<code>-o</code> <i>outdir</i>] [<code>-e</code> <i>errdir</i>] [<code>-t</code> <i>timeout</i>] [<code>-O</code> <i>options</i>] [<code>-x</code> <i>args</i>] [<code>-X</code> <i>arg</i>] [<i>command</i> <i>&#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pssh</code> is a program for executing ssh in parallel on a number of hosts. It provides features such as sending input to all of the processes, passing a password to ssh, saving output to files, and timing out. </p>
<p> The PSSH_NODENUM and PSSH_HOST environment variables are sent to the remote host. The PSSH_NODENUM variable is assigned a unique number for each ssh connection, starting with 0 and counting up. The PSSH_HOST variable is assigned the name of the host as specified in the hosts list. Note that sshd drops environment variables by default, so sshd_config on the remote host must include the line:</p>
<dl>
<dt>
<dd> AcceptEnv PSSH_NODENUM PSSH_HOST</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code><i> host_file</i></p>
<dd>
<dt><code>&#8211;hosts</code><i> host_file</i></p>
<dd> Read hosts from the given <i>host_file</i>. Lines in the host file are of the form [<i>user</i>@]<i>host</i>[:<i>port</i>] and can include blank lines and comments (lines beginning with &quot;#&quot;). If multiple host files are given (the <code>-h</code> option is used more than once), then pssh behaves as though these files were concatenated together. If a host is specified multiple times, then pssh will connect the given number of times. </p>
<dt><code>-H</code></p>
<dd> [<i>user</i>@]<i>host</i>[:<i>port</i>]</p>
<dt><code>&#8211;host</code></p>
<dd> [<i>user</i>@]<i>host</i>[:<i>port</i>]</p>
<dt><code>-H</code></p>
<dd> &quot;[<i>user</i>@]<i>host</i>[:<i>port</i>] [ [<i>user</i>@]<i>host</i>[:<i>port</i> ] &#8230; ]&quot;</p>
<dt><code>&#8211;host</code></p>
<dd> &quot;[<i>user</i>@]<i>host</i>[:<i>port</i>] [ [<i>user</i>@]<i>host</i>[:<i>port</i> ] &#8230; ]&quot;</p>
<dt>
<dd> Add the given host strings to the list of hosts. This option may be given multiple times, and may be used in conjunction with the <code>-h</code> option. </p>
<dt><code>-l</code><i> user</i></p>
<dd>
<dt><code>&#8211;user</code><i> user</i></p>
<dd> Use the given username as the default for any host entries that don&#8217;t specifically specify a user. </p>
<dt><code>-p</code><i> parallelism</i></p>
<dd>
<dt><code>&#8211;par</code><i> parallelism</i></p>
<dd> Use the given number as the maximum number of concurrent connections. </p>
<dt><code>-t</code><i> timeout</i></p>
<dd>
<dt><code>&#8211;timeout</code><i> timeout</i></p>
<dd> Make connections time out after the given number of seconds. With a value of 0, pssh will not timeout any connections. </p>
<dt><code>-o</code><i> outdir</i></p>
<dd>
<dt><code>&#8211;outdir</code><i> outdir</i></p>
<dd> Save standard output to files in the given directory. Filenames are of the form [<i>user</i>@]<i>host</i>[:<i>port</i>][.<i>num</i>] where the user and port are only included for hosts that explicitly specify them. The number is a counter that is incremented each time for hosts that are specified more than once. </p>
<dt><code>-e</code><i> errdir</i></p>
<dd>
<dt><code>&#8211;errdir</code><i> errdir</i></p>
<dd> Save standard error to files in the given directory. Filenames are of the same form as with the <code>-o</code> option. </p>
<dt><code>-x</code><i> args</i></p>
<dd>
<dt><code>&#8211;extra-args</code><i> args</i></p>
<dd> Passes extra SSH command-line arguments (see the <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) man page for more information about SSH arguments). This option may be specified multiple times. The arguments are processed to split on whitespace, protect text within quotes, and escape with backslashes. To pass arguments without such processing, use the <code>-X</code> option instead. </p>
<dt><code>-X</code><i> arg</i></p>
<dd>
<dt><code>&#8211;extra-arg</code><i> arg</i></p>
<dd> Passes a single SSH command-line argument (see the <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) man page for more information about SSH arguments). Unlike the <code>-x</code> option, no processing is performed on the argument, including word splitting. To pass multiple command-line arguments, use the option once for each argument. </p>
<dt><code>-O</code><i> options</i></p>
<dd>
<dt><code>&#8211;options</code><i> options</i></p>
<dd> SSH options in the format used in the SSH configuration file (see the <code><a href="/docs/linux/man/5-ssh_config/">ssh_config</a></code>(5) man page for more information). This option may be specified multiple times. </p>
<dt><code>-A</code></p>
<dd>
<dt><code>&#8211;askpass</code></p>
<dd> Prompt for a password and pass it to ssh. The password may be used for either to unlock a key or for password authentication. The password is transferred in a fairly secure manner (e.g., it will not show up in argument lists). However, be aware that a root user on your system could potentially intercept the password. </p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;inline</code></p>
<dd> Display standard output and standard error as each host completes. </p>
<dt><code>&#8211;inline-stdout</code></p>
<dd> Display standard output (but not standard error) as each host completes. </p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Include error messages from ssh with the <code>-i</code> and <code>\</code> options. </p>
<dt><code>-I</code></p>
<dd>
<dt><code>&#8211;send-input</code></p>
<dd> Read input and send to each ssh process. Since ssh allows a command script to be sent on standard input, the <code>-I</code> option may be used in lieu of the command argument. </p>
<dt><code>-P</code></p>
<dd>
<dt><code>&#8211;print</code></p>
<dd> Display output as it arrives. This option is of limited usefulness because output from different hosts are interleaved. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Connect to host1 and host2, and print &quot;hello, world&quot; from each:</p>
<dl>
<dt>
<dd> pssh -i -H &quot;host1 host2&quot; echo &quot;hello, world&quot;</dl>
<p> Print &quot;hello, world&quot; from each host specified in the file hosts.txt:</p>
<dl>
<dt>
<dd> pssh -i -h hosts.txt echo &quot;hello, world&quot;</dl>
<p> Run a command as root with a prompt for the root password:</p>
<dl>
<dt>
<dd> pssh -i -h hosts.txt -A -l root echo hi</dl>
<p> Run a long command without timing out:</p>
<dl>
<dt>
<dd> pssh -i -h hosts.txt -t 0 sleep 10000</dl>
<p> If the file hosts.txt has a large number of entries, say 100, then the parallelism option may also be set to 100 to ensure that the commands are run concurrently:</p>
<dl>
<dt>
<dd> pssh -i -h hosts.txt -p 100 -t 0 sleep 10000</dl>
<p> Run a command without checking or saving host keys:</p>
<dl>
<dt>
<dd> pssh -i -H host1 -H host2 -x &quot;-O StrictHostKeyChecking=no -O UserKnownHostsFile=/dev/null -O GlobalKnownHostsFile=/dev/null&quot; echo hi</dl>
<p> Print the node number for each connection (this will print 0, 1, and 2):</p>
<dl>
<dt>
<dd> pssh -i -H host1 -H host1 -H host2 &#8216;echo $PSSH_NODENUM&#8217;</dl>
<h2>TIPS</h2>
<p> If you have a set of hosts that you connect to frequently with specific options, it may be helpful to create an alias such as:</p>
<dl>
<dt>
<dd> alias pssh_servers=&quot;pssh -h /path/to/server_list.txt -l root -A&quot;</dl>
<p> The ssh_config file can include an arbitrary number of Host sections. Each host entry specifies ssh options which apply only to the given host. Host definitions can even behave like aliases if the HostName option is included. This ssh feature, in combination with pssh host files, provides a tremendous amount of flexibility. </p>
<h2>EXIT STATUS</h2>
<p> The exit status codes from pssh are as follows: </p>
<dl>
<dt><code>0</code></p>
<dd> Success </p>
<dt><code>1</code></p>
<dd> Miscellaneous error </p>
<dt><code>2</code></p>
<dd> Syntax or usage error </p>
<dt><code>3</code></p>
<dd> At least one process was killed by a signal or timed out. </p>
<dt><code>4</code></p>
<dd> All processes completed, but at least one ssh process reported an error (exit status 255). </p>
<dt><code>5</code></p>
<dd> There were no ssh errors, but at least one remote command had a non-zero exit status. </p>
</dl>
<h2>AUTHORS</h2>
<p> Written by Brent N. Chun &lt;bnc [at] theether.org&gt; and Andrew McNabb &lt;amcnabb [at] mcnabbs.org&gt;. </p>
<p> <a rel="nofollow" href="http://code.google.com/p/parallel-ssh/">http://code.google.com/p/parallel-ssh/</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/5-ssh_config/">ssh_config</a>(5),</code> <code><a href="/docs/linux/man/1-pscp/">pscp</a></code>(1), <code><a href="/docs/linux/man/1-prsync/">prsync</a></code>(1), <code><a href="/docs/linux/man/1-pslurp/">pslurp</a></code>(1), <code><a href="/docs/linux/man/1-pnuke/">pnuke</a></code>(1), </p>
<h2>Index</h2>
