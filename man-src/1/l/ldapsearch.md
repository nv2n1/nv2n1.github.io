---
title: "ldapsearch(1)"
name: "ldapsearch"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldapsearch/"
description: "ldapsearch – LDAP search tool"
---

<h2 class="name">NAME</h2>
<p> ldapsearch &#8211; LDAP search tool </p>
<h2>SYNOPSIS</h2>
<p> <code>ldapsearch</code> [<code>-V</code>[<code>V</code>]] [<code>-d</code><i>&nbsp;<wbr>debuglevel</i>] [<code>-n</code>] [<code>-v</code>] [<code>-c</code>] [<code>-u</code>] [<code>-t</code>[<code>t</code>]] [<code>-T</code><i>&nbsp;<wbr>path</i>] [<code>-F</code><i>&nbsp;<wbr>prefix</i>] [<code>-A</code>] [<code>-L</code>[<code>L</code>[<code>L</code>]]] [<code>-S</code><i>&nbsp;<wbr>attribute</i>] [<code>-b</code><i>&nbsp;<wbr>searchbase</i>] [<code>-s</code>&nbsp;<wbr>{<code>base</code>|<code>one</code>|<code>sub</code>|<code>children</code>}] [<code>-a</code>&nbsp;<wbr>{<code>never</code>|<code>always</code>|<code>search</code>|<code>find</code>}] [<code>-l</code><i>&nbsp;<wbr>timelimit</i>] [<code>-z</code><i>&nbsp;<wbr>sizelimit</i>] [<code>-f</code><i>&nbsp;<wbr>file</i>] [<code>-M</code>[<code>M</code>]] [<code>-x</code>] [<code>-D</code><i>&nbsp;<wbr>binddn</i>] [<code>-W</code>] [<code>-w</code><i>&nbsp;<wbr>passwd</i>] [<code>-y</code><i>&nbsp;<wbr>passwdfile</i>] [<code>-H</code><i>&nbsp;<wbr>ldapuri</i>] [<code>-h</code><i>&nbsp;<wbr>ldaphost</i>] [<code>-p</code><i>&nbsp;<wbr>ldapport</i>] [<code>-P</code>&nbsp;<wbr>{<code>2</code>|<code>3</code>}] [<code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]] [<code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]] [<code>-O</code><i>&nbsp;<wbr>security-properties</i>] [<code>-I</code>] [<code>-Q</code>] [<code>-N</code>] [<code>-U</code><i>&nbsp;<wbr>authcid</i>] [<code>-R</code><i>&nbsp;<wbr>realm</i>] [<code>-X</code><i>&nbsp;<wbr>authzid</i>] [<code>-Y</code><i>&nbsp;<wbr>mech</i>] [<code>-Z</code>[<code>Z</code>]] <i>filter</i> [<i>attrs&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>ldapsearch</i> is a shell-accessible interface to the <code><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a></code>(3) library call. </p>
<p> <code>ldapsearch</code> opens a connection to an LDAP server, binds, and performs a search using specified parameters. The <i>filter</i> should conform to the string representation for search filters as defined in RFC 4515. If not provided, the default filter, <code>(objectClass=*)</code>, is used. </p>
<p> If <code>ldapsearch</code> finds one or more entries, the attributes specified by <i>attrs</i> are returned. If <code>*</code> is listed, all user attributes are returned. If <code>+</code> is listed, all operational attributes are returned. If no <i>attrs</i> are listed, all user attributes are returned. If only 1.1 is listed, no attributes will be returned. </p>
<p> The search results are displayed using an extended version of LDIF. Option <i>-L</i> controls the format of the output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code>[<code>V</code>]</p>
<dd> Print version info. If <code>-VV</code> is given, only the version information is printed.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debuglevel</i></p>
<dd> Set the LDAP debugging level to <i>debuglevel</i>. <code>ldapsearch</code> must be compiled with LDAP_DEBUG defined for this option to have any effect.</p>
<dt><code>-n</code></p>
<dd> Show what would be done, but don&#8217;t actually perform the search. Useful for debugging in conjunction with <code>-v</code>.</p>
<dt><code>-v</code></p>
<dd> Run in verbose mode, with many diagnostics written to standard output.</p>
<dt><code>-c</code></p>
<dd> Continuous operation mode. Errors are reported, but ldapsearch will continue with searches. The default is to exit after reporting an error. Only useful in conjunction with <code>-f</code>.</p>
<dt><code>-u</code></p>
<dd> Include the User Friendly Name form of the Distinguished Name (DN) in the output.</p>
<dt><code>-t</code>[<code>t</code>]</p>
<dd> A single <code>-t</code> writes retrieved non-printable values to a set of temporary files. This is useful for dealing with values containing non-character data such as jpegPhoto or audio. A second <code>-t</code> writes all retrieved values to files.</p>
<dt><code>-T</code><i>&nbsp;<wbr>path</i></p>
<dd> Write temporary files to directory specified by <i>path</i> (default: <code>/var/tmp/</code>)</p>
<dt><code>-F</code><i>&nbsp;<wbr>prefix</i></p>
<dd> URL prefix for temporary files. Default is <code>file://</code><i>path</i> where <i>path</i> is <code>/var/tmp/</code> or specified with <code>-T</code>.</p>
<dt><code>-A</code></p>
<dd> Retrieve attributes only (no values). This is useful when you just want to see if an attribute is present in an entry and are not interested in the specific values.</p>
<dt><code>-L</code></p>
<dd> Search results are display in LDAP Data Interchange Format detailed in <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5). A single <code>-L</code> restricts the output to LDIFv1.<br />
&nbsp;<wbr>A second&nbsp;<wbr><code>-L</code>&nbsp;<wbr>disables comments. A third <code>-L</code> disables printing of the LDIF version. The default is to use an extended version of LDIF.</p>
<dt><code>-S</code><i>&nbsp;<wbr>attribute</i></p>
<dd> Sort the entries returned based on <i>attribute</i>. The default is not to sort entries returned. If <i>attribute</i> is a zero-length string (&quot;&quot;), the entries are sorted by the components of their Distinguished Name. See <code><a href="/docs/linux/man/3-ldap_sort/">ldap_sort</a></code>(3) for more details. Note that <code>ldapsearch</code> normally prints out entries as it receives them. The use of the <code>-S</code> option defeats this behavior, causing all entries to be retrieved, then sorted, then printed.</p>
<dt><code>-b</code><i>&nbsp;<wbr>searchbase</i></p>
<dd> Use <i>searchbase</i> as the starting point for the search instead of the default.</p>
<dt><code>-s</code>&nbsp;<wbr>{<code>base</code>|<code>one</code>|<code>sub</code>|<code>children</code>}</p>
<dd> Specify the scope of the search to be one of <code>base</code>, <code>one</code>, <code>sub</code>, or <code>children</code> to specify a base object, one-level, subtree, or children search. The default is <code>sub</code>. Note: <i>children</i> scope requires LDAPv3 subordinate feature extension.</p>
<dt><code>-a</code>&nbsp;<wbr>{<code>never</code>|<code>always</code>|<code>search</code>|<code>find</code>}</p>
<dd> Specify how aliases dereferencing is done. Should be one of <code>never</code>, <code>always</code>, <code>search</code>, or <code>find</code> to specify that aliases are never dereferenced, always dereferenced, dereferenced when searching, or dereferenced only when locating the base object for the search. The default is to never dereference aliases.</p>
<dt><code>-l</code><i>&nbsp;<wbr>timelimit</i></p>
<dd> wait at most <i>timelimit</i> seconds for a search to complete. A timelimit of <i>0</i> (zero) or <i>none</i> means no limit. A timelimit of <i>max</i> means the maximum integer allowable by the protocol. A server may impose a maximal timelimit which only the root user may override.</p>
<dt><code>-z</code><i>&nbsp;<wbr>sizelimit</i></p>
<dd> retrieve at most <i>sizelimit</i> entries for a search. A sizelimit of <i>0</i> (zero) or <i>none</i> means no limit. A sizelimit of <i>max</i> means the maximum integer allowable by the protocol. A server may impose a maximal sizelimit which only the root user may override.</p>
<dt><code>-f</code><i>&nbsp;<wbr>file</i></p>
<dd> Read a series of lines from <i>file</i>, performing one LDAP search for each line. In this case, the <i>filter</i> given on the command line is treated as a pattern where the first and only occurrence of <code>%s</code> is replaced with a line from <i>file</i>. Any other occurrence of the the <code>%</code> character in the pattern will be regarded as an error. Where it is desired that the search filter include a <code>%</code> character, the character should be encoded as <code>\25</code> (see RFC 4515). If <i>file</i> is a single <code>&#8211;</code> character, then the lines are read from standard input. <code>ldapsearch</code> will exit when the first non-successful search result is returned, unless <code>-c</code> is used.</p>
<dt><code>-M</code>[<code>M</code>]</p>
<dd> Enable manage DSA IT control. <code>-MM</code> makes control critical.</p>
<dt><code>-x </code></p>
<dd> Use simple authentication instead of SASL.</p>
<dt><code>-D</code><i>&nbsp;<wbr>binddn</i></p>
<dd> Use the Distinguished Name <i>binddn</i> to bind to the LDAP directory. For SASL binds, the server is expected to ignore this value.</p>
<dt><code>-W</code></p>
<dd> Prompt for simple authentication. This is used instead of specifying the password on the command line.</p>
<dt><code>-w</code><i>&nbsp;<wbr>passwd</i></p>
<dd> Use <i>passwd</i> as the password for simple authentication.</p>
<dt><code>-y</code><i>&nbsp;<wbr>passwdfile</i></p>
<dd> Use complete contents of <i>passwdfile</i> as the password for simple authentication.</p>
<dt><code>-H</code><i>&nbsp;<wbr>ldapuri</i></p>
<dd> Specify URI(s) referring to the ldap server(s); a list of URI, separated by whitespace or commas is expected; only the protocol/host/port fields are allowed. As an exception, if no host/port is specified, but a DN is, the DN is used to look up the corresponding host(s) using the DNS SRV records, according to RFC 2782. The DN must be a non-empty sequence of AVAs whose attribute type is &quot;dc&quot; (domain component), and must be escaped according to RFC 2396.</p>
<dt><code>-h</code><i>&nbsp;<wbr>ldaphost</i></p>
<dd> Specify an alternate host on which the ldap server is running. Deprecated in favor of <code>-H</code>.</p>
<dt><code>-p</code><i>&nbsp;<wbr>ldapport</i></p>
<dd> Specify an alternate TCP port where the ldap server is listening. Deprecated in favor of <code>-H</code>.</p>
<dt><code>-P</code>&nbsp;<wbr>{<code>2</code>|<code>3</code>}</p>
<dd> Specify the LDAP protocol version to use.</p>
<dt><code>-e</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd>
<dt><code>-E</code>&nbsp;<wbr>[<code>!</code>]<i>ext</i>[<code>=</code><i>extparam</i>]</p>
<dd>
<p> Specify general extensions with <code>-e</code> and search extensions with <code>-E</code>. &#8216;<code>!</code>&#8216; indicates criticality. </p>
<p> General extensions: </p>
<pre><code>
[!] assert = &lt;filter&gt;(an RFC 4515 Filter) !authzid = &lt;authzid&gt;("dn:&lt;dn&gt;" or "u:&lt;user&gt;")
    [!] bauthzid(RFC 3829 authzid control)
        [!] chaining[=&lt;resolve&gt;[/&lt;cont&gt;]]
                    [!] manageDSAit
                        [!] noop
                            ppolicy
                                [!] postread[=&lt;attrs&gt;](a comma - separated attribute list)
                                    [!] preread[=&lt;attrs&gt;](a comma - separated attribute list)
                                        [!] relax
                                            sessiontracking
                                                abandon,
    cancel, ignore(SIGINT sends abandon / cancel, or ignores response; if critical, doesn't wait for SIGINT. not really controls)
</code></pre>
<p> Search extensions:<br />
!dontUseCopy<br />
    [!] domainScope(domain scope)<br />
        [!] mv = &lt;filter&gt;(matched values filter)<br />
    [!] pr = &lt;size&gt;[/ prompt | noprompt](paged results / prompt)<br />
        [!] sss = [-]&lt;attr[:OID]&gt;[/[-]&lt;attr[:OID]&gt;&#8230;](server side sorting)<br />
            [!] subentries[= true | false](subentries)<br />
                [!] sync = ro[/&lt;cookie&gt;](LDAP Sync refreshOnly)<br />
                    rp[/&lt;cookie&gt;][/&lt;slimit&gt;](LDAP Sync refreshAndPersist)<br />
                        [!] vlv = &lt;before&gt; / &lt;after&gt;(/ &lt;offset&gt; / &lt;count&gt; |<br />
                                                     : &lt;value&gt;)(virtual list view)<br />
                                                 [!] deref = derefAttr : attr[, attr[&#8230;]] [; derefAttr:attr[, attr[&#8230;]]]<br />
                                                                             [!]&lt;oid&gt;[=&lt;value&gt;]</p>
<dt><code>-o</code><i>&nbsp;<wbr>opt</i>[=<i>optparam</i>]</p>
<dd>
<p> Specify general options. </p>
<p> General options: </p>
<pre>
  nettimeout=&lt;timeout&gt;  (in seconds, or &quot;none&quot; or &quot;max&quot;)
  ldif-wrap=&lt;width&gt;     (in columns, or &quot;no&quot; for no wrapping)
</pre>
<dt><code>-O</code><i>&nbsp;<wbr>security-properties</i></p>
<dd> Specify SASL security properties.</p>
<dt><code>-I</code></p>
<dd> Enable SASL Interactive mode. Always prompt. Default is to prompt only as needed.</p>
<dt><code>-Q</code></p>
<dd> Enable SASL Quiet mode. Never prompt.</p>
<dt><code>-N</code></p>
<dd> Do not use reverse DNS to canonicalize SASL host name.</p>
<dt><code>-U</code><i>&nbsp;<wbr>authcid</i></p>
<dd> Specify the authentication ID for SASL bind. The form of the ID depends on the actual SASL mechanism used.</p>
<dt><code>-R</code><i>&nbsp;<wbr>realm</i></p>
<dd> Specify the realm of authentication ID for SASL bind. The form of the realm depends on the actual SASL mechanism used.</p>
<dt><code>-X</code><i>&nbsp;<wbr>authzid</i></p>
<dd> Specify the requested authorization ID for SASL bind. <i>authzid</i> must be one of the following formats: <code>dn:</code><i>&lt;distinguished name&gt;</i> or <code>u:</code><i>&lt;username&gt;</i></p>
<dt><code>-Y</code><i>&nbsp;<wbr>mech</i></p>
<dd> Specify the SASL mechanism to be used for authentication. If it&#8217;s not specified, the program will choose the best mechanism the server knows.</p>
<dt><code>-Z</code>[<code>Z</code>]</p>
<dd> Issue StartTLS (Transport Layer Security) extended operation. If you use <code>-ZZ</code>, the command will require the operation to be successful.</dl>
<h2>OUTPUT FORMAT</h2>
<p> If one or more entries are found, each entry is written to standard output in LDAP Data Interchange Format or <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5): </p>
<pre>
    version: 1
    # bjensen, example, net
    dn: uid=bjensen,dc=example,dc=net
    objectClass: person
    objectClass: dcObject
    uid: bjensen
    cn: Barbara Jensen
    sn: Jensen
    ...
</pre>
<p> If the <code>-t</code> option is used, the URI of a temporary file is used in place of the actual value. If the <code>-A</code> option is given, only the &quot;attributename&quot; part is written.</p>
<h2>EXAMPLE</h2>
<p> The following command: </p>
<pre>
    ldapsearch -LLL &quot;(sn=smith)&quot; cn sn telephoneNumber
</pre>
<p> will perform a subtree search (using the default search base and other parameters defined in <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5)) for entries with a surname (sn) of smith. The common name (cn), surname (sn) and telephoneNumber values will be retrieved and printed to standard output. The output might look something like this if two entries are found: </p>
<pre><code>
dn : uid = jts, dc = example, dc = com cn : John Smith cn : John T.Smith sn : Smith sn;
lang - en : Smith
                sn;
lang - de : Schmidt telephoneNumber : 1 555 123 - 4567 dn : uid = sss, dc = example, dc = com cn : Steve Smith cn : Steve S.Smith sn : Smith sn;
lang - en : Smith
                sn;
lang - de : Schmidt telephoneNumber : 1 555 765 - 4321
</code></pre>
<p> The command: </p>
<pre>
    ldapsearch -LLL -u -t &quot;(uid=xyz)&quot; jpegPhoto audio
</pre>
<p> will perform a subtree search using the default search base for entries with user id of &quot;xyz&quot;. The user friendly form of the entry&#8217;s DN will be output after the line that contains the DN itself, and the jpegPhoto and audio values will be retrieved and written to temporary files. The output might look like this if one entry with one value for each of the requested attributes is found: </p>
<pre>
    dn: uid=xyz,dc=example,dc=com
    ufn: xyz, example, com
    audio:&lt; file:///tmp/ldapsearch-audio-a19924
    jpegPhoto:&lt; file:///tmp/ldapsearch-jpegPhoto-a19924
</pre>
<p> This command: </p>
<pre>
    ldapsearch -LLL -s one -b &quot;c=US&quot; &quot;(o=University*)&quot; o description
</pre>
<p> will perform a one-level search at the c=US level for all entries whose organization name (o) begins with <code>University</code>. The organization name and description attribute values will be retrieved and printed to standard output, resulting in output similar to this: </p>
<pre>
    dn: o=University of Alaska Fairbanks,c=US
    o: University of Alaska Fairbanks
    description: Preparing Alaska for a brave new yesterday
    description: leaf node only
    dn: o=University of Colorado at Boulder,c=US
    o: University of Colorado at Boulder
    description: No personnel information
    description: Institution of education and research
    dn: o=University of Colorado at Denver,c=US
    o: University of Colorado at Denver
    o: UCD
    o: CU/Denver
    o: CU-Denver
    description: Institute for Higher Learning and Research
    dn: o=University of Florida,c=US
    o: University of Florida
    o: UFl
    description: Warper of young minds
    ...
</pre>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ldapadd/">ldapadd</a></code>(1), <code><a href="/docs/linux/man/1-ldapdelete/">ldapdelete</a></code>(1), <code><a href="/docs/linux/man/1-ldapmodify/">ldapmodify</a></code>(1), <code><a href="/docs/linux/man/1-ldapmodrdn/">ldapmodrdn</a></code>(1), <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5), <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5), <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_search_ext/">ldap_search_ext</a></code>(3), <code><a href="/docs/linux/man/3-ldap_sort/">ldap_sort</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
