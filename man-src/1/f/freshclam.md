---
title: "freshclam(1)"
name: "freshclam"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freshclam/"
description: "freshclam – update virus databases"
---

<h2>NAME</h2>
<p> freshclam &#8211; update virus databases</p>
<h2>SYNOPSIS</h2>
<p> freshclam [options]</p>
<h2>DESCRIPTION</h2>
<p> freshclam is a virus database update tool for ClamAV.</p>
<h2>OPTIONS</h2>
<p> Freshclam reads its configuration from freshclam.conf. The settings can be overwritten with command line options.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Output help information and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version number and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be verbose. This option causes freshclam to print much additional information.</p>
<dt><code>&#8211;debug</code></p>
<dd> Enable debug messages from LibClamAV.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Be quiet &#8211; output only error messages.</p>
<dt><code>&#8211;no-warnings</code></p>
<dd> Don&#8217;t print and log warnings.</p>
<dt><code>&#8211;stdout</code></p>
<dd> Write all messages to stdout.</p>
<dt><code>&#8211;config-file=FILE</p>
<dd> Read configuration from FILE.</p>
<dt>-l FILE, &#8211;log=FILE</code></p>
<dd> Log report to FILE.</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> Run in a daemon mode. Defaults to 12 checks per day unless otherwise specified by &#8211;checks or freshclam.conf.</p>
<dt><code>-p FILE, &#8211;pid=FILE</code></p>
<dd> Write daemon&#8217;s pid to FILE.</p>
<dt><code>-u USER, &#8211;user USER</code></p>
<dd> Run as USER. By default (when started by root) freshclam drops privileges and operates as the &#8221; user.</p>
<dt><code>&#8211;no-dns</code></p>
<dd> This option forces old non-DNS verification method (without a TTL delay).</p>
<dt><code>-c #n, &#8211;checks=#n</code></p>
<dd> Check #n times per day for a new database. #n must be between 1 and 50.</p>
<dt><code>&#8211;datadir=DIRECTORY</code></p>
<dd> Install new database in DIRECTORY. The directory must be writable for the &#8221; user or unprivileged user running freshclam.</p>
<dt><code>&#8211;daemon-notify=/path/to/clamd.conf</code></p>
<dd> Notify the daemon about the new database. By default it reads a hardcoded config file but you can use a different one. Both local and TCP sockets are supported.</p>
<dt><code>-a IP, &#8211;local-address=IP</code></p>
<dd> Use (local) IP for HTTP downloads. Useful for multi-homed systems. If binding fails for whatever reason, a warning is issued and freshclam behaves like without this flag.</p>
<dt><code>&#8211;on-update-execute=COMMAND</code></p>
<dd> Execute COMMAND after successful update.</p>
<dt><code>&#8211;on-error-execute=COMMAND</code></p>
<dd> Execute COMMAND if error occurred. Remember, that virus database freshness is the most important thing in anti-virus system. With this option freshclam can alert you (eg. send SMS) when something is going wrong.</p>
<dt><code>&#8211;on-outdated-execute=COMMAND</code></p>
<dd> Execute COMMAND when freshclam reports outdated version. In the command string %v will be replaced by the new version number.</p>
<dt><code>&#8211;list-mirrors</code></p>
<dd> Print mirror details from mirrors.dat (cache file for the mirror manager).</p>
<dt><code>&#8211;submit-stats[=/path/to/clamd.conf]</code></p>
<dd> Upload detection statistics to the ClamAV Project (see <a href="/docs/linux/man/5-freshclam-conf/">freshclam.conf</a>(5):SubmitDetectionStats for more details). No database update will be performed. This option only works in the interactive mode.</p>
<dt><code>&#8211;update-db=DBNAME</code></p>
<dd> With this option you can limit updates to a subset of database files. The DBNAME should be &quot;main&quot;, &quot;daily&quot;, &quot;bytecode&quot;, &quot;safebrowsing&quot; or one of the 3rd party database names. This option can be used multiple times and only works with the official and 3rd party databases distrubuted through the ClamAV mirrors, your custom databases (specified with DatabaseCustomURL in freshclam.conf) will not be ignored.</p>
<dt><code>&#8211;enable-stats</code></p>
<dd> Enable submission of statistical data.</p>
<dt><code>&#8211;stats-host-id=UUID</code></p>
<dd> HostID in the form of an UUID to use when submitting statistical information.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>(0) Download database to default directory:</p>
<dd>
<p> <code>freshclam</code></p>
<dt>(1) Download database to current directory:</p>
<dd>
<p> <code>freshclam &#8211;datadir=.</code></p>
<dt>(2) Run as a daemon and check 2 times per day for new database:</p>
<dd>
<p> <code>freshclam -d -c 2</code></dl>
<h2>RETURN CODES</h2>
<p> Some return codes of freshclam can be overwritten with a built-in command EXIT_n which can be passed to &#8211;on-*-execute, eg. &#8211;on-update-execute=EXIT_1 will force freshclam to always return 1 after successful database update.</p>
<dl>
<dt>0 : Database is up-to-date or successfully updated.</p>
<dd>
<dt>40: Unknown option passed.</p>
<dd>
<dt>50: Can&#8217;t change directory.</p>
<dd>
<dt>51: Can&#8217;t check MD5 sum.</p>
<dd>
<dt>52: Connection (network) problem.</p>
<dd>
<dt>53: Can&#8217;t unlink file.</p>
<dd>
<dt>54: MD5 or digital signature verification error.</p>
<dd>
<dt>55: Error reading file.</p>
<dd>
<dt>56: Config file error.</p>
<dd>
<dt>57: Can&#8217;t create new file.</p>
<dd>
<dt>58: Can&#8217;t read database from remote server.</p>
<dd>
<dt>59: Mirrors are not fully synchronized (try again later).</p>
<dd>
<dt>60: Can&#8217;t get information about &#8221; user from /etc/passwd.</p>
<dd>
<dt>61: Can&#8217;t drop privileges.</p>
<dd>
<dt>62: Can&#8217;t initialize logger.</p>
<dd></dl>
<h2>FILES</h2>
<p> /etc/freshclam.conf</p>
<h2>CREDITS</h2>
<p> Please check the full documentation for credits.</p>
<h2>AUTHOR</h2>
<p> Tomasz Kojm &lt;tkojm [at] clamav.net&gt;, Kevin Lin &lt;klin [at] sourcefire.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-freshclam-conf/">freshclam.conf</a>(5), <a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5), <a href="/docs/linux/man/1-clamscan/">clamscan</a>(1) </p>
<h2>Index</h2>
