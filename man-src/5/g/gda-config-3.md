---
title: "gda-config-3(5)"
name: "gda-config-3"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gda-config-3/"
description: "$(sysconfdir)/libgda/config – libgda global configuration file. $(HOME)/.libgda/config – libgda user configuration file."
---

<p>$(sysconfdir)/libgda/config &#8211; libgda global configuration file. $(HOME)/.libgda/config &#8211; libgda user configuration file.</p>
<h2>Description</h2>
<p>The config file of libgda is an XML file. The document starts with &lt;libgda-config&gt; tag, which contains sections that hold the configured database providers for libgda. </p>
<p> The values in the global configuration file are overriden by the ones in the user configuration file. </p>
<p> Each &lt;section&gt; has a &#8216;path&#8217; attribute whose value <i>must</i> be something like &quot;/apps/libgda/Datasources/XXXXXXXX&quot;, where XXXXXXXX is the name of the database backend (i.e., postgres, mysql,&#8230;) </p>
<p> Inside each &lt;section&gt; you can have for &lt;entry&gt; tags with &#8216;name&#8217;, &#8216;type&#8217; and &#8216;value&#8217; attributes. Valid values for &#8216;name&#8217; are: <i>Provider</i>, <i>Username</i>, <i>DSN</i> and <i>Description</i>. &#8216;type&#8217; value is always &quot;string&quot; and &#8216;value&#8217; contains the value for the given &#8216;name&#8217;.</p>
<h2>Example</h2>
<p>This is a sample file. You may modify it manually, add/remove sections,&#8230;</p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;libgda-config&gt;
 &lt;section path=&quot;/apps/libgda/Datasources/postgres&quot;&gt;
 &lt;entry name=&quot;Provider&quot; type=&quot;string&quot; value=&quot;PostgreSQL&quot;/&gt;
 &lt;entry name=&quot;Username&quot; type=&quot;string&quot; value=&quot;gonzalo&quot;/&gt;
 &lt;entry name=&quot;DSN&quot; type=&quot;string&quot;
 value=&quot;DATABASE=test;USER=gonzalo&quot;/&gt;
 &lt;entry name=&quot;Description&quot; type=&quot;string&quot;
 value=&quot;Mi favourite provider&quot;/&gt;
 &lt;/section&gt;
&lt;/libgda-config&gt;</pre>
</dl>
<p> You can also use <code>gda-config-tool-3.0</code> or <code>mergeant</code> (recommended) to modify this file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mergeant/">mergeant</a></code>(1), <code><a href="/docs/linux/man/1-gda-config-tool-3-0/">gda-config-tool-3.0</a></code>(1) </p>
<h2>Name</h2>
<p>$(sysconfdir)/libgda/config &#8211; libgda global configuration file. $(HOME)/.libgda/config &#8211; libgda user configuration file.</p>
<h2>Description</h2>
<p>The config file of libgda is an XML file. The document starts with &lt;libgda-config&gt; tag, which contains sections that hold the configured database providers for libgda. </p>
<p> The values in the global configuration file are overriden by the ones in the user configuration file. </p>
<p> Each &lt;section&gt; has a &#8216;path&#8217; attribute whose value <i>must</i> be something like &quot;/apps/libgda/Datasources/XXXXXXXX&quot;, where XXXXXXXX is the name of the database backend (i.e., postgres, mysql,&#8230;) </p>
<p> Inside each &lt;section&gt; you can have for &lt;entry&gt; tags with &#8216;name&#8217;, &#8216;type&#8217; and &#8216;value&#8217; attributes. Valid values for &#8216;name&#8217; are: <i>Provider</i>, <i>Username</i>, <i>DSN</i> and <i>Description</i>. &#8216;type&#8217; value is always &quot;string&quot; and &#8216;value&#8217; contains the value for the given &#8216;name&#8217;.</p>
<h2>Example</h2>
<p>This is a sample file. You may modify it manually, add/remove sections,&#8230;</p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot;?&gt;
&lt;libgda-config&gt;
 &lt;section path=&quot;/apps/libgda/Datasources/postgres&quot;&gt;
 &lt;entry name=&quot;Provider&quot; type=&quot;string&quot; value=&quot;PostgreSQL&quot;/&gt;
 &lt;entry name=&quot;Username&quot; type=&quot;string&quot; value=&quot;gonzalo&quot;/&gt;
 &lt;entry name=&quot;DSN&quot; type=&quot;string&quot;
 value=&quot;DATABASE=test;USER=gonzalo&quot;/&gt;
 &lt;entry name=&quot;Description&quot; type=&quot;string&quot;
 value=&quot;Mi favourite provider&quot;/&gt;
 &lt;/section&gt;
&lt;/libgda-config&gt;</pre>
</dl>
<p> You can also use <code>gda-config-tool-3.0</code> or <code>mergeant</code> (recommended) to modify this file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mergeant/">mergeant</a></code>(1), <code><a href="/docs/linux/man/1-gda-config-tool-3-0/">gda-config-tool-3.0</a></code>(1) </p>
