---
title: "sievec(1)"
name: "sievec"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sievec/"
description: "sievec – Pigeonhole’s Sieve script compiler"
---

<h2 class="name">NAME</h2>
<p> sievec &#8211; Pigeonhole&#8217;s Sieve script compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>sievec</code> [<i>options</i>] <i>script-file</i> [<i>out-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>sievec</code> command is part of the Pigeonhole Project (<code><a href="/docs/linux/man/7-pigeonhole/">pigeonhole</a></code>(7)), which adds Sieve (RFC 5228) support to the Dovecot secure IMAP and POP3 server (<code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1)). </p>
<p> Using the <code>sievec</code> command, Sieve scripts can be compiled into a binary representation. The resulting binary can be used directly to process e-mail messages during the delivery process. The delivery of mail messages and &#8211; by means of the LDA Sieve plugin &#8211; also the execution of Sieve scripts is performed by Dovecot&#8217;s local delivery agent (LDA) called <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1). Usually, it is not necessary to compile the Sieve script manually using <code>sievec</code>, because <code>dovecot-lda</code> will do this automatically if the binary is missing. However, in some cases <code>dovecot-lda</code> does not have permission to write the compiled binary to disk, forcing it to recompile the script every time it is executed. Using the <code>sievec</code> tool, this can be performed manually by an authorized user to increase performance. </p>
<p> The Pigeonhole Sieve implementation recognizes files with a <code>.sieve</code> extension as Sieve scripts and corresponding files with a <code>.svbin</code> extension as the associated compiled binary. This means for example that Dovecot&#8217;s LDA process will first look for a binary file &quot;dovecot.svbin&quot; when it needs to execute &quot;dovecot.sieve&quot;. It will compile a new binary when it is missing or outdated. </p>
<p> The <code>sievec</code> command is also useful to verify Sieve scripts before using. Additionally, with the <code>-d</code> option it can output a textual (and thus human-readable) dump of the generated Sieve code to the specified file. The output is then identical to what the <code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a></code>(1) command produces for a stored binary file. This output is mainly useful to find bugs in the compiler that yield corrupt binaries.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c&nbsp;<wbr></code><i>config-file</i></p>
<dd> Alternative Dovecot configuration file path.</p>
<dt><code>-d</code></p>
<dd> Don&#8217;t write the binary to <i>out-file</i>, but write a textual dump of the binary instead. In this context, the <i>out-file</i> value &#8216;-&#8216; has special meaning: it causes the the textual dump to be written to <code>stdout</code>. The <i>out-file</i> argument may also be omitted, which has the same effect as &#8216;-&#8216;. The output is identical to what the <code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a></code>(1) command produces for a compiled Sieve binary file. Note that this option is not allowed when the <i>out-file</i> argument is a directory.</p>
<dt><code>-D</code></p>
<dd> Enable Sieve debugging.</p>
<dt><code>-x&nbsp;<wbr></code><i>extensions</i></p>
<dd> Set the available extensions. The parameter is a space-separated list of the active extensions. By prepending the extension identifiers with <code>+</code> or <code>&#8211;</code>, extensions can be included or excluded relative to the configured set of active extensions. If no extensions have a <code>+</code> or <code>&#8211;</code> prefix, only those extensions that are explicitly listed will be enabled. Unknown extensions are ignored and a warning is produced. </p>
<p> For example <code>-x</code> &quot;+imapflags -enotify&quot; will enable the deprecated imapflags extension and disable the enotify extension. The rest of the active extensions depends on the <i>sieve_extensions</i> and <i>sieve_global_extensions</i> settings. By default, i.e. when <i>sieve_extensions</i> and <i>sieve_global_extensions</i> remain unconfigured, all supported extensions are available, except for deprecated extensions or those that are still under development. </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>script-file</i></p>
<dd> Specifies the script to be compiled. If the <i>script-file</i> argument is a directory, all files in that directory with a <i>.sieve</i> extension are compiled into a corresponding <i>.svbin</i> binary file. The compilation is not halted upon errors; it attempts to compile as many scripts in the directory as possible. Note that the <code>-d</code> option and the <i>out-file</i> argument are not allowed when the <i>script-file</i> argument is a directory.</p>
<dt><i>out-file</i></p>
<dd> Specifies where the (binary) output is to be written. This argument is optional. If this argument is omitted, a binary compiled from &lt;scriptname&gt;.sieve is saved as &lt;scriptname&gt;.svbin. If this argument is omitted and <code>-b</code> is specified, the binary dump is output to <code>stdout</code>.</dl>
<h2>EXIT STATUS</h2>
<p> <code>sievec</code> will exit with one of the following values:</p>
<dl>
<dt><code>0</code></p>
<dd> Compile was successful. (EX_OK, EXIT_SUCCESS)</p>
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
<p> <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1), <code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a></code>(1), <code><a href="/docs/linux/man/1-sieve-filter/">sieve-filter</a></code>(1), <code><a href="/docs/linux/man/1-sieve-test/">sieve-test</a></code>(1), <code><a href="/docs/linux/man/7-pigeonhole/">pigeonhole</a></code>(7) </p>
<h2>Index</h2>
