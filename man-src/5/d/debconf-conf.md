---
title: "debconf-conf(5)"
name: "debconf-conf"
section: "5"
letter: "d"
url: "/docs/linux/man/5-debconf-conf/"
description: "debconf.conf – debconf configuration file"
---

<p>debconf.conf &#8211; debconf configuration file</p>
<h2>Description</h2>
<p>Debconf is a configuration system for Debian packages. /etc/debconf.conf and ~/.debconfrc are configuration files debconf uses to determine which databases it should use. These databases are used for storing two types of information; dynamic config data the user enters into it, and static template data. Debconf offers a flexible, extensible database backend. New drivers can be created with a minimum of effort, and sets of drivers can be combined in various ways.</p>
<h2>Synopsis</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>This is a sample config file that is<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sufficient to use debconf.<br />
&nbsp;<wbr>&nbsp;<wbr>Config: configdb<br />
&nbsp;<wbr>&nbsp;<wbr>Templates: templatedb </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: configdb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: File<br />
&nbsp;<wbr>&nbsp;<wbr>Filename:&nbsp;<wbr>/var/cache/debconf/config.dat </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: templatedb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: File<br />
&nbsp;<wbr>&nbsp;<wbr>Mode: 644<br />
&nbsp;<wbr>&nbsp;<wbr>Filename:&nbsp;<wbr>/var/cache/debconf/templates.dat</p>
<h2>File Format</h2>
<p>The format of this file is a series of stanzas, each separated by at least one wholly blank line. Comment lines beginning with a &quot;#&quot; character are ignored. </p>
<p> The first stanza of the file is special, is used to configure debconf as a whole. Two fields are required to be in this first stanza:</p>
<dl>
<dd>
<dl>
<dt><code>Config</code></p>
<dd>Specifies the name of the database from which to load config data.</p>
<dt><code>Templates</code></p>
<dd>Specifies the name of the database to use for the template cache.</dl>
</dl>
<p> Additional fields that can be used include:</p>
<dl>
<dd>
<dl>
<dt><code>Frontend</code></p>
<dd>The frontend Debconf should use, overriding any frontend set in the debconf database.</p>
<dt><code>Priority</code></p>
<dd>The priority Debconf should use, overriding any priority set in the debconf database.</p>
<dt><code>Admin-Email</code></p>
<dd>The email address Debconf should send mail to if it needs to make sure that the admin has seen an important message. Defaults to &quot;root&quot;, but can be set to any valid email address to send the mail there. If you prefer to never have debconf send you mail, specify a blank address. This can be overridden on the fly with the DEBCONF_ADMIN_EMAIL environment variable.</p>
<dt><code>Debug</code></p>
<dd>If set, this will cause debconf to output debugging information to standard error. The value it is set to can be something like &quot;user&quot;, &quot;developer&quot;, &quot;db&quot;, or a regular expression. Typically, rather than setting it permanently in a config file, you will only want to temporarily turn on debugging, and the DEBCONF_DEBUG environment variable can be set instead to accomplish that.</p>
<dt><code>NoWarnings</code></p>
<dd>If set, this will make debconf not display warnings about various things. This can be overridden on the fly with the DEBCONF_NOWARNINGS environment variable.</p>
<dt><code>Log</code></p>
<dd>Makes debconf log debugging information as it runs, to the syslog. The value it is set to controls that is logged. See Debug, above for an explanation of the values that can be set to control what is logged.</p>
<dt><code>Terse</code></p>
<dd>If set to &quot;true&quot;, makes some debconf frontends use a special terse display mode that outputs as little as possible. Defaults to false. Terse mode may be temporarily set via the DEBCONF_TERSE environment variable.</dl>
</dl>
<p> For example, the first stanza of a file might look like this:<br />
&nbsp;<wbr>&nbsp;<wbr>Config: configdb<br />
&nbsp;<wbr>&nbsp;<wbr>Templates: templatedb </p>
<p> Each remaining stanza in the file sets up a database. A database stanza begins by naming the database:<br />
&nbsp;<wbr>&nbsp;<wbr>Name: configdb </p>
<p> Then it indicates what database driver should be used for this database. See DRIVERS, below, for information about what drivers are available.<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: File </p>
<p> You can indicate that the database is not essential to the proper functioning of debconf by saying it is not required. This will make debconf muddle on if the database fails for some reason.<br />
&nbsp;<wbr>&nbsp;<wbr>Required: false </p>
<p> You can mark any database as readonly and debconf will not write anything to it.<br />
&nbsp;<wbr>&nbsp;<wbr>Readonly: true </p>
<p> You can also limit what types of data can go into the database with Accept- and Reject- lines; see ACCESS CONTROLS, below. </p>
<p> The remainder of each database stanza is used to provide configuration specific to that driver. For example, the Text driver needs to know a directory to put the database in, so you might say:<br />
&nbsp;<wbr>&nbsp;<wbr>Filename:&nbsp;<wbr>/var/cache/debconf/config.dat</p>
<h2>Drivers</h2>
<p>A number of drivers are available, and more can be written with little difficulty. Drivers come in two general types. First there are real drivers &#8212; drivers that actually access and store data in some kind of database, which might be on the local filesystem, or on a remote system. Then there are meta-drivers that combine other drivers together to form more interesting systems. Let&#8217;s start with the former.</p>
<dl>
<dt>
<dt><code>File</code></p>
<dd>
<dd>
<dl>
<dd>This database driver allows debconf to store a whole database in a single flat text file. This makes it easy to archive, transfer between machines, and edit. It is one of the more compact database formats in terms of disk space used. It is also one of the slowest. </p>
<p> On the downside, the entire file has to be read in each time debconf starts up, and saving it is also slow. </p>
<p> The following things are configurable for this driver.</p>
<dl>
<dd>
<dl>
<dt><code>Filename</code></p>
<dd>The file to use as the database. This is a required field.</p>
<dt><code>Mode</code></p>
<dd>The permissions to create the file with if it does not exist. Defaults to 600, since the file could contain passwords in some circumstances.</p>
<dt><code>Format</code></p>
<dd>The format of the file. See FORMATS below. Defaults to using a rfc-822 like format.</p>
<dt><code>Backup</code></p>
<dd>Whether a backup should be made of the old file before changing it. Defaults to true.</dl>
</dl>
<p> As example stanza setting up a database using this driver: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: mydb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: File<br />
&nbsp;<wbr>&nbsp;<wbr>Filename:&nbsp;<wbr>/var/cache/debconf/mydb.dat</dl>
<dt><code>DirTree</code></p>
<dd>
<dl>
<dd>This database driver allows debconf to store data in a hierarchical directory structure. The names of the various debconf templates and questions are used as-is to form directories with files in them. This format for the database is the easiest to browse and fiddle with by hand. It has very good load and save speeds. It also typically occupies the most space, since a lot of small files and subdirectories do take up some additional room. </p>
<p> The following things are configurable for this driver.</p>
<dl>
<dd>
<dl>
<dt><code>Directory</code></p>
<dd>The directory to put the files in. Required.</p>
<dt><code>Extension</code></p>
<dd>An extension to add to the names of files. Must be set to a non-empty string; defaults to &quot;.dat&quot;</p>
<dt><code>Format</code></p>
<dd>The format of the file. See FORMATS below. Defaults to using a rfc-822 like format.</p>
<dt><code>Backup</code></p>
<dd>Whether a backup should be made of the old file before changing it. Defaults to true.</dl>
</dl>
<p> As example stanza setting up a database using this driver: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: mydb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: DirTree<br />
&nbsp;<wbr>&nbsp;<wbr>Directory:&nbsp;<wbr>/var/cache/debconf/mydb<br />
&nbsp;<wbr>&nbsp;<wbr>Extension: .txt</dl>
<dt><code>PackageDir</code></p>
<dd>
<dl>
<dd>This database driver is a compromise between the File and DirTree databases. It uses a directory, in which there is (approximately) one file per package that uses debconf. This is fairly fast, while using little more room than the File database driver. </p>
<p> This driver is configurable in the same ways as is the DirTree driver, plus:</p>
<dl>
<dt><code>Mode</code></p>
<dd>The permissions to create files with. Defaults to 600, since the files could contain passwords in some circumstances.</dl>
<p> As example stanza setting up a database using this driver: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: mydb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: PackageDir<br />
&nbsp;<wbr>&nbsp;<wbr>Directory:&nbsp;<wbr>/var/cache/debconf/mydb</dl>
<dt><code>LDAP</code></p>
<dd>
<dl>
<dd>WARNING: This database driver is currently experimental. Use with caution. </p>
<p> This database driver accesses a LDAP directory for debconf configuration data. Due to the nature of the beast, LDAP directories should typically be accessed in read-only mode. This is because multiple accesses can take place, and it&#8217;s generally better for data consistency if nobody tries to modify the data while this is happening. Of course, write access is supported for those cases where you do want to update the config data in the directory. </p>
<p> For information about setting up a LDAP server for debconf, read /usr/share/doc/debconf-doc/README.LDAP (from the debconf-doc package). </p>
<p> To use this database driver, you must have the libnet-ldap-perl package installed. Debconf suggests that package, but does not depend on it. </p>
<p> Please carefully consider the security implications of using a remote debconf database. Unless you trust the source, and you trust the intervening network, it is not a very safe thing to do. </p>
<p> The following things are configurable for this driver.</p>
<dl>
<dd>
<dl>
<dt><code>server</code></p>
<dd>The host name or IP address of an LDAP server to connect to.</p>
<dt><code>port</code></p>
<dd>The port on which to connect to the LDAP server. If none is given, the default port is used.</p>
<dt><code>basedn</code></p>
<dd>The DN under which all config items will be stored. Each config item will be assumed to live in a DN of cn=&lt;item name&gt;,&lt;Base DN&gt;. If this structure is not followed, all bets are off.</p>
<dt><code>binddn</code></p>
<dd>The DN to bind to the directory as. Anonymous bind will be used if none is specified.</p>
<dt><code>bindpasswd</code></p>
<dd>The password to use in an authenticated bind (used with binddn, above). If not specified, anonymous bind will be used.</dl>
<dl>
<dd>This option should not be used in the general case. Anonymous binding should be sufficient most of the time for read-only access. Specifying a bind DN and password should be reserved for the occasional case where you wish to update the debconf configuration data.</dl>
<dl>
<dt><code>keybykey</code></p>
<dd>Enable access to individual LDAP entries, instead of fetching them all at once in the beginning. This is very useful if you want to monitor your LDAP logs for specific debconf keys requested. In this way, you could also write custom handling code on the LDAP server part.</dl>
<dl>
<dd>Note that when this option is enabled, the connection to the LDAP server is kept active during the whole Debconf run. This is a little different from the all-in-one behavior where two brief connections are made to LDAP; in the beginning to retrieve all the entries, and in the end to save eventual changes.</dl>
</dl>
<p> An example stanza setting up a database using this driver, assuming the remote database is on example.com and can be accessed anonymously: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: ldapdb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: LDAP<br />
&nbsp;<wbr>&nbsp;<wbr>Readonly: true<br />
&nbsp;<wbr>&nbsp;<wbr>Server: example.com<br />
&nbsp;<wbr>&nbsp;<wbr>BaseDN: cn=debconf,dc=example,dc=com<br />
&nbsp;<wbr>&nbsp;<wbr>KeyByKey: 0 </p>
<p> Another example, this time the LDAP database is on localhost, and can be written to: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: ldapdb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: LDAP<br />
&nbsp;<wbr>&nbsp;<wbr>Server: localhost<br />
&nbsp;<wbr>&nbsp;<wbr>BaseDN: cn=debconf,dc=domain,dc=com<br />
&nbsp;<wbr>&nbsp;<wbr>BindPasswd: secret<br />
&nbsp;<wbr>&nbsp;<wbr>KeyByKey: 1</dl>
<dt><code>Pipe</code></p>
<dd>
<dl>
<dd>This special-purpose database driver reads and writes the database from standard input/output. It may be useful for people with special needs. </p>
<p> The following things are configurable for this driver.</p>
<dl>
<dd>
<dl>
<dt><code>Format</code></p>
<dd>The format to read and write. See FORMATS below. Defaults to using a rfc-822 like format.</p>
<dt><code>Infd</code></p>
<dd>File descriptor number to read from. Defaults to reading from stdin. If set to &quot;none&quot;, the database will not read any data on startup.</p>
<dt><code>Outfd</code></p>
<dd>File descriptor number to write to. Defaults to writing to stdout. If set to &quot;none&quot;, the database will be thrown away on shutdown.</dl>
</dl>
</dl>
</dl>
<p> That&#8217;s all of the real drivers, now moving on to meta-drivers..</p>
<dl>
<dt><code>Stack</code></p>
<dd>
<dl>
<dd>This driver stacks up a number of other databases (of any type), and allows them to be accessed as one. When debconf asks for a value, the first database on the stack that contains the value returns it. If debconf writes something to the database, the write normally goes to the first driver on the stack that has the item debconf is modifying, and if none do, the new item is added to the first writable database on the stack. </p>
<p> Things become more interesting if one of the databases on the stack is readonly. Consider a stack of the databases foo, bar, and baz, where foo and baz are both readonly. Debconf wants to change an item, and this item is only present in baz, which is readonly. The stack driver is smart enough to realize that won&#8217;t work, and it will copy the item from baz to bar, and the write will take place in bar. Now the item in baz is shadowed by the item in bar, and it will not longer be visible to debconf. </p>
<p> This kind of thing is particularly useful if you want to point many systems at a central, readonly database, while still allowing things to be overridden on each system. When access controls are added to the picture, stacks allow you to do many other interesting things, like redirect all passwords to one database while a database underneath it handles everything else. </p>
<p> Only one piece of configuration is needed to set up a stack: </p>
<dl>
<dd>
<dl>
<dt><code>Stack</code></p>
<dd>This is where you specify a list of other databases, by name, to tell it what makes up the stack.</dl>
</dl>
<p> For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: megadb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: stack<br />
&nbsp;<wbr>&nbsp;<wbr>Stack: passworddb, configdb, companydb </p>
<p> WARNING: The stack driver is not very well tested yet. Use at your own risk.</dl>
</dl>
<p> <code>Backup</code></p>
<dl>
<dd>This driver passes all requests on to another database driver. But it also copies all write requests to a backup database driver. </p>
<p> You must specify the following fields to set up this driver: </p>
<dl>
<dd>
<dl>
<dt><code>Db</code></p>
<dd>The database to read from and write to.</p>
<dt><code>Backupdb</code></p>
<dd>The name of the database to send copies of writes to.</dl>
</dl>
<p> For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Name: backup<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: Backup<br />
&nbsp;<wbr>&nbsp;<wbr>Db: mydb<br />
&nbsp;<wbr>&nbsp;<wbr>Backupdb: mybackupdb</dl>
<p> <code>Debug</code></p>
<dl>
<dd>This driver passes all requests on to another database driver, outputting verbose debugging output about the request and the result. </p>
<p> You must specify the following fields to set up this driver: </p>
<dl>
<dd>
<dl>
<dt><code>Db</code></p>
<dd>The database to read from and write to.</dl>
</dl>
</dl>
<h2>Access Controls</h2>
<p>When you set up a database, you can also use some fields to specify access controls. You can specify that a database only accepts passwords, for example, or make a database only accept things with &quot;foo&quot; in their name.</p>
<dl>
<dt><code>Readonly</code></p>
<dd>As was mentioned earlier, this access control, if set to &quot;true&quot;, makes a database readonly. Debconf will read values from it, but will never write anything to it.</p>
<dt><code>Accept-Name</code></p>
<dd>The text in this field is a perl-compatible regular expression that is matched against the names of items as they are requested from the database. Only if an items name matches the regular expression, will the database allow debconf to access or modify it.</p>
<dt><code>Reject-Name</code></p>
<dd>Like Accept-Name, except any item name matching this regular expression will be rejected.</p>
<dt><code>Accept-Type</code></p>
<dd>Another regular expression, this matches against the type of the item that is being accessed. Only if the type matches the regex will access be granted.</p>
<dt><code>Reject-Type</code></p>
<dd>Like Accept-Type, except any type matching this regular expression will be rejected.</dl>
<h2>Formats</h2>
<p>Some of the database drivers use format modules to control the actual format in which the database is stored on disk. These formats are currently supported:</p>
<dl>
<dt><code>822</code></p>
<dd>This is a file format loosely based upon the rfc-822 format for email message headers. Similar formats are used throughout Debian; in the dpkg status file, and so on.</dl>
<h2>Example</h2>
<p>Here is a more complicated example of a debconf.conf file.<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>This stanza is used for general debconf setup.<br />
&nbsp;<wbr>&nbsp;<wbr>Config: stack<br />
&nbsp;<wbr>&nbsp;<wbr>Templates: templates<br />
&nbsp;<wbr>&nbsp;<wbr>Log: developer<br />
&nbsp;<wbr>&nbsp;<wbr>Debug: developer<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>This is my own local database.<br />
&nbsp;<wbr>&nbsp;<wbr>Name: mydb<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: DirTree<br />
&nbsp;<wbr>&nbsp;<wbr>Directory:&nbsp;<wbr>/var/cache/debconf/config<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>This is another database that I use to hold<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>only X server configuration.<br />
&nbsp;<wbr>&nbsp;<wbr>Name: X<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: File<br />
&nbsp;<wbr>&nbsp;<wbr>Filename:&nbsp;<wbr>/etc/X11/debconf.dat<br />
&nbsp;<wbr>&nbsp;<wbr>Mode: 644<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>It&#8217;s sorta hard to work out what questions<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>belong to X;&nbsp;<wbr>it should be using a deeper<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>tree structure so I could just match on&nbsp;<wbr>^X/<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Oh well.<br />
&nbsp;<wbr>&nbsp;<wbr>Accept-Name: xserver|xfree86|xbase </p>
<pre><code># This is our company's global, read-only
# (for me!) debconf database.
Name: company
Driver: LDAP
Server: debconf.foo.com
BaseDN: cn=debconf,dc=foo,dc=com
BindDN: uid=admin,dc=foo,dc=com
BindPasswd: secret
Readonly: true
# I don't want any passwords that might be
# floating around in there.
Reject-Type: password
# If this db is not accessible for whatever
# reason, carry on anyway.
Required: false</code></pre>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>I use this database to hold<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>passwords safe and secure.<br />
&nbsp;<wbr>&nbsp;<wbr>Name: passwords<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: File<br />
&nbsp;<wbr>&nbsp;<wbr>Filename:&nbsp;<wbr>/etc/debconf/passwords<br />
&nbsp;<wbr>&nbsp;<wbr>Mode: 600<br />
&nbsp;<wbr>&nbsp;<wbr>Accept-Type: password<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Let&#8217;s put them all together<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>in a database stack.<br />
&nbsp;<wbr>&nbsp;<wbr>Name: stack<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: Stack<br />
&nbsp;<wbr>&nbsp;<wbr>Stack: passwords, X, mydb, company<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>So, all passwords go to the password database.<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>Most X configuration stuff goes to the X<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>database, and anything else goes to my main<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>database. Values are looked up in each of those<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>in turn, and if none has a particular value, it<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>is looked up in the company-wide LDAP database<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>(unless it&#8217;s a password).<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>A database is also used to hold templates. We&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>don&#8217;t need to make this as fancy.<br />
&nbsp;<wbr>&nbsp;<wbr>Name: templates<br />
&nbsp;<wbr>&nbsp;<wbr>Driver: File<br />
&nbsp;<wbr>&nbsp;<wbr>Mode: 644<br />
&nbsp;<wbr>&nbsp;<wbr>Format: 822<br />
&nbsp;<wbr>&nbsp;<wbr>Filename:&nbsp;<wbr>/var/cache/debconf/templates</p>
<h2>Notes</h2>
<p>If you use something like ${HOME} in this file, it will be replaced with the value of the named environment variable. </p>
<p> Environment variables can also be used to override the databases on the fly, see <code><a href="/docs/linux/man/7-debconf/">debconf</a></code>(7) </p>
<p> The field names (the part of the line before the colon) is case-insensitive. The values, though, are case sensitive.</p>
<h2>Planned Enhancements</h2>
<p>More drivers and formats. Some ideas include: A SQL driver, with the capability to access a remote database. A DHCP driver, that makes available some special things like hostname, IP address, and DNS servers. A driver that pulls values out of public DNS records TXT fields. A format that is compatible with the output of cdebconf. An override driver, which can override the value field or flags of all requests that pass through it.</p>
<h2>Files</h2>
<p>/etc/debconf.conf </p>
<p> ~/.debconfrc</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-debconf/">debconf</a></code>(7)</p>
<h2>Author</h2>
<p>Joey Hess &lt;joeyh [at] debian.org&gt;</p>
