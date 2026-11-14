---
title: "gitnamespaces(7)"
name: "gitnamespaces"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gitnamespaces/"
description: "gitnamespaces – Git namespaces"
---

<p>gitnamespaces &#8211; Git namespaces</p>
<h2>Synopsis</h2>
<pre>GIT_NAMESPACE=&lt;namespace&gt; <i>git upload-pack</i>
GIT_NAMESPACE=&lt;namespace&gt; <i>git receive-pack</i></pre>
<h2>Description</h2>
<p>Git supports dividing the refs of a single repository into multiple namespaces, each of which has its own branches, tags, and HEAD. Git can expose each namespace as an independent repository to pull from and push to, while sharing the object store, and exposing all the refs to operations such as <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1). Storing multiple repositories as namespaces of a single repository avoids storing duplicate copies of the same objects, such as when storing multiple branches of the same source. The alternates mechanism provides similar support for avoiding duplicates, but alternates do not prevent duplication between new objects added to the repositories without ongoing maintenance, while namespaces do. To specify a namespace, set the <code>GIT_NAMESPACE</code> environment variable to the namespace. For each ref namespace, Git stores the corresponding refs in a directory under <code>refs/namespaces/</code>. For example, <code>GIT_NAMESPACE=foo</code> will store refs under <code>refs/namespaces/foo/</code>. You can also specify namespaces via the <code>&#8211;namespace</code> option to <code><a href="/docs/linux/man/1-git/">git</a></code>(1). Note that namespaces which include a <code>/</code> will expand to a hierarchy of namespaces; for example, <code>GIT_NAMESPACE=foo/bar</code> will store refs under <code>refs/namespaces/foo/refs/namespaces/bar/</code>. This makes paths in <code>GIT_NAMESPACE</code> behave hierarchically, so that cloning with <code>GIT_NAMESPACE=foo/bar</code> produces the same result as cloning with <code>GIT_NAMESPACE=foo</code> and cloning from that repo with <code>GIT_NAMESPACE=bar</code>. It also avoids ambiguity with strange namespace paths such as <code>foo/refs/heads/</code>, which could otherwise generate directory/file conflicts within the <code>refs</code> directory. <code><a href="/docs/linux/man/1-git-upload-pack/">git-upload-pack</a></code>(1) and <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1) rewrite the names of refs as specified by <code>GIT_NAMESPACE</code>. git-upload-pack and git-receive-pack will ignore all references outside the specified namespace. The smart HTTP server, <code><a href="/docs/linux/man/1-git-http-backend/">git-http-backend</a></code>(1), will pass GIT_NAMESPACE through to the backend programs; see <code><a href="/docs/linux/man/1-git-http-backend/">git-http-backend</a></code>(1) for sample configuration to expose repository namespaces as repositories. For a simple local test, you can use <code><a href="/docs/linux/man/1-git-remote-ext/">git-remote-ext</a></code>(1):</p>
<dl>
<dd>
<pre>git clone ext::'git --namespace=foo %s /tmp/prefixed.git'</pre>
</dl>
<h2>Security</h2>
<p>The fetch and push protocols are not designed to prevent one side from stealing data from the other repository that was not intended to be shared. If you have private data that you need to protect from a malicious peer, your best option is to store it in another repository. This applies to both clients and servers. In particular, namespaces on a server are not effective for read access control; you should only grant read access to a namespace to clients that you would trust with read access to the entire repository. </p>
<p> The known attack vectors are as follows: </p>
<dl>
<dd>1. The victim sends &quot;have&quot; lines advertising the IDs of objects it has that are not explicitly intended to be shared but can be used to optimize the transfer if the peer also has them. The attacker chooses an object ID X to steal and sends a ref to X, but isn&#8217;t required to send the content of X because the victim already has it. Now the victim believes that the attacker has X, and it sends the content of X back to the attacker later. (This attack is most straightforward for a client to perform on a server, by creating a ref to X in the namespace the client has access to and then fetching it. The most likely way for a server to perform it on a client is to &quot;merge&quot; X into a public branch and hope that the user does additional work on this branch and pushes it back to the server without noticing the merge.)</dl>
<dl>
<dd>2. As in #1, the attacker chooses an object ID X to steal. The victim sends an object Y that the attacker already has, and the attacker falsely claims to have X and not Y, so the victim sends Y as a delta against X. The delta reveals regions of X that are similar to Y to the attacker.</dl>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
