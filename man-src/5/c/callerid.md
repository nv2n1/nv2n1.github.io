---
title: "callerid(5)"
name: "callerid"
section: "5"
letter: "c"
url: "/docs/linux/man/5-callerid/"
description: "/etc/isdn/callerid.conf – config file for isdnlog numbers and scripts"
---

<p>/etc/isdn/callerid.conf &#8211; config file for isdnlog numbers and scripts</p>
<h2>Format</h2>
<p>This file has the format described in <a href="/docs/linux/man/5-isdnformat/">isdnformat</a>(5). It must be owned by root, and only root may have write access. Every user can create his private telephone book as ~/.isdn with the same file format.</p>
<h2>Variables Section</h2>
<p>Like in isdn.conf, this file has an optional [VARIABLES] section. All variable names must be uppercase. Warning: variables in callerid.conf will override variables in isdn.conf, and variables in ~/.isdn will override variables in both files. First all variables are read, then they are substituted, so a variable defined in ~/.isdn can be used in isdn.conf. This might be a security hole. However, if programs are to be run as root, these files (and the program) cannot be writeable for non-root users. </p>
<p> Using variables: if a reference to a non existing variable is used, isdnrep and isdnlog will give warning messages, and use the variable name (e.g if $FRED isn&#8217;t set, isdnlog will use &quot;$FRED&quot;). The dollar sign can be backslashed if a real dollar sign is needed instead of variable substitution (e.g. \$PATH will be &quot;$PATH&quot;).</p>
<h2>NUMBER and MSN</h2>
<p>In [NUMBER] sections, you can supply information for the outer world, in [MSN] sections; you can supply information about your msns. The format is the same: </p>
<dl>
<dt><code>NUMBER=xxxx</code></p>
<dd>Set the telephone number. This should be your msn or the telephone number with area code (with or without areprefix, countrycode and countryprefix) </p>
<dt><code>SI=x</code></p>
<dd>Service indicator. Isdnlog knows these service indicators: </p>
<pre>1 speech (telephone, fax g3, modem etc.)
2 restricted digital information
3 unrestricted digital information with tones/announcements
4 video
7 unrestricted digital information (hdlc, x.75 etc.)</pre>
<dt><code>Alias=xxxx</code></p>
<dd>Supply a name as alias (e.g. ALIAS=Fred&#8217;s Number) </p>
<dt><code>ZONE=xxx</code></p>
<dd>Only useful with remote numbers: billing zone for connections to this number: </p>
<pre>0 internal connection in your s0 bus (no charge)
1 city area
2 region 50
3 region 200
4 far region
5 the same as 1</pre>
<dt><code>INTERFACE=xxx</code></p>
<dd>Isdn network interface. This information is required with the &quot;-hx&quot; / hangup=&quot;value&quot; option. </p>
<dt><code>START</code></p>
<dd>You can define a subsection here. The whole section is ignored unless you gave the &quot;-S&quot; / start=yes option. Each subsection should have the name [FLAG]. It may hold these values: </p>
<dl>
<dd>
<dl>
<dt><code>FLAGS=x|y|z </code></p>
<dd>Combine these flags (with or without the pipe &quot;|&quot; char; with is preferred) to get the combination you want: </p>
<dl>
<dd>Part 1: Incoming and Outgoing</p>
<dl>
<dt>I</p>
<dd>Incoming call</p>
<dt>O</p>
<dd>Outgoing call</dl>
</dl>
<dl>
<dd>Part 2: Signals from isdn system</p>
<dl>
<dt>C</p>
<dd>Connect (can be used with interval, see below)</p>
<dt>B</p>
<dd>Busy</p>
<dt>E</p>
<dd>Error</p>
<dt>R</p>
<dd>Ring (can be used with interval, see below)</p>
<dt>A</p>
<dd>AOCD (advice of charge signal)</p>
<dt>H</p>
<dd>Hangup</dl>
</dl>
<dl>
<dd>Part 3: Modifiers</p>
<dl>
<dt>L</p>
<dd>Start the program again and again every time it terminates.</p>
<dt>U</p>
<dd>Start the program only once within a interval. Without this, several instances of a program can run in parallel. (Interval required.)</p>
<dt>K</p>
<dd>Kill program at the end of the interval.</dl>
</dl>
<dt><code>USER=xxx</code></p>
<dd>Isdnlog will not run programs as root, and will switch to a different user id for security. You must give the name or uid of the user isdnlog has to use here. </p>
<dt><code>GROUP=xxx</code></p>
<dd>Isdnlog will not run programs as group root, and will switch to a different group id for security. You must give the name or gid of the groups isdnlog has to use here. </p>
<dt><code>TIME=xx</code></p>
<dd>Restrict this flag to a special time. Pleas read <a href="/docs/linux/man/5-isdntime/">isdntime</a>(5). </p>
<dt><code>INTERVAL=xx</code></p>
<dd>With connect (C) or ring (R) flag you can specify an interval, so isdnlog will start the program after every interval. The interval is in seconds and should be at least 2 seconds. If the flags do not include C or R, this option is ignored. </p>
<dt><code>PROGRAM=xxx</code></p>
<dd>
<dl>
<dd>The program you want to start, with the required arguments. You may use the following special tokens: </p>
<dl>
<dt>\$1</p>
<dd>flags that caused execution, e.g. &quot;IR&quot;, &quot;OC&quot;. There are always <code>exactly</code> two characters.</p>
<dt>\$2</p>
<dd>Caller number (complete with area code).</p>
<dt>\$3</p>
<dd>Called number (complete with area code).</p>
<dt>\$4</p>
<dd>Time the connection started. Example:<br />
 &quot;Wed May 28 23:07:44 1997&quot;.<br />
 Contains &quot;?&quot; if there is no connection yet (e.g. still at RING phase).</p>
<dt>\$5</p>
<dd>Duration of connection up to now (in seconds).</p>
<dt>\$6</p>
<dd>Time the connection ended. Same format as \$4.</p>
<dt>\$7</p>
<dd>Number of input bytes.</p>
<dt>\$8</p>
<dd>Number of output bytes.</p>
<dt>\$9</p>
<dd>Input bytes per second.</p>
<dt>\$10</p>
<dd>Output bytes per second.</p>
<dt>\$11</p>
<dd>Service indicator.</p>
<dt>\$12</p>
<dd>Charges.</p>
<dt>\$13</p>
<dd>Caller country code.</p>
<dt>\$14</p>
<dd>Called country code.</p>
<dt>\$15</p>
<dd>Caller area code.</p>
<dt>\$16</p>
<dd>Called area code.</p>
<dt>\$17</p>
<dd>Caller town (derived from area code).</p>
<dt>\$18</p>
<dd>Called town</p>
<dt>\$19</p>
<dd>Caller alias.</p>
<dt>\$20</p>
<dd>Called alias.</dl>
</dl>
<dl>
<dd>Note: within a string you must use \${1} \${2} &#8230;</dl>
</dl>
</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/callerid.conf</code></p>
<dd>This file. </p>
<dt><code>~/.isdn</code></p>
<dd>Per user telephone book. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8) <a href="/docs/linux/man/5-isdnformat/">isdnformat</a>(5) <a href="/docs/linux/man/5-isdntime/">isdntime</a>(5)</code></p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
