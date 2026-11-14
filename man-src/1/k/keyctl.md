---
title: "keyctl(1)"
name: "keyctl"
section: "1"
letter: "k"
url: "/docs/linux/man/1-keyctl/"
description: "keyctl – key management facility control"
---

<h2 class="name">NAME</h2>
<p> keyctl &#8211; key management facility control </p>
<h2>SYNOPSIS</h2>
<p> <code>keyctl</code> &#8211;version<br />
 <code>keyctl</code> show [-x] [&lt;keyring&gt;]<br />
 <code>keyctl</code> add &lt;type&gt; &lt;desc&gt; &lt;data&gt; &lt;keyring&gt;<br />
 <code>keyctl</code> padd &lt;type&gt; &lt;desc&gt; &lt;keyring&gt;<br />
 <code>keyctl</code> request &lt;type&gt; &lt;desc&gt; [&lt;dest_keyring&gt;]<br />
 <code>keyctl</code> request2 &lt;type&gt; &lt;desc&gt; &lt;info&gt; [&lt;dest_keyring&gt;]<br />
 <code>keyctl</code> prequest2 &lt;type&gt; &lt;desc&gt; [&lt;dest_keyring&gt;]<br />
 <code>keyctl</code> update &lt;key&gt; &lt;data&gt;<br />
 <code>keyctl</code> pupdate &lt;key&gt;<br />
 <code>keyctl</code> newring &lt;name&gt; &lt;keyring&gt;<br />
 <code>keyctl</code> revoke &lt;key&gt;<br />
 <code>keyctl</code> clear &lt;keyring&gt;<br />
 <code>keyctl</code> link &lt;key&gt; &lt;keyring&gt;<br />
 <code>keyctl</code> unlink &lt;key&gt; [&lt;keyring&gt;]<br />
 <code>keyctl</code> search &lt;keyring&gt; &lt;type&gt; &lt;desc&gt; [&lt;dest_keyring&gt;]<br />
 <code>keyctl</code> restrict_keyring &lt;keyring&gt; [&lt;type&gt; [&lt;restriction&gt;]]<br />
 <code>keyctl</code> read &lt;key&gt;<br />
 <code>keyctl</code> pipe &lt;key&gt;<br />
 <code>keyctl</code> print &lt;key&gt;<br />
 <code>keyctl</code> list &lt;keyring&gt;<br />
 <code>keyctl</code> rlist &lt;keyring&gt;<br />
 <code>keyctl</code> describe &lt;keyring&gt;<br />
 <code>keyctl</code> rdescribe &lt;keyring&gt; [sep]<br />
 <code>keyctl</code> chown &lt;key&gt; &lt;uid&gt;<br />
 <code>keyctl</code> chgrp &lt;key&gt; &lt;gid&gt;<br />
 <code>keyctl</code> setperm &lt;key&gt; &lt;mask&gt;<br />
 <code>keyctl</code> new_session<br />
 <code>keyctl</code> session<br />
 <code>keyctl</code> session &#8211; [&lt;prog&gt; &lt;arg1&gt; &lt;arg2&gt; &#8230;]<br />
 <code>keyctl</code> session &lt;name&gt; [&lt;prog&gt; &lt;arg1&gt; &lt;arg2&gt; &#8230;]<br />
 <code>keyctl</code> instantiate &lt;key&gt; &lt;data&gt; &lt;keyring&gt;<br />
 <code>keyctl</code> pinstantiate &lt;key&gt; &lt;keyring&gt;<br />
 <code>keyctl</code> negate &lt;key&gt; &lt;timeout&gt; &lt;keyring&gt;<br />
 <code>keyctl</code> reject &lt;key&gt; &lt;timeout&gt; &lt;error&gt; &lt;keyring&gt;<br />
 <code>keyctl</code> timeout &lt;key&gt; &lt;timeout&gt;<br />
 <code>keyctl</code> security &lt;key&gt;<br />
 <code>keyctl</code> reap [-v]<br />
 <code>keyctl</code> purge &lt;type&gt;<br />
 <code>keyctl</code> purge [-i] [-p] &lt;type&gt; &lt;desc&gt;<br />
 <code>keyctl</code> purge -s &lt;type&gt; &lt;desc&gt;<br />
 <code>keyctl</code> get_persistent &lt;keyring&gt; [&lt;uid&gt;]<br />
 <code>keyctl</code> dh_compute &lt;private&gt; &lt;prime&gt; &lt;base&gt;<br />
 <code>keyctl</code> dh_compute_kdf &lt;private&gt; &lt;prime&gt; &lt;base&gt; &lt;output_length&gt; &lt;hash_type&gt;<br />
 <code>keyctl</code> dh_compute_kdf_oi &lt;private&gt; &lt;prime&gt; &lt;base&gt; &lt;output_length&gt; &lt;hash_type&gt;<br />
 <code>keyctl</code> pkey_query &lt;key&gt; &lt;pass&gt; [k=v]*<br />
 <code>keyctl</code> pkey_encrypt &lt;key&gt; &lt;pass&gt; &lt;datafile&gt; [k=v]* &gt;&lt;encfile&gt;<br />
 <code>keyctl</code> pkey_decrypt &lt;key&gt; &lt;pass&gt; &lt;encfile&gt; [k=v]* &gt;&lt;datafile&gt;<br />
 <code>keyctl</code> pkey_sign &lt;key&gt; &lt;pass&gt; &lt;datafile&gt; [k=v]* &gt;&lt;sigfile&gt;<br />
 <code>keyctl</code> pkey_decrypt &lt;key&gt; &lt;pass&gt; &lt;datafile&gt; &lt;sigfile&gt; [k=v]*</p>
<h2>DESCRIPTION</h2>
<p> This program is used to control the key management facility in various ways using a variety of subcommands.</p>
<h2>KEY IDENTIFIERS</h2>
<p> The key identifiers passed to or returned from keyctl are, in general, positive integers. There are, however, some special values with special meanings that can be passed as arguments:</p>
<dl>
<dt>No key: <code>0</code></p>
<dd>
<dt>Thread keyring: <code>@t</code> or <code>-1</code></p>
<dd> Each thread may have its own keyring. This is searched first, before all others. The thread keyring is replaced by (v)fork, exec and clone.</p>
<dt>Process keyring: <code>@p</code> or <code>-2</code></p>
<dd> Each process (thread group) may have its own keyring. This is shared between all members of a group and will be searched after the thread keyring. The process keyring is replaced by (v)fork and exec.</p>
<dt>Session keyring: <code>@s</code> or <code>-3</code></p>
<dd> Each process subscribes to a session keyring that is inherited across (v)fork, exec and clone. This is searched after the process keyring. Session keyrings can be named and an extant keyring can be joined in place of a process&#8217;s current session keyring.</p>
<dt>User specific keyring: <code>@u</code> or <code>-4</code></p>
<dd> This keyring is shared between all the processes owned by a particular user. It isn&#8217;t searched directly, but is normally linked to from the session keyring.</p>
<dt>User default session keyring: <code>@us</code> or <code>-5</code></p>
<dd> This is the default session keyring for a particular user. Login processes that change to a particular user will bind to this session until another session is set.</p>
<dt>Group specific keyring: <code>@g</code> or <code>-6</code></p>
<dd> This is a place holder for a group specific keyring, but is not actually implemented yet in the kernel.</p>
<dt>Assumed request_key authorisation key: <code>@a</code> or <code>-7</code></p>
<dd> This selects the authorisation key provided to the <code>request_key</code>() helper to permit it to access the callers keyrings and instantiate the target key.</p>
<dt>Keyring by name: <code>%:&lt;name&gt;</code></p>
<dd> A named keyring. This will be searched for in the process&#8217;s keyrings and in <i>/proc/keys</i>.</p>
<dt>Key by name: <code>%&lt;type&gt;:&lt;name&gt;</code></p>
<dd> A named key of the given type. This will be searched for in the process&#8217;s keyrings and in <i>/proc/keys</i>.</dl>
<h2>COMMAND SYNTAX</h2>
<p> Any non-ambiguous shortening of a command name may be used in lieu of the full command name. This facility should not be used in scripting as new commands may be added in future that then cause ambiguity.</p>
<h3>Display the package version number</h3>
<p> <code>keyctl &#8211;version</code> </p>
<p> This command prints the package version number and build date and exits: </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl --version
keyctl from keyutils-1.5.3 (Built 2011-08-24)
</pre>
</dl>
<h3>Show process keyrings</h3>
<p> <code>keyctl show [-x] [&lt;keyring&gt;]</code> </p>
<p> By default this command recursively shows what keyrings a process is subscribed to and what keys and keyrings they contain. If a keyring is specified then that keyring will be dumped instead. If <code>-x</code> is specified then the keyring IDs will be dumped in hex instead of decimal.</p>
<h3>Add a key to a keyring</h3>
<p> <code>keyctl add</code> &lt;type&gt; &lt;desc&gt; &lt;data&gt; &lt;keyring&gt;<br />
 <code>keyctl padd</code> &lt;type&gt; &lt;desc&gt; &lt;keyring&gt; </p>
<p> This command creates a key of the specified type and description; instantiates it with the given data and attaches it to the specified keyring. It then prints the new key&#8217;s ID on stdout: </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl add user mykey stuff @u
26
</pre>
</dl>
<p> The <code>padd</code> variant of the command reads the data from stdin rather than taking it from the command line: </p>
<dl>
<dt>
<dd> $ echo -n stuff | keyctl padd user mykey @u 26</dl>
<h3>Request a key</h3>
<p> <code>keyctl request</code> &lt;type&gt; &lt;desc&gt; [&lt;dest_keyring&gt;]<br />
 <code>keyctl request2</code> &lt;type&gt; &lt;desc&gt; &lt;info&gt; [&lt;dest_keyring&gt;]<br />
 <code>keyctl prequest2</code> &lt;type&gt; &lt;desc&gt; [&lt;dest_keyring&gt;] </p>
<p> These three commands request the lookup of a key of the given type and description. The process&#8217;s keyrings will be searched, and if a match is found the matching key&#8217;s ID will be printed to stdout; and if a destination keyring is given, the key will be added to that keyring also. </p>
<p> If there is no key, the first command will simply return the error ENOKEY and fail. The second and third commands will create a partial key with the type and description, and call out to <i>/sbin/request-key</i> with that key and the extra information supplied. This will then attempt to instantiate the key in some manner, such that a valid key is obtained. </p>
<p> The third command is like the second, except that the callout information is read from stdin rather than being passed on the command line. </p>
<p> If a valid key is obtained, the ID will be printed and the key attached as if the original search had succeeded. </p>
<p> If there wasn&#8217;t a valid key obtained, a temporary negative key will be attached to the destination keyring if given and the error &quot;Requested key not available&quot; will be given. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl request2 user debug:hello wibble
23
$ echo -n wibble | keyctl prequest2 user debug:hello
23
$ keyctl request user debug:hello
23
</pre>
</dl>
<h3>Update a key</h3>
<p> <code>keyctl update</code> &lt;key&gt; &lt;data&gt;<br />
 <code>keyctl pupdate</code> &lt;key&gt; </p>
<p> This command replaces the data attached to a key with a new set of data. If the type of the key doesn&#8217;t support update then error &quot;Operation not supported&quot; will be returned. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl update 23 zebra
</pre>
</dl>
<p> The <code>pupdate</code> variant of the command reads the data from stdin rather than taking it from the command line: </p>
<dl>
<dt>
<dd>
<pre>
$ echo -n zebra | keyctl pupdate 23
</pre>
</dl>
<h3>Create a keyring</h3>
<p> <code>keyctl newring</code> &lt;name&gt; &lt;keyring&gt; </p>
<p> This command creates a new keyring of the specified name and attaches it to the specified keyring. The ID of the new keyring will be printed to stdout if successful. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl newring squelch @us
27
</pre>
</dl>
<h3>Revoke a key</h3>
<p> <code>keyctl revoke</code> &lt;key&gt; </p>
<p> This command marks a key as being revoked. Any further operations on that key (apart from unlinking it) will return error &quot;Key has been revoked&quot;. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl revoke 26
$ keyctl describe 26
keyctl_describe: Key has been revoked
</pre>
</dl>
<h3>Clear a keyring</h3>
<p> <code>keyctl clear</code> &lt;keyring&gt; </p>
<p> This command unlinks all the keys attached to the specified keyring. Error &quot;Not a directory&quot; will be returned if the key specified is not a keyring. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl clear 27
</pre>
</dl>
<h3>Link a key to a keyring</h3>
<p> <code>keyctl link</code> &lt;key&gt; &lt;keyring&gt; </p>
<p> This command makes a link from the key to the keyring if there&#8217;s enough capacity to do so. Error &quot;Not a directory&quot; will be returned if the destination is not a keyring. Error &quot;Permission denied&quot; will be returned if the key doesn&#8217;t have link permission or the keyring doesn&#8217;t have write permission. Error &quot;File table overflow&quot; will be returned if the keyring is full. Error &quot;Resource deadlock avoided&quot; will be returned if an attempt was made to introduce a recursive link. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl link 23 27
$ keyctl link 27 27
keyctl_link: Resource deadlock avoided
</pre>
</dl>
<h3>Unlink a key from a keyring or the session keyring tree</h3>
<p> <code>keyctl unlink</code> &lt;key&gt; [&lt;keyring&gt;] </p>
<p> If the keyring is specified, this command removes a link to the key from the keyring. Error &quot;Not a directory&quot; will be returned if the destination is not a keyring. Error &quot;Permission denied&quot; will be returned if the keyring doesn&#8217;t have write permission. Error &quot;No such file or directory&quot; will be returned if the key is not linked to by the keyring. </p>
<p> If the keyring is not specified, this command performs a depth-first search of the session keyring tree and removes all the links to the nominated key that it finds (and that it is permitted to remove). It prints the number of successful unlinks before exiting. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl unlink 23 27
</pre>
</dl>
<h3>Search a keyring</h3>
<p> <code>keyctl search</code> &lt;keyring&gt; &lt;type&gt; &lt;desc&gt; [&lt;dest_keyring&gt;] </p>
<p> This command non-recursively searches a keyring for a key of a particular type and description. If found, the ID of the key will be printed on stdout and the key will be attached to the destination keyring if present. Error &quot;Requested key not available&quot; will be returned if the key is not found. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl search @us user debug:hello
23
$ keyctl search @us user debug:bye
keyctl_search: Requested key not available
</pre>
</dl>
<h3>Restrict a keyring</h3>
<p> <code>keyctl restrict_keyring</code> &lt;keyring&gt; [&lt;type&gt; [&lt;restriction&gt;]] </p>
<p> This command limits the linkage of keys to the given keyring using a provided restriction scheme. The scheme is associated with a given key type, with further details provided in the restriction option string. Options typically contain a restriction name possibly followed by key ids or other data relevant to the restriction. If no restriction scheme is provided, the keyring will reject all links. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl restrict_keyring $1 asymmetric builtin_trusted
</dl>
</pre>
<h3>Read a key</h3>
<p> <code>keyctl read</code> &lt;key&gt;<br />
 <code>keyctl pipe</code> &lt;key&gt;<br />
 <code>keyctl print</code> &lt;key&gt; </p>
<p> These commands read the payload of a key. &quot;read&quot; prints it on stdout as a hex dump, &quot;pipe&quot; dumps the raw data to stdout and &quot;print&quot; dumps it to stdout directly if it&#8217;s entirely printable or as a hexdump preceded by &quot;:hex:&quot; if not. </p>
<p> If the key type does not support reading of the payload, then error &quot;Operation not supported&quot; will be returned. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl read 26
1 bytes of data in key:
62
$ keyctl print 26
b
$ keyctl pipe 26
$
</pre>
</dl>
<h3>List a keyring</h3>
<p> <code>keyctl list</code> &lt;keyring&gt;<br />
 <code>keyctl rlist</code> &lt;keyring&gt; </p>
<p> These commands list the contents of a key as a keyring. &quot;list&quot; pretty prints the contents and &quot;rlist&quot; just produces a space-separated list of key IDs. </p>
<p> No attempt is made to check that the specified keyring is a keyring. </p>
<dl>
<dt>
<dd>
<pre><code>
$ keyctl list @us 2 keys in keyring : 22 : vrwsl-- -- -- -- --4043 - 1 keyring : _uid .4043 23 : vrwsl-- -- -- -- --4043 4043 user : debug : hello
                                                                                                                                                 $ keyctl rlist @us 22 23
</code></pre>
</dl>
<h3>Describe a key</h3>
<p> <code>keyctl describe</code> &lt;keyring&gt;<br />
 <code>keyctl rdescribe</code> &lt;keyring&gt; [sep] </p>
<p> These commands fetch a description of a keyring. &quot;describe&quot; pretty prints the description in the same fashion as the &quot;list&quot; command; &quot;rdescribe&quot; prints the raw data returned from the kernel. </p>
<dl>
<dt>
<dd>
$ keyctl describe @us &#8211; 5 : vrwsl&#8211; &#8212; &#8212; &#8212; &#8211;4043 &#8211; 1 keyring : _uid_ses .4043 $ keyctl rdescribe @us keyring;<br />
4043;<br />
&#8211; 1;<br />
3f1f0000;<br />
_uid_ses .4043
</dl>
<p> The raw string is &quot;&lt;type&gt;;&lt;uid&gt;;&lt;gid&gt;;&lt;perms&gt;;&lt;description&gt;&quot;, where <i>uid</i> and <i>gid</i> are the decimal user and group IDs, <i>perms</i> is the permissions mask in hex, <i>type</i> and <i>description</i> are the type name and description strings (neither of which will contain semicolons).</p>
<h3>Change the access controls on a key</h3>
<p> <code>keyctl chown</code> &lt;key&gt; &lt;uid&gt;<br />
 <code>keyctl chgrp</code> &lt;key&gt; &lt;gid&gt; </p>
<p> These two commands change the UID and GID associated with evaluating a key&#8217;s permissions mask. The UID also governs which quota a key is taken out of. </p>
<p> The chown command is not currently supported; attempting it will earn the error &quot;Operation not supported&quot; at best. </p>
<p> For non-superuser users, the GID may only be set to the process&#8217;s GID or a GID in the process&#8217;s groups list. The superuser may set any GID it likes. </p>
<dl>
<dt>
<dd>
<pre>
$ sudo keyctl chown 27 0
keyctl_chown: Operation not supported
$ sudo keyctl chgrp 27 0
</pre>
</dl>
<h3>Set the permissions mask on a key</h3>
<p> <code>keyctl setperm</code> &lt;key&gt; &lt;mask&gt; </p>
<p> This command changes the permission control mask on a key. The mask may be specified as a hex number if it begins &quot;0x&quot;, an octal number if it begins &quot;0&quot; or a decimal number otherwise. </p>
<p> The hex numbers are a combination of: </p>
<dl>
<dt>
<dd>
Possessor UID GID Other Permission Granted == == == == == == == == == == == == == == == == == == == == == == == == ==<br />
    01000000 00010000 00000100 00000001 View 02000000 00020000 00000200 00000002 Read 04000000 00040000 00000400 00000004 Write 08000000 00080000 00000800 00000008 Search 10000000 00100000 00001000 00000010 Link 20000000 00200000 00002000 00000020 Set Attribute 3f000000 003f0000 00003f00 0000003f All
</dl>
<p> <i>View</i> permits the type, description and other parameters of a key to be viewed. </p>
<p> <i>Read</i> permits the payload (or keyring list) to be read if supported by the type. </p>
<p> <i>Write</i> permits the payload (or keyring list) to be modified or updated. </p>
<p> <i>Search</i> on a key permits it to be found when a keyring to which it is linked is searched. </p>
<p> <i>Link</i> permits a key to be linked to a keyring. </p>
<p> <i>Set Attribute</i> permits a key to have its owner, group membership, permissions mask and timeout changed. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl setperm 27 0x1f1f1f00
</pre>
</dl>
<h3>Start a new session with fresh keyrings</h3>
<p> <code>keyctl session</code><br />
 <code>keyctl session</code> &#8211; [&lt;prog&gt; &lt;arg1&gt; &lt;arg2&gt; &#8230;]<br />
 <code>keyctl session</code> &lt;name&gt; [&lt;prog&gt; &lt;arg1&gt; &lt;arg2&gt; &#8230;] </p>
<p> These commands join or create a new keyring and then run a shell or other program with that keyring as the session key. </p>
<p> The variation with no arguments just creates an anonymous session keyring and attaches that as the session keyring; it then exec&#8217;s $SHELL. </p>
<p> The variation with a dash in place of a name creates an anonymous session keyring and attaches that as the session keyring; it then exec&#8217;s the supplied command, or $SHELL if one isn&#8217;t supplied. </p>
<p> The variation with a name supplied creates or joins the named keyring and attaches that as the session keyring; it then exec&#8217;s the supplied command, or $SHELL if one isn&#8217;t supplied. </p>
<dl>
<dt>
<dd>
<pre><code>
$ keyctl rdescribe @s
    keyring;
4043;
- 1;
3f1f0000;
_uid_ses .4043 $ keyctl session
    Joined session keyring : 28 $ keyctl rdescribe @s
        keyring;
4043;
4043;
3f1f0000;
_ses .24082 $ keyctl session -
    Joined session keyring : 29 $ keyctl rdescribe @s
        keyring;
4043;
4043;
3f1f0000;
_ses .24139 $ keyctl session - keyctl rdescribe @s
                                   Joined session keyring : 30 keyring;
4043;
4043;
3f1f0000;
_ses .24185 $ keyctl session fish
    Joined session keyring : 34 $ keyctl rdescribe @s
        keyring;
4043;
4043;
3f1f0000;
fish
    $ keyctl session fish keyctl rdesc @s
        Joined session keyring : 35 keyring;
4043;
4043;
3f1f0000;
fish
</code></pre>
</dl>
<h3>Instantiate a key</h3>
<p> <code>keyctl instantiate</code> &lt;key&gt; &lt;data&gt; &lt;keyring&gt;<br />
 <code>keyctl pinstantiate</code> &lt;key&gt; &lt;keyring&gt;<br />
 <code>keyctl negate</code> &lt;key&gt; &lt;timeout&gt; &lt;keyring&gt;<br />
 <code>keyctl reject</code> &lt;key&gt; &lt;timeout&gt; &lt;error&gt; &lt;keyring&gt; </p>
<p> These commands are used to attach data to a partially set up key (as created by the kernel and passed to <i>/sbin/request-key</i>). &quot;instantiate&quot; marks a key as being valid and attaches the data as the payload. &quot;negate&quot; and &quot;reject&quot; mark a key as invalid and sets a timeout on it so that it&#8217;ll go away after a while. This prevents a lot of quickly sequential requests from slowing the system down overmuch when they all fail, as all subsequent requests will then fail with error &quot;Requested key not found&quot; (if negated) or the specified error (if rejected) until the negative key has expired. </p>
<p> Reject&#8217;s error argument can either be a UNIX error number or one of &#8216;<code>rejected</code>&#8216;, &#8216;<code>expired</code>&#8216; or &#8216;<code>revoked</code>&#8216;. </p>
<p> The newly instantiated key will be attached to the specified keyring. </p>
<p> These commands may only be run from the program run by request-key &#8211; a special authorisation key is set up by the kernel and attached to the request-key&#8217;s session keyring. This special key is revoked once the key to which it refers has been instantiated one way or another. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl instantiate $1 &quot;Debug $3&quot; $4
$ keyctl negate $1 30 $4
$ keyctl reject $1 30 64 $4
</pre>
</dl>
<p> The <code>pinstantiate</code> variant of the command reads the data from stdin rather than taking it from the command line: </p>
<dl>
<dt>
<dd>
<pre>
$ echo -n &quot;Debug $3&quot; | keyctl pinstantiate $1 $4
</pre>
</dl>
<h3>Set the expiry time on a key</h3>
<p> <code>keyctl timeout</code> &lt;key&gt; &lt;timeout&gt; </p>
<p> This command is used to set the timeout on a key, or clear an existing timeout if the value specified is zero. The timeout is given as a number of seconds into the future. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl timeout $1 45
</pre>
</dl>
<h3>Retrieve a key&#8217;s security context</h3>
<p> <code>keyctl security</code> &lt;key&gt; </p>
<p> This command is used to retrieve a key&#8217;s LSM security context. The label is printed on stdout. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl security @s
unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
</pre>
</dl>
<h3>Give the parent process a new session keyring</h3>
<p> <code>keyctl new_session</code> </p>
<p> This command is used to give the invoking process (typically a shell) a new session keyring, discarding its old session keyring. </p>
<dl>
<dt>
<dd>
<pre>
$  keyctl session foo
Joined session keyring: 723488146
$  keyctl show
Session Keyring
       -3 --alswrv      0     0  keyring: foo
$  keyctl new_session
490511412
$  keyctl show
Session Keyring
       -3 --alswrv      0     0  keyring: _ses
</pre>
</dl>
<p> Note that this affects the <i>parent</i> of the process that invokes the system call, and so may only affect processes with matching credentials. Furthermore, the change does not take effect till the parent process next transitions from kernel space to user space &#8211; typically when the <code>wait</code>() system call returns.</p>
<h3>Remove dead keys from the session keyring tree</h3>
<p> <code>keyctl reap</code> </p>
<p> This command performs a depth-first search of the caller&#8217;s session keyring tree and attempts to unlink any key that it finds that is inaccessible due to expiry, revocation, rejection or negation. It does not attempt to remove live keys that are unavailable simply due to a lack of granted permission. </p>
<p> A key that is designated reapable will only be removed from a keyring if the caller has Write permission on that keyring, and only keyrings that grant Search permission to the caller will be searched. </p>
<p> The command prints the number of keys reaped before it exits. If the <code>-v</code> flag is passed then the reaped keys are listed as they&#8217;re being reaped, together with the success or failure of the unlink.</p>
<h3>Remove matching keys from the session keyring tree</h3>
<p> <code>keyctl</code> purge &lt;type&gt;<br />
 <code>keyctl</code> purge [-i] [-p] &lt;type&gt; &lt;desc&gt;<br />
 <code>keyctl</code> purge -s &lt;type&gt; &lt;desc&gt; </p>
<p> These commands perform a depth-first search to find matching keys in the caller&#8217;s session keyring tree and attempts to unlink them. The number of keys successfully unlinked is printed at the end. </p>
<p> The keyrings must grant Read and View permission to the caller to be searched, and the keys to be removed must also grant View permission. Keys can only be removed from keyrings that grant Write permission. </p>
<p> The first variant purges all keys of the specified type. </p>
<p> The second variant purges all keys of the specified type that also match the given description literally. The -i flag allows a case-independent match and the -p flag allows a prefix match. </p>
<p> The third variant purges all keys of the specified type and matching description using the key type&#8217;s comparator in the kernel to match the description. This permits the key type to match a key with a variety of descriptions.</p>
<h3>Get persistent keyring</h3>
<p> <code>keyctl</code> get_persistent &lt;keyring&gt; [&lt;uid&gt;] </p>
<p> This command gets the persistent keyring for either the current UID or the specified UID and attaches it to the nominated keyring. The persistent keyring&#8217;s ID will be printed on stdout. </p>
<p> The kernel will create the keyring if it doesn&#8217;t exist and every time this command is called, will reset the expiration timeout on the keyring to the value in:</p>
<dl>
<dt>
<dd> /proc/sys/kernel/keys/persistent_keyring_expiry</dl>
<p> (by default three days). Should the timeout be reached, the persistent keyring will be removed and everything it pins can then be garbage collected. </p>
<p> If a UID other than the process&#8217;s real or effective UIDs is specified, then an error will be given if the process does not have the CAP_SETUID capability.</p>
<h3>Compute a Diffie-Hellman shared secret or public key</h3>
<p> <code>keyctl</code> dh_compute &lt;private&gt; &lt;prime&gt; &lt;base&gt; </p>
<p> This command computes either a Diffie-Hellman shared secret or the public key corresponding to the provided private key using the payloads of three keys. The computation is:</p>
<dl>
<dt>
<dd> base ^ private (mod prime)</dl>
<p> The three inputs must be user keys with read permission. If the provided base key contains the shared generator value, the public key will be computed. If the provided base key contains the remote public key value, the shared secret will be computed. </p>
<p> The result is printed to stdout as a hex dump. </p>
<dl>
<dt>
<dd>
<pre>
$ keyctl dh_compute $1 $2 $3
8 bytes of data in result:
00010203 04050607
</dl>
</pre>
<h3>Compute a Diffie-Hellman shared secret and derive key material</h3>
<p> <code>keyctl</code> dh_compute_kdf &lt;private&gt; &lt;prime&gt; &lt;base&gt; &lt;output_length&gt; &lt;hash_type&gt; </p>
<p> This command computes a Diffie-Hellman shared secret and derives key material from the shared secret using a key derivation function (KDF). The shared secret is derived as outlined above and is input to the KDF using the specified hash type. The hash type must point to a hash name known to the kernel crypto API. </p>
<p> The operation derives key material of the length specified by the caller. </p>
<p> The operation is compliant to the specification of SP800-56A. </p>
<p> The result is printed to stdout as hex dump.</p>
<h3>Compute a Diffie-Hellman shared secret and apply KDF with other input</h3>
<p> <code>keyctl</code> dh_compute_kdf_oi &lt;private&gt; &lt;prime&gt; &lt;base&gt; &lt;output_length&gt; &lt;hash_type&gt; </p>
<p> This command is identical to the command <i>dh_compute_kdf</i> to generate a Diffie-Hellman shared secret followed by a key derivation operation. This command allows the caller to provide the other input data (OI data) compliant to SP800-56A via stdin.</p>
<h3>Perform public-key operations with an asymmetric key</h3>
<p> <code>keyctl</code> pkey_query &lt;key&gt; &lt;pass&gt; [k=v]*<br />
 <code>keyctl</code> pkey_encrypt &lt;key&gt; &lt;pass&gt; &lt;datafile&gt; [k=v]* &gt; &lt;encfile&gt;<br />
 <code>keyctl</code> pkey_decrypt &lt;key&gt; &lt;pass&gt; &lt;encfile&gt; [k=v]* &gt; &lt;datafile&gt;<br />
 <code>keyctl</code> pkey_sign &lt;key&gt; &lt;pass&gt; &lt;datafile&gt; [k=v]* &gt; &lt;sigfile&gt;<br />
 <code>keyctl</code> pkey_verify &lt;key&gt; &lt;pass&gt; &lt;datafile&gt; &lt;sigfile&gt; [k=v]* </p>
<p> These commands query an asymmetric key, encrypt data with it, decrypt the encrypted data, generate a signature over some data and verify that signature. For encrypt, decrypt and sign, the resulting data is written to stdout; verify reads the data and the signature files and compares them. </p>
<p> [<code>!</code>] NOTE that the data is of very limited capacity, with no more bits than the size of the key. For signatures, the caller is expected to digest the actual data and pass in the result of the digest as the datafile. The name of the digest should be specified on the end of the command line as &quot;hash=&lt;name&gt;&quot;. </p>
<p> The <i>key</i> ID indicates the key to use; <i>pass</i> is a placeholder for future password provision and should be &quot;0&quot; for the moment; <i>datafile</i> is the unencrypted data to be encrypted, signed or to have its signature checked; <i>encfile</i> is a file containing encrypted data; and <i>sigfile</i> is a file containing a signature. </p>
<p> A list of parameters in &quot;key[=val]&quot; form can be included on the end of the command line. These specify things like the digest algorithm used (&quot;hash=&lt;name&gt;&quot;) or the encoding form (&quot;enc=&lt;type&gt;&quot;). </p>
<dl>
<dt>
<dd>
<pre>
k=`keyctl padd asymmetric &quot;&quot; @s &lt;key.pkcs8.der`
keyctl pkey_query $k 0 enc=pkcs1 hash=sha256
keyctl pkey_encrypt $k 0 foo.hash enc=pkcs1 &gt;foo.enc
keyctl pkey_decrypt $k 0 foo.enc enc=pkcs1 &gt;foo.hash
keyctl pkey_sign $k 0 foo.hash enc=pkcs1 hash=sha256 &gt;foo.sig
keyctl pkey_verify $k 0 foo.hash foo.sig enc=pkcs1 hash=sha256
</pre>
</dl>
<p> See <a href="/docs/linux/man/7-asymmetric-key/">asymmetric-key</a>(7) for more information. </p>
<h2>ERRORS</h2>
<p> There are a number of common errors returned by this program: </p>
<p> &quot;Not a directory&quot; &#8211; a key wasn&#8217;t a keyring. </p>
<p> &quot;Requested key not found&quot; &#8211; the looked for key isn&#8217;t available. </p>
<p> &quot;Key has been revoked&quot; &#8211; a revoked key was accessed. </p>
<p> &quot;Key has expired&quot; &#8211; an expired key was accessed. </p>
<p> &quot;Permission denied&quot; &#8211; permission was denied by a UID/GID/mask combination.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2), <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
<h2>Index</h2>
