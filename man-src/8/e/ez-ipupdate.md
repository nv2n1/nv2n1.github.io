---
title: "ez-ipupdate(8)"
name: "ez-ipupdate"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ez-ipupdate/"
description: "ez-ipupdate – dynamic DNS client"
---

<p>ez-ipupdate &#8211; dynamic DNS client</p>
<h2>Synopsis</h2>
<p><code>ez-ipupdate</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>ez-ipupdate</code> dynamic DNS client. </p>
<h2>Options</h2>
<p><code>ez-ipupdate</code> follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;).</p>
<dl>
<dt><code>-a</code>, <code>&#8211;address</code> &lt;ip address&gt;</p>
<dd>string to send as your ip address</p>
<dt><code>-b</code>, <code>&#8211;cache-file</code> &lt;file&gt;</p>
<dd>file to use for caching the ipaddress</p>
<dt><code>-c</code>, <code>&#8211;config-file</code> &lt;file&gt;</p>
<dd>configuration file, almost all arguments can be given with: &lt;name&gt;[=&lt;value&gt;] to see a list of possible config commands try &quot;echo help | ez-ipupdate <code>-c</code> -&quot;</p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd>run as a daemon periodicly updating if necessary</p>
<dt><code>-e</code>, <code>&#8211;execute</code> &lt;command&gt;</p>
<dd>shell command to execute after a successful update</p>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd>when running as a daemon run in the foreground</p>
<dt><code>-F</code>, <code>&#8211;pid-file</code> &lt;file&gt;</p>
<dd>use &lt;file&gt; as a pid file</p>
<dt><code>-g</code>, <code>&#8211;request-uri</code> &lt;uri&gt;</p>
<dd>URI to send updates to</p>
<dt><code>-h</code>, <code>&#8211;host</code> &lt;host&gt;</p>
<dd>string to send as host parameter</p>
<dt><code>-i</code>, <code>&#8211;interface</code> &lt;iface&gt;</p>
<dd>which interface to use</p>
<dt><code>-L</code>, <code>&#8211;cloak_title</code> &lt;host&gt;</p>
<dd>some stupid thing for DHS only</p>
<dt><code>-m</code>, <code>&#8211;mx</code> &lt;mail exchange&gt;</p>
<dd>string to send as your mail exchange</p>
<dt> <code>-M</code>, <code>&#8211;max-interval</code> &lt;# of sec&gt; max time in between updates</p>
<dt><code>-N</code>, <code>&#8211;notify-email</code> &lt;email&gt;</p>
<dd>
<dd>address to send mail to if bad things happen</p>
<dt><code>-o</code>, <code>&#8211;offline</code></p>
<dd>set to off line mode</p>
<dt><code>-p</code>, <code>&#8211;resolv-period</code> &lt;sec&gt;</p>
<dd>period to check IP if it can&#8217;t be resolved</p>
<dt><code>-P</code>, <code>&#8211;period</code> &lt;# of sec&gt;</p>
<dd>period to check IP in daemon mode (default: 1800 seconds)</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>be quiet</p>
<dt><code>-r</code>, <code>&#8211;retrys</code> &lt;num&gt;</p>
<dd>number of trys (default: 1)</p>
<dt><code>-R</code>, <code>&#8211;run-as-user</code> &lt;user&gt;</p>
<dd>change to &lt;user&gt; for running, be ware that this can cause problems with handeling SIGHUP properly if that user can&#8217;t read the config file. also it can&#8217;t write it&#8217;s pid file to a root directory</p>
<dt><code>-Q</code>, <code>&#8211;run-as-euser</code> &lt;user&gt;</p>
<dd>change to effective &lt;user&gt; for running, this is NOT secure but it does solve the problems with run-as-user and config files and pid files.</p>
<dt><code>-s</code>, <code>&#8211;server</code> &lt;server[:port]&gt;</p>
<dd>the server to connect to</p>
<dt><code>-S</code>, <code>&#8211;service-type</code> &lt;server&gt;</p>
<dd>the type of service that you are using try one of: null ezip pgpow dhs dyndns dyndns-static dyndns-custom ods tzo easydns easydns-partner gnudip justlinux dyns hn zoneedit heipv6tb</p>
<dt><code>-t</code>, <code>&#8211;timeout</code> &lt;sec.millisec&gt;</p>
<dd>the amount of time to wait on I/O</p>
<dt><code>-T</code>, <code>&#8211;connection-type</code> &lt;num&gt;</p>
<dd>number sent to TZO as your connection type (default: 1)</p>
<dt><code>-U</code>, <code>&#8211;url</code> &lt;url&gt;</p>
<dd>string to send as the url parameter</p>
<dt><code>-u</code>, <code>&#8211;user</code> &lt;user[:passwd]&gt;</p>
<dd>user ID and password, if either is left blank they will be prompted for</p>
<dt><code>-w</code>, <code>&#8211;wildcard</code></p>
<dd>set your domain to have a wildcard alias</p>
<dt><code>-z</code>, <code>&#8211;partner</code> &lt;partner&gt;</p>
<dd>specify easyDNS partner (for easydns-partner services)</p>
<dt><code>&#8211;help</code></p>
<dd>display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd>output version information and exit</p>
<dt><code>&#8211;credits</code></p>
<dd>print the credits and exit</p>
<dt><code>&#8211;signalhelp</code></p>
<dd>print help about signals
</dl>
<h2>Author</h2>
<p>This manual page was written by Sam Hocevar &lt;sam [at] zoy.org&gt; for the Debian GNU/Linux system (but may be used by others).</p>
