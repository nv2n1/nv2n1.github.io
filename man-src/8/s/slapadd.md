---
title: "slapadd(8)"
name: "slapadd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slapadd/"
description: "slapadd – Add entries to a SLAPD database"
---

<p>slapadd &#8211; Add entries to a SLAPD database</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/slapadd</code> [<code>-b</code><i>&nbsp;<wbr>suffix</i>] [<code>-c</code>] [<code>-d</code><i>&nbsp;<wbr>debug-level</i>] [<code>-f</code><i>&nbsp;<wbr>slapd.conf</i>] [<code>-F</code><i>&nbsp;<wbr>confdir</i>] [<code>-g</code>] [<code>-j</code><i>&nbsp;<wbr>lineno</i>] [<code>-l</code><i>&nbsp;<wbr>ldif-file</i>] [<code>-n</code><i>&nbsp;<wbr>dbnum</i>] [<code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]] [<code>-q</code>] [<code>-s</code>] [<code>-S</code><i>&nbsp;<wbr>SID</i>] [<code>-u</code>] [<code>-v</code>] [<code>-w</code>]</p>
<h2>Description</h2>
<p><code>Slapadd</code> is used to add entries specified in LDAP Directory Interchange Format (LDIF) to a <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) database. It opens the given database determined by the database number or suffix and adds entries corresponding to the provided LDIF to the database. Databases configured as <code>subordinate</code> of this one are also updated, unless <code>-g</code> is specified. The LDIF input is read from standard input or the specified file. </p>
<p> All files eventually created by <code>slapadd</code> will belong to the identity <code>slapadd</code> is run as, so make sure you either run <code>slapadd</code> with the same identity <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) will be run as (see option <code>-u</code> in <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8)), or change file ownership before running <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8). </p>
<p> Note: slapadd will also perform the relevant indexing whilst adding the database if any are configured. For specfic details, please see <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8).</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code><i>&nbsp;<wbr>suffix</i></p>
<dd>Use the specified <i>suffix</i> to determine which database to add entries to. The <code>-b</code> cannot be used in conjunction with the <code>-n</code> option.</p>
<dt><code>-c</code></p>
<dd>enable continue (ignore errors) mode.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debug-level</i></p>
<dd>enable debugging messages as defined by the specified <i>debug-level</i>; see <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) for details.</p>
<dt><code>-f</code><i>&nbsp;<wbr>slapd.conf</i></p>
<dd>specify an alternative <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file.</p>
<dt><code>-F</code><i>&nbsp;<wbr>confdir</i></p>
<dd>specify a config directory. If both <code>-f</code> and <code>-F</code> are specified, the config file will be read and converted to config directory format and written to the specified directory. If neither option is specified, an attempt to read the default config directory will be made before trying to use the default config file. If a valid config directory exists then the default config file is ignored. If dry-run mode is also specified, no conversion will occur.</p>
<dt><code>-g</code></p>
<dd>disable subordinate gluing. Only the specified database will be processed, and not its glued subordinates (if any).</p>
<dt><code>-j</code><i>&nbsp;<wbr>lineno</i></p>
<dd>Jump to the specified line number in the LDIF file before processing any entries. This allows a load that was aborted due to errors in the input LDIF to be resumed after the errors are corrected.</p>
<dt><code>-l</code><i>&nbsp;<wbr>ldif-file</i></p>
<dd>Read LDIF from the specified file instead of standard input.</p>
<dt><code>-n</code><i>&nbsp;<wbr>dbnum</i></p>
<dd>Add entries to the <i>dbnum</i>-th database listed in the configuration file. The <code>-n</code> cannot be used in conjunction with the <code>-b</code> option. To populate the config database <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), use <code>-n 0</code> as it is always the first database. It must physically exist on the filesystem prior to this, however.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>Specify an <i>option</i> with a(n optional) <i>value</i>. Possible generic options/values are:</dl>
<pre> syslog=&lt;subsystems&gt; (see `-s' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-level=&lt;level&gt; (see `-S' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-user=&lt;user&gt; (see `-l' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 schema-check={yes|no}
 value-check={yes|no}
The <i>schema-check</i> option toggles schema checking (default on);
the <i>value-check</i> option toggles value checking (default off).
The latter is incompatible with <code>-q</code>.
<dl><dt><code>-q</code>
<dd>enable quick (fewer integrity checks) mode. Does fewer consistency checks
on the input data, and no consistency checks when writing the database.
Improves the load time but if any errors or interruptions occur the resulting
database will be unusable.
<dt><code>-s</code>
<dd>disable schema checking. This option is intended to be used when loading
databases containing special objects, such as fractional objects on a
partial replica. Loading normal objects which do not conform to
schema may result in unexpected and ill behavior.
<dt><code>-S</code><i>&nbsp;<wbr>SID</i>
<dd>Server ID to use in generated entryCSN. Also used for contextCSN
if <code>-w</code> is set as well. Defaults to <code>0</code>.
<dt><code>-u</code>
<dd>enable dry-run (don't write to backend) mode.
<dt><code>-v</code>
<dd>enable verbose mode.
<dt><code>-w</code>
<dd>write syncrepl context information.
After all entries are added, the contextCSN
will be updated with the greatest CSN in the database.
</dl></pre>
<h2>Limitations</h2>
<p>Your <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) should not be running when you do this to ensure consistency of the database. </p>
<p> <code>slapadd </code> may not provide naming or schema checks. It is advisable to use <code><a href="/docs/linux/man/1-ldapadd/">ldapadd</a></code>(1) when adding new entries into an existing directory.</p>
<h2>Examples</h2>
<p>To import the entries specified in file <code>ldif</code> into your <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) database give the command: </p>
<pre> /usr/sbin/slapadd -l ldif</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8), <code><a href="/docs/linux/man/8-slapindex/">slapindex</a></code>(8), <code><a href="/docs/linux/man/1-ldapadd/">ldapadd</a></code>(1), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
