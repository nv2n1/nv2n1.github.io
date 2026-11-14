---
title: "atomic-trust(1)"
name: "atomic-trust"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-trust/"
description: "atomic-trust – Manage system container trust policy"
---

<h2 class="name">NAME</h2>
<p> atomic-trust &#8211; Manage system container trust policy </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic trust add|delete|default|reset|show</code> [<code>-h</code>|<code>&#8211;help</code>] [<code>-j</code>|<code>&#8211;json</code>] [<code>&#8211;raw</code>] [<code>-k</code>|<code>&#8211;pubkeys</code> KEY1 [<code>-k</code>|<code>&#8211;pubkeys</code> KEY2,&#8230;]] [<code>-f</code>|<code>&#8211;pubkeysfile</code> KEY1 [<code>f</code>|<code>&#8211;pubkeysfile</code> KEY2,&#8230;]] [<code>&#8211;keytype</code> GPGKeys] [<code>-t</code>|<code>&#8211;type</code> signedBy|insecureAcceptAnything|reject] [<code>-s</code>|<code>&#8211;sigstore</code> &lt;<a rel="nofollow" href="https://URL[:PORT][/PATH]|file:///PATH">https://URL[:PORT][/PATH]|file:///PATH</a>&gt;] [<code>&#8211;sigstoretype</code> web|atomic|local] REGISTRY[/REPOSITORY] </p>
<h2>DESCRIPTION</h2>
<p> <code>atomic trust</code> manages the trust policy of the host system. Trust policy describes a registry scope (registry and/or repository) that must be signed by public keys. Trust is defined in <code>/etc/containers/policy.json</code>. Trust is enforced when a user attempts to pull an image from a registry. </p>
<p> Trust scope is evaluated by most specific to least specific. In other words, policy may be defined for an entire registry, but refined for a particular repository in that registry. See below for examples. </p>
<p> Trust <code>type</code> provides a way to whitelist (&quot;insecureAcceptAnything&quot;) or blacklist (&quot;reject&quot;) registries. </p>
<p> Signature servers, or <code>sigstores</code>, configure where image signatures are served for a particular registry scope. This cofiguration is a flat list of arbitrarily named YAML files in <code>/etc/containers/registries.d/</code>. Filenames must end in <code>.yaml</code>. A sigstore may be either an absolute path to a local directory (file:///PATH) or a remote web server ( &lt;<a rel="nofollow" href="https://URL">https://URL</a>&gt;). </p>
<p> Trust may be updated using the command <code>atomic trust add</code> for an existing trust scope. </p>
<p> The default trust policy is managed by the default command. Options are <code>accept</code> or <code>reject</code>. </p>
<p> The default <code>/etc/containers/policy.json</code> file may be overriden using environment variable <code>TRUST_POLICY</code>. This is typically only useful for testing. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement. </p>
<p> <code>-k</code> <code>&#8211;pubkeys</code><br />
&nbsp;<wbr>&nbsp;<wbr>A reference to a local file, download URL to an exported public key or a<br />
&nbsp;<wbr>&nbsp;<wbr>local user GPG keyring ID&nbsp;<wbr>(see output of&nbsp;<wbr>&#8216;gpg2 &#8211;list-keys&#8217;). Keys are<br />
&nbsp;<wbr>&nbsp;<wbr>parsed and encoded inline with policy.json. Option may be used multiple<br />
&nbsp;<wbr>&nbsp;<wbr>times to require an image be sigend by multiple keys. One of<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;pubkeys</code>&nbsp;<wbr>or&nbsp;<wbr><code>&#8211;pubkeysfile</code>&nbsp;<wbr>is required for&nbsp;<wbr><code>signedBy</code>&nbsp;<wbr>type. This<br />
&nbsp;<wbr>&nbsp;<wbr>option is recommended over&nbsp;<wbr><code>&#8211;pubkeysfile</code>. </p>
<p> <code>-f</code> <code>&#8211;pubkeysfile</code><br />
&nbsp;<wbr>&nbsp;<wbr>A path to an exported public key on the local system. Key paths<br />
&nbsp;<wbr>&nbsp;<wbr>will be referenced in policy.json. Any path may be used but path<br />
&nbsp;<wbr>&nbsp;<wbr><code>/etc/pki/containers</code>&nbsp;<wbr>is recommended. Option may be used multiple times to<br />
&nbsp;<wbr>&nbsp;<wbr>require an image be sigend by multiple keys. One of&nbsp;<wbr><code>&#8211;pubkeys</code>&nbsp;<wbr>or<br />
&nbsp;<wbr>&nbsp;<wbr><code>&#8211;pubkeysfile</code>&nbsp;<wbr>is required for&nbsp;<wbr><code>signedBy</code>&nbsp;<wbr>type. </p>
<p> <code>&#8211;keytype</code><br />
&nbsp;<wbr>&nbsp;<wbr>The public key type. Default: GPGKeys&nbsp;<wbr>(only supported value) </p>
<p> <code>-t</code> <code>&#8211;type</code><br />
&nbsp;<wbr>&nbsp;<wbr>The trust type for this policy entry. Accepted values:<br />
&nbsp;<wbr><code>signedBy</code>&nbsp;<wbr>(default): Require signatures with corresponding list of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>public keys<br />
&nbsp;<wbr><code>insecureAcceptAnything</code>: do not require any signatures for this<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>registry scope<br />
&nbsp;<wbr><code>reject</code>: do not accept images for this registry scope </p>
<p> <code>-u</code> <code>&#8211;sigstore</code><br />
&nbsp;<wbr>&nbsp;<wbr>A path or remote URL where signatures are found. Prefix filesystem path with<br />
&nbsp;<wbr>&nbsp;<wbr><code>file:///PATH</code>&nbsp;<wbr>and remote web server with&nbsp;<wbr><code> &lt;<a rel="nofollow" href="https://URL[:PORT][/PATH/TO/SIGNATURES">https://URL[:PORT][/PATH/TO/SIGNATURES</a>&gt;]</code>. </p>
<p> <code>-s</code> <code>&#8211;sigstoretype</code><br />
&nbsp;<wbr>&nbsp;<wbr>Type of signature transport. Accepted values:<br />
&nbsp;<wbr><code>web</code>&nbsp;<wbr>(default): remote web server<br />
&nbsp;<wbr><code>atomic</code>: OpenShift-based Atomic Registry API<br />
&nbsp;<wbr><code>local</code>: Local filesystem path </p>
<h2>delete OPTIONS</h2>
<p> <code>&#8211;save-sigstore</code><br />
&nbsp;<wbr>&nbsp;<wbr>Do not remove local sigstore configuration. </p>
<h2>default OPTIONS</h2>
<p> The default trust policy is managed by the default command. Options are <code>accept</code> or <code>reject</code>. </p>
<h2>show OPTIONS</h2>
<p> <code>&#8211;raw</code><br />
&nbsp;<wbr>&nbsp;<wbr>Output trust policy file as raw JSON </p>
<p> <code>-j</code> <code>&#8211;json</code><br />
&nbsp;<wbr>&nbsp;<wbr>Output trust as JSON for machine parsing </p>
<h2>reset</h2>
<p> Resets <code>policy.json</code> to the default. Removes all YAML files in<br />
&nbsp;<wbr>&nbsp;<wbr><code>/etc/containers/registries.d/</code>&nbsp;<wbr>except&nbsp;<wbr><code>default.yaml</code>. </p>
<h2>EXAMPLES</h2>
<p> Add public key trust to specific registry repository </p>
<dl>
<dt>
<dd>
<pre><code>
atomic trust add-- pubkeys / etc / pki / containers / foo[at] example.com-- sigstore https: //s3.bucket/foobar/sigstore/ \
       docker.io/foobar
</code></pre>
</dl>
<p> Modify a trust scope, adding a second public key and changing the sigstore web server </p>
<dl>
<dt>
<dd>
<pre><code>
atomic trust add-- pubkeys https: //example.com/keys/example.pub \
       --pubkeys /etc/pki/containers/foo [at] example.com \
       --sigstore https://server.example.com/foobar/sigstore/ \
       docker.io/foobar
</code></pre>
</dl>
<p> Accept all unsigned images from a registry </p>
<dl>
<dt>
<dd>
<pre>
atomic trust add --type insecureAcceptAnything docker.io
</pre>
</dl>
<p> Remove a trust scope </p>
<dl>
<dt>
<dd>
<pre>
atomic trust delete docker.io
</pre>
</dl>
<p> Remove a trust scope but retain the sigstore configuration </p>
<dl>
<dt>
<dd>
<pre>
atomic trust delete docker.io --sigstore
</pre>
</dl>
<p> Modify default trust policy </p>
<dl>
<dt>
<dd>
<pre>
atomic trust default reject
</pre>
</dl>
<p> Display system trust policy </p>
<dl>
<dt>
<dd>
<pre>
atomic trust show
</pre>
</dl>
<p> Display trust policy file </p>
<dl>
<dt>
<dd>
<pre>
atomic trust show --raw
</pre>
</dl>
<p> Display trust as JSON </p>
<dl>
<dt>
<dd>
<pre>
atomic trust show --json
</pre>
</dl>
<h2>HISTORY</h2>
<p> September 2016, originally compiled by Aaron Weitekamp (aweiteka at redhat dot com) </p>
<h2>Index</h2>
