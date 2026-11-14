---
title: "fbsvcmgr(1)"
name: "fbsvcmgr"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fbsvcmgr/"
description: "fbsvcmgr – access services API of Firebird"
---

<h2 class="name">NAME</h2>
<p> fbsvcmgr &#8211; access services API of Firebird </p>
<h2>SYNOPSYS</h2>
<dl>
<dt>fbsvcmgr service_mgr <i>parameter&#8230;</i></p>
<dd>
<dt>fbsvcmgr host:service_mgr <i>parameter&#8230;</i></p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> Firebird (like interbase 6 and before) never had a way to access services <font SIZE="-1">API</font> from command line. With the exception of <code>-service</code> switch of <code><a href="/docs/linux/man/1-gbak/">gbak</a></code>(1) and total use of services <font SIZE="-1">API</font> in <code><a href="/docs/linux/man/1-gsec/">gsec</a></code>(1) since version 2.0, to use services one had to use third party <font SIZE="-1">GUI</font> or write himself a program using C or other programming language. Use of <font SIZE="-1">GUI</font> is almost always not a problem, when you work with local machine or machine in your <font SIZE="-1">LAN.</font> But in case, when you connect to remote unix server using any text-only connection, use of services is almost impossible. And this is really a problem sometimes. </p>
<p> The <code>fbsvcmgr</code> utility solves this problem. With it you may use any service, implemented by firebird. To use this utility you should be familiar with firebird services <font SIZE="-1">API</font> &#8211; <code>fbsvcmgr</code> does <font SIZE="-1">NOT</font> emulate traditional utilities&#8217; switches, it is just frontend to the services <font SIZE="-1">API.</font> </p>
<p> The first required parameter of command line is services manager you want to connect to. For local connection use simply <i>service_mgr</i>, to attach to remote machine something like <i>hostname:service_mgr</i> is required. When required, additional service parameter blocks (<font SIZE="-1">SPB</font>), including any values, follow. Any of them may (or may not) be prefixed with single <code>&#8211;</code> (minus) sign for clarity. For long command lines, typical for fbsvcmgr, use of &#8216;-&#8216; makes command line better human-readable and has no other effects. </p>
<p> Compare: </p>
<pre>
 fbsvcmgr service_mgr user sysdba password \
 masterke action_db_stats \
 dbname employee sts_hdr_pages
</pre>
<p> and </p>
<pre>
 fbsvcmgr service_mgr -user sysdba -password \
 masterke -action_db_stats -dbname \
 employee -sts_hdr_pages
</pre>
<p> Syntax of service parameter blocks, as understood by <code>fbsvcmgr</code>, almost exactly matches the one you may see in <i>ibase.h</i> include file or Borland InterBase 6.0 <font SIZE="-1">API</font> documentation. To save typing and make command line a bit shorter, slightly abbreviated form is used. All <font SIZE="-1">SPB</font> parameters have one of two forms: <i>isc_spb_VALUE</i> or <i>isc_VALUE1_svc_VALUE2</i>. Accordingly in the first case you should type simply <i></i><font SIZE="-1"><i>VALUE</i></font><i></i>, and for the second &#8211; <i></i><font SIZE="-1"><i>VALUE1_VALUE2</i></font><i></i>. For example: </p>
<pre><code>
present in ibase.h becomes-- -- -- -- -- -- -- -- -- -- -- -- - -- -- -- -- -- -- -- -- -isc_spb_dbname dbname
    isc_action_svc_backup action_backup
        isc_spb_sec_username sec_username
            isc_info_svc_get_env_lock info_get_env_lock
</code></pre>
<p> and so on. As an exception, <i>isc_spb_user_name</i> may be specified as either <i>user_name</i> or simply <i>user</i>. </p>
<p> The full description of all <font SIZE="-1">SPB</font> parameters can be found int the InterBase 6.0 beta documentation. It is some 40 pages long, so it is not duplicated here. There are a couple of differences, though, which are described below. Another reference is the <i>ibase.h</i> file distributed by the Firebird project.</p>
<dl>
<dt>multiple actions in single request</p>
<dd> Using fbsvcmgr you may perform single action (and get results of it&#8217;s execution when available) or get multiple information items from services manager. For example: </p>
<pre>
    fbsvcmgr service_mgr -user sysdba -password masterke -action_display_user
</pre>
<p> will list all users of local firebird server: </p>
<pre>
    SYSDBA            Sql Server Administrator      0    0
    QA_USER1                                        0    0
    QA_USER2                                        0    0
    QA_USER3                                        0    0
    QA_USER4                                        0    0
    QA_USER5                                        0    0
    GUEST                                           0    0
    SHUT1                                           0    0
    SHUT2                                           0    0
    QATEST                                          0    0
</pre>
<p> And: </p>
<pre>
    fbsvcmgr service_mgr -user sysdba -password masterke \
    -info_server_version -info_implementation
</pre>
<p> will report both server version and it&#8217;s implementation: </p>
<pre>
    Server version: LI-T2.1.0.15740 Firebird 2.1 Alpha 1
    Server implementation: Firebird/linux AMD64
</pre>
<p> But attempt to mix all of this in single command line: </p>
<pre>
    fbsvcmgr service_mgr -user sysdba -password masterke \
    -action_display_user -info_server_version -info_implementation
</pre>
<p> raises an error: </p>
<pre>
    Unknown switch &quot;-info_server_version&quot;
</pre>
<dt>Buggy documentation</p>
<dd> Some parameters have buggy form in Borland beta documentation. When in trouble, consult <i>ibase.h</i> first for correct form. </p>
<p> <i>isc_spb_rpr_list_limbo_trans</i> was forgotten in Borland beta documentation, but present in fbsvcmgr.</p>
<dt>No licensing stuff</p>
<dd> Everything concerning licensing was removed from interbase 6.0 and therefore not supported here.</p>
<dt>No access to config file</p>
<dd> Config file view/modification is not supported in firebird since 1.5 and therefore is not implemented here.</p>
<dt>Items added in firebird 2.1</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><i>trusted_auth</i></p>
<dd> (Windows-only) Forces use of windows trusted authentication.</p>
<dt><i>dbname</i></p>
<dd> (Only for actions related to security). It is equivalent to the <i>-database</i> switch of the <code><a href="/docs/linux/man/1-gsec/">gsec</a></code>(1) utility. Note that in <code><a href="/docs/linux/man/1-gsec/">gsec</a></code>(1) this switch is mostly used to specify remote server you want to administer. In <code>fbsvcmgr</code> the name of the server is already given in services manager name (first parameter), therefore this parameter in most cases is not needed.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Items added in firebird 2.5</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>bkp_no_triggers</p>
<dd> specify it to avoid executing database-wide triggers</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>AUTHOR</h2>
<p> Alex Peshkov, &#8220;peshkoff at mail.ru&#8221; </p>
<p> This manual page was written by Damyan Ivanov dmn [at] debian.org for the Debian project. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
<h2>Index</h2>
