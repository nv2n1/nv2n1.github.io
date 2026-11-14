---
title: "spamc(1)"
name: "spamc"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spamc/"
description: "spamc – client for spamd"
---

<h2 class="name">NAME</h2>
<p> spamc &#8211; client for spamd </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>spamc [options] &lt; message</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> Spamc is the client half of the spamc/spamd pair. It should be used in place of <tt>&quot;spamassassin&quot;</tt> in scripts to process mail. It will read the mail from <font SIZE="-1">STDIN,</font> and spool it to its connection to spamd, then read the result back and print it to <font SIZE="-1">STDOUT. </font> Spamc has extremely low overhead in loading, so it should be much faster to load than the whole spamassassin program. </p>
<p> See the <i></i><font SIZE="-1"><i>README</i></font><i></i> file in the <i>spamd</i> directory of the SpamAssassin distribution for more details.</p>
<h2>OPTIONS</h2>
<p> All options detailed below can be passed as command line arguments, or be contained in a configuration file, as described in the <font SIZE="-1"><code>CONFIGURATION FILE</code></font> section below. </p>
<p> Note that the long options, a la <tt>&quot;--long-options&quot;</tt>, are new as of SpamAssassin 3.2.0, and were not available in earlier versions.</p>
<dl>
<dt><code>-B</code>, <code>&#8211;bsmtp</code></p>
<dd> Assume input is a single BSMTP-formatted message. In other words, spamc will pull out everything between the <font SIZE="-1">DATA</font> line and the lone-dot line to feed to spamd, and will place the spamd output back in the same envelope (thus, any <font SIZE="-1">SIZE</font> extension in your <font SIZE="-1">BSMTP</font> file will cause many problems).</p>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd> Just check if the message is spam or not. Set process exitcode to 1 if message is spam, 0 if not spam or processing failure occurs. Will print score/threshold to stdout (as ints) or 0/0 if there was an error. Combining <code>-c</code> and <code>-E</code> is a no-op, since <code>-c</code> implies the behaviour of <code>-E</code>.</p>
<dt><code>-d</code> <i>host[,host2]</i>, <code>&#8211;dest</code>=<i>host[,host2]</i></p>
<dd> In <font SIZE="-1">TCP/IP</font> mode, connect to spamd server on given host (default: localhost). Several hosts can be specified if separated by commas. </p>
<p> If <i>host</i> resolves to multiple addresses, then spamc will fail-over to the other addresses, if the first one cannot be connected to. It will first try all addresses of one host before it tries the next one in the list. Note that this fail-over behaviour is incompatible with <code>-x</code>; if that switch is used, fail-over will not occur.</p>
<dt><code>-e</code> <i>command</i> <i>[args]</i>, <code>&#8211;pipe-to</code> <i>command</i> <i>[args]</i></p>
<dd> Instead of writing to stdout, pipe the output to <i>command</i>&#8216;s standard input. Note that there is a very slight chance mail will be lost here, because if the fork-and-exec fails there&#8217;s no place to put the mail message. </p>
<p> Note that this must be the <font SIZE="-1">LAST</font> command line option, as everything after the <code>-e</code> is taken as arguments to the command (it&#8217;s like <i>rxvt</i> or <i>xterm</i>). </p>
<p> This option is not supported on Win32 platforms.</p>
<dt><code>-E</code>, <code>&#8211;exitcode</code></p>
<dd> Filter according to the other options, but set the process exitcode to 1 if message is spam, 0 if not spam or processing failure occurs.</p>
<dt><code>-F</code> <i>/path/to/file</i>, <code>&#8211;config</code>=<i>path</i></p>
<dd> Specify a configuration file to read additional command-line flags from. See <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print this help message and terminate without action.</p>
<dt><code>-H</code>, <code>&#8211;randomize</code></p>
<dd> For <font SIZE="-1">TCP/IP</font> sockets, randomize the <font SIZE="-1">IP</font> addresses returned for the hosts given by the <code>-d</code> switch. This provides for a simple kind of load balancing. It will try only three times though.</p>
<dt><code>-l</code>, <code>&#8211;log-to-stderr</code></p>
<dd> Send log messages to stderr, instead of to the syslog.</p>
<dt><code>-L</code> <i>learn type</i>, <code>&#8211;learntype</code>=<i>type</i></p>
<dd> Send message to spamd for learning. The <tt>&quot;learn type&quot;</tt> can be either spam, ham or forget. The exitcode for spamc will be set to 5 if the message was learned, or 6 if it was already learned, under a condition that a <code>&#8211;no-safe-fallback</code> option is selected too. </p>
<p> Note that the <tt>&quot;spamd&quot;</tt> must run with the <tt>&quot;--allow-tell&quot;</tt> option for this to work.</p>
<dt><code>-C</code> <i>report type</i>, <code>&#8211;reporttype</code>=<i>type</i></p>
<dd> Report or revoke a message to one of the configured collaborative filtering databases. The <tt>&quot;report type&quot;</tt> can be either report or revoke. </p>
<p> Note that the <tt>&quot;spamd&quot;</tt> must run with the <tt>&quot;--allow-tell&quot;</tt> option for this to work.</p>
<dt><code>-p</code> <i>port</i>, <code>&#8211;port</code>=<i>port</i></p>
<dd> In <font SIZE="-1">TCP/IP</font> mode, connect to spamd server listening on given port (default: 783).</p>
<dt><code>-r</code>, <code>&#8211;full-spam</code></p>
<dd> Just output the SpamAssassin report text to stdout, if the message is spam. If the message is ham (non-spam), nothing will be printed. The first line of the output is the message score and the threshold, in this format: </p>
<pre>
        score/threshold
</pre>
<dt><code>-R</code>, <code>&#8211;full</code></p>
<dd> Just output the SpamAssassin report text to stdout, for all messages. See <code>-r</code> for details of the output format used.</p>
<dt><code>-s</code> <i>max_size</i>, <code>&#8211;max-size</code>=<i>max_size</i></p>
<dd> Set the maximum message size which will be sent to spamd &#8212; any bigger than this threshold and the message will be returned unprocessed (default: 500 <font SIZE="-1">KB</font>). If spamc gets handed a message bigger than this, it won&#8217;t be passed to spamd. The maximum message size is 256 <font SIZE="-1">MB.</font> </p>
<p> The size is specified in bytes, as a positive integer greater than 0. For example, <code>-s 500000</code>.</p>
<dt><code>&#8211;connect-retries</code>=<i>retries</i></p>
<dd> Retry connecting to spamd <i>retries</i> times. The default is 3 times.</p>
<dt><code>&#8211;retry-sleep</code>=<i>sleep</i></p>
<dd> Sleep for <i>sleep</i> seconds between attempts to connect to spamd. The default is 1 second.</p>
<dt><code>&#8211;filter-retries</code>=<i>retries</i></p>
<dd> Retry filtering <i>retries</i> times if the spamd process fails (usually times out). This differs from <code>&#8211;connect-retries</code> in that it times out the transaction after the <font SIZE="-1">TCP</font> connection has been established successfully. The default is 1 time (ie. one attempt and no retries).</p>
<dt><code>&#8211;filter-retry-sleep</code>=<i>sleep</i></p>
<dd> Sleep for <i>sleep</i> seconds between failed spamd filtering attempts. The default is 1 second.</p>
<dt><code>-S</code>, <code>&#8211;ssl</code>, <code>&#8211;ssl</code>=<i>sslversion</i></p>
<dd> If spamc was built with support for <font SIZE="-1">SSL,</font> encrypt data to and from the spamd process with <font SIZE="-1">SSL</font>; spamd must support <font SIZE="-1">SSL</font> as well. <i>sslversion</i> specifies the <font SIZE="-1">SSL</font> protocol version to use, either <tt>&quot;sslv3&quot;</tt>, or <tt>&quot;tlsv1&quot;</tt>. The default, is <tt>&quot;sslv3&quot;</tt>.</p>
<dt><code>-t</code> <i>timeout</i>, <code>&#8211;timeout</code>=<i>timeout</i></p>
<dd> Set the timeout for spamc-to-spamd communications (default: 600, 0 disables). If spamd takes longer than this many seconds to reply to a message, spamc will abort the connection and treat this as a failure to connect; in other words the message will be returned unprocessed.</p>
<dt><code>-n</code> <i>timeout</i>, <code>&#8211;connect-timeout</code>=<i>timeout</i></p>
<dd> Set the timeout for spamc-to-spamd connection establishment (default: 600, 0 disables). If spamc takes longer than this many seconds to establish a connection to spamd, spamc will abort the connection and treat this as a failure to connect; in other words the message will be returned unprocessed.</p>
<dt><code>-u</code> <i>username</i>, <code>&#8211;username</code>=<i>username</i></p>
<dd> To have spamd use per-user-config files, run spamc as the user whose config files spamd should load; by default the effective user-ID is sent to spamd. If you&#8217;re running spamc as some other user, though, (eg. root, mail, nobody, cyrus, etc.) then you may use this flag to override the default.</p>
<dt><code>-U</code> <i>socketpath</i>, <code>&#8211;socket</code>=<i>path</i></p>
<dd> Connect to <tt>&quot;spamd&quot;</tt> via <font SIZE="-1">UNIX</font> domain socket <i>socketpath</i> instead of a <font SIZE="-1">TCP/IP</font> connection. </p>
<p> This option is not supported on Win32 platforms.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Report the version of this <tt>&quot;spamc&quot;</tt> client. If built with <font SIZE="-1">SSL</font> support, an additional line will be included noting this, like so: </p>
<pre>
  SpamAssassin Client version 3.0.0-rc4
    compiled with SSL support (OpenSSL 0.9.7d 17 Mar 2004)
</pre>
<dt><code>-x</code>, <code>&#8211;no-safe-fallback</code></p>
<dd> Disables the &#8216;safe fallback&#8217; error-recovery method, which passes through the unaltered message if an error occurs. Instead, exit with an error code, and let the <font SIZE="-1">MTA</font> queue up the mails for a retry later. See also &#8220;<font SIZE="-1">EXIT CODES&#8221;</font>. </p>
<p> This also disables the <font SIZE="-1">TCP</font> fail-over behaviour from <code>-d</code>.</p>
<dt><code>-X</code>, <code>&#8211;unavailable-tempfail</code></p>
<dd> When disabling &#8216;safe fallback&#8217; with <code>-x</code>, this option will turn <font SIZE="-1">EX_UNAVAILABLE</font> errors into <font SIZE="-1">EX_TEMPFAIL.</font> This may allow your <font SIZE="-1">MTA</font> to defer mails with a temporary <font SIZE="-1">SMTP</font> error instead of bouncing them with a permanent <font SIZE="-1">SMTP</font> error. See also &#8220;<font SIZE="-1">EXIT CODES&#8221;</font>.</p>
<dt><code>-y</code>, <code>&#8211;tests</code></p>
<dd> Just output the names of the tests hit to stdout, on one line, separated by commas.</p>
<dt><code>-K</code></p>
<dd> Perform a keep-alive check of spamd, instead of a full message check.</p>
<dt><code>-z</code></p>
<dd> Use gzip compression to compress the mail message sent to <tt>&quot;spamd&quot;</tt>. This is useful for long-distance use of spamc over the internet. Note that this relies on <tt>&quot;zlib&quot;</tt> being installed on the <tt>&quot;spamc&quot;</tt> client side, and the <tt>&quot;Compress::Zlib&quot;</tt> perl module on the server side; an error will be returned otherwise.</p>
<dt><code>&#8211;headers</code></p>
<dd> Perform a scan, but instead of allowing any part of the message (header and body) to be rewritten, limit rewriting to only the message headers. This is much more efficient in bandwidth usage, since the response message transmitted back from the spamd server will not include the body. </p>
<p> Note that this only makes sense if you are using <tt>&quot;report_safe 0&quot;</tt> in the scanning configuration on the remote end; with <tt>&quot;report_safe 1&quot;</tt>, it is likely to result in corrupt messages.</dl>
<h2>CONFIGURATION FILE</h2>
<p> The above command-line switches can also be loaded from a configuration file. </p>
<p> The format of the file is similar to the SpamAssassin rules files; blank lines and lines beginning with <tt>&quot;#&quot;</tt> are ignored. Any space-separated words are considered additions to the command line, and are prepended. Newlines are treated as equivalent to spaces. Existing command line switches will override any settings in the configuration file. </p>
<p> If the <code>-F</code> switch is specified, that file will be used. Otherwise, <tt>&quot;spamc&quot;</tt> will attempt to load spamc.conf in <tt>&quot;SYSCONFDIR&quot;</tt> (default: /etc/mail/spamassassin). If that file doesn&#8217;t exist, and the <code>-F</code> switch is not specified, no configuration file will be read. </p>
<p> Example: </p>
<pre>
    # spamc global configuration file 
    
    # connect to &quot;server.example.com&quot;, port 783
    -d server.example.com
    -p 783
    # max message size for scanning = 350k
    -s 350000
</pre>
<h2>EXIT CODES</h2>
<p> By default, spamc will use the &#8216;safe fallback&#8217; error recovery method. That means, it will always exit with an exit code of <tt>0</tt>, even if an error was encountered. If any error occurrs, it will simply pass through the unaltered message. </p>
<p> The <code>-c</code> and <code>-E</code> options modify this; instead, spamc will use an exit code of <tt>1</tt> if the message is determined to be spam. </p>
<p> If one of the <tt>&quot;-x&quot;</tt>, <tt>&quot;-L&quot;</tt> or <tt>&quot;-C&quot;</tt> options are specified, &#8216;safe fallback&#8217; will be disabled, and certain error conditions related to communication between spamc and spamd will result in an error code. </p>
<p> The exit codes used are as follows: </p>
<pre>
    EX_USAGE        64  command line usage error
    EX_DATAERR      65  data format error       
    EX_NOINPUT      66  cannot open input
    EX_NOUSER       67  addressee unknown
    EX_NOHOST       68  host name unknown
    EX_UNAVAILABLE  69  service unavailable
    EX_SOFTWARE     70  internal software error
    EX_OSERR        71  system error (e.g., can't fork)
    EX_OSFILE       72  critical OS file missing
    EX_CANTCREAT    73  can't create (user) output file
    EX_IOERR        74  input/output error
    EX_TEMPFAIL     75  temp failure; user is invited to retry
    EX_PROTOCOL     76  remote error in protocol
    EX_NOPERM       77  permission denied
    EX_CONFIG       78  configuration error
    * The EX_TOOBIG error level is never used.  If spamc receives a message 
      that is too big, the exit code will be 0.
    EX_TOOBIG       98  message was too big to process (see --max-size)
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-spamd/">spamd</a></i>(1) <i><a href="/docs/linux/man/1-spamassassin/">spamassassin</a></i>(1) <i><a href="/docs/linux/man/3-mail--spamassassin/">Mail::SpamAssassin</a></i>(3)</p>
<h2>PREREQUISITES</h2>
<p> <tt>&quot;Mail::SpamAssassin&quot;</tt></p>
<h2>AUTHORS</h2>
<p> The SpamAssassin(tm) Project &lt;<a rel="nofollow" href="http://spamassassin.apache.org/">http://spamassassin.apache.org/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> SpamAssassin is distributed under the Apache License, Version 2.0, as described in the file <tt>&quot;LICENSE&quot;</tt> included with the distribution. </p>
<h2>Index</h2>
