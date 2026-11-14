---
title: "nikto(1)"
name: "nikto"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nikto/"
description: "nikto – Scan web server for known vulnerabilities"
---

<h2 class="name">NAME</h2>
<p> nikto &#8211; Scan web server for known vulnerabilities </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/local/bin/nikto</code> [options&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>Examine a web server to find potential problems and security vulnerabilities, including: </p>
<dl>
<dt>
<dd> &bull;Server and software misconfigurations</dl>
<dl>
<dt>
<dd> &bull;Default files and programs</dl>
<dl>
<dt>
<dd> &bull;Insecure files and programs</dl>
<dl>
<dt>
<dd> &bull;Outdated servers and programs</dl>
<p> Nikto is built on LibWhisker (by RFP) and can run on any platform which has a Perl environment. It supports SSL, proxies, host authentication, IDS evasion and more. It can be updated automatically from the command-line, and supports the optional submission of updated version data back to the maintainers.</p>
<h2>OPTIONS</h2>
<p> Below are all of the Nikto command line options and explanations. A brief version of this text is available by running Nikto with the -h (-help) option. </p>
<p> <code>-Cgidirs</code></p>
<dl>
<dt>
<dd> Scan these CGI directories. Special words &quot;none&quot; or &quot;all&quot; may be used to scan all CGI directories or none, (respectively). A literal value for a CGI directory such as &quot;/cgi-test/&quot; may be specified (must include trailing slash). If this is option is not specified, all CGI directories listed in config.txt will be tested.</dl>
<p> <code>-config</code></p>
<dl>
<dt>
<dd> Specify an alternative config file to use instead of the config.txt located in the install directory.</dl>
<p> <code>-dbcheck</code></p>
<dl>
<dt>
<dd> Check the scan databases for syntax errors.</dl>
<p> <code>-Display</code></p>
<dl>
<dt>
<dd> Control the output that Nikto shows. See Chapter 5 for detailed information on these options. Use the reference number or letter to specify the type, multiple may be used: </p>
<p> 1 &#8211; Show redirects </p>
<p> 2 &#8211; Show cookies received </p>
<p> 3 &#8211; Show all 200/OK responses </p>
<p> 4 &#8211; Show URLs which require authentication </p>
<p> D &#8211; Debug Output </p>
<p> V &#8211; Verbose Output</dl>
<p> <code>-evasion</code></p>
<dl>
<dt>
<dd> Specify the LibWhisker IDS evasion technique to use (see the LibWhisker docs for detailed information on these). Use the reference number to specify the type, multiple may be used: </p>
<p> 1 &#8211; Random URI encoding (non-UTF8) </p>
<p> 2 &#8211; Directory self-reference (/./) </p>
<p> 3 &#8211; Premature URL ending </p>
<p> 4 &#8211; Prepend long random string </p>
<p> 5 &#8211; Fake parameter </p>
<p> 6 &#8211; TAB as request spacer </p>
<p> 7 &#8211; Change the case of the URL </p>
<p> 8 &#8211; Use Windows directory separator (\)</dl>
<p> <code>-findonly</code></p>
<dl>
<dt>
<dd> Only discover the HTTP(S) ports, do not perform a security scan. This will attempt to connect with HTTP or HTTPS, and report the Server header.</dl>
<p> <code>-Format</code></p>
<dl>
<dt>
<dd> Save the output file specified with -o (-output) option in this format. If not specified, the default will be taken from the file extension specified in the -output option. Valid formats are: </p>
<p> csv &#8211; a comma-seperated list </p>
<p> htm &#8211; an HTML report </p>
<p> txt &#8211; a text report </p>
<p> xml &#8211; an XML report</dl>
<p> <code>-host</code></p>
<dl>
<dt>
<dd> Host(s) to target. Can be an IP address, hostname or text file of hosts. A single dash (-) maybe used for stdout. Can also parse nmap -oG style output</dl>
<p> <code>-Help</code></p>
<dl>
<dt>
<dd> Display extended help information.</dl>
<p> <code>-id</code></p>
<dl>
<dt>
<dd> ID and password to use for host Basic host authentication. Format is &quot;id:password&quot;.</dl>
<p> <code>-list-plugins</code></p>
<dl>
<dt>
<dd> Will list all plugins that Nikto can run against targets and then will exit without performing a scan. These can be tuned for a session using the -plugins option. </p>
<p> The output format is: </p>
<p> Plugin <i>name</i> </p>
<p> &nbsp;<wbr><i>full name</i> &#8211; <i>description</i> </p>
<p> &nbsp;<wbr>Written by <i>author</i>, Copyright (C) <i>copyright</i></dl>
<p> <code>-mutate</code></p>
<dl>
<dt>
<dd> Specify mutation technique. A mutation will cause Nikto to combine tests or attempt to guess values. These techniques may cause a tremendous amount of tests to be launched against the target. Use the reference number to specify the type, multiple may be used: </p>
<p> 1 &#8211; Test all files with all root directories </p>
<p> 2 &#8211; Guess for password file names </p>
<p> 3 &#8211; Enumerate user names via Apache (/~user type requests) </p>
<p> 4 &#8211; Enumerate user names via cgiwrap (/cgi-bin/cgiwrap/~user type requests) </p>
<p> 5 &#8211; Attempt to brute force sub-domain names, assume that the host name is the parent domain </p>
<p> 6 &#8211; Attempt to guess directory names from the supplied dictionary file</dl>
<p> <code>-mutate-options</code></p>
<dl>
<dt>
<dd> Provide extra information for mutates, e.g. a dictionary file</dl>
<p> <code>-nolookup</code></p>
<dl>
<dt>
<dd> Do not perform name lookups on IP addresses.</dl>
<p> <code>-nossl</code></p>
<dl>
<dt>
<dd> Do not use SSL to connect to the server.</dl>
<p> <code>-no404</code></p>
<dl>
<dt>
<dd> Disable 404 (file not found) checking. This will reduce the total number of requests made to the webserver and may be preferable when checking a server over a slow link, or an embedded device. This will generally lead to more false positives being discovered.</dl>
<p> <code>-output</code></p>
<dl>
<dt>
<dd> Write output to the file specified. The format used will be taken from the file extension. This can be over-riden by using the -Format option (e.g. to write text files with a different extenstion. Existing files will have new information appended.</dl>
<p> <code>-plugins</code></p>
<dl>
<dt>
<dd> Select which plugins will be run on the specified targets. A comma separated list should be provided which lists the names of the plugins. The names can be found by using -list-plugins. </p>
<p> There are two special entries: ALL, which specifies all plugins shall be run and NONE, which specifies no plugins shall be run. The default is ALL</dl>
<p> <code>-port</code></p>
<dl>
<dt>
<dd> TCP port(s) to target. To test more than one port on the same host, specify the list of ports in the -p (-port) option. Ports can be specified as a range (i.e., 80-90), or as a comma-delimited list, (i.e., 80,88,90). If not specified, port 80 is used.</dl>
<p> <code>-Pause</code></p>
<dl>
<dt>
<dd> Seconds to delay between each test.</dl>
<p> <code>-root</code></p>
<dl>
<dt>
<dd> Prepend the value specified to the beginning of every request. This is useful to test applications or web servers which have all of their files under a certain directory.</dl>
<p> <code>-ssl</code></p>
<dl>
<dt>
<dd> Only test SSL on the ports specified. Using this option will dramatically speed up requests to HTTPS ports, since otherwise the HTTP request will have to timeout first.</dl>
<p> <code>-Single</code></p>
<dl>
<dt>
<dd> Perform a single request to a target server. Nikto will prompt for all options which can be specified, and then report the detailed output. See Chapter 5 for detailed information.</dl>
<p> <code>-timeout</code></p>
<dl>
<dt>
<dd> Seconds to wait before timing out a request. Default timeout is 10 seconds.</dl>
<p> <code>-Tuning</code></p>
<dl>
<dt>
<dd> Tuning options will control the test that Nikto will use against a target. By default, if any options are specified, only those tests will be performed. If the &quot;x&quot; option is used, it will reverse the logic and exclude only those tests. Use the reference number or letter to specify the type, multiple may be used: </p>
<p> 0 &#8211; File Upload </p>
<p> 1 &#8211; Interesting File / Seen in logs </p>
<p> 2 &#8211; Misconfiguration / Default File </p>
<p> 3 &#8211; Information Disclosure </p>
<p> 4 &#8211; Injection (XSS/Script/HTML) </p>
<p> 5 &#8211; Remote File Retrieval &#8211; Inside Web Root </p>
<p> 6 &#8211; Denial of Service </p>
<p> 7 &#8211; Remote File Retrieval &#8211; Server Wide </p>
<p> 8 &#8211; Command Execution / Remote Shell </p>
<p> 9 &#8211; SQL Injection </p>
<p> a &#8211; Authentication Bypass </p>
<p> b &#8211; Software Identification </p>
<p> c &#8211; Remote Source Inclusion </p>
<p> x &#8211; Reverse Tuning Options (i.e., include all except specified) </p>
<p> The given string will be parsed from left to right, any x characters will apply to all characters to the right of the character.</dl>
<p> <code>-useproxy</code></p>
<dl>
<dt>
<dd> Use the HTTP proxy defined in the configuration file.</dl>
<p> <code>-update</code></p>
<dl>
<dt>
<dd> Update the plugins and databases directly from cirt.net.</dl>
<p> <code>-Version</code></p>
<dl>
<dt>
<dd> Display the Nikto software, plugin and database versions.</dl>
<p> <code>-vhost</code></p>
<dl>
<dt>
<dd> Specify the Host header to be sent to the target.</dl>
<h2>FILES</h2>
<p> <i>nikto.conf</i></p>
<dl>
<dt>
<dd> The Nikto configuration file. This sets Nikto&#8217;s global options. Several nikto.conf files may exist and are parsed in the below order. As each configuration file is loaded is supersedes any previously set configuration: </p>
<dl>
<dt>
<dd> &bull;System wide (e.g. /etc/nikto.conf)</dl>
<dl>
<dt>
<dd> &bull;Home directory (e.g. $HOME/nikto.conf)</dl>
<dl>
<dt>
<dd> &bull;Current directory (e.g. ./nikto.conf)</dl>
</dl>
<p> <i>${NIKTO_DIR}/plugins/db*</i></p>
<dl>
<dt>
<dd> db files are the databases that nikto uses to check for vulnerabilities and issues within the web server.</dl>
<p> <i>${NIKTO_DIR}/plugins/*.plugin</i></p>
<dl>
<dt>
<dd> All nikto&#8217;s plugins exist here. Nikto itself is just a wrapper script to manage CLI and pass through to the plugins.</dl>
<p> <i>${NIKTO_DIR}/templates</i></p>
<dl>
<dt>
<dd> Contains the templates for nikto&#8217;s output formats.</dl>
<h2>BUGS</h2>
<p> The current features are not supported: </p>
<dl>
<dt>
<dd> &bull;SOCKS Proxies</dl>
<h2>AUTHORS</h2>
<p> Nikto was originally written and maintained by Sullo, CIRT, Inc. It is currently maintained by David Lodge. See the main documentation for other contributors. </p>
<p> All code is (C) CIRT, Inc., except LibWhisker which is (C) rfp.labs (wiretrip.net). Other portions of code may be (C) as specified.</p>
<h2>SEE ALSO</h2>
<p> <i>Nikto Homepage</i>[1]</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Nikto Homepage</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.cirt.net/">http://www.cirt.net/</a></dl>
</dl>
<h2>Index</h2>
