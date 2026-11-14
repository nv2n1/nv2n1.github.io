---
title: "v(1)"
name: "v"
section: "1"
letter: "v"
url: "/docs/linux/man/1-v/"
description: "v.what.vect – Uploads vector values at positions of vector points to the table."
---

<h2>NAME</h2>
<p> <i></i><code>v.what.vect</code> &#8211; Uploads vector values at positions of vector points to the table.</p>
<h2>KEYWORDS</h2>
<p> vector, database, attribute table</p>
<h2>SYNOPSIS</h2>
<p> <code>v.what.vect</code><br />
 <code>v.what.vect help</code><br />
 <code>v.what.vect vector</code>=<i>name</i> [<code>layer</code>=<i>integer</i>] <code>column</code>=<i>string</i> <code>qvector</code>=<i>name</i> [<code>qlayer</code>=<i>integer</i>] <code>qcolumn</code>=<i>string</i> [&#8211;<code>verbose</code>] [&#8211;<code>quiet</code>]</p>
<h3>Parameters:</h3>
<dl>
<dt><code>vector</code>=<i>name</i></p>
<dd>
 Points vector map to modify</p>
<dt><code>layer</code>=<i>integer</i></p>
<dd>
 Layer in the vector to be modified<br />
 Default: <i>1</i></p>
<dt><code>column</code>=<i>string</i></p>
<dd>
 Column to be updated with the query result</p>
<dt><code>qvector</code>=<i>name</i></p>
<dd>
 Vector map to be queried</p>
<dt><code>qlayer</code>=<i>integer</i></p>
<dd>
 Layer of the query vector containg data<br />
 Default: <i>1</i></p>
<dt><code>qcolumn</code>=<i>string</i></p>
<dd>
 Column to be queried</dl>
<h2>DESCRIPTION</h2>
<p> <i>v.what.vect</i> transfers attributes from the <code>qvector</code>&#8216;s map attribute table into the attribute table of points present in the <code>vector</code> map. The script is based on <i>v.distance</i>.</p>
<h2>NOTES</h2>
<p> The upload <code>column</code>, into which the query results are stored, must be present in the <code>vector</code> map. Use <i>v.db.addcol</i> to add one if needed. </p>
<p> This module only uploads attributes which exist at the exact positions of the input&#8217;s <code>vector</code> points. For a &quot;nearest feature&quot; fit, use <i>v.distance</i> instead. </p>
<p> In case of a multipoint input <code>vector</code> map, with several points having the same category number, it can happen, that the query result is NULL, if the same category number falls into different <code>qvector</code> polygons.</p>
<h2>EXAMPLE</h2>
<p> In this example, the &#8216;archsites&#8217; point map in the Spearfish location is copied to the current mapset, a new attribute column is added and the owner names from the &#8216;fields&#8217; polygon map are transferred to the &#8216;myarchsites&#8217; map at points&#8217; locations:<br />
 g.copy vect=archsites,myarchsites<br />
 v.db.addcol myarchsites col=&quot;owner varchar(25)&quot;<br />
 v.what.vect myarchsites qvect=fields column=owner qcolumn=label<br />
 # verification:<br />
 v.db.select myarchsites </p>
<h2>SEE ALSO</h2>
<p> <i> v.db.addcol, v.db.select, v.distance, v.rast.stats, v.what.rast </i></p>
<h2>AUTHOR</h2>
<p> Markus Neteler </p>
<p> <i>Last changed: $Date: 2007-06-10 13:23:21 +0200 (Sun, 10 Jun 2007) $</i> </p>
<p> Full index </p>
<p> � 2003-2008 GRASS Development Team </p>
<h2>Index</h2>
