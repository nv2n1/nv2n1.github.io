---
title: "elasticdump(1)"
name: "elasticdump"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elasticdump/"
description: "elasticdump – Import and export tools for elasticsearch"
---

<h2>NAME</h2>
<p> elasticdump &#8211; Import and export tools for elasticsearch</p>
<h2>SYNOPSIS</h2>
<p> <code>elasticdump</code> <i>,&#8211;input SOURCE &#8211;output DESTINATION /</i>[<i>,OPTIONS/</i>]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>&#8211;input</code></p>
<dd> Source location (required)</p>
<dt><code>&#8211;output</code></p>
<dd> Destination location (required)</p>
<dt><code>&#8211;limit</code></p>
<dd> How many objects to move in bulk per operation (default: 100)</p>
<dt><code>&#8211;debug</code></p>
<dd> Display the elasticsearch commands being used (default: false)</p>
<dt><code>&#8211;type</code></p>
<dd> What are we exporting? (default: data, options: [data, mapping])</p>
<dt><code>&#8211;delete</code></p>
<dd> Delete documents one-by-one from the input as they are moved. Will not delete the source index</p>
<dt>
<dd> (default: false)</p>
<dt><code>&#8211;searchBody</code></p>
<dd> Preform a partial extract based on search results (when ES is the input, default: &#8216;{&quot;query&quot;: { &quot;match_all&quot;: {} } }&#8217;)</p>
<dt><code>&#8211;all</code></p>
<dd> Load/store documents from ALL indexes (default: false)</p>
<dt><code>&#8211;bulk</code></p>
<dd> Leverage elasticsearch Bulk API when writing documents (default: false)</p>
<dt><code>&#8211;ignore-errors</code></p>
<dd> Will continue the read/write loop on write error (default: false)</p>
<dt><code>&#8211;scrollTime</code></p>
<dd> Time the nodes will hold the requested search in order. (default: 10m)</p>
<dt><code>&#8211;maxSockets</code></p>
<dd> How many simultaneous HTTP requests can we process make? (default: 5 [node &lt;= v0.10.x] / Infinity [node &gt;= v0.11.x] )</p>
<dt><code>&#8211;bulk-use-output-index-name</code></p>
<dd> Force use of destination index name (the actual output URL) as destination while bulk writing to ES. Allows leveraging Bulk API copying data inside the same elasticsearch instance. (default: false)</p>
<dt><code>&#8211;timeout</code></p>
<dd> Integer containing the number of milliseconds to wait for a request to respond before aborting the request. Passed directly to the request library. If used in bulk writing, it will result in the entire batch not being written. Mostly used when you don&#8217;t care too much if you lose some data when importing but rather have speed.</p>
<dt><code>&#8211;skip</code></p>
<dd> Integer containing the number of rows you wish to skip ahead from the input transport. When importing a large index, things can go wrong, be it connectivity, crashes, someone forgetting to `screen`, etc. This allows you to start the dump again from the last known line written (as logged by the `offset` in the output). Please be advised that since no sorting is specified when the dump is initially created, there&#8217;s no real way to guarantee that the skipped rows have already been written/parsed. This is more of an option for when you want to get most data as possible in the index without concern for losing some rows in the process, gsimilar to the `timeout` option.</p>
<dt><code>&#8211;inputTransport</code></p>
<dd> Provide a custom js file to us as the input transport</p>
<dt><code>&#8211;outputTransport</code></p>
<dd> Provide a custom js file to us as the output transport</p>
<dt><code>&#8211;help</code></p>
<dd> This page</dl>
<h2>EXAMPLES</h2>
<p> Copy an index from production to staging with mappings:</p>
<dl>
<dt>
<pre><code>
elasticdump-- input = http :                               //production.es.com:9200/my_index \
--output=http://staging.es.com:9200/my_index \
--type=mapping
                             elasticdump \--input = http : //production.es.com:9200/my_index \
--output=http://staging.es.com:9200/my_index \
--type=data

                                                           Backup index data to a file :

    elasticdump \--input = http :                               //production.es.com:9200/my_index \
--output=/data/my_index_mapping.json \
--type=mapping
                                  elasticdump \--input = http : //production.es.com:9200/my_index \
--output=/data/my_index.json \
--type=data

                                                                Backup and index to a gzip using stdout :

    elasticdump \--input = http : //production.es.com:9200/my_index \
--output=$ \
| gzip &gt; /data/my_index.json.gz

                                  Backup ALL indices,
              then use Bulk API to populate another ES cluster :

    elasticdump \--all = true --input = http :                                                                                 //production-a.es.com:9200/ \
--output=/data/production.json
                                               elasticdump \--bulk = true --input = / data / production.json-- output = http : // production-b.es.com:9200/

                                                                                                                               Backup the results of a query to a file :

    elasticdump \--input = http: //production.es.com:9200/my_index \
--output=query.json \
--searchBody '{"query":{"term":{"username": "admin"}}}'
</code></pre>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="https://github.com/taskrabbit/elasticsearch-dump">https://github.com/taskrabbit/elasticsearch-dump</a> </p>
<h2>Index</h2>
