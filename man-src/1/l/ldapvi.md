---
title: "ldapvi(1)"
name: "ldapvi"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldapvi/"
description: "ldapvi – LDAP client"
---

<h2>NAME</h2>
<p> ldapvi &#8211; LDAP client</p>
<h2>SYNOPSIS</h2>
<p> <code>ldapvi</code> [<i>OPTION</i>]&#8230; [<i>FILTER</i>] [<i>AD</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<h3>Quickstart:</h3>
<dl>
<dt>
<dd> ldapvi <code>&#8211;discover</code> <code>&#8211;host</code> HOSTNAME</dl>
<p> Perform an LDAP search and update results using a text editor.</p>
<h3>Other usage:</h3>
<dl>
<dt>ldapvi <code>&#8211;out</code> [OPTION]&#8230; [FILTER] [AD]&#8230;</p>
<dd> Print entries</p>
<dt>ldapvi <code>&#8211;in</code> [OPTION]&#8230; [FILENAME]</p>
<dd> Load change records</p>
<dt>ldapvi <code>&#8211;delete</code> [OPTION]&#8230; DN&#8230;</p>
<dd> Edit a delete record</p>
<dt>ldapvi <code>&#8211;rename</code> [OPTION]&#8230; DN1 DN2</p>
<dd> Edit a rename record</dl>
<h3>Connection options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;host</code> URL</p>
<dd> Server.</p>
<dt><code>-D</code>, <code>&#8211;user</code> USER</p>
<dd> Search filter or DN: User to bind as. [1] Sets <code>&#8211;bind</code> simple.</p>
<dt><code>-w</code>, <code>&#8211;password</code> SECRET</p>
<dd> Password (also valid for SASL).</p>
<dt><code>&#8211;bind</code> [simple,sasl]</p>
<dd> Disable or enable SASL.</p>
<dt><code>&#8211;bind-dialog</code> [never,auto,always]</p>
<dd> Interactive login dialog.</dl>
<h3>SASL options (these parameters set &#8211;bind sasl):</h3>
<dl>
<dt> <code>-I</code>, <code>&#8211;sasl-interactive</code> Set <code>&#8211;bind-dialog</code> always.</p>
<dt><code>-O</code>, <code>&#8211;sasl-secprops</code> P</p>
<dd>
<dd>SASL security properties.</p>
<dt><code>-Q</code>, <code>&#8211;sasl-quiet</code></p>
<dd> Set <code>&#8211;bind-dialog</code> never.</p>
<dt><code>-R</code>, <code>&#8211;sasl-realm</code></p>
<dd> R SASL realm.</p>
<dt><code>-U</code>, <code>&#8211;sasl-authcid</code> AC</p>
<dd> SASL authentication identity.</p>
<dt><code>-X</code>, <code>&#8211;sasl-authzid</code> AZ</p>
<dd> SASL authorization identity.</p>
<dt><code>-Y</code>, <code>&#8211;sasl-mech</code></p>
<dd> MECH SASL mechanism.</dl>
<h3>Search parameters:</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;base</code> DN</p>
<dd> Search base.</p>
<dt><code>-s</code>, <code>&#8211;scope</code> SCOPE</p>
<dd> Search scope. One of base|one|sub.</p>
<dt><code>-S</code>, <code>&#8211;sort</code> KEYS</p>
<dd> Sort control (critical).</dl>
<h3>Miscellaneous options:</h3>
<dl>
<dt><code>&#8211;add</code></p>
<dd> (Only with <code>&#8211;in</code>, <code>&#8211;ldapmodify</code>:) Treat attrval records as new entries to add.</p>
<dt><code>-o</code>, <code>&#8211;class</code> OBJCLASS</p>
<dd> Class to add. Can be repeated. Implies <code>-A</code>.</p>
<dt><code>&#8211;config</code></p>
<dd> Print parameters in ldap.conf syntax.</p>
<dt><code>-c</code> <code>&#8211;continue</code></p>
<dd> Ignore LDAP errors and continue processing.</p>
<dt><code>&#8211;deleteoldrdn</code></p>
<dd> (Only with <code>&#8211;rename</code>:) Delete the old RDN.</p>
<dt><code>-a</code>, <code>&#8211;deref</code></p>
<dd> never|searching|finding|always</p>
<dt><code>-d</code>, <code>&#8211;discover</code></p>
<dd> Auto-detect naming contexts. [2]</p>
<dt><code>-A</code>, <code>&#8211;empty</code></p>
<dd> Don&#8217;t search, start with empty file. See <code>-o</code>.</p>
<dt><code>&#8211;encoding</code> [ASCII|UTF-8|binary]</p>
<dd> The encoding to allow. Default is UTF-8.</p>
<dt><code>-H</code>, <code>&#8211;help</code></p>
<dd> This help.</p>
<dt><code>&#8211;ldap-conf</code></p>
<dd> Always read libldap configuration.</p>
<dt><code>-m</code>, <code>&#8211;may</code></p>
<dd> Show missing optional attributes as comments.</p>
<dt><code>-M</code>, <code>&#8211;managedsait</code></p>
<dd> manageDsaIT control (critical).</p>
<dt><code>&#8211;noquestions</code></p>
<dd> Commit without asking for confirmation.</p>
<dt>-!, <code>&#8211;noninteractive</code></p>
<dd> Never ask any questions.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Disable progress output.</p>
<dt><code>-R</code>, <code>&#8211;read</code> DN</p>
<dd> Same as <code>-b</code> DN <code>-s</code> base &#8216;(objectclass=*)&#8217; + *</p>
<dt><code>-Z</code>, <code>&#8211;starttls</code></p>
<dd> Require startTLS.</p>
<dt><code>&#8211;tls</code> [never|allow|try|strict]</p>
<dd> Level of TLS strictess.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Note every update.</dl>
<h3>Shortcuts:</h3>
<dl>
<dt><code>&#8211;ldapsearch</code></p>
<dd> Short for <code>&#8211;quiet</code> <code>&#8211;out</code></p>
<dt><code>&#8211;ldapmodify</code></p>
<dd> Short for <code>&#8211;noninteractive</code> <code>&#8211;in</code></p>
<dt><code>&#8211;ldapdelete</code></p>
<dd> Short for <code>&#8211;noninteractive</code> <code>&#8211;delete</code></p>
<dt><code>&#8211;ldapmoddn</code></p>
<dd> Short for <code>&#8211;noninteractive</code> <code>&#8211;rename</code></dl>
<p> Environment variables: VISUAL, EDITOR, PAGER.</p>
<h3>[1] User names can be specified as distinguished names:</h3>
<dl>
<dt>
<dd> uid=foo,ou=bar,dc=acme,dc=com</p>
<dt>
<dd> or search filters:</p>
<dt>
<dd> (uid=foo)</p>
<dt>
<dd> Note the use of parenthesis, which can be omitted from search filters usually but are required here. For this searching bind to work, your client library must be configured with appropriate default search parameters.</dl>
<p> [2] Repeat the search for each naming context found and present the</p>
<dl>
<dt>concatenation of all search results.</p>
<dd> Conflicts with <code>&#8211;base</code>.</p>
<dt>
<dd> With <code>&#8211;config</code>, show a BASE configuration line for each context.</dl>
<p> A special (offline) option is <code>&#8211;diff</code>, which compares two files and writes any changes to standard output in LDIF format.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &quot;ldapvi [at] lists.askja.de&quot;.</p>
<h2>GETTING STARTED</h2>
<p> Assuming a suitably configured LDAP library, run ldapvi without arguments to see all entries available. </p>
<p> Otherwise, try `ldapvi -h HOSTNAME &#8211;discover&#8217; to query the ROOT DSE for available naming contexts. </p>
<p> Once that works, run `ldapvi -h HOSTNAME &#8211;discover &#8211;config&#8217; to generate sample configuration that can be pasted into ~/.ldaprc or /etc/ldap/ldap.conf. </p>
<h2>FILE FORMAT</h2>
<p> ldapvi uses an LDIF-like syntax, but not standard LDIF. Please refer to <a rel="nofollow" href="http://www.lichteblau.com/ldapvi/manual.xml#syntax">http://www.lichteblau.com/ldapvi/manual.xml#syntax</a> </p>
<h2>BUGS</h2>
<p> Please report bugs to &lt;ldapvi [at] lists.askja.de&gt;. </p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.lichteblau.com/ldapvi/manual.xml">http://www.lichteblau.com/ldapvi/manual.xml</a> </p>
<h2>AUTHOR</h2>
<p> David Lichteblau &lt;david [at] lichteblau.com&gt; </p>
<h2>Index</h2>
