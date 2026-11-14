---
title: "sn(1)"
name: "sn"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sn/"
description: "sn – Digitally sign/verify/compare strongnames on CLR assemblies."
---

<h2>NAME</h2>
<p> sn &#8211; Digitally sign/verify/compare strongnames on CLR assemblies.</p>
<h2>SYNOPSIS</h2>
<p> <code>sn [-q | -quiet] [options] [parameters]</code></p>
<h2>DESCRIPTION</h2>
<p> Digitally sign, verify or compare CLR assemblies using strongnames. </p>
<p> You can use the sn command to create &quot;snk files&quot; using the -k option described below.</p>
<h2>CONFIGURATION OPTIONS</h2>
<p> Configuration options are stored in the machine.config configuration file under /configuration/strongNames.</p>
<dl>
<dt><i>-c provider</i></p>
<dd> Change the default CSP (Crypto Service Provider). Currently not supported in Mono.</p>
<dt><i>-m [y|n]</i></p>
<dd> Use a machine [y] key container or a user [n] key container. Currently not supported in Mono.</p>
<dt><i>-Vl</i></p>
<dd> List the verification options. The list is kept under /configuration/ strongNames/verificationSettings in machine.config.</p>
<dt><i>-Vr assembly [userlist]</i></p>
<dd> Exempt the specified assembly from verification for the specified user list. Currently not supported by sn. You must edit machine.config manually if you require this.</p>
<dt><i>-Vu assembly</i></p>
<dd> Remove the exemption entry for the specified assembly. Currently not supported by sn, you must edit machine.config manually if you require this.</p>
<dt><i>-Vx</i></p>
<dd> Remove all exemptions entries. Currently not supported by sn, you must edit machine.config manually if you require this.</dl>
<h2>CSP RELATED OPTIONS</h2>
<dl>
<dt><i>-d container</i></p>
<dd> Delete the keypair present in the specified key container.</p>
<dt><i>-i keypair.snk container</i></p>
<dd> Import the specified strongname file into the specified container.</p>
<dt><i>-pc container publickey</i></p>
<dd> Export the public key from the specified CSP container to the specified file.</dl>
<h2>CONVERSION OPTIONS</h2>
<dl>
<dt><i>-e assembly output.pub</i></p>
<dd> Export the assembly public key to the specified output file.</p>
<dt><i>-p keypair.snk output.pub</i></p>
<dd> Export the public key from the specified strongname key file (SNK) or from a PKCS#12/PFX password protected file to the specified output file.</p>
<dt><i>-o input output.txt</i></p>
<dd> Convert the input file to a CSV file (using decimal).</p>
<dt><i>-oh input output.txt</i></p>
<dd> Convert the input file to a CSV file (using hexadecimal).</dl>
<h2>STRONGNAME SIGNING OPTIONS</h2>
<dl>
<dt><i>-D assembly1 assembly2</i></p>
<dd> Compare if assembly1 and assembly2 are the same except for their signature. This is done by comparing the hash of the metadata of both assemblies.</p>
<dt><i>-k [size] keypair.snk</i></p>
<dd> Create a new strongname keypair in the specified file. The default key length is 1024 bits and MUST ALWAYS be used when signing 1.x assemblies. Any value from 384 to 16384 bits (in increments of 8 bits) is a valid key length to sign 2.x assemblies. To ensure maximum compatibility you may want to continue using 1024 bits keys. Note that there&#8217;s no good reason, even if it&#8217;s possible, to use length lesser than 1024 bits.</p>
<dt><i>-R assembly keypair.snk</i></p>
<dd> Re-sign the specified assembly using the specified strongname keypair file (SNK) or a PKCS#12/PFX password protected file. You can only sign an assembly with the private key that matches the public key inside the assembly (unless it&#8217;s public key token has been remapped in machine.config).</p>
<dt><i>-Rc assembly container</i></p>
<dd> Re-sign the specified assembly using the specified strongname container.</p>
<dt><i>-t file</i></p>
<dd> Show the public key token from the specified file.</p>
<dt><i>-tp file</i></p>
<dd> Show the public key and the public key token from the specified file.</p>
<dt><i>-T assembly</i></p>
<dd> Show the public key token from the specified assembly.</p>
<dt><i>-Tp assembly</i></p>
<dd> Show the public key and the public key token from the specified assembly.</p>
<dt><i>-v assembly</i></p>
<dd> Verify the specified assembly signature.</p>
<dt><i>-vf assembly</i></p>
<dd> Verify the specified assembly signature (even if disabled).</dl>
<h2>HELP OPTIONS</h2>
<dl>
<dt><i>-h, -?</i></p>
<dd> Display basic help about this tool.</p>
<dt><i>-h config, -? config</i></p>
<dd> Display configuration related help about this tool.</p>
<dt><i>-h csp, -? csp</i></p>
<dd> Display Cryptographic Service Provider related help about this tool.</p>
<dt><i>-h convert, -? convert</i></p>
<dd> Display conversion related help about this tool.</p>
<dt><i>-h sn, -? sn</i></p>
<dd> Display strongname related help about this tool.</dl>
<h2>CONFIGURATION FILE</h2>
<dl>
<dt>Strongnames configuration is kept in &quot;machine.config&quot; file. Currently two</p>
<dd> features can be configured.</p>
<dt><i>/configuration/strongNames/pubTokenMapping</i></p>
<dd> This mechanism lets Mono remap a public key token, like the ECMA token, to another public key for verification. This is useful in two scenarios. First, assemblies signed with the &quot;ECMA key&quot; need to be verified by the &quot;runtime&quot; key (as the ECMA key isn&#8217;t a public key). Second, many assemblies are signed with private keys that Mono can&#8217;t use (e.g. System.Security.dll assembly). A new key cannot be used because it should change the strongname (a new key pair would have a new public key which would produce a new token). Public key token remapping is the solution for both problems. Each token must be configured in a &quot;map&quot; entry similar to this one: &lt;map Token=&quot;b77a5c561934e089&quot; PublicKey=&quot;00&#8230;&quot; /&gt;</p>
<dt><i>/configuration/strongNames/verificationSettings</i></p>
<dd> It is often useful during development to use delay signed assemblies. Normally* the runtime wouldn&#8217;t allow delay-signed assemblies to be loaded. This feature allows some delay-signed assemblies (based on their public key token, optionally assembly name and user name) to be used like they were fully signed assemblies. [*] Note that Mono 1.0 &quot;runtime&quot; doesn&#8217;t validate strongname signatures so this option shouldn&#8217;t be required in most scenarios.</dl>
<h2>AUTHOR</h2>
<p> Written by Sebastien Pouliot</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003 Motus Technologies. Copyright (C) 2004 Novell. Released under BSD license.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-secutil/">secutil</a>(1)</code> </p>
<h2>Index</h2>
