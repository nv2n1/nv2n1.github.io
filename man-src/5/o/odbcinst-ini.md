---
title: "odbcinst-ini(5)"
name: "odbcinst-ini"
section: "5"
letter: "o"
url: "/docs/linux/man/5-odbcinst-ini/"
description: "/etc/odbcinst.ini – An unixODBC drivers configuration"
---

<p>/etc/odbcinst.ini &#8211; An unixODBC drivers configuration</p>
<h2>Description</h2>
<p><code>/etc/odbcinst.ini</code> is a text configuration file for unixODBC drivers. It can be edited by hand, but the recommended way to update this file is to use the <code><a href="/docs/linux/man/1-odbcinst/">odbcinst</a></code>(1) utility. </p>
<h2>File Format</h2>
<p>The general .ini file format is: </p>
<dl>
<dd>
<pre><code>[</code><i>SectionName1</i><code>]</code>
<i>key1</i><code> = </code><i>value1</i>
<i>key2</i><code> = </code><i>value2</i>
<code>...</code>
<code>[</code><i>SectionName2</i><code>]</code>
<i>key1</i><code> = </code><i>value1</i>
<i>key2</i><code> = </code><i>value2</i>
<code>...</code></pre>
</dl>
<p> Each ODBC driver has its own section and can be referred to by the name of its section. Recognized configuration keys are: </p>
<dl>
<dt><code>Description</p>
<dd>A text string briefly describing the driver. </p>
<dt>Driver</p>
<dd>A filesystem path to the actual driver library. </p>
<dt>Setup</p>
<dd>A filesystem path to the driver setup library. </p>
<dt>FileUsage</p>
<dd><a href="/docs/linux/man/1-odbcinst/">odbcinst</a></code>(1) entry, if you edit the configuration file by hand, you have to supply it yourself. </p>
</dl>
<h3>Template Files</h3>
<p>The recommended way to manage the drivers is using the <code><a href="/docs/linux/man/1-odbcinst/">odbcinst</a></code>(1) utility. You can install the drivers by supplying it with template file, which has the same format as this file.</p>
<h2>Examples</h2>
<p>An example of the actual PostgreSQL driver:</p>
<dl>
<dd>
<pre>[PostgreSQL]
Description = PostgreSQL driver for GNU/Linux
Driver = /usr/lib/psqlodbcw.so
Setup = /usr/lib/libodbcpsqlS.so
FileUsage = 1</pre>
</dl>
<p> By specifying the driver like that, you can then reference it in the <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) as follows:</p>
<dl>
<dd>
<pre>Driver = PostgreSQL</pre>
</dl>
<p> The recommended way to add that driver is by creating template file containg:</p>
<dl>
<dd>
<pre>[PostgreSQL]
Description = PostgreSQL driver for GNU/Linux
Driver = /usr/lib/psqlodbcw.so
Setup = /usr/lib/libodbcpsqlS.so</pre>
</dl>
<p> and call the <code><a href="/docs/linux/man/1-odbcinst/">odbcinst</a></code>(1):</p>
<dl>
<dd><code># odbcinst -i -d -f </code><i>template.ini</i></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-odbcinst/">odbcinst</a></code>(1), <code><a href="/docs/linux/man/5-odbc-ini/">odbc.ini</a></code>(5) </p>
<h2>Authors</h2>
<p>The authors of unixODBC are Peter Harvey &lt;<i>pharvey [at] codebydesign.com</i>&gt; and Nick Gorham &lt;<i>nick [at] easysoft.com</i>&gt;. For the full list of contributors see the AUTHORS file.</p>
<h2>Copyright</h2>
<p>unixODBC is licensed under the GNU Lesser General Public License. For details about the license, see the COPYING file.</p>
