---
title: "elektra(7)"
name: "elektra"
section: "7"
letter: "e"
url: "/docs/linux/man/7-elektra/"
description: "elektra – A framework to store configuration atoms hierarchically Library Linkage Architecture.PP The Elektra library (libelektra.so) has 2 layers: public methods and backend access, according to t..."
---

<p>elektra &#8211; A framework to store configuration atoms hierarchically Library Linkage Architecture.PP The Elektra library (<i>libelektra.so</i>) has 2 layers: public methods and backend access, according to the following architecture (these pictures were taken from the <i>Elektra presentation</i>[1]): When using local backends such as the filesys backend, all key access happens in the actual process space as bellow: A remote daemon backend is also possible as noted bellow: True Facts About Elektra</p>
<dl>
<dd>*It is much more an agreement then a piece of software. Relation is 99% to 1%.</dl>
<dl>
<dd>*It is a simple and consistent API to help software developers programatically store and retrieve global and user-specific configuration parameters.</dl>
<dl>
<dd>*All key-value pairs are stored in clear-text files, UTF-8 encoded. All old charsets are also supported, with automatic transparent conversion to and from UTF-8.</dl>
<dl>
<dd>*API supports change notifications and multiple backends.</dl>
<dl>
<dd>*It provides a unique namespace for all values. Anywhere, anytime, any program can preciselly access keys by their names. Security restrictions may obviously apply.</dl>
<dl>
<dd>*It is designed to be secure and lightweight, to let even early boot-stage programs like <code>/sbin/init</code> to use it, instead of <i>/etc/inittab</i> file.</dl>
<dl>
<dd>*It is designed to be easy to administrate with regular command line tools like <code>cat</code>, <code>vi</code>, <code>cp</code>, <code>ls</code>, <code>ln</code>. Its storage is 100% open.</dl>
<dl>
<dd>*It tries to set distribution-independent naming standards to store things like hardware configuration, networking, user&#8217;s session configuration, system&#8217;s mime-types, parameters for kernel modules, etc, that are generally stored under <i>/etc</i>.</dl>
<dl>
<dd>*It requires existing software to be changed to use its API. This will substitute hundreds of configuration-text-file parsing code, into clear Elektra&#8217;s API key-value access methods.</dl>
<dl>
<dd>*It is POSIX compliant. If it doesn&#8217;t compile and run easily on some POSIX system, it should be easily modified to do so.</dl>
<p> Elektra Is Not</p>
<dl>
<dd>*Is NOT something that accesses SQL/relational databases.</dl>
<dl>
<dd>*Is NOT an OS service that can become unavailable and make system unusable. It is just a library to access files according to a namespace.</dl>
<dl>
<dd>*Is NOT an alternative to network information systems like LDAP or NIS. These are still required for networked environments.</dl>
<dl>
<dd>*Is NOT a Webmin-like or other GUI tool to be used by end users.</dl>
<dl>
<dd>*Is NOT an additional software layer to edit/generate existing configuration files.</dl>
<dl>
<dd>*Is NOT a &quot;configuration system&quot;, because one can&#8217;t be created by simply writing some code. A configuration system is an ecosystem, and the Elektra Project tries to help build one.</dl>
<dl>
<dd>*It doesn&#8217;t know a thing about the semantics of each data it stores.</dl>
<p> Namespaces and Key Names.PP All keys are organized in a hierarchical tree with 2 Namespaces (subtrees) as showed by the picture: <code>system</code></p>
<dl>
<dd>Contains all subsystems and global application keys/configuration. Equivalent to files under <i>/etc</i> directory.</dl>
<p> <code>user</code></p>
<dl>
<dd>The current user&#8217;s keys. Equivalent to the dotfiles in a user&#8217;s <code>$HOME</code> directory. These keys are phisically stored under the owner user home directory. The many <i>user:</i><i>username</i> in the picture shows the full name of those trees. Read about user domains bellow for more.</dl>
<p> User Domains.PP Different from the <i>system</i> namespace, the <i>user</i> namespace is dynamic. For example, the key <i>user/env/PATH</i> may have completely different values for users <i>luciana</i> and <i>valeria</i>. In this example, if <i>valeria</i> wants to access this key at <i>luciana</i>&#8216;s space, it should refer to <i>user:luciana/env/PATH</i>. Access permissions apply. User domains were implemented also to address situations when different user names (<code>$USER</code>) have same UID. So a user key is stored in his home directory based on the user name, not the UID. Inactive Keys.PP A great thing about text configuration files is that some configuration items can be there as an example, but inactive or commented. Elektra provides a very simple way to simulate this behavior: if the key name begins with a dot (.), it is considered inactive or commented. In real world applications, the Elektra API will ignore these keys by default, but the keys are still accessible if the developer wants to. These are some keys that have inactive subtrees:</p>
<dl>
<dd>*<i>system/sw/XFree/InputDevice/.Mouse3/Driver</i>: All keys under <i>.Mouse3/*</i> subtree won&#8217;t be read by default.</dl>
<dl>
<dd>*<i>user:valeria/env/env2/.PATH</i>: The <code>$PATH</code> environment variable <i>won&#8217;t</i> be set when <i>valeria</i> login.</dl>
<dl>
<dd>*<i>system/users/.louis/uid</i>: The entire <i>.louis/*</i> subtree is inactive. This is the same as commenting the user entry from a configuration file.</dl>
<p> See bellow more examples of inactive keys. Key Examples.PP Here are some valid key names, and their values: The Elektra keys of the combined <i>/etc/passwd</i> and <i>/etc/shadow</i> entry for user &#8216;nobody&#8217; would look like:</p>
<dl>
<dd>*<i>system/users/nobody/uid</i>: 99</dl>
<dl>
<dd>*<i>system/users/nobody/gid</i>: 99</dl>
<dl>
<dd>*<i>system/users/nobody/gecos</i>: Nobody</dl>
<dl>
<dd>*<i>system/users/nobody/home</i>: /</dl>
<dl>
<dd>*<i>system/users/nobody/shell</i>: /sbin/nologin</dl>
<dl>
<dd>*<i>system/users/nobody/password</i>: *</dl>
<dl>
<dd>*<i>system/users/nobody/passwdChangeBefore</i>: 0</dl>
<dl>
<dd>*<i>system/users/nobody/passwdChangeAfter</i>: 99999</dl>
<dl>
<dd>*<i>system/users/nobody/passwdWarnBefore</i>: 7</dl>
<dl>
<dd>*<i>system/users/nobody/passwdDisableAfter</i>:</dl>
<dl>
<dd>*<i>system/users/nobody/passwdDisabledSince</i>:</dl>
<dl>
<dd>*<i>system/users/nobody/passwdReserved</i>:</dl>
<p> The environment variables I want set, when I log in, with their full key name:</p>
<dl>
<dd>*<i>user:aviram/env/env1/JAVA_HOME</i>: /usr/lib/jvm/java-1.4.1-ibm-1.4.1.0/jre</dl>
<dl>
<dd>*<i>user:aviram/env/env2/PATH</i>: $PATH:~/bin:$JAVA_HOME/bin</dl>
<dl>
<dd>*<i>user:aviram/env/env2/PS1</i>: \h:\w\$</dl>
<dl>
<dd>*<i>user:aviram/env/env3/PILOTRATE</i>: 57600</dl>
<p> The entry in <i>/etc/inittab</i> that is responsible for starting X11 would look:</p>
<dl>
<dd>*<i>system/init/x/runlevels</i>: 5</dl>
<dl>
<dd>*<i>system/init/x/action</i>: respawn</dl>
<dl>
<dd>*<i>system/init/x/process</i>: /etc/X11/prefdm -nodaemon</dl>
<p> The users database files and <i>/etc/inittab</i> were Elektrified to key-value pairs using the <code>users-convert</code> and <code>inittab-convert</code> scripts included with the distribution. An example of an elektrified <i>/etc/X11/xorg.conf</i> or <i>/etc/X11/XF86Config</i>:</p>
<dl>
<dd>*<i>system/sw/xorg/current/Layouts/Default Layout/Inputs/Keyboard0/CoreKeyboard</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Layouts/Default Layout/Inputs/Mouse0/CorePointer</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Layouts/Default Layout/Screens/Screen0/Absolute.x</i>: 0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Layouts/Default Layout/Screens/Screen0/Absolute.y</i>: 0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Layouts/Default Layout/Screens/Screen0/ScreenNumber</i>: 0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Files/FontPath</i>: unix/:7100</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Files/RgbPath</i>: /usr/X11R6/lib/X11/rgb</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Devices/Videocard0/BoardName</i>: Intel 740 (generic)</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Devices/Videocard0/Driver</i>: i740</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Devices/Videocard0/VendorName</i>: Videocard vendor</dl>
<dl>
<dd>*<i>system/sw/xorg/current/InputDevices/Keyboard0/Driver</i>: keyboard</dl>
<dl>
<dd>*<i>system/sw/xorg/current/InputDevices/Keyboard0/Options/XkbLayout</i>: us_intl</dl>
<dl>
<dd>*<i>system/sw/xorg/current/InputDevices/Keyboard0/Options/XkbModel</i>: pc105</dl>
<dl>
<dd>*<i>system/sw/xorg/current/InputDevices/Mouse0/Driver</i>: mouse</dl>
<dl>
<dd>*<i>system/sw/xorg/current/InputDevices/Mouse0/Options/Device</i>: /dev/input/mice</dl>
<dl>
<dd>*<i>system/sw/xorg/current/InputDevices/Mouse0/Options/Emulate3Buttons</i>: yes</dl>
<dl>
<dd>*<i>system/sw/xorg/current/InputDevices/Mouse0/Options/Protocol</i>: IMPS/2</dl>
<dl>
<dd>*<i>system/sw/xorg/current/InputDevices/Mouse0/Options/ZAxisMapping</i>: 4 5</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/Monitor0/DisplaySize.height</i>: 230</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/Monitor0/DisplaySize.width</i>: 300</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/Monitor0/HorizSync</i>: 30.0 &#8211; 61.0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/Monitor0/ModelName</i>: SyncMaster</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/Monitor0/Options/dpms</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/Monitor0/VendorName</i>: Monitor Vendor</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/Monitor0/VertRefresh</i>: 56.0 &#8211; 75.0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/.Monitor1/HorizSync</i>: 30.0 &#8211; 61.0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/.Monitor1/ModelName</i>: Impression</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/.Monitor1/Options/dpms</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/.Monitor1/VendorName</i>: Monitor Vendor</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Monitors/.Monitor1/VertRefresh</i>: 56.0 &#8211; 75.0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Screens/Screen0/DefaultDepth</i>: 16</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Screens/Screen0/Device</i>: Videocard0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Screens/Screen0/Displays/00/Depth</i>: 16</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Screens/Screen0/Displays/00/Modes</i>: 1024&#215;768,800&#215;600,640&#215;480</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Screens/Screen0/Displays/00/Viewport.x</i>: 0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Screens/Screen0/Displays/00/Viewport.y</i>: 0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Screens/Screen0/Monitor</i>: Monitor0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Modules/dbe</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Modules/dri</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Modules/extmod</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Modules/fbdevhw</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Modules/freetype</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Modules/glx</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Modules/record</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/Modules/type1</i>:</dl>
<dl>
<dd>*<i>system/sw/xorg/current/DRI/Group</i>: 0</dl>
<dl>
<dd>*<i>system/sw/xorg/current/DRI/Mode</i>: 0666</dl>
<p> Pay attention that the keys bellow <i>system/sw/XFree/current/Monitor/.Monitor1</i> are inactive because we have <i>.Monitor1</i> as their parent. So unless special options are used when calling the API, these keys will not be retrieved from the database. Throughout this text you will see other examples of key names. Key Data Types.PP There are only two types of data that can be stored: <code>Text</code></p>
<dl>
<dd>Handled as pure text. Regardeless of the charset being used, these values are always stored as UTF-8. This ensures very strong internationalization and migration capabilities, while keeping simplicity. If you don&#8217;t want the Elektra framework to convert your non-ASCII text to UTF-8 (not recomended), you should use the Binary data format.</dl>
<p> <code>Binary</code></p>
<dl>
<dd>A stream of bytes, not necessarily text. It is recommended that you avoid using binary values because UNIX system administrators tend to consider them as unmanageable blackboxes. Anyway, the value will be encoded into pure text format based on hexadecimal digits, for openness and ease of administration. This data type should also be avoided because it is less efficient.</dl>
<p> There are very good reasons why types like <code>Integer</code>, <code>Time</code>, <code>Font</code>, <code>List</code>, etc were not implemented: Elektra was designed to be usefull for any type of program, so having more specific data types implicates in the definition of value limits, separators in the storage format, etc, that may be good for some application and bad for other. So the semantics of the data is handled by the application. A program or framework may define its own special data handling methods using these essential basic types. See the <code>keyGetType()</code> and <code>keySetType()</code> methods documentation in the <code></p>
<p><a href="/docs/linux/man/3-kdb/">kdb</a></code>(3) man page to understand how to set keys with your own data types. There are more two types of keys: <code>Directory</code></p>
<dl>
<dd>It can&#8217;t store a value, but, as a directory in a filesystem, it serves as a way to group correlated keys.</dl>
<p> <code>Link</code></p>
<dl>
<dd>It is a link to another key. They work as symbolic links in the filesystem: when trying to access them, you will actually access the key they point to. The API also provides ways to access these special keys without dereferencing them.</dl>
<p> Key Meta Data.PP Besides the key name and the value, each key has other attributes: <code>Owner&#8217;s User and Group</code></p>
<dl>
<dd>This is a system&#8217;s UID and GID equal to the ones found in regular files&#8217; attributes.</dl>
<p> <code>Access Permissions</code></p>
<dl>
<dd>Filesystem-like access permissions for user, group and others.</dl>
<p> <code>Modification, Access and Stat Times</code></p>
<dl>
<dd>Last time a key was modified, readed and stated (listed), respectively.</dl>
<p> <code>Key Comment</code></p>
<dl>
<dd>Pretty much as a configuration file comment. Not intended to be used in GUI applications, because it isn&#8217;t internationalizable.</dl>
<p> Fine Grained Security Example.PP To show this metadata in action, this screen shows the <code>kdb</code> command listing keys and their attributes related to user <i>nobody</i>.</p>
<dl>
<dd>
<pre>bash$ <code>kdb ls -Rlv system/users/nobody</code>
-rw-r--r-- root root 17 Mar 31 09:07 system/users/nobody/uid=99
-rw-r--r-- root root 17 Mar 31 09:07 system/users/nobody/gid=99
-rw-r--r-- root root 21 Mar 31 09:07 system/users/nobody/gecos=Nobody
-rw-r--r-- root root 16 Mar 31 09:07 system/users/nobody/home=/
-rw-r--r-- root root 28 Mar 31 09:07 system/users/nobody/shell=/sbin/nologin
-rw------- root root 16 Mar 31 09:07 system/users/nobody/password
-rw------- root root 16 Mar 31 09:07 system/users/nobody/passwdChangeBefore
-rw------- root root 20 Mar 31 09:07 system/users/nobody/passwdChangeAfter
-rw------- root root 16 Mar 31 09:07 system/users/nobody/passwdWarnBefore
-rw------- root root 15 Mar 31 09:07 system/users/nobody/passwdDisableAfter
-rw------- root root 15 Mar 31 09:07 system/users/nobody/passwdDisabledSince
-rw------- root root 15 Mar 31 09:07 system/users/nobody/passwdReserved</pre>
</dl>
<p> We ran the <code>kdb</code> command without super-user credentials, asking for long (<code>-l</code>), recursive (<code>-R</code>) listing, and to show each key value (<code>-v</code>). But (since we are) regular user, we don&#8217;t have permission to see the values of the <i>system/users/nobody/passwd*</i> fields. The users database files were elektrified to key-value pairs using the <code>users-convert</code> script included with the distribution. ExamplesSetting Keys.PP bash$<code>kdb set -c &quot;My first key&quot; user/example/key &quot;Some nice value&quot;</code> bash$<code>kdb set user:luciana/example/key &#8212; &quot;Some &#8211; nice &#8211; value with dashes&quot;</code> </p>
<pre><code>bash#KDB_ROOT=user:http/sw/httpd kdb set -u nobody -g http key &quot;Some value&quot;</code></pre>
<p> bash$<code>kdb set -b image.png -t bin user/example/binaryKey</code> bash$<code>kdb set -b file.txt user/example/regularKey</code> bash#<code>kdb set -t link system/sw/XFree/current system/sw/XFree/handmade</code> Getting Keys.PP bash$<code>KDB_ROOT=user/example kdb get some/key/name</code> bash$<code>eval `kdb get -s user/env/env1/PS1`</code> bash$<code>KDB_BACKEND=gconf kdb get user/sw/gnome-terminal/global/active_encodings</code> Listing.PP bash$<code>kdb ls -laR user:valeria</code> bash$<code>kdb ls -lR system/sw/xorg/current</code> bash$<code>KDB_ROOT=system/sw kdb ls -lR xorg</code> bash$<code>KDB_BACKEND=fstab kdb ls -Rv system/filesystems</code> bash$<code>eval `kdb ls -Rvs user/env/env2`</code> Miscelaneous.PP bash#<code>kdb ln system/sw/xorg/handmade system/sw/xorg/current</code> bash#<code>kdb mv system/sw/xorg/current system/sw/xorg/old</code> bash#<code>kdb rm system/inittab/rc4</code> bash$<code>KDB_BACKEND=gconf kdb rm user/gconfKey</code> XML Import and Export.PP bash#<code>kdb export user/sw/app | sed -e &#8216;s|/app/|/app2/|g&#8217; | kdb import</code> bash#<code>KDB_ROOT=system/sw kdb export myapp &gt; myappconf.xml</code> bash#<code>kdb import myappconf.xml</code> bash$<code>KDB_BACKEND=gconf kdb export user/sw</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-kdb/">kdb</a></code>(1), <code><a href="/docs/linux/man/5-elektra/">elektra</a></code>(5)</p>
<h2>Author</h2>
<p><code>Avi Alkalay</code> &lt;avi at unix.sh&gt;<br />
 Linux Market Developer, Senior IT and Software Architect, IBM Linux Impact Team :: <i>ibm.com/linux</i> </p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2004 Avi Alkalay</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Elektra presentation</p>
<dl>
<dd>elektra.sxi</dl>
