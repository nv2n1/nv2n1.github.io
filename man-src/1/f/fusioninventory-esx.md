---
title: "fusioninventory-esx(1)"
name: "fusioninventory-esx"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusioninventory-esx/"
---

<h2 class="name">NAME</h2>
 

 fusioninventory-esx - vCenter/ESX/ESXi remote inventory from command line 

<h2>SYNOPSIS</h2>

 fusioninventory-esx --host &lt;host&gt; --user &lt;user&gt; --password &lt;password&gt; --directory &lt;directory&gt; 

 <pre><code>
  Options:
    --help                 this menu
    --host hostname        ESX server hostname
    --user username        user name
    --password xxxx        user password
    --directory directory  output directory
    --tag tag              tag for the inventoried machine
</code></pre>

<h2>EXAMPLES</h2>

 <pre><code>
% fusioninventory - esx-- host myesx-- user foo-- password bar-- directory / tmp
</code></pre> 

 You can import the .ocs file in your inventory server with the fusioninventory-injector tool. 
&nbsp;<wbr><tt>%fusioninventory</tt>-injector -v --file&nbsp;<wbr>/tmp/*.ocs -u&nbsp;<wbr><a rel="nofollow" HREF="https://myserver/ocsinventory">https://myserver/ocsinventory</a>

<h2>DESCRIPTION</h2>

 <i>fusioninventory-esx</i> creates inventory of remote ESX/ESXi and vCenter VMware. It uses the <font SIZE="-1">SOAP</font> interface of the remote server. 

 Supported systems:
<dl>
<dt><i></i><font SIZE="-1"><i>ESX</i></font><i> and ESXi 3.5</i>
<dd>
<dt><i></i><font SIZE="-1"><i>ESX</i></font><i> and ESXi 4.1</i>
<dd>
<dt><i>ESXi 5.0</i>
<dd>
<dt><i>vCenter 4.1</i>
<dd>
<dt><i>vCenter 5.0</i>
<dd></dl>
 

 Active Directory users, please note the <font SIZE="-1">AD</font> authentication doesn't work. You must create a account on the VMware server.

<h2>LIMITATION</h2>

 So far, <font SIZE="-1">ESX</font> serial number are not collected.

<h2>SECURITY</h2>

 The <font SIZE="-1">SSL</font> hostname check of the server is disabled. 

<h2>Index</h2>


