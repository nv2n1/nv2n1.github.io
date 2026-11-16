---
title: "sieve-test(1)"
name: "sieve-test"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sieve-test/"
description: "sieve-test – Pigeonhole’s Sieve script tester"
---

<h2>NAME</h2>
<p> sieve-test &#8211; Pigeonhole&#8217;s Sieve script tester</p>
<h2>SYNOPSIS</h2>
<p> <code>sieve-test</code> [<i>options</i>] <i>script-file</i> <i>mail-file</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>sieve-test</code> command is part of the Pigeonhole Project (<code><a href="/docs/linux/man/7-pigeonhole/">pigeonhole</a></code>(7)), which adds Sieve (RFC 5228) support to the Dovecot secure IMAP and POP3 server (<code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1)). </p>
<p> Using the <code>sieve-test</code> command, the execution of Sieve scripts can be tested. This evaluates the script for the provided message, yielding a set of Sieve actions. Unless the <code>-e</code> option is specified, it does not actually execute these actions, meaning that it does not store or forward the message anywere. In stead, it prints a detailed list of what actions would normally take place. Note that, even when <code>-e</code> is specified, no messages are ever transmitted to remote SMTP recipients. The outgoing messages are always printed to <code>stdout</code> in stead. </p>
<p> This is a very useful tool to debug the execution of Sieve scripts. It can be used to verify newly installed scripts for the intended behaviour and it can provide more detailed information about script execution problems that are reported by the Sieve plugin, for example by tracing the execution and evaluation of commands and tests respectively.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>orig-recipient-address</i></dt>
<dd> The original envelope recipient address. This is what Sieve&#8217;s envelope test will compare to when the &quot;to&quot; envelope part is requested. Some tests and actions will also use this as the script owner&#8217;s e-mail address. If this option is omitted, the recipient address is retrieved from the &quot;Envelope-To:&quot;, or &quot;To:&quot; message headers. If none of these headers is present either, the recipient address defaults to <i>recipient [at] example.com</i>.</dd>
<dt><code>-c&nbsp;<wbr></code><i>config-file</i></dt>
<dd> Alternative Dovecot configuration file path.</dd>
<dt><code>-C</code></dt>
<dd> Force compilation. By default, the compiled binary is stored on disk. When this binary is found during the next execution of <code>sieve-test</code> and its modification time is more recent than the script file, it is used and the script is not compiled again. This option forces the script to be compiled, thus ignoring any present binary. Refer to <code><a href="/docs/linux/man/1-sievec/">sievec</a></code>(1) for more information about Sieve compilation.</dd>
<dt><code>-D</code></dt>
<dd> Enable Sieve debugging.</dd>
<dt><code>-d&nbsp;<wbr></code><i>dump-file</i></dt>
<dd> Causes a dump of the generated code to be written to the specified file. This is identical to the dump produced by <code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a></code>(1). Using &#8216;-&#8216; as filename causes the dump to be written to <code>stdout</code>.</dd>
<dt><code>-e</code></dt>
<dd> Enables true execution of the set of actions that results from running the script. In combination with the <code>-l</code> parameter, the actual delivery of messages can be tested. Note that this will not transmit any messages to remote SMTP recipients. Such actions only print the outgoing message to <code>stdout</code>.</dd>
<dt><code>-f&nbsp;<wbr></code><i>envelope-sender</i></dt>
<dd> The envelope sender address (return path). This is what Sieve&#8217;s envelope test will compare to when the &quot;from&quot; envelope part is requested. Also, this is where response messages are &#8216;sent&#8217; to. If this option is omitted, the sender address is retrieved from the &quot;Return-Path:&quot;, &quot;Sender:&quot; or &quot;From:&quot; message headers. If none of these headers is present either, the sender envelope address defaults to <i>sender [at] example.com</i>.</dd>
<dt><code>-l&nbsp;<wbr></code><i>mail-location</i></dt>
<dd> The location of the user&#8217;s mail store. The syntax of this option&#8217;s <i>mail-location</i> parameter is identical to what is used for the mail_location setting in the Dovecot config file. This parameter is typically used in combination with <code>-e</code> to test the actual delivery of messages. If <code>-l</code> is omitted when <code>-e</code> is specified, mail store actions like fileinto and keep are skipped.</dd>
<dt><code>-m&nbsp;<wbr></code><i>default-mailbox</i></dt>
<dd> The mailbox where the keep action stores the message. This is &quot;INBOX&quot; by default.</dd>
<dt><code>-r&nbsp;<wbr></code><i>recipient-address</i></dt>
<dd> The final envelope recipient address. Some tests and actions will use this as the script owner&#8217;s e-mail address. For example, this is what is used by the vacation action to check whether a reply is appropriate. If the <code>-r</code> option is omitted, the orignal envelope recipient address will be used in stead (see <code>-a</code> option for more info).</dd>
<dt><code>-s&nbsp;<wbr></code><i>script-file</i></dt>
<dd> Specify additional scripts to be executed before the main script. Multiple <code>-s</code> arguments are allowed and the specified scripts are executed sequentially in the order specified at the command line.</dd>
<dt><code>-t&nbsp;<wbr></code><i>trace-file</i></dt>
<dd> Enables runtime trace debugging. Trace debugging provides detailed insight in the operations performed by the Sieve script. Refer to the runtime trace debugging section below. The trace information is written to the specified file. Using &#8216;-&#8216; as filename causes the trace data to be written to <code>stdout</code>.</dd>
<dt><code>-T&nbsp;<wbr></code><i>trace-option</i></dt>
<dd> Configures runtime trace debugging, which is enabled with the -t option. Refer to the runtime trace debugging section below.</dd>
<dt><code>-x&nbsp;<wbr></code><i>extensions</i></dt>
<dd> Set the available extensions. The parameter is a space-separated list of the active extensions. By prepending the extension identifiers with <code>+</code> or <code>&#8211;</code>, extensions can be included or excluded relative to the configured set of active extensions. If no extensions have a <code>+</code> or <code>&#8211;</code> prefix, only those extensions that are explicitly listed will be enabled. Unknown extensions are ignored and a warning is produced. </dd>
<p> For example <code>-x</code> &quot;+imapflags -enotify&quot; will enable the deprecated imapflags extension and disable the enotify extension. The rest of the active extensions depends on the <i>sieve_extensions</i> and <i>sieve_global_extensions</i> settings. By default, i.e. when <i>sieve_extensions</i> and <i>sieve_global_extensions</i> remain unconfigured, all supported extensions are available, except for deprecated extensions or those that are still under development. </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>script-file</i></dt>
<dd> Specifies the script to (compile and) execute. </dd>
<p> Note that this tool looks for a pre-compiled binary file with a <i>.svbin</i> extension and with basename and path identical to the specified script. Use the <code>-C</code> option to disable this behavior by forcing the script to be compiled into a new binary.</p>
<dt><i>mail-file</i></dt>
<dd> Specifies the file containing the e-mail message to test with.</dd></dl>
<h2>USAGE</h2>
<h3>RUNTIME TRACE DEBUGGING</h3>
<p> Using the <code>-t</code> option, the <code>sieve-test</code> tool can be configured to print detailed trace information on the Sieve script execution to a file or standard output. For example, the encountered commands, the performed tests and the matched values can be printed. </p>
<p> The runtime trace can be configured using the <code>-T</code> option, which can be specified multiple times. It can be used as follows: </p>
<dl>
<dt><code>-Tlevel=&#8230;</code></dt>
<dd> Set the detail level of the trace debugging. One of the following values can be supplied:</dd>
<dl>
<dl>
<dt><i>actions</i> (default)</dt>
<dd> Only print executed action commands, like keep, fileinto, reject and redirect.</dd>
<dt><i>commands</i></dt>
<dd> Print any executed command, excluding test commands.</dd>
<dt><i>tests</i></dt>
<dd> Print all executed commands and performed tests.</dd>
<dt><i>matching</i></dt>
<dd> Print all executed commands, performed tests and the values matched in those tests.</dd></dl>
</dl>
<dt><code>-Tdebug</code></dt>
<dd> Print debug messages as well. This is usually only useful for developers and is likely to produce messy output.</dd>
<dt><code>-Taddresses</code></dt>
<dd> Print byte code addresses for the current trace output. Normally, only the current Sieve source code position (line number) is printed. The byte code addresses are equal to those listed in a binary dump produced using the <code>-d</code> option or by the <code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a>(1)</code> command.</dd></dl>
<h3>DEBUG SIEVE EXTENSION</h3>
<p> To improve script debugging, this Sieve implementation supports a custom Sieve language extension called &#8216;vnd.dovecot.debug&#8217;. It adds the <code>debug_log</code> command that allows logging debug messages. </p>
<p> Example: </p>
<p> require &quot;vnd.dovecot.debug&quot;; </p>
<p> if header :contains &quot;subject&quot; &quot;hello&quot; { </p>
<p>&nbsp;<wbr>&nbsp;<wbr>debug_log&nbsp;<wbr>&quot;Subject header contains hello!&quot;; </p>
<p> } </p>
<p> Tools such as <code>sieve-test</code>, <code>sievec</code> and <code>sieve-dump</code> have support for the vnd.dovecot.debug extension enabled by default and it is not necessary to enable nor possible to disable the availability of the debug extension with the <code>-x</code> option. The logged messages are written to <code>stdout</code> in this case. </p>
<p> In contrast, for the actual Sieve plugin for the Dovecot LDA (<code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1)) the vnd.dovecot.debug extension needs to be enabled explicitly using the <i>sieve_extensions</i> setting. The messages are then logged to the user&#8217;s private script log file. If used in a global script, the messages are logged through the default Dovecot logging facility.</p>
<h2>EXIT STATUS</h2>
<p> <code>sieve-test</code> will exit with one of the following values:</p>
<dl>
<dt><code>0</code></dt>
<dd> Execution was successful. (EX_OK, EXIT_SUCCESS)</dd>
<dt><code>1</code></dt>
<dd> Operation failed. This is returned for almost all failures. (EXIT_FAILURE)</dd>
<dt><code>64</code></dt>
<dd> Invalid parameter given. (EX_USAGE)</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/dovecot/dovecot.conf</i></dt>
<dd> Dovecot&#8217;s main configuration file.</dd>
<dt><i>/etc/dovecot/conf.d/90-sieve.conf</i></dt>
<dd> Sieve interpreter settings (included from Dovecot&#8217;s main configuration file)</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting Dovecot and Pigeonhole bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dovecot/">dovecot</a></code>(1), <code><a href="/docs/linux/man/1-dovecot-lda/">dovecot-lda</a></code>(1), <code><a href="/docs/linux/man/1-sieve-dump/">sieve-dump</a></code>(1), <code><a href="/docs/linux/man/1-sieve-filter/">sieve-filter</a></code>(1), <code><a href="/docs/linux/man/1-sievec/">sievec</a></code>(1), <code><a href="/docs/linux/man/7-pigeonhole/">pigeonhole</a></code>(7) </p>
<h2>Index</h2>
