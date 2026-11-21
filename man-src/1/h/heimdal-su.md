---

title: "heimdal-su(1)"
name: "heimdal-su"
section: "1"
letter: "h"
url: "/docs/linux/man/1-heimdal-su/"
description: "su – substitute user identity"
---

<p> <code>su</code> &#8211; substitute user identity </p>
<p> <code>su</code> [-<code>K | &#8211;no-kerberos</code> ] [-<code>f</code> ] [-<code>l | &#8211;full</code> ] [-<code>m</code> ] [-<code>i </code><i>instance | </i> &#8211;<code>-instance= </code><i>instance</i> ] [-<code>c </code><i>command | </i> &#8211;<code>-command= </code><i>command</i> ] [<i>login </i>[<i>shell arguments</i> ] ]</p>
<p> <code>su</code> will use Kerberos authentication provided that an instance for the user wanting to change effective UID is present in a file named .k5login in the target user id&#8217;s home directory </p>
<p> A special case exists where `root&#8217; Ap s ~/.k5login needs to contain an entry for: `user&#8217; Ns / Ns Ao instance Ac Ns @ Ns REALM for <code>su</code> to succed (where Aq instance is `root&#8217; unless changed with &#8211;<code>i )</code> </p>
<p> In the absence of either an entry for current user in said file or other problems like missing `host/hostname [at] REALM&#8217; keys in the system&#8217;s keytab, or user typing the wrong password, <code>su</code> will fall back to traditional /etc/passwd authentication. </p>
<p> When using /etc/passwd authentication, <code>su</code> allows `root&#8217; access only to members of the group `wheel&#8217; , or to any user (with knowledge of the `root&#8217; password) if that group does not exist, or has no members. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-K</code></dt>
<dd> &#8211;<code>-no-kerberos</code> don&#8217;t use Kerberos.</dd>
<dt><code>-f</code></dt>
<dd> don&#8217;t read .cshrc.</dd>
<dt><code>-l</code></dt>
<dd> &#8211;<code>-full</code> simulate full login.</dd>
<dt><code>-m</code></dt>
<dd> leave environment unmodified.</dd>
<dt><code>-i </code><i>instance</i></dt>
<dd> &#8211;<code>-instance= </code><i>instance</i> root instance to use.</dd>
<dt><code>-c </code><i>command</i></dt>
<dd> &#8211;<code>-command= </code><i>command</i> command to execute.</dd></dl>
