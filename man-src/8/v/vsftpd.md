---
title: "vsftpd(8)"
name: "vsftpd"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vsftpd/"
description: "vsftpd – Very Secure FTP Daemon"
---

<p><code>vsftpd</code> &#8211; Very Secure FTP Daemon</p>
<h2>Synopsis</h2>
<p><code>vsftpd</code> [<i>configuration file and / or options</i> ]</p>
<h2>Description</h2>
<p><code>vsftpd</code> is the Very Secure File Transfer Protocol Daemon. The server can be launched via a &#8220;super-server&#8221; such as <a href="/docs/linux/man/8-inetd/">inetd</a>(8) or <a href="/docs/linux/man/8-xinetd/">xinetd</a>(8). Alternatively, vsftpd can be launched in standalone mode, in which case vsftpd itself will listen on the network. This latter mode is easier to use, and recommended. It is activated by setting listen=YES in /etc/vsftpd/vsftpd.conf Direct execution of the <code>vsftpd</code> binary will then launch the FTP service ready for immediate client connections. </p>
<p> Systemd changes the vsftpd daemon start-up. The vsftpd package contains vsftpd-generator script generating symbolic links to /var/run/systemd/generator/vsftpd.target.wants directory. The generator is called during e.g. &#8216;systemctl &#8211;system daemon-reload&#8217;. All these symbolic links link /usr/lib/systemd/system/vsftpd [at] .service file. The vsftpd daemon(s) is/are controlled by one of following ways: </p>
<p> 1. Single daemon using default /etc/vsftpd/vsftpd.conf configuration file<br />
 # systemctl {start,stop,&#8230;} vsftpd[.service] </p>
<p> 2. Single daemon using /etc/vsftpd/&lt;conf-name&gt;.conf<br />
 # systemctl {start,stop,&#8230;} vsftpd@&lt;conf-name&gt;[.service] </p>
<p> 3. All instances together<br />
 # systemctl {restart,stop} vsftpd.target </p>
<p> See <a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a>(5), <a href="/docs/linux/man/5-systemd-target/">systemd.target</a>(5) for further details.</p>
<h2>Options</h2>
<p>An optional configuration file or files may be given on the command line. These files must be owned as root if running as root. Any command line option not starting with a &quot;-&quot; character is treated as a config file that will be loaded. Note that config files are loaded in the strict order that they are encountered on the command line. If no config files are specified, the default configuration file of /etc/vsftpd/vsftpd.conf will be loaded, after all other command line options are processed. </p>
<p> Supported options are:</p>
<dl>
<dt><code>-v</code></p>
<dd>Print the version information and exit, even if other options are encountered.</p>
<dt><code>-ooption=value</code></p>
<dd>Set a single option, value pair as per the format in the config file. Multiple -o options are supported, and they are applied in strict order relative to their appearance on the command line, including intermingling with loading of config files.</dl>
<h2>Examples</h2>
<p>vsftpd -olisten=NO /etc/vsftpd/vsftpd.conf -oftpd_banner=blah </p>
<p> That example overrides vsftpd&#8217;s built-in default for the &quot;listen&quot; option to be NO, but then loads /etc/vsftpd/vsftpd.conf which may override that setting. Finally, the &quot;ftpd_banner&quot; setting is set to &quot;blah&quot;, which overrides any default vsftpd setting and any identical setting that was in the config file.</p>
<h2>Files</h2>
<p>/etc/vsftpd/vsftpd.conf </p>
<p> /usr/lib/systemd/system/vsftpd.service </p>
<p> /usr/lib/systemd/system/vsftpd [at] .service </p>
<p> /usr/lib/systemd/system/vsftpd.target</p>
<h2>See Also</h2>
<p>vsftpd.conf5 systemd.unit5 </p>
