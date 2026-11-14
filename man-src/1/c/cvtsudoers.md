---
title: "cvtsudoers(1)"
name: "cvtsudoers"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cvtsudoers/"
description: "cvtsudoers – convert between sudoers file formats"
---

<p>Sudo 1.9.9</p>
<h2 class="name">NAME</h2>
<p> <code>cvtsudoers</code> &#8211; convert between sudoers file formats </p>
<h2>SYNOPSIS</h2>
<p> <code>cvtsudoers</code> [-<code>ehMpV</code> ] [-<code>b </code><i>dn</i> ] [-<code>c </code><i>conf_file</i> ] [-<code>d </code><i>deftypes</i> ] [-<code>f </code><i>output_format</i> ] [-<code>i </code><i>input_format</i> ] [-<code>I </code><i>increment</i> ] [-<code>l </code><i>log_file</i> ] [-<code>m </code><i>filter</i> ] [-<code>o </code><i>output_file</i> ] [-<code>O </code><i>start_point</i> ] [-<code>P </code><i>padding</i> ] [-<code>s </code><i>sections</i> ] [<i>input_file &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>cvtsudoers</code> utility accepts one or more security policies in either <i>sudoers</i> or LDIF format as input, and generates a single policy of the specified format as output. The default input format is <i>sudoers.</i> The default output format is LDIF. It is only possible to convert a policy file that is syntactically correct. </p>
<p> If no <i>input_file</i> is specified, or if it is `-&#8216; , the policy is read from the standard input. Input files may be optionally prefixed with a host name followed by a colon (`:&#8217; ) to make the policy rules specific to a host when merging multiple files. By default, the result is written to the standard output. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-b </code><i>dn , &#8211;</i><code>-base = </code><i>dn</i></p>
<dd> The base DN (distinguished name) that will be used when performing LDAP queries. Typically this is of the form <code>ou=SUDOers,dc=my-domain,dc=com</code> for the domain <code>my-domain.com</code> If this option is not specified, the value of the <code>SUDOERS_BASE</code> environment variable will be used instead. Only necessary when converting to LDIF format.</p>
<dt><code>-c </code><i>conf_file , &#8211;</i><code>-config = </code><i>conf_file</i></p>
<dd> Specify the path to the configuration file. Defaults to /etc/cvtsudoers.conf</p>
<dt><code>-d </code><i>deftypes , &#8211;</i><code>-defaults = </code><i>deftypes</i></p>
<dd> Only convert <code>Defaults</code> entries of the specified types. One or more <code>Defaults</code> types may be specified, separated by a comma (`,&#8217; ) The supported types are:</p>
<dl>
<dt><code>all</code></p>
<dd> All Defaults entries.</p>
<dt><code>global</code></p>
<dd> Global Defaults entries that are applied regardless of user, runas, host, or command.</p>
<dt><code>user</code></p>
<dd> Per-user Defaults entries.</p>
<dt><code>runas</code></p>
<dd> Per-runas user Defaults entries.</p>
<dt><code>host</code></p>
<dd> Per-host Defaults entries.</p>
<dt><code>command</code></p>
<dd> Per-command Defaults entries.</dl>
<p> See the <code>Defaults</code> section in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5) for more information. </p>
<p> If the &#8211;<code>d</code> option is not specified, all <code>Defaults</code> entries will be converted.</p>
<dt><code>-e , &#8211;expand-aliases</code></p>
<dd> Expand aliases in <i>input_file</i> Aliases are preserved by default when the output <i>format</i> is JSON or sudoers.</p>
<dt><code>-f </code><i>output_format , &#8211;</i><code>-output-format = </code><i>output_format</i></p>
<dd> Specify the output format (case-insensitive). The following formats are supported:</p>
<dl>
<dt><code>CSV</code></p>
<dd> CSV (comma-separated value) files are often used by spreadsheets and report generators. For CSV output, <code>cvtsudoers</code> double quotes strings that contain commas. For each literal double quote character present inside the string, two double quotes are output. This method of quoting commas is compatible with most spreadsheet programs.</p>
<dt><code>JSON</code></p>
<dd> JSON (JavaScript Object Notation) files are usually easier for third-party applications to consume than the traditional <i>sudoers</i> format. The various values have explicit types which removes much of the ambiguity of the <i>sudoers</i> format.</p>
<dt><code>LDIF</code></p>
<dd> LDIF (LDAP Data Interchange Format) files can be imported into an LDAP server for use with sudoers.ldap5. </p>
<p> Conversion to LDIF has the following limitations: </p>
<ul>
<li> Command, host, runas, and user-specific Defaults lines cannot be translated as they don&#8217;t have an equivalent in the sudoers LDAP schema.
<li> Command, host, runas, and user aliases are not supported by the sudoers LDAP schema so they are expanded during the conversion. </ul>
<dt><code>sudoers</code></p>
<dd> Traditional sudoers format. A new sudoers file will be reconstructed from the parsed input file. Comments are not preserved and data from any include files will be output inline.</dl>
<dt><code>&#8211;group-file = </code><i>file</i></p>
<dd> When the &#8211;<code>M</code> option is also specified, perform group queries using <i>file</i> instead of the system group database.</p>
<dt><code>-h , &#8211;help</code></p>
<dd> Display a short help message to the standard output and exit.</p>
<dt><code>-i </code><i>input_format , &#8211;</i><code>-input-format = </code><i>input_format</i></p>
<dd> Specify the input format. The following formats are supported:</p>
<dl>
<dt><code>LDIF</code></p>
<dd> LDIF (LDAP Data Interchange Format) files can be exported from an LDAP server to convert security policies used by sudoers.ldap5. If a base DN (distinguished name) is specified, only sudoRole objects that match the base DN will be processed. Not all sudoOptions specified in a sudoRole can be translated from LDIF to sudoers format.</p>
<dt><code>sudoers</code></p>
<dd> Traditional sudoers format. This is the default input format.</dl>
<dt><code>-I </code><i>increment , &#8211;</i><code>-increment = </code><i>increment</i></p>
<dd> When generating LDIF output, increment each sudoOrder attribute by the specified number. Defaults to an increment of 1.</p>
<dt><code>-l </code><i>log_file , &#8211;</i><code>-logfile = </code><i>log_file</i></p>
<dd> Log conversion warnings to <i>log_file</i> instead of to the standard error. This is particularly useful when merging multiple <i>sudoers</i> files, which can generate a large number of warnings.</p>
<dt><code>-m </code><i>filter , &#8211;</i><code>-match = </code><i>filter</i></p>
<dd> Only output rules that match the specified <i>filter</i> A <i>filter</i> expression is made up of one or more <code>key = </code><i>value</i> pairs, separated by a comma (`,&#8217; ) The <code>key</code> may be &#8220;cmnd&#8221; (or &#8220;cmd&#8221; ) &#8220;host&#8221; &#8220;group&#8221; or &#8220;user&#8221; For example, <code>user = </code><i>operator</i> or <code>host = </code><i>www</i> An upper-case Cmnd_Alias, Host_alias, or Host_Alias may be specified as the &#8220;cmnd&#8221; &#8220;host&#8221; or &#8220;user&#8221; </p>
<p> A matching <i>sudoers</i> rule may also include users, groups, and hosts that are not part of the <i>filter</i> This can happen when a rule includes multiple users, groups, or hosts. To prune out any non-matching user, group, or host from the rules, the &#8211;<code>p</code> option may be used. </p>
<p> By default, the password and group databases are not consulted when matching against the filter so the users and groups do not need to be present on the local system (see the &#8211;<code>M</code> option). Only aliases that are referenced by the filtered policy rules will be displayed.</p>
<dt><code>-M , &#8211;match-local</code></p>
<dd> When the &#8211;<code>m</code> option is also specified, use password and group database information when matching users and groups in the filter. Only users and groups in the filter that exist on the local system will match, and a user&#8217;s groups will automatically be added to the filter. If the &#8211;<code>M</code> is <i>not</i> specified, users and groups in the filter do not need to exist on the local system, but all groups used for matching must be explicitly listed in the filter.</p>
<dt><code>-o </code><i>output_file , &#8211;</i><code>-output = </code><i>output_file</i></p>
<dd> Write the converted output to <i>output_file</i> If no <i>output_file</i> is specified, or if it is `-&#8216; , the converted <i>sudoers</i> policy will be written to the standard output.</p>
<dt><code>-O </code><i>start_point , &#8211;</i><code>-order-start = </code><i>start_point</i></p>
<dd> When generating LDIF output, use the number specified by <i>start_point</i> in the sudoOrder attribute of the first sudoRole object. Subsequent sudoRole object use a sudoOrder value generated by adding an <i>increment</i> see the &#8211;<code>I</code> option for details. Defaults to a starting point of 1. A starting point of 0 will disable the generation of sudoOrder attributes in the resulting LDIF file.</p>
<dt><code>&#8211;passwd-file = </code><i>file</i></p>
<dd> When the &#8211;<code>M</code> option is also specified, perform passwd queries using <i>file</i> instead of the system passwd database.</p>
<dt><code>-p , &#8211;prune-matches</code></p>
<dd> When the &#8211;<code>m</code> option is also specified, <code>cvtsudoers</code> will prune out non-matching users, groups, and hosts from matching entries.</p>
<dt><code>-P </code><i>padding , &#8211;</i><code>-padding = </code><i>padding</i></p>
<dd> When generating LDIF output, construct the initial sudoOrder value by concatenating <i>order_start</i> and <i>increment</i> padding the <i>increment</i> with zeros until it consists of <i>padding</i> digits. For example, if <i>order_start</i> is 1027, <i>padding</i> is 3, and <i>increment</i> is 1, the value of sudoOrder for the first entry will be 1027000, followed by 1027001, 1027002, etc. If the number of sudoRole entries is larger than the padding would allow, <code>cvtsudoers</code> will exit with an error. By default, no padding is performed.</p>
<dt><code>-s </code><i>sections , &#8211;</i><code>-suppress = </code><i>sections</i></p>
<dd> Suppress the output of specific <i>sections</i> of the security policy. One or more section names may be specified, separated by a comma (`,&#8217; ) The supported section name are: <code>defaults</code> <code>aliases</code> and <code>privileges</code> (which may be shortened to <code>privs )</code></p>
<dt><code>-V , -version</code></p>
<dd> Print the <code>cvtsudoers</code> and <i>sudoers</i> grammar versions and exit.</dl>
<h3>Merging multiple files</h3>
<p> When multiple input files are specified, <code>cvtsudoers</code> will attempt to merge them into a single policy file. It is assumed that user and group names are consistent among the policy files to be merged. For example, user &#8220;bob&#8221; on one host is the same as user &#8220;bob&#8221; on another host. </p>
<p> When merging policy files, it is possible to prefix the input file name with a host name, separated by a colon (`:&#8217; ) When the files are merged, the host name will be used to restrict the policy rules to that specific host where possible. </p>
<p> The merging process is performed as follows: </p>
<ul>
<li> Each input file is parsed into internal sudoers data structures.
<li> Aliases are merged and renamed as necessary to avoid conflicts. In the event of a conflict, the first alias found is left as-is and subsequent aliases of the same name are renamed with a numeric suffix separated with a underscore (`_&#8217; ) For example, if there are two different aliases named <code>SERVERS</code> the first will be left as-is and the second will be renamed <code>SERVERS_1</code> References to the renamed alias are also updated in the policy file. Duplicate aliases (those with identical contents) are pruned.
<li> Defaults settings are merged and duplicates are removed. If there are conflicts in the Defaults settings, a warning is emitted for each conflict. If a host name is specified with the input file, <code>cvtsudoers</code> will change the global Defaults settings in that file to be host-specific. A warning is emitted for command, user, or runas-specific Defaults settings which cannot be made host-specific.
<li> Per-user rules are merged and duplicates are removed. If a host name is specified with the input file, <code>cvtsudoers</code> will change rules that specify a host name of <code>ALL</code> to the host name associated with the policy file being merged. The merging of rules is currently fairly simplistic but will be improved in a later release. </ul>
<p> It is possible to merge policy files with differing formats.</p>
<h3>The cvtsudoers.conf file</h3>
<p> Options in the form &#8220;keyword = value&#8221; may also be specified in a configuration file, /etc/cvtsudoers.conf by default. The following keywords are recognized:</p>
<dl>
<dt><code>defaults = </code><i>deftypes</i></p>
<dd> See the description of the &#8211;<code>d</code> command line option.</p>
<dt><code>expand_aliases = </code><i>yes | no</i></p>
<dd> See the description of the &#8211;<code>e</code> command line option.</p>
<dt><code>group_file = </code><i>file</i></p>
<dd> See the description of the &#8211;<code>-group-file</code> command line option.</p>
<dt><code>input_format = </code><i>ldif | sudoers</i></p>
<dd> See the description of the &#8211;<code>i</code> command line option.</p>
<dt><code>match = </code><i>filter</i></p>
<dd> See the description of the &#8211;<code>m</code> command line option.</p>
<dt><code>match_local = </code><i>yes | no</i></p>
<dd> See the description of the &#8211;<code>M</code> command line option.</p>
<dt><code>order_increment = </code><i>increment</i></p>
<dd> See the description of the &#8211;<code>I</code> command line option.</p>
<dt><code>order_start = </code><i>start_point</i></p>
<dd> See the description of the &#8211;<code>O</code> command line option.</p>
<dt><code>output_format = </code><i>csv | json | ldif | sudoers</i></p>
<dd> See the description of the &#8211;<code>f</code> command line option.</p>
<dt><code>padding = </code><i>padding</i></p>
<dd> See the description of the &#8211;<code>P</code> command line option.</p>
<dt><code>passwd_file = </code><i>file</i></p>
<dd> See the description of the &#8211;<code>-passwd-file</code> command line option.</p>
<dt><code>prune_matches = </code><i>yes | no</i></p>
<dd> See the description of the &#8211;<code>p</code> command line option.</p>
<dt><code>sudoers_base = </code><i>dn</i></p>
<dd> See the description of the &#8211;<code>b</code> command line option.</p>
<dt><code>suppress = </code><i>sections</i></p>
<dd> See the description of the &#8211;<code>s</code> command line option.</dl>
<p> Options on the command line will override values from the configuration file.</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/cvtsudoers.conf </code></p>
<dd> default configuration for cvtsudoers</dl>
<h2>EXAMPLES</h2>
<p> Convert /etc/sudoers to LDIF (LDAP Data Interchange Format) where the ldap.conf file uses a <i>sudoers_base</i> of my-domain,dc=com, storing the result in sudoers.ldif </p>
<blockquote>
<pre>
$ cvtsudoers -b ou=SUDOers,dc=my-domain,dc=com -o sudoers.ldif \
             /etc/sudoers
</pre>
</blockquote>
<p> Convert /etc/sudoers to JSON format, storing the result in sudoers.json </p>
<blockquote>
<pre>
$ cvtsudoers -f json -o sudoers.json /etc/sudoers
</pre>
</blockquote>
<p> Parse /etc/sudoers and display only rules that match user <i>ambrose</i> on host <i>hastur</i> </p>
<blockquote>
<pre>
$ cvtsudoers -f sudoers -m user=ambrose,host=hastur /etc/sudoers
</pre>
</blockquote>
<p> Same as above, but expand aliases and prune out any non-matching users and hosts from the expanded entries. </p>
<blockquote>
<pre>
$ cvtsudoers -ep -f sudoers -m user=ambrose,host=hastur /etc/sudoers
</pre>
</blockquote>
<p> Convert sudoers.ldif from LDIF to traditional <i>sudoers</i> format: </p>
<blockquote>
<pre>
$ cvtsudoers -i ldif -f sudoers -o sudoers.new sudoers.ldif
</pre>
</blockquote>
<p> Merge a global <i>sudoers</i> file with two host-specific policy files from the hosts &#8220;xyzzy&#8221; and &#8220;plugh&#8221; </p>
<blockquote>
<pre>
$ cvtsudoers -f sudoers -o sudoers.merged sudoers \
    xyzzy:sudoers.xyzzy plugh:sudoers.plugh
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), sudoers.ldap5, <a href="/docs/linux/man/8-sudo/">sudo</a>(8)</p>
<h2>AUTHORS</h2>
<p> Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>BUGS</h2>
<p> If you feel you have found a bug in <code>cvtsudoers,</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>SUPPORT</h2>
<p> Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>DISCLAIMER</h2>
<p> <code>cvtsudoers</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details. </p>
<h2>Index</h2>
