---
title: "dnssec-trigger(8)"
name: "dnssec-trigger"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnssec-trigger/"
description: "dnssec-trigger, dnssec-triggerd, dnssec-trigger-panel, dnssec-trigger-control, dnssec-trigger-control-setup, dnssec-trigger.conf – check DNS servers for DNSSEC support and adjust to compensate."
---

<p><code>dnssec-trigger,</code> <code>dnssec-triggerd,</code> <code>dnssec-trigger-panel,</code> <code>dnssec-trigger-control,</code> <code>dnssec-trigger-control-setup,</code> <code>dnssec-trigger.conf</code> &#8211; check DNS servers for DNSSEC support and adjust to compensate.</p>
<h2>Synopsis</h2>
<p><code>dnssec-triggerd</code> [<code>-d</code>] [<code>-v</code>] [<code>-u</code>] [<code>-c</code> <i>file</i>] </p>
<p> <code>dnssec-trigger-control</code> [<code>-c</code> <i>file</i>] [<code>-s</code> ip[@port] ] command [arguments] </p>
<p> <code>dnssec-trigger-panel</code> [<code>-d</code>] [<code>-c</code> <i>file</i>]</p>
<h2>Description</h2>
<p>The <code>dnssec-trigger</code> programs steer <i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8) towards DNSSEC capable DNS servers. A DHCP hook installed on the system calls <code>dnssec-trigger-control</code> that contacts the daemon <code>dnssec-triggerd</code> that probes the list of servers. The daemon then adjusts a running unbound through <i><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></i>(8) and notifies the user applet <code>dnssec-trigger-panel</code> for GUI display. </p>
<p> The <code>dnssec-trigger-panel</code> runs after user login, displays notifications and status to the user. It may popup a warning if no DNSSEC capable servers are available, with options to disconnect or to connect insecurely. </p>
<p> The <code>dnssec-trigger-control</code> tool is used in the background by scripts to notify the daemon of new (DHCP) DNS servers. It can be used to test the system by providing a (fake) list of DNS server IP addresses. </p>
<p> The <code>dnssec-trigger-control-setup</code> tool is used to setup the SSL keys that the daemon and user panel use to communicate securely. It must be run once after installation.</p>
<h2>The Dnssec-Triggerd Daemon</h2>
<p>Thus the dnssec-triggerd daemon runs continually, and is started after boot. It receives a list of IP addresses, probes them, and adjusts unbound and resolv.conf. Unbound acts as the validating local resolver, running on 127.0.0.1. And resolv.conf is modified to point to 127.0.0.1.</p>
<dl>
<dt><code>-c</code><i> cfgfile</i></p>
<dd>Set the config file with settings for the dnssec-triggerd to read instead of reading the file at the default location, <i>/etc/dnssec-trigger/dnssec-trigger.conf</i>. The syntax is described below.</p>
<dt><code>-d</code></p>
<dd>Debug flag, do not fork into the background, but stay attached to the console.</p>
<dt><code>-u</code></p>
<dd>uninstall dns override: makes resolv.conf mutable again, or other OS action.</p>
<dt><code>-v</code></p>
<dd>Increase verbosity. If given multiple times, more information is logged. This is in addition to the verbosity (if any) from the config file.</dl>
<h2>The Dnssec-Trigger.Conf File</h2>
<p>The config file contains options. It is fairly simple, key: value. You can make comments with &#8216;#&#8217; and have empty lines. The parser is simple and expects one statement per line.</p>
<dl>
<dt><code>verbosity: </code>&lt;num&gt;</p>
<dd>Amount of logging, 1 is default. 0 is only errors, 2 is more detail, 4 for debug.</p>
<dt><code>pidfile: </code>&lt;file&gt;</p>
<dd>The filename where the pid of the dnssec-triggerd is stored. Default is /var/run/dnssec-trigger.pid.</p>
<dt><code>logfile: </code>&lt;file&gt;</p>
<dd>Log to a file instead of syslog, default is to syslog.</p>
<dt><code>use-syslog: </code>&lt;yes or no&gt;</p>
<dd>Log to syslog, default is yes. Set to no logs to stderr (if no logfile) or the configured logfile.</p>
<dt><code>unbound-control: </code>&lt;command&gt;</p>
<dd>The string gives the command to execute. It can be &quot;unbound-control&quot; to search the runtime PATH, or a full pathname. With a space after the command arguments can be configured to the command, i.e. &quot;/usr/local/bin/unbound-control -c my.conf&quot;.</p>
<dt><code>resolvconf: </code>/etc/resolv.conf</p>
<dd>The resolv.conf file to edit (on posix systems). The daemon keeps the file readonly and only make it writable shortly to change it itself. This is to keep other software from interfering. On OSX (if compiled in) also the DNS settings are changed in the network configuration machinery (visible in the network settings control panel). On Windows (if compiled), it sets registry settings for network configuration (may be visible in the control panel tab for network devices) and does not write a resolv.conf file.</p>
<dt><code>domain: </code>example.com</p>
<dd>The domain to set in resolv.conf. See <i><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></i>(5). Picked up once during installation, and not from DHCP since it allows directing traffic elsewhere.</p>
<dt><code>search: </code>example.com</p>
<dd>The domain name search path to set in resolv.conf. See <i><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></i>(5). Picked up once during installation, and not from DHCP since it allows directing traffic elsewhere.</p>
<dt><code>noaction: </code>&lt;yes or no&gt;</p>
<dd>Default is no. If yes, no action is taken to change unbound-control or resolv.conf. The software can be tested with this, probe results are available.</p>
<dt><code>port: </code>&lt;8955&gt;</p>
<dd>Port number to use for communication with dnssec-triggerd. Communication uses 127.0.0.1 (the loopback interface). SSL is used to secure it, and the keys are stored on the disk (see below). The other tools read this config file to find the port number and key locations.</p>
<dt><code>login-command: </code></p>
<dd>The command that is run when the user clicks Login on the no web access dialog. That is supposedly a web browser, that is aimed to open some url so that the hot-spot network login can intercept and show its login page. The default is a detected generic web browser. The &quot;&quot; empty string turns off this feature and no command gets run.</p>
<dt><code>login-location: </code><a rel="nofollow" href="http://www.nlnetlabs.nl/projects/dnssec-trigger">http://www.nlnetlabs.nl/projects/dnssec-trigger</a></p>
<dd>The url that is opened with the web browser. Used as commandline argument.</p>
<dt><code>server-key-file: </code>/etc/dnssec-trigger/dnssec_trigger_server.key</p>
<dd>
<dt><code>server-cert-file: </code>/etc/dnssec-trigger/dnssec_trigger_server.pem</p>
<dd>
<dt><code>control-key-file: </code>/etc/dnssec-trigger/dnssec_trigger_control.key</p>
<dd>
<dt><code>control-cert-file: </code>/etc/dnssec-trigger/dnssec_trigger_control.pem</p>
<dd>The files used for SSL secured communication with dnssec-triggerd. These files can be created with dnssec-trigger-control-setup (run as root).</p>
<dt><code>check-updates: </code>&lt;yes or no&gt;</p>
<dd>Check for software updates, if there are, download them and present the user with a dialog that allows them to run the installer to upgrade the software. It checks a SHA256 checksum on the download, the checksum is signed with DNSSEC (from a TXT record). On windows and osx the default is yes. On other systems the default is no (it&#8217;ll download the source tarball if enabled).</p>
<dt><code>url: </code><a rel="nofollow" href="http://example.com">http://example.com</a> OK</p>
<dd>This command adds an url to probe via HTTP (port 80). The first word, before the space is the url to resolve. The remainder is the string that is expected as page contents (that may be prefixed or suffixed with whitespace). The url is resolved, a HTTP 1.1 query is sent. The reply must be type 2xx and contain the page contents. If this is not true, dnssec-trigger knows that there is a &#8216;hot spot&#8217; of some sort interfering with traffic. If you do not configure any urls, then no probes are done. If you configure multiple urls then it probes a random selection of 3 urls, all of their IP addresses in turn, with IP4 and IP6 simultaneously. At most 5 of the DHCP DNS servers are used to resolve (in parallel). If an answer is gotten and it fails the probe stop, the probing continues if there is no connection or response 404.</p>
<dt><code>tcp80: </code>&lt;ip&gt;</p>
<dd>Add an IP4 or IP6 address to the list of fallback open DNSSEC resolvers that are used on TCP port 80.</p>
<dt><code>tcp443: </code>&lt;ip&gt;</p>
<dd>Add an IP4 or IP6 address to the list of fallback open DNSSEC resolvers that are used on TCP port 443.</p>
<dt><code>tcp443: </code>&lt;ip&gt; or &lt;ip&gt; { &lt;hash&gt;}</p>
<dd>Add an IP4 of IP6 address to the list of fallback SSL open DNSSEC resolvers. They serve plain-DNS(tcp-style) over port 443, encapsulated in SSL. The SSL certificate online is checked with the fingerprint (if configured here). You may configure multiple hashes (one space between), if one matches its OK, so that pre-publish rollover of the certificates is possible.</dl>
<h2>The Dnssec-Trigger-Panel</h2>
<p>The dnssec-trigger-panel is an applet that runs in the tray. It shows the DNSSEC status. It can be invoked with -d to test in the build directory. The -c <i>cfgfile</i> option can set the config file away from the default. The applet keeps an SSL connection to the daemon and displays the status, and can show the user dialogs. </p>
<p> The applet has a small menu. The menu item <code>Reprobe</code> causes the daemon to probe the last seen DHCP DNS servers again, which may now work after a hotspot signon. The menu item <code>Hotspot Signon</code> goes into insecure mode for hotspots where this must be used to sign on to the hot spot: use reprobe when done to resume dnssec protection efforts. The <code>Probe Result</code> menu item shows the results of the previous probe to the user, for technical help with network difficulties.</p>
<h2>The Dnssec-Trigger-Control Tool</h2>
<p>The dnssec-trigger-control tool can be used to test. It is also used inside DHCP scripts (platform specific). It can send commands to the daemon. </p>
<p> Options:</p>
<dl>
<dt><code>-c </code><i>cfgfile</i></p>
<dd>Set the config file to use away from the default.</p>
<dt><code>-s </code><i>ip[@port]</i></p>
<dd>Default connects to 127.0.0.1 with the port from config file, but this options overrides that with an IPv4 or IPv6 address and optional a port.</p>
<dt><code>-v</code></p>
<dd>increase verbosity of dnssec-trigger-control.</dl>
<p> Commands:</p>
<dl>
<dt><code>submit </code>&lt;ips&gt;</p>
<dd>Submit a list of space separated IP addresses (from DHCP) that are the DNS servers that the daemon will probe. IPv4 and IPv6 addresses can be used.</p>
<dt><code>unsafe</code></p>
<dd>Test command that probes some 127/8 addresses in a way that makes the daemon conclude that no DNSSEC works. Presents user with &#8216;Insecure?&#8217; dialog.</p>
<dt><code>status</code></p>
<dd>Shows the last probe results.</p>
<dt><code>reprobe</code></p>
<dd>Probe the last probe again. It also cancels forced insecure state from hotspot signon, causing probes for dnssec to resume. This command acts as the menu item with the same name.</p>
<dt><code>skip_http</code></p>
<dd>Skip the http probe step. Setup DNSSEC, as possible, without taking the result of the http probe into account. Once http works again, it&#8217;ll stop skipping the http results. Useful, if you want to have DNSSEC on a network where web access is not possible.</p>
<dt><code>hotspot_signon</code></p>
<dd>This command acts as the menu item with the same name. Use it to force insecure mode, where you can then interact with (weird) hotspot set ups. When you are done, do the reprobe command to resume DNSSEC protection efforts.</p>
<dt><code>results</code></p>
<dd>continuous feed of probe results.</p>
<dt><code>cmdtray</code></p>
<dd>Continuous input feed, used by the tray icon to send commands to the daemon.</p>
<dt><code>stoppanels</code></p>
<dd>Makes connected tray icons quit. Useful for installers that need to update their executable.</p>
<dt><code>stop</code></p>
<dd>stops the daemon.</dl>
<h2>The Dnssec-Trigger-Control-Setup Tool</h2>
<p>This tool aids setup of files. Without arguments it creates the key files. If key files already exist, it resigns certificates with existing private keys. With <code>-d</code> <i>dir</i> the files are placed in the given directory. </p>
<p> With <code>-i</code> the tool changes configuration files. It tests if unbound has <code>remote-control</code>: <code>control-enable:</code> <i>yes</i> and if not appends lines to unbound.conf that enable unbound-control, and it runs unbound-control-setup to generate the keys for unbound-control. It tests if unbound has a trust anchor, if not it enables the root.key as <code>auto-trust-anchor-file</code> and runs <i><a href="/docs/linux/man/8-unbound-anchor/">unbound-anchor</a></i>(8) to initialize the key. It picks up the domain and search from resolv.conf and configures the dnssec-trigger.conf to use that. </p>
<p> Note the tool trusts the domain and search path at install time. You should review them or perform configuration manually. </p>
<p> With <code>-u</code> it removes the options it enabled in <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5).</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/dnssec-trigger/dnssec-trigger.conf</i></p>
<dd>The default configuration file.</p>
<dt><i>/etc/dnssec-trigger</i></p>
<dd>Directory with keys used for SSL connections to dnssec-triggerd.</p>
<dt><i>/var/run/dnssec-trigger.pid</i></p>
<dd>Default pidfile with the pid of the running dnssec-triggerd.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-unbound/">unbound</a></i>(8), <i><a href="/docs/linux/man/8-unbound-control/">unbound-control</a></i>(8), <i><a href="/docs/linux/man/5-unbound-conf/">unbound.conf</a></i>(5), <i><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></i>(5).</p>
<h2>Authors</h2>
<p>This program was developed by Wouter Wijngaards at NLnet Labs.</p>
