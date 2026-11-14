---
title: "heimdal-ktutil(8)"
name: "heimdal-ktutil"
section: "8"
letter: "h"
url: "/docs/linux/man/8-heimdal-ktutil/"
description: "ktutil – manage Kerberos keytabs"
---

<p><code>ktutil</code> &#8211; manage Kerberos keytabs</p>
<h2>Synopsis</h2>
<p>[-<code>k </code><i>keytab | </i> &#8211;<code>-keytab= </code><i>keytab</i> ] [-<code>v | &#8211;verbose</code> ] [-<code>-version</code> ] [-<code>h | &#8211;help</code> ] <i>command</i> [<i>args</i> ]</p>
<h2>Description</h2>
<p>is a program for managing keytabs. Supported options:</p>
<dl>
<dt><code>-v , &#8211;verbose</code></p>
<dd>Verbose output.</dl>
<p> <i>command</i> can be one of the following:</p>
<dl>
<dt><code>add </code>[-<code>p </code><i>principal </i>[-<code>-principal= </code><i>principal </i>] ]</p>
<dd>Oo Fl V Ar kvno Oc Oo Fl Fl kvno= Ns Ar kvno Oc Oo Fl e Ar enctype Oc Oo Fl Fl enctype= Ns Ar enctype Oc Oo Fl w Ar password Oc Oo Fl Fl password= Ns Ar password Oc Oo Fl r Oc Oo Fl Fl random Oc Oo Fl s Oc Oo Fl Fl no-salt Oc Oo Fl H Oc Op Fl Fl hex Adds a key to the keytab. Options that are not specified will be prompted for. This requires that you know the password or the hex key of the principal to add; if what you really want is to add a new principal to the keytab, you should consider the <i>get</i> command, which talks to the kadmin server.</p>
<dt><code>change </code>[-<code>r </code><i>realm </i>[-<code>-realm= </code><i>realm </i>] ]</p>
<dd>Oo Fl Fl a Ar host Oc Oo Fl Fl admin-server= Ns Ar host Oc Oo Fl Fl s Ar port Oc Op Fl Fl server-port= Ns Ar port Update one or several keys to new versions. By default, use the admin server for the realm of a keytab entry. Otherwise it will use the values specified by the options. If no principals are given, all the ones in the keytab are updated.</p>
<dt><code>copy </code><i>keytab-src keytab-dest</i></p>
<dd>Copies all the entries from <i>keytab-src</i> to <i>keytab-dest</i></p>
<dt><code>get </code>[-<code>p </code><i>admin principal </i>]</p>
<dd>Oo Fl Fl principal= Ns Ar admin principal Oc Oo Fl e Ar enctype Oc Oo Fl Fl enctypes= Ns Ar enctype Oc Oo Fl r Ar realm Oc Oo Fl Fl realm= Ns Ar realm Oc Oo Fl a Ar admin server Oc Oo Fl Fl admin-server= Ns Ar admin server Oc Oo Fl s Ar server port Oc Oo Fl Fl server-port= Ns Ar server port Oc Ar principal &#8230; For each <i>principal</i> generate a new key for it (creating it if it doesn&#8217;t already exist), and put that key in the keytab. If no <i>realm</i> is specified, the realm to operate on is taken from the first principal.</p>
<dt><code>list </code>[-<code>-keys </code>[-<code>-timestamp</code> ] ]</p>
<dd>List the keys stored in the keytab.</p>
<dt><code>remove </code>[-<code>p </code><i>principal </i>[-<code>-principal= </code><i>principal </i>] ]</p>
<dd>Oo Fl V kvno Oc Oo Fl Fl kvno= Ns Ar kvno Oc Oo Fl e enctype Oc Oo Fl Fl enctype= Ns Ar enctype Oc Removes the specified key or keys. Not specifying a <i>kvno</i> removes keys with any version number. Not specifying an <i>enctype</i> removes keys of any type.</p>
<dt><code>rename </code><i>from-principal to-principal</i></p>
<dd>Renames all entries in the keytab that match the <i>from-principal</i> to <i>to-principal</i></p>
<dt><code>purge </code>[-<code>-age= </code><i>age</i> ]</p>
<dd>Removes all old versions of a key for which there is a newer version that is at least <i>age</i> (default one week) old.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-kadmin/">kadmin</a>(8) </p>
