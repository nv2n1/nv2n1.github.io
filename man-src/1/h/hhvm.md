---
title: "hhvm(1)"
name: "hhvm"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hhvm/"
description: "hhvm – Execute PHP and Hack files"
---

<h2 class="name">NAME</h2>
<p> hhvm &#8211; Execute PHP and Hack files</p>
<h2>SYNOPSIS</h2>
<p> <code>hhvm</code> [<i>OPTIONS</i>] [<i>-f</i>] file [<i>[</i>&#8212;<i>]</i>args<i>&#8230;</i>]<br />
 <code>hhvm</code> &#8211;php [<i>PHP-OPTIONS</i>] [<i>-f</i>] file [<i>[</i>&#8212;<i>]</i>args<i>&#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) (aka the HipHop Virtual Machine) is an open-source virtual machine designed for executing programs written in Hack and PHP. HHVM uses a just-in-time compilation approach to run programs. HHVM should be used standalone for command line (CLI) scripts or together with a FastCGI-based web server like nginx or apache to serve websites. </p>
<p> This is the command line interface to HHVM. </p>
<p> The simplest way to parse and execute a program is providing a single parameter of a filename. Specifying <code>-f</code> before the filename does this in a more explicit fashion, and allows other <i>OPTIONS</i> to follow. </p>
<p> HHVM has its own set of <i>OPTIONS</i> , but also has the ability to behave like PHP 5.x as well. When the <code>&#8211;php</code> flag is specified to <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) (or the binary is named <code>php</code> ), options available to PHP 5.x can be used. </p>
<p> You may use: </p>
<pre>
<dl><dt><dd>sudo /usr/bin/update-alternatives --install /usr/bin/php php /usr/bin/hhvm 60
</dl>
</pre>
<p> to force <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) to be used even if PHP 5.x is installed on the system. </p>
<h2>FILES</h2>
<p> These are the default configuration files for HHVM. Right now both <code>.ini</code> and <code>.hdf</code> are supported as HHVM continues to migrate completely to <code>.ini</code> </p>
<h3>php.ini</h3>
<p> The default ini settings for <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) are found in <code>/etc/hhvm/php.ini</code> </p>
<h3>config.hdf</h3>
<p> The default hdf options for <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) are found in <code>/etc/hhvm/config.hdf</code> </p>
<h2>OPTIONS</h2>
<p> These are the options you can specify to the <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) executable. </p>
<dl>
<dt><code>-a, &#8211;interactive</code></p>
<dd> Shortcut for the <code>&#8211;mode</code> <i>debug</i> command line option. </p>
<dt><code>&#8211;admin-port</code><i> PORT</i></p>
<dd> Start admin listener at a specified port. The default value for <i>PORT</i> is <code>-1</code>. </p>
<dt><code>&#8211;arg</code><i> ARG</i></p>
<dd> Other arguments. </p>
<dt><code>&#8211;build-id</code><i> ID</i></p>
<dd> Unique identifier to compiled server code. </p>
<dt><code>-c , &#8211;config FILE</code></p>
<dd> Load specified config (.hdf or .ini) <i>FILE</i>. Use multiple <code>-c</code> to specify multiple config files. </p>
<dt><code>&#8211;compiler-id</code></p>
<dd> Display the git hash for the compiler. </p>
<dt><code>&#8211;count</code><i> NUM</i></p>
<dd> How many times to repeat execution. The default value for <i>NUM</i> is <code>1</code>. </p>
<dt><code>-d , &#8211;define SETTING</code></p>
<dd> Define an ini setting in the same format ( foo[=bar] ) as provided in a .ini file. </p>
<dt><code>&#8211;debug-cmd</code><i> ARG</i></p>
<dd> In <code>&#8211;mode</code> <i>debug</i> , this executes the debugger command specified by <i>ARG</i> and returns its output in stdout. Multiple <code>&#8211;debug-cmd</code> can be specified to execute more than one command. </p>
<dt><code>&#8211;debug-config</code><i> FILE</i></p>
<dd> In <code>&#8211;mode</code> <i>debug</i> , load the specified debugger configuration <i>FILE</i>. </p>
<dt><code>&#8211;debug-extension</code><i> ARG</i></p>
<dd> In <code>&#8211;mode</code> <i>debug</i> , <i>ARG</i> specifies which debugger extension PHP file to load. </p>
<dt><code>&#8211;debug-port</code><i> PORT</i></p>
<dd> In <code>&#8211;mode</code> <i>debug</i> , connect to the debugger server at specified <i>PORT</i>. </p>
<dt><code>&#8211;debug-sandbox</code><i> ARG</i></p>
<dd> In <code>&#8211;mode</code> <i>debug</i> , initial sandbox to attach to when the debugger is started. The default for <i>ARG</i> is &quot;default&quot;. </p>
<dt><code>&#8211;extra-header</code><i> ARG</i></p>
<dd> An extra-header to add to the front of each line of logging. </p>
<dt><code>-f , &#8211;file FILE</code></p>
<dd> In <code>&#8211;mode</code> <i>run</i> , execute the specified <i>FILE .</i> </p>
<dt><code>-h , &#8211;debug-host ADDRESS</code></p>
<dd> In <code>&#8211;mode</code> <i>debug</i> , connect to debugger server at specified address. The default for <i>ADDRESS</i> is <code>localhost</code>. </p>
<dt><code>&#8211;help</code></p>
<dd> Display the list of command line options with short descriptions. </p>
<dt><code>&#8211;instance-id</code><i> ID</i></p>
<dd> Unique identifier of server instance. </p>
<dt><code>-l , &#8211;lint FILE</code></p>
<dd> Run lint on the specified <i>FILE</i>. </p>
<dt><code>-m , &#8211;mode MODE</code></p>
<dd> <i>MODE</i> can be any of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> run (default): directly executes the program from the command line.</p>
<dt>&bull;</p>
<dd> debug (d): starts the debugger.</p>
<dt>&bull;</p>
<dd> server (s): starts an HTTP server from command line.</p>
<dt>&bull;</p>
<dd> daemon: starts an HTTP server and runs it as a daemon.</p>
<dt>&bull;</p>
<dd> replay: replays a previously recorded HTTP request file.</p>
<dt>&bull;</p>
<dd> translate (t): translates a hex-encoded stacktrace.</dl>
</dl>
<dt><code>&#8211;no-config</code></p>
<dd> Do not use the default php.ini </p>
<dt><code>&#8211;no-safe-access-check</code><i> BOOL</i></p>
<dd> Whether to allow any file or directory access without security checking. The default value is <code>0</code> (or false). </p>
<dt><code>-p , &#8211;port PORT</code></p>
<dd> Start an HTTP server at the specified port. The default <i>PORT</i> is <code>-1</code>. </p>
<dt><code>&#8211;php</code></p>
<dd> Emulate the standard <code><a href="/docs/linux/man/1-php/">php</a>(1)</code> command line. You can specify the options allowed in PHP 5.x. </p>
<dt><code>&#8211;port-fd FD</code></p>
<dd> Use the specified <i>FD</i> for HTTP instead of creating a socket. The default value is <code>-1</code>. </p>
<dt><code>&#8211;ssl-port-fd FD</code></p>
<dd> Use the specified <i>FD</i> for SSL instead of creating a socket. The default value is <code>-1</code>. </p>
<dt><code>&#8211;repo-schema</code></p>
<dd> Display the repository schema id. </p>
<dt><code>&#8211;temp-file</code><i> FILE</i></p>
<dd> <i>FILE</i> specified is temporary and removed after execution. </p>
<dt><code>-u , &#8211;user USER</code></p>
<dd> Run server under the specified <i>USER</i> account. </p>
<dt><code>-v , &#8211;config-value SETTING</code></p>
<dd> Individual configuration string in HDF format (name=value), where name can be any valid configuration for a config file. e.g., Section.Name=Value. </p>
<dt><code>&#8211;version</code></p>
<dd> Display the <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) version number. </p>
<dt><code>-w , &#8211;show FILE</code></p>
<dd> Directly output the specified <i>FILE</i> and do nothing else. </p>
<dt><code>&#8211;xhprof-flags</code><i> FLAGS</i></p>
<dd> Set the XHProf run flags. </p>
</dl>
<h2>PHP-OPTIONS</h2>
<p> These are the options you can specify to the <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) executable when explicitly specifying the <i>&#8211;php</i> flag, or when the binary is named <code>php .</code> All PHP 5.x options are not supported at this point in time; we are planning to continue to add more option support. </p>
<dl>
<dt><code>-a, &#8211;interactive</code></p>
<dd> Similar to the same option when not specifying <i>&#8211;php .</i> Run HHVM interactively. This lets you enter snippets of PHP code that directly get executed. </p>
<dt><code>-c</code><i> FILE</i></p>
<dd> Use the specified <i>FILE</i> for configuration options. The file should be .ini format. </p>
<dt><code>-d</code><i> SETTING</i></p>
<dd> Define INI entry specified by <i>SETTING</i> of the form <code>foo=[bar] .</code> </p>
<dt><code>-n</code></p>
<dd> Do not use any configuration (e.g., .ini) file when executing. </p>
<dt><code>-r</code><i> CODE</i></p>
<dd> Run HHVM code without using script tags, directly on the command line. </p>
<dt><code>-v</code></p>
<dd> Output the current HHVM build version number. </p>
<dt><code>-w</code></p>
<dd> Output source with stripped comments and whitespace. </p>
<dt><code>-z</code><i> FILE</i></p>
<dd> Load a dynamic extension file. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><i>hhvm foo.php</i></p>
<dd> Execute a PHP file. </p>
<dt><i>hhvm -c custom.ini foo.php</i></p>
<dd> Execute a PHP file given a certain configuration. </p>
<dt><i>hhvm &#8211;php -r &#8216;echo &quot;Hello Everyone!&quot;;&#8217;</i></p>
<dd> Execute code from the command line using the &#8211;php option and -r. </p>
<dt><i>hhvm -m server &#8211;port 9090</i></p>
<dd> Execute HHVM in server mode using a specified port. </p>
</dl>
<h2>BUGS</h2>
<p> The list of current known HHVM issues are found at: <i><a rel="nofollow" href="https://github.com/facebook/hhvm/issues">https://github.com/facebook/hhvm/issues</a></i> </p>
<h2>AUTHORS</h2>
<p> The contributors to HHVM can be found here: <i><a rel="nofollow" href="https://github.com/facebook/hhvm/graphs/contributors">https://github.com/facebook/hhvm/graphs/contributors</a></i> </p>
<h2>VERSION INFORMATION</h2>
<p> This manpage describes <code><a href="/docs/linux/man/1-hhvm/">hhvm</a></code>(1) , version 3.0 and greater </p>
<h2>COPYRIGHT</h2>
<p> HHVM is licensed under the PHP and Zend licenses except as otherwise noted. The full license can be found at: <i><a rel="nofollow" href="https://github.com/facebook/hhvm">https://github.com/facebook/hhvm</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hphpize/">hphpize</a></code>(1)<br />
 <i><a rel="nofollow" href="http://docs.hhvm.com">http://docs.hhvm.com</a></i> </p>
<h2>Index</h2>
