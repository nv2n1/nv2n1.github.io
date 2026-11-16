---
title: "kdb5_util(8)"
name: "kdb5_util"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kdb5_util/"
description: "kdb5_util – Kerberos database maintenance utility"
---

<p>kdb5_util &#8211; Kerberos database maintenance utility</p>
<h2>Synopsis</h2>
<p><code>kdb5_util</code> [<code>-r</code> <i>realm</i>] [<code>-d</code> <i>dbname</i>] [<code>-k</code> <i>mkeytype</i>] [<code>-M</code> <i>mkeyname</i>] [<code>-kv</code> <i>mkeyVNO</i>] [<code>-sf</code> <i>stashfilename</i>] [<code>-m</code>] <i>command</i> [<i>command_options</i>]</p>
<h2>Description</h2>
<p>kdb5_util allows an administrator to perform maintenance procedures on the KDC database. Databases can be created, destroyed, and dumped to or loaded from ASCII files. kdb5_util can create a Kerberos master key stash file or perform live rollover of the master key. </p>
<p> When kdb5_util is run, it attempts to acquire the master key and open the database. However, execution continues regardless of whether or not kdb5_util successfully opens the database, because the database may not exist yet or the stash file may be corrupt. </p>
<p> Note that some KDC database modules may not support all kdb5_util commands.</p>
<h2>Command-Line Options</h2>
<dl>
<dt><code>-r</code> <i>realm</i></dt>
<dd>specifies the Kerberos realm of the database.</dd>
<dt><code>-d</code> <i>dbname</i></dt>
<dd>specifies the name under which the principal database is stored; by default the database is that listed in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>. The password policy database and lock files are also derived from this value.</dd>
<dt><code>-k</code> <i>mkeytype</i></dt>
<dd>specifies the key type of the master key in the database. The default is given by the <code>master_key_type</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</dd>
<dt><code>-kv</code> <i>mkeyVNO</i></dt>
<dd>Specifies the version number of the master key in the database; the default is 1. Note that 0 is not allowed.</dd>
<dt><code>-M</code> <i>mkeyname</i></dt>
<dd>principal name for the master key in the database. If not specified, the name is determined by the <code>master_key_name</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</dd>
<dt><code>-m</code></dt>
<dd>specifies that the master database password should be read from the keyboard rather than fetched from a file on disk.</dd>
<dt><code>-sf</code> <i>stash_file</i></dt>
<dd>specifies the stash filename of the master database password. If not specified, the filename is determined by the <code>key_stash_file</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</dd>
<dt><code>-P</code> <i>password</i></dt>
<dd>specifies the master database password. Using this option may expose the password to other users on the system via the process list.</dd></dl>
<h2>Commands</h2>
<h3>create</h3>
<p><code>create</code> [<code>-s</code>] </p>
<p> Creates a new database. If the <code>-s</code> option is specified, the stash file is also created. This command fails if the database already exists. If the command is successful, the database is opened just as if it had already existed when the program was first run.</p>
<h3>destroy</h3>
<p><code>destroy</code> [<code>-f</code>] </p>
<p> Destroys the database, first overwriting the disk sectors and then unlinking the files, after prompting the user for confirmation. With the <code>-f</code> argument, does not prompt the user.</p>
<h3>stash</h3>
<p><code>stash</code> [<code>-f</code> <i>keyfile</i>] </p>
<p> Stores the master principal&#8217;s keys in a stash file. The <code>-f</code> argument can be used to override the <i>keyfile</i> specified in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</p>
<h3>dump</h3>
<p><code>dump</code> [<code>-b7</code>|<code>-ov</code>|<code>-r13</code>] [<code>-verbose</code>] [<code>-mkey_convert</code>] [<code>-new_mkey_file</code> <i>mkey_file</i>] [<code>-rev</code>] [<code>-recurse</code>] [<i>filename</i> [<i>principals</i>&#8230;]] </p>
<p> Dumps the current Kerberos and KADM5 database into an ASCII file. By default, the database is dumped in current format, &quot;kdb5_util load_dump version 7&quot;. If filename is not specified, or is the string &quot;-&quot;, the dump is sent to standard output. Options:</p>
<dl>
<dt><code>-b7</code></dt>
<dd>causes the dump to be in the Kerberos 5 Beta 7 format (&quot;kdb5_util load_dump version 4&quot;). This was the dump format produced on releases prior to 1.2.2.</dd>
<dt><code>-ov</code></dt>
<dd>causes the dump to be in &quot;ovsec_adm_export&quot; format.</dd>
<dt><code>-r13</code></dt>
<dd>causes the dump to be in the Kerberos 5 1.3 format (&quot;kdb5_util load_dump version 5&quot;). This was the dump format produced on releases prior to 1.8.</dd>
<dt><code>-r18</code></dt>
<dd>causes the dump to be in the Kerberos 5 1.8 format (&quot;kdb5_util load_dump version 6&quot;). This was the dump format produced on releases prior to 1.11.</dd>
<dt><code>-verbose</code></dt>
<dd>causes the name of each principal and policy to be printed as it is dumped.</dd>
<dt><code>-mkey_convert</code></dt>
<dd>prompts for a new master key. This new master key will be used to re-encrypt principal key data in the dumpfile. The principal keys themselves will not be changed.</dd>
<dt><code>-new_mkey_file</code> <i>mkey_file</i></dt>
<dd>the filename of a stash file. The master key in this stash file will be used to re-encrypt the key data in the dumpfile. The key data in the database will not be changed.</dd>
<dt><code>-rev</code></dt>
<dd>dumps in reverse order. This may recover principals that do not dump normally, in cases where database corruption has occurred.</dd>
<dt><code>-recurse</code></dt>
<dd>causes the dump to walk the database recursively (btree only). This may recover principals that do not dump normally, in cases where database corruption has occurred. In cases of such corruption, this option will probably retrieve more principals than the <code>-rev</code> option will.</dd></dl>
<h3>load</h3>
<p><code>load</code> [<code>-b7</code>|<code>-ov</code>|<code>-r13</code>] [<code>-hash</code>] [<code>-verbose</code>] [<code>-update</code>] <i>filename</i> [<i>dbname</i>] </p>
<p> Loads a database dump from the named file into the named database. If no option is given to determine the format of the dump file, the format is detected automatically and handled as appropriate. Unless the <code>-update</code> option is given, <code>load</code> creates a new database containing only the data in the dump file, overwriting the contents of any previously existing database. Note that when using the LDAP KDC database module, the <code>-update</code> flag is required. </p>
<p> Options:</p>
<dl>
<dt><code>-b7</code></dt>
<dd>requires the database to be in the Kerberos 5 Beta 7 format (&quot;kdb5_util load_dump version 4&quot;). This was the dump format produced on releases prior to 1.2.2.</dd>
<dt><code>-ov</code></dt>
<dd>requires the database to be in &quot;ovsec_adm_import&quot; format. Must be used with the <code>-update</code> option.</dd>
<dt><code>-r13</code></dt>
<dd>requires the database to be in Kerberos 5 1.3 format (&quot;kdb5_util load_dump version 5&quot;). This was the dump format produced on releases prior to 1.8.</dd>
<dt><code>-r18</code></dt>
<dd>requires the database to be in Kerberos 5 1.8 format (&quot;kdb5_util load_dump version 6&quot;). This was the dump format produced on releases prior to 1.11.</dd>
<dt><code>-hash</code></dt>
<dd>requires the database to be stored as a hash. If this option is not specified, the database will be stored as a btree. This option is not recommended, as databases stored in hash format are known to corrupt data and lose principals.</dd>
<dt><code>-verbose</code></dt>
<dd>causes the name of each principal and policy to be printed as it is dumped.</dd>
<dt><code>-update</code></dt>
<dd>records from the dump file are added to or updated in the existing database. Otherwise, a new database is created containing only what is in the dump file and the old one destroyed upon successful completion. </dd>
<p> If specified, <i>dbname</i> overrides the value specified on the command line or the default.</dl>
<h3>ark</h3>
<p><code>ark</code> [<code>-e</code> <i>enc</i>:<i>salt</i>,&#8230;] <i>principal</i> </p>
<p> Adds new random keys to <i>principal</i> at the next available key version number. Keys for the current highest key version number will be preserved. The <code>-e</code> option specifies the list of encryption and salt types to be used for the new keys.</p>
<h3>add_mkey</h3>
<p><code>add_mkey</code> [<code>-e</code> <i>etype</i>] [<code>-s</code>] </p>
<p> Adds a new master key to the master key principal, but does not mark it as active. Existing master keys will remain. The <code>-e</code> option specifies the encryption type of the new master key; see <i>Encryption_types</i> in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i> for a list of possible values. The <code>-s</code> option stashes the new master key in the stash file, which will be created if it doesn&#8217;t already exist. </p>
<p> After a new master key is added, it should be propagated to slave servers via a manual or periodic invocation of <i><a href="/docs/linux/man/8-kprop/">kprop</a>(8)</i>. Then, the stash files on the slave servers should be updated with the kdb5_util <code>stash</code> command. Once those steps are complete, the key is ready to be marked active with the kdb5_util <code>use_mkey</code> command.</p>
<h3>use_mkey</h3>
<p><code>use_mkey</code> <i>mkeyVNO</i> [<i>time</i>] </p>
<p> Sets the activation time of the master key specified by <i>mkeyVNO</i>. Once a master key becomes active, it will be used to encrypt newly created principal keys. If no <i>time</i> argument is given, the current time is used, causing the specified master key version to become active immediately. The format for <i>time</i> is <i>getdate</i> string. </p>
<p> After a new master key becomes active, the kdb5_util <code>update_princ_encryption</code> command can be used to update all principal keys to be encrypted in the new master key.</p>
<h3>list_mkeys</h3>
<p><code>list_mkeys</code> </p>
<p> List all master keys, from most recent to earliest, in the master key principal. The output will show the kvno, enctype, and salt type for each mkey, similar to the output of <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i> <code>getprinc</code>. A <code>*</code> following an mkey denotes the currently active master key.</p>
<h3>purge_mkeys</h3>
<p><code>purge_mkeys</code> [<code>-f</code>] [<code>-n</code>] [<code>-v</code>] </p>
<p> Delete master keys from the master key principal that are not used to protect any principals. This command can be used to remove old master keys all principal keys are protected by a newer master key.</p>
<dl>
<dt><code>-f</code></dt>
<dd>does not prompt for confirmation.</dd>
<dt><code>-n</code></dt>
<dd>performs a dry run, showing master keys that would be purged, but not actually purging any keys.</dd>
<dt><code>-v</code></dt>
<dd>gives more verbose output.</dd></dl>
<h3>update_princ_encryption</h3>
<p><code>update_princ_encryption</code> [<code>-f</code>] [<code>-n</code>] [<code>-v</code>] [<i>princ-pattern</i>] </p>
<p> Update all principal records (or only those matching the <i>princ-pattern</i> glob pattern) to re-encrypt the key data using the active database master key, if they are encrypted using a different version, and give a count at the end of the number of principals updated. If the <code>-f</code> option is not given, ask for confirmation before starting to make changes. The <code>-v</code> option causes each principal processed to be listed, with an indication as to whether it needed updating or not. The <code>-n</code> option performs a dry run, only showing the actions which would have been taken.</p>
<h3>tabdump</h3>
<p><code>tabdump</code> [<code>-H</code>] [<code>-c</code>] [<code>-e</code>] [<code>-n</code>] [<code>-o</code> <i>outfile</i>] <i>dumptype</i> </p>
<p> Dump selected fields of the database in a tabular format suitable for reporting (e.g., using traditional Unix text processing tools) or importing into relational databases. The data format is tab-separated (default), or optionally comma-separated (CSV), with a fixed number of columns. The output begins with a header line containing field names, unless suppression is requested using the <code>-H</code> option. </p>
<p> The <i>dumptype</i> parameter specifies the name of an output table (see below). </p>
<p> Options:</p>
<dl>
<dt><code>-H</code></dt>
<dd>suppress writing the field names in a header line</dd>
<dt><code>-c</code></dt>
<dd>use comma separated values (CSV) format, with minimal quoting, instead of the default tab-separated (unquoted, unescaped) format</dd>
<dt><code>-e</code></dt>
<dd>write empty hexadecimal string fields as empty fields instead of as &quot;-1&quot;.</dd>
<dt><code>-n</code></dt>
<dd>produce numeric output for fields that normally have symbolic output, such as enctypes and flag names. Also requests output of time stamps as decimal POSIX time_t values.</dd>
<dt><code>-o</code> <i>outfile</i></dt>
<dd>write the dump to the specified output file instead of to standard output </dd>
<p> Dump types:</p>
<dt><code>keydata</code></dt>
<dd>principal encryption key information, including actual key data (which is still encrypted in the master key)</dd>
<dt><code>name</code></dt>
<dd>principal name</dd>
<dt><code>keyindex</code></dt>
<dd>index of this key in the principal&#8217;s key list</dd>
<dt><code>kvno</code></dt>
<dd>key version number</dd>
<dt><code>enctype</code></dt>
<dd>encryption type</dd>
<dt><code>key</code></dt>
<dd>key data as a hexadecimal string</dd>
<dt><code>salttype</code></dt>
<dd>salt type</dd>
<dt><code>salt</code></dt>
<dd>salt data as a hexadecimal string</dd>
<dt><code>keyinfo</code></dt>
<dd>principal encryption key information (as in <code>keydata</code> above), excluding actual key data</dd>
<dt><code>princ_flags</code></dt>
<dd>principal boolean attributes. Flag names print as hexadecimal numbers if the <code>-n</code> option is specified, and all flag positions are printed regardless of whether or not they are set. If <code>-n</code> is not specified, print all known flag names for each principal, but only print hexadecimal flag names if the corresponding flag is set.</dd>
<dt><code>name</code></dt>
<dd>principal name</dd>
<dt><code>flag</code></dt>
<dd>flag name</dd>
<dt><code>value</code></dt>
<dd>boolean value (0 for clear, or 1 for set)</dd>
<dt><code>princ_lockout</code></dt>
<dd>state information used for tracking repeated password failures</dd>
<dt><code>name</code></dt>
<dd>principal name</dd>
<dt><code>last_success</code></dt>
<dd>time stamp of most recent successful authentication</dd>
<dt><code>last_failed</code></dt>
<dd>time stamp of most recent failed authentication</dd>
<dt><code>fail_count</code></dt>
<dd>count of failed attempts</dd>
<dt><code>princ_meta</code></dt>
<dd>principal metadata</dd>
<dt><code>name</code></dt>
<dd>principal name</dd>
<dt><code>modby</code></dt>
<dd>name of last principal to modify this principal</dd>
<dt><code>modtime</code></dt>
<dd>timestamp of last modification</dd>
<dt><code>lastpwd</code></dt>
<dd>timestamp of last password change</dd>
<dt><code>policy</code></dt>
<dd>policy object name</dd>
<dt><code>mkvno</code></dt>
<dd>key version number of the master key that encrypts this principal&#8217;s key data</dd>
<dt><code>hist_kvno</code></dt>
<dd>key version number of the history key that encrypts the key history data for this principal</dd>
<dt><code>princ_stringattrs</code></dt>
<dd>string attributes (key/value pairs)</dd>
<dt><code>name</code></dt>
<dd>principal name</dd>
<dt><code>key</code></dt>
<dd>attribute name</dd>
<dt><code>value</code></dt>
<dd>attribute value</dd>
<dt><code>princ_tktpolicy</code></dt>
<dd>per-principal ticket policy data, including maximum ticket lifetimes</dd>
<dt><code>name</code></dt>
<dd>principal name</dd>
<dt><code>expiration</code></dt>
<dd>principal expiration date</dd>
<dt><code>pw_expiration</code></dt>
<dd>password expiration date</dd>
<dt><code>max_life</code></dt>
<dd>maximum ticket lifetime</dd>
<dt><code>max_renew_life</code></dt>
<dd>maximum renewable ticket lifetime </dd>
<p> Examples: </p>
<pre>$ kdb5_util tabdump -o keyinfo.txt keyinfo
$ cat keyinfo.txt
name keyindex kvno enctype salttype salt
foo [at] EXAMPLE.COM 0 1 aes128-cts-hmac-sha1-96 normal -1
bar [at] EXAMPLE.COM 0 1 aes128-cts-hmac-sha1-96 normal -1
bar [at] EXAMPLE.COM 1 1 des-cbc-crc normal -1
$ sqlite3
sqlite&gt; .mode tabs
sqlite&gt; .import keyinfo.txt keyinfo
sqlite&gt; select * from keyinfo where enctype like 'des-cbc-%';
bar [at] EXAMPLE.COM 1 1 des-cbc-crc normal -1
sqlite&gt; .quit
$ awk -F'	' '$4 ~ /des-cbc-/ { print }' keyinfo.txt
bar [at] EXAMPLE.COM 1 1 des-cbc-crc normal -1</pre>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
