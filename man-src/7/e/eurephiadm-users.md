---
title: "eurephiadm-users(7)"
name: "eurephiadm-users"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-users/"
description: "eurephiadm users – User management module"
---

<p>eurephiadm users &#8211; User management module</p>
<h2>Synopsis</h2>
<p><code>eurephiadm users</code> \-\-list|\-l [\-S|\-\-sort &lt;sort keys&gt;]<br />
 <code>eurephiadm users</code> \-\-show|\-s [\-i|\-\-uid &lt;user id&gt;] [\-u|\-\-username &lt;user name&gt;] [\-l|\-|-lastlog] [\-L|\-\-lastlog-details] [\-a|\-\-attempts] [\-b|\-\-blacklist]<br />
 <code>eurephiadm users</code> \-\-activate|\-a [\-i|\-\-uid &lt;user id&gt;] [\-u|\-\-username &lt;user name&gt;]<br />
 <code>eurephiadm users</code> \-\-deactivate|\-d [\-i|\-\-uid &lt;user id&gt;] [\-u|\-\-username &lt;user name&gt;]<br />
 <code>eurephiadm users</code> \-\-add|\-A [\-u|\-\-username &lt;user name&gt;] [\-P|\-\-password &lt;plain text password&gt;] [\-C|\-\-certid &lt;certificate ID&gt;] [\-D|\-\-digest &lt;certificate SHA1 digest&gt;] [\-c|\-\-certfile &lt;certificate file&gt;] [\-2|\-\-pkcs12]<br />
 <code>eurephiadm users</code> \-\-delete|\-D [\-i|\-\-uid &lt;user id&gt;] [\-u|\-\-username &lt;user name&gt;]<br />
 <code>eurephiadm users</code> \-\-password|\-p [\-i|\-\-uid &lt;user id&gt;] [\-u|\-\-username &lt;user name&gt;]<br />
 <code>eurephiadm users</code> [\-h|\-\-help [&lt;mode&gt;]]</p>
<h2>Description</h2>
<p><code>eurephiadm users</code> manages eurephia user accounts. It provides an interface for listing, creating new, modify and delete user accounts.</p>
<h2>Modes</h2>
<h3>Available modes:</h3>
<dl>
<dt><code>-l | &#8211;list</code></p>
<dd>[-S|&#8211;sort &lt;sort keys&gt;]<br />
 List all user accounts. Providing <code>-S|&#8211;sort</code> and a sort key will define the sort order of the list. Valid sort keys are:</p>
<dd>uid &#8211; user ID<br />
 username &#8211; User name belonging to the user account<br />
 activated &#8211; When the user account was activated<br />
 deactivated &#8211; When the user account was deactivated<br />
 lastaccess &#8211; When the user account was last used</p>
<dt><code>-s | &#8211;show</code></p>
<dd>[-i|&#8211;uid &lt;user id&gt;] [-u|&#8211;username &lt;user name&gt;] [-l|&#8211;lastlog] [-L|&#8211;lastlog-details] [-a|&#8211;attempts] [-b|&#8211;blacklist]<br />
 Show user account details. <code>&#8211;uid</code> or <code>&#8211;username</code> are required. The other arguments only defined which kind of information to show.</p>
<dt><code>-a | &#8211;activate</code></p>
<dd>[-i|&#8211;uid &lt;user id&gt;] [-u|&#8211;username &lt;user name&gt;]<br />
 Activate a user account. <code>&#8211;uid</code> or <code>&#8211;username</code> is required.</p>
<dt><code>-d | &#8211;deactivate</code></p>
<dd>[-i|&#8211;uid &lt;user id&gt;] [-u|&#8211;username &lt;user name&gt;]<br />
 Deactivate a user account. <code>&#8211;uid</code> or <code>&#8211;username</code> is required.</p>
<dt><code>-A | &#8211;add</code></p>
<dd>[-u|&#8211;username &lt;user name&gt;] [-P|&#8211;password &lt;plain text password&gt;] [-C|&#8211;certid &lt;certificate ID&gt;] [-D|&#8211;digest &lt;certificate SHA1 digest&gt;] [-c|&#8211;certfile &lt;certificate file&gt;] [-2|&#8211;pkcs12]<br />
 Add a new user account. <code>&#8211;username</code> is required. If you want to assign a password for the new user account via the command line, provide the password with <code>&#8211;password</code>.</p>
<dd>To associate this user account against an already regstistered certificate, it can be done by either refering to the certificate ID in eurephia using <code>&#8211;certid</code> or providing the certificate SHA1 digest/fingerprint to <code>&#8211;digest</code>.</p>
<dd>A brand new certificate can be registered and linked to the user account directly if you have access to the certificate file. The file can be in either PEM/DER format or PKCS#12. Use <code>&#8211;certfile</code> to indicate the certificate file to extract the information from and <code>&#8211;pkcs12</code> if it is a PKCS#12 file.</p>
<dt><code>-D | &#8211;delete</code></p>
<dd>[-i|&#8211;uid &lt;user id&gt;] [-u|&#8211;username &lt;user name&gt;]<br />
 Delete a user account. <code>&#8211;uid</code> or <code>&#8211;username</code> is required.</p>
<dt><code>-p | &#8211;password</code></p>
<dd>[-i|&#8211;uid &lt;user id&gt;] [-u|&#8211;username &lt;user name&gt;]<br />
 Change password on a user account. <code>&#8211;uid</code> or <code>&#8211;username</code> is required.</p>
<dt><code>-h | &#8211;help</code></p>
<dd>[&lt;mode&gt;]<br />
 Show a help screen. Without any arguments, all modes are listed. Providing a mode will show more information about the chosen mode.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm/">eurephiadm</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-certs/">eurephiadm-certs</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
