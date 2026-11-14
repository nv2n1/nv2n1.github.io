---
title: "nbprgstr(1)"
name: "nbprgstr"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nbprgstr/"
description: "nbp, nbplkup, nbprgstr, nbpunrgstr – access NBP database"
---

<h2 class="name">NAME</h2>
<p> nbp, nbplkup, nbprgstr, nbpunrgstr &#8211; access NBP database </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nbplkup</code> [-r&nbsp;<wbr><i>maxresponses</i>] [-A&nbsp;<wbr><i>address</i>] [-m&nbsp;<wbr><i>maccodepage</i>] <i>nbpname</i></p>
<dt> <code>nbprgstr</code> [-A&nbsp;<wbr><i>address</i>] [-p&nbsp;<wbr><i>port</i>] [-m&nbsp;<wbr><i>maccodepage</i>] <i>nbpname</i></p>
<dt> <code>nbpunrgstr</code> [-A&nbsp;<wbr><i>address</i>] [-m&nbsp;<wbr><i>maccodepage</i>] <i>nbpname</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>nbprgstr</code></p>
<dd>registers <i>nbpname</i> with <code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8), at the given <i>port</i>. <code>nbpunrgstr</code> informs <code>atalkd</code> that <i>nbpname</i> is no longer to be advertised. </p>
<p> <code>nbplkup</code> displays up to <i>maxresponses</i> (default 1000) entities registered on the AppleTalk internet. <i>nbpname</i> is parsed by <code><a href="/docs/linux/man/3-nbp_name/">nbp_name</a></code>(3). An `<code>=</code>&#8216; for the <i>object</i> or <i>type</i> matches anything, and an `<code>*</code>&#8216; for <i>zone</i> means the local zone. The default values are taken from the <code>NBPLKUP</code> environment variable, parsed as an <i>nbpname</i>.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> NBPLKUP</p>
<dl>
<dt>
<dd> default nbpname for nbplkup</dl>
<p> ATALK_MAC_CHARSET</p>
<dl>
<dt>
<dd> the codepage used by the clients on the Appletalk network</dl>
<p> ATALK_UNIX_CHARSET</p>
<dl>
<dt>
<dd> the codepage used to display extended characters on this shell.</dl>
<h2>EXAMPLE</h2>
<p> Find all devices of type <code>LaserWriter</code> in the local zone. </p>
<dl>
<dt>
<dd>
<pre>
example% <code>nbplkup :LaserWriter</code>
               Petoskey:LaserWriter        7942.129:218
             Gloucester:LaserWriter        8200.188:186
                 Rahway:LaserWriter        7942.2:138
             517 Center:LaserWriter        7942.2:132
                  ionia:LaserWriter        7942.2:136
     Evil DEC from Hell:LaserWriter        7942.2:130
              Hamtramck:LaserWriter        7942.2:134
         Iron Mountain :LaserWriter        7942.128:250
example%
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nbp_name/">nbp_name</a></code>(3), <code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8). </p>
<h2>Index</h2>
