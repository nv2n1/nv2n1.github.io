---
title: "pam_userdb(8)"
name: "pam_userdb"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_userdb/"
description: "pam_userdb – PAM module to authenticate against a db database"
---

<p>pam_userdb &#8211; PAM module to authenticate against a db database</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_userdb.so</code> db=<i>/path/database</i> [debug] [crypt=[crypt|none]] [icase] [dump] [try_first_pass] [use_first_pass] [unknown_ok] [key_only]</dl>
<h2>Description</h2>
<dd>The pam_userdb module is used to verify a username/password pair against values stored in a Berkeley DB database. The database is indexed by the username, and the data fields corresponding to the username keys are the passwords.</p>
<h2>Options</h2>
<p><code>crypt=[crypt|none]</code></p>
<dl>
<dd>Indicates whether encrypted or plaintext passwords are stored in the database. If it is <code>crypt</code>, passwords should be stored in the database in <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3) form. If <code>none</code> is selected, passwords should be stored in the database as plaintext.</dl>
<p> <code>db=</code><i>/path/database</i></p>
<dl>
<dd>Use the /path/database database for performing lookup. There is no default; the module will return <code>PAM_IGNORE</code> if no database is provided. Note that the path to the database file should be specified without the .db suffix.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Print debug information.</dl>
<p> <code>dump</code></p>
<dl>
<dd>Dump all the entries in the database to the log. Don&#8217;t do this by default!</dl>
<p> <code>icase</code></p>
<dl>
<dd>Make the password verification to be case insensitive (ie when working with registration numbers and such). Only works with plaintext password storage.</dl>
<p> <code>try_first_pass</code></p>
<dl>
<dd>Use the authentication token previously obtained by another module that did the conversation with the application. If this token can not be obtained then the module will try to converse. This option can be used for stacking different modules that need to deal with the authentication tokens.</dl>
<p> <code>use_first_pass</code></p>
<dl>
<dd>Use the authentication token previously obtained by another module that did the conversation with the application. If this token can not be obtained then the module will fail. This option can be used for stacking different modules that need to deal with the authentication tokens.</dl>
<p> <code>unknown_ok</code></p>
<dl>
<dd>Do not return error when checking for a user that is not in the database. This can be used to stack more than one pam_userdb module that will check a username/password pair in more than a database.</dl>
<p> <code>key_only</code></p>
<dl>
<dd>The username and password are concatenated together in the database hash as &#8216;username-password&#8217; with a random value. if the concatenation of the username and password with a dash in the middle returns any result, the user is valid. this is useful in cases where the username may not be unique but the username and password pair are.</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>account</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>Authentication failure.</dl>
<p> PAM_AUTHTOK_RECOVERY_ERR</p>
<dl>
<dd>Authentication information cannot be recovered.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>Conversation failure.</dl>
<p> PAM_SERVICE_ERR</p>
<dl>
<dd>Error in service module.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<p> PAM_USER_UNKNOWN</p>
<dl>
<dd>User not known to the underlying authentication module.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre>auth sufficient pam_userdb.so icase db=/etc/dbtest</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_userdb was written by Cristian Gafton &gt;gafton [at] redhat.com&lt;.</p>
