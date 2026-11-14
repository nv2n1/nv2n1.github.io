---
title: "dbsessmgr(1)"
name: "dbsessmgr"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbsessmgr/"
description: "dbsessmgr – session state database manager"
---

<h2>NAME</h2>
<p> dbsessmgr &#8211; session state database manager</p>
<h2>SYNOPSIS</h2>
<p> <code>mono dbsessmgr.exe</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> dbsessmgr allows you to manage the ASP.NET session state database.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>&#8211;clean</i></p>
<dd> Remove all expired sessions.</p>
<dt><i>&#8211;remove</i></p>
<dd> Delete all sessions.</p>
<dt><i>&#8211;show</i></p>
<dd> Display session data.</dl>
<h2>CONFIGURATION</h2>
<p> You can choose the assembly and type used to connect to your database backend and also set the connection string and the SQL parameter prefix through the configuration file, named dbsessmgr.exe.config. The configuration shipped by default is: </p>
<pre>
    &lt;appSettings&gt;
        &lt;add key=&quot;DBProviderAssembly&quot;
             value=&quot;Npgsql&quot;/&gt;
        &lt;add key=&quot;DBConnectionType&quot;
             value=&quot;Npgsql.NpgsqlConnection&quot;/&gt;
        &lt;add key=&quot;DBConnectionString&quot;
             value=&quot;SERVER=127.0.0.1;USER ID=monostate;PASSWORD=monostate;dbname=monostate&quot;/&gt;
        &lt;add key=&quot;DBParamPrefix&quot;
             value=&quot;:&quot; /&gt;
    &lt;/appSettings&gt;
</pre>
<h2>AUTHORS</h2>
<p> dbsessmgr was written by Jackson Harper (jackson [at] ximian.com).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a></code>(1),<code><a href="/docs/linux/man/1-xsp/">xsp</a></code>(1),<code><a href="/docs/linux/man/1-asp-state/">asp-state</a></code>(1),<code><a href="/docs/linux/man/8-mod_mono/">mod_mono</a></code>(8)</p>
<h2>MORE INFORMATION</h2>
<p> The Mono project (<a rel="nofollow" href="http://www.go-mono.com)">http://www.go-mono.com)</a> is a collaborative effort led by Novell (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a> to implement an open source version of the .NET Framework. </p>
<h2>Index</h2>
