---
title: "php-fpm(8)"
name: "php-fpm"
section: "8"
letter: "p"
url: "/docs/linux/man/8-php-fpm/"
---

<dl>
<dt>php-fpm &#8211; PHP FastCGI Process Manager &#8216;PHP-FPM&#8217;</p>
<dd></dl>
<h2>Synopsis</h2>
<p><code>php-fpm</code> [options] </p>
<h2>Description</h2>
<p><code>PHP</code> is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This is a variant of PHP that will run in the background as a daemon, listening for CGI requests. Output is logged to /var/log/php-fpm.log. </p>
<p> Most options are set in the configuration file. The configuration file is /etc/php-fpm.conf. By default, php-fpm will respond to CGI requests listening on localhost http port 9000. Therefore php-fpm expects your webserver to forward all requests for &#8216;.php&#8217; files to port 9000 and you should edit your webserver configuration file appropriately.</p>
<h2>Options</h2>
<dl>
<dt><code>-C</code></p>
<dd>Do not chdir to the script&#8217;s directory</p>
<dd><code>&#8211;php-ini </code><i>path</i>|<i>file</i></p>
<dd><code>-c </code><i>path</i>|<i>file</i> Look for <code>php.ini </code> file in the directory <i>path</i> or use the specified <i>file</i></p>
<dd><code>&#8211;no-php-ini</code></p>
<dd><code>-n</code> No <code>php.ini </code> file will be used</p>
<dd><code>&#8211;define </code><i>foo</i>[=<i>bar</i>]</p>
<dd><code>-d </code><i>foo</i>[=<i>bar</i>] Define INI entry <i>foo</i> with value <i>bar</i></p>
<dt><code>-e</code></p>
<dd>Generate extended information for debugger/profiler</p>
<dd><code>&#8211;help</code></p>
<dd><code>-h</code> This help</p>
<dd><code>&#8211;info</code></p>
<dd><code>-i</code> PHP information and configuration</p>
<dd><code>&#8211;modules</code></p>
<dd><code>-m</code> Show compiled in modules</p>
<dd><code>&#8211;version</code></p>
<dd><code>-v</code> Version number <code>&#8211;prefix </code><i>path</i></p>
<dd><code>-p</code> Specify alternative prefix path (the default is /usr)</p>
<dd><code>&#8211;fpm-config </code><i>file</i></p>
<dd><code>-y</code> Specify alternative path to FastCGI process manager configuration file (the default is /etc/php-fpm.conf)</p>
<dd><code>&#8211;test</code></p>
<dd><code>-t</code> Test FPM configuration file and exit If called twice (-tt), the configuration is dumped before exiting.</p>
<dd><code>&#8211;daemonize</code></p>
<dd><code>-D</code> Force to run in background and ignore daemonize option from configuration file.</p>
<dd><code>&#8211;nodaemonize</code></p>
<dd><code>-F</code> Force to stay in foreground and ignore daemonize option from configuration file.</p>
<dd><code>&#8211;zend-extension </code><i>file</i></p>
<dd><code>-z </code><i>file</i> Load Zend extension <i>file</i></dl>
<h2>Files</h2>
<dl>
<dt><code>php-fpm.conf</code></p>
<dd>The configuration file for the php-fpm daemon.</p>
<dt><code>php.ini</code></p>
<dd>The standard php configuration file.</dl>
<h2>Examples</h2>
<p>For any unix systems which use init.d for their main process manager, you should use the init script provided to start and stop the php-fpm daemon.</p>
<dl>
<dd>sudo /etc/init.d/php-fpm start</dl>
<dl>
<dt>For any unix systems which use systemd for their main process manager, you should use the unit file provided to start and stop the php-fpm daemon.</p>
<dd></dl>
<dl>
<dd>sudo systemctl start php-fpm.service</dl>
<dl>
<dt>If your installation has no appropriate init script, launch php-fpm with no arguments. It will launch as a daemon (background process) by default. The file /var/run/php-fpm.pid determines whether php-fpm is already up and running. Once started, php-fpm then responds to several POSIX signals:</p>
<dd></dl>
<dl>
<dd><code>SIGINT,SIGTERM <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code>immediate termination</p>
<dl>
<dt><code>SIGQUIT <tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code>graceful stop</p>
<dd>
<dt><code>SIGUSR1 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code>re-open log file</p>
<dd>
<dt><code>SIGUSR2 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code>graceful reload of all workers + reload of fpm conf/binary</p>
<dd></dl>
</dl>
<h2>Tips</h2>
<p>The PHP-FPM CGI daemon will work well with most popular webservers, including Apache2, lighttpd and nginx.</p>
<h2>See Also</h2>
<p>The PHP-FPM website: </p>
<p> <code><a rel="nofollow" href="http://php-fpm.org">http://php-fpm.org</a></code> </p>
<p> For a more or less complete description of PHP look here: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/manual/">http://www.php.net/manual/</a></code> </p>
<p> A nice introduction to PHP by Stig Bakken can be found here: </p>
<p> <code><a rel="nofollow" href="http://www.zend.com/zend/art/intro.php">http://www.zend.com/zend/art/intro.php</a></code></p>
<h2>Bugs</h2>
<p>You can view the list of known bugs or report any new bug you found at: </p>
<p> <code><a rel="nofollow" href="http://bugs.php.net">http://bugs.php.net</a></code></p>
<h2>Authors</h2>
<p>PHP-FPM SAPI was written by Andrei Nigmatulin. The mailing-lists are highload-php-en (English) and highload-php-ru (Russian). </p>
<p> The PHP Group: Thies C. Arntzen, Stig Bakken, Andi Gutmans, Rasmus Lerdorf, Sam Ruby, Sascha Schumann, Zeev Suraski, Jim Winstead, Andrei Zmievski. </p>
<p> A List of active developers can be found here: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/credits.php">http://www.php.net/credits.php</a></code> </p>
<p> And last but not least PHP was developed with the help of a huge amount of contributors all around the world.</p>
<h2>Version Information</h2>
<p>This manpage describes <code>php-fpm</code>, version 5.4.16.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 1997-2009 The PHP Group </p>
<p> Copyright (c) 2007-2009, Andrei Nigmatulin </p>
<p> This source file is subject to version 3.01 of the PHP license, that is bundled with this package in the file LICENSE, and is available through the world-wide-web at the following url: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/license/3_01.txt">http://www.php.net/license/3_01.txt</a></code> </p>
<p> If you did not receive a copy of the PHP license and are unable to obtain it through the world-wide-web, please send a note to <code>license [at] php.net</code> so we can mail you a copy immediately.</p>
