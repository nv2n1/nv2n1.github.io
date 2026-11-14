---
title: "php7-2(1)"
name: "php7-2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-php7-2/"
description: "php – PHP Command Line Interface ‘CLI’"
---

<p>php &#8211; PHP Command Line Interface &#8216;CLI&#8217; </p>
<p> php-cgi &#8211; PHP Common Gateway Interface &#8216;CGI&#8217; command </p>
<h2>Synopsis</h2>
<p><code>php</code> [options] [ <code>-f</code> ] <i>file</i> [[&#8211;] <i>args&#8230;</i>] </p>
<p> <code>php</code> [options] <code>-r</code> <i>code</i> [[&#8211;] <i>args&#8230;</i>] </p>
<p> <code>php</code> [options] [-B <i>begin_code</i>] <code>-R</code> <i>code</i> [-E <i>end_code</i>] [[&#8211;] <i>args&#8230;</i>] </p>
<p> <code>php</code> [options] [-B <i>begin_code</i>] <code>-F</code> <i>file</i> [-E <i>end_code</i>] [[&#8211;] <i>args&#8230;</i>] </p>
<p> <code>php</code> [options] &#8212; [ <i>args&#8230;</i>] </p>
<p> <code>php </code>[options] <code>-a</code> </p>
<p> <code>php</code> [options] -S <i>addr:port</i> [-t <i>docroot</i>] </p>
<h2>Description</h2>
<p><code>PHP</code> is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This is the command line interface that enables you to do the following: </p>
<p> You can parse and execute files by using parameter -f followed by the name of the <i>file</i> to be executed. </p>
<p> Using parameter -r you can directly execute PHP <i>code</i> simply as you would do inside a <code>.php</code> file when using the <code>eval()</code> function. </p>
<p> It is also possible to process the standard input line by line using either the parameter -R or -F. In this mode each separate input line causes the <i>code</i> specified by -R or the <i>file</i> specified by -F to be executed. You can access the input line by <code>$argn</code>. While processing the input lines <code>$argi</code> contains the number of the actual line being processed. Further more the parameters -B and -E can be used to execute <i>code</i> (see -r) before and after all input lines have been processed respectively. Notice that the input is read from <code>STDIN</code> and therefore reading from <code>STDIN</code> explicitly changes the next input line or skips input lines. </p>
<p> PHP also contains an built-in web server for application development purpose. By using the -S option where <code>addr:port</code> point to a local address and port PHP will listen to HTTP requests on that address and port and serve files from the current working directory or the <code>docroot</code> passed by the -t option. </p>
<p> If none of -r -f -B -R -F -E or -S is present but a single parameter is given then this parameter is taken as the filename to parse and execute (same as with -f). If no parameter is present then the standard input is read and executed.</p>
<h2>Options</h2>
<dl COMPACT>
<dd><code>&#8211;interactive</code></p>
<dd><code>-a</code> Run PHP interactively. This lets you enter snippets of PHP code that directly get executed. When readline support is enabled you can edit the lines and also have history support.</p>
<dd><code>&#8211;bindpath </code><i>address:port</i>|<i>port</i></p>
<dd><code>-b </code><i>address:port</i>|<i>port</i> Bind Path for external FASTCGI Server mode (CGI only).</p>
<dd><code>&#8211;no-chdir</code></p>
<dd><code>-C</code> Do not chdir to the script&#8217;s directory (CGI only).</p>
<dd><code>&#8211;no-header</code></p>
<dd><code>-q</code> Quiet-mode. Suppress HTTP header output (CGI only).</p>
<dd><code>&#8211;timing </code><i>count</i></p>
<dd><code>-T </code><i>count</i> Measure execution time of script repeated count times (CGI only).</p>
<dd><code>&#8211;php-ini </code><i>path</i>|<i>file</i></p>
<dd><code>-c </code><i>path</i>|<i>file</i> Look for <code>php.ini</code> file in the directory <i>path</i> or use the specified <i>file</i></p>
<dd><code>&#8211;no-php-ini</code></p>
<dd><code>-n</code> No <code>php.ini</code> file will be used</p>
<dd><code>&#8211;define </code><i>foo</i>[=<i>bar</i>]</p>
<dd><code>-d </code><i>foo</i>[=<i>bar</i>] Define INI entry <i>foo</i> with value <i>bar</i></p>
<dt><code>-e</code></p>
<dd>Generate extended information for debugger/profiler</p>
<dd><code>&#8211;file </code><i>file</i></p>
<dd><code>-f </code><i>file</i> Parse and execute <i>file</i></p>
<dd><code>&#8211;help</code></p>
<dd><code>-h</code> This help</p>
<dd><code>&#8211;hide-args</code></p>
<dd><code>-H</code> Hide script name (<i>file</i>) and parameters (<i>args&#8230;</i>) from external tools. For example you may want to use this when a php script is started as a daemon and the command line contains sensitive data such as passwords.</p>
<dd><code>&#8211;info</code></p>
<dd><code>-i</code> PHP information and configuration</p>
<dd><code>&#8211;syntax-check</code></p>
<dd><code>-l</code> Syntax check only (lint)</p>
<dd><code>&#8211;modules</code></p>
<dd><code>-m</code> Show compiled in modules</p>
<dd><code>&#8211;run </code><i>code</i></p>
<dd><code>-r </code><i>code</i> Run PHP <i>code</i> without using script tags <code>&#8216;&lt;?..?&gt;&#8217;</code></p>
<dd><code>&#8211;process-begin </code><i>code</i></p>
<dd><code>-B </code><i>begin_code</i> Run PHP <i>begin_code</i> before processing input lines</p>
<dd><code>&#8211;process-code </code><i>code</i></p>
<dd><code>-R </code><i>code</i> Run PHP <i>code</i> for every input line</p>
<dd><code>&#8211;process-file </code><i>file</i></p>
<dd><code>-F </code><i>file</i> Parse and execute <i>file</i> for every input line</p>
<dd><code>&#8211;process-end </code><i>code</i></p>
<dd><code>-E </code><i>end_code</i> Run PHP <i>end_code</i> after processing all input lines</p>
<dd><code>&#8211;syntax-highlight</code></p>
<dd><code>-s</code> Output HTML syntax highlighted source</p>
<dd><code>&#8211;server </code><i>addr:port</i></p>
<dd><code>-S </code><i>addr:port</i> Start built-in web server on the given local address and port</p>
<dd><code>&#8211;docroot </code><i>docroot</i></p>
<dd><code>-t </code><i>docroot</i> Specify the document root to be used by the built-in web server</p>
<dd><code>&#8211;version</code></p>
<dd><code>-v</code> Version number</p>
<dd><code>&#8211;strip</code></p>
<dd><code>-w</code> Output source with stripped comments and whitespace</p>
<dd><code>&#8211;zend-extension </code><i>file</i></p>
<dd><code>-z </code><i>file</i> Load Zend extension <i>file</i></p>
<dt><i>args&#8230;</i></p>
<dd>Arguments passed to script. Use <code>&#8216;&#8211;&#8216;</code> <i>args</i> when first argument starts with <code>&#8216;-&#8216;</code> or script is read from stdin</p>
<dd><code>&#8211;rfunction</code> <i>name</i></p>
<dd><code>&#8211;rf</code> <i>name</i> Shows information about function <code>name</code></p>
<dd><code>&#8211;rclass</code> <i>name</i></p>
<dd><code>&#8211;rc</code> <i>name</i> Shows information about class <code>name</code></p>
<dd><code>&#8211;rextension</code> <i>name</i></p>
<dd><code>&#8211;re</code> <i>name</i> Shows information about extension <code>name</code></p>
<dd><code>&#8211;rzendextension</code> <i>name</i></p>
<dd><code>&#8211;rz</code> <i>name</i> Shows information about Zend extension <code>name</code></p>
<dd><code>&#8211;rextinfo</code> <i>name</i></p>
<dd><code>&#8211;ri</code> <i>name</i> Shows configuration for extension <code>name</code></p>
<dt><code>&#8211;ini</code></p>
<dd>Show configuration file names</dl>
<h2>Files</h2>
<dl COMPACT>
<dt><code>/etc/php/@PHP_MAJOR_VERSION@.@PHP_MINOR_VERSION@/cli/php.ini</code></p>
<dd>The configuration file for the CLI version of PHP.</p>
<dt><code>/etc/php/@PHP_MAJOR_VERSION@.@PHP_MINOR_VERSION@/cgi/php.ini</code></p>
<dd>The configuration file for the CGI version of PHP.</p>
<dt><code>/etc/php/@PHP_MAJOR_VERSION@.@PHP_MINOR_VERSION@/apache2/php.ini</code></p>
<dd>The configuration file for the version of PHP that apache2 uses.</dl>
<h2>Examples</h2>
<dl COMPACT>
<dt><i>php -r &#8216;echo &quot;Hello World
&quot;;&#8217;</i></p>
<dd>This command simply writes the text &quot;Hello World&quot; to standard out.</p>
<dt><i>php -r &#8216;print_r(gd_info());&#8217;</i></p>
<dd>This shows the configuration of your gd extension. You can use this to easily check which image formats you can use. If you have any dynamic modules you may want to use the same ini file that php uses when executed from your webserver. There are more extensions which have such a function. For dba use:</p>
<dl COMPACT>
<dd><i>php -r &#8216;print_r(<a href="/docs/linux/man/1-dba_handlers/">dba_handlers</a>(1));&#8217;</i></dl>
<dt><i>php -R &#8216;echo strip_tags($argn).&quot;
&quot;;&#8217;</i></p>
<dd>This PHP command strips off the HTML tags line by line and outputs the result. To see how it works you can first look at the following PHP command &#8216;<i>php -d html_errors=1 -i</i>&#8216; which uses PHP to output HTML formatted configuration information. If you then combine those two &#8216;<i>php &#8230;|php &#8230;</i>&#8216; you&#8217;ll see what happens.</p>
<dt><i>php -E &#8216;echo &quot;Lines: $argi
&quot;;&#8217;</i></p>
<dd>Using this PHP command you can count the lines being input.</p>
<dt><i>php -R &#8216;@$l+=count(file($argn));&#8217; -E &#8216;echo &quot;Lines:$l
&quot;;&#8217;</i></p>
<dd>In this example PHP expects each input line being a file. It counts all lines of the files specified by each input line and shows the summarized result. You may combine this with tools like find and change the php scriptlet.</p>
<dt><i>php -R &#8216;echo &quot;$argn
&quot;; fgets(STDIN);&#8217;</i></p>
<dd>Since you have access to STDIN from within -B -R -F and -E you can skip certain input lines with your code. But note that in such cases $argi only counts the lines being processed by php itself. Having read this you will guess what the above program does: skipping every second input line.</dl>
<h2>Tips</h2>
<p>You can use a shebang line to automatically invoke php from scripts. Only the CLI version of PHP will ignore such a first line as shown below: </p>
<dl COMPACT>
<dd>#!/bin/php </p>
<p> &lt;?php </p>
<p>&nbsp;//&nbsp;your script </p>
<p> ?&gt;</dl>
<h2>See Also</h2>
<p>For a more or less complete description of PHP look here: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/manual/">http://www.php.net/manual/</a></code> </p>
<h2>Bugs</h2>
<p>You can view the list of known bugs or report any new bug you found at: </p>
<p> <code><a rel="nofollow" href="http://bugs.php.net">http://bugs.php.net</a></code></p>
<h2>Authors</h2>
<p>The PHP Group: Thies C. Arntzen, Stig Bakken, Andi Gutmans, Rasmus Lerdorf, Sam Ruby, Sascha Schumann, Zeev Suraski, Jim Winstead, Andrei Zmievski. </p>
<p> Additional work for the CLI sapi was done by Edin Kadribasic, Marcus Boerger and Johannes Schlueter. </p>
<p> A List of active developers can be found here: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/credits.php">http://www.php.net/credits.php</a></code> </p>
<p> And last but not least PHP was developed with the help of a huge amount of contributors all around the world.</p>
<h2>Version Information</h2>
<p>This manpage describes <code>php</code>, version 7.2.24-0ubuntu0.18.04.6.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 1997-2018 The PHP Group </p>
<p> This source file is subject to version 3.01 of the PHP license, that is bundled with this package in the file LICENSE, and is available through the world-wide-web at the following url: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/license/3_01.txt">http://www.php.net/license/3_01.txt</a></code> </p>
<p> If you did not receive a copy of the PHP license and are unable to obtain it through the world-wide-web, please send a note to <code>license [at] php.net</code> so we can mail you a copy immediately.</p>
