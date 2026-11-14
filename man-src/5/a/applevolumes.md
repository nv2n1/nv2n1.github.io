---
title: "applevolumes(5)"
name: "applevolumes"
section: "5"
letter: "a"
url: "/docs/linux/man/5-applevolumes/"
description: "AppleVolumes.default – Configuration file used by"
---

<p>AppleVolumes.default &#8211; Configuration file used by <code></p>
<p><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) to determine the shares made available through Appletalk</p>
<h2>Description</h2>
<p>/etc/atalk//AppleVolumes.default is the configuration file used by <code>afpd</code> to determine what portions of the file system will be shared via Apple Filing Protocol, as well as their behaviour. Any line not prefixed with # is interpreted. Newline escaping is supported. The configuration lines are composed like: path <i>[ volume name ] [ options ]</i> The path name must be a fully qualified path name, or a path name using either the ~ shell shorthand or any of the substitution variables, which are listed below. The volume name is the name that appears in the Chooser ot the &quot;connect to server&quot; dialog on Macintoshes to represent the appropriate share. If there are spaces in the name, it should be in quotes (i.e. &quot;File Share&quot;). The volume name may not exceed 27 characters in length, and cannot contain the &#8216;:&#8217; character.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Each volume has to be configured on a <code>single</code> line. Though newline escaping is supported.  The possible options and their meanings are: adouble:<i>[v1|v2|osx]</i></p>
<dl>
<dd>specify the format of the metadata files, which are used for saving Mac resource fork as well. Earlier versions used AppleDouble V1, the new default format is V2. Starting with Netatalk 2.0, the scheme MacOS X uses currently (10.3.x), is also supported</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Using <code>adouble:osx</code> is <code>not</code> recommended for production use. Its only aim is to temporarely share eg. FAT32 formatted FireWire harddrives written on a Macintosh with afpd. Apple&#8217;s metadata scheme lacks several essential features, so using it on the server&#8217;s side will break both CNIDs and MacOS 9 compatibility  allow:<i>[users/groups]</i></p>
<dl>
<dd>The allow option allows the users and groups that access a share to be specified. Users and groups are specified, delimited by commas. Groups are designated by a @ prefix. Example: allow:user1,user2,@group</dl>
<p> deny:<i>[users/groups]</i></p>
<dl>
<dd>The deny option specifies users and groups who are not allowed access to the share. It follows the same format as the allow option.</dl>
<p> allowed_hosts:<i>[IPv4 host address/IPv4 netmask bits[, &#8230; ]]</i></p>
<dl>
<dd>Only listed hosts and networks are allowed, all others are rejected. Example: allowed_hosts:10.1.0.0/16,10.2.1.100</dl>
<p> denied_hosts:<i>[IPv4 host address/IPv4 netmask bits[, &#8230;]]</i></p>
<dl>
<dd>Listed hosts and nets are rejected, all others are allowed. Example: denied_hosts: 192.168.100/24,10.1.1.1</dl>
<p> cnidscheme:<i>[backend]</i></p>
<dl>
<dd>set the CNID backend to be used for the volume, default is [:DEFAULT_CNID_SCHEME:] available schemes: [:COMPILED_BACKENDS:]</dl>
<p> dbpath:<i>[path]</i></p>
<dl>
<dd>Sets the database information to be stored in path. You have to specifiy a writable location, even if the volume is read only.</dl>
<p> maccharset:<i>[charset]</i></p>
<dl>
<dd>specifies the mac client codepage for this Volume, e.g. &quot;MAC_ROMAN&quot;, &quot;MAC_CYRILLIC&quot;. If not specified the setting from afpd.conf is inherited. This setting is only required if you need volumes, where the mac codepage differs from the one globally set in afpd.conf.</dl>
<p> options:<i>[option]</i></p>
<dl>
<dd>This allows multiple options to be specified in a comma delimited format. The available options are: invisibledots</p>
<dl>
<dd>Use with <code>usedots</code>: make dot files invisible.</dl>
<p> limitsize</p>
<dl>
<dd>Limit disk size reporting to 2GB. This can be used for older Macintoshes using newer Appleshare clients.</dl>
<p> preexec_close</p>
<dl>
<dd>a non-zero return code from preexec close the volume being immediately, preventing clients to mount/see the volume in question.</dl>
<p> ro</p>
<dl>
<dd>Specifies the share as being read only for all users. The .AppleDB directory has to be writeable, you can use the <code>-dbpath</code> option to relocate it.</dl>
<p> root_preexec_close</p>
<dl>
<dd>a non-zero return code from root_preexec closes the volume immediately, preventing clients to mount/see the volume in question.</dl>
<p> upriv</p>
<dl>
<dd>use AFP3 unix privileges. Become familiar with the new &quot;unix privileges&quot; AFP permissions concepts in MacOS X before using this option. See also: <code>perm|fperm|dperm</code>.</dl>
<p> usedots</p>
<dl>
<dd>Don&#8217;t do :hex translation for dot files. note: when this option gets set, certain file names become illegal. These are .Parent and anything that starts with .Apple. See also <code>invisibledots</code>.</dl>
</dl>
<p> password:<i>[password]</i></p>
<dl>
<dd>This option allows you to set a volume password, which can be a maximum of 8 characters long (using ASCII strongly recommended at the time of this writing).</dl>
<p> perm|fperm|dperm:[mode]</p>
<dl>
<dd>Add(or) with the client requested permissions: <code>perm</code> affects files and directories, <code>fperm</code> is for files only, <code>dperm</code> is for directories only. Use with <code>options:upriv</code>. <code>Example. Volume for a collaborative workgroup</code></p>
<dl>
<dd>
<pre>/path/to/volume &quot;Workgroup&quot; options:upriv dperm:0770 fperm:0660</pre>
</dl>
</dl>
<p> preexec:<i>[command]</i></p>
<dl>
<dd>command to be run when the volume is mounted, ignored for user defined volumes</dl>
<p> postexec:<i>[command]</i></p>
<dl>
<dd>command to be run when the volume is closed, ignored for user defined volumes</dl>
<p> root_preexec:<i>[command]</i></p>
<dl>
<dd>command to be run as root when the volume is mounted, ignored for user defined volumes</dl>
<p> root_postexec:<i>[command]</i></p>
<dl>
<dd>command to be run as root when the volume is closed, ignored for user defined volumes</dl>
<p> rolist:[<code>users/groups</code>]</p>
<dl>
<dd>Allows certain users and groups to have read-only access to a share. This follows the allow option format.</dl>
<p> rwlist:<i>[users/groups]</i></p>
<dl>
<dd>Allows certain users and groups to have read/write access to a share. This follows the allow option format.</dl>
<p> veto:<i>[vetoed name]</i></p>
<dl>
<dd>hide files and directories,where the path matches one of the &#8216;/&#8217; delimited vetoed names. Matches are partial, e.g. path is /abc/def/file and veto:/abc/ will hide the file.</dl>
<p> volcharset:<i>[charset]</i></p>
<dl>
<dd>specifies the volume codepage, e.g. &quot;UTF8&quot;, &quot;UTF8-MAC&quot;, &quot;ISO-8859-15&quot;. Defaults to &quot;UTF8&quot;.</dl>
<h2>Variable Substitutions</h2>
<p>You can use variables in both volume path and volume name. </p>
<dl>
<dd>1. if you specify an unknown variable, it will not get converted.</dl>
<dl>
<dd>2. if you specify a known variable, but that variable doesn&#8217;t have a value, it will get ignored.</dl>
<p> The variables which can be used for substitutions are: </p>
<p> $b</p>
<dl>
<dd>basename</dl>
<p> $c</p>
<dl>
<dd>client&#8217;s ip or appletalk address</dl>
<p> $d</p>
<dl>
<dd>volume pathname on server</dl>
<p> $f</p>
<dl>
<dd>full name (contents of the gecos field in the passwd file)</dl>
<p> $g</p>
<dl>
<dd>group name</dl>
<p> $h</p>
<dl>
<dd>hostname</dl>
<p> $i</p>
<dl>
<dd>client&#8217;s ip, without port</dl>
<p> $s</p>
<dl>
<dd>server name (this can be the hostname)</dl>
<p> $u</p>
<dl>
<dd>user name (if guest, it is the user that guest is running as)</dl>
<p> $v</p>
<dl>
<dd>volume name (either ADEID_NAME or basename of path)</dl>
<p> $z</p>
<dl>
<dd>appletalk zone (may not exist)</dl>
<p> $$</p>
<dl>
<dd>prints dollar sign ($)</dl>
<p> When using variable substitution in the volume name, always keep in mind, not to exceed the 27 characters limit </p>
<p> <code>Example. Using variable substitution when defining volumes</code> </p>
<dl>
<dd>
<pre>/home/groups/$g &quot;Groupdir for $g&quot;
~ &quot;$f is the best one&quot;</pre>
</dl>
<p> We define &quot;groupdirs&quot; for each primary group and use a personalized server name for homedir shares.</p>
<h2>Cnid Backends</h2>
<p>The AFP protocol mostly refers to files and directories by ID and not by name. Netatalk needs a way to store these ID&#8217;s in a persistent way, to achieve this several different CNID backends are available. The CNID Databases are by default located in the .AppleDB folder in the volume root. </p>
<p> cdb</p>
<dl>
<dd>&quot;Concurrent database&quot;, backend is based on Sleepycat&#8217;s Berkely DB. With this backend several <code>afpd</code> deamons access the CNID database directly. Berkeley DB locking is used to synchronize access, if more than one <code>afpd</code> process is active for a volume. The drawback is, that the crash of a single <code>afpd</code> process might corrupt the database.</dl>
<p> dbd</p>
<dl>
<dd>Access to the CNID database is restricted to the <code>cnid_metad</code> daemon process. <code>afpd</code> processes communicate with the daemon for database reads and updates. If built with Berkeley DB transactions the probability for database corruption is practically zero, but performance can be slower than with <code>cdb</code></dl>
<p> last</p>
<dl>
<dd>This backend is an exception, in terms of ID persistency. ID&#8217;s are only valid for the current session. This is basically what <code>afpd</code> did in the 1.5 (and 1.6) versions. This backend is still available, as it is useful for e.g. sharing cdroms. </p>
<p> <code>Warning</code>: It is <i>NOT</i> recommended to use this backend for volumes anymore, as <code>afpd</code> now relies heavily on a persistent ID database. Aliases will likely not work and filename mangling is not supported.</dl>
<p> Even though <code>./configure &#8211;help</code> might show that there are other CNID backends available, be warned those are likely broken or mainly used for testing. Don&#8217;t use them unless you know what you&#8217;re doing, they may be removed without further notice from future versions.</p>
<h2>Charset Options</h2>
<p>With OS X Apple introduced the AFP3 protocol. One of the most important changes was that AFP3 uses unicode names encoded as UTF-8 decomposed. Previous AFP/OS versions used codepages, like MacRoman, MacCentralEurope, etc. </p>
<p> <code>afpd</code> needs a way to preserve extended macintosh characters, or characters illegal in unix filenames, when saving files on a unix filesystem. Earlier versions used the the so called CAP encoding. An extended character (&gt;0x7F) would be converted to a :xx sequence, e.g. the Apple Logo (MacRoman: 0XF0) was saved as :f0. Some special characters will be converted as to :xx notation as well. &#8216;/&#8217; will be encoded to :2f, if <code>-usedots</code> is not specified, a leading dot &#8216;.&#8217; will be encoded as :2e. </p>
<p> This version now uses UTF-8 as the default encoding for names. Special characters, like &#8216;/&#8217; and a leading &#8216;.&#8217; will still be CAP style encoded . </p>
<p> The <code>-volcharset</code> option will allow you to select another volume encoding. E.g. for western users another useful setting could be -volcharset ISO-8859-15. <code>apfd</code> will accept any <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) provided charset. If a character cannot be converted from the mac codepage to the selected volcharset, afpd will save it as a CAP encoded character. For AFP3 clients, <code>afpd</code> will convert the UTF-8 character to <code>-maccharset</code> first. If this conversion fails, you&#8217;ll receive a -50 error on the mac. </p>
<p> <i>Note</i>: Whenever you can, please stick with the default UTF-8 volume format.</p>
<h2>Compatibility With Earlier Versions</h2>
<p>To use a volume created with an earlier <code>afpd</code> version, you&#8217;ll have to specify the following options: </p>
<p> <code>Example. use a 1.x style volume</code> </p>
<dl>
<dd>
<pre>/path/to/volume &quot;Volname&quot; adouble:v1 volcharset:ASCII</pre>
</dl>
<p> In case you used an NLS you could try using a compatible iconv charset for <code>-volcharset</code>. </p>
<p> <code>Example. use a 1.x style volume, created with maccode.iso8859-1</code> </p>
<dl>
<dd>
<pre>/path/to/volume &quot;Volname&quot; adouble:v1 volcharset:ISO-8859-1</pre>
</dl>
<p> You should consider converting old style volumes to the new UTF-8/AD2 format. The safest way to do this, is to create a new volume with the default options and copy the files between this volumes with a mac. </p>
<p> <i>Note</i>: Using above example options will allow you to downgrade to 1.x netatalk again. </p>
<p> <i>Note</i>: Some 1.x NLS files used non standard mappings, e.g. maccode.iso8859-1.adapted. This is not supported anymore. You&#8217;ll have to copy the contents of those volumes files to a Mac and then back to the netatalk server, preferably to an UTF-8 volume.</p>
<h2>Advanced Options</h2>
<p>The following options should only be used after serious consideration. Be sure you fully understood the, sometimes complex, consequences, before using them. </p>
<p> casefold:<code>[option]</code></p>
<dl>
<dd>The casefold option handles, if the case of filenames should be changed. The available options are: </p>
<p> <code>tolower</code> &#8211; Lowercases names in both directions. </p>
<p> <code>toupper</code> &#8211; Uppercases names in both directions. </p>
<p> <code>xlatelower</code> &#8211; Client sees lowercase, server sees uppercase. </p>
<p> <code>xlateupper</code> &#8211; Client sees uppercase, server sees lowercase.</dl>
<p> options:[<code>option</code>]</p>
<dl>
<dd>This allows multiple options to be specified in a comma delimited format. The available options are: </p>
<p> cachecnid</p>
<dl>
<dd>If set <code>afpd</code> uses the ID information stored in AppleDouble V2 header files to reduce database load. Don&#8217;t set this option if the volume is modified by non AFP clients (NFS/SMB/local). Defaults to off.</dl>
<p> crlf</p>
<dl>
<dd>Enables crlf translation for TEXT files, automatically converting macintosh line breaks into Unix ones. Use of this option might be dangerous since some older programs store binary data files as type &quot;TEXT&quot; when saving and switch the filetype in a second step. <code>Afpd</code> will potentially destroy such files when &quot;erroneously&quot; changing bytes in order to do line break translation.</dl>
<p> dropbox</p>
<dl>
<dd>Allows a volume to be declared as being a &quot;dropbox.&quot; Note that netatalk must be compiled with dropkludge support for this to function. <i>Warning</i>: This option is deprecated and might not work as expected.</dl>
<p> mswindows</p>
<dl>
<dd>Forces filename restrictions imposed by MS WinXX. <i>Warning</i>: This is <i>NOT</i> recommened for volumes mainly used by Macs. Please make sure you fully understand this option before using it. </p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 This option breaks direct saving to netatalk volumes from some applications, i.e. OfficeX. </p>
</dl>
</dl>
<p> noadouble</p>
<dl>
<dd>Forces <code>afpd</code> to not create .AppleDouble directories unless macintosh metadata needs to be written. This option is only useful if you want to share files mostly used NOT by macs, causing <code>afpd</code> to not automatically create .AppleDouble subdirs containing AD header files in every directory it enters (which will it do by default). </p>
<p> In case, you save or change files from mac clients, AD metadata files have to be written even in case you set this option. So you can&#8217;t avoid the creation of .AppleDouble directories and its contents when you give macs write access to a share and they make use of it. </p>
<p> Try to avoid <code>noadouble</code> whenever possible.</dl>
<p> nodev</p>
<dl>
<dd>always use 0 for device number, helps when the device number is not constant across a reboot, cluster, &#8230;</dl>
<p> nofileid</p>
<dl>
<dd>don&#8217;t advertise createfileid, resolveid, deleteid calls.</dl>
<p> nohex</p>
<dl>
<dd>Disables :hex translations for anything except dot files. This option makes the &#8216;/&#8217; character illegal.</dl>
<p> nostat</p>
<dl>
<dd>don&#8217;t stat volume path when enumerating volumes list, useful for automounting or volumes created by a preexec script.</dl>
<p> prodos</p>
<dl>
<dd>Provides compatibility with Apple II clients.</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-afpd-conf/">afpd.conf</a></code>(5), <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) </p>
