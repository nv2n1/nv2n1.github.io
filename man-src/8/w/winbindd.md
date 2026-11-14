---
title: "winbindd(8)"
name: "winbindd"
section: "8"
letter: "w"
url: "/docs/linux/man/8-winbindd/"
description: "winbindd – Name Service Switch daemon for resolving names from NT servers"
---

<p>winbindd &#8211; Name Service Switch daemon for resolving names from NT servers</p>
<h2>Synopsis</h2>
<dl>
<dd>winbindd [-D|&#8211;daemon] [-F|&#8211;foreground] [-S|&#8211;stdout] [-i|&#8211;interactive] [-d&nbsp;<wbr>&lt;debug level&gt;] [-s&nbsp;<wbr>&lt;smb config file&gt;] [-n|&#8211;no-caching] [&#8211;no-process-group]</dl>
<h2>Description</h2>
<p>This program is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> winbindd is a daemon that provides a number of services to the Name Service Switch capability found in most modern C libraries, to arbitrary applications via PAM and ntlm_auth and to Samba itself. </p>
<p> Even if winbind is not used for nsswitch, it still provides a service to smbd, ntlm_auth and the pam_winbind.so PAM module, by managing connections to domain controllers. In this configuration the m[blue]<code>idmap config * : range</code>m[] parameter is not required. (This is known as `netlogon proxy only mode&#8217;.) </p>
<p> The Name Service Switch allows user and system information to be obtained from different databases services such as NIS or DNS. The exact behaviour can be configured through the /etc/nsswitch.conf file. Users and groups are allocated as they are resolved to a range of user and group ids specified by the administrator of the Samba system. </p>
<p> The service provided by winbindd is called `winbind&#8217; and can be used to resolve user and group information from a Windows NT server. The service can also provide authentication services via an associated PAM module. </p>
<p> The pam_winbind module supports the <i>auth</i>, <i>account</i> and <i>password</i> module-types. It should be noted that the <i>account</i> module simply performs a getpwnam() to verify that the system can obtain a uid for the user, as the domain controller has already performed access control. If the libnss_winbind library has been correctly installed, or an alternate source of names configured, this should always succeed. </p>
<p> The following nsswitch databases are implemented by the winbindd service: </p>
<p> hosts</p>
<dl>
<dd>This feature is only available on IRIX. User information traditionally stored in the <a href="/docs/linux/man/5-hosts/">hosts</a>(5) file and used by <a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a>(3) functions. Names are resolved through the WINS server or by broadcast.</dl>
<p> passwd</p>
<dl>
<dd>User information traditionally stored in the <a href="/docs/linux/man/5-passwd/">passwd</a>(5) file and used by <a href="/docs/linux/man/3-getpwent/">getpwent</a>(3) functions.</dl>
<p> group</p>
<dl>
<dd>Group information traditionally stored in the <a href="/docs/linux/man/5-group/">group</a>(5) file and used by <a href="/docs/linux/man/3-getgrent/">getgrent</a>(3) functions.</dl>
<p> For example, the following simple configuration in the /etc/nsswitch.conf file can be used to initially resolve user and group information from /etc/passwd and /etc/group and then from the Windows NT server. </p>
<dl>
<dd>
<pre>passwd: files winbind
group: files winbind
## only available on IRIX: use winbind to resolve hosts:
# hosts: files dns winbind
## All other NSS enabled systems should use libnss_wins.so like this:
hosts: files dns wins</pre>
</dl>
<p> The following simple configuration in the /etc/nsswitch.conf file can be used to initially resolve hostnames from /etc/hosts and then from the WINS server. </p>
<dl>
<dd>
<pre>hosts: files wins</pre>
</dl>
<h2>Options</h2>
<p>-D|&#8211;daemon</p>
<dl>
<dd>If specified, this parameter causes the server to operate as a daemon. That is, it detaches itself and runs in the background on the appropriate port. This switch is assumed if winbindd is executed on the command line of a shell.</dl>
<p> -F|&#8211;foreground</p>
<dl>
<dd>If specified, this parameter causes the main winbindd process to not daemonize, i.e. double-fork and disassociate with the terminal. Child processes are still created as normal to service each connection request, but the main process does not exit. This operation mode is suitable for running winbindd under process supervisors such as supervise and svscan from Daniel J. Bernstein&#8217;s daemontools package, or the AIX process monitor.</dl>
<p> -S|&#8211;stdout</p>
<dl>
<dd>If specified, this parameter causes winbindd to log to standard output rather than a file.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dd><i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 0. </p>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> -V|&#8211;version</p>
<dl>
<dd>Prints the program version number.</dl>
<p> -s|&#8211;configfile=&lt;configuration file&gt;</p>
<dl>
<dd>The file specified contains the configuration details required by the server. The information in this file includes server-specific information such as what printcap file to use, as well as descriptions of all the services that the server is to provide. See smb.conf for more information. The default configuration file name is determined at compile time.</dl>
<p> -l|&#8211;log-basename=logdirectory</p>
<dl>
<dd>Base directory name for log/debug files. The extension <code>&quot;.progname&quot;</code> will be appended (e.g. log.smbclient, log.smbd, etc&#8230;). The log file is never removed by the client.</dl>
<p> &#8211;option=&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dd>Set the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) option &quot;&lt;name&gt;&quot; to value &quot;&lt;value&gt;&quot; from the command line. This overrides compiled-in defaults and options read from the configuration file.</dl>
<p> -?|&#8211;help</p>
<dl>
<dd>Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dd>Display brief usage message.</dl>
<p> -i|&#8211;interactive</p>
<dl>
<dd>Tells winbindd to not become a daemon and detach from the current terminal. This option is used by developers when interactive debugging of winbindd is required. winbindd also logs to standard output, as if the -S parameter had been given.</dl>
<p> -n|&#8211;no-caching</p>
<dl>
<dd>Disable some caching. This means winbindd will often have to wait for a response from the domain controller before it can respond to a client and this thus makes things slower. The results will however be more accurate, since results from the cache might not be up-to-date. This might also temporarily hang winbindd if the DC doesn&#8217;t respond. This does not disable the samlogon cache, which is required for group membership tracking in trusted environments.</dl>
<p> &#8211;no-process-group</p>
<dl>
<dd>Do not create a new process group for winbindd.</dl>
<h2>Name And Id Resolution</h2>
<p>Users and groups on a Windows NT server are assigned a security id (SID) which is globally unique when the user or group is created. To convert the Windows NT user or group into a unix user or group, a mapping between SIDs and unix user and group ids is required. This is one of the jobs that winbindd performs. </p>
<p> As winbindd users and groups are resolved from a server, user and group ids are allocated from a specified range. This is done on a first come, first served basis, although all existing users and groups will be mapped as soon as a client performs a user or group enumeration command. The allocated unix ids are stored in a database and will be remembered. </p>
<p> WARNING: The SID to unix id database is the only location where the user and group mappings are stored by winbindd. If this store is deleted or corrupted, there is no way for winbindd to determine which user and group ids correspond to Windows NT user and group rids.</p>
<h2>Configuration</h2>
<p>Configuration of the winbindd daemon is done through configuration parameters in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file. All parameters should be specified in the [global] section of smb.conf. </p>
<dl>
<dd>&bull; m[blue]<code>winbind separator</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>idmap config * : range</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>idmap config * : backend</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>winbind cache time</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>winbind enum users</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>winbind enum groups</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>template homedir</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>template shell</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>winbind use default domain</code>m[]</dl>
<dl>
<dd>&bull; m[blue]<code>winbind: rpc only</code>m[] Setting this parameter forces winbindd to use RPC instead of LDAP to retrieve information from Domain Controllers.</dl>
<h2>Example Setup</h2>
<p>To setup winbindd for user and group lookups plus authentication from a domain controller use something like the following setup. This was tested on an early Red Hat Linux box. </p>
<p> In /etc/nsswitch.conf put the following: </p>
<dl>
<dd>
<pre>passwd: files winbind
group: files winbind</pre>
</dl>
<p> In /etc/pam.d/* replace the <i> auth</i> lines with something like this: </p>
<dl>
<dd>
<pre>auth required /lib/security/pam_securetty.so
auth required /lib/security/pam_nologin.so
auth sufficient /lib/security/pam_winbind.so
auth required /lib/security/pam_unix.so \
 use_first_pass shadow nullok</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The PAM module pam_unix has recently replaced the module pam_pwdb. Some Linux systems use the module pam_unix2 in place of pam_unix. </p>
</dl>
<p> Note in particular the use of the <i>sufficient </i> keyword and the <i>use_first_pass</i> keyword. </p>
<p> Now replace the account lines with this: </p>
<p> account required /lib/security/pam_winbind.so </p>
<p> The next step is to join the domain. To do that use the net program like this: </p>
<p> net join -S PDC -U Administrator </p>
<p> The username after the <i>-U</i> can be any Domain user that has administrator privileges on the machine. Substitute the name or IP of your PDC for &quot;PDC&quot;. </p>
<p> Next copy libnss_winbind.so to /lib and pam_winbind.so to /lib/security. A symbolic link needs to be made from /lib/libnss_winbind.so to /lib/libnss_winbind.so.2. If you are using an older version of glibc then the target of the link should be /lib/libnss_winbind.so.1. </p>
<p> Finally, setup a <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) containing directives like the following: </p>
<dl>
<dd>
<pre>[global]
 winbind separator = +
 winbind cache time = 10
 template shell = /bin/bash
 template homedir = /home/%D/%U
 idmap config * : range = 10000-20000
 workgroup = DOMAIN
 security = domain
 password server = *</pre>
</dl>
<p> Now start winbindd and you should find that your user and group database is expanded to include your NT users and groups, and that you can login to your unix box as a domain user, using the DOMAIN+user syntax for the username. You may wish to use the commands getent passwd and getent group to confirm the correct operation of winbindd.</p>
<h2>Notes</h2>
<p>The following notes are useful when configuring and running winbindd: </p>
<p> <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8) must be running on the local machine for winbindd to work. </p>
<p> PAM is really easy to misconfigure. Make sure you know what you are doing when modifying PAM configuration files. It is possible to set up PAM such that you can no longer log into your system. </p>
<p> If more than one UNIX machine is running winbindd, then in general the user and groups ids allocated by winbindd will not be the same. The user and group ids will only be valid for the local machine, unless a shared m[blue]<code>idmap config * : backend</code>m[] is configured. </p>
<p> If the Windows NT SID to UNIX user and group id mapping file is damaged or destroyed then the mappings will be lost.</p>
<h2>Signals</h2>
<p>The following signals can be used to manipulate the winbindd daemon. </p>
<p> SIGHUP</p>
<dl>
<dd>Reload the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file and apply any parameter changes to the running version of winbindd. This signal also clears any cached user and group information. The list of other domains trusted by winbindd is also reloaded.</dl>
<p> SIGUSR2</p>
<dl>
<dd>The SIGUSR2 signal will cause winbindd to write status information to the winbind log file. </p>
<p> Log files are stored in the filename specified by the log file parameter.</dl>
<h2>Files</h2>
<p>/etc/<a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a>(5)</p>
<dl>
<dd>Name service switch configuration file.</dl>
<p> /tmp/.winbindd/pipe</p>
<dl>
<dd>The UNIX pipe over which clients communicate with the winbindd program. For security reasons, the winbind client will only attempt to connect to the winbindd daemon if both the /tmp/.winbindd directory and /tmp/.winbindd/pipe file are owned by root.</dl>
<p> $LOCKDIR/winbindd_privileged/pipe</p>
<dl>
<dd>The UNIX pipe over which &#8216;privileged&#8217; clients communicate with the winbindd program. For security reasons, access to some winbindd functions &#8211; like those needed by the ntlm_auth utility &#8211; is restricted. By default, only users in the &#8216;root&#8217; group will get this access, however the administrator may change the group permissions on $LOCKDIR/winbindd_privileged to allow programs like &#8216;squid&#8217; to use ntlm_auth. Note that the winbind client will only attempt to connect to the winbindd daemon if both the $LOCKDIR/winbindd_privileged directory and $LOCKDIR/winbindd_privileged/pipe file are owned by root.</dl>
<p> /lib/libnss_winbind.so.X</p>
<dl>
<dd>Implementation of name service switch library.</dl>
<p> $LOCKDIR/winbindd_idmap.tdb</p>
<dl>
<dd>Storage for the Windows NT rid to UNIX user/group id mapping. The lock directory is specified when Samba is initially compiled using the <i>&#8211;with-lockdir</i> option. This directory is by default /usr/local/samba/var/locks.</dl>
<p> $LOCKDIR/winbindd_cache.tdb</p>
<dl>
<dd>Storage for cached user and group information.</dl>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a>(5), <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7), <code><a href="/docs/linux/man/1-wbinfo/">wbinfo</a></code>(1), <code><a href="/docs/linux/man/8-ntlm_auth/">ntlm_auth</a></code>(8), <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5), <code><a href="/docs/linux/man/8-pam_winbind/">pam_winbind</a></code>(8)</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> wbinfo and winbindd were written by Tim Potter. </p>
<p> The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy.</p>
