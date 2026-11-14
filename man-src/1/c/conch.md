---
title: "conch(1)"
name: "conch"
section: "1"
letter: "c"
url: "/docs/linux/man/1-conch/"
description: "conch – Conch SSH client"
---

<h2>NAME</h2>
<p> <code>conch</code> &#8211; Conch SSH client</p>
<h2>SYNOPSIS</h2>
<p> <code>conch</code> [-<code>AaCfINnrsTtVvx</code> ] [-<code>c </code><i>cipher_spec</i> ] [-<code>e </code><i>escape_char</i> ] [-<code>i </code><i>identity_file</i> ] [-<code>K </code><i>connection_spec</i> ] -words [-<code>L </code> <i>port</i> <i>host</i> <i>hostport</i> ] [-<code>l </code><i>user</i> ] [-<code>m </code><i>mac_spec</i> ] [-<code>o </code><i>openssh_option</i> ] [-<code>p </code><i>port</i> ] -words [-<code>R </code> <i>port</i> <i>host</i> <i>hostport</i> ] [<i>user </i><code>@ </code><i>hostname</i> ] [<i>command</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>conch</code> is a SSHv2 client for logging into a remote machine and executing commands. It provides encrypted and secure communications across a possibly insecure network. Arbitrary TCP/IP ports can also be forwarded over the secure connection. </p>
<p> <code>conch</code> connects and logs into <i>hostname</i> (as <i>user</i> or the current username). The user must prove her/his identity through a public-key or a password. Alternatively, if a connection is already open to a server, a new shell can be opened over the connection without having to reauthenticate. </p>
<p> If <i>command</i> is specified, <i>command</i> is executed instead of a shell. If the &#8211;<code>s</code> option is given, <i>command</i> is treated as an SSHv2 subsystem name.</p>
<h3>Authentication</h3>
<p> Conch supports the public-key, keyboard-interactive, and password authentications. </p>
<p> The public-key method allows the RSA or DSA algorithm to be used. The client uses his/her private key, $HOME/.ssh/id_rsa or $HOME/.ssh/id_dsa to sign the session identifier, known only by the client and server. The server checks that the matching public key is valid for the user, and that the signature is correct. </p>
<p> If public-key authentication fails, <code>conch</code> can authenticate by sending an encrypted password over the connection.</p>
<h3>Connection sharing</h3>
<p> <code>conch</code> has the ability to multiplex multiple shells, commands and TCP/IP ports over the same secure connection. To disable multiplexing for a connection, use the &#8211;<code>I</code> flag. </p>
<p> The &#8211;<code>K</code> option determines how the client connects to the remote host. It is a comma-separated list of the methods to use, in order of preference. The two connection methods are `unix&#8217; (for connecting over a multiplexed connection) and `direct&#8217; </p>
<p> (to connect directly). To disable connecting over a multiplexed connection, do not include `unix&#8217; in the preference list. </p>
<p> As an example of how connection sharing works, to speed up CVS over SSH: </p>
<p> <code>conch</code> &#8211;noshell &#8211;fork -l cvs_user cvs_host<br />
 set CVS_RSH=<code>conch</code> </p>
<p> Now, when CVS connects to cvs_host as cvs_user, instead of making a new connection to the server, <code>conch</code> will add a new channel to the existing connection. This saves the cost of repeatedly negotiating the cryptography and authentication. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-A</code></p>
<dd> Enables authentication agent forwarding.</p>
<dt><code>-a</code></p>
<dd> Disables authentication agent forwarding (default).</p>
<dt><code>-C</code></p>
<dd> Enable compression.</p>
<dt><code>-c </code><i>cipher_spec</i></p>
<dd> Selects encryption algorithms to be used for this connection, as a comma-separated list of ciphers in order of preference. The list that <code>conch</code> supports is (in order of default preference): aes256-ctr, aes256-cbc, aes192-ctr, aes192-cbc, aes128-ctr, aes128-cbc, cast128-ctr, cast128-cbc, blowfish-ctr, blowfish, idea-ctr, idea-cbc, 3des-ctr, 3des-cbc.</p>
<dt><code>-e </code><i>ch | ^ch | none</i></p>
<dd> Sets the escape character for sessions with a PTY (default: `~&#8217; ) . The escape character is only recognized at the beginning of a line (after a newline). The escape character followed by a dot (`.&#8217; ) closes the connection; followed by ^Z suspends the connection; and followed by the escape character sends the escape character once. Setting the character to &#8220;none&#8221; disables any escapes.</p>
<dt><code>-f</code></p>
<dd> Fork to background after authentication.</p>
<dt><code>-I</code></p>
<dd> Do not allow connection sharing over this connection.</p>
<dt><code>-i </code><i>identity_spec</i></p>
<dd> The file from which the identity (private key) for RSA or DSA authentication is read. The defaults are $HOME/.ssh/id_rsa and $HOME/.ssh/id_dsa . It is possible to use this option more than once to use more than one private key.</p>
<dt><code>-K </code><i>connection_spec</i></p>
<dd> Selects methods for connection to the server, as a comma-separated list of methods in order of preference. See <code>Connection sharing</code> for more information.</p>
<dt><code>-L </code> <i>port : host : hostport</i></p>
<dd>
<dd>Specifies that the given port on the client host is to be forwarded to the given host and port on the remote side. This allocates a socket to listen to <i>port </i> on the local side, and when connections are made to that socket, they are forwarded over the secure channel and a connection is made to <i>host</i> port <i>hostport</i> from the remote machine. Only root can forward privieged ports.</p>
<dt><code>-l </code><i>user</i></p>
<dd> Log in using this username.</p>
<dt><code>-m </code><i>mac_spec</i></p>
<dd> Selects MAC (message authentication code) algorithms, as a comma-separated list in order of preference. The list that <code>conch</code> supports is (in order of preference): hmac-sha2-512, hmac-sha2-256, hmac-sha1, hmac-md5.</p>
<dt><code>-N</code></p>
<dd> Do not execute a shell or command.</p>
<dt><code>-n</code></p>
<dd> Redirect input from /dev/null.</p>
<dt><code>-o </code><i>openssh_option</i></p>
<dd> Ignored OpenSSH options.</p>
<dt><code>-p </code><i>port</i></p>
<dd> The port to connect to on the server.</p>
<dt><code>-R </code> <i>port : host : hostport</i></p>
<dd>
<dd>Specifies that the given port on the remote host is to be forwarded to the given host and port on the local side. This allocates a socket to listen to <i>port </i> on the remote side, and when connections are made to that socket, they are forwarded over the secure channel and a connection is made to <i>host</i> port <i>hostport</i> from the client host. Only root can forward privieged ports.</p>
<dt><code>-s</code></p>
<dd> Reconnect to the server if the connection is lost.</p>
<dt><code>-s</code></p>
<dd> Invoke <i>command</i> (mandatory) as a SSHv2 subsystem.</p>
<dt><code>-T</code></p>
<dd> Do not allocate a TTY.</p>
<dt><code>-t</code></p>
<dd> Allocate a TTY even if command is given.</p>
<dt><code>-V</code></p>
<dd> Display version number only.</p>
<dt><code>-v</code></p>
<dd> Log to stderr.</p>
<dt><code>-x</code></p>
<dd> Disable X11 connection forwarding (default).</dl>
<h2>AUTHOR</h2>
<p> Written by Paul Swartz &lt;z3p [at] twistedmatrix.com&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2008 Twisted Matrix Laboratories.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1) </p>
<h2>Index</h2>
