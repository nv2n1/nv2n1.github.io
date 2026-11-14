---
title: "unixodbc(7)"
name: "unixodbc"
section: "7"
letter: "u"
url: "/docs/linux/man/7-unixodbc/"
description: "unixODBC – An ODBC implementation for Unix"
---

<p>unixODBC &#8211; An ODBC implementation for Unix</p>
<h2>Description</h2>
<p>ODBC is an open specification for providing application developers with a predictable API with which to access Data Sources. Data Sources include SQL Servers and any Data Source with an ODBC Driver. The unixODBC Project goals are to develop and promote unixODBC to be the definitive standard for ODBC on non MS Windows platforms. </p>
<h2>Environment Variables</h2>
<dl>
<dt><code>ODBCSYSINI</p>
<dd>Overloads path to unixODBC configuration files. By default equals to &#8216;/etc&#8217;. </p>
<dt>ODBCINSTINI</p>
<dd>Overloads the name of the drivers configuration file. It is relative to ODBCSYSINI</code> and by default set to &#8216;odbcinst.ini&#8217;. </p>
<dt><code>ODBCINSTUI</p>
<dd>Overloads the library name for UI. The final name that is searched for is evaluated as &quot;lib$ODBCINSTUI&quot;. By default it is set to &#8216;odbcinstQ4&#8217;, so the resulting library name is &#8216;libodbcinstQ4&#8217;. </p>
<dt>ODBCSEARCH</p>
<dd>Overloads the configuration mode and determines where to look for configuration files. Must be set to one of ODBC_SYSTEM_DSN, ODBC_USER_DSN or ODBC_BOTH_DSN (the last one is the default value). </p>
<dt>ODBCINI</p>
<dd>Overloads the path to user configuration file. By default it is set to &quot;~/.odbc.ini&quot;. </p>
</dl>
<p> </code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-isql/">isql</a></code>(1), <code><a href="/docs/linux/man/1-odbcinst/">odbcinst</a></code>(1), <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5), <code><a href="/docs/linux/man/5-odbcinst-ini/">odbcinst.ini</a></code>(5) </p>
<h2>Authors</h2>
<p>The authors of unixODBC are Peter Harvey &lt;<i>pharvey [at] codebydesign.com</i>&gt; and Nick Gorham &lt;<i>nick [at] unixodbc.org</i>&gt;. For the full list of contributors see the AUTHORS file.</p>
<h2>Copyright</h2>
<p>unixODBC is licensed under the GNU Lesser General Public License. For details about the license, see the COPYING file.</p>
