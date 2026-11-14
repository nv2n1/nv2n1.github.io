---
title: "edg-mkgridmap-conf(5)"
name: "edg-mkgridmap-conf"
section: "5"
letter: "e"
url: "/docs/linux/man/5-edg-mkgridmap-conf/"
description: "edg-mkgridmap.conf – edg-mkgridmap configuration file"
---

<p>edg-mkgridmap.conf &#8211; edg-mkgridmap configuration file</p>
<h2>Description</h2>
<p><i>edg-mkgridmap.conf</i> file contains configuration informations for <code>edg-mkgridmap</code>. </p>
<p> The default location is <i>/etc/edg-mkgridmap.conf</i>. </p>
<p> The <i>edg-mkgridmap.conf</i> file is a free-form <font SIZE="-1">ASCII</font> text file. It is parsed by the descent parser built into <code>edg-mkgridmap</code>. The file may contain extra tabs and white spaces for formatting purposes. Keywords in the file are case-insensitive. Comments may be placed anywhere within the file (except within quotes). Comments begin with the # character and end at the end of the line. </p>
<p> The file essentially consists of a list of directives composed by a keyword and one or more arguments. Optional arguments are put in square brackets.</p>
<dl>
<dt>* <code>group</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i> <i>[lcluser]</i></p>
<dd>
<dt>* <code>default_lcluser</code> <i>default_lcluser</i></p>
<dd>
<dt>* <code>auth</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i></p>
<dd>
<dt>* <code>allow</code>|<code>deny</code> <i>pattern_to_match</i></p>
<dd>
<dt>* <code>gmf_local</code> <i>grid-mapfile-local</i></p>
<dd></dl>
<h2>Example</h2>
<pre> #### GROUP: group URI [lcluser]
 group <a href="ldaps://grid-vo.infn.it/ou=testbed1,o=infn,c=it">ldaps://grid-vo.infn.it/ou=testbed1,o=infn,c=it</a> .infngrid
 group <a href="ldaps://grid-vo.infn.it/ou=testbed2,o=infn,c=it">ldaps://grid-vo.infn.it/ou=testbed2,o=infn,c=it</a>
 group <a href="ldaps://grid-vo.infn.it/ou=testbed3,o=infn,c=it">ldaps://grid-vo.infn.it/ou=testbed3,o=infn,c=it</a> AUTO
 group <a rel="nofollow" href="https://grid-vo.infn.it/infngrid/testbed1">https://grid-vo.infn.it/infngrid/testbed1</a> .infngrid
 group <a rel="nofollow" href="https://grid-vo.infn.it/infngrid/testbed2">https://grid-vo.infn.it/infngrid/testbed2</a>
 group <a rel="nofollow" href="https://grid-vo.infn.it/infngrid/testbed3">https://grid-vo.infn.it/infngrid/testbed3</a> AUTO
 group <a href="vomss://voms.hellasgrid.gr:8443/voms/dteam?/dteam/Role=lcgadmin">vomss://voms.hellasgrid.gr:8443/voms/dteam?/dteam/Role=lcgadmin</a> dteamsgm
 group <a href="vomss://voms.hellasgrid.gr:8443/voms/dteam?/dteam">vomss://voms.hellasgrid.gr:8443/voms/dteam?/dteam</a> .dteam</pre>
<pre> #### DEFAULT_LCLUSER: default_lcluser lcluser
 default_lcluser .infngrid</pre>
<pre> #### AUTH: auth URI
 auth <a href="ldaps://grid-auth.infn.it/ou=People,o=infn,c=it">ldaps://grid-auth.infn.it/ou=People,o=infn,c=it</a></pre>
<pre> #### ALLOW and DENY: deny|allow pattern_to_match
 deny *L=Parma*
 allow *INFN*</pre>
<pre> #### GMF_LOCAL: gmf_local grid-mapfile-local
 gmf_local /etc/grid-mapfile-local1
 gmf_local /etc/grid-mapfile-local2
 gmf_local /etc/grid-mapfile-local3</pre>
<h2>Reference: Group</h2>
<p>The <i>group</i> <code>directive</code> </p>
<p> <code>group</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i> <i>[lcluser]</i> </p>
<p> A <code>group</code> directive defines a group of people which are members of a <font SIZE="-1">VO</font>. <i>lcluser</i>, if specified, is the local user name associated to each member of the group. If <i>lcluser</i> is not specified, the default local user is implicitly used. If someone belongs to more than one group, the first match is used. </p>
<p> The <i></i><font SIZE="-1"><i>URI</i></font><i></i> may be of these types: </p>
<p> ldap[s]://&lt;host&gt;[:&lt;port&gt;]/&lt;group&gt;[??&lt;scope&gt;?&lt;filter&gt;] </p>
<p> http[s]://&lt;host&gt;[:&lt;port&gt;]/&lt;group&gt; </p>
<p> voms[s]://&lt;host&gt;[:&lt;port&gt;]/edg-voms-admin/&lt;vo&gt;[?&lt;group&gt;[/Role=&lt;role&gt;]] </p>
<p> For ldap <font SIZE="-1">URI</font> the default scope is base and the default filter is (objectClass=*). </p>
<p> For voms/vomss <font SIZE="-1">URI</font> the default port is the same of http/https <font SIZE="-1">URI</font>. </p>
<p> Specify <i></i><font SIZE="-1"><i>AUTO</i></font><i></i> as <i>lcluser</i> or <i>default_lcluser</i> for automatic generation of local usernames. In this case the executable <i>local-subject2user</i> is used. <i>local-subject2user</i> is called with the user certificate subject as argument and writes to the standard output the local username associated with the user certificate subject. This allows local sites to customize the output of <code>edg-mkgridmap</code>. </p>
<p> Specify <i>.</i> or <i>.[</i><font SIZE="-1"><i>PREFIX</i></font><i>]</i> (eg <i>.cms</i>) as <i>lcluser</i> or <i>default_lcluser</i> to enable dynamic allocation of local usernames (Andrew McNab&#8217;s gridmapdir patch).</p>
<h2>Reference: Default_Lcluser</h2>
<p>The <i>default_lcluser</i> <code>directive</code> </p>
<p> <code>default_lcluser</code> <i>default_lcluser</i> </p>
<p> The <code>default_lcluser</code> directive defines the default local user.</p>
<h2>Reference: Auth</h2>
<p>The <i>auth</i> <code>directive</code> </p>
<p> <code>auth</code> <i></i><font SIZE="-1"><i>URI</i></font><i></i> </p>
<p> The <code>auth</code> directive specifies a group of people which are authorized to access to the local resources. If the certificate subject of a member of a ldap/ldaps group is not present in this authorized group, it will not be inserted in the grid-mapfile. If <code>auth</code> is omitted, this feature is disabled. </p>
<p> The <i></i><font SIZE="-1"><i>URI</i></font><i></i> may be of these types: </p>
<p> ldap[s]://&lt;host&gt;[:&lt;port&gt;]/&lt;group&gt;[??&lt;scope&gt;?&lt;filter&gt;] </p>
<p> The default scope is one and the default filter is (description=subject=*).</p>
<h2>REFERENCE: ALLOW and DENY</h2>
<p>The <i>allow</i>|<i>deny</i> <code>directive</code> </p>
<p> <code>allow</code>|<code>deny</code> <i>pattern_to_match</i> </p>
<p> <code>allow</code> and <code>deny</code> directives define the access control list. The pattern to match may contain wildcards; the test is done on the user certificate subject. Parsing stops at the first match. If there is at least an allow, there is an implicit <code>deny</code> <i>*</i> at the end, otherwise there is an implicit <code>allow</code> <i>*</i>. Parsing is not case sensitive.</p>
<h2>Reference: Gmf_Local</h2>
<p>The <i>gmf_local</i> <code>directive</code> </p>
<p> <code>gmf_local</code> <i>grid-mapfile-local</i> </p>
<p> The <code>gmf_local</code> directive specifies a local grid-mapfile useful to add static entries in the grid-mapfile.</p>
<h2>Files</h2>
<p><i>/etc/edg-mkgridmap.conf</i></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-edg-mkgridmap/">edg-mkgridmap</a></i>(8)</p>
<h2>Authors</h2>
<p><font SIZE="-1">EU</font> DataGrid Authorization Working Group, <font SIZE="-1">EGEE</font> Middleware Security Group, Maarten Litmaath (<font SIZE="-1">CERN/WLCG</font>)</p>
