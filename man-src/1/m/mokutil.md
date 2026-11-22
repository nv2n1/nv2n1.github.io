---

title: "mokutil(1)"
name: "mokutil"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mokutil/"
description: "mokutil – utility to manipulate machine owner keys"
---

<p> mokutil &#8211; utility to manipulate machine owner keys</p>
<h2>SYNOPSIS</h2>
<p> <code>mokutil</code> [&#8211;list-enrolled | -l]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;list-new | -N]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;list-delete | -D]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;import <i>keylist</i>| -i <i>keylist</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;delete <i>keylist</i> | -d <i>keylist</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mokx |- X])<br/>
 <code>mokutil</code> [&#8211;revoke-import]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;revoke-delete]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;export | -x]<br/>
 <code>mokutil</code> [&#8211;password | -p]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s])<br/>
 <code>mokutil</code> [&#8211;clear-password | -c]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;simple-hash | -s])<br/>
 <code>mokutil</code> [&#8211;disable-validation]<br/>
 <code>mokutil</code> [&#8211;enable-validation]<br/>
 <code>mokutil</code> [&#8211;sb-state]<br/>
 <code>mokutil</code> [&#8211;test-key <i>keyfile</i> | -t <i>keyfile</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;reset]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mok | -X])<br/>
 <code>mokutil</code> [&#8211;generate-hash=<i>password</i> | -g<i>password</i>]<br/>
 <code>mokutil</code> [&#8211;ignore-db]<br/>
 <code>mokutil</code> [&#8211;use-db]<br/>
 <code>mokutil</code> [&#8211;import-hash <i>hash</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;delete-hash <i>hash</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;([&#8211;hash-file&nbsp;<i>hashfile</i>&nbsp;| -f&nbsp;<i>hashfile</i>]&nbsp;|&nbsp;[&#8211;root-pw | -P]&nbsp;|<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&#8211;simple-hash | -s]&nbsp;|&nbsp;[&#8211;mokx | -X])<br/>
 <code>mokutil</code> [&#8211;set-verbosity (<i>true</i> | <i>false</i>)]<br/>
 <code>mokutil</code> [&#8211;pk]<br/>
 <code>mokutil</code> [&#8211;kek]<br/>
 <code>mokutil</code> [&#8211;db]<br/>
 <code>mokutil</code> [&#8211;dbx] </p>
<h2>DESCRIPTION</h2>
<p> <code>mokutil</code> is a tool to import or delete the machines owner keys (MOK) stored in the database of shim. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l, &#8211;list-enrolled</code></dt>
<dd> List the keys the already stored in the database</dd>
<dt><code>-N, &#8211;list-new</code></dt>
<dd> List the keys to be enrolled</dd>
<dt><code>-D, &#8211;list-delete</code></dt>
<dd> List the keys to be deleted</dd>
<dt><code>-i, &#8211;import</code></dt>
<dd> Collect the followed files and form a enrolling request to shim. The files must be in DER format.</dd>
<dt><code>-d, &#8211;delete</code></dt>
<dd> Collect the followed files and form a deleting request to shim. The files must be in DER format.</dd>
<dt><code>&#8211;revoke-import</code></dt>
<dd> Revoke the current import request (MokNew)</dd>
<dt><code>&#8211;revoke-delete</code></dt>
<dd> Revoke the current delete request (MokDel)</dd>
<dt><code>-x, &#8211;export</code></dt>
<dd> Export the keys stored in MokListRT</dd>
<dt><code>-p, &#8211;password</code></dt>
<dd> Setup the password for MokManager (MokPW)</dd>
<dt><code>-c, &#8211;clear-password</code></dt>
<dd> Clear the password for MokManager (MokPW)</dd>
<dt><code>&#8211;disable-validation</code></dt>
<dd> Disable the validation process in shim</dd>
<dt><code>&#8211;enrolled-validation</code></dt>
<dd> Enable the validation process in shim</dd>
<dt><code>&#8211;sb-state</code></dt>
<dd> Show SecureBoot State</dd>
<dt><code>-t, &#8211;test-key</code></dt>
<dd> Test if the key is enrolled or not</dd>
<dt><code>&#8211;reset</code></dt>
<dd> Reset MOK list</dd>
<dt><code>&#8211;generate-hash</code></dt>
<dd> Generate the password hash</dd>
<dt><code>&#8211;hash-file</code></dt>
<dd> Use the password hash from a specific file</dd>
<dt><code>-P, &#8211;root-pw</code></dt>
<dd> Use the root password hash from /etc/shadow</dd>
<dt><code>-s, &#8211;simple-hash</code></dt>
<dd> Use the old SHA256 password hash method to hash the password<br/>
 Note: &#8211;root-pw invalidates &#8211;simple-hash</dd>
<dt><code>&#8211;ignore-db</code></dt>
<dd> Tell shim to not use the keys in db to verify EFI images</dd>
<dt><code>&#8211;use-db</code></dt>
<dd> Tell shim to use the keys in db to verify EFI images (default)</dd>
<dt><code>-X, &#8211;mokx</code></dt>
<dd> Manipulate the MOK blacklist (MOKX) instead of the MOK list</dd>
<dt><code>-i, &#8211;import-hash</code></dt>
<dd> Create an enrolling request for the hash of a key in DER format. Note that this is not the password hash.</dd>
<dt><code>-d, &#8211;delete-hash</code></dt>
<dd> Create an deleting request for the hash of a key in DER format. Note that this is not the password hash.</dd>
<dt><code>&#8211;set-verbosity</code></dt>
<dd> Set the SHIM_VERBOSE to make shim more or less verbose</dd>
<dt><code>&#8211;pk</code></dt>
<dd> List the keys in the public Platform Key (PK)</dd>
<dt><code>&#8211;kek</code></dt>
<dd> List the keys in the Key Exchange Key Signature database (KEK)</dd>
<dt><code>&#8211;db</code></dt>
<dd> List the keys in the secure boot signature store (db)</dd>
<dt><code>&#8211;dbx</code></dt>
<dd> List the keys in the secure boot blacklist signature store (dbx)</dd>
</dl>
