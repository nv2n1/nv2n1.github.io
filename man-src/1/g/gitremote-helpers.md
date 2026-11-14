---
title: "gitremote-helpers(1)"
name: "gitremote-helpers"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gitremote-helpers/"
description: "gitremote-helpers – Helper programs to interact with remote repositories"
---

<h2 class="name">NAME</h2>
<p> gitremote-helpers &#8211; Helper programs to interact with remote repositories </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git remote-&lt;transport&gt;</i> &lt;repository&gt; [&lt;URL&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> Remote helper programs are normally not used directly by end users, but they are invoked by Git when it needs to interact with remote repositories Git does not support natively. A given helper will implement a subset of the capabilities documented here. When Git needs to interact with a repository using a remote helper, it spawns the helper as an independent process, sends commands to the helper&#8217;s standard input, and expects results from the helper&#8217;s standard output. Because a remote helper runs as an independent process from Git, there is no need to re-link Git to add a new helper, nor any need to link the helper with the implementation of Git. </p>
<p> Every helper must support the &quot;capabilities&quot; command, which Git uses to determine what other commands the helper will accept. Those other commands can be used to discover and update remote refs, transport objects between the object database and the remote repository, and update the local object store. </p>
<p> Git comes with a &quot;curl&quot; family of remote helpers, that handle various transport protocols, such as <i>git-remote-http</i>, <i>git-remote-https</i>, <i>git-remote-ftp</i> and <i>git-remote-ftps</i>. They implement the capabilities <i>fetch</i>, <i>option</i>, and <i>push</i>.</p>
<h2>INVOCATION</h2>
<p> Remote helper programs are invoked with one or (optionally) two arguments. The first argument specifies a remote repository as in Git; it is either the name of a configured remote or a URL. The second argument specifies a URL; it is usually of the form <i>&lt;transport&gt;://&lt;address&gt;</i>, but any arbitrary string is possible. The <code>GIT_DIR</code> environment variable is set up for the remote helper and can be used to determine where to store additional data or from which directory to invoke auxiliary Git commands. </p>
<p> When Git encounters a URL of the form <i>&lt;transport&gt;://&lt;address&gt;</i>, where <i>&lt;transport&gt;</i> is a protocol that it cannot handle natively, it automatically invokes <i>git remote-&lt;transport&gt;</i> with the full URL as the second argument. If such a URL is encountered directly on the command line, the first argument is the same as the second, and if it is encountered in a configured remote, the first argument is the name of that remote. </p>
<p> A URL of the form <i>&lt;transport&gt;::&lt;address&gt;</i> explicitly instructs Git to invoke <i>git remote-&lt;transport&gt;</i> with <i>&lt;address&gt;</i> as the second argument. If such a URL is encountered directly on the command line, the first argument is <i>&lt;address&gt;</i>, and if it is encountered in a configured remote, the first argument is the name of that remote. </p>
<p> Additionally, when a configured remote has <code>remote.&lt;name&gt;.vcs</code> set to <i>&lt;transport&gt;</i>, Git explicitly invokes <i>git remote-&lt;transport&gt;</i> with <i>&lt;name&gt;</i> as the first argument. If set, the second argument is <code>remote.&lt;name&gt;.url</code>; otherwise, the second argument is omitted.</p>
<h2>INPUT FORMAT</h2>
<p> Git sends the remote helper a list of commands on standard input, one per line. The first command is always the <i>capabilities</i> command, in response to which the remote helper must print a list of the capabilities it supports (see below) followed by a blank line. The response to the capabilities command determines what commands Git uses in the remainder of the command stream. </p>
<p> The command stream is terminated by a blank line. In some cases (indicated in the documentation of the relevant commands), this blank line is followed by a payload in some other protocol (e.g., the pack protocol), while in others it indicates the end of input.</p>
<h3>Capabilities</h3>
<p> Each remote helper is expected to support only a subset of commands. The operations a helper supports are declared to Git in the response to the <code>capabilities</code> command (see COMMANDS, below). </p>
<p> In the following, we list all defined capabilities and for each we list which commands a helper with that capability must provide. </p>
<p> <font SIZE="+1"> <code>Capabilities for Pushing</code></p>
<dl>
<dt>
<dd>
<p> <i>connect</i></p>
<dl>
<dt>
<dd> Can attempt to connect to <i>git receive-pack</i> (for pushing), <i>git upload-pack</i>, etc for communication using git&#8217;s native packfile protocol. This requires a bidirectional, full-duplex connection. </p>
<p> Supported commands: <i>connect</i>.</dl>
<p> <i>push</i></p>
<dl>
<dt>
<dd> Can discover remote refs and push local commits and the history leading up to them to new or existing remote refs. </p>
<p> Supported commands: <i>list for-push</i>, <i>push</i>.</dl>
<p> <i>export</i></p>
<dl>
<dt>
<dd> Can discover remote refs and push specified objects from a fast-import stream to remote refs. </p>
<p> Supported commands: <i>list for-push</i>, <i>export</i>.</dl>
<p> If a helper advertises <i>connect</i>, Git will use it if possible and fall back to another capability if the helper requests so when connecting (see the <i>connect</i> command under COMMANDS). When choosing between <i>push</i> and <i>export</i>, Git prefers <i>push</i>. Other frontends may have some other order of preference. </p>
<p> <i>no-private-update</i></p>
<dl>
<dt>
<dd> When using the <i>refspec</i> capability, git normally updates the private ref on successful push. This update is disabled when the remote-helper declares the capability <i>no-private-update</i>.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Capabilities for Fetching</code></p>
<dl>
<dt>
<dd>
<p> <i>connect</i></p>
<dl>
<dt>
<dd> Can try to connect to <i>git upload-pack</i> (for fetching), <i>git receive-pack</i>, etc for communication using the Git&#8217;s native packfile protocol. This requires a bidirectional, full-duplex connection. </p>
<p> Supported commands: <i>connect</i>.</dl>
<p> <i>fetch</i></p>
<dl>
<dt>
<dd> Can discover remote refs and transfer objects reachable from them to the local object store. </p>
<p> Supported commands: <i>list</i>, <i>fetch</i>.</dl>
<p> <i>import</i></p>
<dl>
<dt>
<dd> Can discover remote refs and output objects reachable from them as a stream in fast-import format. </p>
<p> Supported commands: <i>list</i>, <i>import</i>.</dl>
<p> <i>check-connectivity</i></p>
<dl>
<dt>
<dd> Can guarantee that when a clone is requested, the received pack is self contained and is connected.</dl>
<p> If a helper advertises <i>connect</i>, Git will use it if possible and fall back to another capability if the helper requests so when connecting (see the <i>connect</i> command under COMMANDS). When choosing between <i>fetch</i> and <i>import</i>, Git prefers <i>fetch</i>. Other frontends may have some other order of preference.</dl>
<p> </font><font SIZE="+3"> <code>Miscellaneous capabilities</code></p>
<dl>
<dt>
<dd>
<p> <i>option</i></p>
<dl>
<dt>
<dd> For specifying settings like <code>verbosity</code> (how much output to write to stderr) and <code>depth</code> (how much history is wanted in the case of a shallow clone) that affect how other commands are carried out.</dl>
<p> <i>refspec</i> &lt;refspec&gt;</p>
<dl>
<dt>
<dd> For remote helpers that implement <i>import</i> or <i>export</i>, this capability allows the refs to be constrained to a private namespace, instead of writing to refs/heads or refs/remotes directly. It is recommended that all importers providing the <i>import</i> capability use this. It&#8217;s mandatory for <i>export</i>. </p>
<p> A helper advertising the capability <code>refspec refs/heads/*:refs/svn/origin/branches/*</code> is saying that, when it is asked to <code>import refs/heads/topic</code>, the stream it outputs will update the <code>refs/svn/origin/branches/topic</code> ref. </p>
<p> This capability can be advertised multiple times. The first applicable refspec takes precedence. The left-hand of refspecs advertised with this capability must cover all refs reported by the list command. If no <i>refspec</i> capability is advertised, there is an implied <code>refspec *:*</code>. </p>
<p> When writing remote-helpers for decentralized version control systems, it is advised to keep a local copy of the repository to interact with, and to let the private namespace refs point to this local repository, while the refs/remotes namespace is used to track the remote repository.</dl>
<p> <i>bidi-import</i></p>
<dl>
<dt>
<dd> This modifies the <i>import</i> capability. The fast-import commands <i>cat-blob</i> and <i>ls</i> can be used by remote-helpers to retrieve information about blobs and trees that already exist in fast-import&#8217;s memory. This requires a channel from fast-import to the remote-helper. If it is advertised in addition to &quot;import&quot;, Git establishes a pipe from fast-import to the remote-helper&#8217;s stdin. It follows that Git and fast-import are both connected to the remote-helper&#8217;s stdin. Because Git can send multiple commands to the remote-helper it is required that helpers that use <i>bidi-import</i> buffer all <i>import</i> commands of a batch before sending data to fast-import. This is to prevent mixing commands and fast-import responses on the helper&#8217;s stdin.</dl>
<p> <i>export-marks</i> &lt;file&gt;</p>
<dl>
<dt>
<dd> This modifies the <i>export</i> capability, instructing Git to dump the internal marks table to &lt;file&gt; when complete. For details, read up on <code>&#8211;export-marks=&lt;file&gt;</code> in <code><a href="/docs/linux/man/1-git-fast-export/">git-fast-export</a></code>(1).</dl>
<p> <i>import-marks</i> &lt;file&gt;</p>
<dl>
<dt>
<dd> This modifies the <i>export</i> capability, instructing Git to load the marks specified in &lt;file&gt; before processing any input. For details, read up on <code>&#8211;import-marks=&lt;file&gt;</code> in <code><a href="/docs/linux/man/1-git-fast-export/">git-fast-export</a></code>(1).</dl>
<p> <i>signed-tags</i></p>
<dl>
<dt>
<dd> This modifies the <i>export</i> capability, instructing Git to pass <code>&#8211;signed-tags=verbatim</code> to <code><a href="/docs/linux/man/1-git-fast-export/">git-fast-export</a></code>(1). In the absence of this capability, Git will use <code>&#8211;signed-tags=warn-strip</code>.</dl>
</dl>
<p> </font></p>
<h2>COMMANDS</h2>
<p> Commands are given by the caller on the helper&#8217;s standard input, one per line. </p>
<p> <i>capabilities</i></p>
<dl>
<dt>
<dd> Lists the capabilities of the helper, one per line, ending with a blank line. Each capability may be preceded with <i>*</i>, which marks them mandatory for Git versions using the remote helper to understand. Any unknown mandatory capability is a fatal error. </p>
<p> Support for this command is mandatory.</dl>
<p> <i>list</i></p>
<dl>
<dt>
<dd> Lists the refs, one per line, in the format &quot;&lt;value&gt; &lt;name&gt; [&lt;attr&gt; &#8230;]&quot;. The value may be a hex sha1 hash, &quot;@&lt;dest&gt;&quot; for a symref, or &quot;?&quot; to indicate that the helper could not get the value of the ref. A space-separated list of attributes follows the name; unrecognized attributes are ignored. The list ends with a blank line. </p>
<p> See REF LIST ATTRIBUTES for a list of currently defined attributes. </p>
<p> Supported if the helper has the &quot;fetch&quot; or &quot;import&quot; capability.</dl>
<p> <i>list for-push</i></p>
<dl>
<dt>
<dd> Similar to <i>list</i>, except that it is used if and only if the caller wants to the resulting ref list to prepare push commands. A helper supporting both push and fetch can use this to distinguish for which operation the output of <i>list</i> is going to be used, possibly reducing the amount of work that needs to be performed. </p>
<p> Supported if the helper has the &quot;push&quot; or &quot;export&quot; capability.</dl>
<p> <i>option</i> &lt;name&gt; &lt;value&gt;</p>
<dl>
<dt>
<dd> Sets the transport helper option &lt;name&gt; to &lt;value&gt;. Outputs a single line containing one of <i>ok</i> (option successfully set), <i>unsupported</i> (option not recognized) or <i>error &lt;msg&gt;</i> (option &lt;name&gt; is supported but &lt;value&gt; is not valid for it). Options should be set before other commands, and may influence the behavior of those commands. </p>
<p> See OPTIONS for a list of currently defined options. </p>
<p> Supported if the helper has the &quot;option&quot; capability.</dl>
<p> <i>fetch</i> &lt;sha1&gt; &lt;name&gt;</p>
<dl>
<dt>
<dd> Fetches the given object, writing the necessary objects to the database. Fetch commands are sent in a batch, one per line, terminated with a blank line. Outputs a single blank line when all fetch commands in the same batch are complete. Only objects which were reported in the output of <i>list</i> with a sha1 may be fetched this way. </p>
<p> Optionally may output a <i>lock &lt;file&gt;</i> line indicating a file under GIT_DIR/objects/pack which is keeping a pack until refs can be suitably updated. </p>
<p> If option <i>check-connectivity</i> is requested, the helper must output <i>connectivity-ok</i> if the clone is self-contained and connected. </p>
<p> Supported if the helper has the &quot;fetch&quot; capability.</dl>
<p> <i>push</i> +&lt;src&gt;:&lt;dst&gt;</p>
<dl>
<dt>
<dd> Pushes the given local &lt;src&gt; commit or branch to the remote branch described by &lt;dst&gt;. A batch sequence of one or more <i>push</i> commands is terminated with a blank line (if there is only one reference to push, a single <i>push</i> command is followed by a blank line). For example, the following would be two batches of <i>push</i>, the first asking the remote-helper to push the local ref <i>master</i> to the remote ref <i>master</i> and the local <code>HEAD</code> to the remote <i>branch</i>, and the second asking to push ref <i>foo</i> to ref <i>bar</i> (forced update requested by the <i>+</i>). </p>
<dl>
<dt>
<dd>
<pre>
push refs/heads/master:refs/heads/master
push HEAD:refs/heads/branch


push +refs/heads/foo:refs/heads/bar


</pre>
</dl>
<p> Zero or more protocol options may be entered after the last <i>push</i> command, before the batch&#8217;s terminating blank line. </p>
<p> When the push is complete, outputs one or more <i>ok &lt;dst&gt;</i> or <i>error &lt;dst&gt; &lt;why&gt;?</i> lines to indicate success or failure of each pushed ref. The status report output is terminated by a blank line. The option field &lt;why&gt; may be quoted in a C style string if it contains an LF. </p>
<p> Supported if the helper has the &quot;push&quot; capability.</dl>
<p> <i>import</i> &lt;name&gt;</p>
<dl>
<dt>
<dd> Produces a fast-import stream which imports the current value of the named ref. It may additionally import other refs as needed to construct the history efficiently. The script writes to a helper-specific private namespace. The value of the named ref should be written to a location in this namespace derived by applying the refspecs from the &quot;refspec&quot; capability to the name of the ref. </p>
<p> Especially useful for interoperability with a foreign versioning system. </p>
<p> Just like <i>push</i>, a batch sequence of one or more <i>import</i> is terminated with a blank line. For each batch of <i>import</i>, the remote helper should produce a fast-import stream terminated by a <i>done</i> command. </p>
<p> Note that if the <i>bidi-import</i> capability is used the complete batch sequence has to be buffered before starting to send data to fast-import to prevent mixing of commands and fast-import responses on the helper&#8217;s stdin. </p>
<p> Supported if the helper has the &quot;import&quot; capability.</dl>
<p> <i>export</i></p>
<dl>
<dt>
<dd> Instructs the remote helper that any subsequent input is part of a fast-import stream (generated by <i>git fast-export</i>) containing objects which should be pushed to the remote. </p>
<p> Especially useful for interoperability with a foreign versioning system. </p>
<p> The <i>export-marks</i> and <i>import-marks</i> capabilities, if specified, affect this command in so far as they are passed on to <i>git fast-export</i>, which then will load/store a table of marks for local objects. This can be used to implement for incremental operations. </p>
<p> Supported if the helper has the &quot;export&quot; capability.</dl>
<p> <i>connect</i> &lt;service&gt;</p>
<dl>
<dt>
<dd> Connects to given service. Standard input and standard output of helper are connected to specified service (git prefix is included in service name so e.g. fetching uses <i>git-upload-pack</i> as service) on remote side. Valid replies to this command are empty line (connection established), <i>fallback</i> (no smart transport support, fall back to dumb transports) and just exiting with error message printed (can&#8217;t connect, don&#8217;t bother trying to fall back). After line feed terminating the positive (empty) response, the output of service starts. After the connection ends, the remote helper exits. </p>
<p> Supported if the helper has the &quot;connect&quot; capability.</dl>
<p> If a fatal error occurs, the program writes the error message to stderr and exits. The caller should expect that a suitable error message has been printed if the child closes the connection without completing a valid response for the current command. </p>
<p> Additional commands may be supported, as may be determined from capabilities reported by the helper.</p>
<h2>REF LIST ATTRIBUTES</h2>
<p> The <i>list</i> command produces a list of refs in which each ref may be followed by a list of attributes. The following ref list attributes are defined. </p>
<p> <i>unchanged</i></p>
<dl>
<dt>
<dd> This ref is unchanged since the last import or fetch, although the helper cannot necessarily determine what value that produced.</dl>
<h2>OPTIONS</h2>
<p> The following options are defined and (under suitable circumstances) set by Git if the remote helper has the <i>option</i> capability. </p>
<p> <i>option verbosity</i> &lt;n&gt;</p>
<dl>
<dt>
<dd> Changes the verbosity of messages displayed by the helper. A value of 0 for &lt;n&gt; means that processes operate quietly, and the helper produces only error output. 1 is the default level of verbosity, and higher values of &lt;n&gt; correspond to the number of -v flags passed on the command line.</dl>
<p> <i>option progress</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> Enables (or disables) progress messages displayed by the transport helper during a command.</dl>
<p> <i>option depth</i> &lt;depth&gt;</p>
<dl>
<dt>
<dd> Deepens the history of a shallow repository.</dl>
<p> &#8216;option deepen-since &lt;timestamp&gt;</p>
<dl>
<dt>
<dd> Deepens the history of a shallow repository based on time.</dl>
<p> &#8216;option deepen-not &lt;ref&gt;</p>
<dl>
<dt>
<dd> Deepens the history of a shallow repository excluding ref. Multiple options add up.</dl>
<p> <i>option deepen-relative {&#8216;true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> Deepens the history of a shallow repository relative to current boundary. Only valid when used with &quot;option depth&quot;.</dl>
<p> <i>option followtags</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> If enabled the helper should automatically fetch annotated tag objects if the object the tag points at was transferred during the fetch command. If the tag is not fetched by the helper a second fetch command will usually be sent to ask for the tag specifically. Some helpers may be able to use this option to avoid a second network connection.</dl>
<p> <i>option dry-run</i> {<i>true</i>|<i>false</i>}: If true, pretend the operation completed successfully, but don&#8217;t actually change any repository data. For most helpers this only applies to the <i>push</i>, if supported. </p>
<p> <i>option servpath &lt;c-style-quoted-path&gt;</i></p>
<dl>
<dt>
<dd> Sets service path (&#8211;upload-pack, &#8211;receive-pack etc.) for next connect. Remote helper may support this option, but must not rely on this option being set before connect request occurs.</dl>
<p> <i>option check-connectivity</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> Request the helper to check connectivity of a clone.</dl>
<p> <i>option force</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> Request the helper to perform a force update. Defaults to <i>false</i>.</dl>
<p> <i>option cloning</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> Notify the helper this is a clone request (i.e. the current repository is guaranteed empty).</dl>
<p> <i>option update-shallow</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> Allow to extend .git/shallow if the new refs require it.</dl>
<p> <i>option pushcert</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> GPG sign pushes.</dl>
<p> &#8216;option push-option &lt;string&gt;</p>
<dl>
<dt>
<dd> Transmit &lt;string&gt; as a push option. As the push option must not contain LF or NUL characters, the string is not encoded.</dl>
<p> <i>option from-promisor</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> Indicate that these objects are being fetched from a promisor.</dl>
<p> <i>option no-dependents</i> {<i>true</i>|<i>false</i>}</p>
<dl>
<dt>
<dd> Indicate that only the objects wanted need to be fetched, not their dependents.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-git-remote-ext/">git-remote-ext</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-git-remote-fd/">git-remote-fd</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-git-remote-testgit/">git-remote-testgit</a></code>(1) </p>
<p> <code><a href="/docs/linux/man/1-git-fast-import/">git-fast-import</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
