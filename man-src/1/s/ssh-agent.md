---
title: "ssh-agent(1)"
name: "ssh-agent"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssh-agent/"
description: "ssh-agent – OpenSSH authentication agent"
---

<h2 class="name">NAME</h2>
<p> <code>ssh-agent</code> &#8211; OpenSSH authentication agent </p>
<h2>SYNOPSIS</h2>
<p> <code>ssh-agent</code> [-<code>c | s</code> ] [-[-<code>a </code><i>bind_address</i> ] ] [-<code>E </code><i>fingerprint_hash</i> ] [-<code>P </code><i>allowed_providers</i> ] [-<code>t </code><i>life</i> ]<br />
<code>ssh-agent</code> [-<code>a </code><i>bind_address</i> ] [-<code>E </code><i>fingerprint_hash</i> ] [-<code>P </code><i>allowed_providers</i> ] [-<code>t </code><i>life</i> ] <i>command </i>[<i>arg &#8230;</i> ]<br />
<code>ssh-agent</code> [-<code>c | s</code> ] &#8211;<code>k</code></p>
<h2>DESCRIPTION</h2>
<p> <code>ssh-agent</code> is a program to hold private keys used for public key authentication. Through use of environment variables the agent can be located and automatically used for authentication when logging in to other machines using <a href="/docs/linux/man/1-ssh/">ssh</a>(1). </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-a </code><i>bind_address</i></p>
<dd> Bind the agent to the UNIX socket <i>bind_address</i> The default is $TMPDIR/ssh-XXXXXXXXXX/agent.&lt;ppid&gt;</p>
<dt><code>-c</code></p>
<dd> Generate C-shell commands on <code>stdout</code> This is the default if <code>SHELL</code> looks like it&#8217;s a csh style of shell.</p>
<dt><code>-D</code></p>
<dd> Foreground mode. When this option is specified <code>ssh-agent</code> will not fork.</p>
<dt><code>-d</code></p>
<dd> Debug mode. When this option is specified <code>ssh-agent</code> will not fork and will write debug information to standard error.</p>
<dt><code>-E </code><i>fingerprint_hash</i></p>
<dd> Specifies the hash algorithm used when displaying key fingerprints. Valid options are: &#8220;md5&#8221; and &#8220;sha256&#8221; The default is &#8220;sha256&#8221;</p>
<dt><code>-k</code></p>
<dd> Kill the current agent (given by the <code>SSH_AGENT_PID</code> environment variable).</p>
<dt><code>-P </code><i>allowed_providers</i></p>
<dd> Specify a pattern-list of acceptable paths for PKCS#11 provider and FIDO authenticator middleware shared libraries that may be used with the &#8211;<code>S</code> or &#8211;<code>s</code> options to ssh-add1. Libraries that do not match the pattern list will be refused. See PATTERNS in ssh_config5 for a description of pattern-list syntax. The default list is &#8220;/usr/lib/*,/usr/local/lib/*&#8221;</p>
<dt><code>-s</code></p>
<dd> Generate Bourne shell commands on <code>stdout</code> This is the default if <code>SHELL</code> does not look like it&#8217;s a csh style of shell.</p>
<dt><code>-t </code><i>life</i></p>
<dd> Set a default value for the maximum lifetime of identities added to the agent. The lifetime may be specified in seconds or in a time format specified in sshd_config5. A lifetime specified for an identity with ssh-add1 overrides this value. Without this option the default maximum lifetime is forever.</p>
<dt><i>command </i>[<i>arg &#8230;</i> ]</p>
<dd> If a command (and optional arguments) is given, this is executed as a subprocess of the agent. The agent exits automatically when the command given on the command line terminates.</dl>
<p> There are two main ways to get an agent set up. The first is at the start of an X session, where all other windows or programs are started as children of the <code>ssh-agent</code> program. The agent starts a command under which its environment variables are exported, for example <code>ssh-agent xterm &amp;</code> When the command terminates, so does the agent. </p>
<p> The second method is used for a login session. When <code>ssh-agent</code> is started, it prints the shell commands required to set its environment variables, which in turn can be evaluated in the calling shell, for example <code>eval `ssh-agent -s`</code> </p>
<p> In both cases, <a href="/docs/linux/man/1-ssh/">ssh</a>(1) looks at these environment variables and uses them to establish a connection to the agent. </p>
<p> The agent initially does not have any private keys. Keys are added using ssh-add1 or by <a href="/docs/linux/man/1-ssh/">ssh</a>(1) when <code>AddKeysToAgent</code> is set in ssh_config5. Multiple identities may be stored in <code>ssh-agent</code> concurrently and <a href="/docs/linux/man/1-ssh/">ssh</a>(1) will automatically use them if present. ssh-add1 is also used to remove keys from <code>ssh-agent</code> and to query the keys that are held in one. </p>
<p> Connections to <code>ssh-agent</code> may be forwarded from further remote hosts using the &#8211;<code>A</code> option to <a href="/docs/linux/man/1-ssh/">ssh</a>(1) (but see the caveats documented therein), avoiding the need for authentication data to be stored on other machines. Authentication passphrases and private keys never go over the network: the connection to the agent is forwarded over SSH remote connections and the result is returned to the requester, allowing the user access to their identities anywhere in the network in a secure fashion.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SSH_AGENT_PID</code></p>
<dd> When <code>ssh-agent</code> starts, it stores the name of the agent&#8217;s process ID (PID) in this variable.</p>
<dt><code>SSH_AUTH_SOCK</code></p>
<dd> When <code>ssh-agent</code> starts, it creates a UNIX socket and stores its pathname in this variable. It is accessible only to the current user, but is easily abused by root or another instance of the same user.</dl>
<p> In Debian, <code>ssh-agent</code> is installed with the set-group-id bit set, to prevent <a href="/docs/linux/man/2-ptrace/">ptrace</a>(2) attacks retrieving private key material. This has the side-effect of causing the run-time linker to remove certain environment variables which might have security implications for set-id programs, including <code>LD_PRELOAD</code> <code>LD_LIBRARY_PATH</code> and <code>TMPDIR</code> If you need to set any of these environment variables, you will need to do so in the program executed by ssh-agent.</p>
<h2>FILES</h2>
<dl>
<dt><code>$TMPDIR/ssh-XXXXXXXXXX/agent.&lt;ppid&gt; </code></p>
<dd> UNIX sockets used to contain the connection to the authentication agent. These sockets should only be readable by the owner. The sockets should get automatically removed when the agent exits.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-add1, ssh-keygen1, ssh_config5, <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<h2>AUTHORS</h2>
<p> An -nosplit OpenSSH is a derivative of the original and free ssh 1.2.12 release by An Tatu Ylonen . An Aaron Campbell , Bob Beck , Markus Friedl , Niels Provos , Theo de Raadt and An Dug Song removed many bugs, re-added newer features and created OpenSSH. An Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0. </p>
<h2>Index</h2>
