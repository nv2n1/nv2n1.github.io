---
title: "heimdal-kadmin(8)"
name: "heimdal-kadmin"
section: "8"
letter: "h"
url: "/docs/linux/man/8-heimdal-kadmin/"
description: "kadmin – Kerberos administration utility"
---

<p><code>kadmin</code> &#8211; Kerberos administration utility</p>
<h2>Synopsis</h2>
<p>-words [-<code>p </code><i>string | &#8211;</i><code>-principal= </code><i>string</i> ] [-<code>K </code><i>string | &#8211;</i><code>-keytab= </code><i>string</i> ] [-<code>c </code><i>file | &#8211;</i><code>-config-file= </code><i>file</i> ] [-<code>k </code><i>file | &#8211;</i><code>-key-file= </code><i>file</i> ] [-<code>r </code><i>realm | &#8211;</i><code>-realm= </code><i>realm</i> ] [-<code>a </code><i>host | &#8211;</i><code>-admin-server= </code><i>host</i> ] [-<code>s </code><i>port number | &#8211;</i><code>-server-port= </code><i>port number</i> ] [-<code>l | &#8211;local</code> ] [-<code>h | &#8211;help</code> ] [-<code>v | &#8211;version</code> ] [<i>command</i> ]</p>
<h2>Description</h2>
<p>The program is used to make modifications to the Kerberos database, either remotely via the <a href="/docs/linux/man/8-kadmind/">kadmind</a>(8) daemon, or locally (with the &#8211;<code>l</code> option). </p>
<p> Supported options:</p>
<dl>
<dt><code>-p </code><i>string , &#8211;</i><code>-principal= </code><i>string</i></p>
<dd>principal to authenticate as</p>
<dt><code>-K </code><i>string , &#8211;</i><code>-keytab= </code><i>string</i></p>
<dd>keytab for authentication principal</p>
<dt><code>-c </code><i>file , &#8211;</i><code>-config-file= </code><i>file</i></p>
<dd>location of config file</p>
<dt><code>-k </code><i>file , &#8211;</i><code>-key-file= </code><i>file</i></p>
<dd>location of master key file</p>
<dt><code>-r </code><i>realm , &#8211;</i><code>-realm= </code><i>realm</i></p>
<dd>realm to use</p>
<dt><code>-a </code><i>host , &#8211;</i><code>-admin-server= </code><i>host</i></p>
<dd>server to contact</p>
<dt><code>-s </code><i>port number , &#8211;</i><code>-server-port= </code><i>port number</i></p>
<dd>port to use</p>
<dt><code>-l , &#8211;local</code></p>
<dd>local admin mode</dl>
<p> If no <i>command</i> is given on the command line, will prompt for commands to process. Some of the commands that take one or more principals as argument <code>( delete</code> <code>ext_keytab</code> <code>get</code> <code>modify</code> and <code>passwd</code> will accept a glob style wildcard, and perform the operation on all matching principals. </p>
<p> Commands include: </p>
<p> <code>add</code> [-<code>r | &#8211;random-key</code> ] [-<code>-random-password</code> ] [-<code>p </code><i>string | &#8211;</i><code>-password= </code><i>string</i> ] [-<code>-key= </code><i>string</i> ] [-<code>-max-ticket-life= </code><i>lifetime</i> ] [-<code>-max-renewable-life= </code><i>lifetime</i> ] [-<code>-attributes= </code><i>attributes</i> ] [-<code>-expiration-time= </code><i>time</i> ] [-<code>-pw-expiration-time= </code><i>time</i> ] [-<code>-policy= </code><i>policy-name</i> ] <i>principal&#8230;</i> </p>
<blockquote><p> Adds a new principal to the database. The options not passed on the command line will be promped for. The only policy supported by Heimdal servers is </p></blockquote>
<p> <code>add_enctype</code> [-<code>r | &#8211;random-key</code> ] <i>principal enctypes&#8230;</i> </p>
<blockquote><p> Adds a new encryption type to the principal, only random key are supported. </p></blockquote>
<p> <code>delete</code> <i>principal&#8230;</i> </p>
<blockquote><p> Removes a principal. </p></blockquote>
<p> <code>del_enctype</code> <i>principal enctypes&#8230;</i> </p>
<blockquote><p> Removes some enctypes from a principal; this can be useful if the service belonging to the principal is known to not handle certain enctypes. </p></blockquote>
<p> <code>ext_keytab</code> [-<code>k </code><i>string | </i> &#8211;<code>-keytab= </code><i>string</i> ] <i>principal&#8230;</i> </p>
<blockquote><p> Creates a keytab with the keys of the specified principals. Requires get-keys rights, otherwise the principal&#8217;s keys are changed and saved in the keytab. </p></blockquote>
<p> <code>get</code> [-<code>l | &#8211;long</code> ] [-<code>s | &#8211;short</code> ] [-<code>t | &#8211;terse</code> ] [-<code>o </code><i>string | &#8211;</i><code>-column-info= </code><i>string</i> ] <i>principal&#8230;</i> </p>
<blockquote><p> Lists the matching principals, short prints the result as a table, while long format produces a more verbose output. Which columns to print can be selected with the &#8211;<code>o</code> option. The argument is a comma separated list of column names optionally appended with an equal sign (`=&#8217; ) and a column header. Which columns are printed by default differ slightly between short and long output. </p>
<p> The default terse output format is similar to &#8211;<code>s o </code><i>principal=</i> just printing the names of matched principals. </p>
<p> Possible column names include: <code>principal</code> <code>princ_expire_time</code> <code>pw_expiration</code> <code>last_pwd_change</code> <code>max_life</code> <code>max_rlife</code> <code>mod_time</code> <code>mod_name</code> <code>attributes</code> <code>kvno</code> <code>mkvno</code> <code>last_success</code> <code>last_failed</code> <code>fail_auth_count</code> <code>policy</code> and <code>keytypes</code> </p></blockquote>
<p> <code>modify</code> [-<code>a </code><i>attributes | </i> &#8211;<code>-attributes= </code><i>attributes</i> ] [-<code>-max-ticket-life= </code><i>lifetime</i> ] [-<code>-max-renewable-life= </code><i>lifetime</i> ] [-<code>-expiration-time= </code><i>time</i> ] [-<code>-pw-expiration-time= </code><i>time</i> ] [-<code>-kvno= </code><i>number</i> ] [-<code>-policy= </code><i>policy-name</i> ] <i>principal&#8230;</i> </p>
<blockquote><p> Modifies certain attributes of a principal. If run without command line options, you will be prompted. With command line options, it will only change the ones specified. </p>
<p> Only policy supported by Heimdal is </p>
<p> Possible attributes are: <code>new-princ</code> <code>support-desmd5</code> <code>pwchange-service</code> <code>disallow-svr</code> <code>requires-pw-change</code> <code>requires-hw-auth</code> <code>requires-pre-auth</code> <code>disallow-all-tix</code> <code>disallow-dup-skey</code> <code>disallow-proxiable</code> <code>disallow-renewable</code> <code>disallow-tgt-based</code> <code>disallow-forwardable</code> <code>disallow-postdated</code> </p>
<p> Attributes may be negated with a &quot;-&quot;, e.g., </p>
<p> kadmin -l modify -a -disallow-proxiable user </p></blockquote>
<p> <code>passwd</code> [-<code>-keepold</code> ] [-<code>r | &#8211;random-key</code> ] [-<code>-random-password</code> ] [-<code>p </code><i>string | </i> &#8211;<code>-password= </code><i>string</i> ] [-<code>-key= </code><i>string</i> ] <i>principal&#8230;</i> </p>
<blockquote><p> Changes the password of an existing principal. </p></blockquote>
<p> <code>password-quality</code> <i>principal</i> <i>password</i> </p>
<blockquote><p> Run the password quality check function locally. You can run this on the host that is configured to run the kadmind process to verify that your configuration file is correct. The verification is done locally, if kadmin is run in remote mode, no rpc call is done to the server. </p></blockquote>
<p> <code>privileges</code> </p>
<blockquote><p> Lists the operations you are allowed to perform. These include <code>add</code> <code>add_enctype</code> <code>change-password</code> <code>delete</code> <code>del_enctype</code> <code>get</code> <code>get-keys</code> <code>list</code> and <code>modify</code> </p></blockquote>
<p> <code>rename</code> <i>from to</i> </p>
<blockquote><p> Renames a principal. This is normally transparent, but since keys are salted with the principal name, they will have a non-standard salt, and clients which are unable to cope with this will fail. Kerberos 4 suffers from this. </p></blockquote>
<p> <code>check</code> [<i>realm</i> ] </p>
<blockquote><p> Check database for strange configurations on important principals. If no realm is given, the default realm is used. </p></blockquote>
<p> When running in local mode, the following commands can also be used: </p>
<p> <code>dump</code> [-<code>d | &#8211;decrypt</code> ] [-<code>f </code><i>format | &#8211;</i><code>-format= </code><i>format</i> ] [<i>dump-file</i> ] </p>
<blockquote><p> Writes the database in &#8220;machine readable text&#8221; form to the specified file, or standard out. If the database is encrypted, the dump will also have encrypted keys, unless &#8211;<code>-decrypt</code> is used. If &#8211;<code>-format=MIT</code> is used then the dump will be in MIT format. Otherwise it will be in Heimdal format. </p></blockquote>
<p> <code>init</code> [-<code>-realm-max-ticket-life= </code><i>string</i> ] [-<code>-realm-max-renewable-life= </code><i>string</i> ] <i>realm</i> </p>
<blockquote><p> Initializes the Kerberos database with entries for a new realm. It&#8217;s possible to have more than one realm served by one server. </p></blockquote>
<p> <code>load</code> <i>file</i> </p>
<blockquote><p> Reads a previously dumped database, and re-creates that database from scratch. </p></blockquote>
<p> <code>merge</code> <i>file</i> </p>
<blockquote><p> Similar to <code>load</code> but just modifies the database with the entries in the dump file. </p></blockquote>
<p> <code>stash</code> [-<code>e </code><i>enctype | </i> &#8211;<code>-enctype= </code><i>enctype</i> ] [-<code>k </code><i>keyfile | </i> &#8211;<code>-key-file= </code><i>keyfile</i> ] [-<code>-convert-file</code> ] [-<code>-master-key-fd= </code><i>fd</i> ] </p>
<blockquote><p> Writes the Kerberos master key to a file used by the KDC. </p></blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8), <a href="/docs/linux/man/8-kdc/">kdc</a>(8) </p>
