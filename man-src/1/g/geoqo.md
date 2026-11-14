---
title: "geoqo(1)"
name: "geoqo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-geoqo/"
description: "geoqo – Geocaching DataBase"
---

<h2 class="name">NAME</h2>
<p> geoqo &#8211; Geocaching DataBase </p>
<h2>ABOUT GeoQO</h2>
<p> The geoqo program is designed to be: </p>
<pre>
  - usable with a graphical user interface
  - usable on the command line
  - fast (uses a database  (mysql, postgresql, sqlite2 or sqlite supported)
  - highly extensible.  It's easy to:
    - add new search types
    - add new import routines
    - add new export routines
    - add new display routines
    - add new modification plugins
    - ...
  - A very extensive scripting ability that can automatically create
    GUI screens from script definitions.
  - In summary, you should be able to control your data.
</pre>
<h2>DOCUMENT CONVENTIONS</h2>
<p> The documentation uses the following structures for examples: </p>
<pre>
      &gt; geoqo -argument value
      output line 1
      output line 2
</pre>
<p> In the above example, &#8220;&gt;&#8221; is the command prompt. &#8220;geoqo -argument value&#8221; is an example command, and &#8220;output line 1&#8221; (and 2) would be the example output it might give.</p>
<h2>Tutorials and Other Documentation</h2>
<p> Make sure you check out the wiki pages as well, which provide tutorials, tips and tricks, FAQs, and other documentation: </p>
<pre>
  <a rel="nofollow" href="http://www.geoqo.org/wiki/">http://www.geoqo.org/wiki/</a>
</pre>
<p> This document discusses how to use geoqo using the command line syntax. For instructions on using the <font SIZE="-1">GUI</font>, please see the tutorial on the wiki web page above which contains screen-shot walk throughs.</p>
<h2>QUICK OVERVIEW</h2>
<p> Import a file: </p>
<pre>
  geoqo -i filetoimport.gpx
</pre>
<p> Search for and list all caches owned by Yamar </p>
<pre>
  geoqo -s cache:owner_name=Yamar -d list
</pre>
<p> Display result number 3 from the last search: </p>
<pre>
  geoqo -s 3 -d show
</pre>
<p> Export your search to a new file (in this case, the last search [Yamar&#8217;s caches] since a new -s flag wasn&#8217;t specified) </p>
<pre>
  geoqo -e filetoexport.gpx
</pre>
<p> List geocache data sets (includes imports, searches, etc) </p>
<pre>
  geoqo -d sets
</pre>
<p> Show stats about your data: </p>
<pre>
  geoqo -d stats
</pre>
<h2>THE LONG, LONG MANUAL</h2>
<p> GeoQO is very powerful. Thus, you&#8217;ll find that this manual is long. It&#8217;s divided up into sections based on the types of things geoqo can do: setup, import, search, display, modify, and export. </p>
<p> Make sure you check out the wiki pages as well, which provide tips and tricks, FAQs, and other documentation: </p>
<pre>
  <a rel="nofollow" href="http://www.geoqo.org/wiki/">http://www.geoqo.org/wiki/</a>
</pre>
<p> Have I mentioned the wiki yet?</p>
<h2>Help Is Nearby</h2>
<p> The -d switch (you&#8217;ll learn about this later) displays things. One of the things it can display is &#8220;help&#8221;. To get help at any time, run: </p>
<pre>
  &gt; geoqo -d help
</pre>
<p> To get started with the help system. To get help about a particular topic, include the major type and a slash (/) and the subtype. For example, Get get information about importing gpx files: </p>
<pre>
  &gt; geoqo -d help:topic=import/gpx
</pre>
<p> To get a list of the particular subtypes for a given section, look up the major section: </p>
<pre>
  &gt; geoqo -d help:topic=import
</pre>
<p> And it will list all of the subtyes (in the example above, it would display a list of all the import types).</p>
<h2>DATABASE SETUP</h2>
<p> Database setup is automatic for the default database. You can, however, create as many databases using other file names as you want (but why?). </p>
<pre>
      &gt; geoqo --db-name otherdb --setup-database
</pre>
<h2>IMPORTING DATA</h2>
<p> To import an existing pocket query or other gpx file, simply use the -i switch: </p>
<pre>
      &gt; geoqo -i somefile.gpx
</pre>
<p> You can import multiple files: </p>
<pre>
      &gt; geoqo -i somefile.gpx,someotherfile.zip
</pre>
<p> Note that most importing plugins do store things in &#8220;sets&#8221;. See sections further below for more details on what a &#8220;set&#8221; is and how useful they can be. </p>
<p> File import types currently available:</p>
<h2>Import Gpx:</h2>
<pre>
  &gt; geoqo -i myfile.gpx
  &gt; geoqo -i gpx:setname=myname:myfile.gpx
</pre>
<p> The gpx importer imports gpx files taken from the geocaching.com site (and probably many other sites too, but only geocaching.com <font SIZE="-1">GPX</font> files have been tested so for) and imports the data into your geoqo database. </p>
<p> <i>Options:</i></p>
<dl>
<dt>setname:</p>
<dd> Uses setname as the name of geoqo <font SIZE="-1">SET</font> to create based on the data. Normally this is extracted from the <i>name</i> field within the gpx file itself and prepended with &#8220;import:&#8221;. <font SIZE="-1">IE</font>, if you had a pocket query named &#8220;my search&#8221; then, when you imported the gpx file into geoqo, you&#8217;d get a new set named &#8220;import:my search&#8221;.</dl>
<h2>Import Zip:</h2>
<pre>
  &gt; geoqo -i myfile.zip
</pre>
<p> The <i>zip</i> importer allows you to simply specify a zip file for importing instead of having to unzip it yourself. It expects the contents of the zip file to be named similar to the zip file itself, just like groundspeak sends them out for geocaching.com pocket queries. <font SIZE="-1">IE</font>, if you import &#8220;111111.zip&#8221; it&#8217;ll try to unzip it and then import the contained 111111.gpx file. It&#8217;ll also try to import the 1111111-wpts.gpx file, if one existed as well. </p>
<p> Note: using this importer requires you to have <code>unzip</code> installed on your system. </p>
<p> <i>Options:</i></p>
<dl>
<dt>setname:</p>
<dd> Uses setname as the name of geoqo <font SIZE="-1">SET</font> to create based on the data. Normally this is extracted from the <i>name</i> field within the gpx file itself and prepended with &#8220;import:&#8221;. <font SIZE="-1">IE</font>, if you had a pocket query named &#8220;my search&#8221; then, when you imported the gpx file into geoqo, you&#8217;d get a new set named &#8220;import:my search&#8221;.</p>
<dt>tmpdir:</p>
<dd> The zip importer works by copying the zip file to a tmpdir and then unzipping it there. This is normally set to <i></i>$HOME<i>/.geoqo/tmpdir</i>. This option lets you override that default. </p>
<p> default: /home/hardaker/.geoqo/temp</dl>
<h2>Import Dir:</h2>
<pre>
  &gt; geoqo -i /path/to/directory/
</pre>
<p> The <i>dir</i> importer allows you to simply specify a directory (&#8220;folder&#8221;) to attempt to read every file from. It will skip any file types it does not understand. </p>
<p> <i>Options:</i></p>
<dl>
<dt>setname:</p>
<dd> Uses setname as the name of geoqo <font SIZE="-1">SET</font> to create based on the data. Normally this is extracted from the <i>name</i> field within the gpx file itself and prepended with &#8220;import:&#8221;. <font SIZE="-1">IE</font>, if you had a pocket query named &#8220;my search&#8221; then, when you imported the gpx file into geoqo, you&#8217;d get a new set named &#8220;import:my search&#8221;.</p>
<dt>tmpdir:</p>
<dd> The zip importer works by copying the zip file to a tmpdir and then unzipping it there. This is normally set to <i></i>$HOME<i>/.geoqo/tmpdir</i>. This option lets you override that default. </p>
<p> default: /home/hardaker/.geoqo/temp</dl>
<h2>Import Loc:</h2>
<pre>
  &gt; geoqo -i myfile.loc
  &gt; geoqo -i loc:setname=myname:myfile.loc
</pre>
<p> The loc importer imports loc files taken from the geocaching.com and waymarking.com site (and probably many other sites too, but only geocaching.com and waymarking.com <font SIZE="-1">LOC</font> files have been tested so for) and imports the data into your geoqo database. </p>
<p> <i>Options:</i></p>
<dl>
<dt>setname:</p>
<dd> Uses setname as the name of geoqo <font SIZE="-1">SET</font> to create based on the data. Normally this is extracted from the <i>name</i> field within the gpx file itself and prepended with &#8220;import:&#8221;. <font SIZE="-1">IE</font>, if you had a pocket query named &#8220;my search&#8221; then, when you imported the gpx file into geoqo, you&#8217;d get a new set named &#8220;import:my search&#8221;.</dl>
<h2>Import Base64:</h2>
<pre>
  &gt; cat message | geoqo -i base64:-
</pre>
<p> The <i>base64</i> importer allows you to send mail messages with encoded pocket queries directly to geoqo for decoding, unzipping, extracting and importing. </p>
<p> Note: using this importer requires you to have <code>MIME::Base64</code> installed on your system. Most modern perl packages contain this out of the box. </p>
<p> <i>Options:</i></p>
<dl>
<dt>setname:</p>
<dd> Uses setname as the name of geoqo <font SIZE="-1">SET</font> to create based on the data. Normally this is extracted from the <i>name</i> field within the gpx file itself and prepended with &#8220;import:&#8221;. <font SIZE="-1">IE</font>, if you had a pocket query named &#8220;my search&#8221; then, when you imported the gpx file into geoqo, you&#8217;d get a new set named &#8220;import:my search&#8221;.</p>
<dt>tmpdir:</p>
<dd> The zip importer works by copying the zip file to a tmpdir and then unzipping it there. This is normally set to <i></i>$HOME<i>/.geoqo/tmpdir</i>. This option lets you override that default. </p>
<p> default: /home/hardaker/.geoqo/temp</dl>
<h2>Import Wigle:</h2>
<pre>
  &gt; geoqo -i myfile.wigle
  &gt; geoqo -i wigle:setname=myname:mywiglefile
</pre>
<p> The wigle importer imports wigle files taken from the geocaching.com and waymarking.com site (and probably many other sites too, but only geocaching.com and waymarking.com <font SIZE="-1">WIGLE</font> files have been tested so for) and imports the data into your geoqo database. </p>
<p> <i>Options:</i></p>
<dl>
<dt>setname:</p>
<dd> Uses setname as the name of geoqo <font SIZE="-1">SET</font> to create based on the data.</dl>
<h2>Import System:</h2>
<pre>
  &gt; geoqo -i &quot;system:gpsbabel -i garmin -f /dev/ttyS0 -o gpx -F %{file:gpx}&quot;
</pre>
<p> The <i>system</i> importer allows you to simply specify a command to run which generates a file of a type that geoqo can actually import. For example, the above command runs gpsbabel to import all the waypoints stored in a <font SIZE="-1">GPS</font> on a unix system (/dev/ttyS0 is the name of a serial device on a linux machine). </p>
<p> <i>Options:</i></p>
<dl>
<dt>cmd:</p>
<dd> It must contain a %{file:TYPE} string that indicates where the output file will be stored, but the path and the name of that file will be created by geoqo. Example gpsbable arguments would be -o gpx -F %{file:gpx}</p>
<dt>setname:</p>
<dd> Uses setname as the name of geoqo <font SIZE="-1">SET</font> to create based on the data. Normally this is extracted from the <i>name</i> field within the gpx file itself and prepended with &#8220;import:&#8221;. <font SIZE="-1">IE</font>, if you had a pocket query named &#8220;my search&#8221; then, when you imported the gpx file into geoqo, you&#8217;d get a new set named &#8220;import:my search&#8221;. However if your system command doesn&#8217;t properly name the resulting file, this can be used to override it.</p>
<dt>tmpdir:</p>
<dd> The temporary directory to use </p>
<p> default: /home/hardaker/.geoqo/temp</dl>
<h2>Import Create:</h2>
<pre>
  &gt; geoqo -i create:ident=home,lat=N38
</pre>
<p> The <i>create</i> import plugin lets you create new waypoints and inserts them into the database. The list of options is quite long as each type supported by a given supported waypoint system (geocaching, geodining, &#8230;) requires an appropriate set of fields. Running geoqo simply as: </p>
<pre>
  &gt; geoqo -i create
</pre>
<p> should bring up a <font SIZE="-1">GUI</font> form which will prompt you for the needed information. Leave anything out that isn&#8217;t appropriate for the waypoint type you&#8217;re creating. </p>
<p> <i>Options:</i></p>
<dl>
<dt>type:</p>
<dd> default: Waypoint</p>
<dt>ident:</p>
<dd>
<dt>setname:</p>
<dd> default: created</p>
<dt>desc:</p>
<dd>
<dt>lat:</p>
<dd>
<dt>lon:</p>
<dd>
<dt>sym:</p>
<dd>
<dt>time:</p>
<dd>
<dt>subtype:</p>
<dd>
<dt>url:</p>
<dd>
<dt>urlname:</p>
<dd>
<dt>cmt:</p>
<dd></dl>
<h2>Import Average:</h2>
<pre>
  &gt; geoqo -i average:ident=newwaypoint,from1=oldwaypoint1,from2=oldwaypoint2
</pre>
<p> The <i>average</i> import plugin lets you create a new waypoint by averaging the latitude and longitude of a number of other waypoints. Useful to find the center of a number of waypoints, which is required for a number of geocaching puzzle caches. </p>
<p> <i>Options:</i></p>
<dl>
<dt>ident:</p>
<dd>
<dt>type:</p>
<dd> default: Waypoint</p>
<dt>from1:</p>
<dd>
<dt>from2:</p>
<dd>
<dt>setname:</p>
<dd> default: created</dl>
<h2>Import Project:</h2>
<p> <font SIZE="-1">XXXXX</font> <font SIZE="-1">DO</font> <font SIZE="-1">NOT</font> <font SIZE="-1">USE</font> <font SIZE="-1">THIS</font> <font SIZE="-1">PLUGIN</font>; <font SIZE="-1">IT</font> <font SIZE="-1">IS</font> <font SIZE="-1">NOT</font> <font SIZE="-1">FINISHED</font> <font SIZE="-1">XXXXX</font> </p>
<pre>
  &gt; geoqo -i project:ident=newwaypoint,from=oldwaypoint,distance=528,direction=45
</pre>
<p> The <i>project</i> import plugin lets you project a new waypoint which is a distance from an older one. </p>
<p> <i>Options:</i></p>
<dl>
<dt>ident:</p>
<dd>
<dt>type:</p>
<dd>
<dt>from:</p>
<dd>
<dt>distance:</p>
<dd> default: 0</p>
<dt>direction:</p>
<dd> default: 0</p>
<dt>setname:</p>
<dd> default: created</dl>
<h2>SEARCHING THE DATABASE</h2>
<p> The search system in geoqo is highly flexible and extensible. It supports multiple types of searching, which are documented below. The &#8220;-s&#8221; or &#8220;&#8211;search&#8221;. The format of the search field is as follows: </p>
<pre>
  type:terms
</pre>
<p> Type is the type of search you want to do. This can be any of the types shown further below, or any types provided by a plugin. For those that want to write search plugins, please run &#8220;perldoc GeoDB::Search&#8221; to learn how to write search plugins. </p>
<p> Note: searching does nothing if you&#8217;re not going to act on the results. Thus, you should at least provide a -l, -S or -e flag to list, show, or export the results. All the examples below are using the -l flag. </p>
<p> Search types are as follows:</p>
<h2>Search Cache:</h2>
<pre>
  &gt; geoqo -s cache:name=unusual -d count
  Search/Set Count: 6
</pre>
<p> Searchs the database for only waypoints that are of type &#8216;Geocache&#8217; and conform to the terms given. See the documentation on the waypoint: search type for further details on how to use it because everything else is the same. </p>
<p> Possible search columns for geocaches include the following, beyond those listed in the waypoint section: </p>
<pre>
        available
        archived
        groundspeak_name
        groundspeak_placed_by
        groundspeak_owner_id
        groundspeak_owner_name
        groundspeak_type
        groundspeak_container
        groundspeak_difficulty
        groundspeak_terrain
        groundspeak_country
        groundspeak_state
        groundspeak_short_description_html
        groundspeak_short_description
        groundspeak_long_description_html
        groundspeak_long_description
        groundspeak_encoded_hints
</pre>
<h2>Search Waymark:</h2>
<pre>
  &gt; geoqo -s waymark:name=unusual -d count
  Search/Set Count: 6
</pre>
<p> Searches the database for only waypoints that are of type &#8216;Waymark&#8217; and conform to the terms given. See the documentation on the waypoint: search type for further details on how to use it, because everything else is the same. </p>
<p> Possible search columns for waymarks include the following beyond those listed in the waypoint section: </p>
<pre>
      waymark_owner_name
</pre>
<p> When waymarking.com starts releasing more data in .gpx files, this will get significantly longer, of course.</p>
<h2>Search Geodining:</h2>
<pre>
  &gt; geoqo -s geodining:resturant_name=Cafe -d count
  Search/Set Count: 6
</pre>
<p> Searches the database for only waypoints that are of type &#8216;Geodining&#8217; and conform to the terms given. See the documentation on the waypoint: search type for further details on how to use it, because everything else is the same. </p>
<p> Possible search columns for geodining waypoints include the following beyond those listed in the waypoint section: </p>
<pre>
                               geodining_restaurant_name
                               geodining_submitted_by
                               geodining_price
                               geodining_service
                               geodining_continent
                               geodining_country
                               geodining_state
                               geodining_city
                               geodining_zip
                               geodining_address
                               geodining_description
                               geodining_details
</pre>
<h2>Search Wigle:</h2>
<pre>
  &gt; geoqo -s wigle:name=unusual -d count
  Search/Set Count: 6
</pre>
<p> Searches the database for only waypoints that are of type &#8216;Wigle&#8217; and conform to the terms given. See the documentation on the waypoint: search type for further details on how to use it, because everything else is the same. </p>
<p> Possible search columns for wigles include the following beyond those listed in the waypoint section: </p>
<pre>
                           wigle_ssid
                           wigle_netid
                           wigle_discover
                           wigle_channel
                           wigle_type
                           wigle_freenet
                           wigle_firsttime
                           wigle_sep
                           wigle_comment
                           wigle_qos
                           wigle_lastupdt
                           wigle_paynet
                           wigle_userfound
</pre>
<h2>Search Waypoint:</h2>
<pre>
  &gt; geoqo -s waypoint:name=unusual -d count
  Search/Set Count: 6
</pre>
<p> The <i>waypoint</i> search type is for searching for primary fields in a waypoint record. Possible search terms include <code>anything</code> in the type-specific searches (since waypoint: searches include everything) and the following fields which apply to all waypoints regardless of specific type: </p>
<pre>
        desc
        lat
        lon
        sym
        time
        type
        subtype
        url
        urlname
        cmt
</pre>
<p> The following are some examples of how to use the <i>waypoint:</i> search type. Note that <i>cache:</i> and <i>waymark:</i> searches work the exact same way and also do everything below, but limit your search to just waypoints of those types. </p>
<p> The format for using the waypoint (or similarily for cache: or waymark:) search terms is: </p>
<pre>
  geqo -s waypoint:I&lt;TERMS&gt;
</pre>
<p> where <font SIZE="-1">TERMS</font> are a comma separated list of search terms. Normally these would be specified like: </p>
<pre>
  waypoint:FIELDNAME=VALUE
</pre>
<p> The <i></i><font SIZE="-1"><i>FIELDNAME</i></font><i></i> indicates the field name you want to search (see below), and the <i></i><font SIZE="-1"><i>VALUE</i></font><i></i> is the value you want to search for. The value field is actually surrounded by wildcards, and thus searching for &#8220;me&#8221; will match any value with &#8220;me&#8221; somewhere in it including &#8220;He and I went to the store&#8221; and &#8220;sometimes&#8221;. Using two equals signs turns off the automatic wildcard support (ie, name==me means search for a name that is <code>just</code> &#8220;me&#8221;). </p>
<p> An example: find all waypoints with a urlname field containing &#8220;unusual&#8221;: </p>
<pre>
      &gt; geoqo -s waypoint:urlname=tubular -d list
      num GCID     Name
        1 GCDFE0   Hidden Headstones
        2 GCE29A   Celebrated Cemetery
        3 GCHW9M   The eyes have it (Yamar's unusual #1)
        4 GCJ491   O where art thou (Yamar's unusual #2)
        5 GCJ5DV   Inverted Cache (Yamar's unusual #3)
        6 GCJ66H   Gone Fishin' (Yamar's unusual #4)
        7 GCQEBQ   Yamar's Unusual #6: The ORB
        8 GCB284   Don't Be A Drip!
</pre>
<p> An example: find all geocaches owned by &#8216;Spelunk&#8217;: </p>
<pre>
      &gt; geoqo -s cache:owner_name=spelunk -d list
      num GCID     Name
        1 GCJVTR   Here's to Your Health Cache
        2 GCJY4V   Sumac Grove Cache
        3 GCJZ2N   Wildlife View Cache
        4 GCKNZB   Misplaced Seed Cache
        5 GCKQBN   Out-N-About Cache
        6 GCKVFW   We Give-A-Hoot Cache
        7 GCNWM9   BUG JAR
        8 GCP5YP   Greenbelt  Hideaway
        9 GCPZK3   Davis Shopping Spree
       10 GCQ6Q8   BUG JAR II
       11 GCQ6TV   Great Experience Cache
       12 GCQ87Z   Here's to the Greenbelts
       13 GCQFYJ   Toby &amp; Willie's Friends
       14 GCQH1M   Connect the Dots Cache
       15 GCTCC5   Canal Cache
       16 GCTFJH   The Micro Equalizer Cache
       17 GCVVWY   Spelunk's 'Fishy' Doings
       18 GCW26F   Mountain or Desert? Cache
</pre>
<p> Note that terms will match anything beyond the underscore (&#8220;_&#8221;). <font SIZE="-1">IE</font>, if you do a search for: </p>
<pre>
  waypoint:short=some text
</pre>
<p> It will search the short description for &#8220;some text&#8221; even though the actual field name it&#8217;ll search is &#8220;groundspeak_short_description&#8221;. Using an exact fully spelled out field name is the most precise, but you can truncate names for convience. </p>
<p> Finally, you can use &#8216;*&#8217;s to indicate wildcard spots (<i>u*sal</i> would match &#8220;unusual&#8221; and &#8220;unit of sale&#8221;). By default geoqo already adds a * to both the front and the back of your search time (ie, <i>name=unusual</i> is actually interpreted as <i>name=*unusual*</i>). </p>
<p> You can also use the folling <font SIZE="-1">ARGUMENT</font> types when searching for field values in a waypoint: </p>
<pre>
   field ARGUMENT value
</pre>
<dl>
<dt>field=value</p>
<dd> Fuzzy match on value. The value will be surrounding by wildcards, as previously discussed so searching for &#8220;desc=blowfish&#8221; will actually search the desc field for &#8220;*blowfish*&#8221;. </p>
<pre>
  waypoint:desc=blowfish
</pre>
<dt>field==value</p>
<dd> Also as mentioned above, if you don&#8217;t want to use the automatic wild card searching discussed above, you can use 2 equal signs to indicate this. Thus if you search for &#8220;desc=blowfish&#8221; it will search the desc fields for an exact match on the word &#8220;blowfish&#8221; (<font SIZE="-1">IE</font>, must not contain any other words). </p>
<p> You should use == searches for numeric values too, or else something like &#8220;difficult=3&#8221; will also match difficult numbers like 3.5. </p>
<pre>
  waypoint:desc==blowfish
</pre>
<dt>field&lt;value and field&gt;value</p>
<dd> Allows you to search on less than or greater than numeric values. <font SIZE="-1">IE:</font> </p>
<pre>
  waypoint:lon&lt;42.123
</pre>
<p> or </p>
<pre>
  waypoint:terrain&gt;2
</pre>
<dt>&lt;&gt;</p>
<dd> If you use both, it becomes &#8220;not equal to&#8221;. <font SIZE="-1">IE:</font> </p>
<pre>
  waypoint:type&lt;&gt;unusual
</pre>
<p> Will list all waypoints <code>without</code> the word <i>unusual</i> in their desc field. This is also doing the same automatic wildcard matching like the = sign does, and thus the above search is actually searching for &#8220;*unusual*&#8221;.p</p>
<dt>&lt;=&gt;</p>
<dd> This is also &#8220;not equal to&#8221;, but is an exact match and thus: </p>
<pre>
  waypoint:desc&lt;=&gt;blowfish
</pre>
<p> will match any type of cache that doesn&#8217;t have a desc field of &#8220;blowfish&#8221;. It will include, in the search, caches with a desc field of &#8220;blowfish dinner&#8221; however because it&#8217;s not an exact match.</dl>
<h2>Search Ident:</h2>
<pre>
  &gt; geoqo -s ident:gcabcd,gcefgh,gcijkl -d count
  Search/Set Count: 3
  &gt; geoqo -s ident:abcd,efgh,ijkl -d count
  Search/Set Count: 3
</pre>
<p> The <i>ident</i> plugin merely lets you quickly list a bunch of waypoint identifiers you want to select with geodb. </p>
<p> The identifiers do have a wild card inserted before them so you can leave off a common prefix, as shown in the second example above, and still match the list (saves typing). </p>
<p> Really, the <i>ident:</i> search type is just a faster way to type: </p>
<pre>
  &gt; geoqo -s waypoint:ident=abcd||waypoint:ident=efgh||...
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>idents:</p>
<dd> A comma separated list of identifiers to search for</dl>
<h2>Search Log:</h2>
<p> The <i>log:</i> search type lets you search waypoint log entries for waypoints matching a criteria. As an example, you can search for all waypoints in you database found by Yamar (me): </p>
<pre>
      &gt; geoqo -s 'log:finder=Yamar' -d list
      num GCID     Name
        1 GCJVTR   Here's to Your Health Cache
        ...
</pre>
<p> Log tokens to search by: </p>
<pre>
   id
   ident
   date
   type
   logger_id
   logger
   text_encoded
   text
</pre>
<p> Special tokens to search by (makes sure a log was made by someone of a particular type): </p>
<pre>
   finder
   noter
   dnfer
</pre>
<p> <font SIZE="-1">WARNING:</font> this may be amazingly slow on a mysql server. I think. Postgresql or sqlite2 (the defualt) database backends are just zippy, however.</p>
<h2>Search Attribute:</h2>
<p> Attribute searches groundspeak (geocaching.com) attributes that were loaded into the database when doing an import from a groundspeak .gpx file. </p>
<pre>
  &gt; geoqo -s attribute:Dogs -d count
  Search Result Count: 32
</pre>
<p> <font SIZE="-1">NOTE:</font> this does <font SIZE="-1">NOT</font> search the user-defined attributes and only searches (geocaching.com) attributes. For searching user attributes you should use the attr: search plugin intstead.</p>
<h2>Search Attr:</h2>
<p> Attr searches attributes that you yourself have placed on a cache using the modify <i>setattr</i> module. </p>
<pre>
  &gt; geoqo -s ident:gcabcd -m setattr:found=1 --save
  &gt; geoqo -s attr:found=1 -d count
  Search Result Count: 1
</pre>
<p> <font SIZE="-1">NOTE:</font> this does <font SIZE="-1">NOT</font> search groundpseak (geocaching.com) attributes. For this you should use the attribute: search plugin intstead.</p>
<h2>Search Rating:</h2>
<p> The rating plugin lets you search ratings that may have been placed on a cache using the modify <i>rate</i> module. </p>
<pre>
  &gt; geoqo -s ident:gcabcd -m rate:fun=8
  &gt; geoqo -s &quot;rating:fun&gt;5&quot; -d count
  Search Result Count: 1
</pre>
<p> If you have downloaded average ratings from the ratings server, you can search by those as well by prefixing the name with &#8220;others:&#8221; to search by the average rating given to the cache by others: </p>
<pre>
  &gt; geoqo -s &quot;rating:others:fun&gt;5&quot;
</pre>
<p> If you want to search for all caches that you have not rated for a particular category, use: </p>
<pre>
  &gt; geoqo -s &quot;rating:fun=-&quot;
</pre>
<h2>Search Tag:</h2>
<p> Tag searches tags that you yourself or others have placed on a cache. </p>
<p> You can place them using the Tag Modify plugin: </p>
<pre>
  &gt; geoqo -s ident:gcabcd -m tag:cool/awesome
  &gt; geoqo -s tag:cool -d count:
  Search Result Count: 1
</pre>
<p> Prefix the tag names with &#8220;mine:&#8221; if you want to search just you tags, or &#8220;others:&#8221; if you want to search other people&#8217;s tags. </p>
<pre>
  &gt; geoqo -s tag:mine:cool -d count:
  Search Result Count: 1
  &gt; geoqo -s tag:others:cool -d count:
  Search Result Count: 2
</pre>
<h2>Search Set:</h2>
<p> Sets, which are described further below, are a bunch of waypoints all with an identically named &#8220;tag&#8221;. As an example, if your geocaching.com pocket query was named &#8220;my query&#8221; and you import it into geoqo using the -i switch the waypoints contained in that gpx file will be assigned to the &#8220;import:my query&#8221; set. You can use the <i>set:setname</i> search type to load these waypoints. </p>
<pre>
  &gt; geoqo -s &quot;set:import:my query&quot; -d count
  Search Result Count: 500
</pre>
<p> This command would count everything in the database that was in the &#8220;import:my query&#8221; set name (that was likely imported from a pocket query). See the Advanced Searching section in the geoqo documentation for other examples of combining <i>set:</i> searches and <i>waypoint:</i> (or other) searches so you can search for &#8220;all waypoints matching a criteia within a set&#8221; for example. </p>
<p> If you prefix the name with a minus sign (-) then it will include all caches <font SIZE="-1"><code>NOT</code></font> in that set. For example to find all caches that are in seta but not in setb then the following expression would accomplish that: </p>
<pre>
    &gt; geoqo -s 'set:seta&amp;&amp;set:-setb'
</pre>
<h2>Search File:</h2>
<pre>
  &gt; geoqo -s file:foo.gpx -d count
  Search/Set Count: 3
  &gt; geoqo -s file:foo.loc -d count
  Search/Set Count: 3
</pre>
<p> The <i>file</i> plugin loads a file into memory and then searches the normal geoqo database for all the waypoints that match those found in the file. </p>
<p> <i>Options:</i></p>
<dl>
<dt>file:</p>
<dd> A file to load and search for matching waypoints from</dl>
<h2>Search Track:</h2>
<pre>
  &gt; geoqo -s track:mytrackfile.gpx -d count:
  Search/Set Count: 3
</pre>
<p> The <i>track</i> plugin loads track data from a <font SIZE="-1">GPX</font> track file (which you can retrieve from you gps using gpsbabel) and then compares the list of caches in you database to this data. It then matches all caches where your speed dropped below a configurable speed (3MPH is the default) and where the distance from the track is less than a configurable amount (defaults to near 500 feet). </p>
<p> This is even more useful when combined with the Track modify plugin, which can order caches based on the track and report the times you found them as well. </p>
<p> If you know all the caches are in a given set, however, you should probably limit the data it has to search through to a subset of you total database if it runs slowly. </p>
<p> To get track data from the gps, use gpsbabel: </p>
<pre>
  gpsbabel -t -i garmin -f usb: -o gpx -F track.gpx
</pre>
<p> See the Modify/Track plugin for a detailed example </p>
<p> <i>Options:</i></p>
<dl>
<dt>trackfile:</p>
<dd> A <font SIZE="-1">GPX</font> trackfile to load and search by</p>
<dt>speed:</p>
<dd> Only look for caches where your speed dropped below this </p>
<p> default: 3</p>
<dt>delta:</p>
<dd> lat/lon delta to use looking for caches near a stopping point </p>
<p> default: 0.002</p>
<dt>laterthan:</p>
<dd> Only use track points which are beyond a specifed time.</dl>
<h2>Search File:</h2>
<pre>
  &gt; geoqo -s file:foo.gpx -d count
  Search/Set Count: 3
  &gt; geoqo -s file:foo.loc -d count
  Search/Set Count: 3
</pre>
<p> The <i>file</i> plugin loads a file into memory and then searches the normal geoqo database for all the waypoints that match those found in the file. </p>
<p> <i>Options:</i></p>
<dl>
<dt>file:</p>
<dd> A file to load and search for matching waypoints from</dl>
<h2>Search Returnhome:</h2>
<pre>
  &gt; geoqo -s gps -d count
  Search/Set Count: 3
</pre>
<p> This plugin combines the functionality of a number of other ones rolled into one. In particular, it: </p>
<pre>
  1. pulls the existing waypoints from the GPS
  2. pulls the existing track from the GPS
  3. searches for the waypoints in the geoqo database that match the
     ones in the GPS using the GeoDB::Search::File plugin
  4. seaches the results of those for ones that the track came close
     using the GeoDB::Search::Track plugin.
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>gpstype:</p>
<dd> Type of <font SIZE="-1">GPS</font> </p>
<p> default: garmin</p>
<dt>gpsport:</p>
<dd> The port to use </p>
<p> default: usb:</dl>
<h2>Search Gps:</h2>
<pre>
  &gt; geoqo -s gps -d count
  Search/Set Count: 3
</pre>
<p> The <i>gps</i> plugin talks to a gps and finds all the waypoints in the geoqo database that are also in the <font SIZE="-1">GPS</font>. This is done by pulling out all the waypoints from the <font SIZE="-1">GPS</font> and then using the list to search the database. </p>
<p> <i>Options:</i></p>
<dl>
<dt>gpstype:</p>
<dd> Type of <font SIZE="-1">GPS</font> </p>
<p> default: garmin</p>
<dt>gpsport:</p>
<dd> The port to use </p>
<p> default: usb:</dl>
<h2>Search Any:</h2>
<p> The <i>any:</i> search type simply uses all the waypoints in the entire database. It (hopefully) obviously doesn&#8217;t make sense to use this combined with other types of searches.</p>
<h2>ADVANCED SEARCHING</h2>
<p> There are advanced things you can do while searching. This section documents those:</p>
<h2>Accessing a single result from the last search</h2>
<p> Sumarize just the 12th waypoint from the last search results: </p>
<pre>
      &gt; geoqo -s 12 -d list
       12 GCNK57   James Bond 047
</pre>
<p> Export caches 5-10 from the last search results: </p>
<pre>
      &gt; geoqo -s 5-10 -e out.gpx
</pre>
<h2>Logical Searches</h2>
<p> You can use &amp;&amp; (<font SIZE="-1">AND</font>) and || (<font SIZE="-1">OR</font>) pairs to add powerful searching combinations to your results. In fact, this is actually useful and can <code>increase</code> the speed of your queries if used properly (if you know you only want to search the data from a particular import, use a set: search &amp;&amp; with a waypoint: search and the result will likely be returned faster). </p>
<p> This example searches for all waypoints owned by &#8220;spelunk&#8221; that I have found (ie, it exists in the &#8220;import:My Finds Pocket Query&#8221; imported gpx file). </p>
<pre>
      &gt; geoqo -s 'waypoint:owner_name=spelunk&amp;&amp;set:import:My Finds Pocket Query' -d list
      num GCID     Name
        1 GCJVTR   Here's to Your Health Cache
        2 GCJY4V   Sumac Grove Cache
        3 GCJZ2N   Wildlife View Cache
        4 GCKNZB   Misplaced Seed Cache
        5 GCKQBN   Out-N-About Cache
        6 GCKVFW    We Give-A-Hoot Cache
        7 GCNWM9   BUG JAR
        8 GCP5YP   Greenbelt  Hideaway
        9 GCPZK3   Davis Shopping Spree
       10 GCQ6Q8   BUG JAR II
       11 GCQ6TV   Great Experience Cache
       12 GCQ87Z   Here's to the Greenbelts
       13 GCQFYJ   Toby &amp; Willie's Friends
       14 GCQH1M   Connect the Dots Cache
       15 GCTCC5   Canal Cache
       16 GCTFJH   The Micro Equalizer Cache
       17 GCVVWY   Spelunk's 'Fishy' Doings
       18 GCW26F   Mountain or Desert? Cache
</pre>
<p> That is likely faster than doing the next search, but the following is another way to do something similar. In this case, I&#8217;m searching for all waypoints owned by spelunk that there is a log entry by me for (note: finder is a mis-nomer as a finder may have logged it as a &#8220;did not find&#8221;; search on the log &#8220;type&#8221; as well to limit it to just finds): </p>
<pre>
      &gt; geoqo -s 'waypoint:owner_name=spelunk&amp;&amp;log:finder=Yamar' -d list
      num GCID     Name
        1 GCJVTR   Here's to Your Health Cache
        ... [same result] ...
</pre>
<h2>grouping search terms</h2>
<p> The () arguments can be used to group search terms together as well when you need to mix operations. In the following case we&#8217;re looking for all waypoints &#8220;owned by scoobert <font SIZE="-1">AND</font> have the word Ditch in them&#8221;, and add to that all waypoints logged by me and all waypoints with &#8216;ninja&#8217; in the title. Silly example, I know. </p>
<pre>
      &gt; perl -I. geoqo -s '(waypoint:groundspeak:name=Ditch&amp;&amp;waypoint:owner_name=scoobert)||waypoint:groundspeak:name=ninja||log:finder=Yamar' -d list
        1 GCYBDY   Whodunit?
        2 GCP8MT   All Day
        3 GCQJY0   Kate's Watching
        [...]
</pre>
<h2>SETS: Searches, imports, and just about everything are saved in sets</h2>
<p> Actually, just about everything is stored in a set. They&#8217;re a powerful way to &#8220;tag&#8221; a group of waypoints. The -N flag (or &#8211;set-name) flag specifies which name you want to store your current search results into (it&#8217;s currently required and will always store the results somewhere). </p>
<p> Sets can be created from a search </p>
<pre>
    &gt; geoqo -N search:47dad47 -s waypoint:owner_name=47dad47 -d list
    num GCID     Name
      1 GCH5EF   Sacramento's Second Webcam Cache
    [...]
     14 GCR86K   .
    &gt; geoqo -N search:gary -s waypoint:owner_name=gary -d list
    num GCID     Name
      1 GCRWXC   Fishing in Cache Creek
</pre>
<p> Sets can be listed: </p>
<pre>
    &gt; geoqo -d saved
    Set Name             Cache Count
    -------------------- -----------
    file:somefile        200
    search:geoqo         13                   &lt;i&gt;(default search name)&lt;/i&gt;
    search:47dad47       14
    search:gary          1
</pre>
<p> And they can be combined: </p>
<pre>
    &gt; geoqo -s set:search:gary,search:47dad47 -d list
    num GCID     Name
      1 GCRWXC   Fishing in Cache Creek
      2 GCH5EF   Sacramento's Second Webcam Cache
      [...]
     15 GCR86K   .
</pre>
<h2>DISPLAYING SEARCH RESULTS</h2>
<p> You&#8217;ve already seen the effects of the -d list switch, which lists all the waypoints in the resulting set/search. But there are a number of display types to pick from, and &#8216;list&#8217; is only one such search output style:</p>
<h2>Display Help:</h2>
<p> The help module displays help on a given topic. You can specify help on a given topic. </p>
<pre>
  Example 1:
  geoqo -d help
  Example 2:
  geoqo -d help:topicname
</pre>
<p> The help routine displays help for the various geoqo plugins. </p>
<p> <i>Options:</i></p>
<dl>
<dt>topic:</p>
<dd> Specifies the topic to display help on.</dl>
<h2>Display Count:</h2>
<pre>
  Example:
  geoqo -s 'set:import:my pocket query' -d count
  Search/Set Count: 500
</pre>
<p> The Count display simply counts the results in a set. This is very useful for counting the results before you do something with them (like dumping 500 caches to your screen when you were looking for just a few). </p>
<p> <i>Options:</i></p>
<dl>
<dt>prefix:</p>
<dd> The prefix string to print right before the count </p>
<p> default: Search/Set Count:</dl>
<h2>Display List:</h2>
<pre>
  Example 1:
  geoqo -d list
  num GCID     Name
  1   GCMR3M   The Mystery of Livinrgttoo
  2   GCPWBT   Hidden Cactus Garden
  Example 2:
  geoqo -d 'list:format=%{3:count} %{6:ident} terr=%{3:groundspeak_terrain} diff=%{groundspeak_difficulty}'
  1   GCMR3M terr=1.5 diff=1.5
  2   GCPWBT terr=2   diff=1.5
</pre>
<p> The List display shows the contents of the search Set one line at a time. By default, the format is (may vary depending on type though): </p>
<pre>
  %{3:count} %{8:ident} %{66:urlname}
</pre>
<p> The number prefix is the number of spaces to print it in and it will pad with extra spaces if it doesn&#8217;t fill that space. If left out, it&#8217;ll print it straight out in any length it may be. Adding a decimal point will limit it to a maximum of that length. <font SIZE="-1">IE:</font> </p>
<pre>
  %{20.20:urlname}
</pre>
<p> Will print <code>only</code> the first 20 characetrs of the urlname. </p>
<p> <i>Options:</i></p>
<dl>
<dt>format:</p>
<dd> Specifies the formatting parameters</dl>
<h2>Display Show:</h2>
<pre>
  Example 1:
  geoqo -s 1 -d show
Show (-d show) the waypoint details for #3 from the last search (which is
really #3 from the default set or the set specified via the -N
switch):
      &gt; geoqo -s 3 -d show
      GCHW9M     Multi-cache         Location:   38.542933, -121.6998
      Name:      The eyes have it (Yamar's unusual #1)
      Owner:     Yamar                (#183928)  Created:  2004-03-08
      Placed By: yamar
      Rating:    3/1.5
      URL:       <a rel="nofollow" href="http://www.geocaching.com/seek/cache_details.aspx?guid=5f9bd8d4-193a-4e0c-92c4-f107ae6d878b">http://www.geocaching.com/seek/cache_details.aspx?guid=5f9bd8d4-193a-4e0c-92c4-f107ae6d878b</a>
      Short Description:
        A 3 part waypoint: a virtual, an unusual and a regular
      Long Description:
        Yamar to Spelunk on 2004-04-06:
        &quot;If this cache is under that lamp post [again], I'm going to scream.&quot;
        [...]
</pre>
<p> Show the waypoint details and also the logs (-L, but this may change in the future): </p>
<pre>
      &gt; geoqo -s 3 -d show -L
      GCHW9M     Multi-cache         Location:   38.542933, -121.6998
      Name:      The eyes have it (Yamar's unusual #1)
      [...]
      Log #13914681 by Mango101: (Found it)
        This cache took us way too many tries! Finally we found it! TNLN.
      Log #14812407 by Mister Grim &amp; Pooka: (Found it)
        The hint threw us for a loop but we figured it out
        eventually. Thanks for another great cache!
      [...]
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>logs:</p>
<dd> If true, shows the logs in the output. </p>
<p> default: 0</dl>
<h2>Display Map:</h2>
<pre>
  Example 1:
  geoqo -s 'set:import:My Pocket Query' -d map
</pre>
<p> The <i>Map</i> display plugin displays a map of a set of waypoints with little red dots for each waypoint. </p>
<p> This plugin requires internet access since the map tiles are pulled from the <a rel="nofollow" href="http://www.openstreetmap.org/">http://www.openstreetmap.org/</a> project (which I highly recommend you contribute to; it&#8217;s easy and fun to edit/fix the maps!). </p>
<p> (Eventually it should be possible to display with symbols, colors, etc as well as display the density overlays like the <font SIZE="-1">KML</font> export plugin does) </p>
<p> <i>Options:</i></p>
<dl>
<dt>style:</p>
<dd> default: icons</p>
<dt>icondir:</p>
<dd> default: dist/tomtom-icons/</p>
<dt>iconscale:</p>
<dd> Size to scale icon sizes in the map. &#8220;auto&#8221; scales based on the number of waypoints to be shown. </p>
<p> default: auto</p>
<dt>maptiles:</p>
<dd> default: 2</p>
<dt>notext:</p>
<dd>
<dt>dodensity:</p>
<dd></dl>
<h2>Display Top10:</h2>
<p> The top10 dispaly plugin counts the values in a particular field and shows you the top10 results of the counts in that field. </p>
<p> Example (defaults to counting the top 10 waypoint owners): </p>
<pre>
  &gt; geoqo -s any: -d top10
  Top 10 'groundspeak_owner_name's
   Num    % Value
  ----------------------------------------------------------------------
  22    4 BootyBuddies
  20    4 sailorscodgers
  17    3 retiredprof
  16    3 two bison
  14    2 Sac D
  14    2 Oldhippy &amp; Granny
  13    2 TRAKD
  12    2 rivercity
  11    2 2Dee2Dee
  10    2 jimlips
  10    2 Pirate Princesses
</pre>
<p> Example: counting container types </p>
<pre>
  &gt; geoqo -s any: -d top10:groundspeak_container
  Top 10 'groundspeak_container's
   Num    % Value
  ----------------------------------------------------------------------
   234   50 Micro
   103   22 Regular
    92   19 Small
    13    2 Not chosen
    12    2 Other
    10    2 Virtual
     4    0 Large
</pre>
<p> Setting the &#8220;doaverage&#8221; parameter will also display the average value associated with a numeric field: </p>
<pre>
  &gt; geoqo -s 'cache:owner_name=Yamar' -d top10:groundspeak_difficulty,doaverage=1
  Top 10 'groundspeak_difficulty's
   Num    % Value
  ----------------------------------------------------------------------
    14   38 2
     9   25 1.5
     6   16 1
     3    8 2.5
     2    5 3
     1    2 4
     1    2 3.5
  Average: 1.90278
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>field:</p>
<dd> default: groundspeak_owner_name</p>
<dt>show:</p>
<dd> default: 10</p>
<dt>doaverage:</p>
<dd>
<dt>averagetext:</p>
<dd> default: Average:</p>
<dt>script:</p>
<dd>
<dt>noblank:</p>
<dd> default: 1</dl>
<h2>Display Sets:</h2>
<pre>
  Example:
  geoqo -d sets
 Count Set Name
 ----- ----------------------------------------
   450 import:Bethel Island
   500 import:Concord
   500 import:Copy of SanFrancisco
 [...]
</pre>
<p> Shows the list of existing sets remembered by the geoqo system, and the number of caches in each one. See the geoqo documentation on &#8220;sets&#8221; for further details. </p>
<p> <i>Options:</i></p>
<dl>
<dt>match:</p>
<dd> Only lists set names containing this value</p>
<dt>orderby:</p>
<dd> Can be set to order by &#8220;modified&#8221; (default) or &#8220;setname&#8221; or &#8220;count&#8221; </p>
<p> default: modified</dl>
<h2>Display Attributes:</h2>
<pre>
  Example:
  geoqo -d attributes
    Id  Attribute Name
------  ----------------------------------------
     1  Dogs
     3  Climbing gear
     4  Boat
     5  Scuba gear
 [...]
</pre>
<p> Shows the list of known groundspeak/geocaching attributes. This is useful for knowing which attributes you can search with using the &#8216;attribute&#8217; search plugin. </p>
<p> <i>Options:</i></p>
<dl>
<dt>match:</p>
<dd> Only lists attributes names containing this value</p>
<dt>orderby:</p>
<dd> Can be set to order by &#8220;attributename&#8221; (default) or &#8220;attributeid&#8221; </p>
<p> default: attributename</dl>
<h2>Display Stats:</h2>
<p> Example: </p>
<pre>
  &gt; geoqo -d stats
  Waypoints:     8754
  Geocaches:     8751
  Waymarks:         0
  Logs:         56659
  Sets:            33
</pre>
<p> The stats display plugin shows statistics about what is contained in your database.</p>
<h2>Display Gui/list:</h2>
<pre>
  Example:
  geoqo -s cache:urlname=funny -d gui/list
</pre>
<p> The gui/list module displays a <font SIZE="-1">GUI</font> in a graphical window that lets you examine the caches within a cache set. </p>
<p> This is only very preliminary work and is subject to greater expansion in the future. </p>
<p> <i>Options:</i></p>
<dl>
<dt>fields:</p>
<dd> default: Ident Type Subtype Groundspeak_Owner_Name <font SIZE="-1">URLNAME</font></p>
<dt>plugins:</p>
<dd>
<dt>separator:</p>
<dd> default: 0</dl>
<h2>Display Gui/show:</h2>
<pre>
  Example:
  geoqo -s cache:urlname=funny -d gui/show
</pre>
<p> The gui/show module displays a <font SIZE="-1">GUI</font> in a graphical window that lets you examine the caches within a cache set. </p>
<p> This is only very preliminary work and is subject to greater expansion in the future.</p>
<h2>Display Bounds:</h2>
<pre>
  Example 1:
  geoqo -s set:import:minneapolis -d bounds
  min    lat: 44.888483
  max    lat: 45.061767
  min    lon: -93.391317
  max    lon: -93.146517
  center lat: 44.975125
  center lon: -93.268917
</pre>
<p> The Bounds display shows the maximum and minimum latitude and longitude found in the set. It also outputs the center of the bounds as well.</p>
<h2>Display Graph/find:</h2>
<pre>
  Example:
  geoqo -s log:finder=Yamar -d graph/find:finder=Yamar
</pre>
<p> This shows a graph of finds over time by a given person. Generally, you&#8217;ll want to run this after you&#8217;ve incorporated a pocket query of all of your finds. You can run it against other user names too, but it&#8217;s unlikely you have every log record for them unless you&#8217;ve imported their find pocket query too. </p>
<p> <i>Options:</i></p>
<dl>
<dt>finder:</p>
<dd> Sets the <font SIZE="-1">NAME</font> of the finder you&#8217;re looking for to a particular geocaching name (ie, the name of the user that is logging the finds). 99/100 egoists recommend using your own geocaching name here.</p>
<dt>logtype:</p>
<dd> Defines the log type to graph. </p>
<p> default: Found it</dl>
<h2>Display Graph/placed:</h2>
<pre>
  Example:
  geoqo -s any: -d graph/placed:type=month
</pre>
<p> Shows a graph displaying which during months, weeks, etc the caches were placed. Really this just gives an indication of which months are the most popular months for placing a cache (probably due to weather). </p>
<p> <i>Options:</i></p>
<dl>
<dt>type:</p>
<dd> Examines creation date based on this frequency (X-axis column). <font SIZE="-1">PERIOD</font> may be either month, day, year, weekday or yearday. The default is month (ie, the graph will be from 1-12 showing the number of caches placed during each month in your loaded search set). </p>
<p> default: month</dl>
<h2>Display Dump:</h2>
<pre>
  Example 1:
  geoqo -d dump
  Example 2:
  geoqo -d dump:short=1
  Example 3:
  geoqo -d dump:format=perl
</pre>
<p> The <i>Dump</i> display type dumps the contents of a set of waypoints. This is primarily a debugging mechanism. </p>
<p> Options:</p>
<dl>
<dt>short=1</p>
<dd> Makes everything fit on one 80column line per item. This will truncate field values to something short enough to do this.</p>
<dt>format=perl</p>
<dd> Uses Data::Dumper to show the output in perl structure form. For the expert.</dl>
<p> <i>Options:</i></p>
<dl>
<dt>short:</p>
<dd> If specified, limits output to 1 line per field</p>
<dt>includeall:</p>
<dd> If set then all waypoint items will be included, even if the field itself is blank </p>
<p> default: 0</p>
<dt>format:</p>
<dd> If set to &#8220;perl&#8221; will use perl&#8217;s Data::Dumper to dump the perl object</dl>
<h2>MODIFYING RESULTS</h2>
<p> There are a number of modification plugins that modify data after it&#8217;s been extracted from the database and before it gets either displayed (-d) or exported (-e). These are most useful for changing data before it&#8217;s exported.</p>
<h2>Modify Solved:</h2>
<p> Example of solving a puzzle and saving it: </p>
<pre>
  &gt; geoqo -s ident:GCABCD -m 'setattr:puzn=N38 42.444,puzw=W121 42.444' --save
</pre>
<p> Example of exporting it with the replaced coordinates: </p>
<pre>
  &gt; geoqo -s ident:GCABCD -e 'solved:+loc:out.loc'
</pre>
<p> This plugin replaces the latitude and longitude coordinates of a waypoint with those in the puzn and puzw attributes. Use the above examples as a guide for solving a puzzle and then using the solved: plugin when exporting your database ready for uploading into a <font SIZE="-1">GPS</font>. </p>
<p> <i>Options:</i></p>
<dl>
<dt>nattr:</p>
<dd> The name of the attribute storing the new north coordinate </p>
<p> default: puzn</p>
<dt>wattr:</p>
<dd> The name of the attribute storing the new west coordinate </p>
<p> default: puzw</p>
<dt>dropunparsed:</p>
<dd> Drops caches that do not have puzzle answers but are not parseable </p>
<p> default: 1</dl>
<h2>Modify Gctodiff:</h2>
<p> The &#8220;gctodiff&#8221; plugin (short for &#8220;<font SIZE="-1">GC</font> to difficulty&#8221;) replaces the first two letters in the 6-digit cache identifier with a single digit representation of both the difficulty and terrain ratings. </p>
<p> <font SIZE="-1">IE</font>, if you had this cache: </p>
<pre>
    &gt; geoqo -l
    num GCID     Name
    1   GCQEBQ   Yamar's Unusual #6: The ORB
</pre>
<p> It&#8217;s rated a 1.5 in difficulty and a 2 in terrain. If you ran the gctodiff modify plugin on this data, it would replace the &#8216;<font SIZE="-1">GC</font>&#8216; with a 2 and 3: </p>
<pre>
    &gt; geoqo -m gctodiff: -d 'list:format=%{newident} %{desc}'
    23QEBQ   Yamar's Unusual #6: The ORB
</pre>
<p> It actually stores the data in the &#8216;newident&#8217; field so the old one is still available. The export modules, however, use the newident field when writing out the cache identifiers so this is what your <font SIZE="-1">GPS</font>, or what-have-you, will see when you load it into that. </p>
<p> I (Yamar) do this specifically so when I&#8217;m looking at my garmin, for example, I get an immediate feel for how hard a particular cache is going to be without having to pull up data about it. (I also use the symbol plugin to change the symbol so I can see the type of cache it is too). My goal here is to maximize the amount of data I seen on the screen! </p>
<p> The map from groundspeak/geocaching.com ratings is as follows: </p>
<pre>
  1    =&gt; 1
  1.5  =&gt; 2
  2    =&gt; 3
  2.5  =&gt; 4
  3    =&gt; 5
  3.5  =&gt; 6
  4    =&gt; 7
  4.5  =&gt; 8
  5    =&gt; 9
</pre>
<h2>Modify Rewrite:</h2>
<p> The rewrite modify plugin lets you rewrite fields based on other fields. For example, I (Yamar) use the following rewrite when putting stuff to a gpx file I&#8217;m going to load into my TomTom so I get as much information as possible when clicking on the icon in the tomtom map display: </p>
<pre>
  rewrite:groundspeak_name=%{ident}/%{4:subtype}: %{groundspeak_name}
</pre>
<p> That way the groundspeak_name which might have been &#8220;some cache&#8221; becomes &#8220;GCABCD/Trad: some cache&#8221; to give me more information about it. (actually, I use the gctodiff plugin too and use the newident field instead; see the gctodiff plugin for details).</p>
<h2>Modify Setattr:</h2>
<p> The &#8220;Setattr&#8221; plugin (short for &#8216;Set Attributes&#8217;) allows you to add your own &#8220;attributes&#8221; to waypoint(s). You must specify the command line option &#8220;&#8211;save&#8221; to get them to be saved permenently to the database though. You can pick any attribute name you want, although some other modify plugins (like the &#8220;solved&#8221; plugin) may expect particular attribute names. </p>
<p> Atttributes can be used for just about anything. For example, you can use them to store notes, remember hints from other people, collect data for a complex puzzle cache, etc. </p>
<p> Example of storing a note: </p>
<pre>
  &gt; geoqo -s ident:GCABCD -m 'setattr:notes=I hate this puzzle' --save
</pre>
<p> Example of something silly: </p>
<pre>
  &gt; geoqo -s ident:GCABCD -m 'setattr:foo=bar' --save
</pre>
<p> Then you can search for all caches with that name and value later: </p>
<pre>
  &gt; geoqo -s attr:foo=bar -l
</pre>
<p> Example of solving a puzzle and saving it: </p>
<pre>
  &gt; geoqo -s ident:GCABCD -m 'setattr:puzn=N38 42.444,puzw=W121 42.444' --save
</pre>
<p> Example of exporting it with the replaced coordinates: </p>
<pre>
  &gt; geoqo -s ident:GCABCD -e 'solved:+loc:out.loc'
</pre>
<p> The setattr plugin lets you store your own information about a cache into the database. Some of the other plugins use attributes to manipulate things (see the <i>solved</i> plugin for an example). Sometimes you may want your own &#8220;notes&#8221;. As an example, I modify Unknown puzzles that you solve in the field (instead of &#8220;in advance&#8221; puzzles like cross puzzles) with &#8220;setattr:infield=1&#8221;. (then I can use that attribute with the modifier: plugin to drop all unknowns that don&#8217;t have that attribute set or don&#8217;t have a &#8216;puzn&#8217; coordinate assigned showing I&#8217;ve solved it. </p>
<p> <font SIZE="-1"><code>IMPORTANT</code></font><font SIZE="-1"><code>NOTE:</code></font> You must specify &#8211;save to the command line to have geoqo save your attribute changes back to the database. Otherwise you&#8217;re only setting attributes temporarily during the one-time call of geoqo.</p>
<h2>Math and Substitution</h2>
<p> Math and Substition can be done by prefixing the values with &#8220;math:&#8221; and &#8220;substitute:&#8221; where the contents will be searched for names with other attribute names in ()s and replaced with the attribute values. And if the math: was used, it will then be evaluated. Multiple depth replacements/math will work. </p>
<p> Here&#8217;s a more complex than needed example (the puzw attribute needs to be set as well for this to work): </p>
<pre>
  &gt; geoqo -s ident:GCABCD -m 'setattr:puzn=substitute:N38 42.(A)(B)(C)' --save
  &gt; geoqo -s ident:GCABCD -m 'setattr:A=4' --save
  &gt; geoqo -s ident:GCABCD -m 'setattr:B=math:(A)*2' --save
  &gt; geoqo -s ident:GCABCD -m 'setattr:C=math:(B)-(A)' --save
  &gt; geoqo -s ident:GCABCD -m solved: -e out.gpx
</pre>
<p> Note that the actual equation will still be stored as the attribute; The calculation is done when the attribute is later read (for example, by the &#8220;solved&#8221; modify plugin).</p>
<h2>Modify Tag:</h2>
<p> The &#8220;Tag&#8221; plugin allows you to add &#8220;tag&#8221;s to your caches. </p>
<p> Example: </p>
<pre>
  geoqo -s cache:owner_name==Yamar -m 'tag:tags=awesome/cool'
</pre>
<p> Another to remove tags: </p>
<pre>
  geoqo -s cache:owner_name==Yamar -m 'tag:tags=lame,deletetags=1'
</pre>
<p> <i>Publishing tags</i> </p>
<p> Your tags may be published to a geoqo tag server, and you may pull information about how other people have tagged waypoints from the tag server. To do this you must first create an account on the tag server: </p>
<pre>
  <a rel="nofollow" href="http://tagserver.geoqo.org/">http://tagserver.geoqo.org/</a>
</pre>
<p> Then put your created username and password into your <tt>$HOME</tt>/.geoqo/config file like: </p>
<pre>
  geoqouser YOURUSERNAME
  geoqopass YOURPASSWORD
</pre>
<p> Then you can publish your tags for a given set using: </p>
<pre>
  geoqo -s SEARCHTERMS -m tag:publish=1
</pre>
<p> Additionally you can fetch data about other people&#8217;s tags using: </p>
<pre>
  geoqo -s SEARCHTERMS -m tag:fetch=1
</pre>
<p> When you use the -S option to show a the data for a waypoint you will see a list of all your tags as well as a list of other peoples tags that you have fetched. </p>
<p> <i>Options:</i></p>
<dl>
<dt>tags:</p>
<dd>
<dt>deletetags:</p>
<dd>
<dt>publish:</p>
<dd>
<dt>publishtags:</p>
<dd>
<dt>ignoretags:</p>
<dd> default: lamppost/found</p>
<dt>fetch:</p>
<dd>
<dt>geoqouser:</p>
<dd>
<dt>geoqopass:</p>
<dd></dl>
<h2>Modify Rate:</h2>
<p> The &#8220;Rate&#8221; plugin allows you to add &#8220;ratings&#8221;s to your caches. </p>
<p> Example: </p>
<pre>
  geoqo -s cache:owner_name==Yamar -m 'rate:overall=4'
</pre>
<p> (at the moment &#8220;overall&#8221; is the only rating you can provide; more coming) </p>
<p> <i>Publishing ratings</i> </p>
<p> Your ratings may be published to a geoqo rating server, and you may pull information about how other people have rated waypoints from the rating server. To do this you must first create an account on the rating server: </p>
<pre>
  <a rel="nofollow" href="http://ratingserver.geoqo.org/">http://ratingserver.geoqo.org/</a>
</pre>
<p> Then put your created username and password into your <tt>$HOME</tt>/.geoqo/config file like: </p>
<pre>
  geoqouser YOURUSERNAME
  geoqopass YOURPASSWORD
</pre>
<p> Then you can publish your ratings for a given set using: </p>
<pre>
  geoqo -s SEARCHTERMS -m rate:publish=1
</pre>
<p> Additionally you can fetch data about other people&#8217;s ratings using: </p>
<pre>
  geoqo -s SEARCHTERMS -m rate:fetch=1
</pre>
<p> When you use the -S option to show a the data for a waypoint you will see a list of all your ratings as well as a list of other peoples ratings that you have fetched. </p>
<p> <i>Options:</i></p>
<dl>
<dt>overall:</p>
<dd>
<dt>ratings:</p>
<dd>
<dt>publish:</p>
<dd>
<dt>publishtags:</p>
<dd>
<dt>ignoreratings:</p>
<dd>
<dt>deleteratings:</p>
<dd>
<dt>fetch:</p>
<dd>
<dt>geoqouser:</p>
<dd>
<dt>geoqopass:</p>
<dd></dl>
<h2>Modify Makepuzzle:</h2>
<p> This plugin extracts puzzle coordinates and equations from a cache description and sets up some attributes for doing the puzzle solving. If a cache description has text in it like &#8220;N38 <font SIZE="-1">AB</font>.CDE&#8221; then this plugin will create 5 attributes A-E and a &#8220;puzn&#8221; attribute with the text &#8220;replace:N38 (A)(B).(C)(D)(E)&#8221; so that merely by filling in the A-E attributes will complete the puzzle. </p>
<p> <i>Options:</i></p>
<dl>
<dt>nattr:</p>
<dd> The name of the attribute storing the new north coordinate </p>
<p> default: puzn</p>
<dt>wattr:</p>
<dd> The name of the attribute storing the new west coordinate </p>
<p> default: puzw</p>
<dt>reextract:</p>
<dd> Force rextraction of the equation wiping out the existing data </p>
<p> default: 0</dl>
<h2>Modify Delete:</h2>
<p> This command removes the waypoints from the database. Obviously, this should be used with caution because it can not be undone. </p>
<p> For those that really and truly hate puzzles: </p>
<pre>
  &gt; geoqo -s 'cache:subtype=Unknown' -m delete
</pre>
<p> This can be useful for temporarily importing a bunch of items you don&#8217;t want to keep around in the long run.</p>
<h2>Modify Classify:</h2>
<p> <i>Options:</i></p>
<dl>
<dt>inputprefix:</p>
<dd> default:</p>
<dt>outputprefix:</p>
<dd> default: predicted:</p>
<dt>categories:</p>
<dd> default: kids,coolcontainer,goodlocation,fun</p>
<dt>LearningType:</p>
<dd> default: DecisionTree</p>
<dt>stopwordsfile:</p>
<dd> default: /usr/share/geoqo/classify-ignore-words</p>
<dt>Debugging:</p>
<dd></dl>
<h2>Modify Symbol:</h2>
<p> This plugin replaces symbol identifier (normally &#8220;Geocache&#8221; for geocaches) with a new symbol based on your set criteria. </p>
<p> As an example, I (Yamar) use the following mem: file definition to remap all my symbols into things that look (on my garmin) kind like the cache container: </p>
<pre>
  symbol:
  subtype=Multi-cache=Fitness Center,
  subtype=Unknown Cache=Information,
  subtype=Webcam Cache=Shower,
  groundspeak_container=Micro=Cemetery,
  groundspeak_container=Small=Tunnel,
  groundspeak_container=Large=Geocache Found,
  subtype=Virtual Cache=Ultralight Area
</pre>
<p> Then I can run geoqo to remap stuff before exporting it to a .gpx file: </p>
<pre>
  &gt; geoqo -s some_search_criteria -e 'mem:FILENAME+out.gpx'
</pre>
<p> That way all multi-caches get remapped to a &#8216;Fitness Center&#8217; because the &#8216;Fitness Center&#8217; icon on my garmin looks like a little guy lifting weights, and thus I know it&#8217;s going to be a harder cache (or one I&#8217;ll likely have to walk more). I like multi&#8217;s a lot, but I do like to know when I&#8217;m hitting them. Similarily, a Cemetery icon on my etrex is a small dot, a Tunnel is a bit larger, and a Geocache found icon is very large so I use them to represent sizes. </p>
<p> If you want to use the symbol plugin, you should pick your own symbols that seem right on your gps or other software system. Each <font SIZE="-1">GPS</font>&#8216;s symbols tend to be quite different (and the name chosen should be a symbol your <font SIZE="-1">GPS</font> or software actually matches). </p>
<p> <i>Formatting</i> </p>
<p> The format of the plugin is as follows: </p>
<pre>
  symbol:CACHEDATA=CACHEVALUE=SYMBOLNAME,CACHEDATA2=CACHEVALUE2=SYMBOLNAME2,
</pre>
<p> They are <code>exact</code> matches only. So the <font SIZE="-1">CACHEVALUE</font> must exactly equal the value found in the <font SIZE="-1">CACHEDATA</font> field or it won&#8217;t be replaced. The symbol plugin will stop after the first match so the first symbol in the list that gets matched always wins.</p>
<h2>Modify Translate:</h2>
<p> By far, this is one of the most powerful modification plugins. It uses online services (like Google) to translate cache fields from one language to another. As an example, here are some of my caches: </p>
<pre>
  &gt; geoqo -s cache:owner_name==Yamar&amp;&amp;waypoint:ident=GCJ -l
  num GCID     Name
  1   GCJYPW   Hoppin' mad about Davis
  2   GCJGRQ   Beneficial cache
  3   GCJKMD   Historical water tower
  4   GCJ7KT   Got Coffee?
  5   GCJ66H   Gone Fishin' (Yamar's unusual #4)
  6   GCJ491   O where art thou (Yamar's unusual #2)
  7   GCJ5DV   Inverted Cache (Yamar's unusual #3)
</pre>
<p> And here is what they look like when translated from English to Spanish: </p>
<pre>
  &gt; geoqo -s cache:owner_name==Yamar&amp;&amp;waypoint:ident=GCJ -l -m translate:source=English,destination=Spanish
num GCID     Name
  1   GCJYPW   Hoppin' enojado sobre Davis
  2   GCJGRQ   Escondrijo beneficioso
  3   GCJKMD   Torre historica del agua
  4   GCJ7KT   Cafe Conseguido?
  5   GCJ66H   Fishin ido ' (4) inusual de Yamar #
  6   GCJ491   O donde mil del arte (2) inusual de Yamar #
  7   GCJ5DV   Escondrijo invertido (3) inusual de Yamar #
</pre>
<p> Valid languages to pick from: </p>
<pre>
  English
  Spanish
  French
  German
  Italian
  Korean
  Japanese
  Portuguese
</pre>
<p> <i>Requirements</i> </p>
<p> 1) you must be connected to the net </p>
<p> 2) you must have the WWW::Babelfish perl module installed. </p>
<p> <i>Options:</i></p>
<dl>
<dt>source:</p>
<dd> The source language to translate from. </p>
<p> default: Spanish</p>
<dt>destination:</p>
<dd> The destination language to translate to. </p>
<p> default: English</p>
<dt>fields:</p>
<dd> A / separated list of fields to translate. </p>
<p> default: urlname</p>
<dt>service:</p>
<dd> The name of the translation service to use. </p>
<p> default: Babelfish</dl>
<h2>Modify Distance:</h2>
<p> The distance modify plugin puts distance information from a given lat, lon coordinate and inserts the data into the &#8220;distance&#8221; field of the waypoint. You can then use it in other ways like in <i>rewrite</i> modification engines or in list formatting, etc. </p>
<pre>
  &gt; geoqo -s ident:GCABCD -d 'list:format=%{ident} %{distance}
</pre>
<p> You can calculate distance from coordinates: </p>
<pre>
  &gt; geoqo -s ident:GCABCD -m 'distance:n=n38 12.123,w=w42 22.333'
</pre>
<p> or from another waypoint already in the <font SIZE="-1">DB:</font> </p>
<p> You can calculate distance from coordinates: </p>
<pre>
  &gt; geoqo -s ident:GCABCD -m 'distance:from=GCABCD'
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>from:</p>
<dd> The waypoint name distances should be calculated from</p>
<dt>n:</p>
<dd> The North coordiante to calculate distance from</p>
<dt>w:</p>
<dd> The West coordiante to calculate distance from</dl>
<h2>Modify Sortby:</h2>
<p> The sort by function sorts data in a set by a particular field. </p>
<pre>
  &gt; geoqo -s SOMETHING -m sortby:groundspeak_terrain -l
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>sortby:</p>
<dd> Field to sort by </p>
<p> default: distance</dl>
<h2>Modify Track:</h2>
<p> The track plugin lets you compare a list of waypoints found in a search against the data in a gpx track file. Specifically, it: </p>
<pre>
 - adds the following attribute fields to the waypoint's attribuets
   (not permenantly; use --save to save them):
   trkptdate    -  The date of the track point nearest the cache
   trkpttime    -  The time of the track point nearest the cache
   trkptnum     -  The number of the track point nearest the cache
   trkptname    -  The name of the track the point is in
   trkptdist    -  Distance in feet from the cache to the nearest track point
   trkptnum     -  The Nth track point counter into the track point data
   trkptepoch   -  Seconds since 1970 of the trackpoint closest to the cache
   trkptstart   -  Start time of the search (got closer than config distance)
   rtkptend     -  End time of the search
   rtkptnearby  -  Amount of time spent searching (= end - start)
 - optionally sorts the resulting waypoints by time visited if the
   sort option is set.
</pre>
<p> Using this and the track search plugin you can take a track <font SIZE="-1">GPX</font> file downloaded from a <font SIZE="-1">GPS</font> and list all the caches you came near in the order you went to them along with the time stamp when you visited it. As an example, this is the results of a trip I took one day: </p>
<pre>
  &gt; geoqo -s 'track:track.gpx' -m 'track:track.gpx' -d list:'%{7.7:ident} %{attr:trkpttime}  %{urlname}'
  
  GC10J27 10:55:22  This one is Golden
  GCPC2R  11:16:53  &quot;THE ISLAND&quot;
  GCYCGE  13:02:07  Legacy Trail #1 - River BBQ
  GCD8A1  13:10:55  Under Lock &amp; Key
  GC5CBC  13:52:32  Let the Games Begin
  GCPR6E  14:11:27  YFcache10
  GCWR36  14:31:10  Granite Rock
  GCK8YR  14:54:07  The Cache in The Middle of The Freeway
  GCYYXV  16:02:05  Cisco Grove TB Stop
  GC10Q0Q 16:02:41  Hard Rock Exchange #2
  GCW1C3  16:27:08  Crack with a View
  GCG38E  16:45:33  The Solar System - Pluto
</pre>
<p> To get track data from the gps, use gpsbabel: </p>
<pre>
  gpsbabel -t -i garmin -f usb: -o gpx -F track.gpx
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>trackfile:</p>
<dd> Track data to sort by</p>
<dt>sort:</p>
<dd> field to sort resulting set by (if set) </p>
<p> default: trkptepoch</p>
<dt>distance:</p>
<dd> Distance away in feet to use for determining how long you were in the area </p>
<p> default: 528</p>
<dt>hroffset:</p>
<dd> Offset in hours to use from the datestamp found in the track; useful if the timezone in the GPS/track does not match the track was laid</dl>
<h2>Modify Diff:</h2>
<p> <i>Options:</i></p>
<dl>
<dt>out:</p>
<dd> the name of the output file to store the html formated differences in.</dl>
<h2>Modify Limit:</h2>
<p> This module limits the number of waypoints in a set to a certain number (starting at an optional certain point in the list of waypoints). </p>
<p> <font SIZE="-1">IE</font>, it starts at the <i>offset</i>th waypoint in the set being modified, and limits the total number to <i>number</i>, stripping off all of the waypoints before the <i>offset</i> first and then everything from offset+number next. </p>
<p> If just <i>number</i> is specified (the common case) the firest <i>number</i> waypoints are kept. </p>
<p> If there are 250 caches in the set:</p>
<dl>
<dt>number = 100, offset = 0</p>
<dd> Will get the first 100 caches</p>
<dt>number = 100, offset = 100</p>
<dd> Will get the next 100.</p>
<dt>number = 100, offset = 200</p>
<dd> Will get the last 50.</dl>
<p> This module is very useful when combined with the distance and sortby modify pluigns to get the top 10 caches (for example) near something: </p>
<pre>
  geoqo -s 'set:import:mypocketquery' -m distance:from=GCABCD+sortby:+limit:10
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>number:</p>
<dd> default: 100</p>
<dt>offset:</p>
<dd> default: 0</dl>
<h2>Modify Only:</h2>
<p> This is most useful when doing really complex exporting. See Yamar&#8217;s usage description on the web page for why this is helpful sometimes. It&#8217;s mostly useful when you want to only include certain waypoints in a given export file, and you want to create lots of export files (TomTom&#8217;s require one file per <font SIZE="-1">POI</font> you wish to create, and I (Yamar) create different POIs for each cache type, size, etc.) </p>
<p> The argument formatting is: </p>
<pre>
  only:field=value
</pre>
<p> where field is the field (or attribute prefixed with &#8216;attr:&#8217;) name, and value is the exact value. The valid match types are:</p>
<dl>
<dt>only:field=value</p>
<dd> Includes the waypoint only if the value is exactly the same as the waypoint&#8217;s field value.</p>
<dt>only:field&lt;&gt;value</p>
<dd> Matches if the field <code>is not</code> that value</p>
<dt>only:field=-</p>
<dd> Matchs if the field doesn&#8217;t exist.</p>
<dt>only:field=+</p>
<dd> Same as =- but only includes the waypoint if it does exist.</dl>
<h2>Modify Drop:</h2>
<p> This is most useful when doing really complex exporting. See Yamar&#8217;s usage description on the web page for why this is helpful sometimes. </p>
<p> The Drop modifier is a compliment to the only modifier. Generally the &#8220;only&#8221; modifier will be easier for most people to think about, but technically you only need one as they can both accomplish the same tasks with inverse logic. </p>
<p> The argument formatting is: </p>
<pre>
  drop:field=value
</pre>
<p> where field is the field (or attribute prefixed with &#8216;attr:&#8217;) name, and value is the exact value. The valid match types are:</p>
<dl>
<dt>drop:field=value</p>
<dd> Matches only if exactly the same.</p>
<dt>drop:field&lt;&gt;value</p>
<dd> Matches if the field <code>is not</code> that value</p>
<dt>drop:field=-</p>
<dd> Matchs if the field doesn&#8217;t exist. I use this like follows: </p>
<pre>
  #
  # unknown caches with solved puzzle coords
  #
  drop:subtype&lt;&gt;Unknown Cache
  +drop:attr:puzn=-
  +solved:
  +gpx:nologs=1:palm-solved.gpx
</pre>
<p> To drop any unknown cache that a &#8216;puzn&#8217; attribute hasn&#8217;t been added to it (see the <i>Solved</i> modify plugin for details).</p>
<dt>drop:field=+</p>
<dd> Same as =- but only drops it if it does exist.</dl>
<h2>Modify Dropexisting:</h2>
<p> This modify function is really only useful during an import before a data save. </p>
<p> The plugin simply removes all data from the current set that already exists in the database. This can be used to import data where only the new data is desired. </p>
<p> Example: </p>
<pre>
  &gt; geoqo -i 'myfile.gpx+dropexisting'
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>prefix:</p>
<dd> default:</p>
<dt>onlyprefixold:</p>
<dd> default: 1</dl>
<h2>Modify Load:</h2>
<p> This is only useful when you&#8217;re going to be doing complex exporting where you need the caches data loaded early before exporting to multiple files. Otherwise geoqo may load all the data once per file. </p>
<pre>
  &gt; geoqo -s something -m load -e 'gctodiff+file1.gpx;file2.gpx
</pre>
<p> See the export documentation for details on why file1.gpx and file2.gpx may contain separate data. </p>
<p> Basically, since this is a confusing one, is if you&#8217;re doing complex exporting (multiple files at once) put this on the -m switch to speed things up.</p>
<h2>EXPORTING RESULTS</h2>
<p> None of this is useful if you can&#8217;t export your results of course. There are a number of export plugins you can pass to the -e switch to export the results of your search to a file.</p>
<h2><font SIZE="-1">QUICK</font> <font SIZE="-1">EXPORT</font> <font SIZE="-1">EXAMPLES</font></h2>
<p> Some quick examples: </p>
<p> Exporting all waypoints from two sets: </p>
<pre>
    &gt; geodb -s 'set:search:gary&amp;&amp;set:search:47dad47' -e garyand47.gpx --debug 1
    1: writing file: garyand47.gpx
</pre>
<p> Exporting all waypoints in a set that are of type &#8220;Unknown&#8221; to a .loc file: </p>
<pre>
    &gt; geodb -s 'set:import:somefile&amp;&amp;waypoint:type=Unknown' -e partfilebackout.loc
</pre>
<h2><font SIZE="-1">EXPORTING</font> <font SIZE="-1">AND</font> <font SIZE="-1">MODIFYING</font></h2>
<p> You can also combine modifications and exports in one pass. First list the modifications specs you want to do (see the documentation on the modification plugins for details) separated by + signs. Everything before the last + will call a modification plugin, and after the last + will be an export plugin. </p>
<p> An example: </p>
<pre>
    &gt; geodb -s 'cache:type=Unknown' -e gctodiff+partfilebackout.loc
</pre>
<h2><font SIZE="-1">OUTPUTING</font> <font SIZE="-1">TO</font> <font SIZE="-1">MULTIPLE</font> <font SIZE="-1">FILES</font></h2>
<p> You can also specify multiple output files separated by &#8216;;&#8217;s. Modification attributes will <code>only</code> apply to the next file. If you want every file to contain a modification plugin result, use the -m flag instead. </p>
<pre>
    &gt; geodb -s 'cache:type=Unknown' -e 'gctodiff+partfilebackout.loc;partfilebackout2.gpx
</pre>
<p> The above applies the gctodiff plugin to only the .loc file; the gpx file is written out using raw data.</p>
<h2><font SIZE="-1">EXPORT</font> <font SIZE="-1">PLUGIN</font> <font SIZE="-1">TYPES</font></h2>
<h2>Export Gpx:</h2>
<pre>
  &gt; geoqo -s 'cache:name=cool cache' -e myfile.gpx
</pre>
<p> The gpx exporter writes out a gpx file containing all the caches in the search set. </p>
<p> Options are applied between the colon delimiter type specifier (first part) and the file name (th e last part) like so: </p>
<pre>
  &gt; geoqo -s 'cache:name=cool cache' -e gpx:nologs=1,setname=boo:myfile.gpx
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>setname:</p>
<dd> Makes the name field in the gpx file set to this value. </p>
<p> default: geoqo-export</p>
<dt>nologs:</p>
<dd> If set the resulting gpx file does not contain the wayoint logs.</p>
<dt>nogcattributes:</p>
<dd> If set the resulting gpx file does not contain the groundspeak attributes.</dl>
<h2>Export Loc:</h2>
<pre>
  &gt; geoqo -s 'cache:name=cool cache' -e myfile.loc
</pre>
<p> The loc exporter writes out a loc file containing all the caches in the search set.</p>
<h2>Export Map:</h2>
<pre>
  Example:
  geoqo -s set:import:myPQ -e map:output.png
</pre>
<p> The map will show red dots whereever there is a cache (Yes virginia, there will eventually be symbols and names). The output (currently) must be a <font SIZE="-1">PNG</font> file. </p>
<p> <i>Options:</i></p>
<dl>
<dt>style:</p>
<dd> default: icons</p>
<dt>icondir:</p>
<dd> default: dist/tomtom-icons/</p>
<dt>iconscale:</p>
<dd> Size to scale icon sizes in the map. &#8220;auto&#8221; scales based on the number of waypoints to be shown. </p>
<p> default: auto</p>
<dt>maptiles:</p>
<dd> default: 2</p>
<dt>notext:</p>
<dd>
<dt>dodensity:</p>
<dd></dl>
<h2>Export Html:</h2>
<pre>
  &gt; geoqo -s 'cache:name=cool cache' -e myfile.html
  Prints a set of caches to a series of web pages.  Each cache will
  get it's own file and a top level index file will be created that
  links to each cache page.
  Very useful for outputting geocaches to plucker.
</pre>
<p> <i>Options:</i></p>
<dl>
<dt>subdir:</p>
<dd> Puts created <font SIZE="-1">HTML</font> files in this sub directory name. </p>
<p> default: caches</p>
<dt>title:</p>
<dd> The title to put at the top of the page </p>
<p> default: GeoDB <font SIZE="-1">HTML</font> Export</dl>
<h2>Export Kml:</h2>
<pre>
  &gt; geoqo -s 'set:import:near me' -e fortheearth.kml
</pre>
<p> The software will also produce a density plot as well, which shows the density of caches in particular areas color-coded by relief colors (rainbow; red = very few, purple = many). Examples of this can be seen on Yamar&#8217;s cache homepage page <a rel="nofollow" href="http://geocaching.sharedlists.com/.">http://geocaching.sharedlists.com/.</a> </p>
<p> Options:</p>
<dl>
<dt>size=NUM</p>
<dd>
<pre>
  &gt; geoqo -s 'set:import:near me' -e kml:size=100:fortheearth.kml
</pre>
<p> Changes the number of squares in the density plot to <font SIZE="-1">NUM</font> by <font SIZE="-1">NUM</font>. Defaults to 50.</p>
<dt>width=NUM</p>
<dd>
<dt>height=NUM</p>
<dd> Changes just the width and height of the squares. The size parameter can change both at once.</dl>
<p> (there are a bunch of options for the density plot, which are currently undocumented). </p>
<p> <i>Options:</i></p>
<dl>
<dt>bogus:</p>
<dd>
<dt>dataname:</p>
<dd> default: Export from GeoQO</p>
<dt>dowaypoints:</p>
<dd> default: 1</p>
<dt>dodensity:</p>
<dd> default: 1</p>
<dt>dojail:</p>
<dd> default: 0</p>
<dt>bogus:</p>
<dd>
<dt>waypointstyle:</p>
<dd> default: geoqo</p>
<dt>waypointheight:</p>
<dd> default: 150</p>
<dt>waypointmode:</p>
<dd> default: relativeToGround</p>
<dt>waypointextrude:</p>
<dd> default: 1</p>
<dt>includedescriptions:</p>
<dd> default: 1</p>
<dt>bogus:</p>
<dd>
<dt>squareratio:</p>
<dd> default: 1</p>
<dt>size:</p>
<dd> Creates a plot where there are <font SIZE="-1">SIZE</font> by <font SIZE="-1">SIZE</font> squares of colored rectangles </p>
<p> default: 200</p>
<dt>width:</p>
<dd> Normally equal to the size value but can be set independently. It specifies the width (in squares) of the density plot.</p>
<dt>height:</p>
<dd> Normally equal to the size value but can be set independently. It specifies the height (in squares) of the density plot.</p>
<dt>spread:</p>
<dd> Sets the spread that determines the number of neighboring squares that a given cache will effect. <font SIZE="-1">EG</font>, a spread of 5 will affect a circle of density squares in a radius of 5. This generally should be a low value of probably not more than 5 or so. </p>
<p> default: 5</p>
<dt>doempty:</p>
<dd> If set to 1, even empty squares will be colored (red). Otherwise the empty squares are removed from the plot leaving the plane ground underneath. </p>
<p> default: 0</p>
<dt>bogus:</p>
<dd>
<dt>altitude:</p>
<dd> The altitude to set the density plot squares at. </p>
<p> default: 1000</p>
<dt>densitymode:</p>
<dd> default: relativeToGround</p>
<dt>extrude:</p>
<dd> Whether or not to extrude the density plot squares down to the ground. </p>
<p> default: 0</p>
<dt>opaque:</p>
<dd> The opacity of the density squares. Must be between 0 and 100, with 0 being completely see-through (and thus completely useless). </p>
<p> default: 20</p>
<dt>linewidth:</p>
<dd> The width of the border lines to draw (0-4). 0 means don&#8217;t draw borders on the squares. </p>
<p> default: 0</p>
<dt>bagus:</p>
<dd>
<dt>jailaltitude:</p>
<dd> default: 100</p>
<dt>jailmode:</p>
<dd> default: relativeToGround</p>
<dt>bogus:</p>
<dd>
<dt>limitdata:</p>
<dd> default: 1</p>
<dt>nmax:</p>
<dd> The maximum north coordinate value to created the grid over. Normally this is automatically set by the maximum value found in the data, but can be overridden</p>
<dt>nmin:</p>
<dd> The minimum north coordinate value to created the grid over. Normally this is automatically set by the minimum value found in the data, but can be overridden</p>
<dt>wmax:</p>
<dd> The maximum west coordinate value to created the grid over. Normally this is automatically set by the maximum value found in the data, but can be overridden</p>
<dt>wmin:</p>
<dd> The minimum west coordinate value to created the grid over. Normally this is automatically set by the minimum value found in the data, but can be overridden</dl>
<h2>Export System:</h2>
<p> There are two ways to use the <i>system</i> export mechanism:</p>
<dl>
<dt>Run a system command for cache:</p>
<dd>
<pre>
  &gt; geoqo -s 'cache:name=cool cache' -e 'system:cmd=echo %{ident} %{desc}'
</pre>
<p> That command runs echo for each cache in the set, replacing %{ident} and %{desc} with the fields from those caches. </p>
<p> Useful things to do for this would be to open firefox (a web browser) on each cache page: </p>
<pre>
  &gt; geoqo -s 'cache:name=cool cache' -e 'system:cmd=firefox %{url}'
</pre>
<dt>Run a system command</p>
<dd> You can also run a command on a file generated by an export module. As an example, the following command will call gpsbabel to convert a gpx file to a tomtom compatible file: </p>
<pre>
  &gt; geoqo -s 'cache:name=cool cache' -e 'system:cmd=gpsbabel -i gpx -f %{file:gpx} -o tomtom -F mycaches.ov2'
</pre>
</dl>
<p> <i>Options:</i></p>
<dl>
<dt>cmd:</p>
<dd> <font SIZE="-1">COMMAND</font> is what gets run. If it contains a %{file:TYPE} string in it, that will be replaced with a file name of that type and it&#8217;ll get run just once. If it doesn&#8217;t, it&#8217;ll get run once per cache in the set being processed and each %{token} specifier will get replaced by that item from the cache.</p>
<dt>sleep:</p>
<dd> Between each command executed in the per-cache mode, geoqo will sleep for <font SIZE="-1">NUM</font> seconds before running the next. It defaults to 1, and can be set to 0 to just fire them off as fast as possible.</p>
<dt>dontdelete:</p>
<dd> if set to 1, don&#8217;t delete the temporary files</p>
<dt>tmpdir:</p>
<dd> The temporary directory to use </p>
<p> default: /home/hardaker/.geoqo/temp</dl>
<h2>PLUGINS TO USE EVERYWHERE</h2>
<p> Here are some useful plugins that can be used in many command line definitions.</p>
<h2>Everywhere mem:</h2>
<p> It hard to repeatedly type complex queries, tasks, or what have you so to facilitate this you can use the <i>Mem</i> plugin for remembering complex strings (or even simple onse, if you choose). </p>
<p> To do this, take a complex search (or export, or modify) string and save it in a file in the directory &#8220;$HOME/.geoqo/mem/TYPE/FILENAME&#8221;. Where <font SIZE="-1">TYPE</font> is one of &#8220;search&#8221;, &#8220;export&#8221;, or &#8220;modify&#8221; and <font SIZE="-1">FILENAME</font> is a file name of your choosing. You can also store file entries directly in <tt>$HOME</tt>/.geoqo/mem/FILENAME (note the missing &#8220;<font SIZE="-1">TYPE</font>&#8221; part), which then makes the definition usable for all types. It is not likely you&#8217;ll need to use a definition for both searching and exporting (as an example), however, so I suggest you store them in a type-based subdirectory instead. Only because it&#8217;s cleaner. You want to be neat and tidy right? </p>
<p> All lines read in these file will be merged together and leading and trailing white-space characters are stripped as well comment lines (which should start with a #). For example if you had a file like so: </p>
<pre>
  &gt; cat $HOME/.geoqo/mem/search/memtest
    # Searches a particular imported set named &quot;near me&quot;
    set:import:near me
      # but only for items I haven't logged as found
      &amp;&amp;cache:finder&lt;&gt;Yamar
      # and aren't unknown caches.
      &amp;&amp;cache:subtype&lt;&gt;Unknown
</pre>
<p> You can then run geoqo like so: </p>
<pre>
  &gt; geoqo -s mem:memtest -d count
  Search Result Count: 480
</pre>
<p> Which is really a replacement for: </p>
<pre>
  &gt; geoqo -s set:import:near me&amp;&amp;cache:finder&lt;&gt;Yamar&amp;&amp;cache:subtype&lt;&gt;Unknown -d count
</pre>
<p> Since you may want to frequently replace parts of your super-long and complicated definition strings you&#8217;ve built up, you can do this as well by putting %[<font SIZE="-1">NAME</font>,DEFAULT] strings inside your definitions. <font SIZE="-1">IE</font>, doing this: </p>
<pre>
  &gt; cat $HOME/.geoqo/mem/memtest
    set:import:%[setname,near me]
      &amp;&amp;cache:finder&lt;&gt;Yamar
      &amp;&amp;cache:subtype&lt;&gt;Unknown
</pre>
<p> Makes the import: set default to &#8220;near me&#8221; so the above example command will work just like it would before, but if I specify a <i>setname</i> option on the command line I can override it. Here&#8217;s the original command example: </p>
<pre>
  &gt; geoqo -s mem:memtest -d count
  Search Result Count: 480
</pre>
<p> And here&#8217;s using the same search criteria, but using &#8220;fairfield&#8221; as the import set name instead of the default &#8220;near me&#8221;: </p>
<pre>
  &gt; geoqo -s mem:memtest,setname=fairfield -d count
  Search Result Count: 182
</pre>
<p> Final note: you can have mem: definitions that call other mem: definitions. The only caveat there is that parameters aren&#8217;t passed down automatically, so if your second mem: definition being called has a %[something,xxx] definition then you should call it within the higher definition as mem:subdef,something=%[something,xxx] as well.</p>
<h2>SCRIPTING ABILITY</h2>
<p> GeoQO can also perform a bunch of tasks at once in a scripted fashion. <font SIZE="-1">IE</font>, if you find yourself repeatedly doing a standard search followed by an export, you can script things together in a single file and call geoqo -x <font SIZE="-1">FILE</font>. </p>
<p> The script file format contains lines that start with a &#8216;%MODE&#8217; followed by text for that <font SIZE="-1">MODE</font>. <font SIZE="-1">MODE</font> should be one of: search, export, import, modify, display or print. You can break long lines into pieces just like the mem: plugin discusses above. </p>
<p> Thus the following script (saved in, for example, &#8220;myscript.txt&#8221;) will display unsolved puzzles in your database ordered by distance: </p>
<pre>
  # searches for all 'Unknown' caches
  %search
  subtype=Unknown
  &amp;&amp;attr:puzn=-
  # displays them in list format
  %display
  list
</pre>
<p> Then running the script will display the list: </p>
<pre>
  &gt; geoqo -x myscript.txt
  ... [list displayed here] ...
</pre>
<p> Scripts can be stored in <tt>$HOME</tt>/.geoqo/scripts and if a script is run and the file doesn&#8217;t exist in the current working directory, then the <tt>$HOME</tt>/.geoqo/scripts directory will be checked to see if it contains the file. </p>
<p> Scripts can contain %[name,default value] sections just like Everywhere Mem: definitions can and are acted upon the same way. Thus a script of: </p>
<pre>
  %search
  waypoint:type==%[type,Waymark]
  %display
  count
</pre>
<p> Will default to counting all the Waymarks in the database. But if run as: </p>
<pre>
  &gt; geoqo -x myscript.txt:type=Geocache
</pre>
<p> It&#8217;ll count all the geocaches instead.</p>
<h2>Special Script Formatting</h2>
<p> <i>White Space Wrapping</i> </p>
<p> Normally script lines are merged together, stripping leading and trailing white space off of a line. <font SIZE="-1">EG</font>, Scripts that look like: </p>
<pre>
  %search
  waypoint:type=
    =
  Geo
   cache
</pre>
<p> will actually be translated to a search using just: </p>
<pre>
  wayoint:type==Geocache
</pre>
<p> If you need to force whitespace into a script line at the begining or end you can use a triple &quot; in order to forec it. <font SIZE="-1">EG:</font> </p>
<pre>
  %search
  cache:owner_name=Super
  &quot;&quot;&quot; Sleuth&quot;
</pre>
<p> Will keep the space between the &quot;&quot;&quot; and the word Sleuth: </p>
<pre>
  cache:owner_name=Super Sleuth
</pre>
<p> Trailing &quot;&quot;&quot;s work similarily.</p>
<h2>Special Script Keywords</h2>
<p> All script pieces begin with a % sign on a new line. The line format looks like: </p>
<pre>
  %keyword someoption=1 otheroption=yes
</pre>
<p> These special options may include these global options as well as any keyword-specific options discussed below:</p>
<dl>
<dt>allowgui=1</p>
<dd> This lets the <font SIZE="-1">GUI</font> screens be shown for the sub-scripts. Normally they&#8217;re hidden as the top script is always expected to pass needed parameters down.</dl>
<p> The special script keywords that mayb be used are:</p>
<dl>
<dt>%print</p>
<dd> Prints everything from that section to the screen. </p>
<p> Example: </p>
<p> <tt>%print</tt> hello world</p>
<dt>%script</p>
<dd> Runs a subscript based on the text following the <tt>%script</tt> line. (may include the script name and potentially arguments following a &#8216;:&#8217;). </p>
<p> Example: </p>
<p> <tt>%script</tt> scriptname:arg1=value1</p>
<dt>%include <i>[</i><font SIZE="-1"><i>ARGUMENTS</i></font><i>]</i> <i></i><font SIZE="-1"><i>SCRIPT_FILE_NAME</i></font><i></p>
<dd> Include another script as part of this script. Unlike the </i><tt>%script</tt> command, the <tt>%include</tt> command operates on the same search set, becomes part of the same auto-gui screen, etc. </p>
<p> You can also pass a type=hooks argument to include a bunch of files. <font SIZE="-1">EG:</font> </p>
<p> <tt>%include</tt> type=hooks specialhooks/*.inc </p>
<p> Will include every file that matches that pattern in each of the script search paths. The order in which they are included is determined by alphabetical ordering of the last filename component (ie, not directory path component). </p>
<p> Finally, you can auto-wrap includes in if statements and use the resulting titles from the included files in menu to select which file gets executed. This is primarily intended for building dynamic menus from found plugins. This is best seen by an example: </p>
<p> In a file called &#8220;testincludetop.txt&#8221;, we put the menu definition: </p>
<pre>
  %ignore
  %[mymenu,0
  ,labels=(%{VALUELABELS})
  ,type=menu,text=top menu:
  ,refresh_on_change=1
  ]
</pre>
<p> In two files called testinclude-1.txt and testinclude-2.txt we put: </p>
<pre>
  #scriptname: item number 1
  %print
  some thing or other to handle choice #1
</pre>
<p> (And something similar for number 2) </p>
<p> Then finally, in the real top level script you call the whole shabang with: </p>
<pre>
  %include type=hooks autoif=mymenu hookheader=testincludetop.txt testinclude*.txt
</pre>
<p> In the end, the whole result gets built as follows: </p>
<pre>
  %ignore
  %[mymenu,0
  ,labels=(0,item number 1,2,item number 2)
  ,type=menu,text=top menu:
  ,refresh_on_change=1
  ]
  %if &quot;%[mymenu]&quot; eq &quot;0&quot;
  %title
  item number 1
  %print
  some thing or other to handle choice #1
  %endif
  %if &quot;%[mymenu]&quot; eq &quot;1&quot;
  %title
  item number 2
  %print
  some thing or other to handle choice #2
  %endif
</pre>
<p> If you could follow that, I&#8217;ll be impressed. But it&#8217;s really powerful! See the included &#8220;searchbase&#8221; script for a much larger example.</p>
<dt>%save</p>
<dd> Calls &#8216;save&#8217; on the current set saving all the data to the db (needed if modified in anyway that should result in a save, such as when the setattr: modify plugin was called).</p>
<dt>%saveset name=MYNAME</p>
<dd> Remembers the current set as <font SIZE="-1">MYNAME</font>.</p>
<dt>%webfile</p>
<dd> Pulls a file from a <font SIZE="-1">URL</font> and saves it to a file. The format is the file name to save it to, a comma and then the <font SIZE="-1">URL</font>. Example: </p>
<pre>
  %webfile
  waymarks-train.gif,<a rel="nofollow" href="http://www.waymarking.com/images/cat_icons/train.gif">http://www.waymarking.com/images/cat_icons/train.gif</a>
</pre>
<p> You can then refer to these files using webfile:waymarks-train.gif in <tt>%copy</tt> or <tt>%system</tt> commands.</p>
<dt>%copy</p>
<dd> Copy&#8217;s a file from one place to another. Example format: </p>
<pre>
  %copy
  file1.loc,file2.loc
</pre>
<p> Or refering to a webfile previously pulled from a <tt>%webfile</tt> directive: </p>
<pre>
  %copy
  webfile:waymarks-train.gif,/some/path/to/waymarks-train.gif
</pre>
<dt>%system</p>
<dd> Run&#8217;s a system command. webfile: prefixes within the command string will be replaced by paths to a stored <tt>%webfile</tt>.</p>
<dt>%if <font SIZE="-1">CLAUSE</font></p>
<dd>
<dt>%else</p>
<dd>
<dt>%endif</p>
<dd> These sections allow for variablity of what is done based on user input. <font SIZE="-1">CLAUSE</font> is evaluated as perl code (returning a perl true or false response (eg, 1 or 0)) to determine what to do next. <font SIZE="-1">CLAUSE</font> will be evaluated first in terms of parameteritized input. Thus: </p>
<pre>
  %print
  %if %[desire,1,type=checkbox]
  hello
  %else
  world
  %endif
</pre>
<p> Will print &#8220;hello&#8221; if the user clicks the check box (defaults to on) or &#8220;world&#8221; if the user does not. (They may also hand-specify the &#8216;Desire&#8217; parameter as scriptname:desire=1 or equievelent). </p>
<p> Nesting is properly handled.</p>
<dt>%foreach <font SIZE="-1">VAR</font> value1 value2 &#8230;</p>
<dd>
<dt>%endforeach</p>
<dd> Allows repeated script sections with %{<font SIZE="-1">VAR</font>} being replaced with a different value for each section. </p>
<pre>
  %foreach it 1 2 3 a b word
  %print
  This is it: %{it}
  %endforeach
</pre>
<p> Will output: </p>
<pre>
  This is it: 1
  This is it: 2
  This is it: 3
  This is it: a
  This is it: b
  This is it: word
</pre>
<dt>%perl</p>
<dd> Embeds perl into the script. <tt>$self</tt> is a reference to the master GeoDB object. Use this functionality only if you&#8217;re an expert (and in desperate need). </p>
<pre>
  %perl leavewhitespace=1
</pre>
<dt>%title</p>
<dd> Names the script with a title. </p>
<pre>
  %title
  My super title
</pre>
<dt>%introduction</p>
<dd> Includes a paragraph in the top of the <font SIZE="-1">GUI</font> screen when the script is run. </p>
<pre>
  %introduction
  This is how you use this screen
</pre>
</dl>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt>-i <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;import-file=STRING</p>
<dd> Import a file. File should be specified as type:file</p>
<dt>-n <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;name=STRING</p>
<dd> Comma separated names to assign to the objects in the file</p>
<dt>-m <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;modify=STRING</p>
<dd> Modify the search set before displaying or exporting</p>
<dt>-e <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;export-file=STRING</p>
<dd> Export a file. File should be specified as type:file</p>
<dt>&#8211;execute-script=FILENAME</p>
<dd>
<dt>-x <font SIZE="-1">FILENAME</font></p>
<dd> Run a script stored in <font SIZE="-1">FILENAME</font></dl>
<h2>Search Options:</h2>
<dl>
<dt>-s <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;search=STRING</p>
<dd> Search terms for geocaches</p>
<dt>&#8211;limit=INTEGER</p>
<dd> Maximum number of records to return for searches</p>
<dt>-N <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;set-name=STRING</p>
<dd> Set/Search Storage Name (&#8216;search:geoqo&#8217;)</dl>
<h2>Display Options:</h2>
<dl>
<dt>-l</p>
<dd>
<dt>&#8211;list-caches</p>
<dd> List geocaches found in search</p>
<dt>-S</p>
<dd>
<dt>&#8211;show-caches</p>
<dd> Show details of geocaches found</p>
<dt>-L</p>
<dd>
<dt>&#8211;show-logs</p>
<dd> Show log messages in details output</p>
<dt>-d <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;display=STRING</p>
<dd> Display output thingies</p>
<dt>&#8211;save</p>
<dd>
<dt>&#8211;save-changes</p>
<dd> Save changes to the set to the <font SIZE="-1">DB</font></dl>
<h2>Database Options:</h2>
<dl>
<dt>-t <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;db-type=STRING</p>
<dd> Database Type (sqlite2, sqlite, mysql, postgres)</p>
<dt>-H <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;db-host=STRING</p>
<dd> Database Host (localhost)</p>
<dt>-u <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;db-user=STRING</p>
<dd> Database User (geoqo)</p>
<dt>-p <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;db-password=STRING</p>
<dd> Database Password</p>
<dt>&#8211;db-name=STRING</p>
<dd> Database Name (geoqo)</p>
<dt>&#8211;db-flush</p>
<dd> Delete the existing <font SIZE="-1">DB</font> first</p>
<dt>&#8211;db-port=INTEGER</p>
<dd> Port number for the database</p>
<dt>&#8211;setup-database</p>
<dd> Initialize the database table structure</dl>
<h2>Configuration Options:</h2>
<dl>
<dt>-c <font SIZE="-1">STRING</font></p>
<dd>
<dt>&#8211;config-file=STRING</p>
<dd> Configuration File to read</p>
<dt>-C</p>
<dd>
<dt>&#8211;no-config</p>
<dd> Do not read any configuration file</p>
<dt>&#8211;debug=INTEGER</p>
<dd> Turn on debugging output</p>
<dt>&#8211;test</p>
<dd> Prints a bunch of test output that Yamar (or someone else) may ask you for if you have problems.</dl>
<h2>Help Options</h2>
<dl>
<dt>-h</p>
<dd> Display a help summary (short flags preferred)</p>
<dt>&#8211;help</p>
<dd> Display a help summary (long flags preferred)</p>
<dt>&#8211;help-full</p>
<dd> Display all help options (both short and long)</p>
<dt>&#8211;version</p>
<dd> Display the script version number.</dl>
<h2>CONFIGURING</h2>
<p> GeoQO supports a configuration file where multiple types of things can be specified.</p>
<h2>Command Line Options and Default</h2>
<p> You can also store &#8220;always use this&#8221; options in a configuration file named ~/.geoqo/config. This file should be the option name on the left (single letter option if available, not longer ones) followed by the value you want after a space. <font SIZE="-1">EG</font> to always use debugging and postgresql and the &#8216;geo&#8217; database user: </p>
<pre>
  t postgresql
  u geo
  debug 5
</pre>
<p> Any option may be added to this file. Options on the command line will override options in this file (as you&#8217;d expect).</p>
<h2><font SIZE="-1">GUI</font> Defaults</h2>
<p> When using the auto-gui created screens, you can specify your own defaults for widgets created by geoqo modules or scripts using the &#8220;default&#8221; keyword. <font SIZE="-1">EG:</font> </p>
<pre>
  default searchby Power Search
</pre>
<p> Will set the default search mechanism to the &#8220;Power Search&#8221; option. Knowing what keyword to use and what value to use generaly requires understanding how geoqo works at this point though (or you can ask Yamar in the #geoqo <font SIZE="-1">IRC</font> channel).</p>
<h2>Per-Screen <font SIZE="-1">GUI</font> Defaults</h2>
<p> You can also set defaults or for particular script screens. To set the default search type in the devices/cachemate script <font SIZE="-1">GUI</font> screen: </p>
<pre>
  screen devices/cachemate searchby Power Search
</pre>
<h2>Debugging</h2>
<p> If you really want to see what geodb is doing internally, run with the &#8211;debug switch. In particuluar, &#8220;&#8211;debug 5&#8221; will print lots of interesting information. Too much. The higher the number the more you get.</p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> The following people (geocachers) helped in useful ways with this program:</p>
<dl>
<dt>BlueNinja</p>
<dd> Self proclaimed &#8220;test monkey&#8221;. He tested lots of early verions and has caught various bugs as well and given me better usage ideas through his &#8220;why can&#8217;t I do this&#8221; set of questions. </p>
<p> He was also the first person to get it working on Windows and has contributed vastly to the windows documentation.</p>
<dt>ClayJar</p>
<dd> Who won the renaming contest on <font SIZE="-1">IRC</font> after SourceForge told me GeoDB was an internal reserved name: </p>
<pre>
  [03:38:13 pm] &lt;ClayJar_SSH&gt;Yamar: How about &quot;Geoqo&quot;.  You'll have
  sole Google of that one, I imagine. You can pronounce it &quot;ge-OH-ko&quot;,
  and &quot;QO&quot; is DB after ROT13.
</pre>
<p> For those that don&#8217;t know, <font SIZE="-1">ROT13</font> is the cheap encryption mechanism that geocaching.com (and other places) use to encrypt their logs. </p>
<p> (<font SIZE="-1">ROT13</font> is used in many, many other ways too, and the first most popular usage of it was to encrypt potentially offensive material (ie, jokes) when posting to <font SIZE="-1">USENET</font> news groups)</p>
<dt>Planet</p>
<dd> Planet nicely volunteered to proof-read a copy of this manual and sent me many wonderful suggestions about improving it.</p>
<dt>jslagle</p>
<dd> The first person to send me a code patch (implementing a better zip file import handler)! Yay! He&#8217;s now a co-developer.</p>
<dt>brdad</p>
<dd> The first person to wade through what it takes to get the <font SIZE="-1">GUI</font> working under windows.</p>
<dt>lairsdragon</p>
<dd> Submitted patches for the build system to make it more <font SIZE="-1">PREFIX</font> friendly.</p>
<dt>Zemmy</p>
<dd> An early Windows test case for the installer components.</dl>
<h2>AUTHOR</h2>
<p> Wes Hardaker &lt;hardaker <font SIZE="-1">ATAT</font> users.sourceforge.net&gt; </p>
<p> <font SIZE="-1">AKA</font> &#8220;Yamar&#8221; on Geocaching.com, <font SIZE="-1">IRC</font>, and other places </p>
<h2>Index</h2>
