---
title: "callerid-conf(5)"
name: "callerid-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-callerid-conf/"
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
<dt><code>NUMBER=xxxx</code></dt>
<dd>Set the telephone number. This should be your msn or the telephone number with area code (with or without areprefix, countrycode and countryprefix) </dd>
<dt><code>SI=x</code></dt>
<dd>Service indicator. Isdnlog knows these service indicators: </dd>
<pre>1 speech (telephone, fax g3, modem etc.)
2 restricted digital information
3 unrestricted digital information with tones/announcements
4 video
7 unrestricted digital information (hdlc, x.75 etc.)</pre>
<dt><code>Alias=xxxx</code></dt>
<dd>Supply a name as alias (e.g. ALIAS=Fred&#8217;s Number) </dd>
<dt><code>ZONE=xxx</code></dt>
<dd>Only useful with remote numbers: billing zone for connections to this number: </dd>
<pre>0 internal connection in your s0 bus (no charge)
1 city area
2 region 50
3 region 200
4 far region
5 the same as 1</pre>
<dt><code>INTERFACE=xxx</code></dt>
<dd>Isdn network interface. This information is required with the &quot;-hx&quot; / hangup=&quot;value&quot; option. </dd>
<dt><code>START</code></dt>
<dd>You can define a subsection here. The whole section is ignored unless you gave the &quot;-S&quot; / start=yes option. Each subsection should have the name [FLAG]. It may hold these values: </dd>
<dl>
<dd>
</dd><dl>
<dt><code>FLAGS=x|y|z </code></dt>
<dd>Combine these flags (with or without the pipe &quot;|&quot; char; with is preferred) to get the combination you want: </dd>
<dl>
<dd>Part 1: Incoming and Outgoing</dd>
<dl>
<dt>I</dt>
<dd>Incoming call</dd>
<dt>O</dt>
<dd>Outgoing call</dd></dl>
</dl>
<dl>
<dd>Part 2: Signals from isdn system</dd>
<dl>
<dt>C</dt>
<dd>Connect (can be used with interval, see below)</dd>
<dt>B</dt>
<dd>Busy</dd>
<dt>E</dt>
<dd>Error</dd>
<dt>R</dt>
<dd>Ring (can be used with interval, see below)</dd>
<dt>A</dt>
<dd>AOCD (advice of charge signal)</dd>
<dt>H</dt>
<dd>Hangup</dd></dl>
</dl>
<dl>
<dd>Part 3: Modifiers</dd>
<dl>
<dt>L</dt>
<dd>Start the program again and again every time it terminates.</dd>
<dt>U</dt>
<dd>Start the program only once within a interval. Without this, several instances of a program can run in parallel. (Interval required.)</dd>
<dt>K</dt>
<dd>Kill program at the end of the interval.</dd></dl>
</dl>
<dt><code>USER=xxx</code></dt>
<dd>Isdnlog will not run programs as root, and will switch to a different user id for security. You must give the name or uid of the user isdnlog has to use here. </dd>
<dt><code>GROUP=xxx</code></dt>
<dd>Isdnlog will not run programs as group root, and will switch to a different group id for security. You must give the name or gid of the groups isdnlog has to use here. </dd>
<dt><code>TIME=xx</code></dt>
<dd>Restrict this flag to a special time. Pleas read isdntime(5). </dd>
<dt><code>INTERVAL=xx</code></dt>
<dd>With connect (C) or ring (R) flag you can specify an interval, so isdnlog will start the program after every interval. The interval is in seconds and should be at least 2 seconds. If the flags do not include C or R, this option is ignored. </dd>
<dt><code>PROGRAM=xxx</code></dt>
<dd>
</dd><dl>
<dd>The program you want to start, with the required arguments. You may use the following special tokens: </dd>
<dl>
<dt>\$1</dt>
<dd>flags that caused execution, e.g. &quot;IR&quot;, &quot;OC&quot;. There are always <code>exactly</code> two characters.</dd>
<dt>\$2</dt>
<dd>Caller number (complete with area code).</dd>
<dt>\$3</dt>
<dd>Called number (complete with area code).</dd>
<dt>\$4</dt>
<dd>Time the connection started. Example:<br/>
 &quot;Wed May 28 23:07:44 1997&quot;.<br/>
 Contains &quot;?&quot; if there is no connection yet (e.g. still at RING phase).</dd>
<dt>\$5</dt>
<dd>Duration of connection up to now (in seconds).</dd>
<dt>\$6</dt>
<dd>Time the connection ended. Same format as \$4.</dd>
<dt>\$7</dt>
<dd>Number of input bytes.</dd>
<dt>\$8</dt>
<dd>Number of output bytes.</dd>
<dt>\$9</dt>
<dd>Input bytes per second.</dd>
<dt>\$10</dt>
<dd>Output bytes per second.</dd>
<dt>\$11</dt>
<dd>Service indicator.</dd>
<dt>\$12</dt>
<dd>Charges.</dd>
<dt>\$13</dt>
<dd>Caller country code.</dd>
<dt>\$14</dt>
<dd>Called country code.</dd>
<dt>\$15</dt>
<dd>Caller area code.</dd>
<dt>\$16</dt>
<dd>Called area code.</dd>
<dt>\$17</dt>
<dd>Caller town (derived from area code).</dd>
<dt>\$18</dt>
<dd>Called town</dd>
<dt>\$19</dt>
<dd>Caller alias.</dd>
<dt>\$20</dt>
<dd>Called alias.</dd></dl>
</dl>
<dl>
<dd>Note: within a string you must use \${1} \${2} &#8230;</dd></dl>
</dl>
</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/callerid.conf</code></dt>
<dd>This file. </dd>
<dt><code>~/.isdn</code></dt>
<dd>Per user telephone book. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-isdnlog/">isdnlog</a>(8) <a href="/docs/linux/man/5-isdnformat/">isdnformat</a>(5) isdntime(5)</code></p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
