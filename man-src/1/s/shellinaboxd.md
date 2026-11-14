---
title: "shellinaboxd(1)"
name: "shellinaboxd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shellinaboxd/"
description: "shellinaboxd – publish command line shell through AJAX interface"
---

<h2>NAME</h2>
<p> shellinaboxd &#8211; publish command line shell through AJAX interface</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>shellinaboxd</code></p>
<dd> [&nbsp;<wbr><code>-b</code>&nbsp;<wbr>| <code>&#8211;background</code>[<code>=</code><i>pidfile</i>]&nbsp;<wbr>] [&nbsp;<wbr><code>-c</code>&nbsp;<wbr>| <code>&#8211;cert=</code><i>certdir</i>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;cert-fd=</code><i>fd</i>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;css=</code><i>filename</i>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;cgi</code>[<code>=</code><i>portrange</i>]&nbsp;<wbr>] [&nbsp;<wbr><code>-d</code>&nbsp;<wbr>| <code>&#8211;debug</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-f</code>&nbsp;<wbr>| <code>&#8211;static-file=</code><i>url</i>:<i>file</i>&nbsp;<wbr>] [&nbsp;<wbr><code>-g</code>&nbsp;<wbr>| <code>&#8211;group=</code><i>gid</i>&nbsp;<wbr>] [&nbsp;<wbr><code>-h</code>&nbsp;<wbr>| <code>&#8211;help</code>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;linkify</code>=[<code>none</code>|<code>normal</code>|<code>aggressive</code>]&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;localhost-only</code>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;no-beep</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-n</code>&nbsp;<wbr>| <code>&#8211;numeric</code>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;pidfile=</code><i>pidfile</i>&nbsp;<wbr>] [&nbsp;<wbr><code>-p</code>&nbsp;<wbr>| <code>&#8211;port=</code><i>port</i>&nbsp;<wbr>] [&nbsp;<wbr><code>-s</code>&nbsp;<wbr>| <code>&#8211;service=</code><i>service</i>&nbsp;<wbr>] [&nbsp;<wbr><code>-t</code>&nbsp;<wbr>| <code>&#8211;disable-ssl</code>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;disable-ssl-menu</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-q</code>&nbsp;<wbr>| <code>&#8211;quiet</code>&nbsp;<wbr>] [&nbsp;<wbr><code>-u</code>&nbsp;<wbr>| <code>&#8211;user=</code><i>uid</i>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;user-css=</code><i>styles</i>&nbsp;<wbr>] [&nbsp;<wbr><code>-v</code>&nbsp;<wbr>| <code>&#8211;verbose</code>&nbsp;<wbr>] [&nbsp;<wbr><code>&#8211;version</code>&nbsp;<wbr>]</dl>
<h2>DESCRIPTION</h2>
<p> The <code>shellinaboxd</code> daemon implements a webserver that listens on the specified <i>port</i>. The web server publishes one or more <i>services</i> that will be displayed in a VT100 emulator implemented as an AJAX web application. By default, the port is 4200 and the default service URL is <i><a rel="nofollow" href="http://localhost:4200/">http://localhost:4200/</a></i>. </p>
<p> If no particular <i>service</i> was requested, the server launches <code>/bin/login</code> querying the user for their username and password. It then starts the user&#8217;s default login shell. </p>
<p> Any modern JavaScript and CSS enabled browser will be able to access the published <i>service</i> without requiring additional plugins.</p>
<h2>OPTIONS</h2>
<p> The following command line parameters control the operation of the daemon:</p>
<dl>
<dt><code>-b</code>&nbsp;<wbr>| <code>&#8211;background</code>[<code>=</code><i>pidfile</i>]</p>
<dd> Launch <code>shellinaboxd</code> as a background daemon process. Optionally, write the process id to <i>pidfile</i>.</p>
<dt><code>-c</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;cert=</code><i>certdir</i></p>
<dd> If built with SSL/TLS support enabled, the daemon will look in <i>certdir</i> for any certificates. If unspecified, this defaults to the current working directory. </p>
<p> If the browser negotiated a <code>Server Name Identification</code> the daemon will look for a matching <i>certificate-</i>SERVERNAME.pem file. This allows for virtual hosting of multiple server names on the same IP address and port. </p>
<p> If no <code>SNI</code> handshake took place, it falls back on using the certificate in the <i>certificate.pem</i> file. </p>
<p> The administrator should make sure that there are matching certificates for each of the virtual hosts on this server, and that there is a generic <i>certificate.pem</i> file. </p>
<p> If no suitable certificate is installed, <code>shellinaboxd</code> will attempt to invoke <code>/usr/bin/openssl</code> and create a new self-signed certificate. This only succeeds if, after dropping privileges, <code>shellinaboxd</code> has write permissions for <i>certdir</i>. </p>
<p> Most browsers show a warning message when encountering a self-signed certificate and then allow the user the option of accepting the certificate. Due to this usability problem, and due to the perceived security implications, the use of auto-generated self-signed certificates is intended for testing or in intranet deployments, only.</p>
<dt><code>&#8211;cert-fd=</code><i>fd</i></p>
<dd> Instead of providing a <code>&#8211;cert</code> directory, it is also possible to provide a filedescriptor <i>fd</i> where the certificate and key can be retrieved. While this option disables <code>SNI</code> support, it does offer an alternative solution for securely providing the private key data to the daemon.</p>
<dt><code>&#8211;css=</code><i>filename</i></p>
<dd> Sometimes, it is not necessary to replace the entire style sheet using the <code>&#8211;static-file</code> option. But instead a small incremental change should be made to the visual appearance of the terminal. The <code>&#8211;css</code> option provides a means to append additional style rules to the end of the default <code>styles.css</code> sheet. More than one <code>&#8211;css</code> option can be given on the same command line.</p>
<dt><code>&#8211;cgi</code>[<code>=</code><i>portrange</i>]</p>
<dd> Instead of running <code>shellinaboxd</code> as a permanent process, it can be demand-loaded as a CGI web server extension. When doing so, it will spawn a server that lives for the duration of the user&#8217;s session. If an optional <i>portrange</i> of the form <code>MINPORT-MAXPORT</code> has been provided, the server limits itself to these port numbers. They should be configured to pass through the firewall. </p>
<p> The <code>&#8211;cgi</code> option is mutually exclusive with the <code>&#8211;background</code>, <code>&#8211;pidfile</code> and <code>&#8211;port</code> options. </p>
<p> In order to be useful as a CGI script, the <code>shellinaboxd</code> binary probably will have to be made <code>setuid-root</code>. This is currently a discouraged configuration. Use with care.</p>
<dt><code>-d</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;debug</code></p>
<dd> Enables debugging mode, resulting in lots of log messages on <i>stderr</i>. This option is mutually exclusive with <code>&#8211;quiet</code> and <code>&#8211;verbose</code>.</p>
<dt><code>-f</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;static-file=</code><i>url</i>:<i>file</i></p>
<dd> The daemon serves various built-in resources from URLs underneath the <i>service</i> mount points. One or more <code>&#8211;static-file</code> options allow for overriding these resources with customized externally provided <i>files</i>. The <i>url</i> can either be an absolute or a relative path. In the former case, it overrides exactly one built-in resource for one specific <i>service</i>, whereas in the latter case it overrides resources for each defined <i>service</i>. </p>
<p> The following resources are available for customization:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>beep.wav</code></p>
<dd> audio sample that gets played whenever the terminal BEL is sounded.</p>
<dt><code>favicon.ico</code></p>
<dd> favicon image file that is displayed in the browser&#8217;s navigation bar.</p>
<dt><code>ShellInABox.js</code></p>
<dd> JavaScript file implementing the AJAX terminal emulator.</p>
<dt><code>styles.css</code></p>
<dd> CSS style file that controls the visual appearance of the terminal.</p>
<dt><code>print-styles.css</code></p>
<dd> CSS style file that controls the visual appearance of printed pages when using the VT100 transparent printing feature.</dl>
<p> It is not recommended to override the root HTML page for a particular <i>service</i>. Instead, move the service to an anonymous URL and serve a <i>static-file</i> that references the <i>service</i> in an <i>&lt;iframe&gt;</i>. </p>
<p> Instead of a <i>file</i>, it is possible to provide the name of a directory. This turns <code>shellinaboxd</code> into a simple web server that publishes all of the files in that particular directory. This option can be helpful when publishing a more complex root HTML page.</dl>
<dt><code>-g</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;group=</code><i>gid</i></p>
<dd> When started as <code>root</code>, the server drops most privileges at start up. Unless overridden by the <code>&#8211;group</code> option, it switches to <code>nogroup</code>. </p>
<p> When already running as an unprivileged user, group changes are not possible. </p>
<p> If running with SSL/TLS support enabled, the certificates must be accessible to the unprivileged user and/or group that the daemon runs as.</p>
<dt><code>-h</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;help</code></p>
<dd> Display a brief usage message showing the valid command line parameters.</p>
<dt><code>&#8211;linkify</code>=[<code>none</code>|<code>normal</code>|<code>aggressive</code>]</p>
<dd> the daemon attempts to recognize URLs in the terminal output and makes them clickable. This is not necessarily a fool-proof process and both false negatives and false positives are possible. By default, only URLs starting with a well known protocol of <code>http://</code>,&nbsp;<wbr><code>https://</code>,&nbsp;<wbr><code>ftp://</code>, or&nbsp;<wbr><code>mailto:</code> are recognized. In <code>aggressive</code> mode, anything that looks like a hostname, URL or e-mail address is recognized, even if not preceded by a protocol.</p>
<dt><code>&#8211;localhost-only</code></p>
<dd> Normally, <code>shellinaboxd</code> listens on all available network interfaces. When operating behind a reverse-proxy that is not always desirable. This command line option tells the daemon to only listen on the loopback interface.</p>
<dt><code>&#8211;no-beep</code></p>
<dd> not only are audible signals undesired in some working environments, but browser support for media playback is often buggy, too. Setting this option suppresses all audio playback and enables the visual bell by default.</p>
<dt><code>-n</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;numeric</code></p>
<dd> When running in <code>&#8211;verbose</code> mode, the daemon prints an <i>Apache</i>-style log file to <i>stderr</i>. By default, host names of peers get resolved before logging them. As DNS look-ups can be expensive, it is possible to request logging of numeric IP addresses, instead.</p>
<dt><code>&#8211;pidfile=</code><i>pidfile</i></p>
<dd> The <code>shellinaboxd</code> daemon can be configured to store its process identifier in <i>pidfile</i>.</p>
<dt><code>-p</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;port=</code><i>port</i></p>
<dd> Unless overridden by this option, the web server listens on port 4200 for incoming HTTP and HTTPS requests. </p>
<p> <code>shellinaboxd</code> can distinguish between SSL/TLS requests and unencrypted requests. It also knows how to negotiate <code>Server Name</code> <code>Identification</code>, allowing the use of a single port for all types of requests even when virtual hosting.</p>
<dt><code>-s</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;service=</code><i>service</i></p>
<dd> One or more services can be registered on different URL paths: <i>SERVICE</i> := &lt;url-path&gt; &#8216;:&#8217; <i>APPLICATION</i> </p>
<p> There is a pre-defined <i>application</i>, &#8216;LOGIN&#8217;, which causes the daemon to invoke <code>/bin/login</code> requesting the user&#8217;s name and password, and starting his login shell. This is the default option for the <code>root</code> user, if no <code>&#8211;service</code> was defined. Starting <code>/bin/login</code> requires <code>root</code> privileges. </p>
<p> There is another pre-defined <i>application</i>, &#8216;SSH&#8217;. Instead of invoking <code>/bin/login</code>, it calls <code>ssh</code>. This is the default option for unprivileged users, if no <code>&#8211;service</code> was defined. This operation is available to both privileged and regular users. If the optional <i>host</i> parameter is omitted, <code>shellinaboxd</code> connects to <code>localhost</code>. </p>
<p> Alternatively, an <i>application</i> can be specified by providing a <i>user</i> description, a working directory, and a command line: <i>APPLICATION</i> := &#8216;LOGIN&#8217; | &#8216;SSH&#8217; [ &#8216;:&#8217; &lt;host&gt; ] | <i>USER</i> &#8216;:&#8217; <i>CWD</i> &#8216;:&#8217; <i>CMD</i> </p>
<p> <i>USER</i> := &lt;username&gt; &#8216;:&#8217; &lt;groupname&gt; </p>
<p> The working directory can either be given as an absolute path, or it can be the user&#8217;s home directory: <i>CWD</i> := &#8216;HOME&#8217; : &lt;dir&gt; </p>
<p> The command that <code>shellinaboxd</code> executes can either be specified as the &#8216;SHELL&#8217; keyword, denoting the user&#8217;s default login shell, or an arbitrary command line: <i>CMD</i> := &#8216;SHELL&#8217; : &lt;cmdline&gt; </p>
<p> The &lt;cmdline&gt; supports expansion of variables of the form ${VAR}. Supported variables are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>${columns}</code></p>
<dd> number of columns.</p>
<dt><code>${gid}</code></p>
<dd> numeric group id.</p>
<dt><code>${group}</code></p>
<dd> group name.</p>
<dt><code>${home}</code></p>
<dd> home directory.</p>
<dt><code>${lines}</code></p>
<dd> number of rows.</p>
<dt><code>${peer}</code></p>
<dd> name of remote peer.</p>
<dt><code>${realip}</code></p>
<dd> value of HTTP header field &#8216;X-Real-IP&#8217;.</p>
<dt><code>${uid}</code></p>
<dd> numeric user id.</p>
<dt><code>${url}</code></p>
<dd> the URL that serves the terminal session.</p>
<dt><code>${user}</code></p>
<dd> user name.</dl>
<p> Other than the environment variables of <code>$TERM</code>, <code>$COLUMNS,</code> <code>$LINES,</code> <code>$SHELLINABOX_PEERNAME,</code> <code>$SHELLINABOX_REALIP</code> and <code>$SHELLINABOX_URL,</code> services can have environment variables passed to them, by preceding the &lt;cmdline&gt; with space separated variable assignments of the form <i>KEY</i>=<i>VALUE</i>. </p>
<p> The &lt;cmdline&gt; supports single and double quotes, as well as backslashes for escaping characters in the familiar fashion. </p>
<p> Please note that when invoking <code>shellinaboxd</code> from a command line shell, additional quoting might be required to prevent the shell from expanding the variables prior to passing them to the daemon. </p>
<p> If no explicit <code>&#8211;service</code> has been requested, <code>shellinaboxd</code> defaults to attaching the default service to the root directory of the web server. For <code>root</code>, this is <code>/bin/login</code>, and for unprivileged users, this is <code>ssh localhost</code>. This is equivalent to saying <code>&#8211;service=/:LOGIN</code>, or <code>&#8211;service=/:SSH</code>, respectively. </p>
<p> Please note that for SSH service to work properly, we need a running ssh server on local system with enabled password authentication. If we are using &lt;host&gt; parameter, same conditions must be true on that remote system. </p>
</dl>
<dt><code>-t</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;disable-ssl</code></p>
<dd> By default, <code>shellinaboxd</code> redirectes all incoming HTTP requests to their equivalent HTTPS URLs. If promoting of connections to encrypted SSL/TLS sessions is undesired, this behavior can be disabled. </p>
<p> This option is also useful during testing or for deployment in trusted intranets, if SSL certificates are unavailable.</p>
<dt><code>&#8211;disable-ssl-menu</code></p>
<dd> If the user should not be able to switch between HTTP and HTTPS modes, this choice can be removed from the context menu. The user can still make this choice by directly going to the appropriate URL.</p>
<dt><code>-q</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;quiet</code></p>
<dd> Suppresses all messages to <i>stderr</i>. This option is mutually exclusive with <code>&#8211;debug</code> and <code>&#8211;verbose</code>.</p>
<dt><code>-u</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;user=</code><i>uid</i></p>
<dd> If started as <code>root</code>, the server drops privileges by changing to <code>nobody</code>, unless the <i>uid</i> has been overridden by this option. </p>
<p> For more details, refer to the description of the <code>&#8211;group</code> option.</p>
<dt><code>&#8211;user-css=</code><i>styles</i></p>
<dd> The visual appearance of the terminal emulator can be customized through user-selectable style sheets. These style sheets will show up as options in the right-click context menu of the terminal emulator. </p>
<p> Styles sheet make up either independently selectable on/off options, or multiple style sheets can be grouped together. When forming a group, only one member of the group can be active at any given time. This is used for multiple-choice options. </p>
<p> Multiple independent groups are separated by semicolons: <i>STYLES</i> := <i>GROUP</i> { &#8216;;&#8217; <i>GROUP</i> }* </p>
<p> The members of a group are separated by commas: <i>GROUP</i> := <i>OPTION</i> { &#8216;,&#8217; OPTION }* </p>
<p> Groups with exactly one member are used for options that can be independently turned on and off. </p>
<p> Options include a human readable label that will be shown in the context menu, followed by the name of the CSS file. They also must include an indicator showing whether the option should initially be turned on or turned off. Within a group, exactly one option should be turned on: <i>OPTION</i> := &lt;label&gt; &#8216;:&#8217; [ &#8216;-&#8216; | &#8216;+&#8217; ] &lt;css-file&gt; </p>
<p> The user&#8217;s selection of options will be persisted in a cookie. This means, the default settings of options as passed on the command line only takes effect the very first time the user visits the terminal emulator in his browser. On all subsequent visits, the user&#8217;s preferences take precedence.</p>
<dt><code>-v</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;verbose</code></p>
<dd> Enables logging of <i>Apache</i>-style log file to <i>stderr</i>. This option is mutually exclusive with <code>&#8211;debug</code> and <code>&#8211;quiet</code>.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the version number of the binary and exits.</dl>
<h2>CONFIGURATION</h2>
<p> There are no configuration files or permanent settings for <code>shellinaboxd</code>. </p>
<p> A small number of run-time configuration options are available from a context menu that becomes available when clicking the right mouse button. These options get persisted in a browser cookie. </p>
<p> Many sites already have a web server running and would like to integrate <code>shellinaboxd</code> into their existing site. This is most commonly done by means of a reverse-proxy entry for the main web server. For <i>Apache</i> this would require adding an option such as:<br />
&nbsp;<wbr>&lt;Location&nbsp;<wbr>/shell&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>ProxyPass&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://localhost:4200/">http://localhost:4200/</a><br />
&nbsp;<wbr>&nbsp;<wbr>Order&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>allow,deny<br />
&nbsp;<wbr>&nbsp;<wbr>Allow&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>from all<br />
&nbsp;<wbr>&lt;/Location&gt; </p>
<p> If you are using a different web server, refer to that server&#8217;s documentation on how to configure reverse proxy operations. </p>
<p> When using a reverse proxy, the <code>&#8211;localhost-only</code> option would normally be enabled as well. In addition, the <code>&#8211;disable-ssl</code> might also be considered depending on the exact configuration details of the reverse proxy.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>shellinaboxd</code></p>
<dd> Attaches a web-enabled login shell to <i><a rel="nofollow" href="https://localhost:4200/">https://localhost:4200/</a></i>. If the user connected without SSL, the session will automatically be promoted. Unless SSL certificates can be found in the current directory, the daemon will automatically generate suitable self-signed certificates. If the command was invoked by a non-<code>root</code> user, the daemon uses <code>ssh</code> instead of <code>/bin/login</code> for the session.</p>
<dt><code>shellinaboxd -t</code></p>
<dd> Attaches a web-enabled login shell to <i><a rel="nofollow" href="http://localhost:4200/">http://localhost:4200/</a></i> with SSL/TLS support disabled.</p>
<dt><code>shellinaboxd -t -f beep.wav:/dev/null</code></p>
<dd> Runs all services with the audible-bell permanently disabled.</p>
<dt><code>shellinaboxd -s /:SSH:example.org</code></p>
<dd> The terminal connects to a <code>ssh</code> session on <i>example.org</i>.</p>
<dt><code>shellinaboxd -t -s /:AUTH:HOME:/bin/bash</code></p>
<dd> Interactively request the user&#8217;s name and password prior to launching a Bourne shell. This command can be run by unprivileged users. But if doing so, it only allows this particular user to log in.</p>
<dt><code>shellinaboxd -c certificates -u shellinabox -g shellinabox</code></p>
<dd> If the <code>certificates</code> directory exists and is writable by the <code>shellinabox</code> user and group, self-signed SSL certificates will be generated in this directory. This might require creating an appropriately named user first. Running this command as <code>root</code> allows any user on the system to log in at <code><a rel="nofollow" href="http://localhost:4200/">http://localhost:4200/</a></code>. Sessions will automatically be promoted to SSL/TLS.</p>
<dt><code>shellinaboxd -t -s /:LOGIN -s /who:nobody:nogroup:/:w</code></p>
<dd> In addition to the login shell at <i><a rel="nofollow" href="http://localhost:4200">http://localhost:4200</a></i>, show a list of currently logged in users when accessing <i><a rel="nofollow" href="http://localhost:4200/who">http://localhost:4200/who</a></i>. This command must be run as <code>root</code> in order to be able to change to <code>nobody:nogroup</code> as requested by the service description.</p>
<dt><code>shellinaboxd -t -s &#8216;/:root:root:/:wy60 -c /bin/login&#8217;</code></p>
<dd> Instead of the standard <code>ANSI/VT100</code> terminal, publish a <code>Wyse 60</code> terminal. Again, this command should be run as <code>root</code>.</p>
<dt><code>shellinaboxd &#8211;css white-on-black.css</code></p>
<dd> Loads the <code>white-on-black.css</code> style sheet from the current directory and appends it to the built-in <code>styles.css</code> sheet. This causes the terminal to always render white text on a black background.</p>
<dt><code>shellinaboxd &#8211;user-css Normal:+black-on-white.css,Reverse:-white-on-black.css</code></p>
<dd> Allow the user to select whether they want text to be rendered normally or in reverse video. This command line option adds a new entry to the right-click context menu.</dl>
<h2>DIAGNOSTICS</h2>
<p> The daemon returns a non-zero exit code in case of failure. With the exception of a small number of common error cases that are handled explicitly, most errors result in printing a <i>&quot;Check failed&quot;</i> message. This does not typically indicate a bug in the program but is instead its normal way of reporting errors. </p>
<p> Common failure conditions are reusing a port that is already in use, lack of sufficient privileges to run a service, failure to find SSL/TLS certificates, and failure to write newly generated certificates to the certification directory.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1), <code><a href="/docs/linux/man/1-last/">last</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/5-shells/">shells</a></code>(5), <code><a href="//www.systutorials.com/docs/linux/man/1SSL-openssl/">openssl</a></code>(1SSL), <code><a href="/docs/linux/man/1-w/">w</a></code>(1), <code><a href="/docs/linux/man/1-wy60/">wy60</a></code>(1), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1).</p>
<h2>SECURITY</h2>
<p> The daemon uses privilege separation techniques to allow it to drop privileges early. It is aware of setuid flags and restricts some operations when launched as a setuid application. </p>
<p> Despite these safety features, a bug could conceivably lead to a determined attacker gaining elevated privileges. It is therefore strongly discouraged to set the setuid flag on the binary. </p>
<p> The expected deployment would be from a system <i>rc</i> script launched by <code>/sbin/init</code>. For extra security, the <code>&#8211;group</code> and <code>&#8211;user</code> options should be used to change to a dedicated user.</p>
<h2>AUTHOR</h2>
<p> Copyright (C) 2008-2010 by Markus Gutschke &lt;<i>markus [at] shellinabox.com</i>&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software Foundation. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA </p>
<p> In addition to these license terms, the author grants the following additional rights: </p>
<p> If you modify this program, or any covered work, by linking or combining it with the OpenSSL project&#8217;s OpenSSL library (or a modified version of that library), containing parts covered by the terms of the OpenSSL or SSLeay licenses, the author grants you additional permission to convey the resulting work. Corresponding Source for a non-source form of such a combination shall include the source code for the parts of OpenSSL used as well as that of the covered work. </p>
<p> You may at your option choose to remove this additional permission from the work, or from any part of it. </p>
<p> If you would like to negotiate different licensing terms that are compatible for integration with other projects, please contact the author. </p>
<p> If the OpenSSL system libraries can be found at run-time, they will be invoked by <code>shellinaboxd</code> to provide SSL/TLS support. The OpenSSL and SSLeay licenses require the following notices: </p>
<p> This product includes software developed by the OpenSSL Project for use in the OpenSSL Toolkit. (<a rel="nofollow" href="http://www.openssl.org/)">http://www.openssl.org/)</a> </p>
<p> This product includes cryptographic software written by Eric Young (eay [at] cryptsoft.com)</p>
<h2>BUGS</h2>
<p> Due to browser limitations, some features might not be available to users of all browers. </p>
<p> Konqueror does not allow for reliable interception of <i>CTRL</i> keys. If you press a key together with the <i>CTRL</i> modifier, it continues performing the browser&#8217;s predefined behavior for this particular key combination. In most cases, it also fails to report the correct key to the terminal emulator. As a work-around, pressing both the <i>CTRL</i> and the <i>WINDOWS</i> key sometimes works. </p>
<p> Some browsers, most notably IE on Windows, disallow interception of <i>ALT</i> keys and always interpret these keys as menu accelerators. As a work-around, many UNIX applications allow pressing <i>ESC</i>, instead of <i>ALT</i>. </p>
<p> When using non-US keyboard layouts, some browser do not allow for reliably determining shifted <i>ALT</i> keys. Please report these cases if they turn out to be a problem, as work-arounds might be possible. </p>
<p> Access to the native clipboard is typically not possible. Instead, an internal clipboard accessible from the right-button context menu is used for all but IE. </p>
<p> Some browsers restrict the number of concurrent connections to a server. This restricts how many AJAX terminals can be opened simultaneously. If this becomes a problem, users can typically reconfigure their browsers to raise the limit. </p>
<p> There have been reports of the VLC plugin on Linux/x86_64 crashing Firefox when the browser page gets reloaded. Setting the <code>&#8211;no-beep</code> option eliminates all references to VLC and thus appears to work around this crash. </p>
<h2>Index</h2>
