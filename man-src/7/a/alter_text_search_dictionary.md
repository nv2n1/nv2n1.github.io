---
title: "alter_text_search_dictionary(7)"
name: "alter_text_search_dictionary"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_text_search_dictionary/"
---


 </p>
<h2>NAME</h2>
<p> ALTER TEXT SEARCH DICTIONARY &#8211; change the definition of a text search dictionary </p>
<h2>SYNOPSIS</h2>
<pre><code>ALTER TEXT SEARCH DICTIONARY name  ( option  [ = value  ] [, ... ]
)
ALTER TEXT SEARCH DICTIONARY name  RENAME TO newname ALTER TEXT SEARCH DICTIONARY name  OWNER TO newowner 
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ALTER TEXT SEARCH DICTIONARY</code> changes the definition of a text search dictionary. You can change the dictionary&#8217;s template-specific options, or change the dictionary&#8217;s name or owner. </p>
<p> You must be the owner of the dictionary to use <code>ALTER TEXT SEARCH DICTIONARY</code>.  </p>
<h2>PARAMETERS</h2>
<dl>
<dt><i>name</i></dt>
<dd> <p> The name (optionally schema-qualified) of an existing text search dictionary. </p>
 </dd>
<dt><i>option</i></dt>
<dd> <p> The name of a template-specific option to be set for this dictionary. </p>
 </dd>
<dt><i>value</i></dt>
<dd> <p> The new value to use for a template-specific option. If the equal sign and value are omitted, then any previous setting for the option is removed from the dictionary, allowing the default to be used. </p>
 </dd>
<dt><i>newname</i></dt>
<dd> <p> The new name of the text search dictionary. </p>
 </dd>
<dt><i>newowner</i></dt>
<dd> <p> The new owner of the text search dictionary. </p>
 </dd></dl>
<p> Template-specific options can appear in any order. </p>
<h2>EXAMPLES</h2>
<p> The following example command changes the stopword list for a Snowball-based dictionary. Other parameters remain unchanged. </p>
<pre><code>ALTER TEXT SEARCH DICTIONARY my_dict ( StopWords = newrussian );
</code></pre>
<p> The following example command changes the language option to dutch, and removes the stopword option entirely. </p>
<pre><code>ALTER TEXT SEARCH DICTIONARY my_dict ( language = dutch, StopWords );
</code></pre>
<p> The following example command ``updates&#8217;&#8216; the dictionary&#8217;s definition without actually changing anything. </p>
<pre><code>ALTER TEXT SEARCH DICTIONARY my_dict ( dummy );
</code></pre>
<p> (The reason this works is that the option removal code doesn&#8217;t complain if there is no such option.) This trick is useful when changing configuration files for the dictionary: the <code>ALTER</code> will force existing database sessions to re-read the configuration files, which otherwise they would never do if they had read them earlier.  </p>
<h2>COMPATIBILITY</h2>
<p> There is no <code>ALTER TEXT SEARCH DICTIONARY</code> statement in the SQL standard.  </p>
<h2>SEE ALSO</h2>
<p> CREATE TEXT SEARCH DICTIONARY [<code><a href="/docs/linux/man/7-create_text_search_dictionary/">create_text_search_dictionary</a></code>(7)], DROP TEXT SEARCH DICTIONARY [<code><a href="/docs/linux/man/7-drop_text_search_dictionary/">drop_text_search_dictionary</a></code>(7)] </p>
<h2>Index</h2>
