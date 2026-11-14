---
title: "libuser-conf(5)"
name: "libuser-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-libuser-conf/"
description: "libuser.conf – configuration for libuser and libuser utilities"
---

<p>libuser.conf &#8211; configuration for libuser and libuser utilities</p>
<h2>File Format</h2>
<p><code>libuser.conf</code> is a text file. Leading and trailing white space on each line is ignored. Lines starting with <code>#</code> are ignored. </p>
<p> The file defines variables grouped into sections. Each section starts with a section header:</p>
<dl>
<dd><code>[</code><i>section name</i><code>]</code></dl>
<p> A single section header can appear more than once in the file. </p>
<p> The lines following a section header define variables from that section:</p>
<dl>
<dd><i>variable</i> <code>=</code> <i>value</i></dl>
<p> The <i>value</i> can be empty. </p>
<p> A <i>variable</i> can have more than one value, specified by using more than one line defining that <i>variable</i>. All currently defined variables accept only the first value and ignore the others, if any.</p>
<h2><code>[defaults]</code></h2>
<dl>
<dt><code>create_modules</code></p>
<dd>A list of module names to use when creating user or group entries, unless the application specifies a different list. The module names in the list can be separated using space, tab or comma. Default value is <code>files shadow</code>. </p>
<dt><code>crypt_style</code></p>
<dd>The algorithm to use for password encryption when creating new passwords. The current algorithm may be retained when changing a password of an existing user, depending on the application. </p>
<p> Possible values are <code>des</code>, <code>md5</code>, <code>blowfish</code>, <code>sha256</code> and <code>sha512</code>, all case-insensitive. Unrecognized values are treated as <code>des</code>. Default value is <code>des</code>. </p>
<dt><code>hash_rounds_min</code>, <code>hash_rounds_max</code></p>
<dd>These variables specify an inclusive range of hash rounds used when <code>crypt_style</code> is <code>sha256</code> or <code>sha512</code>. A number of hash rounds is chosen from this interval randomly. A larger number of rounds makes password checking, and brute-force attempts to guess the password by reversing the hash, more CPU-intensive. The number of rounds is restricted to the interval [1000, 999999999]. </p>
<p> If only one of the above variables is specified, the number of rounds used is specified by the other variable. If neither variable is specified, the number of rounds is chosen by <code>libc</code>. </p>
<dt><code>mailspooldir</code></p>
<dd>The directory containing user&#8217;s mail spool files. Default value is <code>/var/mail</code>. </p>
<dt><code>moduledir</code></p>
<dd>The directory containing <code>libuser</code> modules. Default value uses the modules installed with <code>libuser</code>, corresponding to the architecture of the <code>libuser</code> library, e.g. <code>/usr/lib/libuser</code> or <code>/usr/lib64/libuser</code> (assuming <code>libuser</code> was configured with <code>&#8211;prefix=/usr</code>). </p>
<dt><code>modules</code></p>
<dd>A list of module names to use when not creating user or group entries, unless the application specifies a different list. The module names in the list can be separated using space, tab or comma. Default value is <code>files shadow</code>. </p>
<dt><code>skeleton</code></p>
<dd>The directory containing files to copy to newly created home directories. Default value is <code>/etc/skel</code>. </p>
</dl>
<h2><code>[import]</code></h2>
<dl>
<dt><code>login_defs</code></p>
<dd>A path to the <i>login.defs</i> file from <code>shadow</code>. If this variable is defined, the variables from the named file are used in place of some <code>libuser</code> variables. Variables explicitly defined in <i>libuser.conf</i> are not affected by contents of <i>login.defs</i>. </p>
<p> The following variables are imported: </p>
<table>
<tr VALIGN=top>
<td>Variable</td>
<td>Imported as
</td>
</tr>
<tr VALIGN=top>
<td>ENCRYPT_METHOD</td>
</tr>
<tr VALIGN=top>
<td><code>GID_MIN</code></td>
<td><code>groupdefaults/LU_GIDNUMBER</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>MAIL_DIR</code></td>
<td><code>defaults/mailspooldir</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>MD5_CRYPT_ENAB</code></td>
<td><code>defaults/crypt_style</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>PASS_MAX_DAYS</code></td>
<td><code>userdefaults/LU_SHADOWMAX</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>PASS_MIN_DAYS</code></td>
<td><code>userdefaults/LU_SHADOWMIN</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>PASS_WARN_AGE</code></td>
<td><code>userdefaults/LU_SHADOWWARNING</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SHA_CRYPT_MIN_ROUNDS</code></td>
<td><code>defaults/hash_rounds_min</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SHA_CRYPT_MAX_ROUNDS</code></td>
<td><code>defaults/hash_rounds_max</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>UID_MIN</code></td>
<td><code>userdefaults/LU_UIDNUMBER</code>
</td>
</tr>
</table>
<p> The following variables are <i>not</i> imported: <code>CREATE_HOME</code>, <code>GID_MAX</code>, <code>MAIL_FILE</code>, <code>SYSLOG_SG_ENAB</code>, <code>UID_MAX</code>, <code>UMASK</code>, <code>USERDEL_CMD</code>, <code>USERGROUPS_ENAB</code> </p>
<dt><code>default_useradd</code></p>
<dd>A path to the <i>default/useradd</i> file from <code>useradd</code> in <code>shadow</code>. If this variable is defined, the variables from the named file are used in place of some <code>libuser</code> variables. Variables explicitly defined in <i>libuser.conf</i> are not affected by contents of <i>default/useradd</i>. </p>
<p> The following variables are imported: </p>
<table>
<tr VALIGN=top>
<td>Variable</td>
<td>Imported as
</td>
</tr>
<tr VALIGN=top>
<td>EXPIRE</td>
</tr>
<tr VALIGN=top>
<td><code>GROUP</code></td>
<td><code>userdefaults/LU_GIDNUMBER</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>HOME</code></td>
<td><code>userdefaults/LU_HOMEDIRECTORY</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>INACTIVE</code></td>
<td><code>userdefaults/LU_SHADOWINACTIVE</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SHELL</code></td>
<td><code>userdefaults/LU_LOGINSHELL</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>SKEL</code></td>
<td><code>defaults/skeleton</code>
</td>
</tr>
</table>
<p> The <code>HOME</code> variable value has <code>/%n</code> appended to it before importing. </p>
</dl>
<h2><code>[userdefaults]</code></h2>
<p>This section defines attribute values of newly created user entities. There is one special variable: </p>
<dl>
<dt><code>LU_UIDNUMBER</code></p>
<dd>A decimal number, the first allowed UID value for regular users (not system users). Default value is <code>500</code>. </p>
</dl>
<p> All other variables have the same names as the attribute names from <code>&lt;libuser/entity.h&gt;</code> and define attribute values. Either the macro name (e.g. <code>LU_GECOS</code>) or the macro content (e.g. <code>pw_gecos</code>) can be used; if both are used, the one appearing later in the configuration file is used. </p>
<p> The <code>%</code> character in the value of the variable introduces an escape sequence: <code>%n</code> is replaced by the user name, <code>%d</code> is replaced by current date in days since the epoch, <code>%u</code> is replaced by the user&#8217;s UID. There is no way to escape the <code>%</code> character and avoid this substitution. </p>
<p> After the <code>userdefaults</code> section is processed, modules may define additional attributes or even override the attributes defined in this section.</p>
<h2><code>[groupdefaults]</code></h2>
<p>The <code>groupdefaults</code> section is similar to <code>userdefaults</code>. There is one special variable: </p>
<dl>
<dt><code>LU_GIDNUMBER</code></p>
<dd>A decimal number, the first allowed GID value for regular groups (not system groups). Default value is <code>500</code>. </p>
</dl>
<p> The other variables follow the same rules as in the <code>userdefaults</code> section, except that <code>%n</code> and <code>%u</code> are replaced by the group name and group&#8217;s GID, respectively. </p>
<p> After the <code>groupdefaults</code> section is processed, modules may define additional attributes or even override the attributes defined in this section.</p>
<h2><code>[files]</code></h2>
<p>Configures the <code>files</code> module, which manages <i>/etc/group</i> and <i>/etc/passwd</i>. The configuration variables are probably useful only for <code>libuser</code> development. </p>
<dl>
<dt><code>directory</code></p>
<dd>The directory containing the <i>group</i> and <i>passwd</i> files. Default value is <code>/etc</code>. </p>
<dt><code>nonroot</code></p>
<dd>Allow module initialization when not invoked as the <code>root</code> user if the value is <code>yes</code>. </p>
</dl>
<h2><code>[shadow]</code></h2>
<p>Configures the <code>files</code> module, which manages <i>/etc/gshadow</i> and <i>/etc/shadow</i>. The configuration variables are probably useful only for <code>libuser</code> development. </p>
<dl>
<dt><code>directory</code></p>
<dd>The directory containing the <i>gshadow</i> and <i>shadow</i> files. Default value is <code>/etc</code>. </p>
<dt><code>nonroot</code></p>
<dd>Allow module initialization when not invoked as the <code>root</code> user if the value is <code>yes</code>. </p>
</dl>
<h2><code>[ldap]</code></h2>
<p>Configures the <code>ldap</code> module, which manages an user database accessible using LDAP. </p>
<dl>
<dt><code>userBranch</code></p>
<dd>The LDAP suffix for user entities. Default value is <code>ou=People</code>. </p>
<dt><code>groupBranch</code></p>
<dd>The LDAP suffix for group entities. Default value is <code>ou=Group</code>. </p>
<dt><code>server</code></p>
<dd>A domain name or an URI of the LDAP server. The URI can use the <code>ldap</code>, <code>ldapi</code> or the <code>ldaps</code> protocol. When a simple domain name is used, the connection fails if TLS can not be used; an URI using the <code>ldap</code> protocol allows connection without TLS. TLS is never used with the <code>ldapi</code> protocol. Default value is <code>ldap</code>. </p>
<dt><code>basedn</code></p>
<dd>The base DN of the server. Default value is <code>dc=example,dc=com</code>. </p>
<dt><code>binddn</code></p>
<dd>A DN for binding to the server. If the value is empty or binding using this DN fails, a DN of <code>uid=</code><i>user</i>,<i>userBranch</i>,<i>basedn</i> is used, where <i>userBranch</i> and <i>basedn</i> are variables from this section and <i>user</i> is the user name of the invoking user, unless overridden by the <code>user</code> variable from this section. Default value is <code>cn=manager,dc=example,dc=com</code>. </p>
<dt><code>user</code></p>
<dd>The SASLv2 identity for authenticating to the LDAP server, also overrides the user name for generating a bind DN. Default value is the name of the invoking user. </p>
<dt><code>password</code></p>
<dd>The password used for a simple bind by default. If not specified, there is no default and the user must supply the password each time. </p>
<p> <code>IT IS STRONGLY RECOMMENDED NOT TO STORE A PASSWORD IN THE SYSTEM-WIDE</code> <i>/etc/libuser.conf</i> <code>FILE.</code> The configuration file is world-readable by default, and setuid programs that prompt for a server name could be used to send the password to an attacker-controlled server. </p>
<dt><code>authuser</code></p>
<dd>The SASLv2 authorization user, if non-empty. Default value is empty. </p>
<dt><code>bindtype</code></p>
<dd>The list of bind types to use, separated by commas. Allowed bind types are <code>simple</code>, <code>sasl</code>, and <code>sasl/</code><i>mechanism</i>, where <i>mechanism</i> is a SASL mechanism. The bind types (but not necessarily <i>mechanism</i>) are case-insensitive. If more than one bind type is specified, their relative order is ignored. Default value is <code>simple,sasl</code>. </p>
</dl>
<h2><code>[sasl]</code></h2>
<p>Configures the <code>sasl</code> module, which manages a SASLv2 user database. </p>
<dl>
<dt><code>appname</code></p>
<dd>Name of the SASLv2 application. Default value is empty. </p>
<dt><code>domain</code></p>
<dd>Domain used by libuser for the SASLv2 authentication object. Default value is empty. </p>
</dl>
<h2>Bugs</h2>
<p>Invalid lines in the configuration file (or the imported <code>shadow</code> configuration files) are silently ignored. </p>
<h2>Files</h2>
<dl>
<dt><i>/etc/libuser.conf</i></p>
<dd>The default location of the configuration file. Can be overridden by the <i>LIBUSER_CONF</i> environment variable, except in set-uid or set-gid programs. </p>
</dl>
