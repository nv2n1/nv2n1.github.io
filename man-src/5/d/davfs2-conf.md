---
title: "davfs2-conf(5)"
name: "davfs2-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-davfs2-conf/"
description: "davfs2.conf – Configuration file for mount.davfs"
---

<p><code>davfs2.conf</code> &#8211; Configuration file for <code>mount.davfs</code> </p>
<h2>Description</h2>
<p>There is a system wide configuration file <i>/etc/davfs2/davfs2.conf</i> and user configuration files <i>~/.davfs2/davfs2.conf</i>. When <code>mount.davfs</code> is invoked by root, only the system wide configuration file is read. When invoked by an ordinary user, the user configuration file is read in addition. Settings from the user configuration file will take precedence over the system wide configuration. The configuration file consists of lines where each line contains a keyword value pair. Keyword and value are seperated by spaces and/or tabs. The file may contain sections that are for one specific mount point only. Such a section starts with a line, that contains the full path of the mount point enclosed in square brackets. The section ends at the start of the next section or the end of file. Options that shall apply to all mounted file system must come before the first sections. Options given in a mount specific section will have precedence. </p>
<h2>Example</h2>
<p>kernel_fs coda<br />
 proxy<tt>&nbsp;<wbr>&nbsp;<wbr></tt>foo.bar:8080</p>
<p> use_locks 0 </p>
<p> [/media/dav]<br />
 use_locks 1 </p>
<p> [/home/otto/mywebspace]<br />
 gui_optimize 1 All mounted davfs2 file systems will use the coda kernel file system and the proxy foo.bar. All davfs2 file systems expect /media/dav will disable the use of the locks. /home/otto/mywebspace will use the gui_optimize option. </p>
<h2>General Syntax Rules</h2>
<p>Lines that only contain spaces and tabs (empty lines) are ignored. </p>
<p> # indicates a comment. The rest of the line is ignored. </p>
<p> \ is the escape character. </p>
<p> &quot;&quot; is used for quotation. </p>
<p> If a value contains one of the special characters space, tab, #, \, or &quot;, this character must be escaped by a preceding \. Use &#8216;\&nbsp;<wbr>&#8216; instead of &#8216;&nbsp;<wbr>&#8216;, &#8216;\#&#8217; instead of &#8216;#&#8217;, &#8216;\&#8217; instead of &#8216;\&#8217; and &#8216;\&quot;&#8217; instead of &#8216;&quot;&#8217;. </p>
<p> Values containing spaces, tabs or # may instead be enclosed in double quotes. But &quot; and &#8216; must be escaped even within double quotes. If the starting line of a section is enclosed in double quotes, the square brakets must be within the quotes (like &quot;[/home/otto/with space]&quot;). </p>
<p> Boolean option values (yes/no) must be given as numerical value. 0 for no, 1 for yes.</p>
<h2>Available Configuration Options</h2>
<h2>General Options</h2>
<dl>
<dt><code>dav_user</code></p>
<dd>When invoked by root the <code>mount.davfs</code> daemon will run as this user. Value must be given as <i>name</i>, <code>not</code> as numerical id.<br />
 Default: davfs2<br />
 <code>Only allowed in the system wide configuration file.</code> </p>
<dt><code>dav_group</code></p>
<dd>The group of the running <code>mount.davfs</code> daemon. Ordinary users must be member of this group in order to mount a davfs2 file system. Value must be given as <i>name</i>, <code>not</code> as numerical id.<br />
 Default: davfs2<br />
 <code>Only allowed in the system wide configuration file.</code> </p>
<dt><code>kernel_fs</code></p>
<dd>Which kernel file system to use, to integrate into the virtual file system. Possible values are <i>fuse</i> and <i>coda</i>.<br />
 Default: fuse </p>
<dt><code>buf_size</code></p>
<dd>Size in KiByte of the buffer used to communicate with the kernel file system. Only usefull with <i>fuse</i>, where read and write operations may profit from a larger buffer.<br />
 Default: 16 </p>
</dl>
<h2>WebDAV Related Options</h2>
<dl>
<dt><code>use_proxy</code></p>
<dd>Whether to use a proxy to connect to the WebDAV server. 0 = no, 1 = yes. If no proxy is defined in the configration file or the environment variables <code>https_proxy</code>, <code>http_proxy</code> and <code>all_proxy</code>, this option has no effect.<br />
 Default: 1<br />
 <code>Only allowed in the system wide configuration file.</code> </p>
<dt><code>proxy</code></p>
<dd>Name of the proxy. The name must be the fully qualified domain name (no scheme). If the proxy port differs from the default of 8080, it must be appended, seperated by a colon. Examples: <i>foo.bar:1704</i> or <i>foo.bar</i><br />
 <code>Only allowed in the system wide configuration file.</code> </p>
<dt><code>servercert</code></p>
<dd>Name of a certificate file in PEM format. The name of the file may be given as absolute path or as file name only. In the latter case the directories <i>~/.davfs2/certs</i> and <i>/etc/davfs2/certs</i> will be searched.<br />
 This option is intended for self-signed server certificates. Self-signed means issuer and subject are the same. Common name (CN) must be the domain name of the server.<br />
 In case the server certificate is not self-singed, this file must contain the certificate of the certificate authority (CA) that signed the server certificate, not the the server certificate itself. If an hirarchy of CA&#8217;s is involved (the CA that signed the server certificate is not the root CA), the file must contain all the certificates from the chain of CAs involved, beginning with the CA that signed the server certificate, up to the self-signed certificate of the root CA. (The option name <code>servertcert</code> is a misnomer in this case. Sorry.) You can create the file by concatenating all the CA-certificates involved.<br />
 <code>Note:</code> Even if the certificate is trusted, that does not mean it is accepted. There is the additional constraint, that the certificate presented by the server must belong to the server. The CN in the server certificate must be the domain name of the server. There is currently no way to automatically accept certificates that don&#8217;t belong to the server. </p>
<dt><code>clientcert</code></p>
<dd>Name of a certificate in PKCS#12 format that will be used to authenticate with the server. The name of the file may be given as absolute path or as file name only. In the latter case the directories <i>~/.davfs2/certs/private</i> and <i>/etc/davfs2/certs/private</i> will be searched. </p>
<dt><code>secrets</code></p>
<dd>Name of a file that holds the credentials for servers and the proxy, and passwords to decrypt the client certificate. The name must be an absolute path. The file must be read and writable by the owner only (mode 600).<br />
 Default: ~/.davfs2/secrets<br />
 <code>Only allowed in the user configuration file.</code> The system wide secrets file is allways <i>/etc/davfs2/secrets</i>. </p>
<dt><code>ask_auth</code></p>
<dd>Ask the user interactively for credentials and passwords if not found in the secretsfile. Ask the user if a servercert cannot be verified. 0 = no, 1 = yes.<br />
 Default: 1 </p>
<dt><code>use_locks</code></p>
<dd>Whether to lock files on the server when they are opened for writing. 0 = no, 1 = yes.<br />
 Default: 1 </p>
<dt><code>lock_owner</code></p>
<dd>A string send to the server to identify the owner of a lock. If a WebDAV resource is used at the same time by different clients using the same credentials, different values for lock_owner should be choosen.<br />
 Default: the username from the credentials </p>
<dt><code>lock_timeout</code></p>
<dd>How long in seconds locks should be valid, before the server removes them. The server may ignore this and set its own timeout value.<br />
 Default: 1800 </p>
<dt><code>lock_refresh</code></p>
<dd>That many seconds before the lock times out, <code>mount.davfs</code> will try to refresh the lock. The value should be substantially greater than <code>delay_upload</code>.<br />
 Default: 60 </p>
<dt><code>use_expect100</code></p>
<dd>To avoid uploading big files that will be refused by the server, <code>mount.davfs</code> uses the header <i>expect: 100-continue</i> to get the o.k. from the server before uploading. Not all servers understand this. 0 = no, 1 = yes.<br />
 Default: 0 </p>
<dt><code>if_match_bug</code></p>
<dd>Some servers do not handle If-Match and If-None-Match-headers correctly. This otion tells <code>mount.davfs</code> to use HEAD instead of thes headers. 0 = no, 1 = yes.<br />
 Default: 0 </p>
<dt><code>drop_weak_etags</code></p>
<dd>Popular servers send a weak etag whenever they are not able to calculate a strong one. This weak etag will never be valid, but after one second it is silently turned into a strong, valid etag. With this flag set to 1, <code>mount.davfs</code> will never use this weak etags. If the flag is 0, the weakness indicator will be removed and the etag is assumed to be strong. There is some danger of the Lost-Update-Problem with this. But it is minimized when using locks.<br />
 You should turn this on, when you can&#8217;t use locks and there is the danger of concurrent access to the same resource. In this case the etag is not used at all and the resource cannot be cached.<br />
 0 = no, 1 = yes.<br />
 Default: 0 </p>
<dt><code>allow_cookie</code></p>
<dd>Some servers will only work when they are allowed to set a cookie and this cookie is returned in subsequent requests. This option adds very simple cookie support. It supports just one cookie which should usually be a session ID. 0 = no, 1 = yes.<br />
 Default: 0 </p>
<dt><code>precheck</code></p>
<dd>If option <code>if_match_bug</code> is set: use HEAD-requests to check for existence or modification of a file to avoid unintended overwriting what somebody else changed. Has no effect if option <code>if_match_bug</code> is 0. You should only set it 0, if there is no concurrent access to the server. 0 = no, 1 = yes.<br />
 Default: 1 </p>
<dt><code>ignore_dav_header</code></p>
<dd>Some servers send wrong information about their capabilities in the DAV-header. In this case the header should be ignored.<br />
 Default: 0 </p>
<dt><code>server_charset</code></p>
<dd>When extracting file names from the path component of the URL, <code>mount.davfs</code> will assume they are encoded using this character set and translate file names to the local character set. This is <code>not</code> about encoding of file contents and <code>not</code> about HTTP escaping rules.<br />
 There is no means in HTTP to know the character encoding of the path component. There may be even different encodings within the same path, as the encoding of file names is often defined by the clients that created them. Nowadays it is best to use only UTF-8 encoding and to do no conversion. If you are not sure that all clients understand UTF-8, restrict file names to pure us-ascii. Never use characters in file names, that may have a special function on some operating systems (like /, : and \).<br />
 Default: no character set conversion </p>
<dt><code>connect_timeout</code></p>
<dd>When creating a TCP connection to the server <code>mount.davfs</code> will wait that many seconds for an answer before assuming an error. If a value of &#8216;0&#8217; is used then no explicit timeout handling is set and the connect call will only timeout as dictated by the TCP stack.<br />
 This parameter only takes effect if the version of neon in use (neon version &gt; 0.26) and the OS support non-blocking I/O.<br />
 Default: 10 </p>
<dt><code>read_timeout</code></p>
<dd>How long in seconds <code>mount.davfs</code> will wait for an answer from the server before assuming an error.<br />
 Default: 30 </p>
<dt><code>retry</code></p>
<dd>When <code>mount.davfs</code> can not reach the server it will try again after <code>retry</code> seconds. For subsequent retries the interval will be increased up to <code>max_retry</code> seconds.<br />
 Default: 30 </p>
<dt><code>max_retry</code></p>
<dd>Maximum value of the retry interval.<br />
 Default: 300 </p>
<dt><code>max_upload_attempts</code></p>
<dd>When uploading a changed file fails temporarily <code>mount.davfs</code> will retry with increasing intervals, but not more often than this.<br />
 With a bad connection this will cause additional traffic. To reduce traffic caused by unsuccessful attempts option <code>use_expect100</code> can be set. But please test it. Most proxies and some servers don&#8217;t support this header.<br />
 Default: 15 </p>
<dt><code>add_header</code></p>
<dd>Your server might expect special headers to do what you want. Different from other options, this one takes two values: the name of the header and its value. Some ASP-backends to IIS seem to require the Microsoft specific header &quot;Translate: F&quot;. You can add it like this:<br />
 add_header Translate F<br />
 <code>mount.davfs</code> will add header &quot;Translate: F&quot; on all requests.<br />
 This option is cumulative. You can enter more than one add_header option and all of them will be added. Also add_header options from /etc/davfs2/davfs2.conf and ~/.davfs2/davfs2.conf are merged. </p>
</dl>
<h2>Cache Related Options</h2>
<dl>
<dt><code>backup_dir</code></p>
<dd>Each mounted davfs2 file system has a directory to store backups of files that could not be stored back to the server. This sets the name of this directory. You should regularly check this directory.<br />
 Default: lost+found </p>
<dt><code>cache_dir</code></p>
<dd>The directory where <code>mount.davfs</code> will store cached files. For every mount point a subdirectory will be created.<br />
 In the systemwide configuration file this will set the system wide cache, used by root. In a users configuration file it will set the cache used by this user.<br />
 Defaults: /var/cache/davfs2 and ~/.davfs2/cache </p>
<dt><code>cache_size</code></p>
<dd>The amount of disk space in MiByte that may be used. <code>mount.davfs</code> will always take enough space to cache open files, ignoring this value if necessary.<br />
 Default: 50 </p>
<dt><code>table_size</code></p>
<dd><code>mount.davfs</code> maintains a hash table with an entry for each known file or directory. This gives the number of entries in this table. For large file systems (more than some hundreds of files) increasing this number may speed up file operations. The value should be a power of 2.<br />
 Default: 1024 </p>
<dt><code>dir_refresh</code></p>
<dd>After <code>mount.davfs</code> has got information about files in a directory it considers it valid for this time in seconds. Note: This does not affect opening of files and reading a directory by an application.<br />
 Default: 60 </p>
<dt><code>file_refresh</code></p>
<dd>When a file or directory is opened by an application, <code>mount.davfs</code> will first check the server for a newer version. But some applications do open calls on the same file in short sequence. To avoid unecessary traffic <code>mount.davfs</code> will wait that many seconds before it send a new request for the same information.<br />
 Default: 1 </p>
<dt><code>delay_upload</code></p>
<dd>When a file that has been changed is closed, <code>mount.davfs</code> will wait that many seconds before it will upload it to the server. This will avoid uploading of temporary files that will be removed immediately after closing. If you need the files to appear on the server immediately after closing, set this option to 0.<br />
 Default: 10 </p>
<dt><code>gui_optimize</code></p>
<dd>When a file is opened, <code>mount.davfs</code> will have to check the server whether there is a newer version. Graphical User Interfaces tend to open just any file, slowing down things dramatically for large directories. With this option <code>mount.davfs</code> will try to get this information from all files in a directory with one PROPFIND request. 0 = no, 1 = yes.<br />
 Default: 0 </p>
</dl>
<h2>Debugging Options</h2>
<dl>
<dt><code>debug</code></p>
<dd>Send debug messages to the syslog daemon. The value tells what kind of information shall be logged. The messages are send with facility LOG_DAEMON and priority LOG_DEBUG. It depends from the configuration of the syslog daemon where the messages will go (propably /var/log/messages, /var/log/syslog or /var/log/daemon.log). Whether HTTP related debug messages are available depends on your neon library.<br />
 Unlike other options, this option is cumulative. If there are several debug entries with different values, all of them will be applied. Also debug options from /etc/davfs2/davfs2.conf and ~/.davfs2/davfs2.conf are merged.<br />
 <code>Note:</code> Debug messages let the log-files grow quickly. Never use this option in normal operation of mount.davfs.<br />
 Default: no debugging messages</p>
<dl>
<dd>
<dl>
<dt><code>Recognized values:</code></p>
<dd>
<dt><code>config</code></p>
<dd>Command line and configuration options.</p>
<dt><code>kernel</code></p>
<dd>Upcalls from the kernel file system.</p>
<dt><code>cache</code></p>
<dd>Cache operations like adding and removing nodes.</p>
<dt><code>http</code></p>
<dd>HTTP headers.</p>
<dt><code>xml</code></p>
<dd>Parsing of the XML-body of WebDAV-requests.</p>
<dt><code>httpauth</code></p>
<dd>Negotiation of authentication.</p>
<dt><code>locks</code></p>
<dd>Information about locks.</p>
<dt><code>ssl</code></p>
<dd>TLS/SSL related stuff like certificates.</p>
<dt><code>httpbody</code></p>
<dd>Complete body of HTTP-responses.</p>
<dt><code>secrets</code></p>
<dd>Also print confidential information, which is usually omitted or obscured.</p>
<dt><code>most</code></p>
<dd>Includes config, kernel, cache and http.</dl>
</dl>
</dl>
<h2>Authors</h2>
<p>This man page was written by by Werner Baumann &lt;werner.baumann [at] onlinehome.de&gt;.</p>
<h2>Davfs2 Home</h2>
<p><a rel="nofollow" href="http://savannah.nongnu.org/projects/davfs2">http://savannah.nongnu.org/projects/davfs2</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mount-davfs/">mount.davfs</a></code>(8), <code><a href="/docs/linux/man/8-umount-davfs/">umount.davfs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) </p>
