---
title: "pkla-check-authorization(8)"
name: "pkla-check-authorization"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pkla-check-authorization/"
description: "pkla-check-authorization – Evaluate pklocalauthority authorization configuration"
---

<p>pkla-check-authorization &#8211; Evaluate pklocalauthority authorization configuration</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pkla-check-authorization</code> [<code>&#8211;help</code>]</p>
<dt> <code>pkla-check-authorization</code> [<code>&#8211;paths</code>&nbsp;<wbr><i>paths</i>] {<i>user-name</i>} {<i>is-local</i>} {<i>is-active</i>} {<i>action</i>}</dl>
<h2>Description</h2>
<p><code>pkla-check-authorization</code></p>
<dd>interprets non-JavaScript configuration files described below to determine the response of <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) to authorization queries. </p>
<p> <i>Note:</i> Authorization decision evaluation is driven by JavaScript rules as described in <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8). <code>pkla-check-authorization</code> is called by a JavaScript rule file named 49-polkit-pkla-compat.rules; other JavaScript rules with a higher priority may exist, so the <code>pkla-check-authorization</code> configuration may not necessarily govern the final <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) authorization decision. </p>
<p> The ordering of the JavaScript rule files and the ordering of <code>pkla-check-authorization</code> configuration files is not integrated and uses different rules; the <code>pkla-check-authorization</code> configuration evaluation is happens at a single point within the JavaScript rule evaluation order. </p>
<p> <code>pkla-check-authorization</code> is an internal helper program of pkla-polkit-compat. You shouldn&#8217;t need to run it directly, except for debugging purposes. </p>
<p> The arguments to <code>pkla-check-authorization</code> are, in order: </p>
<p> <i>user-name</i></p>
<dl>
<dd>Name of the user account asking for authorization</dl>
<p> <i>is-local</i></p>
<dl>
<dd>Whether the attempted action is performed from a local login session, true or false.</dl>
<p> <i>is-active</i></p>
<dl>
<dd>Whether the attempted action is performed from a currently active session (e.g. currently active virtual console), true or false.</dl>
<p> <i>action</i></p>
<dl>
<dd>A string identifying the <code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) action.</dl>
<p> If the configuration specifies an authorization decision, <code>pkla-check-authorization</code> outputs the decision and a terminating newline. If no decision is configured, the output is empty.</p>
<h2>Options</h2>
<p><code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Write a summary of the available options to standard output and exit successfully.</dl>
<p> <code>-p</code>, <code>&#8211;paths</code>=<i>paths</i></p>
<dl>
<dd>Search for configuration files in semicolon-separated <i>paths</i> instead of the default /var/lib/polkit-1/localauthority;/etc/polkit-1/localauthority.</dl>
<h2>Exit Status</h2>
<p><code>pkla-check-authorization</code> exits with 0 on success (even if there is no decision configured), and a non-zero status on error.</p>
<h2>Directory Structure</h2>
<p>Files with .pkla extension are read from all directories located inside the /etc/polkit-1/localauthority and /var/lib/polkit-1/localauthority directories (or as specified using the <code>&#8211;paths</code> option). By default, the following sub-directories are installed. </p>
<dl>
<dd>
<pre>/etc/polkit-1/
`-- localauthority
 |-- 10-vendor.d
 |-- 20-org.d
 |-- 30-site.d
 |-- 50-local.d
 `-- 90-mandatory.d</pre>
</dl>
<p> and </p>
<dl>
<dd>
<pre>/var/lib/polkit-1/
`-- localauthority
 |-- 10-vendor.d
 |-- 20-org.d
 |-- 30-site.d
 |-- 50-local.d
 `-- 90-mandatory.d</pre>
</dl>
<p> The /etc/polkit-1/localauthority hierarchy is intended for local configuration and the /var/lib/polkit-1/localauthority is intended for 3rd party packages. </p>
<p> Each .pkla file contains one or more authorization entries. If the underlying filesystem supports file monitoring, the Local Authority will reload information whenever .pkla files are added, removed or changed. </p>
<p> Each directory is intended for a specific audience </p>
<p> <i>10-vendor.d</i></p>
<dl>
<dd>Intended for use by the OS vendor.</dl>
<p> <i>20-org.d</i></p>
<dl>
<dd>Intended for the organization deploying the OS.</dl>
<p> <i>30-site.d</i></p>
<dl>
<dd>Intended for the site deploying the system.</dl>
<p> <i>50-local.d</i></p>
<dl>
<dd>Intended for local usage.</dl>
<p> <i>90-mandatory.d</i></p>
<dl>
<dd>Intended for the organization deploying the OS.</dl>
<p> and new directories can be added/removed as needed. </p>
<p> As to regards to the content, each .pkla file is a standard <i>key file</i> and contains key/value pairs in one or more groups with each group representing an authorization entry. A .pkla file MUST be named by using a scheme to ensure that the name is unique, e.g. reverse DNS notation or similar. For example, if the organization is &#8220;Acme Corp&#8221; needs to modify policy for the product &#8220;Frobnicator&#8221;, a name like com.acme.frobnicator.pkla would be suitable.</p>
<h2>Authorization Entry</h2>
<p>Each group in a .pkla file must have a name that is unique within the file it belongs to. The following keys are recognized: </p>
<p> <i>Identity</i></p>
<dl>
<dd>A semi-colon separated list of entries to match identities. Each entry should start with unix-user: or unix-group: to specify whether to match on a UNIX user name or a UNIX group name, and continue with a glob matching the group or user name. Netgroups are supported with the unix-netgroup: prefix, but cannot support glob syntax. Finally, an entry &quot;default&quot; (with no prefix) can be used to specify the default match.</dl>
<p> <i>Action</i></p>
<dl>
<dd>A semi-colon separated list of globs to match action identifiers.</dl>
<p> <i>ResultActive</i></p>
<dl>
<dd>The result to return for subjects in an active local session that matches one or more of the given identities. Allowed values are similar to what can be used in the <i>defaults</i> section of .policy files used to define actions, e.g. yes, no, auth_self, auth_self_keep, auth_admin and auth_admin_keep.</dl>
<p> <i>ResultInactive</i></p>
<dl>
<dd>Like <i>ResultActive</i> but instead applies to subjects in inactive local sessions.</dl>
<p> <i>ResultAny</i></p>
<dl>
<dd>Like <i>ResultActive</i> but instead applies to any subject.</dl>
<p> All keys specified above are required except that only at least one of <i>ResultAny</i>, <i>ResultInactive</i> and <i>ResultActive</i> must be present.</p>
<h2>Evaluation Order</h2>
<p>The authorization entries discussed above are consulted using the following algorithm. </p>
<p> The authorization entries from all .pkla files are ordered using the following rules. First all the basename of all sub-directories (e.g. <i>30-site.d</i>) from both the /etc/polkit-1/localauthority and /var/lib/polkit-1/localauthority directories are enumerated and sorted (using the C locale). If a name exists in both /etc and /var, the one in /etc takes precedence. Then all .pkla files are read in order from this list of sub-directories. For each .pkla file, authorizations from each file are appended in order resulting in an ordered list of authorization entries. </p>
<p> For example, given the following files </p>
<dl>
<dd>
<pre>/var/lib/polkit-1
└── localauthority
 ├── 10-vendor.d
 │ └── 10-desktop-policy.pkla
 ├── 20-org.d
 ├── 30-site.d
 ├── 50-local.d
 ├── 55-org.my.company.d
 │ └── 10-org.my.company.product.pkla
 └── 90-mandatory.d
/etc/polkit-1
└── localauthority
 ├── 10-vendor.d
 │ └── 01-some-changes-from-a-subvendor.pkla
 ├── 20-org.d
 ├── 30-site.d
 ├── 50-local.d
 ├── 55-org.my.company.d
 │ └── 10-org.my.company.product.pkla
 └── 90-mandatory.d</pre>
</dl>
<p> the evaluation order of the .pkla files is: </p>
<dl>
<dd>1. 10-desktop-policy.pkla</dl>
<dl>
<dd>2. 01-some-changes-from-a-subvendor.pkla</dl>
<dl>
<dd>3. 10-org.my.company.product.pkla (the /var one)</dl>
<dl>
<dd>4. 10-org.my.company.product.pkla (the /etc one)</dl>
<p> When the list of authorization entries has been calculated, the authorization check can be made. First, the user of the Subject is determined and the groups that the user belongs are looked up. </p>
<p> Then, authorization entries that include the &quot;default&quot; field value in the <i>Identity</i> field are consulted in order. If the authorization entry matches the data from the authorization check, then the authorization result from <i>RequireAny</i>, <i>RequireInactive</i> or <i>RequireActive</i> is used. </p>
<p> Next, for each group identity, all authorization entries that contain a matching group entry are again consulted in the same manner. </p>
<p> Finally, the authorization entries are consulted using the user identity in the same manner. </p>
<p> Note that processing continues even after a match. This allows for so called &#8220;negative authorizations&#8221;, see the section called &#8220;EXAMPLE&#8221; for further discussion.</p>
<h2>Example</h2>
<p>The following .pkla file grants authorization to all users in the staff group for actions matching the glob com.example.awesomeproduct.* provided they are in an active session on the local console: </p>
<dl>
<dd>
<pre>[Normal Staff Permissions]
Identity=unix-group:staff
Action=com.example.awesomeproduct.*
ResultAny=no
ResultInactive=no
ResultActive=yes</pre>
</dl>
<p> If the users homer and grimes are member of the staff group but policy requires that an administrator needs to authenticate every time authorization for any action matching com.example.awesomeproduct.* is required, one would add </p>
<dl>
<dd>
<pre>[Exclude Some Problematic Users]
Identity=unix-user:homer;unix-user:grimes
Action=com.example.awesomeproduct.*
ResultAny=no
ResultInactive=no
ResultActive=auth_admin</pre>
</dl>
<p> and make sure this authorization entry is after the first one. </p>
<p> The following entry modifies the default authorization decision (it is overridden by any entry that matches using unix-user: or unix-group:, but overrides any defaults set by the application author in an .action file): </p>
<dl>
<dd>
<pre>[Disable Access by Default]
Identity=default
Action=com.example.awesomeproduct.*
ResultAny=no
ResultInactive=no
ResultActive=no</pre>
</dl>
<h2>Files</h2>
<p>/etc/polkit-1/localauthority, /var/lib/polkit-1/localauthority</p>
<dl>
<dd>Default directories containing decision configuration files.</dl>
<h2>Author</h2>
<p>Written by David Zeuthen &lt;davidz [at] redhat.com&gt; with a lot of help from many others. Adapted by Miloslav Trmač &lt;mitr [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-polkit/">polkit</a></code>(8) </p>
