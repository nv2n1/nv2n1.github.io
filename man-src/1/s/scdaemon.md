---
title: "scdaemon(1)"
name: "scdaemon"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scdaemon/"
description: "scdaemon – Smartcard daemon for the GnuPG system"
---

<h2>NAME</h2>
<p> <code>scdaemon</code> &#8211; Smartcard daemon for the GnuPG system</p>
<h2>SYNOPSIS</h2>
<p> <code>scdaemon</code> [<code>&#8211;homedir</code> <i>dir</i>] [<code>&#8211;options</code> <i>file</i>] [<i>options</i>] <code>&#8211;server</code><br />
 <code>scdaemon</code> [<code>&#8211;homedir</code> <i>dir</i>] [<code>&#8211;options</code> <i>file</i>] [<i>options</i>] <code>&#8211;daemon</code> [<i>command_line</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>scdaemon</code> is a daemon to manage smartcards. It is usually invoked by <code>gpg-agent</code> and in general not used directly. </p>
<h2>COMMANDS</h2>
<p> Commands are not distinguished from options except for the fact that only one command is allowed. </p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the program version and licensing information. Not that you can abbreviate this command. </p>
<dt><code>&#8211;help, -h</code></p>
<dd> Print a usage message summarizing the most useful command-line options. Not that you can abbreviate this command. </p>
<dt><code>&#8211;dump-options</code></p>
<dd> Print a list of all available options and commands. Not that you can abbreviate this command. </p>
<dt><code>&#8211;server</code></p>
<dd> Run in server mode and wait for commands on the <code>stdin</code>. This is default mode is to create a socket and listen for commands there. </p>
<dt><code>&#8211;multi-server</code></p>
<dd> Run in server mode and wait for commands on the <code>stdin</code> as well as on an additional Unix Domain socket. The server command <code>GETINFO</code> may be used to get the name of that extra socket. </p>
<dt><code>&#8211;daemon</code></p>
<dd> Run the program in the background. This option is required to prevent it from being accidentally running in the background. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;options </code><i>file</i></p>
<dd> Reads configuration from <i>file</i> instead of from the default per-user configuration file. The default configuration file is named &#8216;<i>scdaemon.conf</i>&#8216; and expected in the &#8216;<i>.gnupg</i>&#8216; directory directly below the home directory of the user. </p>
<dt><code>&#8211;homedir </code><i>dir</i></p>
<dd> Set the name of the home directory to <i>dir</i>. If this option is not used, the home directory defaults to &#8216;<i>~/.gnupg</i>&#8216;. It is only recognized when given on the command line. It also overrides any home directory stated through the environment variable &#8216;<i>GNUPGHOME</i>&#8216; or (on W32 systems) by means of the Registry entry <i>HKCU\Software\GNU\GnuPG:HomeDir</i>. </p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Outputs additional information while running. You can increase the verbosity by giving several verbose commands to <code>gpgsm</code>, such as &#8216;-vv&#8217;. </p>
<dt><code>&#8211;debug-level </code><i>level</i></p>
<dd> Select the debug level for investigating problems. <i>level</i> may be a numeric value or a keyword: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> No debugging at all. A value of less than 1 may be used instead of the keyword.</p>
<dt><code>basic</code></p>
<dd> Some basic debug messages. A value between 1 and 2 may be used instead of the keyword.</p>
<dt><code>advanced</code></p>
<dd> More verbose debug messages. A value between 3 and 5 may be used instead of the keyword.</p>
<dt><code>expert</code></p>
<dd> Even more detailed messages. A value between 6 and 8 may be used instead of the keyword.</p>
<dt><code>guru</code></p>
<dd> All of the debug messages you can get. A value greater than 8 may be used instead of the keyword. The creation of hash tracing files is only enabled if the keyword is used.</dl>
</dl>
<p> How these messages are mapped to the actual debugging flags is not specified and may change with newer releases of this program. They are however carefully selected to best aid in debugging. </p>
<dl>
<dt>
<dd> <code>All debugging options are subject to change and thus should not be used by any application program. As the name says, they are only used as helpers to debug problems. </code></dl>
<dt><code>&#8211;debug </code><i>flags</i></p>
<dd> This option is only useful for debugging and the behaviour may change at any time without notice. FLAGS are bit encoded and may be given in usual C-Syntax. The currently defined bits are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0 (1)</code></p>
<dd> command I/O</p>
<dt><code>1 (2)</code></p>
<dd> values of big number integers</p>
<dt><code>2 (4)</code></p>
<dd> low level crypto operations</p>
<dt><code>5 (32)</code></p>
<dd> memory allocation</p>
<dt><code>6 (64)</code></p>
<dd> caching</p>
<dt><code>7 (128)</code></p>
<dd> show memory statistics.</p>
<dt><code>9 (512)</code></p>
<dd> write hashed data to files named <code>dbgmd-000*</code></p>
<dt><code>10 (1024)</code></p>
<dd> trace Assuan protocol. See also option <code>&#8211;debug-assuan-log-cats</code>.</p>
<dt><code>11 (2048)</code></p>
<dd> trace APDU I/O to the card. This may reveal sensitive data.</p>
<dt><code>12 (4096)</code></p>
<dd> trace some card reader related function calls.</dl>
</dl>
<dt><code>&#8211;debug-all</code></p>
<dd> Same as <code>&#8211;debug=0xffffffff</code> </p>
<dt><code>&#8211;debug-wait </code><i>n</i></p>
<dd> When running in server mode, wait <i>n</i> seconds before entering the actual processing loop and print the pid. This gives time to attach a debugger. </p>
<dt><code>&#8211;debug-ccid-driver</code></p>
<dd> Enable debug output from the included CCID driver for smartcards. Using this option twice will also enable some tracing of the T=1 protocol. Note that this option may reveal sensitive data. </p>
<dt><code>&#8211;debug-disable-ticker</code></p>
<dd> This option disables all ticker functions like checking for card insertions. </p>
<dt><code>&#8211;debug-allow-core-dump</code></p>
<dd> For security reasons we won&#8217;t create a core dump when the process aborts. For debugging purposes it is sometimes better to allow core dump. This options enables it and also changes the working directory to &#8216;<i>/tmp</i>&#8216; when running in <code>&#8211;server</code> mode. </p>
<dt><code>&#8211;debug-log-tid</code></p>
<dd> This option appends a thread ID to the PID in the log output. </p>
<dt><code>&#8211;debug-assuan-log-cats </code><i>cats</i></p>
<dd> Changes the active Libassuan logging categories to <i>cats</i>. The value for <i>cats</i> is an unsigned integer given in usual C-Syntax. A value of of 0 switches to a default category. If this option is not used the categories are taken from the environment variable &#8216;ASSUAN_DEBUG&#8217;. Note that this option has only an effect if the Assuan debug flag has also been with the option <code>&#8211;debug</code>. For a list of categories see the Libassuan manual. </p>
<dt><code>&#8211;no-detach</code></p>
<dd> Don&#8217;t detach the process from the console. This is mainly useful for debugging. </p>
<dt><code>&#8211;log-file </code><i>file</i></p>
<dd> Append all logging output to <i>file</i>. This is very helpful in seeing what the agent actually does. </p>
<dt><code>&#8211;pcsc-driver </code><i>library</i></p>
<dd> Use <i>library</i> to access the smartcard reader. The current default is &#8216;<i>libpcsclite.so</i>&#8216;. Instead of using this option you might also want to install a symbolic link to the default file name (e.g. from &#8216;<i>libpcsclite.so.1</i>&#8216;). </p>
<dt><code>&#8211;ctapi-driver </code><i>library</i></p>
<dd> Use <i>library</i> to access the smartcard reader. The current default is &#8216;<i>libtowitoko.so</i>&#8216;. Note that the use of this interface is deprecated; it may be removed in future releases. </p>
<dt><code>&#8211;disable-ccid</code></p>
<dd> Disable the integrated support for CCID compliant readers. This allows to fall back to one of the other drivers even if the internal CCID driver can handle the reader. Note, that CCID support is only available if libusb was available at build time. </p>
<dt><code>&#8211;reader-port </code><i>number_or_string</i></p>
<dd> This option may be used to specify the port of the card terminal. A value of 0 refers to the first serial device; add 32768 to access USB devices. The default is 32768 (first USB device). PC/SC or CCID readers might need a string here; run the program in verbose mode to get a list of available readers. The default is then the first reader found. </p>
<p> To get a list of available CCID readers you may use this command:</p>
<dl>
<dt>
<dd>
<pre>
echo scd getinfo reader_list | gpg-connect-agent --decode | awk '/^D/ {print $2}'
</pre>
</dl>
<dt><code>&#8211;card-timeout </code><i>n</i></p>
<dd> If <i>n</i> is not 0 and no client is actively using the card, the card will be powered down after <i>n</i> seconds. Powering down the card avoids a potential risk of damaging a card when used with certain cheap readers. This also allows non Scdaemon aware applications to access the card. The disadvantage of using a card timeout is that accessing the card takes longer and that the user needs to enter the PIN again after the next power up. </p>
<p> Note that with the current version of Scdaemon the card is powered down immediately at the next timer tick for any value of <i>n</i> other than 0. </p>
<dt><code>&#8211;enable-pinpad-varlen</code></p>
<dd> Please specify this option when the card reader supports variable length input for pinpad (default is no). For known readers (listed in ccid-driver.c and apdu.c), this option is not needed. Note that if your card reader doesn&#8217;t supports variable length input but you want to use it, you need to specify your pinpad request on your card. </p>
<dt><code>&#8211;disable-pinpad</code></p>
<dd> Even if a card reader features a pinpad, do not try to use it. </p>
<dt><code>&#8211;deny-admin</code></p>
<dd> This option disables the use of admin class commands for card applications where this is supported. Currently we support it for the OpenPGP card. This commands is useful to inhibit accidental access to admin class command which could ultimately lock the card through wrong PIN numbers. Note that GnuPG versions older than 2.0.11 featured an <code>&#8211;allow-admin</code> command which was required to use such admin commands. This option has no more effect today because the default is now to allow admin commands. </p>
<dt><code>&#8211;disable-application </code><i>name</i></p>
<dd> This option disables the use of the card application named <i>name</i>. This is mainly useful for debugging or if a application with lower priority should be used by default. </p>
<p> All the long options may also be given in the configuration file after stripping off the two leading dashes. </p>
</dl>
<h2>CARD APPLICATIONS</h2>
<p> <code>scdaemon</code> supports the card applications as described below. </p>
<h3>The OpenPGP card application &#8220;openpgp&#8221;</h3>
<p> &nbsp;<wbr> </p>
<p> This application is currently only used by <code>gpg</code> but may in future also be useful with <code>gpgsm</code>. Version 1 and version 2 of the card is supported. </p>
<p> The specifications for these cards are available at (<code><a rel="nofollow" href="http://g10code.com/docs/openpgp-card-1.0.pdf">http://g10code.com/docs/openpgp-card-1.0.pdf</a></code>) and (<code><a rel="nofollow" href="http://g10code.com/docs/openpgp-card-2.0.pdf">http://g10code.com/docs/openpgp-card-2.0.pdf</a></code>). </p>
<h3>The Telesec NetKey card &#8220;nks&#8221;</h3>
<p> &nbsp;<wbr> </p>
<p> This is the main application of the Telesec cards as available in Germany. It is a superset of the German DINSIG card. The card is used by <code>gpgsm</code>. </p>
<h3>The DINSIG card application &#8220;dinsig&#8221;</h3>
<p> &nbsp;<wbr> </p>
<p> This is an application as described in the German draft standard <i>DIN V 66291-1</i>. It is intended to be used by cards supporting the German signature law and its bylaws (SigG and SigV). </p>
<h3>The PKCS#15 card application &#8220;p15&#8221;</h3>
<p> &nbsp;<wbr> </p>
<p> This is common framework for smart card applications. It is used by <code>gpgsm</code>. </p>
<h3>The Geldkarte card application &#8220;geldkarte&#8221;</h3>
<p> &nbsp;<wbr> </p>
<p> This is a simple application to display information of a German Geldkarte. The Geldkarte is a small amount debit card application which comes with almost all German banking cards. </p>
<h3>The Undefined card application &#8220;undefined&#8221;</h3>
<p> &nbsp;<wbr> </p>
<p> This is a stub application to allow the use of the APDU command even if no supported application is found on the card. This application is not used automatically but must be explicitly requested using the SERIALNO command. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ scdaemon --server -v
</pre>
</dl>
<h2>FILES</h2>
<p> There are a few configuration files to control certain aspects of <code>scdaemons</code>&#8216;s operation. Unless noted, they are expected in the current home directory (see: [option &#8211;homedir]). </p>
<dl>
<dt><code>scdaemon.conf</code></p>
<dd> This is the standard configuration file read by <code>scdaemon</code> on startup. It may contain any valid long option; the leading two dashes may not be entered and the option may not be abbreviated. This default name may be changed on the command line (see: [option &#8211;options]). </p>
<dt><code>scd-event</code></p>
<dd> If this file is present and executable, it will be called on veyer card reader&#8217;s status changed. An example of this script is provided with the distribution </p>
<dt><code>reader_</code><i>n</i>.status</p>
<dd> This file is created by <code>sdaemon</code> to let other applications now about reader status changes. Its use is now deprecated in favor of &#8216;<i>scd-event</i>&#8216;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-gpg2/">gpg2</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
<dd>
<pre>
info gnupg
</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
