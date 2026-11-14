---
title: "sieve-dump(1)"
name: "sieve-dump"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sieve-dump/"
description: "sieve-dump – Pigeonhole’s Sieve script binary dump tool"
---

<h2 class="name">NAME</h2>
<p> sieve-dump &#8211; Pigeonhole&#8217;s Sieve script binary dump tool </p>
<h2>SYNOPSIS</h2>
<p> <code>sieve-dump</code> [<i>options</i>] <i>sieve-binary</i> [<i>out-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>sieve-dump</code> command is part of the Pigeonhole Project (<code><a href="/docs/linux/man/7-pigeonhole/">pigeonhole</a></code>(7)), which adds Sieve (RFC 5228) support to the Dovecot secure IMAP and POP3 server (<code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1)). </p>
<p> Using the <code>sieve-dump</code> command, Sieve binaries, which are produced for instance by <code><a href="/docs/linux/man/1-sievec/">sievec</a></code>(1), can be transformed into a human-readable textual representation. This can provide valuable insight in how the Sieve script is executed. This is also particularly useful to view corrupt binaries that can result from bugs in the Sieve implementation. This tool is intended mainly for development purposes, so normally system administrators and users will not need to use this tool. </p>
<p> The format of the output is not explained here in detail, but it should be relatively easy to understand. The Sieve binaries comprise a set of data blocks, each of which can contain arbitrary data. For the base language implementation two blocks are used: the first containing a specification of all required language extensions and the second containing the main Sieve program. Compiled Sieve programs are represented as flat byte code and therefore the dump of the main program is a disassembly listing of the interpreter operations. Extensions can define new operations and use additional blocks. Therefore, the output of <code>sieve-dump</code> depends greatly on the language extensions used when compiling the binary.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>config-file</i></p>
<dd> Alternative Dovecot configuration file path.</p>
<dt><code>-D</code></p>
<dd> Enable Sieve debugging.</p>
<dt><code>-h</code></p>
<dd> Produce per-block hexdump output of the whole binary instead of the normal human-readable output.</p>
<dt><code>-x&nbsp;<wbr></code><i>extensions</i></p>
<dd> Set the available extensions. The parameter is a space-separated list of the active extensions. By prepending the extension identifiers with <code>+</code> or <code>&#8211;</code>, extensions can be included or excluded relative to the configured set of active extensions. If no extensions have a <code>+</code> or <code>&#8211;</code> prefix, only those extensions that are explicitly listed will be enabled. Unknown extensions are ignored and a warning is produced. </p>
<p> For example <code>-x</code> &quot;+imapflags -enotify&quot; will enable the deprecated imapflags extension and disable the enotify extension. The rest of the active extensions depends on the <i>sieve_extensions</i> and <i>sieve_global_extensions</i> settings. By default, i.e. when <i>sieve_extensions</i> and <i>sieve_global_extensions</i> remain unconfigured, all supported extensions are available, except for deprecated extensions or those that are still under development. </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>sieve-binary</i></p>
<dd> Specifies the Sieve binary file that needs to be dumped.</p>
<dt><i>out-file</i></p>
<dd> Specifies where the output must be written. This argument is optional. If omitted, the output is written to <code>stdout</code>.</dl>
<h2>EXIT STATUS</h2>
<p> <code>sieve-dump</code> will exit with one of the following values:</p>
<dl>
<dt><code>0</code></p>
<dd> Dump was successful. (EX_OK, EXIT_SUCCESS)</p>
<dt><code>1</code></p>
<dd> Operation failed. This is returned for almost all failures. (EXIT_FAILURE)</p>
<dt><code>64</code></p>
<dd> Invalid parameter given. (EX_USAGE)</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></p>
<dd> Dovecot&#8217;s main configuration file.</p>
<dt><i>/etc/dovecot/conf.d/90-sieve.conf</i></p>
<dd> Sieve interpreter settings (included from Dovecot&#8217;s main configuration file)</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting Dovecot and Pigeonhole bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1), <code><a href="/docs/linux/man/1-sieve-filter/">sieve-filter</a></code>(1), <code><a href="/docs/linux/man/1-sieve-test/">sieve-test</a></code>(1), <code><a href="/docs/linux/man/1-sievec/">sievec</a></code>(1), <code><a href="/docs/linux/man/7-pigeonhole/">pigeonhole</a></code>(7) </p>
<h2>Index</h2>
