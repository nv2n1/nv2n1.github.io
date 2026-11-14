---
title: "softhsm2-util(1)"
name: "softhsm2-util"
section: "1"
letter: "s"
url: "/docs/linux/man/1-softhsm2-util/"
description: "softhsm2-util – support tool for libsofthsm2"
---

<h2>NAME</h2>
<p> softhsm2-util &#8211; support tool for libsofthsm2</p>
<h2>SYNOPSIS</h2>
<p> <code>softhsm2-util &#8211;show-slots</code> </p>
<p> <code>softhsm2-util &#8211;init-token</code> <code>&#8211;slot</code> <i>number</i> <code>&#8211;label</code> <i>text</i> \<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>&#8211;so-pin</code> <i>PIN</i> <code>&#8211;pin</code> <i>PIN</i>] </p>
<p> <code>softhsm2-util &#8211;import</code> <i>path</i> [<code>&#8211;file-pin</code> <i>PIN</i>] <code>&#8211;slot</code> <i>number</i> \<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>&#8211;pin</code> <i>PIN</i> <code>&#8211;no-public-key]</code> <code>&#8211;label</code> <i>text</i> <code>&#8211;id</code> <i>hex</i></p>
<h2>DESCRIPTION</h2>
<p> <code>softhsm2-util</code> is a support tool mainly for libsofthsm2. It can also be used with other PKCS#11 libraries by using the option <code>&#8211;module</code> </p>
<p> Read the sections below to get more information on the libsofthsm2 and PKCS#11. Most applications assumes that the token they want to use is already initialized. It is then up to the user to initialize the PKCS#11 token. This is done by using the PKCS#11 interface, but instead of writing your own tool you can use the <code>softhsm2-util</code> tool. </p>
<p> Keys are usually created directly in the token, but the user may want to use an existing key pair. Keys can be imported to a token by using the PKCS#11 interface, but this tool can also be used if the user has the key pair in a PKCS#8 file. If you need to convert keys from BIND .private-key format over to PKCS#8, one can use <code>softhsm2-keyconv</code>. </p>
<p> The libary <code>libsofthsm2</code>, known as SoftHSM, provides cryptographic functionality by using the PKCS#11 API. It was developed as a part of the OpenDNSSEC project, thus designed to meet the requirements of OpenDNSSEC, but can also work together with other software that want to use the functionality of the PKCS#11 API. </p>
<p> SoftHSM is a software implementation of a generic cryptographic device with a PKCS#11 interface. These devices are often called tokens. Read in the manual <a href="/docs/linux/man/5-softhsm2-conf/">softhsm2.conf</a>(5) on how to create these tokens and how they are added to a slot in SoftHSM. </p>
<p> The <code>PKCS#11</code> API can be used to handle and store cryptographic keys. This interface specifies how to communicate with cryptographic devices such as HSMs (Hardware Security Modules) and smart cards. The purpose of these devices is, among others, to generate cryptographic keys and sign information without revealing private-key material to the outside world. They are often designed to perform well on these specific tasks compared to ordinary processes in a normal computer. </p>
<h2>ACTIONS</h2>
<dl>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Show the help information.</p>
<dt><code>&#8211;import </code><i>path</i></p>
<dd> Import a key pair from the given <i>path</i>. The file must be in PKCS#8-format.<br />
 Use with <code>&#8211;file-pin</code>, <code>&#8211;slot</code>, <code>&#8211;pin</code>, <code>&#8211;no-public-key</code>, <code>&#8211;label</code>, and <code>&#8211;id</code>.</p>
<dt><code>&#8211;init-token</code></p>
<dd> Initialize the token at a given slot. If the token is already initialized then this command will reinitialize it, thus erasing all the objects in the token. The matching Security Officer (SO) PIN must also be provided when doing reinitialization.<br />
 Use with <code>&#8211;slot</code> or <code>&#8211;free</code>, <code>&#8211;label</code>, <code>&#8211;so-pin</code>, and <code>&#8211;pin</code>.</dl>
<dl>
<dt><code>&#8211;show-slots</code></p>
<dd> Display all the available slots and their current status.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Show the version info.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;file-pin </code><i>PIN</i></p>
<dd> The <i>PIN</i> will be used to decrypt the PKCS#8 file. If not given then the PKCS#8 file is assumed to be unencrypted.</p>
<dt><code>&#8211;force </code></p>
<dd> Use this option to override the warnings and force the given action.</p>
<dt><code>&#8211;free</code></p>
<dd> Initialize the first free token.</p>
<dt><code>&#8211;id </code><i>hex</i></p>
<dd> Choose an ID of the key pair. The ID is in hexadecimal with a variable length. Use with <code>&#8211;force </code> when importing a key pair if the ID already exists.</p>
<dt><code>&#8211;label </code><i>text</i></p>
<dd> Defines the <i>label</i> of the object or the token.</p>
<dt><code>&#8211;module </code><i>path</i></p>
<dd> Use another PKCS#11 library than SoftHSM.</p>
<dt><code>&#8211;no-public-key</code></p>
<dd> Do not import the public key.</p>
<dt><code>&#8211;pin </code><i>PIN</i></p>
<dd> The <i>PIN</i> for the normal user.</p>
<dt><code>&#8211;slot </code><i>number</i></p>
<dd> The slot where the token is located.</p>
<dt><code>&#8211;so-pin </code><i>PIN</i></p>
<dd> The <i>PIN</i> for the Security Officer (SO).</dl>
<h2>EXAMPLES</h2>
<p> The token can be initialized using this command: </p>
<dl>
<dt>
<dd>
<pre>
softhsm2-util --init-token --slot 1 --label &quot;A token&quot;
</pre>
</dl>
<p> A key pair can be imported using the softhsm tool where you specify the path to the key file, slot number, label and ID of the new objects, and the user PIN. The file must be in PKCS#8 format. </p>
<dl>
<dt>
<dd>
<pre><code>
softhsm2 - util-- import key1.pem-- slot 1 --label "My key"

    &amp; nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
--id A1B2-- pin 123456
</code></pre>
<p> (Add, &#8211;file-pin <i>PIN</i>, if the key file is encrypted.)</dl>
<h2>AUTHORS</h2>
<p> Written by Rickard Bellgrim, Francis Dupont, René Post, and Roland van Rijswijk. </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-softhsm2-keyconv/">softhsm2-keyconv</a></i>(1), <i><a href="/docs/linux/man/1-softhsm2-migrate/">softhsm2-migrate</a></i>(1), <i><a href="/docs/linux/man/5-softhsm2-conf/">softhsm2.conf</a></i>(5) </p>
<h2>Index</h2>
