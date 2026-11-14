---
title: "opencryptoki-conf(5)"
name: "opencryptoki-conf"
section: "5"
letter: "o"
url: "/docs/linux/man/5-opencryptoki-conf/"
description: "opencryptoki.conf – Configuration file for pkcsslotd."
---

<p>opencryptoki.conf &#8211; Configuration file for pkcsslotd. </p>
<h2>Description</h2>
<p>pkcsslotd uses a configuration file at &quot;/etc&quot;/opencryptoki/opencryptoki.conf This is a text file that contains information used to configure pkcs#11 slots. At startup, the pkcsslotd daemon parses this file to determine which slots will be made available. </p>
<h2>Syntax</h2>
<p>This file is made up of slot descriptions. Each slot description is composed of a slot number, brackets and key-value pairs. </p>
<p>&nbsp;<wbr>slot number<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>key&nbsp;<wbr>=&nbsp;<wbr>value<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>} </p>
<p> More than one key-value pair may be used within a slot description. </p>
<p> A key-value pair is composed of, <code>keyword = value.</code> </p>
<p> The following keywords are valid: </p>
<dl>
<dt><code>description</code></p>
<dd>A Description of the slot. PKCS#11v2.20 defined this as a 64-byte max character-string.</p>
<dt><code>stdll</code></p>
<dd>This keyword is used to define the name of the stdll or token library that will be used for this slot. The stdll is an available token library in opencryptoki.</p>
<dt><code>manufacturer</code></p>
<dd>This keyword is used to name the ID of the slot manufacturer. PKCS#11v2.20 defines this as a 32 byte long string.</p>
<dt><code>hwversion</code></p>
<dd>Version number of the slot&#8217;s hardware, if any. The version number is composed of a major version number (the integer portion of the version) and a minor version number (the hundredths portion of the version). For example, version 1.2, major = 1, minor = 2</p>
<dt><code>firmwareversion</code></p>
<dd>Version number of the slot&#8217;s firmware, if any. The version number is composed of a major version number (the integer portion of the version) and a minor version number (the hundredths portion of the version).</p>
<dt><code>confname</code></p>
<dd>If the slot is associated with a token that has its own configuration file, this option identifies the name of that configuration file. For example, confname=ep11tok.conf </p>
</dl>
<h2>Notes</h2>
<p>The pound sign (&#8216;#&#8217;) is used to indicate a comment. Both the comment character and any text after it, up to the end of the line, are ignored. The comment character cannot be used inside the brackets of slot descriptions, as this will cause a syntax error. </p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-opencryptoki/">opencryptoki</a></code>(7),</p>
<dd>
<dt><code><a href="/docs/linux/man/8-pkcsslotd/">pkcsslotd</a></code>(8),</p>
<dd>
