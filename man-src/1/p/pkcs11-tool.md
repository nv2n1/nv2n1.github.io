---
title: "pkcs11-tool(1)"
name: "pkcs11-tool"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkcs11-tool/"
description: "pkcs11-tool – utility for managing and using PKCS #11 security tokens"
---

<h2>SYNOPSIS</h2>
<p> <code>pkcs11-tool</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>pkcs11-tool</code> utility is used to manage the data objects on smart cards and similar PKCS #11 security tokens. Users can list and read PINs, keys and certificates stored on the token. User PIN authentication is performed for those operations that require it.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;login, -l</code></p>
<dl>
<dt>
</dt><dd> Authenticate to the token before performing other operations. This option is not needed if a PIN is provided on the command line.</dd></dl>
<p> <code>&#8211;pin</code> <i>pin</i>, <code>-p</code> <i>pin</i></p>
<dl>
<dt>
</dt><dd> Use the given <i>pin</i> for token operations. WARNING: Be careful using this option as other users may be able to read the command line from the system or if it is embedded in a script. </dd>
<p> This option will also set the <code>&#8211;login</code> option.</dl>
<p> <code>&#8211;so-pin</code> <i>pin</i></p>
<dl>
<dt>
</dt><dd> Use the given <i>pin</i> as the Security Officer PIN for some token operations (token initialization, user PIN initialization, etc). The same warning as <code>&#8211;pin</code> also applies here.</dd></dl>
<p> <code>&#8211;init-token</code></p>
<dl>
<dt>
</dt><dd> Initializes a token: set the token label as well as a Security Officer PIN (the label must be specified using <code>&#8211;label</code>).</dd></dl>
<p> <code>&#8211;init-pin</code></p>
<dl>
<dt>
</dt><dd> Initializes the user PIN. This option differs from &#8211;change-pin in that it sets the user PIN for the first time. Once set, the user PIN can be changed using <code>&#8211;change-pin</code>.</dd></dl>
<p> <code>&#8211;change-pin, -c</code></p>
<dl>
<dt>
</dt><dd> Change the user PIN on the token</dd></dl>
<p> <code>&#8211;test, -t</code></p>
<dl>
<dt>
</dt><dd> Performs some tests on the token. This option is most useful when used with either <code>&#8211;login</code> or <code>&#8211;pin</code>.</dd></dl>
<p> <code>&#8211;show-info, -I</code></p>
<dl>
<dt>
</dt><dd> Displays general token information.</dd></dl>
<p> <code>&#8211;list-slots, -L</code></p>
<dl>
<dt>
</dt><dd> Displays a list of available slots on the token.</dd></dl>
<p> <code>&#8211;list-mechanisms, -M</code></p>
<dl>
<dt>
</dt><dd> Displays a list of mechanisms supported by the token.</dd></dl>
<p> <code>&#8211;list-objects, -O</code></p>
<dl>
<dt>
</dt><dd> Displays a list of objects.</dd></dl>
<p> <code>&#8211;sign, s</code></p>
<dl>
<dt>
</dt><dd> Sign some data.</dd></dl>
<p> <code>&#8211;hash, -h</code></p>
<dl>
<dt>
</dt><dd> Hash some data.</dd></dl>
<p> <code>&#8211;mechanism</code> <i>mechanism</i>, <code>-m</code> <i>mechanism</i></p>
<dl>
<dt>
</dt><dd> Use the specified <i>mechanism</i> for token operations. See <code>-M</code> for a list of mechanisms supported by your token.</dd></dl>
<p> <code>&#8211;keypairgen, -k</code></p>
<dl>
<dt>
</dt><dd> Generate a new key pair (public and private pair.)</dd></dl>
<p> <code>&#8211;write-object</code> <i>id</i>, <code>-w</code> <i>id</i></p>
<dl>
<dt>
</dt><dd> Write a key or certificate object to the token.</dd></dl>
<p> <code>&#8211;type</code> <i>type</i>, <code>-y</code> <i>type</i></p>
<dl>
<dt>
</dt><dd> Specify the type of object to operate on. Examples are <i>cert</i>, <i>privkey</i> and <i>pubkey</i>.</dd></dl>
<p> <code>&#8211;id</code> <i>id</i>, <code>-d</code> <i>id</i></p>
<dl>
<dt>
</dt><dd> Specify the id of the object to operate on.</dd></dl>
<p> <code>&#8211;label</code> <i>name</i>, <code>-a</code> <i>name</i></p>
<dl>
<dt>
</dt><dd> Specify the name of the object to operate on (or the token label when <code>&#8211;init-token</code> is used).</dd></dl>
<p> <code>&#8211;slot</code> <i>id</i></p>
<dl>
<dt>
</dt><dd> Specify the id of the slot to use.</dd></dl>
<p> <code>&#8211;slot-id</code> <i>name</i></p>
<dl>
<dt>
</dt><dd> Specify the name of the slot to use.</dd></dl>
<p> <code>&#8211;set-id</code> <i>id</i>, <code>-e</code> <i>id</i></p>
<dl>
<dt>
</dt><dd> Set the CKA_ID of the object.</dd></dl>
<p> <code>&#8211;attr-from</code> <i>path</i></p>
<dl>
<dt>
</dt><dd> Extract information from <i>path</i> (DER-encoded certificate file) and create the corresponding attributes when writing an object to the token. Example: the certificate subject name is used to create the CKA_SUBJECT attribute.</dd></dl>
<p> <code>&#8211;input-file</code> <i>path</i>, <code>-i</code> <i>path</i></p>
<dl>
<dt>
</dt><dd> Specify the path to a file for input.</dd></dl>
<p> <code>&#8211;output-file</code> <i>path</i>, <code>-o</code> <i>path</i></p>
<dl>
<dt>
</dt><dd> Specify the path to a file for output.</dd></dl>
<p> <code>&#8211;module</code> <i>mod</i></p>
<dl>
<dt>
</dt><dd> Specify a PKCS#11 module (or library) to load.</dd></dl>
<p> <code>&#8211;moz-cert</code> <i>path</i>, <code>-z</code> <i>path</i></p>
<dl>
<dt>
</dt><dd> Tests a Mozilla-like keypair generation and certificate request. Specify the <i>path</i> to the certificate file.</dd></dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dt>
</dt><dd> Causes <code>pkcs11-tool</code> to be more verbose. Specify this flag several times to enable debug output in the OpenSC library.</dd></dl>
<h2>SEE ALSO</h2>
<p> opensc(7) </p>
