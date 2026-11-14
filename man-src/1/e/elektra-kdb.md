---
title: "elektra-kdb(1)"
name: "elektra-kdb"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elektra-kdb/"
description: "kdb – Elektra key database command line administration tool"
---

<h2 class="name">NAME</h2>
<p> kdb &#8211; Elektra key database command line administration tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kdb get</code> [<code>-dlr</code>] key/name</p>
<dt> <code>kdb set</code> [<code>-t</code>&nbsp;<wbr><code>type</code>] [<code>-d</code>] [<code>-c</code>&nbsp;<wbr><code>&quot;A comment about this key&quot;</code>] [<code>-m</code>&nbsp;<wbr><code>mode</code>] [<code>-u</code>&nbsp;<wbr><code>uid</code>] [<code>-g</code>&nbsp;<wbr><code>gid</code>] key/name &quot;the value&quot;</p>
<dt> <code>kdb set</code> [<code>-t</code>&nbsp;<wbr><code>type</code>] [<code>-m</code>&nbsp;<wbr><code>mode</code>] [<code>-c</code>&nbsp;<wbr><code>&quot;A comment&quot;</code>] key/name &#8212; &quot;the value&quot;</p>
<dt> <code>kdb set</code> [<code>-t</code>&nbsp;<wbr><code>type</code>] [<code>-b</code>&nbsp;<wbr><code>file</code>] key/name</p>
<dt> <code>kdb ls</code> [<code>-lRfvs</code>] [key/dir | key/name]</p>
<dt> <code>kdb ls</code> [<code>-lRfvx</code>] [key/dir | key/name] &gt; keys.xml</p>
<dt> <code>kdb edit</code> [<code>-R</code>] [key/dir | key/name]</p>
<dt> <code>kdb rm</code> key/name</p>
<dt> <code>kdb mv</code> key/src key/dest</p>
<dt> <code>kdb ln</code> key/src key/dest</p>
<dt> <code>kdb export</code> [<code>-f</code>] system/some/tree.root &gt; [file.xml]</p>
<dt> <code>kdb import</code> &lt; file.xml</p>
<dt> <code>kdb import</code> file.xml</p>
<dt> <code>kdb monitor</code> some/key/name</p>
<dd>Description.PP The <code>kdb</code> command provide ways to manipulate the Elektra keys database.</dl>
<p> The subcommands implemented are very similar to regular UNIX commands like <code>ls</code>, and <code>rm</code>, specially in their output and options. Subcommands.PP <code>get</code></p>
<dl>
<dt>
<dd> Get the value from the specified key. Accepts options: <code>-d</code>, <code>-l</code>, <code>-f</code>, <code>-s</code></dl>
<p> <code>set</code></p>
<dl>
<dt>
<dd> Set the value to the specified key. Accepts options: <code>-c</code>, <code>-t</code>, <code>-d</code>, <code>-m</code>, <code>-b</code></dl>
<p> <code>ls</code></p>
<dl>
<dt>
<dd> As the <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) command, list key names for the specified key, or children keys, if specified a folder key. The <code>-v</code> argument will make it show also the values of each key. The <code>-d</code> (descriptive) will make it show the comment, key name and its value, as you are watching a plain text file. Accepts options: <code>-x</code>, <code>-d</code>, <code>-l</code>, <code>-f</code>, <code>-v</code>, <code>-R</code>, <code>-s</code></dl>
<p> <code>ln</code></p>
<dl>
<dt>
<dd> Creates a key that is a symbolic links to another key.</dl>
<p> <code>mv</code></p>
<dl>
<dt>
<dd> Move, or renames a key. Currently it can&#8217;t move keys across different filesystems.</dl>
<p> <code>rm</code></p>
<dl>
<dt>
<dd> As the <code><a href="/docs/linux/man/1-rm/">rm</a></code>(1) command, removes the key specified.</dl>
<p> <code>edit</code></p>
<dl>
<dt>
<dd> A very powerfull subcommand that lets you edit an XML representation of the keys. The parameters it accepts is usually a parent key, so its child keys will be gathered. Can be used with the <code>-R</code> flag to work recursively. The editor used is the one set in the <code>$EDITOR</code> environment variable, or <code>vi</code>. After editing the keys, <code>kdb edit</code> will analyze them and commit only the changed keys, remove the keys removed, and add the keys added. This command is only available when <i>/usr/lib/libelektratools.so</i> is available.</dl>
<p> <code>export</code>, <code>save</code></p>
<dl>
<dt>
<dd> Export a subtree of keys to XML. If no subtree is defined right after the <code>export</code> command, <i>system</i> and current <i>user</i> trees will be exported. Output is written to standard output. The output encoding will allways be UTF-8, regardeless of your system encoding. UTF-8 is the most universal charset you can get when exchanging data between multiple systems. Accepts <code>-f</code>.</dl>
<p> <code>import</code>, <code>load</code></p>
<dl>
<dt>
<dd> Import an XML representation of keys and save it to the keys database. If no filename is passed right after the <code>import</code> command, standard input is used. This command is only available when <i>/usr/lib/libelektratools.so</i> is available.</dl>
<p> <code>monitor</code>, <code>mon</code></p>
<dl>
<dt>
<dd> Monitor a key for some value change. It will block your command line until a change in the key value is detected, then return its new value.</dl>
<p> Options.PP <code>-R</code></p>
<dl>
<dt>
<dd> Causes to work recursively. In <code>ls</code>, will list recursively.</dl>
<p> <code>-x</code></p>
<dl>
<dt>
<dd> Makes <code>ls</code> output an XML representation of the keys, instead of an <code>ls</code>-compatible output.</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> Causes to display long results. With <code>ls</code>, will generate lists similar to <code>ls -l</code>. With <code>get</code>, will show also the key name.</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Causes <code>ls</code> to display also inactive keys. Generate lists similar to <code>ls -a</code>. Inactive keys are keys which basename begins with a &#8216;.&#8217; (dot). An example of inactive key: <i>system/sw/XFree/current/Monitor/.Monitor1</i></dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Causes to work with full key names. A full key name makes sense only on <i>user/*</i> keys, and differentiate from the regular key names in specifying the owner user. If the current user is <i>someuser</i>, the <i>user/some/key</i> full name is <i>user:someuser/some/key</i>. Makes effect in <code>ls</code>, <code>export</code> and <code>get</code> subcommands.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Causes <code>get</code> to work descriptivelly. When requesting a key it will show the comment, key name and its value in a fancy format. Causes <code>set</code> to mark the key as a directory key.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Causes <code>get</code> and <code>ls</code> to be more friendly to Shell scripts. For example, when requesting <i>user/env/env2/PATH</i>, the output will be PATH=&quot;the value&quot;, that is, only the basename of the key will be showed and the value will be surrounded by &#8216; &quot; &#8216;.</dl>
<p> <code>-t type</code></p>
<dl>
<dt>
<dd> When <code>set</code>ting a key&#8217;s value, you can specify the type with this switch. Currently accepted types are <code>string</code> for plain text, <code>bin</code> for binary as-is values, <code>dir</code> to create folder keys and <code>link</code> to create symbolic links between keys. Plain text are always stored as <code><a href="/docs/linux/man/7-utf-8/">UTF-8</a></code>(7) in Elektra, regardeless of your current encoding (<code>$LANG</code>). If you want to force a value to be stored without the <code><a href="/docs/linux/man/7-utf-8/">UTF-8</a></code>(7) encoding (a bad idea), you can set it as binary. Binary values should be avoided, because they are black boxes for system administrators.</dl>
<p> <code>-b filename</code></p>
<dl>
<dt>
<dd> Set the key value as the content of file <i>filename</i>. This option is more usefull when setting binary keys.</dl>
<p> <code>-m mode</code></p>
<dl>
<dt>
<dd> For the <code>set</code> command. Will set the key access permission to <code>mode</code>, which must be an octal number as for <code><a href="/docs/linux/man/1-chmod/">chmod</a></code>(1).</dl>
<p> <code>-u uid</code></p>
<dl>
<dt>
<dd> Create the key with <code>uid</code> user ID. It can be a user name or a uid number.</dl>
<p> <code>-g gid</code></p>
<dl>
<dt>
<dd> Create the key with <code>gid</code> group ID. It can be a group name or a gid number</dl>
<p> <code>-c comment</code></p>
<dl>
<dt>
<dd> When <code>set</code>ting keys, you can use this argument to set a descriptive comment for it. This comment is exactly as a comment in a plain text configuration file. The comment is stored as <code><a href="/docs/linux/man/7-utf-8/">UTF-8</a></code>(7) regardeless of your current encoding (<code>$LANG</code>).</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> With the <code>ls</code> subcommand, will make it show also the value stored in the key.</dl>
<p> <code>&#8212;</code></p>
<dl>
<dt>
<dd> With the <code>set</code> subcommand, everything after it will be considered the value, even text with dashes (-).</dl>
<p> Best Practices When Creating Keys.PP When using Elektra to store your application&#8217;s configuration and state, please keep in mind the following rules: </p>
<dl>
<dt>
<dd> *You are not allowed to create keys right under <i>system</i> or <i>user</i>.</dl>
<dl>
<dt>
<dd> *You are not allowed to create folder keys right under <i>system</i> or <i>user</i>. They are reserved for very essential OS subsystems.</dl>
<dl>
<dt>
<dd> *The keys for your application, called say <i>MyApp</i>, should be created under <i>system/sw/MyApp</i> and/or <i>user/sw/MyApp</i>.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>KDB_ROOT</code> if defined, prepends it to key names. </p>
<p> <code>KDB_BACKEND</code> defines the name of another backend plugin library to use ExamplesSetting Keys.PP bash$<code>kdb set -c &quot;My first key&quot; user/example/key &quot;Some nice value&quot;</code> </p>
<p> bash$<code>kdb set user:luciana/example/key &#8212; &quot;Some &#8211; nice &#8211; value with dashes&quot;</code> </p>
<p> bash#<code>KDB_ROOT=user:http/sw/httpd kdb set -u nobody -g http key &quot;Some value&quot;</code> </p>
<p> bash$<code>kdb set -b image.png -t bin user/example/binaryKey</code> </p>
<p> bash$<code>kdb set -b file.txt user/example/regularKey</code> </p>
<p> bash#<code>kdb set -t link system/sw/XFree/current system/sw/XFree/handmade</code> Getting Keys.PP bash$<code>KDB_ROOT=user/example kdb get some/key/name</code> </p>
<p> bash$<code>eval `kdb get -s user/env/env1/PS1`</code> </p>
<p> bash$<code>KDB_BACKEND=gconf kdb get user/sw/gnome-terminal/global/active_encodings</code> Listing.PP bash$<code>kdb ls -laR user:valeria</code> </p>
<p> bash$<code>kdb ls -lR system/sw/xorg/current</code> </p>
<p> bash$<code>KDB_ROOT=system/sw kdb ls -lR xorg</code> </p>
<p> bash$<code>KDB_BACKEND=fstab kdb ls -Rv system/filesystems</code> </p>
<p> bash$<code>eval `kdb ls -Rvs user/env/env2`</code> Miscelaneous.PP bash#<code>kdb ln system/sw/xorg/handmade system/sw/xorg/current</code> </p>
<p> bash#<code>kdb mv system/sw/xorg/current system/sw/xorg/old</code> </p>
<p> bash#<code>kdb rm system/inittab/rc4</code> </p>
<p> bash$<code>KDB_BACKEND=gconf kdb rm user/gconfKey</code> XML Import and Export.PP bash#<code>kdb export user/sw/app | sed -e &#8216;s|/app/|/app2/|g&#8217; | kdb import</code> </p>
<p> bash#<code>KDB_ROOT=system/sw kdb export myapp &gt; myappconf.xml</code> </p>
<p> bash#<code>kdb import myappconf.xml</code> </p>
<p> bash$<code>KDB_BACKEND=gconf kdb export user/sw</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-elektra/">elektra</a></code>(7), <code><a href="/docs/linux/man/5-elektra/">elektra</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> <code>Avi Alkalay</code> &lt;avi at unix.sh&gt;<br />
 Linux Market Developer, Senior IT and Software Architect, IBM Linux Impact Team :: <i>ibm.com/linux</i> </p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004 Avi Alkalay </p>
<h2>Index</h2>
