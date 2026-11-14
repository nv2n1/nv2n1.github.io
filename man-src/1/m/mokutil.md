---
title: "mokutil(1)"
name: "mokutil"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mokutil/"
description: "mokutil – utility to manipulate machine owner keys"
---

<h2 class="name">NAME</h2>
<p> mokutil &#8211; utility to manipulate machine owner keys</p>
<h2>SYNOPSIS</h2>
<p> <code>mokutil</code> [&#8211;list-enrolled | -l]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;list-new | -N]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;list-delete | -D]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;import <i>keylist</i>| -i <i>keylist</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;delete <i>keylist</i> | -d <i>keylist</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mokx |- X])<br />
 <code>mokutil</code> [&#8211;revoke-import]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;revoke-delete]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;export | -x]<br />
 <code>mokutil</code> [&#8211;password | -p]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s])<br />
 <code>mokutil</code> [&#8211;clear-password | -c]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;simple-hash | -s])<br />
 <code>mokutil</code> [&#8211;disable-validation]<br />
 <code>mokutil</code> [&#8211;enable-validation]<br />
 <code>mokutil</code> [&#8211;sb-state]<br />
 <code>mokutil</code> [&#8211;test-key <i>keyfile</i> | -t <i>keyfile</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;reset]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mok | -X])<br />
 <code>mokutil</code> [&#8211;generate-hash=<i>password</i> | -g<i>password</i>]<br />
 <code>mokutil</code> [&#8211;ignore-db]<br />
 <code>mokutil</code> [&#8211;use-db]<br />
 <code>mokutil</code> [&#8211;import-hash <i>hash</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;delete-hash <i>hash</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mokx | -X])<br />
 <code>mokutil</code> [&#8211;set-verbosity (<i>true</i> | <i>false</i>)]<br />
 <code>mokutil</code> [&#8211;pk]<br />
 <code>mokutil</code> [&#8211;kek]<br />
 <code>mokutil</code> [&#8211;db]<br />
 <code>mokutil</code> [&#8211;dbx] </p>
<h2>DESCRIPTION</h2>
<p> <code>mokutil</code> is a tool to import or delete the machines owner keys (MOK) stored in the database of shim. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l, &#8211;list-enrolled</code></p>
<dd> List the keys the already stored in the database</p>
<dt><code>-N, &#8211;list-new</code></p>
<dd> List the keys to be enrolled</p>
<dt><code>-D, &#8211;list-delete</code></p>
<dd> List the keys to be deleted</p>
<dt><code>-i, &#8211;import</code></p>
<dd> Collect the followed files and form a enrolling request to shim. The files must be in DER format.</p>
<dt><code>-d, &#8211;delete</code></p>
<dd> Collect the followed files and form a deleting request to shim. The files must be in DER format.</p>
<dt><code>&#8211;revoke-import</code></p>
<dd> Revoke the current import request (MokNew)</p>
<dt><code>&#8211;revoke-delete</code></p>
<dd> Revoke the current delete request (MokDel)</p>
<dt><code>-x, &#8211;export</code></p>
<dd> Export the keys stored in MokListRT</p>
<dt><code>-p, &#8211;password</code></p>
<dd> Setup the password for MokManager (MokPW)</p>
<dt><code>-c, &#8211;clear-password</code></p>
<dd> Clear the password for MokManager (MokPW)</p>
<dt><code>&#8211;disable-validation</code></p>
<dd> Disable the validation process in shim</p>
<dt><code>&#8211;enrolled-validation</code></p>
<dd> Enable the validation process in shim</p>
<dt><code>&#8211;sb-state</code></p>
<dd> Show SecureBoot State</p>
<dt><code>-t, &#8211;test-key</code></p>
<dd> Test if the key is enrolled or not</p>
<dt><code>&#8211;reset</code></p>
<dd> Reset MOK list</p>
<dt><code>&#8211;generate-hash</code></p>
<dd> Generate the password hash</p>
<dt><code>&#8211;hash-file</code></p>
<dd> Use the password hash from a specific file</p>
<dt><code>-P, &#8211;root-pw</code></p>
<dd> Use the root password hash from /etc/shadow</p>
<dt><code>-s, &#8211;simple-hash</code></p>
<dd> Use the old SHA256 password hash method to hash the password<br />
 Note: &#8211;root-pw invalidates &#8211;simple-hash</p>
<dt><code>&#8211;ignore-db</code></p>
<dd> Tell shim to not use the keys in db to verify EFI images</p>
<dt><code>&#8211;use-db</code></p>
<dd> Tell shim to use the keys in db to verify EFI images (default)</p>
<dt><code>-X, &#8211;mokx</code></p>
<dd> Manipulate the MOK blacklist (MOKX) instead of the MOK list</p>
<dt><code>-i, &#8211;import-hash</code></p>
<dd> Create an enrolling request for the hash of a key in DER format. Note that this is not the password hash.</p>
<dt><code>-d, &#8211;delete-hash</code></p>
<dd> Create an deleting request for the hash of a key in DER format. Note that this is not the password hash.</p>
<dt><code>&#8211;set-verbosity</code></p>
<dd> Set the SHIM_VERBOSE to make shim more or less verbose</p>
<dt><code>&#8211;pk</code></p>
<dd> List the keys in the public Platform Key (PK)</p>
<dt><code>&#8211;kek</code></p>
<dd> List the keys in the Key Exchange Key Signature database (KEK)</p>
<dt><code>&#8211;db</code></p>
<dd> List the keys in the secure boot signature store (db)</p>
<dt><code>&#8211;dbx</code></p>
<dd> List the keys in the secure boot blacklist signature store (dbx)</p>
<dt>
<dd></dl>
<h2>Index</h2>
