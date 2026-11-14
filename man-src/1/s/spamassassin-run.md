---
title: "spamassassin-run(1)"
name: "spamassassin-run"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spamassassin-run/"
description: "spamassassin – simple front-end filtering script for SpamAssassin"
---

<h2 class="name">NAME</h2>
<p> spamassassin &#8211; simple front-end filtering script for SpamAssassin </p>
<h2>SYNOPSIS</h2>
<p> <code>spamassassin</code> [options] [ &lt; <i>mailmessage</i> | <i>path</i> &#8230; ] </p>
<p> <code>spamassassin</code> <code>-d</code> [ &lt; <i>mailmessage</i> | <i>path</i> &#8230; ] </p>
<p> <code>spamassassin</code> <code>-r</code> [ &lt; <i>mailmessage</i> | <i>path</i> &#8230; ] </p>
<p> <code>spamassassin</code> <code>-k</code> [ &lt; <i>mailmessage</i> | <i>path</i> &#8230; ] </p>
<p> <code>spamassassin</code> <code>-W</code>|<code>-R</code> [ &lt; <i>mailmessage</i> | <i>path</i> &#8230; ] </p>
<p> Options: </p>
<pre><code>
 -L, --local                       Local tests only (no online tests)
 -r, --report                      Report message as spam
 -k, --revoke                      Revoke message as spam
 -d, --remove-markup               Remove spam reports from a message
 -C path, --configpath=path, --config-file=path
                                   Path to standard configuration dir
 -p prefs, --prefspath=file, --prefs-file=file
                                   Set user preferences file
 --siteconfigpath=path             Path for site configs
                                   (def: /etc/mail/spamassassin)
 --cf='config line'                Additional line of configuration
 -x, --nocreate-prefs              Don't create user preferences file
 -e, --exit-code                   Exit with a non-zero exit code if the
                                   tested message was spam
 --mbox                            read in messages in mbox format
 --mbx                             read in messages in UW mbx format
 -t, --test-mode                   Pipe message through and add extra
                                   report to the bottom
 --lint                            Lint the rule set: report syntax errors
 -W, --add-to-whitelist            Add addresses in mail to persistent address whitelist
 --add-to-blacklist                Add addresses in mail to persistent address blacklist
 -R, --remove-from-whitelist       Remove all addresses found in mail from
                                   persistent address list
 --add-addr-to-whitelist=addr      Add addr to persistent address whitelist
 --add-addr-to-blacklist=addr      Add addr to persistent address blacklist
 --remove-addr-from-whitelist=addr Remove addr from persistent address list
 -4 --ipv4only, --ipv4-only, --ipv4 Use IPv4, disable use of IPv6 for DNS etc.
 -6                                Use IPv6, disable use of IPv4 where possible
 --progress                        Print progress bar
 -D, --debug [area=n,...]          Print debugging messages
 -V, --version                     Print version
 -h, --help                        Print usage message
</code></pre>
<h2>DESCRIPTION</h2>
<p> spamassassin is a simple front-end filter for SpamAssassin. </p>
<p> Using the SpamAssassin rule base, it uses a wide range of heuristic tests on mail headers and body text to identify &#8220;spam&#8221;, also known as unsolicited bulk email. Once identified, the mail is then tagged as spam for later filtering using the user&#8217;s own mail user-agent application. </p>
<p> The default tagging operations that take place are detailed in &#8220;<font SIZE="-1">TAGGING&#8221;</font> in spamassassin. </p>
<p> By default, message(s) are read in from <font SIZE="-1">STDIN </font>(&lt; <i>mailmessage</i>), or from specified files and directories (<i>path</i> &#8230;) <font SIZE="-1">STDIN</font> and files are assumed to be in <i>file</i> format, with a single message per file. Directories are assumed to be in a format where each file in the directory contains only one message (directories are not recursed and filenames containing whitespace or beginning with &#8220;.&#8221; or &#8220;,&#8221; are skipped). The options <i>&#8211;mbox</i> and <i>&#8211;mbx</i> can override the assumed format, see the appropriate <font SIZE="-1">OPTION</font> information below. </p>
<p> Please note that SpamAssassin is not designed to scan large messages. Don&#8217;t feed messages larger than about 500 <font SIZE="-1">KB</font> to SpamAssassin, as this will consume a huge amount of memory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code>, <code>&#8211;error-code</code>, <code>&#8211;exit-code</code></p>
<dd> Exit with a non-zero error code, if the message is determined to be spam.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit.</p>
<dt><code>-t</code>, <code>&#8211;test-mode</code></p>
<dd> Test mode. Pipe message through and add extra report. Note that the report text assumes that the message is spam, since in normal use it is only visible in this case. Pay attention to the score instead. </p>
<p> If you run this with <code>-d</code>, the message will first have SpamAssassin markup removed before being tested.</p>
<dt><code>-r</code>, <code>&#8211;report</code></p>
<dd> Report this message as manually-verified spam. This will submit the mail message read from <font SIZE="-1">STDIN</font> to various spam-blocker databases. Currently, these are the Distributed Checksum Clearinghouse <tt>&quot;<a rel="nofollow" href="http://www.dcc-servers.net/dcc/">http://www.dcc-servers.net/dcc/</a>&quot;</tt>, Pyzor <tt>&quot;<a rel="nofollow" href="http://pyzor.sourceforge.net/">http://pyzor.sourceforge.net/</a>&quot;</tt>, Vipul&#8217;s Razor <tt>&quot;<a rel="nofollow" href="http://razor.sourceforge.net/">http://razor.sourceforge.net/</a>&quot;</tt>, and SpamCop <tt>&quot;<a href="http://www.spamcop.net/">http://www.spamcop.net/</a>&quot;</tt>. </p>
<p> If the message contains SpamAssassin markup, the markup will be stripped out automatically before submission. The support modules for <font SIZE="-1">DCC,</font> Pyzor, and Razor must be installed for spam to be reported to each service. SpamCop reports will have greater effect if you register and set the <tt>&quot;spamcop_to_address&quot;</tt> option. </p>
<p> The message will also be submitted to SpamAssassin&#8217;s learning systems; currently this is the internal Bayesian statistical-filtering system (the <font SIZE="-1">BAYES</font> rules). (Note that if you <i>only</i> want to perform statistical learning, and do not want to report mail to third-parties, you should use the <tt>&quot;sa-learn&quot;</tt> command directly instead.)</p>
<dt><code>-k</code>, <code>&#8211;revoke</code></p>
<dd> Revoke this message. This will revoke the mail message read from <font SIZE="-1">STDIN</font> from various spam-blocker databases. Currently, these are Vipul&#8217;s Razor. </p>
<p> Revocation support for the Distributed Checksum Clearinghouse, Pyzor, and SpamCop is not currently available. </p>
<p> If the message contains SpamAssassin markup, the markup will be stripped out automatically before submission. The support modules for Razor must be installed for spam to be revoked from the service. </p>
<p> The message will also be submitted as &#8216;ham&#8217; (non-spam) to SpamAssassin&#8217;s learning systems; currently this is the internal Bayesian statistical-filtering system (the <font SIZE="-1">BAYES</font> rules). (Note that if you <i>only</i> want to perform statistical learning, and do not want to report mail to third-parties, you should use the <tt>&quot;sa-learn&quot;</tt> command directly instead.)</p>
<dt><code>&#8211;lint</code></p>
<dd> Syntax check (lint) the rule set and configuration files, reporting typos and rules that do not compile correctly. Exits with 0 if there are no errors, or greater than 0 if any errors are found.</p>
<dt><code>-W</code>, <code>&#8211;add-to-whitelist</code></p>
<dd> Add all email addresses, in the headers and body of the mail message read from <font SIZE="-1">STDIN,</font> to a persistent address whitelist. Note that you must be running <tt>&quot;spamassassin&quot;</tt> or <tt>&quot;spamd&quot;</tt> with a persistent address list plugin enabled for this to work.</p>
<dt><code>&#8211;add-to-blacklist</code></p>
<dd> Add all email addresses, in the headers and body of the mail message read from <font SIZE="-1">STDIN,</font> to the persistent address blacklist. Note that you must be running <tt>&quot;spamassassin&quot;</tt> or <tt>&quot;spamd&quot;</tt> with a persistent address list plugin enabled for this to work.</p>
<dt><code>-R</code>, <code>&#8211;remove-from-whitelist</code></p>
<dd> Remove all email addresses, in the headers and body of the mail message read from <font SIZE="-1">STDIN,</font> from a persistent address list. <font SIZE="-1">STDIN</font> must contain a full email message, so to remove a single address you should use <code>&#8211;remove-addr-from-whitelist</code> instead. </p>
<p> Note that you must be running <tt>&quot;spamassassin&quot;</tt> or <tt>&quot;spamd&quot;</tt> with a persistent address list plugin enabled for this to work.</p>
<dt><code>&#8211;add-addr-to-whitelist</code></p>
<dd> Add the named email address to a persistent address whitelist. Note that you must be running <tt>&quot;spamassassin&quot;</tt> or <tt>&quot;spamd&quot;</tt> with a persistent address list plugin enabled for this to work.</p>
<dt><code>&#8211;add-addr-to-blacklist</code></p>
<dd> Add the named email address to a persistent address blacklist. Note that you must be running <tt>&quot;spamassassin&quot;</tt> or <tt>&quot;spamd&quot;</tt> with a persistent address list plugin enabled for this to work.</p>
<dt><code>&#8211;remove-addr-from-whitelist</code></p>
<dd> Remove the named email address from a persistent address whitelist. Note that you must be running <tt>&quot;spamassassin&quot;</tt> or <tt>&quot;spamd&quot;</tt> with a persistent address list plugin enabled for this to work.</p>
<dt><code> &#8211;ipv4only</code>, <code>&#8211;ipv4-only</code>, <code>&#8211;ipv4</code></p>
<dd> Do not use IPv6 for <font SIZE="-1">DNS</font> tests. Normally, SpamAssassin will try to detect if IPv6 is available, using only IPv4 if it is not. Use if the existing tests for IPv6 availability produce incorrect results or crashes.</p>
<dt><code>-L</code>, <code>&#8211;local</code></p>
<dd> Do only the &#8221;local&#8221; tests, ones that do not require an internet connection to operate. Normally, SpamAssassin will try to detect whether you are connected to the net before doing these tests anyway, but for faster checks you may wish to use this. </p>
<p> Note that SpamAssassin&#8217;s network rules are run in parallel. This can cause overhead in terms of the number of file descriptors required if <code>&#8211;local</code> is not used; it is recommended that the minimum limit on fds be raised to at least 256 for safety.</p>
<dt><code>-d</code>, <code>&#8211;remove-markup</code></p>
<dd> Remove SpamAssassin markup (the &#8220;SpamAssassin results&#8221; report, X-Spam-Status headers, etc.) from the mail message. The resulting message, which will be more or less identical to the original, pre-SpamAssassin input, will be output to <font SIZE="-1">STDOUT.</font> </p>
<p> (Note: the message will not be exactly identical; some headers will be reformatted due to some features of the Mail::Internet package, but the body text will be.)</p>
<dt><code>-C</code> <i>path</i>, <code>&#8211;configpath</code>=<i>path</i>, <code>&#8211;config-file</code>=<i>path</i></p>
<dd> Use the specified path for locating the distributed configuration files. Ignore the default directories (usually <tt>&quot;/usr/share/spamassassin&quot;</tt> or similar).</p>
<dt><code>&#8211;siteconfigpath</code>=<i>path</i></p>
<dd> Use the specified path for locating site-specific configuration files. Ignore the default directories (usually <tt>&quot;/etc/mail/spamassassin&quot;</tt> or similar).</p>
<dt><code>&#8211;cf=&#8217;config line&#8217;</code></p>
<dd> Add additional lines of configuration directly from the command-line, parsed after the configuration files are read. Multiple <code>&#8211;cf</code> arguments can be used, and each will be considered a separate line of configuration. For example: </p>
<pre>
        spamassassin -t --cf=&quot;body NEWRULE /text/&quot; --cf=&quot;score NEWRULE 3.0&quot;
</pre>
<dt><code>-p</code> <i>prefs</i>, <code>&#8211;prefspath</code>=<i>prefs</i>, <code>&#8211;prefs-file</code>=<i>prefs</i></p>
<dd> Read user score preferences from <i>prefs</i> (usually <tt>&quot;$HOME/.spamassassin/user_prefs&quot;</tt>).</p>
<dt><code>&#8211;progress</code></p>
<dd> Prints a progress bar (to <font SIZE="-1">STDERR</font>) showing the current progress. This option will only be useful if you are redirecting <font SIZE="-1">STDOUT </font>(and not <font SIZE="-1">STDERR</font>). In the case where no valid terminal is found this option will behave very much like the &#8211;showdots option in other SpamAssassin programs.</p>
<dt><code>-D</code> [<i>area,&#8230;</i>], <code>&#8211;debug</code> [<i>area,&#8230;</i>]</p>
<dd> Produce debugging output. If no areas are listed, all debugging information is printed. Diagnostic output can also be enabled for each area individually; <i>area</i> is the area of the code to instrument. For example, to produce diagnostic output on bayes, learn, and dns, use: </p>
<pre>
        spamassassin -D bayes,learn,dns
</pre>
<p> Higher priority informational messages that are suitable for logging in normal circumstances are available with an area of &#8220;info&#8221;. </p>
<p> For more information about which areas (also known as channels) are available, please see the documentation at: </p>
<pre>
        L&lt;<a rel="nofollow" href="http://wiki.apache.org/spamassassin/DebugChannels">http://wiki.apache.org/spamassassin/DebugChannels</a>&gt;
</pre>
<dt><code>-x</code>, <code>&#8211;nocreate-prefs</code></p>
<dd> Disable creation of user preferences file.</p>
<dt><code>&#8211;mbox</code></p>
<dd> Specify that the input message(s) are in mbox format. mbox is a standard Unix message folder format.</p>
<dt><code>&#8211;mbx</code></p>
<dd> Specify that the input message(s) are in <font SIZE="-1">UW </font>.mbx format. mbx is the mailbox format used within the University of Washington&#8217;s <font SIZE="-1">IMAP</font> implementation; see <tt>&quot;<a rel="nofollow" href="http://www.washington.edu/imap/">http://www.washington.edu/imap/</a>&quot;</tt>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-sa-learn/">sa-learn</a></i>(1) <i><a href="/docs/linux/man/1-spamd/">spamd</a></i>(1) <i><a href="/docs/linux/man/1-spamc/">spamc</a></i>(1) <i><a href="/docs/linux/man/3-mail--spamassassin--conf/">Mail::SpamAssassin::Conf</a></i>(3) <i><a href="/docs/linux/man/3-mail--spamassassin/">Mail::SpamAssassin</a></i>(3)</p>
<h2>PREREQUISITES</h2>
<p> <tt>&quot;Mail::SpamAssassin&quot;</tt></p>
<h2>BUGS</h2>
<p> See &lt;<a rel="nofollow" href="http://issues.apache.org/SpamAssassin/">http://issues.apache.org/SpamAssassin/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> The SpamAssassin(tm) Project &lt;<a rel="nofollow" href="http://spamassassin.apache.org/">http://spamassassin.apache.org/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> SpamAssassin is distributed under the Apache License, Version 2.0, as described in the file <tt>&quot;LICENSE&quot;</tt> included with the distribution. </p>
<h2>Index</h2>
