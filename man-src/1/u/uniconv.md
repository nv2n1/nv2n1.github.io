---
title: "uniconv(1)"
name: "uniconv"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uniconv/"
description: "uniconv – convert Netatalk volume encoding"
---

<h2 class="name">NAME</h2>
<p> uniconv &#8211; convert Netatalk volume encoding </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>uniconv</code> [-ndv] -c&nbsp;<wbr><i>cnidbackend</i> -f&nbsp;<wbr><i>fromcode</i> -t&nbsp;<wbr><i>tocode</i> [-m&nbsp;<wbr><i>maccode</i>] <i>volumepath</i></dl>
<h2>DESCRIPTION</h2>
<p> <code>uniconv</code></p>
<dd>converts the volume encoding of <i>volumepath</i> from the <i>fromcode</i> to the <i>tocode</i> encoding.</p>
<h2>OPTIONS</h2>
<p> -c</p>
<dl>
<dt>
<dd> CNID backend used on this volume, usually cdb or dbd. Should match the backend selected with afpd for this volume. If not specified, the default CNID backend `cdb&#8217; is used</dl>
<p> -d</p>
<dl>
<dt>
<dd> don&#8217;t CAP encode leading dots (:2e), equivalent to <code>usedots</code> in <code><a href="/docs/linux/man/5-applevolumes-default/">AppleVolumes.default</a></code>(5)</dl>
<p> -f</p>
<dl>
<dt>
<dd> encoding to convert from, use ASCII for CAP encoded volumes</dl>
<p> -h</p>
<dl>
<dt>
<dd> display help</dl>
<p> -m</p>
<dl>
<dt>
<dd> Macintosh client codepage, required for CAP encoded volumes. Defaults to `MAC_ROMAN&#8217;</dl>
<p> -n</p>
<dl>
<dt>
<dd> `dry run&#8217;, don&#8217;t do any real changes</dl>
<p> -t</p>
<dl>
<dt>
<dd> volume encoding to convert to, e.g. UTF8</dl>
<p> -v</p>
<dl>
<dt>
<dd> verbose output, use twice for maximum logging.</dl>
<p> -V</p>
<dl>
<dt>
<dd> print version and exit</dl>
<h2>WARNING</h2>
<p> Setting the wrong options might render your data unusable!!! Make sure you know what you are doing. Always backup your data first. </p>
<p> It is <code>*strongly*</code> recommended to do a `dry run&#8217; first and to check the output for conversion errors. </p>
<p> <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) should <i>not</i> be running while you change the volume encoding. Remember to change <code>volcodepage</code> in <code><a href="/docs/linux/man/5-applevolumes-default/">AppleVolumes.default</a></code>(5) to the new codepage, before restarting afpd. </p>
<p> <code>USE AT YOUR OWN RISK!!!</code></p>
<h2>SELECTABLE CHARSETS</h2>
<p> Netatalk provides internal support for UTF-8 (pre- and decomposed) and CAP. If you want to use other charsets, they must be provided by <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) </p>
<p> <code>uniconv</code> also knows iso-8859.adapted, an old style 1.x NLS widely used. This is only intended for upgrading old volumes, <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8) cannot handle iso-8859.adapted anymore.</p>
<h2>CNID BACKGROUND</h2>
<p> The CNID backends maintains name to ID mappings. If you change a filename outside <a href="/docs/linux/man/8-afpd/">afpd</a>(8) (shell, samba), the CNID db, i.e. the DIDNAME index, gets inconsistent. Netatalk tries to recover from such inconsistencies as gracefully as possible. The mechanisms to resolve such inconsistencies may fail sometimes, though, as this is not an easy task to accomplish. I.e. if several names in the path to the file or directory have changed, things may go wrong. </p>
<p> If you change a lot of filenames at once, chances are higher that the afpds fallback mechanisms fail, i.e. files will be assigned new IDs, even though the file hasn&#8217;t changed. <code>uniconv</code> therefore updates the CNID entry for each file/directory directly after it changes the name to avoid inconsistencies. The two supported backends for volumes, dbd and cdb, use the same CNID db format. Therefore, you <i>could</i> use <code>uniconv</code> with cdb and <code>afpd</code> with dbd later. </p>
<p> <code>Warning</code>: There must not be two processes opening the CNID database using different backends at once! If a volume is still opened with dbd (cnid_metad/cnid_dbd) and you start <code>uniconv</code> with cdb, the result will be a corrupted CNID database, as the two backends use different locking schemes. You might run into additional problems, e.g. if dbd is compiled with transactions, cdb will not update the transaction logs. </p>
<p> In general, it is recommended to use the same backend for <code>uniconv</code> you are using with <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8).</p>
<h2>EXAMPLES</h2>
<p> convert 1.x CAP encoded volume to UTF-8, clients used MacRoman codepage, cnidscheme is dbd: </p>
<dl>
<dt>
<dd>
<pre>
example%<code> uniconv -c dbd -f ASCII -t UTF8 -m MAC_ROMAN /path/to/share</code>
</pre>
</dl>
<p> convert iso8859-1 volume to UTF-8, cnidscheme is cdb: </p>
<dl>
<dt>
<dd>
<pre>
example%<code> uniconv -c cdb -f ISO-8859-1 -t UTF8 -m MAC_ROMAN /path/to/share</code>
</pre>
</dl>
<p> convert 1.x volume using iso8859-1 adapted NLS to CAP encoding: </p>
<dl>
<dt>
<dd>
<pre>
example%<code> uniconv -f ISO-8859-ADAPTED -t ASCII -m MAC_ROMAN/path/to/share</code>
</pre>
</dl>
<p> convert UTF-8 volume to CAP, for MacCyrillic clients: </p>
<dl>
<dt>
<dd>
<pre>
example%<code> uniconv -f UTF8 -t ASCII -m MAC_CYRILLIC /path/to/share</code>
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-applevolumes-default/">AppleVolumes.default</a></code>(5),<code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8),<code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1),<code><a href="/docs/linux/man/8-cnid_metad/">cnid_metad</a></code>(8),<code><a href="/docs/linux/man/8-cnid_dbd/">cnid_dbd</a></code>(8) </p>
<h2>Index</h2>
