---
title: "ssh-copy-id(1)"
name: "ssh-copy-id"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssh-copy-id/"
description: "ssh-copy-id – use locally available keys to authorise logins on a remote machine"
---

<h2 class="name">NAME</h2>
<p> <code>ssh-copy-id</code> &#8211; use locally available keys to authorise logins on a remote machine </p>
<h2>SYNOPSIS</h2>
<p> <code>ssh-copy-id</code> [-<code>f</code> ] [-<code>n</code> ] [-<code>s</code> ] [-<code>i </code>[<i>identity_file</i> ] ] [-<code>p </code><i>port</i> ] [-<code>o </code><i>ssh_option</i> ] [<i>user </i><code>@ </code><i>hostname</i> ]<br />
<code>ssh-copy-id</code> &#8211;<code>h | &#8211; </code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ssh-copy-id</code> is a script that uses <a href="/docs/linux/man/1-ssh/">ssh</a>(1) to log into a remote machine (presumably using a login password, so password authentication should be enabled, unless you&#8217;ve done some clever use of multiple identities). It assembles a list of one or more fingerprints (as described below) and tries to log in with each key, to see if any of them are already installed (of course, if you are not using ssh-agent1 this may result in you being repeatedly prompted for pass-phrases). It then assembles a list of those that failed to log in, and using ssh, enables logins with those keys on the remote server. By default it adds the keys by appending them to the remote user&#8217;s ~/.ssh/authorized_keys (creating the file, and directory, if necessary). It is also capable of detecting if the remote system is a NetScreen, and using its `set&#8217; ssh pka-dsa key &#8230; command instead. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-i </code><i>identity_file</i></p>
<dd> Use only the key(s) contained in <i>identity_file</i> (rather than looking for identities via ssh-add1 or in the <code>default_ID_file )</code> If the filename does not end in .pub this is added. If the filename is omitted, the <code>default_ID_file</code> is used. </p>
<p> Note that this can be used to ensure that the keys copied have the comment one prefers and/or extra options applied, by ensuring that the key file has these set as preferred before the copy is attempted.</p>
<dt><code>-f</code></p>
<dd> Forced mode: doesn&#8217;t check if the keys are present on the remote server. This means that it does not need the private key. Of course, this can result in more than one copy of the key being installed on the remote system.</p>
<dt><code>-n</code></p>
<dd> do a dry-run. Instead of installing keys on the remote system simply prints the key(s) that would have been installed.</p>
<dt><code>-s</code></p>
<dd> SFTP mode: usually the public keys are installed by executing commands on the remote side. With this option the user&#8217;s ~/.ssh/authorized_keys file will be downloaded, modified locally and uploaded with sftp. This option is useful if the server has restrictions on commands which can be used on the remote side.</p>
<dt><code>-h , &#8211; </code></p>
<dd> Print Usage summary</p>
<dt><code>-p </code><i>port , &#8211;</i><code>o </code><i>ssh_option</i></p>
<dd> These two options are simply passed through untouched, along with their argument, to allow one to set the port or other <a href="/docs/linux/man/1-ssh/">ssh</a>(1) options, respectively. </p>
<p> Rather than specifying these as command line options, it is often better to use (per-host) settings in <a href="/docs/linux/man/1-ssh/">ssh</a>(1)Ns&#8217;s configuration file: ssh_config5.</dl>
<p> Default behaviour without &#8211;<code>i</code> is to check if `ssh-add&#8217; -L provides any output, and if so those keys are used. Note that this results in the comment on the key being the filename that was given to ssh-add1 when the key was loaded into your ssh-agent1 rather than the comment contained in that file, which is a bit of a shame. Otherwise, if ssh-add1 provides no keys contents of the <code>default_ID_file</code> will be used. </p>
<p> The <code>default_ID_file</code> is the most recent file that matches: ~/.ssh/id*.pub (excluding those that match ~/.ssh/*-cert.pub so if you create a key that is not the one you want <code>ssh-copy-id</code> to use, just use <a href="/docs/linux/man/1-touch/">touch</a>(1) on your preferred key&#8217;s .pub file to reinstate it as the most recent. </p>
<h2>EXAMPLES</h2>
<p> If you have already installed keys from one system on a lot of remote hosts, and you then create a new key, on a new client machine, say, it can be difficult to keep track of which systems on which you&#8217;ve installed the new key. One way of dealing with this is to load both the new key and old key(s) into your ssh-agent1. Load the new key first, without the &#8211;<code>c</code> option, then load one or more old keys into the agent, possibly by ssh-ing to the client machine that has that old key, using the &#8211;<code>A</code> option to allow agent forwarding: </p>
<p> now, if the new key is installed on the server, you&#8217;ll be allowed in unprompted, whereas if you only have the old key(s) enabled, you&#8217;ll be asked for confirmation, which is your cue to log back out and run </p>
<p> The reason you might want to specify the -i option in this case is to ensure that the comment on the installed key is the one from the .pub file, rather than just the filename that was loaded into your agent. It also ensures that only the id you intended is installed, rather than all the keys that you have in your ssh-agent1. Of course, you can specify another id, or use the contents of the ssh-agent1 as you prefer. </p>
<p> Having mentioned ssh-add1Ns&#8217;s &#8211;<code>c</code> option, you might consider using this whenever using agent forwarding to avoid your key being hijacked, but it is much better to instead use <a href="/docs/linux/man/1-ssh/">ssh</a>(1)Ns&#8217;s <i>ProxyCommand</i> and &#8211;<code>W</code> option, to bounce through remote servers while always doing direct end-to-end authentication. This way the middle hop(s) don&#8217;t get access to your ssh-agent1. A web search for `ssh&#8217; proxycommand nc should prove enlightening (N.B. the modern approach is to use the &#8211;<code>W</code> option, rather than <a href="/docs/linux/man/1-nc/">nc</a>(1)).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), ssh-agent1, <a href="/docs/linux/man/8-sshd/">sshd</a>(8) </p>
<h2>Index</h2>
