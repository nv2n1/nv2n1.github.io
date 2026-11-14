---
title: "git-bundle(1)"
name: "git-bundle"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-bundle/"
description: "git-bundle – Move objects and refs by archive"
---

<h2 class="name">NAME</h2>
<p> git-bundle &#8211; Move objects and refs by archive </p>
<h2>SYNOPSIS</h2>
<pre><code>
git bundle create[-q | --quiet | --progress | --all - progress][--all - progress - implied]
                 [--version = &lt;version&gt;]&lt;file&gt;&lt;git - rev - list - args&gt;
                     git bundle verify[-q | --quiet]&lt;file&gt;
                         git bundle list - heads&lt;file&gt;[&lt;refname&gt;...] git bundle unbundle[--progress]&lt;file&gt;[&lt;refname&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Create, unpack, and manipulate &quot;bundle&quot; files. Bundles are used for the &quot;offline&quot; transfer of Git objects without an active &quot;server&quot; sitting on the other side of the network connection. </p>
<p> They can be used to create both incremental and full backups of a repository, and to relay the state of the references in one repository to another. </p>
<p> Git commands that fetch or otherwise &quot;read&quot; via protocols such as <code>ssh://</code> and <code>https://</code> can also operate on bundle files. It is possible <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) a new repository from a bundle, to use <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1) to fetch from one, and to list the references contained within it with <code><a href="/docs/linux/man/1-git-ls-remote/">git-ls-remote</a></code>(1). There&#8217;s no corresponding &quot;write&quot; support, i.e.a <i>git push</i> into a bundle is not supported. </p>
<p> See the &quot;EXAMPLES&quot; section below for examples of how to use bundles.</p>
<h2>BUNDLE FORMAT</h2>
<p> Bundles are <code>.pack</code> files (see <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1)) with a header indicating what references are contained within the bundle. </p>
<p> Like the the packed archive format itself bundles can either be self-contained, or be created using exclusions. See the &quot;OBJECT PREREQUISITES&quot; section below. </p>
<p> Bundles created using revision exclusions are &quot;thin packs&quot; created using the <code>&#8211;thin</code> option to <code><a href="/docs/linux/man/1-git-pack-objects/">git-pack-objects</a></code>(1), and unbundled using the <code>&#8211;fix-thin</code> option to <code><a href="/docs/linux/man/1-git-index-pack/">git-index-pack</a></code>(1). </p>
<p> There is no option to create a &quot;thick pack&quot; when using revision exclusions, and users should not be concerned about the difference. By using &quot;thin packs&quot;, bundles created using exclusions are smaller in size. That they&#8217;re &quot;thin&quot; under the hood is merely noted here as a curiosity, and as a reference to other documentation. </p>
<p> See m[blue]<code>the bundle-format</code> documentationm[]<font SIZE="-2">[1]</font> for more details and the discussion of &quot;thin pack&quot; in m[blue]<code>the pack format documentation</code>m[]<font SIZE="-2">[2]</font> for further details.</p>
<h2>OPTIONS</h2>
<p> create [options] &lt;file&gt; &lt;git-rev-list-args&gt;</p>
<dl>
<dt>
<dd> Used to create a bundle named <i>file</i>. This requires the <i>&lt;git-rev-list-args&gt;</i> arguments to define the bundle contents. <i>options</i> contains the options specific to the <i>git bundle create</i> subcommand.</dl>
<p> verify &lt;file&gt;</p>
<dl>
<dt>
<dd> Used to check that a bundle file is valid and will apply cleanly to the current repository. This includes checks on the bundle format itself as well as checking that the prerequisite commits exist and are fully linked in the current repository. <i>git bundle</i> prints a list of missing commits, if any, and exits with a non-zero status.</dl>
<p> list-heads &lt;file&gt;</p>
<dl>
<dt>
<dd> Lists the references defined in the bundle. If followed by a list of references, only references matching those given are printed out.</dl>
<p> unbundle &lt;file&gt;</p>
<dl>
<dt>
<dd> Passes the objects in the bundle to <i>git index-pack</i> for storage in the repository, then prints the names of all defined references. If a list of references is given, only references matching those in the list are printed. This command is really plumbing, intended to be called only by <i>git fetch</i>.</dl>
<p> &lt;git-rev-list-args&gt;</p>
<dl>
<dt>
<dd> A list of arguments, acceptable to <i>git rev-parse</i> and <i>git rev-list</i> (and containing a named ref, see SPECIFYING REFERENCES below), that specifies the specific objects and references to transport. For example, <code>master~10..master</code> causes the current master reference to be packaged along with all objects added since its 10th ancestor commit. There is no explicit limit to the number of references and objects that may be packaged.</dl>
<p> [&lt;refname&gt;&#8230;]</p>
<dl>
<dt>
<dd> A list of references used to limit the references reported as available. This is principally of use to <i>git fetch</i>, which expects to receive only those references asked for and not necessarily everything in the pack (in this case, <i>git bundle</i> acts like <i>git fetch-pack</i>).</dl>
<p> &#8211;progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces progress status even if the standard error stream is not directed to a terminal.</dl>
<p> &#8211;all-progress</p>
<dl>
<dt>
<dd> When &#8211;stdout is specified then progress report is displayed during the object count and compression phases but inhibited during the write-out phase. The reason is that in some cases the output stream is directly linked to another command which may wish to display progress status of its own as it processes incoming pack data. This flag is like &#8211;progress except that it forces progress report for the write-out phase as well even if &#8211;stdout is used.</dl>
<p> &#8211;all-progress-implied</p>
<dl>
<dt>
<dd> This is used to imply &#8211;all-progress whenever progress display is activated. Unlike &#8211;all-progress this flag doesn&#8217;t actually force any progress display by itself.</dl>
<p> &#8211;version=&lt;version&gt;</p>
<dl>
<dt>
<dd> Specify the bundle version. Version 2 is the older format and can only be used with SHA-1 repositories; the newer version 3 contains capabilities that permit extensions. The default is the oldest supported format, based on the hash algorithm in use.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> This flag makes the command not to report its progress on the standard error stream.</dl>
<h2>SPECIFYING REFERENCES</h2>
<p> Revisions must be accompanied by reference names to be packaged in a bundle. </p>
<p> More than one reference may be packaged, and more than one set of prerequisite objects can be specified. The objects packaged are those not contained in the union of the prerequisites. </p>
<p> The <i>git bundle create</i> command resolves the reference names for you using the same rules as <code>git rev-parse &#8211;abbrev-ref=loose</code>. Each prerequisite can be specified explicitly (e.g. <code>^master~10</code>), or implicitly (e.g. <code>master~10..master</code>, <code>&#8211;since=10.days.ago master</code>). </p>
<p> All of these simple cases are OK (assuming we have a &quot;master&quot; and &quot;next&quot; branch): </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle create master.bundle master
$ echo master | git bundle create master.bundle --stdin
$ git bundle create master-and-next.bundle master next
$ (echo master; echo next) | git bundle create master-and-next.bundle --stdin
</pre>
</dl>
<p> And so are these (and the same but omitted <code>&#8211;stdin</code> examples): </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle create recent-master.bundle master~10..master
$ git bundle create recent-updates.bundle master~10..master next~5..next
</pre>
</dl>
<p> A revision name or a range whose right-hand-side cannot be resolved to a reference is not accepted: </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle create HEAD.bundle $(git rev-parse HEAD)
fatal: Refusing to create empty bundle.
$ git bundle create master-yesterday.bundle master~10..master~5
fatal: Refusing to create empty bundle.
</pre>
</dl>
<h2>OBJECT PREREQUISITES</h2>
<p> When creating bundles it is possible to create a self-contained bundle that can be unbundled in a repository with no common history, as well as providing negative revisions to exclude objects needed in the earlier parts of the history. </p>
<p> Feeding a revision such as <code>new</code> to <code>git bundle create</code> will create a bundle file that contains all the objects reachable from the revision <code>new</code>. That bundle can be unbundled in any repository to obtain a full history that leads to the revision <code>new</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle create full.bundle new
</pre>
</dl>
<p> A revision range such as <code>old..new</code> will produce a bundle file that will require the revision <code>old</code> (and any objects reachable from it) to exist for the bundle to be &quot;unbundle&quot;-able: </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle create full.bundle old..new
</pre>
</dl>
<p> A self-contained bundle without any prerequisites can be extracted into anywhere, even into an empty repository, or be cloned from (i.e., <code>new</code>, but not <code>old..new</code>). </p>
<p> It is okay to err on the side of caution, causing the bundle file to contain objects already in the destination, as these are ignored when unpacking at the destination. </p>
<p> If you want to match <code>git clone &#8211;mirror</code>, which would include your refs such as <code>refs/remotes/*</code>, use <code>&#8211;all</code>. If you want to provide the same set of refs that a clone directly from the source repository would get, use <code>&#8211;branches &#8211;tags</code> for the <code>&lt;git-rev-list-args&gt;</code>. </p>
<p> The <i>git bundle verify</i> command can be used to check whether your recipient repository has the required prerequisite commits for a bundle.</p>
<h2>EXAMPLES</h2>
<p> Assume you want to transfer the history from a repository R1 on machine A to another repository R2 on machine B. For whatever reason, direct connection between A and B is not allowed, but we can move data from A to B via some mechanism (CD, email, etc.). We want to update R2 with development made on the branch master in R1. </p>
<p> To bootstrap the process, you can first create a bundle that does not have any prerequisites. You can use a tag to remember up to what commit you last processed, in order to make it easy to later update the other repository with an incremental bundle: </p>
<dl>
<dt>
<dd>
<pre>
machineA$ cd R1
machineA$ git bundle create file.bundle master
machineA$ git tag -f lastR2bundle master
</pre>
</dl>
<p> Then you transfer file.bundle to the target machine B. Because this bundle does not require any existing object to be extracted, you can create a new repository on machine B by cloning from it: </p>
<dl>
<dt>
<dd>
<pre>
machineB$ git clone -b master /home/me/tmp/file.bundle R2
</pre>
</dl>
<p> This will define a remote called &quot;origin&quot; in the resulting repository that lets you fetch and pull from the bundle. The $GIT_DIR/config file in R2 will have an entry like this: </p>
<dl>
<dt>
<dd>
<pre>
[remote &quot;origin&quot;]
    url = /home/me/tmp/file.bundle
    fetch = refs/heads/*:refs/remotes/origin/*
</pre>
</dl>
<p> To update the resulting mine.git repository, you can fetch or pull after replacing the bundle stored at /home/me/tmp/file.bundle with incremental updates. </p>
<p> After working some more in the original repository, you can create an incremental bundle to update the other repository: </p>
<dl>
<dt>
<dd>
<pre>
machineA$ cd R1
machineA$ git bundle create file.bundle lastR2bundle..master
machineA$ git tag -f lastR2bundle master
</pre>
</dl>
<p> You then transfer the bundle to the other machine to replace /home/me/tmp/file.bundle, and pull from it. </p>
<dl>
<dt>
<dd>
<pre>
machineB$ cd R2
machineB$ git pull
</pre>
</dl>
<p> If you know up to what commit the intended recipient repository should have the necessary objects, you can use that knowledge to specify the prerequisites, giving a cut-off point to limit the revisions and objects that go in the resulting bundle. The previous example used the lastR2bundle tag for this purpose, but you can use any other options that you would give to the <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) command. Here are more examples: </p>
<p> You can use a tag that is present in both: </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle create mybundle v1.0.0..master
</pre>
</dl>
<p> You can use a prerequisite based on time: </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle create mybundle --since=10.days master
</pre>
</dl>
<p> You can use the number of commits: </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle create mybundle -10 master
</pre>
</dl>
<p> You can run <code>git-bundle verify</code> to see if you can extract from a bundle that was created with a prerequisite: </p>
<dl>
<dt>
<dd>
<pre>
$ git bundle verify mybundle
</pre>
</dl>
<p> This will list what commits you must have in order to extract from the bundle and will error out if you do not have them. </p>
<p> A bundle from a recipient repository&#8217;s point of view is just like a regular repository which it fetches or pulls from. You can, for example, map references when fetching: </p>
<dl>
<dt>
<dd>
<pre>
$ git fetch mybundle master:localRef
</pre>
</dl>
<p> You can also see what references it offers: </p>
<dl>
<dt>
<dd>
<pre>
$ git ls-remote mybundle
</pre>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the <code>bundle-format</code> documentation</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/technical/bundle-format.html</dl>
<dt> 2.</p>
<dd> the pack format documentation</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/technical/pack-format.html</dl>
</dl>
<h2>Index</h2>
