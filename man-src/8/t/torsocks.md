---
title: "torsocks(8)"
name: "torsocks"
section: "8"
letter: "t"
url: "/docs/linux/man/8-torsocks/"
description: "torsocks — Library for intercepting outgoing network connections and redirecting them through the Tor SOCKS proxy."
---

<p>torsocks &#8212; Library for intercepting outgoing network connections and redirecting them through the Tor SOCKS proxy.</p>
<h2>Description</h2>
<p>Torsocks library overloads the libc symbols use for Internet communication such as <code><a href="/docs/linux/man/2-connect/">connect</a>(2)</code> system call. Using that technique, the library sends everything through the Tor network including DNS resolution done by the application. For DNS, <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a>(3)</code> family functions are rerouted through Tor. Please note that the ISC res_* API is currently not supported. Here is an example on how to use torsocks library with <code><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</code>:<br />
 $ LD_PRELOAD=/path/to/libtorsocks.so ssh -l kalexander -p 1234 prism.nsa.gov [&#8230;] </p>
<h2>Shell Usage</h2>
<p>Set LD_PRELOAD to load the library then use applications as normal. The syntax to force preload of the library for different shells is specified below: </p>
<p> Bash, Ksh and Bourne shell: </p>
<p> $ export LD_PRELOAD=/path/to/libtorsocks.so </p>
<p> C Shell: </p>
<p> $ setenv LD_PRELOAD=/path/to/libtorsocks.so </p>
<p> This process can be automated (for Bash, Bourne and Korn shell users) for a single command or for all commands in a shell session by using the <code><a href="/docs/linux/man/1-torsocks/">torsocks</a>(1)</code> script. </p>
<p> You can also setup <code><a href="/docs/linux/man/1-torsocks/">torsocks</a>(1)</code> in such a way that all processes automatically use it, a very useful configuration. Please refer to the torsocks script documentation for more information.</p>
<h2>Environment Variables</h2>
<dl>
<dt>TORSOCKS_CONF_FILE</p>
<dd>This environment variable overrides the default location of the torsocks configuration file. This variable is not honored if the program torsocks is embedded in is setuid. </p>
</dl>
<dl>
<dt>TORSOCKS_LOG_LEVEL</p>
<dd>Enable logging level of torsocks library. By default, warnings and errors are printed (level 3). Note that each level includes the lower ones except the 1 which disables any possible logging. (default: 3) </p>
<table>
<tr VALIGN=top>
<td>1</td>
<td> No log at all.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> Error messages.
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td> Warning messages.
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td> Notice messages.
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td> Debug messages.
</td>
</tr>
</table>
</dl>
<dl>
<dt>TORSOCKS_LOG_TIME</p>
<dd>Control whether or not the time is added to each logging line. (default: 1) </p>
</dl>
<dl>
<dt>TORSOCKS_LOG_FILE_PATH</p>
<dd>If set, torsocks will log in the file set by this variable. (default: stderr) </p>
</dl>
<dl>
<dt>TORSOCKS_USERNAME</p>
<dd>Set the username for the SOCKS5 authentication method. Password MUST be set also with the variable below. </p>
</dl>
<dl>
<dt>TORSOCKS_PASSWORD</p>
<dd>Set the password for the SOCKS5 authentication method. Username MUST be set also with the variable above. </p>
</dl>
<dl>
<dt>TORSOCKS_ALLOW_INBOUND</p>
<dd>Allow inbound connections so the application can accept and listen for connections. </p>
</dl>
<dl>
<dt>TORSOCKS_ISOLATE_PID</p>
<dd>Set the username and password for the SOCKS5 authentication method to a PID/current time based value automatically. Username and Password MUST NOT be set. </p>
</dl>
<h2>Known Issues</h2>
<h3>Dns</h3>
<p>Torsocks is not able to send DNS queries through Tor since UDP is not supported. Thus, any UDP socket is denied. However, DNS queries that can be intercept are sent to Tor and sent back to the caller.</p>
<h3>Errors</h3>
<p>Torsocks might generate error messages and print them to stderr when there are problems with the configuration file or the SOCKS negotiation with the Tor daemon. The TORSOCKS_LOG_LEVEL environment variable controls that behavior as well as the log file option. Keep in mind that this library can output on the stderr of the application.</p>
<h2>Limitations</h2>
<p>Outgoing TCP connections can only be proxified through the Tor network. </p>
<p> Torsocks forces the libc resolver to use TCP for name queries, if it does this it does it regardless of whether or not the DNS to be queried is local or not. This introduces overhead and should only be used when needed. </p>
<p> Torsocks uses ELF dynamic loader features to intercept dynamic function calls from programs in which it is embedded. As a result, non-ELF executables, or executables that make system calls directly with the system call trap (int 0x80).</p>
<h2>Files</h2>
<p>/etc/tor/torsocks.conf &#8211; default torsocks configuration file</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-torsocks-conf/">torsocks.conf</a>(5),</code> <code><a href="/docs/linux/man/1-torsocks/">torsocks</a>(1)</code> </p>
<h2>Author</h2>
<p>David Goulet &lt;dgoulet [at] ev0ke.net&gt;</p>
