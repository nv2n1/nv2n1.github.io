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
<dt><code>-r</code> <i>realm</i></p>
<dd>specifies the Kerberos realm of the database.</p>
<dt><code>-d</code> <i>dbname</i></p>
<dd>specifies the name under which the principal database is stored; by default the database is that listed in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>. The password policy database and lock files are also derived from this value.</p>
<dt><code>-k</code> <i>mkeytype</i></p>
<dd>specifies the key type of the master key in the database. The default is given by the <code>master_key_type</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</p>
<dt><code>-kv</code> <i>mkeyVNO</i></p>
<dd>Specifies the version number of the master key in the database; the default is 1. Note that 0 is not allowed.</p>
<dt><code>-M</code> <i>mkeyname</i></p>
<dd>principal name for the master key in the database. If not specified, the name is determined by the <code>master_key_name</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</p>
<dt><code>-m</code></p>
<dd>specifies that the master database password should be read from the keyboard rather than fetched from a file on disk.</p>
<dt><code>-sf</code> <i>stash_file</i></p>
<dd>specifies the stash filename of the master database password. If not specified, the filename is determined by the <code>key_stash_file</code> variable in <i><a href="/docs/linux/man/5-kdc-conf/">kdc.conf</a>(5)</i>.</p>
<dt><code>-P</code> <i>password</i></p>
<dd>specifies the master database password. Using this option may expose the password to other users on the system via the process list.</dl>
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
<dt><code>-b7</code></p>
<dd>causes the dump to be in the Kerberos 5 Beta 7 format (&quot;kdb5_util load_dump version 4&quot;). This was the dump format produced on releases prior to 1.2.2.</p>
<dt><code>-ov</code></p>
<dd>causes the dump to be in &quot;ovsec_adm_export&quot; format.</p>
<dt><code>-r13</code></p>
<dd>causes the dump to be in the Kerberos 5 1.3 format (&quot;kdb5_util load_dump version 5&quot;). This was the dump format produced on releases prior to 1.8.</p>
<dt><code>-r18</code></p>
<dd>causes the dump to be in the Kerberos 5 1.8 format (&quot;kdb5_util load_dump version 6&quot;). This was the dump format produced on releases prior to 1.11.</p>
<dt><code>-verbose</code></p>
<dd>causes the name of each principal and policy to be printed as it is dumped.</p>
<dt><code>-mkey_convert</code></p>
<dd>prompts for a new master key. This new master key will be used to re-encrypt principal key data in the dumpfile. The principal keys themselves will not be changed.</p>
<dt><code>-new_mkey_file</code> <i>mkey_file</i></p>
<dd>the filename of a stash file. The master key in this stash file will be used to re-encrypt the key data in the dumpfile. The key data in the database will not be changed.</p>
<dt><code>-rev</code></p>
<dd>dumps in reverse order. This may recover principals that do not dump normally, in cases where database corruption has occurred.</p>
<dt><code>-recurse</code></p>
<dd>causes the dump to walk the database recursively (btree only). This may recover principals that do not dump normally, in cases where database corruption has occurred. In cases of such corruption, this option will probably retrieve more principals than the <code>-rev</code> option will.</dl>
<h3>load</h3>
<p><code>load</code> [<code>-b7</code>|<code>-ov</code>|<code>-r13</code>] [<code>-hash</code>] [<code>-verbose</code>] [<code>-update</code>] <i>filename</i> [<i>dbname</i>] </p>
<p> Loads a database dump from the named file into the named database. If no option is given to determine the format of the dump file, the format is detected automatically and handled as appropriate. Unless the <code>-update</code> option is given, <code>load</code> creates a new database containing only the data in the dump file, overwriting the contents of any previously existing database. Note that when using the LDAP KDC database module, the <code>-update</code> flag is required. </p>
<p> Options:</p>
<dl>
<dt><code>-b7</code></p>
<dd>requires the database to be in the Kerberos 5 Beta 7 format (&quot;kdb5_util load_dump version 4&quot;). This was the dump format produced on releases prior to 1.2.2.</p>
<dt><code>-ov</code></p>
<dd>requires the database to be in &quot;ovsec_adm_import&quot; format. Must be used with the <code>-update</code> option.</p>
<dt><code>-r13</code></p>
<dd>requires the database to be in Kerberos 5 1.3 format (&quot;kdb5_util load_dump version 5&quot;). This was the dump format produced on releases prior to 1.8.</p>
<dt><code>-r18</code></p>
<dd>requires the database to be in Kerberos 5 1.8 format (&quot;kdb5_util load_dump version 6&quot;). This was the dump format produced on releases prior to 1.11.</p>
<dt><code>-hash</code></p>
<dd>requires the database to be stored as a hash. If this option is not specified, the database will be stored as a btree. This option is not recommended, as databases stored in hash format are known to corrupt data and lose principals.</p>
<dt><code>-verbose</code></p>
<dd>causes the name of each principal and policy to be printed as it is dumped.</p>
<dt><code>-update</code></p>
<dd>records from the dump file are added to or updated in the existing database. Otherwise, a new database is created containing only what is in the dump file and the old one destroyed upon successful completion. </p>
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
<dt><code>-f</code></p>
<dd>does not prompt for confirmation.</p>
<dt><code>-n</code></p>
<dd>performs a dry run, showing master keys that would be purged, but not actually purging any keys.</p>
<dt><code>-v</code></p>
<dd>gives more verbose output.</dl>
<h3>update_princ_encryption</h3>
<p><code>update_princ_encryption</code> [<code>-f</code>] [<code>-n</code>] [<code>-v</code>] [<i>princ-pattern</i>] </p>
<p> Update all principal records (or only those matching the <i>princ-pattern</i> glob pattern) to re-encrypt the key data using the active database master key, if they are encrypted using a different version, and give a count at the end of the number of principals updated. If the <code>-f</code> option is not given, ask for confirmation before starting to make changes. The <code>-v</code> option causes each principal processed to be listed, with an indication as to whether it needed updating or not. The <code>-n</code> option performs a dry run, only showing the actions which would have been taken.</p>
<h3>tabdump</h3>
<p><code>tabdump</code> [<code>-H</code>] [<code>-c</code>] [<code>-e</code>] [<code>-n</code>] [<code>-o</code> <i>outfile</i>] <i>dumptype</i> </p>
<p> Dump selected fields of the database in a tabular format suitable for reporting (e.g., using traditional Unix text processing tools) or importing into relational databases. The data format is tab-separated (default), or optionally comma-separated (CSV), with a fixed number of columns. The output begins with a header line containing field names, unless suppression is requested using the <code>-H</code> option. </p>
<p> The <i>dumptype</i> parameter specifies the name of an output table (see below). </p>
<p> Options:</p>
<dl>
<dt><code>-H</code></p>
<dd>suppress writing the field names in a header line</p>
<dt><code>-c</code></p>
<dd>use comma separated values (CSV) format, with minimal quoting, instead of the default tab-separated (unquoted, unescaped) format</p>
<dt><code>-e</code></p>
<dd>write empty hexadecimal string fields as empty fields instead of as &quot;-1&quot;.</p>
<dt><code>-n</code></p>
<dd>produce numeric output for fields that normally have symbolic output, such as enctypes and flag names. Also requests output of time stamps as decimal POSIX time_t values.</p>
<dt><code>-o</code> <i>outfile</i></p>
<dd>write the dump to the specified output file instead of to standard output </p>
<p> Dump types:</p>
<dt><code>keydata</code></p>
<dd>principal encryption key information, including actual key data (which is still encrypted in the master key)</p>
<dt><code>name</code></p>
<dd>principal name</p>
<dt><code>keyindex</code></p>
<dd>index of this key in the principal&#8217;s key list</p>
<dt><code>kvno</code></p>
<dd>key version number</p>
<dt><code>enctype</code></p>
<dd>encryption type</p>
<dt><code>key</code></p>
<dd>key data as a hexadecimal string</p>
<dt><code>salttype</code></p>
<dd>salt type</p>
<dt><code>salt</code></p>
<dd>salt data as a hexadecimal string</p>
<dt><code>keyinfo</code></p>
<dd>principal encryption key information (as in <code>keydata</code> above), excluding actual key data</p>
<dt><code>princ_flags</code></p>
<dd>principal boolean attributes. Flag names print as hexadecimal numbers if the <code>-n</code> option is specified, and all flag positions are printed regardless of whether or not they are set. If <code>-n</code> is not specified, print all known flag names for each principal, but only print hexadecimal flag names if the corresponding flag is set.</p>
<dt><code>name</code></p>
<dd>principal name</p>
<dt><code>flag</code></p>
<dd>flag name</p>
<dt><code>value</code></p>
<dd>boolean value (0 for clear, or 1 for set)</p>
<dt><code>princ_lockout</code></p>
<dd>state information used for tracking repeated password failures</p>
<dt><code>name</code></p>
<dd>principal name</p>
<dt><code>last_success</code></p>
<dd>time stamp of most recent successful authentication</p>
<dt><code>last_failed</code></p>
<dd>time stamp of most recent failed authentication</p>
<dt><code>fail_count</code></p>
<dd>count of failed attempts</p>
<dt><code>princ_meta</code></p>
<dd>principal metadata</p>
<dt><code>name</code></p>
<dd>principal name</p>
<dt><code>modby</code></p>
<dd>name of last principal to modify this principal</p>
<dt><code>modtime</code></p>
<dd>timestamp of last modification</p>
<dt><code>lastpwd</code></p>
<dd>timestamp of last password change</p>
<dt><code>policy</code></p>
<dd>policy object name</p>
<dt><code>mkvno</code></p>
<dd>key version number of the master key that encrypts this principal&#8217;s key data</p>
<dt><code>hist_kvno</code></p>
<dd>key version number of the history key that encrypts the key history data for this principal</p>
<dt><code>princ_stringattrs</code></p>
<dd>string attributes (key/value pairs)</p>
<dt><code>name</code></p>
<dd>principal name</p>
<dt><code>key</code></p>
<dd>attribute name</p>
<dt><code>value</code></p>
<dd>attribute value</p>
<dt><code>princ_tktpolicy</code></p>
<dd>per-principal ticket policy data, including maximum ticket lifetimes</p>
<dt><code>name</code></p>
<dd>principal name</p>
<dt><code>expiration</code></p>
<dd>principal expiration date</p>
<dt><code>pw_expiration</code></p>
<dd>password expiration date</p>
<dt><code>max_life</code></p>
<dd>maximum ticket lifetime</p>
<dt><code>max_renew_life</code></p>
<dd>maximum renewable ticket lifetime </p>
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
