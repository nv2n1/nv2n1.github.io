---
title: "dconf(7)"
name: "dconf"
section: "7"
letter: "d"
url: "/docs/linux/man/7-dconf/"
description: "dconf – A configuration system"
---

<p>dconf &#8211; A configuration system</p>
<h2>Description</h2>
<p>dconf is a simple key/value storage system that is heavily optimised for reading. This makes it an ideal system for storing user preferences (which are read 1000s of times for each time the user changes one). It was created with this usecase in mind. </p>
<p> All preferences are stored in a single large binary file. Layering of preferences is possible using multiple files (ie: for site defaults). Lock-down is also supported. The binary file for the defaults can optionally be compiled from a set of plain text keyfiles. </p>
<p> dconf has a partial client/server architecture. It uses D-Bus. The server is only involved in writes (and is not activated in the user session until the user modifies a preference). The service is stateless and can exit freely at any time (and is therefore robust against crashes). The list of paths that each process is watching is stored within the D-Bus daemon itself (as D-Bus signal match rules). </p>
<p> Reads are performed by direct access (via mmap) to the on-disk database which is essentially a hashtable. For this reason, dconf reads typically involve zero system calls and are comparable to a hashtable lookup in terms of speed. Practically speaking, in simple non-layered setups, dconf is less than 10 times slower than GHashTable. </p>
<p> Writes are assumed only to happen in response to explicit user interaction (like clicking on a checkbox in a preferences dialog) and are therefore not optimised at all. On some file systems, dconf-service will call fsync() for every write, which can introduce a latency of up to 100ms. This latency is hidden by the client libraries through a clever &quot;fast&quot; mechanism that records the outstanding changes locally (so they can be read back immediately) until the service signals that a write has completed. </p>
<p> The binary database format that dconf uses by default is not suitable for use on NFS, where mmap does not work well. To handle this common use case, dconf can be configured to place its binary database in <code>XDG_RUNTIME_DIR</code> (which is guaranteed to be local, but non-persistent) and synchronize it with a plain text keyfile in the users home directory.</p>
<h2>Profiles</h2>
<p>A profile is a list of configuration databases that dconf consults to find the value for a key. The user&#8217;s personal database always takes the highest priority, followed by the system databases in the order prescribed by the profile. </p>
<p> On startup, dconf consults the <code>DCONF_PROFILE</code> environment variable. If set, dconf will attempt to open the named profile, aborting if that fails. If the environment variable is not set, it will attempt to open the profile named &quot;user&quot; and if that fails, it will fall back to an internal hard-wired configuration. dconf stores its profiles in text files. <code>DCONF_PROFILE</code> can specify a relative path to a file in /etc/dconf/profile/, or an absolute path (such as in a user&#8217;s home directory). The profile name can only use alphanumeric characters or &#8216;_&#8217;. </p>
<p> A profile file might look like the following: </p>
<dl>
<dd>
<pre>user-db:user
system-db:local
system-db:site</pre>
</dl>
<p> Each line in a profile specifies one dconf database. The first line indicates the database used to write changes, and the remaining lines indicate read-only databases. (The first line should specify a user-db or service-db, so that users can actually make configuration changes.) </p>
<p> A &quot;user-db&quot; line specifies a user database. These databases are found in <code>$XDG_CONFIG_HOME</code>/dconf/. The name of the file to open in that directory is exactly as it is written in the profile. This file is expected to be in the binary dconf database format. Note that <code>XDG_CONFIG_HOME</code> cannot be set/modified per terminal or session, because then the writer and reader would be working on different DBs (the writer is started by DBus and cannot see that variable). </p>
<p> A &quot;service-db&quot; line instructs dconf to place the binary database file for the user database in <code>XDG_RUNTIME_DIR</code>. Since this location is not persistent, the rest of the line instructs dconf how to store the database persistently. A typical line is service-db:keyfile/user, which tells dconf to synchronize the binary database with a plain text keyfile in <code>$XDG_CONFIG_HOME</code>/dconf/user.txt. The synchronization is bi-directional. </p>
<p> A &quot;system-db&quot; line specifies a system database. These databases are found in /etc/dconf/db/. Again, the name of the file to open in that directory is exactly as it is written in the profile and the file is expected to be in the dconf database format. </p>
<p> If the <code>DCONF_PROFILE</code> environment variable is unset and the &quot;user&quot; profile can not be opened, then the effect is as if the profile was specified by this file: </p>
<dl>
<dd>
<pre>user-db:user</pre>
</dl>
<p> That is, the user&#8217;s personal database is consulted and there are no system settings.</p>
<h2>Key Files</h2>
<p>To facilitate system configuration with a text editor, dconf can populate databases from plain text keyfiles. For any given system database, keyfiles can be placed into the /etc/dconf/db/<i>database</i>.d/ directory. The keyfiles contain groups of settings as follows: </p>
<dl>
<dd>
<pre># Some useful default settings for our site
[system/proxy/http]
host='172.16.0.1'
enabled=true
[org/gnome/desktop/background]
picture-uri='file:///usr/local/rupert-corp/company-wallpaper.jpeg'</pre>
</dl>
<p> After changing keyfiles, the database needs to be updated with the <code><a href="/docs/linux/man/1-dconf/">dconf</a></code>(1) tool.</p>
<h2>Locks</h2>
<p>System databases can contain &#8216;locks&#8217; for keys. If a lock for a particular key or subpath is installed into a database then no database listed above that one in the profile will be able to modify any of the affected settings. This can be used to enforce mandatory settings. </p>
<p> To add locks to a database, place text files in the /etc/dconf/db/<i>database</i>.d/locks directory, where <i>database</i> is the name of a system database, as specified in the profile. The files contain list of keys to lock, on per line. Lines starting with a # are ignored. Here is an example: </p>
<dl>
<dd>
<pre># prevent changes to the company wallpaper
/org/gnome/desktop/background/picture-uri</pre>
</dl>
<p> After changing locks, the database needs to be updated with the <code><a href="/docs/linux/man/1-dconf/">dconf</a></code>(1) tool.</p>
<h2>Portability</h2>
<p>dconf mostly targets Free Software operating systems. It will theoretically run on Mac OS but there isn&#8217;t much point to that (since Mac OS applications want to store preferences in plist files). It is not possible to use dconf on Windows because of the inability to rename over a file that&#8217;s still in use (which is what the dconf-service does on every write).</p>
<h2>Api Stability</h2>
<p>The dconf API is not particularly friendly, and is not guaranteed to be stable. Because of this and the lack of portability, you almost certainly want to use some sort of wrapper API around it. The wrapper API used by GTK+ and GNOME applications is m[blue]<code>GSettings</code>m[]<font SIZE="-2">[1]</font>, which is included as part of GLib. GSettings has backends for Windows (using the registry) and Mac OS (using property lists) as well as its dconf backend and is the proper API to use for graphical applications.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dconf-service/">dconf-service</a></code>(1), <code><a href="/docs/linux/man/1-dconf-editor/">dconf-editor</a></code>(1), <code><a href="/docs/linux/man/1-dconf/">dconf</a></code>(1), m[blue]<code>GSettings</code>m[]<font SIZE="-2">[1]</font></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>GSettings</p>
<dl>
<dd><a rel="nofollow" href="http://developer.gnome.org/gio/stable/GSettings.html">http://developer.gnome.org/gio/stable/GSettings.html</a></dl>
