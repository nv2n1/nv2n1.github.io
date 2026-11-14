---
title: "tracker-fts-cfg(5)"
name: "tracker-fts-cfg"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tracker-fts-cfg/"
description: "tracker-fts.cfg"
---

<p>tracker-fts.cfg</p>
<h2>Synopsis</h2>
<p>$HOME/.config/tracker/tracker-fts.cfg </p>
<h2>Description</h2>
<p>Tracker&#8217;s configuration is built on top of GSettings, part of GLib. This means that there is a proper schema for configurations and they can be viewed (normally) using the <code>dconf-editor</code> tool. Tracker also allows switching from the GSettings database, used by most (cross) desktop applications, to a key/value formatted files (like Microsoft&#8217;s INI format). To do this, the environment variable <code>TRACKER_USE_CONFIG_FILES</code> must be defined before running the application using that configuration. So where is this configuration? Well, normally they&#8217;re stored in <i>$HOME/.config/tracker/</i>, however, default values are not stored to config files, only <code>different</code> values are. This man page describes what keys and values can be used. See EXAMPLES for a general overview. </p>
<h2>Options</h2>
<dl>
<dt><code>max-word-length</code>=30</p>
<dd>
<pre>Words with more characters than this length will be ignored by the indexer.
Values range from 0 to 200.</pre>
<dt><code>max-words-to-index</code>=10000</p>
<dd>
<pre>Indexer will read only this maximum number of words from a single document.</pre>
<dt><code>enable-stemmer</code>=false</p>
<dd>
<pre>Simplify the words to their root to provide more results. E.g. 'shelves' and 'shelf' to 'shel'</pre>
<dt><code>enable-unaccent</code>=true</p>
<dd>
<pre>Translate accented characters to the equivalent unaccented. E.g. 'Idéa' to 'Idea' for improved matching.</pre>
<dt><code>ignore-numbers</code>=true</p>
<dd>
<pre>If enabled, numbers will not be indexed.</pre>
<dt><code>ignore-stop-words</code>=true</p>
<dd>
<pre>If enabled, the words listed in the stop-words list are ignored. E.g. common words like 'the', 'yes', 'no', etc.</pre>
</dl>
<h2>Examples</h2>
<p>The top level group is &quot;General&quot;. The default configuration (if saved to tracker-fts.cfg), would look like: </p>
<pre><code>[General]
max-word-length=30;
max-words-to-index=10000;
enable-stemmer=false;
enable-unaccent=true;
ignore-numbers=true;
ignore-stop-words=true;
</code></pre>
<h2>See Also</h2>
<p><code>tracker-ftsfg</code> </p>
