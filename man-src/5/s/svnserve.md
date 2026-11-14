---
title: "svnserve(5)"
name: "svnserve"
section: "5"
letter: "s"
url: "/docs/linux/man/5-svnserve/"
description: "svnserve.conf – Repository configuration file for svnserve"
---

<p>svnserve.conf &#8211; Repository configuration file for svnserve</p>
<h2>Synopsis</h2>
<dl>
<dt><i>repository-path</i><code>/conf/svnserve.conf</code></p>
<dd></dl>
<h2>Description</h2>
<p><code>svnserve.conf</code> controls the behavior of the <code>svnserve</code> daemon on a per-repository basis. It is located in the <code>conf</code> subdirectory of the repository. </p>
<p> The overall structure of the file is the same as the structure of Subversion user configuration files. At the top level are sections, which are specified by words in square brackets; inside each section are variable definitions of the form &quot;variable = value&quot;. Lines beginning with &#8216;#&#8217; are ignored. <code>svnserve.conf</code> currently uses only one section named &quot;general&quot;, and supports the following variables: </p>
<dl>
<dt><code>anon-access</code> = <code>none</code>|<code>read</code>|<code>write</code></p>
<dd>Determines the access level for unauthenticated users. <code>write</code> access allows all repository operations. <code>read</code> access allows all operations except committing and changing revision properties. <code>none</code> access allows no access. The default level is <code>read</code>.</dl>
<dl>
<dt><code>auth-access</code> = <code>none</code>|<code>read</code>|<code>write</code></p>
<dd>Determines the access level for authenticated users, using the same access levels as above. The default level is <code>write</code>.</dl>
<dl>
<dt><code>password-db</code> = <i>filename</i></p>
<dd>Sets the location of the password database. <i>filename</i> may be relative to the repository conf directory. There is no default value. The password database has the same overall format as this file. It uses only one section &quot;users&quot;; each variable within the section is a username, and each value is a password.</dl>
<dl>
<dt><code>authz-db</code> = <i>path</i></p>
<dd>The authz-db option controls the location of the authorization rules for path-based access control. <i>path</i> may be relative to the repository conf directory. <i>path</i> may be a repository relative URL (^/) or absolute file:// URL to a text file in a Subversion repository. There is no default value. If you don&#8217;t specify an authz-db, no path-based access control is done.</dl>
<dl>
<dt><code>realm</code> = <i>realm-name</i></p>
<dd>Sets the authentication realm of the repository. If two repositories have the same password database, they should have the same realm, and vice versa; this association allows clients to use a single cached password for several repositories. The default realm value is the repository&#8217;s uuid.</dl>
<h2>Example</h2>
<p>The following example <code>svnserve.conf</code> allows read access for authenticated users, no access for anonymous users, points to a passwd database in the same directory, and defines a realm name. </p>
<pre> [general]
 anon-access = none
 auth-access = read
 password-db = passwd
 realm = My First Repository</pre>
<p>The file &quot;passwd&quot; would look like: </p>
<pre> [users]
 joeuser = joepassword
 jayrandom = randomjay</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-svnserve/">svnserve</a></code>(8) </p>
