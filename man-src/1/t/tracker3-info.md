---
title: "tracker3-info(1)"
name: "tracker3-info"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-info/"
description: "tracker3-info – Retrieve all information available for a certain file."
---

<h2 class="name">NAME</h2>
<p> tracker3-info &#8211; Retrieve all information available for a certain file. </p>
<h2>SYNOPSIS</h2>
<p> <code>tracker3 info</code> [<i>options</i>&#8230;] &lt;<i>file1</i>&gt; [[<i>file2</i>] &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>tracker3 info</code> asks for all the known metadata available for the given <i>file</i>. </p>
<p> Multiple <i>file</i> arguments can be provided to retrieve information about multiple files. </p>
<p> The <i>file</i> argument can be either a local path or a URI. It also does not have to be an absolute path.</p>
<h2>OPTIONS</h2>
<p> <code>-f, &#8211;full-namespaces</code></p>
<dl>
<dt>
<dd> By default, all keys and values reported about any given <i>file</i> are returned in shortened form, for example, <i>nie:title</i> is shown instead of <i><a rel="nofollow" href="http://tracker.api.gnome.org/ontology/v3/nie#title">http://tracker.api.gnome.org/ontology/v3/nie#title</a></i>. This makes things much easier to see generally and the output is less cluttered. This option reverses that so FULL namespaces are shown instead.</dl>
<p> <code>-c, &#8211;plain-text-content</code></p>
<dl>
<dt>
<dd> If the resource being displayed has nie:PlainTextContent (i.e. information about the content of the resource, which could be the contents of a file on the disk), then this option displays that in the output.</dl>
<p> <code>-i, &#8211;resource-is-iri</code></p>
<dl>
<dt>
<dd> In most cases, the <i>file</i> argument supplied points to a URL or PATH which is queried for according to the resource associated with it by <i>nie:url</i>. However, in cases where the <i>file</i> specified turns out to be the actual URN itself, this argument is required to tell &quot;tracker3 info&quot; not to do the extra step of looking up the URN related by <i>nie:url</i>.</dl>
<p> For example, consider that you store URNs by the actual URL itself and use the unique nie:url in another resource (which is quite reasonable when using containers and multi-resource conditions), you would need this argument to tell &quot;tracker3 info&quot; that the <i>file</i> supplied is actually a URN not URL. </p>
<p> <code>-t, &#8211;turtle</code></p>
<dl>
<dt>
<dd> Output results as Turtle RDF. If -f is enabled, full URIs are shown for subjects, predicates and objects; otherwise, shortened URIs are used, and all the prefixes Tracker knows about are printed at the top of the output.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-sparql/">tracker3-sparql</a></code>(1). </p>
<p> <code><a rel="nofollow" href="http://nepomuk.semanticdesktop.org/">http://nepomuk.semanticdesktop.org/</a></code> <code><a rel="nofollow" href="http://www.w3.org/TR/rdf-sparql-query/">http://www.w3.org/TR/rdf-sparql-query/</a></code> </p>
<h2>Index</h2>
