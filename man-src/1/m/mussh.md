---
title: "mussh(1)"
name: "mussh"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mussh/"
description: "mussh – MUltihost SSH"
---

<h2>NAME</h2>
<p> mussh &#8211; MUltihost SSH</p>
<h2>SYNOPSIS</h2>
<p> <code>mussh [</code> <i>OPTIONS</i> <code>] &lt;-h </code> <i>host&#8230;</i> <code>| -H </code> <i>hostfile</i> <code>&gt; [-c</code> <i>cmd</i> <code>] [-C </code> <i>scriptfile</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>mussh</code> is a shell script that allows you to execute a command or script over <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) on multiple hosts with one command. When possible mussh will use <code><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></code>(1) and RSA/DSA keys to minimize the need to enter your password more than once.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;help</p>
<dd> Prints full help text.</p>
<dt>-d</p>
<dd> Same as -d 1</p>
<dt>-d 0</p>
<dd> Turns debug mode off.</p>
<dt>-d 1</p>
<dd> On STDERR prints out basic actions and ssh-agent activity and which host is being connected to.</p>
<dt>-d 2</p>
<dd> Includes all of the output from -d1, the list of hosts, the command/script as it will be executed on each host, and a lot more.</p>
<dt>-v</p>
<dd> Same as -v 1</p>
<dt>-v 1</p>
<dd> Sets ssh in debug1 mode by passing &quot;-v&quot; to ssh.</p>
<dt>-v 2</p>
<dd> Sets ssh in debug2 mode by passing &quot;-v -v&quot; to ssh.</p>
<dt>-v 3</p>
<dd> Sets ssh in debug3 mode by passing &quot;-v -v -v&quot; to ssh.</p>
<dt>-m [n]</p>
<dd> Run concurrently on &#8216;n&#8217; hosts at a time (asynchronous). Use &#8216;0&#8217; (zero) for infinite. (default)</p>
<dt>-q</p>
<dd> No output unless necessary. This will cancel -d and -v if after them on the command line. It also suppresses the output of each host. This will NOT suppress the password/passphrase prompts required to log into each host.</p>
<dt>-i &lt;identity&gt; [identity ..]</p>
<dd> Load an identity file. When -i is used, the specified identity file(s) is loaded instead of the default identity. You can load as many RSA/DSA identities as you&#8217;d like.</p>
<dt>-o &lt;ssh-args&gt;</p>
<dd> Args to pass to ssh with -o option. See the <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1) man page for more info on the -o option.</p>
<dt>-a</p>
<dd> Force loading ssh-agent. Without this flag, mussh will not load another agent when one is already loaded.</p>
<dt>-A</p>
<dd> Do NOT load ssh-agent. If no agent is loaded you will be prompted for a password or passphrase by ssh for each host. If you do not have RSA/DSA keys for the destination hosts, this will save you some hassle.</p>
<dt>-b</p>
<dd> Print each hosts&#8217; output in a block without mingling with other hosts&#8217; output.</p>
<dt>-B</p>
<dd> Allow hosts&#8217; output to mingle. (default)</p>
<dt>-u</p>
<dd> Unique. Eliminate duplicate hosts. (default) If you a host or user [at] host occurs more than once across files specified with -H or hosts specified with -h, the host or user [at] host is used only once.</p>
<dt>-U</p>
<dd> Do NOT make host list unique. This simply overrides the -u flag. This will cause scripts to be executed on duplicate hosts once per listing.</p>
<dt>-P</p>
<dd> Do NOT fall back to passwords on any host. This will skip hosts where keys fail. If you use this with &#8211; d&#8217; you&#8217;ll still see which hosts failed.</p>
<dt>-l &lt;login&gt;</p>
<dd> Use &#8216;login&#8217; when no other is specified with hostname.</p>
<dt>-L &lt;login&gt;</p>
<dd> Force use of &#8216;login&#8217; name on all hosts. These can be handy for adding &#8216;root@&#8217; to hostnames kept in a file for -H option. With -h it means you get to type less.</p>
<dt>-s &lt;shell&gt;</p>
<dd> Path to shell on remote host. (Default: bash)</p>
<dt>-t &lt;secs&gt;</p>
<dd> Timeout setting for each session. (requires openssh 3.8 or newer)</p>
<dt>-V</p>
<dd> Print version info and exit.</dl>
<h2>PROXY ARGS</h2>
<dl>
<dt>-p [user@]&lt;host&gt;</p>
<dd> Host to use as proxy. (Must have mussh installed)</p>
<dt>-po &lt;ssh-args&gt;</p>
<dd> Args to pass to ssh on proxy with -o option.</dl>
<h2>HOST ARGS</h2>
<dl>
<dt>-h [user@]&lt;host&gt; [[user@]&lt;host&gt; ..]</p>
<dd> Add a host to list of hosts. May be used more than once.</p>
<dt>-H &lt;file&gt; [file ..]</p>
<dd> Add contents of file(s) to list of hosts. Files should have one host per line. Use &quot;#&quot; for comments.</dl>
<h2>COMMAND ARGS</h2>
<p> If neither is specified, commands will be read from standard input.</p>
<dl>
<dt>-c &lt;command&gt;</p>
<dd> Add a command or quoted list of commands and args to list of commands to be executed on each host. May be used more than once.</p>
<dt>-C &lt;file&gt; [file ..]</p>
<dd> Add file contents to list of commands to be executed on each host. May be used more than once.</dl>
<h2>PROXY MODE</h2>
<p> When proxying, mussh can use a single remote server to as a bastion host. All hosts will be connected to from the central host rather than from the computer where you are initially running mussh. This can be handy when you only have access to one machine behind a firewall. </p>
<p> The proxy host must have OpenSSH 2.3 or greater, or an sshd that works with ForwardAgent under ssh2. Proxy server must also have mussh installed in your PATH. To verify that it is in your path use &quot;ssh user [at] proxy &#8216;which mussh&#8217;&quot;. Use &quot;ssh user [at] proxy &#8216;echo $PATH&#8217;&quot; to determine what your path is.</p>
<h2>SSH-AGENT INTERACTION</h2>
<p> Assuming that you&#8217;re not turning off the agent with &#8216;-A&#8217; mussh will attempt to use <code><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></code>(1). Normally mussh will get rid of the agent when it exits. See EXAMPLES for examples.</p>
<h2>EXAMPLES</h2>
<p> There is an EXAMPLES file with detailed examples. </p>
<dl>
<dt>The basic command:</p>
<dd> <code>$ mussh -h foo bar baz </code> </p>
<dt>A simple command:</p>
<dd> <code>$ mussh -h foo bar baz -c &#8216;rpm -e emacs&#8217;</code> </p>
<dt>A simple command asynchronously:</p>
<dd> <code>$ mussh -h foo bar baz -c &#8216;rpm -e emacs&#8217; -m</code> </p>
<dt>Using a specific key:</p>
<dd> <code>$ mussh -h foo bar baz -c &#8216;rpm -e emacs&#8217; -i ~/.ssh/my_other.key</code> </p>
<dt>Loading a list of hosts from a file:</p>
<dd> <code>$ mussh -H /tmp/hostlist.txt -c &#8216;rpm -e emacs&#8217;</code> </p>
<dt>Loading a script from a file:</p>
<dd> <code>$ mussh -h foo bar baz -C /tmp/scriptfile.sh</code> </p>
</dl>
<h2>BUGS</h2>
<p> Please report any bugs at <a rel="nofollow" href="http://sourceforge.net/projects/mussh/">http://sourceforge.net/projects/mussh/</a></p>
<h2>AUTHOR</h2>
<p> Dave Fogarty &lt;doughnut at doughnut dot net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1), <code><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></code>(1) </p>
<h2>Index</h2>
