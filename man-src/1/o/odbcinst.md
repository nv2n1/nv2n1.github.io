---
title: "odbcinst(1)"
name: "odbcinst"
section: "1"
letter: "o"
url: "/docs/linux/man/1-odbcinst/"
description: "odbcinst – An unixODBC tool for manipulating configuration files"
---

<h2 class="name">NAME</h2>
<p> odbcinst &#8211; An unixODBC tool for manipulating configuration files</p>
<h2>SYNOPSIS</h2>
<p> <code>odbcinst</code> <i>ACTION OBJECT OPTIONS</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>odbcinst</code> is a command line tool which has been created for allowing people who are developing the install scripts/RPMs for Drivers to be able to easily create/remove entries in odbc.ini and odbcinst.ini. This command line tool is a complement to the shared library of the same name (libodbcinst.so). This tool is a part of the odbcinst component of unixODBC. </p>
<h2>OPTIONS</h2>
<h3>ACTIONS</h3>
<dl>
<dt>-i</dt>
<dd> Install (add section to config file) new <i>OBJECT</i>. </dd>
<dt>-u</dt>
<dd> Uninstall (remove section from config file) existing <i>OBJECT</i>. </dd>
<dt>-q</dt>
<dd> Query the config files and print the options for specified <i>OBJECT</i>. </dd>
<dt>-j</dt>
<dd> Prints current configuration of unixODBC, listing (among others) the paths to the configuration files. </dd>
<dt>-c</dt>
<dd> Calls SQLCreateDataSource </dd>
<dt>-m</dt>
<dd> Calls SQLManageDataSources </dd>
<dt>&#8211;version</dt>
<dd> Prints program version and exits. </dd>
</dl>
<h3>OBJECTS</h3>
<dl>
<dt>-d</dt>
<dd> The <i>ACTION</i> affect drivers (and thus the odbcinst.ini configuration file). </dd>
<dt>-s</dt>
<dd> The <i>ACTION</i> affect data sources (and thus the user or system odbc.ini configuration file). </dd>
</dl>
<h3>OPTIONS</h3>
<dl>
<dt>-f <i>FILE</i></dt>
<dd> The <i>FILE</i> is template file, describing the configuration of installed <i>OBJECT</i> (only valid for the -i <i>ACTION</i>). </dd>
<dt>-r</dt>
<dd> Same as the -f <i>OPTION</i>, only take the standard input as the template file. </dd>
<dt>-n <i>NAME</i></dt>
<dd> Specifies the <i>NAME</i> of the <i>OBJECT</i>. </dd>
<dt>-v</dt>
<dd> Turn off verbose mode. This turns off all information, warning and error messages. </dd>
<dt>-l</dt>
<dd> The specified data source is system-wide. Has any effect only with the -s <i>OBJECT</i>. </dd>
<dt>-h</dt>
<dd> The specified data source is user-specific. Has any effect only with the -s <i>OBJECT</i>. </dd>
</dl>
<h2>RETURN VALUES</h2>
<p> This command returns zero on success and non-zero value on failure. </p>
<h2>FILES</h2>
<p> <i>/etc/odbinst.ini</i></p>
<dl>
<dt>
</dt><dd> Configuration file containing all the database drivers specifications. See <code><a href="/docs/linux/man/5-odbcinst-ini/">odbcinst.ini</a></code>(5) for more details.</dd></dl>
<p> <i>/etc/odbc.ini</i></p>
<dl>
<dt>
</dt><dd> System-wide data sources specifications. See <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) for more details.</dd></dl>
<p> <i>$HOME/.odbc.ini</i></p>
<dl>
<dt>
</dt><dd> User-specific data sources specifications. See <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) for more details.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-odbcinst-ini/">odbcinst.ini</a></code>(5), <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) </p>
<h2>AUTHORS</h2>
<p> The authors of unixODBC are Peter Harvey &lt;<i>pharvey [at] codebydesign.com</i>&gt; and Nick Gorham &lt;<i>nick [at] easysoft.com</i>&gt;. For the full list of contributors see the AUTHORS file. </p>
<h2>COPYRIGHT</h2>
<p> unixODBC is licensed under the GNU Lesser General Public License. For details about the license, see the COPYING file. </p>
<h2>Index</h2>
