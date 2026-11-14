---
title: "rlm_detail(5)"
name: "rlm_detail"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_detail/"
description: "rlm_detail – FreeRADIUS Module"
---

<p>rlm_detail &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_detail</i> module writes radius packets to &#8216;detail&#8217; files. It is primarily used for storing accounting information, but can be used in other sections to write packet details as well. </p>
<p> The file format is similar to that of the old Livingston servers, and many &#8216;detail&#8217; file parsers should work with FreeRADIUS. </p>
<p> The main configuration items to be aware of are:</p>
<dl>
<dt>file</p>
<dd>The file name in which to store the radius packet records. NOTE: this variable is run through dynamic string expansion, and can include FreeRADIUS variables to create a dynamic filename.</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>%{radacctdir}/%{Client-IP-Address}/detail-%Y%m </p>
<p>&nbsp;<wbr>&nbsp;<wbr>This will create one file per month, for each client.&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>This accomplishes&nbsp;<wbr>&#8216;file rotation&#8217;&nbsp;<wbr>automatically from&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>within the server. </p>
<dl>
<dt>perm</p>
<dd>The file permissions of the file. If omitted, the default is 0600.</p>
<dt>dirperm</p>
<dd>The directory permissions of the directory where the detail files are created. The default is 0755.</p>
<dt>locking</p>
<dd>This option is set to &#8216;yes&#8217; or &#8216;no&#8217;. By default it is &#8216;no&#8217;. Set this to yes to enable file locking, which is used with the &#8216;radrelay&#8217; program.</dl>
<h2>Configuration</h2>
<dl>
<dd>
<pre>modules {
 ...
<br>
 detail {
<br>
 filename = %A/%{Client-IP-Address}/detail-%Y%m
<br>
 permissions = 0600
<br>
 dir_permissions = 0755
<br>
 locking = no
<br>
 }
<br>
 ... 
<br>
}
 ...
<br>
accounting {
 ...
<br>
 detail
 ...
<br>
}</pre>
</dl>
<h2>Sections</h2>
<p><code>authorization,</code> <code>accounting,</code> <code>pre_proxy,</code> <code>post_proxy,</code> <code>post_authentication</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Authors</h2>
<p>Chris Parker, cparker [at] segv.org</p>
