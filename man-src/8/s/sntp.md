---
title: "sntp(8)"
name: "sntp"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sntp/"
description: "sntp – standard Simple Network Time Protocol program"
---

<p>sntp &#8211; standard Simple Network Time Protocol program</p>
<h2>Synopsis</h2>
<p><code>sntp</code> [<code>&#8211;</code><i>flag</i> [<i>value</i>]]&#8230; [<code>&#8212;</code><i>opt-name</i> [[=| ]<i>value</i>]]&#8230;<br />
 [ hostname-or-IP &#8230;] </p>
<h2>Description</h2>
<p>This manual page briefly documents the <code>sntp</code> command. <i>sntp</i> can be used as a SNTP client to query a NTP or SNTP server and either display the time or set the local system&#8217;s time (given suitable privilege). It can be run as an interactive command or in a <i>cron</i> job. </p>
<p> NTP (the Network Time Protocol) and SNTP (the Simple Network Time Protocol) are defined and described by RFC 5905. </p>
<p> The default is to write the estimated correct local date and time (i.e. not UTC) to the standard output in a format like <code>&#8216;1996-10-15 20:17:25.123 (+0800) +4.567 +/- 0.089 secs&#8217;</code>, where the <code>&#8216;(+0800)&#8217;</code> means that to get to UTC from the reported local time one must add 8 hours and 0 minutes, and the <code>&#8216;+4.567 +/- 0.089 secs&#8217;</code> indicates the local clock is 4.567 seconds behind the correct time (so 4.567 seconds must be added to the local clock to get it to be correct), and the time of is believed to be correct to within +/- 0.089 seconds.</p>
<h2>Options</h2>
<dl>
<dt><code>-4</code>, <code>&#8211;ipv4</code></p>
<dd>Force IPv4 DNS name resolution. This option must not appear in combination with any of the following options: ipv6. </p>
<p> Force DNS resolution of the following host names on the command line to the IPv4 namespace.</p>
<dt><code>-6</code>, <code>&#8211;ipv6</code></p>
<dd>Force IPv6 DNS name resolution. This option must not appear in combination with any of the following options: ipv4. </p>
<p> Force DNS resolution of the following host names on the command line to the IPv6 namespace.</p>
<dt><code>-d</code>, <code>&#8211;normalverbose</code></p>
<dd>Normal verbose. </p>
<p> Diagnostic messages for non-fatal errors and a limited amount of tracing should be written to standard error. Fatal ones always produce a diagnostic. This option should be set when there is a suspected problem with the server, network or the source.</p>
<dt><code>-K</code> <i>file-name</i>, <code>&#8211;kod</code>=<i>file-name</i></p>
<dd>KoD history filename. </p>
<p> Specifies the filename to be used to persist the history of KoD responses received from servers. The default is /var/lib/sntp/kod.</p>
<dt><code>-p</code>, <code>&#8211;syslog</code></p>
<dd>Logging with syslog. This option must not appear in combination with any of the following options: logfile. </p>
<p> When this option is set all logging will be done using syslog.</p>
<dt><code>-l</code> <i>file-name</i>, <code>&#8211;logfile</code>=<i>file-name</i></p>
<dd>Log to specified logfile. This option must not appear in combination with any of the following options: syslog. </p>
<p> This option causes the client to write log messages to the specified logfile.</p>
<dt><code>-s</code>, <code>&#8211;settod</code></p>
<dd>Set (step) the time with settimeofday(). This option must not appear in combination with any of the following options: adjtime. </p>
<dt><code>-j</code>, <code>&#8211;adjtime</code></p>
<dd>Set (slew) the time with adjtime(). This option must not appear in combination with any of the following options: settod. </p>
<dt><code>-b</code> <i>broadcast-address</i>, <code>&#8211;broadcast</code>=<i>broadcast-address</i></p>
<dd>Use broadcasts to the address specified for synchronisation. </p>
<p> If specified SNTP will listen to the specified broadcast address for NTP broadcasts. The default maximum wait time, 68 seconds, can be modified with -t.</p>
<dt><code>-t</code> <i>seconds</i>, <code>&#8211;timeout</code>=<i>seconds</i></p>
<dd>Specify the number of seconds to wait for broadcasts. This option takes an integer number as its argument. The default <i>seconds</i> for this option is:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>68 </p>
<p> When waiting for a broadcast packet SNTP will wait the number of seconds specified before giving up. Default 68 seconds.</p>
<dt><code>-a</code> <i>auth-keynumber</i>, <code>&#8211;authentication</code>=<i>auth-keynumber</i></p>
<dd>Enable authentication with the key auth-keynumber. This option takes an integer number as its argument. </p>
<p> This option enables authentication using the key specified in this option&#8217;s argument. The argument of this option is the keyid, a number specified in the keyfile as this key&#8217;s identifier. See the keyfile option (-k) for more details.</p>
<dt><code>-k</code> <i>file-name</i>, <code>&#8211;keyfile</code>=<i>file-name</i></p>
<dd>Specify a keyfile. SNTP will look in this file for the key specified with -a. </p>
<p> This option specifies the keyfile. SNTP will search for the key specified with -a keyno in this file. Key files follow the following format: </p>
<p> keyid keytype key </p>
<p> Where<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>keyid is a number identifying this key<br />
 keytype is one of the follow: S Key in 64 Bit hexadecimal number as specified in in the DES specification. N Key in 64 Bit hexadecimal number as specified in the NTP standard. A Key in a 1-to-8 character ASCII string. M Key in a 1-to-8 character ASCII string using the MD5 authentication scheme. </p>
<p> For more information see <a href="/docs/linux/man/5-ntp-keys/">ntp.keys</a>(5).</p>
<dt><code>-?</code>,<code> &#8211;help</code></p>
<dd>Display extended usage information and exit.</p>
<dt><code>-!</code>,<code> &#8211;more-help</code></p>
<dd>Extended usage information passed thru pager.</p>
<dt><code>-&gt;</code> [<i>rcfile</i>],<code> &#8211;save-opts</code>[=<i>rcfile</i>]</p>
<dd>Save the option state to <i>rcfile</i>. The default is the <i>last</i> configuration file listed in the <code>OPTION PRESETS</code> section, below.</p>
<dt><code>-&lt;</code> <i>rcfile</i>,<code> &#8211;load-opts</code>=<i>rcfile</i>,<code> &#8211;no-load-opts</code></p>
<dd>Load options from <i>rcfile</i>. The <i>no-load-opts</i> form will disable the loading of earlier RC/INI files. <i>&#8211;no-load-opts</i> is handled early, out of order.</p>
<dt><code>&#8211;</code> [{<i>v|c|n</i>}],<code> &#8211;version</code>[=<i>{v|c|n}</i>]</p>
<dd>Output version of program and exit. The default mode is `v&#8217;, a simple version. The `c&#8217; mode will print copyright information and `n&#8217; will print the full copyright notice.</dl>
<h2>Option Presets</h2>
<p>Any option that is not marked as <i>not presettable</i> may be preset by loading values from configuration (&quot;RC&quot; or &quot;.INI&quot;) file(s) and values from environment variables named: </p>
<pre> <code>SNTP_&lt;option-name&gt;</code> or <code>SNTP</code></pre>
<p>The environmental presets take precedence (are processed later than) the configuration files. The <i>homerc</i> files are &quot;<i>$HOME</i>&quot;, and &quot;<i>.</i>&quot;. If any of these are directories, then the file <i>.ntprc</i> is searched for within those directories.</p>
<h2>Usage</h2>
<p>The simplest use of this program is as an unprivileged command to check the current time and error in the local clock. For example:</p>
<dl>
<dd><code>sntp ntpserver.somewhere</code></dl>
<p> With suitable privilege, it can be run as a command or in a <i>cron</i> job to reset the local clock from a reliable server, like the <i>ntpdate</i> and <i>rdate</i> commands. For example:</p>
<dl>
<dd><code>sntp -a ntpserver.somewhere</code></dl>
<h2>Return Value</h2>
<p>The program returns a zero exit status for success, and a non-zero one otherwise.</p>
<h2>Bugs</h2>
<p>Please report bugs to <a rel="nofollow" href="http://bugs.ntp.org">http://bugs.ntp.org</a> .</p>
<h2>Author</h2>
<p>David L. Mills and/or others<br />
 Please send bug reports to: <a rel="nofollow" href="http://bugs.ntp.org,">http://bugs.ntp.org,</a> bugs [at] ntp.org </p>
<pre>see html/copyright.html</pre>
<p>This manual page was <i>AutoGen</i>-erated from the <code>sntp</code> option definitions.</p>
