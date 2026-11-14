---
title: "k5srvutil(1)"
name: "k5srvutil"
section: "1"
letter: "k"
url: "/docs/linux/man/1-k5srvutil/"
description: "k5srvutil – host key table (keytab) manipulation utility"
---

<h2>NAME</h2>
<p> k5srvutil &#8211; host key table (keytab) manipulation utility</p>
<h2>SYNOPSIS</h2>
<p> <code>k5srvutil</code> <i>operation</i> [<code>-i</code>] [<code>-f</code> <i>filename</i>] [<code>-e</code> <i>keysalts</i>]</p>
<h2>DESCRIPTION</h2>
<p> k5srvutil allows an administrator to list keys currently in a keytab, to obtain new keys for a principal currently in a keytab, or to delete non-current keys from a keytab. </p>
<p> <i>operation</i> must be one of the following:</p>
<dl>
<dt><code>list</code></p>
<dd> Lists the keys in a keytab, showing version number and principal name.</p>
<dt><code>change</code></p>
<dd> Uses the kadmin protocol to update the keys in the Kerberos database to new randomly-generated keys, and updates the keys in the keytab to match. If a key&#8217;s version number doesn&#8217;t match the version number stored in the Kerberos server&#8217;s database, then the operation will fail. If the <code>-i</code> flag is given, k5srvutil will prompt for confirmation before changing each key. If the <code>-k</code> option is given, the old and new keys will be displayed. Ordinarily, keys will be generated with the default encryption types and key salts. This can be overridden with the <code>-e</code> option. Old keys are retained in the keytab so that existing tickets continue to work, but <code>delold</code> should be used after such tickets expire, to prevent attacks against the old keys.</p>
<dt><code>delold</code></p>
<dd> Deletes keys that are not the most recent version from the keytab. This operation should be used some time after a change operation to remove old keys, after existing tickets issued for the service have expired. If the <code>-i</code> flag is given, then k5srvutil will prompt for confirmation for each principal.</p>
<dt><code>delete</code></p>
<dd> Deletes particular keys in the keytab, interactively prompting for each key. </p>
<p> In all cases, the default keytab is used unless this is overridden by the <code>-f</code> option. </p>
<p> k5srvutil uses the <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i> program to edit the keytab in place.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-kadmin/">kadmin</a>(1)</i>, <i><a href="/docs/linux/man/1-ktutil/">ktutil</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
