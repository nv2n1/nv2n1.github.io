---
title: "pure-ftpd(8)"
name: "pure-ftpd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pure-ftpd/"
description: "pure-ftpd – simple File Transfer Protocol server"
---

<p>pure-ftpd &#8211; simple File Transfer Protocol server </p>
<h2>Synopsis</h2>
<p><code>pure-ftpd [-0] [-1] [-2] [-4] [-6] [-a gid] [-A] [-b] [-B] [-c clients] [-C cnx/ip] [-d [-d]] [-D] [-e] [-E] [-f facility] [-F fortunes file] [-g pidfile] [-G] [-H] [-i] [-I] [-j] [-J ciphers] [-k percentage] [-K] [-l authentication[:config file]] [-L max files:max depth] [-m maxload] [-M] [-n maxfiles:maxsize] [-N] [-o] [-O format:log file] [-p first:last] [-P ip address or host name] [-q upload:download ratio] [-Q upload:download ratio] [-r] [-R] [-s] [-S [address,][port]] [-t upload bandwidth:download bandwidth] [-T upload bandwidth:download bandwidth] [-u uid] [-U umask files:umask dirs] [-v bonjour name] [-V ip address] [-w] [-W] [-x] [-X] [-y max user sessions:max anon sessions] [-Y tls behavior] [-z] [-Z]</code><br />
 Alternative style :<br />
 -0 &#8211;notruncate<br />
 -1 &#8211;logpid<br />
 -2 &#8211;certfile<br />
 -4 &#8211;ipv4only<br />
 -6 &#8211;ipv6only<br />
 -a &#8211;trustedgid<br />
 -A &#8211;chrooteveryone<br />
 -b &#8211;brokenclientscompatibility<br />
 -B &#8211;daemonize<br />
 -c &#8211;maxclientsnumber<br />
 -C &#8211;maxclientsperip<br />
 -d &#8211;verboselog<br />
 -D &#8211;displaydotfiles<br />
 -e &#8211;anonymousonly<br />
 -E &#8211;noanonymous<br />
 -f &#8211;syslogfacility<br />
 -F &#8211;fortunesfile<br />
 -g &#8211;pidfile<br />
 -G &#8211;norename<br />
 -h &#8211;help<br />
 -H &#8211;dontresolve<br />
 -i &#8211;anonymouscantupload<br />
 -I &#8211;maxidletime<br />
 -j &#8211;createhomedir<br />
 -J &#8211;tlsciphersuite<br />
 -k &#8211;maxdiskusagepct<br />
 -K &#8211;keepallfiles<br />
 -l &#8211;login<br />
 -L &#8211;limitrecursion<br />
 -m &#8211;maxload<br />
 -M &#8211;anonymouscancreatedirs<br />
 -n &#8211;quota<br />
 -N &#8211;natmode<br />
 -o &#8211;uploadscript<br />
 -O &#8211;altlog<br />
 -p &#8211;passiveportrange<br />
 -P &#8211;forcepassiveip<br />
 -q &#8211;anonymousratio<br />
 -Q &#8211;userratio<br />
 -r &#8211;autorename<br />
 -R &#8211;nochmod<br />
 -s &#8211;antiwarez<br />
 -S &#8211;bind<br />
 -t &#8211;anonymousbandwidth<br />
 -T &#8211;userbandwidth<br />
 -u &#8211;minuid<br />
 -U &#8211;umask<br />
 -v &#8211;bonjour<br />
 -V &#8211;trustedip<br />
 -w &#8211;allowuserfxp<br />
 -W &#8211;allowanonymousfxp<br />
 -x &#8211;prohibitdotfileswrite<br />
 -X &#8211;prohibitdotfilesread<br />
 -y &#8211;peruserlimits<br />
 -Y &#8211;tls<br />
 -z &#8211;allowdotfiles<br />
 -Z &#8211;customerproof </p>
<h2>Description</h2>
<p><code>Pure-FTPd</code> is a small, simple server for the old and hairy File Transfer Protocol, designed to use less resources than older servers, be smaller and very secure, and to never execute any external program. It support most-used features and commands of FTP (including many modern extensions), and leaves out everything which is deprecated, meaningless, insecure, or correlates with trouble. IPv6 is fully supported. </p>
<h2>Options</h2>
<dl>
<dt><code>-0</code></p>
<dd>When a file is uploaded and there is already a previous version of the file with the same name, the old file will neither get removed nor truncated. Upload will take place in a temporary file and once the upload is complete, the switch to the new version will be atomic. This option should not be used together with virtual quotas.</p>
<dt><code>-1</code></p>
<dd>Add the PID to the syslog output. Ignored if <code>-f</code> <code>none</code> is set.</p>
<dt><code>-2 file</code></p>
<dd>When using TLS, set the path to the certificate file.</p>
<dt><code>-4</code></p>
<dd>Listen only to IPv4 connections.</p>
<dt><code>-6</code></p>
<dd>Listen only to IPv6 connections.</p>
<dt><code>-a gid</code></p>
<dd>Regular users will be chrooted to their home directories, unless they belong to the specified gid. Note that root is always trusted, and that chroot() occurs only for anonymous ftp without this option.</p>
<dt><code>-A</code></p>
<dd>Chroot() everyone, but root.</p>
<dt><code>-b</code></p>
<dd>Be broken. Turns on some compatibility hacks for shoddy clients, and for broken Netfilter gateways.</p>
<dt><code>-B</code></p>
<dd>Start the standalone server in background (daemonize).</p>
<dt><code>-c clients</code></p>
<dd>Allow a maximum of <i>clients</i> to be connected. <i>clients</i> must be at least 1, and if you combine it with <code>-p</code> it will be forced down to half the number of ports specified by <code>-p.</code> If more than <i>clients</i> are connected, new clients are rejected at once, even clients wishing to upload, or to log in as normal users. Therefore, it is advisable to use <code>-m</code> as primary overload protection. The default value is 50.</p>
<dt><code>-C max connection per ip</code></p>
<dd>Limit the number of simultanous connections coming from the same IP address. This is yet another very effective way to prevent stupid denial of services and bandwidth starvation by a single user. It works only when the server is launched in standalone mode (if you use a super-server, it is supposed to do that). If the server is launched with <code>-C 2</code> , it doesn&#8217;t mean that the total number of connection is limited to 2. But the same client, coming from the same machine (or at least the same IP), can&#8217;t have more than two simultaneous connections. This features needs some memory to track IP addresses, but it&#8217;s recommended to use it.</p>
<dt><code>-d</code></p>
<dd>turns on debug logging. Every command is logged, except that the argument to PASS is changed to &quot;&lt;password&gt;&quot;. If you repeat <code>-d</code> , responses too are logged.</p>
<dt><code>-e</code></p>
<dd>Only allow anonymous users to log in.</p>
<dt><code>-E</code></p>
<dd>Only allow authenticated login. Anonymous users are prohibited.</p>
<dt><code>-f facility</code></p>
<dd>makes ftpd use <i>facility</i> for all <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) messages. <i>facility</i> defaults to <code>ftp</code>. The facility names are normally listed in <i>/usr/include/sys/syslog.h</i>. Note that if <code>-f</code> is not the first option on the command line, a couple of messages may be logged to local2 before the <code>-f</code> option is parsed. Use <code>-f none</code> to disable logging.</p>
<dt><code>-F fortunes file</code></p>
<dd>Display a funny random message in the initial login banner. The random cookies are extracted from a text file, in the standard <code>fortune</code> format. If you installed the <code>fortune</code> package, you should have a directory (usually <code>/usr/share/fortune</code> ) with binary files ( <code>xxxx.dat</code> ) and text files (without the <code>.dat</code> extension).</p>
<dt><code>-g pidfile</code></p>
<dd>In standalone mode, write the pid to that file in instead of /var/run/pure-ftpd.pid .</p>
<dt><code>-G</code></p>
<dd>When this option is enabled, people can no more change the name of already uploaded files, even if they own those files or their directory.</p>
<dt><code>-H</code></p>
<dd>Don&#8217;t resolve host names (&quot;192.0.34.166&quot; will be logged instead of &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>&quot;). It can significantly speed up connections and reduce bandwidth usage on busy servers. Use it especially on public FTP sites.</p>
<dt><code>-i</code></p>
<dd>Disallow upload for anonymous users, whatever directory permissions are. This option is especially useful for virtual hosting, to avoid your users create warez sites in their account.</p>
<dt><code>-I timeout</code></p>
<dd>Change the maximum idle time. The timeout is in minutes, and defaults to 15.</p>
<dt><code>-j</code></p>
<dd>If the home directory of a user doesn&#8217;t exist, automatically create it. The newly created home directory belongs to the user, and permissions are set according to the current directory mask. To avoid local attacks, the parent directory should never belong to an untrusted user.</p>
<dt><code>-J ciphers</code></p>
<dd>Set the list of ciphers that will be accepted for SSL/TLS connections.</p>
<dt><code>-k percentage</code></p>
<dd>Disallow upload if the partition is more than <code>percentage</code> full. Example: -k 95 will ensure that your disk will never get filled more than 95% by FTP users.</p>
<dt><code>-K</code></p>
<dd>Allow users to resume and upload files, but NOT to delete them. Directories can be removed, but only if they are empty.</p>
<dt><code>-l authentication:file</code></p>
<dd>Enable a new authentication method. It can be one of : <i>-l unix</i> For standard (/etc/passwd) authentication. <i>-l pam</i> For PAM authentication. <i>-l ldap:LDAP config file</i> For LDAP directories. <i>-l mysql:MySQL config file</i> For MySQL databases. <i>-l pgsql:Postgres config file</i> For Postgres databases. <i>-l puredb:PureDB database file</i> For PureDB databases. <i>-l extauth:path to pure-authd socket</i> For external authentication handlers.<br />
 Different authentication methods can be mixed together. For instance if you run the server with <i>-lpuredb:/etc/pure-ftpd/pwd.pdb -lmysql:/etc/pure-ftpd/my.cf -lunix</i> Accounts will first be authenticated from a PureDB database. If it fails, a MySQL server will be asked. If the account is still not found is the database, standard unix accounts will be scanned. Authentication methods are tried in the order you give the -l options, if you do not give -l, then the decision comes from configure, if PAM is built in, it is used, if not, then UNIX (/etc/passwd) is used by default.<br />
 See the <i>README.LDAP</i> and <i>README.MySQL</i> files for info about the built-in LDAP and SQL directory support.</p>
<dt><code>-L max files:max depth</code></p>
<dd>Avoid denial-of-service attacks by limiting the number of displayed files in a &#8216;ls&#8217; and the maximum depth of a recursive &#8216;ls&#8217;. Defaults are 2000:5 (2000 files displayed for a single &#8216;ls&#8217; and walk through 5 subdirectories max).</p>
<dt><code>-m load</code></p>
<dd>Do not allow anonymous users to download files if the load is above <i>load</i> when the user connects. Uploads and file listings are still allowed, as are downloads by real users. The user is not told about this until he/she tries to download a file.</p>
<dt><code>-M</code></p>
<dd>Allow anonymous users to create directories.</p>
<dt><code>-n maxfiles:maxsize</code></p>
<dd>Enable <code>virtual quotas</code> When virtual quotas are enabled, .ftpquota files are created, and the number of files for a user is restricted to &#8216;maxfiles&#8217;. The max total size of his directory is also restricted to &#8216;maxsize&#8217; Megabytes. Members of the trusted group aren&#8217;t subject to quotas.</p>
<dt><code>-N</code></p>
<dd>NAT mode. Force <code>active</code> mode. If your FTP server is behind a NAT box that doesn&#8217;t support applicative FTP proxying, or if you use port redirection without a transparent FTP proxy, use this. Well&#8230; the previous sentence isn&#8217;t very clear. Okay: if your network looks like this:<br />
 FTP&#8211;NAT.gateway/router&#8211;Internet<br />
 and if you want people coming from the internet to have access to your FTP server, please try without this option first. If Netscape clients can connect without any problem, your NAT gateway rulez. If Netscape doesn&#8217;t display directory listings, your NAT gateway sucks. Use <code>-N</code> as a workaround.</p>
<dt><code>-o</code></p>
<dd>Enable <i>pure-uploadscript</i>.</p>
<dt><code>-O format:log file</code></p>
<dd>Record all file transfers into a specific log file, in an alternative format. Currently, three formats are supported : CLF, Stats, W3C and xferlog.<br />
 If you add<br />
 <code>-O clf:/var/log/pureftpd.log</code><br />
 to your starting options, Pure-FTPd will log transfers in <code>/var/log/pureftpd.log</code> in a format similar to the Apache web server in default configuration.<br />
 If you add<br />
 <code>-O stats:/var/log/pureftpd.log</code><br />
 to your starting options, Pure-FTPd will create accurate log files designed for traffic analys software like ftpStats.<br />
 If you add<br />
 <code>-O w3c:/var/log/pureftpd.log</code><br />
 to your starting options, Pure-FTPd will create W3C-conformant log files.<br />
 For security purposes, the path must be absolute (eg. <code>/var/log/pureftpd.log</code>, not <code> ../log/pureftpd.log</code>).</p>
<dt><code>-p first:last</code></p>
<dd>Use only ports in the range <i>first</i> to <i>last</i> inclusive for passive-mode downloads. This means that clients will not try to open connections to TCP ports outside the range <i>first &#8211; last</i>, which makes pure-ftpd more compatible with packet filters. Note that the maximum number of clients (specified with <code>-c</code>) is forced down to <i>(last + 1 &#8211; first)/2</i> if it is greater, as the default is. (The syntax for the port range is, conveniently, the same as that of <code>iptables).</code></p>
<dt><code>-P ip address or host name</code></p>
<dd>Force the specified IP address in reply to a <code>PASV/EPSV/SPSV</code> command. If the server is behind a masquerading (NAT) box that doesn&#8217;t properly handle stateful FTP masquerading, put the ip address of that box here. If you have a dynamic IP address, you can use a symbolic host name (probably the one of your gateway), that will be resolved every time a new client will connect.</p>
<dt><code>-q upload:download</code></p>
<dd>Enable an upload/download ratio for anonymous users (ex: <i>-q 1:5</i> means that 1 Mb of goodies have to be uploaded to leech 5 Mb).</p>
<dt><code>-Q upload:download</code></p>
<dd>Enable ratios for anonymous and non-anonymous users. If the <i>-a</i> option is also used, users from the trusted group have no ratio.</p>
<dt><code>-r</code></p>
<dd>Never overwrite existing files. Uploading a file whose name already exists cause an automatic rename. Files are called xyz.1, xyz.2, xyz.3, etc.</p>
<dt><code>-R</code></p>
<dd>Disallow users (even non-anonymous ones) usage of the CHMOD command. On hosting services, it may prevent newbies from doing mistakes, like setting bad permissions on their home directory. Only root can use CHMOD when this switch is enabled.</p>
<dt><code>-s</code></p>
<dd>Don&#8217;t allow anonymous users to retrieve files owned by &quot;ftp&quot; (generally, files uploaded by other anonymous users).</p>
<dt><code>-S [{ip address|hostname}] [,{port|service name}]</code></p>
<dd>This option is only effective when the server is launched as a standalone server. Connections are accepted on the specified IP and port. IPv4 and IPv6 are supported. Numeric and fully-qualified host names are accepted. A service name (see /etc/services) can be used instead of a numeric port number.</p>
<dt><code>-t bandwidth</code></p>
<dd>or <code>-t upload bandwidth:download bandwidth</code> Enable process priority lowering and bandwidth throttling for anonymous users. Delay should be in kilobytes/seconds.</p>
<dt><code>-T bandwidth</code></p>
<dd>or <code>-T upload bandwidth:download bandwidth</code> Enable process priority lowering and bandwidth throttling for *ALL* users. Pure-FTPd should have been explicitely compiled with throttling support to have these flags work. It is possible to have different bandwidth limits for uploads and for downloads. &#8216;-t&#8217; and &#8216;-T&#8217; can indeed be followed by two numbers delimited by a column (&#8216;:&#8217;). The first number is the upload bandwidth and the next one applies only to downloads. One of them can be left blank which means infinity. A single number without any column means that the same limit applies to upload and download.</p>
<dt><code>-u uid</code></p>
<dd>Do not allow uids below <i>uid</i> to log in (typically, low-numbered <i>uid</i>s are used for administrative accounts). <code>-u 100</code> is sufficient to deny access to all administrative accounts on many linux boxes, where 99 is the last administrative account. Anonymous FTP is allowed even if the uid of the ftp user is smaller than <i>uid</i>. <code>-u 1</code> denies access only to root accounts. The default is to allow FTP access to all accounts.</p>
<dt><code>-U umask files:umask dirs</code></p>
<dd>Change the mask for creation of new files and directories. The default are 133 (files are readable -but not writable- by other users) and 022 (same thing for directory, with the execute bit on). If new files should only be readable by the user, use 177:077. If you want uploaded files to be executable, use 022:022 (files will be readable by other people) or 077:077 (files will only be readable by their owner).</p>
<dt><code>-v bonjour name</code></p>
<dd>Set the Bonjour name of the service (only available on MacOS X when Bonjour support is compiled in).</p>
<dt><code>-V ip address</code></p>
<dd>Allow non-anonymous FTP access only on this specific local IP address. All other IP addresses are only anonymous. With that option, you can have routed IPs for public access, and a local IP (like 10.x.x.x) for administration. You can also have a routable trusted IP protected by firewall rules, and only that IP can be used to login as a non-anonymous user.</p>
<dt><code>-w</code></p>
<dd>Enable support for the FXP protocol, for non-anonymous users only.</p>
<dt><code>-W</code></p>
<dd>Enable the FXP protocol for everyone. <i>FXP IS AN UNSECURE PROTOCOL. NEVER ENABLE IT ON UNTRUSTED NETWORKS.</i></p>
<dt><code>-x</code></p>
<dd>In normal operation mode, authenticated users can read/write files beginning with a dot (&#8216;.&#8217;). Anonymous users can&#8217;t, for security reasons (like changing banners or a forgotten .rhosts). When &#8216;-x&#8217; is used, authenticated users can download dot-files, but not overwrite/create them, even if they own them. That way, you can prevent hosted users from messing .qmail files.</p>
<dt><code>-X</code></p>
<dd>This flag is identical to the previous one (writing dot-files is prohibited), but in addition, users can&#8217;t even *read* files and directories beginning with a dot (like &quot;cd .ssh&quot;).</p>
<dt><code>-y per user max sessions:max anonymous sessions</code></p>
<dd>This switch enables per-user concurrency limits. Two values are separated by a column. The first one is the max number of concurrent sessions for a single login. The second one is the maximum number of anonoymous sessions.</p>
<dt><code>-Y tls behavior</code></p>
<dd><code>-Y 0</code> (default) disables SSL/TLS security mechanisms.<br />
 <code>-Y 1</code> Accept both normal sessions and SSL/TLS ones.<br />
 <code>-Y 2</code> refuses connections that aren&#8217;t using SSL/TLS security mechanisms, including anonymous ones.<br />
 <code>-Y 3</code> refuses connections that aren&#8217;t using SSL/TLS security mechanisms, and refuse cleartext data channels as well.<br />
 The server must have been compiled with SSL/TLS support and a valid certificate must be in place to accept encrypted sessions.</p>
<dt><code>-z</code></p>
<dd>Allow anonymous users to read files and directories starting with a dot (&#8216;.&#8217;).</p>
<dt><code>-Z</code></p>
<dd>Add safe guards against common customer mistakes (like chmod 0 on their own files) . </p>
</dl>
<h2>Authentication</h2>
<p>Some of the complexities of older servers are left out. </p>
<p> This version of pure-ftpd can use PAM for authentication. If you wan&#8217;t it to consult any files like /etc/shells or /etc/ftpd/ftpusers consult pam docs. LDAP directories and SQL databases are also supported. </p>
<p> Anonymous users are authenticated in any of three ways: </p>
<p> 1. The user logs in as &quot;ftp&quot; or &quot;anonymous&quot; and there is an account called &quot;ftp&quot; with an existing home directory. This server does not ask anonymous users for an email address or other password. </p>
<p> 2. The user connects to an IP address which resolves to the name of a directory in <i>/etc/pure-ftpd/pure-ftpd</i> (or a symlink in that directory to a real directory), and there is an account called &quot;ftp&quot; (which does not need to have a valid home directory). See <code>Virtual Servers</code> below. </p>
<p> <code>Ftpd</code> does a <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) to the relevant base directory when an anonymous user logs in. </p>
<p> Note that <code>ftpd</code> allows remote users to log in as root if the password is known and -u not used.</p>
<h2>Unusual Features</h2>
<p>If a user&#8217;s home directory is <code>/path/to/home/./</code>, FTP sessions under that UID will be chroot()ed. In addition, if a users&#8217;s home directory is <code>/path/to/home/./directory</code> the session will be chroot()ed to /path/to/home and the FTP session will start in &#8216;directory&#8217;. </p>
<p> As noted above, this <code>pure-ftpd</code> omits several features that are required by the RFC or might be considered useful at first. Here is a list of the most important omissions. </p>
<p> On-the-fly tar is not supported, for several reasons. I feel that users who want to get many files should use a special FTP client such as &quot;mirror,&quot; which also supports incremental fetch. I don&#8217;t want to either add several hundred lines of code to create tar files or execute an external tar. Finally, on-the-fly tar distorts log files. </p>
<p> On-the-fly compression is left out too. Most files on an FTP site are compressed already, and if a file isn&#8217;t, there presumably is a reason why. (As for decompression: Don&#8217;t FTP users waste bandwidth enough without help from on-the-fly decompression?)</p>
<h2>Directory Aliases</h2>
<p>Shortcuts for the &quot;cd&quot; command can be set up if the server has been compiled with the &#8211;with-diraliases feature. </p>
<p> To enable directory aliases, create a file called <i>/etc/pure-ftpd/pureftpd-dir-aliases</i> and alternate lines of alias names and associated directories.</p>
<h2>Anonymous Ftp</h2>
<p>This server leaves out some of the commands and features that have been used to subvert anonymous FTP servers in the past, but still you have to be a little bit careful in order to support anonymous FTP without risk to the rest of your files. </p>
<p> Make <i>~ftp</i> and all files and directories below this directory owned by some user other than &quot;ftp,&quot; and only the <i>&#8230;/incoming</i> directory/directories writable by &quot;ftp.&quot; It is probably best if all directories are writable only by a special group such as &quot;ftpadmin&quot; and &quot;ftp&quot; is not a member of this group. </p>
<p> If you do not trust the local users, put <i>~ftp</i> on a separate partition, so local users can&#8217;t hard-link unapproved files into the anonymous FTP area. </p>
<p> Use of the <code>-s</code> option is strongly suggested. (Simply add &quot;-s&quot; to the end of the <code>ftpd</code> line in <i>/etc/inetd.conf</i> to enable it.) </p>
<p> Most other FTP servers require that a number of files such as <i>~ftp/bin/ls</i> exist. This server does not require that any files or directories within <i>~/ftp</i> whatsoever exist, and I recommend that all such unnecessary files are removed (for no real reason). </p>
<p> It may be worth considering to run the anonymous FTP service as a virtual server, to get automatic logins and to firewall off the FTP address/port to which real users can log in. </p>
<p> If your server is a public FTP site, you may want to allow only &#8216;ftp&#8217; and &#8216;anonymous&#8217; users to log in. Use the <code>-e</code> option for this. Real accounts will be ignored and you will get a secure, anonymous-only FTP server.</p>
<h2>Magic Files</h2>
<p>The files <i>&lt;ftproot&gt;/.banner</i> and <i>.message</i> are magical. </p>
<p> If there is a file called <i>.banner</i> in the root directory of the anonymous FTP area, or in the root directory of a virtual host, and it is shorter than 1024 bytes, it is printed upon login. (If the client does not log in explicitly, and an implicit login is triggered by a CWD or CDUP command, the banner is not printed. This is regrettable but hard to avoid.) </p>
<p> If there is a file called <i>.message</i> in any directory and it is shorter than 1024 bytes, that file is printed whenever a user enters that directory using CWD or CDUP.</p>
<h2>Virtual Servers</h2>
<p>You can run several different anonymous FTP servers on one host, by giving the host several IP addresses with different DNS names. </p>
<p> Here are the steps needed to create an extra server using an IP alias on linux 2.4.x, called &quot;<a href="ftp://ftp.example.com">ftp.example.com</a>&quot; on address 10.11.12.13. on the IP alias eth0. </p>
<p> 1. Create an &quot;ftp&quot; account if you do not have one. It it best if the account does not have a valid home directory and shell. I prefer to make <i>/dev/null</i> the ftp account&#8217;s home directory and shell. <code>Ftpd</code> uses this account to set the anonymous users&#8217; uid. </p>
<p> 2. Create a directory as described in <code>Anonymous FTP</code> and make a symlink called <i>/etc/pure-ftpd/pure-ftpd/10.11.12.13</i> which points to this directory. </p>
<p> 3. Make sure your kernel has support for IP aliases. </p>
<p> 4. Make sure that the following commands are run at boot: </p>
<p> /sbin/ifconfig eth0:1 10.11.12.13 </p>
<p> That should be all. If you have problems, here are some things to try. </p>
<p> First, symlink <i>/etc/pure-ftpd/pure-ftpd/127.0.0.1</i> to some directory and say &quot;ftp localhost&quot;. If that doesn&#8217;t log you in, the problem is with <code>ftpd.</code> </p>
<p> If not, &quot;ping -v 10.11.12.13&quot; and/or &quot;ping -v <a href="ftp://ftp.example.com">ftp.example.com</a>&quot; from the same host. If this does not work, the problem is with the IP alias. </p>
<p> Next, try &quot;ping -v 10.11.12.13&quot; from a host on the local ethernet, and afterwards &quot;/sbin/arp -a&quot;. If 10.11.12.13 is listed among the ARP entries with the correct hardware address, the problem is probably with the IP alias. If 10.11.12.13 is listed, but has hardware address 0:0:0:0:0:0, then proxy-ARP isn&#8217;t working. </p>
<p> If none of that helps, I&#8217;m stumped. Good luck. </p>
<p> <code>Warning:</code> If you setup a virtual hosts, normal users will not be able to login via this name, so <code>don&#8217;t</code> create link/directory in <i>/etc/pure-ftpd/pure-ftpd</i> for your regular hostname.</p>
<h2>Files</h2>
<p><i>/etc/passwd</i> is used via libc (and PAM is this case), to get the uid and home directory of normal users, the uid and home directory of &quot;ftp&quot; for normal anonymous ftp, and just the uid of &quot;ftp&quot; for virtual ftp hosts. </p>
<p> <i>/etc/shadow</i> is used like <i>/etc/passwd</i> if shadow support is enabled. </p>
<p> <i>/etc/group</i> is used via libc, to get the group membership of normal users. </p>
<p> <i>/proc/net/tcp</i> is used to count existing FTP connections, if the <code>-c</code> or <code>-p</code> options are used </p>
<p> <i>/etc/pure-ftpd/pure-ftpd/&lt;ip address&gt;</i> is the base directory for the &lt;ip address&gt; virtual ftp server, or a symbolic link to its base directory. <code>Ftpd</code> does a <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) into this directory when a user logs in to &lt;ip address&gt;, thus symlinks outside this directory will not work. </p>
<p> <i>~ftp</i> is the base directory for &quot;normal&quot; anonymous FTP. <code>Ftpd</code> does a <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) into this directory when an anonymous user logs in, thus symlinks outside this directory will not work.</p>
<h2>Ls</h2>
<p>The behaviour of LIST and NLST is a tricky issue. Few servers send RFC-compliant responses to LIST, and some clients depend on non-compliant responses. </p>
<p> This server uses <code><a href="/docs/linux/man/3-glob/">glob</a></code>(3) to do filename globbing. </p>
<p> The response to NLST is by default similar to that of <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), and that to LIST is by default similar to that of <code>ls -l</code> or <code>ls -lg</code> on most Unix systems, except that the &quot;total&quot; count is meaningless. Only regular files, directories and symlinks are shown. Only important <code>ls</code> options are supported:</p>
<dl>
<dt><code>-1</code></p>
<dd>Undoes <code>-l</code> and <code>-C</code>.</p>
<dt><code>-a</code></p>
<dd>lists even files/directories whose names begin with &quot;.&quot;.</p>
<dt><code>-C</code></p>
<dd>lists files in as many colums as will fit on the screen. Undoes <code>-1</code> and <code>-l</code>.</p>
<dt><code>-d</code></p>
<dd>lists argument directories&#8217; names rather their contents.</p>
<dt><code>-D</code></p>
<dd>List files beginning with a dot (&#8216;.&#8217;) even when the client doesn&#8217;t append the <code>-a</code> option to the <code>list</code> command.</p>
<dt><code>-F</code></p>
<dd>appends &#8216;*&#8217; to executable regular files, &#8216;@&#8217; to symlinks and &#8216;/&#8217; to directories.</p>
<dt><code>-l</code></p>
<dd>shows various details about the file, including file group. See <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) for details. Undoes <code>-1</code> and <code>-C</code>.</p>
<dt><code>-r</code></p>
<dd>reverses the sorting order (modifies <code>-S</code> and <code>-t</code> and the default alphabetical ordering).</p>
<dt><code>-R</code></p>
<dd>recursively descends into subdirectories of the argument directories.</p>
<dt><code>-S</code></p>
<dd>Sorts by file size instead of by name. Undoes <code>-t</code>.</p>
<dt><code>-t</code></p>
<dd>Sorts by file modification time instead of by name. Undoes <code>-S</code>. </p>
</dl>
<h2>Protocol</h2>
<p>Here are the FTP commands supported by this server.<br />
 <code>ABOR</code> <code>ALLO</code> <code>APPE</code> <code>AUTH TLS</code> <code>CCC</code> <code>CDUP</code> <code>CWD</code> <code>DELE</code> <code>EPRT</code> <code>EPSV</code> <code>ESTA</code> <code>ESTP</code> <code>FEAT</code> <code>HELP</code> <code>LIST</code> <code>MDTM</code> <code>MFMT</code> <code>MKD</code> <code>MLSD</code> <code>MLST</code> <code>MODE</code> <code>NLST</code> <code>NOOP</code> <code>PASS</code> <code>PASV</code> <code>PBSZ</code> <code>PORT</code> <code>PROT</code> <code>PWD</code> <code>QUIT</code> <code>REST</code> <code>RETR</code> <code>RMD</code> <code>RNFR</code> <code>RNTO</code> <code>SIZE</code> <code>SPSV</code> <code>STAT</code> <code>STOR</code> <code>STOU</code> <code>STRU</code> <code>SYST</code> <code>TYPE</code> <code>USER</code> <code>XCUP</code> <code>XCWD</code> <code>XDBG</code> <code>XMKD</code> <code>XPWD</code> <code>XRMD</code> <code>OPTS MLST</code> <code>OPTS UTF8</code> <code>SITE CHMOD</code> <code>SITE HELP</code> <code>SITE IDLE</code> <code>SITE TIME</code> <code>SITE UTIME</code></p>
<h2>Bugs</h2>
<p>Please report bugs to the mailing-list (see below). Pure-FTPd looks very stable and is used on production servers. However it comes with no warranty and it can have nasty bugs or security flaws. </p>
<h2>Home Page</h2>
<p><a rel="nofollow" href="http://www.pureftpd.org/">http://www.pureftpd.org/</a></p>
<h2>New Versions</h2>
<p>See the mailing-list on <code><a rel="nofollow" href="http://www.pureftpd.org/ml/">http://www.pureftpd.org/ml/</a></code>.</p>
<h2>Author And License</h2>
<p>Troll-FTPd was written by Arnt Gulbrandsen &lt;agulbra [at] troll.no&gt; and copyright 1995-2002 Troll Tech AS, Waldemar Thranes gate 98B, N-0175 Oslo, Norway, fax +47 22806380. </p>
<p> Pure-FTPd is (C)opyleft 2001-2015 by Frank DENIS &lt;j at pureftpd dot org&gt; and the Pure-FTPd team. </p>
<p> This software is covered by the BSD license. </p>
<p> Contributors: </p>
<p>&nbsp;<wbr>Arnt Gulbrandsen,<br />
&nbsp;<wbr>Troll Tech AS,<br />
&nbsp;<wbr>Janos Farkas,<br />
&nbsp;<wbr>August Fullford,<br />
&nbsp;<wbr>Ximenes Zalteca,<br />
&nbsp;<wbr>Patrick Michael Kane,<br />
&nbsp;<wbr>Arkadiusz Miskiewicz,<br />
&nbsp;<wbr>Michael K. Johnson,<br />
&nbsp;<wbr>Kelley Lingerfelt,<br />
&nbsp;<wbr>Sebastian Andersson,<br />
&nbsp;<wbr>Andreas Westin,<br />
&nbsp;<wbr>Jason Lunz,<br />
&nbsp;<wbr>Mathias Gumz,<br />
&nbsp;<wbr>Claudiu Costin,<br />
&nbsp;<wbr>Ping,<br />
&nbsp;<wbr>Paul Lasarev,<br />
&nbsp;<wbr>Jean-Mathieux Schaffhauser,<br />
&nbsp;<wbr>Emmanuel Hocdet,<br />
&nbsp;<wbr>Sami Koskinen,<br />
&nbsp;<wbr>Sami Farin,<br />
&nbsp;<wbr>Luis Llorente Campo,<br />
&nbsp;<wbr>Peter Pentchev,<br />
&nbsp;<wbr>Darren Casey,<br />
&nbsp;<wbr>The Regents of the University of California,<br />
&nbsp;<wbr>Theo de Raadt&nbsp;<wbr>(OpenBSD),<br />
&nbsp;<wbr>Matthias Andree,<br />
&nbsp;<wbr>Isak Lyberth,<br />
&nbsp;<wbr>Steve Reid,<br />
&nbsp;<wbr>RSA Data Security Inc,<br />
&nbsp;<wbr>Trilucid,<br />
&nbsp;<wbr>Dmtry Lebkov,<br />
&nbsp;<wbr>Johan Huisman,<br />
&nbsp;<wbr>Thorsten Kukuk,<br />
&nbsp;<wbr>Jan van Veen,<br />
&nbsp;<wbr>Roger Constantin Demetrescu,<br />
&nbsp;<wbr>Stefano F.,<br />
&nbsp;<wbr>Robert Varga,<br />
&nbsp;<wbr>Freeman,<br />
&nbsp;<wbr>James Metcalf,<br />
&nbsp;<wbr>Im Eunjea,<br />
&nbsp;<wbr>Philip Gladstone,<br />
&nbsp;<wbr>Kenneth Stailey,<br />
&nbsp;<wbr>Brad Smith,<br />
&nbsp;<wbr>Ulrik Sartipy,&nbsp;<wbr><br />
&nbsp;<wbr>Cindy Marasco,<br />
&nbsp;<wbr>Nicolas Doye,<br />
&nbsp;<wbr>Thomas Briggs,<br />
&nbsp;<wbr>Stanton Gallegos,<br />
&nbsp;<wbr>Florin Andrei,<br />
&nbsp;<wbr>Chan Wilson,<br />
&nbsp;<wbr>Bjoern Metzdorf,<br />
&nbsp;<wbr>Ben Gertzfield,<br />
&nbsp;<wbr>Akhilesch Mritunjai,<br />
&nbsp;<wbr>Dawid Szymanski,<br />
&nbsp;<wbr>Kurt Inge Smadal,<br />
&nbsp;<wbr>Alex Dupre,<br />
&nbsp;<wbr>Gabriele Vinci,<br />
&nbsp;<wbr>Andrey Ulanov,<br />
&nbsp;<wbr>Fygul Hether,<br />
&nbsp;<wbr>Jeffrey Lim,<br />
&nbsp;<wbr>Ying-Chieh Liao,<br />
&nbsp;<wbr>Johannes Erdfelt,<br />
&nbsp;<wbr>Martin Sarfy,<br />
&nbsp;<wbr>Clive Goodhead,<br />
&nbsp;<wbr>Aristoteles Pagaltzis,<br />
&nbsp;<wbr>Stefan Hornburg,<br />
&nbsp;<wbr>Mehmet Cokcevik,<br />
&nbsp;<wbr>Brynjar Eide,<br />
&nbsp;<wbr>Torgnt Wernersson,<br />
&nbsp;<wbr>Banhalmi Csaba,<br />
&nbsp;<wbr>Volodin D,<br />
&nbsp;<wbr>Oriol Magran�,<br />
&nbsp;<wbr>Jui-Nan Lin,<br />
&nbsp;<wbr>Patrick Gosling,<br />
&nbsp;<wbr>Marc Balmer,<br />
&nbsp;<wbr>Rajat Upadhyaya&nbsp;<wbr>/&nbsp;<wbr>Novell,<br />
&nbsp;<wbr>Christian Cier-Zniewski,<br />
&nbsp;<wbr>Wilco Baan Hofman,<br />
&nbsp;<wbr>Clement Chauplannaz.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code>, <code><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a>(8)</code> <code><a href="/docs/linux/man/8-pure-ftpwho/">pure-ftpwho</a>(8)</code> <code><a href="/docs/linux/man/8-pure-mrtginfo/">pure-mrtginfo</a>(8)</code> <code><a href="/docs/linux/man/8-pure-uploadscript/">pure-uploadscript</a>(8)</code> <code><a href="/docs/linux/man/8-pure-statsdecode/">pure-statsdecode</a>(8)</code> <code><a href="/docs/linux/man/8-pure-pw/">pure-pw</a>(8)</code> <code><a href="/docs/linux/man/8-pure-quotacheck/">pure-quotacheck</a>(8)</code> <code><a href="/docs/linux/man/8-pure-authd/">pure-authd</a>(8)</code> <code>RFC 959</code>, <code>RFC 2228,</code> <code>RFC 2389,</code> <code>RFC 2428</code> and <code>RFC 4217</code>. </p>
