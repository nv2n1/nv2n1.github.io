---
title: "tftp(1)"
name: "tftp"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tftp/"
description: "tftp – IPv4 Trivial File Transfer Protocol client"
---

<h2>NAME</h2>
<p> <code>tftp</code> &#8211; IPv4 Trivial File Transfer Protocol client</p>
<h2>SYNOPSIS</h2>
<p> <code>tftp</code> [ <i>options&#8230;</i> ] [<i>host</i> [<i>port</i>]] [<code>-c</code> <i>command</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>tftp</code> is a client for the Trivial file Transfer Protocol, which can be used to transfer files to and from remote machines, including some very minimalistic, usually embedded, systems. The remote <i>host</i> may be specified on the command line, in which case <code>tftp</code> uses <i>host</i> as the default host for future transfers (see the <code>connect</code> command below.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-4</code></p>
<dd> Connect with IPv4 only, even if IPv6 support was compiled in.</p>
<dt><code>-6</code></p>
<dd> Connect with IPv6 only, if compiled in.</p>
<dt><code>-c</code> <i>command</i></p>
<dd> Execute <i>command</i> as if it had been entered on the tftp prompt. Must be specified last on the command line.</p>
<dt><code>-l</code></p>
<dd> Default to literal mode. Used to avoid special processing of &#8216;:&#8217; in a file name.</p>
<dt><code>-m</code> <i>mode</i></p>
<dd> Set the default transfer mode to <i>mode</i>. This is usually used with -c.</p>
<dt><code>-R</code> <i>port:port</i></p>
<dd> Force the originating port number to be in the specified range of port numbers.</p>
<dt><code>-v</code></p>
<dd> Default to verbose mode.</p>
<dt><code>-V</code></p>
<dd> Print the version number and configuration to standard output, then exit gracefully.</dl>
<h2>COMMANDS</h2>
<p> Once <code>tftp</code> is running, it issues the prompt <tt>tftp&gt;</tt> and recognizes the following commands:</p>
<dl>
<dt><code>?</code> <i>command-name&#8230;</i></p>
<dd>
<dt><code>help</code> <i>command-name&#8230;</i></p>
<dd> Print help information</p>
<dt><code>ascii</code></p>
<dd> Shorthand for <code>mode ascii</code>.</p>
<dt><code>binary</code></p>
<dd> Shorthand for <code>mode binary</code>.</p>
<dt><code>connect</code> <i>host [port]</i></p>
<dd> Set the <i>host</i> (and optionally <i>port</i>) for transfers. Note that the TFTP protocol, unlike the FTP protocol, does not maintain connections between transfers; thus, the <code>connect</code> command does not actually create a connection, but merely remembers what host is to be used for transfers. You do not have to use the <code>connect</code> command; the remote host can be specified as part of the <code>get</code> or <code>put</code> commands.</p>
<dt><code>get</code> <i>file</i></p>
<dd>
<dt><code>get</code> <i>remotefile localfile</i></p>
<dd>
<dt><code>get</code> <i>file1 file2 file3&#8230;</i></p>
<dd> Get a file or set of files from the specified sources. A remote filename can be in one of two forms: a plain filename on the remote host, if the host has already been specified, or a string of the form <i>host:filename</i> to specify both a host and filename at the same time. If the latter form is used, the last hostname specified becomes the default for future transfers. Enable <code>literal</code> mode to prevent special treatment of the &#8216;:&#8217; character (e.g. C:\dirile).</p>
<dt><code>literal</code></p>
<dd> Toggle literal mode. When set, this mode prevents special treatment of &#8216;:&#8217; in filenames.</p>
<dt><code>mode</code> <i>transfer-mode</i></p>
<dd> Specify the mode for transfers; <i>transfer-mode</i> may be one of <code>ascii</code> (or <code>netascii</code>) or <code>binary</code> (or <code>octet</code>.) The default is <code>ascii</code>.</p>
<dt><code>put</code> <i>file</i></p>
<dd>
<dt><code>put</code> <i>localfile remotefile</i></p>
<dd>
<dt><code>put</code> <i>file1 file2 file3&#8230; remote-directory</i></p>
<dd> Put a file or set of files to the specified remote file or directory. The destination can be in one of two forms: a filename on the remote host, if the host has already been specified, or a string of the form <i>host:filename</i> to specify both a host and filename at the same time. If the latter form is used, the hostname specified becomes the default for future transfers. If the remote-directory form is used, the remote host is assumed to be a UNIX system or another system using <code>/</code> as directory separator. Enable <code>literal</code> mode to prevent special treatment of the &#8216;:&#8217; character (e.g. C:\dirile).</p>
<dt><code>quit</code></p>
<dd> Exit <code>tftp</code>. End-of-file will also exit.</p>
<dt><code>rexmt</code> <i>retransmission-timeout</i></p>
<dd> Set the per-packet retransmission timeout, in seconds.</p>
<dt><code>status</code></p>
<dd> Show current status.</p>
<dt><code>timeout</code> <i>total-transmission-timeout</i></p>
<dd> Set the total transmission timeout, in seconds.</p>
<dt><code>trace</code></p>
<dd> Toggle packet tracing (a debugging feature.)</p>
<dt><code>verbose</code></p>
<dd> Toggle verbose mode.</dl>
<h2>NOTES</h2>
<p> The TFTP protocol provides no provisions for authentication or security. Therefore, the remote server will probably implement some kinds of access restriction or firewalling. These access restrictions are likely to be site- and server-specific.</p>
<h2>AUTHOR</h2>
<p> This version of <code>tftp</code> is maintained by H. Peter Anvin &lt;hpa [at] zytor.com&gt;. It was derived from, but has substantially diverged from, an OpenBSD source base, with added patches by Markus Gutschke and Gero Kulhman.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-tftpd/">tftpd</a></code>(8). </p>
<h2>Index</h2>
