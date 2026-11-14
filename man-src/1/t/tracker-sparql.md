---
title: "tracker-sparql(1)"
name: "tracker-sparql"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-sparql/"
description: "tracker-sparql – Use SparQL to query the Tracker databases."
---

<h2 class="name">NAME</h2>
<p> tracker-sparql &#8211; Use SparQL to query the Tracker databases.</p>
<h2>SYNOPSIS</h2>
<pre><code>
tracker sparql - q&lt;sparql&gt;[-u] | -f&lt;file&gt;
                                         tracker sparql -
                                     t[class][-s&lt;needle&gt;][-p] tracker sparql[-c][-p][-x][-n[class]][-i[property]][-s&lt;needle&gt;] tracker sparql[--get - longhand&lt;class&gt;][--get - shorthand&lt;class&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command allows probing of the current database schema (also known as ontology) and running low level queries or updates on the data set. In terms of the database ontology, it&#8217;s easy to find out what properties are indexed for speed, or notified on changes, what classes are available and the properties belonging to those classes. There are also visual tools to display an ascii tree layout of the classes and their relationships to each other. </p>
<p> When the caller runs a query, the query is in RDF and SPARQL. This can be done two ways. Either by providing a <i>file</i> with the query or by providing a string with the <i>sparql</i> query. </p>
<p> The <i>file</i> argument can be either a local path or a URI. It also does not have to be an absolute path. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f, &#8211;file</code>=&lt;<i>file</i>&gt;</p>
<dd> Use a <i>file</i> with SPARQL content to query or update.</p>
<dt><code>-q, &#8211;query</code>=&lt;<i>sparql</i>&gt;</p>
<dd> Use a <i>sparql</i> string to query the database with.</p>
<dt><code>-u, &#8211;update</code></p>
<dd> This has to be used with <code>&#8211;query</code>. This tells &quot;tracker sparql&quot; to use the SPARQL update extensions so it knows it isn&#8217;t a regular data lookup request. So if your query is intended to change data in the database, this option is needed.</p>
<dt><code>-c, &#8211;list-classes</code></p>
<dd> Returns a list of classes which describe the ontology used for storing data. These classes are also used in queries. For example, <i><a rel="nofollow" href="http://www.w3.org/2000/01/rdf-schema#Resource">http://www.w3.org/2000/01/rdf-schema#Resource</a></i> is one of many classes which should be returned here.</p>
<dt><code>-x, &#8211;list-class-prefixes</code></p>
<dd> Returns a list of classes and their related prefixes. Prefixes are used to make querying a lot simpler and are much like an alias. For example, <i><a rel="nofollow" href="http://www.w3.org/2000/01/rdf-schema#Resource">http://www.w3.org/2000/01/rdf-schema#Resource</a></i> has the prefix <i>rdfs</i> so queries can be cut down to: </p>
<p> &quot;SELECT ?u WHERE { ?u a rdfs:Resource }&quot; </p>
<dt><code>-p, &#8211;list-properties</code>=[<i>class</i>]</p>
<dd> Returns a list of properties which pertain to a <i>class</i>. You can use both formats here for the <i>class</i>, either the full name <i><a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Video">http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#Video</a></i> or the shortened prefix name <i>nfo:Video</i>. </p>
<p> This gives the following result: </p>
<pre>
$ tracker sparql -p nfo:Video
Properties: 2
  <a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#frameRate">http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#frameRate</a>
  <a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#frameCount">http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#frameCount</a>
</pre>
<p> These properties <i>nfo:frameRate</i> and <i>nfo:frameCount</i> can then be used in queries. </p>
<p> See also <code>&#8211;tree</code> and <code>&#8211;query</code>. </p>
<dt><code>-n, &#8211;list-notifies</code>=[<i>class</i>]</p>
<dd> Returns a list of classes which are notified over D-Bus about any changes that occur in the database. The <i>class</i> does not have to be supplied here. This is optional and filters the results according to any argument supplied. With no <i>class</i>, all classes are listed. </p>
<dt><code>-i, &#8211;list-indexes</code>=[<i>property</i>]</p>
<dd> Returns a list of properties which are indexed in the database. Indexes improves query speed but also add an indexing penalty. The <i>property</i> does not have to be supplied here. This is optional and filters the results according to any argument supplied. With no <i>property</i>, all properties are listed. </p>
<dt><code>-t, &#8211;tree</code>=[<i>class</i>]</p>
<dd> Prints a tree showing all parent classes of <i>class</i> in the ontology. The <i>class</i> can be provided in shorthand or longhand (see <code>&#8211;get-shorthand</code> and <code>&#8211;get-longhand</code> for details). For example: </p>
<p>$ tracker sparql &#8211; t nmo : MMSMessage ROOT + &#8211;rdfs : Resource(C) | +&#8211;nie : InformationElement(C) | | +&#8211;nfo : Document(C) | | | +&#8211;nfo : TextDocument(C) | | | |  `&#8211;nmo : Message(C) | | | | | +&#8211;nmo : PhoneMessage(C) | | | | | |  `&#8211;nmo : MMSMessage(C)</p>
<p> If no <i>class</i> is given, the entire tree is shown. </p>
<p> The <code>&#8211;search</code> command line option can be used to highlight parts of the tree you&#8217;re looking for. The search is case insensitive. </p>
<p> The <code>&#8211;properties</code> command line option can be used to show properties for each class displayed, for example: </p>
<p>$ tracker sparql &#8211; t nfo : FileDataObject &#8211; p ROOT + &#8211;rdfs : Resource(C) | &#8212; &gt; http :                                                                                                                                                                                                     // purl.org/dc/elements/1.1/contributor (P)<br />
                                                                                        | &#8212; &gt; http :                                                                                                                                                                                       // purl.org/dc/elements/1.1/coverage (P)<br />
                                                                                                      | &#8212; &gt; http :                                                                                                                                                                         // purl.org/dc/elements/1.1/creator (P)<br />
                                                                                                                    | &#8212; &gt; http :                                                                                                                                                           // purl.org/dc/elements/1.1/date (P)<br />
                                                                                                                                  | &#8212; &gt; http :                                                                                                                                             // purl.org/dc/elements/1.1/description (P)<br />
                                                                                                                                                | &#8212; &gt; http :                                                                                                                               // purl.org/dc/elements/1.1/format (P)<br />
                                                                                                                                                              | &#8212; &gt; http :                                                                                                                 // purl.org/dc/elements/1.1/identifier (P)<br />
                                                                                                                                                                            | &#8212; &gt; http :                                                                                                   // purl.org/dc/elements/1.1/language (P)<br />
                                                                                                                                                                                          | &#8212; &gt; http :                                                                                     // purl.org/dc/elements/1.1/publisher (P)<br />
                                                                                                                                                                                                        | &#8212; &gt; http :                                                                       // purl.org/dc/elements/1.1/relation (P)<br />
                                                                                                                                                                                                                      | &#8212; &gt; http :                                                         // purl.org/dc/elements/1.1/rights (P)<br />
                                                                                                                                                                                                                                    | &#8212; &gt; http :                                           // purl.org/dc/elements/1.1/source (P)<br />
                                                                                                                                                                                                                                                  | &#8212; &gt; http :                             // purl.org/dc/elements/1.1/subject (P)<br />
                                                                                                                                                                                                                                                                | &#8212; &gt; http :               // purl.org/dc/elements/1.1/title (P)<br />
                                                                                                                                                                                                                                                                              | &#8212; &gt; http : // purl.org/dc/elements/1.1/type (P)<br />
                                                                                                                                                                                                                                                                                            | &#8212; &gt; nao : deprecated(P) | &#8212; &gt; nao : hasTag(P) | &#8212; &gt; nao : identifier(P) | &#8212; &gt; nao : isRelated(P) | &#8212; &gt; nao : lastModified(P) | &#8212; &gt; nao : numericRating(P) | &#8212; &gt; rdf : type(P) | &#8212; &gt; rdfs : comment(P) | &#8212; &gt; rdfs : label(P) | &#8212; &gt; tracker : added(P) | &#8212; &gt; tracker : damaged(P) | &#8212; &gt; tracker : modified(P) | +&#8211;nie : DataObject(C) | | &#8212; &gt; nfo : belongsToContainer(P) | | &#8212; &gt; nie : byteSize(P) | | &#8212; &gt; nie : created(P) | | &#8212; &gt; nie : dataSource(P) | | &#8212; &gt; nie : interpretedAs(P) | | &#8212; &gt; nie : isPartOf(P) | | &#8212; &gt; nie : lastRefreshed(P) | | &#8212; &gt; nie : url(P) | | &#8212; &gt; tracker : available(P) | | +&#8211;nfo : FileDataObject(C) | | | &#8212; &gt; nfo : fileCreated(P) | | | &#8212; &gt; nfo : fileLastAccessed(P) | | | &#8212; &gt; nfo : fileLastModified(P) | | | &#8212; &gt; nfo : fileName(P) | | | &#8212; &gt; nfo : fileOwner(P) | | | &#8212; &gt; nfo : fileSize(P) | | | &#8212; &gt; nfo : hasHash(P) | | | &#8212; &gt; nfo : permissions(P)</p>
<dt><code>-s, &#8211;search</code>=&lt;<i>needle</i>&gt;</p>
<dd> Returns a list of classes and properties which partially match <i>needle</i> in the ontology. This is a case insensitive match, for example: </p>
<pre>
$ tracker sparql -s text
Classes: 4
  <a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#TextDocument">http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#TextDocument</a>
  <a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#PlainTextDocument">http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#PlainTextDocument</a>
  <a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#PaginatedTextDocument">http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#PaginatedTextDocument</a>
  <a rel="nofollow" href="http://www.tracker-project.org/temp/nmm#SynchronizedText">http://www.tracker-project.org/temp/nmm#SynchronizedText</a>
Properties: 4
  <a rel="nofollow" href="http://www.tracker-project.org/ontologies/tracker#fulltextIndexed">http://www.tracker-project.org/ontologies/tracker#fulltextIndexed</a>
  <a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/01/19/nie#plainTextContent">http://www.semanticdesktop.org/ontologies/2007/01/19/nie#plainTextContent</a>
  <a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#plainTextMessageContent">http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#plainTextMessageContent</a>
  <a rel="nofollow" href="http://www.tracker-project.org/temp/scal#textLocation">http://www.tracker-project.org/temp/scal#textLocation</a>
</pre>
<p> See also <code>&#8211;tree</code>. </p>
<dt><code>&#8211;get-shorthand</code>=&lt;<i>class</i>&gt;</p>
<dd> Returns the shorthand for a class given by a URL. For example: </p>
<pre>
$ tracker sparql --get-shorthand <a rel="nofollow" href="http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#plainTextMessageContent">http://www.semanticdesktop.org/ontologies/2007/03/22/nmo#plainTextMessageContent</a>
nmo:plainTextMessageContent
</pre>
<dt><code>&#8211;get-longhand</code>=&lt;<i>class</i>&gt;</p>
<dd> Returns the longhand for a class given in the form of CLASS:PROPERTY. For example: </p>
<pre>
$ tracker sparql --get-longhand nmm:MusicPiece
<a rel="nofollow" href="http://www.tracker-project.org/temp/nmm#MusicPiece">http://www.tracker-project.org/temp/nmm#MusicPiece</a>
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRACKER_SPARQL_BACKEND</code></p>
<dd> This option allows you to choose which backend you use for connecting to the database. This choice can limit your functionality. There are three settings. </p>
<p> With &quot;<code>direct</code>&quot; the connection to the database is made directly to the file itself on the disk, there is no intermediary daemon or process. The &quot;<code>direct</code>&quot; approach is purely <i>read-only</i>. </p>
<p> With &quot;<code>bus</code>&quot; the <code>tracker-store</code> process is used to liase with the database queuing all requests and managing the connections via an IPC / D-Bus. This adds a small overhead <i>BUT</i> this is the only approach you can use if you want to <i>write</i> to the database. </p>
<p> With &quot;<code>auto</code>&quot; the backend is decided for you, much like it would be if this environment variable was undefined. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>List all classes</p>
<dd>
<pre>
$ tracker sparql -q &quot;SELECT ?cl WHERE { ?cl a rdfs:Class }&quot;
</pre>
<dt>List all properties for the Resources class (see &#8211;list-properties)</p>
<dd>
<pre>
$ tracker sparql -q &quot;SELECT ?prop WHERE {
      ?prop a rdf:Property ;
      rdfs:domain &lt;<a rel="nofollow" href="http://www.w3.org/2000/01/rdf-schema#Resource">http://www.w3.org/2000/01/rdf-schema#Resource</a>&gt;
 }&quot;
</pre>
<dt>List all class namespace prefixes</p>
<dd>
<pre>
$ tracker sparql -q &quot;SELECT ?prefix ?ns WHERE {
      ?ns a tracker:Namespace ;
      tracker:prefix ?prefix
  }&quot;
</pre>
<dt>List all music files</p>
<dd>
<pre>
$ tracker sparql -q &quot;SELECT ?song WHERE { ?song a nmm:MusicPiece }&quot;
</pre>
<dt>List all music albums, showing title, track count, and length in seconds.</p>
<dd>
<p>$ tracker sparql -q &#8220;SELECT ?title COUNT(?song)<br />
                     AS songs<br />
                     SUM(?length) AS totallength<br />
                     WHERE<br />
{<br />
    ? album a nmm : MusicAlbum;<br />
nie:<br />
    title ? title.<br />
                ? song nmm<br />
                : musicAlbum<br />
                ? album;<br />
nfo:<br />
    duration ? length<br />
}<br />
GROUP BY ? album &#8221;</p>
<dt>List all music from a particular artist</p>
<dd>
<p>$ tracker sparql &#8211; q &#8220;SELECT ?song ?title WHERE {<br />
    ? song nmm<br />
    : performer [nmm:artistName &#8216;Artist Name&#8217;];<br />
nie : title ? title<br />
}<br />
&#8221;</p>
<dt>Set the played count for a song</p>
<dd>
<p>$ tracker sparql &#8211; u &#8211; q &#8220;DELETE {<br />
    &lt; file: /// home/user/Music/song.mp3&gt; nie:usageCounter ?count<br />
}<br />
WHERE{<br />
    &lt; file : /// home/user/Music/song.mp3&gt; nie:usageCounter ?count<br />
} INSERT<br />
{<br />
    &lt; file: /// home/user/Music/song.mp3&gt; nie:usageCounter 42<br />
}<br />
&#8221;</p>
<dt>List all image files</p>
<dd>
<pre>
$ tracker sparql -q &quot;SELECT ?image WHERE { ?image a nfo:Image }&quot;
</pre>
<dt>List all image files with a specific tag</p>
<dd>
<p>$ tracker sparql &#8211; q &#8220;SELECT ?image WHERE {<br />
    ? image a nfo<br />
    : Image;<br />
nao : hasTag [nao:prefLabel &#8216;tag&#8217;]<br />
}<br />
&#8221;</p>
<dt>List all image files created on a specific month and order by date</p>
<dd>
<pre><code>
$ tracker sparql - q "SELECT ?image ?date WHERE {
    ? image a nfo
    : Image;
nie : contentCreated ? date.FILTER(? date &gt;= '2008-07-01T00:00:00' &amp;&amp;
                                   ? date &lt; '2008-08-01T00:00:00')
}
ORDER BY ? date "
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-sql/">tracker-sql</a></code>(1), <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1).</p>
<dl>
<dt><code><a rel="nofollow" href="http://nepomuk.semanticdesktop.org/">http://nepomuk.semanticdesktop.org/</a></code></p>
<dd>
<dt><code><a rel="nofollow" href="http://www.w3.org/TR/rdf-sparql-query/">http://www.w3.org/TR/rdf-sparql-query/</a></code></p>
<dd>
</dl>
<h2>Index</h2>
