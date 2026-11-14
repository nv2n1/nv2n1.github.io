---
title: "swift(1)"
name: "swift"
section: "1"
letter: "s"
url: "/docs/linux/man/1-swift/"
description: "swift – OpenStack Swift client tool"
---

<h2 class="name">NAME</h2>
<p> <code>swift</code> &#8211; OpenStack Swift client tool</p>
<h2>SYNOPSIS</h2>
<p> <code>swift</code> [options] &lt;command&gt; [args] </p>
<h2>DESCRIPTION</h2>
<p> The <code>swift</code> tool is a command line utility for communicating with an OpenStack Object Storage (Swift) environment. It allows one to perform several types of operations. </p>
<h2>COMMANDS</h2>
<p> <code>stat</code> [<i>container</i>] [<i>object</i>]</p>
<dl>
<dt>
<dd> Displays information for the account, container, or object depending on the args given (if any). In verbose mode, the Storage URL and the authentication token are displayed as well.</dl>
<p> <code>list</code> [<i>command-options</i>] [<i>container</i>]</p>
<dl>
<dt>
<dd> Lists the containers for the account or the objects for a container. The -p or &#8211;prefix is an option that will only list items beginning with that prefix. The -d or &#8211;delimiter is option (for container listings only) that will roll up items with the given delimiter (see OpenStack Swift general documentation for what this means). </p>
<p> The -l and &#8211;lh options provide more detail, similar to ls -l and ls -lh, the latter providing sizes in human readable format (eg 3K, 12M, etc). These latter 2 switches use more overhead to get those details, which is directly proportional to the number of container or objects being listed.</dl>
<p> <code>upload</code> [<i>command-options</i>] container file_or_directory [<i>file_or_directory</i>] [&#8230;]</p>
<dl>
<dt>
<dd> Uploads to the given container the files and directories specified by the remaining args. The -c or &#8211;changed is an option that will only upload files that have changed since the last upload. The &#8211;object-name &lt;object-name&gt; is an option that will upload file and name object to &lt;object-name&gt; or upload dir and use &lt;object-name&gt; as object prefix. The -S &lt;size&gt; or &#8211;segment-size &lt;size&gt; and &#8211;leave-segments are options as well (see &#8211;help for more).</dl>
<p> <code>post</code> [<i>command-options</i>] [<i>container</i>] [<i>object</i>]</p>
<dl>
<dt>
<dd> Updates meta information for the account, container, or object depending on the args given. If the container is not found, it will be created automatically; but this is not true for accounts and objects. Containers also allow the -r (or &#8211;read-acl) and -w (or &#8211;write-acl) options. The -m or &#8211;meta option is allowed on all and used to define the user meta data items to set in the form Name:Value. This option can be repeated. <code>Example</code>: post -m Color:Blue -m Size:Large</dl>
<p> <code>download</code> [<i>command-options</i>] [<i>container</i>] [<i>object</i>] [<i>object</i>] [&#8230;]</p>
<dl>
<dt>
<dd> Downloads everything in the account (with &#8211;all), or everything in a container, or a list of objects depending on the args given. For a single object download, you may use the -o [&#8211;output] &lt;filename&gt; option to redirect the output to a specific file or if &quot;-&quot; then just redirect to stdout. You can specify optional headers with the repeatable cURL-like option -H [&#8211;header].</dl>
<p> <code>delete</code> [<i>command-options</i>] [<i>container</i>] [<i>object</i>] [<i>object</i>] [&#8230;]</p>
<dl>
<dt>
<dd> Deletes everything in the account (with &#8211;all), or everything in a container, or a list of objects depending on the args given. Segments of manifest objects will be deleted as well, unless you specify the &#8211;leave-segments option.</dl>
<p> <code>capabilities</code> [<i>proxy-url</i>]</p>
<dl>
<dt>
<dd> Displays cluster capabilities. The output includes the list of the activated Swift middlewares as well as relevant options for each ones. Addtionaly the command displays relevant options for the Swift core. If the proxy-url option is not provided the storage-url retrieved after authentication is used as proxy-url.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version Show program&#8217;s version number and exit</p>
<dd>
<dt>-h, &#8211;help Show this (or any subcommand) help message and exit</p>
<dd>
<dt>-s, &#8211;snet Use SERVICENET internal network</p>
<dd>
<dt>-v, &#8211;verbose Print more info</p>
<dd>
<dt>-q, &#8211;quiet Suppress status output</p>
<dd>
<dt>-A AUTH, &#8211;auth=AUTH URL for obtaining an auth token</p>
<dd>
<dt>-U USER, &#8211;user=USER User name for obtaining an auth token</p>
<dd>
<dt>-V 1|2 Authentication protocol version</p>
<dd>
<dt>-K KEY, &#8211;key=KEY Key for obtaining an auth token</p>
<dd>
<dt>&#8211;os-storage-url=URL Use this instead of URL returned from auth</p>
<dd>
</dl>
<h2>EXAMPLE</h2>
<p> swift -A <a rel="nofollow" href="https://127.0.0.1:443/auth/v1.0">https://127.0.0.1:443/auth/v1.0</a> -U swiftops:swiftops -K swiftops stat </p>
<dl>
<dt>
<dd>
<dl>
<dt> Account: AUTH_43b42dae-dc0b-4a4b-ac55-97de614d6e6e</p>
<dd>
<dt>Containers: 1</p>
<dd>
<dt> Objects: 1</p>
<dd>
<dt> Bytes: 1124</p>
<dd>
<dt>Accept-Ranges: bytes</p>
<dd>
<dt>X-Trans-Id: txb21186a9eef64ed295a1e95896a0fc72</p>
<dd></dl>
</dl>
<h2>DOCUMENTATION</h2>
<p> More in depth documentation about OpenStack Swift as a whole can be found at <code><a rel="nofollow" href="http://swift.openstack.org">http://swift.openstack.org</a></code> </p>
<h2>Index</h2>
