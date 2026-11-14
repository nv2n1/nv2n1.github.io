---
title: "eurephiadm-certs(7)"
name: "eurephiadm-certs"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-certs/"
description: "eurephiadm certs – Certificate management for eurephia"
---

<p><code>eurephiadm certs</code> &#8211; Certificate management for <code>eurephia</code></p>
<h2>Description</h2>
<p>Available modes for the certificate command are:</p>
<dl>
<dt><code>-A</code> | <code>&#8211;add</code></p>
<dd>Register a new certificate</p>
<dt><code>-D</code> | <code>&#8211;delete</code></p>
<dd>Delete a registered certificate</p>
<dt><code>-l</code> | <code>&#8211;list</code></p>
<dd>List all registered certificates</p>
<dt> <code>-h</code> | <code>&#8211;help</code> &lt;mode&gt;</p>
<dd>
<dd>Help about a specific mode</dl>
<h2>List Mode</h2>
<p>The list mode will list all registered certificates. It accepts one parameter:</p>
<dl>
<dt><code>-S</code> | <code>&#8211;sort</code> &lt;sort key&gt;</p>
<dd>Decide the sort order of the certificate list</dl>
<p> Available sort keys are:</p>
<dl>
<dd><code>certid</code><br />
&nbsp;<wbr>Numeric certificate ID</p>
<dd><code>depth</code><br />
&nbsp;<wbr>Certificate depth</p>
<dd><code>digest</code><br />
&nbsp;<wbr>Certificate SHA1 digest</p>
<dd><code>cname</code><br />
&nbsp;<wbr>Certificate Common Name field</p>
<dd><code>org</code><br />
&nbsp;<wbr>Certificate organisation field</p>
<dd><code>email</code><br />
&nbsp;<wbr>Certificate e-mail address field</p>
<dd><code>registered</code><br />
&nbsp;<wbr>When the certificate was registered in eurephia.</dl>
<h2>Add Mode</h2>
<p>The add mode will register a new certificate.</p>
<dl>
<dt><code>-d</code> | <code>&#8211;depth</code></p>
<dd>Certificate depth, required.</p>
<dt><code>-D</code> | <code>&#8211;digest</code></p>
<dd>SHA1 fingerprint/digest of the new certificate</p>
<dt><code>-C</code> | <code>&#8211;common-name</code></p>
<dd>Common name (CN) field of the certificate</p>
<dt><code>-O</code> | <code>&#8211;organisation</code></p>
<dd>Organisation (O) field of the certificate</p>
<dt><code>-E</code> | <code>&#8211;email</code></p>
<dd>e-mail address (emailAddress) of the certificate</dl>
<p> Usually the certificate depth value needs to be 0, if you are registering user account certificates. CA certificates usually have a value bigger than 0. </p>
<p> If you have the certificate file available, you can use the following options to retrieve the needed information directly from a certificate file.</p>
<dl>
<dt><code>-f</code> | <code>&#8211;certfile</code></p>
<dd>File name of the certificate file.</p>
<dt><code>-p</code> | <code>&#8211;pkcs12</code></p>
<dd>If the file is in PKCS#12 format.</dl>
<p> The default format is PEM format, unless <code>&#8211;pkcs12</code> is given. These two options cannot be used together with <code>-D</code>, <code>-C</code>, <code>-O</code> or <code>-E</code>. But the certificate depth must be given to indicate the certificate depth.</p>
<h2>Delete Mode</h2>
<p>The delete mode will remove a certificate from the certificate database.</p>
<dl>
<dt><code>-i</code> | <code>&#8211;certid</code></p>
<dd>Indicates a unique certificate ID</p>
<dt><code>-d</code> | <code>&#8211;digest</code></p>
<dd>A unique SHA1 fingerprint/digest value</p>
<dt><code>-C</code> | <code>&#8211;common-name</code></p>
<dd>Common Name (CN) field of a certificate</p>
<dt><code>-O</code> | <code>&#8211;organisation</code></p>
<dd>Organisation (O) field of a certificate</p>
<dt><code>-E</code> | <code>&#8211;email</code></p>
<dd>e-mail address (emailAddress) of a certificate</dl>
<p> You can use any of these parameters to indicate a search criteria for the certificate (or certificates) you want to delete. You will be provided with a list over certificates which matches your search criteria and you will need to approve the deletion of the matching certificate(s).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm-users/">eurephiadm-users</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-usercerts/">eurephiadm-usercerts</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
